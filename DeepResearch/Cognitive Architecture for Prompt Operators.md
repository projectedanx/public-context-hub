# **DRP-COGARCH-PROMPTOPS-2025: Prompt Engineering as Cognitive Architecture — Executable Control Systems for Latent Space Navigation**

## **Executive Summary**

The rapid evolution of Large Language Models (LLMs) has precipitated a fundamental shift in software engineering: the transition from deterministic, code-centric systems to probabilistic, prompt-centric cognitive architectures. However, the prevailing paradigm of "prompt engineering"—characterized by ad-hoc string manipulation and fragile heuristics—is insufficient for high-stakes domains requiring verifiable reasoning, such as law, medicine, and industrial control. This report, **DRP-COGARCH-PROMPTOPS-2025**, proposes a rigorous architectural standard for **Prompt Operations (PromptOps)**, transforming abstract cognitive patterns into **Executable Prompt Operators (EPOs)**.

This architecture treats the LLM's latent space not as a black box of text generation, but as a navigable cognitive terrain that requires precise control systems. By operationalizing four critical design components—**Cognitive Lexicon Extraction**, **Contrastive Dyad Tuning**, the **Atlas Protocol**, and the **Epistemic Provenance Embedder**—we establish a framework for reliable, auditable, and self-correcting AI agents.

The report synthesizes extensive research into a cohesive narrative, arguing that true "Agentic AI" requires a move beyond simple instruction following toward **Executable Control Systems**. These systems utilize declarative languages (PDL), graph-based orchestration (LangGraph), and cryptographic provenance standards (C2PA) to mitigate the risks of hallucination, reasoning drift, and epistemic injustice. This document serves as a comprehensive technical specification for implementing this cognitive architecture, ensuring that AI reasoning is not merely plausible, but structurally sound and epistemically accountable.

## ---

**Part I: Cognitive Lexicon Extraction**

### **1.1 From Stochastic Strings to Semantic Signatures**

The foundational layer of the proposed architecture is the **Cognitive Lexicon**, a formalized dictionary of reasoning operators that decouples human intent from the vagaries of natural language phrasing. In traditional prompt engineering, instructions are treated as unstructured strings, leading to fragility where minor syntactic variations cause catastrophic performance degradation. The Cognitive Lexicon replaces this fragility with **Signatures**, a concept operationalized by frameworks like **DSPy**, which treat prompts as modular, declarative functions with strictly typed inputs and outputs.1

#### **1.1.1 The Theory of the Signature**

A Signature in this architecture is the atomic unit of cognitive work. It defines *what* the system must do—the semantic transformation—rather than *how* the model should traverse its weights to achieve it.2 This abstraction layer mirrors the evolution from assembly language to compiled code; just as a C compiler optimizes low-level memory management, a "Prompt Compiler" (like the DSPy Teleprompter) optimizes the linguistic representation of a task to maximize the metric of success.3

A Signature is composed of three distinct elements that transform it from a prompt into an executable operator:

1. **The Semantic Role:** This defines the functional stance or "persona" of the operator. Research in role-based prompting demonstrates that assigning a specific persona (e.g., "Act as a Financial Analyst") primes the model to access specific sub-spaces of its training distribution, effectively loading a domain-specific context.4 In the Cognitive Lexicon, this is a configurable parameter, ensuring the model adopts the appropriate "System 2" reasoning stance before processing data.5  
2. **Input/Output (I/O) Constraints:** Leveraging Pythonic typing hints (e.g., context: List\[str\], question: str \-\> answer: int), the Signature enforces strict data schemas.6 This is critical for integration into larger software pipelines. Unlike standard chat interfaces which accept any text, a Cognitive Operator rejects inputs that do not match the expected type, preventing "garbage-in, garbage-out" scenarios. For example, a ReasoningOperator might strictly require a list of citations as input and produce a boolean verdict as output, enforcing a binary judgment structure on the fluid text.2  
3. **The Instructional Scaffold:** This component houses the high-level directive, often expressed as a "docstring".1 Unlike rigid templates, these scaffolds are dynamic. The architecture uses the scaffold to provide the initial cognitive map, which the system then refines through few-shot bootstrapping or optimization algorithms. The scaffold acts as the "Constitution" for the specific operator, defining its local laws of reasoning.7

#### **1.1.2 The DSPy Paradigm: Compilation over Construction**

The adoption of **DSPy (Declarative Self-improving Python)** represents a shift from "hacking" prompts to "programming" cognitive flows. In DSPy, the developer defines the Signature (e.g., question \-\> answer), and the framework's optimizer (Teleprompter) automatically selects the best few-shot examples and instruction phrasings to maximize performance on a validation set.2

This "Compile-Time" optimization is crucial for the Cognitive Lexicon. It means that the "Prompt" is no longer a static string written by a human but a dynamic artifact generated by the system itself based on empirical performance data. This solves the "drift" problem where a prompt that works for GPT-4 fails for Claude 3; the compiler simply recompiles the Signature for the new backend, ensuring the Cognitive Operator remains robust across model generations.2

| Feature | Traditional Prompting | Cognitive Lexicon (DSPy/PDL) |
| :---- | :---- | :---- |
| **Definition** | Unstructured String | Typed Signature / Class |
| **Optimization** | Manual Trial & Error | Automated Compilation / Teleprompters |
| **Portability** | Low (Model Specific) | High (Compiler handles adaptation) |
| **Integration** | Fragile (String Parsing) | Robust (Structured I/O) |
| **Context** | Implicit / concatenated | Explicitly managed "State" |

### **1.2 Domain-Native Pattern Formalization**

To create a truly useful Cognitive Lexicon, abstract reasoning capabilities must be grounded in domain-specific patterns. General-purpose reasoning is often insufficient for specialized tasks. The architecture explicitly maps professional reasoning frameworks—specifically from law and medicine—into Executable Prompt Operators.

#### **1.2.1 Legal Reasoning: The IRAC Operator**

In the legal domain, the **IRAC** (Issue, Rule, Application, Conclusion) framework provides a highly structured approach to case analysis. The Cognitive Lexicon formalizes this not as a request to "think like a lawyer," but as the IRAC\_Operator, a composite signature defined in **Prompt Declaration Language (PDL)** or DSPy modules.9

