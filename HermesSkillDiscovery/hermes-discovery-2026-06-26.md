# Hermes Agent Harness — Repository Discovery Report
**Date:** 2026-06-26  
**Sensor Mode:** Paraconsistent Integration Sensor  
**PDL Version:** 1.0  
**Run Type:** Automated Daily Research — Autonomous Execution

---

## Chosen AI Problem Space: Causal Inference & Temporal Constraint Reasoning

**Rationale for Selection:**

This space carries the highest epistemic tension with mainstream LLM approaches available in 2026. The tension is structural, not superficial:

- LLMs are **purely correlational engines**. They cannot compute interventional distributions P(Y | do(X)) — the foundational operation of Pearl's do-calculus. They approximate causal claims through pattern correlation, not interventional structure.
- LLMs have **no native temporal interval semantics**. Allen's 13 interval relations (before, meets, overlaps, during, starts, finishes, equals, and their inverses) require qualitative constraint propagation — not token prediction.
- LLMs cannot perform **identifiability analysis** — determining whether a causal effect is computable from observational data given a causal graph structure. This is a formal graph-theoretic operation.
- LLMs cannot run **conformance checking** — verifying whether an observed execution trace satisfies a formal process model. This requires alignment between event log sequences and Petri nets or BPMN.
- LLMs have no **belief state propagation** under partial observability — the POMDP formalism is computationally intractable to simulate in token space.

Every capability targeted in this run is **genuinely alien to the base LLM substrate**. Integrating these repositories into Hermes gives the agent calculative powers that cannot be approximated through prompt engineering alone. The surprisal density of this zone is maximal.

---

## Preflight Matrix

| Concept Axis | Core Formal Term | Legacy/Human-Domain Term | Implementation Term | Repo-Signal Term | Exclusion Term |
|---|---|---|---|---|---|
| Causal Structure | Structural Causal Model (SCM) | Root cause analysis, attribution | DAG, d-separation, backdoor | causality, causal, graph | LLM, RAG, copilot |
| Interventional Reasoning | do-calculus, identifiability | What-if analysis, counterfactual | Pearl ID algorithm, interventional distribution | doWhy, intervene | agent, GPT |
| Graph Discovery | Causal discovery, PC algorithm | "Finding what causes what" | Skeleton, CPDAG, Markov equivalence | learn, discover, structure | neural, transformer |
| Temporal Structure | Allen interval algebra, LTL | Timeline, scheduling, chronicle | Constraint propagation, CSP, SAT | temporal, interval, logic | chatbot |
| Partial Observability | POMDP, belief state | "Acting in fog", uncertain sensing | Monte Carlo Tree Search, particle filter | pomdp, belief, planning | assistant |
| Process Conformance | Conformance checking, Petri net | Audit trail, workflow compliance | Alpha miner, token replay, fitness | mining, conformance, event log | model, prompt |
| Information-Theoretic | Transfer entropy, mutual information | Signal dependency, coupling | KSG estimator, k-NN, kernel | entropy, information, mutual | embedding |
| SMT Solving | Satisfiability modulo theories | Constraint scheduling, verification | Z3, bitvector, quantifier elimination | solver, theorem, prover | completion |
| Bayesian Structure | Markov blanket, d-separation | "What variables matter?" | BIC score, hill climbing, exact inference | pgm, network, belief | fine-tuning |
| Graph Rewriting | Sesqui-pushout, DPO rewriting | System evolution, state morphism | Pushout, category theory, rule application | rewriting, morphism, graph | generation |

---

## Repository Analysis — Full PDL Loop

---

### Repository 01: `py-why/dowhy`
**URL:** https://github.com/py-why/dowhy  
**Domain:** Causal Inference — Structural Causal Models + do-calculus  
**Language:** Python  
**Summary:** DoWhy is the reference Python library for causal inference, implementing Pearl's unified framework. It supports explicit causal graph modeling, identification using do-calculus, estimation via multiple estimators, and refutation testing of causal assumptions.

---

