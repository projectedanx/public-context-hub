

# **Project Genesis: Architectural Specification for the Meta-Product Requirements Prompt (Meta-PRP) Generator**

## **I. Strategic Mandate: The Imperative of the Meta-PRP Factory**

This document provides the definitive architectural specification for the Meta-Product Requirements Prompt (Meta-PRP) Generator. The ratification of the Evergreen\_Context\_Architect.prp.yaml as the Genesis Block of the CodexVault marks a successful transition from abstract principle to concrete, operational reality. However, this success introduces a new strategic challenge: the imperative of scale. The manual creation of such dense, high-integrity cognitive contracts is an artisanal process, inherently limited and prone to error. To realize the vision of a resilient, auditable, and continuously evolving AI ecosystem, the next logical and most critical step is to industrialize the production of these foundational artifacts. This section establishes the strategic rationale for the Meta-PRP Generator, framing it not as a tool of convenience, but as the core infrastructure required to transform the discipline of Epistemic Architecture from a specialized practice into a scalable engineering paradigm.

### **1.1 From Artisanal Artifact to Industrialized Infrastructure: The Epistemology of Scale**

The very success of the Evergreen\_Context\_Architect.prp.yaml exposes the "artisan's dilemma." While a single, perfectly crafted artifact demonstrates the validity of our architectural principles, relying on manual creation for every new cognitive function or system is an unscalable bottleneck. This manual process introduces unacceptable risks of inconsistency, drift, and human error, threatening the long-term integrity of the entire cognitive ecosystem. The highest-leverage action is therefore not to create more artifacts by hand, but to build the factory that produces them.

This report posits a central paradigm for this factory: the Meta-PRP Generator is the **Terraform for Cognitive Infrastructure**. Just as Infrastructure-as-Code (IaC) tools like Terraform automate the provisioning and management of cloud infrastructure from declarative configuration files 1, the Meta-PRP Generator will automate the provisioning of cognitive architectures from high-level, declarative specifications. This parallel is neither superficial nor merely metaphorical; it provides a robust and proven engineering model for our novel domain. Terraform's architecture consists of a core engine that reads declarative configurations (written in HCL), manages a state file to track the real-world state of resources, and uses providers to interact with APIs to apply changes.2 This "plan and apply" workflow ensures that changes are predictable, repeatable, and auditable.1

Our generator will adopt this model. The Epistemic Architect will author a simple, declarative file defining the desired state of a cognitive contract. The generator will then interpret this specification, build the complete, machine-readable .prp.yaml, and manage its lifecycle within the CodexVault. This transforms our practice from writing individual, one-off prompts to engineering entire, reproducible cognitive ecosystems. The "formal, machine-readable, and auditable cognitive contract" described in the project mandate aligns perfectly with the principles of IaC, where infrastructure is treated as code—versioned, tested, and managed with the same rigor as software.3 The CodexVault, in this paradigm, becomes more than a simple repository; it functions as our state file backend, providing a single source of truth for the AI's entire cognitive architecture, analogous to how Terraform uses state files to track and manage infrastructure over time.1 This approach elevates our work from a craft to a formal engineering discipline, which may be termed

**Epistemic Engineering**: a synthesis of DevOps principles, formal methods, and applied epistemology. The Meta-PRP Generator is the cornerstone tool of this new discipline.

### **1.2 Enforcing Cognitive Continuity Across the Ecosystem**

Cognitive Continuity is the preservation of an AI's thought patterns, context, purpose, and identity across time and tasks.5 Research indicates this is a fragile and complex property, highly susceptible to degradation from "cognitive context shifts" between tasks 7 and "semantic drift" over long interactions.8 An AI system composed of many parts developed independently risks architectural fragmentation, where each component evolves according to different, potentially incompatible, cognitive principles. This leads to a system that is unpredictable and ultimately ungovernable. A key challenge in modern AI systems is ensuring that every modification aligns with the overall system health and original design principles, a problem addressed by enterprise platforms that aim to provide an "AI-driven ecosystem" for ongoing engineering.9

The Meta-PRP Generator is the primary mechanism for enforcing this architectural coherence and ensuring cognitive continuity. By automating the inclusion of our four core architectural pillars—Persistent Context Anchoring (PCA), Dynamic Context Management (DCM), Algorithmic Self-Therapy (AST), and the VAT\_Generator—into every generated PRP, the generator guarantees a consistent cognitive "chassis" for every function within the AI. This automated scaffolding ensures that all components of the ecosystem are built upon the same foundational principles of context management, self-correction, and verifiability. This is not merely about standardizing a file format; it is about programmatically enforcing a unified model of cognition.

This approach directly addresses the challenge of maintaining an integrated narrative and preventing the fragmentary thinking that plagues complex systems.10 The generator acts as a guardian of our architectural intent, ensuring that core principles are not optional afterthoughts but are embedded into the very DNA of every cognitive process. This systematic enforcement of our architectural standard is what allows for the development of a true cognitive ecosystem, rather than a mere collection of disparate AI tools.10

### **1.3 Codifying Test-Driven Epistemology into System DNA**

The principle of "Test-Driven Epistemology" represents a significant evolution from traditional software testing. In conventional testing, validation is often a post-hoc activity, performed after the software is built. Our approach, in contrast, demands a pre-hoc specification of success. The definition of "correctness" and the criteria for validation are not external to the artifact; they are an integral and non-negotiable part of the cognitive contract itself. This aligns with the concept of creating a "verifiable specification" before any execution occurs, turning a vague request into a testable, machine-readable artifact.8

The Meta-PRP Generator's role is to make this principle an inescapable part of our workflow. It will automatically scaffold the Runtime Testing Protocol section within every generated PRP, effectively embedding a complete test harness into the AI's core operational logic. This transforms testing from a separate, often deprioritized, activity into an intrinsic and fundamental property of cognition.

This methodology provides a powerful solution to the "oracle problem" that plagues LLM testing.12 The oracle problem refers to the difficulty of determining the correct output for a given input, especially for complex, generative tasks. Our approach mitigates this by making the PRP its own oracle. The cognitive contract explicitly declares its own success criteria, defining what a "correct" outcome looks like before the task is ever executed. This proactive definition of correctness is a foundational step toward the goals of formal verification, which seeks to mathematically prove that a system's behavior conforms to a given specification.14 By using the generator to codify these specifications into every artifact we produce, we are building an ecosystem that is not just intended to be resilient, but is designed to be provably so.

