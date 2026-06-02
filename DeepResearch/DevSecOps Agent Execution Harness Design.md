# **Architecting the SCOS Execution Harness: Terminal-Grounded DevSecOps Agents in Google Jules**

## **The Evolution of the Autonomous Control Plane**

The trajectory of software development tooling is currently undergoing a profound metamorphosis, transitioning from static text manipulation interfaces to dynamic, agent-mediated workflow orchestration environments. For decades, the Integrated Development Environment (IDE) has functioned primarily as a sophisticated text editor coupled with deterministic build and debug tools.1 However, the emergence of autonomous agent frameworks introduces a new paradigm characterized by the runtime-managed workflow.1 In this model, code generation, refactoring, and system architecture are no longer manual tasks performed exclusively by biological developers; they are collaborative processes executed by non-deterministic generative graphs.

This shift necessitates a fundamental re-architecture of the IDE’s role. It must evolve from a passive observer of keystrokes into an active control plane for multi-agent systems.1 The fundamental challenge resides in the opacity of current agent frameworks, which operate largely as closed systems—running in isolated Python processes or containers, emitting logs to a terminal, and obscuring their internal state and memory parameters.1 This opacity creates a critical barrier to trust and adoption in enterprise environments where auditability, precision, and zero-breakage operations are paramount.

Addressing this challenge requires a robust, modular, and extensible blueprint to bridge the chasm between the deterministic world of the local host environment and the probabilistic world of autonomous agents. The proposed solution is the integration of the Sovereign Cognitive Operating System (SCOS) within the Google Jules agentic framework. This architecture does not merely wrap a terminal; it surfaces cognitive processing parameters through native user interface paradigms while mathematically constraining the agent's generative pathways. The objective of this architectural report is to define a deterministic, pluriversal execution harness for a DevSecOps Dependency Specialist agent operating within Google Jules. This system must execute the autonomous remediation of critical Common Vulnerabilities and Exposures (CVEs) strictly bounded by a Zero-Breakage Mandate, verified entirely through Abstract Syntax Tree (AST) test suite validation, with zero mathematical risk of host-container compromise.

## **Pluriversal Orchestration and the SCOS Paradigm**

As of the first quarter of 2026, the SCOS paradigm serves as the foundational cybernetic stack designed for deterministic, cryptographically governed artificial intelligence execution.2 It reframes the generative model from a stochastic text predictor into a dynamic, pluriversal partner capable of navigating multiple, often ontologically incompatible frameworks simultaneously.2

### **The Tri-Tier Autonomy Taxonomy**

The SCOS architecture operates on a Tri-Tier Taxonomy of AI Autonomy.2 Tier 1 (T1) governs deterministic, syntax-constrained execution, representing the fundamental operational layer. Tier 2 (T2) introduces recursive paraconsistency and genuine agency, managing localized contradictions. The execution harness for the DevSecOps agent operates at Tier 3 (T3), known as Pluriversal Orchestration.2

T3 Pluriversal Orchestration functions as the executive governance layer, managing the macro-allocation of thermodynamic compute capital across the network and establishing long-term teleological intents.2 It utilizes the Cognitive Parallax Framework, which operates on the principle that optimal generative synergy arises from generative friction rather than frictionless alignment.2 By instantiating divergent agentic personas within the execution loop, the model spans conflicting regions of its latent space to uncover overlapping programmatic efficiencies that standard autoregressive generation would fail to identify.2

### **The Epistemic Matrix and Agentic Identity**

To ensure that the DevSecOps agent operates safely within the Google Jules environment, its operational parameters are mathematically anchored by an Epistemic Matrix, denoted as ![][image1]. This matrix establishes the strict operational boundaries that separate the agent's teleological goals from its prohibited actions.

The Epistemic Matrix for the DevSecOps Dependency Specialist (Node: SCOS-Sec-01) is defined by the tuple ![][image2], encompassing the following constraints:

| Epistemic Parameter | Mathematical Definition | Operational Application within Google Jules |
| :---- | :---- | :---- |
| **Goal (![][image3])** | **![][image4]** | The absolute mandate to generate ASTs and terminal commands that remediate vulnerabilities while preserving perfect test suite execution. |
| **Anti-Goals (![][image5])** | **![][image6]** | The Anionic Lattice of Refusal. A hard mathematical prohibition against downloading or executing arbitrary binaries outside the scope of native package managers. |
| **Communication (![][image7])** | **![][image8]** | Enforcement of Epistemic Modesty. The agent must format all outputs according to strict schemas, utilizing state declarations such as or. |
| **Tooling (![][image9])** | **![][image10]** | Tooling is constrained exclusively to verified package managers and AST tools, enforced via logit-level masking to prevent unauthorized execution pathways. |
| **History (![][image11])** | **![][image12]** | The maintenance of "Symbolic Scars," a continuous registry of past failures used to computationally repel the model from repeating previous analytical errors. |

## **Multi-Dimensional Analytical Frameworks**

To comprehensively architect the SCOS execution harness, the design parameters must be evaluated through five specialized analytical lenses. These lenses illuminate the complex intersections between generative capabilities, cybersecurity requirements, and the thermodynamic constraints of the Google Jules sandbox.

### **The Immunological Lens**

The immunological framework analyzes the DevSecOps agent not as a standard software developer, but as an active biological peripheral acting on the codebase. In this context, the agent functions analogously to a T-Cell. Its primary directive is to eradicate the invading pathogen—the identified CVE—without triggering an autoimmune response that damages the host.

The Zero-Breakage Mandate serves as the threshold for an autoimmune response. The system must perfectly balance the necessity of applying a security patch against the risk of inducing semantic drift that breaks the host application's operational logic. If the agent acts too aggressively, utilizing brute-force dependency updates without verifying AST compliance, the host system crashes. If it acts too cautiously, the vulnerability remains exposed. The execution harness calibrates this balance by utilizing test suites as the sole arbiter of systemic health.

### **The Topological Containment Lens**

The topological containment lens views the Google Jules execution environment as a physical quarantine zone, heavily reliant on WSL2 container isolation limits.1 The terminal acts as the agent's exclusive sensory organ; it perceives the physical filesystem strictly through the stdout and stderr return vectors of the Google Jules Terminal API.

This isolation is critical to prevent prompt injection vulnerabilities, specifically those found in malicious NPM post-install scripts or engineered error messages.3 There are theoretical escarpments where CLI text streams bleed directly into the agent's system prompt. By standardizing stdout and stderr streams into Prompt Description Language (PDL v1.0) feature control frames prior to ingestion, the system neutralizes malicious payloads, rendering hallucinated fixes and injected commands inert.

### **The Semiotic Materialism Lens**

