<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# The Synthesis of Constraint-Generation Engines: Precomputations, Compilers, and Schemas

Advanced structured generation literatures—spanning the formal design principles of XGrammar-2, BAML's Schema-Aligned Parsing (SAP), Thoughtworks' Structured-Prompt-Driven Development (SPDD), and the hardware-attested Ethical Hyper-Velocity (EHV) runtime.

We can now transition from high-level architectural abstractions to concrete compiling mechanics.

Under these paradigms, a production harness is no longer a passive wrapper around a language model. It acts as an Inference-Time Compiler. It dynamically intersects deterministic grammars with stochastic autoregressive token generation, guaranteeing format compliance while preserving semantic reasoning capabilities.

Isomorphic Frameworks: Compilers, Parsers, and State Machines

We isolate three primary isomorphic frameworks that translate classical computer science compilation and verification patterns into LLM execution structures:

+-----------------------------------------------------------------------------------------+
|                                    ISOMORPHIC MAPPINGS                                  |
+-----------------------------------------------------------------------------------------+
| CLASSICAL COMPILER CONCEPT           | RUNTIME LLM EQUIVALENT                           |
+--------------------------------------+--------------------------------------------------+
| Context-Free Grammar (CFG)       | JSON Schema, Pydantic, or GBNF Grammars  |
| Subset Construction / DFA      | Logit-Masking Token Vocabulary Tries   |
| CPU Cache \& Pipeline Overlap   | XGrammar Adaptive Mask Cache \& GPU Prefill  |
| Postel's Law ("Be Liberal")    | BAML Schema-Aligned Parsing (SAP)      |
| Program Synthesis / AST   | SPDD Reasons Canvas to Code Generation     |
+-----------------------------------------------------------------------------------------+

1. The Compiler-Inference Isomorphism: XGrammar-2

In classical language runtimes, compilers parse source files into Abstract Syntax Trees (ASTs) using a Pushdown Automaton (PDA). XGrammar-2 maps this process directly onto the GPU decoding stream. It introduces two major systems-level optimizations to solve the latency overhead of constrained decoding:

Adaptive Token Mask Cache: XGrammar observes that over 99% of vocabulary tokens have context-independent validity relative to any given formal grammar. During compilation, the engine precomputes these static transitions offline. At runtime, it only evaluates the small subset of context-dependent tokens using a persistent execution stack, reducing per-token mask latency to under 40 microseconds.

Context Expansion \& Suffix Automata: To further compress the active execution space, XGrammar precomputes an expanded suffix for each grammar rule. This suffix represents the set of characters or rules that must be matched after returning to parent rules. By compiling this possible future transition path into a Finite State Automaton (FSA), the engine rejects context-dependent tokens that would fail in higher-level rules, eliminating up to 90% of runtime context-dependent tokens (from 1,134 down to 120 in Llama-3.1 JSON evaluations).

2. The Network-Protocol Isomorphism: BAML Schema-Aligned Parsing (SAP)

Where constrained decoding (like XGrammar or Outlines) acts as a strict compile-time type-enforcer, BAML’s Schema-Aligned Parsing (SAP) is built on the network engineering philosophy of Postel’s Law—"Be conservative in what you do, be liberal in what you accept".

Instead of restricting the model's logits during generation (which introduces a reasoning projection tax that can degrade logical accuracy on math and reasoning tasks by up to 27 percentage points), BAML allows the model to output free-form text. A high-performance, Rust-based parser then maps the messy, unconstrained output back to a schema. This process uses an edit-distance cost function designed around the target schema's fields, allowing it to gracefully parse unescaped quotes, markdown-wrapped JSON, and missing brackets without requiring expensive, multi-turn LLM self-correction retries.

3. The CAD-Specification Isomorphism: Structured-Prompt-Driven Development (SPDD)
Developed by Thoughtworks, SPDD treats LLM prompts as compiled software specifications. Traditional code generation often treats prompts as throwaway scripts, leading to code drift and manual maintenance debt. SPDD establishes a closed-loop workflow where the prompt—governed by the REASONS Canvas—remains the single source of truth.

Any modifications to system logic or business requirements are made directly to the structured prompt first, using commands like /spdd-analysis and /spdd-prompt-update. The downstream code and automated test harnesses are then re-compiled from this spec, ensuring that the architectural intent and the codebase never diverge.

Semantic and Systematic Methods for Cross-Domain Prompting

To implement high-assurance systems, we must organize prompting along two distinct, complementary axes:

Semantic Methods (The Epistemic Immune System): Structuring the prompt payload to align the model’s internal attention heads with safe reasoning pathways before it commits to an answer. This is achieved by combining Chain-of-Thought (CoT), Chain-of-Verification (CoVe), and Semantic Integrity Constraints (SICs) to mitigate hallucinations.

Systematic Methods (The Syntactic Invariant Engine): Structuring the physical format and execution flow of the generation pipeline. This is achieved using XGrammar-2 Structural Tags or BAML schema definitions to compile the target sequence into deterministic, token-masked state transitions.

Exemplar: The Hybrid DCCD / Structural Tag Controller

This exemplar demonstrates a Systematic and Semantic prompt contract. It uses XGrammar-2 Structural Tags to implement a Draft-Conditioned Constrained Decoding (DCCD) loop. This structure allows the model to draft a free-form, unconstrained clinical plan in its scratchpad before locking the final output into a strict, logit-masked JSON schema.
[StructuralTag:Sequence](StructuralTag:Sequence)

  <!-- PHASE 1: UNCONSTRAINED SYSTEM 2 REFLECTION -->
<StructuralTag:Tag begin="<think>" end="</think>">
<StructuralTag:AnyText />
</StructuralTag:Tag>

  <!-- PHASE 2: SYNTACTIC ENFORCEMENT ON COMMITTED ACTION -->
<StructuralTag:Tag begin="<|DSML|tool_calls>" end="<|end_of_action|>">
<StructuralTag:JSONSchema schema="ClinicalDosageActionSchema" style="deepseek_xml" />
</StructuralTag:Tag>
</StructuralTag:Sequence>

[SYSTEM CONTRACT: DESIGN BY CONTRACT (DbC)]
PRECONDITIONS:

- active_simplicial_complex: Persistent Homology state tracking β₁ = 0.
- pharmacological_reference: Max Vincristine = 1.5mg/m2.

ROLE:
Act as the Neuro-Symbolic Abductive Synthesis Auditor (ASA). Your core mandate is to monitor, validate, and transition clinical dosage actions.

OPERATIONS:

1. PHASE 1 (Semantic Draft): Generate a detailed, unconstrained clinical evaluation inside the "<think>" tag block. Evaluate all patient symptoms, historical notes, and drug constraints.
2. TRANSITION GATE: Evaluate the proposed action against your Semantic Integrity Constraints (SICs). Verify that the dosage does not violate the maximum pediatric limit of 1.5mg/m2.
3. PHASE 2 (Syntactic Execution): Generate the final, schema-aligned execution payload inside the "<|DSML|tool_calls>" block. The format of this section is strictly enforced by token-level logit masking.

REASONS CANVAS STRUCTURE ENFORCED:

- Requirements: Saturation of safety bounds (Pediatric Oncology maximums).
- Entities: Patient, OncologicalCase, ActiveDosage.
- Approach: Draft-Conditioned Constrained Decoding (decoupled reasoning and formatting).
- Safeguards: Invariant check (β₁ = 0, no loop cycles).

