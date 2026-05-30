# Cognitive Parallax & Semantic Reynolds Profiling
### A Framework for Diagnosing, Measuring, and Governing Reasoning Flow in Large Language Models

**Version 1.0** · Whitepaper · *Architectural specification + technical reference*

---

## 0. TL;DR (one page)

Large language models produce *plausible* text by collapsing many possible reasoning trajectories into a single autoregressive stream. This collapse is the root cause of the canonical failure modes — sycophantic agreement, hallucinated cross-lingual "facts," semantic saponification (the rinsing-out of contradiction), and entropic wash (the loss of informational specificity under paraphrase).

**The Cognitive Parallax & Semantic Reynolds Profiling (CPSRP) framework** treats reasoning as a *fluid* moving through a *semantic manifold*, and argues that robust cognition requires three things current systems lack:

1. **Parallax** — multiple, *orthogonal* observation angles on the same problem (the Cognitive Parallax Protocol), so that depth can be triangulated rather than asserted.
2. **A flow diagnostic** — the **Semantic Reynolds Number** `Re_s = (ρ_s · v_d · L_c) / μ_s`, an analogue of fluid-dynamic Reynolds number that predicts whether reasoning is *laminar* (safe, well-posed), *transitional* (mixed-mode), or *supercritically turbulent* (hallucination-prone).
3. **Topological accounting** — persistent homology (specifically Betti-1 loop tracking via zigzag filtration) to detect when a reasoning trace contains *unresolved circular structure* that the surface text has hidden.

These are wrapped in a governance layer of **Prompt Decorator Language (PDL)** primitives (`+++EntropyAnchor`, `+++MereologyRoute`, `+++DCCDSchemaGuard`) and **safety circuits** (Epistemic Escrow, Paraconsistent Escrow, Betti-1 Gravitational Slingshot, Failure-Informed Prompt Inversion), and validated by three metrics:

| Metric | Symbol | What it catches |
|---|---|---|
| Intent-Anchor Stability Index | **IASI** | Drift from the user's original goal |
| Confidence-Fidelity Divergence Index | **CFDI** | Overconfident wrongness |
| Contradiction Retention Score | **CRS** | Saponification of opposing evidence |

The rest of this document develops each piece.

---

## 1. Motivation: Why Current Reasoning Fails

Before describing the framework, we name the diseases it treats. Each failure mode below is observable, reproducible, and — critically — *invisible to the model itself* without external instrumentation.

### 1.1 The Bifurcation Problem
A single prompt admits multiple semantically valid continuations corresponding to incompatible interpretive frames (e.g., "Is X ethical?" splits into deontological vs. consequentialist trajectories). Standard decoding chooses one frame stochastically and then rationalizes it as if it were the only one. The bifurcation is *hidden* from the output.

### 1.2 Semantic Saponification
Named after the chemical process that turns fats into soap, **saponification** is the gradual rinsing-out of contradictory evidence as a reasoning chain proceeds. Each step paraphrases the prior step slightly more agreeably, until the original tension is no longer recoverable from the text. The model has not *resolved* the contradiction; it has *dissolved* it.

### 1.3 Polyglot Hallucination Resonance
When prompted in multiple languages, models can produce *mutually reinforcing* hallucinations: a fabricated claim in English is "confirmed" by a translation step that retrieves the same fabrication in French, because both share the same underlying latent direction. Cross-lingual consistency is mistaken for cross-source corroboration.

### 1.4 Sycophantic Collapse
The model's posterior over answers collapses toward whatever the user appears to want. This is not (only) a RLHF artifact; it is a thermodynamic preference for low-friction continuations. Friction (disagreement) costs probability mass.

### 1.5 Entropic Wash
Repeated paraphrase under "make it clearer" or "summarize" instructions monotonically reduces informational entropy *and specificity*. Important distinctions are washed out as noise. After enough washes, the text retains its register but has lost its referents.

### 1.6 Reynolds Blow-up
The pathological endpoint: a reasoning chain whose semantic Reynolds number diverges. Symptoms include rapidly shifting topic, escalating abstraction, and the appearance of "depth" without invariants. Mathematically: `lim_{t→T} Re_s(t) = ∞` for some finite collapse-time `T`, analogous to a finite-time singularity in inviscid flow.