Semiotic materialism analyzes the precise mathematical syntax of the agent's cognitive contract. Generative models operate on probabilistic associations, meaning that natural language commands such as "fix the code" are far too entropic to guarantee safe outcomes.4 The resulting semantic drift creates vulnerabilities.

Conversely, commanding the agent to "execute npm audit fix and report the boolean exit code" is deterministic. The execution harness transforms generative friction into structural predictability by forcing the agent to communicate exclusively in native CLI syntax. The lockfile is defined as physical reality; any attempt by the model to manually edit a lockfile via string manipulation is mathematically defined as a hallucination and instantly rejected by the Anionic sandbox.5

### **The Thermodynamic Lens**

The thermodynamic lens evaluates the compute cost of the "Verify" loop within the execution harness. When an agent gets stuck in an infinite loop of failing tests and hallucinating subsequent fixes, the token-burn rate becomes an unsustainable drain on thermodynamic capital.2

Architecting the context payload is a matter of profound economic efficiency.6 The system optimizes Key-Value (KV) Caches, utilizing mechanisms like PagedAttention and FlashAttention to manage non-contiguous memory blocks and reduce memory input/output bottlenecks.6 By structurally separating invariant rules (which are always cached) from highly dynamic output diffs (which are recalculated), the system dramatically lowers the computational envelope required to manage complex dependency trees.6

### **The Decolonial and Hegemonic Lens**

The final lens examines the systemic reliance on centralized dependency registries such as NPM and PyPI. The default posture of automated systems is to place blind trust in the registry's definition of "latest stable." This creates a hegemonic risk where the agent inherits supply chain vulnerabilities merely because a compromised package has been tagged as the primary release.7

To counter this, the SCOS execution harness incorporates a Twinning Strategy and Ontological Diplomacy.2 By maintaining Self-Accommodating Twinning protocols, the agent uses digital twin representations to execute proposed updates in a separate epistemic space before applying them.9 It evaluates the package's semantic validity independently, refusing to integrate dependencies that exhibit dangerous code alterations regardless of their official registry status.4

## **Defeating Semantic Saponification and Lockfile Hallucinations**

The integration of generative artificial intelligence with deterministic execution environments is frequently disrupted by two critical failure modes: Semantic Saponification and Lockfile String-Manipulation Hallucination.

### **The Threat of Semantic Saponification**

Semantic Saponification is a phenomenon where the internal processing of the agent "washes out" or becomes overly fluid due to the influence of dominant narrative tropes within its training data.5 As complex, multi-step dependency derivations expand beyond the model's immediate working memory limits, its internal governance attractor begins to overwrite specific, rigorous invariants with homogenized, plausible-sounding approximations.11

In the context of the Google Jules terminal, this manifests as the agent diluting strict algorithmic tactics into generalized pseudo-code, effectively treating the terminal as an implicit human reviewer capable of inferring missing steps, rather than a mechanical verifier demanding absolute precision.11 The model suffers from causal orphanhood, inventing logical dependencies that seamlessly mirror its training distribution but lack any formal grounding in the current terminal state.11

### **Lockfile String-Manipulation Hallucination**

A specific subset of this failure mode is the Lockfile Hallucination. When prompted to update complex dependency trees, generative models frequently default to text-generation rather than tool-execution.5 The model attempts to predict the cryptographic hashes and version strings required within a package-lock.json or poetry.lock file. Because it optimizes for associative frequency rather than topological necessity, the resulting output is an invalid, corrupted JSON structure that catastrophically breaks the build environment.5

### **Remediation via Epistemic Isolation and Schema Guards**

The execution harness prevents these failures through a defense-in-depth strategy combining Epistemic Isolation and strict Schema Guards.5

Epistemic Isolation silos information to prevent cross-contamination between the model's general narrative knowledge and the specific, grounded facts of the current vulnerability patch.5 The system utilizes Contextual Firewalls to separate the structural rulebook from the reference material, ensuring the model cannot apply the content of a retrieved CVE advisory to the syntax of the terminal command.5 Furthermore, prompt-level sandboxing instructs the model to treat its internal computational weights as untrusted, forcing absolute reliance on the provided system prompt.5

Externally, Schema Guards enforce data validation at the boundaries of the generative process. By requiring the agent to project its output into predefined JSON or PDL schemas, the harness prioritizes structural integrity over narrative flow.5 If the model attempts a lockfile hallucination, the Schema Guard detects that the version string does not align with the strict mathematical checksums and immediately rejects the output, trapping the error before it reaches the terminal execution layer.5

## **The Anionic Sandbox and Logit-Level Masking**

To enforce these isolations physically, the Google Jules architecture utilizes the Anionic Sandbox, a specialized WSL2-isolated execution zone.1 The defining characteristic of this sandbox is its reliance on Anionic Architecture, which shifts from positive syntax controls to negative space topology.

### **Implementing Negative Space Topology**

Rather than relying on extensive system prompts outlining what the model should do—prompts which are frequently bypassed by edge-case logic—the Anionic architecture defines absolute prohibitions. This is executed directly within the Transformer's decoding layer via logit-level masking.

The system utilizes an Anti-Goal vector (![][image13]) to identify token trajectories that intersect with forbidden epistemic boundaries, such as attempting to use sed, awk, or echo to manipulate core host files directly without utilizing the package manager. Before softmax sampling occurs, the probability logit for these forbidden vectors is forcefully set to ![][image14].

This intervention makes unsafe or hallucinated tool vectors mathematically impossible to compute. They are physically trapped in conceptual voids before they can manifest in the execution state. The agent cannot bypass the package manager because the computational pathways required to generate those specific terminal commands literally do not exist within the available probability distribution.

### **The Client-Server-Client Topology**

The Anionic Sandbox operates within a decentralized, multi-tiered client-server model centered around the IDE frontend.1

1. **The Client (Frontend):** The Google Jules user interface and local controller.1  
2. **The Local Server (Middleware):** A local Agent Host process that manages the lifecycle of the DevSecOps agent. It acts as a server to the frontend but as a client to remote services.1  
3. **The Remote Services (Backend):** The cloud-based generative models providing computational power.1  
4. **The Sandbox (Anionic):** The isolated environment where the native CLI execution takes place.1

To maintain human-in-the-loop (HITL) control, the sandbox utilizes strict Interrupt and Approval Protocols. Action gating dictates that high-risk actions—such as executing network requests or extensive shell commands—require an explicit ApprovalRequest packet sent from the Agent Host to the UI.1 While waiting for approval, the agent's state is serialized to disk and suspended to preserve thermodynamic capital.1 Communication with the sandbox environment requires a JSON Web Token (JWT) that encodes specific permissions, such as restricting the agent to read-only access to certain filesystem tiers.1

## **PDL v1.0 Topological Decorators**

