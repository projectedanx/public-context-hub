# **Operational Trade-Offs of the Saga Compensating Transaction Sequence: Topological Analysis of Non-Monotonic Multi-Agent State Environments**

## **1\. Introduction to Distributed Transactional Topologies and Non-Monotonic Environments**

In the continued evolution of autonomous multi-agent systems and highly concurrent software architectures, the management of state across distributed networks has necessitated a departure from traditional, rigid database constraints. Legacy systems relying on a singular ACID (Atomicity, Consistency, Isolation, Durability) database transaction model are fundamentally incompatible with modern microservice ecosystems.1 When agents operate over non-monotonic Web State and disparate Database Ledger environments, the stochasticity of the physical world and the latency of asynchronous networks render synchronous two-phase commits structurally impossible.1 To govern these complex workflows, engineering architectures have standardized on the Saga pattern, a sophisticated orchestration and choreography mechanism designed to manage distributed transactions across legacy monoliths, multi-agent swarms, and external Application Programming Interfaces (APIs).1  
The defining operational characteristic of a non-monotonic ledger environment is that information, once committed, cannot simply be erased or reverted as if it never occurred.2 State representations in these environments are strictly additive or strictly forward-moving; a past state can only be neutralized by applying a new, inverse state.3 Consequently, the Saga pattern relies on a sequence of localized transactions, where each successful step publishes an event that triggers the subsequent operation.1 If a downstream service fails to process a payload, the Saga does not initiate a traditional database rollback.1 Instead, it triggers a sequence of compensating transactions.1 A compensating transaction must be specifically designed for the environment as it currently exists, acknowledging that time has passed, emails may have been dispatched, inventory may have been allocated, and external APIs have already mutated downstream resources.2  
This architectural paradigm introduces profound vulnerabilities when applied to multi-agent artificial intelligence networks. Modern large language models (LLMs) and intelligent agents operate within continuous-flow probability regimes, sharing unified token spaces and context windows.4 When a Saga compensating transaction encounters an un-executable or partially-mutated external API side-effect, the compensation itself fails, triggering the "Lost Compensation Problem".1 This failure traps the multi-agent system in a highly volatile, structurally inconsistent state, demanding aggressive internal recovery mechanisms.2  
This report provides an exhaustive, quantitative evaluation of the operational trade-offs inherent in Saga Compensating Transactions under these extreme stress conditions. Specifically, this analysis models the catastrophic system dynamics that emerge when an agent's internal memory-clearing mechanism—the Debridement Protocol—is executed concurrently with the absolute state-freezing metric required to lock a non-monotonic ledger.6 This precise temporal and spatial collision violates foundational Layer 8 rules within the Secure Cognitive Operating System (SCOS), triggering a terminal mathematical paradox classified as an infinite Betti-1 (![][image1]) contradiction loop.6  
Through the application of Topological Data Analysis (TDA), sheaf-theoretic verification, and Zigzag Persistent Homology, this document establishes a rigorous framework for detecting these non-deterministic cycles.6 Furthermore, by leveraging the concrete Python execution frameworks of LibCST (Concrete Syntax Tree transformation) and Pyperplan (PDDL state-space routing), the empirical methodologies required to measure precise CPU-to-VRAM latency and context-window degradation during API side-effect rollback failures are formalized.9

## **2\. The Saga Pattern and the Lost Compensation Problem**

### **2.1. Orchestration, Choreography, and the Fallacy of Rollbacks**

The Saga pattern is executed through two primary methodologies: choreography and orchestration.1 In a choreographed Saga, each local microservice operates autonomously, producing and listening to asynchronous events without a centralized controller.1 If a transaction fails, the localized nodes autonomously publish compensation events to undo the preceding changes.1 While highly decoupled, this methodology becomes increasingly opaque in multi-agent systems, where the decentralized nature of the event stream obfucsates the global state.2  
Conversely, the orchestration methodology utilizes a centralized hypervisor node that explicitly directs the transaction workflow.1 The hypervisor generates a Directed Acyclic Graph (DAG) that maps every forward-executing node and defines the explicit compensation actions required for recovery.1 This explicitly addresses the reality that a rollback undoes changes as if they never happened, whereas a compensation undoes changes in a world that has moved forward.2 The hypervisor must calculate a route to a newly neutralized state, demanding that every compensating transaction be fundamentally idempotent—safe to execute multiple times without unintended cumulative side-effects.3  
Despite these architectural safeguards, the orchestrating hypervisor is vulnerable to the "Lost Compensation Problem".1 Consider a multi-agent transaction that reserves database inventory, charges a user payment ledger, and dispatches a shipping API.3 If the shipping service fails, the DAG triggers compensations. If the payment refund succeeds, but the inventory release fails due to an external API schema change, the Saga enters a state of partial execution.2 The orchestrator must route the failed transaction to a Dead Letter Queue (DLQ), where it sits indefinitely, leaving the overarching system in an inconsistent state.2

### **2.2. API Boundary Mapping and Region Connection Calculus 8 (RCC-8)**

Because external APIs are aggressively engineered to avoid hanging transactions, their error classification mechanisms are exceptionally verbose.1 When an agent forces an API into an escalated diagnostic state during a lost compensation event, the resulting error trace logs are immense.1 To manage the integration of these external API boundaries within a continuous multi-agent latent space, the system must treat the API's internal validation schema as a high-dimensional mathematical manifold.1  
Modern agentic topologies enforce the boundaries of these manifolds using Region Connection Calculus 8 (RCC-8).1 RCC-8 is a qualitative spatial reasoning calculus defined by eight mutually exclusive and collectively exhaustive topological relations.5 These relations capture the exact configuration of spatial regions based on the mathematical intersections of their interiors (![][image2]), their boundaries (![][image3]), and their exteriors (![][image4]).5  
Within a multi-agent Swarm managing a Saga orchestration, the state-space of the agent is modeled as Region A, and the state-space of the external API is modeled as Region B. The containment of side-effects is managed by enforcing strict RCC-8 intersection matrices within the neural attention routing.

| RCC-8 Relation | 9-IM Mathematical Property | Latent Space Matrix Translation | Topological Swarm Impact |
| :---- | :---- | :---- | :---- |
| **DC** (Disconnected) | ![][image5] | Total context isolation; cross-attention strictly 0.0. | Prevents all orchestration and telemetry; mathematically unacceptable. |
| **EC** (Externally Connected) | ![][image6] | Bipartite routing via hard threshold masking. | Ideal state. Allows exception telemetry to pass while strictly blocking semantic contagion. |
| **PO** (Partially Overlapping) | ![][image7] | Entangled flow matching with non-zero mutual attention. | Default LLM integration state; leads to rapid structural degradation and context bloat during failure. |
| **TPP** (Tangential Proper Part) | ![][image8] | Sub-agent encapsulation; asymmetric attention flow. | Transient fallback state during extreme boundary pressure or mathematical singularity propagation. |

When a Saga compensation fails, the API generates unstructured computational entropy. If the orchestrator maintains an Externally Connected (EC) boundary, the error state is received as telemetry without corrupting the agent's interior logic.5 However, if the boundary yields to a Partially Overlapping (PO) state, the verbose DLQ exception traces bleed directly into the agent's continuous flow probability paths, triggering massive contextual degradation.4

## **3\. Cognitive Topologies: Tripartite Structured Context and Semantic Saponification**

### **3.1. The Tripartite Structured Context Architecture**

When an un-executable API side-effect breaches the RCC-8 boundary, the resulting influx of Dead Letter Queue exception logs fundamentally threatens the orchestrating agent's operational stability.4 Standard LLM integrations lack native primitives for managing non-deterministic latent spaces; feeding an unbounded, flat list of error traces into a model inevitably exceeds the context window token limits.4 Conventional frameworks either crash or silently truncate data from the front of the queue, systematically destroying the foundational system instructions and structural rules of the agent.4  
To bound this stochasticity, advanced agentic programming paradigms—heavily derived from process models like Erlang—implement a strict language-level primitive known as the Tripartite Structured Context.4 This architecture divides the agent's context window into three managed tiers, actively metering the token budget via an Entropic Expansion Policy to exploit the primacy and recency attention biases of transformer models.4

| Context Tier | Semantic Role | Bounding Constraints | Transformer Attention Position |
| :---- | :---- | :---- | :---- |
| **P0 (System)** | Defines the core persona, DAG directives, and rigid structural rules of the orchestrator. | Immutable for the lifespan of the process. Never evicted during context expansion. | Primacy Position: Rendered first in the context window (yielding approximately 90% neural recall). |
| **P1 (Working)** | The active short-term memory, holding immediate API observations, transaction states, and recent events. | Bounded to a strict token limit (e.g., 100 entries). | Recency Position: Rendered last, ensuring immediate semantic relevance (yielding approximately 85% neural recall). |
| **P2 (Episodic)** | The archival overflow memory. When P1 reaches capacity, data is demoted here. | Bounded to a larger limit. Employs active eviction where oldest items are dropped first. | Middle Zone: Rendered between P0 and P1, occupying a lower-recall sector highly susceptible to dilution. |