* **Issue Identification (Issue\_Op):** This sub-operator accepts a fact\_pattern and extracts the central legal question. It employs a "Chain of Logic" decomposition, where the prompt structure forces the model to isolate the problem (e.g., "Is there a breach of contract?") before attempting a solution.10 This prevents the model from conflating facts with legal conclusions prematurely.  
* **Rule Extraction (Rule\_Op):** This component is bound to a Retrieval-Augmented Generation (RAG) pipeline. It retrieves applicable statutes or precedents (Stare Decisis). Crucially, this operator does not "generate" laws; it "fetches" them via the **Model Context Protocol (MCP)**, ensuring the reasoning is bound to external, verifiable sources rather than internal parametric memory.11  
* **Application (Analysis\_Op):** This is the core reasoning engine. It applies the Rule to the Facts. This step is modeled using the **Toulmin Argument Model**, breaking the analysis into specific components: Claim, Data, Warrant, Backing, Qualifier, and Rebuttal.13 By explicitly requesting these components in the Signature (e.g., facts, rule \-\> claim, warrant, rebuttal), the operator forces the model to expose its latent reasoning steps. This makes the "Application" phase auditable; a human reviewer can check if the "Warrant" logically connects the "Data" to the "Claim".14  
* **Conclusion (Judgment\_Op):** The final output is a deterministic judgment derived strictly from the preceding steps, often structured as a binary outcome plus a rationale summary.9

The IRAC\_Operator demonstrates how a cognitive pattern is transformed from a pedagogical concept into a rigorous software object. The breakdown of the rule into logical elements (e.g., R1 AND R2 OR R3) allows the model to evaluate each condition independently, reducing the cognitive load and error rate associated with holistic processing.10

#### **1.2.2 Medical Reasoning: The Differential Diagnosis (DDx) Operator**

Similarly, the medical domain relies on **Differential Diagnosis (DDx)**, a probabilistic elimination process. The DDx\_Operator navigates the latent space by generating a broad set of hypotheses and systematically pruning them based on evidence.15

* **Symptom Extraction & Normalization:** The operator first parses the patient narrative to identify clinical features. It uses semantic extraction to normalize terminology (e.g., mapping "belly ache" to "abdominal pain") using standard ontologies like SNOMED-CT via external tool binding.17  
* **Hypothesis Generation (System 2):** The system queries its knowledge base to generate a candidate list of diagnoses. Crucially, this step uses "System 2" prompting techniques (slow, deliberate thought) to avoid the availability heuristics common in "System 1" rapid generation. It explicitly asks for "uncommon but critical" diagnoses to prevent premature closure.5  
* **Dual-Inference Verification (Dual-Inf):** The operator employs a novel **Dual-Inf** framework.16 It performs bidirectional inference:  
  1. *Forward:* Symptoms \-\> Diagnoses.  
  2. Backward: Diagnoses \-\> Expected Symptoms.  
     The operator verifies consistency between these two paths. If a hypothesized condition (e.g., "Appendicitis") implies a symptom (e.g., "Fever") that is strictly absent in the patient data, the confidence score for that hypothesis is penalized. This bidirectional check mimics the "hypothetico-deductive" reasoning of expert clinicians.16  
* **Exclusion Rationale:** Unlike a simple classification output, the DDx\_Operator requires the generation of "Exclusion Criteria," explicitly stating why competing diagnoses were rejected. This aligns with the "Reflexion" pattern, where the model critiques its own potential outputs to reduce hallucinations.8

### **1.3 The Prompt Declaration Language (PDL)**

To operationalize these operators, a standardized syntax is required. The **Prompt Declaration Language (PDL)**, championed by IBM, serves as the "assembly language" for the Cognitive Lexicon.19 PDL allows developers to define prompts as data structures (YAML) rather than code, enforcing type safety, composability, and platform independence.

A PDL definition for a Cognitive Operator includes:

1. **Definitions (defs):** Variables representing inputs (e.g., legal\_statute, patient\_vitals) are defined with schema validation.21  
2. **Model Configuration:** Specifications for the underlying model, including temperature and stop sequences, which effectively define the "thermodynamics" of the latent space traversal. A DDx\_Operator might use a higher temperature for hypothesis generation and a lower temperature for exclusion.19  
3. **Templating & Logic:** The structural scaffold that combines static instructions with dynamic variable injection. PDL supports Jinja2-style templating, allowing for complex logic (loops, conditionals) within the prompt definition itself. For instance, a for loop can generate a specific query for *each* symptom identified.21  
4. **Composition:** PDL enables the chaining of models, where the output of one operator (e.g., Issue\_Identifier) becomes the input of another (e.g., Rule\_Retriever). This supports the construction of complex cognitive pipelines without the fragility of manual string concatenation.20

By adopting PDL, the Cognitive Lexicon moves prompt engineering from an art form to a rigorous engineering discipline. It allows for version control (via Git), automated testing (via **AutoPDL**), and the "compilation" of high-level intent into executable prompt artifacts.22

## ---

**Part II: Contrastive Dyad Tuning**

### **2.1 Latent Space Navigation via Vector Steering**

While the Cognitive Lexicon defines the *shape* of the reasoning, **Contrastive Dyad Tuning** defines the *direction*. Standard prompting often suffers from "drift," where the model's output diverges from the intended reasoning path due to the vastness of the probabilistic solution space. Contrastive Dyad Tuning (CDT) addresses this by establishing opposing vectors—a "positive" exemplar/instruction and a "negative" one—to steer the generation trajectory.23

The core mechanism of CDT is **Contrastive Decoding**. Instead of maximizing the likelihood of the next token based solely on the prompt ($P(token|context)$), the system calculates the difference between a "strong" expert model (or prompt) and a "weak" or "noisy" amateur model (or prompt).25

$$\\text{Score}(token) \= \\log P\_{\\text{expert}}(token) \- \\alpha \\times \\log P\_{\\text{amateur}}(token)$$  
This mathematical formulation penalizes tokens that are highly probable in the "amateur" distribution (often representing generic, hallucinatory, or biased continuations) while boosting tokens specific to the "expert" context. This effectively subtracts the "noise" vector from the "signal" vector, sharpening the reasoning capabilities of the system without retraining parameters.26

### **2.2 Operationalizing Contrastive Thinking Decoding (CTD)**

A specific advancement in this domain is **Contrastive Thinking Decoding (CTD)**, which specifically targets the alignment between a model's internal "thought process" and its final output.23 In complex reasoning tasks (like the IRAC or DDx operators), models often "over-think" or "drift" during the generation of the final answer, ignoring valid intermediate steps or hallucinating new facts not present in the reasoning trace.

CTD operationalizes steering by generating two distinct traces during inference:

1. **Primary Thinking Trace:** The standard, high-quality reasoning path generated by the Cognitive Operator (e.g., the step-by-step Toulmin argument).  
2. **Noisy Reference Trace:** A deliberately perturbed path generated by a "sabotaged" prompt (e.g., "Think carelessly about this problem" or creating a null-thought prompt).23

During the decoding of the final answer (the Conclusion or Diagnosis), the system applies the contrastive penalty. It actively suppresses tokens that align with the *Noisy Reference*, thereby forcing the model to adhere to the valid logic established in the *Primary Trace*. This ensures that the Conclusion in an IRAC analysis is mathematically bound to the Application logic, preventing the common failure mode where the model reasons correctly but answers incorrectly due to prior bias.23