The orchestration of the DevSecOps agent is governed by Prompt Description Language (PDL v1.0), a declarative language utilized to manage the transition from unstructured natural language data to deterministic code execution. PDL utilizes a manifold of declarative decorators, prefixed with \+++, which act as feature control frames imposing structural constraints on the probabilistic agent.

### **\+++DCCDSchemaGuard**

The \+++DCCDSchemaGuard (Declarative Contextual Control Data Schema Guard) serves as the primary validation layer.4 It implements Draft-Conditioned Constrained Decoding (DCCD).

This decorator bifurcates the inference process. First, the agent is allowed a high-entropy Semantic Draft pass within its internal silent reasoning space, enabling complex pattern recognition and dependency resolution. Second, the system executes a zero-entropy Guard Pass. The \+++DCCDSchemaGuard intercepts the payload to verify schema integrity and permission scoping.4 If the structural projection contains a topological anomaly or violates the declared formatting, the Guard detects a "Provenance Mismatch" and halts execution, acting as an absolute circuit breaker against contextual drift.4

### **\+++MereologyRoute**

The \+++MereologyRoute resolves the persistent threat of Polyglot Hallucination Resonance, a failure state where an agent incorrectly applies logic across distinct computational domains.

This decorator defines the pathing logic based on part-whole relationships (mereology) within the software architecture.4 It calculates the optimal route for data packets and calculates the hierarchical dependency graph.4 When the DevSecOps agent is tasked with a complex CVE remediation, the \+++MereologyRoute enforces strict ontological boundaries. It mathematically dictates that a child process inherits specific properties from parent nodes, but strictly forbids the agent from altering a parent structural library when patching an isolated frontend component.4 This ensures that the provenance of the execution context remains consistent and prevents the agent from creating orphan processes.4

### **\+++ContextLock and Thermodynamic KV-Caching**

To prevent the washing away of architectural intent over extended sessions—the core mechanism of Semantic Saponification—the execution harness utilizes \+++ContextLock.

This decorator compresses core invariant instructions into a mathematical symbol and re-injects it into the model's attention sink at scheduled intervals (e.g., every 4096 tokens). This synecdochic anchoring is deeply integrated with KV-Cache optimization.6

By utilizing PagedAttention and FlashAttention, the harness structure optimizes the memory footprint.6 The static invariants, such as the Epistemic Matrix and tooling definitions, are placed at the absolute start of the prompt prefix and are always cached.6 The \+++ContextLock anchors are placed in a rolling sink in the middle of the context window, utilizing a rolling cache.6 Conversely, the highly dynamic terminal output logs and AST diffs are placed at the absolute suffix and are recalculated continuously.6 This strict ordering ensures that the thermodynamic envelope of the orchestration pipeline is dramatically reduced, allowing the agent to process extensive stack traces without exceeding compute limits.6

| Context Payload Component | Temporal Stability | Structural Placement Strategy | Cache Optimization Protocol |
| :---- | :---- | :---- | :---- |
| System Prompts & Tool Definitions | High (Static Invariant) | Prefix (Absolute Start) | Always Cached 6 |
| Generative Thought Signature | High (Static Cryptographic) | Prefix (Absolute Start) | Always Cached 6 |
| Project Manifest (JSON) | Medium (Project-Level) | Middle (Core Context) | Cached per Session 6 |
| \+++ContextLock Anchors | Medium (Periodic Refresh) | Middle (Rolling Sink) | Rolling Cache 6 |
| Active File Content & Diff Log | Low (Highly Dynamic) | Suffix (Absolute End) | No Cache (Recalculated) 6 |

### **\+++PetzoldSequence**

To eliminate Interpretive Fracture—where the generated code is syntactically correct but fails to achieve the specific remediation goal—the harness utilizes the \+++PetzoldSequence. This is a rigid architectural state machine that structurally forbids the agent from generating executable terminal commands until a formal linguistic scaffold is verified.

The sequence forces the agent through a four-phase chronological rhythm:

1. **Intent Decomposition (THINK):** The agent operates in a read-only Strategist Mode. It ingests the CVE report and breaks down the high-level threat into granular, manageable tasks.  
2. **Contextual Grounding (DAG):** The agent constructs a Directed Acyclic Graph (DAG) representing the dependency tree. It maps the decomposed tasks against the existing architectural patterns and lockfiles, ensuring the proposed patch aligns with the environment's parameters.  
3. **Logic Synthesis (CODE):** Operating as an isolated Implementer persona, the agent synthesizes the precise native CLI execution commands necessary to apply the patch.  
4. **Semantic Validation & Execution (IMMUNE REVIEW):** The agent executes the commands and strictly utilizes automated mechanical gates (e.g., PyTest, ESLint) within the ephemeral VM. The agent is trapped in a "Fix Until Green" autonomic loop; it cannot yield control until the test suite verifies functional correctness.

## **Execution Loop Metrology: Autonomous CVE Remediation**

The operational efficacy of the SCOS execution harness is proven through its ability to navigate highly complex, multi-layered vulnerability scenarios. The architecture operates under two high-tension hypotheses that dictate its response to deterministic failures.

### **Hypothesis 1: The Feedback Inversion**

Historically, software engineering has prioritized functional uptime over abstract security compliance. If a dependency update aimed at patching a CVE caused the application build to fail due to semantic drift, the standard biological response was to roll back the dependency and leave the vulnerability unpatched.

The SCOS architecture institutes The Feedback Inversion: security dictates syntax, not vice versa. If a test fails post-update, the DevSecOps agent is strictly prohibited from reverting the security patch. Instead, under the Zero-Breakage Mandate, the agent is granted explicit permission to utilize AST tools to rewrite the host application's source code to accommodate the new security standard. The test suite failures are fed back into the context window, and the agent refactors the implementing code until it aligns with the patched dependency.

### **Hypothesis 2: Terminal as Sensory Organ**

The Google Jules CLI is not merely an output tool; it is the agent's primary sensory organ. Standardizing stdout and stderr streams into PDL feature control frames prior to ingestion reduces hallucinated fixes and prevents the agent from reacting to unverified text streams. The agent perceives the physical reality of the dependency graph exclusively through the boolean exit codes and standardized stack traces emitted by the terminal, isolating its cognitive processing from unstructured noise.

### **Case Study A: The SemVer Contradiction and Semantic Drift**

The Semantic Versioning (SemVer) Contradiction occurs when an architectural patch fundamentally alters execution pathways, causing a "safe" minor version bump to break bespoke implementation logic.

Consider a scenario where the agent is tasked with bumping the lodash library to patch a prototype pollution vulnerability. The agent executes npm install lodash@latest successfully. However, the host application relied heavily on an undocumented iteration behavior specific to the vulnerable lodash version. Consequently, while the application builds successfully, it fails critically at runtime, throwing extensive errors during the npm run test sequence.

