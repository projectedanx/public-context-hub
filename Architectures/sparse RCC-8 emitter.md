<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# ok

```json
{
  "Hickam_Orientation": {
    "Occam_Reject": "I have rejected the simple explanation that sparse emission is just dense classification plus a final filter.",
    "Comorbid_Factors": [
      "Sparse topological output needs semantic fidelity and memory compaction at the same time.",
      "Global atomics solve reservation but can introduce contention and correctness edge cases.",
      "H100 rewards coalesced blockwise staging more than irregular fine-grained writes."
    ]
  },
  "Contrastive_Delta": {
    "Amateur_Impulse": "The generic response would be to classify all pairs densely and then call nonzero().",
    "Inductive_Synthesis": "The stronger pattern is that RCC-8 classification and sparse storage should share the same tile-local evidence path, but compaction should remain structured.",
    "Abductive_Leap": "The best architecture is a two-stage sparse emit pipeline: classify-and-count per tile, then prefix-sum and scatter survivors.",
    "Expert_Correction": "Therefore, I am giving a Hopper-fit sparse adjacency design that minimizes divergence, limits atomic pressure, and preserves mereotopological invariants."
  },
  "Martensite_Metrics": {
    "Aesthetic_Tension": "Medium",
    "Intent_Divergence_Risk": "Safe (>0.25)",
    "Twinning_Mechanism": "I stabilize the design with a conservative two-stage compaction path instead of a fragile one-shot atomic writer."
  }
}
```


***

Yes — the next step should be a **sparse RCC-8 emitter** for H100, not a dense `[M, N, 8]` output, because most large topological graphs are dominated by `DC` and modern sparse graph kernels show large gains from reducing memory traffic and storing only meaningful edges.[^1][^2]
For Hopper, the most robust design is a two-stage pipeline: tile-local classify-and-count, then prefix-sum and scatter, because warp divergence hurts throughput and naive branch-heavy control flow forces threads in a warp to serialize.[^3][^4]

## Sparse plan

Triton gives you `tl.atomic_add`, but atomics are better as a narrow fallback than as the primary reservation mechanism, because Triton documents the primitive while a reported issue shows undefined values can appear when broadcasted atomic return values are misused across threads.[^5][^6]
So the practical architecture is: `Kernel A = evaluate RCC-8 and count non-DC survivors per tile`, `scan = exclusive prefix sum over tile counts`, and `Kernel B = scatter survivors into COO or CSR-style buffers`, which mirrors the broader sparse-kernel trend of avoiding excessive atomic accumulation.[^7][^1]

```yaml
sparse_emit_pipeline:
  stage_A_classify_count:
    input: [Q, K, volA, volB]
    output:
      - tile_counts[int32]          # one count per tile
      - tile_scratch_rows[int16]
      - tile_scratch_cols[int16]
      - tile_scratch_state[uint8]
    rule: "Only non-DC relations are buffered"
  stage_scan:
    input: tile_counts
    output: tile_offsets[int32]
    rule: "Exclusive scan gives each tile a deterministic write segment"
  stage_B_scatter:
    input:
      - tile_offsets
      - tile_scratch_rows
      - tile_scratch_cols
      - tile_scratch_state
    output:
      - coo_rows[int32]
      - coo_cols[int32]
      - coo_state[uint8]
```


## H100 fit

H100 supports up to 228 KB shared memory per SM and up to 227 KB per thread block, so a `64x64x128` BF16 tile pair plus FP32 accumulators still fits comfortably if you keep the scratch buffer tile-local and bounded.[^4]
That means you should still stage `Q` and `K` blocks in shared memory, compute all RCC-8 evidence in FP32, and only write sparse survivors to global memory, because coalesced contiguous layouts remain a core GPU advantage on H100-class hardware.[^8][^4]

```yaml
hopper_starting_point:
  BLOCK_M: 64
  BLOCK_N: 64
  BLOCK_D: 128
  num_warps: 8
  num_stages: 3
  tile_strategy: "shared-memory staging, global sparse scatter"
  output_format: "COO first, CSR later if row aggregation becomes dominant"
```


## Kernel A

The first kernel should compute the same tile-local invariants as before, but instead of storing dense scores, it packs only surviving non-DC entries into a per-tile scratch buffer. Using `tl.where` keeps the logic mostly predicated, and Triton’s semantics page notes that `tl.where` participates in normal type-promotion rules, which is another reason to keep predicate math in FP32 and state payloads in compact integer types.[^9]

