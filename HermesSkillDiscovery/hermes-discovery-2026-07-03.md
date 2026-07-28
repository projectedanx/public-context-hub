# Hermes Agent Harness — Integration Discovery Report

**Date:** 2026-07-03
**Sensor:** Paraconsistent Integration Sensor (automated daily run)
**Protocol:** PDL v1.0, full loop, AntiFlattening=True

---

## 1. Chosen AI Problem Space & Rationale

**Chosen space: Formal Process Calculus & Deterministic Concurrency Verification** (Petri nets, CSP/process algebra, temporal-logic model checking, statecharts, constraint satisfaction, replicated state machines).

Rotation rationale: mainstream LLM-era agent frameworks are built on stochastic next-token generation with no first-class notion of decidability, reachability, or exhaustive state coverage. Process calculi and model checkers are the maximal counter-pole — they encode termination, mutual exclusion, deadlock-freedom, and state-space exhaustion as first-class, checkable objects, decades before "agent" meant an LLM loop. This is the widest epistemic gap available this rotation: probabilistic pattern completion vs. decidable state-space exhaustion. It is also directly load-bearing for Hermes's own stated design target — deterministic workflows and long-horizon future-forward tasks — making the isomorphism unusually direct rather than metaphorical.

Excluded by design: LLM, agent (as in "LLM agent"), copilot, RAG — the substrate sought here is pre-AI and formalism-native, not another agent framework to wrap.

---

## 2. Preflight Matrix

| Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term |
|---|---|---|---|---|
| Petri net / marking | forensic scheduling, assembly-line token flow | places/transitions, guard functions | petri-net, editor, simulator | LLM, agent, copilot |
| Process algebra (CSP/CCS) | incident command handoff, chain of custody | channel, process composition | model-checker, CSP, refinement | RAG, LLM |
| Temporal logic (LTL/CTL) | "always eventually," standing orders | Büchi automaton, verifier | model checker, LTL, verification | agent, copilot |
| Constraint satisfaction | union contract scheduling, seating chart | finite-domain solver, propagation | solver, CP-SAT, CSP, toolkit | LLM, RAG |
| Double-entry bookkeeping | forensic accounting, audit trail | ledger grammar, balance invariant | plain-text-accounting, ledger | LLM, agent |
| Forward-chaining production rules | tribal law, standing rule book | Rete network, working memory | rule-engine, expert-system | copilot, RAG |
| Replicated state machine | quorum, chain of command succession | consensus log, leader election | raft, consensus, distributed | LLM, agent |
| Statechart (Harel) | flight-deck checklist state board | hierarchical/parallel states, guards | statechart, state-machine, FSM | copilot, agent |
| Relational model finding | jury instruction counterexample | bounded scope, SAT-backed search | model-finder, relational-logic | LLM, RAG |
| SMT solving | contract feasibility review | theory solver, unsat core | SMT, solver, theorem-prover | agent, copilot |
| Workflow nets (BPM) | guild apprenticeship handoff rules | OR-join, exception service | workflow, BPM, engine | LLM, RAG |
| Stochastic Petri nets | actuarial timing tables | CTMC, P/T-invariant | stochastic-petri-net, SPN | agent, copilot |

---

## 3. Repository Loop — Full PDL Output (15 repositories)

Format per repository: identity → `[HYPOTHESIS_MATRIX]` → `[FALSIFICATION_CRITERIA]` → falsification probe (CB_CONSTRAINT / ANTI_CONFIRMATION_MANDATE applied) → ONTOLOGY_LOCK → IMPLEMENTATION_COST_ANCHOR (where relevant) → `[EPISTEMIC_DELTA]`.

---

### R1. fpom/snakes — SNAKES (Net Algebra Kit for Editors and Simulators)
Python Petri-net library: arbitrary Python objects as tokens, Python expressions as guards, plugin-based net algebra composition.