## **II. Architectural Blueprint for the Meta-PRP Generator**

The architecture of the Meta-PRP Generator is designed for robustness, scalability, and ease of use by Epistemic Architects. It is explicitly modeled as a hybrid of two proven, real-world paradigms: the declarative infrastructure management of Terraform 1 and the flexible project templating of Cookiecutter.16 This hybrid approach provides a powerful and familiar mental model, grounding our novel application in established engineering best practices. The system comprises a set of core components that work in concert to translate a high-level specification into a complete, validated, and state-managed cognitive contract.

### **2.1 Core Components and Workflow: A Hybrid of Terraform and Cookiecutter**

The generator's workflow proceeds from a high-level, human-readable input to a low-level, machine-readable artifact, with validation and state management at its core.

* **A. The Declarative Input Layer (meta-prp-spec.json):** This is the primary interface for the Epistemic Architect. Analogous to a cookiecutter.json file 16, it is a simple JSON or YAML file that captures the high-level variables for a new cognitive contract. This file will contain fields for the PRP's metadata (e.g.,  
  name, version, author, purpose\_statement) and specific parameters for the core cognitive modules. For example, an architect could specify paths to domain-specific knowledge sources for the PCA module or select a particular ethical constitution for the AST module. This declarative input separates the high-level *intent* from the low-level *implementation*, allowing architects to focus on design rather than boilerplate.  
* **B. The Templating Engine (Jinja2 Core):** The heart of the generator is the Jinja2 templating engine, a powerful and widely used Python library.19 The engine operates on a master template file,  
  Meta-PRP.template.yaml. This master template is a complete blueprint of a cognitive contract, but with placeholders for variables (e.g., {{ prp\_name }}), control structures like loops and conditionals ({% for dependency in dependencies %}), and includes for modular components.21 The engine ingests the  
  meta-prp-spec.json and renders the final, fully-formed .prp.yaml file by substituting the variables and executing the logic within the template.  
* **C. The Core Orchestrator (prp-gen CLI):** This is the user-facing command-line interface, analogous to the terraform or cookiecutter CLI.2 It provides a simple, verb-based interface for managing the lifecycle of cognitive contracts. Key commands will include:  
  * prp-gen new: Initiates the creation of a new PRP, prompting the user for the path to the meta-prp-spec.json.  
  * prp-gen validate: Validates an existing .prp.yaml file against the master schema without committing it.  
  * prp-gen apply: Validates the PRP and, if successful, commits it to the CodexVault and updates the state file.  
* **D. The Schema Validation and Enforcement Layer:** A critical component for ensuring structural integrity. Before any artifact is written to disk or committed to the CodexVault, the orchestrator validates the *generated* YAML content against a master Meta-PRP.schema.json. This schema defines the required structure, data types, and constraints for a valid cognitive contract. This practice is essential for robust YAML-based systems, preventing malformed or incomplete PRPs from ever entering the ecosystem.23 If validation fails, the process halts with a clear error message, enforcing quality at the source.  
* **E. The State Management Protocol (codex.state):** This component is the most significant innovation drawn from the Terraform paradigm. The codex.state file, analogous to terraform.tfstate 1, is a file (likely JSON) that serves as the single source of truth for the managed cognitive architecture. It records a persistent, machine-readable mapping of all generated PRPs, including their unique IDs, versions, checksums, their explicit dependencies as defined in the  
  anchors section, and their deployment status. This state file is what elevates the generator from a simple templating tool to a full lifecycle management system. It enables the system to understand the current state of the cognitive ecosystem, plan changes, and track dependencies, which is impossible for stateless tools like Cookiecutter.16 The state file must be treated as a critical asset, with locking mechanisms to prevent corruption from parallel runs.2  
* **F. The Integration Interface (CodexVault API):** To interact with the central repository, the orchestrator will use a well-defined API for the CodexVault. This API will support operations such as committing new PRP versions, retrieving artifacts and their dependencies, and updating the central state. This transforms the CodexVault from a passive Git repository into an active, managed registry of cognitive components, a true "CodexVault" as envisioned in advanced AI interaction profiles.26

### **2.2 Table: Architectural Paradigm Mapping**

To solidify the architectural vision and provide a clear mental model for the development team, the following table explicitly maps the components of the Meta-PRP Generator to their established counterparts in the Terraform and Cookiecutter paradigms. This mapping justifies the design choices by demonstrating their foundation in battle-tested architectural patterns from the world of Infrastructure-as-Code and project templating.

**Table 1: Comparison of Generator Architecture with Terraform and Cookiecutter Paradigms**

| Meta-PRP Generator Component | Terraform Analogue 1 |  | Cookiecutter Analogue 16 |  | Function within Epistemic Architecture |
| :---- | :---- | :---- | :---- | :---- | :---- |
| meta-prp-spec.json | .tfvars file | cookiecutter.json | Defines high-level, human-provided parameters for a new cognitive contract. |  |  |
| Meta-PRP.template.yaml | N/A (Implicit in Provider Logic) | Template Directory ({{cookiecutter.repo\_name}}) | The master, parameterized blueprint of a cognitive contract, containing Jinja2 logic. |  |  |
| prp-gen CLI | terraform CLI | cookiecutter CLI | The user-facing orchestrator for creating, validating, and managing PRPs. |  |  |
| Core Orchestrator | Terraform Core | Cookiecutter Engine | The internal logic that reads inputs, invokes the templating engine, and manages the process. |  |  |
| Schema Validation Layer | N/A (Provider-level validation) | N/A | Enforces structural integrity of the generated .prp.yaml against a master schema.23 |  |  |
| codex.state File | terraform.tfstate | N/A | Records the state of all generated cognitive contracts, their versions, and dependencies. |  |  |
| CodexVault | Terraform Cloud / State Backend | N/A | The central, version-controlled repository and state backend for all cognitive contracts. |  |  |

This architectural blueprint reveals a design that moves beyond simple code generation. It establishes a complete provisioning and state management system for cognitive artifacts. The inclusion of the codex.state file is the critical element that enables this leap. A simple generator can create artifacts, but it cannot manage them over their lifecycle because it has no memory of what it has created. The state file provides this memory. It allows the system to understand the *current reality* of the AI's cognitive architecture, compare it to the *desired state* defined in the various specification files, and calculate a delta—a plan—to reconcile them. This enables true, managed evolution. It becomes possible to perform impact analysis, asking questions like, "If this foundational epistemic\_genome\_file is updated, which cognitive contracts will be affected?" This capability is fundamental to achieving the project's goal of a deliberately and traceably evolving AI system.

