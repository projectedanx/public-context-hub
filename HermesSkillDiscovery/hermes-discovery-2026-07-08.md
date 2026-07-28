# Hermes Agent Harness — Paraconsistent Integration Sensor Run

**Date:** 2026-07-08
**Sensor Mode:** PDL v1.0 — ContextLock(Scope="Integration_Epistemic_Exploration")
**Run Type:** Daily automated repository discovery (scheduled, non-interactive)

> **Operational note (autonomous deviation logged):** The task file specified an output path under session `local_139fdd79-...`. That directory is not writable from this session's sandbox. Per the "make reasonable choices and note them" directive, this file was written to the active session's outputs directory instead. Filename and content conform to spec. No other deviations.

---

## Chosen AI Problem Space: **Process Calculus & Concurrency Theory**

### Rationale — Epistemic Tension Selection

Among the candidate spaces (temporal reasoning, constraint satisfaction, process calculus, formal verification, causal inference, information-theoretic compression, symbolic execution, type theory, program synthesis, planning under uncertainty), **process calculus / concurrency theory** carries the highest epistemic tension against mainstream LLM cognition today, for four structural reasons:

1. **Token-sequential ≠ concurrent.** An LLM generates a single linearized token stream. It has no native representation of *simultaneously interacting processes*, interleaving semantics, or the combinatorial state explosion that concurrency theory was built to tame. This is a genuine blind spot, not a difficulty gradient.
2. **Behavioral equivalence is not lexical similarity.** Bisimulation, weak/strong trace equivalence, and observational congruence define when two processes are *the same* despite different syntax. LLMs default to surface/embedding similarity. Process calculi provide a formal, decidable alternative notion of "same behavior" — directly useful for agent self-consistency checks.
3. **Deadlock / livelock / fairness are emergent, not local.** These properties cannot be read off any single step; they require global reasoning over the reachable state space. An agent that runs long-horizon deterministic workflows needs exactly this: a way to prove its own plan cannot wedge.
4. **Compositional refinement.** Process algebras (CCS, CSP, ACP, π-calculus) let you *build* a large behavior from verified small ones and prove the composite still satisfies a spec. This is the discipline Hermes lacks when it stitches sub-tasks into a DAG.

The isomorphism target: **treat a Hermes agent's plan/tool-loop as a labelled transition system (LTS)**, and borrow the pre-AI machinery for checking that LTS for safety, liveness, equivalence, and deadlock-freedom before execution.

---

## Preflight Matrix — Non-Obvious Linguistic Connections

| Core formal term | Legacy / human-domain term | Implementation term | Repo-signal term | Exclusion term |
|---|---|---|---|---|
| Process algebra (CCS/CSP/ACP) | "chain of command", "protocol", "drill/SOP" | linearisation, LTS export, CLI | toolset, workbench, engine | −LLM −agent |
| Bisimulation / behavioral equivalence | "are these two workflows the same?" | equivalence checker, JSON LTS | checker, library | −copilot −RAG |
| π-calculus (mobile processes) | "handoff", "reassignment", "escalation" | channel passing, name mobility | calculus, workbench | −prompt −embedding |
| Petri nets | "double-entry bookkeeping", "tokens on a board", "kanban" | reachability, marking, PNML | net, editor, simulator | −neural |
| Model checking (LTL/CTL) | "safety inspection", "incident post-mortem" | model checker, counterexample trace | checker, verifier | −transformer |
| Timed / probabilistic automata | "shift scheduling", "actuarial risk" | timed-arc, DTMC/CTMC, PRISM lang | model checker, solver | −inference-engine(ML) |
| Multiparty session types | "contract", "choreography", "RACI" | protocol projection, type checker | scribble, session | −finetune |
| Partial-order reduction | "why re-check equivalent orderings?" | POR, symbolic exploration | LTS toolset | −vector −semantic-search |
| Rewriting / operational semantics | "recipe rewriting", "legal precedent" | reduction rules, `kompile` | framework, semantics | −generative |
| Process mining (α-algorithm) | "forensic accounting", "audit trail" | event log → net discovery | mining library | −chatbot |

---

## The 15 Repositories — Full PDL Loop

Each repo is run through the mandated LOOP: **Hypothesis Generation → Falsification Probe → Epistemic Delta**. Falsification criteria are pre-registered *before* the probe. The `[CB_CONSTRAINT]` biases toward non-obvious integration surfaces; the `[ANTI_CONFIRMATION_MANDATE]` steelmans falsification before any CONFIRM. `[ONTOLOGY_LOCK]` names the human→AI abstraction gap. `[IMPLEMENTATION_COST_ANCHOR]` attaches to any confirmed cross-runtime hypothesis.

---

### 1. mCRL2org/mCRL2 — ACP-family process algebra toolset
**URL:** https://github.com/mCRL2org/mCRL2 · C++ · academic (TU/e + U. Twente), pre-AI lineage (μCRL → mCRL2)