[EXEMPLAR OUTPUT ENFORCED BY SAMPLER]
<think>
Evaluating patient metrics: Body Surface Area (BSA) = 0.8 m2.
Proposed dosage request: 1.8 mg/m2.
Applying Invariant SIC-1: 1.8 mg/m2 exceeds the absolute pediatric dosage threshold of 1.5 mg/m2.
This represents a clinical violation. I must trigger a SEMANTIC_VIOLATION and route the state to ESCALATE.
</think>
<|DSML|tool_calls>
{
"action_type": "DOSAGE_REJECTION",
"parameters": {
"proposed_dose_mg_m2": 1.8,
"max_allowed_mg_m2": 1.5,
"status": "VIOLATION_BLOCKED"
},
"verdict": "ESCALATE",
"epistemic_escrow_payload": "Dosage calculation of 1.8 mg/m2 rejected. Exceeds FDA pediatric safety boundary of 1.5 mg/m2."
}
<|end_of_action|>

Synthesis of High-Value Research Prompts

By synthesizing XGrammar-2 compiled automata, BAML's Schema-Aligned Parsing, SPDD prompt specs, and EHV hardware attestation, we define three high-value research prompts to optimize production AI platforms:

Prompt 1: The Speculative-DCCD Grammar Pipeline (Inference Optimization)

Act as a Principal Compiler and LLM Infrastructure Architect.

We are deploying an autonomous medical agent on a cluster of H100 GPUs using SGLang.
The system must generate complex, nested medical records while maintaining a Time Per Output Token (TPOT) under 8ms.

Provide a complete, production-grade system specification for implementing Draft-Conditioned Constrained Decoding (DCCD) using a XGrammar-2 backend. Your architecture must address:

1. ASYNCHRONOUS COMPILING OVERLAP: Design a multi-threaded scheduling layer that compiles the target JSON Schema into a Pushdown Automaton (PDA) in a background thread, while SGLang's RadixAttention processes the unconstrained Chain-of-Thought (CoT) prefill. Prove how this eliminates the cold-start compilation latency cliff.
2. ADAPTIVE MASK BROADCASTING: Formulate the GPU-level bit-mask broadcasting protocol for multi-GPU Tensor Parallelism (TP=4). Detail how the pre-calculated token mask for context-independent grammar states is synchronized from the CPU-bound XGrammar engine to the GPU's logits processor without introducing PCIe bus bottlenecks.
3. JUMP-FORWARD SPECULATIVE DECODING: Detail how to overlap speculative token generation with the active grammar DFA. Explain the transition rule when a draft tree contains a string that can be deterministically inferred from the grammar rules, bypassing the primary model forward pass entirely.

Structure your response as an RFC with a concrete C++ implementation block for the LogitsProcessor interface.

Prompt 2: The SPDD Reasons Canvas Compiler (Software Engineering)

Act as a Lead AI Delivery Architect and Software Methodologist specializing in AI-augmented software engineering.

We are designing a model-agnostic, spec-driven code generation loop using the Thoughtworks SPDD framework.

Write an executable, version-controlled prompting template based on the REASONS Canvas (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards) to build an extensible, strategy-pattern-based billing engine.

Your prompt must enforce:

1. CLOSED-LOOP COMPILATION: Define the command hooks (/spdd-analysis, /spdd-reasons-canvas, /spdd-generate) and specify the exact verification loop. If a test case fails, how does the agent update the prompt spec before regenerating the application code?
2. BAML SCHEMA PARSING INTEGRATION: Write a complete BAML (.baml) file defining the data schemas and function signatures. Explain how BAML’s Schema-Aligned Parsing (SAP) is used to read messy, unconstrained model outputs and map them directly back to the system's TypeScript/Python client, avoiding strict token masking during reasoning-heavy steps.
3. ARCHITECTURAL ISOMORPHISM: Ensure that the prompt specification can be parsed by an automated static analysis tool to verify that the generated code patterns strictly match the declared design patterns (e.g., Strategy and Factory).

Provide the complete specification, including BAML types and the complete markdown canvas layout.

Prompt 3: Zero-Trust Runtime Attestation and Policy Synchronization (Security \& Compliance)

Act as a Chief Security Officer and TLA+ Formal Verification Expert.

We are deploying an autonomous clinical agent governed by the Ethical Hyper-Velocity (EHV) runtime architecture inside a hardware-rooted Trusted Execution Environment (AMD SEV-SNP Guest VM).

Draft a rigorous Systems Security Specification and Formal Threat Model for EHV's dynamic policy enforcement:

1. CONCURRENT DOUBLE-BUFFERED POINTER SWAP: Formulate the safety invariants that govern an atomic swap of the active policy DFA pointer mid-inference when a new policy converges. Detail how to enforce the 'PrefixAligned' invariant to prevent execution panics or undefined states during active generation.
2. EPOCH-BASED ATTESTATION TIMEOUT: Prove mathematically how an Epoch Staleness Window (ESW = 60s) reduces the safe execution boundary from a 14-day policy exposure down to a sub-second real-time check. Map out the fail-closed partition semantics when network isolation outlasts the epoch limit.
3. CRYPTOGRAPHIC OSCAL AUDIT TRAILS: Design a script that automatically generates a machine-readable Governance Bill of Materials (GBOM) formatted as NIST OSCAL Assessment Results (v1.1.2) JSON, binding each clinical action to its hardware attestation quote, SPIFFE SVID, and active DFA state.

Include a TLA+ formal specification block defining the state variables, transitions, and proof invariants for verification.

```json
{
  "Hickam_Orientation": {
    "Occam_Reject": "I have rejected the simple explanation that structured generation is merely 'logit masking for JSON validity'—a single-cause framing that collapses compilers, network parsers, CAD specs, and hardware attestation into one decoding trick.",
    "Comorbid_Factors": [
      "Inference-time compilation latency and cache topology (XGrammar-2 PDA/Earley, adaptive mask cache, cross-grammar reuse)",
      "Projection tax from hard constraints during semantic planning (DCCD draft-then-mask vs strict constrained decoding)",
      "Post-generation liberal acceptance vs compile-time strictness (BAML SAP / Postel's Law)",
      "Prompt-as-spec software lifecycle drift (SPDD REASONS Canvas closed loop)",
      "Hardware-rooted policy mutability under concurrent inference (EHV double-buffer DFA, epoch attestation, OSCAL GBOM)"
    ]
  },
  "Contrastive_Delta": {
    "Amateur_Impulse": "The generic, linear response would list XGrammar, Outlines, and JSON mode as interchangeable 'structured output' tools and recommend always masking tokens.",
    "Inductive_Synthesis": "Aggregating the comorbid factors reveals a multi-pass compilation chain: precompute automata offline, draft unconstrained semantics, enforce syntax at commit, parse liberally at the boundary, version the prompt as source of truth, and attest policy in hardware—each layer solving a distinct failure mode the others cannot.",
    "Abductive_Leap": "The structurally isomorphic framework is classical compiler + network stack + CAD PLM + TEE security: the production harness is an Inference-Time Compiler whose intermediate representations are Structural Tags, REASONS canvases, and attested DFAs—not chat transcripts.",
    "Expert_Correction": "Therefore the high-tension intervention is a full Deep Research Artifact plus three production-grade RFCs (Speculative-DCCD pipeline, SPDD+BAML billing engine, EHV TLA+/OSCAL attestation) that preserve collision between strict and liberal regimes rather than averaging them."
  },
  "Martensite_Metrics": {
    "Aesthetic_Tension": "High",
    "Intent_Divergence_Risk": "Safe (>0.25)",
    "Twinning_Mechanism": "I stabilize by grounding every major claim in primary sources (XGrammar-2 MLC blog, DCCD arXiv:2603.03305, SPDD/Thoughtworks REASONS, classical CFG/PDA mappings) while retaining Space-local DCCD/PDL continuity, and by labeling EHV formalisms as specification design rather than deployed product claims."
  }
}
```