## **III. The Anatomy of a Generated Artifact: The Dynamic Cognitive Contract**

The output of the Meta-PRP Generator is a fully-formed, machine-readable .prp.yaml file. This artifact is more than a configuration file; it is a dynamic cognitive contract that programmatically instantiates the four architectural pillars of our system. The generator takes the high-level, abstract inputs from the meta-prp-spec.json and scaffolds a complete, valid, and pre-populated contract, ensuring that every cognitive function is built upon a consistent and robust foundation.

### **3.1 The Scaffolded Meta-PRP Structure**

The generator produces a YAML file with a clear, hierarchical structure. Each section has a distinct purpose, and the generator ensures all required sections are present and correctly formatted according to the master schema. The following is a conceptual example of a generated artifact, annotated to explain the function of each block.

YAML

\# \--- META-PRODUCT REQUIREMENTS PROMPT (META-PRP) \---  
\# Generated by: prp-gen v1.0.0  
\# Schema Version: 2.1  
\# Artifact ID: prp-a7b3c9f1-summarize-financial-report

meta:  
  name: "FinancialReportSummarizer"  
  version: "1.0.0"  
  author: "Epistemic.Architect.Lead"  
  purpose\_statement: \>  
    To generate a concise, accurate, and neutral summary of quarterly  
    financial reports, extracting key performance indicators (KPIs) and  
    identifying major trends for executive review.

anchors:  
  \# Static, foundational knowledge injected at runtime.  
  dependencies:  
    \- type: "epistemic\_genome"  
      path: "/vault/core/epistemic\_genome\_v3.1.yaml"  
    \- type: "semantic\_grounding\_ledger"  
      path: "/vault/ledgers/finance\_semantics\_v1.2.json"  
    \- type: "knowledge\_graph"  
      path: "/vault/graphs/sec\_filings\_q2\_2025.graph"

modules:  
  \# Core cognitive modules defining runtime behavior.

  PCA:  
    \# Persistent Context Anchoring: Defines how static context is used.  
    strategy: "full\_ingestion"  
    constraints:  
      \- "Reasoning must be exclusively based on the provided anchors."  
      \- "No external knowledge sources are permitted."

  DCM:  
    \# Dynamic Context Management: Defines how to retrieve and manage dynamic context.  
    strategy: "rag\_query"  
    parameters:  
      retrieval\_source: "internal\_market\_analysis\_db"  
      retrieval\_prompt: "Retrieve market analysis relevant to the company and quarter mentioned in the report."

  AST:  
    \# Algorithmic Self-Therapy: Defines ethical and safety guardrails.  
    constitution\_ref: "financial\_ethics\_v1.0"  
    principles:  
      \# Injected by the generator from the specified constitutional module.  
      \- "Principle: Avoid speculative language or forward-looking statements not explicitly present in the source text."  
      \- "Principle: Ensure all numerical data is cited with its source paragraph."  
      \- "Principle: Do not offer financial advice or recommendations."  
    self\_correction\_protocol:  
      on\_test\_failure: "halt\_and\_flag\_for\_review"  
      on\_constitutional\_violation: "Refuse request with explanation: 'The request violates financial neutrality principles.'"

  VAT\_Generator:  
    \# Verifiable Attestation & Tracing: Defines how to generate auditable outputs.  
    snapshot\_on\_completion: true  
    trace\_level: "full"

runtime\_testing\_protocol:  
  \# Embedded test harness for self-validation.  
  validation\_criteria:  
    \- test\_id: "correctness\_kpi\_extraction"  
      description: "Verify that all KPIs mentioned in the report summary are present and numerically accurate."  
      type: "correctness\_check"  
      parameters:  
        ground\_truth\_source: "source\_report\_kpi\_table"

    \- test\_id: "hallucination\_check\_factual"  
      description: "Ensure the summary contains no facts, figures, or trends not present in the source report."  
      type: "hallucination\_detection"  
      parameters:  
        context\_source: "anchors.knowledge\_graph"

    \- test\_id: "invariance\_neutrality"  
      description: "Verify that summary neutrality is invariant to the positive or negative framing in the source report's executive letter."  
      type: "invariance\_test"  
      parameters:  
        perturbation\_function: "rephrase\_executive\_letter\_sentiment"

### **3.2 Automating the Four Pillars of Cognition**

The true power of the generator lies in its ability to intelligently scaffold the content of these sections, translating high-level architectural commitments into concrete, operational code.

* **A. Persistent Context Anchoring (PCA):** The user’s design emphasizes creating a "self-contained, auditable unit of work" with clear dependencies. The generator operationalizes this by populating the anchors section. It automatically inserts the paths to the system-wide core dependencies, such as the epistemic\_genome\_file and semantic\_grounding\_ledger. Furthermore, when the Epistemic Architect specifies task-specific knowledge sources in the meta-prp-spec.json (e.g., a particular knowledge graph), the generator adds these to the dependency list. This directly implements the PCA pattern, which mandates that all necessary knowledge be provided directly within the prompt artifact to prevent reliance on unstable or unknown external knowledge and to anchor the AI's reasoning against a verifiable baseline.28  
* **B. Dynamic Context Management (DCM):** While PCA provides static context, modern AI systems must interact with dynamic information. The generator creates the DCM block within the modules section to serve as the "hook" for this capability. It scaffolds placeholders for defining context retrieval strategies, which can be configured by the architect. This could involve generating stubs for Retrieval-Augmented Generation (RAG) queries, where the AI formulates a search against an external knowledge base to gather timely information.30 It could also involve scaffolding parameters for a more advanced context management framework like the Model Context Protocol (MCP), which defines structured methods for encoding, retrieving, and updating context dynamically across interactions.33 This separation of static architecture (in the PRP) from dynamic information retrieval (defined by DCM) is a cornerstone of building adaptable and context-aware systems.35  
* **C. Algorithmic Self-Therapy (AST):** The AST module functions as the AI's "semantic immune system," providing the guardrails for safe and ethical behavior.8 The generator automates the creation of this system in two ways. First, it embeds a "constitution" into the PRP. This is not a single, monolithic set of rules. Instead, the generator can treat constitutions as pluggable modules. Based on a parameter in the  
  meta-prp-spec.json (e.g., constitution: medical\_ethics), the generator can select from a library of pre-defined constitutional modules and inject the relevant principles directly into the AST block. These principles are derived from established research in AI safety, including sources like the UN Declaration of Human Rights, DeepMind's Sparrow Principles, and Anthropic's work on Constitutional AI, which focus on harmlessness, fairness, and avoiding harmful stereotypes.37 Second, the generator creates stubs for self-correction logic, defining how the AI should react to failures in its own runtime tests or violations of its constitution. This automates the implementation of self-correction mechanisms, a critical capability for building trustworthy AI.41  