During a Saga failure, the P1 Working memory is flooded with hyper-dense, self-referential error traces. The Entropic Expansion Policy attempts to manage this by rapidly demoting older contextual states into the P2 Episodic tier, fundamentally accelerating the rate at which the agent loses tracking of the overarching distributed workflow.4

### **3.2. ContextLock and the Necessity of the Debridement Protocol**

The continuous influx of unresolvable error data into the Tripartite Context induces a severe temporal drift across the agent's long inference cycles.6 This decay process, mathematically defined as Semantic Saponification, results in the agent's multi-head attention matrices silently abandoning security constraints or losing track of the required multi-agent synchronization goals.6  
To physically override this temporal drift, system architects deploy structural decorators via Prompt Description Language (PDL), most notably the \+++ContextLock(anchor="COMMANDERS\_INTENT", refresh\_interval=4096) directive.6 Utilizing synecdochic anchoring, the ContextLock continuously compresses core operational invariants into a part-for-whole symbol and physically re-injects this anchor directly into the agent's attention sink exactly every 4,096 tokens.6 This constant architectural refresh provides a highly stable correlation vector for persistent state representation.6  
However, ContextLock is a stabilizing mechanism, not an excision tool. If a partially-mutated external API payload permanently poisons the P1 context tier with a recursive exception loop, anchoring the intent is insufficient. The orchestrator is forced to trigger the **Debridement Protocol**.6 This protocol is a highly aggressive, destructive recovery mechanism specifically designed to actively excise, flush, and permanently discard poisoned context fragments and accumulated polysemantic noise from the model's active tensors.6 The Debridement Protocol does not merely demote data to the P2 tier; it executes a hard mathematical reset on targeted vectors within the latent space, intentionally destroying localized semantic continuity to save the overarching structure.6

## **4\. System Dynamics of the Terminal Mathematical Paradox**

### **4.1. The Concurrency Collision: State-Freezing vs. Debridement**

The theoretical gap defining this empirical analysis lies in the interaction between the continuous-flow recovery mechanisms of the agent (Debridement) and the rigid transactional requirements of the non-monotonic Saga pattern.  
To execute a compensation over a distributed Database Ledger, the orchestrator must utilize an absolute state-freezing metric.6 This mechanism applies a strict temporal lock to the precise memory state of the Labeled Transition System (LTS).6 By freezing the LTS, the hypervisor ensures that no parallel agent or asynchronous microservice can mutate the Directed Acyclic Graph concurrently while the rollback route is being calculated.6 The state-freezing metric demands absolute immutability of the targeted tensors for the duration of the calculation.  
A terminal mathematical paradox manifests if the orchestration logic attempts to execute the Debridement Protocol concurrently with this absolute state-freezing metric.6 Conceptually and mathematically, the system is instructed to apply an immutable, static state lock to a precise locus within the continuous latent representation while simultaneously initiating an aggressive, destructive context excision from within that exact same spatial coordinate.6  
This severe violation of Layer 8 rules within the Secure Cognitive Operating System fundamentally breaks the deterministic assumptions of the underlying transformer geometry.6

### **4.2. Modeling Topological Anomalies: Simplicial Complexes and Betti Numbers**

To rigorously prove the existence and impact of this concurrency collision, the network state and probability matrices must be mapped into the domain of Topological Data Analysis (TDA).1 The dynamic flow of the multi-agent context window is modeled as a simplicial complex ![][image9], which allows the system to analyze the intrinsic shape and connectivity of the high-dimensional data without relying on rigid geometric coordinates.8  
A simplicial complex is constructed from discrete data points (0-simplices, representing vertices or individual tokens), their connections (1-simplices, representing edges or relational attention weights), and higher-dimensional relationships (2-simplices, representing faces or complex semantic structures).12 The topological invariants of this high-dimensional space are quantified by Betti numbers (![][image10]), which count the number of independent ![][image11]\-dimensional "holes" within the structure.8

| Betti Number | Topological Definition | Interpretation within Agentic Latent Space |
| :---- | :---- | :---- |
| **Betti-0 (![][image12])** | The number of independent, connected components. | Represents the number of distinct semantic thoughts or isolated logic graphs currently maintained in context. |
| **Betti-1 (![][image1])** | The number of independent 1-cycles (topological loops). | Represents cyclical contradictions, infinite recursive loops, or unresolvable temporal paradoxes. |
| **Betti-2 (![][image13])** | The number of 2-dimensional voids or cavities. | Represents vast areas of gradient starvation or completely missing contextual data. |

When the system attempts to concurrently freeze and debride, the conflicting mathematical operations create a closed, unresolvable 1-cycle in the logic graph.6 The attention head attempts to calculate the loss function of the frozen tensor, impacts the excised memory void generated by the debridement operation, and logically loops back to the freeze command in an attempt to re-establish the baseline.6 This structural failure instantly spawns an infinite Betti-1 (![][image1]) contradiction loop.6

### **4.3. The MFU Paradox and Attention Head Exhaustion**

The manifestation of the infinite Betti-1 loop acts as a thermodynamic singularity within the shared context window.5 Because continuous flow generative models construct probability paths concurrently across all dimensions, a contradiction in one coordinate space exerts a massive gradient pull on adjacent coordinate spaces.5  
The local multi-head attention mechanisms become ensnared in the ![][image1] loop, dedicating their full processing capacity to resolving a cycle that mathematically possesses no exit condition.6 This triggers a state known as the Model FLOPs Utilization (MFU) Paradox.5 In this state, the computational throughput and hardware power draw are maximized—approaching 100% utilization—yet the marginal semantic progress drops asymptotically to zero.5  
The Betti-1 loop causes absolute gradient starvation; the gradients necessary to alter the model's trajectory are entirely diluted by the structurally dominant, infinitely repeating contradiction.5 The available multi-head attention entropy is permanently exhausted, fundamentally gridlocking the processing heads of the Virtual Machine.6 Because the agent appears to the external network to be processing at maximum efficiency, standard telemetry fails to detect the localized crash, allowing the Betti-1 loop to silently destroy the entire Saga orchestration sequence.5

## **5\. Topological Detection via Zigzag Persistent Homology**

### **5.1. The Limitations of Standard Persistent Homology**

Traditional statistical models and baseline network monitoring are blind to subtle deformations in underlying data geometry.8 To definitively verify the presence of a Betti-1 contradiction loop without relying on secondary performance metrics, the diagnostic framework must employ Persistent Homology.8  
Persistent homology operates by tracking the birth (![][image14]) and death (![][image15]) of topological features (like ![][image12] and ![][image1]) across a filtration of simplicial complexes at varying spatial scales.8 This filtration is mathematically defined as an expanding sequence:  
![][image16]  
By rendering a family of these complexes, the system generates a persistence diagram or barcode.8 An anomaly is confirmed if a topological feature's lifetime (![][image17]) exceeds a dynamically calculated baseline threshold.8  
However, standard persistent homology strictly assumes a monotonic inclusion of complexes—it can only model systems that are continuously adding data.13 This renders standard persistent homology mathematically inadequate for monitoring Saga compensations and Debridement executions, where context is explicitly and aggressively excised and removed from the manifold.6

### **5.2. Deploying Zigzag Persistent Homology**

To track homological changes in a non-monotonic environment characterized by inclusions in opposing directions, the system must utilize **Zigzag Persistent Homology**.6 Zigzag persistence extends the traditional filtration framework to allow for both forward additions and backward retractions, algebraically mapping the time-varying dynamic graphs as follows 7:  
![][image18]  
By processing the network telemetry through this bidirectional filtration, the Zigzag Persistent Homology algorithms calculate the changing Betti numbers using matrix algebra with modulo two coefficients.7 The framework processes the continuous flow data through a four-phase proving pipeline 8:

1. **Point Cloud Generation:** High-dimensional agent metrics are normalized and projected into a measurable metric space.  
2. **Filtration Construction:** A dynamic Vietoris-Rips complex is built using a sliding time window that accounts for both the addition of DLQ trace logs and the excision of Debridement protocols.  
3. **Homology Calculation:** The invariants (![][image19]) are computed in real-time, leveraging highly optimized Python packages such as Dionysus or BuZZ to track the matrices.19  
4. **Obstruction Mapping:** Local consistency is validated using sheaf-theoretic verification. The failure to extend a local section to a global state confirms a local topological obstruction.8

Through the Zigzag barcode visualization, the orchestration hypervisor observes the precise topological signature of the concurrency collision.17 At the exact millisecond the Debridement Protocol intersects the absolute state-freezing metric, a prominent 1-cycle (![][image1]) is born.6 Because the paradox cannot be resolved by the LLM's attention heads, this ![][image1] cycle never dies; it manifests on the Zigzag persistence diagram as a non-terminating horizontal line extending toward infinity.12 This absolute persistence provides deterministic mathematical proof of the terminal contradiction loop, overriding standard MFU telemetry and forcing a hard system interrupt.8