[HYPOTHESIS_MATRIX:  
1. DoWhy's `identify_effect()` can function as a **causal gate** in Hermes — before any claim of dependency between two agent-produced variables, the gate verifies whether the relationship is identifiable from the available causal graph structure, blocking spurious correlational reasoning.  
2. DoWhy's refutation methods (placebo treatment, random common cause, data subset) can serve as **epistemic immune responses** in Hermes — when the agent produces a causal claim, the refuters automatically probe whether that claim survives counterfactual stress tests.  
3. DoWhy's effect estimation pipeline (matching, IV, regression discontinuity) can act as a **quantitative backbone** for Hermes's attribution layer — assigning numerical causal weights to detected interventions in a workflow log.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if DoWhy's identification algorithm requires a pre-specified DAG and Hermes cannot reliably supply one — without a graph, `identify_effect()` returns None and the gate is inoperable.  
H2: FALSIFIED if refutation tests require a held-out dataset that Hermes does not have access to during runtime (refutations need observational data to run bootstrap resampling).  
H3: FALSIFIED if the estimation methods assume continuous numeric treatment/outcome variables — Hermes operates on structured text/tool outputs that don't map cleanly to regression inputs without feature engineering.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — Graph supply is a real constraint. Hermes would need a parallel causal graph construction module (e.g., from causal-learn). The hypothesis survives if paired with Repo 02.  
H2: CONFIRMED — The refutation interface accepts a pandas DataFrame and Hermes can supply tool-output logs in tabular form. The stress-test protocol is directly implementable as a post-reasoning audit step.  
H3: FALSIFIED — Confirmed steelman fails. Hermes's outputs are rarely numeric time-series without preprocessing. This is a real translation cost.]

[SELF_REFLEXIVE_CHECK:  
- State representability: PASS — Causal graphs are serializable as JSON/networkx.  
- Tool I/O stability: PASS — DoWhy's API is stable; py-why is actively maintained by Amazon, Microsoft contributors.  
- Cost-benefit: PASS — Pure Python, no compile step. Subprocess cost is zero.  
- Runtime survival: PASS — Graph structure is environment-independent.]

---

### Repository 02: `py-why/causal-learn`
**URL:** https://github.com/py-why/causal-learn  
**Domain:** Causal Discovery — PC, FCI, GES, LiNGAM, Granger  
**Language:** Python  
**Summary:** Causal-learn provides implementations of classical and modern causal discovery algorithms. Given observational data, it learns the causal graph structure. This is the upstream complement to DoWhy — Repo 01 identifies and estimates effects; Repo 02 discovers the graph.

---

[HYPOTHESIS_MATRIX:  
1. PC algorithm in causal-learn can function as an **automatic DAG bootstrapper** — given a matrix of agent-produced variables (e.g., tool latencies, output token counts, loop iteration counts), PC discovers the skeleton of causal structure without domain specification.  
2. FCI algorithm can handle **latent confounding** between Hermes modules — when hidden variables exist (e.g., user intent that affects both the query formulation and tool selection), FCI produces a PAG rather than a DAG, preserving epistemic honesty about unobserved common causes.  
3. Granger causality functions can act as a **temporal precedence detector** — in time-series logs of agent actions, Granger tests identify which actions statistically precede and predict which outcomes, building a runtime causal timeline.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if PC's conditional independence tests fail on sample sizes typical of Hermes session logs (PC requires n >> p and performs poorly under n < 200 samples).  
H2: FALSIFIED if FCI's PAG output cannot be consumed downstream by DoWhy for effect identification — the two libraries must share a compatible graph format.  
H3: FALSIFIED if Granger causality detects non-causal temporal correlations (Granger causality is not true causality — a faster clock process will Granger-cause a slower one without structural relationship).]

[EPISTEMIC_DELTA:  
H1: DEFERRED — Session logs are typically short. Fisher Z-test works with n~50 if variables are ~5-10. Hermes could aggregate across sessions for discovery. Viable with batching.  
H2: CONFIRMED — causal-learn exports graphs in networkx/graphviz format. DoWhy accepts networkx DiGraph. Integration path is clear.  
H3: FALSIFIED — Anti-confirmation holds. Granger is a temporal precedence test, not structural causation. Labeling it "causal" would introduce ontological contamination into Hermes's reasoning layer.]

---

### Repository 03: `IntelLabs/causality-lab`
**URL:** https://github.com/IntelLabs/causality-lab  
**Domain:** Causal Discovery Research — FCI, ICD, OrdICD, TS-ICD  
**Language:** Python  
**Summary:** Intel Labs' research-grade causal discovery framework with novel algorithms including ICD (Iterative Causal Discovery) and time-series variants. Provides lower-level graph manipulation primitives than causal-learn.

---

[HYPOTHESIS_MATRIX:  
1. ICD algorithm (Iterative Causal Discovery) can serve as a **progressive refinement loop** in Hermes — rather than requiring all data upfront, ICD iteratively updates the causal skeleton as new observations arrive, matching Hermes's streaming tool-output architecture.  
2. The graph primitives (PAG, MAG, CPDAG classes) can form the **ontological backbone** of a Hermes internal state representation — capturing not just "what happened" but "what could have caused what" in a session.  
3. TS-ICD (time-series ICD) can detect **causal phase transitions** in long-horizon Hermes workflows — identifying when a causal structure shifts (e.g., a dependency changes after a tool failure or context shift).]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if ICD is not incremental in practice — if the algorithm requires restarting from scratch on new data rather than updating an existing skeleton.  
H2: FALSIFIED if Intel's graph classes are not interoperable with networkx or DoWhy's expected format — requiring a translation layer with non-trivial maintenance cost.  
H3: FALSIFIED if TS-ICD requires long time-series (100+ timesteps) to detect structural change, making it impractical for per-session Hermes windows.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — The repo description suggests incremental operation but documentation is research-grade. Requires source inspection to confirm. Potential high value if confirmed.  
H2: DEFERRED — Interop path is plausible but not explicitly documented. A thin adapter class is likely needed.  
H3: FALSIFIED — TS-ICD is designed for multivariate time series with stationary regimes. Single Hermes sessions are too short. Multi-session aggregation required.]

---

### Repository 04: `pgmpy/pgmpy`
**URL:** https://github.com/pgmpy/pgmpy  
**Domain:** Probabilistic Graphical Models — Bayesian Networks, Structure Learning, Exact/Approximate Inference  
**Language:** Python (MIT License, published JMLR 2025)  
**Summary:** pgmpy is the most comprehensive Python toolkit for probabilistic graphical models. Covers Bayesian Networks, Dynamic Bayesian Networks, Structural Equation Models, exact inference (Variable Elimination, Belief Propagation), approximate inference (MCMC, Loopy BP), and structure learning (Hill-Climb, PC, BIC).

---

[HYPOTHESIS_MATRIX:  
1. pgmpy's BayesianNetwork inference engine can serve as a **probabilistic belief tracker** in Hermes — maintaining a probability distribution over hidden state variables (user intent, task phase, tool reliability) and updating it as observations arrive.  
2. pgmpy's structure learning (HillClimbSearch + BIC) can automatically construct **skill-dependency graphs** from historical Hermes execution logs — discovering which upstream skills influence downstream success rates.  
3. pgmpy's CausalInference module (which wraps do-calculus) can provide **intervention simulation** — "If I force tool X to execute (do(X=1)), what is the predicted downstream effect on task completion probability?"]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if exact inference (Variable Elimination) is computationally intractable for networks with > 20 nodes — Hermes's state space may have many variables.  
H2: FALSIFIED if structure learning over Hermes execution logs requires > 1000 sessions to produce a stable graph (Hill-Climb is sample-hungry).  
H3: FALSIFIED if pgmpy's causal inference module is a wrapper of DoWhy — in which case Repos 01 and 04 partially duplicate each other.]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — For online belief tracking, approximate inference (Loopy BP) is tractable for any network size. Hermes can use the approximate engine for real-time operation and exact inference for batch audits.  
H2: DEFERRED — Requires empirical testing with Hermes execution data. Conservative estimate: 200+ sessions needed for stable skeleton, 1000+ for parameters. Viable as an offline learning step.  
H3: CONFIRMED (complementary) — pgmpy's value over DoWhy is its unified parameter estimation + inference pipeline. Use pgmpy for inference+learning, DoWhy for identification+refutation. Non-redundant.]

---

### Repository 05: `pwollstadt/IDTxl`
**URL:** https://github.com/pwollstadt/IDTxl  
**Domain:** Information Dynamics — Transfer Entropy, Multivariate Mutual Information, Network Inference  
**Language:** Python  
**Summary:** Information Dynamics Toolkit XL (IDTxl) is a comprehensive package for inferring directional information flow in multivariate time series using information-theoretic measures. Implements transfer entropy (TE), multivariate TE (MTE), active information storage (AIS), and Granger causality. Used in neuroscience, finance, and complex systems research.

---

[HYPOTHESIS_MATRIX:  
1. Transfer entropy from IDTxl can function as a **directional information flow meter** between Hermes modules — measuring how much information about module A's future state is contained in module B's past state, without assuming any parametric model.  
2. IDTxl's active information storage (AIS) measure can quantify **memory utilization** in Hermes's processing loops — identifying which context variables carry the most predictive information across time steps.  
3. IDTxl's network inference (MultivariateTE) can produce an **empirical information architecture map** of a running Hermes session — a directed graph where edges represent statistically significant information transfer between components.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if TE estimation requires continuous-valued time series of length > 500 — Hermes tool outputs are often categorical/discrete and session length is bounded.  
H2: FALSIFIED if AIS computation is too slow for real-time integration (IDTxl uses kernel estimators with O(n²) complexity).  
H3: FALSIFIED if MultivariateTE produces too many false-positive edges in short series — Hermes sessions may not meet the minimum sample requirements for reliable estimation.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — IDTxl supports discrete estimators (CMI from discrete mutual information). If Hermes outputs are discretized, TE is computable. Requires testing with real session data.  
H2: FALSIFIED — Confirmed steelman. O(n²) kernel estimation is too slow for real-time use in Hermes. Viable only as offline analytics.  
H3: DEFERRED — IDTxl implements surrogate testing to control false positive rates. The Bonferroni-corrected network inferences are more conservative. Needs empirical validation.]

---

### Repository 06: `gregversteeg/NPEET`
**URL:** https://github.com/gregversteeg/NPEET  
**Domain:** Non-parametric Entropy Estimation  
**Language:** Python (NumPy/SciPy only)  
**Summary:** NPEET implements non-parametric k-nearest-neighbor estimators for entropy, mutual information, conditional mutual information, and divergence for both continuous and discrete variables. Implements the Kraskov-Stögbauer-Grassberger (KSG) estimator.

---

[HYPOTHESIS_MATRIX:  
1. NPEET's mutual information estimator can serve as a **dependency probe** between Hermes input features and output quality — measuring information content without assuming linearity or Gaussianity.  
2. NPEET's conditional mutual information (CMI) can implement **causal screening** in Hermes — CMI(X; Y | Z) = 0 iff X⊥Y|Z, which is the d-separation test underlying PC-algorithm. This enables lightweight independence testing without a full causal discovery run.  
3. NPEET's divergence estimators can function as a **distribution shift detector** — measuring KL divergence between historical and current Hermes behavioral distributions to flag when the agent is operating in a novel regime.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if KSG estimator produces high-variance estimates for the small sample sizes typical of Hermes (n < 100 tool calls per session).  
H2: FALSIFIED if CMI tests have unacceptable false-positive rates at small n — making the causal screening gates unreliable.  
H3: FALSIFIED if KL divergence estimation between behavioral distributions requires continuous vector representations that Hermes's tool outputs don't naturally inhabit.]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — KSG with k=5 nearest neighbors is reliable at n~50 for low-dimensional data. Hermes tool call latencies, token counts, and retry rates are ~5-10 dimensional and suitable.  
H2: CONFIRMED — CMI for independence testing works at n~100 with appropriate k. False positive rate is controllable via permutation testing (NPEET includes shuffle-based null distribution). Concrete, deployable path.  
H3: DEFERRED — Requires that Hermes behavioral states be embedded in a continuous feature space. If tool outputs are featurized (timing, length, success bit), the estimator applies.]

---

### Repository 07: `dit/dit`
**URL:** https://github.com/dit/dit  
**Domain:** Information Theory — Multivariate Information Measures, Partial Information Decomposition  
**Language:** Python  
**Summary:** `dit` implements a vast range of multivariate information measures including entropy, mutual information, interaction information, total correlation, dual total correlation, and partial information decomposition (PID). Exact computation over discrete distributions.

---

[HYPOTHESIS_MATRIX:  
1. `dit`'s Partial Information Decomposition (PID) can decompose the information that multiple Hermes modules jointly provide about an outcome — separating **unique, redundant, and synergistic** contributions, enabling precise attribution of which combination of tools is non-redundantly necessary.  
2. `dit`'s total correlation (TC) measure can quantify **coupling tightness** between Hermes sub-agents — high TC indicates modules are over-correlated and a single failure will cascade; low TC indicates excessive independence and missed coordination.  
3. `dit`'s interaction information can detect **higher-order dependencies** in Hermes that pairwise mutual information misses — capturing three-way interactions between modules that create emergent risks or capabilities.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if PID requires exact joint probability distributions that Hermes cannot reliably estimate from finite sessions.  
H2: FALSIFIED if total correlation computation becomes exponentially expensive for more than ~8 variables (dit requires explicit joint distribution enumeration).  
H3: FALSIFIED if interaction information for three-way Hermes dependencies requires n >> 10^4 samples to estimate reliably.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — PID is theoretically powerful but requires reliable probability estimates. With Hermes session aggregation (1000+ runs), this becomes viable. As offline analytics: CONFIRMED.  
H2: FALSIFIED — dit's exact computation is exponential in the number of variables. For > 8 Hermes modules, TC is computationally impractical. NPEET's estimators (Repo 06) are the practical alternative for online use.  
H3: FALSIFIED — Same sample complexity argument. Suitable only for offline analysis over large session archives.]

---

### Repository 08: `moraneus/MonAmI`
**URL:** https://github.com/moraneus/MonAmI  
**Domain:** Runtime Monitoring — First-Order Allen Temporal Logic (foATL)  
**Language:** Python  
**Summary:** MonAmI is a Python library for monitoring the First-Order Allen Temporal Logic (foATL), extending Allen's 13 interval relations with first-order quantification. Given a formula and a trace of timestamped events, it evaluates whether the trace satisfies the formula. Runtime monitor, not post-hoc verifier.

---

[HYPOTHESIS_MATRIX:  
1. MonAmI can serve as a **behavioral contract monitor** in Hermes — expressing workflow contracts ("tool B must always start after tool A finishes, and tool C must overlap with tool B") in foATL and verifying them against actual execution traces in real time.  
2. MonAmI's first-order extension enables **parameterized temporal assertions** — "For all session S, if tool X was invoked during S, then validation Y must have occurred before S ended" — enabling cross-session policy enforcement impossible with propositional temporal logics.  
3. MonAmI's trace prefix evaluation can function as an **early warning system** — detecting partial traces that cannot possibly satisfy the foATL contract, allowing Hermes to abort and retry before the full workflow completes.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if MonAmI cannot process event traces in real time — if formula evaluation is too slow for Hermes's execution cadence.  
H2: FALSIFIED if foATL formula specification is too expressive for Hermes's actual contract needs — first-order quantification may be overkill if propositional Allen logic suffices.  
H3: FALSIFIED if MonAmI only evaluates complete traces (no prefix monitoring) — making it unsuitable for early-warning detection during execution.]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — MonAmI processes event traces incrementally. Python implementation overhead is manageable for agent-scale traces (tens to hundreds of events per session).  
H2: CONFIRMED (calibrated) — First-order extension is genuinely useful for Hermes when contracts involve "for all invocations of tool X" — parameterized across dynamic session content. The expressiveness is a feature, not overfit.  
H3: DEFERRED — Library documentation mentions monitoring; prefix evaluation behavior requires source inspection to fully confirm. If confirmed, this is one of the highest-value integration targets in this set.]