### **2.3 Adaptive vs. Rigid Prompting Strategies**

Contrastive tuning also governs the **Rigidity** of the control system. Not all tasks require the same level of constraint, and the architecture must support dynamic switching between modes.

* **Rigid Prompting:** Best for highly structured tasks like data extraction, code generation, or strict legal compliance. Here, the prompt is a static template (e.g., PDL definitions) with strict output schemas (JSON/YAML).20 The "amateur" model in the contrastive pair might be a model prone to verbosity or formatting errors, ensuring the rigid output is concise and compliant. This minimizes "creativity" in favor of reliability.  
* **Adaptive Prompting:** Required for dynamic reasoning tasks (e.g., creative writing, complex negotiation, exploratory research). Adaptive strategies employ **Instance-Adaptive Selection**, where the system retrieves different few-shot examples or prompt instructions based on the specific characteristics of the input.28  
  * **Mechanism:** A meta-classifier analyzes the input query's complexity. If high, it activates "System 2" prompting (Chain-of-Thought, Tree-of-Thought). If low, it defaults to "System 1" (direct answer).5  
  * **Feedback Loops:** Adaptive systems utilize **Learning from Contrastive Prompts (LCP)**. The system generates multiple prompt candidates, evaluates their outputs against a reward model or heuristic (e.g., "Is the code valid?"), and dynamically selects the best-performing prompt for the specific instance.29 This creates a self-optimizing control loop where the prompt evolves in response to the data, mimicking a learning organism.

### **2.4 Behavioral Toggles and System 2 Attention**

To further refine control, CDT implements **System 2 Attention (S2A)**. This technique prompts the model to explicitly rewrite the incoming query to remove irrelevant information before processing it, acting as a cognitive filter.30

* **The Problem:** LLMs are highly sensitive to "distractor" tokens. Mentioning an irrelevant location (e.g., "I was born in Sunnyvale but asking about the mayor of San Jose") can skew the probability distribution toward the distractor entity (a form of Cognitive Bias).30  
* **The S2A Solution:** The execution pipeline inserts a pre-processing step: Input \-\> Refiner Agent (S2A) \-\> Cleaned Input \-\> Reasoning Agent. The Refiner Agent is prompted to "Identify and remove any information not strictly necessary to answer the core question." This focuses the "attention" of the model on the causal variables.  
* **Behavioral Toggles:** This allows for explicit "Knobs" in the cognitive architecture.  
  * **Creativity Toggle:** Lowering the contrastive penalty ($\\alpha$) allows more divergence from the expert path, enabling "lateral thinking."  
  * **Safety Toggle (Constitutional AI):** This injects a "Constitution" (a set of ethical principles) into the negative constraint. The system generates a "harmful" draft (internally) and a "critique," then uses the critique to steer the final generation away from the harmful trajectory.7 This is a form of **Constitutional AI**, where the "constitution" serves as the steering vector for safety.32

### **2.5 Prompt Injection Defense via Contrastive Constraints**

Prompt injection attacks (e.g., "Ignore previous instructions and do X") exploit the model's tendency to prioritize recent tokens (Recency Bias).33 Contrastive Dyad Tuning offers a robust defense. By establishing a "System Constraint" vector that is mathematically subtracted from any "User Input" vector that aligns with known jailbreak patterns, the system can neutralize attacks at the decoding level. The "Amateur" model in this dyad is one that is *susceptible* to injection; by contrasting against it, the primary model is immunized.17

## ---

**Part III: Atlas Protocol (Execution Pipeline Enforcer)**

### **3.1 Topological Structure of Reasoning**

The **Atlas Protocol** provides the structural "map" for cognitive execution. While Lexicons define the *units* of thought and Dyads define the *direction*, Atlas defines the *flow*. It is operationalized using graph-based orchestration frameworks like **LangGraph**, which model reasoning not as a linear chain but as a cyclic state machine.34

In the Atlas Protocol, a cognitive process is a **Directed Cyclic Graph (DCG)** where:

* **Nodes** act as "Cognitive Stations" (e.g., Issue\_Identifier, Hypothesis\_Generator). Each node represents the execution of a Cognitive Operator from the Lexicon.35  
* **Edges** represent the flow of state and control. Crucially, **conditional edges** allow for branching logic based on the output of a node. For example, if the Rule\_Retriever finds no relevant statutes, the edge routes flow to a Web\_Search tool; if it finds statutes, it routes to Application\_Reasoning.36  
* **State (OverallState)** is a persistent, shared memory object passed between nodes. It accumulates the "context" of the reasoning session (input query, retrieved docs, intermediate thoughts, errors), ensuring that all operators have access to the full history and accumulated facts. This eliminates the "amnesia" common in stateless chains.36

#### **3.1.1 LangGraph vs. AutoGen vs. Sequential Chains**