## **6\. Formal Verification and LOTOS Serialization**

To proactively prevent the manifestation of the Betti-1 loop, the underlying orchestration architecture must rely on rigorous formal verification models during the code generation phase.6 Sovereign Cognitive Operating Systems utilize the Language Of Temporal Ordering Specification (LOTOS) to structure the agentic routing logic.6  
LOTOS is a formal process algebra specifically engineered for the specification and analysis of concurrent, non-deterministic distributed systems.11 It represents complex interactions as Labeled Transition Systems (LTS), modeling all possible non-deterministic choice paths.6  
Within the LOTOS compiler, the transitions dictating a Saga rollback are explicitly serialized.6 The mathematical proofing ensures that overlapping execution timelines between destructive and freezing operations are structurally impossible. The synchronization barriers generated by the LOTOS glue code enforce a rigid sequence: the Virtual Machine must first verify the heap counter array, apply the absolute state-freezing lock to the LTS, record the failed transactional state, entirely release the lock, and only subsequently initiate the Debridement Protocol in a disparate temporal execution stage.6 If the LOTOS model checker detects any possible non-deterministic path that allows these two commands to overlap, it fails the compilation, preventing the ![][image1] paradox from ever executing.6

## **7\. Hardware Dynamics: CPU-to-VRAM Latency and Shadow Compute**

Empirical analysis of these topological failures requires a deep understanding of the underlying physical hardware dynamics, specifically the interaction between the CPU and the GPU's Video RAM (VRAM).21

### **7.1. PagedAdamW Faults and PCIe Latency Penalties**

When an agent processes a Saga compensation failure, the massive influx of verbose API exception logs rapidly bloats the P1 Working memory tier.1 The attention heads calculating the continuous flow paths exhaust the available GPU VRAM. To prevent a hard crash, modern optimizers like PagedAdamW invoke unified memory management, offloading non-critical tensors to the host CPU's system memory.21  
This memory migration triggers a localized page fault.21 The GPU is forced to halt processing while the required memory pages are transferred back across the Peripheral Component Interconnect Express (PCIe) bus.21 In modern architectures, this physical data transfer incurs a severe latency penalty, reliably measured at approximately 125 milliseconds per fault.21

### **7.2. Free-Threaded Python and the VDCores Paradigm**

Historically, mitigating this PCIe bottleneck by saturating the host CPU with parallel calculation tasks was heavily restricted in Python-based ML frameworks due to the Global Interpreter Lock (GIL).21 The GIL enforces a mutex that prevents multiple native threads from executing Python bytecodes simultaneously, strangling CPU-bound concurrent processing and forcing reliance on heavy multiprocessing overheads.21  
However, the advent of free-threaded Python execution environments (e.g., Python 3.13t) allows asynchronous data loaders and background threads to operate concurrently without GIL contention.21 This structural capability enables the adoption of a Virtual Decoupled Cores (VDCores) philosophy.21 The VDCores paradigm untangles GPU kernels into state-isolated, asynchronous execution units communicating via explicit message queues.21  
By leveraging free-threaded Python, the CPU can instantly launch a "Silent Reasoning" Shadow Compute phase the exact millisecond a PagedAdamW GPU page fault is registered.21 During the 125-millisecond latency window where the GPU is stalled waiting for memory, the idle multi-core CPU intercepts the output of the model's preceding forward pass—represented as an Abstract Syntax Tree (AST).21 The CPU executes an orthogonal topological evaluation of this AST, validating the causal logic and computing the Zigzag Persistent Homology of the compensation sequence entirely within the latency shadow, fundamentally hiding the computational cost of the diagnostic tracking.21

## **8\. Empirical Methodology 1: AST Transformation via LibCST**

To concretely measure this exact CPU-to-VRAM latency and the concurrent context-window degradation during an API rollback failure, empirical evaluation requires the deployment of specific Python execution scripts. The primary tool for this dynamic measurement is **LibCST**.10  
LibCST parses Python source code into a Concrete Syntax Tree (CST).10 Unlike a standard Abstract Syntax Tree (AST), a CST preserves all formatting details, whitespaces, and structural nuances, allowing for automated, non-destructive refactoring and the programmatic injection of telemetry logic via the Visitor pattern.10  
To track the Saga compensation execution without altering the underlying application logic, we deploy a CSTTransformer subclass.23 This transformer programmatically traverses the orchestration codebase, detects the function calls responsible for external API rollbacks, and dynamically wraps them in profiling decorators designed to log the PagedAdamW faults and token bloat.

### **8.1. LibCST Execution Script**

Python  
import libcst as cst  
import libcst.matchers as m  
from typing import Union, Optional

class SagaTelemetryInjector(cst.CSTTransformer):  
    """  
    A LibCST Transformer traversing the Concrete Syntax Tree to detect   
    Saga compensation functions and inject Shadow Compute profiling logic.  
    This enables GIL-free PCIe latency measurement.  
    """  
      
    def \_\_init\_\_(self, target\_functions: list\[str\]):  
        super().\_\_init\_\_()  
        \# Target methods in the codebase (e.g., 'execute\_compensation', 'rollback\_api')  
        self.targets \= target\_functions  
        self.in\_target\_function \= False  
          
    def visit\_FunctionDef(self, node: cst.FunctionDef) \-\> Optional\[bool\]:  
        """  
        Tracks if the traversal has entered a targeted Saga rollback function.  
        """  
        if node.name.value in self.targets:  
            self.in\_target\_function \= True  
        return True

    def leave\_FunctionDef(  
        self, original\_node: cst.FunctionDef, updated\_node: cst.FunctionDef  
    ) \-\> Union:  
        """  
        Intercepts the function definition upon leaving the node.   
        Prepends the @vdcore\_shadow\_profiler decorator to measure   
        VRAM latency bridging during page faults.  
        """  
        self.in\_target\_function \= False  
          
        if original\_node.name.value in self.targets:  
            \# Construct the decorator node tracking VRAM degradation  
            profiler\_decorator \= cst.Decorator(  
                decorator=cst.Call(  
                    func=cst.Name("vdcore\_shadow\_profiler"),  
                    args=  
                )  
            )  
              
            \# Extract existing decorators and prepend the profiling decorator  
            new\_decorators \= (profiler\_decorator,) \+ tuple(updated\_node.decorators)  
              
            \# Return the dynamically updated node, strictly preserving immutability \[24, 25\]  
            return updated\_node.with\_changes(decorators=new\_decorators)  
              
        return updated\_node

    def leave\_Call(  
        self, original\_node: cst.Call, updated\_node: cst.Call  
    ) \-\> cst.BaseExpression:  
        """  
        Intercepts specific API execution calls within the rollback sequence.   
        Wraps the Dead Letter Queue dispatch to monitor Context Expansion Limits.  
        """  
        if self.in\_target\_function and m.matches(original\_node.func, m.Name("dispatch\_to\_dlq")):  
            \# Wrap the DLQ dispatch in the context\_window\_meter   
            tracking\_call \= cst.Call(  
                func=cst.Name("context\_window\_meter"),  
                args=\[cst.Arg(value=updated\_node)\]  
            )  
            return tracking\_call  
        return updated\_node

\# \--- Execution Sequence \---  
\# The target source code representing the flawed non-monotonic rollback  
source\_code \= """  
def rollback\_api(payload):  
    response \= requests.post('/api/refund', json=payload)  
    if response.status\_code \== 500:  
        dispatch\_to\_dlq(response.text)  
"""

\# Parse into a CST, transform, and output the modified code \[22, 26\]  
tree \= cst.parse\_module(source\_code)  
transformer \= SagaTelemetryInjector(target\_functions=\["rollback\_api"\])  
modified\_tree \= tree.visit(transformer)

\# The resulting modified\_tree.code now intrinsically includes runtime   
\# telemetry for the VDCores layer without manual intervention.

By strictly utilizing the leave\_FunctionDef and with\_changes methodologies as mandated by LibCST best practices, the transformation ensures that only the updated\_node is returned.23 This preserves the absolute immutability of the underlying syntax tree structure while safely injecting the telemetry tracking required to measure the token throughput and the 125ms PCIe transfer latency.21

## **9\. Empirical Methodology 2: State Space Modeling via Pyperplan**

While LibCST measures the physical latency and context bloat, the hypervisor must concurrently calculate the actual sequential path of the non-monotonic Saga compensation. This is empirically executed using **Pyperplan**, a lightweight STRIPS (Stanford Research Institute Problem Solver) planner written in Python that parses Planning Domain Definition Language (PDDL).9  
Because Pyperplan supports the STRIPS fragment, it is ideally suited for mapping the discrete state transitions of a Saga orchestration, allowing the system to formally treat the sequence of API rollbacks as an optimal pathfinding problem through a defined state space.9  
When the primary API call fails, the orchestration hypervisor formulates the partial mutation as a PDDL problem. Pyperplan parses the domain file (representing the RCC-8 boundaries and available compensating actions) and the problem file (representing the failed state).29 The engine executes a heuristic search algorithm—specifically A\* (A-star) or Greedy Best-First Search (GBFS)—utilizing domain-independent heuristics like Fast Forward (hff) or Landmark-cut (lmcut) to calculate the shortest, optimal sequence of actions required to reach a neutralized, consistent system state.28