---

### Repository 09: `Z3Prover/z3`
**URL:** https://github.com/Z3Prover/z3  
**Domain:** SMT Solving — Satisfiability Modulo Theories  
**Language:** C++ with Python bindings (`z3-solver` pip package)  
**Summary:** Z3 is Microsoft Research's industrial-grade SMT solver handling arithmetic, bitvectors, arrays, uninterpreted functions, quantifiers, and string theories. Python bindings provide a high-level interface. Z3 is the backbone of many formal verification, program synthesis, and planning tools.

---

[HYPOTHESIS_MATRIX:  
1. Z3 can function as a **hard constraint satisfaction oracle** for Hermes — when the agent must schedule tool invocations subject to resource limits, dependency ordering, and time windows, Z3 guarantees optimal or infeasibility-certified solutions rather than heuristic guesses.  
2. Z3's Optimize() functionality can implement **multi-objective workflow planning** in Hermes — minimizing token cost while maximizing information gain and satisfying dependency constraints, producing a provably Pareto-optimal execution plan.  
3. Z3's incremental solving (push/pop stack) can power **online constraint revision** in Hermes — as new information invalidates earlier assumptions, the constraint stack is popped and revised without full resolving.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if constraint encoding of Hermes workflows requires quantifiers that make Z3 decidability undetermined (quantified integer arithmetic is undecidable in general).  
H2: FALSIFIED if multi-objective optimization in Z3 is too slow for interactive planning timescales — Z3 Pareto optimization can be exponential in the number of objectives.  
H3: FALSIFIED if incremental solving provides no speedup over re-solving for the constraint sizes typical of Hermes planning (small instances may have negligible caching benefit).]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — Hermes workflow constraints (ordering, resource limits, dependency chains) are expressible in quantifier-free linear arithmetic (QFLIA) — which Z3 decides in polynomial time with its Simplex-based solver.  
H2: DEFERRED — Multi-objective Z3 optimization with 3-5 objectives and 20-50 tools is tractable in practice (seconds range). Needs benchmarking against actual Hermes planning instances.  
H3: CONFIRMED — Z3's incremental stack is specifically designed for this use case and provides significant speedup for sequential constraint refinement. This is a textbook Z3 application pattern.]