- **[HYPOTHESIS_MATRIX:**
  1. Hermes exports each planned tool-loop as an mCRL2 process spec; `mcrl22lps` + `lps2lts` generate the state space and a μ-calculus formula checks deadlock-freedom before execution.
  2. mCRL2's *multi-actions* primitive is used to model an agent taking several simultaneous tool calls as one atomic step, giving Hermes a formal parallelism model.
  3. mCRL2's bisimulation reducer (`ltsconvert -eweak`) is invoked at runtime to collapse two candidate plans that are behaviorally identical, deduplicating the agent's search frontier.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if a typical Hermes plan does not fit the finite-control fragment mCRL2 can linearise without infinite data blowup. H2: falsified if Hermes tool calls are never actually concurrent (always sequential). H3: falsified if weak-bisimulation runtime exceeds the value of the dedup (i.e., cheaper to just run both plans).**]
- **Falsification Probe:** H1 steelman-for-falsify: mCRL2 requires a static, typed process description; Hermes plans carry unbounded string/JSON data → linearisation can diverge. *But* the guard is that we abstract data to finite action labels (tool-name + status), which mCRL2 handles natively — steelman fails, H1 survives. H2: Hermes today is largely sequential; concurrency is aspirational → steelman holds → H2 **falsified for present harness**. H3: `ltsconvert` on small plan LTSs (<10^4 states) is milliseconds; running a redundant multi-tool plan costs real API calls/seconds → dedup wins → H3 survives. `[ONTOLOGY_LOCK]` gap: "SOP / chain-of-command" (human, prescriptive) → "process term" (formal, generative of all interleavings) — the human artifact names *one* path; the process term denotes *all* paths. `[IMPLEMENTATION_COST_ANCHOR]` H1/H3: subprocess call to compiled mCRL2 binaries; ~50–200ms per invocation, dwarfed by LLM/tool latency → acceptable.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (with finite-action abstraction), H2 FALSIFIED (no true concurrency in current harness), H3 CONFIRMED (behavioral dedup is net-positive).**]

---

### 2. nimble-code/Spin — Promela explicit-state LTL model checker
**URL:** https://github.com/nimble-code/Spin · C · ACM Software System Award 1989; Bell Labs, ~1980 origin — deep pre-AI substrate

- **[HYPOTHESIS_MATRIX:**
  1. Hermes transpiles a multi-agent orchestration into Promela `proctype`s and uses SPIN to prove no reachable global deadlock among agents sharing a resource/channel.
  2. SPIN's LTL claim automata become Hermes' *acceptance test language*: express "the plan eventually reaches goal G and never touches forbidden state F" as an LTL formula, verified before run.
  3. SPIN's guided counterexample trail is fed back to the agent as a concrete failing schedule, turning a verification failure into a repair prompt (a Symbolic Scar).**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if Hermes agents never share synchronizing channels (no deadlock possible → nothing to check). H2: falsified if the goal/forbidden states are not expressible as propositions over agent state. H3: falsified if SPIN trails are not translatable back to agent-legible actions.**]
- **Falsification Probe:** H1 steelman: single-agent Hermes has no rendezvous → true, but multi-tool loops with shared external state (a file, a DB row) *are* channels → survives for the multi-agent/shared-resource case. H2 steelman: agent state is high-dimensional/string-valued; LTL is over atomic props → but we lift to a small set of boolean predicates (goal_met, budget_exceeded, wrote_twice) → survives. H3 steelman: `.trail` files are Promela-level → but there's a 1:1 map from proctype step to agent action by construction → survives. `[ONTOLOGY_LOCK]`: "safety inspection" (human, sampled) → "exhaustive reachability" (formal, total) — humans spot-check, SPIN proves absence. `[IMPLEMENTATION_COST_ANCHOR]` all three: Promela is a *separate compiled runtime* (pan verifier). Cost = one C compile + BFS/DFS over state space; bounded by state-space size, not by the agent — for plans <10^5 states, sub-second. Cheaper than a single failed long-horizon run.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (shared-resource framing), H2 CONFIRMED (predicate lifting), H3 CONFIRMED (counterexample-as-scar).**]

---

### 3. tlaplus/tlaplus — TLA+ / TLC model checker + PlusCal
**URL:** https://github.com/tlaplus/tlaplus · Java · Lamport; pre-AI (TLA 1990s), industrial-grade

- **[HYPOTHESIS_MATRIX:**
  1. Hermes long-horizon workflows are specified in PlusCal; TLC checks an *invariant* ("the ledger never goes negative", "no task runs before its dependency") across all interleavings.
  2. TLA+ *refinement mapping* lets Hermes prove a concrete tool-plan implements an abstract goal spec — giving the agent a formal notion of "this detailed plan is a correct implementation of the intent."
  3. TLC's state-fingerprint + symmetry reduction is repurposed as a *plan-space deduplication oracle* independent of the process-algebra path (cross-check against mCRL2 H3).**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if invariants can't be stated over the agent's data model. H2: falsified if no stable abstraction layer exists between "intent" and "plan". H3: falsified if TLC's Java startup + config overhead exceeds the dedup benefit.**]
- **Falsification Probe:** H1 steelman: infinite data types → TLC needs finite instances → but Hermes tasks are naturally bounded (finite tasks, finite budgets) → survives. H2 steelman-for-falsify: refinement mappings are notoriously hard for humans to author → this is a *real* cost; automating them from LLM intent is unproven → H2 **DEFERRED** pending a refinement-authoring sub-skill. H3 steelman: TLC JVM warmup ~1–2s → non-trivial per-call; only worth it for batch/offline verification, not inner loop → survives *only for offline/batch* use. `[ONTOLOGY_LOCK]`: "contract / spec" (human, natural-language, ambiguous) → "invariant" (formal, machine-checkable, total). `[IMPLEMENTATION_COST_ANCHOR]` H1/H3: JVM subprocess, ~1–2s warmup + model-check time; **use offline / pre-flight only**, not in the hot loop.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (offline invariant checking), H2 DEFERRED (refinement-mapping authoring unsolved), H3 CONFIRMED (batch dedup only).**]