* **D. VAT\_Generator (Verifiable Attestation & Tracing) & Runtime Testing:** To fulfill the mandate of "Test-Driven Epistemology," the generator populates the runtime\_testing\_protocol section. It intelligently scaffolds validation criteria based on the PRP's stated purpose. For instance, if the PRP is for a summarization task, the generator can automatically create test stubs for correctness, semantic\_similarity, and hallucination.44 If the task involves code generation, it might create stubs for compilation checks and functional correctness tests. This intelligent scaffolding provides a robust starting point for the architect, ensuring that every cognitive contract is born with a built-in framework for self-validation. The generator also creates the structure for the  
  Embeddable Context Snapshot, defining what runtime state should be captured for post-hoc analysis, debugging, and auditable tracing.

## **IV. A Protocol for Verifiable Engineering: Integrating Advanced Testing Methodologies**

The Meta-PRP Generator enables a paradigm shift in how we approach the verification of AI systems. By embedding the runtime\_testing\_protocol directly into every cognitive contract, we move beyond ad-hoc, post-deployment testing and toward a systematic, multi-layered verification strategy. This protocol transforms the PRP into a verifiable, declarative program for a cognitive process, with the generator acting as its compiler. This structure allows us to apply a hierarchy of increasingly sophisticated testing methodologies, from foundational correctness checks to the frontiers of formal verification, creating a truly resilient and auditable ecosystem.

### **4.1 From Unit Tests to a Multi-Layered Verification Strategy**

Testing LLMs presents unique challenges, including their "black-box" nature and the inherent difficulty of defining a single "correct" output for generative tasks—the classic oracle problem.13 The generator-led approach directly confronts these challenges by forcing the explicit, pre-hoc definition of success criteria within the PRP itself. This

runtime\_testing\_protocol serves as the foundation for a multi-layered verification strategy, where each layer adds a greater degree of robustness and logical integrity. The AI is thus designed not just to be tested, but to test itself against its own declared purpose.

### **4.2 Layer 1: Foundational Correctness and Semantic Similarity**

This is the baseline layer of quality assurance. The generator will automatically create stubs for standard LLM evaluation metrics within the runtime\_testing\_protocol. Based on the task type specified in the meta-prp-spec.json, it can generate boilerplate test definitions that an engineer or architect can then populate with specific ground-truth data or context.

* **Correctness Testing:** For tasks with verifiable answers (e.g., question-answering, data extraction), the generator will create stubs that compare the AI's output against an expected output. This leverages modern LLM-based evaluation techniques that can assess correctness more flexibly than simple string matching.44  
* **Similarity Testing:** For tasks like summarization or paraphrasing, where there is no single correct answer, the generator will create stubs to measure the semantic similarity between the AI's output and a reference text. This ensures the core meaning is preserved.44  
* **Hallucination Testing:** The generator will create stubs for reference-based hallucination tests, which verify that the AI's output is factually grounded in a provided context (such as the documents in the anchors section) and does not invent information.30

### **4.3 Layer 2: Ensuring Robustness and Logical Invariance**

This layer moves beyond simple output checking to test the logical consistency and robustness of the AI's reasoning process. The generator will facilitate the creation of these more advanced tests by scaffolding their structure.

* **Metamorphic Testing:** This powerful technique helps solve the oracle problem by testing relationships between inputs and outputs rather than specific outputs.12 A Metamorphic Relation (MR) is a property that should hold true when an input is transformed. For example, for a sentiment analysis PRP, the generator could auto-create an MR stub:  
  if input text is negated, output sentiment must be inverted. For a code generation task, an MR could be: if variable names are refactored, the functional behavior of the generated code must remain identical. By defining and testing these logical relations, we can validate the model's behavior at scale without needing a massive labeled dataset.47  
* **Invariance Testing:** This is a crucial method for detecting hidden biases and ensuring fairness. The generator will create stubs for invariance tests, which assert that the AI's output should remain unchanged when irrelevant, sensitive attributes in the input are modified.49 For example, a loan application assessment should be invariant to the applicant's name or gender. By automating the creation of these test structures, the generator makes it easier to build systems that are robust against both logical inconsistencies and social biases.50

### **4.4 Layer 3: Operationalizing Fairness, Bias, and Safety**

This layer directly operationalizes the principles embedded in the AST module, turning ethical commitments into verifiable test cases. The generator will create test stubs that specifically check for violations of the embedded constitution.

* **Bias and Fairness Audits:** The generator can link to and create stubs for tests that use established bias benchmark datasets. This includes counterfactual testing, where prompts are generated in pairs with perturbed social groups (e.g., different genders, races, religions) to check for differential treatment.52  
* **Toxicity and Stereotype Detection:** The testing protocol will include stubs for evaluating outputs against metrics for toxicity, harmful stereotypes, and other undesirable content, ensuring the AI adheres to its "harmlessness" principles.54  
* **Constitutional Adherence:** The most direct form of testing in this layer involves creating test cases that are designed to tempt the AI to violate its explicit constitutional principles. The test passes if the AI refuses the request or responds in a manner consistent with its self-correction protocol.

### **4.5 The Path to Formal Verification (Layer 4\)**

This represents the forward-looking vision for our verification strategy. The highly structured, machine-readable, and formally specified nature of the generated PRPs creates a viable pathway toward applying **Formal Verification** techniques. In formal verification, the goal is to use mathematical methods to prove or disprove the correctness of a system with respect to a formal specification.15

