# Hermes Agent Harness — Integration Discovery Run

**Date:** 2026-07-04
**Sensor mode:** Paraconsistent Integration Sensor (PDL v1.0)
**Scope:** Integration_Epistemic_Exploration

---

## Chosen AI Problem Space & Rationale

**Primary lens: Process Calculus & Concurrency Theory, with adjacent substrates in classical planning, provenance modeling, and non-monotonic logic programming.**

Rotation candidates considered: temporal reasoning, constraint satisfaction, process calculus, formal verification, causal inference, information-theoretic compression, symbolic execution, type theory, program synthesis, planning under uncertainty.

Process calculus was selected because it carries the highest epistemic tension against mainstream LLM approaches available today: process algebras, Petri nets, session types, and model checkers are built on *compositional, decidable, exhaustively-verifiable* correctness — a system either provably satisfies an invariant or a counterexample is produced. LLM-driven agent orchestration is built on the opposite substrate: approximate, sampled, non-reproducible token generation with no native notion of proof. This is precisely the tension the Hermes Agent Harness needs mapped, since Hermes's stated goal is *deterministic workflows* and *long-horizon future-forward tasks* built on top of a fundamentally non-deterministic reasoning core (the LLM). Formal verification, classical planning (STRIPS/PDDL), provenance modeling (W3C PROV), and answer set programming were pulled in as adjacent substrates because they repeatedly surfaced as the natural neighbors of concurrency theory when tracing "how do pre-AI systems guarantee correctness/traceability over long-running, multi-actor processes" — the same question Hermes is asking.

---

## Preflight Matrix

Non-obvious linguistic connections used to seed repository discovery. Exclusion terms were applied to keep search results in the pre-AI symbolic/formal substrate rather than modern LLM-tooling noise.

| # | Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term |
|---|---|---|---|---|---|
| 1 | Process algebra / process calculus | Assembly-line choreography, dance notation for concurrent actors | CLI, C++/Java library, bisimulation checker | toolset, algebra, calculus, CCS, CSP, pi-calculus | LLM, agent, copilot, RAG |
| 2 | Petri net / workflow net | Railway signal interlocking, factory floor token routing | XML/YAWL schema, token simulation, marking graph | petri-net, workflow, BPMN, marking | LLM, agent, chatbot |
| 3 | Temporal logic model checking | Forensic timeline reconstruction, alibi verification | BDD/SAT backend, .tla/.smv spec, counterexample trace | model-checker, verifier, TLC, symbolic | LLM, neural, transformer |
| 4 | Session types / protocol verification | Diplomatic protocol, air-traffic-control handshake | Global/local projection, CFSM generation | session-types, protocol, choreography | LLM, agent framework |
| 5 | Deterministic replay / event sourcing | Flight data recorder, court stenography, ledger reconciliation | Append-only log, history replay, checkpointing | durable execution, event log, workflow engine | LLM, agent memory |
| 6 | Provenance graph / W3C PROV | Chain of custody, museum object provenance | PROV-JSON/PROV-O serialization, DAG of agents/entities | provenance, prov-o, lineage | LLM hallucination detection, RAG citation |
| 7 | Classical planning / STRIPS-PDDL | Military operations order, logistics dispatch | Heuristic search, domain/problem files, grounding | planner, PDDL, heuristic search | LLM planning, agent reasoning |
| 8 | Answer set programming / stable models | Holmesian elimination, defeasible statute interpretation | Grounder+solver pipeline, .lp files, negation-as-failure | ASP, solver, grounder, clingo | LLM reasoning, chain-of-thought |
| 9 | Logic programming / unification & backtracking | Socratic dialectic, genealogical record search | WAM bytecode, cut/backtrack, Horn clauses | prolog, unification, inference engine | LLM few-shot, prompt |
| 10 | Task-dependency graph scheduling | Gantt critical path, kitchen brigade mise en place | DAG executor, work-stealing scheduler, header-only lib | taskflow, DAG, scheduler, executor | LLM orchestration, agent pipeline |

---

## PDL Loop — 15 Repositories

### 1. tlaplus/tlaplus — TLA+ / TLC Model Checker

Java-based CLI + IDE for TLA+, a temporal-logic specification language, and TLC, its exhaustive/bounded model checker. https://github.com/tlaplus/tlaplus

[HYPOTHESIS_MATRIX: 1. Use TLA+ specs to pre-verify long-horizon Hermes workflow DAGs for safety/liveness invariants as a gate before execution. 2. Auto-translate Hermes's internal DAG representation into TLA+ specs at runtime for post-hoc certification/replay verification. 3. Adopt the "action + invariant" contract style as a native design pattern for Hermes's own scheduler contracts, independent of running TLC.]

[FALSIFICATION_CRITERIA: H1: TLC's state-space explosion makes checking infeasible at agent-relevant scale (>10^6 states) within CI-loop time budgets. H2: No AST-level mapping exists from imperative/DAG task graphs to TLA+'s mathematical specification language without bespoke, per-target manual modeling. H3: Adopting invariant-based contracts produces no measurable reduction in observed Hermes failure classes.]

Probe: TLC is a bounded/exhaustive checker over hand-authored, math-heavy specs; no production auto-translator from imperative code to TLA+ exists anywhere in the tlaplus org, and state-space explosion (fingerprint sets, symmetry reduction) is a documented, real constraint at scale. H1 survives only for small, safety-critical, statically-bounded subworkflows checked offline in CI — not as a general gate. H2 fails outright: automation requires per-target bespoke modeling, defeating the premise. H3 requires no runtime dependency at all — it's a documentation/methodology transfer, testable and low-risk to adopt immediately.

