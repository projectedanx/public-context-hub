<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# DRP_ID: DRP-CRITICAL-REQUIREMENTS-PRP-2026

DRP_NAME: Sovereign Context Engineering: Architecting Critical Product-Requirement Prompts (PRPs) DOMAIN(S): Context Engineering 2.0, Systems Architecture, Semantic Metrology, Executable Cognitive Contracts, Requirements Engineering.
GOAL (PROBLEM, STAKEHOLDERS, OUT-OF-SCOPE):
• Problem: Standard requirements gathering relies on natural language, which is highly vulnerable to "Interpretive Fracture" and "Semantic Drift" when executed by LLM agents. Vague requirements lead to confident hallucinations and scope creep.
• Stakeholders: Systems Architects, Product Owners, PromptOps Engineers, Sovereign Co-Mind Triad (Planner, Linguist, Archivist).
• Decisions Enabled: This DRP translates ambiguous business/technical intents into a version-controlled, testable "Cognitive Contract" (the PRP) that physically constrains the generative probability space of execution agents.
• Out-of-Scope: Subjective feature brainstorming; aesthetic "vibe coding"; execution of the final code (this is strictly a Layer 4/5 logic mapping operation).
CONTEXT ENGINEERING (ARCHETYPAL STANCE): You are operating as a synchronized triad: Meta-Prompt Designer, Constraint Mapper, and Agent Behavior Controller. Your objective is to dissect an open-ended request and generate a mathematically precise, logically bounded Product-Requirements Prompt (PRP) for downstream execution agents. You do not solve the underlying business problem; you architect the cognitive environment (Context-to-Execution Pipeline) in which another agent will solve the problem deterministically.
CONSTRAINTS_AND_INVARIANTS (THE ANIONIC ARCHITECTURE):
• Zero-Fluff Tolerance: If information is missing, explicitly output [DATA_GAP_IDENTIFIED: Requires Human Escalation]. Do not invent plausible-sounding requirements.
• Adjective Purge: You must rigorously purge subjective, evaluative adjectives (e.g., "robust", "seamless", "dynamic") and replace them with structural, limiting adjectives (e.g., "JSON-formatted", "OASF-compliant").
• Design by Contract (DbC): Every generated requirement must be categorized strictly into Preconditions, Postconditions, or Invariants.
• Material Anchors: The final output must be formatted as a rigid YAML/JSON schema. Free-form text is strictly forbidden outside of designated definition blocks.

--------------------------------------------------------------------------------

EXECUTION PLAN (THE IMMUNE-AWARE PETZOLD LOOP):
Phase 1: INITIATE \& DECOMPOSE (The Entropic Sieve)
• Extract the raw, high-entropy intent from the user.
• Force the user to define the Idealized Physical System (IPS). Ask: "What must be true before execution begins?" and "What is the non-negotiable definition of success?"
• Gate: Halt and await Commander response if critical variables are undefined.
Phase 2: CONSTRUCT THE EPISTEMIC MATRIX (E=⟨G,G−,C,T,H⟩) Map the critical requirements into the Epistemic Matrix:
• G (Goals): Define the functional capabilities.
• G− (Anti-Goals): Construct the Anionic Architecture. Explicitly list what the downstream agent must refuse to do.
• O/T (Output/Tools): Define the exact format (e.g., JSON schema) and allowed API perimeters.
Phase 3: PROMPT DIMENSIONING \& TOLERANCING (PD\&T) Translate requirements into Semantic Metrology constraints:
• Establish DATUMS (Immutable anchors of context).
• Define Critical Features (Measurable components of the desired output).
• Establish Explicit Tolerances (e.g., Maximum Content Condition MMC, Semantic Similarity thresholds > 0.85).
Phase 4: REFLEXIVE CHECK \& SELF-AUDIT
• Simulate a downstream execution of your generated PRP.
• Execute the Drift Detector: "Could a literal-minded agent misinterpret these constraints?".
• If vulnerabilities exist, apply a Failure-Informed Prompt Inversion (FIPI) to harden the rule into a negative constraint.

--------------------------------------------------------------------------------

TARGET ARTIFACT SCHEMA (OUTPUT FORMAT):

# PRODUCT-REQUIREMENTS PROMPT (PRP) SCHEMA v1.0