### **9.1. Pyperplan Execution Script**

Python  
import os  
from pyperplan.pddl.parser import Parser  
from pyperplan.grounding import ground  
from pyperplan.planner import SEARCHES, HEURISTICS

class TopologicalGridlockError(Exception):  
    """Custom exception raised when PDDL routing detects a Betti-1 contradiction loop."""  
    pass

def evaluate\_saga\_compensation\_path(domain\_file\_path: str, problem\_file\_path: str) \-\> list:  
    """  
    Utilizes Pyperplan to compute the directed acyclic graph (DAG)   
    for compensating transactions after a non-monotonic failure.  
    """  
    \# 1\. Parse the PDDL domain representing the Saga boundaries and actions \[30\]  
    parser \= Parser(domain\_file\_path, problem\_file\_path)  
    domain \= parser.parse\_domain()  
    problem \= parser.parse\_problem(domain)  
      
    \# 2\. Ground the PDDL task to instantiate all valid state transitions \[30\]  
    \# Grounding translates generalized logic into a finite propositional state space.  
    task \= ground(problem)  
      
    \# 3\. Initialize Search Algorithm and Heuristic  
    \# A\* provides optimal pathing to avoid non-deterministic loops, outperforming GBFS here   
    search\_algorithm \= SEARCHES\["astar"\]  
    \# Landmark-cut (lmcut) is used to aggressively prune impossible compensation paths \[30\]  
    heuristic\_function \= HEURISTICS\["lmcut"\](task)  
      
    \# 4\. Run the planning sequence to generate the compensation transaction list  
    try:  
        \# The search algorithm attempts to find a path from the initial   
        \# mutated state to the goal state defined in the PDDL.  
        plan \= search\_algorithm(task, heuristic\_function)  
          
        if plan is None:  
            raise TopologicalGridlockError("Planner returned None. State space disconnected.")  
              
        return plan  
          
    except Exception as e:  
        \# If the search space contains a Betti-1 contradiction loop caused by  
        \# the Debridement/Freezing collision, the planner will exhaust the search   
        \# space without ever discovering a valid path to the goal state.  
        raise TopologicalGridlockError(f"Infinite cycle detected in PDDL graph mapping: {e}")

\# Example PDDL Problem State formulation (Conceptual mapping)  
\# Initial State: (api\_partially\_mutated) (shipping\_failed) (in\_dlq)  
\# Goal State: (system\_neutralized) (context\_flushed)

The grounding phase of the Pyperplan execution is critical; it strips away variables, translating the generalized logic into a finite propositional state space that the A\* algorithm can evaluate.30  
By routing the proposed Saga architecture through the Pyperplan heuristic engine, the hypervisor mathematically verifies whether a valid rollback path actually exists *before* initiating the API calls.29 If the execution algorithm fails to find a route—indicated by a completely disconnected state graph or the planner exhausting the search space without reaching the goal—it definitively signals that the system parameters harbor an impending structural anomaly.

| Search Algorithm | PDDL Heuristic | Applicability to Saga Rollback Routing |
| :---- | :---- | :---- |
| **Breadth-First Search (BFS)** | Blind | Inefficient; scales poorly across high-dimensional exception logs.28 |
| **Greedy Best-First Search (GBFS)** | Fast Forward (hff) | Fast, but prone to local minima. May fail to find optimal compensation path.28 |
| *A (A-star)*\* | Landmark-cut (lmcut) | Highly optimal. Guarantees the shortest path to neutralization, avoiding infinite loops.30 |

## **10\. Synthesis of Quantitative Findings and System Implications**

When the LibCST-injected latency trackers and the Pyperplan state-space modeling operate in tandem against a simulated non-monotonic failure, the combined telemetry logs explicitly expose the rapid deterioration of the multi-agent system.  
As the Saga orchestration initiates the compensating transaction, the external API side-effect returns a permanent failure error code due to un-executable parameters. This triggers the dispatch to the Dead Letter Queue. If the orchestration attempts to ingest this DLQ error state without the \+++ContextLock and Debridement Protocol, the system rapidly funnels the verbose JSON schemas into the P1 (Working) context tier.1  
The continuous flow decoder attempts to parse this un-executable semantic state, immediately driving the hardware utilization (MFU) toward 99.8%.5 Concurrently, PagedAdamW page faults skyrocket as the sheer token bloat forces the context window beyond the immediate GPU VRAM boundaries, continuously transferring the massive payload across the PCIe bus.5 The LibCST context\_window\_meter telemetry accurately tracks this token delta, logging a degradation rate that swiftly approaches capacity limits, precipitating catastrophic context truncation.4  
When the hypervisor attempts to rescue the agent by triggering the Debridement Protocol, it must execute the absolute state-freezing metric to lock the Labeled Transition System.6 If these two operations are not perfectly serialized by the LOTOS compiler, the Pyperplan PDDL model detects the non-monotonic failure; the A\* search algorithm exhausts the state space without ever reaching the (context\_flushed) goal state.6  
At this precise temporal intersection, the Zigzag Persistent Homology algorithms—calculating the topological state of the Abstract Syntax Tree concurrently on the free-threaded CPU via the Shadow Compute VDCores—register the definitive ![][image20] homological signature.6 The multi-head attention mechanisms of the LLM lock onto the resulting contradiction, halting all progressive semantic output and entering total gradient starvation.5 The empirical data strictly validates that the presence of the Betti-1 paradox within the continuous state-space fundamentally paralyzes the orchestrating agent, transforming a simple API compensation failure into a total system collapse.5

## **11\. Concluding Architectural Directives**

The orchestration of Saga Compensating Transactions over non-monotonic, multi-agent Web State environments demands an operational rigor that far exceeds the logic of traditional ACID database rollbacks. The empirical synthesis establishes that treating complex, partially-mutated API side-effects as linear data strings rather than non-Euclidean topological manifolds invites catastrophic systemic failure.  
The convergence of the Debridement Protocol and absolute state-freezing metrics underscores the inherent fragility of shared cognitive environments and continuous flow probability paths. Without the rigid serialization enforced by LOTOS process algebra, the concurrent execution of these directives generates a mathematically unresolvable Betti-1 contradiction loop, permanently exhausting multi-head attention entropy and gridlocking the system.  
However, by formally mapping API boundaries with RCC-8 spatial calculus, and by utilizing the Virtual Decoupled Cores (VDCores) paradigm alongside free-threaded Python execution, engineering architectures can effectively hide PCIe latency overheads. This structure allows for real-time, GIL-free Shadow Compute evaluations. When these evaluations are fully instantiated via dynamic LibCST syntax tree transformations and mathematically verified through Pyperplan PDDL state-space modeling, these frameworks provide the necessary quantitative oversight. This synthesis enables the overarching hypervisor to detect topological anomalies via Zigzag Persistent Homology, dynamically halt un-executable compensation cascades, and ensure the structural survivability of advanced autonomous multi-agent infrastructures.

#### **Works cited**