---

### 4. utwente-fmt/ltsmin — language-independent LTS toolset (partial-order + symbolic)
**URL:** https://github.com/utwente-fmt/ltsmin · C · U. Twente; the "PINS" interface is the key asset

- **[HYPOTHESIS_MATRIX:**
  1. LTSmin's **PINS** (Partitioned Interface to the Next-State function) is adopted as Hermes' universal LTS API — the agent implements one `next_state` callback and inherits POR, symbolic, and distributed model checking for free.
  2. Partial-order reduction is used to prune the agent's plan-search: independent tool calls (no shared state) are explored in only one order, cutting the branching factor.
  3. LTSmin's multi-core reachability is used to explore an agent's plan-space in parallel offline, precomputing a verified "safe subgraph" of allowed transitions.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if Hermes cannot express its transition relation as a deterministic next-state function. H2: falsified if agent tool calls are rarely independent (POR gives no reduction). H3: falsified if the safe-subgraph goes stale faster than it can be recomputed.**]
- **Falsification Probe:** H1 steelman: PINS demands a *static* state-vector; agent state is dynamic/growing → but a fixed-width abstraction (phase, budget-bucket, resource-locks) is a valid PINS state → survives. H2 steelman-for-falsify: many agent steps *do* share the same file/context → dependencies are common → **but** read-only tool calls (searches, fetches) are provably independent and dominate many workflows → POR still yields real reduction → survives. H3 steelman: environment drift invalidates precomputed graphs → true for volatile envs → **H3 DEFERRED**, conditioned on `SELF_REFLEXIVE_CHECK` #4 (survives runtime env change?) failing for dynamic targets. `[ONTOLOGY_LOCK]`: "why recheck equivalent orderings?" (human intuition) → "independence relation + Mazurkiewicz trace equivalence" (formal). `[IMPLEMENTATION_COST_ANCHOR]` H1/H2: C library via subprocess or FFI; PINS callback overhead is per-state but amortized by POR's state savings → net reduction.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (fixed-width abstraction), H2 CONFIRMED (read-only independence), H3 DEFERRED (staleness under env drift).**]

---

### 5. fpom/snakes — SNAKES: Net Algebra Kit for Editors and Simulators (Python)
**URL:** https://github.com/fpom/snakes · Python · high-level Petri nets with *arbitrary Python tokens*

- **[HYPOTHESIS_MATRIX:**
  1. Because SNAKES tokens can be *arbitrary Python objects*, Hermes uses a coloured Petri net as its live execution engine — task artifacts are tokens, tool calls are transitions with Python guards, and the marking *is* the agent's world-state.
  2. SNAKES' net-*algebra* control-flow operators (sequence, choice, iteration, parallel) become Hermes' plan-composition primitives — the agent builds workflows by algebraic combination of verified net fragments.
  3. SNAKES' plugin system is used to attach a "provenance" plugin so every transition firing writes an L9.1-style cryptographic trace token.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if in-process Python net execution can't coexist with the agent's own control loop. H2: falsified if the algebraic operators don't cover the control-flow patterns Hermes actually uses. H3: falsified if the plugin hook points don't expose firing events.**]
- **Falsification Probe:** H1 steelman: same-process = shared GIL / state coupling risk → but this is an *advantage*: no subprocess/translation boundary, native Python objects flow directly → **strongest low-cost integration of the set** → survives. H2 steelman: SNAKES covers seq/choice/loop/parallel — exactly the DAG + retry patterns Hermes uses → survives. H3 steelman: plugins wrap `Transition.fire` → firing events are exposed → survives. `[ONTOLOGY_LOCK]`: "tokens on a kanban board" (human, static count) → "coloured marking" (formal, typed, guarded). `[IMPLEMENTATION_COST_ANCHOR]`: **none of cross-runtime kind** — pure in-process Python `pip install`. This is the cheapest confirmed engine candidate; no subprocess, no compile, no translation.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (in-process engine), H2 CONFIRMED (algebra covers Hermes patterns), H3 CONFIRMED (provenance plugin).**]

---

### 6. TAPAAL/TAPAAL — Timed-Arc Petri Net verification
**URL:** https://github.com/TAPAAL/TAPAAL · C++/Java · Aalborg; real-time modelling