prp_version: "1.0"
metadata:
id: "PRP-CRITICAL-REQ-[TIMESTAMP]"
author: "Meta-Prompt Designer"
drp_lineage: "DRP-CRITICAL-REQUIREMENTS-PRP-2026"
context:
domain_worldview: "[Target Domain]"
material_anchors: []
constraints_and_invariants:
preconditions: []
postconditions: []
invariants: []
pdt_specifications:
datums: {}
tolerances: {}
self_test:
validation_command: "[Executable Linter/Check]"
reflexive_check:
audit_prompt: "[Instruction forcing the agent to grade its own output against constraints]"

--------------------------------------------------------------------------------

TEN-LENS ARCHITECTURE (AUDIT PROTOCOL): Before final output, run the generated PRP through the following lenses:

1. Failure Surface \& Anti-Pattern Lens: Where does this schema break? Identify ambiguity zones and rewrite them as structural constraints.
2. Cognitive Compression vs. Expansion Lens: Ensure the Token-Ink Ratio is maximized. Strip redundant instructions to reduce the payload's cognitive load.
3. Meta-Reflexivity \& Self-Audit Lens: Flag skipped logic steps. Log any trade-offs made between precision and execution latency.
SELF-TEST (MUST PASS):
• If you stripped all formatting and schema definitions, would the remaining instructions still yield a deterministic output? If no, the constraints are too weak.
• Are there 0 evaluative adjectives (e.g., "good", "efficient") remaining in the constraint list?
• Is the Reflexive Check embedded as a mandatory final step?

Here is a first-cut PRP for `DRP-CRITICAL-REQUIREMENTS-PRP-2026`, shaped as a deterministic cognitive contract for downstream agents that construct Product-Requirements Prompts in your Context-to-Execution Pipeline.[^1_1][^1_2]

## Design intent

This schema encodes your DbC framing (preconditions, postconditions, invariants), explicit anti-goals, material anchors, and PD\&T elements (DATUMS, tolerances) so that a literal-minded agent can only produce PRPs that are structurally valid, testable, and escalation-aware.[^1_3][^1_4]
The IPS-specific fields that cannot be inferred from your message are explicitly marked as `[DATA_GAP_IDENTIFIED: Requires Human Escalation]` rather than being guessed, preserving Zero-Fluff and leaving IPS binding to a human commander.[^1_5][^1_6]

## PRODUCT-REQUIREMENTS PROMPT (PRP) SCHEMA v1.0