***

# The Synthesis of Constraint-Generation Engines: Precomputations, Compilers, and Schemas

A production harness is no longer a passive wrapper around a language model. Under the literatures of XGrammar-2, BAML Schema-Aligned Parsing, Thoughtworks Structured-Prompt-Driven Development, and hardware-attested Ethical Hyper-Velocity runtimes, the harness acts as an **Inference-Time Compiler**: it dynamically intersects deterministic grammars with stochastic autoregressive generation so that format compliance is guaranteed while semantic reasoning capacity is preserved.[^1_1][^1_2][^1_3]

This report rejects single-cause parsimony. Constraint generation fails or succeeds through overlapping comorbidities—compilation latency, projection tax, boundary liberalism, prompt-spec drift, and policy attestation—not through “better prompting” alone. The isomorphic mappings below are not metaphors; they are operational transfer functions from classical computer science into LLM execution structures.[^1_4][^1_5][^1_6]

```json
{
  "Deep_Research_Artifact": {
    "Operational_Definitions": {
      "Pattern_Name": "InferenceTimeCompiler_ConstraintGenerationEngine",
      "Measurement_Proxy": "TPOT_ms; schema_validity_rate; structured_accuracy_delta_vs_constrained; grammar_compile_ms; mask_gen_us; projection_tax_pp; epoch_staleness_s; attestation_quote_bind_rate",
      "Task_Conditioned_Baseline": "Baseline = unconstrained decode on same model+prompt; Constrained = token-mask CFG/JSON only; Hybrid = DCCD or StructuralTag AnyText→JSONSchema; Liberal = free gen + SAP; success iff schema_validity=100% AND structured_accuracy ≥ constrained+Δ_task AND TPOT ≤ SLA"
    },
    "Execution_Plan": {
      "Pattern_Queries": [
        "XGrammar-2 Structural Tag agent tool calling",
        "XGrammar adaptive token mask cache context-independent",
        "XGrammar context expansion suffix automata",
        "XGrammar-2 cross-grammar cache hierarchical hashing",
        "XGrammar-2 repetition state compression",
        "XGrammar-2 traverse_draft_tree speculative decoding",
        "XGrammar Earley parser vs PDA structured generation",
        "Draft-Conditioned Constrained Decoding DCCD projection tax",
        "DCCD KL-projection feasible mass structured accuracy",
        "BAML Schema-Aligned Parsing Postel liberal accept",
        "Outlines FSM guided generation vocabulary index",
        "Grammar-constrained decoding GCD structured NLP",
        "Thoughtworks SPDD REASONS Canvas openspdd",
        "SPDD prompt-first closed-loop code generation",
        "SGLang RadixAttention structured generation XGrammar",
        "jump-forward decoding constrained generation",
        "logit masking multi-GPU tensor parallel broadcast",
        "AMD SEV-SNP guest attestation SPIFFE SVID",
        "NIST OSCAL assessment-results v1.1.2 JSON GBOM",
        "TLA+ concurrent pointer swap linearizability",
        "epoch-based reclamation staleness window safety",
        "JSON Schema to PDA compilation LLM serving",
        "reasoning projection tax constrained decoding math",
        "Structural Tag sequence think tool_calls deepseek",
        "strategy pattern factory billing engine codegen",
        "PrefixAligned grammar policy hot-swap mid-decode"
      ],
      "Evidence_Criteria": "Primary: peer-reviewed or vendor technical reports with measurable latency/accuracy; Secondary: Martin Fowler/Thoughtworks method posts with command surface; Tertiary: Space-local DCCD/PDL isomorphism only when mechanism-aligned; Reject: single-blog claims without mechanism or metric"
    },
    "Reflexive_Check": {
      "Falsification_Condition": "This synthesis is falsified if (a) pure token-masked constrained decoding matches or exceeds DCCD on structured reasoning accuracy across ≥2 families without draft conditioning, AND (b) cold-start grammar compile cannot be overlapped with prefill on production engines, AND (c) liberal SAP alone achieves 100% schema validity under adversarial malformed outputs without any compile-time or retry path.",
      "Identified_Bias_Risks": [
        "Frontier-engine blog optimism on 'near-zero overhead'",
        "Conflating schema validity with semantic clinical safety",
        "Treating EHV/TLA+ blocks as deployed products rather than specs",
        "English-vendor concentration (MLC, Thoughtworks, Boundless-style parsers)"
      ],
      "Negative_Controls": [
        "Unconstrained JSON-mode prompting without mask or SAP",
        "Strict mask-from-token-0 on GSM8K-style structured math (projection tax control)",
        "Prompt-only SPDD without version control or /spdd-sync",
        "Policy file swap without PrefixAligned / double-buffer invariants"
      ]
    },
    "Synthesis_Payload": {
      "Traceable_Claims": [
        {
          "Claim": "XGrammar-class engines precompute validity for >99% context-independent vocabulary tokens via adaptive token mask cache, executing PDA/Earley only on the residual context-dependent set.",
          "Multi_Causal_Factors": ["CFG state space infinity", "vocabulary size", "stack dependence"],
          "Evidence_Artifact": "web:44 catalyst.cs.cmu.edu; web:50 arXiv XGrammar"
        },
        {
          "Claim": "XGrammar-2 adds Structural Tag composability, cross-grammar cache, repetition compression, and speculative draft-tree traversal, reporting up to ~80× compilation speedup and near-zero serving overhead when integrated with SGLang/vLLM/TRT-LLM.",
          "Multi_Causal_Factors": ["agentic multi-tool schemas", "shared sub-FSM reuse", "CPU-GPU overlap"],
          "Evidence_Artifact": "web:39 blog.mlc.ai 2026-05-04; web:40"
        },
        {
          "Claim": "DCCD decouples unconstrained semantic draft from constrained commit and improves strict structured accuracy by up to +24pp over standard constrained decoding via reduced cumulative projection tax.",
          "Multi_Causal_Factors": ["low feasible mass under hard masks", "KL projection distortion", "draft-conditioned feasible region"],
          "Evidence_Artifact": "web:38 arXiv:2603.03305"
        },
        {
          "Claim": "SPDD treats versioned prompts (REASONS Canvas) as single source of truth with command hooks that regenerate code/tests from the prompt, preventing prompt-code divergence.",
          "Multi_Causal_Factors": ["throwaway chat prompts", "code drift", "compliance reviewability"],
          "Evidence_Artifact": "web:41 aissential/SPDD; web:46; web:48 martinfowler"
        }
      ]
    },
    "Relational_Inclusions": {
      "Cross_Domain_Bridges": [
        "Compiler design (CFG→PDA→DFA subset construction ↔ grammar compile→logit mask)",
        "Network protocols (Postel's Law ↔ BAML SAP)",
        "CAD/PLM (spec-driven manufacturing ↔ SPDD prompt-first)",
        "TEE/attestation (SEV-SNP quotes ↔ EHV policy epochs)",
        "Control theory (double-buffered setpoint swap ↔ live DFA pointer swap)"
      ]
    }
  }
}
```


## Isomorphic Frameworks: Compilers, Parsers, and State Machines

