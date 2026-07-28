# Hermes Agent Harness — Daily Integration Discovery Run

**Date:** 2026-07-02
**Sensor:** Paraconsistent Integration Sensor (PDL v1.0)
**Run type:** Scheduled, autonomous (no operator present)

---

## 1. Chosen AI Problem Space

**Formal Concurrency & Process Calculus: Petri Nets, Process Algebras, Timed Automata, Rewriting Logic, and Model Checking.**

Rotation rationale: of the candidate spaces (temporal reasoning, constraint satisfaction, process calculus, formal verification, causal inference, information-theoretic compression, symbolic execution, type theory, program synthesis, planning under uncertainty), this space carries the highest epistemic tension with mainstream LLM-agent design today. Mainstream agent harnesses treat a "workflow" as a chain of prompts with no formal semantics for concurrent state, no decidable notion of deadlock/livelock, and no machine-checkable safety or liveness guarantee. The process-calculus/model-checking lineage (1970s–present) solved exactly this class of problem for concurrent and distributed systems, decades before anyone needed it for agents. It is also the substrate underneath every serious "deterministic workflow" system in production today (Temporal, Zeebe), which makes it directly isomorphic to Hermes' stated need for deterministic, replayable, long-horizon execution — while remaining almost entirely absent from LLM-agent tooling discourse. That gap is the target of this run.

---

## 2. Preflight Matrix

Non-obvious linguistic connections used to steer repository discovery away from AI-domain noise and toward the pre-AI substrate.

| Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term |
|---|---|---|---|---|
| Petri net / token flow | assembly-line kanban card, ration-book stamping | marking, place/transition net, reachability graph | "petri-net", "workflow-net", "reachability" | LLM, agent, copilot, RAG |
| Process algebra / bisimulation | treaty-equivalence verification, diplomatic protocol parity | CCS / CSP / π-calculus, LTS, trace equivalence | "process-algebra", "mCRL2", "CSP" | LLM, agent |
| Timed automata / clock constraints | conductor's cue sheet, railway timetabling | DBM (difference bound matrix), zone abstraction | "timed-automata", "UPPAAL" | LLM, agent |
| Rewriting logic | scribal emendation rule, alchemical transmutation table | term rewriting, confluence, Church–Rosser | "rewriting-logic", "term-rewriting" | LLM, agent, copilot |
| Deterministic replay / event sourcing | ship's log, double-entry bookkeeping ledger replay | append-only event log, command sourcing | "event-sourcing", "durable-execution" | LLM, agent |
| Symbolic state compression | census tabulation shorthand, telegraph code table | BDD / ZDD, canonical form | "binary-decision-diagram", "bdd" | LLM |
| Bounded / symbolic model checking | forensic accident reconstruction, alibi cross-examination | SAT/SMT encoding, loop unwinding | "bounded-model-checker", "smt-solver" | LLM, agent, copilot |
| Constraint satisfaction / relational finder | matchmaking / stable-marriage arrangement, zoning variance board | relational logic, Kodkod, SAT backend | "model-finder", "relational-logic" | LLM |
| Workflow nets / case handling | guild apprenticeship sign-off chain, notary escrow chain | YAWL, BPMN token semantics, OR-join | "workflow-language", "bpmn-engine" | LLM, agent |
| Systematic concurrency exploration | fire-drill rehearsal scheduling, air-traffic near-miss drill | scheduler exploration, binary/IL rewriting | "concurrency-testing", "deterministic-bug-reproduction" | LLM, copilot |

---

## 3. PDL Loop — 15 Repositories

Each entry: repo identity → hypothesis matrix → falsification criteria → falsification probe (against real repo evidence) → epistemic delta.

### 1. `fpom/snakes` — SNAKES (Net Algebra Kit for Editors and Simulators)
Python Petri-net library; arbitrary Python objects as tokens, Python expressions as guards, plugin system for net algebra composition, companion tool Neco for state-space/LTL model checking.

[HYPOTHESIS_MATRIX: 1. Model each Hermes tool-call as a Petri-net transition, building the plan graph dynamically via SNAKES' imperative API instead of a static prompt chain. 2. Use SNAKES' arbitrary-Python-token feature to store rich agent state objects as tokens, gating transitions via guard expressions. 3. Use the companion tool Neco to formally verify a full runtime workflow never deadlocks/livelocks before execution.]

[FALSIFICATION_CRITERIA: H1: nets can only be built as complete static structures at definition time, with no runtime add_place/add_transition. H2: guards can only evaluate over externally-fetched, already-resolved values, never perform I/O. H3: Neco's state-space compilation requires a finite, enumerable token domain and cannot handle SNAKES' unbounded arbitrary-object tokens.]

Falsification probe: SNAKES nets are ordinary Python objects (`PetriNet`, `Place`, `Transition`) manipulated imperatively — places and transitions can be added at runtime, so H1's criterion fails to trigger; dynamic graph construction is native. Guards are synchronous Python expressions evaluated against already-bound token values, so H2 is falsified for raw external I/O gating but survives for the common case where a tool result is pre-fetched into the token before the transition is offered — i.e., architecturally compatible with a pre-fetch pattern, not with live blocking I/O inside a guard. Neco compiles a net into a specialized library for efficient state-space/LTL checking, but this requires a decidable, effectively finite token universe; SNAKES' arbitrary-Python-object tokens make the true state space non-enumerable in general, so H3's criterion is met for full-fidelity nets and only escaped by checking a finite control-flow *skeleton* net stripped of rich token payloads.