```python
@triton.jit
def rcc8_count_pack_kernel(
    Q_ptr, K_ptr, VolA_ptr, VolB_ptr,
    tile_counts_ptr,
    scratch_row_ptr, scratch_col_ptr, scratch_state_ptr,
    M, N, D,
    stride_qm, stride_qd, stride_km, stride_kd,
    tiles_n,
    EPS: tl.constexpr,
    BLOCK_M: tl.constexpr,
    BLOCK_N: tl.constexpr,
    BLOCK_D: tl.constexpr,
    MAX_TILE_NNZ: tl.constexpr,
):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)
    tile_id = pid_m * tiles_n + pid_n

    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_d = tl.arange(0, BLOCK_D)

    mask_m = offs_m < M
    mask_n = offs_n < N

    acc_dot = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    acc_q2 = tl.zeros((BLOCK_M,), dtype=tl.float32)
    acc_k2 = tl.zeros((BLOCK_N,), dtype=tl.float32)

    for d0 in range(0, D, BLOCK_D):
        d = d0 + offs_d
        mask_d = d < D
        q = tl.load(Q_ptr + offs_m[:, None] * stride_qm + d[None, :] * stride_qd,
                    mask=mask_m[:, None] & mask_d[None, :], other=0.0)
        k = tl.load(K_ptr + offs_n[:, None] * stride_km + d[None, :] * stride_kd,
                    mask=mask_n[:, None] & mask_d[None, :], other=0.0)
        qf = q.to(tl.float32)
        kf = k.to(tl.float32)
        acc_dot += tl.dot(qf, tl.trans(kf))
        acc_q2 += tl.sum(qf * qf, axis=1)
        acc_k2 += tl.sum(kf * kf, axis=1)

    delta = tl.sqrt(tl.maximum(acc_q2[:, None] + acc_k2[None, :] - 2.0 * acc_dot, 0.0))
    iota = acc_dot

    volA = tl.load(VolA_ptr + offs_m, mask=mask_m, other=0.0).to(tl.float32)[:, None]
    volB = tl.load(VolB_ptr + offs_n, mask=mask_n, other=0.0).to(tl.float32)[None, :]

    boundary_touch = tl.abs(delta) <= EPS
    no_interior = iota <= EPS
    A_in_B = iota >= (volA - EPS)
    B_in_A = iota >= (volB - EPS)
    vol_eq = tl.abs(volA - volB) <= EPS
    A_smaller = volA < (volB - EPS)
    B_smaller = volB < (volA - EPS)

    s_EC    = boundary_touch & no_interior
    s_PO    = (iota > EPS) & (~A_in_B) & (~B_in_A)
    s_EQ    = A_in_B & B_in_A & vol_eq
    s_TPP   = A_in_B & A_smaller & boundary_touch
    s_NTPP  = A_in_B & A_smaller & (~boundary_touch)
    s_TPPi  = B_in_A & B_smaller & boundary_touch
    s_NTPPi = B_in_A & B_smaller & (~boundary_touch)

    # DC is implicit zero; emit only non-DC
    state = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.int32)
    state = tl.where(s_EC,    1, state)
    state = tl.where(s_PO,    2, state)
    state = tl.where(s_EQ,    3, state)
    state = tl.where(s_TPP,   4, state)
    state = tl.where(s_NTPP,  5, state)
    state = tl.where(s_TPPi,  6, state)
    state = tl.where(s_NTPPi, 7, state)

    live = state > 0
    live_i = offs_m[:, None] * tl.ones((1, BLOCK_N), dtype=tl.int32)
    live_j = tl.ones((BLOCK_M, 1), dtype=tl.int32) * offs_n[None, :]

    flat_live = tl.reshape(live, (BLOCK_M * BLOCK_N,))
    flat_i = tl.reshape(live_i, (BLOCK_M * BLOCK_N,))
    flat_j = tl.reshape(live_j, (BLOCK_M * BLOCK_N,))
    flat_s = tl.reshape(state, (BLOCK_M * BLOCK_N,))

    # Conservative per-tile compaction; exact implementation can use prefix over flat_live.
    # Store bounded survivors into scratch, then record tile count.
```


## Scatter stage

The second kernel should write each tile’s survivors into a deterministic global segment using the scanned `tile_offsets`, which removes inter-tile write contention and keeps the output in a clean COO structure.[^7][^5]
This is usually preferable to a one-pass global atomic writer on H100, because sparse workloads benefit when you minimize irregular synchronization and keep memory traffic predictable.[^1][^8]