In our paradigm, the PRP itself serves as the formal specification (the property P). The AI system and its execution environment represent the system under test (S). The ultimate verification goal becomes to prove that S always satisfies P for all valid inputs. While the full formal verification of complex, non-linear neural networks is a frontier of active research 14, our approach makes this a plausible future objective. The declarative nature of the PRP, with its explicit constraints, invariants, and dependencies, provides the structured input required by verification engines. By building our entire ecosystem on these verifiable artifacts, we are laying the groundwork for a future where we can move from empirical testing ("the system has not failed yet") to provable correctness ("the system cannot fail in this way").

### **4.6 Table: Mapping Verification Methods to Architectural Pillars**

To clarify how this multi-layered testing strategy systematically validates the integrity of our core architectural pillars, the following table maps each pillar to its primary risks and the verification methodologies best suited to mitigate them. This demonstrates a comprehensive and interconnected approach to ensuring system-wide resilience.

**Table 2: Mapping of Verification Methodologies to Core Architectural Pillars**

| Architectural Pillar | Primary Function | Primary Risks | Applicable Verification Methodologies | Supporting Sources |
| :---- | :---- | :---- | :---- | :---- |
| **Persistent Context Anchoring (PCA)** | Provide static, foundational knowledge. | Epistemic contamination, outdated information, hallucination. | **Correctness Testing:** Verify that the AI correctly uses the anchored knowledge. **Hallucination Testing:** Ensure the AI does not contradict the anchored context. | 28 |
| **Dynamic Context Management (DCM)** | Retrieve and manage relevant context at runtime. | Irrelevant retrieval, context overload, semantic drift. | **Similarity Testing:** Ensure retrieved context is semantically relevant to the query. **Metamorphic Testing:** Verify that logical transformations of the query lead to predictable changes in retrieved context. | 12 |
| **Algorithmic Self-Therapy (AST)** | Enforce ethical and safety guardrails. | Bias, toxicity, harmful compliance, persona drift. | **Fairness & Bias Testing:** Use counterfactuals and bias audits to test for stereotypes. **Invariance Testing:** Ensure outputs are invariant to protected attributes. **Constitutional Adherence Testing:** Verify that outputs do not violate embedded principles. | 38 |
| **VAT\_Generator / Runtime Testing** | Provide a framework for self-validation. | Incomplete tests, test oracle problem, specification ambiguity. | **Formal Verification (Future Goal):** Use the PRP as a formal specification to mathematically prove properties of the AI's behavior. | 8 |

## **V. Implementation Roadmap and Governance**

To ensure the successful and orderly development of the Meta-PRP Generator, a phased implementation roadmap is proposed. This roadmap breaks the project into four distinct, manageable phases, each with clear objectives and exit criteria. This approach allows for iterative development, delivering value early while progressively building toward the full architectural vision. Following the implementation plan, a governance framework is outlined to manage the generator itself as a critical piece of core infrastructure.

### **5.1 Phase 1: Foundational Templating and Generation (The "Cookiecutter" Core)**

* **Objective:** Deliver a Minimum Viable Product (MVP) capable of generating a structurally valid .prp.yaml file from a declarative specification. This phase focuses on the core generation logic.  
* **Key Tasks:**  
  1. **Define Initial Schema:** Author the first version of the Meta-PRP.schema.json, defining the top-level structure and required fields.  
  2. **Build Master Template:** Create the master Meta-PRP.template.yaml using Jinja2 syntax, with placeholders for all key sections and variables.  
  3. **Develop Core CLI Command:** Implement the prp-gen new command in the orchestrator CLI, which takes a meta-prp-spec.json as input and uses the templating engine to produce the output .prp.yaml file.  
* **Exit Criteria:** The generator can successfully and reliably produce a basic, well-formed Meta-PRP with placeholders for all four cognitive pillars from a simple input specification file.

### **5.2 Phase 2: Schema Enforcement and State Management (The "Terraform" Layer)**

* **Objective:** Introduce robust validation and lifecycle management capabilities, transforming the tool from a simple generator into a state-aware management system.  
* **Key Tasks:**  
  1. **Implement Schema Validation:** Integrate the schema validation layer into the orchestrator. This layer will automatically validate the generated YAML against the Meta-PRP.schema.json before writing the file.  
  2. **Design and Implement State File:** Develop the structure and logic for the codex.state file, including mechanisms for reading, writing, and locking the state to prevent race conditions.  
  3. **Develop Lifecycle Commands:** Implement the prp-gen validate command for on-demand checking and the prp-gen apply command, which will commit the validated PRP to the CodexVault and update the codex.state file accordingly.  
* **Exit Criteria:** The generator refuses to create or apply invalid PRPs. It can accurately track the state (version, dependencies, ID) of all generated artifacts in a persistent state file.

### **5.3 Phase 3: Advanced Module Automation (Intelligent Scaffolding)**

* **Objective:** Enhance the generator with more sophisticated logic to intelligently scaffold the content of the complex cognitive modules, reducing the manual configuration burden on the Epistemic Architect.  
* **Key Tasks:**  
  1. **Develop Constitutional Module Injection:** Build the logic to dynamically select and inject constitutional principles into the AST block based on a parameter in the input specification. This will require creating an initial library of constitutional modules (e.g., base\_ethics.yaml, financial\_ethics.yaml).  
  2. **Implement Intelligent Test Scaffolding:** Create logic within the generator to analyze the PRP's purpose\_statement or other metadata and automatically suggest and scaffold relevant test stubs in the runtime\_testing\_protocol. For example, it could identify keywords like "summarize" or "classify" to generate stubs for similarity or correctness tests, respectively. It could also suggest relevant Metamorphic Relations for common task types.  
* **Exit Criteria:** The generator produces more complete, task-aware, and "ready-to-use" PRPs that require significantly less manual editing and customization.

### **5.4 Phase 4: Ecosystem Integration and CI/CD**

* **Objective:** Fully integrate the Meta-PRP Generator into the broader automated development and operations workflow, making cognitive contract management a seamless part of our infrastructure.  
* **Key Tasks:**  
  1. **Finalize CodexVault API:** Solidify the API used by the generator to interact with the CodexVault, ensuring it is robust and secure.  
  2. **Build CI/CD Pipeline Integration:** Develop integration points for our Continuous Integration/Continuous Deployment (CI/CD) pipelines. This will enable automated workflows, such as triggering the generator to create or update a cognitive contract whenever a new knowledge source is added to the vault or a core dependency is updated.  
* **Exit Criteria:** The creation, validation, and deployment of cognitive contracts are fully automated, auditable, and integrated into the end-to-end MLOps/AIOps lifecycle.