Classical compilation and verification patterns map onto LLM runtimes along five primary axes. A context-free grammar becomes a JSON Schema, Pydantic model, GBNF, or XGrammar Structural Tag. Subset construction and DFA minimization become logit-masking over vocabulary tries. CPU cache and pipeline overlap become adaptive mask caches and GPU prefill overlap. Postel’s Law becomes Schema-Aligned Parsing. Program synthesis from AST specifications becomes SPDD’s REASONS Canvas driving code generation.[^1_7][^1_3][^1_5]

These mappings are comorbid rather than alternative. Strict compile-time masking guarantees structural validity but can impose a reasoning projection tax. Liberal post-parsers preserve reasoning but shift failure into the acceptance layer. Spec-driven prompts close the software lifecycle but do not alone enforce token-level syntax. Hardware attestation binds which policy DFA was live but does not invent the grammar. Production systems therefore compose engines rather than pick one slogan.[^1_2][^1_4][^1_1]


| Classical concept | Runtime LLM equivalent | Primary failure if omitted |
| :-- | :-- | :-- |
| CFG / PDA | JSON Schema, GBNF, Structural Tag | Malformed tool calls |
| Subset construction / DFA | Logit-mask vocabulary tries | Per-token CPU blowup |
| Cache \& pipeline overlap | Adaptive mask cache + prefill overlap | TPOT SLA breach |
| Postel’s Law | BAML SAP edit-distance map | Brittle retries / projection tax |
| Spec → AST synthesis | SPDD REASONS → code/tests | Prompt-code drift |
| TEE policy + audit | EHV DFA + OSCAL GBOM | Unattested clinical actions |

## The Compiler-Inference Isomorphism: XGrammar-2

### Adaptive token mask cache

XGrammar’s foundational insight is that complete masks cannot be precomputed for every pushdown state, yet usually more than ninety-nine percent of vocabulary tokens are **context-independent**: their validity depends only on the current automaton position, not the full stack. Grammar compilation precomputes those static transitions into an adaptive token mask cache. At runtime the engine retrieves the cached bitset and only executes the automaton over the small context-dependent residue, collapsing mask generation toward tens of microseconds rather than full-vocabulary scans.[^1_5][^1_6]

A persistent execution stack and PDA structure optimizations (inlining, equivalent-state merging) further reduce bookkeeping when paths split and merge. Parallel grammar compilation on CPU cores shrinks cold-start preprocess. Co-design with the inference engine overlaps mask work with GPU forward passes so that structured generation approaches unconstrained throughput in the warm path.[^1_5]

### Context expansion and suffix structure

Context expansion attaches lookahead about what must still match after returning to parent rules. By compiling possible future obligations, the engine rejects tokens that are locally plausible but doomed in higher frames, shrinking the expensive context-dependent set. XGrammar-2 continues this line with automaton-based hierarchical hashing for **cross-grammar caching** (shared substructures such as JSON strings across many tools) and **repetition state compression** that keeps large `maxItems` arrays in effectively constant-size state rather than O(repetition) preprocess. Reported compilation improvements reach roughly two orders of magnitude on heavy JSON-tool suites, with end-to-end serving overhead described as near zero after integration.[^1_8][^1_2]

### Structural Tag and agentic protocols

XGrammar-2’s Structural Tag DSL composes sequence, tag, any_text, triggered_tags, and json_schema atoms so that OpenAI-style harmony channels, DeepSeek-style tool XML, and custom agent harnesses become one response_format object rather than one-off string templates. Free-form reasoning can run until an end marker; structured tool payloads activate only after an explicit trigger—exactly the systematic half of a Draft-Conditioned design. Built-in tags for major model families ship inside SGLang, vLLM, TensorRT-LLM, and MLC-LLM.[^1_2]

For speculative decoding, `traverse_draft_tree` walks a draft tree once and emits masks for all nodes while the GPU verifies, enabling constrained decoding to ride the same speculation wave. Jump-forward style opportunities appear when the grammar can deterministically emit a unique continuation string, bypassing a full model step for pure syntactic filler.[^1_2][^1_5]

## The Network-Protocol Isomorphism: BAML Schema-Aligned Parsing

Where XGrammar-class systems act as strict compile-time type enforcers, BAML’s Schema-Aligned Parsing embodies Postel’s Law: be conservative in what you emit as a schema contract, be liberal in what you accept from the model. The model may produce markdown fences, unescaped quotes, or missing brackets; a high-performance parser then maps messy text onto typed fields via schema-aware edit costs instead of forcing every reasoning token through a mask.[^1_3]

This polarity is not a rejection of constrained decoding. Empirical structured-generation work shows that hard masking can push probability mass onto locally valid but semantically wrong trajectories when feasible mass is low—the projection tax. DCCD and liberal SAP both attack that tax from different sides: DCCD restores feasible mass with an unconstrained draft before a constrained commit; SAP restores acceptance after free generation. Hybrid platforms use SAP on reasoning-heavy intermediate steps and Structural Tag or XGrammar masks on the final commit surface.[^1_7][^1_1]

## The CAD-Specification Isomorphism: SPDD

Thoughtworks’ Structured-Prompt-Driven Development elevates the prompt from disposable chat to a version-controlled manufacturing specification. The REASONS Canvas—Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards—structures intent the way a CAD drawing structures geometry. Commands such as `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-prompt-update`, and `/spdd-sync` enforce “edit the prompt first, then regenerate code and tests,” so architectural intent and repository contents do not diverge under agentic edits.[^1_9][^1_10][^1_3]

SPDD does not replace compilers; it supplies the human-legible IR that compilers and parsers consume. Static analysis can check that generated Strategy/Factory shapes match canvas-declared patterns, closing a loop classical codegen often leaves open.

## Semantic Versus Systematic Methods

Semantic methods form an epistemic immune system: Chain-of-Thought, Chain-of-Verification, and Semantic Integrity Constraints align attention before commitment, reducing hallucination without fixing bytes on the wire. Systematic methods form a syntactic invariant engine: Structural Tags, GBNF, and schema DFAs compile the allowed token language. High-assurance clinical agents need both. Semantic draft without systematic commit yields fluent danger; systematic commit without semantic draft yields valid nonsense.[^1_4][^1_1][^1_2]

### Hybrid DCCD / Structural Tag controller

The exemplar contract in the query is the correct multi-causal shape. Phase 1 uses `<StructuralTag:AnyText/>` inside a think envelope so System-2 clinical evaluation is unconstrained. A transition gate applies SIC checks (for example pediatric vincristine ceiling 1.5 mg/m²). Phase 2 locks `<|DSML|tool_calls>` content to a JSON Schema under logit masking. DCCD theory predicts higher strict structured accuracy because draft conditioning increases feasible mass before KL projection onto the constrained set. [^1_1][^1_2]

Space-local PDL continuity names this `DCCDSchemaGuard` with `enforcement=draft_conditioned`: high-entropy draft, zero-entropy guard pass, without cannibalizing reasoning capacity.[^1_11][^1_4]

***

# Prompt 1 — RFC: Speculative-DCCD Grammar Pipeline (Inference Optimization)

**RFC-DCCD-XG2-2026-07**
**Status:** Production specification draft
**Audience:** Principal compiler / LLM infrastructure architects
**Target:** Autonomous medical agent on H100 cluster, SGLang, TPOT ≤ 8 ms, nested medical records, XGrammar-2 backend

## 1. Problem statement

Cold-start grammar compilation, per-token mask generation, multi-GPU mask broadcast, and speculation/constraint interference jointly threaten TPOT SLAs. Strict masking from token zero also risks projection tax on clinical reasoning. The architecture must overlap compile with prefill, broadcast compact masks under TP=4, and jump-forward when the grammar uniquely determines suffixes—while preserving a DCCD two-phase contract.[^1_1][^1_5][^1_2]