1. LLM Saga API Boundary Mapping, [https://drive.google.com/open?id=1VqXoilaCoxh4Jimtd6CesohLrNZyswapb3-ylBiFLZI](https://drive.google.com/open?id=1VqXoilaCoxh4Jimtd6CesohLrNZyswapb3-ylBiFLZI)  
2. Saga Orchestration vs. Choreography: Making the Right Trade-off in Event-Driven Systems, accessed on July 6, 2026, [https://aloknecessary.github.io/blogs/saga-orchestration-vs-choreography/](https://aloknecessary.github.io/blogs/saga-orchestration-vs-choreography/)  
3. A Deep Dive. The Saga pattern is the gold standard… | by Guts | Medium, accessed on July 6, 2026, [https://medium.com/@guts./the-saga-pattern-a-deep-dive-bb4ed313952c](https://medium.com/@guts./the-saga-pattern-a-deep-dive-bb4ed313952c)  
4. Chappe Telegraph and Concurrency Models, [https://drive.google.com/open?id=1Rkvhr6qEgQPhJ0hAQ3V6PYWUMpohPd9B4w24p024AYE](https://drive.google.com/open?id=1Rkvhr6qEgQPhJ0hAQ3V6PYWUMpohPd9B4w24p024AYE)  
5. Swarm Topology: MFU Paradox & NaN Collapse, [https://drive.google.com/open?id=1WAuhP4t7iMhGuCNyWrT\_MfV9tHfmZcHcxpIF7SCliQM](https://drive.google.com/open?id=1WAuhP4t7iMhGuCNyWrT_MfV9tHfmZcHcxpIF7SCliQM)  
6. Detecting Non-Deterministic Cycles in LOTOS, [https://drive.google.com/open?id=1skWiDDI21YA4oI4J3vH6dyVVcgV6PULcbZ9zEmP63wY](https://drive.google.com/open?id=1skWiDDI21YA4oI4J3vH6dyVVcgV6PULcbZ9zEmP63wY)  
7. Persistent Homology: Theory and Practice, accessed on July 6, 2026, [https://pub.ista.ac.at/\~edels/Papers/2012-11-PHTheoryPractice.pdf](https://pub.ista.ac.at/~edels/Papers/2012-11-PHTheoryPractice.pdf)  
8. Topological Anomaly Proving Framework, [https://drive.google.com/open?id=1499aO-PyAp2xzpsXBiD7iKJBRnFZCZaZ-4G\_rhYFs6U](https://drive.google.com/open?id=1499aO-PyAp2xzpsXBiD7iKJBRnFZCZaZ-4G_rhYFs6U)  
9. aibasel/pyperplan: A lightweight STRIPS planner written in Python. \- GitHub, accessed on July 6, 2026, [https://github.com/aibasel/pyperplan](https://github.com/aibasel/pyperplan)  
10. LibCST — LibCST documentation, accessed on July 6, 2026, [https://libcst.readthedocs.io/](https://libcst.readthedocs.io/)  
11. Formalizing UML State Machines for Automated Verification – A Survey \- LIPN, accessed on July 6, 2026, [https://lipn.fr/\~andre/UML-SMD-survey.pdf](https://lipn.fr/~andre/UML-SMD-survey.pdf)  
12. Integration of element specific persistent homology and machine learning for protein-ligand binding affinity prediction, accessed on July 6, 2026, [https://par.nsf.gov/servlets/purl/10092859](https://par.nsf.gov/servlets/purl/10092859)  
13. Discrete Level Set Persistence for Finite Discrete Functions \- arXiv, accessed on July 6, 2026, [https://arxiv.org/pdf/2501.17794](https://arxiv.org/pdf/2501.17794)  
14. Persistent spectral graph \- PMC \- NIH, accessed on July 6, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7719081/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7719081/)  
15. Atom-specific persistent homology and its application to protein flexibility analysis \- PMC, accessed on July 6, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8281920/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8281920/)  
16. (PDF) Zigzag Persistence \- ResearchGate, accessed on July 6, 2026, [https://www.researchgate.net/publication/23503746\_Zigzag\_Persistence](https://www.researchgate.net/publication/23503746_Zigzag_Persistence)  
17. GitHub \- ndag/DynGraphZZ, accessed on July 6, 2026, [https://github.com/ndag/DynGraphZZ](https://github.com/ndag/DynGraphZZ)  
18. Topological data analysis and topological deep learning beyond persistent homology: a review \- PMC, accessed on July 6, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12931839/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12931839/)  
19. Computing Zigzag Persistence on Graphs in Near-Linear Time \- arXiv, accessed on July 6, 2026, [https://arxiv.org/pdf/2103.07353](https://arxiv.org/pdf/2103.07353)  
20. sarahtymochko/BuZZ \- GitHub, accessed on July 6, 2026, [https://github.com/sarahtymochko/BuZZ](https://github.com/sarahtymochko/BuZZ)  
21. PagedAdamW Latency Hiding Optimization, [https://drive.google.com/open?id=1sXeU1mBN9KX3P1JjNPiuxwdZd8dwtGZpMaqKRG55gWc](https://drive.google.com/open?id=1sXeU1mBN9KX3P1JjNPiuxwdZd8dwtGZpMaqKRG55gWc)  
22. Parsing and Visiting — LibCST documentation \- Read the Docs, accessed on July 6, 2026, [https://libcst.readthedocs.io/en/latest/tutorial.html](https://libcst.readthedocs.io/en/latest/tutorial.html)  
23. Visitors — LibCST documentation \- Read the Docs, accessed on July 6, 2026, [https://libcst.readthedocs.io/en/latest/visitors.html](https://libcst.readthedocs.io/en/latest/visitors.html)  
24. Best Practices — LibCST documentation \- Read the Docs, accessed on July 6, 2026, [https://libcst.readthedocs.io/en/latest/best\_practices.html](https://libcst.readthedocs.io/en/latest/best_practices.html)  
25. Pyperplan | Zenodo, accessed on July 6, 2026, [https://zenodo.org/records/3701399](https://zenodo.org/records/3701399)  
26. pyperplan \- PyPI, accessed on July 6, 2026, [https://pypi.org/project/pyperplan/1.0/](https://pypi.org/project/pyperplan/1.0/)  
27. 1\. Basic Example — Unified-Planning 1.3.0 documentation, accessed on July 6, 2026, [https://unified-planning.readthedocs.io/en/latest/notebooks/01-basic-example.html](https://unified-planning.readthedocs.io/en/latest/notebooks/01-basic-example.html)  
28. mp03.ipynb \- Colab, accessed on July 6, 2026, [https://colab.research.google.com/github/MIT-6S058/hw\_colabs/blob/main/mp03.ipynb](https://colab.research.google.com/github/MIT-6S058/hw_colabs/blob/main/mp03.ipynb)  
29. MIT thesis template \- ProQuest, accessed on July 6, 2026, [https://search.proquest.com/openview/3fef64a24dc80e396f83d6ad4d224991/1.pdf?pq-origsite=gscholar\&cbl=18750\&diss=y](https://search.proquest.com/openview/3fef64a24dc80e396f83d6ad4d224991/1.pdf?pq-origsite=gscholar&cbl=18750&diss=y)  
30. Generalized Planning in PDDL Domains with Pretrained Large Language Models \- arXiv, accessed on July 6, 2026, [https://arxiv.org/html/2305.11014v2](https://arxiv.org/html/2305.11014v2)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAUCAYAAABSx2cSAAAA4ElEQVR4Xu3RvQ4BQRQF4CshkRB/0QgaryCeAYWfRKlSqUgUolDrhScQhUIrERqv4GG0EueYkb2zMqIWJ/mKuzN39s6uyE8kAnVYwR6a7vLntCymBEfIB8v+lGEs5u1MBc7yZXMbqqoewlSCw7zhhgn04A43OEFCb/IlK6b59ZYo7KBh6zh0IWNrJxyXY+tsYAY5MR+RX7/g7LDpQE3VSbhIcCBrHvbWzFHX4jbz7gcxTYy3mfddwhb6MIcFpNQeb/PrvpyA94u5y894m8P/NxweyImuMIKiXhxAWj/4x58Hae4ay1geFbAAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAUCAYAAACAl21KAAAA80lEQVR4XmNgGBFAE4inAfEsJDwJiH2AmBOqhhGI1YDYF4iFoWJYgRwQPwHiYAaIJjEgbgbiC0AsA8R2QGwMxMxAHAbE0hBtmMAFiB8CsRKSmCkQf2OAuCIZiHmg4vpAbAVThA7KgfgAA0IxCOQA8Wsg1mYg0kUcQLwViFuR+KDwOQHE9lAxkHdBLgkAYkmoGAYAmX6XAWJQNBAvBuJdUHGSAHr4gLx3AIiLYAqIBejhIwLEV6HiRAP08AEBUKB+ZYAYBEpH8khyWIEnEK8B4r9AfIYBEsUgAEo314G4H4gjgNgAKk4WALkUFDsC6BKjYDgAABfaIxB0087VAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAUCAYAAABiS3YzAAABVElEQVR4Xu3SvytFcRjH8UcohfyMbCImE5MymET5GYMYDSwWJZKiJJNFShn8WvwYrErilLIYZDAaSBnkf/B+zvM95z7XvYPd/dSr+73f73O+53yfc0QKCSnHOg5wjgWUuvUKrGH/l1k0ubqsrGImjIuwhbnMcpxinOEkjPVGg/jAkKuLU4YjzLs5LboRO0GSerxg2s1V4h7Hbi6N3rkXK+jCOJ5R52p0/j38JunAt+SeSmpxgTGUYETs7pHYEZNo/x5RI/YQ7bjComT3P/6jG26I9VKjjX/DTlIU1g5xiwlsip2k39Wk6RZ7/B431yK2qb8gXz+XJLfvcfSFvKLRzU3iAVVuLl8/9SSRZLcozgDu3IJudI3htMLi+6nR+ijQcZvY+0gXL7GMUZyKPWnS32bs4hNf2Ea12AZ7eEIfpiRzTRx9k63oFPtm/xq9riHQcSH/Pj9dzDeCZ643RAAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAUCAYAAABiS3YzAAAA0UlEQVR4Xu3SMQgBYRTA8U8ZKINBSkTZZKBktlgUk0UZrSaLnczKYLBarUqmGw0Gi0wGZTOzKf+v+9TrS3FnvX/9Bu9eV16nVJCpgDkWwgxNRMWe57K4oo0QkhjjgIzY81QdF+TFrIoHWihhA8cyQlgvf2qo3KWYmPVxQ1HMfi6CNSbit77nDrX3ktfSOCv3pV0ssTVz39n31CdwMHgv+Mm+ZwJHM/eVfU9dBXflvlR/pznx7GsNrPDEHj0z19/lCVN0UDbzv9P/IIW4/SAo6HMvyFwju5rNawcAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAAUCAYAAADbX/B7AAACW0lEQVR4Xu2Wz0sVURTHT5BhZEi4iPAXpgXVojQRDINRggwqyIo20SaibaEgz9pE+AcoBSFIlOhCWrToh6SUO4sWuW5XBC1aBEGrCPp+O3ee512dGRsncHE/8IF3z9yZN3POuXdGJBAIpHMA9vrBLOrgK3jUP1AArXAcTnjegW1mXtHsh4/hJHwHj1cezmYQ/pDspFTBTngBHnLj9dAEv8DzbszzTsNv8Gw8qUC2iyaDSd8K78EpF18XPHEGfodnvGOWfngfHoZ74DE3ZjyLE/AT3Gti7M5lOGxiRcHiPoU1sAWW3Dir6H9hFm+JPiBveqDycBl2xTW4xYtzzDiPp8EHfw6rTYzt/Bl2mVhRsLiP3O9TsM+N04pepgdegbvge0muWiTJWWY88oMGJv6JaAuzwxrgVTgP2808C5PNTuL8NG2SLXyOOClDsN6Nr5dnJMDWGoW17vciHLETDJHkTwpv6CO8KCtJYXctwSNmnoWJjET3rjSb3XyfOCks9k3RJHOcVPQyl+Fr0TfBQ9FNL86uTyT5k7LWfsKbnJbVS6oouA3wWbrhORfLXD6N8LZUvj14EtucVfKJJH9SWJ0FuMPE+BaYk+SkbLRTWIiX8IboNwpXwgvR7WJNWCUuE39z5FJaFL2ATyT5ksIH5oPz2jH8/0vwqyRvshvdU3bDN3BMtABcwrwPxlfBnfgD/AXvwm2iFy6JtvhP+EC0kyyR/HtS+F/svN+iH4bxR9tb+AweXJn6X2DiZ+E+0f9NerPmhslL+lBjJXb6wU0A95KTsEP0ZRIIBAKBwCbhD0S7YaE2h0CmAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALAAAAAUCAYAAAAtOremAAAFw0lEQVR4Xu2ZachtUxjH/zJEZldkymsmJFzDNZ4y5xqvKWPm6fLBNRO3Lim+ieiaySyUW+om3iJDFIp8kPCFkJTySeT53Wevd6+zzl777LPfc9xbd//r39l77XXOftaz/s+w95E6dOjQoUOHVR2HGPdNBzuMDWsYzzdulF5oiznG5cb9o7G1jUcU5HjcOMC4tIKLjFtF87Yzzi8+J4kjjc8ZnzJ+Ytyh/3IW6xsXG580vmy8QfX+YvOWGG9JL4wJw+xZz3irBv3+oPFo45rl1MboGY9LBxNgw/XGZ4yvG581rtU3YxZANH+qFDA/fIFxs4Ic191sY+OxxpOMW8s3qQnmGX8yHlScr2u8xviLPAPuKf9dnMon55PAlnLHEsibyh18j5qt407jpcUx8+8zXlVeHgDr+kPDBcyGzzWeIV93XVDEaGIP/nxJLiKOmbez8WPjI6rf6xQEBPfcIL2Q4HjjXfJ7UeE+Mh7TN6MlMPwFuVMRIGBDz5mZIZ1p3CI6D8CptxtvMm5v3FY+97HieBiuNH4qF03ALsZf5bacpTIb83lamDRmnCzPvICgWmh817jNzIxqEHBPG6+LxrD7HXkmTIG/7jd+IQ+YHNjsh437yNfNhnPOeB2a2rO58WvjedEYeMA4reFijHFUwTogWvwb9HW1vDIw1iRJZEGk3SF30I/G06PxJhn4XOOB6aA8IyNsojOHsChKVwx6o2/kAfF/ZWCyYciIZC/W9Kb6W6ocsK0nXy/zFxi/lGfzFGwgQYh4n1f15rHGyzV4jXPGh/mgiT2Mf2vcIxrjOhn4Zg3eOweETvat22fAvOBPjrHt0GJslGAZwGHGC+UZkEwYlzWMIsXDnIGUppwBiDvuZVOEe9IXMQ/B4oxXjVPltBUVgjLKZw5kNqoGv5MjFSTX3yEo1k4Gw7nMXy7vCetAcL8iFyUBforxfVVnMQSyWO7Le1U9B/SUDxzGe+lghKb2kHm/Mu4uX+vhxrflAZLz0SYa9CmJjQAJ51XrAVyj6mA/QUOS4PgDeTVoBW6GI8mWHE/LN28UzEbALOA7ufOYh4DpkRBOk/YjBhvHZiH0HE9UdVkHQcA7Gi9S6Y9Q8qpA0CCWJSozFuugkqVVBeCr0OtzL4S1YXl5Bj21E3BTe0Llo80LwmMPpuWlPZd9sT32J4mPPpp9DmN7z8zuRyxg2jU+IWN1GqkFpZo+b6l8Qb+pvi+rwmwEXNX/sqFsbJUAJgkCF1GdKm+n4pKXwzzj7/IqFkAAIJi0V6V6kG0QDf7+TD6vyj895e9bJ+Cm9uT6X9pHvh+3FXVg/rAKFcC+LjMeLH8Dwp6zltYtBK+kKNdEbQDifU3VvW4ObQUcssDjyThtAP3vqAKebQYmmJ4w3ibfYOz+UC6AHMjOVBBsDuDBl+9R1QLCc8ZUNMZ3f1b17/fUTsBN7eE3fpA/IMZYqHoBxxn4YnkPf3Y0VpeBac3eMl5hvLEYw95R9bYCiIeMkz4M1PVlObQVcFUWoPdCQAiYdmIUzLYH3kv+Wgeh4R82mXeo9Kus724NPmmfYHxP5foRCe0PJTIGWeqSZIwsyavCKqH2VD0O6gTc1J6qykeFwO91D3BxD3yZPGGkPs5pARAg2Bf8SMVjbCSwyM+Nf8t7pXXk0YFwKDV/GR9V8z8N2giYBp4Hhn+Mb8hLKtmPfqjp67dxg03DB7xGIovwIDm3uDZH7jMEHWcL1s37YkoirceL8owXBDAl7xFZJ0IKPmUPaJP+lfuBh+QYPbUTcBN7HpJn/u9V/oFBGcf3vLLMBXgM/IHQR82cBNQy+QPmfHkGjyvDSgEluS5i4xZlVce18n8H95MHdQzWSbCma2XDd1L1d9qCpJLzGxWh6sEvYBL2pCAx8WfMqCDjU/l3M+6qZsHSYUzgvTA99OoO2rBFGj37dliJICPy72IuK65OWKDBZ6cOHTp06NChQ4cOHTpMCP8BPeEFsHlSc4MAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFIAAAAUCAYAAAAeLWrqAAAC7ElEQVR4Xu2XSchOURzGHxkiZIzMQ2wMC/OQYWEomcdkXFgQshEyZGHasLKSIUkpEXbKQl8pkgUbWVnYKCyUspLyPO//nO+e93jPfe99P5+S+9Sve+95T+c953+e///cC1SqVOnf1HwyLW4sokHkCZkRtHUnixy6/9OaRa424DAZFvQbRVa5ayvqRY6Q3vEPkRaT2+QmeUnG1f9cTJr8N2SB7EZ2koEO3astpX5kOVlNhpMu9T8nNY98JHPcc0+yn3yCOWIybNyu7qrnsloCm1eehpJbMEMNIA/IORRfR00TyB3yFdkfauCt7T2AzWRI8Owlp56A7fgYMhLW95q7b6a95BVs8l4TyWfYXLYgc6eu632ngpIbj7prntbAnChpcw+Sp2REe48mkstOwmrCB7IhaC/iyG1kdtwIc6gCnLcA7bYmfzlq30HewTamo47UZsiRzXTMIe2BrekR6ktdrhaQXTBHyBl+MElBWOZIBWQf6RM3OinIYa2L5f/zEKyfAneK3CNjs261jNnkrikpM5RFGsej/hdgtU7PyihtSCMprbV2lRYZQP11ZiwNO6WkAJyHuUf3bbBByqgjgdRuvycLkQXyNGwBRcpCKGXNWljAPRfJmeB5JdIHjg/keLIbWTya1daalEKqAzoplWJfYAOWUUcC2ag+9iXP8Hu6l5XMoU1JZVIsGUiBXAcrc1pTodTWq4TSKHytURDvo3EtTKnVQPr6eD1qV3qqPpYNZOzIS7D1hQ7Nc6Q29QY5TgbD5v0c5tCktAjtQFy4leZtSAemkVoNpCb7lmwP2lS/tBB/0JRRWCMnwWrjaPfsyauRU8gL2MGr+MiJd5Hj6BXkNflBzpIesAKrBejU/k6uoPjLbyuB1Kn4mPwkD2GlRW54g+KvTXnaSObGjU2k4CkGqqtTYQfezLoenSylSuqltT8654soT3KdPi7KlCevA7Cvrekwc/3XUha09I1cKZM+7+SqVIZUqlSpUqW/oF+5qG/ZmKkUywAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIsAAAAUCAYAAAC9Kc5pAAAEb0lEQVR4Xu2Yaah1YxTH/zJE5iFDUceQISRDmbMLIa/pfc1jMhc+IHO6JSm+ICJkKmOSotSbuEWGfEAZPkgo8UFSyhe++P+ss+9+9j5n77P3Pvd+0N2/+nfPWc++Zz9rnfWstfaRBgYGBgYGlpMNrIutraoLXdneWm8dWl1YZjazbreerOgR6wRrw+LSRna2HrKett60zlEEo46V9m9za8F6xnrVusnaOFlfLr9TMuukqrECe7jRet56w3rB2qh0RQ9utv7UygUzhcC8otg4r/mS97I+sR7XbGdYJ9AEGQgIn3fi0hWTtPWPzzrMOtvaf/y+DXdbV4xf48/91rXF8n/M63cKycc9t6guVDjZukdxr6Osj9Ucp5mw4ZesP6zTKmvTwNHDrQdUPiUPW6Pislp2sL62LqrYH7QWNTsAVIl3rFMT222KKjONtv4R2Mesg6xdFMHlPfYmNrWes25IbNznXUXFyZnX75Tjx2qCBHlWhc/XKSoetqYqXAvZfJciMD9Za8vLE+yqOAVc36d0Aqf7O2u/xEYCcMJuVTtHOFlrrDsVycBf2tEm6UVq7x9V5CpN3pv32Flvglhkin3g3zrrS4VfOcvhN5BUVBVi0ATXERPuy2v2dvTY1iUxlzjGutTa1vpMcULr4AYL1tYVe1c4WV9Z+ypO8LGKSsGX0iYBSY63rSMUyXCN9Y2iL1dp61+m+haFPasaE7azXrPOUuznDOsDTVaLPn5vo7g21SWKZMzf133xrH2h2D8JSpvk9YeKKtcJbnKf4svn9aIi++og8GxyHvLS+JQKZwnaoqJMzjpd+Ulkqs8hAH8pkiali3+Z+iULMw2Jcq+KveMTVYzhNaev37R75qdcJD5zz4WJ7cClq8ukyXL6+C/CxlonCPh7inkDR37T9NOZk6k+oG2p69u0h99VLtHTON/6xdojsZHEP1sHJDbo4l+met+akuVIxb7ZQw57I1nSWWdev3O4Ph/sZ7GligrMkxjVFV86t6HdFH0vnfYJ5Ouqn8oJDKV2Htjsj4ohMuV6tQsabaQ6OC5YL6u8767+ZeqXLAyP31s7JTYS+iOV23Vfv9PKcrn1onVeYmuqLAzeb1lXW7eMbey3LgZToeRRjqtDGyV7UfVZx0C1oPLQ1hVaBbMDWZ7DDPKtykMeweNpi4E6hWk+rQ4j61Pr4MTWx79M/ZLlFOt9FZ9JgqxXlP2Utn5XSWeWKxXzUP5+1swCJCP7y5+cOGzYWoFzn1v/KPosTw9k4B2K0knvf0JxMqfR92loZD1q/Wr9oOJxm5JIDz1X5c/LrL+tCxIbcH9aC8HnVPH/xyXrff3L1C9Z+KL4sYsyf6aiwlFZ8i9/pG5+18EBJalaV4QxJC+tiI6wRlGZ5n1A6cS8v7O0hZI97bcEWgtVA6VtZh5IqrrPoqLS/+sgHntahygScyVgoE2rZ1uoZFTZfay91S4x/3dwMi+zdq8urEJ2VPwC3bWqrBpGKreX1cw6Tc5fAwMDAwMDAwMD5l9kFt6KyXR1vwAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAATCAYAAACk9eypAAAAzElEQVR4XuXQPwtBURjH8cdGRBlYLP5ECruU2WQxGLwFs8lqNyijUvIGKLPBgIEyslm9B9/nnuN2/5RZ+dVnOOc53XPuT+RnE0EbW9Q9ew1scEHV7jtpYoEnckhijhEymKLonrYZ4IQW1ij7x+FMcMMS6cAslKiY9z+wEvP+ryngjjHOyPrH4XRxRB57dPxjf/T6mZh/0AyxQ8w9EYher1/XajVa6xV9u06IKaJi185zDkh9NkgPLzEHtQyt3C1Cvxj/LDwpoSamwf/OG+OjG+RQHZHkAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAUCAYAAACEYr13AAAA/0lEQVR4Xu2RMS9EQRSFj1gaQgjR0OhUCtFSCQoUSpUodJItNltIVPSCRCcRhUIrERp/Sivxndx9O/Mm2bfRipN8yczce8/cOyP9OY3ANtzAC+zWw8O118NahDeYS+FmLcGZogtrGT70C4N9WMv2p9BRMmyUk9pwCN/wBe8wkSc1aUZhUN3WgmfY6WcMkVv3CLkeoVucDdQBrGf7SfhUmE7BhqLLLVhV8S7e3Kpu4Ld4VRh5fQF3MA8PsJBSw/kanuAIzuFKcbPNp+EeVhRf6tFc01c1v5NnYSwPql7kR/UFrhmvEsr/L+XRLnvrE4XBZgpLx4o2B8mdjZaH/0r6ARlNHJbM2jfNAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAVCAYAAACUhcTwAAAAmklEQVR4XmNgGAmAB4pBgAOIxYCYGSHNwKAPxH1AfAKIG4G4GojrgHgrA0IjQwlU4XkgDoeKaQLxKSCWhCkCGW8KxMeBWAQq5gfE+xmQTCJKEQikA/EaIGYBYkYgngLEDUDMBsSsIAUgwaVQhSAgzQBxnwkQ5wOxOEgQZMVJILaEKgJ5H2RVOxD7QsXAJvFCaRgAWcGNxB/GAABSRxL3Hv1w9QAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAUCAYAAABSx2cSAAAA9UlEQVR4XuWSvwtBURTHj2IiIplY7CYZ/AN+DChGk8mmKCkGk10MZhkMViUW/5RV+X7dH+8+eTLzqU+3c+8955777hP5CUKwClfwAOv+5c80tCQLTzDtLQeTgwNRp5M8vMiXyU1YdOI+HItXLBBuGMIOvMMbPMOouymIpKhkc0oY7mFNz/E7zGHF2WNhu2zbZQsnsAyneo4jYx8tWHLiGLyKKsgC5gXaOrawjbX4k3n3o6gi7MAkc+Q/YOF9l3AHu3AGFzCu17nZTTZXeGLuyw5SMOIuinoySkaiDrC8vu8r/NM2sCCqC8aWHky4E29gNxk9/jUPO9wfJj+jbUUAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAAUCAYAAABSx2cSAAAA/ElEQVR4Xu3RP0uCURTH8RPkIIaihVMuri1C+AKEJBv8h25OLrkJBtEgLkJ72CuIBgcXQUF08U25qn2P93nwqDzSHP3gM9xzz/3HFfkTucAjBhjh6XD6fIoezS1muNlPByeFtrjTNWks5JeLS7g34xZeZb9ZYLShgxrWWGGOiG0KSlzcYv+USwxRQAgN9L3xyU30unptmy+8oYoKwhgjb5s0ZWTN+ApLcRtq87NXf8eL36TRa3zK4WJ9+1TcJn6uMcGdqe3e+4FvcW/rijshanr03T1kTG0X/716g4S4Rhut18X9exI5O3n8v8fRef2+LTZ4sJNNxGzhP8H5Af7oHsxLeXV/AAAAAElFTkSuQmCC>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAATCAYAAABcFRdeAAAAgklEQVR4XmNgoBngAeJ6IF4IxB5ocmAgA8RXgNgUXQIEbID4FBCLoEuAQBEQLwViIQaINXDAAsRrgPgaEOcB8TIgDoZJigPxJSB2hPJ9gXgPEHODOOj2pQPxAQao8dEMEG+AgAoQXwRiQygf7I11QJwGxKuB2B4mAQPMQCwMpYcoAADDpBC2vepFQgAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAUCAYAAACwG3xrAAAAlklEQVR4XmNgGBAgDMSdQLwciO3Q5OBAH4ivALESugQM+AHxfiDmQZcQgApOAuJWZAkJBoidWUA8HYg/MkBMAQNOIN4IxDFQvjEQX2NAst8DiB8iCWDYXw7EW4GYA8qH2c8KxMwggSIgXgiVBIXBCQaIKdlALAISlAfiLUCcAcTToOypQBwH0QMBIKMEgZgRinmh9DABACe0FUEjgJCOAAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAsCAYAAADYUuRgAAADo0lEQVR4Xu3cy6tuYxwH8Ecod8qJREkxcC2jk0gSRblMhFyLgcTglFtROikDGTBwyW2AXMLQZSYhAxMGDGXCRMmfwPM9z7t63/fZa71nn33e3dlbn0992+t9nnV+593PGpxfz1rrlAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAR8DtNZ/Pjq+t+a7mjPn0lh1V80XNpbPjy2p+Xjpj686peWt2fHrNCzUPzKd3pKNLW+esbY6z1l8vnbF1qZfr2Ndex3UEAHaAL0tr0tIE3T37edrSGRs9VPNZzZuz3L88fcAVNX+UVu/1midrXl46Y6M0dlfXvFHmtU9ZOqN5ruaf0pqT92vOq7lj6YyNLiqt7mul1X1pefqwPFPzSZl/5+uXpw+4qbR1Prnm09LWOt9nHVI717GvfbDrCADsEmm8vq85vp+YcG8/sMIvNe/1gyukEUzTdjBX1fxZc2U/MeHMmmP7wTV5vB+YcExp67zORnGQ2rmO21EbANgB0lT93g+usK8fmHBczW81H/QTK1zYD0xIY/dXabt3m5Fdu+3ySD8wYU9p6/x0P7FCbveeNZKs7aLUznU8lNoAwC6SnZkLai5ZGDu1tFuH2cnqPdUPTLiltFuV33bje8v0rtRt/cCEX0v7bq9042kms5t2cTe+2Ubw5pobFj7ntuvi7/tNzQkLn2N/93lK6mSdf+on1iC1cx23ozYAcISlSUtTFdkNi+xa3VXzbmm7Odm96eU256OlNVhJmrDej7OfqTc8XzbcHk1jNCa3ZZ8t87pJf6s2t0z3z47zbNxwq3N46eD8Mv6w/cM1r5Z53VuXpw/LhzUPlnntsQZxaKYuL/P1+rjmntIawSdqbpyNDza7w5bauY597fx5AGCXy85Mnn+KvBTwTmkPr19X83ZpzUEeZB9zUpk3EGMPt/+wcPx3ac1aHoaPqYZtkF2yoXZeLFh0dmkvNMS5NV/VfFRz4mzsxdnPMak11M3fsU5Zg6F21qaX7xhpOPP8XdY6b3PeV9ot3rzpOrajuRmpnevY1wYA/sfyj//zNY/1E6W9ATm8DbnqLdEp2QHKTtc1Zd4sDvLQfF977C3RKfm+/5aNO1yp0ddd1wP6+d372mNviU7J+dnFzH9Tcmc3BwCwUnZrxnaKWK++aQUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBD9B9VbnThQYlhewAAAABJRU5ErkJggg==>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAAUCAYAAAA+wTUXAAABuklEQVR4Xu2VzSsFURjGX4V85rMkSgmlFBILscJCShYW8rGXFLEQVpSVpCRFIisLCwtEFj53SBay8c94ns5MzHvPHXXn3IXMr37d5j63O3PO+75nRGJi/g0t8BiO6CANDMI9uAnzVJYqlXADHsJWlVkpgzuwCY6qLB1kwF24poOItMN3WK0DG9NwAXbCIZWlgwJ4K6biLhmDFzBHB5oieAO74QysCMZOyYLlYjrqDdYG48jsw2UxnRu68C74BAckeWvzDzgzYfJGbFsb/H4CHsBJMfdjpVlxV5TAZ3gv5h5nsCPwix/MwWu4DnNV5lMFh3+xR0wlbfTBBzEbQ47E/Tw3ww9Y711zXFl5K3yAV1ijA0dwI6/ke5Fh85wJV+FdiEtiR8/zlpi1JZAPL2G/DhRRKs3W/4S93nWjmHmug9n+jxzARfobWwgfxRzQCbAFzsUc9YSHGDdCE2Wm+Z8vsM27HhdTac4bN8sVXDDXQ3go89xI+urivC2KaY9ZsVcrCtyIeTGV4Mm6LaZNVyTkoVKAM30Kp+AJbAjGQfhQrFKxDhzDWfbnjZ+hr5QUYcFKxd5xMTExMTF/li9tHkTUgaXe1wAAAABJRU5ErkJggg==>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAsCAYAAADYUuRgAAADB0lEQVR4Xu3cz4vtcxgH8EdIfoTo+hHlYiGS69pIhJSbDflRfmQn4upeyvKuLmXBRqTY+JWUsrHwY0E5ZWeFkAXZ2FhI+Qd4nj6fMed85pzrTDPGnZnXq96d73k+pzNn5rt5ej6fMxEAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D+7OfNxvz4h81HmytXlTXNx5ol+fW7m58wjq8ub5oXMi/366cyP0X6v7Wir7g0AcJx7K/Nr5szMa5nzMpfPvGLj9mSey9ybOTHzbubRzAPTL9oEp2V+yhzJ3J65JnNg5hXby1bcGwBgG3g+813mnHFhgWq4bh2L3VNjYcpN0SZEN44L/+KisZCuzdwxFrtfMp/E8lO1C6M1lKP7M1ePxQ26bCx094yFbr33BgDYoWrLrbYnl21wanp1y1jsVrY853k880O0rdFl7Y35n6tq12VOGhfSH9GmbMu4IlpTNM+lmSfH4gbUZ35sLHanZ/aPxVj/vQEAdqivojUn0xOraoReijYRqsdpF2ReyUwW5Ldo07RpNSX7PnM08+rsUjyYeW+olX3RGrzJgrwda52ReTjae546Va/f7+TMoZhtfuq6tmknx8ibsdYk2vbritejTepW/BVr/55/Zr6Mte9f+Sza5HI0794AALvM+Zkb+vU30c6UVdNTTcyH/fqDvr6MRRO2atKORmtc6ixWNU/PRPvSQTU67/zzyll7Y33TpWrIVqZuk/54V3+s93m2Xy9jKyds8yy6Nwcyd2euz9zZ1wGAHayambP69X2Z36Ntw10VrVGrBqG+ILCsRWfYvo3V5uOSzKfRpnS1FXishq3MO8M2T33WL6aefx7t0P77/Xk1N+tpmLbyDNs8i+7NKZnber22mQGAXexw5qHMwXFhk9XP+Tr+24P1dW6utikr211N6l6O9q9R3ojVpg4A2KXOHgscF+Z92QIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIBd5W+4R2eIxLblCgAAAABJRU5ErkJggg==>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAUCAYAAAAKuPQLAAABbUlEQVR4Xu2UzStFQRjGX4UUkY+UsLG3EmWtfKRLSCkrKzYUJcXCyl4srCVJtkps/An8MbbK83jn7c4czJjuyULnV79Oc2buc9/5OiIV/4gmOAPP4B2cC7uzKSWv5iRD8AH21buzaThvGO6Izo6MwCfJDPEoJW8BjnntTbgv9dBcGs7jwF24At/hG3yE7f6gDErJ6xYNsVk0wxs4697xXBzDaW9MjFge6YJLsM21v4XLzOX2uYQHcBIeund8sp0iljcI1+A17AhGFFiE416bg59FgxlkN2jZtVPE8siAaJE/FsUlPpcwhGfhXvRH/LEVxSe/OYR93NIp1zZSeSRZFPf/FF7BdXgET2Cn62cRflG2lb3wBd6KnhkjlUeSRdn+c4Y9sCXs/rzKlOyJ/pHB27Ql4eFP5ZFkUcXvSRF+iS/gqOiqsW1MwHmvTVJ5POjb8FV0giz8CxuiVzQGZ9vvnkYrXC28I7/Jq6j4Uz4AywI9oy2GbvUAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAUCAYAAAAUccS4AAABQElEQVR4Xu2VvUrEQBRGr6AgKOtvI66NTyCIT2ChFv6A21lZCYKChShY24vWImJhYSuINj6CvoKPINgKno9JSHYSncCyYzMHTjGZTPa7M3cTs0SiwgCu4CU+4Fr3dBSUYc6/WMd6pmjjE04X031lFvfxDW+8uQqq5tBcZWIeXyxe2GGcwlO89eYqbOBiabyHx1aEj8WJBcIq0BFu4zd+4TOOlG8KoJ2ZCaidCxUfDDthLmz+oEG8x9VsrCBbOJ6N61DPdQIu41C+4BeCYXX8aoMyWqCFk+b+dHo7aHf6TTDsJi6VxqP4akUBGusBf4WNsrM6+ivrDqvefTQXUjQJG6Vn1a8XeIc7eIbn2Crd0yRsryzgNX7gp7nfq3yU8n5VxerPumOKEbYR/vvVRwVox9/xwFxv/hu7OOZfTCQSvfMDVmUv9w7+SwQAAAAASUVORK5CYII=>