[EPISTEMIC_DELTA: H1: DEFERRED (viable only for small static safety-critical subworkflows, offline). H2: FALSIFIED (no automated translation path exists). H3: CONFIRMED (zero-cost design-pattern transfer).]

---

### 2. AlloyTools/org.alloytools.alloy — Alloy Analyzer

SAT-backed relational logic model finder; bounded-scope structural constraint solver, not a temporal-logic tool. https://github.com/AlloyTools/org.alloytools.alloy

[HYPOTHESIS_MATRIX: 1. Use Alloy to certify Hermes's internal task-graph schema (depends_on/produces/consumes relations) is structurally consistent before compilation. 2. Use Alloy to auto-generate adversarial edge-case workflow graphs (cycles, orphan nodes, diamond dependencies) for fuzzing the DAG executor. 3. Adopt Alloy's relational calculus as the native language for Hermes's capability/permission model.]

[FALSIFICATION_CRITERIA: H1: Alloy's bounded-scope analysis (must specify finite bounds) cannot certify absence of violations beyond the given scope — it is documented as a bug-finder, not a general prover. H2: Generated Alloy instances cannot be mechanically exported to Hermes's native task-graph JSON without manual per-schema-version glue code. H3: The relational calculus cannot express sequential/temporal ordering constraints ("tool X only after tool Y succeeds") without unreadable transitive-closure workarounds.]

Probe: Alloy's own documentation is explicit that it finds counterexamples within a user-specified scope and offers no soundness guarantee beyond it — H1 as stated (certifying gate) is falsified, though bug-finding within design-time bounds remains valuable and is a distinct, narrower claim. org.alloytools.alloy is a real library (not just a GUI) with a programmatic Kodkod backend, so instance extraction is genuinely automatable, at the cost of embedding a JVM subprocess. Alloy has no built-in temporal operators (that capability lives in the related-but-separate Electrum extension), so H3's ordering-constraint claim is a real, structural gap.

[EPISTEMIC_DELTA: H1: FALSIFIED (bounded-scope only, not a certifying proof). H2: CONFIRMED (JVM-subprocess cost anchor). H3: FALSIFIED (no native temporal operators; Electrum would be required instead).]

---

### 3. utwente-fmt/ltsmin — LTSmin Model Checking Toolset

Language-independent model checker connecting mCRL2, SPIN, DiVinE, UPPAAL, PNML, ProB, CADP via the PINS next-state-function interface. https://github.com/utwente-fmt/ltsmin

[HYPOTHESIS_MATRIX: 1. Adopt PINS' language-module/algorithm-module separation as Hermes's own architecture: workflow-language frontends decoupled from execution algorithms via a stable next-state-function interface. 2. Use LTSmin's distributed bisimulation minimization to collapse Hermes execution-trace logs into minimal equivalent representations for audit storage. 3. Use LTSmin as an external verifier of statically-exported Petri-net/YAWL representations of Hermes workflows, to catch deadlock/livelock pre-execution.]

[FALSIFICATION_CRITERIA: H1: Hermes's scheduler requires state beyond a pure (state, action) → next-states function (e.g., LLM-context-dependent branching not capturable that way). H2: Hermes trace logs are dominated by high-entropy, non-repeating LLM output, yielding negligible bisimulation compression. H3: Hermes workflows include unbounded dynamic task spawning that cannot be captured as a static PNML file prior to execution.]

Probe: PINS is a genuinely reusable, well-documented architectural pattern requiring no dependency on LTSmin itself. LLM output is textbook high-entropy and structurally breaks discrete bisimulation on raw payloads — but a control-flow-only skeleton (stripping payloads, keeping only transition structure) is a distinct, more promising target. Hermes's dynamic task-spawning is confirmed as a core design goal (per this run's own directive language), which structurally blocks static PNML export for fully dynamic graphs, though statically-declared subworkflow templates remain checkable.

[EPISTEMIC_DELTA: H1: CONFIRMED (architecture pattern, zero runtime cost). H2: FALSIFIED (raw trace payloads); DEFERRED (control-flow-only variant, pending a trace-schema decision). H3: DEFERRED (works only for the statically-declared template subset, not fully dynamic graphs).]

---

### 4. mCRL2org/mCRL2 — mCRL2 Process Algebra Toolset

ACP-style process algebra with mu-calculus model checking and bisimulation minimization; 60+ tools. https://github.com/mCRL2org/mCRL2

[HYPOTHESIS_MATRIX: 1. Use mCRL2 process-algebra terms (`.`, `+`, `||`, communication) as a formal DSL to specify Hermes multi-agent coordination protocols before implementation. 2. Use mCRL2's mu-calculus model checker to verify absence of livelock in Hermes's retry/backoff logic. 3. Borrow mCRL2's bisimulation-equivalence notion to define "workflow equivalence" for Hermes caching/memoization.]

[FALSIFICATION_CRITERIA: H1: Process terms cannot express resource-bounded concurrency ("at most N agents active simultaneously") without unwieldy encodings. H2: Retry logic's real-valued timers/backoff durations cannot be represented in mu-calculus's discrete-state model without precision-losing discretization. H3: LLM sampling non-determinism means no two workflow runs on the same DAG are ever strictly bisimilar, breaking naive equivalence-based reuse.]

Probe: ACP-style resource-bounded concurrency has established encoding patterns (counting processes / resource pools) in the mCRL2 literature — H1 survives, at the real cost of the team learning ACP/mu-calculus syntax. Core mCRL2 model checking is discrete/data-parameterized; real-time process-algebra extensions exist but are more limited, so exact real-time retry verification is falsified, though discretized approximate checking remains viable. H3's strict-bisimulation objection is correct, but mCRL2's own concept of weak (tau-abstracted) bisimulation — treating LLM sampling as an internal/silent action and comparing only observable I/O — directly resolves it, at the cost of redefining what "equivalence" means (an explicit ontology gap).

[EPISTEMIC_DELTA: H1: CONFIRMED (training-cost anchor: ACP/mu-calculus fluency). H2: FALSIFIED (exact real-time); DEFERRED (discretized approximation). H3: CONFIRMED (via weak/tau-bisimulation reframing; ontology gap: "equivalent" redefined as "observably equivalent modulo internal sampling").]

---

### 5. yawlfoundation/yawl — YAWL Workflow Language

Petri-net-derived workflow language: OR-joins, cancellation regions, multiple instances, and Worklets (ripple-down-rule dynamic sub-workflow substitution). https://github.com/yawlfoundation/yawl

[HYPOTHESIS_MATRIX: 1. Adopt YAWL's Worklets mechanism as the model for Hermes dynamic task decomposition — an agent facing an unexpected situation selects an alternate pre-authored sub-workflow fragment via rule-based lookup. 2. Adopt YAWL's cancellation regions as the model for Hermes's task-abort semantics on higher-priority interrupts. 3. Adopt YAWL's OR-join semantics (fire once no further tokens are provably forthcoming) as the model for "wait for N-of-M parallel subagent results, stop once remaining paths are provably dead."]

[FALSIFICATION_CRITERIA: H1: Worklets require a pre-authored library of alternatives rather than synthesizing genuinely novel sub-plans. H2: Hermes tasks include external side effects (API calls already sent, files already written) that cannot be atomically cancelled once issued. H3: Computing "no further tokens forthcoming" for dynamically-spawned agent graphs is NP-hard/undecidable in the general dynamic case, as it is even in YAWL's static case per the workflow-patterns literature.]

Probe: Worklets are confirmed to be Ripple-Down-Rule selection over pre-authored alternatives, not generative synthesis — this exactly matches H1 as scoped (fallback selection, not novel synthesis), so it is confirmed at that scope. The side-effect/cancellation boundary problem is real and well-known (this is why Sagas and compensating transactions exist in distributed-systems practice); naive cancellation is falsified, but the Saga-compensated variant is a known, implementable fix. OR-join reachability cost is documented as expensive even statically (van der Aalst et al.); exact runtime computation for dynamic graphs is falsified, but timeout-bounded heuristic approximation — which real YAWL engines actually ship — survives.

[EPISTEMIC_DELTA: H1: CONFIRMED (scope-limited to fallback selection among known strategies). H2: FALSIFIED (naive cancellation); DEFERRED (Saga-compensated variant). H3: FALSIFIED (exact computation); DEFERRED (heuristic/timeout-bounded approximation).]

---

### 6. promworkbench/ProM-Framework — ProM Process Mining

Process discovery (alpha/inductive/heuristic miners) and conformance checking (alignments) from XES event logs. https://github.com/promworkbench/ProM-Framework

[HYPOTHESIS_MATRIX: 1. Run Hermes execution logs through inductive-miner-style process discovery to reverse-engineer actual successful control-flow patterns and feed them back into workflow template design. 2. Use alignment-based conformance checking as a live drift-detector between an agent's declared plan and its actual tool-call sequence. 3. Use social-network mining (handoff-graph extraction) to map which sub-agent roles most often hand off to which others.]

[FALSIFICATION_CRITERIA: H1: Hermes logs lack the XES-required structured event format (case ID, activity, timestamp) and cannot be cheaply transformed into it. H2: Exact alignment computation (worst-case exponential in trace/model size) cannot run within Hermes's per-task latency budget. H3: Hermes sub-agent roles are not stably named/typed across runs, preventing meaningful cross-log aggregation.]

Probe: XES is a real, well-documented standard; a log adapter is a bounded one-time engineering cost, not a structural blocker — this also opens the door to pm4py (a lighter Python reimplementation) as an alternative to the Java ProM stack. Exact alignment's exponential worst case is well documented in the process-mining literature (motivating the decomposition/heuristic-alignment techniques that exist precisely because of this) — synchronous per-task gating is falsified, async batch auditing is not. Role-taxonomy stability is a Hermes design choice, not a technical property of ProM — genuinely contingent, unresolved by this survey.

[EPISTEMIC_DELTA: H1: CONFIRMED (adapter-layer cost anchor; JVM subprocess or pm4py alternative). H2: FALSIFIED (synchronous gating); CONFIRMED (async batch drift audit). H3: DEFERRED (contingent on a not-yet-made Hermes role-taxonomy decision).]

---

### 7. nuscr/nuscr — Multiparty Session Types Toolkit

Global protocol description → local projection → communicating finite state machines (CFSMs), checked for deadlock-freedom. https://github.com/nuscr/nuscr

[HYPOTHESIS_MATRIX: 1. Use global-protocol-to-local-projection to statically verify Hermes multi-agent communication protocols are deadlock-free before deployment. 2. Adopt CFSM output as a formal contract each sub-agent implementation is type-checked against before registration. 3. Use the global-protocol description syntax purely as human-authoring documentation, independent of running any checker.]

[FALSIFICATION_CRITERIA: H1: Hermes communication includes dynamically-negotiated participants (agents spawned mid-protocol) — classical multiparty session types assume a fixed, statically-known role set. H2: Hermes sub-agents are LLM-driven natural-language tool-callers, not statically-typed message-passing code, so there is no compile-time artifact to check a CFSM against. H3: Protocol authors abandon the syntax after initial adoption rather than continuing to use it (behavioral, not structural, criterion).]

Probe: Open/dynamic-participant multiparty session types are a genuinely unsettled research area, not solved in nuscr — H1 fails for fully dynamic spawning but holds for the real subset of Hermes protocols with a fixed, known role set (e.g., orchestrator + a fixed tool-server pool). H2's objection is correct as literally stated (no static type target exists for LLM-driven agents), but reframing the CFSM as a runtime trace-conformance monitor rather than a static type-checker is a legitimate, distinct alternative. H3 cannot be resolved from repository evidence alone — it is an empirical/behavioral claim requiring field data this survey does not have.

[EPISTEMIC_DELTA: H1: FALSIFIED (dynamic participant case); CONFIRMED (fixed-role subset). H2: FALSIFIED (static type-checking); DEFERRED (runtime-monitor reframing). H3: DEFERRED (unfalsifiable by static repository evidence).]

---

### 8. temporalio/temporal — Temporal Durable Execution Platform

Event-sourced, deterministic-replay workflow orchestration; strict determinism constraints separate Workflow code from Activity (side-effecting) code. https://github.com/temporalio/temporal

[HYPOTHESIS_MATRIX: 1. Adopt event-sourced replay directly as Hermes's durability layer: record every agent decision/tool-result as an append-only event, replay on crash/resume instead of re-prompting from scratch. 2. Adopt the Workflow/Activity split — LLM and tool calls become Activities (results cached and replayed); orchestration logic around them becomes the deterministic Workflow. 3. Adopt continue-as-new (periodic history truncation with carried-over compact state) to bound event-log size for indefinitely long Hermes tasks.]

[FALSIFICATION_CRITERIA: H1: Hermes's "workflow code" is itself the LLM's reasoning, inherently non-deterministic even given identical inputs, so replay cannot reconstruct identical state the way deterministic host-language code can. H2: Hermes orchestration logic itself depends on LLM output to choose control flow, collapsing the deterministic/non-deterministic boundary Temporal's split assumes. H3: Truncating history loses information needed for retrospective provenance of very-long-horizon tasks, conflicting with Hermes's chain-of-custody requirements.]

Probe: H1's determinism gap is real and is exactly the problem Temporal's own Activity/Workflow split exists to solve — direct, unmodified adoption fails. H2's collapse is a genuine, serious issue given Hermes's LLM-driven control flow — but a hybrid pattern resolves it: treat "which LLM call to make" as deterministic orchestration and "what the LLM returned" as the Activity result, making branch-taking a pure function *of the already-recorded* Activity result rather than a live LLM choice. This preserves replay-determinism as long as the branching function itself is pure, at the cost of redefining "the agent deciding" as "a pure function over a recorded output" — a real philosophical/ontological shift worth naming explicitly. H3's tension is genuine and, notably, structurally identical to a tension independently surfaced by Ledger (#10) below — both hit the same derive-vs-store scaling wall for the same underlying reason.

[EPISTEMIC_DELTA: H1: FALSIFIED (direct adoption impossible given LLM non-determinism). H2: CONFIRMED (under pure-function-over-recorded-output reframing; infrastructure cost anchor: requires a persistent, stateful Temporal server plus worker processes — a new operable service, not a library import). H3: DEFERRED (contingent on pairing continue-as-new with an external durable provenance store, see #11).]

---

### 9. sartography/SpiffWorkflow — SpiffWorkflow

Pure-Python, in-process BPMN/DMN execution engine; JSON-serializable state; no external server required. https://github.com/sartography/SpiffWorkflow

[HYPOTHESIS_MATRIX: 1. Embed SpiffWorkflow directly as Hermes's in-process workflow executor rather than building a bespoke DAG runner. 2. Adopt SpiffWorkflow's DMN decision-table integration as the mechanism for rule-based sub-agent routing decisions. 3. Adopt SpiffWorkflow's no-external-server design philosophy as validation that a Petri-net-derived engine can run embedded, informing a build-vs-adopt decision.]

[FALSIFICATION_CRITERIA: H1: BPMN's business-process constructs (gateways, lanes, pools) cannot naturally express Hermes-specific constructs (dynamic LLM-driven sub-agent spawning, streaming partial results) without extensions costly enough to exceed building bespoke. H2: Hermes routing decisions are frequently open-ended LLM classifications rather than finite, enumerable rules, exceeding DMN's finite-table model. H3: Unfalsifiable as a pure "philosophy validation" claim from repository evidence — must be reframed as a testable version (e.g., serialization/versioning survives Hermes's schema-evolution rate) or deferred.]

Probe: SpiffWorkflow's Script Task and Service Task extension points genuinely accommodate arbitrary Python logic, including dynamic spawning — mitigating H1's concern without eliminating it; extension work stays in-process Python, a low marginal cost relative to building a scheduler from scratch. H2's objection is correct and structural: DMN tables are finite by construction and cannot cover open LLM classification, but remain valid for the genuinely rule-based subset of routing (e.g., static priority-based lane assignment). H3 as originally posed resists falsification by design — the correct epistemic move, per protocol, is to flag the hypothesis as malformed rather than force a verdict; this is itself logged as a process finding.

[EPISTEMIC_DELTA: H1: CONFIRMED (extension points mitigate the gap; low in-process glue cost). H2: FALSIFIED (as primary routing mechanism); CONFIRMED (as secondary mechanism for the rule-based subset only). H3: DEFERRED (hypothesis as stated is unfalsifiable by repository evidence; requires reframing before it can be tested).]

---

### 10. ledger/ledger — Ledger CLI

Plain-text, append-only, double-entry accounting; every transaction must balance; all reports are computed on demand, never stored. https://github.com/ledger/ledger

[HYPOTHESIS_MATRIX: 1. Adopt the double-entry balance invariant as an integrity check for Hermes's resource/budget accounting (every token/compute debit matched by a traceable credit, making drift a hard error). 2. Adopt plain-text-is-the-database as the storage format for Hermes's provenance/audit log, human-readable and tool-agnostic. 3. Adopt the never-store-computed-state principle for Hermes's status/progress reporting, always derived fresh from the immutable event log.]

[FALSIFICATION_CRITERIA: H1: Some Hermes resource consumption (e.g., elapsed wall-clock time) has no natural counter-account to balance against, unlike money or finite token pools. H2: Hermes provenance events include binary/high-volume streaming payloads (full LLM completions, tool outputs) that don't diff or compress sensibly as plain text at long-horizon volumes. H3: Recomputing full status from the entire event log becomes too slow at Hermes's scale (thousands of events per long-horizon task) to serve interactive queries.]

Probe: H1 genuinely fits finite, poolable resources (token budgets, API-call quotas) cleanly, but wall-clock/latency resources have no natural dual entry — the hypothesis is real but must be explicitly scoped, not universal. H2's objection is correct for raw payloads; the standard real-world resolution is a hybrid — plain-text ledger entries holding references to externally-stored blobs — which is a distinct, weaker but implementable claim. H3 reproduces, independently, the identical derive-vs-store scaling tension already surfaced in Temporal's continue-as-new analysis (#8, H3) — a genuine cross-repository convergence worth flagging as a meta-finding: two structurally unrelated systems hit the same wall for the same underlying reason.

[EPISTEMIC_DELTA: H1: CONFIRMED (explicitly scoped to budget/quota-style resources only); FALSIFIED (as a universal resource-accounting claim). H2: FALSIFIED (pure plain-text-everything); CONFIRMED (hybrid: text ledger + external blob references). H3: CONFIRMED (small/medium-scale logs); DEFERRED (large scale, pending a materialized-view strategy — same resolution class as #8, H3).]

---

### 11. trungdong/prov — W3C PROV Python Library

Formal Entity/Activity/Agent provenance graph model with PROV-JSON/PROV-O/PROV-XML serialization. https://github.com/trungdong/prov

[HYPOTHESIS_MATRIX: 1. Adopt the PROV-DM Entity/Activity/Agent triple as the canonical schema for Hermes's provenance layer, with wasDerivedFrom chains giving verifiable lineage for every output. 2. Use PROV-JSON as the interchange format for cross-session handoffs, replacing ad hoc handoff notes with a formally structured, machine-verifiable graph. 3. Combine wasDerivedFrom chains with cryptographic hashing of each Entity for tamper-evident, hash-chained provenance.]

[FALSIFICATION_CRITERIA: H1: Hermes's actual causal structure includes relations PROV-DM doesn't model natively (e.g., "generated despite contradicting evidence" — an epistemic/dialectical relation, not a derivation relation). H2: Session handoff must convey forward-looking intent and open questions in addition to backward-looking provenance, which PROV-DM (models only what occurred) structurally cannot represent. H3: The `prov` library has no built-in cryptographic hashing/signing — if required, it must be built externally and composed with `prov`.]

Probe: PROV-DM is explicitly extensible (the standard supports domain-specific extensions and qualified relations), so H1 survives as a base layer, with a named, real gap: PROV-DM's world is "what happened," while epistemic/dialectical relations (holding contradictions, contested claims) are a genuinely different ontological category not reducible to derivation edges. H2's structural objection is correct — PROV-DM is backward-looking only — so it fails as a complete handoff replacement but survives as the backward-looking half, paired with a separate forward-looking intent document. H3 is verified directly against the library's scope: model + serializers only, no crypto module — so "out of the box" is false, but composing a SHA-256 hash-chain wrapper over canonical PROV-JSON is a small, well-understood, in-language (no new runtime) engineering task.

[EPISTEMIC_DELTA: H1: CONFIRMED (as an extensible base layer; epistemic-relation gap explicitly named as an ontology lock). H2: FALSIFIED (as a complete handoff replacement); CONFIRMED (backward-looking half only, paired with existing handoff-note practice). H3: FALSIFIED (not out-of-the-box); CONFIRMED (composed with an external hash-chain wrapper; low cost, stays in Python).]

---

### 12. aibasel/downward — Fast Downward Planning System

Domain-independent classical STRIPS/PDDL planner using heuristic forward search over grounded planning tasks. https://github.com/aibasel/downward

[HYPOTHESIS_MATRIX: 1. Express Hermes goal states and typed tool actions as PDDL, and use Fast Downward's heuristic search to produce provably goal-achieving action sequences for well-defined tasks, replacing LLM-improvised planning for that subset. 2. Use the grounding phase alone, independent of search, as a static-analysis validator catching schema errors (undeclared predicates, type mismatches) in proposed Hermes action schemas. 3. Adopt heuristic-search-with-admissible-heuristics conceptually (not the tool) as a lightweight in-process ranker for candidate LLM-proposed next steps, without full PDDL formalization.]

[FALSIFICATION_CRITERIA: H1: Hermes tool actions have effects that are discovered at call time rather than crisply enumerable in advance, violating PDDL's closed-world, fully-specified-effects requirement. H2: Grounding failures are reported only as generic translation errors without diagnostics mapping back to the specific malformed schema element. H3: A useful distance-to-goal heuristic requires the same fully-specified action-effect model full PDDL needs — there is no meaningfully lighter-weight version.]

Probe: PDDL's closed-world assumption and the frame problem are foundational, well-documented limitations — the domain cleanly bifurcates into a closed, well-specified tool subset (filesystem operations, deterministic build/deploy steps, typed API contracts) where H1 holds, versus open-ended/discovered-effects tool use where it does not. H2 cannot be resolved from a repository-survey level — it requires actually running the translator and inspecting real error output, which is out of this run's scope; deferring is the epistemically honest move rather than guessing. H3's "no free lunch" reasoning is sound and is itself a core AI-planning-theory result: admissible heuristics are derived from relaxations of the same underlying action model they claim to lighten — so this hypothesis collapses back into H1's scope rather than escaping it, a correctly-identified false lead.

[EPISTEMIC_DELTA: H1: CONFIRMED (closed-world, typed-tool-action subset only, explicitly scoped). H2: DEFERRED (requires empirical inspection of translator diagnostics, out of survey scope). H3: FALSIFIED (collapses into H1; not a genuinely lighter alternative).]

---

### 13. potassco/clingo — Clingo Answer Set Programming Solver

Grounder + solver computing all stable models of a non-monotonic logic program; naturally expresses defaults, exceptions, and combinatorial choice. https://github.com/potassco/clingo

[HYPOTHESIS_MATRIX: 1. Encode Hermes's sub-agent-to-task assignment as an ASP program (capability constraints, load balancing, priority) and use clingo to compute optimal/near-optimal assignments. 2. Use ASP's non-monotonic negation-as-failure as the semantic model for Hermes's defeasible permissions ("agents may access tool X by default, unless explicitly revoked"). 3. Use clingo's enumeration of *all* stable models as a signal that a task specification is genuinely ambiguous/underdetermined and needs Commander clarification, rather than silently picking one answer.]

[FALSIFICATION_CRITERIA: H1: Grounding cost scales with instance size and dominates real-time scheduling latency budgets for large/dense constraint sets. H2: Hermes's permission model needs temporal defeasibility (a permission's history of grants/revocations/reinstatements matters, not just current default/exception state) beyond ASP's atemporal per-solve semantics. H3: The number of valid answer sets for realistic Hermes task specs is either always exactly one (mechanism vacuous) or combinatorially enormous even for well-specified tasks (signal drowned in noise).]

Probe: Grounding, not solving, is well documented as ASP's dominant scalability bottleneck — real-time, fine-grained per-task assignment is falsified, while batch/periodic re-optimization (every N minutes or on major state change) survives. ASP's default-with-exceptions pattern is exactly its designed use case (the canonical "birds fly unless penguin" example), so the atemporal/snapshot permission model is confirmed; the temporal gap I identified is real but addressable via a documented re-grounding-with-timestamped-facts pattern rather than a hard block. H3 cannot be resolved without empirical data on real Hermes task specifications — this is exactly the kind of theoretically elegant claim the Anti-Confirmation Mandate warns against confirming on appeal alone; it survives only as an open, testable question.

[EPISTEMIC_DELTA: H1: CONFIRMED (batch/periodic re-optimization); FALSIFIED (real-time fine-grained assignment). H2: CONFIRMED (atemporal/snapshot model); DEFERRED (temporal/historical variant, solvable via re-grounding pattern, not "ASP alone"). H3: DEFERRED (requires empirical testing against real Hermes task specs).]

---

### 14. taskflow/taskflow — Taskflow

Header-only C++ task-dependency-graph library with static graphs plus dynamic "subflow" tasks that build nested DAGs at runtime; work-stealing scheduler. https://github.com/taskflow/taskflow

[HYPOTHESIS_MATRIX: 1. Adopt Taskflow's static-graph-plus-dynamic-subflow hybrid model directly as Hermes's execution-graph abstraction, matching its need for runtime-discovered branching. 2. Adopt Taskflow's work-stealing scheduler as Hermes's sub-agent dispatch concurrency model, replacing a central-queue dispatcher. 3. Adopt Taskflow's DAG visualization/profiling tooling as inspiration for Hermes's own workflow-debugging observability.]

[FALSIFICATION_CRITERIA: H1: Taskflow's subflow mechanism requires spawning logic to be native, compiled C++ in the same binary — no built-in cross-language task-body definition exists. H2: Hermes tasks are dominated by external I/O wait (LLM/API latency) rather than CPU-bound compute, and work-stealing's benefit is specifically about balancing CPU-bound work across cores. H3: Unfalsifiable-by-repository-evidence "borrow this UX pattern" claim, structurally untestable against source code alone.]

Probe: H1's language-boundary objection is confirmed directly — Taskflow is C++-only with no native cross-language task definition, and embedding it in a Python/TS harness would require a substantial FFI/binding project (e.g., pybind11); the pattern itself (static graph + runtime-discovered dynamic subflow) is real and directly matches Hermes's stated need, so it survives as an architecture to reimplement natively, not a library to embed. H2's objection is textbook concurrency theory and directly applicable: agent harnesses are I/O-latency-dominated, not CPU-compute-dominated, so work-stealing's specific benefit does not transfer — the correct concurrency primitive is async I/O concurrency, which a Python/TS harness almost certainly already uses. H3 is the second instance in this survey (after #9, H3) of a design-inspiration hypothesis that resists falsification by construction — a pattern about hypothesis *quality*, not content, worth naming explicitly in the final report.

[EPISTEMIC_DELTA: H1: FALSIFIED (direct library embedding; cross-language FFI cost); CONFIRMED (pattern transfer — reimplement natively). H2: FALSIFIED (I/O-bound workload mismatch with a CPU-bound-oriented scheduler design). H3: DEFERRED (unfalsifiable design-inspiration claim; same class as #9, H3).]

---

### 15. SWI-Prolog/swipl-devel — SWI-Prolog

Full Prolog implementation: unification, SLD-resolution backtracking, cut, plus CLP(FD)/CLP(Q) constraint libraries, tabling (memoized termination-guaranteed recursion), and a WASM build. https://github.com/SWI-Prolog/swipl-devel

[HYPOTHESIS_MATRIX: 1. Use CLP(FD) as a constraint-solving backend for Hermes resource scheduling, exploiting Prolog's relational bidirectionality (same predicate validates and generates a schedule). 2. Use tabling to guarantee termination for recursive/self-referential Hermes planning queries (e.g., circular delegation chains) without external cycle-detection bookkeeping. 3. Use the WASM build as a sandboxed, dependency-light local reasoning engine for lightweight policy checks without a network call to a larger service.]

[FALSIFICATION_CRITERIA: H1: The scheduling problems Hermes needs solved are pure discrete combinatorics already equally or better covered by clingo (#13), offering no net-new capability over an already-confirmed pathway. H2: LLM-driven delegation chains generate unboundedly many syntactically-distinct subgoals (different phrasings that don't unify), exceeding tabling's guarantee, which covers only a finite set of distinct subgoals. H3: Hermes's runtime environment is already Python/Node-native throughout, and introducing a second logic-programming runtime adds operational surface without a clearly unique capability.]

Probe: H1 is a fair redundancy check flagged explicitly per the Anti-Confirmation Mandate's instruction to prioritize non-obvious surfaces over duplicated dominant paths — CLP(FD) and ASP substantially overlap for finite-domain CSPs, and clingo likely wins on solving/tooling maturity for pure combinatorial search, but Prolog's relational bidirectionality (identical code validates or generates from the same spec) is a genuine, distinct capability clingo's generate-and-test stable-model semantics doesn't offer in the same way — not yet proven necessary, not proven unnecessary. H2's boundary is real: tabling's termination guarantee covers a finite set of distinct subgoals, which holds for structurally-bounded delegation (a fixed, known set of agent roles — a common and plausible Hermes pattern) but not for fully open-ended, LLM-phrased delegation chains. H3's cost-benefit argument is sound and matches this session's own observed tooling ecosystem directly (every visible skill/tool in this environment is Python/Node-based, with zero WASM-Prolog signal anywhere) — technically feasible, practically unjustified given redundant coverage already assessed via CLP(FD)/clingo.

[EPISTEMIC_DELTA: H1: DEFERRED (relational-bidirectionality differentiator is a genuine open question, neither proven necessary nor unnecessary). H2: CONFIRMED (bounded/fixed-role delegation); FALSIFIED (fully open-ended LLM-phrased delegation). H3: FALSIFIED (redundant given clingo/CLP(FD) coverage already assessed; no unique capability justifying a second logic runtime).]

---

## Self-Reflexive Check

- **Is the structure representable in the agent's state space?** For the CONFIRMED set, yes for the design-pattern-transfer hypotheses (TLA+ contracts, PINS separation, Taskflow's static+dynamic-subflow model, mCRL2 protocol specs) since these become native Hermes code, not foreign state. For tool-embedding hypotheses (SpiffWorkflow, Fast Downward, clingo, Alloy, ProM), representability holds only for the explicitly-scoped subsets identified — general-purpose LLM-driven state does not reduce cleanly into any of these formalisms' native state spaces without an abstraction gap, which has been named per hypothesis above (Ontology Lock discipline).
- **Is the tool's input/output stable enough for automation?** Strong yes for clingo, Fast Downward, Alloy (stable file-format APIs, decades of tooling maturity). Weaker for ProM (JVM/XES ecosystem friction, mitigated by pm4py as a lighter alternative) and Taskflow (stable API, but wrong-language boundary for this harness).
- **Does the benefit exceed subprocess, compile, or translation costs?** Confirmed only where cost anchors were explicitly named: Alloy (JVM subprocess, justified by adversarial fuzz-testing value), Temporal (stateful server, justified only for high-value long-horizon tasks), prov (in-language hash-chain wrapper, low cost). Where costs were not clearly justified against benefit (Taskflow direct embedding, SWI-Prolog WASM), hypotheses were falsified on cost-benefit grounds even where technically feasible.
- **Does the abstraction survive runtime environmental change?** This is the axis most hypotheses failed on: LLM non-determinism (Temporal H1, mCRL2 H3's original form), dynamic participant sets (nuscr H1), dynamic task spawning (LTSmin H3, YAWL H3), and open-ended subgoal generation (SWI-Prolog H2) all represent the same underlying failure mode — formalisms built for closed, statically-known worlds meeting an open, LLM-driven one. Every CONFIRMED hypothesis in this run either avoids this failure mode by being a static design-time artifact (contracts, schemas, architecture patterns) or explicitly reframes the boundary (tau-abstraction, pure-function-over-recorded-output) to contain the non-determinism rather than deny it.

---

## [HARNESS_HERMES]

Compiling CONFIRMED hypotheses into functional layers for the Hermes Agent Harness:

**1. Verification & Contract Layer** (design-pattern only, zero/low cost, no new runtime): TLA+-style invariant/action contracts for scheduler design; PINS-style language/algorithm-module separation as Hermes's own internal architecture; mCRL2-style process-algebra notation for documenting coordination protocols pre-implementation.

**2. Coordination & Protocol Layer**: mCRL2 process-algebra specs for concurrency-bounded coordination; nuscr-style deadlock verification scoped to fixed-role multi-agent protocols; weak/tau-bisimulation-based workflow-result caching (equivalence defined over observable I/O, not internal LLM sampling).

**3. Execution Engine Layer**: SpiffWorkflow embedded (or its extension-point pattern reimplemented) as the in-process executor; Taskflow's static-graph-plus-dynamic-subflow model reimplemented natively (no FFI); a YAWL-Worklets-style fallback-strategy library for known failure modes, populated with pre-authored alternatives rather than expected to synthesize novel plans.

**4. Durability & Replay Layer**: Temporal-style deterministic-orchestration-over-recorded-Activity-result pattern — branch-taking as a pure function of an already-recorded LLM/tool output, not a live re-decision — gated by the real infrastructure cost of a stateful orchestration server, reserved for high-value long-horizon tasks.

**5. Provenance & Audit Layer**: PROV-DM-shaped Entity/Activity/Agent schema for the Hermes event log, extended for epistemic/dialectical relations PROV-DM doesn't natively cover; external SHA-256 hash-chain wrapper for tamper evidence; hybrid plain-text ledger with external blob references for large payloads; double-entry balance invariant scoped specifically to finite, poolable resources (token/compute budgets), not general resource accounting.

**6. Planning & Scheduling Layer**: Fast Downward for the closed-world, typed-tool-action subset of task decomposition (deterministic tools with fully-specified effects only); clingo for batch/periodic sub-agent assignment optimization and atemporal defeasible-permission modeling.

**7. Process Intelligence Layer**: ProM-style (or pm4py-based) process discovery run periodically offline against Hermes logs to surface emergent effective strategies; async, batch conformance-drift auditing between declared plans and actual execution traces.

**8. Bounded Recursion Layer**: SWI-Prolog tabling for termination-guaranteed handling of recursive delegation chains, scoped strictly to a fixed, known agent-role vocabulary — not applicable to open-ended LLM-phrased delegation.

**Cross-cutting meta-findings**: (a) Two independent repositories (Temporal, Ledger) converge on the identical derive-vs-store scaling tension for long-horizon logs — this is a single unresolved architectural question, not two. (b) Two independent repositories (SpiffWorkflow, Taskflow) produced unfalsifiable "borrow the UX/design pattern" hypotheses — a recognizable hypothesis-quality failure mode worth avoiding in future PDL runs by requiring behavioral/structural falsification criteria up front. (c) The single dominant abstraction gap across all FALSIFIED hypotheses is formalisms assuming closed, statically-known worlds meeting Hermes's open, LLM-driven one; every surviving CONFIRMED hypothesis either stays at design-time (never touches runtime non-determinism) or explicitly contains it via a named reframing.

## [IMPLEMENTATION_WORKFLOW]

**Phase 0 — Foundational methodology (no new dependencies, immediately actionable):** Adopt TLA+-style invariant/action contract documentation for the scheduler; restructure Hermes's internal codebase along PINS-style language/algorithm separation; adopt process-algebra notation (mCRL2-inspired) for coordination-protocol design docs.

**Phase 1 — Provenance & budget substrate (prerequisite layer):** Implement the PROV-DM-shaped Entity/Activity/Agent event schema; add the external hash-chain wrapper; implement the double-entry budget ledger (hybrid plain-text + blob references) scoped to token/compute accounting.

**Phase 2 — Execution engine:** Prototype SpiffWorkflow embedding against Hermes's real workflow shapes to validate the extension-point mitigation found in this run; reimplement Taskflow's static+dynamic-subflow graph model natively; build the YAWL-Worklets-style fallback-strategy library, seeded with known failure-mode alternatives.

**Phase 3 — Durability (cost-gated):** Prototype the Temporal-style deterministic-orchestration/recorded-Activity-result split for a single high-value long-horizon task type before committing to standing up a full stateful orchestration server; measure whether the infrastructure cost is justified relative to the current retry model.

**Phase 4 — Planning & scheduling:** Integrate Fast Downward for the explicitly closed-world, typed-tool-action subset of task decomposition; integrate clingo for batch sub-agent assignment optimization and atemporal defeasible-permission modeling.

**Phase 5 — Verification, protocol & process intelligence (ongoing, parallel):** Stand up Alloy-driven adversarial fuzz-testing of workflow schemas in CI; add nuscr-style deadlock checking for the fixed-role subset of multi-agent protocols; schedule recurring (weekly/monthly) offline ProM/pm4py log-mining passes; add async conformance-drift auditing.

**Phase 6 — Deferred research queue (not yet actionable, blocks noted explicitly):** Resolve Hermes's role-taxonomy stability question (blocks ProM H3 and constrains SWI-Prolog H2's scope); decide the continue-as-new-plus-external-provenance-store pairing strategy (resolves the Temporal/Ledger convergent scaling tension identified above); empirically test Fast Downward's grounding-error diagnostic quality; empirically test clingo's answer-set-multiplicity-as-ambiguity-signal against real Hermes task specs; resolve whether Prolog's relational bidirectionality (CLP(FD)) earns a place alongside clingo or is fully subsumed by it.

---

*End of PDL trajectory. No hypothesis was synthesized into the workflow above without completing Steps 1–3 of the loop for its source repository.*
