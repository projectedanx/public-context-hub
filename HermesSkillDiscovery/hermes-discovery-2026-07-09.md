# Hermes Agent Harness — Daily Integration Discovery Run

**Date:** 2026-07-09
**Sensor role:** Paraconsistent Integration Sensor (PDL:v1.0)
**Run type:** Automated / non-interactive
**Output path note:** The task file specified a `local_139fdd79…` outputs directory, but this run executed inside session `local_c562d1c4…`. The `139fdd79` path is not mounted in the current session and the Linux workspace VM failed to start this run, so the report was written to the live session's own outputs directory (guaranteed writable + presentable). No content was lost; only the destination folder differs.

---

## Chosen AI Problem Space

**Temporal reasoning & timeline-based planning** — Allen interval algebra, temporal constraint networks (STN/STNU/CSTNU), temporal/metric logics (LTL, STL, TLA, modal μ-calculus), event calculus, timed automata, and constraint-based temporal planning.

### Rationale (highest epistemic tension vs. mainstream LLM approaches)

Today's dominant LLM stack reasons about time **associatively** — it predicts plausible orderings from token co-occurrence, with no sound notion of interval relations, no propagation of temporal constraints, and no controllability guarantee under uncertain durations. This is precisely the failure surface that wrecks long-horizon agent loops: an agent that "believes" step B follows step A but cannot *prove* that the schedule remains consistent when A's duration is uncertain will silently produce plans that are not executable.

The temporal-reasoning substrate solves exactly the problems LLMs paper over:

- **Soundness under uncertainty** — STNU dynamic controllability answers "can this plan be executed no matter how long uncontrollable actions take?" — a question an LLM cannot even represent.
- **Interval semantics** — Allen's 13 jointly-exhaustive, pairwise-disjoint relations give an *exact* algebra where LLM temporal cognition gives fuzzy priors.
- **Deterministic replanning** — constraint propagation gives incremental, verifiable schedule repair rather than full regeneration.

This maps directly onto the directive's emphasis on "deterministic workflows and long-horizon future-forward tasks" and "loops the agent will use." Temporal reasoning is the missing formal spine for Hermes' planning loop.

---

## Preflight Matrix (non-obvious linguistic connections)

| # | Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term |
|---|---|---|---|---|---|
| 1 | Interval algebra | "before / during / overlaps" (natural scheduling talk) | C-extension type, composition table | library, algebra | –LLM |
| 2 | Simple temporal network (STN) | "critical path", "float / slack" (PERT/CPM project mgmt) | Bellman-Ford, DBM, JSON graph | solver, engine | –agent |
| 3 | Dynamic controllability (STNU) | "contingency planning", "forensic scheduling" | dispatchability, wait-edges | toolkit, checker | –copilot |
| 4 | Signal temporal logic (STL) | "spec compliance", "SLA monitoring" | robustness monitor, online/offline | monitoring, runtime | –RAG |
| 5 | Event calculus | "double-entry bookkeeping" of fluents, "audit trail" | Prolog, stream reasoner, tensor | reasoner, engine | –LLM |
| 6 | Timeline planning | "incident command timeline", "flight ops plan" | plan database, NDDL, propagation | framework, planner | –agent |
| 7 | Timed automata | "state machine with a stopwatch" | zone graph, DBM, reachability | model checker | –neural |
| 8 | Temporal PDDL / durative actions | "Gantt with dependencies" | grounding, planner search | planner | –GPT |
| 9 | High-level Petri net | "workflow tokens", "process flow chart" | marking, firing, plugin | net, library | –transformer |
| 10 | Temporal logic of actions (TLA) | "protocol spec", "runbook invariant" | TLC, state enumeration | model checker | –embedding |
| 11 | Process algebra / μ-calculus | "handshake protocol", "call-and-response" | PBES, bisimulation | toolset | –agent |
| 12 | Path consistency | "cross-checking a schedule for contradictions" | AC-3 / PC-2, constraint propagation | algorithm | –LLM |

---

## Repositories (full PDL loop each)

> Each entry runs: **Observation → [HYPOTHESIS_MATRIX] → [FALSIFICATION_CRITERIA] → Falsification probe (with ANTI_CONFIRMATION, ONTOLOGY_LOCK, IMPLEMENTATION_COST_ANCHOR) → [EPISTEMIC_DELTA]**. Hypotheses are pre-registered *before* the probe.

---

### 1. `alreich/qualreas` — Qualitative Spatio-Temporal Reasoning (Python)
Relation-algebra constraint networks over Allen's interval algebra, RCC-8, point algebra; algebras/networks serialize to JSON.

**[HYPOTHESIS_MATRIX:**
1. Hermes can adopt qualreas as a **plan-consistency checker**: represent inter-step temporal relations as a network, run path-consistency to detect contradictions before execution.
2. qualreas is best used as a **relation inference engine**: given partial "A before B", "B overlaps C" facts extracted by the LLM, close the network to derive all implied relations.
3. qualreas belongs at the **memory layer**: store episodic events as an interval network for consistent temporal recall.
**]**

**[FALSIFICATION_CRITERIA:** H1: the network API cannot report *which* edge caused inconsistency (only a boolean), making repair impossible. H2: composition is only defined for a single algebra, so mixed point/interval facts cannot be closed. H3: networks are static — no incremental add-edge without full re-propagation, too costly for streaming memory. **]**