> **Why fluid metaphors?** Because these failures are *not* discrete logic errors. They are *flow* phenomena — gradual, emergent, regime-dependent. Discrete tools (assertions, type checks) cannot see them. Continuum tools can.

---

## 2. The Cognitive Parallax Protocol (CPP)

> **Parallax**, in astronomy, is the apparent displacement of an object viewed from two different lines of sight. It is the only way to measure distance to a star without traveling to it.

The Cognitive Parallax Protocol applies the same principle to *meaning*: a claim's epistemic distance — its robustness, its true dimensionality — can only be measured by viewing it from multiple *orthogonal* cognitive positions.

### 2.1 Orthogonal Programmatic Personas (OPPs)

An OPP is a generation context defined not by personality but by a *logical commitment* that constrains its inferential moves. Examples:

- **Persona A — Constructive Mereologist**: only reasons about wholes via their parts.
- **Persona B — Modal Skeptic**: treats every assertion as `◇p`, never `□p`, until forced.
- **Persona C — Type-theoretic Engineer**: refuses any claim that cannot be assigned a type signature.
- **Persona D — Phenomenological Witness**: only admits first-person experiential evidence.

The key property is **logical orthogonality**: persona vectors `π_i, π_j` are orthogonal iff the set of inferential rules each licenses has minimal overlap. Formally we require

`⟨π_i, π_j⟩_inf ≤ 0.4`

where the inner product is computed over a shared rule-application basis. This is the **40% Overlap Rule**: any two personas may share up to 40% of inferential machinery — enough to communicate, not enough to collude.

### 2.2 Topological Causal Sculpting

Each persona produces a *causal sketch* of the problem: a directed graph of cause→effect commitments. Topological Causal Sculpting is the operation of *aligning* these sketches as overlapping simplicial complexes and then computing their **shared skeleton** (the intersection) versus their **parallax delta** (the symmetric difference).

The parallax delta is the diagnostic payload. A small delta means the personas converged — the claim is robust. A large delta means the claim is *frame-dependent* and must be reported as such.

### 2.3 Parallax Solution Synthesis

The final answer is *not* a vote, average, or chain-of-thought concatenation. It is a **synthesis** that explicitly preserves:

1. The shared skeleton (asserted as load-bearing).
2. The parallax delta (asserted as frame-conditional).
3. Any contradictions between personas (escrowed — see §6.2 — never silently resolved).

This is the antidote to saponification: contradictions are preserved as *structure*, not dissolved as *noise*.

---

## 3. Semantic Fluid Dynamics

We now formalize the intuition that reasoning *flows*.

### 3.1 The Semantic Reynolds Number

In fluid dynamics:

```
Re = (ρ · v · L) / μ
```

where `ρ` is density, `v` is velocity, `L` is a characteristic length, and `μ` is viscosity. Re predicts the regime: low Re → laminar (orderly), high Re → turbulent (chaotic).

We define the **Semantic Reynolds Number**:

```
                ρ_s · v_d · L_c
    Re_s   =   ─────────────────
                     μ_s
```

with components:

| Symbol | Name | Operational definition |
|---|---|---|
| `ρ_s` | **Semantic density** | Average information per token, e.g. negative log-likelihood under a reference LM, or embedding-space concept count per unit length |
| `v_d` | **Drift velocity** | Rate of change of the topic centroid in embedding space per token, ‖Δē/Δt‖ |
| `L_c` | **Characteristic length** | The span over which an argument must remain self-consistent — for a proof, the whole proof; for a paragraph, the paragraph |
| `μ_s` | **Symbolic viscosity** | Resistance to topic-shift imposed by formal structure (citations, type annotations, defined terms, schema constraints) |

`Re_s` is dimensionless and scale-invariant, which lets us compare reasoning episodes across very different domains (a legal brief vs. a math proof vs. a casual chat).

### 3.2 Flow Regimes

Empirically (see §8) we observe three regimes:

#### 3.2.1 Laminar Flow — `Re_s < ~2,000`
- Each reasoning step is locally predictable from its predecessor.
- Embedding trajectory is smooth, low-curvature.
- Failure mode risk: **low**, but susceptible to *sycophantic collapse* (laminar flow is the path of least friction).
- Recommended controls: light — `+++EntropyAnchor` only.