---

### Repository 10: `process-intelligence-solutions/pm4py`
**URL:** https://github.com/process-intelligence-solutions/pm4py  
**Domain:** Process Mining — Discovery, Conformance Checking, Performance Analysis  
**Language:** Python (AGPL-3.0, Fraunhofer FIT origin)  
**Summary:** PM4Py is the reference Python library for process mining. Given an event log (CSV/XES), it discovers process models (Petri nets, BPMN, DFG), checks conformance between logs and models, computes fitness/precision/generalization metrics, and produces performance diagnostics.

---

[HYPOTHESIS_MATRIX:  
1. PM4Py's conformance checking (token-replay, alignments) can serve as a **Hermes workflow auditor** — given a declared process model (the intended DAG) and an actual execution log (what Hermes actually did), it computes fitness scores and identifies exact deviations.  
2. PM4Py's process discovery (Alpha Miner, Inductive Miner) can **reverse-engineer Hermes's emergent behavior** from execution logs — discovering what the agent actually does versus what it was designed to do, surfacing hidden execution patterns.  
3. PM4Py's performance analysis (dotted chart, performance DFG) can identify **bottleneck activities and temporal anti-patterns** in Hermes workflows — tools that consistently delay the critical path or sessions that enter pathological timing patterns.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if Hermes execution logs are not structured as case-activity-timestamp event logs (PM4Py requires this format; Hermes may use a different trace schema).  
H2: FALSIFIED if discovered process models are too complex (spaghetti processes with many arcs) to be interpretable or actionable — this happens when real behavior is highly variant.  
H3: FALSIFIED if per-session performance analysis requires at least hundreds of sessions to identify stable bottleneck patterns.]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — Hermes execution logs can be formatted as XES or pandas DataFrame with case_id=session_id, activity=tool_name, timestamp=call_time. Direct schema mapping.  
H2: DEFERRED — Inductive Miner (sound process tree discovery) produces readable models even for high-variance logs. Interpretability depends on behavioral variance in practice.  
H3: CONFIRMED — PM4Py's dotted chart and performance DFG are meaningful with as few as 50 sessions. Bottleneck identification is a primary use case with low data requirements.]