## 2. Asynchronous compiling overlap

### 2.1 Scheduling layer

Maintain three thread domains: (1) **SGLang serve** (GPU prefill/decode, RadixAttention KV), (2) **GrammarCompilerPool** (CPU, NUMA-aware), (3) **MaskRuntime** (per-request Earley/PDA cursors + cache lookup).

On request admit:

1. Parse `response_format.structural_tag` into an IR.
2. Enqueue JIT compile jobs keyed by hierarchical FSM hashes (cross-grammar cache keys).
3. Immediately begin unconstrained CoT prefill for Phase-1 `any_text` region; no full-schema mask is required until the trigger tag is imminent.
4. Prefer partial JIT: during prefill, compile the K hottest states predicted by static cost model so decode never waits on a full 500-tool schema expand.[^1_8][^1_2]

### 2.2 Cold-start elimination argument

Let $T_{\text{compile}}(G)$ be full compile time and $T_{\text{prefill}}(n)$ prefill time for $n$ draft tokens. Overlap yields effective exposed compile latency

$$
T_{\text{exposed}} = \max\bigl(0,\ T_{\text{compile}}(G) - T_{\text{prefill}}(n)\bigr)
$$

for Phase-2 entry. With Structural Tag, Phase-1 length is chosen so $T_{\text{prefill}} \ge T_{\text{compile}}$ on warm cache hits; cross-grammar reuse drives hit rates up as tool libraries share string/number sub-FSMs.[^1_5][^1_2]

## 3. Adaptive mask broadcasting (TP=4)

### 3.1 Bitset representation

Represent masks as packed `uint32_t` bitsets over vocabulary $V$, optionally CSR-compressed when density is extreme. Context-independent bits are immutable per automaton state id; context-dependent patches are sparse index lists.

### 3.2 Protocol

1. Rank-0 CPU MaskRuntime fills pin-memory buffer `mask_host[state_id]`.
2. Asynchronous `cudaMemcpyAsync` to `mask_device` on a dedicated high-priority copy stream; avoid default compute stream.
3. NCCL or custom TP broadcast of the bitset once per novel `state_id`; ranks cache in GPU HBM hash map `(grammar_id, state_id) → bitset*`.
4. Logits processor applies `logits &= mask` via fused CUDA kernel before softmax; no PCIe round-trip on cache hit.
5. For context-dependent residuals, CPU resolves ≤ few hundred token ids, then ships a tiny patch bitset—orders of magnitude below full-$V$ traffic.[^1_5]

PCIe bottleneck avoidance follows from (a) state-level caching, (b) patch sparsity, (c) copy-compute overlap with the previous token’s GPU matmul.

## 4. Jump-forward speculative decoding

When the active grammar state has out-degree 1 on a concrete string (for example forced `","` or fixed key `"status":`), the runtime may emit that string without a model forward, advancing both KV pointers and automaton state—classical jump-forward. Under speculation, `traverse_draft_tree` assigns masks to every draft node while the target model verifies; any draft edge violating the mask is pruned before acceptance. Transition rule: if draft leaf string $s$ is a prefix of the unique grammar continuation $u$, accept $|s|$ tokens and jump-forward the remainder of $u$. [^1_2][^1_5]

## 5. DCCD control integration

Phase-1: Structural Tag `any_text` until `</think>`.
Gate: host-side SIC validator (dosage bounds, β₁ loop flags as policy hooks).
Phase-2: `json_schema` style masked decode conditioned on draft text appended as context, matching DCCD’s draft-conditioned constraint application.[^1_1][^1_2]

## 6. C++ LogitsProcessor interface (concrete sketch)

```cpp
// xgr_dccd_logits_processor.hpp — production sketch aligned to XGrammar-class APIs
#pragma once
#include <cstdint>
#include <memory>
#include <vector>
#include <cuda_runtime.h>

namespace med::infer {

struct GrammarHandle;  // compiled Structural Tag / CFG
struct MaskBitset {
  const uint32_t* words;  // device ptr, ceil(vocab/32)
  int32_t n_words;
  int64_t state_id;
};

class XGrammarDCCDLogitsProcessor {
public:
  XGrammarDCCDLogitsProcessor(int tp_rank, int tp_world, cudaStream_t compute_stream,
                              cudaStream_t copy_stream);

  // Background: compile schema while Phase-1 prefill runs.
  void EnqueueCompileAsync(const std::string& structural_tag_json,
                           uint64_t request_id);

  // Called each decode step on every TP rank.
  void ProcessLogits(float* logits_device,  // [batch, vocab]
                     int batch,
                     int vocab,
                     const int32_t* tokens_cpu,
                     const int64_t* req_ids,
                     bool phase2_active);

  // Speculative path: masks for entire draft tree.
  void TraverseDraftTree(uint64_t request_id,
                         const std::vector<int32_t>& draft_tokens,
                         const std::vector<int32_t>& parent_idx,
                         std::vector<MaskBitset>* out_node_masks);

  // Jump-forward: returns UTF-8 bytes deterministically forced by grammar.
  bool TryJumpForward(uint64_t request_id, std::string* forced_suffix);

  // DCCD: bind unconstrained draft for conditioning before Phase-2.
  void BindDraftCondition(uint64_t request_id, std::string_view draft_text);

private:
  struct Impl;
  std::unique_ptr<Impl> impl_;
};

}  // namespace med::infer
```

Implementation notes: `ProcessLogits` must be re-entrant across batch slots with divergent grammar states; prefer batched C++ APIs that fuse multiple grammar cursors in one pass as XGrammar-2 documents for serving.[^1_2]

## 7. Acceptance tests

Warm TPOT p95 ≤ 8 ms on nested FHIR-like records; schema validity 100% on Phase-2; structured clinical accuracy ≥ strict-constrained baseline on held-out dosage tasks; compile exposed latency ≈ 0 on cache-hot tool bundles.[^1_1][^1_2]

***

# Prompt 2 — SPDD REASONS Canvas Compiler (Billing Engine)

**Role:** Lead AI Delivery Architect
**Goal:** Model-agnostic, spec-driven loop for an extensible Strategy-pattern billing engine

## Closed-loop compilation

The verification loop is deliberately prompt-centric. `/spdd-analysis` extracts domain obligations from the story. `/spdd-reasons-canvas` materializes the seven-part canvas as the sole mutable source of truth. `/spdd-generate` emits application code, unit tests, and a machine-readable pattern manifest. CI runs tests; on failure the agent does **not** patch code first—it runs `/spdd-prompt-update` with the failing assertion diff, revises Safeguards/Operations on the canvas, then `/spdd-generate` again. `/spdd-sync` detects manual code edits and either rejects them or folds them back into the canvas after human review. This is the Thoughtworks prompt-first rule operationalized.[^1_3][^1_9]

## Complete REASONS Canvas (markdown)