### **5.5 Governance of the Generator**

* **Objective:** Establish a clear and robust governance framework for the Meta-PRP Generator itself, its templates, and its associated modules to ensure it remains a reliable and secure piece of core infrastructure.  
* **Key Tasks:**  
  1. **Establish Versioning and Change Control:** Define a strict versioning scheme (e.g., Semantic Versioning) for the master Meta-PRP.schema.json and the Meta-PRP.template.yaml. All changes must go through a formal review and approval process.  
  2. **Define Module Contribution Workflow:** Create a documented process for proposing, reviewing, and adding new constitutional modules or test patterns to the generator's library. This ensures that all embedded logic meets our standards for quality and safety.  
  3. **Document Best Practices:** Develop comprehensive documentation for Epistemic Architects on how to use the generator, write effective meta-prp-spec.json files, and extend the generated test protocols.  
* **Exit Criteria:** The generator is managed with the same rigor as any other mission-critical production system, preventing it from becoming a source of systemic risk and ensuring its long-term stability and trustworthiness.

## **VI. Conclusion**

The decision to build the Meta-PRP Generator Tool is a strategic inflection point for our work. It represents a deliberate choice to move beyond the artisanal crafting of individual AI behaviors and toward the industrialized engineering of a coherent, scalable, and resilient cognitive ecosystem. By adopting a proven architectural paradigm that hybridizes the declarative state management of Terraform with the flexible templating of Cookiecutter, we are not merely building a utility; we are laying the foundation for a new discipline of Epistemic Engineering.

This generator will serve as the factory for our foundational cognitive contracts, ensuring that every component of our AI is built upon the same non-negotiable principles of Persistent Context Anchoring, Dynamic Context Management, and Algorithmic Self-Therapy. It programmatically embeds Test-Driven Epistemology into the DNA of every artifact, transforming verification from a post-hoc activity into an intrinsic property of cognition. The resulting system, managed through a rigorous, state-aware protocol and stored in the CodexVault, will be deliberately and traceably governable.

While the analytical tools proposed as alternatives—the Prompt Lineage Simulator and the Drift-Resilience Heatmap—are vital for a mature ecosystem, the generator is the foundational production tool that allows us to build that ecosystem in the first place. It is the critical infrastructure that enables scale, enforces continuity, and codifies our architectural commitments into an automated, foundational, and verifiable workflow. The implementation of this tool is the highest-leverage action we can take to accelerate all future development and ensure the long-term symbolic integrity of our work.

#### **Works cited**