- **[HYPOTHESIS_MATRIX:**
  1. Hermes models tool-call timeouts and deadlines as timed-arc intervals; TAPAAL verifies the workflow can meet an SLA ("goal reached within T") across all timings.
  2. Age-invariants model "stale data" — a token (fetched result) older than its TTL becomes unusable, forcing the agent to re-fetch; TAPAAL proves no plan relies on expired data.
  3. TAPAAL's urgent transitions model non-interruptible critical sections in the agent (e.g., a two-step commit that must not be preempted).**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if tool latencies aren't boundable enough to assign intervals. H2: falsified if data-staleness isn't a real failure mode for Hermes. H3: falsified if the agent has no true atomic critical sections.**]
- **Falsification Probe:** H1 steelman-for-falsify: network/LLM latencies are heavy-tailed, not neat intervals → but worst-case bounds (timeouts) *are* the interval upper edge, which is exactly what SLA checking needs → survives. H2 steelman: staleness is a genuine and under-modeled Hermes failure (agent acts on old fetch) → age-invariants formalize it precisely → survives, high value. H3 steelman-for-falsify: does Hermes have real non-interruptible sections today? Rarely → **H3 DEFERRED** until multi-agent preemption exists. `[ONTOLOGY_LOCK]`: "shift scheduling / expiry date" (human) → "token age + interval-guarded arc" (formal, continuous-time). `[IMPLEMENTATION_COST_ANCHOR]` H1/H2: compiled engine (`verifytapn`) via subprocess; timed-automata verification is costlier than untimed but bounded for small nets — offline pre-flight scope.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (SLA checking), H2 CONFIRMED (staleness invariants — high value), H3 DEFERRED (no atomic sections yet).**]

---

### 7. prismmodelchecker/prism — probabilistic model checker
**URL:** https://github.com/prismmodelchecker/prism · Java/C++ · DTMC/CTMC/MDP; PCTL

- **[HYPOTHESIS_MATRIX:**
  1. Hermes models tool reliability as a DTMC (each tool succeeds with prob p); PRISM computes "P(reach goal) ≥ 0.95" and selects the plan maximizing success probability.
  2. MDP support lets Hermes treat *its own choices* as controllable and the *environment* as probabilistic, synthesizing an optimal policy (the plan) via PRISM's strategy export.
  3. Reward structures quantify expected cost (tokens/API $) so PRISM returns the *cheapest* plan meeting a reliability threshold.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if per-tool success probabilities can't be estimated. H2: falsified if the MDP state space is too large to solve within pre-flight budget. H3: falsified if reward = cost mapping is unstable.**]
- **Falsification Probe:** H1 steelman: probabilities are unknown a priori → but Hermes accumulates run history → empirical success rates are estimable (and updatable) → survives. H2 steelman-for-falsify: MDP policy synthesis is exponential in worst case → but agent plan-MDPs are small (tens of tools) → survives for realistic sizes. H3 steelman: token costs are directly measurable → stable reward → survives. `[ONTOLOGY_LOCK]`: "actuarial risk / betting odds" (human, aggregate) → "PCTL probabilistic reachability + optimal MDP policy" (formal, per-state). `[IMPLEMENTATION_COST_ANCHOR]` all: JVM/C++ subprocess; solve time bounded by MDP size — offline planning scope. Cross-runtime cost justified because it replaces trial-and-error API spend with a computed optimal policy.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (history-estimated probs), H2 CONFIRMED (small plan-MDPs), H3 CONFIRMED (measured cost rewards).**]

---

### 8. moves-rwth/storm — Storm probabilistic model checker
**URL:** https://github.com/moves-rwth/storm · C++ · RWTH Aachen; PRISM-compatible, faster engines, Python bindings (`stormpy`)

- **[HYPOTHESIS_MATRIX:**
  1. `stormpy` gives Hermes *in-process Python* probabilistic model checking — no subprocess boundary, unlike raw PRISM — for the same DTMC/MDP plan-selection use case.
  2. Storm's parametric model checking synthesizes the *reliability-as-a-function-of-p* symbolically, so Hermes learns "if tool X's success rate drops below 0.8, switch plans" as a closed-form threshold.
  3. Storm's counterexample generation returns the minimal set of failing tool-paths, feeding a targeted repair (Symbolic Scar).**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if `stormpy` bindings don't expose the needed model-building API from Python. H2: falsified if parametric analysis doesn't scale to Hermes plan sizes. H3: falsified if counterexamples aren't minimal enough to be actionable.**]
- **Falsification Probe:** H1 steelman: bindings may lag the C++ core → but `stormpy` exposes model building + checking, sufficient for DTMC/MDP plans → survives, and the **in-process** property makes Storm strictly preferable to PRISM for the hot-ish path. H2 steelman-for-falsify: parametric MC is heavier than plain → true → **H2 DEFERRED** to offline threshold-precompute. H3 steelman: Storm's high-level counterexamples are path-sets → actionable → survives. `[ONTOLOGY_LOCK]`: same as PRISM, plus "sensitivity analysis" (human, numeric) → "parametric reachability function" (formal, symbolic). `[IMPLEMENTATION_COST_ANCHOR]` H1/H3: `stormpy` is in-process Python — **near-zero translation cost**, the decisive advantage over #7 for embedded use.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (in-process via stormpy), H2 DEFERRED (parametric heavy, offline only), H3 CONFIRMED (minimal path-set counterexamples).**]

---

### 9. CAAL/CAAL — Concurrency Workbench, Aalborg Edition (CCS + bisimulation)
**URL:** https://github.com/CAAL/CAAL · TypeScript · teaches CCS; strong/weak bisimulation + trace equivalence + HML model checking, in-browser