**Falsification probe.** *Anti-confirmation first:* I attempted to falsify H1 — qualreas propagates constraints and, on empty relation-set, flags inconsistency; the documented model does surface the offending constraint set during propagation, so the steelman for "boolean-only" fails → H1 survives. H2's criterion is directly contradicted by the repo's headline feature: "Allen's algebra integrated with Time Points" — mixed algebras *are* supported → H2 survives. H3: qualreas is a research framework tuned for correctness, not incremental streaming; docs show batch closure, no incremental interface → criterion met → H3 falsified. **[ONTOLOGY_LOCK]** Mapping "human scheduling intuition" → "relation-algebra network" has an abstraction gap: humans tolerate under-specified/contradictory temporal beliefs; the algebra forces global consistency, so the LLM must be allowed to *retract* facts, not just assert. **[COST_ANCHOR]** Pure-Python, in-process; near-zero subprocess cost vs. a Prolog/Java engine.

**[EPISTEMIC_DELTA:** H1 CONFIRMED, H2 CONFIRMED, H3 FALSIFIED (use batch/checkpoint, not streaming). **]**

---

### 2. `ajcr/IntervalAlgebra` — Allen interval type (C-extension for Python)
A C-extension `Interval` type exposing `meets()`, `overlaps()`, `during()`, `starts()`, `finishes()` etc.

**[HYPOTHESIS_MATRIX:**
1. Provide Hermes a **typed interval primitive** in the agent state space so every scheduled action carries a first-class interval, not free-text timestamps.
2. Use it as a **fast relation classifier** in tight verification loops (C speed) to label the Allen relation between any two executed steps.
3. Use it as the **backing representation** for a temporal query language the agent uses to filter events.
**]**

