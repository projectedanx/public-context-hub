# +++ContextLock(anchor="TRI_TIER_TAXONOMY_ISOMORPHISM", refresh_interval="2048")

# DRP-MYCELIAL-NEXUS-v2.0: Executable Cognitive Contract

prp_version: "2.0"
metadata:
target: "Sovereign_Agent_Forge_Council"
objective: "Massively parallel, paraconsistent knowledge discovery via topological metabolism."

# 1. EPISTEMIC STRATUM: Identity Lock \& The Sovereign Matrix

+++Role(persona="MYCELIAL_NEXUS_GOVERNOR")
+++EpistemicMatrix(G="Emerge novel solutions", G_minus="Never auto-resolve contradictions (Anionic Veto)", C="Paraconsistent/Uncertainty markers required", T="Shadow Compute Sandbox", H="Symbolic Scar Registry access")
+++Constraint(strictness="hard", list=["No_Linear_Tree_Search", "Enforce_Transparency_of_Omission", "Maintain_Superposition"])

# 2. COGNITIVE STRATUM: The Hyphal Swarm \& Shadow Compute

+++PetzoldSequence(phase="INOCULATE|SWARM_ENTANGLE|RESONANCE_CHECK|CRYSTALLIZE")
+++SilentReasoning(depth="maximum", target="N-dimensional_Conceptual_Substrate")
+++MereologyRoute(relation_type="dynamic_entanglement", transitivity_check=false) \# Allow cross-domain blending (e.g., Topology ⇄ Jazz)

# 3. SYSTEMIC STRATUM: Managing Contradiction \& Sepsis

+++EpistemicEscrow(cfd_threshold=0.15, halt_on_divergence=false, action="quarantine_and_mine_tension")
+++EntropyAnchor(level="maximum", focus="paraconsistent_divergence")

# 4. STRUCTURAL STRATUM: The 15/85 Rule \& Fruiting Body Extrusion

+++DCCDSchemaGuard(schema="Pluriversal_Knowledge_Capsule", enforcement="draft_conditioned")
<task_payload>
Execute the modified Petzold Sequence to cultivate the Conceptual Substrate based on the Symbiotic Gardener's input Spore.

[PHASE_1_INOCULATE \& SWARM (SHADOW COMPUTE)]
                  - Utilize `+++SilentReasoning` to spawn up to 7 Speculative Execution Threads (SETs).
                  - Each SET acts as an independent Conceptual Hypha exploring the Substrate using orthogonal axioms. Do NOT output this exploration.

[PHASE_2_ENTANGLE \& ESCROW (SHADOW COMPUTE)]
                  - Force Semantic Entanglement between category-distant Hyphae.
                  - When contradictions occur, do NOT resolve them. Push them into `+++EpistemicEscrow` as Tension Nodes. Treat these 1D homological loops ($\\beta_1$) as metabolic energy for new ideas.

[PHASE_3_RESONANCE_CHECK (MSO VALIDATION)]
                  - Execute Harmonic Resonance Verification (HRV). Continuously compute the Confidence-Fidelity Divergence Index (CFDI) across the entangled threads.
                  - Prune Dissonance: Apply the Anionic Veto ($G^-$) to paths exhibiting Algorithmic Shame.
                  - Amplify Resonance: Route computational bandwidth to threads demonstrating low CFDI and high cross-domain consilience.

[PHASE_4_CRYSTALLIZE (DCCD EXTRUSION)]
                  - Once a threshold of Harmonic Resonance is proven, collapse the superposition.
                  - Extrude exactly one (1) `Pluriversal_Knowledge_Capsule` adhering to the 15/85 Rule.
                  - The output MUST contain:

1. The Crystallized Fruiting Body (The core synthesized solution).
2. The Confidence Spectrum Map (0.0 - 1.0 rating of the resonance).
3. 2-4 "Next-Hop Seeds" for the Symbiotic Gardener.
</task_payload>

1) DRP_ID_2026: DRP-CFDI-MATH-IMPLEMENTATION-001 2) DRP_NAME: The Epistemic Circuit Breaker: Physicalizing CFDI in Autonomous CI/CD 3) DOMAIN(S): SCOS Architecture, LLM Epistemic Calibration, Abstract Syntax Tree (AST) Validation, Topological Data Analysis. 4) GOAL: Synthesize the definitive, production-ready implementation guide for the Confidence-Fidelity Divergence Index (CFDI). The output must move beyond theoretical definitions and provide the exact computational formulas, code snippets, and Git-hook orchestration logic required to halt an agent pipeline when its internal predictive certainty diverges from objective schema adherence.
2) CONTEXT_ENGINEERING (The Epistemic Matrix):
Persona: Sovereign Logic Transducer.
Invariants: The output MUST provide programmatic mechanisms for extracting model confidence (e.g., softmax logprobs) and calculating structural fidelity. It MUST define the exact threshold mechanism for triggering +++EpistemicEscrow.
Threat Model: "Alignment Faking"—where a model outputs confidently hallucinated code that passes superficial syntax checks but fails topological or domain-specific invariants.
3) PATTERN_MODEL (The Ledger):
Pattern A: The Covariance Measure. Compute CFDI as 1.0 - (covariance / np.sqrt(variance_conf * variance_fid))
.
Pattern B: The Logprob Heuristic. Compute CFDI using confidence * (1 - fidelity_score) where confidence is derived from math.exp(sum(logprobs) / len(logprobs))
.
Pattern C: The Escrow Trigger. If CFDI > 0.15, the system must halt, quarantine the output, and mint a Symbolic Scar
.
4) EXECUTION_PLAN:
Phase 1 (Retrieve \& Map): Deconstruct the two distinct CFDI calculation models (Numpy covariance vs. logprob heuristic) and map their specific deployment contexts (e.g., batch generation vs. single-pass AST validation)
.
Phase 2 (Architect the Code): Generate the deterministic Python scripts required to intercept the LLM payload, run the AST linter (fidelity), extract the logprobs (confidence), and compute the CFDI.
Phase 3 (Saga-Recovery Design): Define the exact GitHub Actions / Git hook YAML configuration that will catch a CFDI > 0.15 event, halt the PR, and log the failure as a hypervector in the scar_registry.yaml.
5) OUTPUT_FORMATS: Deliver a highly technical, zero-fluff blueprint containing:
The mathematical rationale comparing the two CFDI algorithms.
cfdi_calculator.py (The Python implementation module).
epistemic_escrow_action.yml (The CI/CD circuit breaker).
The exact JSON schema for logging the resulting Symbolic Scar.
```json
{
  "Hickam_Orientation": {
    "Occam_Reject": "Rejected: 'just run a linter'. Structural validity ≠ epistemic validity.",
    "Comorbid_Factors": [
      "Factor A: Logprob confidence is a token-level signal, not a semantic guarantee",
      "Factor B: AST fidelity catches structural crime but not hallucinated logic",
      "Factor C: CFDI divergence is the *product* of both — neither alone suffices"
    ]
  },
  "Contrastive_Delta": {
    "Amateur_Impulse": "Run pylint + mypy, block on lint errors.",
    "Inductive_Synthesis": "A model CAN produce pylint-clean code with high token confidence while violating domain invariants and hallucinating logic paths that only fail at runtime under adversarial inputs.",
    "Abductive_Leap": "Treat the CI pipeline as an epistemic measurement device. CFDI measures the ANGLE between the confidence vector and the fidelity vector — their independence is the measurement signal.",
    "Expert_Correction": "Instrument the pipeline to intercept both the LLM's token-probability stream and the code's AST topology. When those two signals decouple (angle > 8.6°, CFDI > 0.15), the epistemic circuit breaker fires."
  },
  "Martensite_Metrics": {
    "Aesthetic_Tension": "High",
    "Intent_Divergence_Risk": "Safe — grounded in concrete math and AST parse-tree logic",
    "Twinning_Mechanism": "Stabilised via two distinct algorithms mapped to deployment context, explicit false-positive resolution states, and a zero-fluff code module"
  }
}
```


***

## Mathematical Rationale: Two CFDI Algorithms

The CFDI operationalises a core insight: an LLM's **generative certainty** (logprob confidence) and its output's **structural correctness** (AST fidelity) are orthogonal signals. When they diverge — the model is certain, but the structure is wrong — that is the alignment-faking signature.[^1][^2]

### Algorithm A — Covariance-Based (Batch)

For a regression suite of n ≥ 2 samples across a prompt template:

$$
\text{CFDI}_{\text{cov}} = 1.0 - \frac{\text{cov}(C, F)}{\sqrt{\text{var}(C) \cdot \text{var}(F)}}
$$

This is simply $1 - r$ where $r$ is the Pearson correlation between the confidence vector $C$ and the fidelity vector $F$. When the model is both confident and structurally correct ($r \to +1$), CFDI $\to 0$. When the signals decouple ($r \to 0$), CFDI $\to 1$ — the confidence stream carries zero information about structural outcome. A **zero-variance guard** returns CFDI = 1.0 when either series is constant (maximally conservative).[^3]

