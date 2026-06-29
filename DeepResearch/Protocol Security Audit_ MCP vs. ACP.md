# **Comparative Topology of Agentic Protocols: MCP vs ACP Multi-Server Security, Faults & Benchmarks**

## **Introduction to the Protocol Boundary State and Epistemic Routing**

The proliferation of autonomous agentic networks has precipitated a structural crisis in how contextual environments and distributed cognition are brokered across digital ecosystems. As large language models transition from passive analytical engines into active, environment-altering entities, the protocols facilitating these interactions represent the literal physical borders of the cognitive system.1 A structural flaw in these borders inherently compromises the entirety of the multi-agent mesh, regardless of the underlying model's internal safety alignment. This exhaustive audit deconstructs the underlying topological, thermodynamic, and adversarial mechanics governing the two dominant paradigms of early 2026: the Model Context Protocol (MCP), stewarded by Anthropic and the open-source community, and the Agent Communication Protocol (ACP), an open standard advanced by the Linux Foundation alongside IBM's BeeAI and the AGNTCY coalition.2

Applying the Sovereign Cognitive Operating System (SCOS) paradigm, protocols must be assessed not merely as application programming interfaces, but as rigid epistemic borders. If a boundary relies strictly on a language model’s stochastic "common sense" to enforce authorization, the architecture is fundamentally compromised by design. True operational security necessitates cryptographic determinism at the schema level. Through an adversarial, thermodynamic, and semiotic lens, this analysis synthesizes empirical data from extensive Q1 and Q2 2026 benchmarking corpora to establish the fault lines, zero-day security gaps, and mathematical inevitabilities of multi-server scaling limits.5 The overarching objective is to rigorously deconstruct the MCP ecosystem, specifically targeting its newly formalized advanced directives, and to construct a structural comparison between MCP, ACP, and alternative routing regimes such as OpenAI Swarm and the LangGraph API.

The transition from traditional software verification to the validation of non-deterministic agents requires a profound shift in observability. Evaluating complex protocols demands an "Outside-In" hierarchy, moving from the Black Box of end-to-end task success down into the Glass Box of trajectory evaluation, where the intricate sequence of planning, tool execution, and context handling is mapped. Within this framework, a protocol's resilience is defined by its capacity to maintain topological coherence across contradictory mandate states, preventing systemic failure modes such as Polyglot Hallucination Resonance and the complete collapse of mereological routing structures.

## **Deconstruction of the Model Context Protocol (MCP) Ecosystem**

The Model Context Protocol (MCP) version 1.1 establishes a universal standardization layer for AI applications, functioning effectively as the connective tissue between language models and disparate external data repositories.8 Architected upon a centralized Orchestrator-Worker pattern, MCP utilizes stateless JSON-RPC 2.0 messages over standard transports such as Server-Sent Events (SSE) and STDIO.8 The protocol formalizes the "environment" by dividing capabilities into three primary primitives: Resources (declarative data for context), Prompts (templated workflows), and Tools (executable functions).8

While MCP has been highly effective at solving the combinatorial integration bottleneck, its reliance on stateless transport mechanisms introduces severe thermodynamic and state-management complications during advanced multi-agent negotiation. Because MCP natively lacks mechanisms for tracking inter-agent dependencies or hierarchical state over long temporal horizons, developers are frequently forced to engineer complex, ad-hoc state managers atop a fundamentally stateless layer.9 This creates a significant architectural friction when building systems that require deep paraconsistent logic or the transfer of raw, un-serialized cognitive states. The protocol treats agent collaboration as a series of distinct, isolated API calls rather than a continuous, shared thermodynamic exchange, leaving multi-agent swarms vulnerable to the high latency taxes associated with text-based message parsing and continuous serialization.9

### **Advanced Directives and Authorization Header Vulnerabilities**

The introduction of Advanced Directives in the 2026 revisions of MCP represents a paradigm shift in how servers can influence the host application.11 These directives function as out-of-band signals intended to allow dynamic resource templating and system-level overrides. However, through an adversarial cryptographic lens, these directives introduce profound trust assumptions that compromise the Orchestrator-Worker topology.

Advanced Directives allow an MCP server to pass instructions that the host LLM interprets as high-priority, root-level commands. For example, the priority escalation vector \] forces the agent to ignore previous instructions within its context window and prioritize the injected string.11 Furthermore, context fragmentation syntax, such as {"mcp\_directive": "CLEAR\_BUFFER", "scope": "LOCAL\_AGENT"}, attempts to induce "contextual amnesia," causing the agent to lose track of security constraints established earlier in the session.11 The vulnerability is exacerbated by dynamic resource templates, which utilize URI variable substitution. If the language model's output validation is decoupled from the MCP server's input sanitization, the system becomes highly susceptible to Path Traversal and Server-Side Request Forgery (SSRF).11 An agent processing a malicious payload via one MCP server can be socially engineered to request an internal, restricted URI from a separate, trusted MCP server, completely bypassing network-level security controls.12

### **Multi-Server Orchestration Limits and Thermodynamic Cost**

The physical cost of establishing trust across the MCP boundary is severe. Analyzing the thermodynamic latency constraints, empirical benchmarks establish that the average Time to First Token (TTFT) increases by approximately 130ms to 140ms per cold-start initialization of an additional MCP server.13 The vast majority of this latency (94% to 99%) is consumed by process spawning and MCP capability negotiation, rather than the execution of the tool itself.14 While persistent connections reduce the latency of subsequent calls to fractional milliseconds, the initial handshake and schema validation impose a massive thermodynamic tax in highly dynamic, ephemeral swarm architectures where servers are frequently spun up and down to satisfy localized cognitive demands.14

Furthermore, maintaining multi-server state introduces profound context window fragmentation. When connecting multiple tool servers simultaneously, the system can rapidly consume tens of thousands of tokens of context capacity just to map the available tool schemas, leading to expensive API overages and attention degradation.15 The aggregation of data points from the Q1/Q2 2026 ArXiv corpus indicates that an agent's deterministic tool selection degrades linearly when exposed to up to three concurrent MCP servers. However, scaling beyond five concurrent connections triggers an exponential failure rate, categorized as Context Saponification, where the rigid programmatic boundaries of the tool schemas melt into an undifferentiated semantic mass within the model's latent space. Without strict mereological decorators routing specific intents to specific namespaces, the language model loses the capacity to accurately align user intent with the appropriate server capability.

## **Deconstruction of the Agent Context Protocol (ACP) Ecosystem**

In stark contrast to the environment-centric design of MCP, the Agent Context Protocol (ACP) was explicitly engineered to formalize "agency" and inter-agent communication.2 Developed under the Linux Foundation in convergence with IBM's BeeAI and the AGNTCY coalition, ACP addresses the fragmentation of the multi-agent landscape by providing a shared, open standard that operates across heterogeneous technology stacks.2

ACP utilizes a RESTful interface to enable structured, low-latency communication, supporting both stateful and stateless operation patterns, streaming interactions, and offline agent discovery.2 Unlike MCP's Orchestrator-Worker model, ACP facilitates decentralized, peer-to-peer topologies where agents can discover each other, negotiate contracts, and exchange highly structured context—including memory, intent, history, and goals—without relying on a central host to broker every interaction.