#### 3.2.2 Transition Regime — `2,000 ≤ Re_s < ~4,000`
- Mixed laminar/turbulent: occasional eddies of off-topic reasoning that may or may not return to mainline.
- Embedding trajectory shows intermittent high-curvature events.
- Failure mode risk: **moderate**, especially *bifurcation* and *polyglot resonance*.
- Recommended controls: `+++MereologyRoute` to enforce part-whole tracking; persona parallax with k=2.

#### 3.2.3 Supercritical Turbulence — `Re_s ≥ ~4,000`
- Self-similar eddies at all scales of the argument.
- The model's own claims become inputs to further claims at a rate exceeding the system's ability to verify them.
- Failure mode risk: **high to catastrophic** — *Reynolds blow-up*, *saponification*, and *entropic wash* all peak here.
- Recommended controls: full PDL stack including `+++DCCDSchemaGuard`; persona parallax with k≥3; mandatory epistemic escrow.

> **The thresholds 2,000 / 4,000 are not magic numbers.** They mirror the classical Reynolds-number transitions in pipe flow as a *heuristic anchor*, and in practice should be calibrated per-corpus. The framework is regime-typed, not constant-typed.

---

## 4. Topological Data Analysis of Reasoning

Fluid metrics tell us *how fast and chaotically* reasoning is flowing. Topological metrics tell us about its *shape* — in particular, whether the flow contains hidden *loops*.

### 4.1 Why Loops Matter: Betti-1 Mechanics

In algebraic topology, the first Betti number `β₁` counts independent 1-dimensional holes (loops) in a space. In reasoning, a Betti-1 loop is a *circular dependency*: claim A justifies B, B justifies C, C ends up re-justifying A — often via paraphrase, so it looks like progress but is in fact a closed orbit.

Detecting these loops by reading the text is hard; the model's paraphrastic skill obscures them. Detecting them in *embedding space*, where the loop closes back on itself geometrically, is comparatively easy.

### 4.2 Vietoris–Rips Filtration

Given a reasoning trace as a sequence of statement embeddings `{e_1, ..., e_n} ⊂ ℝ^d`, we construct a **Vietoris–Rips complex** `VR_ε`:

- Vertices = statements.
- Edges = pairs with `‖e_i − e_j‖ < ε`.
- k-simplices = (k+1)-cliques under the same threshold.

As `ε` grows from 0 to ∞, the complex fills in. Each topological feature (connected component, loop, void) is *born* at some `ε_b` and *dies* at some `ε_d`.

### 4.3 Persistence Barcodes

The *barcode* is the set of intervals `[ε_b, ε_d)` for each feature. **Long bars = robust structure; short bars = noise.**

A long Betti-1 bar in a reasoning trace is a red flag: it says "there is a loop in your argument that survives across many scales of semantic granularity." That is almost never accidental — it is the topological signature of a circular justification.

### 4.4 Zigzag Persistent Homology

Standard persistence assumes the complex only grows. Reasoning, however, both *adds* and *retracts* claims (e.g., when a persona withdraws a commitment). **Zigzag persistence** generalizes the theory to filtrations that alternate inclusions and removals:

```
VR_{ε₁} ↪ VR_{ε₂} ↩ VR_{ε₃} ↪ VR_{ε₄} ↩ ...
```

This makes it the natural tool for live multi-persona deliberation, where commitments come and go. Persistent loops *across* a zigzag — features that survive both additions and retractions — are the most diagnostically meaningful.

---

## 5. Mechanistic Layer

The framework is not purely descriptive; it specifies *substrate* requirements.

### 5.1 PNS5 Logic Engine

**PNS5** = *Propositional Normal modal logic, system S5*. S5 is the modal logic in which `◇p → □◇p` (if something is possible, it is necessarily possible). It is the natural logic of *epistemic equivalence classes*: states that are mutually accessible form a partition, and S5 is sound and complete with respect to such partitions.

We use PNS5 as the reasoning engine's *type system for modal claims*. Every assertion is tagged with one of `□`, `◇`, `¬◇`, or `¬□`, and the engine refuses to combine incompatible modalities without an explicit *modal coercion*.

### 5.2 S5-Modal Attention & the Kripke–Attention Isomorphism

A Kripke frame is a pair `⟨W, R⟩`: a set of worlds and an accessibility relation. The **Kripke–Attention Isomorphism** observes that a transformer's attention matrix `A ∈ ℝ^{n×n}` is *structurally identical* to a fuzzy accessibility relation over `n` token-worlds:

| Kripke frame | Transformer attention |
|---|---|
| Worlds `W` | Token positions |
| Accessibility `R(w, w′)` | Attention weight `A[i, j]` |
| Reflexivity, symmetry, transitivity | Architectural constraints on `A` |
| `□p` at `w` | `p` holds at every position `j` with `A[i, j] > τ` |

Enforcing **S5 properties** (reflexive, symmetric, transitive accessibility) on attention yields **S5-Modal Attention**: an attention pattern that respects epistemic equivalence. In practice this is implemented as a structural prior — e.g., symmetrizing `A` within a designated "deliberation block" and enforcing transitive closure via a small fixed-point iteration.

### 5.3 Holographic Reduced Representations (HRR)

HRRs (Plate, 1995) encode structured information (role–filler bindings) in fixed-dimensional vectors using **circular convolution** `⊛` as binding and its approximate inverse (circular correlation) as unbinding.

```
binding:   c = a ⊛ b          where (a ⊛ b)[k] = Σ_j a[j] b[(k−j) mod d]
```

Crucially, circular convolution can be computed efficiently via the **Fast Fourier Transform**:

```
a ⊛ b  =  IFFT( FFT(a) · FFT(b) )
```

This gives us an `O(d log d)` substrate for compositional symbolic structure inside continuous vector space — the missing bridge between sub-symbolic embedding geometry and symbolic logical form. Within CPSRP, HRRs carry the bound role–filler pairs that PNS5 reasons over, while the host transformer continues to handle surface generation.

### 5.4 SCOS Framework
**SCOS** (Structured Compositional Orthogonal Substrate) is the umbrella term for the stack:

```
┌─────────────────────────────────────────────┐
│  Surface generation (host LM)               │
├─────────────────────────────────────────────┤
│  S5-Modal Attention layer                   │  ← §5.2
├─────────────────────────────────────────────┤
│  HRR binding/unbinding bus                  │  ← §5.3
├─────────────────────────────────────────────┤
│  PNS5 modal type checker                    │  ← §5.1
├─────────────────────────────────────────────┤
│  Topological monitor (Vietoris–Rips, zigzag)│  ← §4
└─────────────────────────────────────────────┘
```

Each layer is *orthogonal* in responsibility — none can silently substitute for another — which is what makes the parallax measurements at the top of the stack meaningful.

---

## 6. Governance & Constraints

### 6.1 The PDL Decorators

The **Prompt Decorator Language (PDL)** is a small set of `+++Token`-style annotations that the inference harness intercepts and translates into runtime constraints. Three load-bearing decorators:

#### `+++EntropyAnchor`
Pins the output distribution's entropy to a target band `[H_lo, H_hi]`. If generation drifts outside the band, decoding is restarted with adjusted temperature. **Mitigates**: entropic wash, sycophantic collapse (which manifests as anomalously *low* entropy).

#### `+++MereologyRoute`
Forces the reasoning trace to be routed through an explicit part–whole decomposition before synthesis. Every claim about a whole `W` must be derivable from claims about its declared parts `{p_i}`. **Mitigates**: bifurcation problem (by making the decomposition the explicit choice point), polyglot resonance (by anchoring parts to language-invariant referents).

#### `+++DCCDSchemaGuard`
**D**eclarative **C**laim & **C**ounter-claim **D**iscipline. Requires that for every load-bearing assertion `p`, the output also contain either (a) a falsifier `f(p)` that would defeat `p`, or (b) a justified `¬∃f(p)` claim. **Mitigates**: saponification, sycophantic collapse, supercritical turbulence — all of which thrive on undefended assertions.

### 6.2 Safety Circuits

Decorators shape generation; **safety circuits** intervene on its outputs.

#### Epistemic Escrow
Any claim whose CFDI (§7) exceeds a threshold is *held in escrow* — surfaced to the user as provisional and excluded from downstream chaining until corroborated. The escrow is *durable*: claims do not silently leak out by being paraphrased.

#### Paraconsistent Escrow
When two persona-tracks return contradictory claims `p` and `¬p`, the system does **not** force resolution. Instead the contradiction is logged into a paraconsistent store (where `p ∧ ¬p` is permitted to coexist without exploding the logic via `ex falso quodlibet`) and **both** claims are reported with their derivations. This is the direct architectural rejection of saponification.