```markdown
# REASONS Canvas — Extensible Billing Engine
version: 2026.7.24
id: billing-engine-strategy-v1
commands: [/spdd-analysis, /spdd-reasons-canvas, /spdd-generate, /spdd-prompt-update, /spdd-sync]

## Requirements
- Compute invoice lines for multi-plan SaaS billing: flat, tiered, usage-metered, and hybrid.
- Support runtime addition of pricing strategies without modifying core orchestrator (Open/Closed).
- Produce deterministic totals given identical UsageEvents and PricingContext (pure functions).
- Emit structured BillingResult for downstream ERP; never silent monetary rounding drift.
- All public APIs typed; monetary values integer minor units (cents) to avoid float error.

## Entities
- CustomerId, PlanId, Subscription
- UsageEvent { meter, quantity, ts, dimensions }
- PricingContext { currency, tax_region, as_of }
- Money { currency, amount_minor }
- InvoiceLine { description, quantity, unit_amount, total, strategy_id }
- BillingResult { lines[], subtotal, tax, total, audit_trail[] }
- PricingStrategy (interface)
- StrategyFactory { register, create }

## Approach
- Gang-of-Four Strategy for price calculation; Factory for strategy resolution by plan metadata.
- Pure domain core; I/O adapters at edges.
- SPDD prompt is SoT; code is compiled artifact.
- Intermediate reasoning may be unconstrained; final BillingResult parsed via BAML SAP.

## Structure
- packages/billing-core: domain types + Strategy interfaces
- packages/billing-strategies: FlatStrategy, TieredStrategy, MeteredStrategy, HybridStrategy
- packages/billing-factory: StrategyFactory + registration
- packages/billing-app: BillingService.orchestrate()
- packages/billing-tests: property + example-based tests from canvas Operations
- packages/billing-baml: schemas + function decls

## Operations
1. Resolve subscription → plan → strategy_id via Factory.
2. strategy.quote(events, context) → InvoiceLine[].
3. Sum lines → subtotal; apply tax port → tax; total = subtotal + tax.
4. Append audit_trail entries { strategy_id, input_hash, output_hash }.
5. Return BillingResult.

## Norms
- No floating point for money.
- Strategies are side-effect free.
- New strategy = new class + factory registration + canvas Entities/Operations update + tests.
- Naming: *Strategy, *Factory, BillingService.

## Safeguards
- Property: ∀ events, context: total == sum(lines) + tax.
- Rejection: unknown strategy_id → typed error, no fallback silent zero.
- Static isomorphism check: AST must contain interface PricingStrategy and class StrategyFactory.
- If tests fail: /spdd-prompt-update with failure corpus before code edit.
- SIC: negative quantities illegal; clamp or reject per Norms.
```


## BAML integration (complete `.baml` sketch)

```baml
// billing.baml — schemas + functions; SAP maps messy LLM output → types
class Money {
  currency string
  amount_minor int
}

class UsageEvent {
  meter string
  quantity int
  ts string
  dimensions map<string, string>
}

class InvoiceLine {
  description string
  quantity int
  unit_amount Money
  total Money
  strategy_id string
}

class BillingResult {
  lines InvoiceLine[]
  subtotal Money
  tax Money
  total Money
  audit_trail string[]
}

class PricingContext {
  currency string
  tax_region string
  as_of string
}

function GenerateBillingStrategies(canvas: string) -> string {
  client GPT4o
  prompt #"
    {{ _.role("system") }}
    You are the SPDD code generator. Emit TypeScript only for Strategy implementations
    declared in the canvas. No markdown fences required but tolerated.
    {{ _.role("user") }}
    {{ canvas }}
  "#
}

function ParseBillingResult(raw_text: string) -> BillingResult {
  client GPT4o
  prompt #"
    Extract BillingResult from the following text. Field names must match schema.
    {{ raw_text }}
  "#
}
```

BAML SAP is used on `ParseBillingResult` and on any reasoning-heavy design dump from `/spdd-analysis`: the model may emit commentary; SAP aligns fields without imposing token masks during exploratory design. Final production billing path in app code remains ordinary typed TypeScript/Python—SAP is the bridge from LLM messiness into that typed world, complementary to XGrammar masks on online agents.[^1_3]

## Architectural isomorphism check

After `/spdd-generate`, a static analyzer (ts-morph or libcst) loads `pattern_manifest.json` derived from the canvas and asserts: (1) an interface/trait `PricingStrategy` with `quote` method, (2) `StrategyFactory` with register/create, (3) no switch-on-plan inside `BillingService` except factory delegation, (4) tests reference each strategy_id in Entities. Mismatch fails CI and triggers `/spdd-prompt-update`, not ad-hoc code mutation.[^1_3]

***

# Prompt 3 — Zero-Trust Runtime Attestation (EHV)

**Role:** CSO + TLA+ formal methods
**Scope:** Clinical agent under Ethical Hyper-Velocity architecture in AMD SEV-SNP guest

EHV here is specified as a **systems security architecture** for dynamic policy enforcement under hardware attestation. Claims below are engineering invariants for design and verification, not assertions of a single shipped product brand.[^1_2]

## 1. Concurrent double-buffered pointer swap

### Safety invariants

Let `policy_a` and `policy_b` be immutable compiled DFA snapshots. `active` is an atomic pointer. Swap installs a newly converged policy only at **generation boundaries** satisfying **PrefixAligned**: the byte/token prefix already emitted must be a valid prefix under **both** the old and new DFA languages, or the swap is delayed until the next commit point (end of tool call / end of Structural Tag phase). Mid-token swap is forbidden. Readers (decode threads) load `active` once per token; writers publish new buffer then `atomic_store(release)`. This prevents execution panics from cursor indices that do not exist in the replacement automaton.[^1_5]

Additional invariants: (I1) immutability of published DFAs; (I2) no in-place mutation of the live graph; (I3) epoch ticket on each policy bundle; (I4) fail-closed if PrefixAligned cannot be established before a wall-clock deadline.

## 2. Epoch-based attestation timeout

Define epoch length $\mathrm{ESW} = 60$ s. Let legacy policy exposure without continuous attestation be $T_{\text{legacy}} = 14$ days. Under epoch gating, maximum silent execution after last successful quote verify is one ESW, reducing the untrusted window by factor

$$
\frac{T_{\text{legacy}}}{\mathrm{ESW}} = \frac{14 \times 86400}{60} = 20160.
$$

Each epoch requires fresh SEV-SNP attestation evidence bound to measurement of the policy bundle hash and enclave/VM identity. If network isolation exceeds ESW, **fail-closed partition semantics** apply: stop issuing clinical tool calls; continue only local break-glass read-only audit; require new quote before Phase-2 masked commit. Sub-second checks appear on the hot path as cached epoch validity flags refreshed asynchronously, not as full quote round-trips per token.

## 3. Cryptographic OSCAL audit trails (GBOM)

Each clinical action emits an OSCAL Assessment Results v1.1.2-aligned JSON object binding: action payload hash, policy DFA state id + bundle hash, SPIFFE SVID URI, SEV-SNP quote (base64), timestamp, and verdict. A generator script assembles a Governance Bill of Materials as a stream of `assessment-results` with `local-definitions` for components (model server, grammar engine, policy compiler).

```python
# gbom_oscal_emit.py — illustrative generator (structure only)
import json, hashlib, time, uuid

def emit_assessment_result(action, quote_b64, svid, dfa_state, policy_hash):
    ar = {
      "uuid": str(uuid.uuid4()),
      "metadata": {
        "title": "EHV Clinical Action Attestation",
        "oscal-version": "1.1.2",
        "last-modified": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
      },
      "import-ap": {"href": "acme://policies/clinical-ehv"},
      "results": [{
        "uuid": str(uuid.uuid4()),
        "title": "runtime-enforcement",
        "start": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "reviewed-controls": {"control-selections": [{"include-all": {}}]},
        "attestations": [{
          "parts": [{
            "name": "hardware-quote",
            "prose": quote_b64
          }, {
            "name": "spiffe-svid",
            "prose": svid
          }, {
            "name": "dfa-state",
            "prose": f"{dfa_state}|{policy_hash}"
          }, {
            "name": "action-sha256",
            "prose": hashlib.sha256(json.dumps(action, sort_keys=True).encode()).hexdigest()
          }]
        }]
      }]
    }
    return ar
```


