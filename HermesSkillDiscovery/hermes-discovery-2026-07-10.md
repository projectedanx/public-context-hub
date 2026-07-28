# Hermes Agent Harness — Paraconsistent Integration Sensor Run

**Date:** 2026-07-10
**Run type:** Automated daily PDL discovery (PDL:v1.0)
**Sensor identity:** Paraconsistent Integration Sensor — mapping integration potential, not solving implementation.
**Prior runs:** None found in outputs history — this is the inaugural run of the sensor.

> Path note: the SKILL.md target path referenced a stale session directory (`local_139fdd79-…`). This run's active outputs directory is `local_5527fdd9-…`. File saved there and presented directly so continuity is preserved regardless of the path drift.

---

## Chosen AI Problem Space: **Temporal Reasoning**

**Rationale (highest epistemic tension selection).** Among the rotation candidates, temporal reasoning carries the sharpest tension with mainstream LLM behavior *for an agent harness specifically*. Transformer LLMs collapse time into a flat token window: they have no first-class representation of ordering, duration, concurrency, valid-time vs. transaction-time, or "what must hold over an interval." Yet Hermes' core mandate — deterministic workflows and long-horizon future-forward tasks — is *irreducibly temporal*. The gap is not stylistic; it is representational. Pre-AI temporal-reasoning substrate (interval algebras, temporal logics, timed automata, synchronous dataflow, bitemporal stores, temporal planners) encodes exactly the state-space discipline that autoregressive generation lacks. This is the substrate most likely to give the agent a "human skill engineers overlook": reasoning about *time as structure* rather than time as narration.

**Scope lock:** `Integration_Epistemic_Exploration` — target = repository integration potential into Hermes. Falsification trajectory is the primary deliverable; the implementation workflow is downstream and uses CONFIRMED hypotheses only.

---

## Preflight Matrix — Non-Obvious Linguistic Connections

Cross-mapping used to surface high-surprisal, non-AI-noise repositories. Columns map candidate concepts across register.

| Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term (drop AI noise) |
|---|---|---|---|---|
| Interval algebra | Court-docket scheduling; alibi reconciliation | C-extension, composition table, path-consistency | library, engine | −LLM −agent −copilot |
| Linear/branching temporal logic | Watch-officer standing orders; "must always / eventually" | automaton translation, BDD, HOA | model checker, toolkit | −RAG −prompt |
| Timed automata | Assembly-line takt time; railway interlocking | zone graph, DBM, reachability | verifier, solver | −chatbot −embedding |
| Temporal logic of actions | Double-entry ledger of state changes | TLC, breadth-first state enum | spec, checker | −transformer |
| Durative-action planning | Gantt / critical-path; incident command | PDDL2.1, `at start`/`over all`/`at end` | planner, engine | −LLM −neural |
| Synchronous dataflow | Musical score / conductor beat; relay logic | clock calculus, step function, Obc | compiler, language | −agent −copilot |
| Progress-tracked dataflow | Shift handover with logical clocks | timestamp lattice, frontier, epoch | framework, engine | −LLM |
| Signal temporal logic | Vital-sign monitoring; SLA/SLO watch | robustness semantics, online monitor | monitoring library | −RAG −prompt |
| Metric first-order temporal logic | Audit/compliance log review; forensic accounting | policy formula, event DB, aggregation | monitor, tool | −LLM −agent |
| Bitemporal store | Ledger with "as-known-then" vs "as-true-then" | valid-time/transaction-time columns | database, layer | −vector −embedding |
| Event calculus | Detective narrative reconstruction | SAT encoding, fluents, initiates/terminates | reasoner | −LLM −neural |
| Statechart / SCXML | Air-traffic-control mode board | delayed events, simulated clock, guards | interpreter, engine | −agent −copilot |
| Qualitative spatio-temporal | Eyewitness "before/after/while" testimony | QSR calculus, relation network | library, toolkit | −LLM −RAG |

---

## Repository Findings — Full PDL Loop (×15)

Each entry runs `Hypothesis_Generation → Falsification_Probe (anti-confirmation) → Epistemic_Delta_Logging` and a self-reflexive check. Cost anchors are comparative (subprocess/compile/translation vs. native-state).

---

### 1. `ajcr/IntervalAlgebra` — Allen's Interval Algebra (C-extension for Python)
**URL:** https://github.com/ajcr/IntervalAlgebra
**Observed concept:** Native interval type + the 13 Allen base relations (before, meets, overlaps, during, starts, finishes, equals + inverses) with constant-time relation queries.

- **[HYPOTHESIS_MATRIX:** 1. Hermes adopts the 13-relation vocabulary as the *canonical schema* for representing relationships between any two agent sub-tasks (task A `meets` task B, etc.), replacing ad-hoc "after step 3" prose. 2. The interval type becomes a runtime guard: before scheduling, the harness checks pairwise Allen consistency to catch impossible orderings (a task that must both `precede` and be `during` another). 3. The composition table is imported wholesale to let the agent *infer* unstated ordering constraints transitively (if A before B and B before C, derive A before C) without an LLM call.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if the 13 relations cannot express a genuine Hermes dependency (e.g., partial/optional overlap with resource contention). H2: falsified if pairwise-only checking misses global inconsistency that requires full network path-consistency. H3: falsified if the C-extension exposes the composition table only internally with no Python-level API to compose relations.**]
- **Falsification probe (anti-confirmation first):** Steelman for FALSIFYING H1 — real agent dependencies carry resource and data payloads, not just temporal ordering; Allen relations are purely ordinal. But the criterion is *expressibility of the temporal skeleton*, and the 13 relations are provably jointly-exhaustive/pairwise-disjoint over interval pairs, so the skeleton is fully covered; payload lives on the edge, not in the relation. H1 survives. H2 genuinely fails: pairwise Allen relations are locally consistent yet globally unsatisfiable networks exist — this repo is a *relation type*, not a *network solver*, so H2's criterion (needs path-consistency) is met → route to repo #2. H3: the module is a relations engine over an interval type; composition is not its headline export, criterion partially triggers → DEFER.
- **[ONTOLOGY_LOCK]** Abstraction gap: Allen intervals are *dense-time human intervals* ("the meeting lasted an hour"); Hermes tasks are *discrete, possibly instantaneous* execution spans. Mapping "interval" → "task lifetime" silently assumes non-zero, well-ordered duration — degenerate for zero-cost or racing tasks.
- **[IMPLEMENTATION_COST_ANCHOR]** In-process Python C-extension: ~microsecond relation checks, zero subprocess/IPC. Cost ≪ an LLM ordering call (~seconds, non-deterministic). The relation *vocabulary* alone (13 enums) is near-free to adopt independent of the binary.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (adopt the 13-relation vocabulary as task-dependency schema). H2 FALSIFIED (needs a network solver, not this type). H3 DEFERRED (composition API surface unverified).**]
- **Self-reflexive check:** Representable in state space ✔ (13-value enum on task-pair edges). I/O stable ✔ (pure functions). Benefit > cost ✔ (vocabulary is free). Survives runtime change ✔ (relations are environment-independent).