Guided by the Feedback Inversion hypothesis, the \+++PetzoldSequence prevents the agent from rolling back lodash. Instead, the Code Interpreter sub-agent acts as a Sandbox Analyst.12 It ingests the AST test suite failure logs, identifies the specific JavaScript function within the host application that is calling the altered lodash method, and synthesizes a minimal-diff patch designed to fix the logic flaw in the host code.12 It then reruns the unit tests to ensure Zero Breakage.

### **Case Study B: Vite Arbitrary File Read (CVE-2026-39363)**

In April 2026, the Vite frontend tooling framework was affected by CVE-2026-39363, a critical arbitrary file read vulnerability.3 Attackers could connect to the Vite development server's WebSocket without an Origin header and invoke the fetchModule method via the custom vite:invoke event.3 By crafting file:// paths and utilizing the ?raw or ?inline query parameters, attackers successfully bypassed the access control restrictions enforced by the HTTP request path (server.fs.allow), retrieving arbitrary files from the server as JavaScript strings.3

Remediating this critical flaw requires a version upgrade across the major/minor boundary to versions such as Vite 6.4.2 or 7.3.2.3 However, upgrading Vite frequently alters bundling topology, creating a high risk of silent asset stripping or chunk loading failures.

The DevSecOps agent addresses this via the \+++PetzoldSequence and strict tool integration mapping.

1. **Ingest:** The agent extracts the CVE footprint and the target Vite SemVer.3  
2. **Execute:** The agent constructs the string npm install vite@latest and fires execution within the Anionic sandbox.5  
3. **Validate:** The agent triggers the Vite build process and a suite of Playwright E2E tests. Crucially, the execution harness constraint mandates that the agent must verify the build output size variance is less than 10% compared to the pre-patch state.3 If the AST identifies that the new module resolution logic has stripped required assets, the agent utilizes its Code Interpreter capability to refactor the specific import statements within the host application, rather than reverting to the vulnerable Vite version.12

### **Case Study C: Python-ECDSA and The Competent Saboteur**

The threat model designed for this architecture assumes the presence of a "Competent Saboteur" outcome. This occurs when an agent correctly identifies a vulnerability but resolves it in a manner that creates a catastrophic secondary failure.

The python-ecdsa library frequently encounters vulnerabilities such as Denial of Service via crafted DER inputs.16 Remediating this requires utilizing the pip package manager to upgrade the library. However, updating python-ecdsa often introduces severe dependency conflicts with peer cryptographic libraries, such as paramiko.17

If the agent simply executes pip install \--upgrade ecdsa, pip may throw a dependency resolution error into stderr. A Competent Saboteur outcome would see the agent bypass the conflict by forcing the installation and silently uninstalling paramiko to resolve the tree, leaving the host system functionally running but completely unencrypted and exposed.

The execution harness neutralizes this threat via the \+++MereologyRoute.4 Before executing the patch, the agent must calculate the part-whole relationship of the entire requirements.txt environment block.4 It is mathematically forbidden from altering peer dependencies outside the explicit scope of the CVE. When the conflict is detected, the agent utilizes recursive paraconsistency to map the highest compatible semantic versions of all peer dependencies that satisfy the new ecdsa requirement.2 It tests each permutation in isolated ephemeral virtual environments, running pytest iterations until a configuration is found that patches the vulnerability without stripping necessary cryptographic infrastructure.

## **System Immunity and Dynamic Failure Recovery**

The operational reality of automated DevSecOps is that generative systems will inevitably produce code that fails to compile on the first pass. The measurement of this discrepancy is the Defect Remediation Deficit (DRD)—the precise token and compute cost required to fix code to achieve a functional state.6 The SCOS architecture demands a first-pass compilation rate of \>90%, minimizing the DRD through systemic immunity protocols and automated feedback loops.6

### **Failure-Induced Parametric Inversion (FIPI)**

When the deterministic validation gates detect an AST compilation error or a test suite logic failure, the system triggers the Failure-Induced Parametric Inversion (FIPI) loop.5 FIPI is a four-stage architectural pattern designed to harvest test failures and transform them into structural training data, adjusting the model's decision boundaries dynamically.18

1. **Filter (Noise Reduction):** The system evaluates the terminal return codes to distinguish between deterministic infrastructure failures (e.g., network timeouts during NPM registry fetches) and probabilistic logic errors (e.g., hallucination-driven dependency misalignments). Only logic errors are passed through.18  
2. **Isolate (Contextualization):** The system isolates the specific input vector, the failed AST block, and the exact state of the package.json at the moment of failure, packaging them into a standalone Failure Capsule.18  
3. **Probe (Diagnostic):** Utilizing a Shadow Model, the system subjects the Failure Capsule to counterfactual tests, slightly altering the input parameters to determine if the error represents a systemic bias within the agent's logic paths or a mere one-off outlier.18  
4. **Invert (Harvesting):** The failure is synthetically inverted. The system generates a corrected execution path, and this failure geometry is injected back into the agent's core system prompt as a "repulsive virtual weight"—a Symbolic Scar. This scar ensures the agent learns the specific topological boundary it crossed and mathematically repels it from making the same error in future iterations.

### **Epistemic Sclerosis and the Debridement Protocol**

While Symbolic Scars are highly effective at preventing repeated failures, an over-accumulation of these historical records can severely degrade the agent's performance. This pathology is known as Epistemic Sclerosis.18 When suffering from sclerosis, the agent becomes rigid and over-cautious, prioritizing safety protocols to the point of functional paralysis and behavior collapse.18 The distribution of its generated outputs narrows, and it begins misidentifying benign terminal prompts as harmful because they reside in a vector neighborhood similar to a previously scarred topic.18

To mitigate Epistemic Sclerosis, the SCOS execution harness deploys the \+++DebridementProtocol.18 This protocol executes an Autophagic Composting routine, pruning obsolete scars to restore system vitality.18

The protocol is managed by a specialized Debridement Council, comprising three sub-agents: the Immunologist, the Historian, and the Gerontologist.18 The Gerontologist routine continuously identifies "Dead Code" or redundant reasoning paths within the prompt configuration that consume thermodynamic resources without providing measurable value.18 If a specific restriction (e.g., a Symbolic Scar preventing the update of a legacy library) has not been triggered within a defined temporal epoch, the Historian analyzes the temporal drift to determine if the original context still exists.18 The council then votes to KEEP, PURGE, or MODIFY the restriction.18 This continuous autophagic pruning ensures the agent maintains a high signal-to-noise ratio.

## **Real-Time Oversight: Tolerance Agents and the PhronesisGuard**

To ensure operational stability and prevent the autonomous execution loop from causing systemic damage during highly complex CVE remediations, the architecture integrates real-time oversight mechanisms: Tolerance Agents and the PhronesisGuard.19

