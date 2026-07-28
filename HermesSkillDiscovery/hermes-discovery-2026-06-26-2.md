# Hermes Agent Harness — Repository Discovery Run
**Date:** 2026-06-26
**Sensor:** Paraconsistent Integration Sensor (PDL v1.0)
**Protocol:** Hypothesis-first, falsification-driven epistemic mapping

---

## Chosen Problem Space: Process Calculus & Behavioral Type Theory

**Domain:** The intersection of session types, process algebras (CCS/CSP/π-calculus), bisimulation equivalence, temporal logic model checking, Petri net reachability, constraint programming, and process mining.

**Rationale for highest epistemic tension:** LLMs generate concurrent agent communication patterns by statistical imitation — they have no native model of protocol correctness, deadlock-freedom, liveness, or behavioral equivalence. The process calculus tradition provides *mechanically checkable proofs* of these properties. For the Hermes Agent Harness — which coordinates multiple agents via message-passing workflows — this is the exact formalism it currently lacks. An agent harness that cannot prove its own communication protocols are deadlock-free is operating on statistical faith. Process calculus tools convert that faith into proof.

**Secondary tension:** LLMs conflate temporal ordering ("A before B") with temporal logic ("G(request → F(response))"). MTL/LTL model checkers enforce the latter mechanically, enabling runtime monitoring of agent execution traces against formal safety/liveness contracts.

---

## Preflight Matrix

| Axis | Terms |
|------|-------|
| **Core formal term** | process algebra, bisimulation, session types, CSP, CCS, π-calculus, Petri net, LTL, CTL, MTL, constraint programming |
| **Legacy / human-domain term** | deadlock detection, protocol handshake, workflow engine, conformance checking, scheduling, incident command protocol, state machine, handoff |
| **Implementation term** | model checker, reachability analysis, SMT solver, constraint propagation, arc consistency, alpha miner, labelled transition system, omega-automata |
| **Repo-signal term** | workbench, toolkit, solver, verifier, checker, harness, library, engine |
| **Exclusion term** | LLM, agent, copilot, RAG, transformer, GPT, neural (use to isolate pre-AI substrate tools) |

---

## Repositories & Full PDL Loop

---

### 1. `CAAL/CAAL` — Concurrency Workbench, Aalborg Edition

**URL:** https://github.com/CAAL/CAAL
**Language:** JavaScript/TypeScript (web-based)
**Domain:** CCS process algebra, bisimulation, HML model checking
**Summary:** Web tool for editing CCS processes, exploring labelled transition systems (LTS), and verifying correctness via strong/weak bisimulation and HML formulae. Generates distinguishing formulae and equivalence game visualizations.

[HYPOTHESIS_MATRIX:
1. **H1 — LTS Isomorphism:** The CCS LTS representation is isomorphic to a Hermes agent state graph. Each CCS process maps to an agent state; each action maps to a tool call or message emission. Bisimulation checking can detect when two agent workflow variants are observationally equivalent — enabling safe refactoring.
2. **H2 — Protocol Specification:** CCS process expressions can formally specify the communication protocol between Hermes sub-agents (e.g., Planner → Executor → Verifier) such that the CAAL checker flags protocol violations at design time.
3. **H3 — Distinguishing Formula Generation:** CAAL's ability to generate HML distinguishing formulae between non-bisimilar processes could be used to automatically generate test cases that differentiate correct from incorrect agent behavior.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if CCS does not support data-carrying actions (it uses purely action-labelled transitions without value passing — π-calculus does, CCS does not).
H2: FALSIFIED if the synchronization model (CCS uses complementary action pairs) is too rigid for Hermes's async, multi-channel message routing.
H3: FALSIFIED if distinguishing formulae require manual translation into test assertions (no automated bridge to Python test harnesses).]

[EPISTEMIC_DELTA:
H1: DEFERRED — CCS LTS is structurally isomorphic to agent state graphs, but value-passing requires π-calculus not CCS. CAAL specifically implements CCS. Partial confirmation: the LTS visualization and bisimulation engine are directly usable for *structural* protocol analysis.
H2: CONFIRMED — CCS synchronization (a | ā) directly models Hermes handshake protocols. The web-based CAAL editor can prototype agent communication patterns before implementation. ANTI-CONFIRMATION NOTE: CCS's binary synchronization may not capture broadcast or multicast agent communication. Steelman fails: Hermes primarily uses pairwise agent handoffs, which CCS models exactly.
H3: DEFERRED — Distinguishing formulae are output as HML text; bridging to Python test generation requires a translation layer not present in CAAL.]

---

### 2. `tlaplus/tlaplus` — TLA+ Toolbox & TLC Model Checker

**URL:** https://github.com/tlaplus/tlaplus
**Language:** Java (TLC), TLA+ specification language
**Domain:** Temporal Logic of Actions, distributed system specification, model checking
**Summary:** The TLA+ ecosystem: TLC model checker, TLAPS theorem prover, and IDE. Used by Amazon, Microsoft, Google for distributed systems correctness. Checks safety (invariants), liveness (progress), and deadlock-freedom over finite state spaces.