---

### 2. `strands-project/strands_qsr_lib` — Qualitative Spatio-Temporal Reasoning Library
**URL:** https://github.com/strands-project/strands_qsr_lib
**Observed concept:** A library of qualitative calculi (Allen relations, RCC, QTC…) that compute symbolic relations from raw timestamped/quantitative data — i.e., a *quantizer* from metric traces to qualitative relation streams.

- **[HYPOTHESIS_MATRIX:** 1. Hermes uses the QSR quantizer to convert its numeric event log (timestamps, durations) into a stream of qualitative Allen/temporal relations the agent can reason over symbolically. 2. The multi-calculus architecture lets Hermes swap temporal *and* spatial calculi through one interface, enabling cross-domain reasoning (a task's temporal `before` and a resource's spatial `disconnected` in the same relation graph). 3. The library's "make world → make QSR" pipeline becomes Hermes' standard trace-abstraction layer, feeding a downstream consistency solver.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if quantization requires a fixed sampling model incompatible with sparse, event-driven agent logs. H2: falsified if calculi cannot share a relation graph (each is siloed). H3: falsified if the QSR output format is not machine-stable enough for automated downstream consumption.**]
- **Falsification probe:** Steelman FALSIFY H1 — QSR libraries were built for robot sensor streams (regular sampling); agent logs are bursty and irregular. Yet the criterion is *compatibility with sparse event logs*, and QSR calculi operate on ordered timestamped states regardless of sampling regularity — irregular spacing degrades resolution but not correctness. H1 survives. H2: the calculi are pluggable but each produces its own relation namespace; a *shared* graph requires an integration layer the repo does not ship → criterion met → FALSIFY H2. H3: output is structured QSR-state dictionaries, stable and serializable → survives → lean CONFIRM H3, but H3 folds into H1.
- **[ONTOLOGY_LOCK]** Gap: QSR was engineered for *embodied perception* (a robot seeing objects move). Re-targeting it to *abstract task execution* maps "physical trajectory" → "task state history" — the abstraction survives temporally but the spatial calculi become metaphorical, not literal, for a non-embodied harness.
- **[IMPLEMENTATION_COST_ANCHOR]** Pure-Python, in-process. Trace→relation abstraction is O(n) over events, cheap vs. re-deriving orderings via LLM per query. Chief cost is dependency weight (a ROS-adjacent research lib) — vendoring only the Allen/temporal calculi is lower-cost than adopting the whole package.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (adopt as the trace→qualitative-relation abstraction layer, temporal calculi only). H2 FALSIFIED (no shared cross-calculus graph out of the box). H3 CONFIRMED-into-H1.**]
- **Self-reflexive check:** Representable ✔. I/O stable ✔ (serializable QSR states). Benefit > cost ◐ (trim to temporal calculi to avoid dependency bloat). Survives runtime change ✔.

---

### 3. `jurajmajor/ltl3tela` — LTL → ω-automata translator (generic acceptance)
**URL:** https://github.com/jurajmajor/ltl3tela
**Observed concept:** Compiles Linear Temporal Logic formulas into small ω-automata with generic (Emerson–Lei) acceptance — i.e., turns a *declarative liveness/safety spec* into an *executable recognizer*.

- **[HYPOTHESIS_MATRIX:** 1. Hermes expresses its own success/safety invariants as LTL ("eventually the deliverable is produced", "never touch prod before tests pass") and compiles them to automata that run alongside execution as monitors. 2. The generated automaton becomes a *goal-progress oracle*: the agent checks which automaton states are still reachable to know if a long-horizon goal is still achievable. 3. LTL formulas become the harness's portable, model-agnostic contract language that survives swapping the underlying LLM.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if agent-relevant properties need metric/quantitative time (deadlines), which pure LTL cannot express. H2: falsified if "reachable acceptance state" does not correspond to "goal still achievable" under the agent's actual transition semantics. H3: falsified if the tool requires a heavyweight external toolchain (e.g., Spot) making automation brittle.**]
- **Falsification probe:** Steelman FALSIFY H1 — Hermes cares about deadlines ("finish within 10 steps"), and LTL is untimed; therefore LTL under-expresses. Criterion (needs metric time) is genuinely met for *deadline* properties → PARTIAL. But for *qualitative* ordering/liveness/safety invariants (the majority of workflow correctness constraints), LTL is exactly right and the steelman does not touch those → H1 CONFIRMED for the qualitative fragment, deadlines routed to STL (#10/#11) and timed automata (#13). H2: mapping "automaton acceptance reachable" → "goal achievable" requires the agent's execution to be modeled as the automaton's input alphabet — an isomorphism that holds only if agent actions are faithfully alphabetized; unproven here → DEFER. H3: LTL3TELA depends on Spot as backend; automation is feasible but adds a compiled dependency → note in cost.
- **[ONTOLOGY_LOCK]** Gap: LTL semantics assume *infinite* traces (ω-words); agent runs are *finite*. Mapping requires LTLf (LTL over finite traces) semantics or a stutter-extension convention — using ω-LTL naively on finite agent runs mis-scores termination.
- **[IMPLEMENTATION_COST_ANCHOR]** One-time compile of formula→automaton (milliseconds for small formulas), then O(1) per-step transition at runtime — dramatically cheaper and *deterministic* vs. asking an LLM "are we still on track?" each step. Backend compile dependency (Spot) is a heavier install than a pure-Python lib.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (qualitative fragment; use LTLf semantics). H2 DEFERRED (action-alphabet isomorphism unproven). H3 CONFIRMED with dependency caveat.**]
- **Self-reflexive check:** Representable ✔ (automaton state = extra scalar in agent state). I/O stable ✔. Benefit > cost ✔ for qualitative invariants. Survives runtime change ✔ (spec is LLM-agnostic).

---

### 4. `tlaplus/tlaplus` — TLA+ / TLC (Temporal Logic of Actions)
**URL:** https://github.com/tlaplus/tlaplus
**Observed concept:** Specify systems as state machines with temporal-logic invariants; TLC exhaustively enumerates reachable states to find invariant violations and deadlocks.