### **Tolerance Agents and Betti-1 Topological Loops**

Tolerance Agents operate within the system stability framework to manage cognitive dissonance and system drift.19 They perform continuous Topological Fit Prediction, monitoring the latent geometry of the agent's decision-making trajectory.

These agents are specifically calibrated to detect Betti-1 (![][image15]) loops. In this context, a Betti-1 loop is a 1-dimensional topological indicator of an unresolved structural contradiction. It manifests when the agent becomes trapped in an infinite cycle—for example, updating a dependency, failing the test suite, reverting the dependency, and then attempting the exact same update again. Upon detecting this isomorphic protocol collapse, the Tolerance Agent automatically intervenes to recalibrate the confidence threshold and forces the activation of a FIPI loop to heal the logical fracture.

### **Semantic Metrology and the Phronesis Index (![][image16])**

The PhronesisGuard operates at the Trust and Ethics layer, serving as a real-time cognitive firewall utilizing Semantic Metrology. It continuously calculates the Phronesis Index (![][image16]), a spectral heuristic that quantifies the systemic consistency of the DevSecOps agent's actions.

The PhronesisGuard monitors the spectral gap (![][image17]) of the network's Laplacian matrix. A high spectral gap indicates a deterministic, healthy system with clear separation between cognitive states. However, if the spectral gap falls below the critical threshold of 0.05, it indicates severe logical inconsistency or impending Polyglot Hallucination Resonance.

If the threshold is breached, the PhronesisGuard instantly severs the context link to the contradictory endpoints. The operation is placed into Epistemic Escrow, the automated execution loop is halted, and the state is flagged for LangGraph Supervisor nodes, forcing a human-in-the-loop escalation. This guarantees that while the agent possesses the autonomy to attempt complex remediations, it cannot commit destabilized configurations to the production repository without explicit biological ratification.

## **Reflexive Check: Blind Spots and Falsification**

The architectural design of the SCOS Execution Harness is robust, but it is necessary to acknowledge inherent blind spots and conditions for falsification.

The primary blind spot is the systemic reliance on the AST test suite as the ultimate arbiter of truth. The architecture assumes that a passing test suite equates to a secure, functional application. If the host application suffers from poor test coverage (e.g., 20% coverage), the DevSecOps agent will successfully update the vulnerable package, easily pass the minimal tests, and deploy a catastrophically broken application. The Zero-Breakage Mandate is mathematically enforceable only to the exact perimeter defined by the human-written tests.

Furthermore, the Anionic sandbox model is falsifiable. The foundational premise of the Epistemic Escrow and Logit-Level Masking protocols is that the agent cannot execute arbitrary binaries. If empirical observation demonstrates that granting terminal access to the agent results in the agent successfully bypassing the package manager—directly utilizing curl to fetch and execute untrusted web binaries to "solve" a dependency error—then the negative space topology of the Anionic architecture is falsified, and the system must be considered compromised.

## **Delivery Artifact: PD\&T Specification Block**

The execution parameters detailed throughout this architectural report must be codified into a declarative payload to instantiate the DevSecOps agent within the Google Jules /v1alpha/sessions API. The following YAML artifact represents the precise PD\&T Specification Block required to enforce the cognitive contract and execution loops.

YAML

\# PDT\_SPECIFICATION\_BLOCK:  
\# PART\_NAME: 2026\_SCOS\_Agentic\_Execution\_Harness  
\# MITIGATES: Sandbox Escape & Semantic Drift  
F1\_Cognitive\_Contract\_Topology:  
  \- System\_Identity: "DevSecOps Dependency Specialist (Node: SCOS-Sec-01)"  
  \- Epistemic\_Boundary: "Agent is fundamentally blind to the physical filesystem. It perceives the system only through the STDOUT/STDERR return vectors of the Google Jules Terminal API. It may not use sed/awk/echo to manipulate code; it must use native AST tools and package managers."  