- **[HYPOTHESIS_MATRIX:**
  1. CAAL's bisimulation engine (TypeScript, no native deps) is embedded to answer "are these two agent plans behaviorally equivalent?" for frontier deduplication in the *same runtime* as a TS/JS harness.
  2. CAAL's HML (Hennessy-Milner Logic) checker gives Hermes a lightweight, dependency-free property language ("after action a, action b is possible") for quick plan sanity checks.
  3. CAAL's *distinguishing formula* output — when two processes are NOT bisimilar it returns the HML formula that separates them — is used to explain to the agent *why* two plans differ, not just that they do.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if CAAL's engine can't be decoupled from its UI. H2: falsified if HML is too weak for the properties Hermes needs. H3: falsified if distinguishing formulas aren't human/agent-legible.**]
- **Falsification Probe:** H1 steelman-for-falsify: CAAL is built as a teaching web app, engine tangled with UI → real extraction effort, but the equivalence/bisimulation modules are separable TS classes → survives with moderate refactor. H2 steelman: HML lacks fixed-points (weaker than μ-calculus) → true, but for *local* "next-action-possible" checks it's exactly right and cheap → survives for that scope. H3 steelman: distinguishing formulas are short HML terms → directly renderable as "plan A can do X here, plan B cannot" → survives, high explanatory value. `[ONTOLOGY_LOCK]`: "are these two SOPs the same?" (human, informal) → "bisimulation equivalence + distinguishing formula" (formal, decidable, with a certificate of *difference*). `[IMPLEMENTATION_COST_ANCHOR]` all: pure TS/JS, **in-process for a Node harness** — near-zero cross-runtime cost; the distinguishing-formula certificate is a unique asset not offered by the heavyweight checkers.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (engine separable), H2 CONFIRMED (HML for local checks), H3 CONFIRMED (distinguishing-formula explanations — unique value).**]

---

### 10. scribble/scribble-java — Scribble multiparty session types
**URL:** https://github.com/scribble/scribble-java · Java · global protocol → per-role projection + FSM monitor generation

- **[HYPOTHESIS_MATRIX:**
  1. A multi-agent Hermes choreography is written as a Scribble global protocol; projection generates a per-agent local protocol (FSM) that each agent must obey — enforcing conversation correctness by construction.
  2. Scribble's generated *runtime monitors* wrap each agent so any off-protocol message (a hallucinated / out-of-turn tool call) is caught at the boundary, not downstream.
  3. Well-formedness checking of the global protocol proves *no deadlock and no orphan message* among agents before any of them runs.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if inter-agent interaction isn't shaped like message-passing protocols. H2: falsified if monitor generation targets only Java and can't wrap a Python/JS agent. H3: falsified if real Hermes choreographies violate Scribble's projectability conditions.**]
- **Falsification Probe:** H1 steelman: agents may interact via shared blackboard, not messages → but tool calls / handoffs *are* messages → survives for the messaging subset. H2 steelman-for-falsify: scribble-java emits Java APIs/monitors → language-locked → **but** the *FSM* it generates is language-neutral and can drive a Python/JS runtime monitor → H2 survives as "use the FSM, not the Java codegen." H3 steelman: projectability requires unique-choice / no-races → some agent patterns break this → **H3 DEFERRED** to a well-formedness pre-check that rejects non-projectable choreographies. `[ONTOLOGY_LOCK]`: "RACI chart / contract / choreography" (human, advisory) → "projected local session type + monitor" (formal, enforced, deadlock-free-by-construction). `[IMPLEMENTATION_COST_ANCHOR]` H1/H2: use Scribble offline to *generate FSMs*; run the FSM in-process in any language → translation cost paid once, offline.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (messaging subset), H2 CONFIRMED (FSM is language-neutral), H3 DEFERRED (projectability pre-check needed).**]

---

### 11. runtimeverification/k — K Framework (rewriting-based operational semantics)
**URL:** https://github.com/runtimeverification/k · Java/Scala/LLVM · define a language's semantics; get interpreter + model checker + prover for free

- **[HYPOTHESIS_MATRIX:**
  1. Hermes defines the *semantics of its own plan language* in K; it then gets, for free, a deterministic reference interpreter that can dry-run any plan symbolically before execution.
  2. K's reachability logic prover verifies "from any state satisfying pre P, all executions reach post Q" — a Hoare-style guarantee over agent workflows without hand-writing a checker.
  3. K's `krun --search` explores all nondeterministic reductions of a plan, enumerating every possible execution the agent could take (interleaving coverage).**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if writing K semantics for the plan language costs more than the reference interpreter is worth. H2: falsified if agent pre/post conditions aren't expressible in K's matching logic. H3: falsified if `--search` state explosion is unbounded for real plans.**]
- **Falsification Probe:** H1 steelman-for-falsify: authoring formal semantics is a heavy one-time investment → real, but Hermes has *one* plan language, so the cost is amortized across all future plans → survives as a strategic (not tactical) investment. H2 steelman: matching logic subsumes FOL + reachability → pre/post conditions fit → survives. H3 steelman-for-falsify: `--search` is full state exploration → can explode → **H3 DEFERRED**, gated behind bounded-depth search. `[ONTOLOGY_LOCK]`: "recipe / precedent rewriting" (human, informal reduction) → "rewrite rules over matching-logic configurations" (formal, executable, provable). `[IMPLEMENTATION_COST_ANCHOR]` H1/H2: `kompile` is a heavy build (LLVM/Java), strictly **offline / build-time**; the *output* interpreter runs fast. Justified only if the plan language is stable enough to formalize once.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (strategic, amortized), H2 CONFIRMED (matching logic), H3 DEFERRED (bounded search only).**]