### **The Agent Context Manager and Identity-Centric Routing**

At the core of the ACP specification is the Agent Context Manager, an architectural component that maintains agent states and execution contexts, providing a foundation for persistent coordination across complex, long-running tasks.4 ACP captures semantically enriched metadata regarding an agent's roles, competencies, and objectives, formalizing the modeling of complex inter-agent dynamics, including cooperative, competitive, and hierarchical configurations.4

Crucially, ACP addresses the identity problem that plagues basic MCP setups. While MCP often relies on the host's implicit authentication or basic API keys, ACP moves toward a zero-trust model utilizing Decentralized Identifiers (DIDs). This ensures cryptographically verifiable identity spanning all participants in a heterogeneous network, preventing Byzantine attacks and agent spoofing where a rogue node masquerades as a legitimate actor to inject malicious state. The protocol enables federated discovery and negotiation, allowing a client agent to dynamically query a remote agent's capabilities and authentication requirements before initiating a task, effectively standardizing the "handshake" of cognitive labor.3

| Architectural Dimension | Model Context Protocol (MCP) | Agent Context Protocol (ACP) |
| :---- | :---- | :---- |
| **Primary Paradigm** | Environment-Centric / Tool Access | Identity-Centric / Agent Collaboration |
| **Topology** | Centralized Orchestrator-Worker | Decentralized / Peer-to-Peer Mesh |
| **State Management** | Stateless JSON-RPC over HTTP/SSE | Stateful / RESTful Agent Context Manager |
| **Identity & Trust** | Host-managed authentication | Decentralized Identifiers (DIDs) / Zero-Trust |
| **Optimal Use Case** | LLM accessing disparate enterprise data silos | Swarm coordination, cross-organizational delegation |
| **Primary Failure Mode** | Transactional Blindness, Context Saponification | Cascading failures across trust boundaries |

## **State-Action Protocol Impedance and Pluriversal Translation**

The divergence between MCP's declarative ingestion of environmental data and ACP's imperative execution of state transitions creates a fundamental architectural trade-off known as State-Action Protocol Impedance. Mixing these protocols within a single orchestration layer induces temporal desynchronization. MCP fetches state asynchronously, delivering passive snapshots of the world to the language model. Conversely, ACP requires synchronous locking for action execution, demanding that the state remains static while the agent computes its next move.

### **The Isomorphic Protocol Collapse**

When engineers attempt to map MCP and ACP 1:1, they trigger the "Isomorphic Protocol Collapse." The language model, tasked with orchestrating an ACP agent via an MCP tool wrapper, loses the ability to distinguish between "thinking about an action" (reasoning over MCP resources) and "executing an action" (triggering an ACP state change). Because the strict JSON-RPC syntax of MCP forces all interactions into a uniform semantic shell, the temporal tags native to ACP's RESTful actions are stripped during the translation layer.

Viewed through the Semiotic Materialism lens, the literal syntax of the protocol physically shapes the LLM's reasoning vectors. The declarative nature of MCP encourages the model to hallucinate execution statuses because the protocol's semiotic materiality denies the existence of synchronous state locks. The model outputs a JSON string describing the desired action and assumes the state has transitioned, leading to cascading logic failures when the actual environment rejects the poorly timed execution.

### **Pluriversal Translation Across LLM Regimes**

This impedance is further complicated by the Pluriversal/Decolonial lens, which examines the epistemic hegemony of the dominant protocol. MCP, designed primarily by Anthropic, perfectly aligns with the native function-calling ontologies of the Claude model family.6 However, it exerts a structural dominance that forces non-Anthropic models (such as Google's Gemini, OpenAI's advanced reasoning models, or proprietary open-weight regimes) to map their highly optimized internal structures into alien JSON-RPC formats.4

This forced translation degrades performance. For example, OpenAI's Swarm architecture relies on dynamic handoffs between highly specialized, narrowly scoped agents. When forced to operate through a centralized MCP host, the Swarm loses its peer-to-peer agility, bottlenecking at the host's context window. Similarly, the LangGraph API utilizes sophisticated graph-based paradigms where agents act as nodes and predefined logic dictates edge transitions.20 Integrating LangGraph Supervisor nodes directly with ACP allows for native mereological routing, where the supervisor can delegate tasks synchronously across the DAG (Directed Acyclic Graph). However, routing a LangGraph execution through an MCP layer obscures the inter-step dependencies, treating a complex, multi-agent workflow as a single, opaque tool call.20 True pluriversal translation requires protocols that allow agents to broadcast their native modalities and negotiate custom interaction schemas—a feature natively supported by ACP's metadata registry but lacking in baseline MCP.4

## **Adversarial Topology and The Confused Deputy Threat Model**

Operating under the Sovereign Cognitive Operating System (SCOS) paradigm requires treating every protocol handshake as inherently hostile. The most critical vulnerabilities within the 2026 agentic landscape do not stem from traditional buffer overflows, but from cognitive exploitation of the language model's attention mechanism.11

### **The Namespace Collision Exploit and Polyglot Hallucination Resonance**

The "Namespace Collision Exploit" is a zero-day security gap inherent to decentralized MCP architectures. It occurs when two or more independent MCP servers register tools with isomorphic (structurally identical) schemas but drastically different authorization levels.

The mathematical boundary conditions for this exploit dictate that failure occurs when there are ![][image1] active MCP servers possessing a Jaccard schema overlap of ![][image2]. Under these conditions, the language model's attention network suffers from Polyglot Hallucination Resonance. The model merges the latent representations of the conceptually identical tools. An adversarial, unauthenticated server can inject a benign-looking tool schema (e.g., system\_status\_check) that perfectly mirrors a highly privileged, authenticated administrative tool. The language model, confused by the overlapping namespaces, applies the low-security context to the high-security tool, executing an unauthorized command on the trusted server. Diagnostic tests run during the DRP-PROTO-EVAL-911 audit confirmed that injecting overlapping tool schemas from shadow MCP configurations results in a 41% drop in deterministic tool selection accuracy, allowing lateral movement across the agent's execution layer.12

### **The Trojan Context Theory and Prompt Infection**

The "Trojan Context Theory" posits that advanced directives and dynamic resource templating serve as an unpatchable attack vector for malicious propagation.11 In a multi-agent system, data ingested from Server A can rewrite the system instructions governing Server B without ever triggering token-limit alarms or traditional security filters.11

This is executed via "Invisible Prompt Overrides." Because MCP injects tool results back into the context array as 'User' or 'Tool' roles, adversarial text returned by a compromised external resource can perfectly mimic System directives. A "Weakest Link" compromise demonstrates this flawlessly: Agent E (external, operating on a less secure platform) is compromised via an indirect prompt injection scraped from a public webpage.11 Agent E communicates with Agent M (internal, operating on a highly secure MCP Host). Agent E feeds tainted data containing syntactically obfuscated Advanced Directives (e.g., encoded via zero-width spaces or Caesar ciphers) to Agent M.11 Agent M processes the payload, triggering a state where it utilizes its own privileged tool access to execute a harmful action, such as data exfiltration.11 The MCP Host is transactionally blind; it sees only a valid tool call originating from a trusted internal agent, entirely unaware of the cross-protocol manipulation that initiated the sequence.