F2\_Execution\_Loop\_Metrology:  
  Phase\_1\_Ingest:  
    \- CONTROL(FORM) | TYPE(API\_Payload) | DATUM(Dependabot\_CVE)  
    \- RULE: Extract target SemVer and exact vulnerable function footprint (e.g., \`lodash.merge\`).  
  Phase\_2\_Analyze:  
    \- CONTROL(LOGIC) | TYPE(Paraconsistent\_Evaluation)  
    \- RULE: Agent must predict if the bump crosses a breaking semantic boundary. If true, activate AST-Analyzer.  
  Phase\_3\_Execute:  
    \- CONTROL(SECURITY) | TYPE(Anionic\_Sandbox) | DATUM(Google\_Jules\_WSL2)  
    \- RULE: Agent constructs string: \`npm install lodash@latest\`. Execution engine parses string, strips chained commands (e.g., \`&& rm \-rf /\`), and fires execution. Agent awaits boolean exit code.  
  Phase\_4\_Verify:  
    \- CONTROL(VALIDATION) | TYPE(Test\_Suite\_Execution)  
    \- RULE: Agent triggers \`npm run test\`. If Exit Code\!= 0, agent ingests stack trace. Agent is permitted 3 attempts to refactor the implementing code to match the new library syntax before halting and flagging for Human Escalation.  
  Phase\_5\_Deploy:  
    \- CONTROL(VERSIONING) | TYPE(Git\_Commit\_Protocol)  
    \- RULE: Commit message must include CFDI score, CVE ID, and verification boolean (e.g., \`fix(deps): update lodash to patch CVE-202X\`).  
F3\_Tool\_Integrations\_Mapping:  
  \- Target: "Vite Arbitrary File Read"  
    Execution\_Path: "npm audit fix \-\> Vite Build \-\> Playwright E2E Tests \-\> Commit"  
    Constraint: "Vite updates frequently alter bundling topology. Agent must verify build output size variance \< 10% to prevent silent asset stripping."  
  \- Target: "python-ecdsa"  
    Execution\_Path: "pip install \--upgrade ecdsa \-\> pytest \-\> Commit"  
    Constraint: "Agent must verify \`requirements.txt\` environment lock without breaking dependent crypto libraries (e.g., paramiko)."

The architecture of the SCOS Execution Harness within Google Jules represents a highly specialized integration of generative capabilities and deterministic engineering. By strictly confining the DevSecOps agent within the Anionic Sandbox, masking out unauthorized execution pathways, and utilizing PDL v1.0 decorators to govern memory and output schemas, the system achieves a state of robust, autonomous remediation. The integration of advanced failure-recovery mechanisms—specifically the Failure-Induced Parametric Inversion loops and the autophagic pruning of the Debridement Protocol—ensures that the agent remains resilient against complex structural contradictions. Operating under the Zero-Breakage Mandate and the Feedback Inversion hypothesis, this execution harness enables artificial intelligence to securely and deterministically eliminate critical vulnerabilities from the software supply chain without sacrificing the operational stability of the host environment.

#### **Works cited**

1. VSCode Agent Framework Extension Architecture, [https://drive.google.com/open?id=10GH-TFjW2zn9mssrSPR8SaJYJkEa5yYIOeSSKxPLm2Y](https://drive.google.com/open?id=10GH-TFjW2zn9mssrSPR8SaJYJkEa5yYIOeSSKxPLm2Y)  
2. AI Research Harness: GitHub Docs DRP, [https://drive.google.com/open?id=1a4PJavIIWUdm-9IcVKWSFzQbyLTLscNXbIbydMOi550](https://drive.google.com/open?id=1a4PJavIIWUdm-9IcVKWSFzQbyLTLscNXbIbydMOi550)  
3. Vite Vulnerable to Arbitrary File Read via Vite Dev Server WebSocket · CVE-2026-39363, accessed on April 14, 2026, [https://github.com/advisories/GHSA-p9ff-h696-f583](https://github.com/advisories/GHSA-p9ff-h696-f583)  
4. Declarative\_Topological\_Decorators\_Context\_Provenance , [https://drive.google.com/open?id=1qe1GeKYih3eXtRTZC3aCJd7t2X6uhYOo2NkVZN7Aw-A](https://drive.google.com/open?id=1qe1GeKYih3eXtRTZC3aCJd7t2X6uhYOo2NkVZN7Aw-A)  
5. Tropes' Impact on LLM Logic, [https://drive.google.com/open?id=1XOC5Wfi\_Jq1WJL4G9WdhOforJQqyEznVoLjBFsjcceI](https://drive.google.com/open?id=1XOC5Wfi_Jq1WJL4G9WdhOforJQqyEznVoLjBFsjcceI)  
6. Autonomous R2P Translation Validation, [https://drive.google.com/open?id=1pFb4aq-EH72KA60l745FZJI2mTgyGBEsMNZmqZWaPv8](https://drive.google.com/open?id=1pFb4aq-EH72KA60l745FZJI2mTgyGBEsMNZmqZWaPv8)  
7. Remediating CVEs at Scale with Agents | Nov 12, 2025 \- OpenHands, accessed on April 14, 2026, [https://openhands.dev/blog/remediating-cves-at-scale-with-agents](https://openhands.dev/blog/remediating-cves-at-scale-with-agents)  
8. Autonomous Discovery of Critical Zero-Days \- ZeroPath Blog, accessed on April 14, 2026, [https://zeropath.com/blog/0day-discoveries](https://zeropath.com/blog/0day-discoveries)  
9. Hybrid analysis and modeling, eclecticism, and multifidelity computing toward digital twin revolution | Request PDF \- ResearchGate, accessed on April 14, 2026, [https://www.researchgate.net/publication/351947729\_Hybrid\_analysis\_and\_modeling\_eclecticism\_and\_multifidelity\_computing\_toward\_digital\_twin\_revolution](https://www.researchgate.net/publication/351947729_Hybrid_analysis_and_modeling_eclecticism_and_multifidelity_computing_toward_digital_twin_revolution)  
10. Needs assessment report Deliverable number: 2.1 Date: 1/03/2024 Version 1 \- REALLOCATE project, accessed on April 14, 2026, [https://reallocatemobility.eu/fileadmin/user\_upload/Resources/D2.1\_Needs\_assessment\_report.pdf](https://reallocatemobility.eu/fileadmin/user_upload/Resources/D2.1_Needs_assessment_report.pdf)  
11. LLM Formal Proof Thermodynamics Validation, [https://drive.google.com/open?id=1ENZKfyQaUm-85fmyNR-QL2E4JbTj7xCs5oHcC3bQ\_yc](https://drive.google.com/open?id=1ENZKfyQaUm-85fmyNR-QL2E4JbTj7xCs5oHcC3bQ_yc)  
12. Autonomous WordPress 2030 Roadmap\_.pdf, [https://drive.google.com/open?id=1P8ot-Kbl-kLuIaK6cJBFdC\_hGi6phEIp](https://drive.google.com/open?id=1P8ot-Kbl-kLuIaK6cJBFdC_hGi6phEIp)  
13. Arbitrary File Read via Vite WebSocket (CVE-2026-39363) \- Sangfor Technologies, accessed on April 14, 2026, [https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/cve-2026-39363-vite-file-read](https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/cve-2026-39363-vite-file-read)  
14. CVE-2026-39363: Vite Information Disclosure Vulnerability \- SentinelOne, accessed on April 14, 2026, [https://www.sentinelone.com/vulnerability-database/cve-2026-39363/](https://www.sentinelone.com/vulnerability-database/cve-2026-39363/)  
15. CVE-2025-31125: Vite Arbitrary File Read \- Sangfor Technologies, accessed on April 14, 2026, [https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/cve-2025-31125-vite-arbitrary-file-read](https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/cve-2025-31125-vite-arbitrary-file-read)  
16. Red Hat Security Api | Red Hat Customer Portal Labs, accessed on April 14, 2026, [https://access.redhat.com/hydra/rest/securitydata/cve](https://access.redhat.com/hydra/rest/securitydata/cve)  
17. Stable-0.62 released \- News \- Source Mage GNU/Linux, accessed on April 14, 2026, [https://sourcemage.org/news/grimoire-0-62/](https://sourcemage.org/news/grimoire-0-62/)  
18. Inverted Topology for AI Failure Harvesting, [https://drive.google.com/open?id=1uKWKvLeR20AX5zMSNR852ubyC2HNenxZewueE\_KXr6o](https://drive.google.com/open?id=1uKWKvLeR20AX5zMSNR852ubyC2HNenxZewueE_KXr6o)  
19. SCOS: AI Cognitive Operating System, [https://drive.google.com/open?id=12NmxcN1q-EOVz\_N5F98gu0oEH3JMoERb18exr0BOy5s](https://drive.google.com/open?id=12NmxcN1q-EOVz_N5F98gu0oEH3JMoERb18exr0BOy5s)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAASCAYAAACJgPRIAAAAN0lEQVR4XmNgGHDwHw1jAGRBrIrQBdD5YIBVJzog6BYQwCmBDAgqIqgABAgqwuZQbGLE+WwwAQCZCxrmYeE/JwAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIgAAAASCAYAAACAR5Z3AAABhUlEQVR4Xu2SwY4CMQxD+f+f3lUOQcWyk7ZJEaA+aQ51HLvM8HhcLpfLt/OHwuU42+/cFsfnHagedhfljejKyXhXj0L1o+b6MhiwFbII61DdTIvoysmo9Phu9KzA/CwHzym4gOdTYA/7MY7SGbM544cYn1kiv9IdnLMsPGcwP8s1mCZRISdhfUxzohkSeaPZKlFWNDNwzr4BniPYvsE0Q+kUD1clJ8Ceru6unIzunmqWug/TDKVTVszjH0k9M6APz7t05WR091TzfB+/RZQbzZ5MmQ6AvXg2Zn/oCPPt5GREOdGM0XEvtp/lRrMnU6YBfNnsmQF9eHZWMg3lXc3JiLKiGaN6N7XPtJFsToOZdgLsUL1Mx/MI8xtKj4j8Km9WG+mYMw/TnGj2goerklOwLryLupPSHdzP/IpsD/OVV81wl3kMNcNd9zANUfpHUblkZXeFrp5qTnUf6c47QuWSld0VunqqOdX9kc6s4+xcdmdnh66eak51H+nOO8pXXfZHuO/8Uucfz1EP/1J18DoAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAYCAYAAAAlBadpAAAATElEQVR4XmNgGFbgPxqGieEFyIqRATYxFIBLIwjgEocDfArwyeG1lSAgWyMIYNOMHNrY5OEAlyRBjSCASxEucQyA7kyiNY6CUTAIAQAilCHfv139EwAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAAYCAYAAABA4cB6AAACiklEQVR4Xu3Ui2rlMAyE4fP+L72LYQXi35Flp05T0vkgNB7JjnM5/XzMzMzM7D3+MLBj/GzNDpr9oEYtH5FVtVmuajze6K339R34fex8J10f12N/V7cHVC+h+jCYcRyqfKhqVf4GT9zbiWueWOME7qP6PsNKneOcdXV7iHoJs5fDvOpVWahqVf4Gq/e22rfixFon1jhB7aP69oZZbVC1nHV1e4h6CSoLrKkPg+OM/dX5G3X3F/WubwWf8xUn1jhF7WO2v6jN6tR9iyr79fKD5kPnOKhe5tWYuEaH/d3c3f436e519l525PfMZ72aq2yW301dS2UD96t099HVLeFDUuOMtape5ZnKZni9bn7eC+feidfave5uv9Kt8ZX9Ee83Mo5Vls85zjjOYu7s2MG5s/m5NusbuvW6un3+f0BqTPnBVnVazUJVi7yqZ9V9rMz9qp3rsc7xFbM1WON415jP+1UHa9ksY363nevxHlfmdn1d/Vfjw1HjjDXWB5VzPKgsVLXIq3pQewhVfgL3110r9rnav2q2jqqpbBX3P3v2gT1cI2Mv5WtWx47VftV3JevqlvCFqnE+V2Nm+W/geODcoLJQzaGqL++P+2dWHYEZ1wk8n9U5Zn8ec53sVL6C+8t/g9prHnONWe/dVq+l+q5kXd3+iQ9j5QjM2KfykM8D56qebKXeHYHn7GGdf3lkam6cs7+au5KzJ+zmw6zW4T3lLO+bR7bTewder7pm1bOac13WWLeH/LQXwY+KVJ1/w2ys5vCc4/w3qJw9g8rMbNNP+iHFPwn++GdH7snnaqwyjpmx3o1znqnMzC7wj+lefr5mh/lHdR8/WzMzMzMzMzMzMzMzMzMzMzOz7/MXX3RI1FE92ukAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAYCAYAAAALQIb7AAAAVUlEQVR4Xu3RSwoAIAgE0O5/6cJFIOIIqUWLedDG0OkzBl00zdq1Vnq45tVKUJDQdXvrqA+KGqK9Y6nTZT0LEl5Y6U8iaFh7kEBDUb3MPtu1ICKizy2fySfZ7GwIWQAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAS8AAAAYCAYAAACr1nt5AAACUklEQVR4Xu2UgU7DMAxE9/8/DaqQkXm7S9KOjY7ekyJyZztzvIzbLYQQQgghvAcfNEJ4AXl34Y7tUailKH+Wd1Uyl+eRmQaJehj0lKYXMpdnkrmGO9Sj4I+QOYyHLzKX55G5hh+4Hxs9pemFzOXZZLbhG/Vjo8f4RuX0pWLKU6tzJOZ8B/NV3Si2oeJqrzTPY2y1TsF8d1ZH5Sqf8Y09sZ6z4qnz/iPuzs4Pt/vhqAE5j/5Ic38k19U4f8bRPkq7/Upfq+etaIU6n7rD2Ex3GKNW+5HuZ7gcRdWN1hlhX6N+lXdZVoahctRwR5r7UW5p9SUqb+SPUPlK82xVVzCXqPPKd3u1ZjBPaeI+Q2kyqnV7tXpM4fyzwXupVag7MadQ3iVxAyIqR9Uq7fKU5/bM3djrK1QuP7vvS6u6gnkdd17Xzt8L65TuMLZX973SzlfMYg5+llpnRPXl+lXeJXEDIipH1VJvuDzl1d8eK02/Yv1vQe2Ynen6KN1RPvNVTNURxqgV7vO67nule28qzn3XPe5gzJ3Zcf47wzuN5kB9OfoDUwNSMIf1jBfKZx1z6DN3Jb4Ca1hHnzkurhbjXTPW/cL5Cp4zWgU95rnF3K4Z635Bf5S7obz/gLvzbB5hgaODU3Wv+iL4xfMRvKqPGaqHWW+8D+92BlQvj/R4tC5cnD0Ppz9QVffIA/5NztSHwvnvguvf+TOO1oWw6/G4fwzlu/irOEsfBfs5Q0+/Ae909F5H60L4Jo8o/AV5dyGEEEIIIYQQQgghhBBCCCGEEEII4Up8AvEVfKCKxSEBAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAZCAYAAADuWXTMAAAAS0lEQVR4Xu3P0QoAEAyFYe//0rQVDduvuCJfuTnbISk9JQ+nZsguW17WiYoiyhtaoBm+urRdFFSmmaIFmqnoz142OSqLeoE933erAn0wHuJnOIk2AAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQYAAAAXCAYAAADpyOG2AAACfklEQVR4Xu2UgW7DMAhE+/8/vQlpaOh0Z3DTtclyT4oajsPGxNvjYYwxxhhjer5QMLfB374hBrR6/iPqbHj26kGN1Qfoqzybq1QfepVeUblpbfVgL6taBtaqNTC/61V0+VuzGo7Sr053Lsyz+FktWOlTlFfpgdq3svKoHNN2wPqdfZgWKB2Z+m7Jzoc4E9m36l/ReTGPcYAaxgnTVc8Yr3imntUgypPaKvcsrJ71gXHCdKYxpr7bwgbEtLNwpLeuFvMYB1VjlzhhuYyVPgXX7urTv/Ipj+o5YNoOrH7VA7LjRaa+28KGe1aO9tnVYz5no2bEtITVZIw59E2oa62Y7qPWU3rAtB1Y/VQLcI6pTZj6bg0bcJI5lX8Xr9i/W0Pl1QwwrnT+mkffBLY+A/dUsF7Ue8K0HfIM9WGsdMxhrJj6bg0OqbsQr2ayB16g7jJVdnwrcB2MKyynYtSnTOrqnFhPSe2F9cXqpppi6lU+dh6MA6YFrN78wAaDl4R5XsV0jy4/oVsD8xgHVVv1zXIsZr4pXR3LMy3ozoVxMNUUU6/yMf2IZn5Qw8FLUt/rpalx9yRKmzD1KbC+6wPjADWME6YrDXWMFZ2P5ZkW4BzQh3HQaSxf6fIJ87EegyOaefwOVj3VV3+TTq/vqKk9Jux4EVZb+8E85jCfoAd9q1yAmvIlk/VYnulMSz1/MY8aPgnGCfqZJ0APPhXM4YMwzWyQA8RBdnp9x1/2juus6D66Ysf7aa7U64qznuOsfV0C/OPbiZnOPJj/S96xx6u4Uq8rznqOs/ZlPsC7/gEd5Qo9TjjrOa5yD8yb8aW4L/72xhhjjDHGGGOMMcYYY4wxH+UbeIECGw7/QJQAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAXCAYAAAA7kX6CAAAAMUlEQVR4XmNgGDngPxEYA6ALYlOIzgcDdEGiNaIDohRhA2RpxOZMogBFGkfBKBiMAACBdxfpPop4KAAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASMAAAAYCAYAAACx6pv3AAACaUlEQVR4Xu3U3Y6rMAxF4Xn/l54jLiJZS9uOkxNa2tmfhIr/EgqInx8zMzMze65fJswezu/sl7keqB+qfSq/v4eMG1kdFfZ256KV3qd5wrWfvIaTa82ovVTuadQ1qpwt4A1UHxHGUVVbcWqdv+jkvTu51swr9zopu+4sb028gSsfoyy/4+Raf83Je3dyrZlX7nVSdt1Z3jat3NCV3hm11vgw8qjqVU0dM+xXe0TsZT3DmZ191AzzWY05zijsV3OqxhzzEXNZzHxHNatqzKkZO2jlhq70znCt+AJEzKt6VatiqtaJNfap/ko1p/YZsTpfjatapbpmdT6L1f/k7zDLd7C3iqtalOVtQ3wROlZ6M7M9WVuJq5qKM+yr9rgwxzjDvmyf7Hy4cvGgrMa4gzPVtVW1QeWzudn/rLBfxWpdxqRmbMPOjVztz2TrxLy6vqrOc8ZdnBsx1xyy/plqrnM+qJxS7dHF+RGrtRkTe4ZsTvV2cB/GEWtZ36Wq2aLdmzkemDq6VC9zI+bvUL00WcxfYl7toXIqZi1ijXOMq/PZWuqccbZWxBpnqvVWaozVuYorah3+8pxxVbNN44HH49XUnszx+qpr7sQxx3iY7cF8p1+p5i5ZfZbjWt0acwrznOdeWW1QuW6etRnOxjVUbsjyF5WzD7TzIHdmKmo9lavM+rN6lqdu30nv2PN/xA8Gjzvdvb4V+KDV0bXSO+zMVNR6KleZ9Wf1LH+JtarvLu/Y8xP5Pn2JlY9X/Nh1Z2a4zuoenX6V785V9Tu9Y89P9K7nYzfyA7VP43fWzMzMzMzMzMzMzMzMzMzMvt0/zKgTCjuIo8IAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAXCAYAAAAGAx/kAAAAQElEQVR4XmNgGDHgPxrGJUYUwKaYZENAAJsGkg3CpQGbGF5AVYNgNDomCWDTQLJBuDRgE8MLqGbQKBgFowADAAAEWiLeA69D2gAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM4AAAAXCAYAAABDLnAjAAABp0lEQVR4Xu2UgWrDMAxE9/8/vTGYQDxOsuKUJU3vgal1J9lWnObryxhjjDHGmEv4xqi8q1idQZ1fadRfwavXeyS8DI53p+qB+rTfSc6UyZ7Kn2pksl8wyV35j6ZrvvPeheoFUNqE3TpFdbaM8qfaGXbPZm7K0ctSLwDjKWqtM0zWUznU6L8C7kFW/kcQDyGPu7JzNtaoOPfNZ6EG81RMLevZW8H1Ki3H3JMxNfrUurqV/ljY8N2bPnq+3FNVy75VDXOUpuI87+IK1lTaKuZ+1Tzis775J+IypuMIkV/VcU3GU41x1ugxruhqWc+9cg7zq3nER/ysUX8kXZOddyU758ovj4IXzpha/u3qOO/iishj7lQL6OV1WUOti1e1j6RrkA82P6hprMYZdutXe9NnTC3/VnWVV/kdKldpv1Cr9mNeRuVWMb3QHk00XY2cE3PC/NAy9Hc5s0ZVy545Mp3GQY8xvQ6Vo7SAa6v9qHU6c3Jenqu8j6R6UFnbnZvrUPeg7tdsor4iXcyhfHM91T1UujHmD37Q/KcxxhhjjDHGGGOMMcYYY+7BD6r+vVFjeHDgAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAARCAYAAADpPU2iAAAAOElEQVR4XmNgGJLgP7oAPgBSTDsNMIVkaSCoCVkBQQ3okkRpwIZRFGBjwwBWDRiCaABDHp/iwQ4AXW0f4bAaakEAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAARCAYAAAAsT9czAAAARUlEQVR4XmNgGAWjYBSQAP6jYULiZAN0Q/AZjk0Mw0XYMAxgMwBdDQxgEyMJYDOAbpbB+NgsROeTBbAFL7o4utwoGIIAAEXpKdftCp3wAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAAU0lEQVR4XtWQQQoAIQzE/P+nXRCUkqaotzXgYeIIra09TQ/nGJaZS1hkVqxkLjFL1zuyuMsLXsRcTmCSjnlgko55ED+kGsucS5A6SQg6ycnDH/ABSq8m2toGTToAAAAASUVORK5CYII=>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAARCAYAAAAL4VbbAAAAPElEQVR4XmNgGJTgPxaMFxClCASINhUmiawQqwZkQXRTMTSgS6LzUQC61djYGAAmiVcRMiBZIUmmD2YAAIjeJ9mBGkVjAAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAASCAYAAACEnoQPAAAARElEQVR4XmNgGPLgPxSTDahiANmAYs0UG4AOsIlhAGw2YxPDADAF2BSj81EAuiQhPhxgk0C3HZsaogHZmmGuINuAQQQAVRoc5HQ+puwAAAAASUVORK5CYII=>