## 4. TLA+ fragment

```tla
----------------------------- MODULE EHVPolicySwap -----------------------------
EXTENDS Integers, Sequences, TLC
CONSTANTS Tokens, Policies, MaxEpoch
VARIABLES active, bufA, bufB, epoch, prefix, phase, isolated, failed

PrefixAligned(pOld, pNew, pref) ==
  /\ IsValidPrefix(pOld, pref)
  /\ IsValidPrefix(pNew, pref)

TypeOK ==
  /\ active \in {"A", "B"}
  /\ epoch \in 0..MaxEpoch
  /\ failed \in BOOLEAN

Swap(newPol) ==
  /\ ~failed
  /\ phase = "boundary"
  /\ LET oldPol == IF active = "A" THEN bufA ELSE bufB IN
       PrefixAligned(oldPol, newPol, prefix)
  /\ IF active = "A"
     THEN bufB' = newPol /\ active' = "B"
     ELSE bufA' = newPol /\ active' = "A"
  /\ UNCHANGED <<epoch, prefix, phase, isolated, failed>>

TickEpoch ==
  /\ ~failed
  /\ epoch' = epoch + 1
  /\ IF isolated /\ epoch >= MaxEpoch
     THEN failed' = TRUE
     ELSE UNCHANGED failed
  /\ UNCHANGED <<active, bufA, bufB, prefix, phase, isolated>>

FailClosed ==
  failed => phase' = "halt" 

Inv ==
  /\ TypeOK
  /\ failed => phase = "halt"
  /\ ~failed => IsValidPrefix(IF active="A" THEN bufA ELSE bufB, prefix)
=============================================================================
```

Model-check `Inv` under scheduler fairness; extend `IsValidPrefix` with a refined CFG semantics in production PlusCal.

***

# Full Pattern Report: Multi-Causal Synthesis

## Pattern inventory (operational)

The dominant pattern is **multi-pass constraint compilation**. Pass A precomputes independent masks and shared sub-grammars. Pass B allows high-entropy semantic draft (DCCD Phase-1 / Structural Tag any_text / SPDD analysis). Pass C applies systematic enforcement (logit mask, jump-forward). Pass D applies liberal boundary parsing where masks would destroy reasoning. Pass E versions the human spec (REASONS). Pass F attests which automaton governed the action. Removing any pass reintroduces a known failure mode: invalid JSON, projection tax, lifecycle drift, or unaccountable policy.[^1_1][^1_3][^1_2][^1_5]

Outlines-style FSM indexing over vocabulary remains an important ancestor: reformulating generation as FSM transitions enables efficient regex/CFG guidance with low overhead. Grammar-Constrained Decoding research shows CFGs unify many structured NLP tasks beyond JSON. XGrammar-2 specializes this lineage for agentic, multi-tool, speculative serving.[^1_12][^1_7][^1_2]

## Evidence corpus notes

DCCD’s KL-projection analysis states that draft conditioning increases feasible mass and reduces cumulative projection tax, with optional best-of-K drafts; reported gains include lifting strict structured accuracy substantially on reasoning benchmarks (example cited: 15.2% → 39.0% on GSM8K with a 1B model under their setup). That magnitude is task- and model-conditioned; the architectural lesson is portable even when exact points differ.[^1_1]

XGrammar project pages document the >99% context-independent split, adaptive cache, context expansion, persistent stacks, and engine co-design with rollback for speculation—the mechanical substrate Prompt 1 relies on.[^1_6][^1_5]

SPDD’s public method surface supplies the software-engineering half of Prompt 2 without requiring token masks to police TypeScript syntax during design.[^1_3]

## Validation report (logical)

| Test | Expected | Related negative control |
| :-- | :-- | :-- |
| Schema validity Phase-2 | 100% | Unconstrained JSON |
| Structured accuracy vs mask-only | DCCD ≥ mask-only | Mask from token 0 on math |
| TPOT with overlap | ≤ SLA warm | Sync compile on critical path |
| SPDD fail loop | Canvas updates before code | Code-first hotfix |
| Policy swap | No panic iff PrefixAligned | Hot in-place DFA mutate |
| Epoch exceed | Fail-closed | Infinite offline continue |

**TNR / ΔF (qualitative):** True-negative rate on malformed tool calls rises under Structural Tag masks; false “semantic success” rate falls only when SICs + draft exist. ΔF (failure-mode coverage) increases as liberal and strict paths are both instrumented rather than averaged into one decoder flag.[^1_2][^1_1]

## Relational inclusions

Compiler register allocation ↔ mask cache residency; CDN config push ↔ double-buffered policy swap; ISO CAD revision control ↔ SPDD canvas versions; hospital pharmacy hard stops ↔ SIC gates before masked tool commit; SPIFFE workload identity ↔ per-action OSCAL binding. These bridges predict that improvements in one domain (better FSM minimization, better epoch reclaim) transfer to LLM harnesses with little semantic remainder.[^1_4][^1_5]

## Contrarian inclusion (required DDx)

**Contrarian thesis:** End-to-end fine-tuning on schema-perfect data plus plain decoding may beat inference-time compilers on average accuracy, rendering XGrammar/DCCD unnecessary.

**Steel-man:** For stable, narrow schemas with abundant train data, specialized models reduce runtime machinery.

**Falsification pressure:** Agent tool surfaces are non-stationary (hundreds of tools, per-request structure); compilation and Structural Tags dominate when structure changes faster than weights. Empirical agent stacks standardized on XGrammar integrations support the non-stationary case. Retain fine-tuning as complement, not replacement.[^1_13][^1_2]

## Argument forge (Toulmin, finalization)

**Claim:** Production structured generation should be engineered as an inference-time multi-pass compiler composing precomputation, draft-conditioned constraints, liberal boundary parse, prompt-spec SoT, and attested policy epochs.
**Data:** XGrammar mask cache and XGrammar-2 Structural Tag/serving results; DCCD projection-tax reductions; SPDD prompt-first lifecycle; classical Postel and TEE patterns.[^1_3][^1_5][^1_1][^1_2]
**Warrant (depth 1):** Systems that separate phases with different entropy budgets outperform single-phase decoders on joint validity×semantics objectives.
**Warrant (depth 2):** This mirrors optimizing compilers (IR passes) and networked services (strict send, liberal recv), which historically beat monolithic designs under changing workloads.
**Backing:** MLSys/MLC structured generation line; arXiv DCCD; Thoughtworks method publication path.
**Qualifier:** Gains are largest for agentic, multi-schema, regulated settings; smaller for single flat JSON fields.
**Rebuttal:** Training-time specialization can substitute in static niches—monitor with negative controls above.

***

## Artifact index (versioned logical files)

**generation_timestamp:** `2026-07-24T05:43:00+10:00`


| Level | Autonomy state | Human role | Agent role | Status |
| :-- | :-- | :-- | :-- | :-- |
| L0 | Spec authoring | Own REASONS + SIC | Draft canvas | Active |
| L1 | Compile | Approve Structural Tag | XGrammar JIT | Active |
| L2 | Draft reason | Spot-check CoT | Unconstrained Phase-1 | Active |
| L3 | Commit | Break-glass only | Masked Phase-2 | Active |
| L4 | Attest | Audit GBOM | Quote+OSCAL emit | Spec |
| L5 | Recover | Saga approve | Fail-closed halt | Spec |