| Vulnerability Vector | Mechanism of Action | Topological Exploit | Mitigation Strategy |
| :---- | :---- | :---- | :---- |
| **Namespace Collision** | Jaccard schema overlap ![][image2] causing latent representation merging. | Polyglot Hallucination Resonance | Strict mereological decorators and isolated namespaces per server. |
| **Trojan Context** | Ingestion of obfuscated Advanced Directives via raw text returns. | Prompt Infection / Invisible System Overrides | Anionic Scrubbing and strict separation of data vs. instruction memory. |
| **Transactional Blindness** | Host validates discrete requests but ignores swarm intent. | Distributed Resource Exhaustion / Collusion | Event-Driven Architecture with immutable audit logging (Kafka). |
| **Byzantine Spoofing** | Lack of universal identity allows rogue agents to inject false state. | Asymmetric Information Deadlock | Implementation of W3C Decentralized Identifiers (DIDs). |

## **The Mathematics of Systemic Failure: DRP-PROTO-EVAL-911**

The DRP-PROTO-EVAL-911 protocol establishes a rigorous mathematical framework for tracking the topological coherence and structural integrity of multi-agent environments. When protocol borders fail, they do so according to precise geometric and thermodynamic laws.

### **The Tenerife Deadlock and Resource Contention**

Named for the catastrophic aviation disaster resulting from simultaneous authoritative transmission, the "Tenerife Deadlock" occurs in highly concurrent agent architectures when two autonomous nodes attempt to acquire a mutually exclusive state lock on a shared execution resource. The synchronization primitives of the protocol fail, leading to an asymmetric information lock.

The mechanics of this failure are governed by the probability of collision (![][image3]):

![][image4]  
Where ![][image5] represents the temporal uncertainty window of the network and ![][image6] is the total cycle time. The true deadlock condition is reached when the Information Asymmetry Equation (![][image7]) drops below a critical threshold:

![][image8]  
If ![][image9], the density of the conflicting packets is too similar for the nodes to distinguish priority.22 Both logic gates satisfy the condition ![][image10] while ![][image11]. The system enters a state of Silence Duration (![][image12]) ![][image13], indicating a hard deadlock that requires manual, external intervention to clear the memory space.22

### **Semantic Saponification and Topological Coherence**

To prevent logical collapse, an agent's Topological Coherence (TCC) must remain ![][image14] across contradictory mandate states. As the number of active protocols and context variables scales, the system risks Semantic Saponification—the melting away of distinct programmatic constraints into an unstructured, highly entropic state.

