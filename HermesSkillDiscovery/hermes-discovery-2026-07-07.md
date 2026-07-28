# Hermes Agent Harness — Daily Integration Discovery Run

**Date:** 2026-07-07
**Sensor:** Paraconsistent Integration Sensor (PDL v1.0)
**Run type:** Scheduled autonomous (no human in loop)
**Deliverable priority:** Epistemic trajectory > implementation speed

---

## Chosen AI Problem Space: Formal Verification & Model Checking

**Rationale (epistemic tension selection).** Among the rotation candidates (temporal reasoning, constraint satisfaction, process calculus, formal verification, causal inference, information-theoretic compression, symbolic execution, type theory, program synthesis, planning under uncertainty), **formal verification & model checking** carries the highest epistemic tension with mainstream LLM approaches *today*, for four structural reasons:

1. **Soundness vs. plausibility.** LLMs produce the *most probable* continuation; model checkers produce a *proof or a concrete counterexample*. The two epistemologies are near-orthogonal. This is exactly the gap Hermes needs to close if it is to run deterministic, long-horizon workflows without silent drift.
2. **Counterexample generation is a native "why-it-fails" oracle.** Model checkers do not just say "no" — they emit a minimal trace witnessing the violation. That is a first-class *Symbolic Scar* generator (maps directly to L3.8 Ontological Metabolism in the SCOS stack).
3. **State-space reasoning is the substrate for planning under uncertainty.** MDP/probabilistic model checking (PRISM, Storm) is planning-under-uncertainty with *guarantees* rather than sampled rollouts.
4. **Pre-AI maturity.** This field peaked *before* the LLM era (SPIN won the ACM System Software Award in 2002; SMV/BDDs date to the early 1990s). The substrate is deep, stable, headless, and almost entirely overlooked by agent builders who reach for RAG and tool-calling first. High surprisal, high value.

The problem space also spans the four requested capability vectors cleanly: (1) implementable as subprocess/JSON tools, (2) enables cross-domain-language mutation (a spec language is a *mutation grammar*), (3) encodes human skills engineers overlook (invariant discovery, refinement, counterexample-guided abstraction), and (4) hardens the agent's own execution loops (bounded checking of its own plans before it commits to them).

---

## Preflight Matrix (Non-Obvious Linguistic Connections)

Used to steer discovery away from modern-AI noise and toward the pre-AI substrate.

| Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term |
|---|---|---|---|---|
| model checking | "exhaustive proofreading", "flight-envelope testing" | CLI, headless, JSON trace, subprocess | engine, toolset, checker | LLM |
| temporal logic (LTL/CTL) | "if-this-then-eventually-that rulebook" | property file, `.ltl`, Büchi automaton | model checker, verifier | agent |
| symbolic execution | "exploring every branch of a decision tree by hand" | LLVM bitcode, path constraints, SMT query | engine, symbolic VM | copilot |
| SMT / SAT solving | "constraint arithmetic", "logic puzzle solver" | Python bindings, DIMACS, SMT-LIB2 | solver, prover | RAG |
| bounded model checking | "what breaks within N steps" | goto-program, loop unwinding, C/C++ | model checker | prompt |
| refinement | "does the blueprint match the building" | trace refinement, `refines` clause | checker, toolset | fine-tune |
| relational model finding | "sketch every legal configuration" | SAT backend, `.als`, instance JSON | analyzer, finder | embedding |
| probabilistic model checking | "actuarial risk over a process", "double-entry of probabilities" | MDP, DTMC, JANI, PRISM lang | model checker | neural |
| process algebra / μ-calculus | "choreography of interacting parties", "incident command comms" | `.mcrl2`, LTS, linearisation | toolset, engine | transformer |
| constraint-based animation | "war-gaming a specification" | Prolog interpreter, state animation | animator, solver | vector DB |
| interactive theorem proving | "machine-checked mathematical argument" | tactic script, proof term, OCaml extraction | proof assistant | inference |
| language-independent MC | "universal adapter for verifiers" | PINS matrix, glue code, next-state fn | toolset | GPT |

---

## The 15 Repositories (Full PDL Loop Per Concept)

> Loop discipline per DCCDSchemaGuard: for each repo — observe concept → generate ≥3 mutually exclusive integration hypotheses → pre-register falsification criteria → steelman the falsification → classify CONFIRMED / FALSIFIED / DEFERRED. Loop is not collapsed; no workflow synthesis until after all 15.

---

### 1. `tlaplus/tlaplus` — TLC explicit-state model checker + TLA⁺
**Concept observed.** TLA⁺ specifies systems as state machines with invariants and temporal properties; TLC exhaustively checks finite instances and emits a minimal counterexample trace. Java, headless via `tla2tools.jar`, Java 11+.