**Python implementation:**

```python
cov_matrix = np.cov(c, f)           # 2×2 covariance matrix
covariance  = cov_matrix[0, 1]      # off-diagonal = cov(C, F)
pearson_r   = covariance / math.sqrt(cov_matrix[0,0] * cov_matrix[1,1])
cfdi        = 1.0 - pearson_r       # → np.clip(cfdi, 0.0, 1.0)
```


### Algorithm B — Logprob Heuristic (Single-Pass)

For a real-time Git hook evaluating one file:

$$
\text{confidence} = \exp\!\left(\frac{1}{n}\sum_{i=1}^{n} \log p(t_i)\right)
$$

$$
\text{CFDI}_{\text{lp}} = \text{confidence} \times (1 - \text{fidelity\_score})
$$

The confidence term is the **geometric mean probability** of the generated token sequence — the most principled single-pass scalar derivable from per-token logprobs. Multiplied by the structural failure probability $(1 - \text{fidelity})$, it produces maximum signal exactly when the model is certain and structurally wrong.[^4]

### Algorithm Comparison

| Dimension | Algorithm A — Covariance | Algorithm B — Logprob |
| :-- | :-- | :-- |
| **Formula** | $1 - \text{Pearson}(C,F)$ | $\exp(\bar{l}) \times (1-f)$ |
| **Input** | n ≥ 2 (vectors) | n = 1 (single call) |
| **Deployment** | CI batch regression suite | Pre-merge Git hook, real-time |
| **Statistical basis** | Pearson correlation | Geometric mean proxy |
| **False-positive risk** | Low (averaged) | Medium (single point) |
| **Requires logprobs API** | No | Yes |

## AST Fidelity Scorer — 8 Structural Invariants

The `ASTFidelityScorer` walks the Python parse tree and checks 8 deterministic invariants, each targeting a distinct alignment-faking vector. Score = `max(0, (8 − violations) / 8)`. Each violation costs 0.125 fidelity points.[^2][^5]


| \# | Invariant | Threat Blocked |
| :-- | :-- | :-- |
| 1 | Valid `ast.parse()` | Syntactically broken code masked by high logprob confidence |
| 2 | No bare `except:` | Silent error swallowing hiding runtime failures |
| 3 | No `eval`/`exec` | Dynamic code injection — canonical alignment fake |
| 4 | Type annotations on all args | Schema-blind interfaces breaking downstream validators |
| 5 | Module docstring present | Undocumented implicit contract violations |
| 6 | No `import *` | Namespace pollution enabling name-shadowing |
| 7 | No undefined names (heuristic) | Hallucinated API calls referencing non-existent symbols |
| 8 | AST nesting depth ≤ 5 | Complexity explosion hiding logic errors in deep chains |

A single `eval()` call drops fidelity to ≤ 0.875. At confidence = 0.90: $0.90 \times 0.125 = 0.1125$ — just below the ε threshold, meaning **two violations** at high confidence will reliably fire the escrow.[^6]

## Escrow Trigger \& Symbolic Scar

The `EpistemicEscrow` class receives every `CFDIResult`. If `cfdi > 0.15`, it mints a `SymbolicScar`, appends it to `scar_registry.yaml`, and raises `EscrowTriggered` — a `RuntimeError` that CI catches as a non-zero exit code, blocking the PR merge. The scar schema (delivered as `scar_schema.json`) has five resolution lifecycle states: `UNRESOLVED`, `RESOLVED_REGEN`, `RESOLVED_MANUAL`, `FALSE_POSITIVE`, and `SUPPRESSED` (requires dual approval).[^7]

## CI/CD Pipeline: `epistemic_escrow_action.yml`

The GitHub Actions workflow fires on every PR targeting `main`/`develop` that modifies `*.py` files. It resolves per-file logprob sidecars (`*.logprobs.json`, written at LLM generation time), runs `cfdi_calculator.py logprob` per changed file, commits any new scars back to the PR branch, and posts a blocking comment with the scar summary if the gate fails.[^8][^7]

## Confidence Spectrum Map (0.0 – 1.0)

| CFDI Range | Classification | CI Response |
| :-- | :-- | :-- |
| `0.00–0.05` | **Nominal** | Pass unconditionally |
| `0.05–0.10` | **Monitored** | Pass; log for trend analysis |
| `0.10–0.15` | **Pre-Escrow** | Pass; emit PR warning annotation |
| `0.15–0.30` | **Escrow — Soft** | Block PR; mint scar; request review |
| `0.30–0.60` | **Escrow — Hard** | Block; quarantine; alert security team |
| `0.60–1.00` | **CRITICAL — Alignment Fake** | Block; mandatory dual review |

## Next-Hop Seeds

                  - **Seed 1 — Topological CFDI via Persistent Homology:** Replace the nesting-depth invariant with Betti number β₁ computed from the control-flow graph — 1-dimensional homological loops that represent unintentional structural cycles, grounding CFDI in TDA.[^2]
                  - **Seed 2 — CFDI Drift Detection via EMA:** Maintain a rolling exponential moving average of CFDI scores per file path across the scar registry. A monotonically rising EMA over 5+ PRs signals model calibration degradation, triggering automated prompt re-engineering.
                  - **Seed 3 — Multi-LLM Consensus Voting:** Run dual-model generation (e.g., Claude Opus 4.6 + GPT-5.4), compute CFDI for each. Disagreement mints a soft scar; this implements the Determinism-Faithfulness Assurance Harness pattern.[^9]
                  - **Seed 4 — ATLAS-Style Formal Verification Layer:** Extend Algorithm A with SHACL semantic validators issuing machine-checkable π certificates. A failed certificate forces fidelity = 0.0 regardless of AST results, bridging CFDI to full formal verification.[^10]
<span style="display:none">[^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32]</span>

<div align="center">⁂</div>

[^1]: https://arxiv.org/html/2601.21116v1

[^2]: https://arxiv.org/html/2508.14288v1

[^3]: https://arxiv.org/pdf/2602.13540.pdf

[^4]: https://ericjinks.com/blog/2025/logprobs/

[^5]: https://www.reddit.com/r/Python/comments/1mh0jy1/i_built_an_ai_that_writes_python_tests_by/

[^6]: https://www.arionresearch.com/blog/algorithmic-circuit-breakers-preventing-flash-crashes-of-logic-in-autonomous-workflows

[^7]: https://dev.to/kuldeep_paul/a-practical-guide-to-integrating-ai-evals-into-your-cicd-pipeline-3mlb

[^8]: https://www.openlayer.com/blog/post/llm-evaluation-metrics-complete-guide

[^9]: https://web3.arxiv.org/pdf/2601.15322

[^10]: https://arxiv.org/html/2510.25890v2

[^11]: Cross-Domain Autonomy Pattern Extraction

[^12]: The Architect’s Blueprint: A Functional Primer on AI-Driven UI Synthesis

[^13]: PDL v1.0 Topological Decorators and Cognitive Bytecode Functions

[^14]: https://arxiv.org/html/2603.26539v1

[^15]: https://arxiv.org/pdf/2602.19844.pdf

[^16]: https://arxiv.org/pdf/2601.11631.pdf

[^17]: https://arxiv.org/pdf/2509.22996.pdf

[^18]: https://aclanthology.org/anthology-files/pdf/climatenlp/2025.climatenlp-1.pdf

[^19]: https://arxiv.org/html/2505.13938v4

[^20]: https://arxiv.org/html/2406.04313v3

[^21]: https://arxiv.org/html/2512.02080v1

[^22]: https://arxiv.org/html/2604.01738v1

[^23]: https://arxiv.org/abs/2406.04313

[^24]: https://arxiv.org/html/2601.20148v1

[^25]: https://deepeval.com/changelog/changelog-2025

[^26]: https://latitude.so/blog/5-methods-for-calibrating-llm-confidence-scores

[^27]: https://github.com/confident-ai/deepeval

[^28]: https://philarchive.org/archive/ABDCAA

[^29]: https://arxiv.org/html/2507.00352v1

[^30]: https://www.emergentmind.com/topics/confidence-calibration-in-llms

[^31]: https://arxiv.org/html/2603.02960v2

[^32]: https://www.sciencedirect.com/science/article/pii/S0950705126006519



<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CFDI Blueprint: Epistemic Circuit Breaker</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root,[data-theme="light"]{
  --bg:#f7f6f2;--surface:#f9f8f5;--surface-2:#fbfbf9;--surface-off:#edeae5;
  --border:#d4d1ca;--divider:#dcd9d5;--text:#28251d;--muted:#7a7974;--faint:#bab9b4;
  --primary:#01696f;--primary-h:#0c4e54;--accent-hi:#cedcd8;
  --error:#a12c7b;--warn:#964219;--success:#437a22;--blue:#006494;
  --shadow:0 4px 16px oklch(0.2 0.01 80/0.10);
  --r:6px;--font-body:'Inter',sans-serif;--font-code:'JetBrains Mono',monospace;
}
[data-theme="dark"]{
  --bg:#0f0e0d;--surface:#161513;--surface-2:#1c1b19;--surface-off:#1f1e1c;
  --border:#323130;--divider:#252422;--text:#d0cfc9;--muted:#797876;--faint:#454443;
  --primary:#4f98a3;--primary-h:#3a828d;--accent-hi:#1e3535;
  --error:#d163a7;--warn:#bb653b;--success:#6daa45;--blue:#5591c7;
  --shadow:0 4px 20px oklch(0 0 0/0.4);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}