---

### Repository 11: `h2r/pomdp-py`
**URL:** https://github.com/h2r/pomdp-py  
**Domain:** Planning Under Uncertainty — Partially Observable Markov Decision Processes  
**Language:** Python/Cython (Brown University H2R Lab)  
**Summary:** pomdp-py is a framework for defining and solving POMDP problems in Python. Provides interfaces for State, Action, Observation, TransitionModel, ObservationModel, RewardModel, and PolicyTree. Implements POUCT (POMCP-UCT), Value Iteration, and other solvers. Cython-accelerated for performance.

---

[HYPOTHESIS_MATRIX:  
1. pomdp-py can model Hermes's **tool selection problem under partial observability** — when the agent doesn't know which tool will succeed (hidden state = tool reliability), POMCP-UCT computes an optimal policy over the belief state rather than greedy selection.  
2. The Observation model in pomdp-py can integrate **noisy feedback signals** from Hermes tools — when tool outputs are probabilistic (OCR errors, API timeouts, model hallucinations), the observation model maintains a probability distribution over true task states.  
3. pomdp-py's policy tree representation can encode **contingency plans** for Hermes — specifying exactly which tool to invoke given each possible observation, replacing reactive ad-hoc retry logic with a principled decision tree.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if the state space for Hermes's tool reliability is too large for POMCP-UCT to explore — exponential state spaces require enormous simulation budgets.  
H2: FALSIFIED if defining observation models for Hermes tools requires manual probability specification that is too expensive to maintain as tools evolve.  
H3: FALSIFIED if pomdp-py's Cython compilation fails in the Hermes deployment environment (requires C compiler and Cython build step).]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — POMCP-UCT is an anytime algorithm that works with continuous/large state spaces via particle-based belief representation. Hermes's tool state space (~10 tools, each with 3-5 reliability states) is well within tractable range.  
H2: DEFERRED — Observation model probabilities could be learned from historical execution data rather than specified manually (using pgmpy's parameter learning — Repo 04). Integration between Repos 04 and 11 is high-value.  
H3: DEFERRED — Cython build is a real deployment friction. The pure Python fallback incurs 5-10x slowdown but is functional. For batch offline planning, acceptable.]

---

### Repository 12: `eth-sri/fastsmt`
**URL:** https://github.com/eth-sri/fastsmt  
**Domain:** ML-Guided SMT Solving — Strategy Learning for Z3  
**Language:** Python (ETH Zurich SRI Lab)  
**Summary:** FastSMT learns to select and sequence Z3's internal solving tactics using machine learning, reducing solving time by 10-100x on benchmarks. It trains a policy over Z3's tactic language to construct solver strategies tailored to problem families.

---

[HYPOTHESIS_MATRIX:  
1. FastSMT can provide **Hermes-specific Z3 strategy specialization** — by training FastSMT on constraint instances generated by Hermes's planning problems, it learns a solving strategy 10-100x faster than Z3's default on Hermes's specific constraint patterns.  
2. FastSMT's tactic language (Z3 tactic combinators: `Then`, `OrElse`, `TryFor`) can be used **independently of FastSMT's ML component** as a programmable interface for constructing domain-specific Z3 solvers inside Hermes.  
3. FastSMT's benchmark generation pipeline can serve as a **constraint instance factory** — generating diverse planning constraint instances for testing Hermes's planning components under varied constraint pressures.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if Hermes's planning constraint instances are too diverse (across different problem families) for FastSMT to learn a specialized strategy.  
H2: FALSIFIED if Z3 tactic combinators require expertise in Z3 internals that creates prohibitive maintenance burden.  
H3: FALSIFIED if the benchmark generation pipeline is tightly coupled to the ML training loop and cannot be used independently.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — Hermes's planning constraints are likely from a narrow family (scheduling + dependency ordering). FastSMT's specialization should be effective if Hermes generates enough training instances (100-1000 planning problems).  
H2: CONFIRMED — Z3 tactic combinators are well-documented and provide real value independently of ML. `Tactic("smt")`, `Then(Tactic("simplify"), Tactic("solve-eqs"))` are immediately usable patterns.  
H3: CONFIRMED — The benchmark pipeline is a standalone Python module. It can generate constraint instances from Hermes planning scenarios without requiring the ML training loop.]

---

### Repository 13: `ajcr/IntervalAlgebra`
**URL:** https://github.com/ajcr/IntervalAlgebra  
**Domain:** Qualitative Temporal Reasoning — Allen's Interval Algebra  
**Language:** Python/C extension  
**Summary:** IntervalAlgebra is a C extension module implementing an Interval type and the 13 Allen relations (before, meets, overlaps, during, starts, finishes, equals, and their converses). Provides efficient computation of relation composition, constraint propagation via path-consistency algorithm, and transitivity table lookup.

---

[HYPOTHESIS_MATRIX:  
1. IntervalAlgebra's 13 relations can model **coarse-grained temporal relationships** between Hermes execution phases — rather than comparing exact timestamps, the agent reasons qualitatively ("phase A overlaps with phase B") which is more robust to clock imprecision.  
2. The path-consistency algorithm can validate **temporal feasibility** of Hermes's planned execution order — given a set of interval constraints between planned activities, path-consistency detects contradictions before execution begins.  
3. Allen relation composition tables can power **temporal inference** in Hermes — "If A is before B and B overlaps C, then A is before or meets or overlaps C" — enabling the agent to derive implicit temporal relationships without explicit enumeration.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if qualitative temporal reasoning is too coarse for Hermes's needs — if exact duration constraints matter, Allen algebra cannot express them.  
H2: FALSIFIED if path-consistency algorithm is too slow for large constraint networks (it is O(n³) in the number of intervals).  
H3: FALSIFIED if Allen's transitivity table produces too many disjunctive constraints to be useful — the composition of two Allen relations is often a disjunction of multiple relations, making inference ambiguous.]

[EPISTEMIC_DELTA:  
H1: CONFIRMED — Hermes's temporal structure is well-suited for qualitative reasoning. "Tool invocation A is before tool B" is more meaningful than exact timestamps in most agent contexts. The coarseness is a robustness feature.  
H2: CONFIRMED — For Hermes's planning graph (20-50 activities), O(n³) path-consistency is microseconds on modern hardware. Trivially tractable.  
H3: DEFERRED — Disjunctive inference is inherent to interval algebra. The critical use case for Hermes is detecting inconsistency (precise), not fully determining all relations (ambiguous). Inconsistency detection is the primary target.]

---

### Repository 14: `Kappa-Dev/ReGraph`
**URL:** https://github.com/Kappa-Dev/ReGraph  
**Domain:** Graph Rewriting — Sesqui-pushout Rewriting, Knowledge Graph Evolution  
**Language:** Python  
**Summary:** ReGraph is a Python framework for graph-based hierarchical knowledge representation and rewriting. Implements sesqui-pushout (SqPO) rewriting — a category-theoretic framework for applying transformation rules to graphs. Supports NetworkX and Neo4j backends. Used in systems biology for Kappa rule-based models.

---

[HYPOTHESIS_MATRIX:  
1. ReGraph's rule-based graph transformation can model **Hermes ontology evolution** — as the agent's knowledge graph is updated (new entities discovered, relationships revised, nodes merged), these updates are expressed as formal rewriting rules that preserve ontological invariants.  
2. SqPO rewriting's categorical structure can enforce **compositionality constraints** on Hermes's tool pipeline — tool compositions that violate structural invariants are detectable as invalid rewrites before execution.  
3. ReGraph's hierarchical representation can model **Hermes's multi-level abstraction** — the same task at the semantic level (intent graph), planning level (DAG of steps), and execution level (tool call graph) as a hierarchy of graphs with coarsening morphisms between levels.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if Hermes's knowledge graph updates are too frequent or too large to process with SqPO rewriting in real time.  
H2: FALSIFIED if tool pipeline composition constraints are better expressed as type systems or JSON Schema validation — making graph rewriting an over-engineered solution.  
H3: FALSIFIED if the hierarchical graph representation is redundant with Hermes's existing multi-level architecture and provides no additional invariant guarantees.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — Overhead depends on implementation. For small-scale knowledge graph updates (tens of nodes), SqPO is fast. For Hermes's session-level graph evolution, viable.  
H2: FALSIFIED — Anti-confirmation succeeds. JSON Schema and Python type hints provide a lower-cost path for tool schema validation. ReGraph's value is specifically when compositions create emergent graph structures that schemas cannot capture — a niche but real use case.  
H3: CONFIRMED (non-redundant) — The coarsening morphism between levels is genuinely useful: it provides a formal map between what the agent intends (semantic level) and what it does (execution level), enabling formal identification of intent-execution gaps. Not expressible as a type system.]

---

### Repository 15: `mckinsey/causalnex`
**URL:** https://github.com/mckinsey/causalnex  
**Domain:** Causal Bayesian Networks — Structural Learning + Interventional Inference  
**Language:** Python (McKinsey & Company, Apache 2.0)  
**Summary:** CausalNex provides tools for building, learning, and querying Bayesian Networks with interventional (do-calculus) support. Combines structural learning (NOTEARS — differentiable acyclicity constraint), Bayesian Network parameter estimation, and do-calculus for computing P(Y | do(X)).

---

[HYPOTHESIS_MATRIX:  
1. CausalNex's NOTEARS structure learning can produce **gradient-descent-discovered causal graphs** from Hermes execution data — unlike PC algorithm (combinatorial), NOTEARS is a continuous optimization problem, enabling warm-starting from prior session knowledge.  
2. CausalNex's BayesianNetwork + intervention API can simulate **what-if scenarios** for Hermes planning — "If I force tool X to execute (do(X=1)), what is the probability that downstream outcome Y succeeds?" — enabling rational action selection grounded in causal estimates.  
3. CausalNex's integration with sklearn-style preprocessing enables **end-to-end pipeline construction** — raw Hermes session logs → feature engineering → NOTEARS structure learning → parameter estimation → interventional query — as a single continuous Python pipeline.]

[FALSIFICATION_CRITERIA:  
H1: FALSIFIED if NOTEARS structure learning is sensitive to initialization and produces different graphs on different runs (the optimization landscape has local optima), making it unreliable for Hermes's architecture map.  
H2: FALSIFIED if CausalNex's do-calculus implementation is less mature than DoWhy's (Repo 01) — making it a redundant and inferior alternative.  
H3: FALSIFIED if the end-to-end pipeline requires hyperparameter tuning that is difficult to automate for a continuously evolving Hermes session dataset.]

[EPISTEMIC_DELTA:  
H1: DEFERRED — NOTEARS's non-convexity is a known limitation. In practice, multiple random restarts and averaging produce stable skeletons. Viable with an ensemble approach.  
H2: CONFIRMED (complementary, not redundant) — CausalNex's value over DoWhy is its NOTEARS structure learning + Bayesian Network parameter fitting in one pipeline. DoWhy assumes a given graph; CausalNex discovers and estimates together. Complementary.  
H3: DEFERRED — NOTEARS has one main hyperparameter (acyclicity regularization λ). Automated tuning via cross-validation fitness is feasible.]

---

## Final Synthesis

---

[HARNESS_HERMES:

The 15 repositories form a **Causal-Temporal Intelligence Stack** for the Hermes Agent Harness, organized into six functional layers:

**Layer C — Causal Graph Infrastructure (Repos 01, 02, 15)**
The agent gains the ability to: (1) discover causal structure from execution data (causal-learn, CausalNex/NOTEARS), (2) identify whether a causal effect is computable from observational data (DoWhy), and (3) estimate interventional distributions (DoWhy refutation + CausalNex BN). This eliminates the agent's native reliance on correlation as a proxy for causation.

**Layer T — Temporal Contract Enforcement (Repos 08, 13)**
The agent can express behavioral contracts in foATL (MonAmI) and check them against execution traces in real time. Allen's interval algebra (IntervalAlgebra) provides qualitative temporal reasoning between execution phases that is robust to clock imprecision and captures ordering structure that exact timestamps lose.

**Layer P — Probabilistic Planning Under Uncertainty (Repos 04, 11)**
The agent gains a full POMDP-based decision framework (pomdp-py) for tool selection under partial observability, with belief state tracking powered by pgmpy's Bayesian Network inference. This replaces reactive greedy selection with principled lookahead planning.

**Layer S — Constraint Satisfaction & SMT (Repos 09, 12)**
Z3 provides a hard constraint solver for planning feasibility and optimization. FastSMT provides the ability to specialize Z3's strategy for Hermes-family constraint instances, reducing solve time by orders of magnitude.

**Layer I — Information-Theoretic Monitoring (Repos 05, 06, 07)**
NPEET provides lightweight mutual information-based dependency probes and independence tests (underpinning causal discovery). IDTxl provides directional information flow analysis for offline session audits. `dit` provides partial information decomposition for attribution of joint module contributions.

**Layer X — Process Mining & Formal Evolution (Repos 03, 10, 14)**
PM4Py enables process discovery and conformance checking against declared workflow models. Intel's causality-lab provides research-grade causal discovery for novel algorithm experimentation. ReGraph provides formal graph rewriting for ontology evolution and intent-execution gap detection.
]

---

[IMPLEMENTATION_WORKFLOW:

**Phase 0 — Foundation (Week 1-2)**

Install core packages:
```bash
pip install dowhy causal-learn pgmpy pm4py z3-solver npeet causalNex
pip install git+https://github.com/pwollstadt/IDTxl
pip install git+https://github.com/moraneus/MonAmI
pip install dit pomdp-py
```

Build IntervalAlgebra C extension from source:
```bash
git clone https://github.com/ajcr/IntervalAlgebra && cd IntervalAlgebra && pip install .
```

---

**Phase 1 — Execution Log Schema (Week 2)**

Define Hermes's canonical execution log schema (compatible with PM4Py, causal-learn, and NPEET):
```python
hermes_trace_schema = {
    "case_id": str,           # session identifier
    "activity": str,          # tool name or step label
    "timestamp": datetime,    # ISO8601 call start time
    "duration_ms": float,     # call duration
    "success": bool,          # outcome
    "tokens_in": int,         # input token count
    "tokens_out": int,        # output token count
    "retry_count": int,       # retry attempts
    "parent_activity": str    # which step invoked this one
}
```

---

**Phase 2 — Causal Architecture Discovery (Week 3-4)**

Run causal-learn PC algorithm on aggregated session logs:
```python
from causallearn.search.ConstraintBased.PC import pc
import pandas as pd

df = load_hermes_sessions()
data = df[['duration_ms', 'tokens_in', 'tokens_out', 'retry_count', 'success']].to_numpy()
cg = pc(data, alpha=0.05, indep_test='fisherz')

# Export to DoWhy for effect identification
import dowhy
model = dowhy.CausalModel(data=df, graph=cg.G)
identified_effect = model.identify_effect(proceed_when_unidentifiable=False)
```

---

**Phase 3 — Temporal Contract Layer (Week 5)**

Express Hermes behavioral contracts in foATL and monitor in real time:
```python
from monami import Monitor

# Contract: for every invocation of tool_X, validation_Y must occur before session ends
contract = "FORALL s: (tool_X DURING s) IMPLIES (validation_Y BEFORE_END s)"
monitor = Monitor(formula=contract)

for event in hermes_execution_stream():
    monitor.update(event)
    if monitor.is_violated():
        trigger_remediation()
```

Add Allen interval consistency checking for planned execution orders:
```python
from interval_algebra import Interval, path_consistency

planned = [Interval('phase_A'), Interval('phase_B'), Interval('phase_C')]
constraints = {('phase_A', 'phase_B'): 'before', ('phase_B', 'phase_C'): 'overlaps'}
is_consistent = path_consistency(planned, constraints)
```

---

**Phase 4 — POMDP Tool Selection (Week 6-7)**

Model Hermes tool selection as a POMDP with belief state planning:
```python
import pomdp_py

class HermesToolState(pomdp_py.State):
    def __init__(self, tool_reliabilities): ...

class HermesToolAction(pomdp_py.Action):
    def __init__(self, tool_name): ...

# Transition, observation, and reward models learned from historical data (pgmpy)
agent = pomdp_py.Agent(init_belief, policy_model, transition_model,
                        observation_model, reward_model)
planner = pomdp_py.POUCT(max_depth=5, num_sims=1000, exploration_const=math.sqrt(2))
action = planner.plan(agent)
```

---

**Phase 5 — Constraint Planning via Z3 (Week 7-8)**

Hard constraint planning for Hermes tool scheduling:
```python
from z3 import *

opt = Optimize()
tools = {name: Bool(name) for name in hermes_tool_registry}

# Dependency constraints
for dep_a, dep_b in dependency_graph.edges():
    opt.add(Implies(tools[dep_b], tools[dep_a]))

# Objective: minimize token cost
token_cost = Sum([If(tools[t], cost[t], 0) for t in tools])
opt.minimize(token_cost)

result = opt.check()
if result == sat:
    plan = opt.model()
```

---

**Phase 6 — Process Mining Audit Loop (Week 8-9)**

PM4Py conformance checking as a post-session audit:
```python
import pm4py

log = pm4py.format_dataframe(hermes_session_df, case_id='case_id',
                               activity_key='activity', timestamp_key='timestamp')
net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
fitness = pm4py.fitness_token_based_replay(log, net, initial_marking, final_marking)
deviations = pm4py.conformance_diagnostics_token_based_replay(log, net, im, fm)

for dev in deviations:
    if dev['trace_fitness'] < 0.95:
        log_symbolic_scar(dev)  # FIREBEARER mode integration
```

---

**Phase 7 — Information-Theoretic Monitoring (Week 9-10)**

NPEET as lightweight online dependency probe:
```python
from npeet.entropy_estimators import mi, cmi

x = extract_feature(sessions, 'tokens_in')
y = extract_feature(sessions, 'success').astype(float)
z = extract_feature(sessions, 'retry_count')

mutual_info = mi(x, y, k=5)
conditional_mi = cmi(x, y, z, k=5)

# If CMI ≈ 0 and MI > 0: z is a sufficient mediator (z-blocks x→y)
# If CMI > 0: direct dependence survives conditioning
```

---

**Phase 8 — Symbolic Scar Integration (FIREBEARER Loop)**

All deviations, falsified hypotheses, and causal violations are logged as Symbolic Scars:

```
SCAR[2026-06-26-01]: MonAmI contract violation — validation_Y missing before session end 
in 3.2% of sessions. Root cause (DoWhy): tool_Z invocation (do(tool_Z=1)) reduces 
P(validation_Y) by 0.18. Action: add conditional constraint in Z3 planner to force 
validation_Y whenever tool_Z is invoked.
```

Each scar encodes: what violated, the causal mechanism, and the constraint patch applied.
This is L3.8 Ontological Metabolism operationalized.
]

---

*End of Hermes Discovery Report — 2026-06-26*  
*Sensor: Paraconsistent Integration Sensor | PDL:v1.0 | Autonomous Run | Epistemic Trajectory: Primary Deliverable*