**[HYPOTHESIS_MATRIX: 1.** Hermes pre-validates its own generated plans by auto-translating a workflow DAG into a small TLA⁺ spec and running TLC as a subprocess before execution ("plan model-checking"). **2.** Hermes uses TLC purely as a *counterexample factory* — feed a suspected-buggy invariant, harvest the trace, convert to a Symbolic Scar for L3.8. **3.** Hermes embeds TLC as a live runtime monitor, checking every state transition of a long-running task against a temporal property.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if DAG→TLA⁺ translation is not mechanizable without human-level modeling insight (i.e., the abstraction gap requires taste, not rules). **H2:** disproved if TLC cannot be driven headlessly to emit a machine-parseable trace. **H3:** disproved if TLC's checking latency (seconds–minutes on nontrivial specs) exceeds the per-step budget of a live loop.]**

**Falsification probe.** H3 steelman succeeds: TLC does full state-space enumeration; it is a batch tool, not a per-step monitor — runtime coupling violates the IMPLEMENTATION_COST_ANCHOR (JVM startup + enumeration per transition is prohibitive). **H3 FALSIFIED.** H2 steelman fails: TLC emits structured error traces and has a JSON-friendly output path; parseable. **H1 steelman partially fails:** for the *restricted* class of Hermes workflow DAGs (finite tasks, explicit state variables) the translation is a template, not open modeling — [ONTOLOGY_LOCK] the abstraction gap is "human system-design intuition → fixed DAG schema"; because Hermes already emits typed DAGs, the gap is bridged by construction. CONFIRMED with scope limit. [IMPLEMENTATION_COST_ANCHOR: JVM subprocess ~1–3 s startup; acceptable for plan-time, not run-time.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (plan-time only, restricted DAG class); H2 CONFIRMED; H3 FALSIFIED (batch latency).]**

---

### 2. `informalsystems/apalache` (a.k.a. `apalache-mc/apalache`) — Symbolic model checker for TLA⁺ / Quint
**Concept observed.** Translates TLA⁺ into SMT and checks *inductive invariants* and *bounded executions* via Z3. Symbolic, so it sidesteps TLC's state explosion for parameterised systems.

**[HYPOTHESIS_MATRIX: 1.** Hermes uses Apalache's *inductive invariant* checking to prove a loop invariant of a long-horizon task holds for *all* iterations, not just bounded ones. **2.** Hermes swaps Apalache in as a drop-in "harder" backend when TLC's explicit enumeration blows up. **3.** Hermes targets Quint (Apalache's friendlier surface syntax) as the *native* language it emits for self-verification.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if inductive invariant checking requires a human-supplied inductive strengthening that Hermes cannot synthesize. **H2:** disproved if Apalache and TLC accept incompatible spec dialects requiring separate authoring. **H3:** disproved if Quint tooling is not stable/headless enough for automation.]**

**Falsification probe.** H1 steelman succeeds strongly: finding an *inductive* invariant (vs. an ordinary one) is the classic hard step — it typically needs strengthening that is itself a research act. [ONTOLOGY_LOCK] gap = "mathematician's invariant-strengthening intuition → automated candidate generation"; unbridged today. **H1 DEFERRED** (viable only if paired with a candidate-invariant generator — a future run). H2 steelman fails: both consume TLA⁺; Apalache is genuinely a *stronger backend* for the same artifact — [IMPLEMENTATION_COST_ANCHOR] same spec, different engine, marginal cost = one extra subprocess. **H2 CONFIRMED.** H3: Quint has stable CLI + JSON; but committing Hermes' self-model to Quint over TLA⁺ is premature. **H3 DEFERRED.**

**[EPISTEMIC_DELTA: H1 DEFERRED (needs invariant synthesis); H2 CONFIRMED (stronger backend, same artifact); H3 DEFERRED.]**

---

### 3. `mCRL2org/mCRL2` — Process algebra toolset + modal μ-calculus checking
**Concept observed.** Systems as communicating processes; properties in the modal μ-calculus; pipeline of linearisation → state-space generation → μ-calculus check. Boost-licensed, C++, rich CLI toolchain.

**[HYPOTHESIS_MATRIX: 1.** Hermes models *multi-agent orchestration* (L7) as concurrent processes in mCRL2 and checks for deadlock/livelock between sub-agents before dispatch. **2.** Hermes uses μ-calculus properties as a *reusable property library* for "eventually terminates", "no two agents write the same resource". **3.** Hermes uses mCRL2's LTS output as a visualization/introspection substrate for its own workflow graphs.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if agent orchestration cannot be expressed as finite communicating processes (unbounded dynamic spawning breaks it). **H2:** disproved if μ-calculus is too expert-hostile to template. **H3:** disproved if LTS export is not stable/automatable.]**

**Falsification probe.** H1 steelman: dynamic agent spawning *is* unbounded in general — but Hermes' orchestration in practice has a bounded fan-out per plan; for that bounded slice, deadlock checking is exactly what mCRL2 was built for. **H1 CONFIRMED (bounded fan-out).** H2 steelman succeeds: raw μ-calculus is notoriously unreadable; **but** a *fixed, small* library of pre-written formulas (deadlock-freedom, termination) removes the authoring burden entirely — the agent selects, it does not write. **H2 CONFIRMED (curated library only).** [ONTOLOGY_LOCK] gap = "concurrency theorist's μ-calculus fluency → menu of vetted properties". H3: LTS/`.aut` export is stable and scriptable. **H3 CONFIRMED.** [IMPLEMENTATION_COST_ANCHOR: C++ binaries, multi-stage pipeline — heavier than a single call; batch/plan-time only.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (bounded orchestration); H2 CONFIRMED (curated μ-formula library); H3 CONFIRMED.]**

---

### 4. `prismmodelchecker/prism` — Probabilistic model checker (DTMC/CTMC/MDP/PA)
**Concept observed.** Builds and analyses probabilistic models with BDD/MTBDD symbolic engines; answers "probability of reaching a bad state within N steps" and optimal-policy queries over MDPs. Latest 4.10 (Jan 2026).

**[HYPOTHESIS_MATRIX: 1.** Hermes encodes *planning under uncertainty* (retry policies, flaky-tool fallbacks) as an MDP and lets PRISM compute the reward-optimal policy instead of a hand-coded heuristic. **2.** Hermes uses PRISM to bound the *probability of task failure* over a long-horizon workflow and gate execution on a risk threshold. **3.** Hermes uses PRISM's DTMC analysis to model its own token/cost budget as a random walk and predict budget exhaustion.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if transition probabilities cannot be estimated (no data → garbage MDP). **H2:** disproved if the failure model is not Markovian (history-dependent failures break DTMC/MDP assumptions). **H3:** disproved if budget dynamics are deterministic (no randomness → model checker is overkill).]**

**Falsification probe.** H1 steelman: cold-start has no probabilities — **but** Hermes accumulates per-tool success rates across runs (the scheduled-task history *is* the estimator); after warmup the MDP is populated. **H1 CONFIRMED (post-warmup).** H2 steelman succeeds partially: real failures are often correlated/history-dependent, violating Markov memorylessness. [ONTOLOGY_LOCK] gap = "true dependent failure process → memoryless approximation". The approximation is *useful but lossy*; **H2 CONFIRMED as bounded-fidelity approximation** (flag the modeling error explicitly, per ONTOLOGY_LOCK). H3 steelman succeeds: if budget burn is deterministic, use arithmetic, not PRISM. **H3 FALSIFIED** (unless tool latency/cost is itself stochastic — then re-open). [IMPLEMENTATION_COST_ANCHOR: JVM + model build; plan-time policy synthesis, cached.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (post-warmup MDP); H2 CONFIRMED (lossy Markov approx, gap named); H3 FALSIFIED (deterministic budget).]**

---

### 5. `moves-rwth/storm` — Modern probabilistic model checker (+ `stormpy`)
**Concept observed.** Faster, modular probabilistic MC supporting PRISM & JANI, with **Python bindings (`stormpy`)** via PyBind11 — a decisive automation advantage over subprocess-only tools.

**[HYPOTHESIS_MATRIX: 1.** Hermes calls Storm *in-process* through `stormpy`, eliminating subprocess/serialization overhead for probabilistic queries. **2.** Hermes standardizes on **JANI** as a common interchange format so PRISM and Storm are hot-swappable engines. **3.** Hermes uses Storm's fault-tree support to model cascading tool/connector failures.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if `stormpy` is not importable in Hermes' runtime (build/ABI friction). **H2:** disproved if JANI round-trips lose semantics between engines. **H3:** disproved if fault-tree modeling requires domain expertise Hermes lacks.]**

**Falsification probe.** H1 steelman: Storm's native build is heavy (C++ deps) — but `stormpy` is a stable, documented Python API; once installed it removes the JVM-subprocess tax entirely, a genuine [IMPLEMENTATION_COST_ANCHOR] win vs. PRISM (in-process call ≪ subprocess+parse). **H1 CONFIRMED.** H2 steelman fails: JANI is *designed* as an engine-neutral interchange; both Storm and PRISM consume it. **H2 CONFIRMED** — this is the strongest cross-tool integration surface in the whole run (decouples Hermes from any single checker). H3 steelman succeeds: dynamic fault trees need reliability-engineering knowledge to author well. [ONTOLOGY_LOCK] gap = "reliability engineer's failure taxonomy → agent-authored fault tree". **H3 DEFERRED.**

**[EPISTEMIC_DELTA: H1 CONFIRMED (in-process stormpy); H2 CONFIRMED (JANI as neutral IR — keystone); H3 DEFERRED (fault-tree expertise gap).]**

---

### 6. `klee/klee` — Symbolic execution engine (LLVM)
**Concept observed.** Executes a program on *symbolic* inputs, exploring all feasible paths and emitting concrete test inputs per path via SMT constraint solving. UIUC license.

**[HYPOTHESIS_MATRIX: 1.** Hermes uses KLEE to auto-generate high-coverage test inputs for any C/C++ artifact it produces, closing the "did my generated code actually get exercised" gap. **2.** Hermes borrows the *path-constraint* abstraction as a design pattern for its own reasoning: represent an in-progress plan as a set of accumulated symbolic constraints and prune infeasible branches early. **3.** Hermes runs KLEE as a live guardrail during code execution.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if KLEE's LLVM-bitcode requirement makes the toolchain fragile for arbitrary code Hermes emits. **H2:** disproved if "path constraint as plan state" is a metaphor with no computational cash-out. **H3:** disproved if per-run symbolic execution is too slow for a live loop.]**

**Falsification probe.** H1 steelman partly succeeds: KLEE needs code compiled to LLVM bitcode with modeled environment — real friction for arbitrary targets, but *tractable and bounded* for self-contained functions. **H1 CONFIRMED (self-contained C/C++ units).** H2: [ONTOLOGY_LOCK] this maps a *program-analysis* primitive (path constraint) onto an *agent-planning* primitive (partial-plan feasibility). The abstraction gap is real and wide — but it cashes out concretely: Hermes can carry an SMT constraint set alongside a plan and use Z3 (#12) to test feasibility before committing a branch. **H2 CONFIRMED as a design-pattern transfer** (implemented via Z3, not KLEE itself). H3 steelman succeeds: path explosion makes live use infeasible. **H3 FALSIFIED.**

**[EPISTEMIC_DELTA: H1 CONFIRMED (bounded test-gen); H2 CONFIRMED (path-constraint pattern → Z3, gap named); H3 FALSIFIED (path explosion).]**

---

### 7. `AlloyTools/org.alloytools.alloy` — Relational model finder (Kodkod + SAT)
**Concept observed.** Describe structures relationally; Alloy *finds instances* (or shows none exist) within a bounded scope via SAT. Java 17+, runnable jar, usable as an API. Excellent for "show me a configuration that satisfies these constraints."

**[HYPOTHESIS_MATRIX: 1.** Hermes uses Alloy as a *configuration synthesizer* — given declarative constraints on a desired system/data state, get a concrete satisfying instance. **2.** Hermes uses Alloy's bounded "no instance exists" result as a cheap consistency check on a set of requirements before it starts building. **3.** Hermes treats Alloy scopes as a *mutation dial* — enumerate diverse instances to feed the L1.8 Glitch Engine's divergent search.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if relational specs cannot express Hermes' target domains. **H2:** disproved if bounded non-existence gives no useful signal (small scope misses violations). **H3:** disproved if instance enumeration is not diverse/controllable enough to drive mutation.]**

**Falsification probe.** H1 steelman fails for the target use: relational logic is *expressly* general-purpose for structural domains; the Alloy API returns instances as structured objects. **H1 CONFIRMED.** H2 steelman succeeds meaningfully: Alloy's "small scope hypothesis" is heuristic — non-existence within scope N is *not* a proof. **H2 CONFIRMED but epistemically flagged** (report as "no counterexample up to scope N", never "consistent"). H3 is the surprising win: Alloy can enumerate *distinct* instances, and this is a legitimate, *sound* divergent generator for the Glitch Engine — mutations that are guaranteed to satisfy hard constraints while varying freely elsewhere. [ONTOLOGY_LOCK] gap = "designer exploring a design space by hand → bounded SAT enumeration". **H3 CONFIRMED (highest-surprisal hypothesis in run — sound divergence).** [IMPLEMENTATION_COST_ANCHOR: JVM API call, in-process via jar; moderate.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (config synth); H2 CONFIRMED (scoped, flagged); H3 CONFIRMED (sound mutation engine — flagship).]**

---

### 8. `nimble-code/Spin` — Explicit-state LTL model checker (Promela)
**Concept observed.** The canonical concurrency verifier (ACM award 2002). Models processes + channel communication in Promela; checks LTL; famous for finding subtle interleaving bugs.

**[HYPOTHESIS_MATRIX: 1.** Hermes verifies *communication protocols* between itself and connectors/MCPs (message ordering, ack/retry) by modeling them in Promela. **2.** Hermes uses SPIN's LTL checking on its own retry/timeout state machine to catch livelock. **3.** Hermes uses SPIN's generated C verifier (`pan`) as a compiled, reusable runtime monitor.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if connector protocols are too underspecified to model. **H2:** disproved if SPIN and mCRL2 fully overlap (redundant). **H3:** disproved if compiling `pan` per-property is too heavyweight to be reusable.]**

**Falsification probe.** H1 steelman fails: channel-based protocols are SPIN's home turf; connector handshakes (request/ack/retry/timeout) map directly to Promela channels. **H1 CONFIRMED.** H2 steelman succeeds partially — SPIN (LTL, explicit-state) and mCRL2 (μ-calculus, process algebra) overlap in *purpose* but differ in *expressive sweet spot*; keeping both is justified only if Hermes standardizes on one by default. [ONTOLOGY_LOCK not triggered — same domain.] **H2 DEFERRED (pick one default; SPIN for protocol/LTL, mCRL2 for orchestration/μ).** H3: `pan` compiles to a fast standalone checker — reusable if the property is stable; **H3 CONFIRMED (stable properties only).**

**[EPISTEMIC_DELTA: H1 CONFIRMED (protocol verification); H2 DEFERRED (overlap with mCRL2); H3 CONFIRMED (compiled pan for stable props).]**

---

### 9. `diffblue/cbmc` — C Bounded Model Checker (v6.10)
**Concept observed.** Unwinds loops to a bound and hands the resulting formula to an SMT/SAT backend; checks array bounds, pointer safety, assertions. The reference BMC for C/C++.

**[HYPOTHESIS_MATRIX: 1.** Hermes runs CBMC on generated C/C++ to check memory safety and assertions before it ever executes the artifact. **2.** Hermes adopts the *bounded* philosophy for its own plans: "is any failure reachable within N steps?" as a universal, tractable safety gate (vs. unbounded proof). **3.** Hermes uses CBMC's counterexample traces as precise, line-level Symbolic Scars.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if CBMC cannot run headlessly with machine-readable output. **H2:** disproved if "bounded reachability" does not transfer beyond code to plan-level reasoning. **H3:** disproved if traces are not granular enough to localize the fault.]**

**Falsification probe.** H1 steelman fails: CBMC is a mature headless CLI with structured (incl. JSON/XML) trace output. **H1 CONFIRMED.** H2 is the conceptually important one: bounded model checking is a *transferable epistemic stance* — trade completeness for a decidable, cheap, honest answer ("no bug within horizon N"). This maps cleanly onto Hermes' long-horizon planning: check the next N steps exhaustively rather than reason unboundedly. [ONTOLOGY_LOCK] gap = "program loop bound → planning horizon"; narrow and bridgeable. **H2 CONFIRMED (bounded-horizon stance as core loop discipline).** H3: CBMC traces are line/assignment level — highly localizing. **H3 CONFIRMED.** [IMPLEMENTATION_COST_ANCHOR: single subprocess, C/C++ only; cheap relative to KLEE.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (safety gate); H2 CONFIRMED (bounded-horizon stance — core); H3 CONFIRMED (line-level scars).]**

---

### 10. `model-checking/kani` — Kani Rust Verifier (CBMC backend)
**Concept observed.** Bit-precise model checking for Rust: compiles MIR → goto-program → CBMC. Proof harnesses via a `kani` crate; verifies safe *and* unsafe Rust.

**[HYPOTHESIS_MATRIX: 1.** Hermes writes Kani proof harnesses for Rust artifacts to verify panics/overflows are unreachable. **2.** Hermes adopts Kani's *harness* pattern — a small, declarative "here is the property, here are the symbolic inputs" wrapper — as its universal template for invoking any BMC tool. **3.** Hermes uses Kani's MIR→goto pipeline as evidence that *any* typed IR can be lowered into a checkable form, and generalizes to lowering its own DAG IR.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if Kani only supports a Rust subset that excludes Hermes' generated code. **H2:** disproved if the harness pattern does not generalize across tools. **H3:** disproved if DAG→goto lowering is a false analogy (goto-programs assume imperative control flow).]**

**Falsification probe.** H1 steelman: Kani supports a growing but real subset; for self-contained functions it works today. **H1 CONFIRMED (subset).** H2 is strong: the *harness* abstraction (property + symbolic input generators + bound) is exactly the stable input/output contract the SELF_REFLEXIVE_CHECK demands — it recurs across CBMC, Kani, KLEE. **H2 CONFIRMED (universal harness contract).** H3 steelman succeeds: goto-programs presuppose imperative semantics; Hermes' DAG is dataflow, not control-flow. [ONTOLOGY_LOCK] gap = "imperative goto IR → dataflow DAG IR" — genuinely mismatched. **H3 FALSIFIED** (do not lower the DAG to goto; use TLA⁺/mCRL2 for DAG-level checking instead).

**[EPISTEMIC_DELTA: H1 CONFIRMED (Rust subset); H2 CONFIRMED (universal harness contract — key pattern); H3 FALSIFIED (IR mismatch).]**

---

### 11. `utwente-fmt/ltsmin` (orig. `alaarman/ltsmin`) — Language-independent MC toolset (PINS)
**Concept observed.** The **PINS** architecture splits model checking into three decoupled layers — language module ↔ PINS dependency matrix ↔ checking algorithm — so a new language needs only ~200–600 lines of "glue." Connects muCRL, mCRL2, DiVinE, SPIN, UPPAAL, ProB, CADP.

**[HYPOTHESIS_MATRIX: 1.** Hermes adopts the **PINS interface pattern** architecturally: define one neutral "next-state + dependency matrix" contract so any verification backend plugs in behind a single Hermes-side adapter. **2.** Hermes writes a ~300-line PINS language module for *its own* workflow IR, instantly gaining LTSmin's reachability/symbolic/multi-core algorithms for free. **3.** Hermes uses LTSmin as a live multi-core reachability engine on its running state.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if PINS is too C-specific to reimplement as an abstract Hermes interface. **H2:** disproved if Hermes' IR cannot expose a finite next-state function + dependency matrix. **H3:** disproved if LTSmin startup/coupling is too heavy for live use.]**

**Falsification probe.** H1: PINS is a *concept* (three-layer decoupling) independent of its C implementation; adopting it as Hermes' internal verifier-adapter contract is pure architecture and highly valuable — it is the software-engineering answer to "don't marry one checker." **H1 CONFIRMED (adopt PINS as adapter contract — architectural keystone alongside JANI).** H2 steelman: exposing a next-state function requires Hermes' state to be a fixed-width integer vector; its DAG state *can* be projected onto such a vector for the bounded slice. [ONTOLOGY_LOCK] gap = "arbitrary agent state → fixed integer vector"; bridgeable with a projection but lossy. **H2 CONFIRMED (with declared projection/abstraction step).** H3 steelman succeeds: batch tool. **H3 FALSIFIED.**

**[EPISTEMIC_DELTA: H1 CONFIRMED (PINS adapter contract — architecture keystone); H2 CONFIRMED (via lossy state projection); H3 FALSIFIED (batch only).]**

---

### 12. `Z3Prover/z3` — SMT solver (MIT, first-class Python bindings)
**Concept observed.** Decides satisfiability modulo theories (arithmetic, bit-vectors, arrays, datatypes, quantifiers). MIT-licensed, mature Python API — the connective tissue under Apalache, CBMC, KLEE, and countless tools.

**[HYPOTHESIS_MATRIX: 1.** Hermes uses `z3-solver` *directly, in-process* to check feasibility of a set of accumulated plan constraints (the path-constraint pattern from #6) before committing a branch. **2.** Hermes uses Z3's `Optimize` to solve small scheduling/resource-allocation subproblems inside a workflow (constraint satisfaction as a native tool). **3.** Hermes uses Z3 as the *shared backend* so all higher-level checkers reduce to one solver it already controls.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if plan constraints cannot be encoded in SMT theories. **H2:** disproved if realistic scheduling problems exceed Z3's tractable size. **H3:** disproved if bundling a shared Z3 causes version conflicts across tools.]**

**Falsification probe.** H1 steelman fails: linear/integer/boolean/bit-vector constraints cover the overwhelming majority of plan-feasibility and resource questions; the Python API returns models/`unsat` cleanly. **H1 CONFIRMED (lowest-friction, highest-leverage integration in the run — pure library, MIT, no subprocess).** H2 steelman succeeds only at scale: NP-hard problems blow up eventually, but agent-sized scheduling (tens–hundreds of vars) is squarely tractable. **H2 CONFIRMED (bounded size).** H3: shared-backend version pinning is a real but ordinary packaging concern. [IMPLEMENTATION_COST_ANCHOR: `pip install z3-solver`, in-process, microsecond–second solves — the cheapest tool here.] **H3 CONFIRMED (with dependency pinning).**

**[EPISTEMIC_DELTA: H1 CONFIRMED (in-process feasibility — anchor tool); H2 CONFIRMED (agent-scale CSP); H3 CONFIRMED (pin versions).]**

---

### 13. `rocq-prover/rocq` (formerly `coq/coq`) — Rocq/Coq interactive theorem prover
**Concept observed.** Dependently-typed proof assistant; machine-checked proofs; tactic language; OCaml extraction of verified programs. The gold standard for *proof*, not just *checking*.

**[HYPOTHESIS_MATRIX: 1.** Hermes generates Rocq proof obligations for critical invariants and discharges them for total correctness. **2.** Hermes uses Rocq's *extraction* to obtain correct-by-construction executable code from a verified spec. **3.** Hermes uses Rocq as a live proof-search loop inside planning.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if interactive proof requires human tactic guidance that Hermes cannot automate. **H2:** disproved if extraction demands a fully-formalized spec that is itself the hard part. **H3:** disproved if proof search is unbounded/undecidable for live use.]**

**Falsification probe.** H1 steelman succeeds decisively: interactive theorem proving is *interactive* precisely because full automation is undecidable; tactic authoring is expert human labor. [ONTOLOGY_LOCK] gap = "proof engineer's tactical creativity → automated tactic synthesis" — the widest gap in the run. **H1 DEFERRED.** H2 inherits the same problem (the formal spec is the bottleneck). **H2 DEFERRED.** H3 steelman succeeds: undecidable, unbounded. **H3 FALSIFIED.** Rocq is the correct *aspirational* boundary marker — it defines what Hermes cannot yet do autonomously, which is itself valuable epistemic information (do not over-reach into full ITP this cycle).

**[EPISTEMIC_DELTA: H1 DEFERRED (tactic automation gap); H2 DEFERRED (spec bottleneck); H3 FALSIFIED (undecidable live search).]**

---

### 14. `why3` (Inria — `gitlab.inria.fr/why3/why3`; GitHub mirrors incl. `AdaCore/why3`) — Deductive verification platform (WhyML)
**Concept observed.** WhyML specification/programming language + a *dispatcher* that sends verification conditions to *many* back-end provers (Z3, CVC, Alt-Ergo, Coq…). Also the IR behind SPARK/Ada, C, and Java verification.

**[HYPOTHESIS_MATRIX: 1.** Hermes uses Why3 as a **prover-multiplexer** — emit one set of verification conditions, fan out to whichever backend closes them, harvesting the "portfolio" effect. **2.** Hermes uses WhyML as an intermediate verification language so it never binds to a single prover's syntax. **3.** Hermes uses Why3's extraction to OCaml for correct-by-construction utility code.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if the multiplexer needs manual per-prover tuning to be useful. **H2:** disproved if WhyML overlaps JANI/PINS with no added value. **H3:** disproved if extraction requires full manual proof (same as Rocq).]**

**Falsification probe.** H1: the portfolio/dispatch idea is the *point* of Why3 and largely automated — many VCs close without human help via the strongest-of-N provers. This is a genuinely valuable *pattern* (portfolio solving) even if Hermes reimplements it lightly over Z3/CVC5. **H1 CONFIRMED as a pattern (portfolio dispatch).** H2 steelman succeeds: WhyML operates at the *proof/VC* layer, whereas JANI/PINS operate at the *model-checking* layer — different altitudes, but Why3's value (portfolio dispatch) is orthogonal and reusable without adopting WhyML wholesale. **H2 CONFIRMED (adopt dispatch pattern, not the language).** H3 steelman succeeds for full functional correctness → **H3 DEFERRED.** [IMPLEMENTATION_COST_ANCHOR: adopting the *pattern* over Z3+CVC5 is cheap; adopting the *full platform* is heavy — take the pattern.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (portfolio-dispatch pattern); H2 CONFIRMED (pattern > platform); H3 DEFERRED (extraction needs proof).]**

---

### 15. `hhu-stups/prob2_ui` (+ core ProB) — Constraint-based animator & model checker for B / Event-B / TLA⁺ / Z / CSP
**Concept observed.** ProB *animates* specifications and does **constraint-based** checking, model finding, and test-case generation via a Prolog interpreter of each formalism's operational semantics. Uniquely blends model checking with constraint solving and *interactive animation*.

**[HYPOTHESIS_MATRIX: 1.** Hermes uses ProB's **animation** to "dry-run" a specification step-by-step, harvesting reachable states as a *guided exploration* signal (between random rollout and exhaustive check). **2.** Hermes uses ProB's constraint-based *test-case generation* to synthesize edge-case inputs for its workflows. **3.** Hermes uses ProB's multi-formalism front-end (it already reads TLA⁺) as a *single adapter* covering several spec languages at once.]**

**[FALSIFICATION_CRITERIA: H1:** disproved if animation requires interactive human step-selection with no headless driver. **H2:** disproved if constraint-based test-gen cannot be scripted. **H3:** disproved if the multi-formalism support is shallow/unstable outside its native B.]**

**Falsification probe.** H1 steelman: the UI is interactive, **but** ProB has a documented headless/CLI + programmatic (Prolog/`probcli`) interface — animation *can* be driven automatically. **H1 CONFIRMED (via probcli).** [ONTOLOGY_LOCK] gap = "human war-gaming a spec → scripted guided state exploration"; bridgeable. H2 steelman fails: constraint-based test-case generation is a first-class, scriptable ProB feature. **H2 CONFIRMED.** H3 steelman succeeds partially: non-B formalisms are supported but with varying maturity; relying on ProB as the *sole* TLA⁺ path is riskier than using TLC/Apalache directly. **H3 DEFERRED (use ProB for B/Event-B/constraint-animation; keep TLC/Apalache for TLA⁺).** [IMPLEMENTATION_COST_ANCHOR: probcli subprocess; moderate.]

**[EPISTEMIC_DELTA: H1 CONFIRMED (headless animation via probcli); H2 CONFIRMED (scriptable test-gen); H3 DEFERRED (multi-formalism maturity varies).]**

---

## SELF_REFLEXIVE_CHECK (applied across all CONFIRMED hypotheses)

- **Representable in the agent's state space?** Yes for the bounded slice: Hermes' workflow IR projects to finite state vectors (LTSmin/PINS H2) and typed DAGs (TLC H1). Full unbounded agent state is *not* representable — hence all live-monitor hypotheses were FALSIFIED.
- **Input/output stable enough for automation?** Strongest for library-native tools: **Z3 (`z3-solver`)**, **Storm (`stormpy`)**, **Alloy (jar API)** — no fragile text parsing. Subprocess tools (TLC, CBMC, mCRL2, SPIN, probcli) have stable, machine-readable trace formats. **JANI** and **PINS** give format/interface stability across engines.
- **Benefit > subprocess/compile/translation cost?** Yes for plan-time/batch use; **No** for per-step live use (JVM/enumeration/path-explosion) — consistently FALSIFIED. Prefer in-process (Z3, stormpy) where latency matters.
- **Survives runtime environmental change?** The *patterns* (bounded-horizon stance, harness contract, portfolio dispatch, PINS adapter, JANI IR, sound Alloy mutation) survive environment change; specific tool binaries are swappable behind those patterns — which is the entire point of adopting the abstractions rather than the tools.

---

## [HARNESS_HERMES]

CONFIRMED integrations, grouped by the abstraction they contribute to Hermes (tools are interchangeable behind each abstraction):

1. **In-process feasibility & CSP core — Z3 (`z3-solver`, #12).** The anchor. Every plan carries an SMT constraint set; branches are tested for `sat` before commitment. Also solves agent-scale scheduling/allocation. MIT, pure library, cheapest possible cost.
2. **Bounded-horizon safety stance — CBMC (#9) + Kani harness contract (#10).** Universal discipline: exhaustively check the next N steps rather than reason unboundedly. Line-level counterexamples become Symbolic Scars (L3.8). The *harness contract* (property + symbolic inputs + bound) is the uniform way Hermes invokes any checker.
3. **Neutral model-checking IR & adapter — JANI (Storm/PRISM, #5/#4) + PINS (LTSmin, #11).** Hermes never marries one checker: it emits JANI for probabilistic queries and exposes a PINS-style next-state/dependency contract so backends hot-swap behind one adapter.
4. **Probabilistic planning under uncertainty — Storm/`stormpy` (#5) + PRISM (#4).** Post-warmup MDPs (populated from scheduled-run history) yield reward-optimal retry/fallback policies and failure-probability bounds — with the Markov approximation error explicitly flagged.
5. **Plan-level temporal/concurrency checking — TLC (#1, restricted DAG class), Apalache (#2, stronger backend), mCRL2 (#3, bounded orchestration + curated μ-formula library), SPIN (#8, connector-protocol LTL).** Hermes model-checks its own DAGs and connector handshakes at plan time.
6. **Sound divergent generation — Alloy (#7).** Flagship surprisal: bounded SAT instance enumeration is a *sound* mutation engine for the L1.8 Glitch Engine — divergent candidates guaranteed to satisfy hard constraints. (Report "no counterexample up to scope N," never "consistent.")
7. **Portfolio dispatch pattern — Why3 (#14).** Fan one VC set out to strongest-of-N provers (Z3, CVC5) and take the first close.
8. **Scriptable guided exploration & test-gen — ProB `probcli` (#15).** Constraint-based animation as a middle path between random rollout and exhaustive check; constraint-based edge-case test generation.

**DEFERRED (re-open in future runs, gap named):** inductive-invariant synthesis (Apalache H1), fault-tree authoring (Storm H3), full interactive theorem proving & extraction (Rocq #13, Why3 H3), single-tool multi-formalism reliance (ProB H3), SPIN-vs-mCRL2 default selection (H2). **FALSIFIED (do not pursue):** any live per-step model-checking monitor; lowering the dataflow DAG to imperative goto-programs (Kani H3).

---

## [IMPLEMENTATION_WORKFLOW]

Phased, using **only CONFIRMED** hypotheses. Each phase is independently shippable and ordered by cost-to-value.

**Phase 0 — Anchor (lowest cost, highest leverage).**
Vendor `z3-solver` in-process. Add a `PlanConstraintSet` object to Hermes' planner; test branch feasibility with Z3 before commit; expose a `solve_schedule()` helper for small CSP/allocation subproblems. No subprocess, no parsing. (From #12.)

**Phase 1 — Bounded-horizon safety gate + harness contract.**
Define one `VerificationHarness` interface (property + symbolic-input generators + bound) — the Kani/CBMC contract (#10/#9). Wire CBMC as the first backend for any C/C++ artifact Hermes emits; convert counterexample traces into structured Symbolic Scars (L3.8). Adopt "check next N steps" as the default planning discipline.

**Phase 2 — Neutral IR & swappable backends.**
Introduce **JANI** as Hermes' probabilistic-model interchange and a **PINS-style adapter** (next-state fn + dependency matrix, via a declared lossy state projection) as the single seam behind which all checkers plug in (#5/#11). This is the architectural insurance that makes every later tool hot-swappable.

**Phase 3 — Probabilistic planning under uncertainty.**
Install `stormpy` (in-process). Populate MDPs from accumulated scheduled-run success/latency history; compute reward-optimal retry/fallback policies and per-workflow failure-probability bounds; gate execution on a risk threshold. Explicitly log the Markov-approximation error each time (ONTOLOGY_LOCK compliance). PRISM as an alternate JANI backend. (#5/#4.)

**Phase 4 — Plan- and protocol-level temporal checking.**
Template DAG → TLA⁺ for TLC (#1); use Apalache as the stronger backend on the same specs (#2). Model connector handshakes in Promela for SPIN LTL checks (#8). Model bounded multi-agent orchestration in mCRL2 with a *curated* μ-calculus property library for deadlock/livelock/termination (#3).

**Phase 5 — Sound divergence & guided exploration (discovery amplifiers).**
Integrate the Alloy jar API as a *sound mutation generator* feeding the L1.8 Glitch Engine — enumerate distinct constraint-satisfying instances for divergent search (#7, flagship). Add ProB `probcli` for scriptable guided animation and constraint-based edge-case test generation (#15). Add a lightweight **portfolio-dispatch** layer (Why3 pattern) fanning VCs across Z3 + CVC5 (#14).

**Standing rule (all phases).** Everything runs at **plan-time / batch**, never as a per-step live monitor (all live-monitor hypotheses were FALSIFIED on latency). Tools sit behind the Phase-2 abstractions so any single binary can be replaced without touching Hermes' core.

---

## Run Provenance / Sources

- TLA⁺ / TLC — [github.com/tlaplus/tlaplus](https://github.com/tlaplus/tlaplus)
- Apalache — [github.com/informalsystems/apalache](https://github.com/informalsystems/apalache)
- mCRL2 — [github.com/mCRL2org/mCRL2](https://github.com/mCRL2org/mCRL2)
- PRISM — [github.com/prismmodelchecker/prism](https://github.com/prismmodelchecker/prism)
- Storm / stormpy — [github.com/moves-rwth/storm](https://github.com/moves-rwth/storm) · [github.com/moves-rwth/stormpy](https://github.com/moves-rwth/stormpy)
- KLEE — [github.com/klee/klee](https://github.com/klee/klee)
- Alloy — [github.com/AlloyTools/org.alloytools.alloy](https://github.com/AlloyTools/org.alloytools.alloy)
- SPIN — [github.com/nimble-code/Spin](https://github.com/nimble-code/Spin)
- CBMC — [github.com/diffblue/cbmc](https://github.com/diffblue/cbmc)
- Kani — [github.com/model-checking/kani](https://github.com/model-checking/kani)
- LTSmin — [github.com/utwente-fmt/ltsmin](https://github.com/utwente-fmt/ltsmin) (orig. [github.com/alaarman/ltsmin](https://github.com/alaarman/ltsmin))
- Z3 — [github.com/Z3Prover/z3](https://github.com/Z3Prover/z3)
- Rocq / Coq — [github.com/rocq-prover/rocq](https://github.com/rocq-prover/rocq)
- Why3 — [gitlab.inria.fr/why3/why3](https://gitlab.inria.fr/why3/why3) · mirror [github.com/AdaCore/why3](https://github.com/AdaCore/why3)
- ProB — [github.com/hhu-stups/prob2_ui](https://github.com/hhu-stups/prob2_ui)

*Autonomous run — modeling choices made without human input: problem space selected on epistemic-tension criterion; Why3 counted via its GitHub mirror since canonical hosting is Inria GitLab; LTSmin attributed to the maintained `utwente-fmt` fork.*