```python
@triton.jit
def rcc8_scatter_kernel(
    tile_offsets_ptr,
    tile_counts_ptr,
    scratch_row_ptr, scratch_col_ptr, scratch_state_ptr,
    out_row_ptr, out_col_ptr, out_state_ptr,
    MAX_TILE_NNZ: tl.constexpr,
):
    tile_id = tl.program_id(0)
    base = tl.load(tile_offsets_ptr + tile_id)
    nnz = tl.load(tile_counts_ptr + tile_id)

    offs = tl.arange(0, MAX_TILE_NNZ)
    mask = offs < nnz

    rows = tl.load(scratch_row_ptr + tile_id * MAX_TILE_NNZ + offs, mask=mask, other=0)
    cols = tl.load(scratch_col_ptr + tile_id * MAX_TILE_NNZ + offs, mask=mask, other=0)
    state = tl.load(scratch_state_ptr + tile_id * MAX_TILE_NNZ + offs, mask=mask, other=0)

    tl.store(out_row_ptr + base + offs, rows, mask=mask)
    tl.store(out_col_ptr + base + offs, cols, mask=mask)
    tl.store(out_state_ptr + base + offs, state, mask=mask)
```


## Validation

I would validate this version against three failure classes: semantic drift, compaction overflow, and divergence regression. Semantic drift means checking that sparse COO re-expanded to dense matches the dense RCC-8 reference, compaction overflow means any tile with `nnz > MAX_TILE_NNZ` must trip a fallback path, and divergence regression means profiling whether the sparse path actually beats dense storage at your observed non-DC rate.[^2][^3]
As a starting heuristic, sparse emission is usually worth it when non-DC occupancy is low enough that saved HBM traffic dominates the extra scan/scatter work, which is exactly the regime where recent sparse graph kernels report strong speed and memory gains.[^2][^1]

Would you like the next pass as a **complete runnable Triton + PyTorch file set** with scan glue and a benchmark script?
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31]</span>

<div align="center">⁂</div>

[^1]: https://arxiv.org/html/2505.08098v1

[^2]: https://arxiv.org/html/2604.16715v1

[^3]: https://learnbydoingwithsteven1.substack.com/p/stanford-cs336-language-modeling

[^4]: https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html

[^5]: https://triton-lang.org/main/python-api/generated/triton.language.atomic_add.html

[^6]: https://github.com/triton-lang/triton/issues/7402

[^7]: https://arxiv.org/html/2508.18224v2

[^8]: https://arxiv.org/html/2311.02206v5

[^9]: https://triton-lang.org/main/python-api/triton-semantics.html

[^10]: https://arxiv.org/html/2512.02550v1

[^11]: https://arxiv.org/html/2508.18224v1

[^12]: https://arxiv.org/html/2310.04361v4

[^13]: https://arxiv.org/pdf/2503.21176.pdf

[^14]: https://www.biorxiv.org/content/biorxiv/early/2025/07/22/2025.07.17.665342.full.pdf

[^15]: https://arxiv.org/html/2511.11571v1

[^16]: https://arxiv.org/html/2603.02804v2

[^17]: https://arxiv.org/html/2605.06057v1

[^18]: https://arxiv.org/html/2604.24927v1

[^19]: https://arxiv.org/html/2603.14110v1

[^20]: https://arxiv.org/html/2512.02189v2

[^21]: https://towardsdatascience.com/learning-triton-one-kernel-at-a-time-softmax/

[^22]: https://arxiv.org/html/2603.25011v1

[^23]: https://kapilsh.github.io/posts/deep-dive-into-triton-internals-3/

[^24]: https://github.com/XunhaoLai/native-sparse-attention-triton/blob/main/README.md

[^25]: https://massedcompute.com/faq-answers/?question=What+is+sparse+matrix+multiplication+and+how+does+it+relate+to+GPU+performance%3F

[^26]: https://jarvislabs.ai/ai-faqs/what-is-the-flops-performance-of-the-nvidia-h100-gpu

[^27]: https://github.com/triton-lang/triton/issues/4737

[^28]: https://github.com/deepspeedai/DeepSpeed/issues/4857

[^29]: https://www.reddit.com/r/nvidia/comments/z185xp/nvidia_h100_gpu_performance_shatters_machine/

[^30]: https://openreview.net/pdf?id=doa11nN5vG

[^31]: http://hc34.hotchips.org/assets/program/conference/day1/GPU HPC/HC2022.NVIDIA.Choquette.vfinal01.pdf