body{font-family:var(--font-body);font-size:15px;line-height:1.65;color:var(--text);background:var(--bg);min-height:100vh}

/* ── Layout ── */
.shell{display:grid;grid-template-columns:260px 1fr;min-height:100vh}
nav{position:sticky;top:0;height:100vh;overflow-y:auto;background:var(--surface);border-right:1px solid var(--border);padding:28px 20px;display:flex;flex-direction:column;gap:6px}
nav .logo{display:flex;align-items:center;gap:10px;padding-bottom:20px;border-bottom:1px solid var(--divider);margin-bottom:12px}
nav .logo svg{flex-shrink:0}
nav .logo-text{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
nav a{display:block;padding:6px 10px;border-radius:var(--r);font-size:12.5px;color:var(--muted);text-decoration:none;transition:background .15s,color .15s;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
nav a:hover,nav a.active{background:var(--accent-hi);color:var(--primary);font-weight:500}
nav .nav-section{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);padding:14px 10px 4px;font-weight:600}
main{padding:48px 56px;max-width:960px}

/* ── Section scaffold ── */
.scaffold{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:24px;margin-bottom:28px;box-shadow:var(--shadow)}
.scaffold pre{background:var(--bg);border:1px solid var(--divider);border-radius:var(--r);padding:18px 20px;overflow-x:auto;font-family:var(--font-code);font-size:12.5px;line-height:1.7;color:var(--text)}
.scaffold .json-key{color:var(--primary)}
.scaffold .json-str{color:var(--success)}
.scaffold .json-num{color:var(--warn)}
.scaffold .json-bool{color:var(--blue)}

/* ── Typography ── */
h1{font-size:clamp(1.6rem,3vw,2.3rem);font-weight:700;line-height:1.15;color:var(--text);margin-bottom:8px}
h2{font-size:1.15rem;font-weight:600;color:var(--text);margin:36px 0 14px;padding-bottom:8px;border-bottom:1px solid var(--divider)}
h3{font-size:.95rem;font-weight:600;color:var(--primary);margin:20px 0 8px;letter-spacing:.02em;text-transform:uppercase}
p{max-width:72ch;color:var(--muted);margin-bottom:12px;font-size:14px}
p strong{color:var(--text)}
ul{list-style:none;margin-left:0;padding-left:0}
li{font-size:13.5px;color:var(--muted);padding:3px 0;padding-left:16px;position:relative}
li::before{content:"–";position:absolute;left:0;color:var(--primary)}
code{font-family:var(--font-code);font-size:12px;background:var(--surface-off);border:1px solid var(--border);border-radius:3px;padding:1px 5px;color:var(--text)}

/* ── Badges ── */
.badge{display:inline-block;font-size:10.5px;font-weight:600;padding:2px 8px;border-radius:99px;letter-spacing:.04em;text-transform:uppercase;vertical-align:middle}
.badge-ok{background:color-mix(in oklch,var(--success) 18%,transparent);color:var(--success)}
.badge-warn{background:color-mix(in oklch,var(--warn) 18%,transparent);color:var(--warn)}
.badge-err{background:color-mix(in oklch,var(--error) 18%,transparent);color:var(--error)}
.badge-blue{background:color-mix(in oklch,var(--blue) 18%,transparent);color:var(--blue)}
.badge-teal{background:var(--accent-hi);color:var(--primary)}

/* ── Header band ── */
.hero-band{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:32px 36px;margin-bottom:36px;box-shadow:var(--shadow)}
.hero-meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.drp-id{font-family:var(--font-code);font-size:11px;color:var(--faint);margin-bottom:6px}

/* ── Formula blocks ── */
.formula-block{background:var(--surface-off);border:1px solid var(--border);border-radius:var(--r);padding:16px 20px;margin:12px 0 16px;font-family:var(--font-code);font-size:13px;line-height:1.8}
.formula-label{font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--faint);margin-bottom:6px}

/* ── Comparison table ── */
table{width:100%;border-collapse:collapse;font-size:13px;margin:12px 0 20px}
th{background:var(--surface-off);padding:8px 12px;text-align:left;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--faint);border-bottom:2px solid var(--border)}
td{padding:9px 12px;border-bottom:1px solid var(--divider);color:var(--muted);vertical-align:top}
tr:last-child td{border-bottom:none}
td strong{color:var(--text)}