- **[HYPOTHESIS_MATRIX:** 1. Hermes authors a TLA+ spec of a *workflow class* once and uses TLC offline to prove the workflow cannot deadlock or violate an invariant before ever executing it live. 2. The agent generates candidate multi-step plans and hands each to TLC as a bounded model to reject unsafe plans deterministically. 3. TLA+'s "action = state-transition relation" primitive becomes Hermes' internal representation of every tool call (pre-state → post-state), giving a uniform algebra over actions.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if realistic Hermes workflows have state spaces too large for TLC's exhaustive enumeration (state explosion). H2: falsified if plan-to-TLA+ translation cannot be automated reliably (requires human spec-writing). H3: falsified if agent actions have non-deterministic external effects TLC cannot model as pure state transitions.**]
- **Falsification probe:** Steelman FALSIFY H1 — TLC does breadth-first over *finite, enumerable* states and blows up combinatorially; agent workflows touching filesystems/APIs have astronomically large state. Criterion (state explosion) is real for *unabstracted* state → H1 FALSIFIED at full fidelity. But TLA+'s value survives at the *abstraction* level: model the control skeleton (which step, which guard) not the data — at that granularity spaces are small. So H1 → FALSIFIED as stated, re-CONFIRMED only under an explicit abstraction discipline (log as scar). H2: automatic English/plan → TLA+ is unsolved and the repo offers no such translator; criterion met → FALSIFY H2. H3: external non-determinism can be modeled as environment-choice actions, a standard TLA+ idiom → H3 survives falsification → CONFIRM as a *modeling primitive*.
- **[ONTOLOGY_LOCK]** Gap: TLA+ "action" is a *mathematical relation on states*; a tool call is a *side-effecting procedure*. Mapping tool-call → action assumes effects are capturable as state deltas — false for irreversible or observation-dependent effects (sending an email). Name the gap: **effect-purity assumption**.
- **[IMPLEMENTATION_COST_ANCHOR]** TLC is a Java process — heavyweight subprocess, seconds-to-minutes per model, JVM startup. Far costlier than in-process checks; justified only for *high-stakes, reused* workflow templates, not per-run. Comparative: cheaper than a production incident, far more expensive than an LTLf monitor.
- **[EPISTEMIC_DELTA:** H1 FALSIFIED (state explosion; only viable under strict control-skeleton abstraction — SYMBOLIC SCAR: "verify the skeleton, never the data"). H2 FALSIFIED (no auto-translation). H3 CONFIRMED (action-as-state-transition primitive adopted internally).**]
- **Self-reflexive check:** Representable ◐ (only abstracted skeleton). I/O stable ✔ (TLC exit codes/traces). Benefit > cost ◐ (only for reused templates). Survives runtime change ✖ at data fidelity, ✔ at skeleton level.

---

### 5. `nimble-code/Spin` — SPIN / Promela explicit-state LTL model checker
**URL:** https://github.com/nimble-code/Spin
**Observed concept:** Models concurrent processes in Promela, checks LTL properties via on-the-fly explicit-state search with partial-order reduction; ACM System Software Award winner.

- **[HYPOTHESIS_MATRIX:** 1. When Hermes orchestrates *concurrent* sub-agents, it models their interaction in Promela and uses SPIN to detect races/deadlocks in the coordination protocol before deploying it. 2. SPIN's partial-order reduction technique (not the tool) is ported as an idea: prune equivalent interleavings of independent agent actions to shrink the reasoning space. 3. SPIN counterexample traces become concrete failing schedules the agent replays to debug multi-agent coordination.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if Hermes concurrency is coarse enough (few processes) that races never arise, making the tool moot. H2: falsified if agent actions are not independent enough for partial-order reduction to yield savings. H3: falsified if SPIN counterexamples cannot be mapped back to executable agent schedules.**]
- **Falsification probe:** Steelman FALSIFY H1 — most agent harnesses run sequentially; concurrency verification is premature. Criterion (concurrency rarely arises) partly holds *today* but Hermes' mandate is long-horizon multi-agent orchestration where interleaving bugs are exactly the failure mode → H1 survives for the concurrent-orchestration roadmap, DEFER until concurrency exists. H2: the *concept* of partial-order reduction is soundly transferable — independent actions do commute — criterion (insufficient independence) fails because agent tool calls on disjoint resources are provably independent → CONFIRM H2 as a design principle. H3: Promela↔agent-action mapping is manual and lossy; criterion met → FALSIFY H3 as automated, keep as manual debugging aid.
- **[ONTOLOGY_LOCK]** Gap: Promela processes are *fixed, statically-declared*; agent sub-tasks are *dynamically spawned*. Mapping assumes a bounded, pre-known process set — false for open-ended agent fan-out. Name: **static-topology assumption**.
- **[IMPLEMENTATION_COST_ANCHOR]** SPIN compiles a C verifier per model then runs it — compile + subprocess cost, but very fast search once built. The *idea* (partial-order reduction) is zero-runtime-cost to adopt. Full tool integration ≫ cost of adopting the principle.
- **[EPISTEMIC_DELTA:** H1 DEFERRED (contingent on real concurrency in Hermes). H2 CONFIRMED (partial-order reduction as an interleaving-pruning principle). H3 FALSIFIED as automated (manual aid only).**]
- **Self-reflexive check:** Representable ◐. I/O stable ◐ (trace format parseable). Benefit > cost ◐ (only under concurrency). Survives runtime change ✔ for the principle.

---

### 6. `neighthan/tfd` — Temporal Fast Downward (PDDL2.1 durative actions)
**URL:** https://github.com/neighthan/tfd
**Observed concept:** Heuristic temporal planner over durative actions with `at start` / `over all` / `at end` condition-effect timing and a context-enhanced additive heuristic in temporal state space.

- **[HYPOTHESIS_MATRIX:** 1. Hermes offloads long-horizon task sequencing to TFD: express tools as durative PDDL actions and let a *deterministic planner* produce the schedule, replacing LLM step-by-step planning. 2. The `at start`/`over all`/`at end` decomposition becomes Hermes' internal contract shape for every tool (preconditions that must hold at invocation, invariants over execution, effects at completion). 3. TFD's temporal heuristic guides the agent's own search when full planning is too slow — used as a cheap admissible estimate of "steps to goal".**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if the agent's action set cannot be expressed in PDDL (conditional/continuous effects beyond PDDL2.1). H2: falsified if the three-part timing decomposition cannot capture real tool semantics. H3: falsified if the heuristic is entangled with the planner internals and not extractable as a standalone estimate.**]
- **Falsification probe:** Steelman FALSIFY H1 — agent tools have data-dependent, open-world effects; PDDL demands a closed, typed, fully-specified action model. Criterion (inexpressible effects) holds for *content-generating* tools whose effects aren't enumerable → H1 FALSIFIED for open-world tools, re-CONFIRMED for the *structured/deterministic* subset (file ops, deploy steps, ordered pipelines) which is precisely Hermes' deterministic-workflow mandate. H2: the `at start / over all / at end` triple is a genuinely superior contract shape — it survives every falsification attempt because it strictly generalizes point pre/post-conditions → CONFIRM H2 strongly. H3: the heuristic is baked into TFD's C++ search; extracting it standalone is high-effort → FALSIFY H3.
- **[ONTOLOGY_LOCK]** Gap: PDDL planning assumes a *fully-observable, closed world* with known action models; agents operate in *partially-observable, open* worlds. Mapping "PDDL action" → "agent tool" imports a closed-world assumption the agent's reality violates. Name: **closed-world / full-observability assumption**.
- **[IMPLEMENTATION_COST_ANCHOR]** TFD is a compiled C++ subprocess; planning is seconds for small domains, exponential worst-case. Cross-process translation (state→PDDL→plan) has real marshalling cost but is *deterministic and reusable* vs. per-run LLM planning. Justified when the same workflow shape recurs.
- **[EPISTEMIC_DELTA:** H1 FALSIFIED for open-world tools / CONFIRMED for the deterministic-workflow subset. H2 CONFIRMED (adopt `at start`/`over all`/`at end` as universal tool-contract shape — highest-value takeaway). H3 FALSIFIED (heuristic not cleanly extractable).**]
- **Self-reflexive check:** Representable ✔ (PDDL domain is explicit state). I/O stable ✔ (plan = ordered action list). Benefit > cost ✔ for recurring deterministic workflows. Survives runtime change ◐ (needs closed-world subset).

---

### 7. `aig-upf/temporal-planning` — Temporal planning algorithms (Fast Downward fork + wrappers)
**URL:** https://github.com/aig-upf/temporal-planning
**Observed concept:** A packaged pipeline of temporal-planning approaches (including compilation of temporal problems to classical planning) with a cleaner invocation surface than raw TFD.

- **[HYPOTHESIS_MATRIX:** 1. Hermes uses the compilation-to-classical-planning trick to reduce its temporal scheduling to a simpler, better-tooled classical planner it can call reliably. 2. The repo's wrapper/CLI is the integration seam — Hermes shells out via a stable command interface rather than binding to planner internals. 3. The multiple bundled algorithms let Hermes *portfolio-plan*: race several planners and take the first valid schedule.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if the temporal→classical compilation loses required concurrency semantics (required concurrency = actions that *must* overlap). H2: falsified if the CLI is unstable/undocumented, breaking automation. H3: falsified if portfolio planning gives no diversity benefit (all planners fail on the same inputs).**]
- **Falsification probe:** Steelman FALSIFY H1 — temporal-to-classical compilations famously cannot express *required concurrency* (two actions that must run simultaneously). Criterion met → H1 FALSIFIED for domains needing required concurrency; but Hermes' deterministic workflows are overwhelmingly *sequential-with-optional-overlap*, where the compilation is sound → re-CONFIRMED for the sequential majority (scar: "compilation is unsafe when overlap is mandatory"). H2: the wrapper exists precisely to stabilize invocation; criterion (unstable CLI) fails → CONFIRM H2 as the integration seam. H3: portfolio diversity helps only if planners have different failure modes; unproven for this bundle → DEFER.
- **[ONTOLOGY_LOCK]** Gap: same closed-world planning assumption as #6; additionally, "compilation to classical" trades *temporal* semantics for *ordering* semantics — mapping durations → sequence loses metric duration entirely. Name: **duration-erasure under compilation**.
- **[IMPLEMENTATION_COST_ANCHOR]** Subprocess, comparable to #6 but with lighter invocation overhead thanks to the wrapper. Preferable *entry point* to temporal planning than binding TFD directly; lower integration cost, same runtime cost.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED for sequential/optional-overlap workflows (FALSIFIED where concurrency is required). H2 CONFIRMED (CLI wrapper = integration seam). H3 DEFERRED (portfolio benefit unverified).**]
- **Self-reflexive check:** Representable ✔. I/O stable ✔ (CLI). Benefit > cost ✔ as the preferred planner entry point. Survives runtime change ◐ (sequential subset).

---

### 8. `TimelyDataflow/timely-dataflow` — Timely Dataflow (logical-timestamp progress tracking)
**URL:** https://github.com/TimelyDataflow/timely-dataflow
**Observed concept:** A dataflow engine where every message carries a *logical timestamp* and the system tracks *frontiers* — the guarantee that no more data at-or-before a timestamp will arrive — enabling correct incremental, cyclic computation.

- **[HYPOTHESIS_MATRIX:** 1. Hermes adopts the *frontier / progress-tracking* concept to know deterministically when a long-horizon sub-computation is "complete up to time T" — replacing heuristic "is it done yet?" polling. 2. Logical timestamps become Hermes' mechanism for coordinating out-of-order results from parallel sub-agents while preserving a total causal order. 3. The cyclic-dataflow model lets Hermes express *iterative refinement loops* (re-plan, re-run) with guaranteed termination detection.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if agent tasks lack a meaningful partial order to timestamp (all effectively independent or all sequential). H2: falsified if the Rust engine's timestamp model can't be reproduced as a lightweight bookkeeping layer without adopting the whole runtime. H3: falsified if frontier/progress tracking requires a static dataflow graph incompatible with dynamic agent task creation.**]
- **Falsification probe:** Steelman FALSIFY H1 — if agent tasks are a simple linear chain, logical timestamps add nothing over a step counter. Criterion holds for trivial linear workflows → H1 FALSIFIED for the linear case, CONFIRMED for *fan-out/fan-in* workflows where partial order is real and progress must be tracked across branches. H2: the *concept* (frontier = "done up to T") is a lightweight invariant portable without the Rust runtime — criterion (can't reproduce cheaply) fails → CONFIRM H2 as an adopted concept, not a dependency. H3: timely supports dynamic scopes but faithful adoption of the *engine* wants structured graphs; dynamic agent spawning strains this → DEFER the full-engine path.
- **[ONTOLOGY_LOCK]** Gap: timely timestamps are *data-plane* markers on a streaming graph; Hermes needs *control-plane* progress over tasks. Mapping "message frontier" → "task-completion frontier" reuses the *math* (lattice of timestamps, antichains) while changing the *referent* — the abstraction survives because progress-tracking is domain-neutral, but the runtime does not transfer.
- **[IMPLEMENTATION_COST_ANCHOR]** Adopting the *concept*: near-zero (a timestamp lattice + frontier bookkeeping in the harness's own language). Adopting the *Rust engine*: high — cross-language FFI or a Rust sidecar process, plus the impedance of driving it from an LLM loop. Recommendation strongly favors concept-adoption over runtime-adoption.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED for fan-out/fan-in workflows (FALSIFIED for linear chains). H2 CONFIRMED (frontier as a portable progress invariant). H3 DEFERRED (full-engine dynamic-graph path).**]
- **Self-reflexive check:** Representable ✔ (frontier = antichain of timestamps in state). I/O stable ✔. Benefit > cost ✔ for concept, ✖ for full engine. Survives runtime change ✔ (progress math is invariant).

---

### 9. `TimelyDataflow/differential-dataflow` — Differential Dataflow (incremental recomputation)
**URL:** https://github.com/TimelyDataflow/differential-dataflow
**Observed concept:** Computations over collections that update *incrementally* — when inputs change by a delta, only the affected outputs are recomputed, using difference traces indexed by (time, diff).

- **[HYPOTHESIS_MATRIX:** 1. Hermes memoizes long-horizon derived state as differential collections so that when one upstream fact changes, it recomputes only the affected downstream tasks instead of re-running the whole workflow. 2. The (data, time, diff) triple becomes Hermes' representation of *belief updates* — the agent tracks what changed and when, enabling cheap what-if/rollback. 3. Differential's `iterate` operator models fixpoint agent loops (keep refining until no diffs) with automatic convergence detection.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if agent task outputs are non-deterministic (same input, different output), breaking the incremental-recompute correctness guarantee. H2: falsified if the diff-trace bookkeeping cost exceeds the recompute it saves for small workflows. H3: falsified if `iterate`'s convergence requires monotone lattices agent state doesn't form.**]
- **Falsification probe:** Steelman FALSIFY H1 — LLM tool calls are non-deterministic; incremental recomputation assumes pure functions of inputs, so caching a task's output and reusing it on unchanged inputs is *unsound* when the tool is an LLM. Criterion met → H1 FALSIFIED for LLM-backed tasks, re-CONFIRMED only for *deterministic* sub-tasks (parsing, transforms, computations) where reuse is sound — a real but bounded subset. H2: for small linear workflows, trace overhead > savings; criterion met → FALSIFY H2 for small cases, benefit appears only at scale/high-fan-out. H3: general agent state is not a monotone lattice; `iterate` correctness criterion met → FALSIFY H3 as general, keep for monotone accumulation loops.
- **[ONTOLOGY_LOCK]** Gap: differential dataflow assumes *deterministic, functional* operators; agent reasoning is *stochastic*. Mapping "incremental view maintenance" → "belief update" imports a purity assumption stochastic reasoning breaks. Name: **operator-determinism assumption** (the sharpest gap in this run).
- **[IMPLEMENTATION_COST_ANCHOR]** Same Rust cross-language cost as #8, *plus* trace-storage memory overhead. The *concept* — key outputs by (input-version, time) and reuse on unchanged deterministic inputs — is portable and cheap; the engine is not worth cross-language cost for an agent loop.
- **[EPISTEMIC_DELTA:** H1 FALSIFIED for stochastic tasks / CONFIRMED for deterministic-subtask memoization. H2 FALSIFIED for small workflows (benefit only at scale). H3 FALSIFIED as general (monotone-loop niche only).**]
- **Self-reflexive check:** Representable ◐ (diff traces are heavy state). I/O stable ✖ for stochastic ops. Benefit > cost ✖ except deterministic-at-scale. Survives runtime change ✖ (determinism assumption).

---

### 10. `nickovic/rtamt` — Signal Temporal Logic runtime monitoring (Python + C++ backend)
**URL:** https://github.com/nickovic/rtamt
**Observed concept:** Online/offline monitors from STL specs with *quantitative robustness* semantics (how strongly satisfied/violated, not just yes/no), past+future operators, dense- and discrete-time.

- **[HYPOTHESIS_MATRIX:** 1. Hermes encodes SLOs/deadlines as STL ("response within 5s", "resource stays below limit over the whole run") and attaches RTAMT online monitors that stream a robustness score during execution. 2. The *robustness* (real-valued) signal becomes a graded reward/health metric the agent uses to steer — a smooth "how close to violating" gauge rather than a binary alarm. 3. Interface-aware STL (input vs. output vars) lets Hermes monitor contracts *between* sub-agents at their boundaries.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if agent-relevant properties are non-metric/qualitative, where STL's real-valued signals add nothing over LTLf. H2: falsified if robustness requires a numeric signal but agent events are discrete symbols with no natural metric. H3: falsified if the online monitor's bounded-future requirement conflicts with unbounded-horizon agent goals.**]
- **Falsification probe:** Steelman FALSIFY H2 — STL robustness needs a real-valued signal (temperature, latency); agent execution is a symbol stream (tool called / not) with no metric. Criterion met for *purely symbolic* properties → H2 FALSIFIED there, but Hermes *does* emit numeric signals (elapsed time, token spend, retry count, resource use) where robustness is exactly right → re-CONFIRMED for the numeric-signal subset, which covers the high-value deadline/budget class. H1: STL strictly adds metric time over LTLf; for deadline/budget properties LTLf *cannot* substitute → H1 CONFIRMED (STL owns the metric fragment). H3: online STL monitors the *bounded-future* fragment; unbounded liveness can't be online-monitored → criterion met → FALSIFY H3 for unbounded goals (use past-STL / bounded windows instead).
- **[ONTOLOGY_LOCK]** Gap: STL was built for *continuous physical signals* (CPS/robotics); mapping to agent telemetry treats "token spend over time" as a continuous signal — legitimate, but discrete/bursty agent signals need a sampling/hold convention the CPS origin assumes implicitly. Name: **continuous-signal assumption**.
- **[IMPLEMENTATION_COST_ANCHOR]** Python API with optimized C++ discrete-time backend — in-process, low per-sample cost, designed for online use (ROS/Simulink integrations prove automation-stability). Far cheaper and more informative than an LLM judging "are we within budget?"; the robustness gradient is a *free* steering signal.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (STL owns metric-time deadline/budget properties). H2 CONFIRMED for numeric telemetry (FALSIFIED for purely symbolic). H3 FALSIFIED for unbounded liveness (use bounded/past fragment).**]
- **Self-reflexive check:** Representable ✔ (robustness = scalar in state). I/O stable ✔ (numeric stream in, robustness out). Benefit > cost ✔ (graded steering signal). Survives runtime change ✔ (spec is model-agnostic).

---

### 11. `anand-bala/signal-temporal-logic` — STL quantitative semantics library (C++ + Python bindings)
**URL:** https://github.com/anand-bala/signal-temporal-logic
**Observed concept:** A focused, embeddable library for STL formulas and their quantitative semantics with clean Python bindings — lighter-weight than a full monitoring framework.

- **[HYPOTHESIS_MATRIX:** 1. Hermes embeds this as the *minimal* STL robustness kernel when it wants scoring without RTAMT's monitoring-framework surface. 2. The library's AST for STL formulas becomes Hermes' internal, serializable representation of quantitative temporal specs (portable across sessions). 3. Offline batch scoring of completed-run traces feeds a post-hoc "how healthy was this run" audit for the fossilization log.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if the library only supports offline (not online) evaluation, blocking in-loop steering. H2: falsified if the formula AST is not stably serializable/deserializable for cross-session persistence. H3: falsified if it duplicates #10 with no distinct advantage (redundant integration).**]
- **Falsification probe:** Steelman FALSIFY H3 — this overlaps RTAMT; adopting both is redundant surface area. Criterion (no distinct advantage) partially holds, *but* the advantage is *weight*: a small embeddable kernel with Python bindings is a lower-integration-cost choice when only offline/batch robustness scoring is needed, whereas RTAMT is the online-monitoring choice → H3 FALSIFIED (they occupy different cost/capability points; pick per need). H1: it centers on quantitative semantics; online support is weaker than RTAMT → criterion partly met → for *online steering* prefer #10; for *offline audit* this suffices → H1 CONFIRMED for the offline-audit role. H2: an STL AST is inherently serializable (tree of operators) → criterion fails → CONFIRM H2.
- **[ONTOLOGY_LOCK]** Same continuous-signal assumption as #10; additionally the "library not framework" framing means Hermes owns the trace-plumbing — mapping "agent trace" → "STL signal" is the integrator's responsibility, not the library's.
- **[IMPLEMENTATION_COST_ANCHOR]** Lowest-cost STL entry point: header-lib + Python bindings, in-process, no framework. For offline audit scoring it beats RTAMT on integration cost; for online monitoring RTAMT beats it on capability. Choose by axis.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED for offline-audit robustness scoring. H2 CONFIRMED (serializable STL AST as spec format). H3 FALSIFIED (distinct low-weight niche vs. #10).**]
- **Self-reflexive check:** Representable ✔. I/O stable ✔ (AST serializes). Benefit > cost ✔ for offline audit. Survives runtime change ✔.

---

### 12. `AlexandreDecan/sismic` — Statechart (SCXML) interpreter with controllable clock
**URL:** https://github.com/AlexandreDecan/sismic
**Observed concept:** Executes statecharts with a *controllable simulation clock* (real or simulated time), delayed events, guards/actions in Python, plus design-by-contract invariants on states/transitions.

- **[HYPOTHESIS_MATRIX:** 1. Hermes models its own control flow as a statechart, gaining explicit states, guarded transitions, and *delayed events* — a principled alternative to implicit LLM-driven control. 2. The *simulated clock* lets Hermes dry-run time-dependent workflows (timeouts, retries-after-delay) deterministically and fast, decoupled from wall-clock. 3. Sismic's design-by-contract (invariants/pre/post on states) gives Hermes per-state runtime assertions that fail loudly on control-flow corruption.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if agent control flow is too open-ended to fit a finite statechart (states can't be enumerated ahead of time). H2: falsified if the simulated clock cannot be advanced faithfully when transitions depend on external I/O whose timing is unknown. H3: falsified if DbC contracts can't reference the semantic content agents care about (only structural state).**]
- **Falsification probe:** Steelman FALSIFY H1 — agent behavior is emergent; forcing it into a pre-declared statechart defeats the flexibility that makes agents useful. Criterion (states not enumerable) holds for *open-ended reasoning*, but Hermes' *deterministic workflow* layer is exactly a finite control skeleton — statecharts fit the harness's orchestration layer even if not the reasoning layer → H1 CONFIRMED for the orchestration layer (scar: "statechart the harness, not the thought"). H2: simulated clock advances cleanly for *internal* delays; external-I/O timing must be injected as events — criterion partly met but standard (mock the clock, feed events) → CONFIRM H2 with an event-injection convention. H3: DbC on statechart state is *structural*; semantic ("is the output correct?") contracts need external evaluators — criterion met → FALSIFY H3 for semantic contracts, keep for structural control-flow invariants.
- **[ONTOLOGY_LOCK]** Gap: statecharts assume *discrete, well-defined modes*; agent cognition is continuous/latent. Mapping "statechart state" → "agent phase" is faithful for the *harness's* orchestration modes and metaphorical for the *model's* internal reasoning. Pure-Python, so the fit for the harness layer is literal.
- **[IMPLEMENTATION_COST_ANCHOR]** Pure-Python, in-process, `pip install sismic` — the lowest-friction integration in this run. Simulated clock makes time-dependent logic *testable without waiting*, a large win vs. wall-clock-bound LLM retry loops. Cost ≪ any subprocess tool here.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (statechart the orchestration/harness layer). H2 CONFIRMED (simulated clock + event injection for deterministic dry-runs — high value for long-horizon retry/timeout logic). H3 FALSIFIED for semantic contracts / CONFIRMED for structural control-flow DbC.**]
- **Self-reflexive check:** Representable ✔ (statechart config = explicit state). I/O stable ✔ (events in, state out). Benefit > cost ✔ (pure-Python, testable time). Survives runtime change ✔ (harness layer is LLM-agnostic).

---

### 13. `ticktac-project/tchecker` — Timed automata verifier (zones / DBMs)
**URL:** https://github.com/ticktac-project/tchecker
**Observed concept:** C++17 library + tools for timed automata: zone graphs via Difference Bound Matrices, reachability and liveness over *dense real time* with clock constraints — the canonical way to reason about deadlines and timing windows exactly.

- **[HYPOTHESIS_MATRIX:** 1. Hermes models deadline-laden workflows as timed automata and uses reachability to *prove* a schedule meets all timing windows before running it. 2. The DBM/zone abstraction (not the tool) is borrowed as a compact representation of *sets* of feasible timings, letting the agent reason about "any timing in this window works" rather than enumerating instants. 3. `tck-liveness` checks that a long-horizon workflow can't get stuck waiting forever (no timelock).**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if real workflow timing is stochastic (distributions) rather than the bounded nondeterminism timed automata assume. H2: falsified if DBM zones can't be represented/manipulated inside the agent without the C++ library. H3: falsified if constructing the timed-automaton model requires manual expertise incompatible with automation.**]
- **Falsification probe:** Steelman FALSIFY H1 — task durations are random variables with tails; timed automata model *intervals* [lo,hi], not distributions, so they can't reason about "95th-percentile latency". Criterion met → H1 FALSIFIED for probabilistic timing, re-CONFIRMED for *hard-bound* timing (SLA ceilings, hard timeouts) where interval semantics are exactly the right, conservative model. H2: DBMs are a well-documented data structure reproducible in any language; criterion (can't reproduce without the lib) fails → CONFIRM H2 as an adoptable representation, though the *library's* optimized extrapolations are non-trivial to match. H3: authoring timed automata is expert work with no auto-synthesis here → criterion met → FALSIFY H3 (manual modeling barrier).
- **[ONTOLOGY_LOCK]** Gap: timed automata assume *clocks that advance uniformly and are read exactly*; agent "time" includes queueing, external-service latency, and pauses that aren't clean clocks. Mapping "automaton clock" → "wall-clock elapsed" imports an idealized-clock assumption. Name: **ideal-clock assumption**.
- **[IMPLEMENTATION_COST_ANCHOR]** Compiled C++ subprocess; verification is fast for small automata but zone graphs can blow up. Cross-process modeling cost is real and expert-gated. Justified only for *safety-critical timing* on reused workflow templates — comparable to #4's cost profile. The DBM *concept* is cheap; the *verifier* is not.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED for hard-bound timing (FALSIFIED for stochastic/percentile timing). H2 CONFIRMED (DBM/zone as a feasible-timing-set representation). H3 FALSIFIED (manual modeling barrier, no auto-synthesis).**]
- **Self-reflexive check:** Representable ◐ (zones representable; extrapolation logic heavy). I/O stable ✔ (reachability verdict + trace). Benefit > cost ◐ (safety-critical templates only). Survives runtime change ◐ (ideal-clock assumption).

---

### 14. `ticktac-project/tcltl` — LTL model checker for timed automata (TChecker + Spot)
**URL:** https://github.com/ticktac-project/tcltl
**Observed concept:** Composes #13 (timed automata) with LTL (via Spot) to check *temporal-logic liveness/safety properties over timed systems* — i.e., "eventually X, and always within the timing constraints."

- **[HYPOTHESIS_MATRIX:** 1. Hermes states combined qualitative+timed properties ("the deploy eventually succeeds AND tests always finish before deploy starts within the window") and checks them in one pass. 2. The *composition pattern itself* (timed-automaton engine ⊗ LTL engine) is the reusable lesson: Hermes should layer a qualitative-logic checker over a timing model rather than pick one. 3. tcltl becomes the verification backend for Hermes' highest-stakes, timing-sensitive workflow templates.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if combined timed-LTL checking inherits *both* parents' scalability limits (state explosion × zone explosion), making it intractable. H2: falsified if the two-tool composition is fragile (version-coupled TChecker+Spot) and breaks automation. H3: falsified if no Hermes property genuinely needs *both* metric time and qualitative liveness simultaneously (i.e., #10 or #13 alone suffices).**]
- **Falsification probe:** Steelman FALSIFY H1 — combining model checkers multiplies state spaces; timed-LTL is among the most expensive verification classes, so it's tractable only for tiny models. Criterion met → H1 FALSIFIED at scale, CONFIRMED only for *small, high-value* control skeletons — which is acceptable because verification targets templates, not runs. H2: it explicitly depends on two coupled projects (TChecker + Spot); criterion (fragile composition) is materially met → FALSIFY H2 as a *robust automation dependency*, keep as an *offline expert* tool. H3: many Hermes properties are *either* timed *or* qualitative; needing *both at once* is rarer than assumed → criterion partly met → DEFER until a genuine joint-property case arises (avoid premature integration).
- **[ONTOLOGY_LOCK]** Inherits both #3's infinite-trace (ω-LTL vs. finite runs) and #13's ideal-clock gaps *simultaneously* — the joint mapping compounds two idealizations, so the abstraction is the most fragile in this run. Name it explicitly: **compounded ω-trace × ideal-clock gap**.
- **[IMPLEMENTATION_COST_ANCHOR]** Highest integration cost in the run: two compiled tools, version-coupled, subprocess-invoked, expert-authored models. Only justifiable for the rare workflow where a timing violation *and* a liveness violation are both catastrophic. Cost ≫ using #10 (STL) or #13 (timed reachability) singly.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED for small high-value skeletons (FALSIFIED at scale). H2 FALSIFIED as a robust automated dependency (offline-expert use only). H3 DEFERRED (no confirmed joint-property need yet — resist premature synthesis).**]
- **Self-reflexive check:** Representable ◐. I/O stable ◐ (two-tool coupling). Benefit > cost ✖ for now (deferred). Survives runtime change ✖ (compounded assumptions).

---

### 15. `1123/bitemporaldb` — Bitemporal database layer (valid-time × transaction-time)
**URL:** https://github.com/1123/bitemporaldb
**Observed concept:** Stores objects along *two* time axes — *valid time* (when a fact is true in the world) and *transaction time* (when the system knew it) — so history and "what we believed when" are both queryable.

- **[HYPOTHESIS_MATRIX:** 1. Hermes stores its beliefs/facts bitemporally so it can answer "what did I know at step N, and what was actually true then?" — separating knowledge-revision from world-change, the exact distinction LLMs collapse. 2. Transaction-time gives Hermes deterministic *rollback/replay*: reconstruct the agent's exact epistemic state at any past decision point for debugging (the FIREBEARER scar log). 3. Valid-time lets the agent reason about facts with future/expiring validity ("this credential is valid until T") natively rather than re-checking each step.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if the two-axis model is overkill and a single append-only event log gives the same replay ability more cheaply. H2: falsified if bitemporal query semantics are too complex to drive reliably from the agent loop. H3: falsified if the specific repo (Scala/MongoDB layer) is too tied to its stack to reuse as a pattern.**]
- **Falsification probe:** Steelman FALSIFY H1 — an append-only event log already supports replay; the *transaction-time* axis seems redundant. Criterion (single log suffices) holds for pure replay, *but* the decisive value is the **valid-time × transaction-time separation**: a plain log conflates "the fact changed" with "we corrected our belief about the fact," and that conflation is precisely the epistemic error LLMs make. Bitemporality structurally prevents it → H1 CONFIRMED for the *conceptual model* (not necessarily this implementation). H2: full bitemporal SQL is complex, but the *two-timestamp-pair-per-fact* schema is simple to adopt without a full bitemporal query engine → criterion partly met → CONFIRM the schema, DEFER the query engine. H3: this specific repo is a Scala/MongoDB layer — criterion (stack-tied) met → FALSIFY H3 (adopt the *pattern*, not the code; it's a reference, not a dependency).
- **[ONTOLOGY_LOCK]** Gap — the cleanest human-skill transfer in this run: bitemporality is the *accountant's / historian's* discipline of distinguishing "what happened" from "what we recorded/knew." Mapping "database record" → "agent belief" is faithful because both are *revisable knowledge about a changing world* — the abstraction survives with almost no gap; only the storage substrate differs.
- **[IMPLEMENTATION_COST_ANCHOR]** Adopting the *schema* (4 timestamp columns / two interval pairs per fact): near-zero, works in any store Hermes already uses. Adopting *this repo*: mismatched (Scala/MongoDB) — reference only. So cost of the valuable part is negligible; cost of the code is avoided.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (adopt bitemporal knowledge model — separate valid-time from transaction-time in the belief store; highest cross-domain-skill takeaway). H2 CONFIRMED for the schema / DEFERRED for a full bitemporal query engine. H3 FALSIFIED (repo is stack-tied; use as pattern reference, not dependency).**]
- **Self-reflexive check:** Representable ✔ (two interval pairs per fact). I/O stable ✔ (schema). Benefit > cost ✔ (schema is nearly free, replay/audit is high-value). Survives runtime change ✔ (model is substrate-independent).

---

## [HARNESS_HERMES]

Synthesizing only CONFIRMED hypotheses, three integration tiers emerge, ordered by benefit-to-cost. The recurring, decisive pattern across this run: **adopt formal temporal *concepts and schemas* natively into the harness's own language; invoke *compiled verifiers* only as offline gates on reused, high-stakes workflow templates.** The single sharpest abstraction gap surfaced repeatedly — the **operator-determinism / effect-purity assumption**: nearly every formal tool assumes pure, deterministic transitions, while LLM-backed tasks are stochastic. This bounds all caching/incremental/verification claims to the *deterministic sub-task* subset and must be respected as a standing constraint (Symbolic Scar SS-1).

**Tier A — Near-free native concept/schema adoptions (in-process, LLM-agnostic, high leverage):**
- Allen 13-relation vocabulary as the canonical task-dependency schema (#1), fed by a trace→relation abstraction layer (#2).
- Durative-action contract shape `at start / over all / at end` as the universal tool-contract template (#6).
- Bitemporal knowledge model — separate valid-time from transaction-time in the belief/fossilization store, enabling deterministic replay and "what I knew when" audit (#15). *Highest cross-domain human-skill transfer.*
- Frontier / progress-tracking invariant for fan-out/fan-in completion detection (#8, concept only).
- Statechart orchestration layer with a *simulated clock* for deterministic dry-runs of timeout/retry logic (#12).

**Tier B — Lightweight in-process runtime monitors (deterministic steering signals):**
- LTLf qualitative invariants compiled to small automata as always-on safety/liveness monitors (#3, finite-trace semantics).
- STL robustness monitors over numeric telemetry (elapsed time, token/budget spend, retries) — online steering via RTAMT (#10) and offline run-audit scoring via the lightweight STL kernel (#11).

**Tier C — Offline verification gates on reused, high-stakes workflow templates (compiled subprocess, expert-gated):**
- TLA+/TLC to verify the *control skeleton* (never the data) of critical workflow classes for deadlock/invariant safety (#4, under SS-1 abstraction discipline).
- Temporal planning (via the aig-upf wrapper #7, backed by TFD #6) to synthesize schedules for the deterministic, sequential-with-optional-overlap workflow subset.
- Timed-automata reachability (#13) for hard-bound deadline verification on safety-critical templates.
- SPIN partial-order-reduction *principle* (#5) for pruning independent-action interleavings once true concurrency exists.
- Differential-dataflow memoization (#9) reserved for deterministic sub-computations at high fan-out scale only.
- tcltl joint timed-LTL checking (#14) explicitly **deferred** — resist premature synthesis until a genuine joint metric-and-liveness property is on the table.

## [IMPLEMENTATION_WORKFLOW]

**Phase 0 — Scar registration (immediate).** Record SS-1 (operator-determinism/effect-purity boundary) and SS-2 ("verify the control skeleton, never the data") as standing constraints in the FIREBEARER log. All later phases inherit them.

**Phase 1 — Native schemas (lowest cost, no external deps).** Implement in the harness's own language: (a) the Allen 13-relation task-dependency vocabulary (#1); (b) the `at start / over all / at end` tool-contract shape (#6); (c) the bitemporal belief store — two interval pairs per fact (#15). These are additive, testable, and LLM-agnostic. Verification step: unit-test relation exhaustiveness/disjointness and bitemporal replay round-trips.

**Phase 2 — Progress + orchestration.** Add the frontier progress invariant for fan-out/fan-in (#8) and model the deterministic-workflow layer as a Sismic statechart with a simulated clock (#12). Verification step: dry-run timeout/retry workflows under simulated time and assert deterministic outcomes.

**Phase 3 — In-process monitors.** Attach LTLf safety/liveness monitors (#3) and STL robustness monitors over numeric telemetry (#10 online, #11 offline audit). Verification step: inject known-violating traces and confirm monitors flag them with correct robustness sign.

**Phase 4 — Offline verification gates (opt-in, template-scoped).** For reused high-stakes templates only, wire TLA+/TLC skeleton checks (#4) and, where hard deadlines exist, timed-automata reachability (#13); use the temporal-planning wrapper (#7/#6) to synthesize schedules for the deterministic subset. Verification step: confirm each gate rejects a seeded unsafe template and accepts a known-good one; measure subprocess cost against a per-run budget.

**Deferred / not scheduled:** SPIN full integration (#5, await concurrency), differential-dataflow engine (#9, concept-only unless deterministic-at-scale case arises), tcltl (#14, await genuine joint-property need). These remain DEFERRED to avoid DCCD schema-flattening into premature synthesis.

---

*End of PDL:v1.0 trajectory. Deliverable priority honored: the falsification/epistemic-delta trajectory precedes and constrains the workflow; only CONFIRMED hypotheses entered the workflow, DEFERRED ones were held open, and each cross-runtime confirmation carries a comparative cost anchor.*