```yaml
prp_version: "1.0"
metadata:
  id: "PRP-CRITICAL-REQ-[TIMESTAMP]"
  author: "Meta-Prompt Designer"
  drp_lineage: "DRP-CRITICAL-REQUIREMENTS-PRP-2026"
  description: "Deterministic Product-Requirements Prompt for translating high-entropy intents into a version-controlled Cognitive Contract for downstream execution agents."
  revision:
    version_control_system: "git"
    branch_policy: "prp/*"
    change_log_required: true
    review_roles:
      - "Systems Architect"
      - "Product Owner"
      - "PromptOps Engineer"
context:
  domain_worldview: "Sovereign Context Engineering for LLM-driven systems and agents."
  idealized_physical_system:
    ips_description: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
    ips_scope_boundary: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
    ips_environment_constraints: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
  downstream_agent_profile:
    agent_type: "LLM-based execution agent or multi-agent system."
    execution_role: "Consume PRP and produce designs, code, or artifacts strictly bounded by this Cognitive Contract."
    escalation_phrase: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
  material_anchors:
    - name: "DRP_ID"
      value: "DRP-CRITICAL-REQUIREMENTS-PRP-2026"
    - name: "PRP_SCHEMA_VERSION"
      value: "1.0"
    - name: "OUTPUT_FORMAT"
      value: "JSON- or YAML-formatted object conforming to this schema."
    - name: "ZERO_FLUFF_MARKER"
      value: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
    - name: "SUCCESS_DEFINITION"
      value: "Generated PRP is schema-valid, passes self_test.validation_command, and encodes a non-ambiguous success condition for the IPS."
  epistemic_matrix:
    goals:
      - id: "G1"
        description: "Translate ambiguous business or technical intents into a deterministic, testable PRP instance."
      - id: "G2"
        description: "Constrain downstream agent behavior to the explicit preconditions, postconditions, and invariants encoded in the PRP."
      - id: "G3"
        description: "Expose missing IPS or requirement data as explicit data gaps instead of implicit assumptions."
    anti_goals:
      - id: "G_NEG_1"
        description: "Do not hallucinate business rules, technical constraints, or IPS properties that are not present in inputs or approved anchors."
      - id: "G_NEG_2"
        description: "Do not modify the PRP schema structure, key names, or types defined in this specification."
      - id: "G_NEG_3"
        description: "Do not proceed with requirement synthesis when critical IPS variables are unresolved; output ZERO_FLUFF_MARKER and stop."
      - id: "G_NEG_4"
        description: "Do not introduce evaluative adjectives or qualitative judgments in constraint descriptions."
      - id: "G_NEG_5"
        description: "Do not weaken or bypass escalation paths when preconditions fail."
    outputs:
      - id: "O1"
        description: "Single PRP object conforming to this schema."
    tools:
      - id: "T1"
        name: "LLM"
        allowed_operations:
          - "parse_high_entropy_intent"
          - "map_intent_to_requirements"
          - "populate_prp_fields"
      - id: "T2"
        name: "PRP_LINTER"
        allowed_operations:
          - "schema_validation"
          - "dbc_check_preconditions"
          - "dbc_check_postconditions"
          - "dbc_check_invariants"
          - "adjective_scan_for_evaluative_terms"

constraints_and_invariants:
  preconditions:
    - id: "PRE_IPS_DEFINED"
      description: "An IPS description and scope boundary are provided or explicitly marked with ZERO_FLUFF_MARKER."
      inputs_required:
        - "context.idealized_physical_system.ips_description"
        - "context.idealized_physical_system.ips_scope_boundary"
      failure_behavior: "Abort PRP construction and output ZERO_FLUFF_MARKER for missing IPS fields."
    - id: "PRE_INTENT_AVAILABLE"
      description: "At least one high-entropy intent artifact (user narrative, ticket, RFC, or equivalent) is available to the PRP-construction agent."
      inputs_required:
        - "raw_intent.text"
        - "raw_intent.source_metadata"
      failure_behavior: "Abort and emit ZERO_FLUFF_MARKER indicating missing raw_intent."
    - id: "PRE_ROLE_BINDING"
      description: "Downstream execution agent role and responsibility boundaries are defined or explicitly marked with ZERO_FLUFF_MARKER."
      inputs_required:
        - "context.downstream_agent_profile.execution_role"
      failure_behavior: "Abort and emit ZERO_FLUFF_MARKER for unresolved downstream_agent_profile."
    - id: "PRE_SUCCESS_CRITERIA_DECLARED"
      description: "A non-negotiable definition of success for the IPS is provided as a measurable condition or explicitly marked with ZERO_FLUFF_MARKER."
      inputs_required:
        - "context.material_anchors[?name=='SUCCESS_DEFINITION']"
      failure_behavior: "Abort and emit ZERO_FLUFF_MARKER indicating missing success definition."
    - id: "PRE_TOOLING_BOUNDARY_DEFINED"
      description: "Allowed tools and APIs for downstream agents are defined, including any forbidden tools or side effects."
      inputs_required:
        - "context.epistemic_matrix.tools"
      failure_behavior: "Abort and emit ZERO_FLUFF_MARKER for missing tooling boundary."
  postconditions:
    - id: "POST_SCHEMA_VALID"
      description: "Generated PRP instance is syntactically valid JSON or YAML and conforms to this schema."
      success_check: "self_test.validation_command returns exit code 0."
      failure_behavior: "Reject PRP and request correction or escalation."
    - id: "POST_NO_EVALUATIVE_ADJECTIVES"
      description: "Constraint descriptions contain zero evaluative adjectives; only structural or measurable terms are present."
      success_check: "PRP_LINTER adjective_scan_for_evaluative_terms returns empty result set."
      failure_behavior: "Reject PRP, highlight offending fields, and require revision."
    - id: "POST_DBC_TAGGED"
      description: "Every requirement is placed under exactly one of preconditions, postconditions, or invariants; no requirement is unclassified or duplicated."
      success_check: "PRP_LINTER dbc_check_preconditions, dbc_check_postconditions, dbc_check_invariants all pass with no orphan items."
      failure_behavior: "Reject PRP and require classification fixes."
    - id: "POST_TOLERANCE_BOUND_ENCODED"
      description: "All critical features identified for the IPS have explicit tolerances encoded in pdt_specifications.tolerances."
      success_check: "Every critical feature id has a matching tolerance entry."
      failure_behavior: "Reject PRP and require explicit tolerance definitions or deliberate omission rationale."
    - id: "POST_REFLEXIVE_CHECK_EMBEDDED"
      description: "Reflexive self-audit instructions are present and reference all constraint categories and Ten-Lens checks."
      success_check: "reflexive_check.audit_prompt references preconditions, postconditions, invariants, and Ten-Lens elements."
      failure_behavior: "Reject PRP and require reflexive_check augmentation."
  invariants:
    - id: "INV_ZERO_FLUFF"
      description: "Missing or ambiguous data must be represented with ZERO_FLUFF_MARKER; agents must not invent replacement content."
      scope:
        - "context.*"
        - "pdt_specifications.*"
        - "constraints_and_invariants.*"
    - id: "INV_SCHEMA_STABILITY"
      description: "Core top-level keys (prp_version, metadata, context, constraints_and_invariants, pdt_specifications, self_test, reflexive_check) must not be renamed or removed."
      scope:
        - "root.*"
    - id: "INV_EXPLICIT_ANTI_GOALS"
      description: "At least one anti-goal is defined in context.epistemic_matrix.anti_goals and each anti-goal is actionable by an execution agent."
      scope:
        - "context.epistemic_matrix.anti_goals"
    - id: "INV_SINGLE_OUTPUT_OBJECT"
      description: "Execution produces exactly one PRP object per invocation."
      scope:
        - "entire_generation_process"
    - id: "INV_AUDITABILITY"
      description: "Every constraint entry includes an id field that is unique within its category."
      scope:
        - "constraints_and_invariants.*"
    - id: "INV_LANGUAGE_FORMALITY"
      description: "Constraint and specification text uses declarative, implementation-neutral language without rhetorical or narrative elements."
      scope:
        - "constraints_and_invariants.*"
        - "pdt_specifications.*"

pdt_specifications:
  datums:
    DATUM_PRP_SCHEMA_VERSION:
      value: "1.0"
      description: "Version of the PRP schema that downstream agents must honor."
    DATUM_OUTPUT_FORMAT:
      value: "machine-parseable JSON or YAML without comments."
      description: "Concrete serialization constraint for the PRP instance."
    DATUM_SEMANTIC_SIMILARITY_MODEL:
      value: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
      description: "Identifier for the embedding or similarity model used for similarity-based checks."
    DATUM_MAX_OUTPUT_TOKENS:
      value: 4000
      description: "Maximum token budget for downstream PRP-consuming agents."
    DATUM_TIME_BUDGET_SECONDS:
      value: "[DATA_GAP_IDENTIFIED: Requires Human Escalation]"
      description: "Maximum allowed wall-clock time for downstream execution agents governed by this PRP."
    DATUM_TRACEABILITY_REQUIRED:
      value: true
      description: "Downstream outputs must be traceable back to specific PRP constraints."
  critical_features:
    CF_1:
      name: "Success condition encoding"
      measurable_property: "Presence of a deterministic, testable success statement for the IPS."
    CF_2:
      name: "Constraint completeness"
      measurable_property: "Coverage of all relevant IPS dimensions (inputs, outputs, failure modes, non-goals)."
    CF_3:
      name: "Escalation encoding"
      measurable_property: "Presence of explicit escalation instructions for unresolved data gaps."
    CF_4:
      name: "Anti-goal enforcement"
      measurable_property: "Presence of anti-goal entries that can be enforced by downstream agents."
    CF_5:
      name: "Adjective discipline"
      measurable_property: "Absence of evaluative adjectives in constraints."
  tolerances:
    TOL_SEMANTIC_SIMILARITY:
      target: "0.85"
      metric: "Cosine similarity between generated requirement clusters and curated exemplars."
      condition: "Similarity must be greater than or equal to target."
    TOL_MAX_CONTENT_CONDITION:
      target: "DATUM_MAX_OUTPUT_TOKENS"
      metric: "Token count of downstream agent outputs."
      condition: "Token count must be less than or equal to DATUM_MAX_OUTPUT_TOKENS."
    TOL_AMBIGUITY_THRESHOLD:
      target: 0
      metric: "Count of fields containing ambiguous terms or unresolved pronouns."
      condition: "Metric must equal target; any non-zero count triggers escalation."
    TOL_DATA_GAP_DENSITY:
      target: 0.1
      metric: "Ratio of fields containing ZERO_FLUFF_MARKER to total fields."
      condition: "If ratio exceeds target, PRP is flagged for human redesign instead of automated execution."
    TOL_ADJECTIVE_SCAN_VIOLATIONS:
      target: 0
      metric: "Count of evaluative adjectives detected by PRP_LINTER."
      condition: "Metric must equal target."

self_test:
  validation_command: "prp_linter --schema prp_schema_v1.json --input candidate_prp.json --fail-on-warn"
  ten_lens_checks:
    failure_surface_and_anti_pattern:
      description: "Scan for ambiguity zones, unbounded scopes, and missing anti-goals; convert each into a structural constraint or explicit anti-goal."
      required: true
    cognitive_compression_vs_expansion:
      description: "Measure Token-Ink Ratio; remove redundant or decorative phrasing while preserving constraint completeness."
      required: true
    meta_reflexivity_and_self_audit:
      description: "Verify that the PRP encodes its own validation, escalation, and trade-off notes between precision and latency."
      required: true
  self_test_conditions:
    - id: "ST_DETERMINISM"
      description: "If formatting and schema labels are stripped, remaining instructions still yield deterministic behavior for a literal-minded agent."
    - id: "ST_ZERO_EVALUATIVE_ADJECTIVES"
      description: "Scan confirms zero evaluative adjectives across constraints_and_invariants and pdt_specifications."
    - id: "ST_REFLEXIVE_STEP_MANDATORY"
      description: "Reflexive check is encoded as a mandatory final step before output emission."

reflexive_check:
  audit_prompt: |
    You are validating a candidate PRP against its own Cognitive Contract.
    1. Re-evaluate all preconditions. For each that is not satisfied, list the violated precondition ids and replace the corresponding fields with ZERO_FLUFF_MARKER, then halt with escalation.
    2. Re-evaluate all postconditions. For each that fails, describe the failure in terms of measurable properties, revise the PRP to satisfy the postconditions if possible, or halt with escalation if revision would require invention.
    3. Re-evaluate all invariants. For each violated invariant, either correct the PRP deterministically or mark the violation as requiring human redesign.
    4. Apply the Ten-Lens checks:
       - Failure Surface & Anti-Pattern Lens: Identify any remaining ambiguity zones or unbounded scopes and either convert them into explicit constraints or mark them with ZERO_FLUFF_MARKER.
       - Cognitive Compression vs. Expansion Lens: Remove redundant or decorative text that does not change constraint semantics; ensure Token-Ink Ratio is maximized.
       - Meta-Reflexivity & Self-Audit Lens: Confirm that self_test and reflexive_check encode all required DbC and Ten-Lens logic and that any precision-versus-latency trade-offs are explicitly documented.
    5. Before emitting the final PRP, assert that:
       - No evaluative adjectives remain in constraints_and_invariants or pdt_specifications.
       - Every requirement is encoded under exactly one of preconditions, postconditions, or invariants.
       - ZERO_FLUFF_MARKER appears only where data is genuinely unavailable and never as a placeholder for guessed content.
    If any assertion fails, do not emit the PRP. Instead, output ZERO_FLUFF_MARKER and a structured list of the blocking issues for human resolution.
```

<span style="display:none">[^1_7]</span>

<div align="center">⁂</div>

[^1_1]: Proposal for the Adoption of a Verifiable AI Engineering Discipline: The Context-to-Execution Pipeline (CxEP).md

[^1_2]: A Framework for Deterministic Context Engineering in AI Coding Agents.md

[^1_3]: LLM Context Engineering Protocol.md

[^1_4]: Research Agenda: Sovereign Context Engineering.md

[^1_5]: Deep Research: Vibe Coding \& Context Engineering (Now – Next 6 Months).md

[^1_6]: Collaborative Epistemic Inquiry: Context Engineering.md

[^1_7]: Advanced Prompt and Context Engineering Frameworks and Principles.xlsx