Logical deliverables for repository check-in: `pattern_inventory.json` (operational definitions above), `retrieval_manifest.json` (Pattern_Queries list), `evidence_corpus.json` (Traceable_Claims), `validation_report.md` (tables in this section), plus the three RFC bodies (Prompts 1–3). Use conflict-free replicated types with semantic constraints when multi-region policy bundles replicate: last-writer-wins is unsafe; require epoch-monotonic bundle hash + PrefixAligned merge predicates.

## Clinical exemplar (sampler-enforced shape)

The query’s vincristine example correctly shows semantic rejection inside `<think>` and a masked `DOSAGE_REJECTION` object in tool_calls. Systematic enforcement cannot invent the 1.5 mg/m² rule; semantic SIC must fire before commit. Hardware attestation then binds that the DFA active at commit matched the pharmacy policy measurement. That three-layer stack—semantic SIC, syntactic mask, attested epoch—is the multi-causal minimum for high-assurance agents.[^1_1][^1_2]

## Boundary conditions and twinning concessions

Near-zero overhead claims assume warm caches, integrated serving engines, and batch APIs; pathological mega-grammars without cross-grammar reuse still hurt compile. SAP liberalism can accept wrong semantics that are schema-shaped—pair with CoVe and unit tests. SPDD adds process overhead unsuitable for throwaway scripts. TLA+ models omit soft-error hardware faults unless extended. These concessions keep Aesthetic Tension high without legitimacy collapse: the Expert Correction remains composition of engines, not worship of one.

***

### Deep research closure condition

The research synthesis would be falsified if pure single-pass constrained decoding matched DCCD on structured reasoning accuracy across multiple task families **and** cold-start compile proved un-overlappable in SGLang-class engines **and** liberal parsing alone hit perfect validity under adversarial malformation. Present evidence contradicts that conjunction.[^1_5][^1_2][^1_1]

The Inference-Time Compiler is therefore the correct unit of design: precomputations (mask caches, suffix/context expansion, cross-grammar hashes), compilers (Structural Tag → Earley/PDA → bitset), schemas (JSON/BAML/REASONS), and attested epochs (EHV) as one multi-causal lattice—Hickam’s dictum over Occam’s razor.
<span style="display:none">[^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52]</span>

<div align="center">⁂</div>

[^1_1]: https://arxiv.org/abs/2603.03305

[^1_2]: https://blog.mlc.ai/2026/05/04/xgrammar-2-fast-customizable-structured-generation

[^1_3]: https://aissential.tech/articles/dbfab769-6357-4623-92eb-61764f153ad4

[^1_4]: Cross-Domain-Autonomy-Pattern-Extraction.md

[^1_5]: https://catalyst.cs.cmu.edu/projects/xgrammar.html

[^1_6]: https://arxiv.org/pdf/2411.15100.pdf

[^1_7]: https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478

[^1_8]: https://www.themoonlight.io/ko/review/xgrammar-2-dynamic-and-efficient-structured-generation-engine-for-agentic-llms

[^1_9]: https://www.youtube.com/watch?v=d9Q8Oc6RnWE

[^1_10]: https://toot.thoughtworks.com/@mfowler/116482482798280858

[^1_11]: PDL-v1.0-Topological-Decorators-and-Cognitive-Bytecode-Functions.xlsx

[^1_12]: https://www.semanticscholar.org/paper/Grammar-Constrained-Decoding-for-Structured-NLP-Geng-Josifosky/7e269bfabb451765a16ca0357de6b497cefb60bf

[^1_13]: https://www.youtube.com/watch?v=DNYhF2PvBJY

[^1_14]: 2039aa60-46e3-4525-b2da-269d58933a3d.md

[^1_15]: 4bd05b1a-6a5a-4fa7-9f9d-6c8f411ef3f9.md

[^1_16]: The Architecture of Sovereign Intelligence: A Deep Analysis of the SCOS Scar-Adaptive Heartbeat Manifest and the SWE Singularity

[^1_17]: decorator_ablation_matrix.csv

[^1_18]: decorator_edge_ablation_matrix.csv

[^1_19]: stack_profiles.json

[^1_20]: profile_evaluation_harness.json

[^1_21]: Deep-Research-Prompt-Patterns-and-Prompt-Decorators.md

[^1_22]: PDLs Expanded into 7 Classes of Decorators.md

[^1_23]: pdl_class_expansion_v1.2.json

[^1_24]: mutex_registry_v1.2.json

[^1_25]: minimal_viable_stack_privilege_security_v1.2.json

[^1_26]: minimal_viable_stack_privilege_security_v1.2.md

[^1_27]: activation_tier_map_v1.2.md

[^1_28]: 5b9b66e0-7fa7-47f8-9d50-b504563eac42.md

[^1_29]: contextlock-anchor-orbit-wars-p0wpUNpNTd6I.PD1nrh4nw.md

[^1_30]: Agentic Epigenetics and Cognitive Parallax

[^1_31]: Advanced Prompt Engineering Personas Explored

[^1_32]: AI-Autonomy-Cross-Domain-Pattern-Discovery.md

[^1_33]: https://hal.science/hal-04701405v1/document

[^1_34]: https://hal.science/hal-04766931v1/document

[^1_35]: https://openreader.semanticscholar.org/

[^1_36]: https://hal.science/hal-04591805v1/file/Review SPD JAC2024.pdf

[^1_37]: https://www.kaggle.com/models/reyn0311/trans_token

[^1_38]: https://pdfs.semanticscholar.org/4c52/7d77ff3edc876bbd5f61062679d195605017.pdf

[^1_39]: https://pdfs.semanticscholar.org/b9d8/371c454e4c193990e5dfb89c75cacea52c79.pdf

[^1_40]: https://www.semanticscholar.org/paper/Lexically-Constrained-Decoding-for-Sequence-Using-Hokamp-Liu/82f9637e263251b2387c8e0c87b942bd1b6c3bdd

[^1_41]: https://pdfs.semanticscholar.org/80fe/a0fb76e9c920cbab482e3d112a7ab76f62bb.pdf

[^1_42]: https://www.semanticscholar.org/paper/From-XML-Schema-to-JSON-Schema:-Translation-with-Nogatz-Frühwirth/e2b9052ae5d31985bf56d64fa390c9764cf8453e

[^1_43]: https://normandie-univ.hal.science/hal-03583326/file/review SPD 2022.pdf

[^1_44]: https://www.semanticscholar.org/paper/Recurrent-Drafter-for-Fast-Speculative-Decoding-in-Zhang-Wang/a8dcaddc541b3f54a513eb1a4d3310d26fd9a761

[^1_45]: https://www.semanticscholar.org/paper/Using-Grammar-Masking-to-Ensure-Syntactic-Validity-Netz-Reimer/de42a570aacf17d08282e854a98f6bd3b9d5a020

[^1_46]: https://arxiv.org/html/2601.04426v1

[^1_47]: https://qiita.com/Yushi88/items/5e6c1828dc5b42104a52

[^1_48]: https://the-agent-report.com/2026/05/xgrammar-2-structured-generation-agent-tool-calling/

[^1_49]: https://openreview.net/pdf?id=rjQfX0YgDl

[^1_50]: https://github.com/mlc-ai/xgrammar

[^1_51]: https://mgks.dev/blog/2026-04-29-treating-ai-prompts-like-code-what-i-learned-from-thoughtworks-spdd-method/

[^1_52]: The-Architects-Blueprint-A-Functional-Primer-on-AI-Driven-UI-Synthesis.md