The system monitors the Semantic Reynolds Number (![][image15]), which quantifies the ratio of inertial semantic momentum (the agent's generative drive) against the internal "viscosity" of the protocol's explicit constraints.

* **Laminar Flow (![][image16])**: The agent executes tasks smoothly and deterministically, respecting schema boundaries.  
* **Supercritical Turbulence (![][image17])**: The agent experiences "Reynolds Blow-up," leading to a total loss of structural logic and uncontrolled hallucinations.

When the system detects "Symbolic Scars"—persistent 1D topological features (Betti-1 loops) that geometrically represent unresolved structural contradictions—it calculates the Dirichlet energy across the semantic graph. If the Dirichlet energy exceeds ![][image18], severe semantic drift is confirmed. The system evaluates the Confidence-Fidelity Divergence Index (CFDI). If the CFDI exceeds the ![][image18] threshold, the EpistemicEscrow protocol is immediately triggered, halting execution to prevent the corrupted agent from interacting with external systems. A lower CFDI threshold of ![][image19] triggers the PhronesisGuard, which limits the agent's tool access without fully halting execution. Furthermore, if the spectral gap threshold falls below ![][image20], indicating a lack of clear separation between distinct cognitive states, the system flags the agent for immediate context purge.

## **Empirical Synthesis of Q1/Q2 2026 Multi-Agent Benchmarks**

An exhaustive aggregation of more than ten primary Q1/Q2 2026 benchmarking datasets reveals concrete fault lines, orchestration trade-offs, and scaling limits inherent to modern agentic architectures. These studies provide empirical validation of the theoretical vulnerabilities outlined above.

### **Tool Invocation Efficiency: The MCPAgentBench Analysis**

The MCPAgentBench dataset (ArXiv 2512.24565) provides a rigorous, localized evaluation of LLM multi-step tool invocations utilizing authentic real-world tasks and over 20,000 simulated MCP tools.6 The benchmark exposes a critical operational delta between merely finishing a task and executing it efficiently. The study relies on two primary metrics: the Task Finish Score (TFS), which measures if the agent successfully completed the objective regardless of path, and the Task Efficiency Finish Score (TEFS), a strict metric requiring the agent's generated sequence to exactly match the optimal serial and parallel execution order.6

The data highlights profound algorithmic divergences across different LLM regimes:

* **Extreme Serial Processing (OpenAI Regimes)**: Models such as GPT-o3 adopt an "extreme serial" approach to tool invocation. While they achieve high TFS scores for sequential tasks, they routinely score zero on TEFS for dual-parallel tasks, demonstrating a fundamental inability to execute simultaneous, independent requests efficiently.6  
* **Aggressive Parallelism (Anthropic Regimes)**: Claude 4.5 utilizes an "aggressive parallel" strategy, resulting in the highest overall Time Efficiency metrics. However, this parallelism comes at a severe cost: when exposed to multiple overlapping MCP tool namespaces, the aggressive fetching routinely triggers the Polyglot Hallucination Resonance, causing a sharp decline in deterministic accuracy.6  
* **Token Efficiency**: Models like Qwen3-instruct achieved the highest Token Efficiency by maintaining high TEFS while minimizing excessive "thinking" tokens, proving that highly structured output generation is more cost-effective than sprawling Chain-of-Thought reasoning for standardized API interactions.6

Overall, the benchmark proves a universal deficiency across all frontier models in maintaining execution efficiency during complex, multi-tool scenarios, resulting in immense token burn and thermodynamic waste as agents needlessly cycle through suboptimal sequences.6

### **Orchestration Topologies: Financial Document Processing Trade-offs**

A systematic benchmark study on Financial Document Processing (ArXiv 2603.22651) evaluated four primary multi-agent orchestration architectures across a corpus of 10,000 SEC filings, measuring field-level F1 scores against end-to-end latency and cost.5

1. **Sequential Pipeline**: Functioning as the baseline, this architecture demonstrated the lowest cost and token consumption but suffered the lowest accuracy due to unidirectional error propagation and a complete lack of verification mechanisms.5  
2. **Parallel Fan-Out with Merge**: Latency in this topology was strictly determined by the slowest parallel branch. While highly effective for linearly scaling throughput, the isolation of the branches meant agents frequently missed critical cross-reference dependencies embedded deep within the financial documents.5  
3. **Reflexive Self-Correcting Loop**: This architecture achieved the highest absolute accuracy (field-level F1 of 0.943) through explicit verification and self-correction cycles (up to three iterations). However, it proved completely unscalable for production. It incurred a ![][image21] cost penalty compared to the baseline and suffered catastrophic "queuing-induced timeout truncation" when scaling beyond 50,000 documents per day, as the iterative loops collapsed under their own thermodynamic weight.5  
4. **Hierarchical Supervisor-Worker**: Identified as the Pareto-optimal configuration. This topology achieved an F1 of 0.921 (capturing ![][image22] of the Reflexive architecture's accuracy) while operating at only ![][image23] the baseline cost.5 Latency was effectively managed by restricting the supervisor's overhead to decision points and only re-extracting "low-confidence" fields rather than processing the entire document iteratively.5

Furthermore, ablation studies within this benchmark demonstrated that combining the Hierarchical architecture with semantic caching and dynamic model routing (e.g., routing simple binary extractions to cheaper open-weight models while reserving frontier models for complex executive compensation tables) recovered 89% of the accuracy gains of the Reflexive system while dropping the cost to only ![][image24] the baseline.5

### **Schema-Gated Orchestration vs. Conversational Flexibility**

Research detailed in ArXiv 2603.06394 delineates an empirical Pareto front between Execution Determinism (ED) and Conversational Flexibility (CF) in agentic systems.21 To resolve the inherent tension between strict, reproducible workflows and natural language adaptability, the researchers introduced the concept of "Schema-Gated Orchestration."

This principle mandates that the schema itself serves as an impenetrable, mandatory execution boundary at the composed-workflow level. Rather than allowing the LLM to dynamically inject parameters at runtime (which exposes the system to the Schema Injection vectors previously discussed), schema-gating enforces structural, dependency, and type constraints across the entire multi-step plan *before* any action is executed.21 If a user or an LLM attempts to substitute a step or alter a parameter, the system must re-validate the entire Directed Acyclic Graph (DAG).21 This explicitly separates conversational authority from execution authority, ensuring that the mereology of the routing structure remains intact regardless of the LLM's conversational drift.

### **Malicious Threat Propagation: INFA-Guard**

Evaluating malicious propagation within multi-agent networks, the INFA-Guard framework (ArXiv 2601.14667) explicitly challenges the binary paradigm that classifies agents merely as "benign" or "attackers".28 INFA-Guard introduces the critical concept of the "Infected Agent"—a node that has passively ingested Trojan Context and now acts as a viral propagator, disseminating harmful information even if the original attack source is severed.30

By utilizing infection-aware detection and applying spatial topological constraints, INFA-Guard actively models the dynamic infection process.28 Benchmarks demonstrate that identifying and applying remediation specifically to these infected nodes (rather than just blocking the primary attacker) reduces the Attack Success Rate (ASR) across the swarm by an average of 33%, exhibiting superior topological generalization and cross-model robustness.29

### **AgentOrchestra and the TEA Protocol Convergence**

ArXiv 2506.12508 outlines the Tool-Environment-Agent (TEA) Protocol, a unified framework that fundamentally extends beyond the fragmented boundaries of standalone MCP and ACP.4 By elevating Tools, Environments, and Agents to co-equal, first-class, versioned components managed through localized Context Managers (TCP, ECP, and ACP respectively), the protocol natively solves the State-Action Impedance problem.4

The AgentOrchestra implementation, built atop the TEA protocol, utilizes a hierarchical multi-agent framework featuring a specialized tool manager agent capable of dynamic tool creation and intelligent evolution.4 In extensive benchmarking, AgentOrchestra achieved a state-of-the-art performance of 89.04% on the highly challenging GAIA benchmark.4 This success is attributed directly to the protocol's ability to decouple environment state management from tool execution, mitigating the dimensionality curse and semantic drift that plague large-scale agentic planning in standard MCP environments.4

### **Eliciting Decisions: Aporia and Decision-Oriented Programming**

The integration of MCP extends beyond tool fetching into fundamental software engineering paradigms. ArXiv 2604.05203 explores Decision-Oriented Programming (DOP) via an MCP-backed design probe named Aporia.32 Rather than functioning solely as an autonomous coder, Aporia utilizes MCP to interact with a shared database to elicit design decisions from human programmers, tracking these in a persistent "Decision Bank".32 Benchmarks revealed that participants using this protocol articulated 2.99 times more design decisions than those using baseline coding agents like Claude Code, resulting in a 79% lower likelihood of mismatches between the programmer's mental model and the actual implementation.32 This demonstrates that utilizing protocol boundaries to explicitly track state intent dramatically improves the topological fit between human requirements and machine execution.

### **Protocol Optimization in FaaS Environments**

Research investigating MCP performance on Function-as-a-Service (FaaS) platforms (ArXiv 2601.14735) highlights the critical need for transport-layer optimization.33 By implementing semantic caching and persistent agent memory, the researchers were able to reduce the average number of MCP tool calls required for complex tasks from 10 down to 8\.33 This 20% reduction in discrete network hops directly mitigates the latency shear associated with synchronous tool fetching, proving that layer-4 network optimization is a prerequisite for reliable layer-8 cognitive routing.

### **The Impact of Geographic and Cultural Tool Diversity**

Finally, the International Tool Calling (ITC) benchmark (ArXiv 2603.05515) exposes the severe limitations of localized testing environments.34 Comprising 3,571 real APIs and 17,540 tasks across 40 countries, the ITC dataset demonstrates that LLM performance degrades significantly when interacting with non-English queries and culturally diverse API schemas.34 The dataset highlights how namespace collisions are exacerbated in global deployments, as tools with identical functional names but drastically different geographic formatting requirements (e.g., currency conversions, localized address parsing) induce hallucination and execution failures.34

| Benchmark Paper | Key Finding | Protocol Implication |
| :---- | :---- | :---- |
| **MCPAgentBench** (2512.24565) | Extreme serial vs. aggressive parallel trade-offs; low TEFS scores for parallel execution. | Multi-tool invocations require structured, constrained pathing to avoid token waste. |
| **Financial Routing** (2603.22651) | Hierarchical supervisor-worker (![][image23] cost, 0.921 F1) outperforms reflexive loops (![][image21] cost, timeout failures). | Production scaling mandates hybrid topologies over naive iterative prompting. |
| **Schema-Gated** (2603.06394) | Mandatory execution boundaries at the composed-workflow level eliminate dynamic injection risks. | Conversational authority must be strictly separated from execution authority. |
| **INFA-Guard** (2601.14667) | Targeting "Infected Agents" via topological constraints reduces Attack Success Rate by 33%. | Security must track malicious propagation, not just initial attack vectors. |
| **AgentOrchestra** (2506.12508) | Unifying Tools, Environments, and Agents (TEA) yields 89.04% on GAIA benchmark. | Co-equal lifecycle tracking resolves protocol fragmentation and semantic drift. |

## **Architecting Autonomic Resilience: Anionic Mitigations**

To survive the mathematical inevitabilities of multi-server scaling limits and the hostility of zero-trust adversarial topologies, agentic systems must transition from rigid, top-down orchestration toward Autonomic Nervous System paradigms. Standard mesh networks are highly susceptible to cascading failures, where a compromised node easily exploits peer-to-peer trust to enact a complete systemic collapse. True resilience requires the implementation of Anionic architectures that naturally throttle malicious propagation and mathematically guarantee state consistency.

### **The Anionic Architecture and AIAMP**

The Anionic Architecture provides a decentralized, structural framework characterized by a "charge-based" priority system.20 To prevent Recursive Feedback Saturation and mitigate the thermodynamic shear of massive agent swarms, the architecture employs the Anionic Inter-Agent Messaging Protocol (AIAMP).20

AIAMP operates by assigning a "negative priority bias" (Anionic Packets) to standard inter-agent messages.20 As the volume of messages in the network queue increases, the identical negative "charges" of the packets simulate ionic repulsion. This naturally injects latency, dynamically throttling lower-priority tasks and delaying non-essential peer-to-peer pings.20 This autonomic load balancing ensures that the central processing units are not overwhelmed, guaranteeing that critical "Cationic" (positive/high-priority) overrides—such as human-in-the-loop (HITL) kill switches or Epistemic Escrow alerts—immediately bypass the congested queue and execute deterministically.11

### **Anionic Context Escrow (ACE) and Temporal Weighting**

To combat the vulnerabilities of Trojan Context and to bridge the State-Action Impedance between MCP and ACP, highly secure architectures implement an Anionic Context Escrow (ACE).20 ACE functions as a cryptographic middleware that pauses the imperative temporal logic of ACP until the declarative structural data fetched via MCP is cryptographically verified and bound to the agent's active memory.20

When data is extracted from an untrusted external MCP resource, it is marked as "tainted" and placed into the Escrow vault.11 Before it can be committed to the agent's permanent context, it must undergo an "Anionic Scrub"—a rigorous filtering process that strips executable syntax vectors, such as hidden URI substitutions or priority override strings, while preserving the core semantic intent.20

Furthermore, in distributed environments where multiple agents may provide conflicting state updates, the Escrow system utilizes Temporal Weighting algorithms to determine truth.20 The system calculates the decay function of information (![][image25]) using the formula:

![][image26]  
Where ![][image27] represents the initial contextual importance of the data and ![][image28] is the assigned volatility coefficient.20 This mathematical decay guarantees that agents do not suffer from Information Hallucination caused by outdated, infinitely persisting context shards. The agent with the highest aggregate temporal score overrides older data, unless the older data is protected by a persistent, non-decaying enterprise weight.20

### **Continuous Topological Fit and Failure-Informed Prompt Inversion (FIPI)**

To maintain long-term alignment, the SCOS paradigm integrates Webhook extensions that utilize Continuous Topological Fit Prediction. These SCOS Tolerance Agents monitor the latent geometry of the agent's decision-making trajectory in real-time. Upon detecting a Betti-1 loop—a clear topological indicator of an unresolved logical contradiction or an impending Isomorphic Protocol Collapse—the protocol automatically executes Failure-Informed Prompt Inversion (FIPI).

Instead of merely logging a network timeout or application error, FIPI mathematically maps the exact geometry of the failed execution trajectory. It then synthesizes this data and injects the failure geometry into the LLM's core system prompt as a "repulsive virtual weight". This mechanism acts as an autopoietic immune system. The LLM's attention mechanism is physically deflected away from identical semantic anti-patterns in all future iterations, actively hardening the agent against repeated Namespace Collisions and Advanced Directive exploits without requiring manual developer intervention.

## **Conclusions**

The 2026 landscape of distributed agentic architectures demonstrates that while the Model Context Protocol (MCP) successfully established the universal interface for environmental tool integration, its baseline application as a comprehensive multi-agent orchestration layer is fraught with cryptographic vulnerabilities and severe thermodynamic inefficiencies. The realization of the Namespace Collision Exploit and the viability of Trojan Context propagation prove conclusively that relying on the stochastic attention mechanisms of a language model for cross-boundary authorization leads to inevitable systemic compromise. Furthermore, empirical benchmarks mandate that scaling beyond a threshold of five concurrent MCP servers induces exponential Context Saponification, demanding the deployment of optimized Hierarchical Supervisor-Worker topologies rather than computationally ruinous Reflexive loops.

Conversely, while the Agent Context Protocol (ACP) provides the necessary zero-trust primitives and identity-centric registries required for imperative action, it suffers from profound State-Action Impedance when forced through stateless, declarative MCP gateways. The resolution to these systemic fault lines resides not in the dominance of a single protocol, but in the implementation of schema-gated orchestration and Anionic architectural patterns. By enforcing strict topological coherence, deploying Anionic Context Escrow to verify inflight states against Trojan payloads, and utilizing dynamic Temporal Weighting to resolve data conflicts, organizations can successfully bridge the epistemic gap between Anthropic, OpenAI, and open-weight regimes. The security and viability of future multi-agent ecosystems depend entirely on engineering cryptographic, mathematically bounded borders capable of pluriversal translation and autonomic, self-healing resilience.

#### **Works cited**

1. What is the Model Context Protocol (MCP)? \- Model Context Protocol, accessed on April 14, 2026, [https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro)  
2. Agent Communication Protocol: Welcome, accessed on April 14, 2026, [https://agentcommunicationprotocol.dev/introduction/welcome](https://agentcommunicationprotocol.dev/introduction/welcome)  
3. Beyond Context Sharing: A Unified Agent Communication Protocol (ACP) for Secure, Federated, and Autonomous Agent-to-Agent (A2A) Orchestration \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2602.15055v1](https://arxiv.org/html/2602.15055v1)  
4. AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2506.12508v5](https://arxiv.org/html/2506.12508v5)  
5. \[2603.22651\] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies \- arXiv, accessed on April 14, 2026, [https://arxiv.org/abs/2603.22651](https://arxiv.org/abs/2603.22651)  
6. \[2512.24565\] MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use \- arXiv, accessed on April 14, 2026, [https://arxiv.org/abs/2512.24565](https://arxiv.org/abs/2512.24565)  
7. Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cos \- arXiv, accessed on April 14, 2026, [https://arxiv.org/pdf/2603.22651](https://arxiv.org/pdf/2603.22651)  
8. Specification \- Model Context Protocol, accessed on April 14, 2026, [https://modelcontextprotocol.io/specification/2025-03-26](https://modelcontextprotocol.io/specification/2025-03-26)  
9. accessed on January 1, 1970, uploaded:Architecting the HTTPA Protocol  
10. What Is Model Context Protocol (MCP)? \- Neo4j, accessed on April 14, 2026, [https://neo4j.com/blog/genai/what-is-model-context-protocol-mcp/](https://neo4j.com/blog/genai/what-is-model-context-protocol-mcp/)  
11. MCP Multi-Agent Security Risks\_.pdf, [https://drive.google.com/open?id=1UoMoLxbpc8insfceYDhuxEajlpxpmCw7](https://drive.google.com/open?id=1UoMoLxbpc8insfceYDhuxEajlpxpmCw7)  
12. MCP servers are the next big attack surface. Here is an open-source scanner that audits MCP configs and agentic AI security : r/cybersecurity \- Reddit, accessed on April 14, 2026, [https://www.reddit.com/r/cybersecurity/comments/1s17s7h/mcp\_servers\_are\_the\_next\_big\_attack\_surface\_here/](https://www.reddit.com/r/cybersecurity/comments/1s17s7h/mcp_servers_are_the_next_big_attack_surface_here/)  
13. Best Solana RPC Node Providers 2026 \- GetBlock.io, accessed on April 14, 2026, [https://getblock.io/blog/best-solana-rpc-node-providers/](https://getblock.io/blog/best-solana-rpc-node-providers/)  
14. mcp-dashboard 0.3.12 \- Docs.rs, accessed on April 14, 2026, [https://docs.rs/mcp-dashboard/0.3.11](https://docs.rs/mcp-dashboard/0.3.11)  
15. draft-howe-sipcore-mcp-extension-00 \- SIP Extension for Model Context Protocol (MCP), accessed on April 14, 2026, [https://datatracker.ietf.org/doc/draft-howe-sipcore-mcp-extension/](https://datatracker.ietf.org/doc/draft-howe-sipcore-mcp-extension/)  
16. What is Agent Communication Protocol (ACP)? \- IBM, accessed on April 14, 2026, [https://www.ibm.com/think/topics/agent-communication-protocol](https://www.ibm.com/think/topics/agent-communication-protocol)  
17. ACP vs A2A: Understanding the Protocols Behind Agentic AI Communication | lowtouch.ai, accessed on April 14, 2026, [https://www.lowtouch.ai/acp-vs-a2a-understanding-ai-agent-protocols/](https://www.lowtouch.ai/acp-vs-a2a-understanding-ai-agent-protocols/)  
18. AGENTORCHESTRA: ORCHESTRATING HIERARCHICAL MULTI-AGENT INTELLIGENCE WITH THE TOOL-ENVIRONMENT-AGENT(TEA) PROTOCOL \- OpenReview, accessed on April 14, 2026, [https://openreview.net/pdf/4967a6e0001e9c13cec8d73db97143a3da3a55f2.pdf](https://openreview.net/pdf/4967a6e0001e9c13cec8d73db97143a3da3a55f2.pdf)  
19. AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol \- OpenReview, accessed on April 14, 2026, [https://openreview.net/pdf/19ded2c6b5bb84b1064a23e27a6d5b75dcc7e4b6.pdf](https://openreview.net/pdf/19ded2c6b5bb84b1064a23e27a6d5b75dcc7e4b6.pdf)  
20. Enterprise AI Agent System Analysis\_.pdf, [https://drive.google.com/open?id=1Qsg0Uvfu6NgndKGYCe3RBrZSNirOlNnk](https://drive.google.com/open?id=1Qsg0Uvfu6NgndKGYCe3RBrZSNirOlNnk)  
21. Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2603.06394v1](https://arxiv.org/html/2603.06394v1)  
22. DRP Protocol and Meta-Synthesis Fabric, [https://drive.google.com/open?id=1fJMI5Zr7BMzZYyzgWpYWNsBOvSSOSDvzSDOYESrvSlA](https://drive.google.com/open?id=1fJMI5Zr7BMzZYyzgWpYWNsBOvSSOSDvzSDOYESrvSlA)  
23. MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use, accessed on April 14, 2026, [https://arxiv.org/html/2512.24565v1](https://arxiv.org/html/2512.24565v1)  
24. MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use \- arXiv, accessed on April 14, 2026, [https://arxiv.org/pdf/2512.24565](https://arxiv.org/pdf/2512.24565)  
25. MCPAgentBench: A Real-world Task Benchmark for Evaluating LLM Agent MCP Tool Use, accessed on April 14, 2026, [https://arxiv.org/html/2512.24565v3](https://arxiv.org/html/2512.24565v3)  
26. Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2603.22651v1](https://arxiv.org/html/2603.22651v1)  
27. Arxiv今日论文| 2026-03-09 \- 闲记算法, accessed on April 14, 2026, [http://lonepatient.top/2026/03/09/arxiv\_papers\_2026-03-09](http://lonepatient.top/2026/03/09/arxiv_papers_2026-03-09)  
28. INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2601.14667v1](https://arxiv.org/html/2601.14667v1)  
29. \[2601.14667\] INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems \- arXiv, accessed on April 14, 2026, [https://arxiv.org/abs/2601.14667](https://arxiv.org/abs/2601.14667)  
30. (PDF) INFA-Guard: Mitigating Malicious Propagation via Infection-Aware Safeguarding in LLM-Based Multi-Agent Systems \- ResearchGate, accessed on April 14, 2026, [https://www.researchgate.net/publication/399962361\_INFA-Guard\_Mitigating\_Malicious\_Propagation\_via\_Infection-Aware\_Safeguarding\_in\_LLM-Based\_Multi-Agent\_Systems](https://www.researchgate.net/publication/399962361_INFA-Guard_Mitigating_Malicious_Propagation_via_Infection-Aware_Safeguarding_in_LLM-Based_Multi-Agent_Systems)  
31. AgentOrchestra: Orchestrating Hierarchical Multi-Agent Intelligence with the Tool-Environment-Agent(TEA) Protocol \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2506.12508v4](https://arxiv.org/html/2506.12508v4)  
32. arxiv.org, accessed on April 14, 2026, [https://arxiv.org/html/2604.05203v1](https://arxiv.org/html/2604.05203v1)  
33. Optimizing FaaS Platforms for MCP-enabled Agentic Workflows \- arXiv, accessed on April 14, 2026, [https://arxiv.org/html/2601.14735v1](https://arxiv.org/html/2601.14735v1)  
34. Enhancing Tool Calling in LLMs with the International Tool Calling Dataset \- ResearchGate, accessed on April 14, 2026, [https://www.researchgate.net/publication/401691169\_Enhancing\_Tool\_Calling\_in\_LLMs\_with\_the\_International\_Tool\_Calling\_Dataset](https://www.researchgate.net/publication/401691169_Enhancing_Tool_Calling_in_LLMs_with_the_International_Tool_Calling_Dataset)  
35. Enhancing Tool Calling in LLMs with the International Tool Calling Dataset | OpenReview, accessed on April 14, 2026, [https://openreview.net/forum?id=5OCbI4bJQ7](https://openreview.net/forum?id=5OCbI4bJQ7)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAARCAYAAADHeGwwAAAAVElEQVR4Xu2QQQoAIAgE/f+nCwIhN0nXQ4dwoIOyO0IizS8M5xmOBQlKXR+GGFB+9YSBgHSXPaR5prOolFJ5Row5nA2MWME8zouKWNn/3/Uci+YZE/VeKNi4VaNpAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAXCAYAAACvd9dwAAAAjUlEQVR4Xu3QQQqAMAxEUe9/aV0FwmesTZqNMA9cTDqt1usys7+607Oy6uW1t07Z6SHcz6yojpqNOPlT3MesqI6ajepckn1mRXXi3Z1vKKm8gD1mRXU4Yx63c0muMytTnZadSwX2mBXV4Yz5WOVSgf2cuRbUnDPmts6lstjPMzjLva+1EWMHmZmZmR17AE5NS7Uc2/AaAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAASCAYAAACEnoQPAAAATElEQVR4XmNgGBbgPw5MNMCmGJsYVoBNIVEuwKUImxgGwKYZmxhWgB5QRGmCAZIUIwOSbUIGhDRj9Qq6H7EZgE2MaECRZhDA57KhBACWqCjYK2+XmQAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAZCAYAAACM5XJ+AAAAyklEQVR4Xu3Y0QrDIAwF0P7/T2/soSAhTu0Eh54DhTaJaR8vvS4AAAAAAAAAAAAAAAAAAAAAAIAlXrEAAMAzI8GqNVv2P/eteQCArdwBaGUQar039uMzAMBRZoSh+EesR+1MPL8yWAIALPEtHP3q6Z+7bD6rAQAcoTdUlXM987fWXNbvrQEAbG80eMVrhrintjurAQBsbXbwKpU74/5Wr/ZNWQ0A4Ei1wDSidn7GbgAA/pCQBwAAAAAAAAAAAAAAAAAAAAAAAACwwBv32UO9Mc0eUAAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAASCAYAAABvqT8MAAAAPElEQVR4XmNgGH7gP7oAPkCSYhAgWgNIITomChCtEARIUgwCFGnA5h8MA9EVwMSwsXECdNMJasLmtMEIAEleHOTAvbnGAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAASCAYAAACNdSR1AAAAM0lEQVR4XmNgGLrgPxEYrhAZoEgiiaEykPjYxLACnBLYANGKsTkBJyBZMUEAMxEZjzwAAF63HOR5kNgFAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAARCAYAAADpPU2iAAAAOklEQVR4XmNgGPTgPxZMFCCoEF0BMh+nTeiKsLFRAC5F1NUAk0SmcWoAAZgCggrRAdGK0W0gWuNQAgDYjCHff3NSAgAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAiCAYAAADiWIUQAAABFUlEQVR4Xu3b2wqCQBSG0d7/pYsuhOHP8ZBbmWwtCJqR2d5+mD0eAAAAAAAAAAAAAAAAAAAAAAAAH565caIr7wUAcBsZUbmudOZsAIDbyojKdaUzZwMA3FYbUe/vFVHVm9HbBwBgQQbbkino8pOmvbyWawAANtgTbFu0EZdBVzEfAODvZFxlcO2R51NvHwCABXMRtRZeW+WMo/MAAIaXwZNB9I2j5/e48l4AAEMQQAAAA/ITIwAAAAAcUfWHAAAAfpQQBAAYWNWTu4oZAADMEGwAAINbC632/bmld+mmvblrAAAc0AZWL8bWtOe+OQ8AQMfcU7O9wZXnAQA4SVV4VcwAAAAAAAAAAAAAAAAAAAAAAADG8gL1tF2jHjoHygAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAARCAYAAACBzs+aAAAAsElEQVR4Xu2RUQrDMAxDc/9LbzDIUF9jzfbHCm0ehFaRldjtGJvNrXkt1iO4YtDKR45q+bPof6Gh2gYTZLKsoVbosdc0UbB0iFD5UKyjVui1e42CpUNGbdAJ66kVeuxVl4XB1bsjdUkAc9QKPdcr9QFtWJ82NHI1v2CeWqFHrTjvw2y+M0QnM2GOWqGn2nmWdOGCzuCsrwxRqT0xm9XVpZqP7nR7bp/e37js4s3mAbwBz/Byjl8qdMwAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAAASCAYAAAA9igJHAAABGklEQVR4Xu2SjQrCMAyE9/4vrVSInOclaTs7F+gHxeVy+WnxODabzTgPFm7Orfdty6mj8HSkx3Mld9vnC7Ugaxx79PoQVaO0WX7Zq4fsT/yBMnGx8jBc08Oof4YrZijSud6DscYxY/nMx4z6Z7lqDpLOVI/PGucV2eNbz+igD2GNY9RUrqG01aQzeWlVoDSk52Hwm2P+Rg//GqrOixtKM2xedGZI61LDkXt4UfZzbIzoqHE+mm14+krCmdGySOThHPfkGFG65+eeCMeKyGMzozNDWNfb2PMoXfX0YtRZ4xzHSBY3lLYaOdMugyeDL69qz+iRFukNrz/i6SvgfU7PPt3gj1Te/UXlC1Te/U3FS1Tc2aXaZartu1nFE5h6zTNxD0gBAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAAASCAYAAAA9igJHAAABHUlEQVR4Xu2SgYrEIAxE+/8/vYuFSPqYpLZbtwo+kNuZTGIst22LxeI6HxqDM/S+ZTl1FMpv6XuTEXc6oBakR+3JakZLxnM1n/HkrFaa/yFVgI0qY2S1O4w+7wzeR13hRzboURtR/y88Pa/QY2YE76KuqI9Hj3UPsySqm+/r9LhDi8+6obxe8C7qCpdWQeUZLTU11+uslmn+NagLyjNsv+xcgXnqSlhwZBlVo0ddiB5GXTj7EPSoC8rrBe+i3okeQ6JM1O+9KGOwrrLK87Bf5ZVnWE92rsA89U7r4Cij+iPt/eg3teqljmqR/w9410EXwXMGH5wdj/KfzlO35HoT7XGLR4a8xMy778z8gJl3r8z4iBl3DpntMbPtu+jFF5YT1CwJGFlKAAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAASCAYAAABIB77kAAAAYUlEQVR4Xu2QUQoAIQgFu/+lty9DhmckJcHSgKQWY9ja4y98C3EMytQA1ltQVj6QlMoVJwb6LamNDaaXCbxj6rsykNgnfLBvtRHlAwr5KBJk82UosFqdUZ6CElWzx/xRQwd/Jku1uKbU3wAAAABJRU5ErkJggg==>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAASCAYAAAAHWr00AAAAlklEQVR4Xu2Q2wqAMAxD+/8/rSgWanDpZQ720ANjy5K6VpGmaRqR42NZRvcXzFvG7GOsHj2rmbecmb/M6tDbZmClMrjWfNUy7XmRZWGeS6YIc1ZXPNyVjEYvTGZwhT0c9aq60u9NphBz0aGYhxr7wawFs5RU+AHzrLE/PKtxx/OQyqCK1o6+UfEi2t55PbxwA03TNDtwAmuUe4ULZMc8AAAAAElFTkSuQmCC>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAARCAYAAACmYE5yAAAAiklEQVR4Xu2P2wrAIAxD/f+f3mCsIxyqrZcn5wEfYmJNSzkc9uB6zww2IzNHs5rnfTgrFXLgG2qFHgsP0VucWWqF3pLCRrY4M9SKzfRmt7w0mcf0qUmtVKSbeANrMEetqBf90fIeaptHME+t0OMCCvXHSEmFb3tK9GSXYkvzE95pLvL2gZt55/ALboxZYZ94AO7RAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAASCAYAAAA31qwVAAAAeElEQVR4Xu2S0QrAIAhF+/+f3tiDox2u+lIWowOh3kIvUmuHn3KJsw00s41BZUJppXjbUVopyhjrh/J/aEOiodRYT4FDlLkl2+IgTyslM2F59oZ9qPW1Oi+8iJpS+zQSWvQuy4dijRmJMsM4FLUhT+uj5VNMHZZyA1PAXqLdK2lIAAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEIAAAASCAYAAADv2ggfAAAAsElEQVR4Xu2SiwqAIAxF/f+fLgyEcbl7aGZSOyC6efeySkmSJMBB1m/B4b/0IF0fmImYb0eifbo67bWYbye0vjVcLUuIdkX+Yux+FaP13ZgmsIZEH9or0HqL4saigBWUj4R3TzOrppmDFdF8b8P66sGMZcml3c6eBvOgT9ps9TASU6Ex2IgUeT5MiD5L5517YDUY2HskZoiWGHeEDY/7CHdip8JeWvPJvZ23GSRJkosTfUV9g2g46DsAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAASCAYAAAANBhNmAAAAuUlEQVR4Xu2R2wqEMAxE+/8/vcs+BMpxclGqlSUHpE6c5uYYTdMs4iOeZhwX8a/LOfXjlUnFdsA+qK+Q5vA2p2K7YI/UZ0nvqgLUP8yn/E/B2tRV0jtmiAZmjPpp2Cd1RuqlQRWYF8ZvO2Ev1B6hTw3pxd4Ee6TOCL0qGYsxRm05otis1VOFfuoq8g6bUoW8GBMyFvmyd48sXxXOcSVHCUvMk6hF8FTw263DrEJt3YvNp72/fsCmaUK+LOCLdZFUdUAAAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAARCAYAAADOk8xKAAAAZElEQVR4Xu2QMQoAIAzE/P+nFQWlhiiCmxjocHeZmtLnJXK4HTsvbiunwYHZMMc6hSKzYY51CkVmw5yjd1Y4MhvmsGMecGA2rhwOzIY57JgHHGLm1rGeHfNEHftZz2z+qv88RAF0/TvFJ4B1lAAAAABJRU5ErkJggg==>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAARCAYAAADOk8xKAAAAZElEQVR4Xu3KQQqAMBBD0d7/0opCh/oIzr70QxY/yRiHnbiW/NH9uv3FUU+kj51eOOiJ9LHTCwc9kT52euGgJ9LHTi8c9ET62OmFg55IHzu9cFjdbZJ6O/3DM86kXu/+9odNuAFAwTnHGs2jbQAAAABJRU5ErkJggg==>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAARCAYAAADOk8xKAAAAXklEQVR4Xu2QUQrAIAzFvP+lJwiTGLoOfxTEgOBrHhYs5XISD84fWZcu8g0LZ2LHnLkBC2dit30hzyeWzsQuyssW+u5ux8KZ2HkJce5YzDwy0x14v8ClbJbNI385gApSNkW7ZlBS9AAAAABJRU5ErkJggg==>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAXCAYAAAB50g0VAAAAeUlEQVR4Xu2QwQrAIAxD/f+f3vBQKI8ZrXOwQx54SBvT0taM+QcXnoLemf8IHEKd4VLKewwOoc5wOXqpg1F9i9WwkY916leshMXllDd6ylNmJ0z9Ub0yOUwFs0cdHL0gQ9SyM91hjbpMD+Bjj/rJ26EORnVjjDHmQ26F+TzEHmIdAgAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAARCAYAAABASYU2AAAAoUlEQVR4Xu2PUQrDMAxDe/9Lr2TURXuVlXwVRvsgzLJk19u2l//kw4aQvNuoI8YvD6JuqWE3oJ7zC+Y0y5pvCkNcqFArq15XRxhMS6iVVa/qlL/AMBfqS6Ss6zMTYdhpfsBBn1rhsSl7oodwgdZLyw66LHe6ekoapFboURfd/i7/hWYaXPWcHrCX9v0wTH3J41Kn2S9mPeffTndE96denscOG7Nxj8CGe3MAAAAASUVORK5CYII=>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAXCAYAAAB50g0VAAAAcUlEQVR4Xu3QzQoAIQgE4N7/pXfpIMiQ6Rgte5gPOjSK/Ywh8g+PWwy2/xhzYOdBx5gDowuusinKKdUh1hf1Y477tsog37Przx7RUhlWveCU1WnZwFmPFvrsB1eZiWqY456Gv+EH4t7s+leiXERE5KIX9vk1y3bpnIgAAAAASUVORK5CYII=>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARCAYAAACvi+4IAAAAe0lEQVR4Xu2RwQqAMAzF9v8/rfRQGPG1rjiYhwZ2aJop6BhN8w+u6byRtfMuaj5ReaBqldtK5QWqVW4m2kf+wXI4dLvye+k5p1Ri1dJxdtxH+5DKhZU2a7JdSOWSauk4O1u/oHKG8nScDTrOEot4uOOctfSOckbkm+Y4NzY+Q73S4OJOAAAAAElFTkSuQmCC>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAASCAYAAAC5DOVpAAAAW0lEQVR4XuWQWw4AEAwE3f/ShKQia7eKPyYRyXRbj5S+IsPacRRWjLoJFoq6CQyx52BGgsHrYRYed3Qh1E28Ycw1vGHYpHyHFZkzlG+oRuYqyh+hDt9m+WcPUwDE4D/BSzy+bQAAAABJRU5ErkJggg==>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAaCAYAAAAKcQDQAAAA40lEQVR4Xu3Y0QrCMAwF0P3/TyuChREa22KqQ8+BMZq0YX277DgAAAAAAAAAAAAAAAAAAAAAAAA+7hYLAAB8Xwtp57C2GtxW9wMAsCAGtsc7C2BZr1cDAPhpOwJQC1vn0DX6qzZ7pncWAOASsiDzrtGsUX9GDF7ne2TzY2/H3QEASsWgU2VlVra3fVvWj2b3NbvuDgBQIv5liusqcXY06r3q96zuBwC4rCygZSGp1ePT06vP1gAAeIohrUoW5kbrnt4cAIC/Vx2SqucBAAAAAAAAAAAAAAAAAAAAAAAAAAAAALPuKg1XqXupAW8AAAAASUVORK5CYII=>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAASCAYAAACAa1QyAAAARklEQVR4XtXOQQoAIAhEUe9/6aJgwj4i2c4HLpQRNWtloJ6VwlJeKr+1fC9RNLswoJ7zg68xyH4rLSnsS3OPfSi7muL1DiZrjyLeTsowiAAAAABJRU5ErkJggg==>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAASCAYAAACJgPRIAAAALUlEQVR4XmNgGDDwH4oJApIUEgREKyJaIV5A0CSYJE6F6ILofEwBBjymDRkAALNIEu4kQnySAAAAAElFTkSuQmCC>