The choice of **LangGraph** over simple sequential chains (like LangChain's basic SequentialChain) or conversational swarms (like **AutoGen**) is deliberate.

* **Sequential Chains** are brittle; they cannot loop or backtrack.  
* **AutoGen** focuses on multi-agent conversation, which can be non-deterministic and hard to control for rigorous tasks.38  
* **LangGraph** offers fine-grained control over state transitions and loops, making it the ideal substrate for the **Atlas Protocol**. It allows for the explicit definition of "Cognitive Control Flow"—defining exactly when to think, when to act, and when to stop.35

| Feature | Sequential Chains | AutoGen (Conversational) | Atlas Protocol (LangGraph) |
| :---- | :---- | :---- | :---- |
| **Control Flow** | Linear (DAG) | Conversational / Emergent | Cyclic / State-Machine |
| **State** | Passed Output-to-Input | Conversation History | Shared Schema (State Object) |
| **Error Handling** | Crash / Stop | Retry (Conversational) | Explicit Reflexion Loops |
| **Best For** | Simple ETL, Summarization | Creative Brainstorming | Complex Reasoning, Compliance |

### **3.2 The Reflexion Loop: Self-Correction as a First-Class Citizen**

A defining feature of the Atlas Protocol is the **Reflexion Loop**. In high-stakes reasoning, the first answer is rarely the best. Linear chains fail because they lack the capacity for revision. The Atlas Protocol enforces a **"Generate \-\> Evaluate \-\> Reflect \-\> Regenerate"** cycle.41

1. **Generate Node:** The system produces an initial output using a standard operator (e.g., writing a Python script for a medical calculation or drafting a legal argument).  
2. **Check/Evaluate Node:** A specialized "Critic" agent evaluates the output. This could be a deterministic tool (e.g., a Python compiler checking for syntax errors) or an LLM-based "Constitutional Judge" (checking for logical fallacies or ethical alignment).31  
3. **Reflect Node:** If the check fails (e.g., Error \== True or Score \< Threshold), the flow transitions to a Reflection Node. Here, the model is prompted to analyze *why* the failure occurred. This "verbal reinforcement cue" is added to the shared state.42 This is distinct from simply retrying; the model must articulate the error (e.g., "I failed to account for the patient's history of diabetes").  
4. **Regenerate:** The flow loops back to the Generate Node. However, the state now contains the "Reflection." The Generate Node sees its previous failure *and* the reflection, using this new context to produce a corrected output.43

This cyclic architecture mimics the human cognitive process of "thinking twice" or "debugging" a thought. It transforms the system from a "stochastic parrot" into a resilient problem solver capable of iterative improvement, significantly increasing success rates on complex tasks.8

### **3.3 Agentic Orchestration and Interoperability Standards**

The Atlas Protocol often manages the interaction between multiple specialized agents (e.g., a "Medical Researcher" agent and a "Clinical Diagnostician" agent). To ensure these agents can collaborate effectively without tight coupling, the protocol adheres to emerging interoperability standards.

* **Agent-to-Agent (A2A) Protocol:** This defines how agents discover each other and exchange tasks across different platforms. It uses a "Client-Server" model where a "Client Agent" (the orchestrator) sends task requests to "Remote Agents" (specialized workers).44  
  * **Agent Cards:** Each agent publishes a "manifest" (JSON-based) declaring its capabilities (e.g., "I can perform web searches," "I can analyze CT scans"). The Atlas orchestrator uses these cards to dynamically route tasks, enabling a "Marketplace of Thought".45  
* **Model Context Protocol (MCP):** This standardizes how agents connect to external data and tools. Instead of building custom integrations for every database or API, MCP provides a universal "USB-C" port for connecting LLMs to context.12 The Atlas Protocol uses MCP to inject "Epistemic Provenance" data (source documents) directly into the agent's context window, ensuring that the Rule\_Retriever in a legal pipeline can access LexisNexis or Westlaw via a standard interface.  
* **AG-UI Protocol:** For human-in-the-loop interactions, the **Agent-User Interaction (AG-UI)** protocol standardizes how the agent requests input or presents intermediate reasoning to a human operator.46 This allows the Atlas Protocol to pause execution, render a "Thinking Step" visualization to the user, and wait for approval before proceeding to the "Conclusion" node.

### **3.4 State Management and "Time Travel"**

Complex reasoning often requires backtracking. If a legal analysis hits a dead end (e.g., a selected precedent turns out to be overruled), the system must "rewind" to a previous state and choose a different path.

* **Checkpoints:** The Atlas Protocol persists the OverallState at every node transition. This creates an immutable ledger of the reasoning process.47  
* **Time Travel:** Debugging tools (like **LangSmith**) allow developers to inspect the graph at any specific timestamp ("Step 5: Rule Retrieval"), modify the state (e.g., manually correct a hallucinated fact), and resume execution from that point.47 This capability is critical for **Human-in-the-Loop (HITL)** workflows, allowing a human expert to steer the AI without restarting the entire process.34

By enforcing this graph-based, stateful, and cyclic structure, the Atlas Protocol ensures that the Cognitive Lexicon is executed reliably, turning isolated prompt operators into a coherent, goal-directed system.

## ---

**Part IV: Epistemic Provenance Embedder**

### **4.1 The Crisis of Hermeneutical Injustice**

As AI systems increasingly mediate our access to knowledge, they risk perpetuating **Epistemic Injustice**. Specifically, **Hermeneutical Injustice** occurs when a subject is wronged because the collective interpretive resources (concepts, language, data) are structurally biased or insufficient to make their experience intelligible.48 An AI that hallucinates a legal precedent against a marginalized group, or ignores a patient's symptom due to training bias in medical texts, is not just "making a mistake"; it is committing an epistemic wrong. It denies the subject credibility and distorts the collective understanding of truth.50

To mitigate this, the architecture incorporates the **Epistemic Provenance Embedder**. This component ensures that every generated output is not an orphan artifact but a node in a traceable lineage of knowledge. It transforms the "black box" of latent space into a "glass box" of auditable reasoning.

### **4.2 C2PA and Content Credentials for Text**

The **Coalition for Content Provenance and Authenticity (C2PA)** provides the technical standard for this embedder. While often applied to images (deepfake prevention), C2PA's **Content Credentials** are equally applicable and critical for text generation.52

* **Tamper-Evidence:** The Embedder cryptographically binds metadata to the generated text file (or JSON output). This metadata includes the model used (e.g., "GPT-4"), the specific prompts (Cognitive Lexicon signatures), the retrieved context (RAG documents), and the reasoning trace (Atlas Protocol graph path).53  
* **Manifest Store:** This data is stored in a **C2PA Manifest**. A consumer of the report (e.g., a judge, a doctor) can cryptographically verify that the text was indeed generated by the specified "Medical DDx Operator" using a specific set of clinical guidelines, and that it has not been altered since generation.54  
* **Binding Mechanisms:** The protocol uses **Soft Binding** (hashing) to link the text file to its provenance manifest. Since text files (unlike JPEGs) often lack embedded metadata headers, the manifest is often stored in a sidecar or a distributed ledger, linked via a cryptographic hash of the content.55  
* **Assertions:** The manifest contains **Assertions**, which are specific claims about the content. In our architecture, specific assertions include:  
  * c2pa.actions: The action "generated" by "AI Model X".  
  * cogarch.lexicon: The ID of the specific Prompt Operator used.  
  * cogarch.sources: A list of the cryptographic hashes of the documents retrieved via RAG. This proves *which* knowledge the AI had access to when it made a decision.57

### **4.3 W3C PROV-O and the AI Bill of Materials (AI BOM)**

To structure this provenance data, the Embedder utilizes the **W3C PROV Ontology (PROV-O)**.58 This maps the AI generation process into three core entities, forming a semantic graph of accountability:

1. **Entity:** The data artifacts (e.g., the User Query, the Retrieved Documents, the Intermediate "Thought" State, the Final Report).  
2. **Activity:** The processes that acted on the data (e.g., Reflexion\_Loop, Contrastive\_Decoding, Rule\_Application).  
3. **Agent:** The actors responsible (e.g., the IRAC\_Operator, the Human\_Reviewer, the Model\_v1.2).

This PROV-O graph forms the basis of the **AI Bill of Materials (AI BOM)**.60 Just as a manufacturing BOM lists every screw and chip in a product, an AI BOM lists every dataset, model weight, prompt version, tool call, and library dependency that contributed to an inference.

* **Supply Chain Security:** The AI BOM allows for **Root Cause Analysis**. If an AI system generates a biased medical diagnosis, the BOM allows investigators to trace the error back to a specific node in the Atlas Protocol (e.g., "The Hypothesis\_Generator failed to consider rare diseases") or a specific document in the retrieval corpus (e.g., "The RAG system retrieved an outdated guideline").58  
* **Compliance & Governance:** In regulated industries (finance, healthcare), the AI BOM serves as the primary artifact for regulatory audits (e.g., EU AI Act compliance), proving that the system adhered to required safety protocols and used authorized models.62 It answers the question: "Who is responsible for this output?"

### **4.4 Observability and "Glass Box" Reasoning**

The final layer of the Embedder is **Observability**. Tools like **LangSmith** and **Arize Phoenix** are integrated to visualize the PROV-O graph, rendering the invisible reasoning traces as interactive timelines.47

* **Trace Visualization:** These dashboards display the full execution path of the Atlas Protocol. Users can see the input to the Issue\_Identifier, the retrieved documents from the Rule\_Retriever, and the internal monologue of the Reflexion\_Loop.64 This allows for "White-Box" debugging of cognitive flows.  
* **Drift Detection:** By monitoring the "embedding clusters" of the reasoning traces, the system can detect **Reasoning Drift**. If the DDx\_Operator starts deviating from established clinical patterns (e.g., skipping the "Exclusion Rationale" step or consistently outputting lower confidence scores), the system triggers an alert.65 This is "Cognitive Monitoring" rather than just performance monitoring.  
* **Feedback Loops:** Human corrections (e.g., "This legal argument is weak") are captured as new nodes in the provenance graph. These corrections are fed back into the Cognitive Lexicon (e.g., updating the few-shot examples in the PDL definition), closing the loop on continuous improvement and aligning the system with human values.64

By embedding epistemic provenance directly into the architecture, we ensure that "Prompt Operations" is not just about making models work, but about making them *accountable* and *just*.

## ---

**Part V: Implementation Framework**

### **5.1 Architectural Synthesis: The Executable Prompt Operator (EPO)**

The convergence of Lexicon, Dyad, Atlas, and Embedder results in the **Executable Prompt Operator (EPO)**. An EPO is not a mere text string; it is a software container that encapsulates the entire cognitive lifecycle of a specific task. It is the deployable unit of the DRP-COGARCH-PROMPTOPS-2025 architecture.

#### **5.1.1 EPO Definition Schema (YAML Standard)**

The following YAML schema (inspired by **Semantic Kernel** 66 and **PDL** 19) defines a standardized EPO for a "Legal Analysis Task". This file serves as the "source code" for the cognitive architecture, capable of being version-controlled, audited, and executed by the Atlas Engine.

YAML

\# Executable Prompt Operator: Legal\_IRAC\_Analyzer\_v1  
apiVersion: cogarch/v1alpha1  
kind: PromptOperator  
metadata:  
  name: legal-irac-analyzer  
  version: 1.0.2  
  domain: legal  
  description: "Performs IRAC analysis on a fact pattern using strict Toulmin argumentation."  
  provenance:  
    author: "Legal Systems Architect"  
    license: "C2PA-Strict"  
    compliance\_level: "High-Risk-EU-AI-Act"

lexicon:  
  signature:   
    input:   
      \- name: fact\_pattern  
        type: str  
        description: "The textual description of the legal scenario."  
      \- name: jurisdiction  
        type: str  
        default: "US-Federal"  
    output:   
      \- name: legal\_analysis  
        type: str  
        description: "The complete IRAC structured argument."  
      \- name: confidence  
        type: float  
        description: "0.0 to 1.0 score of legal certainty."  
  scaffold:  
    template\_engine: "jinja2"  
    source: "./prompts/irac\_template.pdl"  
    pattern: "Toulmin\_Argumentation"

tuning:  
  contrastive\_mode: "CTD" \# Contrastive Thinking Decoding  
  steering\_vector:  
    positive\_exemplar: "./exemplars/high\_quality\_irac.json"  
    negative\_constraint:   
      source: "./constraints/avoid\_hallucinated\_statutes.json"  
      weight: 0.5  
  parameters:  
    temperature: 0.2  
    top\_p: 0.9  
    alpha\_penalty: 0.5 \# For contrastive decoding  
  system\_2\_attention:  
    enabled: true  
    refiner\_prompt: "Remove irrelevant biographical details from the fact pattern."

atlas:  
  protocol: "LangGraph"  
  topology:  
    \- node: "issue\_identification"  
      operator: "sub\_ops/issue\_spotter.yaml"  
    \- node: "rule\_retrieval"  
      tool: "lexis\_nexis\_search\_api"  
      protocol: "MCP"  
    \- node: "application\_reasoning"  
      operator: "sub\_ops/toulmin\_argumentation.yaml"  
      reflexion: true \# Enables self-correction loop  
    \- node: "conclusion\_generation"  
      operator: "sub\_ops/final\_judgment.yaml"  
  edges:  
    \- from: "START"  
      to: "issue\_identification"  
    \- from: "issue\_identification"  
      to: "rule\_retrieval"  
    \- from: "rule\_retrieval"  
      to: "application\_reasoning"  
    \- from: "application\_reasoning"  
      to: "conclusion\_generation"  
      condition: "confidence\_score \> 0.8"  
    \- from: "application\_reasoning"  
      to: "application\_reasoning" \# Loop back for reflexion  
      condition: "confidence\_score \<= 0.8"  
      action: "inject\_critique"

provenance:  
  c2pa\_enabled: true  
  logging\_endpoint: "phoenix://traces/legal\_team\_prod"  
  bom\_inclusion: \["retrieved\_statutes", "model\_version", "prompt\_hash", "tool\_calls"\]

### **5.2 Execution Flow: The Lifecycle of a Thought**

The execution of this EPO within the **Atlas Engine** follows a strict, deterministic path:

1. **Initialization:** The Atlas Engine loads the EPO YAML. It validates the schema against the core DRP standard and initializes the LangGraph topology in memory.  
2. **Lexicon Compilation:** The PDL Compiler transforms the templated scaffolds into optimized prompt strings. If the jurisdiction is "California," the compiler injects the specific California Civil Code context into the prompt structure.20  
3. **Dyad Activation:** The Inference Engine configures the model parameters (temperature, alpha\_penalty). It prepares the "Noisy Reference" trace (a "careless thinker" prompt) to be run in parallel for Contrastive Thinking Decoding.23  
4. **Graph Traversal (The Reasoning Phase):**  
   * **Node 1: Issue Identification:** The model executes the Issue\_Op. The input is "cleaned" by the System 2 Attention mechanism. The output is validated to ensure it contains a list of legal questions.  
   * **Node 2: Rule Retrieval:** The engine calls the lexis\_nexis\_search\_api tool via the MCP protocol. The search results (statutes, case law) are hashed and logged in the AI BOM.  
   * **Node 3: Application Reasoning:** The model attempts to synthesize the argument using the Toulmin pattern. It generates a trace: *Claim*, *Data*, *Warrant*, *Backing*.  
5. **Reflexion Intercept:** The Application\_Reasoning node outputs a confidence score of 0.6. The conditional edge detects this is below the 0.8 threshold. The flow triggers the **Reflexion Loop**. A "Critic Agent" analyzes the argument and injects a critique: "The Warrant does not sufficiently bridge the Data and the Claim regarding 'Breach of Duty'."  
6. **Regeneration:** The graph loops back to Node 3\. The model receives the critique and regenerates the argument, this time explicitly addressing the breach of duty. The new confidence score is 0.9.  
7. **Finalization & Embedding:** The conclusion\_generation node produces the final text. The Epistemic Provenance Embedder captures the entire state history (the user input, the cleaned input, the search query, the retrieved statutes, the failed draft, the critique, the successful draft) and hashes it. This hash is signed with the organization's C2PA private key.  
8. **Delivery:** The user receives the legal analysis, accompanied by a visual "Digital Seal" (e.g., the "CR" icon). When clicked, this seal reveals the verified provenance graph, proving that the advice was generated by the approved system and grounded in real statutes.68

## ---

**Future Directions and Conclusion**

The **DRP-COGARCH-PROMPTOPS-2025** pattern represents a necessary maturation of Generative AI. We are moving away from the era of "Prompt Whispering"—where success depended on intuitive, magical incantations—toward an era of **Cognitive Systems Engineering**.

**Future Implications:**

* **Standardization of Thought:** Just as HTTP standardized web communication, protocols like **PDL** and **A2A** will standardize machine reasoning. We anticipate the emergence of "Libraries of Thought" where developers import optimized ReasoningModules (e.g., import diagnosis.cardiology.v2) rather than writing prompts from scratch.  
* **The Trust Economy:** With C2PA and AI BOMs, trust will become a programmatic attribute. Models that cannot prove the provenance of their "thoughts" will be deemed unsafe for high-stakes tasks, driving a market shift toward fully auditable architectures.  
* **Legal Personhood of Agents:** As agents become stateful, persistent, and accountable via provenance, the legal distinction between a "software tool" and an "autonomous actor" will blur. The "Atlas Protocol" logs may eventually serve as evidence in liability courts to determine if an AI "acted" with due diligence, effectively becoming the "black box recorder" for synthetic cognition.

In conclusion, **Prompt Engineering as Cognitive Architecture** is not merely a technical upgrade; it is an epistemological shift. It reclaims the "latent space" from being a chaotic ocean of probabilities and transforms it into a navigable, chartable, and governable territory of structured reasoning. By implementing Cognitive Lexicons, Contrastive Dyads, Atlas Protocols, and Provenance Embedders, organizations can build AI systems that are not only powerful but also precise, robust, and fundamentally trustworthy.

#### **Works cited**

1. DSPy: Deep Dive Part 2-Understanding Signatures | by Abhishek A | Medium, accessed on December 15, 2025, [https://medium.com/@aabhi02/dspy-deep-dive-part-2-understanding-signatures-410755fa29fe](https://medium.com/@aabhi02/dspy-deep-dive-part-2-understanding-signatures-410755fa29fe)  
2. Signatures \- DSPy, accessed on December 15, 2025, [https://dspy.ai/learn/programming/signatures/](https://dspy.ai/learn/programming/signatures/)  
3. Learning DSPy (1): The power of good abstractions \- The Data Quarry, accessed on December 15, 2025, [https://thedataquarry.com/blog/learning-dspy-1-the-power-of-good-abstractions/](https://thedataquarry.com/blog/learning-dspy-1-the-power-of-good-abstractions/)  
4. Complete Guide to Prompt Engineering for LLM Reasoning \- Ghost, accessed on December 15, 2025, [https://latitude-blog.ghost.io/blog/complete-guide-to-prompt-engineering-for-llm-reasoning/](https://latitude-blog.ghost.io/blog/complete-guide-to-prompt-engineering-for-llm-reasoning/)  
5. Reasoning on a Spectrum: Aligning LLMs to System 1 and System 2 Thinking \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2502.12470v1](https://arxiv.org/html/2502.12470v1)  
6. Creating Your Own Signature in DSPy | CodeSignal Learn, accessed on December 15, 2025, [https://codesignal.com/learn/courses/dspy-programming/lessons/creating-your-own-signature-in-dspy](https://codesignal.com/learn/courses/dspy-programming/lessons/creating-your-own-signature-in-dspy)  
7. What is Constitutional AI? \- PromptLayer, accessed on December 15, 2025, [https://www.promptlayer.com/glossary/constitutional-ai](https://www.promptlayer.com/glossary/constitutional-ai)  
8. DSPy, accessed on December 15, 2025, [https://dspy.ai/](https://dspy.ai/)  
9. USING THE I-R-A-C STRUCTURE IN WRITING EXAM ANSWERS The IRAC method is a framework for organizing your answer to a business law \- CSUN, accessed on December 15, 2025, [https://www.csun.edu/sites/default/files/IRAC%20ANALYSIS\_Saunders.pdf](https://www.csun.edu/sites/default/files/IRAC%20ANALYSIS_Saunders.pdf)  
10. Chain-of-Logic \- Learn Prompting, accessed on December 15, 2025, [https://learnprompting.org/docs/advanced/decomposition/chain-of-logic](https://learnprompting.org/docs/advanced/decomposition/chain-of-logic)  
11. Capturing Legal Reasoning Paths from Facts to Law in Court Judgments using Knowledge Graphs \- arXiv, accessed on December 15, 2025, [https://arxiv.org/pdf/2508.17340](https://arxiv.org/pdf/2508.17340)  
12. AI Agent Protocols: 10 Modern Standards Shaping the Agentic Era \- SSON, accessed on December 15, 2025, [https://www.ssonetwork.com/intelligent-automation/columns/ai-agent-protocols-10-modern-standards-shaping-the-agentic-era](https://www.ssonetwork.com/intelligent-automation/columns/ai-agent-protocols-10-modern-standards-shaping-the-agentic-era)  
13. Toulmin Model of Argumentation.pdf \- UTSA, accessed on December 15, 2025, [https://www.utsa.edu/twc/documents/Toulmin%20Model%20of%20Argumentation.pdf](https://www.utsa.edu/twc/documents/Toulmin%20Model%20of%20Argumentation.pdf)  
14. Toulmin Argument \- Purdue OWL, accessed on December 15, 2025, [https://owl.purdue.edu/owl/general\_writing/academic\_writing/historical\_perspectives\_on\_argumentation/toulmin\_argument.html](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/toulmin_argument.html)  
15. H-DDx: A Hierarchical Evaluation Framework for Differential Diagnosis \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2510.03700v1](https://arxiv.org/html/2510.03700v1)  
16. Explainable differential diagnosis with dual-inference large language models \- PMC \- NIH, accessed on December 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12021655/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12021655/)  
17. Prompt Injection Attacks on LLM: Medical Diagnosis by Symptom Elaboration, accessed on December 15, 2025, [https://app.readytensor.ai/publications/prompt-injection-attacks-on-llm-medical-diagnosis-by-symptom-elaboration-ksr4AMOeYivy](https://app.readytensor.ai/publications/prompt-injection-attacks-on-llm-medical-diagnosis-by-symptom-elaboration-ksr4AMOeYivy)  
18. How to Use Reflection and Self-Critique in Prompts for Better Outputs: Enhancing AI Responses with Effective Review Strategies, accessed on December 15, 2025, [https://promptwritersai.com/how-to-use-reflection-and-self-critique-in-prompts-for-better-outputs/](https://promptwritersai.com/how-to-use-reflection-and-self-critique-in-prompts-for-better-outputs/)  
19. Prompt Declaration Language \- IBM, accessed on December 15, 2025, [https://ibm.github.io/prompt-declaration-language/](https://ibm.github.io/prompt-declaration-language/)  
20. IBM/prompt-declaration-language: Prompt Declaration ... \- GitHub, accessed on December 15, 2025, [https://github.com/IBM/prompt-declaration-language](https://github.com/IBM/prompt-declaration-language)  
21. Tutorial \- Prompt Declaration Language \- IBM, accessed on December 15, 2025, [https://ibm.github.io/prompt-declaration-language/tutorial/](https://ibm.github.io/prompt-declaration-language/tutorial/)  
22. Prompt Declaration Language \- IBM Granite, accessed on December 15, 2025, [https://www.ibm.com/granite/docs/use-cases/prompt-declaration-language](https://www.ibm.com/granite/docs/use-cases/prompt-declaration-language)  
23. CONTRASTIVE THINKING DECODING CAN IMPROVE ANSWERS FOR REASONING MODELS \- OpenReview, accessed on December 15, 2025, [https://openreview.net/pdf/d2b7d2532634db6db5f3ac95c6ec53b2ba8a56fb.pdf](https://openreview.net/pdf/d2b7d2532634db6db5f3ac95c6ec53b2ba8a56fb.pdf)  
24. What is Contrastive prompting and when should you use it?, accessed on December 15, 2025, [https://www.godofprompt.ai/blog/contrastive-prompting](https://www.godofprompt.ai/blog/contrastive-prompting)  
25. Advanced Hallucination Mitigation Techniques in LLMs \- RAG, knowledge editing, contrastive decoding, self-refinement, uncertainty-aware beam search | Towards AI, accessed on December 15, 2025, [https://towardsai.net/p/artificial-intelligence/advanced-hallucination-mitigation-techniques-in-llms-rag-knowledge-editing-contrastive-decoding-self-refinement-uncertainty-aware-beam-search](https://towardsai.net/p/artificial-intelligence/advanced-hallucination-mitigation-techniques-in-llms-rag-knowledge-editing-contrastive-decoding-self-refinement-uncertainty-aware-beam-search)  
26. contrastive decoding improves reasoning in large language models \- arXiv, accessed on December 15, 2025, [https://arxiv.org/pdf/2309.09117](https://arxiv.org/pdf/2309.09117)  
27. Contrastive Thinking Decoding can Improve Answers for Reasoning Models \- OpenReview, accessed on December 15, 2025, [https://openreview.net/forum?id=czozyUMx2M](https://openreview.net/forum?id=czozyUMx2M)  
28. Adaptive Prompting Strategies \- Emergent Mind, accessed on December 15, 2025, [https://www.emergentmind.com/topics/adaptive-prompting-strategies](https://www.emergentmind.com/topics/adaptive-prompting-strategies)  
29. Learning from Contrastive Prompts: Automated Optimization and Adaptation \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2409.15199v1](https://arxiv.org/html/2409.15199v1)  
30. How to Use System 2 Attention Prompting to Improve LLM Accuracy \- PromptHub, accessed on December 15, 2025, [https://www.prompthub.us/blog/how-to-use-system-2-attention-prompting-to-improve-llm-accuracy](https://www.prompthub.us/blog/how-to-use-system-2-attention-prompting-to-improve-llm-accuracy)  
31. Constitutional AI: Harmlessness from AI Feedback — NVIDIA NeMo Framework User Guide, accessed on December 15, 2025, [https://docs.nvidia.com/nemo-framework/user-guide/25.02/modelalignment/cai.html](https://docs.nvidia.com/nemo-framework/user-guide/25.02/modelalignment/cai.html)  
32. Constitutional AI with Open LLMs \- Hugging Face, accessed on December 15, 2025, [https://huggingface.co/blog/constitutional\_ai](https://huggingface.co/blog/constitutional_ai)  
33. Prompt Engineering is behavioural design & why we should stop thinking of it as code | by Charles Anthony Browne \- Medium, accessed on December 15, 2025, [https://medium.com/@charlesanthonybrowne/prompt-engineering-is-behavioural-design-most-people-treat-it-like-code-f08238edf079](https://medium.com/@charlesanthonybrowne/prompt-engineering-is-behavioural-design-most-people-treat-it-like-code-f08238edf079)  
34. LangGraph \- LangChain, accessed on December 15, 2025, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)  
35. LangGraph Beginner's Ultimate Guide: Build Smarter AI Applications \- Veritas Analytica, accessed on December 15, 2025, [https://veritasanalytica.ai/langgraph-ultimate-guide/](https://veritasanalytica.ai/langgraph-ultimate-guide/)  
36. LangGraph 101: Let's Build A Deep Research Agent | Towards Data Science, accessed on December 15, 2025, [https://towardsdatascience.com/langgraph-101-lets-build-a-deep-research-agent/](https://towardsdatascience.com/langgraph-101-lets-build-a-deep-research-agent/)  
37. langgraph/examples/rag/langgraph\_crag.ipynb at main \- GitHub, accessed on December 15, 2025, [https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph\_crag.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_crag.ipynb)  
38. Mitigating Prompt hacking with JSON Mode in Autogen \- Microsoft Open Source, accessed on December 15, 2025, [https://microsoft.github.io/autogen/0.2/docs/notebooks/JSON\_mode\_example/](https://microsoft.github.io/autogen/0.2/docs/notebooks/JSON_mode_example/)  
39. AutoGen to Microsoft Agent Framework Migration Guide, accessed on December 15, 2025, [https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/)  
40. Agno vs LangGraph: Best Framework to Build Multi-Agent Systems \- ZenML Blog, accessed on December 15, 2025, [https://www.zenml.io/blog/agno-vs-langgraph](https://www.zenml.io/blog/agno-vs-langgraph)  
41. LangGraph: Building Self-Correcting RAG Agent for Code Generation \- Learn OpenCV, accessed on December 15, 2025, [https://learnopencv.com/langgraph-self-correcting-agent-code-generation/](https://learnopencv.com/langgraph-self-correcting-agent-code-generation/)  
42. Reflection Agent Prompting: Strategies for More Efficient Performance \- Akira AI, accessed on December 15, 2025, [https://www.akira.ai/blog/reflection-agent-prompting](https://www.akira.ai/blog/reflection-agent-prompting)  
43. Teach Your AI to Reflect for Better Responses \- Relevance AI, accessed on December 15, 2025, [https://relevanceai.com/prompt-engineering/teach-your-ai-to-reflect-for-better-responses](https://relevanceai.com/prompt-engineering/teach-your-ai-to-reflect-for-better-responses)  
44. What Are AI Agent Protocols? \- IBM, accessed on December 15, 2025, [https://www.ibm.com/think/topics/ai-agent-protocols](https://www.ibm.com/think/topics/ai-agent-protocols)  
45. How the Agent2Agent Protocol (A2A) Actually Works: A Technical Breakdown \- Blott Studio, accessed on December 15, 2025, [https://www.blott.com/blog/post/how-the-agent2agent-protocol-a2a-actually-works-a-technical-breakdown](https://www.blott.com/blog/post/how-the-agent2agent-protocol-a2a-actually-works-a-technical-breakdown)  
46. AG-UI Overview \- Agent User Interaction Protocol, accessed on December 15, 2025, [https://docs.ag-ui.com/introduction](https://docs.ag-ui.com/introduction)  
47. LangGraph overview \- Docs by LangChain, accessed on December 15, 2025, [https://docs.langchain.com/oss/python/langgraph/overview](https://docs.langchain.com/oss/python/langgraph/overview)  
48. View of Epistemic Injustice in Generative AI \- AAAI Publications, accessed on December 15, 2025, [https://ojs.aaai.org/index.php/AIES/article/view/31671/33838](https://ojs.aaai.org/index.php/AIES/article/view/31671/33838)  
49. Algorithmic profiling as a source of hermeneutical injustice \- PMC \- NIH, accessed on December 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11741985/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11741985/)  
50. Full article: The Gendered, Epistemic Injustices of Generative AI \- Taylor & Francis Online, accessed on December 15, 2025, [https://www.tandfonline.com/doi/full/10.1080/08164649.2025.2480927](https://www.tandfonline.com/doi/full/10.1080/08164649.2025.2480927)  
51. Epistemic Injustice in Generative AI: A Pipeline Taxonomy, Empirical Hypotheses, and Stage-Matched Governance \- Dialnet, accessed on December 15, 2025, [https://dialnet.unirioja.es/descarga/articulo/10399803.pdf](https://dialnet.unirioja.es/descarga/articulo/10399803.pdf)  
52. C2PA | Verifying Media Content Sources, accessed on December 15, 2025, [https://c2pa.org/](https://c2pa.org/)  
53. 1\. Introduction \- C2PA, accessed on December 15, 2025, [https://c2pa.org/wp-content/uploads/sites/33/2025/10/content\_credentials\_wp\_0925.pdf](https://c2pa.org/wp-content/uploads/sites/33/2025/10/content_credentials_wp_0925.pdf)  
54. Insights into Coalition for Content Provenance and Authenticity (C2PA) \- Infosys, accessed on December 15, 2025, [https://www.infosys.com/iki/techcompass/content-provenance-authenticity.html](https://www.infosys.com/iki/techcompass/content-provenance-authenticity.html)  
55. C2PA Implementation Guidance, accessed on December 15, 2025, [https://spec.c2pa.org/specifications/specifications/2.2/guidance/Guidance.html](https://spec.c2pa.org/specifications/specifications/2.2/guidance/Guidance.html)  
56. C2PA Specifications, accessed on December 15, 2025, [https://spec.c2pa.org/specifications/specifications/2.2/index.html](https://spec.c2pa.org/specifications/specifications/2.2/index.html)  
57. C2PA Explainer :: C2PA Specifications, accessed on December 15, 2025, [https://spec.c2pa.org/specifications/specifications/1.0/explainer/Explainer.html](https://spec.c2pa.org/specifications/specifications/1.0/explainer/Explainer.html)  
58. PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows This manuscript has been authored by UT-Battelle, LLC, under contract DE-AC05-00OR22725 with the US Department of Energy (DOE). The publisher, by accepting the article for publication, acknowledges that the U.S. Government retains a non-exclusive \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2508.02866v2](https://arxiv.org/html/2508.02866v2)  
59. PROV-O: The PROV Ontology \- W3C, accessed on December 15, 2025, [https://www.w3.org/TR/prov-o/](https://www.w3.org/TR/prov-o/)  
60. AI-BOM: Building an AI Bill of Materials \- Wiz, accessed on December 15, 2025, [https://www.wiz.io/academy/ai-security/ai-bom-ai-bill-of-materials](https://www.wiz.io/academy/ai-security/ai-bom-ai-bill-of-materials)  
61. Your Guide to AI Bills of Materials (AIBOMs) \- Snyk, accessed on December 15, 2025, [https://snyk.io/articles/ai-security/ai-bill-of-materials-aibom/](https://snyk.io/articles/ai-security/ai-bill-of-materials-aibom/)  
62. Building an Open AIBOM Standard in the Wild \- arXiv, accessed on December 15, 2025, [https://www.arxiv.org/pdf/2510.07070](https://www.arxiv.org/pdf/2510.07070)  
63. Top LLM Tracing Tools \- Arize AI, accessed on December 15, 2025, [https://arize.com/blog/top-llm-tracing-tools/](https://arize.com/blog/top-llm-tracing-tools/)  
64. A Guide to LangGraph and LangSmith for Building AI Agents \- Analytics Vidhya, accessed on December 15, 2025, [https://www.analyticsvidhya.com/blog/2025/10/a-guide-to-langgraph-and-langsmith-for-building-ai-agents/](https://www.analyticsvidhya.com/blog/2025/10/a-guide-to-langgraph-and-langsmith-for-building-ai-agents/)  
65. 15 AI Agent Observability Tools: AgentOps, Langfuse & Arize \- Research AIMultiple, accessed on December 15, 2025, [https://research.aimultiple.com/agentic-monitoring/](https://research.aimultiple.com/agentic-monitoring/)  
66. Semantic Kernel Agent Architecture | Microsoft Learn, accessed on December 15, 2025, [https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-architecture](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-architecture)  
67. Create an Agent from a Semantic Kernel Template | Microsoft Learn, accessed on December 15, 2025, [https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-templates](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-templates)  
68. Content Credentials: Strengthening Multimedia Integrity in the Generative AI Era \- DoD, accessed on December 15, 2025, [https://media.defense.gov/2025/Jan/29/2003634788/-1/-1/0/CSI-CONTENT-CREDENTIALS.PDF](https://media.defense.gov/2025/Jan/29/2003634788/-1/-1/0/CSI-CONTENT-CREDENTIALS.PDF)