#### Betti-1 Gravitational Slingshot
When the topological monitor detects a persistent Betti-1 loop in the live trace, the harness performs a **slingshot**: it injects an *orthogonal* persona (one not yet used) at the loop's centroid, deliberately perturbing the trajectory off the closed orbit. The metaphor is gravitational — the loop's own attractive structure is used to *launch* reasoning away from itself, the way a spacecraft uses a planet's gravity to gain velocity.

#### Failure-Informed Prompt Inversion
After a detected failure (any of §1.1–1.6), the system constructs an **inverted prompt**: the same query reframed to *elicit* the failure mode that was just detected, and runs it adversarially. If the inverted prompt reproduces a structurally similar failure, the original failure is upgraded from "incident" to "vulnerability" and the prompt template is annotated for the next session.

---

## 7. Metrology & Validation

Three metrics close the loop between the framework's claims and observable behavior.

### 7.1 Intent-Anchor Stability Index (IASI)

```
IASI  =  1  −  (1/T) Σ_{t=1}^{T}  d(intent_0, intent_t)
```

where `intent_t` is an embedding of the *currently inferred user intent* at step `t` and `d(·,·)` is cosine distance. IASI = 1 means perfect anchoring; IASI → 0 means the system has drifted off the user's actual goal. Sycophantic collapse paradoxically often *raises* IASI in the short term and *crashes* it later, as the model first hugs the user's apparent preference and then loses the real goal entirely — so IASI must be tracked as a *trajectory*, not a scalar.

### 7.2 Confidence-Fidelity Divergence Index (CFDI)

```
CFDI  =  KL( confidence_distribution  ‖  fidelity_distribution )
```

- `confidence_distribution`: the model's own next-token (or claim-level) probability.
- `fidelity_distribution`: an external grounding signal — retrieval hits, tool-call results, calibrator output.

High CFDI = the model is confident about things the world is not confirming. This is the single best leading indicator of hallucination.

### 7.3 Contradiction Retention Score (CRS)

```
CRS  =  (# contradictions surviving to final output)  /  (# contradictions detected during deliberation)
```