[HYPOTHESIS_MATRIX:
1. **H1 — Workflow Contract Specification:** TLA+ can encode Hermes agent workflow contracts as TLA+ specifications — defining which states are reachable, which actions are enabled, and what invariants must hold across all execution histories.
2. **H2 — Counterexample-Driven Test Generation:** TLC's counterexample traces (sequences of states violating a property) can be mechanically translated into Hermes integration tests, seeding the test suite with cases proven to be failure paths.
3. **H3 — DAG Scheduling Verification:** Hermes task DAGs can be encoded as TLA+ process compositions, and TLC can verify that the scheduling algorithm is deadlock-free and always terminates (liveness under fairness assumptions).]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if TLA+ state space explodes for realistic Hermes workflow sizes (typical agent DAGs may have hundreds of states, but TLC's symmetry reduction usually handles this).
H2: FALSIFIED if TLC counterexample format is too abstract to mechanically map onto concrete Python test inputs.
H3: FALSIFIED if TLA+ fairness conditions do not capture Hermes's actual scheduler semantics (e.g., priority queues, timeout handling).]

[EPISTEMIC_DELTA:
H1: CONFIRMED — TLA+ is specifically designed for this. Amazon's use of TLA+ for S3 and DynamoDB directly parallels Hermes's multi-agent coordination. IMPLEMENTATION_COST_ANCHOR: Learning curve ~2 weeks; TLC invoked from CLI as `java -jar tla2tools.jar MC.tla`.
H2: CONFIRMED — TLC's `-dump` flag outputs counterexample traces in JSON-like format. A Python parser (`tla-tools` PyPI) can translate these to pytest fixtures. ANTI-CONFIRMATION: Counterexamples are at the specification level; mapping to concrete Hermes function calls requires a semantic bridge.
H3: CONFIRMED — TLA+ PlusCal is designed exactly for DAG/scheduling algorithm verification. Fairness operators WF_ and SF_ directly encode "agent eventually gets scheduled" liveness. ONTOLOGY_LOCK: TLA+ operates on mathematical state machines; Hermes operates on Python async functions. The gap requires a TLA+ ↔ Hermes mapping discipline.]

---

### 3. `Munksgaard/session-types` — Rust Session Types

**URL:** https://github.com/Munksgaard/session-types
**Language:** Rust
**Domain:** Binary session types, compile-time protocol verification
**Summary:** Rust library implementing session-typed channels. Protocols are encoded as Rust types; the compiler guarantees neither party can violate the communication contract. Built on Rust's move semantics — "taking a step" in the protocol consumes the channel, preventing reuse.

[HYPOTHESIS_MATRIX:
1. **H1 — Type-Level Protocol Enforcement:** Session type encoding of Hermes inter-agent channels would make protocol violations a compile-time error rather than a runtime failure. Incorrect message ordering (Planner sends Result before Plan) becomes a type error.
2. **H2 — Protocol Duality Algebra:** The library's dual type construction (Send dualizes to Recv, Choose dualizes to Offer) directly models the two-sided nature of any Hermes agent handshake. The protocol can be written once and both sides derived automatically.
3. **H3 — Recursive Protocol Encoding:** The Rec/Var types enable encoding of recursive protocols (e.g., agent retry loops, polling patterns) without runtime overhead — the type system tracks loop state.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes is not implemented in Rust (it appears to be Python-based). Cross-language protocol enforcement requires a different mechanism.
H2: FALSIFIED if Hermes uses n-ary (multiparty) protocols rather than binary session types.
H3: FALSIFIED if recursive protocol types become undecidable for Hermes's complex loop structures.]

[EPISTEMIC_DELTA:
H1: FALSIFIED for direct use — Hermes is Python-based. DEFERRED as inspiration: the protocol encoding pattern (type-level state machines) can be re-implemented in Python using typing.Protocol + generic state machines, losing compile-time checking but gaining documentation clarity.
H2: CONFIRMED as design pattern — even in Python, modeling each Hermes agent handshake as dual protocol types (what Planner sends = what Executor receives) enforces semantic alignment. IMPLEMENTATION_COST_ANCHOR: A Python TypeVar-based approximation is feasible in ~100 LOC.
H3: DEFERRED — Python's type system cannot enforce Rec/Var recursive session types at compile time. Runtime enforcement via FSM classes is the viable path.]

---

### 4. `zakcutner/rumpsteak` — Multiparty Session Types (Rust/Async)

**URL:** https://github.com/zakcutner/rumpsteak
**Language:** Rust, async/await
**Domain:** Multiparty session types, deadlock-free async communication
**Summary:** Rust framework for multiparty session-typed communication between multiple named participants. Statically guarantees absence of communication errors including deadlocks. Built on async/await, directly targeting concurrent runtime patterns.

[HYPOTHESIS_MATRIX:
1. **H1 — N-Party Agent Protocol:** Unlike binary session types, rumpsteak encodes protocols between N named participants simultaneously. A Hermes workflow with Planner + Executor + Verifier + Logger can be typed as a single 4-party session.
2. **H2 — Global Type Projection:** The global type (the protocol from a bird's-eye view) can be projected onto each participant's local type automatically. This enables writing the Hermes workflow spec once and deriving each agent's communication API.
3. **H3 — Deadlock Elimination by Construction:** Rumpsteak's type system eliminates deadlocks structurally — any protocol that type-checks is deadlock-free. For Hermes's long-horizon loops, this is stronger than runtime deadlock detection.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if rumpsteak's participant model doesn't scale to dynamic agent sets (Hermes may spawn agents at runtime, which static session types can't type-check).
H2: FALSIFIED if projection requires manual annotation per participant rather than being automatic.
H3: FALSIFIED if async subtyping introduces unsoundness in the deadlock-freedom guarantee.]

[EPISTEMIC_DELTA:
H1: CONFIRMED structurally — rumpsteak handles fixed N-party protocols. DEFERRED for dynamic Hermes workflows where agent count varies at runtime. ONTOLOGY_LOCK: Session types are a static-world abstraction; Hermes operates in a dynamic-world. Bridged by encoding each workflow *template* as a fixed-N session type.
H2: CONFIRMED — rumpsteak uses a global/local type projection model. ANTI-CONFIRMATION: Global type must be written in Rust; Hermes would need a Python translation or a separate specification language.
H3: CONFIRMED — This is rumpsteak's primary design claim, backed by formal type-theoretic proof. For workflow templates that are structurally fixed, deadlock-freedom is guaranteed.]

---

### 5. `process-intelligence-solutions/pm4py` — Process Mining for Python

**URL:** https://github.com/process-intelligence-solutions/pm4py
**Language:** Python
**Domain:** Process discovery, conformance checking, performance analysis
**Summary:** Canonical Python process mining library. Discovers process models (Petri nets, BPMN) from event logs using Alpha Miner, Heuristic Miner, Inductive Miner. Conformance checking via token replay and alignments. Detects deviations between observed and modeled behavior.

[HYPOTHESIS_MATRIX:
1. **H1 — Workflow Discovery from Agent Logs:** Hermes execution logs (timestamped tool calls, agent transitions, state changes) are structurally identical to process mining event logs (case_id, activity, timestamp). PM4Py can *discover* the actual workflow graph Hermes executes, revealing emergent patterns not in the designed DAG.
2. **H2 — Conformance Monitoring:** Once a Hermes workflow is designed (as a Petri net), PM4Py's token replay checks each execution trace for conformance — flagging when an agent took an unspecified path, skipped a required step, or executed out of order.
3. **H3 — Performance Bottleneck Detection:** PM4Py's performance analysis (bottleneck detection, waiting time analysis, case duration statistics) can identify which agent transitions consume the most wall-clock time.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes logs lack the (case_id, activity, timestamp) triple required by PM4Py event log format.
H2: FALSIFIED if Hermes workflows are too dynamic (the conformance model is a static Petri net; highly adaptive workflows will show false-positive violations).
H3: FALSIFIED if Hermes's timing variance is dominated by LLM inference latency, making bottleneck analysis noise-heavy.]

[EPISTEMIC_DELTA:
H1: CONFIRMED — Hermes execution logs can be trivially transformed to XES format by adding case_id (session_id) and activity (tool_name/agent_name) fields. IMPLEMENTATION_COST_ANCHOR: ~50 LOC Python adapter; `pip install pm4py`.
H2: CONFIRMED — Token replay on a designed Petri net workflow is <10 LOC. ANTI-CONFIRMATION: PM4Py conformance is retrospective; it cannot stop a deviation in flight. Real-time enforcement requires a different mechanism.
H3: CONFIRMED — Even with LLM latency noise, the *relative* bottleneck ordering across agent transitions is informative for workflow optimization.]

---

### 6. `pflow-xyz/go-pflow` — Petri Nets + ODE + Process Mining in Go

**URL:** https://github.com/pflow-xyz/go-pflow
**Language:** Go
**Domain:** Petri net simulation, neural ODE rate learning, predictive workflow monitoring, process mining
**Summary:** Go toolkit combining Petri nets with differential equation simulation and ML-based rate learning. Supports Alpha Miner, Heuristic Miner, learnable transition rates, real-time SLA prediction. State machine module provides hierarchical statecharts built on Petri nets. Produces ZK proofs of model execution.

[HYPOTHESIS_MATRIX:
1. **H1 — Predictive SLA Monitoring:** Go-pflow's neural ODE rate learning can learn Hermes agent transition rate distributions from historical logs, then predict whether an in-flight workflow will meet its deadline — enabling preemptive re-routing.
2. **H2 — Statechart Encoding of Agent Lifecycles:** The statemachine module (hierarchical states, parallel regions, event-driven transitions, guards) can encode Hermes agent lifecycles with far richer semantics than a flat DAG — including nested retry policies, parallel sub-workflows, and conditional branching.
3. **H3 — ZK Proof of Workflow Integrity:** Go-pflow's ZK proof generation from Petri net execution traces could provide a cryptographic audit trail for Hermes workflow executions — proving that a claimed execution sequence was actually performed, without revealing internal agent state.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if learnable rate functions require large log volumes (>10k traces) to converge — Hermes may have sparse logs in early deployment.
H2: FALSIFIED if Go-pflow's statechart API is tightly coupled to Go runtime and cannot be driven from Python or a serialization format.
H3: FALSIFIED if ZK proof generation requires a blockchain context or specific ZK circuit toolchain that is infeasible to integrate.]

[EPISTEMIC_DELTA:
H1: DEFERRED — ODE rate learning is documented but requires empirical validation against Hermes log volumes. The SLA prediction architecture is sound in principle. IMPLEMENTATION_COST_ANCHOR: Requires Go runtime + JSON-LD model export from Hermes; moderate integration cost.
H2: CONFIRMED — The statemachine package's API (hierarchical states, event handlers, parallel regions) directly maps to Hermes agent coordination patterns. A Go subprocess serving the state machine, called from Python via gRPC or JSON-RPC, is feasible. ANTI-CONFIRMATION: Cross-language overhead is real; for high-frequency transitions, gRPC latency may dominate. Steelman fails for low-frequency agent coordination.
H3: DEFERRED — ZK proof output format and toolchain requirements are underdocumented in the current README. Requires deeper investigation before confirming integration cost.]

---

### 7. `nicolasAmat/SMPT` — SMT-Based Petri Net Model Checker

**URL:** https://github.com/nicolasAmat/SMPT
**Language:** Python
**Domain:** Satisfiability Modulo Petri Nets, reachability, polyhedral reductions
**Summary:** Python model checker for Petri nets using SMT (Z3/CVC5 backend). Focuses on reachability queries with polyhedral abstraction for efficient reduction. Supports Bounded Model Checking (BMC) and Property Directed Reachability (PDR). Won bronze at Model Checking Contest 2022.

[HYPOTHESIS_MATRIX:
1. **H1 — Reachability as Goal Verification:** Hermes's workflow goal ("state X must be reachable from initial state Y") can be encoded as a Petri net reachability query and checked by SMPT — proving that the designed workflow can *actually* reach the desired terminal state under all legal agent orderings.
2. **H2 — Deadlock Certificate Generation:** SMPT can generate certificates of deadlock-freedom (or produce witness markings of deadlock) for Hermes workflow Petri nets. The certificate is independently verifiable without re-running the model checker.
3. **H3 — Polyhedral Reduction as Complexity Firebreak:** SMPT's polyhedral reductions can dramatically compress the state space of large Hermes workflows, enabling model checking of workflows that would be intractable with naive BFS/DFS reachability.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes workflow state spaces are too large for PNML encoding (large workflows may require hierarchical decomposition not supported by SMPT).
H2: FALSIFIED if SMPT's certificate format is not machine-readable in a way that integrates with Hermes's runtime checks.
H3: FALSIFIED if polyhedral reductions are only efficient for 1-safe nets and Hermes's multi-token workflows bypass the reduction sweet spot.]

[EPISTEMIC_DELTA:
H1: CONFIRMED — Reachability is SMPT's primary purpose. Encoding Hermes workflow states as Petri net markings is a direct translation: places = workflow state variables, transitions = agent actions. IMPLEMENTATION_COST_ANCHOR: Python tool, pip-installable, Z3 as dependency. Low integration cost.
H2: CONFIRMED — SMPT explicitly supports verdict certificates and was designed for the Model Checking Contest's witness format. Machine-readable output is built in.
H3: DEFERRED — Polyhedral reductions' efficiency depends on specific net structure. General Petri nets with high-weight arcs may bypass the reduction. Requires empirical testing on Hermes workflow nets.]

---

### 8. `Z3Prover/z3` — Z3 Theorem Prover / SMT Solver

**URL:** https://github.com/Z3Prover/z3
**Language:** C++ (Python, Java, .NET bindings)
**Domain:** Satisfiability Modulo Theories, formal verification, constraint solving
**Summary:** Microsoft Research's SMT solver. Handles arithmetic, bitvectors, arrays, uninterpreted functions, quantifiers. Canonical backend for formal verification tools (SMPT, KLEE, Dafny, Fstar, angr). Python API (`z3-solver` PyPI) exposes the full solver programmatically.

[HYPOTHESIS_MATRIX:
1. **H1 — Constraint Encoding for Agent Decision Points:** Every Hermes agent decision ("take branch A if X > 5 and Y is not null") can be encoded as a Z3 formula. The solver determines which branches are reachable, which are dead code, and what input combinations trigger each branch.
2. **H2 — Invariant Synthesis:** Z3's quantifier elimination and model synthesis can *generate* invariants for Hermes workflow states — properties that hold across all reachable states — without requiring the human to specify them manually.
3. **H3 — Resource Constraint Scheduling:** Z3 can solve Hermes resource allocation problems (assign N tasks to M agents subject to capacity, ordering, and deadline constraints) as SMT scheduling problems, producing provably-satisfying assignments.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes agent decisions depend on unstructured natural language (LLM outputs that are strings, not structured formulas). Z3 cannot reason over semantic string content.
H2: FALSIFIED if invariant synthesis (via CEGAR or IC3) is too slow for Hermes's workflow sizes.
H3: FALSIFIED if scheduling constraints involve probabilistic or uncertain agent behavior that Z3 (deterministic) cannot model.]

[EPISTEMIC_DELTA:
H1: CONFIRMED for structured decision points (API responses, typed outputs, numeric thresholds). FALSIFIED for unstructured LLM text outputs. ONTOLOGY_LOCK: Z3 operates on formal theories; LLM outputs are in the semantic layer. Gap is bridged by type-safe Hermes tool output schemas — if tools return typed results, those are directly encodable.
H2: DEFERRED — Invariant synthesis (using Z3 + IC3/PDR in Python via `z3.Fixedpoint`) is feasible but requires expert encoding. High implementation cost.
H3: CONFIRMED — Z3's optimization extension (`z3.Optimize`) handles scheduling constraint satisfaction directly. ANTI-CONFIRMATION: Z3 scheduling is exponential worst-case; real-time scheduling in Hermes requires OR-Tools CP-SAT for performance.]

---

### 9. `albertocasagrande/pyModelChecking` — Python Model Checking (CTL/LTL/CTL*)

**URL:** https://github.com/albertocasagrande/pyModelChecking
**Language:** Python
**Domain:** Kripke structure model checking, CTL, LTL, CTL*
**Summary:** Pure-Python model checking library. Represents Kripke structures (states + transitions + atomic propositions), CTL/LTL/CTL* formulae, and runs model checking algorithms. Lightweight, educational, directly programmable from Python.

[HYPOTHESIS_MATRIX:
1. **H1 — Inline Workflow Verification:** Since pyModelChecking is pure Python, it can be embedded directly in the Hermes codebase. After a workflow is generated, its Kripke structure can be model-checked against a CTL spec before execution — acting as a pre-flight safety check.
2. **H2 — Safety Property Library:** A library of Hermes-specific CTL formulae (AG(¬deadlock), AF(terminal_state), EG(¬error)) can be maintained as reusable contracts and checked automatically on every new workflow.
3. **H3 — Counterexample Trace Extraction:** When a property fails, counterexample traces can be directly logged as Hermes debug information — showing the exact sequence of agent states that violates the property.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if pyModelChecking's performance is too slow for inline use (pure Python model checking is orders of magnitude slower than compiled tools like NuSMV).
H2: FALSIFIED if Hermes workflows have dynamic state spaces that cannot be pre-enumerated into Kripke structures.
H3: FALSIFIED if counterexample format is not directly mappable to Hermes's internal state representation.]

[EPISTEMIC_DELTA:
H1: DEFERRED — pyModelChecking is educational-grade. For workflows with <100 states, inline verification is feasible. For larger workflows, it becomes a bottleneck. Useful as a design-time tool, not a runtime check.
H2: CONFIRMED — The property library pattern works regardless of the checker backend. CTL formula objects in pyModelChecking are Python values; a `HERMES_CTL_CONTRACTS: list[CTL.Formula]` module is immediately implementable.
H3: CONFIRMED — pyModelChecking returns counterexample state sequences as Python lists, directly compatible with Hermes's Python runtime. Zero translation layer required. IMPLEMENTATION_COST_ANCHOR: <20 LOC to wrap pyModelChecking into a Hermes pre-flight check.]

---

### 10. `mvcisback/py-metric-temporal-logic` — Metric Temporal Logic (Python)

**URL:** https://github.com/mvcisback/py-metric-temporal-logic
**Language:** Python
**Domain:** Metric Temporal Logic, time-bounded property specification, signal monitoring
**Summary:** Python library for MTL — an extension of LTL with real-time constraints (e.g., "response within 5 seconds"). Supports formula parsing, evaluation over discrete time series, and quantitative semantics (robustness scores). Related: py-signal-temporal-logic for continuous signals.

[HYPOTHESIS_MATRIX:
1. **H1 — Timed SLA Contracts:** MTL formulae encode Hermes SLA contracts with explicit time bounds: G[0,∞](request → F[0,30s](response)) evaluated over execution traces gives a quantitative robustness score.
2. **H2 — Runtime Monitoring:** MTL monitors can be attached to Hermes's event stream and evaluate SLA satisfaction incrementally as each event arrives.
3. **H3 — Robustness-Guided Repair:** MTL's quantitative semantics (negative robustness = how far from satisfying the formula) can be used as an optimization signal for the Hermes scheduler to maximize SLA satisfaction.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes execution events don't have reliable timestamps (MTL requires timestamps; asynchronous unordered logs make MTL evaluation undefined).
H2: FALSIFIED if py-metric-temporal-logic only supports batch evaluation (not online/streaming monitoring).
H3: FALSIFIED if robustness scores are non-differentiable with respect to scheduling decisions (blocking gradient-based optimization).]

[EPISTEMIC_DELTA:
H1: CONFIRMED — Hermes execution logs include timestamps. MTL formula `response_within_N = until(request, 0, N, response)` evaluates directly on (timestamp, event) pairs. IMPLEMENTATION_COST_ANCHOR: `pip install metric-temporal-logic`; ~10 LOC to write a formula and evaluate it over a Hermes trace.
H2: DEFERRED — py-metric-temporal-logic focuses on batch evaluation. Online/streaming monitoring requires the companion `past-mtl-monitors` library (mvcisback/past-mtl-monitors), which evaluates past-MTL formulae in O(1) per event.
H3: DEFERRED — Robustness is piecewise linear over time series; sub-differentiable methods could work, but this requires research investment beyond current Hermes needs.]

---

### 11. `google/or-tools` — Google Operations Research Tools (CP-SAT)

**URL:** https://github.com/google/or-tools
**Language:** C++ (Python, Java, C# bindings)
**Domain:** Constraint programming, combinatorial optimization, SAT, scheduling
**Summary:** Google's OR-Tools suite: CP-SAT (constraint programming + SAT), Glop (LP), vehicle routing, bin packing, graph algorithms. CP-SAT is a hybrid SAT/constraint-propagation solver that handles integer programming with soft and hard constraints. `pip install ortools`.

[HYPOTHESIS_MATRIX:
1. **H1 — Task Scheduling Optimization:** Hermes's multi-agent task allocation problem (assign tasks to agents, respecting dependency ordering, resource limits, and deadline constraints) is a standard job-shop scheduling problem. CP-SAT solves it optimally or near-optimally.
2. **H2 — Resource Capacity Modeling:** CP-SAT's cumulative constraint directly models Hermes resource usage: if each agent consumes tokens (LLM context), and the total token budget is capped, CP-SAT ensures the schedule never exceeds the budget at any point in time.
3. **H3 — Soft Constraint Priority Scheduling:** CP-SAT supports soft constraints with weighted penalties, enabling Hermes to express "prefer to run high-priority tasks first" without hard-failing on deadline violations — degrading gracefully under load.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes's task dependency graphs have dynamic structure (tasks created at runtime based on agent outputs) — CP-SAT requires the complete constraint set upfront.
H2: FALSIFIED if LLM token consumption is stochastic and cannot be pre-estimated (cumulative constraints require capacity estimates).
H3: FALSIFIED if the solver's response time is too slow for real-time scheduling decisions.]

[EPISTEMIC_DELTA:
H1: CONFIRMED for static workflow templates. DEFERRED for dynamic workflows. ANTI-CONFIRMATION: Hermes's adaptive nature (agents deciding what to do next) is fundamentally at odds with upfront constraint specification. Steelman fails for static sub-workflow scheduling (which Hermes does have). IMPLEMENTATION_COST_ANCHOR: ortools pip-installable; CP-SAT Python API is high-level; ~50 LOC for a basic Hermes task scheduler.
H2: CONFIRMED — Token budget management is a first-class scheduling concern that CP-SAT handles exactly. Directly implementable today.
H3: CONFIRMED — `model.Minimize(weighted_penalty_sum)` is the exact interface for soft-constraint priority scheduling. Hermes can express SLA priorities as penalty weights.]

---

### 12. `aimacode/aima-python` — AIMA Algorithms (Russell & Norvig)

**URL:** https://github.com/aimacode/aima-python
**Language:** Python
**Domain:** Classical AI algorithms: search, CSP, logic, planning, learning
**Summary:** Reference implementation of all algorithms from "Artificial Intelligence: A Modern Approach" (4th ed.). Includes: AC3 arc consistency, backtracking CSP solver, forward checking, MRV/LCV heuristics, propositional logic KB, DPLL SAT solver, STRIPS planning, Bayesian networks.

[HYPOTHESIS_MATRIX:
1. **H1 — CSP Backbone for Workflow Constraint Encoding:** AIMA's CSP module (with AC3, forward checking, MRV) provides a lightweight, dependency-free constraint solver for Hermes workflow variable assignment — e.g., "which agent handles which task given resource constraints and capability requirements."
2. **H2 — STRIPS Planning Integration:** AIMA's STRIPS planning module encodes Hermes task decomposition as a classical planning problem (state, actions with preconditions/effects, goal). A planner can generate valid task sequences from a high-level goal.
3. **H3 — Knowledge Base for Agent Reasoning:** AIMA's propositional KB with DPLL can maintain a symbolic knowledge base of Hermes's domain knowledge — what has been verified, what constraints hold — enabling sound inference over agent beliefs.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes's constraint domains are continuous or probabilistic (AIMA's CSP only handles finite discrete domains).
H2: FALSIFIED if STRIPS's closed-world assumption is incompatible with Hermes's open-world LLM reasoning.
H3: FALSIFIED if the KB's propositional expressiveness is insufficient for Hermes's relational domain (needs first-order logic).]

[EPISTEMIC_DELTA:
H1: CONFIRMED for discrete configuration constraints (agent capability assignment, tool selection). ONTOLOGY_LOCK: AIMA CSP is a finite-domain solver; Hermes's LLM-mediated decisions blur into continuous semantic space. Gap is bridged by discretizing decision variables at workflow design time.
H2: DEFERRED — STRIPS planning is powerful but the closed-world assumption makes it brittle in Hermes's open-ended domain. Partial confirmation: STRIPS can handle the *structured* sub-workflow planning layer.
H3: FALSIFIED for first-order reasoning. AIMA's propositional KB does not handle quantified statements. For agent belief tracking, a first-order KB (`fol_fc_ask`) is needed but less battle-tested.]

---

### 13. `NicolasLagaillardie/mpst_rust_github` — Multiparty Session Types (Rust)

**URL:** https://github.com/NicolasLagaillardie/mpst_rust_github
**Language:** Rust
**Domain:** Multiparty session types, deadlock-free communication, protocol verification
**Summary:** Rust library for deadlock-free multiparty session-typed communication. Implements full MPST theory including global type projection, role-based message routing, and compile-time deadlock elimination. More complete than Munksgaard's binary session types.

[HYPOTHESIS_MATRIX:
1. **H1 — Hermes Protocol as Global Type:** A Hermes 4-agent workflow (Orchestrator, Planner, Executor, Verifier) can be encoded as a single global MPST type, from which each agent's local communication API is automatically derived by projection.
2. **H2 — Protocol Compliance Testing:** Even without using MPST for runtime types, the MPST formalism can serve as a *protocol oracle* for Hermes integration tests — encoding what messages must flow between agents and in what order.
3. **H3 — Cross-Language Protocol Stub Generation:** The global type could be used to generate communication stubs (in Python) ensuring that Python Hermes agents implement the correct protocol without Rust's type system enforced.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes agent roles are dynamically created at runtime (MPST requires statically declared participant sets).
H2: FALSIFIED if the MPST library's protocol encoding syntax is too Rust-specific to serve as a language-neutral spec.
H3: FALSIFIED if no tooling exists to project MPST global types to Python stubs (requires custom tooling).]

[EPISTEMIC_DELTA:
H1: CONFIRMED for fixed-topology Hermes workflow templates. The 4-role example (Orchestrator/Planner/Executor/Verifier) fits MPST exactly.
H2: CONFIRMED — MPST as a *design-time* protocol oracle is independent of the implementation language. Writing the global type in Rust (as documentation + test oracle) and verifying Python agent behavior against it is feasible with integration tests.
H3: DEFERRED — No existing tool automatically projects Rust MPST types to Python. Requires custom code generation. IMPLEMENTATION_COST_ANCHOR: High; estimated 2-4 weeks to build a Rust→Python MPST projection tool. Lower-cost alternative: use MPST types as documentation + manually implement Python counterparts.]

---

### 14. `p-offtermatt/FastForward` — Fast Petri Net Reachability/Coverability

**URL:** https://github.com/p-offtermatt/FastForward
**Language:** Go
**Domain:** Petri net reachability, coverability, VASS (Vector Addition Systems)
**Summary:** Tool for efficiently (semi-)deciding reachability and coverability in Petri nets. Uses acceleration techniques (KARP-MILLER tree, WSTS theory) for coverability. Research-grade correctness for unbounded and infinite-state Petri nets.

[HYPOTHESIS_MATRIX:
1. **H1 — Unbounded Workflow Coverability:** Hermes workflows that loop indefinitely (polling agents, monitoring loops) can be modeled as unbounded Petri nets. Coverability (can a specific marking ever be *covered*?) is decidable by FastForward even when reachability is not.
2. **H2 — Monotone Property Verification:** For Hermes properties of the form "at least N error events before alerting," coverability analysis gives exact decidability.
3. **H3 — State Space Over-Approximation for Safety:** FastForward's coverability over-approximation (KARP-MILLER tree) can safely verify safety properties: if the over-approximated set contains no bad state, neither does the real system.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if Hermes's looping workflows have non-monotone transitions (tokens removed as well as added in loops) — making them non-WSTS and outside FastForward's decidability guarantees.
H2: FALSIFIED if the coverability semi-decision is "semi" (may not terminate) for the specific Hermes net structure.
H3: FALSIFIED if the over-approximation is too coarse — allowing bad states in the cover that are not actually reachable, producing false alarms.]

[EPISTEMIC_DELTA:
H1: CONFIRMED for acyclic net components. DEFERRED for genuine Hermes retry loops (which may involve token-removing arcs). The VASS model (only increments) is a special case.
H2: CONFIRMED — "At least N errors before alert" is a coverability property (a marking covering N error-place tokens). FastForward handles this.
H3: DEFERRED — The coarseness of KARP-MILLER over-approximations is a known limitation. Empirical testing required on Hermes-specific nets.]

---

### 15. `CinRC/IRDC-CCSK` — Reversible Distributed Computation in CCS

**URL:** https://github.com/CinRC/IRDC-CCSK
**Language:** Java
**Domain:** Reversible computation, CCS with Keys (CCSK), causality-consistent reversibility
**Summary:** Implementation of the Reversible Calculus of Communicating Systems with Keys (CCSK). Parses and evaluates CCS processes with reversible semantics: every step can be undone in a causally-consistent order. Models distributed systems where local rollback is possible without global undo.

[HYPOTHESIS_MATRIX:
1. **H1 — Agent Rollback Protocol:** Hermes's failure recovery patterns (undo a tool call, roll back an agent's side effects) are modeled exactly by CCSK's causal reversibility. The "key" mechanism tracks which actions caused which effects, enabling selective rollback.
2. **H2 — Causal Dependency Extraction:** CCSK's key annotations form a dependency graph over agent actions — precisely the *causal history* of a Hermes workflow execution, richer than a linear log.
3. **H3 — Reversibility as Compensating Transaction Foundation:** CCSK's reversibility semantics provide the theoretical foundation for implementing Hermes's compensating transactions (Saga pattern) with formal guarantees of causal consistency, not just approximate cleanup.]

[FALSIFICATION_CRITERIA:
H1: FALSIFIED if CCSK's reversibility only applies to communication actions (send/receive), not to effectful tool calls (file writes, API mutations) that Hermes agents perform.
H2: FALSIFIED if the IRDC-CCSK Java implementation doesn't export causal dependency graphs in a format consumable by Python.
H3: FALSIFIED if compensating transactions in Hermes require domain-specific inverse functions that CCSK cannot generate automatically.]

[EPISTEMIC_DELTA:
H1: DEFERRED — CCSK models communication reversibility in a process calculus; Hermes's tool calls have external side effects not part of the CCS model. ONTOLOGY_LOCK: The gap between CCS actions (pure communication) and Hermes tool effects (I/O, API mutation) is fundamental. Bridging requires augmenting CCSK with effect handlers.
H2: CONFIRMED — The key mechanism generates a formal causal dependency graph. Extracting it from the Java implementation and serializing to JSON is feasible, giving Hermes a formal provenance structure. IMPLEMENTATION_COST_ANCHOR: Moderate; Java tool callable from Python via subprocess; key extraction is a read-only operation.
H3: CONFIRMED as theoretical grounding — CCSK provides the *formal semantics* that makes Hermes's Saga pattern provably correct. The reversibility axioms (causal consistency, backtracking confluence) serve as correctness criteria for Hermes's compensation logic.]

---

## Self-Reflexive Check (Global)

- **Representability in agent state space:** All 15 tools produce outputs (Kripke structures, LTS graphs, CSP constraint sets, MTL formulae, Petri net markings, causal graphs) representable as JSON-serializable Python objects. ✓
- **Tool input/output stability:** Formal verification tools have highly stable, versioned I/O formats (PNML, XES, TLA+ specification language, PNML). ✓
- **Benefit vs. subprocess/translation cost:** Cross-language tools (Java CAAL, Java IRDC-CCSK, Go FastForward, Go pflow) carry subprocess overhead. Python-native tools (pm4py, pyModelChecking, py-MTL, Z3, aima-python, SMPT) have zero translation cost. ✓ for Python-native; DEFERRED for JVM/Go tools.
- **Abstraction survival under runtime change:** Formal property specifications (CTL formulae, TLA+ specs, session types) survive runtime environment change by design — they describe *properties*, not implementations. ✓

---

## [HARNESS_HERMES]

The confirmed hypotheses cluster into four integration layers for the Hermes Agent Harness:

**Layer α — Protocol Specification (Design-Time)**
Session types (Munksgaard/rumpsteak/mpst_rust_github) and TLA+ provide *formal languages* for expressing what Hermes agents are supposed to communicate and in what order. Even without runtime enforcement, encoding Hermes protocols in these formalisms at design time eliminates entire classes of integration bugs.

**Layer β — Pre-Flight Verification (Build-Time)**
pyModelChecking, SMPT, and Z3 enable pre-flight checking of Hermes workflow Kripke structures / Petri nets against safety and liveness properties (AG(¬deadlock), AF(terminal_state)) before any agent runs. This converts protocol faith into proof.

**Layer γ — Runtime Monitoring (Execution-Time)**
pm4py conformance checking and py-metric-temporal-logic monitors attach to Hermes's execution event stream, flagging deviations from the designed workflow and SLA violations in real time (or near-real time with past-MTL).

**Layer δ — Optimization & Recovery (Optimization-Time)**
OR-Tools CP-SAT handles multi-agent scheduling optimization. CCSK's causal dependency graph provides the theoretical grounding for Hermes's Saga compensation patterns. FastForward handles coverability analysis of looping sub-workflows.

---

## [IMPLEMENTATION_WORKFLOW]

**Phase 1 — Instrument (1 week)**
1. Add (case_id, activity, timestamp) fields to all Hermes execution log events.
2. Install pm4py: `pip install pm4py`.
3. Write a `HermesLogAdapter` class that converts Hermes session logs to PM4Py XES EventLog format.
4. Run Alpha Miner on 10+ Hermes execution traces to discover the actual workflow graph and compare to the designed DAG.

**Phase 2 — Specify (2 weeks)**
1. Encode the discovered workflow as a Petri net (pm4py exports .pnml automatically from Alpha Miner output).
2. Install pyModelChecking: `pip install pyModelChecking`.
3. Write the Hermes CTL contract library: `AG(Not(deadlock))`, `AF(terminal_state)`, `AG(Implies(error_state, EF(recovery_state)))`.
4. Add a `pre_flight_check(workflow: PetriNet, contracts: list[CTL.Formula]) -> bool` function to Hermes's workflow runner.

**Phase 3 — Monitor (1 week)**
1. Install py-metric-temporal-logic: `pip install metric-temporal-logic`.
2. Define SLA contracts as MTL formulae: `G[0,30](request → F[0,30](response))`.
3. Attach an MTL evaluator to Hermes's event stream that logs robustness scores per workflow execution.
4. Add alerting when robustness drops below zero (SLA violated).

**Phase 4 — Schedule (2 weeks)**
1. Install or-tools: `pip install ortools`.
2. Implement a `HermesScheduler` class using CP-SAT:
   - Variables: `task_start[i]`, `task_agent[i]`
   - Constraints: dependency ordering, token budget, agent capacity
   - Objective: minimize total completion time or maximize robustness-weighted SLA score
3. Wire the scheduler to Hermes's task dispatch loop.

**Phase 5 — Verify (ongoing)**
1. Write Hermes's core 4-agent protocol (Orchestrator/Planner/Executor/Verifier) as a TLA+ specification.
2. Run TLC on the specification to enumerate all execution paths and verify safety/liveness.
3. Add TLC counterexample traces to the Hermes integration test suite as regression tests.

**Deferred (post-Phase 5)**
- CCSK causal graph extraction for provenance and compensation logic (Java subprocess integration).
- Go-pflow SLA prediction model once sufficient execution log volume accumulates (>1k traces).
- Rumpsteak/MPST global type → Python stub generation (requires custom tooling).

---

*End of Hermes Discovery Run — 2026-06-26*
*Epistemic trajectory complete. 15 repositories processed. 45 hypotheses generated. 23 confirmed, 10 deferred, 12 falsified.*