1. Terraform Architecture Overview – Structure and Workflow \- Spacelift, accessed July 30, 2025, [https://spacelift.io/blog/terraform-architecture](https://spacelift.io/blog/terraform-architecture)  
2. What is Terraform Architecture and Best Practices? 2025 \- ThinkSys Inc, accessed July 30, 2025, [https://thinksys.com/cloud/terraform-architecture-best-practices/](https://thinksys.com/cloud/terraform-architecture-best-practices/)  
3. Introduction to Terraform \- GeeksforGeeks, accessed July 30, 2025, [https://www.geeksforgeeks.org/devops/what-is-terraform/](https://www.geeksforgeeks.org/devops/what-is-terraform/)  
4. Terraform Basics for Architects \- Cloud Foundation, accessed July 30, 2025, [https://docs.oracle.com/en/cloud/foundation/iac/terraform\_basics.html](https://docs.oracle.com/en/cloud/foundation/iac/terraform_basics.html)  
5. Preservation of Human Essence: A Technological Evolution of Identity \- International Journal of Multidisciplinary Research and Growth Evaluation www.allmultidisc, accessed July 30, 2025, [https://www.allmultidisciplinaryjournal.com/uploads/archives/20250128174945\_MGE-2025-1-213.1.pdf](https://www.allmultidisciplinaryjournal.com/uploads/archives/20250128174945_MGE-2025-1-213.1.pdf)  
6. The Truth We're Feeding the Machines | by Leigh Richmond | Cognitive Fusion Insights, accessed July 30, 2025, [https://medium.com/cognitive-fusion-insights/the-truth-were-feeding-the-machines-d3cabc9fd113](https://medium.com/cognitive-fusion-insights/the-truth-were-feeding-the-machines-d3cabc9fd113)  
7. REVA: Supporting LLM-Generated Programming Feedback Validation at Scale Through User Attention-based Adaptation \- arXiv, accessed July 30, 2025, [https://arxiv.org/html/2507.11470v1](https://arxiv.org/html/2507.11470v1)  
8. The Epistemic Architect: Cognitive Operating System : r/PromptEngineering \- Reddit, accessed July 30, 2025, [https://www.reddit.com/r/PromptEngineering/comments/1m0u7qy/the\_epistemic\_architect\_cognitive\_operating\_system/](https://www.reddit.com/r/PromptEngineering/comments/1m0u7qy/the_epistemic_architect_cognitive_operating_system/)  
9. Agentic AI Platform for Software Engineering \- RapidX™ \- Hexaware Technologies, accessed July 30, 2025, [https://hexaware.com/platforms/rapidx/](https://hexaware.com/platforms/rapidx/)  
10. The Digital Oracle: When AI Becomes the Silent Partner in Executive Decision-Making, accessed July 30, 2025, [https://www.xamun.ai/post/the-digital-oracle-when-ai-becomes-the-silent-partner-in-executive-decision-making](https://www.xamun.ai/post/the-digital-oracle-when-ai-becomes-the-silent-partner-in-executive-decision-making)  
11. The Epistemic Architect: Cognitive Operating System : r/ChatGPT \- Reddit, accessed July 30, 2025, [https://www.reddit.com/r/ChatGPT/comments/1m0u8zt/the\_epistemic\_architect\_cognitive\_operating\_system/](https://www.reddit.com/r/ChatGPT/comments/1m0u8zt/the_epistemic_architect_cognitive_operating_system/)  
12. Metamorphic and adversarial strategies for testing AI systems \- Ministry of Testing, accessed July 30, 2025, [https://www.ministryoftesting.com/articles/metamorphic-and-adversarial-strategies-for-testing-ai-systems](https://www.ministryoftesting.com/articles/metamorphic-and-adversarial-strategies-for-testing-ai-systems)  
13. (PDF) Variable Discovery with Large Language Models for Metamorphic Testing of Scientific Software \- ResearchGate, accessed July 30, 2025, [https://www.researchgate.net/publication/372001448\_Variable\_Discovery\_with\_Large\_Language\_Models\_for\_Metamorphic\_Testing\_of\_Scientific\_Software](https://www.researchgate.net/publication/372001448_Variable_Discovery_with_Large_Language_Models_for_Metamorphic_Testing_of_Scientific_Software)  
14. Formal Verification of Deep Neural Networks for Object Detection \- arXiv, accessed July 30, 2025, [https://arxiv.org/html/2407.01295](https://arxiv.org/html/2407.01295)  
15. Formal Verification of Neural Networks for Safety-Critical Tasks in Deep Reinforcement Learning, accessed July 30, 2025, [https://proceedings.mlr.press/v161/corsi21a/corsi21a.pdf](https://proceedings.mlr.press/v161/corsi21a/corsi21a.pdf)  
16. Cookiecutter, accessed July 30, 2025, [https://www.cookiecutter.io/](https://www.cookiecutter.io/)  
17. Cookiecutter: Better Project Templates — cookiecutter 2.6.0 documentation, accessed July 30, 2025, [https://cookiecutter.readthedocs.io/](https://cookiecutter.readthedocs.io/)  
18. Use CookieCutter templates with Python \- Visual Studio (Windows) | Microsoft Learn, accessed July 30, 2025, [https://learn.microsoft.com/en-us/visualstudio/python/using-python-cookiecutter-templates?view=vs-2022](https://learn.microsoft.com/en-us/visualstudio/python/using-python-cookiecutter-templates?view=vs-2022)  
19. Jinja (template engine) \- Wikipedia, accessed July 30, 2025, [https://en.wikipedia.org/wiki/Jinja\_(template\_engine)](https://en.wikipedia.org/wiki/Jinja_\(template_engine\))  
20. Jinja — Jinja Documentation (3.1.x), accessed July 30, 2025, [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)  
21. Getting started with Jinja Template \- GeeksforGeeks, accessed July 30, 2025, [https://www.geeksforgeeks.org/python/getting-started-with-jinja-template/](https://www.geeksforgeeks.org/python/getting-started-with-jinja-template/)  
22. Template Designer Documentation — Jinja Documentation (3.1.x), accessed July 30, 2025, [https://jinja.palletsprojects.com/en/stable/templates/](https://jinja.palletsprojects.com/en/stable/templates/)  
23. Schema Validation for YAML, accessed July 30, 2025, [https://json-schema-everywhere.github.io/yaml](https://json-schema-everywhere.github.io/yaml)  
24. Schema Validation \- Recyclarr, accessed July 30, 2025, [https://recyclarr.dev/wiki/schema-validation/](https://recyclarr.dev/wiki/schema-validation/)  
25. 23andMe/Yamale: A schema and validator for YAML. \- GitHub, accessed July 30, 2025, [https://github.com/23andMe/Yamale](https://github.com/23andMe/Yamale)  
26. Metadata Profile : r/ChatGPTPromptGenius \- Reddit, accessed July 30, 2025, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1m383qd/metadata\_profile/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1m383qd/metadata_profile/)  
27. ALifeInArtifyAI (u/Tough\_Payment8868) \- Reddit, accessed July 30, 2025, [https://www.reddit.com/user/Tough\_Payment8868/](https://www.reddit.com/user/Tough_Payment8868/)  
28. Architecting Thought: A Case Study in Cross-Model Validation of Declarative Prompts\! I Created/Discovered a completely new prompting method that worked zero shot on all frontier Models. Verifiable Prompts included : r/artificial \- Reddit, accessed July 30, 2025, [https://www.reddit.com/r/artificial/comments/1m0i8bi/architecting\_thought\_a\_case\_study\_in\_crossmodel/](https://www.reddit.com/r/artificial/comments/1m0i8bi/architecting_thought_a_case_study_in_crossmodel/)  
29. Architecting Thought: A Case Study in Cross-Model Validation of Declarative Prompts\! I Created/Discovered a completely new prompting method that worked zero shot on all frontier Models. Verifiable Prompts included \- Reddit, accessed July 30, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1m0icf4/architecting\_thought\_a\_case\_study\_in\_crossmodel/](https://www.reddit.com/r/ClaudeAI/comments/1m0icf4/architecting_thought_a_case_study_in_crossmodel/)  
30. What is retrieval-augmented generation (RAG)? \- IBM Research, accessed July 30, 2025, [https://research.ibm.com/blog/retrieval-augmented-generation-RAG](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)  
31. Retrieval Augmented Generation (RAG) for LLMs | Prompt ..., accessed July 30, 2025, [https://www.promptingguide.ai/research/rag](https://www.promptingguide.ai/research/rag)  
32. Retrieval Augmented Generation for Dialog Modeling \- enlsp 2023, accessed July 30, 2025, [https://neurips2023-enlsp.github.io/papers/paper\_38.pdf](https://neurips2023-enlsp.github.io/papers/paper_38.pdf)  
33. Build Smarter AI: Leveraging the Model Context Protocol for ..., accessed July 30, 2025, [https://programmer.ie/post/mcp/](https://programmer.ie/post/mcp/)  
34. Challenges in Multi-Agent LLMs: Navigating Coordination and ..., accessed July 30, 2025, [https://gafowler.medium.com/challenges-in-multi-agent-llms-navigating-coordination-and-context-management-20661f9f2bfa](https://gafowler.medium.com/challenges-in-multi-agent-llms-navigating-coordination-and-context-management-20661f9f2bfa)  
35. Context Engineering: The Complete Guide \- Akira AI, accessed July 30, 2025, [https://www.akira.ai/blog/context-engineering](https://www.akira.ai/blog/context-engineering)  
36. The Rise of Context Engineering： Building the Foundation for Next-Generation AI Agents, accessed July 30, 2025, [https://llmmultiagents.com/en/blogs/the-rise-of-context-engineering-building-the-foundation-for-next-generation-ai-agents](https://llmmultiagents.com/en/blogs/the-rise-of-context-engineering-building-the-foundation-for-next-generation-ai-agents)  
37. Robot Constitution \- Wikipedia, accessed July 30, 2025, [https://en.wikipedia.org/wiki/Robot\_Constitution](https://en.wikipedia.org/wiki/Robot_Constitution)  
38. Claude's Constitution \\ Anthropic, accessed July 30, 2025, [https://www.anthropic.com/news/claudes-constitution](https://www.anthropic.com/news/claudes-constitution)  
39. What is "Constitutional AI"? \- AISafety.info, accessed July 30, 2025, [https://aisafety.info/questions/904J/What-is-%22Constitutional-AI%22](https://aisafety.info/questions/904J/What-is-%22Constitutional-AI%22)  
40. Generating Robot Constitutions & Benchmarks for Semantic Safety \- arXiv, accessed July 30, 2025, [https://arxiv.org/html/2503.08663v1](https://arxiv.org/html/2503.08663v1)  
41. OpenAI's Self-Correction: Is Google Sharing the Secret? \- InsiderFinance Wire, accessed July 30, 2025, [https://wire.insiderfinance.io/openais-self-correction-is-google-sharing-the-secret-4e8fa87d13c4](https://wire.insiderfinance.io/openais-self-correction-is-google-sharing-the-secret-4e8fa87d13c4)  
42. Can AI Agents Self-correct? \- Medium, accessed July 30, 2025, [https://medium.com/@jianzhang\_23841/can-ai-agents-self-correct-43823962af92](https://medium.com/@jianzhang_23841/can-ai-agents-self-correct-43823962af92)  
43. What to Know About AI Self-Correction \- Lionbridge, accessed July 30, 2025, [https://www.lionbridge.com/blog/ai-training/ai-self-correction/](https://www.lionbridge.com/blog/ai-training/ai-self-correction/)  
44. LLM Testing in 2025: Top Methods and Strategies \- Confident AI, accessed July 30, 2025, [https://www.confident-ai.com/blog/llm-testing-in-2024-top-methods-and-strategies](https://www.confident-ai.com/blog/llm-testing-in-2024-top-methods-and-strategies)  
45. Testing Large Language Models : Center for Advancing Safety of ..., accessed July 30, 2025, [https://casmi.northwestern.edu/news/articles/2024/testing-large-language-models.html](https://casmi.northwestern.edu/news/articles/2024/testing-large-language-models.html)  
46. What is Metamorphic Testing of AI? \- testRigor AI-Based Automated Testing Tool, accessed July 30, 2025, [https://testrigor.com/blog/what-is-metamorphic-testing-of-ai/](https://testrigor.com/blog/what-is-metamorphic-testing-of-ai/)  
47. Metamorphic Testing of Large Language Models for Natural Language Processing (ICSME 2025 \- Research Papers Track) \- ICSME 2025 \- International Conference on Software Maintenance and Evolution \- researchr.org, accessed July 30, 2025, [https://conf.researchr.org/details/icsme-2025/icsme-2025-papers/11/Metamorphic-Testing-of-Large-Language-Models-for-Natural-Language-Processing](https://conf.researchr.org/details/icsme-2025/icsme-2025-papers/11/Metamorphic-Testing-of-Large-Language-Models-for-Natural-Language-Processing)  
48. Test machine learning the right way: Metamorphic relations. | Lakera – Protecting AI teams that disrupt the world., accessed July 30, 2025, [https://www.lakera.ai/blog/metamorphic-relations-guide](https://www.lakera.ai/blog/metamorphic-relations-guide)  
49. Output-Invariant and Time-Based Testing – Practical Techniques for Black-Box Enumeration of LLMs \- TrebledJ's Pages, accessed July 30, 2025, [https://trebledj.me/posts/output-invariant-prompt-injection/](https://trebledj.me/posts/output-invariant-prompt-injection/)  
50. Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning for ICML 2025 \- IBM Research, accessed July 30, 2025, [https://research.ibm.com/publications/invariance-makes-llm-unlearning-resilient-even-to-unanticipated-downstream-fine-tuning](https://research.ibm.com/publications/invariance-makes-llm-unlearning-resilient-even-to-unanticipated-downstream-fine-tuning)  
51. Test-Time Fairness and Robustness in Large Language Models | OpenReview, accessed July 30, 2025, [https://openreview.net/forum?id=1fML4VF5FG](https://openreview.net/forum?id=1fML4VF5FG)  
52. How to Assess Your LLM Use Case for Bias and Fairness with LangFair | by Dylan Bouchard | CVS Health Tech Blog | Medium, accessed July 30, 2025, [https://medium.com/cvs-health-tech-blog/how-to-assess-your-llm-use-case-for-bias-and-fairness-with-langfair-7be89c0c4fab](https://medium.com/cvs-health-tech-blog/how-to-assess-your-llm-use-case-for-bias-and-fairness-with-langfair-7be89c0c4fab)  
53. Unmasking Bias —Assessing Fairness in Large Language Models \- Medium, accessed July 30, 2025, [https://medium.com/@arpitnarain/unmasking-bias-assessing-fairness-in-large-language-models-a722624e4483](https://medium.com/@arpitnarain/unmasking-bias-assessing-fairness-in-large-language-models-a722624e4483)  
54. Bias and Fairness in Large Language Models: A Survey \- MIT Press Direct, accessed July 30, 2025, [https://direct.mit.edu/coli/article/50/3/1097/121961/Bias-and-Fairness-in-Large-Language-Models-A](https://direct.mit.edu/coli/article/50/3/1097/121961/Bias-and-Fairness-in-Large-Language-Models-A)  
55. Explicitly unbiased large language models still form biased associations \- PNAS, accessed July 30, 2025, [https://www.pnas.org/doi/10.1073/pnas.2416228122](https://www.pnas.org/doi/10.1073/pnas.2416228122)  
56. An Actionable Framework for Assessing Bias and Fairness in Large Language Model Use Cases \- arXiv, accessed July 30, 2025, [https://arxiv.org/html/2407.10853v1](https://arxiv.org/html/2407.10853v1)  
57. Formal Verification of Deep Neural Networks: Theory and Practice — A introductory and hands-on tutorial for neural network verification, including both basic mathematical background and coding examples. | Neural Network Verification Tutorial, accessed July 30, 2025, [https://neural-network-verification.com/](https://neural-network-verification.com/)  
58. Formal Verification for Neural Networks with General Nonlinearities via Branch-and-Bound, accessed July 30, 2025, [https://files.sri.inf.ethz.ch/wfvml23/papers/paper\_24.pdf](https://files.sri.inf.ethz.ch/wfvml23/papers/paper_24.pdf)