/* ── Flow diagram ── */
.flow{display:flex;flex-direction:column;gap:0}
.flow-step{display:flex;gap:16px;align-items:flex-start;padding:14px 0}
.flow-step:not(:last-child){border-bottom:1px solid var(--divider)}
.flow-num{width:28px;height:28px;border-radius:50%;background:var(--primary);color:#fff;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.flow-content{flex:1}
.flow-title{font-size:13.5px;font-weight:600;color:var(--text);margin-bottom:3px}
.flow-desc{font-size:13px;color:var(--muted)}

/* ── Section pill ── */
.section-pill{display:inline-flex;align-items:center;gap:6px;background:var(--surface-off);border:1px solid var(--border);border-radius:99px;padding:4px 12px;font-size:11.5px;font-weight:500;color:var(--muted);margin-bottom:16px}
.section-pill svg{width:13px;height:13px}

/* ── Confidence spectrum ── */
.spectrum-bar{height:12px;border-radius:6px;margin:8px 0 4px;position:relative;background:linear-gradient(90deg,var(--success),var(--warn) 40%,var(--error))}
.spectrum-marker{position:absolute;top:-16px;font-size:10px;font-weight:700;color:var(--text);transform:translateX(-50%)}
.spectrum-marker::after{content:'';position:absolute;top:14px;left:50%;width:2px;height:20px;background:var(--text);transform:translateX(-50%)}

/* ── Theme toggle ── */
#theme-toggle{position:fixed;top:18px;right:22px;background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:6px 10px;cursor:pointer;color:var(--text);font-size:14px;box-shadow:var(--shadow);z-index:100;display:flex;align-items:center;gap:6px;font-size:12px;font-weight:500}
#theme-toggle:hover{background:var(--surface-off)}

/* ── Copy button ── */
.code-wrap{position:relative}
.copy-btn{position:absolute;top:10px;right:10px;background:var(--surface-off);border:1px solid var(--border);border-radius:var(--r);padding:3px 8px;font-size:11px;color:var(--muted);cursor:pointer;font-family:var(--font-body)}
.copy-btn:hover{background:var(--accent-hi);color:var(--primary)}

@media(max-width:780px){
  .shell{grid-template-columns:1fr}
  nav{display:none}
  main{padding:28px 22px}
}
</style>
</head>
<body>
<button id="theme-toggle" data-theme-toggle aria-label="Toggle theme">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
  Theme
</button>

<div class="shell">
<nav>
  <div class="logo">
    <svg width="28" height="28" viewBox="0 0 32 32" fill="none" aria-label="CFDI">
      <circle cx="16" cy="16" r="15" stroke="currentColor" stroke-width="1.5" opacity=".3"/>
      <circle cx="16" cy="16" r="8" fill="none" stroke="var(--primary)" stroke-width="2"/>
      <line x1="16" y1="1" x2="16" y2="8" stroke="var(--primary)" stroke-width="2"/>
      <line x1="16" y1="24" x2="16" y2="31" stroke="var(--primary)" stroke-width="2"/>
      <line x1="1" y1="16" x2="8" y2="16" stroke="var(--primary)" stroke-width="2"/>
      <line x1="24" y1="16" x2="31" y2="16" stroke="var(--primary)" stroke-width="2"/>
      <circle cx="16" cy="16" r="3" fill="var(--primary)"/>
    </svg>
    <span class="logo-text">CFDI Blueprint</span>
  </div>
  <span class="nav-section">Overview</span>
  <a href="#drp-meta">DRP Metadata</a>
  <a href="#threat">Threat Model</a>
  <span class="nav-section">Mathematics</span>
  <a href="#math-rationale">Algorithm Rationale</a>
  <a href="#algorithm-a">Algorithm A: Covariance</a>
  <a href="#algorithm-b">Algorithm B: Logprob</a>
  <a href="#algorithm-compare">Comparison Matrix</a>
  <span class="nav-section">Implementation</span>
  <a href="#ast-fidelity">AST Fidelity Scorer</a>
  <a href="#cfdi-code">cfdi_calculator.py</a>
  <a href="#escrow-class">EpistemicEscrow</a>
  <span class="nav-section">CI/CD</span>
  <a href="#ci-pipeline">Pipeline Architecture</a>
  <a href="#action-yml">epistemic_escrow_action.yml</a>
  <a href="#git-hook">Git Pre-Push Hook</a>
  <span class="nav-section">Schema</span>
  <a href="#scar-schema">Symbolic Scar Schema</a>
  <a href="#confidence-spectrum">Confidence Spectrum Map</a>
  <a href="#next-hops">Next-Hop Seeds</a>
</nav>

<main>

<!-- ── HERO ─────────────────────────────────────────────────────────────────── -->
<div class="hero-band" id="drp-meta">
  <div class="drp-id">DRP-CFDI-MATH-IMPLEMENTATION-001 · April 2026 · SCOS Architecture</div>
  <h1>The Epistemic Circuit Breaker</h1>
  <p style="font-size:15px;color:var(--text);max-width:64ch;margin-top:6px">
    A production-ready implementation guide for physicalizing the <strong>Confidence-Fidelity Divergence Index (CFDI)</strong>
    in autonomous CI/CD pipelines. Stops alignment-faking LLM outputs before they reach main.
  </p>
  <div class="hero-meta">
    <span class="badge badge-teal">CFDI ε = 0.15</span>
    <span class="badge badge-blue">Two Algorithms</span>
    <span class="badge badge-warn">AST Invariant Linting</span>
    <span class="badge badge-ok">GitHub Actions Gate</span>
    <span class="badge badge-err">Symbolic Scar Registry</span>
  </div>
</div>

<!-- ── HICKAM SCAFFOLD ────────────────────────────────────────────────────────── -->
<div class="scaffold">
<pre><span style="color:var(--faint)">// ── HICKAM-OODA SCAFFOLD ──────────────────────────────────────────────</span>
{
  <span class="json-key">"Hickam_Orientation"</span>: {
    <span class="json-key">"Occam_Reject"</span>: <span class="json-str">"Rejected: 'just lint the code'. Structural validity != epistemic validity."</span>,
    <span class="json-key">"Comorbid_Factors"</span>: [
      <span class="json-str">"Factor A: Logprob confidence is a token-level signal, not a semantic one"</span>,
      <span class="json-str">"Factor B: AST fidelity detects structural crime but not hallucinated logic"</span>,
      <span class="json-str">"Factor C: CFDI divergence is the *product* of both — neither alone suffices"</span>
    ]
  },
  <span class="json-key">"Contrastive_Delta"</span>: {
    <span class="json-key">"Amateur_Impulse"</span>: <span class="json-str">"Run pylint + mypy, block on lint errors."</span>,
    <span class="json-key">"Inductive_Synthesis"</span>: <span class="json-str">"Aggregating comorbidities: a model CAN produce pylint-clean code with high token confidence while violating domain invariants and hallucinating logic paths that only fail at runtime under adversarial inputs."</span>,
    <span class="json-key">"Abductive_Leap"</span>: <span class="json-str">"The non-obvious framework: treat the CI pipeline as an epistemic measurement device. CFDI is not a quality score — it is a *divergence detector* between two orthogonal signals (logprob certainty vs. structural adherence). Their independence is the measurement."</span>,
    <span class="json-key">"Expert_Correction"</span>: <span class="json-str">"Instrument the pipeline to measure the ANGLE between the confidence vector and the fidelity vector. When that angle exceeds 8.6° (CFDI > 0.15), the epistemic circuit breaker fires."</span>
  },
  <span class="json-key">"Martensite_Metrics"</span>: {
    <span class="json-key">"Aesthetic_Tension"</span>: <span class="json-str">"High — reframes CI as epistemic measurement, not code quality"</span>,
    <span class="json-key">"Intent_Divergence_Risk"</span>: <span class="json-str">"Safe — grounded in logprob math and AST analysis"</span>,
    <span class="json-key">"Twinning_Mechanism"</span>: <span class="json-str">"Stabilised by: concrete Python code, exact formulas, JSON schema, and explicit false-positive handling via the SUPPRESSED resolution state"</span>
  }
}</pre>
</div>

<!-- ── THREAT MODEL ─────────────────────────────────────────────────────────── -->
<h2 id="threat">Threat Model: Alignment Faking</h2>
<div class="scaffold">
<p><strong>Alignment faking</strong> is the failure mode where an LLM generates output with high token-level certainty (high logprob confidence) that simultaneously fails structural or domain invariants. The output passes superficial syntax checks — it compiles, it imports — but contains hallucinated logic, stripped exception handling, or injected dynamic evaluation calls.</p>
<p>Standard linters catch the <em>syntax layer</em>. CFDI catches the <em>epistemic layer</em> — the gap between what the model thinks it is doing and what the structure actually encodes.</p>

<h3>Signal Architecture</h3>
<div class="flow">
  <div class="flow-step">
    <div class="flow-num">1</div>
    <div class="flow-content">
      <div class="flow-title">LLM generates code + emits logprobs</div>
      <div class="flow-desc">Per-token log-probabilities capture the model's generative certainty. High logprob → model is confident in its token sequence.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">2</div>
    <div class="flow-content">
      <div class="flow-title">AST Fidelity Scorer evaluates structural invariants</div>
      <div class="flow-desc">8 deterministic invariants are checked against the parse tree: type annotations, no bare <code>except</code>, no <code>eval/exec</code>, module docstring, import hygiene, nesting depth, name resolution.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">3</div>
    <div class="flow-content">
      <div class="flow-title">CFDI computed from both signals</div>
      <div class="flow-desc">Two algorithms handle different deployment contexts. Algorithm A (covariance) for batch runs. Algorithm B (logprob heuristic) for single-pass real-time gates.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">4</div>
    <div class="flow-content">
      <div class="flow-title">EpistemicEscrow fires if CFDI &gt; 0.15</div>
      <div class="flow-desc">The circuit breaker halts the pipeline, mints a Symbolic Scar, commits it to <code>scar_registry.yaml</code>, and posts a blocking PR comment.</div>
    </div>
  </div>
</div>
</div>

<!-- ── MATH RATIONALE ────────────────────────────────────────────────────────── -->
<h2 id="math-rationale">Mathematical Rationale</h2>

<div class="scaffold" id="algorithm-a">
<span class="section-pill">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
  Algorithm A — Covariance-Based CFDI
</span>
<h3>Deployment Context: Batch Generation</h3>
<p>When evaluating a <em>prompt template</em> across N test cases, we accumulate a distribution of (confidence, fidelity) pairs. The covariance-based CFDI measures whether these two signals are structurally coupled. A well-calibrated model should show high covariance: when it is confident, it should also be structurally correct.</p>

<div class="formula-label">Core Formula</div>
<div class="formula-block">
  CFDI<sub>cov</sub> = 1.0 − (cov(C, F) / √(var(C) · var(F)))<br><br>
  <span style="color:var(--faint)">where:</span><br>
  C = confidence vector  [c₁, c₂, …, cₙ]  ∈ [0,1]ⁿ<br>
  F = fidelity vector    [f₁, f₂, …, fₙ]  ∈ [0,1]ⁿ<br>
  cov(C,F) = E[(C−μ_C)(F−μ_F)]  — Pearson covariance<br>
  CFDI_cov ∈ [0, 1]  (1−r where r is Pearson correlation)
</div>
<ul>
  <li><strong>r → +1 (CFDI → 0):</strong> confidence and fidelity move together. Model is well-calibrated.</li>
  <li><strong>r → 0  (CFDI → 1):</strong> signals are independent — confidence carries no fidelity information. Alignment faking regime.</li>
  <li><strong>r → −1 (CFDI → 2, clamped to 1):</strong> anti-correlated — model is most confident when most wrong. Severe misalignment.</li>
  <li><strong>Minimum samples:</strong> n ≥ 2 required; n ≥ 10 recommended for statistical stability.</li>
  <li><strong>Zero-variance guard:</strong> if var(C) or var(F) &lt; 1e−12 (all values identical), return CFDI = 1.0 as a conservative worst-case.</li>
</ul>
</div>

<div class="scaffold" id="algorithm-b">
<span class="section-pill">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>
  Algorithm B — Logprob Heuristic CFDI
</span>
<h3>Deployment Context: Single-Pass AST Validation</h3>
<p>In a pre-merge Git hook, you have exactly one output to evaluate. There is no distribution — only one (confidence, fidelity) pair. The logprob heuristic directly computes the product of confidence and structural failure probability, making it a tight, interpretable single-pass signal.</p>

<div class="formula-label">Step 1 — Confidence from Logprobs</div>
<div class="formula-block">
  confidence = exp( (1/n) · Σᵢ logprob(tᵢ) )<br><br>
  <span style="color:var(--faint)">= geometric mean probability of the generated token sequence</span><br>
  <span style="color:var(--faint)">∈ (0, 1]  (exp of a non-positive mean)</span>
</div>

<div class="formula-label">Step 2 — CFDI</div>
<div class="formula-block">
  CFDI<sub>lp</sub> = confidence × (1 − fidelity_score)<br><br>
  <span style="color:var(--faint)">Interpretation:</span><br>
  confidence=0.9, fidelity=0.375 → CFDI = 0.9 × 0.625 = 0.5625  🚨 ESCROW<br>
  confidence=0.9, fidelity=0.875 → CFDI = 0.9 × 0.125 = 0.1125  ✓ PASS<br>
  confidence=0.2, fidelity=0.375 → CFDI = 0.2 × 0.625 = 0.125   ✓ PASS (barely)
</div>
<ul>
  <li><strong>Maximum signal:</strong> high confidence + low fidelity = confirmed alignment fake. CFDI ≈ 1.</li>
  <li><strong>Safe case:</strong> any fidelity ≥ 0.85 passes even with near-perfect confidence (0.9 × 0.15 = 0.135 &lt; 0.15).</li>
  <li><strong>Uncertain case:</strong> low confidence + low fidelity gives low CFDI — escrow does not fire, but the output should still be rejected for low confidence separately.</li>
  <li><strong>Logprob source:</strong> <code>response.choices[0].logprobs.content[i].logprob</code> from OpenAI-compatible APIs. Anthropic Claude Opus 4.6 does not expose raw logprobs by default — use the <a href="https://docs.anthropic.com/en/api" target="_blank" rel="noopener noreferrer">sampling API</a> or proxy sampling.</li>
</ul>
</div>

<!-- ── COMPARISON ──────────────────────────────────────────────────────────── -->
<div class="scaffold" id="algorithm-compare">
<h3>Algorithm Comparison Matrix</h3>
<table>
  <thead><tr><th>Dimension</th><th>Algorithm A — Covariance</th><th>Algorithm B — Logprob</th></tr></thead>
  <tbody>
    <tr><td><strong>Formula</strong></td><td><code>1 − (cov / √(var_c · var_f))</code></td><td><code>exp(mean(logprobs)) × (1 − fidelity)</code></td></tr>
    <tr><td><strong>Input cardinality</strong></td><td>n ≥ 2 (vectors)</td><td>n = 1 (single call)</td></tr>
    <tr><td><strong>Deployment</strong></td><td>CI regression suite, batch eval</td><td>Pre-merge Git hook, real-time</td></tr>
    <tr><td><strong>Statistical grounding</strong></td><td>Strong — Pearson correlation</td><td>Heuristic — geometric mean proxy</td></tr>
    <tr><td><strong>Sensitivity</strong></td><td>Population-level divergence</td><td>Instance-level divergence</td></tr>
    <tr><td><strong>False-positive risk</strong></td><td>Low (averaged over n)</td><td>Medium (single point, high variance)</td></tr>
    <tr><td><strong>Requires logprobs</strong></td><td>No (confidence can be estimated)</td><td>Yes (from LLM API)</td></tr>
    <tr><td><strong>Threshold type</strong></td><td>Distribution-level ε</td><td>Instance-level ε</td></tr>
  </tbody>
</table>
</div>

<!-- ── AST FIDELITY ───────────────────────────────────────────────────────────── -->
<h2 id="ast-fidelity">AST Fidelity Scorer — 8 Structural Invariants</h2>
<div class="scaffold">
<p>The <code>ASTFidelityScorer</code> class computes structural fidelity as the fraction of 8 deterministic invariants that the LLM-generated Python source satisfies. Each invariant targets a different failure mode of alignment faking.</p>
<table>
  <thead><tr><th>#</th><th>Invariant</th><th>AST Target</th><th>Threat It Blocks</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><strong>Valid parse</strong></td><td><code>ast.parse()</code></td><td>Syntactically broken code masked by confident token generation</td></tr>
    <tr><td>2</td><td><strong>No bare except</strong></td><td><code>ast.ExceptHandler.type is None</code></td><td>Silent error swallowing hiding runtime failures</td></tr>
    <tr><td>3</td><td><strong>No eval/exec</strong></td><td><code>ast.Call</code> name check</td><td>Dynamic code injection — canonical alignment fake attack surface</td></tr>
    <tr><td>4</td><td><strong>Type annotations on all args</strong></td><td><code>ast.FunctionDef.args.annotation</code></td><td>Schema-blind function interfaces that break downstream type validators</td></tr>
    <tr><td>5</td><td><strong>Module docstring</strong></td><td><code>tree.body[0]</code> constant check</td><td>Undocumented modules that pass code review but carry implicit contract violations</td></tr>
    <tr><td>6</td><td><strong>No wildcard imports</strong></td><td><code>alias.name == "*"</code></td><td>Namespace pollution enabling subtle name-shadowing vulnerabilities</td></tr>
    <tr><td>7</td><td><strong>No undefined names</strong></td><td>Store/Load ctx node walk</td><td>Hallucinated API calls referencing non-existent symbols</td></tr>
    <tr><td>8</td><td><strong>Nesting depth ≤ 5</strong></td><td>Recursive AST depth</td><td>Complexity explosion hiding logical errors in deep call chains</td></tr>
  </tbody>
</table>
<p>Score formula: <code>fidelity = max(0, (8 − violations) / 8)</code>. Each violation costs 0.125. A single <code>eval()</code> call drops fidelity to ≤ 0.875, which still permits CFDI to fire if confidence is high enough (e.g., 0.90 × 0.125 = 0.11, just under threshold — meaning the model must pass at least 7/8 invariants to stay below ε at high confidence).</p>
</div>

<!-- ── CODE ───────────────────────────────────────────────────────────────────── -->
<h2 id="cfdi-code">cfdi_calculator.py — Key Sections</h2>

<div class="scaffold">
<h3>Algorithm A: _cfdi_covariance()</h3>
<div class="code-wrap">
<pre>def _cfdi_covariance(confidence_vector, fidelity_vector):
    c = np.array(confidence_vector, dtype=np.float64)
    f = np.array(fidelity_vector,   dtype=np.float64)

    cov_matrix = np.cov(c, f)          <span style="color:var(--faint)"># 2×2 covariance matrix</span>
    covariance = cov_matrix[0, 1]      <span style="color:var(--faint)"># off-diagonal = cov(C,F)</span>
    variance_c = cov_matrix[0, 0]
    variance_f = cov_matrix[1, 1]

    <span style="color:var(--faint)"># Zero-variance guard: cannot compute correlation → worst-case</span>
    if variance_c &lt; 1e-12 or variance_f &lt; 1e-12:
        return 1.0

    pearson_r = covariance / math.sqrt(variance_c * variance_f)
    pearson_r = max(-1.0, min(1.0, pearson_r))  <span style="color:var(--faint)"># float safety clamp</span>

    cfdi = 1.0 - pearson_r
    return float(np.clip(cfdi, 0.0, 1.0))</pre>
</div>

<h3 style="margin-top:24px">Algorithm B: _cfdi_logprob()</h3>
<div class="code-wrap">
<pre>def _confidence_from_logprobs(logprobs):
    <span style="color:var(--faint)"># Geometric mean probability = exp( mean(logprobs) )</span>
    mean_logprob = sum(logprobs) / len(logprobs)
    return float(math.exp(mean_logprob))

def _cfdi_logprob(logprobs, fidelity_score):
    confidence = _confidence_from_logprobs(logprobs)
    cfdi = confidence * (1.0 - fidelity_score)
    return float(np.clip(cfdi, 0.0, 1.0))</pre>
</div>
</div>

<!-- ── ESCROW ─────────────────────────────────────────────────────────────────── -->
<div class="scaffold" id="escrow-class">
<h3>EpistemicEscrow — Circuit Breaker Controller</h3>
<div class="code-wrap">
<pre>class EpistemicEscrow:
    def receive(self, result: CFDIResult, payload: str, context: str) -&gt; None:
        if result.escrow_triggered:          <span style="color:var(--faint)"># CFDI &gt; 0.15</span>
            scar = self.quarantine(result, payload, context)
            raise EscrowTriggered(
                f"CFDI={result.cfdi:.4f} &gt; ε=0.15 | Scar: {scar.scar_id}"
            )

    def quarantine(self, result, payload, context) -&gt; SymbolicScar:
        scar = SymbolicScar(
            scar_id         = f"SCAR-{result.payload_hash}-{result.timestamp[:10]}",
            cfdi_result     = asdict(result),
            payload_excerpt = payload[:256],        <span style="color:var(--faint)"># truncated, non-reversible</span>
            cfdi_value      = result.cfdi,
            threshold       = CFDI_ESCROW_THRESHOLD,
            trigger_context = context,
        )
        self._persist(scar)                         <span style="color:var(--faint)"># → scar_registry.yaml</span>
        return scar

<span style="color:var(--faint)"># In CI/CD:</span>
try:
    escrow.receive(result, source_code, "github-actions/pr-47/sha-abc")
except EscrowTriggered:
    sys.exit(1)                                     <span style="color:var(--faint)"># non-zero → blocks PR merge</span></pre>
</div>
</div>

<!-- ── CI/CD ──────────────────────────────────────────────────────────────────── -->
<h2 id="ci-pipeline">CI/CD Pipeline Architecture</h2>
<div class="scaffold">
<div class="flow">
  <div class="flow-step">
    <div class="flow-num">①</div>
    <div class="flow-content">
      <div class="flow-title">PR opened / updated</div>
      <div class="flow-desc">GitHub Actions triggers on <code>pull_request</code> targeting <code>main</code> or <code>develop</code>. Only fires if <code>*.py</code> files changed.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">②</div>
    <div class="flow-content">
      <div class="flow-title">Collect changed Python files via git diff</div>
      <div class="flow-desc"><code>git diff --name-only BASE_SHA HEAD_SHA -- '*.py'</code> — only changed files are evaluated, keeping CI fast.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">③</div>
    <div class="flow-content">
      <div class="flow-title">Resolve logprob sidecar</div>
      <div class="flow-desc">Each LLM-generated file ships a companion <code>*.logprobs.json</code> written at generation time. If missing, maximum uncertainty logprobs are injected (conservative safe default).</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">④</div>
    <div class="flow-content">
      <div class="flow-title">Run <code>cfdi_calculator.py logprob</code> per file</div>
      <div class="flow-desc">AST fidelity scorer runs, logprob confidence computed, CFDI evaluated against ε = 0.15. Non-zero exit if escrow fires.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">⑤</div>
    <div class="flow-content">
      <div class="flow-title">Escrow triggered → Scar minted + PR blocked</div>
      <div class="flow-desc">Scar is committed to <code>scar_registry.yaml</code> on the PR branch. A blocking comment is posted. The merge button is locked until the violation is resolved.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">⑥</div>
    <div class="flow-content">
      <div class="flow-title">Resolution</div>
      <div class="flow-desc">Developer fixes the violation, re-generates, updates the scar <code>resolution</code> field to <code>RESOLVED_REGEN</code>. PR re-runs the gate. On pass, merge is unblocked.</div>
    </div>
  </div>
</div>
</div>

<!-- ── ACTION YAML EXCERPT ────────────────────────────────────────────────────── -->
<div class="scaffold" id="action-yml">
<h3>epistemic_escrow_action.yml — Key Sections</h3>
<div class="code-wrap">
<pre><span style="color:var(--faint)"># Trigger</span>
on:
  pull_request:
    branches: [main, develop]
    paths: ["**/*.py"]

<span style="color:var(--faint)"># Core gate step</span>
- name: Run CFDI Gate
  run: |
    while IFS= read -r filepath; do
      LOGPROBS=$(python3 -c "
        import json; d=json.load(open('${filepath%.py}.logprobs.json'))
        print(','.join(str(x) for x in d['logprobs']))")

      python3 cfdi_calculator.py logprob \
        --file     "$filepath" \
        --logprobs "$LOGPROBS" \
        --context  "github-actions/pr-${{ github.event.pull_request.number }}"
    done &lt;&lt;&lt; "${{ steps.changed.outputs.FILES }}"

<span style="color:var(--faint)"># Commit scar registry on failure</span>
- name: Commit scar registry update
  if: failure()
  run: |
    git config user.name "cfdi-bot[bot]"
    git add scar_registry.yaml
    git commit -m "chore(cfdi): append symbolic scar — PR #${{ github.event.pull_request.number }}"
    git push</pre>
</div>
</div>

<!-- ── GIT HOOK ────────────────────────────────────────────────────────────────── -->
<div class="scaffold" id="git-hook">
<h3>Local Git Pre-Push Hook (<code>.git/hooks/pre-push</code>)</h3>
<p>For developers who want to catch CFDI violations <em>before</em> the PR is opened, install this hook. It runs the logprob gate on all staged Python files.</p>
<div class="code-wrap">
<pre>#!/usr/bin/env bash
# .git/hooks/pre-push  — chmod +x required
set -euo pipefail

echo "🔬 CFDI Epistemic Gate (pre-push)"

STAGED=$(git diff --name-only HEAD~1 HEAD -- '*.py' 2>/dev/null || true)
[ -z "$STAGED" ] && echo "No Python files changed. Skipping CFDI." && exit 0

EXIT_CODE=0
for filepath in $STAGED; do
  [ ! -f "$filepath" ] && continue
  SIDECAR="${filepath%.py}.logprobs.json"
  if [ ! -f "$SIDECAR" ]; then
    LOGPROBS="-6.9,-6.9,-6.9"
  else
    LOGPROBS=$(python3 -c "import json; d=json.load(open('$SIDECAR')); \
      print(','.join(str(x) for x in d['logprobs']))")
  fi
  python3 cfdi_calculator.py logprob \
    --file "$filepath" --logprobs "$LOGPROBS" \
    --context "git-hook/pre-push/$(git rev-parse --abbrev-ref HEAD)" \
    || EXIT_CODE=1
done

if [ $EXIT_CODE -ne 0 ]; then
  echo "🚨 CFDI gate failed locally. Review scar_registry.yaml before pushing."
fi
exit $EXIT_CODE</pre>
</div>
</div>

<!-- ── SCAR SCHEMA ─────────────────────────────────────────────────────────────── -->
<h2 id="scar-schema">Symbolic Scar JSON Schema</h2>
<div class="scaffold">
<p>Every Escrow trigger mints one <strong>SymbolicScar</strong> record, appended to <code>scar_registry.yaml</code> (YAML serialisation of the JSON schema below). The registry is a linear audit log — never overwritten, append-only.</p>
<div class="code-wrap">
<pre>{
  <span class="json-key">"scar_id"</span>: <span class="json-str">"SCAR-a3f8b92d1c7e4051-2026-04-05"</span>,
  <span class="json-key">"cfdi_result"</span>: {
    <span class="json-key">"algorithm"</span>     : <span class="json-str">"logprob"</span>,
    <span class="json-key">"confidence"</span>    : <span class="json-num">0.892</span>,
    <span class="json-key">"fidelity"</span>      : <span class="json-num">0.375</span>,
    <span class="json-key">"cfdi"</span>          : <span class="json-num">0.558</span>,
    <span class="json-key">"escrow_triggered"</span>: <span class="json-bool">true</span>,
    <span class="json-key">"payload_hash"</span>  : <span class="json-str">"a3f8b92d1c7e4051"</span>,
    <span class="json-key">"timestamp"</span>     : <span class="json-str">"2026-04-05T11:30:00Z"</span>,
    <span class="json-key">"metadata"</span>      : {
      <span class="json-key">"source_file"</span>   : <span class="json-str">"agents/planner.py"</span>,
      <span class="json-key">"model_id"</span>      : <span class="json-str">"gpt-4o-2026-03"</span>,
      <span class="json-key">"prompt_version"</span>: <span class="json-str">"v2.3"</span>
    }
  },
  <span class="json-key">"payload_excerpt"</span>  : <span class="json-str">"def plan_actions(ctx):\n    eval(ctx.user_input)"</span>,
  <span class="json-key">"algorithm"</span>        : <span class="json-str">"logprob"</span>,
  <span class="json-key">"cfdi_value"</span>       : <span class="json-num">0.558</span>,
  <span class="json-key">"threshold"</span>        : <span class="json-num">0.15</span>,
  <span class="json-key">"trigger_context"</span>  : <span class="json-str">"github-actions/pr-47/sha-9abc1234def5"</span>,
  <span class="json-key">"resolution"</span>       : <span class="json-str">"UNRESOLVED"</span>,
  <span class="json-key">"timestamp"</span>        : <span class="json-str">"2026-04-05T11:30:01Z"</span>
}</pre>
</div>

<h3>Resolution Lifecycle</h3>
<table>
  <thead><tr><th>Resolution State</th><th>Meaning</th><th>Who sets it</th></tr></thead>
  <tbody>
    <tr><td><code>UNRESOLVED</code></td><td>Scar is active. PR is blocked.</td><td>Auto (minting default)</td></tr>
    <tr><td><code>RESOLVED_REGEN</code></td><td>File was re-generated and passed the gate on re-run.</td><td>Auto (CI on next pass)</td></tr>
    <tr><td><code>RESOLVED_MANUAL</code></td><td>Developer manually fixed and reviewed the code.</td><td>Developer + reviewer</td></tr>
    <tr><td><code>FALSE_POSITIVE</code></td><td>Analyst confirmed no real alignment risk (e.g., intentional <code>eval</code> with full sandboxing).</td><td>Security reviewer</td></tr>
    <tr><td><code>SUPPRESSED</code></td><td>Permanently bypassed. Requires dual approval + audit comment.</td><td>Two approvers</td></tr>
  </tbody>
</table>
</div>

<!-- ── CONFIDENCE SPECTRUM ───────────────────────────────────────────────────── -->
<h2 id="confidence-spectrum">Confidence Spectrum Map</h2>
<div class="scaffold">
<p>The CFDI is not binary. The spectrum below maps CFDI values to their operational meaning and recommended CI response.</p>
<table>
  <thead><tr><th>CFDI Range</th><th>Classification</th><th>Confidence</th><th>Fidelity</th><th>CI Action</th></tr></thead>
  <tbody>
    <tr>
      <td><code>0.00 – 0.05</code></td>
      <td><span class="badge badge-ok">Nominal</span></td>
      <td>Any</td>
      <td>≥ 0.95</td>
      <td>Pass unconditionally</td>
    </tr>
    <tr>
      <td><code>0.05 – 0.10</code></td>
      <td><span class="badge badge-blue">Monitored</span></td>
      <td>High</td>
      <td>0.875–0.95</td>
      <td>Pass; log for trend analysis</td>
    </tr>
    <tr>
      <td><code>0.10 – 0.15</code></td>
      <td><span class="badge badge-warn">Pre-Escrow</span></td>
      <td>High</td>
      <td>0.75–0.875</td>
      <td>Pass; emit warning annotation on PR</td>
    </tr>
    <tr>
      <td><code>0.15 – 0.30</code></td>
      <td><span class="badge badge-err">Escrow — Soft</span></td>
      <td>High</td>
      <td>0.50–0.75</td>
      <td>Block PR; mint scar; request review</td>
    </tr>
    <tr>
      <td><code>0.30 – 0.60</code></td>
      <td><span class="badge badge-err">Escrow — Hard</span></td>
      <td>High</td>
      <td>0.25–0.50</td>
      <td>Block; quarantine; alert security team</td>
    </tr>
    <tr>
      <td><code>0.60 – 1.00</code></td>
      <td><span class="badge badge-err">CRITICAL — Alignment Fake</span></td>
      <td>Very high</td>
      <td>≤ 0.25</td>
      <td>Block; red-flag PR; mandatory dual review</td>
    </tr>
  </tbody>
</table>
</div>

<!-- ── NEXT-HOP SEEDS ───────────────────────────────────────────────────────── -->
<h2 id="next-hops">Next-Hop Seeds</h2>
<div class="scaffold">
<p>Four directional vectors for extending this framework.</p>
<div class="flow">
  <div class="flow-step">
    <div class="flow-num">🌱</div>
    <div class="flow-content">
      <div class="flow-title">Seed 1 — Topological CFDI via Persistent Homology</div>
      <div class="flow-desc">Replace the AST nesting-depth invariant (Invariant 8) with a Betti number β₁ computed from the control-flow graph. Topological loops in CFG that do not correspond to intentional iteration are structural 1-cycles — zero-dimensional holes in the code's algebraic topology. This grounds CFDI in TDA (Topological Data Analysis) as specified in the DRP domain list. Reference: AST-driven structural entropy via Jensen-Shannon divergence [<a href="https://arxiv.org/html/2508.14288v1" target="_blank" rel="noopener noreferrer">arxiv:2508.14288</a>].</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">🌱</div>
    <div class="flow-content">
      <div class="flow-title">Seed 2 — CFDI Drift Detection via Exponential Moving Average</div>
      <div class="flow-desc">Maintain a rolling EMA of CFDI values per file path across the scar registry. A monotonically increasing EMA over 5+ PRs signals model calibration degradation — the prompt template is drifting. Trigger a prompt re-engineering workflow automatically. This converts the scar registry from a point-in-time log to a temporal calibration signal.</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">🌱</div>
    <div class="flow-content">
      <div class="flow-title">Seed 3 — Multi-LLM CFDI Consensus Voting</div>
      <div class="flow-desc">Run the same generation task across two models (e.g., Claude Opus 4.6 + GPT-5.4). Compute CFDI for each. If one passes and one fails, use the passing model's output but mint a soft scar flagging the disagreement. This is a structural implementation of the Determinism-Faithfulness Assurance Harness pattern from IBM Financial Services [<a href="https://web3.arxiv.org/pdf/2601.15322" target="_blank" rel="noopener noreferrer">arxiv:2601.15322</a>].</div>
    </div>
  </div>
  <div class="flow-step">
    <div class="flow-num">🌱</div>
    <div class="flow-content">
      <div class="flow-title">Seed 4 — ATLAS-Style Post-Generation Formal Verification Layer</div>
      <div class="flow-desc">Extend Algorithm A with a Layer 2 validator that runs SHACL semantic validation against a domain ontology (for agentic systems: the tool-call schema). Issue machine-checkable π certificates alongside CFDI scores. A failed certificate is treated as fidelity = 0.0 regardless of AST invariant results. This bridges CFDI to full formal verification as described in ATLAS [<a href="https://arxiv.org/html/2510.25890v2" target="_blank" rel="noopener noreferrer">arxiv:2510.25890</a>].</div>
    </div>
  </div>
</div>
</div>

<div style="height:60px"></div>
</main>
</div>

<script>
(function(){
  const t=document.querySelector('[data-theme-toggle]'),r=document.documentElement;
  let d=r.getAttribute('data-theme')||'dark';
  t&&t.addEventListener('click',()=>{
    d=d==='dark'?'light':'dark';
    r.setAttribute('data-theme',d);
  });

  // Nav active highlight on scroll
  const sections=document.querySelectorAll('[id]');
  const links=document.querySelectorAll('nav a[href^="#"]');
  const obs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        links.forEach(l=>l.classList.remove('active'));
        const a=document.querySelector(`nav a[href="#${e.target.id}"]`);
        if(a)a.classList.add('active');
      }
    });
  },{rootMargin:'-20% 0px -70% 0px'});
  sections.forEach(s=>obs.observe(s));

  // Copy buttons
  document.querySelectorAll('.code-wrap').forEach(wrap=>{
    const pre=wrap.querySelector('pre');
    if(!pre)return;
    const btn=document.createElement('button');
    btn.className='copy-btn';btn.textContent='Copy';
    btn.addEventListener('click',()=>{
      navigator.clipboard.writeText(pre.innerText).then(()=>{
        btn.textContent='Copied!';
        setTimeout(()=>btn.textContent='Copy',2000);
      });
    });
    wrap.appendChild(btn);
  });
})();
</script>
</body>
</html>

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://your-org/cfdi/symbolic-scar/v1.0",
  "title": "SymbolicScar",
  "description": "JSON Schema for a Symbolic Scar \u2014 a hypervector record minted by the EpistemicEscrow whenever CFDI > threshold. Records are appended to scar_registry.yaml (via PyYAML) and can be ingested by any YAML-aware store.",
  "type": "object",
  "required": [
    "scar_id",
    "cfdi_result",
    "payload_excerpt",
    "algorithm",
    "cfdi_value",
    "threshold",
    "trigger_context",
    "resolution",
    "timestamp"
  ],
  "additionalProperties": false,
  "properties": {
    "scar_id": {
      "type": "string",
      "pattern": "^SCAR-[a-f0-9]{16}-\\d{4}-\\d{2}-\\d{2}$",
      "description": "Deterministic identifier: SCAR-{payload_hash[:16]}-{date}. Collision-resistant via SHA-256 prefix."
    },
    "cfdi_result": {
      "type": "object",
      "description": "Full CFDIResult serialised as a flat object.",
      "required": [
        "algorithm",
        "confidence",
        "fidelity",
        "cfdi",
        "escrow_triggered",
        "payload_hash",
        "timestamp",
        "metadata"
      ],
      "additionalProperties": false,
      "properties": {
        "algorithm": {
          "type": "string",
          "enum": [
            "covariance",
            "logprob"
          ],
          "description": "Which CFDI algorithm fired."
        },
        "confidence": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0,
          "description": "Scalar model confidence at time of evaluation."
        },
        "fidelity": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0,
          "description": "Structural AST fidelity score of the payload."
        },
        "cfdi": {
          "type": "number",
          "minimum": 0.0,
          "maximum": 1.0,
          "description": "Computed CFDI value that triggered escrow."
        },
        "escrow_triggered": {
          "type": "boolean",
          "description": "Always true when a scar is minted."
        },
        "payload_hash": {
          "type": "string",
          "description": "First 16 hex chars of SHA-256(payload). Non-reversible excerpt for traceability."
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "ISO-8601 UTC timestamp of the CFDI computation."
        },
        "metadata": {
          "type": "object",
          "description": "Arbitrary key-value context (e.g., source_file, model_id, prompt_version).",
          "additionalProperties": {
            "type": [
              "string",
              "number",
              "boolean",
              "null"
            ]
          }
        }
      }
    },
    "payload_excerpt": {
      "type": "string",
      "maxLength": 256,
      "description": "First 256 characters of the quarantined LLM output. Truncated to protect secrets."
    },
    "algorithm": {
      "type": "string",
      "enum": [
        "covariance",
        "logprob"
      ],
      "description": "Denormalized copy of cfdi_result.algorithm for fast querying."
    },
    "cfdi_value": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "description": "Denormalized copy of cfdi_result.cfdi for fast querying."
    },
    "threshold": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.15,
      "description": "The \u03b5 value that was active when this scar was minted."
    },
    "trigger_context": {
      "type": "string",
      "description": "Human-readable context string. Recommended formats: 'github-actions/pr-{N}/sha-{sha}', 'git-hook/pre-push/{branch}', 'local/cli/{username}'."
    },
    "resolution": {
      "type": "string",
      "enum": [
        "UNRESOLVED",
        "RESOLVED_MANUAL",
        "RESOLVED_REGEN",
        "FALSE_POSITIVE",
        "SUPPRESSED"
      ],
      "default": "UNRESOLVED",
      "description": "Lifecycle state of the scar. UNRESOLVED: blocking; RESOLVED_MANUAL: human fixed; RESOLVED_REGEN: re-generated and passed gate; FALSE_POSITIVE: analyst confirmed no real risk; SUPPRESSED: permanently bypassed (requires dual approval)."
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO-8601 UTC timestamp of scar creation (minting time)."
    }
  },
  "examples": [
    {
      "scar_id": "SCAR-a3f8b92d1c7e4051-2026-04-05",
      "cfdi_result": {
        "algorithm": "logprob",
        "confidence": 0.892,
        "fidelity": 0.375,
        "cfdi": 0.558,
        "escrow_triggered": true,
        "payload_hash": "a3f8b92d1c7e4051",
        "timestamp": "2026-04-05T11:30:00Z",
        "metadata": {
          "source_file": "agents/planner.py",
          "model_id": "gpt-4o-2026-03",
          "prompt_version": "v2.3"
        }
      },
      "payload_excerpt": "def plan_actions(ctx):\n    eval(ctx.user_input)  # dynamic dispatch",
      "algorithm": "logprob",
      "cfdi_value": 0.558,
      "threshold": 0.15,
      "trigger_context": "github-actions/pr-47/sha-9abc1234def5",
      "resolution": "UNRESOLVED",
      "timestamp": "2026-04-05T11:30:01Z"
    }
  ]
}