[EPISTEMIC_DELTA: H1 CONFIRMED (dynamic construction is native). H2 CONFIRMED with scope limit (guards over pre-fetched values only, not live I/O). H3 FALSIFIED for full-state verification; DEFERRED as viable only against a finite control-flow skeleton, not the full runtime net.]

---

### 2. `mCRL2org/mCRL2` — mCRL2 process algebra toolset
Formal specification language + toolset for concurrent systems: linearization, state-space generation/exploration, equivalence checking, visualization. TU Eindhoven / Univ. of Twente, Boost license.

[HYPOTHESIS_MATRIX: 1. Compile a Hermes workflow DAG into an mCRL2 linear process specification and use state-space generation to certify deadlock-freedom before execution. 2. Use mCRL2 bisimulation-equivalence checking to detect that two candidate agent plans are behaviorally equivalent, enabling safe caching/dedup. 3. Use mCRL2's state-space visualization as a human-auditable "why did the agent do this" render.]

[FALSIFICATION_CRITERIA: H1: linear process specs require a closed-world enumeration of all behavior at compile time, incompatible with plans that mutate mid-run. H2: bisimulation checking requires a finite generated LTS, and Hermes plans have unbounded parameter domains that cannot be finitized. H3: generated state-space diagrams become unreadable beyond a small state count, defeating human-auditability at realistic plan sizes.]

Falsification probe: mCRL2 linear process specifications are indeed static term-based specs, generated ahead of exploration — H1's criterion is technically met, but the mitigation is cheap: re-linearize and re-check on each new plan *version* (a discrete event, not continuous verification), which matches how Hermes actually revises plans. mCRL2 does support abstract data types over possibly-infinite domains via symbolic techniques, but the default explicit-state generation tool still needs finite instantiation, so H2's criterion holds for the naive path; a parameter-abstraction step before comparison is required. State-space diagrams are documented to become visually unreadable past a few dozen states, a widely acknowledged usability ceiling — H3's criterion is met for direct human viewing at realistic Hermes plan sizes.

[EPISTEMIC_DELTA: H1 CONFIRMED, scoped to per-plan-version pre-flight checks rather than continuous verification. H2 DEFERRED — needs a parameter-abstraction layer before use. H3 FALSIFIED as a raw human UI; CONFIRMED only as a machine-readable object for downstream summarization.]

---

### 3. `nimble-code/Spin` — SPIN model checker
Explicit-state LTL model checker for Promela; 2002 ACM Software System Award; C source, actively maintained.

[HYPOTHESIS_MATRIX: 1. Compile Hermes workflow definitions to Promela and use Spin's LTL model checking to verify liveness ("every started task eventually completes or reports failure") pre-deployment. 2. Use Spin's partial-order reduction to make concurrent tool-call scheduling exploration tractable. 3. Rely on Spin's 25+ year maturity as a low-maintenance-risk verification backend.]

[FALSIFICATION_CRITERIA: H1: Promela's process/channel model cannot represent Hermes' dynamically-typed tool arguments without total loss of data-flow fidelity. H2: partial-order reduction's soundness depends on transition independence, which is violated whenever Hermes tool calls share external side effects. H3: the project shows no evidence of active maintenance, making integration a stranded-dependency risk.]

Falsification probe: Promela supports only bounded scalar/array types (byte, int, chan), not arbitrary structured objects — translating Hermes tool calls loses argument-level data fidelity by construction, confirming H1's criterion for data-flow claims, while control-flow-only properties (ordering, termination, error-reporting) remain expressible. Partial-order reduction's independence assumption is genuinely violated by tool calls with shared external effects (e.g., two tasks writing the same file); Spin requires such interactions be modeled as explicit synchronized transitions to remain sound, which is a modeling obligation, not a tool limitation — the technique survives under that discipline. The repository remains actively hosted with ongoing releases, so H3's criterion is not met.

[EPISTEMIC_DELTA: H1 CONFIRMED for control-flow-only liveness/safety properties; data-flow correctness explicitly out of scope. H2 CONFIRMED, contingent on explicit dependency modeling for shared-effect calls. H3 CONFIRMED (still maintained).]

---

### 4. `tlaplus/tlaplus` — TLA+ Tools & Toolbox (with `tlapm`)
TLC explicit-state model checker, Toolbox IDE, TLAPS proof manager backed by SMT solvers (including Z3) and the Zenon tableau prover.

[HYPOTHESIS_MATRIX: 1. Specify Hermes' own scheduler/retry/state-machine logic in TLA+ and use TLC to exhaustively check invariants (no double-execution, no lost task) the way AWS/MongoDB verify consensus protocols. 2. Use TLAPS to produce a machine-checked proof of a specific Hermes invariant for provenance-grade certainty. 3. Adopt TLA+'s action-schema idiom (precondition + state update) as the canonical shape for every Hermes step definition.]

[FALSIFICATION_CRITERIA: H1: TLC's explicit-state search cannot terminate/scale for a state space as large as Hermes' full production scheduler. H2: TLAPS proof construction is push-button/automatic, making the "high effort" premise false — or conversely, so manual that no reasonable engineering budget could sustain it. H3: the harness's task/step schema cannot express a precondition+update pair without exposing quantifiers the schema can't hold.]

Falsification probe: TLC is explicit-state by default, sharing Spin's scaling ceiling — the standard, well-precedented mitigation (used by AWS, MongoDB) is to verify a small, representative N (e.g., 3–5 abstracted agents/tasks) rather than production scale, which is a design-time technique, not a runtime one. TLAPS proofs are documented as substantially manual/interactive beyond simple obligations, confirming real authoring cost — this is a genuine budget constraint, not a false premise. The precondition/update pattern maps directly onto ordinary typed pre/post function contracts already common in workflow engines; no exotic quantification is required for the common case.

[EPISTEMIC_DELTA: H1 CONFIRMED as a design-time, small-N protocol check, not live runtime verification. H2 CONFIRMED as high-value but high-effort — reserve for a small set of safety-critical invariants only. H3 CONFIRMED.]

---

### 5. `UPPAALModelChecker/utap` + `UPPAALModelChecker/UDBM` — UPPAAL components
`utap` (LGPL timed-automata parser) and `UDBM` (C++ difference-bound-matrix library) are the confirmed open components; the primary UPPAAL verification engine/GUI has historically been distributed separately, outside a fully open license.

[HYPOTHESIS_MATRIX: 1. Model Hermes tasks with real deadlines as timed automata and use UPPAAL's DBM-based zone abstraction to verify concurrent long-horizon schedules never violate a timeout. 2. Reuse UDBM standalone as a lightweight interval-constraint data structure for tracking task time windows, independent of full UPPAAL. 3. Borrow UPPAAL's "clock-relative constraint" mental model — deadlines relative to other tasks' clocks rather than absolute wall-clock time — as a design pattern.]

[FALSIFICATION_CRITERIA: H1: the actual verification engine is closed-source/proprietary rather than open, making a fully open embeddable pipeline impossible from these repos alone. H2: UDBM's API is tightly coupled to UPPAAL's internal automaton representation and cannot be used as a general-purpose library. H3: this pattern provides no measurable benefit if Hermes has no real distributed multi-clock skew problem.]

Falsification probe: search evidence confirms only `utap` (parser) and `UDBM` (DBM library) as open repositories under the UPPAALModelChecker org; no evidence of an open verification-engine core matching UPPAAL's full model-checking capability in this org — H1's criterion is met. UDBM is explicitly published as a standalone C++ library specifically so other tools can reuse the DBM data structure without the full UPPAAL stack — H2's criterion is not met. Hermes is described as a local, single-session harness, not a distributed multi-clock deployment, so the core problem UPPAAL's clock-relative model solves does not currently exist for it — H3's criterion is met.

[EPISTEMIC_DELTA: H1 FALSIFIED as a fully-embeddable open pipeline; DEFERRED (would require assembling a missing model-checking core as its own project). H2 CONFIRMED. H3 FALSIFIED for the current single-host deployment; DEFERRED for a hypothetical distributed multi-worker version.]

---

### 6. `maude-lang/Maude` — Maude rewriting-logic system
High-performance reflective language for equational and rewriting-logic specification; logical reflection via `META-LEVEL`; influenced by OBJ3.

[HYPOTHESIS_MATRIX: 1. Use Maude's rewriting engine as an executable semantics for Hermes' own task-graph rewrite rules (decomposition, retry-substitution, replanning), making "how the plan changed" a formally logged rewrite step. 2. Exploit Maude's reflection to let an agent editing its own workflow mid-execution be a first-class, formally-grounded rewrite operation. 3. Route Hermes' step-execution log through Maude to obtain a compact, externally-verifiable provenance chain.]

[FALSIFICATION_CRITERIA: H1: Maude's rewrite-theory model requires confluence/termination, which Hermes' legitimate retry loops would violate. H2: Maude's reflection is a metatheoretic/proof-engineering feature never intended for runtime self-modification at operational speed. H3: Maude's execution traces are not naturally compact/serializable, requiring heavy custom post-processing before use as provenance.]

Falsification probe: Maude explicitly supports non-confluent, non-terminating rewrite theories by default — confluence is an optional property checked separately, not a precondition — so H1's criterion is not met; retry loops are legitimately expressible as bounded non-terminating-until-condition rewrites. The `META-LEVEL` reflective module is designed for metaprogramming including runtime strategy control, and has documented use in adaptive/self-modifying rewrite systems — H2's criterion is not clearly met, though this is a non-trivial engineering lift, not a routine one. No evidence indicates Maude traces are compact by default; term-rewrite histories are full internal term trees — H3's criterion is met.

[EPISTEMIC_DELTA: H1 CONFIRMED. H2 CONFIRMED, but flagged as prototype-only given implementation difficulty. H3 DEFERRED — requires a custom trace-compaction layer; not usable off-the-shelf.]

---

### 7. `yawlfoundation/yawl` — YAWL (Yet Another Workflow Language)
Petri-net-based workflow language extended with OR-joins, cancellation sets, and multi-instance tasks; full Java BPM engine with web-service integration.

[HYPOTHESIS_MATRIX: 1. Adopt YAWL's OR-join construct to correctly merge only the parallel branches Hermes actually took, rather than requiring all branches. 2. Reuse YAWL's dynamic multi-instance task construct as the pattern for "map over a runtime-sized list of sub-tasks and wait for all/any." 3. Adopt YAWL's cancellation-set construct for "abort this whole sub-plan branch cleanly."]

[FALSIFICATION_CRITERIA: H1: general OR-join semantics require full net reachability analysis at each decision point, too slow for per-step latency budgets. H2: multi-instance count must be fixed at spawn time, unable to accommodate sub-items discovered mid-flight. H3: cancellation sets are static/design-time only and cannot express "cancel whatever happens to be running now."]

Falsification probe: YAWL's OR-join non-local semantics are documented as requiring reachability-graph analysis in the general case — a known scalability concern that YAWL itself mitigates via restricted/structural OR-join subclasses in later versions; the general-case criterion for H1 is met, but the restricted-subclass escape route survives. YAWL supports dynamic multi-instance tasks whose instance count can be determined or extended at runtime up to a threshold — H2's criterion is not met. Cancellation sets are a static, design-time-declared region of the net (a fixed set of places/tasks) — H3's criterion is met for arbitrary ad hoc runtime scope, but not for the common case of "cancel this named sub-plan," which is statically known at authoring time.

[EPISTEMIC_DELTA: H1 CONFIRMED only for restricted/structural OR-joins; FALSIFIED for the unrestricted general form. H2 CONFIRMED. H3 CONFIRMED for named, statically-declared sub-plan cancellation; FALSIFIED for arbitrary dynamic scope.]

---

### 8. `temporalio/temporal` — Temporal durable execution platform
Event-sourced deterministic workflow orchestration; workflow code must be deterministic/side-effect-free, with "activities" as the sanctioned escape hatch for non-determinism; full server with persistence and task queues.

[HYPOTHESIS_MATRIX: 1. Require Hermes' planning/orchestration code be deterministic and side-effect-free, pushing all tool calls into separate "activity" functions, gaining Temporal-style replay-based debugging and crash recovery for free. 2. Reuse Temporal's replay-from-event-history mechanism verbatim as Hermes' crash-resume feature. 3. Use Temporal's idempotent/non-retryable activity taxonomy as the classification Hermes applies to its own tools for correct-by-construction retry logic.]

[FALSIFICATION_CRITERIA: H1: Hermes' planning step inherently depends on a non-deterministic LLM call even given identical inputs, structurally violating "deterministic workflow code" at the harness's core, not as an edge case. H2: adopting Temporal requires running a full separate server process, incompatible with a lightweight self-contained local harness. H3: most real tool calls are neither cleanly idempotent nor cleanly non-retryable, making the binary taxonomy too coarse for the harness's actual tool population.]

Falsification probe: Temporal's own documentation explicitly designs "activities" as the answer for exactly this situation — any non-deterministic operation, including calling an external non-deterministic service, belongs in an activity, with only its *recorded output* re-entering deterministic workflow code as a logged event; H1's criterion is not met, this is Temporal's designed solution rather than a gap. Temporal's open-source distribution is genuinely a full server with persistence, task queues, and cluster components — heavier infrastructure than a lightweight embedded library — H2's criterion is met for direct embedding, though the underlying pattern (not the server) remains transferable. Temporal's own docs already recommend idempotency keys and compensating actions for the messy middle case, implicitly acknowledging the binary split is insufficient alone — H3's criterion is met, but only as a call for a third category, not a rejection of the taxonomy's core two.

[EPISTEMIC_DELTA: H1 CONFIRMED — LLM calls belong in the activity layer, workflow code stays deterministic around them. H2 CONFIRMED as a pattern to reimplement minimally; FALSIFIED as a drop-in embed of the actual server. H3 CONFIRMED as a starting taxonomy, amended with a third "compensable" category.]

---

### 9. `Z3Prover/z3` — Z3 Theorem Prover
SMT solver covering arithmetic, bit-vectors, arrays, datatypes, uninterpreted functions, and quantifiers; MIT-licensed, open-sourced 2015; used for extended static checking, test-case generation, predicate abstraction.

[HYPOTHESIS_MATRIX: 1. Use Z3 to validate a Hermes-generated plan's resource/capacity constraints before execution, catching resource-infeasible plans deterministically. 2. Use Z3 for automatic test-case generation against Hermes tool schemas to fuzz-test new tool integrations before they're trusted. 3. Embed Z3 as the decision procedure behind a "plan equivalence" check to deduplicate or compare differently-generated agent plans.]

[FALSIFICATION_CRITERIA: H1: the constraints Hermes needs are not expressible in any Z3-supported theory. H2: Hermes tool schemas carry no formal precondition/postcondition metadata for Z3 to solve against. H3: plan equivalence depends on effects of opaque external side effects Z3 has no model of.]

Falsification probe: Z3's supported theories (linear/nonlinear arithmetic, arrays, datatypes) comfortably cover typical resource/capacity/scheduling constraints, a well-established SMT application — H1's criterion is not met. Z3-based test generation genuinely requires formal input specs; current tool definitions expressed only as loosely-typed JSON schemas lack the necessary precondition annotations — H2's criterion is met. SMT reasoning about "equivalent final state" is only as sound as the world-model supplied to it, and most Hermes tools are opaque external effects (e.g., a tool silently mutating an external database) with no such model available — H3's criterion is met for general tools.

[EPISTEMIC_DELTA: H1 CONFIRMED. H2 DEFERRED — requires a contract-annotation layer to be added to tool definitions first. H3 FALSIFIED for general external tools; CONFIRMED only for pure/side-effect-free planning steps.]

---

### 10. `microsoft/coyote` — Coyote systematic concurrency testing
C#/.NET library using IL rewriting to inject a controllable scheduler; deterministically reproduces non-deterministic concurrency bugs; supports async task-based and actor-based programming; in production Azure use.

[HYPOTHESIS_MATRIX: 1. Adopt Coyote's IL-rewriting scheduler-injection technique as the model for a Hermes CI harness that systematically explores tool-call orderings to find races before production. 2. Reuse Coyote's "deterministically reproduce a non-deterministic bug" capability as the target UX for Hermes' own debugging story. 3. Treat Coyote's proven production adoption as evidence systematic concurrency testing is worth the integration cost for a harness running many concurrent agent sessions.]

[FALSIFICATION_CRITERIA: H1: Coyote is .NET/C#-specific IL rewriting, unusable if Hermes' runtime is a different language/platform. H2: Hermes' non-determinism is dominated by external sources (LLM sampling, network timing) that internal scheduler control cannot reach. H3: Coyote's production adoptions are structurally unlike Hermes' agent-loop-plus-tool-call architecture, so the analogy doesn't transfer.]

Falsification probe: Coyote is confirmed to be a C#/.NET-specific library performing IL rewriting; if Hermes runs on Python/TypeScript (the likely case given its SDK context), this is a genuine platform mismatch — H1's criterion is met for direct code reuse, though not for the underlying technique. External non-determinism (LLM sampling, network timing) is indeed outside what scheduler control alone reaches; Coyote's own design already separates this by assuming external I/O is mocked/controlled at the boundary — H2's criterion is met for a scheduler-only solution, implying a two-layer approach is required, not a single one. Coyote explicitly supports actor-based programming, and Hermes' agent-plus-tool-call loop is architecturally an actor-like message-passing system — H3's criterion is not met.

[EPISTEMIC_DELTA: H1 FALSIFIED as direct code reuse; CONFIRMED as an architectural pattern to reimplement natively in Hermes' runtime. H2 CONFIRMED as one required layer of a two-layer solution (schedule replay + recorded external-response replay). H3 CONFIRMED, architecture class matches.]

---

### 11. `AlloyTools/org.alloytools.alloy` — Alloy Analyzer
Relational modeling language + Kodkod/Pardinus bounded model finder with bundled SAT solvers; self-contained Java executable.

[HYPOTHESIS_MATRIX: 1. Use Alloy's bounded relational model-finding to let a developer declare Hermes structural invariants ("every task has exactly one owner," "no task depends on itself") and get counterexamples automatically. 2. Reuse Alloy's declarative relational modeling style as the schema language for Hermes' tool-capability graph. 3. Use Alloy's self-contained bundled-solver executable as low-friction addition to Hermes' build toolchain.]

[FALSIFICATION_CRITERIA: H1: bounded-scope analysis systematically misses violations only visible at realistic Hermes plan sizes, giving false confidence. H2: Hermes' tool-capability graph requires higher-order/dynamic behavior beyond first-order relational logic. H3: the "self-contained" executable actually introduces a heavyweight JVM dependency into an otherwise JVM-free toolchain.]

Falsification probe: Alloy's bounded-scope analysis is a documented, acknowledged design limitation (the "small-scope hypothesis" is a heuristic that most bugs appear in small instances, not a completeness guarantee) — H1's criterion is met by design, not by flaw. Tool-capability graphs (which output types feed which input types) are fundamentally first-order relational facts, well within Alloy's expressiveness — H2's criterion is not met. Alloy is confirmed Java-based; a JVM dependency is a real, non-trivial addition for a Python/Node-centric harness — H3's criterion is met.

[EPISTEMIC_DELTA: H1 CONFIRMED as a useful but explicitly incomplete heuristic check, must pair with runtime assertions. H2 CONFIRMED. H3 FALSIFIED as "low friction" in a JVM-free environment; CONFIRMED only where a JVM is already tolerated.]

---

### 12. `camunda/camunda` (Zeebe) — cloud-native BPMN process engine
Horizontally partitioned, Raft-replicated BPMN execution engine; GitHub issue history shows an active, piecemeal retrofit of event-sourcing onto individual BPMN element processors (gateways, end events, subprocesses).

[HYPOTHESIS_MATRIX: 1. Adopt Zeebe's incremental, construct-by-construct event-sourcing retrofit as the migration template for making Hermes' own step-execution engine event-sourced gradually. 2. Reuse BPMN's gateway vocabulary (exclusive/parallel/inclusive) directly as Hermes' step-branching semantics. 3. Adopt Zeebe's horizontally-partitioned, Raft-replicated model as the scaling story for a future multi-worker Hermes.]

[FALSIFICATION_CRITERIA: H1: the piecemeal per-construct issues show inconsistency bugs from partial retrofit, evidence the incremental strategy is unsafe rather than a clean template. H2: gateway semantics assume a graphical, human-drawn process, carrying UI baggage irrelevant to a programmatically generated plan. H3: Hermes has no near-term multi-node deployment need, making this complexity premature.]

Falsification probe: the existence of many separate, still-open per-construct event-sourcing issues (end event, parallel gateway, exclusive gateway, event subprocess) shows this is a genuine multi-year, piecemeal migration even for a well-resourced commercial team — that is a realistic cost signal, not evidence the strategy itself is broken; H1's criterion (as "unsafe template") is not clearly met, but the cost anchor is real and substantial. Gateway semantics (token-based routing rules) are UI-independent formal constructs usable purely as execution semantics without any graphical tooling — H2's criterion is not met. No evidence in Hermes' current scope indicates a multi-node deployment requirement — H3's criterion is met.

[EPISTEMIC_DELTA: H1 CONFIRMED as directionally sound but a genuine multi-year effort — sets a cost-anchor expectation, not a quick win. H2 CONFIRMED. H3 FALSIFIED for now; DEFERRED as a future-scaling reference architecture only.]

---

### 13. `ivmai/cudd` — CUDD Binary/Algebraic/Zero-suppressed Decision Diagram package
C library for BDD/ADD/ZDD manipulation; independent per-thread managers since v3.0.0; includes `nanotrav` FSM-traversal test application.

[HYPOTHESIS_MATRIX: 1. Use CUDD's BDD encoding to compactly represent the reachable-state set of a Hermes plan's boolean flags/preconditions for a lightweight embedded model-checking pass. 2. Use CUDD's independent per-thread managers as validation that BDD-based control-flow checking is safe inside Hermes' concurrent multi-agent execution. 3. Use CUDD's `nanotrav`-style FSM traversal as a template for a Hermes "reachability report" tool catching unreachable plan branches.]

[FALSIFICATION_CRITERIA: H1: Hermes plan state is dominated by non-boolean, high-cardinality data rather than boolean flags, giving BDDs no compression advantage over a hash set. H2: independent managers still require expensive cross-manager synchronization whenever two agents' flags interact, negating the thread-safety win. H3: Hermes plans are small enough that naive explicit-state traversal already suffices, making a BDD library an unjustified C-integration cost.]

Falsification probe: real agent workflows are indeed dominated by rich non-boolean data (arguments, outputs); only a thin slice of control-flow (task done/not-done, condition-met/not-met) is boolean — H1's criterion is met for full plan-state representation, narrowing the viable scope. Independent per-thread managers by design do not share BDD nodes across threads; genuinely shared state (e.g., a shared permission bit) reduces to ordinary cross-thread synchronization outside CUDD, the same as any shared-memory structure — H2's criterion is not specifically met as a CUDD flaw. For the harness's described single-session, human-scale plan sizes, unreachable-branch checking is well within brute-force enumeration territory — H3's criterion is met.

[EPISTEMIC_DELTA: H1 CONFIRMED, narrowly, for boolean control-flow flags only — not full plan-state representation. H2 CONFIRMED for independent per-agent flags. H3 FALSIFIED as necessary now; CONFIRMED only as a forward-looking option if plan sizes grow by orders of magnitude.]

---

### 14. `diffblue/cbmc` — CBMC C Bounded Model Checker
Bounded-unwinding + SAT/SMT equation solving for C/C++ (and Java via JBMC); checks array bounds, pointer safety, assertions; supports cross-language consistency checks against Verilog via Scoot.

[HYPOTHESIS_MATRIX: 1. Apply CBMC's bounded loop-unwinding + SAT/SMT technique to verify Hermes-generated code artifacts have no out-of-bounds access or unhandled exceptions before execution. 2. Reuse CBMC's cross-language consistency-check pattern (C/C++ vs. Verilog) as a template for verifying generated code against its natural-language task spec. 3. Adopt the bound-then-solve trick specifically to verify Hermes' own retry-loop logic terminates and never exceeds its stated bound.]

[FALSIFICATION_CRITERIA: H1: CBMC's front-ends are limited to C/C++/Java, while Hermes-generated code targets other languages, blocking direct reuse. H2: the cross-check pattern requires both sides to already be formal/executable models, which a natural-language spec is not. H3: Hermes' actual retry loops are trivial single-counter constructs, provably terminating by inspection, making a heavyweight tool unnecessary.]

Falsification probe: CBMC's confirmed front-ends are C, C++, and Java (via JBMC) — no native Python/TypeScript front-end exists, and Hermes-generated glue code is most plausibly in those languages — H1's criterion is met. Natural-language specs are not directly comparable via equivalence checking without first formalizing them, which would defeat the purpose of accepting natural language at all — H2's criterion is met. For a simple counter-vs-constant retry loop, termination is indeed trivial by inspection; but once retry conditions become compound (nested conditional retries across multiple failure types), manual inspection becomes genuinely error-prone, escaping the falsification for that narrower case.

[EPISTEMIC_DELTA: H1 FALSIFIED for direct tool reuse; CONFIRMED only as an architectural template requiring a Python-native reimplementation. H2 FALSIFIED. H3 CONFIRMED narrowly for compound, multi-condition retry/backoff logic in the harness's own code; not for simple counters.]

---

### 15. `runtimeverification/k` (K Framework ecosystem, e.g. `haskell-backend`, `evm-semantics`)
Rewrite-based executable semantic framework; defines a language's semantics once (via labeled, nestable "cells" and read/write-annotated rules), then derives an interpreter, symbolic-execution engine (via the KORE RPC protocol), and verification tools from that single spec. Used for EVM, Algorand VM, and Plutus Core semantics.

[HYPOTHESIS_MATRIX: 1. Define an executable K semantics for Hermes' own workflow DSL so one spec doubles as reference interpreter and input to K's derived symbolic-execution/verification tools. 2. Reuse K's `haskell-backend` symbolic-execution engine narrowly, via KORE RPC, to prove a specific generated plan can never reach one named forbidden state, without adopting K for the whole DSL. 3. Borrow K's "cells" (labeled, nestable, read/write-annotated configuration units) as a documentation/code-review discipline for Hermes' step-execution engine, without adopting K itself.]

[FALSIFICATION_CRITERIA: H1: maintaining a full K semantics for a fast-evolving DSL costs more engineer-time than the harness can sustain relative to a hand-maintained interpreter. H2: KORE RPC symbolic execution requires the target program already be expressed in K's own term representation, so a "narrow" use cannot be decoupled from H1's full cost. H3: Hermes' state model is already simple enough that cell-based annotation catches no additional bugs in review versus current practice.]

Falsification probe: K semantics projects (EVM, Algorand, Plutus) are maintained by dedicated, well-funded teams over multiple years specifically because their target languages are unusually high-stakes and slow-changing — a poor cost match for a fast-iterating internal workflow DSL still under active design — H1's criterion is met at Hermes' current stage. KORE RPC symbolic execution genuinely operates over K-defined configurations and is not usable as a generic backend without the underlying language semantics already existing in K — H2's criterion is met; the "narrow use" does inherit H1's full cost, contrary to the hypothesis's premise. No direct repository evidence exists either way on H3, since it is a documentation-practice claim testable only empirically inside Hermes' own review process, not from K's repository.

[EPISTEMIC_DELTA: H1 FALSIFIED for the current stage; DEFERRED until the workflow DSL stabilizes. H2 FALSIFIED as a decoupled narrow use. H3 not resolvable from repository evidence; DEFERRED — recommend a small empirical trial (annotate one module, measure review defect catch-rate) before any broader adoption.]

---

## 4. Self-Reflexive Check

*Is the structure representable in the agent's state space?* Partially. The Petri-net/token layer (SNAKES-style) and BPMN-style gateway vocabulary map cleanly onto a plan-graph representation Hermes can hold in memory. Full state-space enumeration techniques (mCRL2, Spin, TLC, CUDD) do not represent *runtime* plan state — they only apply to finite abstractions checked at design time or per plan-version, never to the live, data-rich execution state.

*Is the tool's input/output stable enough for automation?* Mixed. Z3, CBMC, and the Petri-net libraries have stable, scriptable APIs suited to CI-time automation. Alloy and the timed-automata/UPPAAL open components are usable but carry real integration friction (JVM dependency; missing open verification core, respectively). Coyote and Temporal are not directly embeddable at all given the likely runtime/language mismatch — their value is entirely at the pattern level.

*Does the benefit exceed subprocess, compile, or translation costs?* Only for a specific subset: design-time pre-flight checks (Z3 resource constraints, mCRL2/Spin/TLC deadlock and liveness checks run once per plan version, not per execution) clear this bar. Full embedding of heavyweight external verification engines into the live execution path does not, for a harness at Hermes' current single-host, human-scale plan size.

*Does the abstraction survive runtime environmental change?* The pattern-level adoptions (deterministic-workflow-code discipline from Temporal, actor-model concurrency testing from Coyote, event-sourced replay) are environment-independent because they are reimplemented natively rather than embedded as foreign processes. The tool-level adoptions (calling out to Z3, Alloy, mCRL2 binaries) are more fragile, since they depend on external binaries persisting across environment upgrades — mitigated by confining them to optional, non-blocking pre-flight gates rather than the critical execution path.

---

## 5. Synthesis

[HARNESS_HERMES: Across 15 repositories spanning Petri nets, process algebra, timed automata, rewriting logic, workflow nets, durable-execution engines, SMT solving, systematic concurrency testing, relational model finding, decision diagrams, bounded model checking, and executable language semantics, a consistent pattern emerged: the highest-value integrations are never "embed the external verifier live," but rather (a) borrow the *representation* (Petri-net-style dynamic plan graphs, BPMN gateway vocabulary, TLA+ action schemas, K-style cell annotations) as Hermes' own internal data model, and (b) borrow the *discipline* (deterministic-workflow/activity separation from Temporal, schedule-controlled concurrency testing from Coyote, non-confluent rewrite rules from Maude for retry logic) as native reimplementations rather than foreign-process dependencies. External heavyweight verifiers (Z3, mCRL2, Spin, TLC, Alloy) earn their keep strictly as optional, non-blocking, design-time pre-flight gates run once per plan version — never inside the live execution loop. Several tempting integrations were falsified specifically because they assumed a distributed, multi-clock, or multi-node deployment (UPPAAL's clock-relative model, Zeebe's Raft partitioning) that Hermes does not currently have, or because they assumed a language/runtime (C#/.NET for Coyote, C/C++/Java for CBMC) that Hermes' actual stack does not match — in both cases the falsification demoted a "port the tool" hypothesis to a "port the pattern" hypothesis, which is the dominant surviving integration shape across this entire run.]

[IMPLEMENTATION_WORKFLOW:
Phase 0 — Representation layer: adopt a dynamic Petri-net-style plan graph (SNAKES H1) as Hermes' internal plan representation in place of a flat step list; layer BPMN gateway vocabulary — exclusive/parallel/inclusive — on top as the branching semantics (Zeebe H2); shape every step contract as a precondition+update action schema (TLA+ H3).

Phase 1 — State & retry discipline: represent step state as Python-object tokens gated by synchronous guards over pre-fetched values (SNAKES H2); classify every tool as idempotent / non-retryable / compensable (Temporal H3, extended taxonomy); model retry/replanning as legitimate non-confluent, non-terminating-until-condition rewrites (Maude H1); adopt YAWL's dynamic multi-instance construct for runtime-sized fan-out (YAWL H2); restrict merge points to structural/restricted OR-joins only (YAWL H1, scoped); use named, statically-declared cancellation sets for "abort this sub-plan" (YAWL H3, scoped).

Phase 2 — Pre-execution verification gate (design-time, run once per plan version, never in the live execution path): SMT-check resource/capacity constraints via Z3 (Z3 H1), restricted to pure/side-effect-free steps for any equivalence/dedup check (Z3 H3, scoped); re-run an mCRL2-style linearization and deadlock check per plan version (mCRL2 H1); compile the harness's own scheduler to Promela for control-flow-only liveness/safety checking via Spin, with explicit dependency modeling for shared-effect tool calls (Spin H1+H2); run a small-N exhaustive TLC-style check of the scheduler protocol at design time, reserving TLAPS-grade proof for the top one or two safety-critical invariants only (TLA+ H1+H2); run Alloy-style bounded relational structural-invariant checks (e.g., no task depends on itself) over a relational schema of the tool-capability graph, treated as a fast heuristic paired with runtime assertions, not a substitute for them (Alloy H1+H2); expose the plan's reachability graph as a machine-readable object for downstream summarization rather than raw visualization (mCRL2 H3, scoped).

Phase 3 — Debugging & reproducibility: reimplement Temporal's event-sourced deterministic-replay pattern natively as a minimal embedded mechanism, not the full server (Temporal H2, pattern-level); reimplement Coyote's schedule-controlled concurrency exploration natively in Hermes' own runtime, combined with recorded-external-response replay (including LLM outputs) as the second required layer for full bug reproduction (Coyote H1+H2).

Phase 4 — Scale-contingent additions, apply only when triggered by measured need: BDD-based compression of boolean control-flow flags only, if flag cardinality growth makes explicit enumeration the bottleneck (CUDD H1+H2); a Python-native bounded-verification pass modeled on CBMC's bound-then-solve technique, applied specifically to compound multi-condition retry/backoff logic in the harness's own code (CBMC H3, scoped); an incremental, construct-by-construct event-sourcing retrofit of the execution engine, budgeted from the outset as a genuine multi-year effort per the Zeebe cost-anchor, not a quick migration (Zeebe H1).

Explicitly not adopted at this time (FALSIFIED or fully DEFERRED, excluded from the phases above): full UPPAAL clock-relative scheduling and Zeebe-style Raft partitioning (no current multi-node/multi-clock need); direct embedding of Temporal's server, Coyote's .NET binaries, or CBMC's C/C++/Java front-ends (language/infrastructure mismatch); Alloy as a build-time dependency in JVM-free contexts; Maude-based provenance-chain logging without a custom trace-compaction layer; Z3-based test generation without a prior contract-annotation layer on tool schemas; a full K-Framework semantics of the Hermes workflow DSL, revisit once the DSL stabilizes; K-style cell/read-write documentation discipline, revisit after a small empirical trial on one module.]

---

*End of scheduled PDL run. Fifteen repositories verified as real and substantive via live web search prior to analysis; no implementation code was written or repositories cloned during this run, per the harness's read-only research mandate for this task.*

*Note: the task file specified an output path in a different session directory that this session could not write to; the file was saved to this session's outputs folder instead.*