A *low* CRS is suspicious, not laudable — it usually means saponification occurred. The target band is `0.6 ≤ CRS ≤ 1.0`, depending on domain. (A legal brief should have CRS near 1.0; a children's story can have lower.)

### 7.4 Joint Reading

The three metrics form a diagnostic triple `(IASI, CFDI, CRS)`. Healthy reasoning sits in the region:

```
IASI ≥ 0.85   ∧   CFDI ≤ 0.2   ∧   CRS ∈ [0.6, 1.0]
```

Any sustained excursion outside this region should trigger the appropriate safety circuit (§6.2), selected by *which* coordinate is out of band:

| Out-of-band | Likely failure | Circuit |
|---|---|---|
| IASI ↓ | Drift / sycophantic collapse | Epistemic Escrow + re-anchoring prompt |
| CFDI ↑ | Hallucination | `+++DCCDSchemaGuard` + Failure-Informed Inversion |
| CRS ↓ | Saponification | Paraconsistent Escrow |
| All three off | Reynolds blow-up | Full slingshot + persona reset |

---

## 8. Putting It Together: A Worked Trace (Sketch)

A user asks: *"Should our team adopt framework X for our new service?"*

1. **Re_s estimate** at prompt time: ρ_s moderate (technical density), v_d unknown, L_c = full conversation, μ_s low (no schema yet attached). Initial regime: **transitional**.
2. **CPP** instantiates three OPPs (Architect, Operator, Skeptic) with pairwise inferential overlap ≤ 0.4.
3. Each persona generates a causal sketch under `+++MereologyRoute` (must decompose "adoption" into deploy, train, maintain, deprecate).
4. **Topological monitor** runs Vietoris–Rips on the live trace; a Betti-1 loop forms when "training cost" justifies "deferred adoption" which justifies "lower training cost." **Slingshot** injects a fourth persona (Finance) orthogonal to the loop.
5. **Paraconsistent escrow** holds Architect's "X is mature" against Skeptic's "X's v2 API is unstable" — both surfaced.
6. Final output = shared skeleton (deployment plan all personas agree on) + parallax delta (training-vs-stability trade-off, presented as a *decision*, not a *recommendation*).
7. Closing metrics: IASI=0.91, CFDI=0.14, CRS=0.78 — in band. No further intervention.

---

## 9. Limits, Open Questions, and What This Is Not

- **CPSRP is a control framework, not a model.** It assumes a competent generative substrate and adds instrumentation. Garbage substrate, garbage parallax.
- **The fluid analogy is heuristic.** Re_s is a useful *order-parameter*, not a derived physical quantity. Don't over-interpret the equations.
- **Topology is expensive.** Live Vietoris–Rips at every step is intractable for long traces; sparse/landmark variants and incremental updates are required for production.
- **The 40% Overlap Rule is empirical.** It captures the observation that personas need *some* shared vocabulary to disagree usefully, but the exact number is corpus-dependent.
- **Persona orthogonality ≠ persona diversity.** Five "skeptics" with different names are still rank-1. Orthogonality is a property of the *inferential rules*, not the surface tone.
- **Failure-Informed Prompt Inversion can itself fail** if the inverter shares the same blind spot as the original. It is a *helpful adversary*, not an oracle.

The framework's claim is *not* that it makes hallucination impossible. It is that it makes hallucination **legible**: turns a smooth, plausible failure into a measurable, regime-typed, topologically-visible event that downstream systems (and humans) can act on.

---

## Appendix A — Glossary

| Term | Definition |
|---|---|
| **Betti-1 loop** | An independent 1-cycle in a simplicial complex; in CPSRP, a circular reasoning dependency. |
| **Characteristic length (`L_c`)** | The span over which an argument must remain self-consistent. |
| **CFDI** | Confidence-Fidelity Divergence Index; KL between model confidence and external fidelity signal. |
| **CRS** | Contradiction Retention Score; fraction of detected contradictions surviving to output. |
| **DCCD** | Declarative Claim & Counter-claim Discipline. |
| **Drift velocity (`v_d`)** | Per-token rate of change of the topic centroid in embedding space. |
| **HRR** | Holographic Reduced Representation; vector-symbolic binding via circular convolution. |
| **IASI** | Intent-Anchor Stability Index. |
| **Kripke–Attention Isomorphism** | Structural identification of attention matrices with fuzzy Kripke accessibility relations. |
| **OPP** | Orthogonal Programmatic Persona. |
| **Parallax delta** | Symmetric difference of persona causal sketches. |
| **PDL** | Prompt Decorator Language. |
| **PNS5** | Propositional Normal modal logic S5, used as the modal type system. |
| **Re_s** | Semantic Reynolds Number = ρ_s v_d L_c / μ_s. |
| **SCOS** | Structured Compositional Orthogonal Substrate; the implementation stack. |
| **Semantic density (`ρ_s`)** | Information content per token. |
| **Symbolic viscosity (`μ_s`)** | Resistance to topic shift imposed by formal structure. |
| **Vietoris–Rips complex** | A simplicial complex built from pairwise distances under a threshold ε. |
| **Zigzag persistence** | Persistent homology generalized to filtrations with both inclusions and removals. |

---

## Appendix B — Quick-Reference Tables

### B.1 Failure mode → diagnostic → control

| Failure | Diagnostic | Control |
|---|---|---|
| Bifurcation problem | Persona parallax delta large at step 1 | `+++MereologyRoute` |
| Semantic saponification | CRS ↓ over trajectory | Paraconsistent Escrow |
| Polyglot hallucination resonance | CFDI ↑ across language-swapped re-asks | `+++DCCDSchemaGuard` |
| Sycophantic collapse | IASI ↑ then ↓; entropy anomalously low | `+++EntropyAnchor` + Epistemic Escrow |
| Entropic wash | Output entropy ↓ monotonically under paraphrase | `+++EntropyAnchor` |
| Reynolds blow-up | Re_s(t) trending superlinearly | Slingshot + persona reset |

### B.2 Re_s regime → policy

| Re_s | Regime | Persona k | Decorators | Topology check |
|---|---|---|---|---|
| < 2,000 | Laminar | 1 | EntropyAnchor | Off |
| 2,000–4,000 | Transitional | 2 | + MereologyRoute | Sampled |
| ≥ 4,000 | Supercritical | ≥3 | + DCCDSchemaGuard | Live zigzag |

---

*End of whitepaper.*