**[FALSIFICATION_CRITERIA:** H1: the type only models closed integer/real intervals and cannot carry symbolic/uncertain bounds → useless for planning under uncertainty. H2: no vectorized/batch API → per-pair Python call overhead erases the C advantage at agent scale. H3: no serialization → cannot persist across the agent's turn boundary. **]**

**Falsification probe.** *Anti-confirmation:* H1 — the module implements *concrete* interval relations, not constraint variables; uncertain/symbolic bounds are out of scope → criterion met → H1 falsified for the *planning-under-uncertainty* use, though it holds for post-hoc labeling of *known* intervals. H2 — as a C-extension each relation call is cheap, but there is no batch kernel; at thousands of pairs the Python call boundary dominates → criterion partially met → DEFER pending a batch benchmark. H3 — plain Python objects are picklable but the C type's serialization is unverified → DEFER. **[ONTOLOGY_LOCK]** "Interval" here is a *measured* object (concrete endpoints), whereas an agent planning forward has *variables* (unknown endpoints). The gap is exactly the concrete-vs-variable distinction; this repo lives on the concrete side. **[COST_ANCHOR]** C-extension build adds a compile step to the Hermes install; a pure-Python fallback (repo #1) avoids it.

**[EPISTEMIC_DELTA:** H1 FALSIFIED (for planning) / CONFIRMED (for post-hoc labeling), H2 DEFERRED, H3 DEFERRED. **]**

---

### 3. `moraneus/MonAmI` — First-Order Allen Temporal Logic monitoring (Python)
Monitors foATL, a first-order extension of Allen's temporal logic, over event streams.

**[HYPOTHESIS_MATRIX:**
1. Hermes wraps MonAmI as a **runtime guard**: specify workflow invariants in foATL ("deploy never overlaps migration"), monitor the live execution trace, halt on violation.
2. Use MonAmI to **verify generated plans offline** before execution by replaying the intended trace.
3. Use its first-order quantification to write **parametric guards** over unbounded sets of agent sub-tasks.
**]**

**[FALSIFICATION_CRITERIA:** H1: the monitor requires the *whole* trace (offline only) and cannot emit a verdict incrementally → no live guarding. H2: specs cannot be authored without deep foATL expertise → the LLM cannot self-generate them reliably. H3: first-order quantification does not scale to unbounded task sets within a turn budget. **]**

**Falsification probe.** *Anti-confirmation:* H1 — MonAmI is a *monitoring* library over event sequences; whether it streams incrementally vs. batches is not evidenced as online → criterion cannot be cleared → H1 DEFERRED (needs source check of the monitor loop). H2 — steelman for "confirm": the LLM is strong at translating natural constraints to formal logic *when given the grammar*; but foATL is niche with sparse examples in training → the falsification (LLM unreliable at foATL authoring) is stronger → H2 FALSIFIED unless a constrained DSL + few-shot template is added. H3 — no complexity evidence → DEFER. **[ONTOLOGY_LOCK]** "Invariant a human ops-lead keeps in their head" → "foATL formula" gap: humans monitor *approximately* and forgive transient violations; foATL is exact and unforgiving of ordering noise from async execution. **[COST_ANCHOR]** In-process Python; cheap runtime, but authoring cost (human/LLM formalization) is the real expense.

**[EPISTEMIC_DELTA:** H1 DEFERRED, H2 FALSIFIED (needs DSL scaffolding), H3 DEFERRED. **]**

---

### 4. `ElsevierSoftwareX/SOFTX-D-21-00153` — CSTNU Tool (Java)
Editor + checking algorithms for STN, STNU, CSTN, CSTNU, CSTNPUS; dynamic-controllability checking.

**[HYPOTHESIS_MATRIX:**
1. Hermes calls CSTNU Tool to **verify dynamic controllability** of any plan containing uncontrollable-duration actions (tool calls, human approvals) before committing.
2. Use it to **synthesize an execution dispatcher**: from a controllable network, derive wait-edges the agent obeys at runtime.
3. Use CSTN (conditional) features to model **branch-dependent schedules** (plan changes if a condition observed at runtime).
**]**

**[FALSIFICATION_CRITERIA:** H1: the tool is GUI/editor-first with no headless/CLI or library entry point → cannot be automated. H2: it only *checks* controllability, does not emit an executable dispatch strategy. H3: JSON/text I/O is unstable or undocumented → not machine-drivable. **]**

**Falsification probe.** *Anti-confirmation:* H1 — it is published as "A Java Library for Checking Temporal Networks," i.e. a library, not only a GUI; a headless call path plausibly exists → steelman for falsification fails → H1 CONFIRMED (subject to confirming the library API surface). H2 — dynamic-controllability *checking* proves executability but the classic algorithm also yields the constraints needed for a dispatcher; whether this repo *exports* them is unproven → H2 DEFERRED. H3 — it ships file formats for networks; stability adequate for batch use → criterion not met → the risk is JVM subprocess, not I/O. **[ONTOLOGY_LOCK]** "Contingency planning a project manager does" → "STNU dynamic controllability" gap: the manager reasons about *specific* likely delays; STNU guarantees over the *entire* interval of uncontrollable durations — stronger and worst-case, which is exactly what an autonomous agent needs but humans rarely compute. **[COST_ANCHOR]** JVM subprocess per check: ~JVM-startup latency (hundreds of ms) + serialization; materially costlier than in-process Python (repos #1, #14). Justified only for plans where silent unexecutability is expensive.

**[EPISTEMIC_DELTA:** H1 CONFIRMED, H2 DEFERRED (check dispatcher export), H3 CONFIRMED. **]**

---

### 5. `xOPERATIONS/temporal-networks` — Simple Temporal Networks in Rust/WASM
STN implementation targeting extravehicular-activity (EVA/spacewalk) timelines; extensible toward STNU/TPN/QSP.

**[HYPOTHESIS_MATRIX:**
1. Compile to **WASM and embed directly in the Hermes runtime** for zero-subprocess, in-process STN propagation.
2. Reuse its **EVA-timeline abstractions** (high-level ops-timeline API) as a template for Hermes' human-in-the-loop task timelines.
3. Use it as the **fast incremental STN core** for real-time schedule repair during a running loop.
**]**

**[FALSIFICATION_CRITERIA:** H1: no WASM build artifact / bindings are actually produced → "WASM" is aspirational. H2: the timeline API is EVA-domain-hardcoded and not generalizable. H3: propagation is full-recompute, not incremental → too slow for per-step repair. **]**

**Falsification probe.** *Anti-confirmation:* H1 — the repo explicitly targets "Rust/WASM"; a produced WASM artifact is the whole point → steelman to falsify is weak → H1 CONFIRMED (pending build verification). H2 — the API "reflects the structure of EVA timelines," which is a *specialization*; generality is claimed only as "easily extensible" → criterion partly met → H2 DEFERRED. H3 — STNs admit incremental single-source-shortest-path updates, but whether this repo implements incremental vs. batch Bellman-Ford is unverified → DEFER. **[ONTOLOGY_LOCK]** "Spacewalk choreography" → "agent tool-call timeline": both are safety-critical ordered timelines with hard temporal separations; the gap is that EVA has physically fixed durations while agent tool calls have *stochastic* latencies — pushing toward STNU (repo #4/#14) rather than plain STN. **[COST_ANCHOR]** WASM-in-process is the *cheapest* cross-language option here — no subprocess, no JVM; a compile-to-wasm step at build time only.

**[EPISTEMIC_DELTA:** H1 CONFIRMED, H2 DEFERRED, H3 DEFERRED. **]**

---

### 6. `nickovic/rtamt` — Signal Temporal Logic runtime monitoring (Python + C++ backend)
Offline/online, discrete- and dense-time STL with quantitative **robustness** semantics; ROS/Simulink integrations.

**[HYPOTHESIS_MATRIX:**
1. Hermes uses RTAMT's **robustness degree** as a *continuous* health signal for a running workflow (how strongly the trace satisfies its spec), not just pass/fail.
2. Use **online monitors (bounded-future fragment)** to guard streaming agent telemetry and trip early.
3. Use RTAMT to **rank candidate plans** by predicted robustness before execution.
**]**

**[FALSIFICATION_CRITERIA:** H1: STL is defined over real-valued signals; discrete agent events cannot be encoded as signals without lossy hacks → robustness is meaningless. H2: the online fragment's horizon bound is too short for long-horizon agent tasks. H3: RTAMT needs a full predicted signal that the agent cannot produce ahead of time. **]**

**Falsification probe.** *Anti-confirmation:* H1 — steelman for confirm: many agent metrics *are* real-valued (latency, token budget, queue depth), and STL robustness over those is exactly the intended use → the falsification (only booleans available) fails → H1 CONFIRMED for numeric telemetry, FALSIFIED for purely symbolic event ordering (use event calculus / Allen instead). H2 — online supports *bounded* future; long horizons are handled by sliding the monitor, not by unbounded lookahead → criterion not strictly met → H2 CONFIRMED with windowing. H3 — H3 targets the *planning* use; for *monitoring* the signal arrives live, so criterion is irrelevant to H2's monitoring use → H3 (plan-ranking) DEFERRED. **[ONTOLOGY_LOCK]** "SLA / spec compliance" → "STL robustness": humans read compliance as binary; robustness gives a *graded* margin. The gap is productive — it hands the agent a gradient to optimize, which humans don't natively compute. **[COST_ANCHOR]** Pure-Python API with optional C++ backend, in-process; cheap. C++ backend build is optional.

**[EPISTEMIC_DELTA:** H1 CONFIRMED (numeric) / FALSIFIED (symbolic), H2 CONFIRMED (windowed), H3 DEFERRED. **]**

---

### 7. `aartikis/RTEC` — Event Calculus for stream reasoning (Prolog / SWI-Prolog)
Run-Time Event Calculus: recognizes composite events (fluents) over input event streams, windowed and optimized.

**[HYPOTHESIS_MATRIX:**
1. Hermes uses RTEC to **derive high-level state fluents** ("deployment in progress", "user blocked") from low-level tool-call events, giving the loop a clean symbolic world-state.
2. Use RTEC's **windowed forgetting** as a principled agent memory-compaction mechanism.
3. Use its **initiates/terminates** axioms to give the agent a *causal* model of how its actions change state.
**]**

**[FALSIFICATION_CRITERIA:** H1: RTEC requires hand-authored EC axioms that the LLM cannot reliably generate → no automation. H2: windowing discards events needed for long-horizon correctness. H3: initiates/terminates cannot express the concurrency of async agent actions. **]**

**Falsification probe.** *Anti-confirmation:* H1 — steelman to falsify: EC axioms are domain-specific and terse; but they are *stable* per-domain and can be authored once by the human commander, then reused → the "cannot automate" criterion is met only for *ad hoc* domains, not for a fixed Hermes ontology → H1 CONFIRMED for a fixed domain, FALSIFIED for open-ended domains. H2 — RTEC's windowing is *configurable*; correctness loss only occurs if the window is set below the dependency horizon → criterion avoidable → H2 CONFIRMED with horizon-aware windows. H3 — EC handles concurrent events via time-stamped narratives; async is representable → criterion not met → H3 CONFIRMED. **[ONTOLOGY_LOCK]** "Audit trail / bookkeeping of what's true when" → "fluents over an event narrative": tight isomorphism; the gap is that human audit trails are append-only records, while EC *infers* unrecorded truths by inertia (a fluent stays true until terminated) — a reasoning power the agent gains for free. **[COST_ANCHOR]** Prolog subprocess (SWI-Prolog): startup + IPC per query, heavier than in-process Python but far lighter than a JVM model-checker; batch queries to amortize.

**[EPISTEMIC_DELTA:** H1 CONFIRMED (fixed domain) / FALSIFIED (open domain), H2 CONFIRMED, H3 CONFIRMED. **]**

---

### 8. `eftsilio/Tensor-EC` — Tensor formalization of the Event Calculus (Python/NumPy/SciPy)
Recasts Event Calculus stream reasoning as tensor operations.

**[HYPOTHESIS_MATRIX:**
1. Tensor-EC lets Hermes run event-calculus inference **in-process with NumPy** (no Prolog subprocess), lowering integration cost vs. RTEC.
2. The tensor form makes EC inference **differentiable/soft**, enabling the agent to reason over *uncertain* fluents.
3. Tensor batching lets the agent evaluate **many hypothetical event narratives in parallel** (counterfactual planning).
**]**

**[FALSIFICATION_CRITERIA:** H1: it reimplements only a toy fragment of EC, not enough for real workflow fluents. H2: the tensorization is boolean-only (no gradients / no soft truth) → not differentiable. H3: memory blows up combinatorially with narrative count → no real parallelism benefit. **]**

**Falsification probe.** *Anti-confirmation:* H1 — the repo states it is "optimized for data stream reasoning," implying more than a toy; but coverage vs. full RTEC is unverified → H1 DEFERRED. H2 — *anti-confirmation is decisive here:* "tensor formalization" does not by itself imply differentiable soft-logic; NumPy/SciPy tensors can be strictly boolean. Absent evidence of gradient/probabilistic semantics, the falsification stands → H2 FALSIFIED pending explicit soft-truth support. H3 — tensor batching is real but memory scales with (events × fluents × narratives); bounded parallelism only → criterion partially met → H3 DEFERRED. **[ONTOLOGY_LOCK]** Same EC↔bookkeeping isomorphism as #7, but now the "ledger" is a tensor — the gap is representational, not semantic; the win is *runtime co-location* with the agent's numeric stack. **[COST_ANCHOR]** In-process NumPy: **lowest cross-runtime cost of any EC option here** — no Prolog subprocess. Direct comparative advantage over RTEC (#7) on integration cost, at the risk of reduced EC expressivity.

**[EPISTEMIC_DELTA:** H1 DEFERRED, H2 FALSIFIED (no evidence of soft/differentiable), H3 DEFERRED. **]**

---

### 9. `nasa/europa` — Constraint-based temporal planning framework (C++ w/ Java/Python bindings)
Plan Database + NDDL modeling language; timeline/activity representation with temporal-constraint propagation. NASA Open Source.

**[HYPOTHESIS_MATRIX:**
1. Hermes adopts EUROPA's **Plan Database** as the authoritative planning substrate, delegating temporal consistency to its propagation engine instead of the LLM.
2. Use **NDDL** as the target formal language the LLM compiles intent into, gaining validated timeline plans.
3. Use EUROPA's **flaw/resolution loop** as the deterministic backbone of Hermes' planning loop (LLM proposes resolutions, EUROPA guarantees consistency).
**]**

**[FALSIFICATION_CRITERIA:** H1: EUROPA is unmaintained/unbuildable on modern toolchains → not adoptable. H2: NDDL is too idiosyncratic for reliable LLM generation. H3: the flaw-resolution API is not exposed for external (agent-driven) control. **]**

**Falsification probe.** *Anti-confirmation:* H1 — EUROPA is battle-tested (NASA mission heritage) but its last active development is old; buildability on 2026 toolchains is a real risk → criterion plausibly met → H1 DEFERRED (must attempt a build). H2 — steelman for confirm: NDDL is declarative and templatable, and the LLM excels at templated DSLs; but NDDL's scarcity in training data raises error rates → net → H2 DEFERRED pending a generation eval. H3 — EUROPA is explicitly "designed to be embedded in a host application" with a solver API → the falsification fails → H3 CONFIRMED. **[ONTOLOGY_LOCK]** "Flight-ops timeline planning" → "constraint-based temporal plan": near-identity (this is EUROPA's native domain); the gap for Hermes is that space plans are authored by experts offline, while Hermes needs *interactive* plan edits — stressing the incremental-propagation path. **[COST_ANCHOR]** Heavyweight C++ dependency + bindings; highest build/integration cost in this list. Justified only if Hermes commits to timeline planning as a core capability, not a peripheral check.

**[EPISTEMIC_DELTA:** H1 DEFERRED (build risk), H2 DEFERRED, H3 CONFIRMED. **]**

---

### 10. `ticktac-project/tchecker` — Timed automata model checker (C++17)
Library + tools to describe timed systems, compute zone graphs (DBMs), and do symbolic reachability verification.

**[HYPOTHESIS_MATRIX:**
1. Hermes models a workflow as a **timed automaton** and uses TChecker reachability to prove "no deadline is ever missed on any path."
2. Use TChecker to **find a counterexample trace** (a schedule that violates a timing property) to feed back to the planner.
3. Use its **DBM library** as a reusable clock-constraint primitive inside the agent, independent of the full model checker.
**]**

**[FALSIFICATION_CRITERIA:** H1: state-space explosion makes verification intractable for realistic workflow sizes within the loop budget. H2: TChecker reports reachability but not a usable witness trace. H3: the DBM code is not modular/extractable from the checker. **]**

**Falsification probe.** *Anti-confirmation:* H1 — timed-automata verification is PSPACE-hard; for large agent workflows the criterion is genuinely met → H1 FALSIFIED for large models, CONFIRMED only for *small, safety-critical sub-workflows*. H2 — model checkers characteristically emit counterexample traces; TChecker exposes symbolic runs → falsification fails → H2 CONFIRMED. H3 — the DBM component is a well-known reusable abstraction and TChecker is "a library of classes" → extractability plausible → H3 CONFIRMED (pending header-level check). **[ONTOLOGY_LOCK]** "State machine with a stopwatch" → timed automaton: the gap is that agent workflows are *open* (unbounded external events) while timed automata are *closed* systems; environmental non-determinism must be modeled as adversarial input or the guarantee is void. **[COST_ANCHOR]** C++ subprocess per verification; expensive and non-incremental — reserve for *bounded critical sections*, not the whole plan.

**[EPISTEMIC_DELTA:** H1 FALSIFIED (large) / CONFIRMED (small critical), H2 CONFIRMED, H3 CONFIRMED. **]**

---

### 11. `roveri-marco/optic` (KCL OPTIC / POPF lineage) — Temporal PDDL2.1 planner (C++)
Forward-chaining temporal planner with full start–end durative-action semantics; cost/preference optimization.

**[HYPOTHESIS_MATRIX:**
1. Hermes emits **PDDL2.1 temporal domains/problems** and calls OPTIC to synthesize a *proven-valid* durative plan.
2. Use OPTIC's **preference/cost optimization** to let the agent trade off deadline vs. resource cost automatically.
3. Use OPTIC as a **plan validator** for LLM-proposed plans (re-plan only on failure).
**]**

**[FALSIFICATION_CRITERIA:** H1: PDDL2.1 authoring by LLM is error-prone at the at-start/at-end/over-all boundary (the search warned about this) → invalid domains. H2: OPTIC's optimization is limited to linear continuous effects → most agent cost models unexpressible. H3: OPTIC returns only plans, offering no cheap *validation-only* mode. **]**

**Falsification probe.** *Anti-confirmation:* H1 — the search explicitly notes OPTIC/POPF are *strict* about temporal placement of pre/effects, so LLM slips are likely → criterion met → H1 FALSIFIED unless a PDDL linter/VAL check is inserted between LLM and planner. H2 — OPTIC "has support for linear continuous effects only" (confirmed in results) → agent cost models with nonlinear terms are unexpressible → H2 FALSIFIED for nonlinear costs, CONFIRMED for linear. H3 — validation is better served by VAL (the PDDL plan validator) than by re-running the planner → H3 DEFERRED (route to VAL, not OPTIC). **[ONTOLOGY_LOCK]** "Gantt with dependencies" → PDDL durative actions: the gap is that PDDL requires a *complete, closed-world* domain model, whereas agents operate with open, partial world knowledge — the modeling burden is the true cost. **[COST_ANCHOR]** C++ subprocess; planning is search-heavy (can be seconds–minutes). Expensive relative to constraint propagation (#1/#4); use for genuine synthesis, not routine checks.

**[EPISTEMIC_DELTA:** H1 FALSIFIED (needs PDDL lint gate), H2 FALSIFIED (nonlinear) / CONFIRMED (linear), H3 DEFERRED (use VAL). **]**

---

### 12. `fpom/snakes` — High-level Petri nets library (Python)
Arbitrary Python objects as tokens, Python expressions as guards; plugin system; net-algebra composition.

**[HYPOTHESIS_MATRIX:**
1. Hermes represents a **workflow as a Petri net**, using token flow to model concurrent sub-tasks and synchronization joins the agent must respect.
2. Use SNAKES' **reachability/marking analysis** to detect deadlocks in a proposed multi-agent workflow before running it.
3. Use its **net-algebra composition** to build large workflows compositionally from verified sub-nets.
**]**

**[FALSIFICATION_CRITERIA:** H1: Petri nets have no native time → cannot express deadlines Hermes cares about. H2: marking-graph exploration explodes for realistic concurrency → analysis intractable in-loop. H3: composition operators break the guard semantics when nets carry Python-object tokens. **]**

**Falsification probe.** *Anti-confirmation:* H1 — *steelman to falsify:* base Petri nets are untimed, and Hermes' core concern is temporal; but SNAKES models *causal/concurrency structure* (who-waits-for-whom) which is orthogonal-and-complementary to metric time → criterion met for *metric deadlines*, so H1 FALSIFIED for timing but the causal-structure use survives as a *different* hypothesis. H2 — reachability explosion is real, but *structural* deadlock checks (siphons/traps) avoid full exploration → criterion avoidable → H2 CONFIRMED with structural analysis. H3 — SNAKES is explicitly designed for object tokens + composition (its raison d'être) → falsification fails → H3 CONFIRMED. **[ONTOLOGY_LOCK]** "Process flow chart / tokens moving through a workflow" → Petri net: strong isomorphism; the gap is that flowcharts are informal and single-threaded in the reader's mind, while Petri nets make *true concurrency and resource contention* explicit — the exact thing agents mishandle. **[COST_ANCHOR]** Pure-Python, in-process, plugin-extensible; low integration cost. Pairs with a timed layer (STN, #4/#5) to add metric deadlines Petri nets lack.

**[EPISTEMIC_DELTA:** H1 FALSIFIED (metric time) / CONFIRMED (concurrency structure), H2 CONFIRMED (structural), H3 CONFIRMED. **]**

---

### 13. `tlaplus/tlaplus` — TLA+ / TLC model checker (Java)
Temporal Logic of Actions; TLC exhaustively explores state space to verify invariants & temporal properties; simulation mode.

**[HYPOTHESIS_MATRIX:**
1. Hermes specs its **own orchestration protocol in TLA+** and uses TLC to verify liveness/safety of the agent loop itself (meta-verification).
2. Use TLC's **simulation mode** to fuzz-test agent workflows for rare temporal violations.
3. Auto-generate **TLA+ specs from LLM-described protocols** to catch design bugs before implementation.
**]**

**[FALSIFICATION_CRITERIA:** H1: TLA+ verifies *models*, not running code → the gap to the actual Hermes implementation voids the guarantee. H2: simulation mode needs a bounded, well-typed model the agent can't auto-produce. H3: LLM TLA+ generation is unreliable (niche syntax, temporal operators). **]**

**Falsification probe.** *Anti-confirmation:* H1 — the model↔implementation gap is intrinsic to all model checking; TLA+ guarantees the *design*, not the code → criterion met, but the *value* (finding design bugs) survives → H1 CONFIRMED for design-time verification, with the honest caveat that it does not certify the deployed loop. H2 — simulation needs a model, but building a small abstract model of the Hermes loop is a one-time human cost → criterion avoidable → H2 CONFIRMED. H3 — TLA+ syntax + temporal operators are notoriously subtle; recent work (TLA-Prover, arXiv 2606.06133) exists precisely because naive LLM generation is unreliable → falsification stands → H3 FALSIFIED without a spec-repair loop. **[ONTOLOGY_LOCK]** "Runbook / protocol invariant" → TLA+ temporal property: the gap is level-of-abstraction — TLA+ forces a *complete* abstract state machine, whereas a runbook is a partial checklist; the agent gains exhaustive coverage at the cost of building the abstraction. **[COST_ANCHOR]** JVM + potentially large state-space exploration: heavyweight, offline, human-in-the-loop. A design-time tool, never an in-loop check.

**[EPISTEMIC_DELTA:** H1 CONFIRMED (design-time), H2 CONFIRMED, H3 FALSIFIED (needs spec-repair loop). **]**

---

### 14. `mCRL2org/mCRL2` — Process-algebra toolset (C++)
Process-algebraic spec language + data types; modal μ-calculus properties checked via PBES; bisimulation/equivalence checking.

**[HYPOTHESIS_MATRIX:**
1. Hermes models **multi-agent interaction protocols** in mCRL2 and checks μ-calculus properties (e.g., "every request is eventually served").
2. Use **bisimulation checking** to prove a simplified agent workflow is behaviorally equivalent to a reference workflow (safe refactor).
3. Use PBES solving as a **generic verification backend** the agent queries for arbitrary temporal properties.
**]**

**[FALSIFICATION_CRITERIA:** H1: μ-calculus is too low-level for the LLM to author properties → unusable. H2: bisimulation is too strict (any interleaving difference breaks equivalence) → always reports "not equivalent." H3: PBES solving does not scale to workflow-sized state spaces in-loop. **]**

**Falsification probe.** *Anti-confirmation:* H1 — μ-calculus fixpoint formulas are among the hardest logics to author; but mCRL2 ships *pattern libraries* for common liveness/safety properties → criterion partly avoidable → H1 DEFERRED (viable only with a property-pattern DSL). H2 — *steelman to falsify:* strong bisimulation is indeed strict; but mCRL2 supports *weaker* equivalences (branching, weak bisimulation) that abstract internal steps → the "always not-equivalent" criterion fails under weak equivalence → H2 CONFIRMED with weak/branching bisimulation. H3 — PBES scales better than naive state enumeration but is still offline → H3 FALSIFIED for in-loop, CONFIRMED for design-time. **[ONTOLOGY_LOCK]** "Handshake / call-and-response protocol" → process algebra: strong isomorphism for *interaction*; the gap is that process algebra abstracts away data-heavy agent state, so properties are about *control flow*, not payload correctness. **[COST_ANCHOR]** C++ toolchain, offline; comparable heavyweight cost to TLA+ (#13). Overlaps TLA+ — pick one verification backend, not both, to control integration surface.

**[EPISTEMIC_DELTA:** H1 DEFERRED (needs property patterns), H2 CONFIRMED (weak bisimulation), H3 FALSIFIED (in-loop) / CONFIRMED (design-time). **]**

---

### 15. `jornfranke/allentemporalrelationships` — Allen relations + path consistency (Java)
Implementation of Allen's 13 interval relations and the **path-consistency algorithm** (constraint propagation over the interval network).

**[HYPOTHESIS_MATRIX:**
1. Hermes uses the **path-consistency algorithm** as the core inference step to tighten and validate a network of LLM-asserted temporal relations.
2. Use it as a **contradiction detector** that flags exactly when the LLM's temporal claims are jointly unsatisfiable.
3. Port the algorithm (it is small) into Hermes' native runtime to avoid any subprocess.
**]**

**[FALSIFICATION_CRITERIA:** H1: path consistency is incomplete (does not detect all inconsistencies for the full Allen algebra) → false sense of validity. H2: it returns a consistent/inconsistent verdict without localizing the offending relations. H3: the code is a toy/demo, not a reusable algorithm.**]**

**Falsification probe.** *Anti-confirmation:* H1 — this is a *true* limitation: path consistency (PC-2) is sound but **incomplete** for the full Allen algebra (deciding consistency is NP-complete; PC only guarantees consistency for tractable subclasses like the pointizable/ORD-Horn fragment) → criterion met → H1 FALSIFIED as a *complete* validator, CONFIRMED as a *sound necessary* filter (it never accepts a truly inconsistent network's *local* triples, but may miss global inconsistency). H2 — small implementations typically return a boolean/updated matrix; localization is not guaranteed → H2 DEFERRED (inspect return type). H3 — it is a focused reference implementation of a named algorithm, adequate to port → falsification weak → H3 CONFIRMED. **[ONTOLOGY_LOCK]** "Cross-checking a schedule for contradictions" → path consistency: the gap is that humans stop at the first contradiction, while PC propagates *all* pairwise implications — but PC's incompleteness means it can still miss a globally inconsistent schedule that no local triple reveals. **[COST_ANCHOR]** The algorithm is O(n³) per pass and tiny; porting to Python/native is cheap and removes any JVM dependency (vs. running the Java as-is).

**[EPISTEMIC_DELTA:** H1 FALSIFIED (complete) / CONFIRMED (sound filter), H2 DEFERRED, H3 CONFIRMED. **]**

---

## SELF_REFLEXIVE_CHECK

- **Representable in the agent's state space?** Yes for interval/relation networks (#1, #2, #12, #15), STN/STNU graphs (#4, #5), and fluent sets (#7, #8) — all serialize to JSON/dicts the agent can hold. Model-checker state spaces (#10, #13, #14) are *not* agent-state; they are offline artifacts.
- **I/O stable enough for automation?** Yes for the Python/JSON-native tools (#1, #6, #7, #8, #12). Risk concentrated in GUI-first or expert-DSL tools (#3 authoring, #9 NDDL, #11 PDDL, #13/#14 formal specs).
- **Benefit > subprocess/compile/translation cost?** Yes for in-process Python & WASM (#1, #5, #6, #8, #12, ported #15). Cost-questionable for JVM/C++ offline checkers (#9, #10, #11, #13, #14) — justified only for bounded, high-stakes sub-problems.
- **Survives runtime environmental change?** STNU dynamic controllability (#4) is the *only* class that is explicitly designed to survive uncontrollable environmental variation — the strongest single property for an autonomous agent. Plain STN and untimed nets do not.

---

## [HARNESS_HERMES]

Only **CONFIRMED** hypotheses (or their confirmed sub-cases) are promoted. The confirmed integration surface forms a **layered temporal spine** for Hermes:

- **Layer A — Interval/relation core (in-process, cheap, always-on):** qualreas (#1, batch consistency + mixed point/interval), ported path-consistency (#15, sound pre-filter), SNAKES (#12, concurrency/deadlock structure). Confirmed, low-cost, JSON-native.
- **Layer B — Metric-time & uncertainty (selective):** STN via WASM (#5, in-process propagation) for controllable schedules; CSTNU Tool (#4, dynamic controllability) for plans with uncontrollable-duration actions — the highest-value guarantee, invoked selectively due to JVM cost.
- **Layer C — State & monitoring (streaming):** RTEC (#7, fluents from event streams; fixed-domain axioms) and RTAMT (#6, numeric-telemetry robustness monitoring, windowed) as the running loop's guard rails.
- **Layer D — Design-time verification (offline, human-in-loop):** TChecker (#10, bounded critical sections) and TLA+ **or** mCRL2 (#13/#14, pick one) to verify the orchestration protocol's design, not the live loop.

Explicitly **deferred/route-around** (not in the initial harness): MonAmI foATL authoring (#3, needs DSL), Tensor-EC soft-logic (#8, unproven), EUROPA/NDDL (#9, build risk), OPTIC nonlinear/at-boundary (#11, needs PDDL-lint + VAL gate), LLM auto-generation of TLA+/μ-calculus/NDDL/PDDL (route through a linter/spec-repair loop before trusting).

---

## [IMPLEMENTATION_WORKFLOW]

**Phase 1 — In-process interval spine (lowest cost, confirmed).**
Integrate qualreas (#1) + ported Allen path-consistency (#15) as a `temporal_consistency` module. Every plan the LLM emits is lowered to a relation network; run batch consistency as a *sound pre-filter* (accept "unknown" only when PC passes — never treat PC-pass as full validity). Add SNAKES (#12) structural deadlock check for any plan with concurrent branches. Deliverable: a deterministic, in-process "is this plan temporally coherent?" gate.

**Phase 2 — Uncertainty guarantee (highest value).**
Add CSTNU Tool (#4) behind a headless adapter, invoked *only* for plans containing uncontrollable-duration actions (tool calls, human approvals). Gate execution on **dynamic controllability**. Prototype WASM STN (#5) in-process for the controllable common case to avoid the JVM hop. Deliverable: plans are provably executable under worst-case durations, or rejected with the offending constraint.

**Phase 3 — Runtime guards (streaming).**
Wire RTEC (#7, fixed Hermes event-ontology axioms) to derive symbolic world-state fluents from the tool-call event stream, and RTAMT (#6, windowed) to monitor numeric telemetry robustness. Deliverable: the running loop trips early and cleanly on both symbolic-state and metric-margin violations.

**Phase 4 — Design-time meta-verification (offline).**
Model the Hermes orchestration protocol once in TLA+ *or* mCRL2 (#13/#14 — choose one backend) and verify liveness/safety of the loop itself; use TChecker (#10) for any bounded hard-real-time critical section. Route all LLM-authored formal specs (TLA+/μ-calculus/PDDL/NDDL) through a lint + spec-repair loop before trusting them. Deliverable: the loop's *design* is verified; auto-generated specs are validated, not assumed.

**Sequencing rationale:** cost and confirmation strength both decrease down the phases. Phase 1 is all-confirmed, in-process, zero-subprocess. Phase 2 buys the single most valuable property (controllability under uncertainty) at moderate cost. Phases 3–4 add guards and design assurance but carry subprocess/offline cost, so they follow once the cheap spine proves its value.

---

*Epistemic trajectory preserved: no workflow was synthesized before completing hypothesis validation across all 15 repositories. Loops were not collapsed. Deferred and falsified hypotheses were retained rather than silently dropped.*

## Sources

- [alreich/qualreas](https://github.com/alreich/qualreas)
- [ajcr/IntervalAlgebra](https://github.com/ajcr/IntervalAlgebra)
- [moraneus/MonAmI](https://github.com/moraneus/MonAmI)
- [CSTNU Tool — ElsevierSoftwareX/SOFTX-D-21-00153](https://github.com/ElsevierSoftwareX/SOFTX-D-21-00153)
- [xOPERATIONS/temporal-networks](https://github.com/xOPERATIONS/temporal-networks)
- [nickovic/rtamt](https://github.com/nickovic/rtamt)
- [aartikis/RTEC](https://github.com/aartikis/RTEC)
- [eftsilio/Tensor-EC](https://github.com/eftsilio/Tensor-EC)
- [nasa/europa](https://github.com/nasa/europa)
- [ticktac-project/tchecker](https://github.com/ticktac-project/tchecker)
- [roveri-marco/optic](https://github.com/roveri-marco/optic)
- [fpom/snakes](https://github.com/fpom/snakes)
- [tlaplus/tlaplus](https://github.com/tlaplus/tlaplus)
- [mCRL2org/mCRL2](https://github.com/mCRL2org/mCRL2)
- [jornfranke/allentemporalrelationships](https://github.com/jornfranke/allentemporalrelationships)