[HYPOTHESIS_MATRIX: 1. Represent Hermes long-horizon task graphs as executable Petri nets (places=preconditions, transitions=tool calls, tokens=in-flight task instances), replacing static DAG execution with native enabled/fireable-transition concurrency semantics. 2. Use SNAKES's net-algebra composition operators as a formal sub-workflow/subroutine mechanism for composing validated micro-workflows into macro-workflows. 3. Use live marking (place→token multiset) as a self-describing runtime snapshot for crash recovery / mid-workflow resumption.]

[FALSIFICATION_CRITERIA: H1: enabled-transition computation is a full linear scan per step with no incremental index, capping usable net size before step latency degrades. H2: composition flattens to a single non-hierarchical net with no preserved sub-net boundary at runtime. H3: marking history is not persisted by default (only current marking held in memory, no built-in disk serialization).]

Probe: SNAKES is documented as a flexible, general-purpose library, explicitly not optimized for large/hot-loop nets — each transition's guard is re-evaluated against the current marking per step, with no indexed enabled-set cache. This is a real, not hypothetical, ceiling. H1's falsification condition is met at scale but not at Hermes's likely real scale (tens–hundreds of concurrent nodes) — reclassified DEFERRED pending a workload benchmark rather than outright FALSIFIED. SNAKES's plugin system does provide net-algebra composition with sub-nets addressable as substitution-transitions — H2's falsification condition is not met — CONFIRMED. SNAKES's core keeps only the current marking; no transition-history log ships by default — H3's condition is met — FALSIFIED as stated, though the required marking-change callback hook is well-defined and cheap to add.

**ONTOLOGY_LOCK:** "task precondition" (ops term) mapped onto "place with capacity 1" (formal primitive) loses the *reason* a precondition holds — Petri nets encode reachability, not justification. A parallel provenance layer is still required; SNAKES supplies none.

**IMPLEMENTATION_COST_ANCHOR (H2):** pure Python, no compiled dependency; if Hermes core isn't Python, a JSON-RPC-over-stdio bridge is the standard cost — comparable to running a local linter sidecar, low.

[EPISTEMIC_DELTA: H1: DEFERRED (needs workload benchmark). H2: CONFIRMED. H3: FALSIFIED (mitigation path is cheap but not shipped).]

---

### R2. tlaplus/tlaplus — TLC model checker + TLA+ Toolbox
Explicit-state model checker for TLA+ specifications; JVM-based, CLI/CI-invokable.

[HYPOTHESIS_MATRIX: 1. Use TLA+/TLC to formally verify Hermes's own workflow-DAG scheduler for safety (no double-execution) and liveness (every enqueued task eventually completes) as a CI regression gate. 2. Auto-compile a subset of Hermes's workflow DSL into TLA+ so every user-authored workflow gets a free exhaustive deadlock/livelock check pre-execution. 3. Use TLA+ temporal operators (□, ◇) as the native language for Hermes's DAG success/failure postconditions, replacing ad hoc boolean checks.]

[FALSIFICATION_CRITERIA: H1: TLC's state-space exploration is exponential in modeled actor count and cannot check schedulers at Hermes's real actor counts within a CI-viable time budget. H2: TLA+ next-state relations cannot be mechanically derived from an imperative DSL without a full semantic translator (translation cost ≈ writing a second interpreter). H3: TLA+ properties are only checkable over the finite explored state graph, providing no guarantee for genuinely unbounded long-horizon tasks.]

Probe: TLC does explicit-state checking with symmetry reduction; state explosion is real and documented, but for a bounded-actor scheduler core (Hermes's actual scheduler, not arbitrary user workflows) this is typically tractable in CI minutes — H1 CONFIRMED, explicitly scoped to the scheduler core, not arbitrary workflow sizes. No DSL→TLA+ compiler ships with tlaplus/tlaplus and building one is a nontrivial semantics project — H2's condition is met — FALSIFIED as "free." H3's boundedness objection is accurate: TLC verifies bounded instances, not the open class of all possible long-horizon tasks — FALSIFIED as a general claim, though CONFIRMED at the same scoped level as H1 (scheduler-core spec tool).

**ONTOLOGY_LOCK:** "liveness" (□◇P — holds infinitely often) has no idiomatic analogue in agent-harness vocabulary ("should eventually finish"); importing it forces Hermes to define what "infinitely often" means for runs that are finite by construction. Naming this prevents false formal-coverage confidence.

**IMPLEMENTATION_COST_ANCHOR (H1):** TLC runs on JVM 11+, CLI/Maven-invokable — CI cost ≈ adding a Java step, comparable to a linter, low, one-time.

[EPISTEMIC_DELTA: H1: CONFIRMED (scheduler-scoped). H2: FALSIFIED. H3: FALSIFIED (general) / CONFIRMED (scheduler-scoped, same as H1).]

---

### R3. yawlfoundation/yawl — YAWL (Yet Another Workflow Language)
Formally-grounded (Petri-net-derived) BPM engine with worklets/RDR exception handling and OR-join semantics.

[HYPOTHESIS_MATRIX: 1. Adopt YAWL's worklet mechanism (RDR-driven dynamic sub-workflow substitution) as the model for Hermes's adaptive task substitution on sub-plan failure. 2. Use YAWL's OR-join resolution algorithm (a formally hard reachability problem) as a reference algorithm for Hermes's ad hoc "wait for some-but-not-all upstream" nodes. 3. Import YAWL's exception taxonomy (work-item / case / external, each with compensation actions) as Hermes's error classification scheme.]

[FALSIFICATION_CRITERIA: H1: worklet selection requires YAWL's RDR exception service running statefully inside a full YAWL server, non-extractable headlessly. H2: the OR-join algorithm is inseparable from YAWL's full reachability-graph engine, making "reference algorithm" require reimplementation from the paper rather than code reuse. H3: the taxonomy is entangled with YAWL's Java object model (`YWorkItem` hierarchy) such that categories cannot be lifted cleanly.]

Probe: YAWL ships as a full Java BPM server; worklets/RDR are a YAWL-coupled custom service, not a standalone library — H1's condition is met — FALSIFIED as code-reuse, though the rule-driven substitution *design pattern* is independently documented in YAWL's academic papers — DEFERRED as a design import. The OR-join algorithm (van der Aalst et al.) is published as a reachability-graph algorithm, conceptually separable from the engine despite codebase coupling — H2's condition is not met — CONFIRMED as an algorithm-level reference (reimplement, don't vendor). The three-tier exception taxonomy plus compensation model is documented independently of the Java object model — H3's condition is not met — CONFIRMED as a categorical import.

**ONTOLOGY_LOCK:** a YAWL "case" (one workflow instance with OR-join state) assumes a closed-world task set known at design time; Hermes's long-horizon tasks may spawn tasks unknown at authoring time, which YAWL's formal OR-join proof does not cover. Flag, don't silently patch.

**IMPLEMENTATION_COST_ANCHOR:** none — both confirmed items are algorithm/ontology reimplementation, not runtime dependencies; cost is engineering time, not bridging overhead.

[EPISTEMIC_DELTA: H1: FALSIFIED (code-reuse) / DEFERRED (design import). H2: CONFIRMED. H3: CONFIRMED.]

---

### R4. python-constraint/python-constraint — finite-domain CSP solver
Backtracking/min-conflicts solvers over finite-domain constraint satisfaction problems, pure Python.

[HYPOTHESIS_MATRIX: 1. Use as backend for Hermes's task-scheduling/resource-allocation layer, replacing greedy heuristics with a provably-valid CSP-derived schedule. 2. Use the declarative `Constraint` class as a standalone validator that checks a proposed plan (regardless of origin, including LLM-generated) against hard constraints before execution. 3. Use arc-consistency domain reduction as a pre-filter that prunes an LLM's action space before sampling, reducing hallucinated-but-infeasible tool calls at generation time.]

[FALSIFICATION_CRITERIA: H1: backtracking search is worst-case exponential with no timeout/anytime fallback, risking a hang on a single hard instance. H2: constraint-checking requires the full CSP model constructed, not a candidate assignment checkable in isolation. H3: only full-solve APIs are exposed, with no intermediate arc-consistency step accessible pre-sampling.]

Probe: solvers expose `forwardcheck` but no wall-clock timeout or anytime degrade — H1's condition is met — FALSIFIED. `Constraint.__call__` is designed for invocation during the solver's search loop, with no public single-shot "validate this complete assignment" entrypoint — H2's condition is met — FALSIFIED as "independent of generation," though a ~20-line manual wrapper (call each constraint over the full assignment) is a cheap mitigation — DEFERRED. No exposed intermediate consistency-pruning API exists publicly (only full backtracking or local search) — H3's condition is met — FALSIFIED.

**ONTOLOGY_LOCK:** "resource conflict" maps cleanly onto CSP's all-different family, but Hermes's resources (rate limits, token budgets) are consumable and time-decaying, not binary-occupied — the CSP model silently assumes static capacity, which is false for rate-limited APIs.

**IMPLEMENTATION_COST_ANCHOR:** none confirmed directly; if the DEFERRED H2 workaround is pursued, cost is near-zero (pure Python, no compiled dependency).

[EPISTEMIC_DELTA: H1: FALSIFIED. H2: FALSIFIED (as stated) / DEFERRED (cheap workaround). H3: FALSIFIED.]

*Negative result carried forward — see R15 (OR-Tools) for a direct mitigation.*

---

### R5. smarr/CLIPS — CLIPS expert-system shell
Forward-chaining production system built on the Rete algorithm; `deftemplate` facts, salience-based conflict resolution.

[HYPOTHESIS_MATRIX: 1. Use CLIPS's Rete network as Hermes's live working memory (event-driven fact assert/retract triggering rule firing) replacing polling-based agent loops. 2. Use CLIPS's conflict-resolution strategies (depth, breadth, LEX, MEA, salience) as a portable vocabulary/algorithm set for choosing among multiple eligible next actions. 3. Embed CLIPS as a subprocess for pure fact-pattern-matching subtasks (e.g., failure-signature detection over tool-call traces), leveraging Rete's sub-linear incremental matching.]

[FALSIFICATION_CRITERIA: H1: Rete's incremental match assumes a closed, enumerable fact schema fixed at compile time, incompatible with dynamically-typed LLM-generated facts. H2: conflict-resolution logic is hard-coded to CLIPS's internal "activation" structure and cannot be extracted for an externally-defined action-candidate list. H3: CLIPS exposes no machine-readable batch/API I/O mode, requiring fragile REPL screen-scraping for subprocess embedding.]

Probe: `deftemplate` schemas are statically declared, but CLIPS also supports unordered facts, multifield slots, and templates dynamically defined at load time from generated `.clp` text — "closed schema" is a soft, not hard, constraint — H1's condition is not fully met — DEFERRED (workable via generated-template codegen, added complexity, not disqualifying). Conflict-resolution strategy semantics (salience, LEX/MEA ordering) are documented, portable algorithmic vocabulary independent of Rete internals — H2's condition is not met — CONFIRMED as an ontology import. CLIPS provides batch execution and Python bindings (`clipspy`), a genuine scriptable I/O surface — H3's condition is not met — CONFIRMED, via `clipspy` specifically, not raw REPL scraping.

**ONTOLOGY_LOCK:** "rule salience" (human-authored priority hint) is not the same primitive as an LLM's implicit token-probability preference — collapsing "highest salience" onto "highest model confidence" is a category error; keep separate namespaces.

**IMPLEMENTATION_COST_ANCHOR (H3):** `clipspy` gives Python bindings directly; for non-Python cores, CLIPS's C API needs a compiled FFI bridge — moderate, comparable to embedding SQLite via FFI.

[EPISTEMIC_DELTA: H1: DEFERRED. H2: CONFIRMED. H3: CONFIRMED.]

---

### R6. nimble-code/Spin — SPIN model checker
Explicit-state LTL model checker for Promela; 2002 ACM System Software Award; includes Modex (C-model extraction) and Swarm (parallel verification).

[HYPOTHESIS_MATRIX: 1. Model Hermes's multi-agent message-passing protocol in Promela and use SPIN's exhaustive search plus swarm verification to catch protocol-level deadlocks/races pre-production. 2. Use SPIN's LTL-to-Büchi-automaton translation to compile Hermes's "always eventually" guarantees into live runtime monitors, not just offline verification. 3. Use nimble-code/Modex's C-model-extraction technique as a template for extracting a Promela-like model directly from Hermes's own workflow DSL, giving verification without hand-written specs.]

[FALSIFICATION_CRITERIA: H1: Promela's fixed-capacity, statically-typed channel model cannot represent Hermes's dynamically-typed, schema-evolving messages without a lossy abstraction that could hide the races being checked for. H2: SPIN's LTL translator only emits verifier code coupled to Promela's own `pan.c` execution model, with no standalone Büchi-automaton export for external runtime monitors. H3: Modex's extraction is fundamentally C/pthreads-specific with no generalizable technique for a different host language.]

Probe: Promela channels do require declared types and fixed capacities, forcing abstraction of dynamic payloads to type tags — a standard, not disqualifying, model-checking technique, but the residual risk (abstraction hiding real races) is genuine and must be actively managed — H1 → DEFERRED, not cleanly confirmed. SPIN's LTL-to-Büchi translation is embedded in the `pan.c` offline-verifier generation pipeline with no decoupled export for online monitoring — H2's condition is met — FALSIFIED. Modex's own documentation confirms it is irreducibly C/pthreads-specific — H3's condition is met — FALSIFIED.

**ONTOLOGY_LOCK:** SPIN "deadlock" means no enabled transition in the global state — a structural property. Hermes's colloquial "the agent is stuck" often means an LLM call succeeded but returned an unusable answer — a semantic, not structural, failure. Importing SPIN's deadlock detector will not catch this; conflating the two would be a governance failure for a project centered on epistemic validation.

**IMPLEMENTATION_COST_ANCHOR (DEFERRED H1):** `pan.c` is C-generated-and-compiled, invoked offline in CI — cost is a build step (gcc), comparable to a static analyzer, no production runtime coupling.

[EPISTEMIC_DELTA: H1: DEFERRED. H2: FALSIFIED. H3: FALSIFIED.]

*Negative result — no direct mitigation identified elsewhere in this survey; flagged for a future rotation focused on runtime monitor synthesis specifically.*

---

### R7. ledger/ledger — Ledger CLI (plain-text double-entry accounting)
Stateless batch report generator reading flat-text journals; BSD-licensed, since 2003.

[HYPOTHESIS_MATRIX: 1. Adopt double-entry's balanced-transaction invariant as Hermes's resource-consumption audit model, making budget drift structurally detectable rather than requiring separate reconciliation. 2. Reuse Ledger's plain-text journal grammar itself as Hermes's canonical long-horizon execution-log format — diffable, git-friendly, human-auditable. 3. Use Ledger's typed-commodity system to track incommensurable resources (tokens, dollars, wall-clock seconds) side by side in one ledger.]

[FALSIFICATION_CRITERIA: H1: balance-checking is purely offline/batch (no streaming/incremental invariant-check API), requiring re-implementation of incremental checking to claim "structurally detectable" live. H2: the grammar cannot represent non-monetary, non-numeric events without abusing the amount field, making the format lossy or dishonest. H3: cross-commodity reports require a defined conversion path to a base currency, forcing a fictitious exchange rate for genuinely incommensurable resources.]

Probe: Ledger's own documentation states "there is no other database or stored state" — it is explicitly batch/stateless — H1's condition is met — FALSIFIED as streaming, CONFIRMED only as periodic batch reconciliation (still valuable, narrower claim). The grammar natively supports non-currency commodities (hours, shares) as first-class quantities via tags/metadata, not an abuse of the amount field — H2's condition is not met — CONFIRMED. Ledger can report multiple commodities side by side unconverted ("3.2 hours, $4.10, 900 tokens") without forcing a common unit — H3's condition is not met for per-commodity breakdowns, only for single-number aggregates — CONFIRMED with caveat.

**ONTOLOGY_LOCK:** double-entry "balance" is a closed-world conservation law (money moves, doesn't vanish). Token/API costs are consumed, not conserved — using double-entry form for a consumption-only resource is a deliberate, honest fiction (debit consumption / credit a sink account) and must be documented as a modeling choice, not presented as a literal accounting identity.

**IMPLEMENTATION_COST_ANCHOR (H2/H3):** CLI tool over flat text — zero runtime coupling; Hermes writes ledger-format text and optionally shells out for reports — near-zero cost.

[EPISTEMIC_DELTA: H1: FALSIFIED (streaming) / CONFIRMED (batch). H2: CONFIRMED. H3: CONFIRMED with caveat.]

---

### R8. MiniZinc/libminizinc — MiniZinc compiler
Solver-independent constraint modeling language compiling to FlatZinc, targetable at Gecode, Chuffed, OR-Tools, CBC, and others.

[HYPOTHESIS_MATRIX: 1. Adopt MiniZinc as a solver-agnostic IR for Hermes's planning problems, letting Hermes swap backend solvers by problem size/deadline without rewriting the model. 2. Adopt the `.mzn`/`.dzn` model/data separation as the architectural pattern for Hermes's own workflow-template system (template = model, run parameters = data). 3. Use MiniZinc's global-constraint library (all_different, cumulative, circuit) as a source of pre-validated scheduling idioms for Hermes's resource-allocation planning.]

[FALSIFICATION_CRITERIA: H1: FlatZinc compilation is solver-specific in practice, requiring materially different source per backend rather than a flag change. H2: the model/data split has no analogous clean separation available in Hermes's actual workflow DSL, blocking transfer without a DSL refactor. H3: invoking global constraints requires committing to the full MiniZinc toolchain even for narrow, simple use cases.]

Probe: the same `.mzn` model does run across registered backends with only a solver-selection flag in the common case; solver-specific annotations exist but are opt-in performance tuning, not mandatory — H1's condition is not met — CONFIRMED, with the annotation caveat noted. Hermes's actual workflow-DSL internals are not available to this sensor, so H2's transferability claim cannot be verified either way — DEFERRED, blocked on missing internal access rather than on MiniZinc's design. The global-constraint *algorithms* are published, standard OR literature independent of MiniZinc, portable without the full toolchain even though MiniZinc's own implementations require the compiler — H3's condition is not met for the idiom itself — CONFIRMED as an idiom-reference (reimplement key constraints natively).

**ONTOLOGY_LOCK:** none of note — model/instance separation is a clean, well-understood abstraction with no human-domain mismatch.

**IMPLEMENTATION_COST_ANCHOR (H1):** C++-compiled toolchain invoked via CLI or C++ API — cost ≈ shelling out to a compiled binary (like `ffmpeg`), low operational cost, moderate packaging cost.

[EPISTEMIC_DELTA: H1: CONFIRMED. H2: DEFERRED (blocked on internal access). H3: CONFIRMED (as idiom-reference).]

---

### R9. AlloyTools/org.alloytools.alloy — Alloy Analyzer
Relational logic + bounded exhaustive search via SAT; MIT-licensed, JVM-based.

[HYPOTHESIS_MATRIX: 1. Use Alloy to design-check Hermes's own data model (e.g., mutually exclusive states, cycle-freedom) pre-implementation via bounded exhaustive search. 2. Use Alloy specs as executable, checkable documentation of Hermes's workflow-DSL invariants, version-controlled and CI-re-run on DSL changes. 3. Use Alloy's instance visualizer as a general debugging aid for arbitrary Hermes runtime states, not just Alloy-internal solve output.]

[FALSIFICATION_CRITERIA: H1: bounded scope systematically misses violations only manifesting at larger scale, with no small-scope justification for Hermes's model, giving false confidence. H2: Alloy models require substantial independent re-authoring on every DSL grammar change, with no mechanical sync, letting documentation silently rot. H3: the visualizer only operates on Alloy-internally-generated instances, with no public API for loading externally-produced instances.]

Probe: Alloy's small-scope hypothesis (most bugs have small counterexamples) is its own founding, empirically-supported claim for design-level structural bugs — but Alloy is deliberately unsound beyond the checked scope, sound only for finding bugs within it, never for proving their absence — H1 CONFIRMED strictly as a bug-finding tool, explicitly not as a proof tool; this distinction must be preserved. No standard mechanical extraction path exists from an arbitrary external DSL grammar to an Alloy model — sync is manual — H2's condition is met — FALSIFIED as mechanical, DEFERRED as manual-but-valuable-if-maintained. The visualizer accepts externally-loaded XML instance files, not solely Alloy-internal output — H3's condition is not met — CONFIRMED, contingent on writing a Hermes-state→Alloy-XML exporter.

**ONTOLOGY_LOCK:** an Alloy "counterexample" is a flat relational instance satisfying all constraints but one — purely logical, no causal narrative. A human's intuitive "counterexample" often carries "this happened because..." that Alloy does not provide; the visualizer shows *what*, not *why* — must not be presented as causal explanation.

**IMPLEMENTATION_COST_ANCHOR (H1/H3):** JVM 17+ standalone jar with bundled SAT solver — CI cost ≈ a JVM step, comparable to the TLA+ integration (R2); no production runtime coupling (design-time/offline).

[EPISTEMIC_DELTA: H1: CONFIRMED (bug-finding, not proof). H2: FALSIFIED (mechanical) / DEFERRED (manual). H3: CONFIRMED.]

---

### R10. Z3Prover/z3 — Z3 Theorem Prover
SMT solver (MIT-licensed, Microsoft Research); official Python/C/Java/.NET bindings.

[HYPOTHESIS_MATRIX: 1. Use Z3 as a runtime oracle checking feasibility of an LLM-proposed multi-step plan against declared resource/precondition SMT constraints before committing to execution. 2. Use Z3's incremental (push/pop) solving to maintain a live, continuously-updated world-state constraint model across a long-horizon task, querying cheaply per step rather than re-solving from scratch. 3. Use Z3's unsat-core extraction as a root-cause explainer when a plan is rejected, returning the minimal conflicting constraint subset instead of a bare "no valid plan."]

[FALSIFICATION_CRITERIA: H1: the theories Hermes actually needs (strings for API parameter validation, nonlinear arithmetic for probabilistic budgets) fall outside Z3's efficiently-decidable fragments, forcing timeouts/unknowns on the queries that matter most. H2: incremental solving's cost savings degrade to negligible as assertion count grows across a long session, undermining the "cheap per-step" claim. H3: unsat-core extraction only works reliably for propositional constraints and degrades to large/non-minimal cores for richer theories (arrays, quantifiers).]

Probe: Z3 does support strings and nonlinear arithmetic, but both are documented hard fragments where Z3 can return `unknown` rather than a definitive answer — a real, not hypothetical, limitation — H1 → DEFERRED, confirmed for the linear-arithmetic/boolean subset, genuinely uncertain for the string/nonlinear subset (a fallback for `unknown` must be designed). Incremental solving with internal lemma-reuse across contexts is Z3's core design strength, empirically validated in industrial interactive-verifier use over hours-long sessions — H2's condition is not met — CONFIRMED. Unsat cores are supported across Z3's full theory set, but minimality is only guaranteed if explicitly requested (extra solving cost); the unrequested default core is "an" unsat core, not necessarily minimal — H3's condition is partially met — CONFIRMED with caveat.

**ONTOLOGY_LOCK:** "unsatisfiable" is a purely logical property of a formula set; a plan being logically infeasible given stated constraints says nothing about whether the constraints were correctly elicited from the world. Z3 cannot detect "your model of reality is wrong," only "your model of reality, as stated, is self-contradictory" — the single most important gap for an epistemic-validation-centered project to hold onto.

**IMPLEMENTATION_COST_ANCHOR (H2/H3):** official bindings across major languages plus a CLI reading SMT-LIB2 — cost ≈ a single native-library dependency (like SQLite/libssl), low for Python/C-family cores, moderate FFI cost otherwise.

[EPISTEMIC_DELTA: H1: DEFERRED (scoped to decidable subset). H2: CONFIRMED. H3: CONFIRMED with caveat.]

---

### R11. apache/incubator-kie-optaplanner — OptaPlanner
JVM metaheuristic constraint solver (tabu search, simulated annealing, late acceptance) for vehicle routing, rostering, scheduling.

[HYPOTHESIS_MATRIX: 1. Use the planning-entity/planning-variable/constraint-provider pattern (incremental score calculation, hard+soft constraints) as the model for Hermes's resource-to-agent assignment. 2. Use OptaPlanner's local-search metaheuristics as a tested algorithm library for re-optimizing an in-flight long-horizon schedule when new constraints arrive mid-run. 3. Use Constraint Streams as a lightweight, standalone declarative policy-scoring DSL separate from full optimization.]

[FALSIFICATION_CRITERIA: H1: incremental scoring requires a closed, statically-declared Java POJO object graph, incompatible with dynamically-shaped LLM-generated task objects. H2: the solving loop is a single blocking batch call with no supported pause/inject-constraints/resume-from-best API. H3: Constraint Streams require the full solver runtime (JVM, planning-entity annotations) to evaluate even a single constraint in isolation.]

Probe: the planning-entity model does require `@PlanningEntity`/`@PlanningVariable` Java annotations on POJOs — genuinely static, compile-time-declared, real friction for dynamic LLM-generated objects requiring an adapter layer — H1's condition is met — FALSIFIED as direct fit, DEFERRED as usable-behind-an-adapter. OptaPlanner documents a `ProblemFactChange`/daemon-mode API for injecting changes into a running solver and continuing from the best-known solution — genuine online replanning exists — H2's condition is not met — CONFIRMED. Constraint Streams compile into the solver's incremental score calculator and are not usable standalone outside a `SolverFactory`-constructed instance — H3's condition is met — FALSIFIED.

**ONTOLOGY_LOCK:** OptaPlanner's "score" (hard/soft violation counts) is a closed-world optimization metric — it cannot represent genuine uncertainty (an LLM's calibrated confidence a plan will work), only preference. Conflating "low score" with "low confidence" misrepresents two different epistemic categories — precisely the category error the user's semantic-integrity framework is designed to catch; named explicitly here.

**IMPLEMENTATION_COST_ANCHOR (H2):** JVM-only, no non-Java bindings; a non-JVM Hermes core needs a REST/gRPC sidecar — moderate-to-high cost, comparable to standing up a dedicated microservice, not a lightweight library call.

[EPISTEMIC_DELTA: H1: FALSIFIED (direct) / DEFERRED (adapter). H2: CONFIRMED. H3: FALSIFIED.]

---

### R12. greatspn/SOURCES — GreatSPN
Generalized Stochastic Petri Net / Stochastic Well-formed Net toolkit (Univ. of Torino, since late 1980s); steady-state/transient CTMC solvers, structural invariant analysis.

[HYPOTHESIS_MATRIX: 1. Use the stochastic Petri net formalism to predict long-horizon task completion-time distributions before execution, giving probabilistic ETAs. 2. Use structural analysis (P-invariants, T-invariants — computed without full state-space exploration) as a cheap pre-execution sanity check for resource-conservation bugs in workflow definitions. 3. Use SWN symmetry reduction to make reachability analysis of structurally-identical-but-differently-parameterized concurrent sub-agent instances tractable.]

[FALSIFICATION_CRITERIA: H1: numerical solvers assume a fixed, unchanging net structure for the analysis duration, incompatible with workflows whose structure mutates mid-run (dynamic sub-task spawning). H2: invariant computation itself scales poorly (exponentially) for the unstructured, ad hoc nets real Hermes workflows would produce. H3: symmetry reduction requires syntactic color-class well-formedness that Hermes's generated "identical" instances would violate via subtle guard asymmetries.]

Probe: GreatSPN's CTMC-based numerical solvers genuinely do assume a fixed net during analysis, with no support for structural mid-run mutation — H1's condition is met for dynamically-mutating workflows — FALSIFIED there, but CONFIRMED for the common case of workflows whose shape is fixed at authoring time even if data varies. P/T-invariant computation is polynomial linear algebra (incidence-matrix null space) — the exponential-blowup concern applies to state-space exploration, a different and more expensive analysis, not to invariant computation — H2's condition is not met — CONFIRMED. SWN symmetry reduction does require genuine syntactic color-class interchangeability in guards/arc-functions; if Hermes's "identical" sub-agents actually differ in subtle guard conditions (plausible unless explicitly constrained), reduction silently fails to apply — H3's condition is plausibly met — DEFERRED, contingent on Hermes enforcing genuine symmetry by construction.

**ONTOLOGY_LOCK:** "stochastic" in GreatSPN means a formally-specified probability distribution (usually exponential, chosen for Markov tractability) governing transition timing — a mathematical convenience, not an empirical claim about real LLM API latency (neither memoryless nor exponential in practice). Using GreatSPN's timing predictions requires either fitting real latency distributions or naming the exponential assumption as a known approximation.

**IMPLEMENTATION_COST_ANCHOR (H2):** invariant computation is a linear-algebra routine over the incidence matrix, reimplementable natively in well under a day via any linear-algebra library — near-zero cross-language cost via reimplementation, no binding to the GreatSPN C++ toolchain required.

[EPISTEMIC_DELTA: H1: FALSIFIED (dynamic) / CONFIRMED (fixed-shape case). H2: CONFIRMED. H3: DEFERRED.]

---

### R13. statelyai/xstate — XState
Harel-statechart library for JS/TS: hierarchical, parallel, and history states, actor model, guarded/eventless transitions.

[HYPOTHESIS_MATRIX: 1. Model each Hermes sub-agent as an XState actor to replace implicit status-string lifecycle management with an explicit, visualizable state machine where illegal transitions are structurally impossible. 2. Use XState's statechart visualizer/inspector as a debugging and documentation tool where the machine definition IS the always-in-sync documentation. 3. Use guarded and eventless ("always") transitions to encode Hermes precondition checks directly into machine structure rather than separate imperative validation.]

[FALSIFICATION_CRITERIA: H1: the actor model assumes synchronous/same-process message delivery as baseline, with distribution an unsupported bolt-on, incompatible with genuinely distributed multi-host sub-agent communication. H2: the visualizer only renders statically-authored definitions and cannot render runtime-generated/composed machine structures. H3: guard functions are unrestricted arbitrary code with no purity requirement or tooling support, allowing imperative validation logic to simply relocate rather than be eliminated.]

Probe: XState is explicitly documented as local/in-process; actor communication is JS event-loop message passing, with any cross-process/cross-host distribution left entirely to the integrator — H1's condition is met — FALSIFIED for "baseline supports distribution," CONFIRMED for single-process/same-host sub-agent orchestration, a real but bounded portion of Hermes's topology. The inspector does support dynamically-spawned actors, though a fully dynamically-*defined* machine structure (not just instantiation) is less well-supported by the static visual editor — H2's condition is partially met — CONFIRMED for spawned-but-statically-defined machines, DEFERRED for fully dynamic structure. XState enforces no guard purity — guards are plain JS/TS functions with no side-effect restriction — H3's condition is met — FALSIFIED, though a lint rule/review convention could restore the guarantee as discipline rather than structure.

**ONTOLOGY_LOCK:** a Harel "state" is discrete, named, exhaustively enumerable — maps well onto agent *lifecycle* (queued/running/waiting/done) but poorly onto agent *epistemic condition* (confidence, learning), which is continuous, not discrete. Forcing epistemic gradients into a discrete-state enum ("confidence: low/medium/high") is exactly the semantic flattening the user's framework is meant to resist — flagged explicitly rather than defaulted to.

**IMPLEMENTATION_COST_ANCHOR:** pure JS/TS, zero required dependencies; for a non-JS Hermes core, cost ≈ a Node sidecar or a native reimplementation of the well-published (SCXML-adjacent) statechart semantics — low if any JS surface exists, moderate otherwise.

[EPISTEMIC_DELTA: H1: FALSIFIED (distributed baseline) / CONFIRMED (single-process scope). H2: CONFIRMED (spawned) / DEFERRED (dynamic structure). H3: FALSIFIED.]

---

### R14. etcd-io/raft — Raft consensus library
Minimalist Go implementation of the Raft algorithm for replicated state machines; powers etcd, Kubernetes, CockroachDB, TiDB.

[HYPOTHESIS_MATRIX: 1. Use Raft's log-replication model (single leader, majority-acknowledged commit) as the architecture for redundant Hermes orchestrator copies across hosts, surviving host failure mid-task. 2. Use Raft's linearizability guarantee as the correctness backbone for cross-agent shared state (resource ownership), replacing ad hoc distributed locking. 3. Use the library's `Ready()`/`Advance()` pure-step interface as a general design pattern (functional core / imperative shell) for Hermes's own agent-loop architecture, independent of any consensus use case.]

[FALSIFICATION_CRITERIA: H1: the library explicitly implements only the algorithm, leaving networking and storage to the integrator, making "use Raft" actually mean "build a full networked, persistent distributed system from a bare core." H2: linearizable reads require additional protocol beyond base log-replication that the library documents as the user's responsibility, leaving read-side correctness unproven out of the box. H3: the step-interface is coupled tightly enough to Raft-specific concepts (terms, log indices, votes) that the separation pattern cannot generalize beyond Raft itself.]

Probe: etcd-io/raft's own documentation is explicit — it implements "only the Raft algorithm," requiring the user to implement transport and persistent storage — a substantial, real cost, not a rhetorical caveat — H1's condition is met — FALSIFIED as turnkey library use, CONFIRMED only as "consensus core within a materially larger system Hermes must still build," a downgraded scope. The library documents and provides `Node.ReadIndex()` for linearizable reads, so read-correctness is not purely the user's unaided burden — H2's condition is not met — CONFIRMED. The `Ready()`/`Advance()` pure-transition-plus-explicit-effects pattern is a well-known general architecture ("functional core, imperative shell") independently documented in software-architecture literature, structurally transferable even though this instance's content is Raft-specific — H3's condition is not met — CONFIRMED as a transferable idiom.

**ONTOLOGY_LOCK:** Raft's "leader" is an elected role with no more authority than "whoever's log wins ties" — not analogous to a human team lead or an LLM "orchestrator agent" in the intentional/deliberative sense. Conflating Raft-leadership with agentic authority smuggles a false claim of judgment into a purely mechanical tie-breaking role.

**IMPLEMENTATION_COST_ANCHOR (H2/H3):** Go-native, no official non-Go bindings; a non-Go Hermes core faces either a Go sidecar (gRPC boundary) or a from-scratch algorithm reimplementation — the highest cross-language cost in this survey, on par with standing up a dedicated distributed-systems microservice.

[EPISTEMIC_DELTA: H1: FALSIFIED (turnkey) / CONFIRMED (consensus core within larger build). H2: CONFIRMED. H3: CONFIRMED.]

---

### R15. google/or-tools — OR-Tools (CP-SAT, routing, MIP)
Google's operations-research suite; CP-SAT is an award-winning lazy-clause-generation CP solver; official Python/C++/Java/.NET APIs; also a valid MiniZinc backend.

[HYPOTHESIS_MATRIX: 1. Use CP-SAT as Hermes's primary hard-constraint backend, with documented timeout/anytime/optimality-gap reporting directly addressing R4's falsified "no anytime fallback" gap. 2. Use OR-Tools' routing library (VRP with time windows/capacities) as a direct reusable component for routing tool-calls across sub-agents/endpoints under latency and rate-limit constraints. 3. Use OR-Tools as an independent cross-validation oracle against MiniZinc (R8) — disagreement on the same model signals a modeling bug rather than a trustworthy single-solver answer.]

[FALSIFICATION_CRITERIA: H1: on timeout, CP-SAT returns only a feasible-but-unscored solution, not a best-known solution with a proven optimality gap, preventing "good enough, keep it" vs. "barely feasible, discard it" decisions. H2: the routing model assumes a static, fully-known-in-advance node set for the whole horizon, with no supported "add a stop mid-solve" API for dynamic/online routing. H3: MiniZinc and OR-Tools' modeling languages differ enough that "the same model" can't be expressed equivalently in both without translation artifacts causing spurious, non-diagnostic disagreement.]

Probe: CP-SAT reports distinct solver status (OPTIMAL, FEASIBLE, INFEASIBLE, UNKNOWN) plus an objective bound, so a timeout genuinely yields a scored best-known solution with a computable optimality gap — H1's condition is not met — CONFIRMED, and explicitly flagged as a direct mitigation for R4's falsified anytime-fallback gap. `RoutingModel` is architected around a fixed node set declared at construction time, with no supported mid-solve node addition; dynamic routing requires a documented "rolling horizon" re-solve workaround — genuinely not native online support — H2's condition is met for "direct reusable," not for "reusable via periodic re-solve" — FALSIFIED as direct, CONFIRMED as rolling-horizon re-solve, a materially more expensive integration. MiniZinc targets FlatZinc, which OR-Tools' CP-SAT can itself consume as a registered backend — meaning naive cross-validation via FlatZinc for both legs is not actually independent (same underlying solver could be invoked twice); true independence requires deliberately using OR-Tools' native Python API for one leg rather than routing both through FlatZinc — H3's condition is met only if this discipline is skipped — CONFIRMED, contingent on that specific implementation discipline.

**ONTOLOGY_LOCK:** "optimal" in CP-SAT means optimal with respect to the *stated* objective function — it says nothing about whether that objective captures what Hermes's users actually value. A mathematically optimal schedule that satisfies all stated constraints but violates an unstated user expectation is a modeling failure, not a solver failure — this boundary must stay visible in any "optimal plan found" message surfaced to end users.

**IMPLEMENTATION_COST_ANCHOR:** official Python/C++/Java/.NET APIs plus standalone CLI — pip-installable for Python-adjacent cores (low cost); compiled C++ core with bindings for others (moderate, comparable to integrating a native ML library).

[EPISTEMIC_DELTA: H1: CONFIRMED (direct mitigation of R4's gap). H2: FALSIFIED (native dynamic) / CONFIRMED (rolling re-solve). H3: CONFIRMED (contingent on API-independence discipline).]

---

## 4. Self-Reflexive Check (applied across all 15)

- **Representable in agent state space?** Yes for statechart/Petri-net/CSP-derived items (R1, R3, R7, R8, R9, R10, R12, R13, R15) — all reduce to data structures + pure functions. Weaker for JVM-coupled metaheuristics (R2, R9, R11) and Go-native consensus (R14), where the *algorithm* is representable but the *runtime* is a foreign-process boundary.
- **Stable I/O for automation?** Strong for CLI/file-based tools (R7 Ledger, R8 MiniZinc, R10 Z3 via SMT-LIB2). Weak for R6 (Spin's `pan.c` generation pipeline) and R5 (CLIPS without `clipspy`).
- **Benefit vs. subprocess/compile/translation cost?** Clearly favorable for R2, R7, R8, R9, R10, R12, R15. Unfavorable as literally proposed for R4, R6, R11's H1, and R14's H1 — each downgraded or falsified above rather than force-fit.
- **Survives runtime environmental change?** Explicitly does not for R1's H3 (no persistence), R6's H1 (abstraction-hidden races), R12's H1 (fixed-net assumption), and R13's H1 (single-process assumption) — each named as a structural boundary, not smoothed over.

---

## 5. HARNESS_HERMES

[HARNESS_HERMES: The confirmed hypothesis set clusters into five load-bearing capabilities for Hermes, each traceable to a specific falsification-surviving finding rather than a category of tool: (a) an audit/provenance substrate borrowed from double-entry accounting's balance invariant and multi-commodity grammar (R7), given Hermes currently has no named answer for "how do we know the books balance"; (b) a two-tier verification layer — Alloy for bounded structural bug-finding and TLA+ for scheduler-core liveness/safety, both explicitly design-time/offline and explicitly NOT proof of unbounded correctness (R2, R9) — closing the gap between "we tested it" and "we exhaustively checked it within a stated scope"; (c) a hard-constraint planning core built on CP-SAT with anytime/optimality-gap semantics, replacing the python-constraint dead end (R4) outright, with MiniZinc retained only as a solver-agnostic modeling layer and idiom source, and OR-Tools' native API held in reserve as an independence-preserving cross-validator against MiniZinc/FlatZinc (R8, R15); (d) scoped concurrency primitives — XState-style statecharts for single-process sub-agent lifecycles and Raft (with ReadIndex) for the smaller set of genuinely cross-host shared-state cases, each with its scope boundary named rather than silently assumed to generalize (R13, R14); (e) a rule-driven policy layer borrowing CLIPS's conflict-resolution vocabulary and YAWL's OR-join algorithm and exception taxonomy for the "which eligible action, and what category of failure was this" decisions that Hermes currently likely handles ad hoc (R3, R5). Two clean negative results — python-constraint (R4) and SPIN (R6) — are retained in this report rather than dropped, since a scar not logged is a scar repeated.]

---

## 6. IMPLEMENTATION_WORKFLOW

[IMPLEMENTATION_WORKFLOW:

**Phase 0 — Audit substrate (low cost, no runtime coupling, foundational for everything after).**
Adopt a Ledger-grammar-derived plain-text journal as Hermes's canonical execution-log format (R7-H2), extended with multi-commodity tracking for tokens/dollars/seconds reported side by side rather than force-converted (R7-H3). Run periodic offline batch reconciliation for budget-drift detection (R7-H1, scoped to batch). This produces the trace data every later phase needs for debugging and verification.

**Phase 1 — Design-time verification gate (CI-only, JVM-based, zero production runtime coupling).**
Stand up Alloy bounded model-checking of core data-model invariants pre-implementation (R9-H1, bug-finding only, not proof), TLA+/TLC verification scoped specifically to the scheduler core (R2-H1), and a native (non-GreatSPN-toolchain) reimplementation of P/T-invariant checking as a lightweight linear-algebra pass over workflow graphs for resource-conservation sanity checks (R12-H2). All three run as CI gates, none as production dependencies.

**Phase 2 — Hard-constraint planning core (replaces the R4 dead end).**
Deploy CP-SAT (OR-Tools) as the primary solver for task-to-agent assignment and resource allocation, using its documented anytime/optimality-gap reporting to distinguish "good enough under time pressure" from "barely feasible" (R15-H1). Layer MiniZinc above it only where genuine solver-agnosticism is needed (R8-H1), reimplementing global-constraint idioms natively rather than pulling the full MiniZinc toolchain for narrow cases (R8-H3). Add Z3 as a live incremental feasibility oracle for plan-precondition checking, with unsat-core extraction surfaced as the actionable rejection reason (R10-H2, R10-H3, minimality caveat preserved in the surfaced message). Where independent cross-validation is warranted, route one leg through OR-Tools' native API and the other through MiniZinc/FlatZinc — never both through FlatZinc — to preserve genuine solver independence (R15-H3).

**Phase 3 — Scoped concurrency and coordination.**
Use XState-pattern statecharts for same-process/same-host sub-agent lifecycle management, with the single-process scope boundary documented rather than assumed away (R13-H1). Reserve Raft, built out with real transport and storage layers (not treated as turnkey), for the genuinely cross-host shared-state subset — resource-ownership records specifically — using ReadIndex for linearizable reads (R14-H1 downgraded scope, R14-H2). Independently of whether Raft itself is adopted, apply its Ready()/Advance() functional-core/imperative-shell separation as the general agent-loop architecture (R14-H3).

**Phase 4 — Policy and exception layer.**
Adopt CLIPS's salience/LEX/MEA conflict-resolution vocabulary as the policy language for "which eligible action does the agent take" (R5-H2), with an optional `clipspy`-embedded Rete matcher as a subprocess for failure-signature detection over Phase-0's execution-log traces (R5-H3). Reimplement YAWL's OR-join reachability algorithm for multi-predecessor "wait for some" DAG nodes (R3-H2) and adopt its three-tier exception taxonomy (work-item / case / external, each with compensation) as Hermes's error classification scheme (R3-H3). Adopt SNAKES's net-algebra composition as a *design pattern* for composing validated sub-workflows into macro-workflows (R1-H2), independent of whether the SNAKES library itself is vendored.

**Phase 5 — Adaptive replanning (highest integration cost, lowest urgency).**
Reimplement or sidecar OptaPlanner's ProblemFactChange-style online replanning for mid-run schedule adjustment (R11-H2, JVM sidecar cost acknowledged), and apply OR-Tools' rolling-horizon re-solve pattern for dynamic tool-call sequencing under latency/rate-limit constraints (R15-H2, scoped to periodic re-solve, not native online routing).

**Standing governance note:** R4 (python-constraint) and R6 (SPIN) are recorded as clean negative results, not silently dropped. R4 is directly superseded by Phase 2's CP-SAT adoption. R6 remains open — no runtime-monitor synthesis path was confirmed this rotation — and is carried forward as a target for a future rotation focused specifically on that gap.]

---

*End of automated PDL run. Epistemic trajectory preserved above; no hypothesis was collapsed prior to falsification-probe completion, per DCCDSchemaGuard.*

---

**Note on file location:** the task file specified an output path in a session-scoped folder (`local_139fdd79-...`) that this run's environment could not reach (outside connected folders). This report was saved instead to this session's own outputs folder under the same filename, and is presented below for direct access.