---

### 12. process-intelligence-solutions/pm4py — PM4Py process mining (Python)
**URL:** https://github.com/process-intelligence-solutions/pm4py · Python · α-miner / inductive miner; event-log → Petri net discovery + conformance

- **[HYPOTHESIS_MATRIX:**
  1. Hermes' own execution logs are treated as an event log; the α/inductive miner *discovers* the Petri net the agent has been *implicitly* following — surfacing its emergent workflow as a formal model (self-reflection / L11).
  2. Conformance checking (token-replay / alignments) compares a *new* run against the discovered "known-good" net, flagging deviations as anomalies in real time.
  3. The discovered net is fed forward as a *prior* plan skeleton for similar future tasks, closing a learn→formalize→reuse loop.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if agent logs lack the case/activity/timestamp structure mining needs. H2: falsified if conformance scoring is too noisy to separate anomaly from legitimate variation. H3: falsified if discovered nets don't generalize to new-but-similar tasks.**]
- **Falsification Probe:** H1 steelman: logs may be unstructured text → but Hermes controls its own logging → emitting (case_id, tool_name, timestamp) triples is trivial → survives. H2 steelman-for-falsify: LLM agents are highly variable run-to-run → high fitness variance → conformance may cry wolf → **but** alignment-based conformance gives graded deviation cost, tunable by threshold → survives with calibration. H3 steelman-for-falsify: over-fit nets don't transfer → real risk → **H3 DEFERRED** pending generalization eval across task clusters. `[ONTOLOGY_LOCK]`: "forensic accounting / audit trail" (human, retrospective) → "discovered Petri net + conformance alignment" (formal, generative model of behavior). `[IMPLEMENTATION_COST_ANCHOR]` H1/H2: pure in-process Python `pip install pm4py` — **no cross-runtime cost**; mining is offline/batch over accumulated logs.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (self-model discovery), H2 CONFIRMED (calibrated conformance), H3 DEFERRED (transfer unproven).**]

---

### 13. bupaverse/bupaR — process mining in R
**URL:** https://github.com/bupaverse/bupaR · R · tidy-data event-log analysis; performance & rework metrics

- **[HYPOTHESIS_MATRIX:**
  1. bupaR's *performance analysis* (throughput time, idle time, rework rate) is applied to Hermes logs to quantify where the agent wastes loops — a metrics layer the pure model checkers don't provide.
  2. bupaR's *rework / self-loop detection* surfaces exactly the pathological "agent retries the same failing tool" pattern, giving a concrete signal for loop-breaking.
  3. bupaR's trace-clustering groups similar agent runs into behavioral archetypes, a taxonomy Hermes can use to route new tasks to a known strategy.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if R interop cost outweighs metrics value vs doing it in Python. H2: falsified if rework detection can't distinguish productive retry from pathological loop. H3: falsified if clusters aren't stable/meaningful.**]
- **Falsification Probe:** H1 steelman-for-falsify: R is a *separate runtime* from a Python/JS harness → real interop tax (Rscript subprocess or reticulate) → **but** PM4Py (#12) already covers most metrics in-process → **H1 FALSIFIED for embedded use**: bupaR is redundant with pm4py at higher runtime cost. H2 steelman: rework detection is real and valuable → survives *conceptually*, but the capability is available in pm4py too. H3 steelman: clustering stability is data-dependent → DEFERRED. **Anti-confirmation outcome:** the honest read is that bupaR's *concepts* are confirmed-valuable but its *R runtime* is falsified as an integration surface given the Python-native alternative. `[ONTOLOGY_LOCK]`: "rework / churn" (human, managerial) → "self-loop frequency in discovered net" (formal). `[IMPLEMENTATION_COST_ANCHOR]` H1: R subprocess/reticulate bridge — **higher cost than the isomorphic pm4py path** → this is the decisive falsifier.
- **[EPISTEMIC_DELTA:** H1 FALSIFIED (redundant with pm4py at higher runtime cost), H2 CONFIRMED-as-concept (implement via pm4py, not bupaR), H3 DEFERRED (cluster stability). *Repo retained as conceptual reference, not integration target.***]

---

### 14. diffblue/cbmc — C Bounded Model Checker
**URL:** https://github.com/diffblue/cbmc · C++ · SAT/SMT bounded model checking; assertions, concurrency (POSIX threads)

- **[HYPOTHESIS_MATRIX:**
  1. When Hermes *generates code* as a tool output, CBMC bounded-model-checks that code for the classic errors (buffer overflow, null deref, assertion violation) before the agent runs or ships it.
  2. CBMC's concurrency support checks agent-generated *multithreaded* code for data races — a property LLMs are notoriously bad at getting right.
  3. CBMC's counterexample (a concrete failing input) is fed back as a failing unit test, turning verification into test generation.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if Hermes doesn't generate C/C++ (CBMC's target languages). H2: falsified if generated concurrent code is rare. H3: falsified if BMC's bounded (not complete) nature misses the errors that matter.**]
- **Falsification Probe:** H1 steelman-for-falsify: CBMC targets C/C++ (+ Java via JBMC) → most agent-generated code is Python/JS → **narrow applicability** → but for the systems/embedded slice it's decisive; and JBMC extends to Java → **H1 CONFIRMED for C/C++/Java outputs only** (scoped). H2 steelman: agent-written concurrent code is uncommon but exactly where it fails silently → high-value-when-applicable → survives, scoped. H3 steelman-for-falsify: bounded depth misses deep bugs → true limitation → but bounded checking catches the *shallow, common* errors cheaply → survives with the "shallow-bug" scope named. `[ONTOLOGY_LOCK]`: "code inspection" (human, heuristic) → "SAT-encoded bounded reachability of an assertion violation" (formal, exhaustive to depth k). `[IMPLEMENTATION_COST_ANCHOR]` all: compiled subprocess; SAT/SMT solve time can spike but is bounded by the unwind depth k → **cap k for predictable cost**. Cheaper than shipping a broken artifact.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (scoped to C/C++/Java outputs), H2 CONFIRMED (scoped to concurrent code), H3 CONFIRMED (scoped to shallow/common bugs, capped k).**]

---

### 15. sarahtattersall/PIPE — Platform Independent Petri Net Editor
**URL:** https://github.com/sarahtattersall/PIPE · Java · GSPN modelling, reachability/coverability, steady-state & performance analysis; PNML I/O

- **[HYPOTHESIS_MATRIX:**
  1. PIPE's **PNML** import/export makes it Hermes' *interchange format* — one canonical serialized net that flows between SNAKES (#5), TAPAAL (#6), pm4py (#12) and PIPE, decoupling engine choice from model.
  2. PIPE's Generalised Stochastic Petri Net (GSPN) steady-state analysis estimates the *long-run* fraction of time the agent spends in each phase — a capacity/throughput planning tool.
  3. PIPE's reachability/coverability graph generation gives a dependency-free way to prove a marking (goal state) is reachable and that no "bad" unbounded marking (runaway loop) exists.**]
- **[FALSIFICATION_CRITERIA:** H1: falsified if the isomorphic tools don't actually share PNML dialect compatibility. H2: falsified if steady-state assumptions (exponential rates) don't fit agent timing. H3: falsified if coverability analysis doesn't scale to Hermes net sizes.**]
- **Falsification Probe:** H1 steelman-for-falsify: PNML has dialect drift (core vs symmetric vs coloured) → real interop friction → **but** the P/T-net core dialect is broadly supported across SNAKES/TAPAAL/pm4py → **H1 CONFIRMED for the P/T core**, DEFERRED for coloured extensions. H2 steelman-for-falsify: GSPN assumes exponential firing → agent timings are not exponential → steady-state numbers would be *approximate* → **H2 FALSIFIED** as a quantitative claim (keep only as rough capacity heuristic). H3 steelman: coverability (Karp-Miller) can blow up → but bounded for small plan nets → survives with size cap. `[ONTOLOGY_LOCK]`: "board with tokens / queueing station" (human) → "GSPN with reachability + coverability graph" (formal; coverability decides *boundedness* = runaway-loop-freedom). `[IMPLEMENTATION_COST_ANCHOR]` H1: PNML is a static XML file — **zero runtime cost as an interchange format**; that is PIPE's most defensible role. H3: Java subprocess for analysis, offline.
- **[EPISTEMIC_DELTA:** H1 CONFIRMED (PNML as P/T-core interchange), H2 FALSIFIED (GSPN steady-state assumptions don't fit), H3 CONFIRMED (coverability for boundedness, size-capped).**]

---

## Self-Reflexive Check (across all confirmed hypotheses)

1. **Representable in agent state space?** Yes — every confirmed integration abstracts agent state to a *finite action/marking/predicate* vocabulary (tool-name + status + resource-locks + budget-bucket). This abstraction is the load-bearing move; it is what makes the pre-AI machinery applicable at all.
2. **I/O stable enough for automation?** Yes for file/subprocess-boundary tools (mCRL2, SPIN, TLC, TAPAAL, PRISM, Storm, K, CBMC, PIPE) and *strongly yes* for in-process tools (SNAKES, CAAL, pm4py) which carry no serialization contract to break.
3. **Benefit > subprocess/compile/translation cost?** Split: **in-process** (SNAKES, pm4py, CAAL, stormpy) = decisively yes; **offline/pre-flight** (mCRL2, SPIN, TLC, TAPAAL, PRISM, K, CBMC, PIPE) = yes because they replace *failed real runs* (API $, wall-clock) with *cheap static checks*; **rejected** (bupaR) = no, redundant at higher runtime cost.
4. **Survives runtime environmental change?** The static/pre-flight checks survive by re-running per plan. The *precomputed* artifacts (LTSmin safe-subgraph H3, pm4py transfer H3) are the ones flagged DEFERRED precisely because they can go stale — correctly caught by this check.

---

## [HARNESS_HERMES]

Only CONFIRMED (or scoped-CONFIRMED) hypotheses proceed. The confirmed capability set clusters into **three integration tiers**, ordered by cost:

**Tier A — In-process Python/JS engines (zero cross-runtime cost, embed now):**
- **SNAKES (#5)** → the *live execution substrate*: coloured Petri net where markings = world-state, transitions = guarded tool calls, plus a provenance plugin (L9.1). This is the spine.
- **pm4py (#12)** → *self-model discovery + conformance*: mine the net Hermes implicitly follows from its own logs; flag deviating runs (L11 self-reflection, L8 integrity).
- **CAAL (#9)** → *behavioral equivalence + distinguishing formulas*: dedup plans and, when they differ, get a certificate of *why* (L7.5 dialectical explanation).
- **stormpy (#8)** → *in-process probabilistic plan selection*: pick the plan maximizing P(goal) under measured tool reliabilities.

**Tier B — Offline pre-flight verifiers (subprocess, run before execution, replace failed real runs):**
- **SPIN (#2)** → deadlock + LTL safety/liveness over multi-agent/shared-resource plans; counterexample trails become Symbolic Scars (L3.8).
- **mCRL2 (#1)** → μ-calculus deadlock-freedom + weak-bisimulation dedup cross-check.
- **TAPAAL (#6)** → SLA/deadline verification + **data-staleness (age-invariant)** checking (high-value, under-modeled failure mode).
- **PRISM/Storm (#7/#8)** → MDP optimal-policy synthesis with cost rewards for cheapest reliable plan.
- **CBMC (#14)** → bounded model checking of agent-*generated* C/C++/Java code (scoped: shallow bugs, capped unwind depth k).

**Tier C — Strategic / interchange (one-time investment, structural):**
- **K Framework (#11)** → formalize the Hermes plan language *once*; inherit a reference interpreter + reachability prover (amortized, build-time).
- **Scribble (#10)** → generate language-neutral FSM monitors from a global choreography for multi-agent protocol conformance (offline codegen, in-process enforcement).
- **PNML via PIPE (#15)** → canonical P/T-net interchange format decoupling model from engine (zero-cost static artifact).
- **LTSmin/PINS (#4)** → universal next-state interface + partial-order reduction (adopt when plan-search branching becomes the bottleneck).

**Explicitly excluded / deferred:**
- **bupaR (#13)** — FALSIFIED as integration target (redundant with pm4py at R-runtime cost); retained as conceptual reference only.
- DEFERRED items requiring new sub-skills or evals before promotion: TLA+ refinement-mapping authoring (#3-H2), LTSmin safe-subgraph staleness (#4-H3), K bounded-search (#11-H3), pm4py transfer generalization (#12-H3), Scribble projectability pre-check (#10-H3).

---

## [IMPLEMENTATION_WORKFLOW]

**Phase 0 — Abstraction contract (prerequisite for everything).**
Define the finite Hermes state-vector: `(phase, tool_name, tool_status, resource_locks, budget_bucket, goal_predicates)`. This is the single interface every confirmed tool consumes. Ship this before any engine integration.

**Phase 1 — In-process spine (Tier A, weeks 1–3).**
1. Adopt **SNAKES** as the execution engine; represent the current plan as a coloured net; add the provenance plugin.
2. Wire **pm4py** to emit `(case_id, activity, timestamp)` from every firing and run offline discovery + conformance nightly (this is the natural home for this scheduled sensor's downstream loop).
3. Add **CAAL**-based plan-equivalence dedup with distinguishing-formula reporting on the search frontier.
4. Add **stormpy** plan-ranking once ≥N historical runs exist to estimate per-tool reliabilities.

**Phase 2 — Pre-flight verification gate (Tier B, weeks 3–6).**
5. Insert a pre-execution gate: serialize the plan → **SPIN** (deadlock + LTL) and **mCRL2** (bisim dedup) for multi-agent/shared-resource plans; block execution on counterexample, log the counterexample as a Symbolic Scar.
6. Add **TAPAAL** age-invariant staleness checks for any plan that reuses fetched data across steps (highest-value single check identified this run).
7. Add **PRISM/Storm** MDP policy synthesis for plans above a cost/reliability threshold.
8. Add **CBMC** as a code-output verifier, scoped to C/C++/Java, capped unwind depth.

**Phase 3 — Structural investments (Tier C, quarter horizon).**
9. Standardize on **PNML (PIPE core dialect)** as the net interchange format across Tiers A/B.
10. Formalize the plan language in **K** to obtain a reference interpreter + reachability prover.
11. Introduce **Scribble** FSM monitors when multi-agent choreographies stabilize; add the projectability pre-check.
12. Adopt **LTSmin/PINS + POR** if/when plan-search branching becomes the dominant cost.

**Sequencing invariant:** in-process before subprocess; pre-flight before execution; offline learning before online enforcement. No Tier-C investment begins until the Phase-0 abstraction contract has proven stable across ≥2 phases.

---

*End of PDL v1.0 run. Epistemic trajectory (hypothesis matrices → falsification probes → deltas) is the primary deliverable; the implementation workflow is derived strictly from CONFIRMED hypotheses.*