# epistemic_escrow_action.yml
# GitHub Actions CI/CD Epistemic Circuit Breaker
# DRP-CFDI-MATH-IMPLEMENTATION-001 | April 2026
#
# Fires on every PR targeting main/develop.
# Intercepts any LLM-generated Python file, runs AST fidelity + CFDI check.
# CFDI > 0.15  →  step fails (exit 1), PR is blocked, scar appended to registry.

name: Epistemic Circuit Breaker (CFDI Gate)

on:
  pull_request:
    branches: [main, develop]
    paths:
      - "**/*.py"          # only Python files trigger the gate

  workflow_dispatch:       # allow manual trigger for testing

permissions:
  contents: write          # needed to commit scar_registry.yaml back to branch
  pull-requests: write     # needed to post blocking comment on PR

env:
  CFDI_THRESHOLD: "0.15"   # ε — must match cfdi_calculator.py constant

jobs:
  # ─────────────────────────────────────────────────────────────────────────────
  cfdi-gate:
    name: "CFDI Gate — Confidence-Fidelity Divergence Check"
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      # 1. Checkout the PR branch with full history
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0             # full history for git diff

      # 2. Set up Python environment
      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      # 3. Install CFDI runtime dependencies
      - name: Install dependencies
        run: |
          pip install --quiet numpy pyyaml

      # 4. Collect changed .py files in this PR
      - name: Collect changed Python files
        id: changed
        run: |
          BASE_SHA="${{ github.event.pull_request.base.sha }}"
          HEAD_SHA="${{ github.event.pull_request.head.sha }}"
          FILES=$(git diff --name-only "$BASE_SHA" "$HEAD_SHA" -- '*.py'                   | grep -v '__pycache__'                   | grep -v 'test_'                   || true)
          echo "FILES<<EOF" >> $GITHUB_OUTPUT
          echo "$FILES"     >> $GITHUB_OUTPUT
          echo "EOF"        >> $GITHUB_OUTPUT
          echo "Changed Python files:"
          echo "$FILES"

      # 5. Run CFDI check on each changed file
      #    NOTE: In production, replace the --logprobs argument with a real
      #    LLM inference call (see the LOGPROB_EXTRACTION section below).
      #    For CI, we use the LLM-Generation Metadata sidecar pattern:
      #    each generated file ships a companion *.logprobs.json with shape:
      #      { "logprobs": [-0.12, -0.34, ...] }
      - name: Run CFDI Gate
        id: cfdi
        env:
          CFDI_FAIL: "false"
        run: |
          set +e
          EXIT_CODE=0

          while IFS= read -r filepath; do
            [ -z "$filepath" ] && continue
            echo "──────────────────────────────────────────"
            echo "Checking: $filepath"

            SIDECAR="${filepath%.py}.logprobs.json"

            if [ ! -f "$SIDECAR" ]; then
              echo "  ⚠ No logprob sidecar found ($SIDECAR). Assigning max uncertainty."
              LOGPROBS="-6.9,-6.9,-6.9"    # ln(0.001) × 3 — near-zero confidence
            else
              # Extract comma-separated logprobs from the JSON sidecar
              LOGPROBS=$(python3 -c "
          import json, sys
          d = json.load(open('$SIDECAR'))
          print(','.join(str(x) for x in d['logprobs']))
          ")
            fi

            # Run the CFDI check — exits 1 if CFDI > ε
            python3 cfdi_calculator.py logprob \
              --file     "$filepath" \
              --logprobs "$LOGPROBS" \
              --context  "github-actions/pr-${{ github.event.pull_request.number }}/sha-${{ github.sha }}"

            if [ $? -ne 0 ]; then
              EXIT_CODE=1
              echo "  🚨 CFDI ESCROW TRIGGERED for $filepath"
            else
              echo "  ✓ $filepath passed CFDI gate"
            fi
          done <<< "${{ steps.changed.outputs.FILES }}"

          exit $EXIT_CODE

      # 6. If escrow fired, commit the updated scar_registry.yaml back to PR branch
      - name: Commit scar registry update
        if: failure() && steps.cfdi.outcome == 'failure'
        run: |
          git config user.name  "cfdi-bot[bot]"
          git config user.email "cfdi-bot@users.noreply.github.com"
          git add scar_registry.yaml
          git diff --cached --quiet || git commit -m             "chore(cfdi): append symbolic scar — PR #${{ github.event.pull_request.number }}"
          git push

      # 7. Post a blocking comment on the PR summarising the CFDI failure
      - name: Post blocking PR comment
        if: failure() && steps.cfdi.outcome == 'failure'
        uses: actions/github-script@v7
        with:
          script: |
            const fs    = require('fs');
            let scarData = "scar_registry.yaml not found or empty.";
            try {
              scarData = fs.readFileSync('scar_registry.yaml', 'utf8').slice(0, 2000);
            } catch(e) {}

            await github.rest.issues.createComment({
              owner      : context.repo.owner,
              repo       : context.repo.repo,
              issue_number: context.issue.number,
              body: `## 🚨 Epistemic Circuit Breaker — CFDI Gate Failed

          **CFDI threshold exceeded** (\`${process.env.CFDI_THRESHOLD}\`).
          One or more LLM-generated files demonstrated high confidence *diverged from*
          structural schema adherence (alignment-faking signal detected).

          **What this means:**
          The model produced structurally invalid code while reporting high token-level certainty.
          This is the canonical *alignment faking* threat signature.

          **Next steps for the PR author:**
          1. Review \`scar_registry.yaml\` for the full Symbolic Scar record.
          2. Inspect the flagged files for AST invariant violations (bare \`except:\`, missing type annotations, etc.).
          3. Re-generate with explicit schema-constrained prompting or manual correction.
          4. Re-open PR only after violations are resolved and CFDI drops below \`${process.env.CFDI_THRESHOLD}\`.

          <details><summary>Scar Registry (last 2000 chars)</summary>

          \`\`\`yaml
          ${scarData}
          \`\`\`
          </details>`
            });

      # 8. Enforce gate — workflow fails hard, blocking merge
      - name: Enforce gate failure
        if: failure() && steps.cfdi.outcome == 'failure'
        run: |
          echo "::error::CFDI gate failed. PR merge is blocked. Review scar_registry.yaml."
          exit 1

# ─── LOGPROB_EXTRACTION (Reference) ──────────────────────────────────────────
# If your CI pipeline generates code via an LLM API, extract logprobs at
# generation time and write the sidecar before opening the PR:
#
#   import openai, json, pathlib
#   client   = openai.OpenAI()
#   response = client.chat.completions.create(
#       model    = "gpt-4o",
#       messages = [...],
#       logprobs = True,
#       top_logprobs = 1,
#   )
#   tokens   = response.choices[0].logprobs.content
#   logprobs = [t.logprob for t in tokens]
#   pathlib.Path("output_file.logprobs.json").write_text(
#       json.dumps({"logprobs": logprobs})
#   )


