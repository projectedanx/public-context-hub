# **The Triadic Stabilizer System: Architectures of Agency, Oversight, and Intervention**

## **1\. The Triadic Paradigm in Modern Control Theory**

The exponential increase in the complexity of autonomous systems—ranging from high-frequency fuel injection mechanisms in combustion engines to large language models (LLMs) orchestrating multi-agent workflows—has necessitated a fundamental shift in control architecture. Traditional feedback loops, characterized by rigid setpoints and linear error correction, are increasingly insufficient for systems that must operate in dynamic, partially observable, and stochastic environments. To address these challenges, contemporary research points toward a convergence on a **Triadic Stabilizer System (TSS)**. This high-level architectural paradigm effectively decouples the generation of primary behavior from its surveillance and modulation, establishing a robust framework for **Runtime Assurance (RTA)**.

The TSS is defined by the interaction of three distinct yet interdependent components: the **Generator**, which provides agency and performance optimization; the **Monitor**, which provides epistemic oversight and state estimation; and the **Injector**, which serves as the actuator of the control protocol, capable of introducing either entropy (noise) or order (constraints) based on the system's operational context.1 The intellectual core of this system is the **Decision Rule**, a logical algorithm that arbitrates the "Exploration-Exploitation-Safety" trade-off. This rule determines whether the system requires **controlled noise injection** to facilitate learning, adaptation, and robustness, or **constraint enforcement** to guarantee safety and prevent catastrophic failure.4

This report provides an exhaustive analysis of the TSS, synthesizing data from cyber-physical systems (CPS), reinforcement learning (RL), and generative artificial intelligence (GenAI). By dissecting the functional roles of the triad and rigorous mathematical formulations of the decision rules, we establish a unified theory of stabilized autonomy.

### **1.1 The Necessity of Closed-Loop Runtime Assurance**

Historically, safety-critical systems relied on **Design-Time Verification**, where all possible system states and transitions were mathematically proven safe prior to deployment. However, the integration of "black-box" Generators, such as Deep Neural Networks (DNNs) in autonomous vehicles or complex heuristics in industrial controllers, has rendered exhaustive offline verification intractable.6 The Generator’s behavior in corner cases is often undefined or unpredictable, necessitating a shift to **Runtime Assurance (RTA)**—a paradigm where safety constraints are enforced online, in real-time, during system operation.8

The TSS serves as the architectural embodiment of RTA. It allows the system to benefit from the high performance of advanced, unverified Generators while maintaining the safety guarantees of verified, simpler Monitors and Injectors. This structure is visible in the "Simplex Architecture" used in avionics, where a high-performance controller is wrapped by a safety monitor and a baseline backup controller.3 It is equally present in LLM architectures where "Guardrails" (Monitors) analyze generated text and "System Prompts" (Injectors) modify behavior to prevent toxicity.11

### **1.2 The Exploration-Exploitation-Safety Trade-off**

The central operational tension within the TSS is the management of the **Exploration-Exploitation-Safety Trade-off**.

* **Exploitation** demands that the Generator act optimally based on its current internal model to maximize an objective function (e.g., trajectory tracking accuracy or token probability).  
* **Exploration** requires the system to deviate from known optimal paths to discover new strategies or refine its model of the environment. This is achieved via the **Injector** introducing **controlled noise**.13  
* **Safety** mandates that neither exploitation nor exploration violates fundamental system invariants (e.g., collision avoidance, thermal limits, ethical guidelines). This requires the **Injector** to enforce **constraints**.15

The Decision Rule acts as the switching logic that navigates this trade-off. Advanced implementations utilize metrics of **uncertainty** (both aleatoric and epistemic) and **distance-to-danger** to modulate the Injector's behavior, creating a dynamic system that breathes—expanding into exploration when safe and contracting into constraints when threatened.17

## ---

**2\. Component Analysis: The Generator**

The **Generator** represents the locus of agency within the Triadic Stabilizer System. It is the component responsible for producing the primary output—be it a control signal, a data stream, or a linguistic response. In the context of the TSS, the Generator is often characterized by high capability but low trustworthiness.

### **2.1 Sources of Agency: Deterministic vs. Stochastic**

Generators span a spectrum from rigid determinism to high-entropy stochasticity, influencing how the Monitor and Injector must intervene.

* **Deterministic Control Generators:** In industrial automation and traditional CPS, the Generator is often a Model Predictive Controller (MPC) or a complex PID loop. These systems calculate an optimal control input $u$ based on a predefined cost function $J$. While deterministic, they are susceptible to "semantic faults"—logic errors where the controller creates a valid but unsafe command due to modeling mismatches or sensor noise.10  
* **Stochastic AI Generators:** In modern applications, the Generator is frequently a stochastic policy $\\pi(a|s)$ (in Reinforcement Learning) or a probabilistic foundation model (in GenAI).  
  * **Reinforcement Learning (RL):** The Generator outputs a probability distribution over actions. The inherent stochasticity is a feature, not a bug, used for exploration. However, this randomness introduces "native noise" that the Monitor must distinguish from dangerous instability.18  
  * **Large Language Models (LLMs):** The Generator predicts the next token based on a probability distribution derived from massive training corpora. The "temperature" parameter controls the entropy of this distribution. High temperature leads to high creativity (exploration) but low coherence; low temperature leads to determinism (exploitation).20

### **2.2 The "Unverified Actor" Problem**

A defining characteristic of the Generator in high-assurance architectures is its status as an **unverified** or **untrusted** component. In the canonical **Simplex Architecture**, the Generator corresponds to the "Advanced Controller" (AC). The AC is typically designed for high performance (e.g., aggressive flight maneuvers, fuel-efficient driving) using complex software stacks that are too large to formally verify. Consequently, the AC is assumed to contain residual software faults.3

This assumption of untrustworthiness drives the design of the Monitor. The Monitor cannot rely on the internal state of the Generator (which might be corrupted or hallucinatory); it must observe the Generator's *outputs* and the System's *state* independently. This "black-box" treatment is crucial for security-critical applications, such as identifying malware that uses LLMs to generate code 23 or detecting "ghost obstacles" in autonomous driving perception systems.24

### **2.3 Generative Models as Trajectory Planners**

In the domain of autonomous driving and robotics, the Generator creates spatiotemporal trajectories. Generative models like **Motion Diffusion Models (MDM)** or **Variational Autoencoders (VAEs)** are used to synthesize diverse future paths for agents in complex traffic scenes. These models operate by denoising random latent variables into coherent trajectories.25

* **Noise-Driven Generation:** These Generators intrinsically use noise injection during the inference process. For example, diffusion models start with Gaussian noise and iteratively refine it into a trajectory. The TSS must ensure that this internal noise injection does not result in a trajectory that violates physical safety constraints (e.g., kinematic limits, collision boundaries).25  
* **Imitation Learning:** Generators trained via imitation learning often suffer from "covariate shift"—when the system enters a state not seen during training, the Generator's behavior becomes undefined. This epistemic uncertainty is a primary signal for the Monitor to trigger constraint enforcement.28

## ---

**3\. Component Analysis: The Monitor**

The **Monitor** is the epistemic authority of the TSS. It observes the interactions between the Generator, the System/Environment, and the Injector. It does not act directly on the plant; rather, it judges the safety and validity of the current state and the proposed action. Its primary output is a set of metrics—Safety Margins, Uncertainty Estimates, and Anomaly Scores—that feed the Decision Rule.

### **3.1 State Estimation and Safety Envelopes**

The most fundamental role of the Monitor is determining whether the system is within its **Safety Envelope** or **Admissible Region** ($\\mathcal{O}\_{adm}$).

* **Safety Instrumented Systems (SIS):** In industrial processing, the Monitor (often a Logic Solver or Safety PLC) compares process variables against pre-set thresholds (e.g., High-High Pressure). If a threshold is breached, it signals the need for intervention.30  
* **Barrier Functions:** In advanced control, the Monitor calculates the value of a **Control Barrier Function (CBF)**, $h(x)$. The safety envelope is defined as the superlevel set $\\mathcal{C} \= \\{x \\in \\mathbb{R}^n : h(x) \\ge 0\\}$. The Monitor tracks not just the current value of $h(x)$, but its time derivative $\\dot{h}(x)$. A negative derivative indicates the system is moving towards the unsafe region boundary $\\partial \\mathcal{C}$.15  
* **Recoverable Regions:** In Simplex architectures, the Monitor checks if the system state is within the **Recoverable Region** ($\\mathcal{R}\_{BC}$). This is a subset of the safety envelope from which the backup controller is mathematically guaranteed to recover the system to stability. The Monitor uses reachability analysis—often approximating reachable sets via Taylor expansions or zonotopes—to predict if the Generator's proposed action will push the system out of $\\mathcal{R}\_{BC}$ within the next decision cycle.22

### **3.2 Uncertainty Quantification (UQ): The Measure of Trust**

In systems driven by AI Generators, knowing the state is insufficient; the Monitor must also quantify the **uncertainty** of the Generator's predictions.

* **Aleatoric vs. Epistemic Uncertainty:**  
  * **Aleatoric Uncertainty** arises from inherent stochasticity in the environment (e.g., sensor noise, wind gusts).  
  * Epistemic Uncertainty arises from the model's lack of knowledge (e.g., OOD scenarios).  
    High epistemic uncertainty suggests the Generator is operating in a regime where its training is inapplicable, necessitating a switch to safety constraints.33  
* **Quantification Techniques:**  
  * **Ensembles:** Running multiple instances of the Generator (or a separate ensemble of critics) and measuring the variance of their predictions. High variance implies high uncertainty.34  
  * **Monte Carlo Dropout:** Activating dropout layers during inference to generate a distribution of outputs from a single neural network, providing a computationally efficient uncertainty estimate.28  
  * **Predictive Entropy:** In LLMs and Decision Transformers, the entropy of the next-token distribution serves as a proxy for uncertainty. A "flattened" distribution (high entropy) indicates the model is unsure of the correct path.12

### **3.3 Anomaly and Fault Detection**

In cybersecurity and fault tolerance, the Monitor functions as an **Intrusion Detection System (IDS)** or a **Watchdog**.

* **Side-Channel Monitoring:** In the "Secure System Simplex" (S3A) architecture, the Monitor observes hardware side-channels, such as execution time and power consumption, to detect malware injection in real-time controllers. Deviations as small as 0.6 $\\mu$s can trigger a safety intervention.36  
* **I/O Pattern Recognition:** For detecting keyloggers or malware, the Monitor analyzes Input/Output streams. By comparing the distribution of injected inputs (from a test injector) to the monitored outputs, the system can detect anomalies indicative of malicious interception.37  
* **Threshold-Based Detection:** In network security, monitors track the rate of requests (e.g., HTTP requests per second). If the cumulative behavior exceeds a defined threshold within a time window, the Monitor flags a "Slow Attack" or "Scraping" event.38

## ---

**4\. Component Analysis: The Injector**

The **Injector** is the actuator of the assurance layer. While the Generator proposes, the Injector disposes. Based on the output of the Decision Rule, the Injector modifies the system's input, parameters, or environment. The Injector operates in two distinct modes: **Noise Injection** (for exploration/robustness) and **Constraint Enforcement** (for safety).

### **4.1 Mode A: Controlled Noise Injection**

Noise is often perceived as detrimental, but in the TSS, the Injector introduces it strategically to enhance system performance and learning.

* **Exploration and Active Learning:** In "Dual Control" theory, the Injector adds excitation signals to the control input to probe the system dynamics. If a controller strictly exploits known dynamics, it may fail to identify changes in the environment. The Injector adds noise $\\eta$ when the Monitor indicates that the "Information Gain" from exploration is high and the "Safety Risk" is low.5  
* **Dithering:** In mechanical systems like fuel injectors and hydraulic valves, the Injector superimposes a high-frequency, low-amplitude signal (dither) onto the control command. This noise prevents "stiction" (static friction) and hysteresis, effectively linearizing the actuator's response and ensuring smooth operation.39  
* **Adversarial Training and Robustness:**  
  * **Fault Injection:** In testing environments, the Injector (Fault Injector) deliberately corrupts memory, flips bits, or delays packets. This "noise" forces the system to exercise its error-handling pathways, verifying the Monitor's detection capabilities.40  
  * **Differential Privacy:** In data systems, the Injector adds Laplacian or Gaussian noise to query results. This noise "masks" the contribution of individual data points, enforcing privacy constraints while allowing aggregate analysis.43  
* **Generative Diversity:** In LLMs, increasing the "temperature" parameter is a form of noise injection. The Injector flattens the probability distribution, allowing the model to sample less probable tokens. This promotes creativity and prevents repetitive loops.21

### **4.2 Mode B: Constraint Enforcement**

When the Monitor detects a violation of the safety envelope or high uncertainty, the Injector switches to enforcing constraints.

* **Shielding:** In Safe RL and autonomous systems, a **Shield** acts as a filter Injector. It receives the action $u\_{gen}$ from the Generator. If the Monitor deems $u\_{gen}$ unsafe, the Injector replaces it with a safe action $u\_{safe}$ derived from the Baseline Controller or a valid policy subset. This is a "hard" intervention.44  
* **Prompt Injection and RAG:** In LLM agents, the Injector enforces constraints by modifying the input context.  
  * **Retrieval Augmented Generation (RAG):** The Injector retrieves factual documents and "injects" them into the prompt, constraining the LLM's hallucination by grounding it in external data.20  
  * **System Prompts:** The Injector prepends instructions (e.g., "You are a helpful assistant," "Do not generate toxic content") that act as soft constraints on the Generator's output space.20  
* **Safety Filtering (CBF-QP):** The Injector solves a quadratic program to find the control input $u^\*$ closest to $u\_{gen}$ that satisfies the safety constraint $L\_f h \+ L\_g h u \\ge \-\\alpha(h)$. This acts as a "soft" clamp, minimally deviating the system to maintain invariance.15  
* **Logic Locking:** In hardware security, constraints are injected into the circuit design itself. Logic gates are added that function as "locks," ensuring the circuit only operates correctly when a specific "key" (input pattern) is provided, effectively constraining unauthorized usage.46

## ---

**5\. The Decision Rule: Logic for Switching**

The core challenge of the TSS is defining the **Decision Rule** that governs the Injector. This rule must robustly determine when to prioritize exploration (Noise) and when to prioritize safety (Constraints). The synthesis of research suggests a **Uncertainty-Weighted Safety Filter** logic.

### **5.1 The Unified Switching Logic**

We can formalize the generalized decision rule for a TSS as follows.

Let $u\_{gen}(t)$ be the Generator's proposed action at time $t$.  
Let $u\_{safe}(t)$ be a verified safe fallback action (e.g., from a Baseline Controller).  
Let $h(x)$ be a Control Barrier Function measuring the safety margin (where $h(x) \> 0$ is safe).  
Let $\\mathcal{U}(x)$ be an Uncertainty Metric (e.g., variance of the state estimate or predictive entropy).  
Let $\\mathcal{I}(x)$ be an Information Gain metric (value of exploration).  
The final injected action $u\_{final}(t)$ is determined by a mixing parameter $\\lambda \\in $ and a noise term $\\eta$:

$$u\_{final}(t) \= (1 \- \\lambda) \\cdot \\text{Clip}\_{\\mathcal{C}}(u\_{gen}(t) \+ \\eta) \+ \\lambda \\cdot u\_{safe}(t)$$  
where $\\text{Clip}\_{\\mathcal{C}}$ ensures the action remains within actuator limits. The switching parameter $\\lambda$ and noise $\\eta$ are dynamic functions of the Monitor's metrics.

### **5.2 Decision Rule Mechanics**

The decision rule $D(h, \\mathcal{U}, \\mathcal{I})$ determines the operational mode:

#### **5.2.1 The Safety Condition (Constraint Trigger)**

The primary trigger for constraint enforcement is the **Safety Margin** $h(x)$. If the system approaches the boundary of the recoverable set, safety overrides all other objectives.

* **Logic:** If $h(x) \\le \\delta\_{critical}$, then $\\lambda \\to 1$. The Injector enforces $u\_{safe}$.  
* **Simplex Switching:** In the Simplex architecture, this is a binary switch. If the state enters the "Simplex Boundary" (derived via Linear Matrix Inequalities or Lyapunov functions), the decision module hard-switches to the safety controller to prevent a crash.3  
* **Look-Ahead:** The rule must account for system inertia. It checks not just $h(x\_t)$ but the predicted future state $h(x\_{t+1})$. If the Generator's action *will* cause a violation, the Injector intervenes *now*.6

#### **5.2.2 The Uncertainty Condition (Pessimism Trigger)**

High uncertainty acts as a proxy for safety risk. Even if the nominal state estimate appears safe ($h(\\hat{x}) \> 0$), high uncertainty $\\mathcal{U}(x)$ implies the *true* state might be unsafe.

* **Logic:** If $\\mathcal{U}(x) \> \\epsilon\_{uncertainty}$, then $\\lambda \\to 1$ (or a value scaling with risk).  
* **Uncertainty-Weighted Decision Transformers:** Research shows that weighting the loss function by predictive entropy forces the model to be conservative in uncertain scenarios. In runtime, this translates to: **"If you don't know, don't explore."** The decision rule suppresses noise injection and enforces nominal constraints when epistemic uncertainty is high.17  
* **Probabilistic Shielding:** A probabilistic shield computes $P(\\text{safe}|a)$. The decision rule rejects any action where $P(\\text{safe}|a) \< \\text{Threshold}$. This is effectively an uncertainty-weighted constraint.18

#### **5.2.3 The Exploration Condition (Noise Trigger)**

Noise injection is permitted only when the system is verified to be safe *and* there is value in exploration.

* **Logic:** If $h(x) \> \\delta\_{safe}$ **AND** $\\mathcal{U}(x) \< \\epsilon\_{uncertainty}$ **AND** $\\mathcal{I}(x) \> \\text{Threshold}$, then Inject Noise $\\eta \\sim \\mathcal{N}(0, \\sigma\_{exp})$.  
* **Safe Exploration:** Algorithms like **SafeOpt** and **StageOpt** explicitly classify the domain into "Safe Sets" and "Potential Expanders." The decision rule only allows the injection of exploration noise if the resulting state is guaranteed (with high probability) to remain within the safe set. This ensures "Safe Exploration"—learning without crashing.5  
* **Information-Driven Noise:** The magnitude of the injected noise $\\eta$ should be proportional to the potential Information Gain. In "Active Learning," the system targets areas of the state space that maximize the reduction of uncertainty, but only if they satisfy the safety constraints.13

### **5.3 Mathematical Formulation of the Switch**

To avoid "chattering" (rapid, unstable switching between modes), the decision rule often employs a smooth transition function rather than a binary switch.

$$\\lambda(x) \= \\begin{cases} 0 & \\text{if } h(x) \> \\delta\_{safe} \\text{ AND } \\mathcal{U}(x) \< \\epsilon \\\\ \\frac{\\delta\_{safe} \- h(x)}{\\delta\_{safe}} & \\text{if } 0 \\le h(x) \\le \\delta\_{safe} \\text{ (Blending Region)} \\\\ 1 & \\text{if } h(x) \< 0 \\text{ OR } \\mathcal{U}(x) \\ge \\epsilon \\end{cases}$$  
This "Blending Region" allows for a graceful handover of control from the Generator (Agent) to the Injector (Safety Constraints), a technique validated in **Neural Simplex** and **Fuzzy Control** architectures.32

## ---

**6\. Domain-Specific Implementations**

The TSS architecture is universal, but its implementation details vary significantly across domains.

### **6.1 Cyber-Physical Systems (CPS) & Autonomous Vehicles**

* **Generator:** Deep Neural Networks (DNNs) for perception and trajectory planning.  
* **Monitor:** **Perception Simplex ($P\\Sigma$)**. This architecture uses a reliable, non-ML obstacle detector (e.g., geometric LiDAR clustering) alongside the DNN. The Monitor compares the two. If the DNN fails to detect an obstacle found by the reliable detector, the Monitor flags a "Safety Violation".24  
* **Injector:** **Emergency Braking / Control Filter**.  
* **Decision Rule:** The **Forward Switching Condition (FSC)** checks if the vehicle is entering a state from which the baseline controller cannot prevent a collision. If FSC \== True, the Injector overrides the DNN and applies maximum braking.3  
  * *Table 1: Simplex Switching Logic*

| State Condition | AC Action | BC Capability | Decision |
| :---- | :---- | :---- | :---- |
| Inside Recoverable | Safe | Capable | Allow AC (Generator) |
| Inside Recoverable | Unsafe | Capable | Switch to BC (Injector) |
| Boundary | Any | Capable | Switch to BC (Injector) |
| Outside Recoverable | Any | Incapable | Emergency State (Fail) |

### **6.2 Large Language Model (LLM) Agents**

* **Generator:** The LLM (e.g., GPT-4) generating tokens.  
* **Monitor:** **Guardrails / Hallucination Detectors**. These can be separate smaller models (BERT-based classifiers) or deterministic rule sets (regex for PII). They measure toxicity, relevance, and factual consistency.  
* **Injector:** **System Prompts / RAG**.  
* **Decision Rule:** **Uncertainty-Weighted Generation**.  
  * *Exploration:* If the query is creative ("Write a poem") and Toxicity Score is low, the Injector sets Temperature \= 0.9 (Inject Noise).  
  * *Safety:* If the query is sensitive ("Medical advice") or the Monitor detects "Jailbreak" patterns, the Injector sets Temperature \= 0 (Constraint) and injects a restrictive System Prompt ("You are a medical assistant, do not diagnose...").20  
  * *Correction:* If the Monitor detects hallucination (via RAG consistency check), the Injector forces a regeneration with "Grounding Constraints" added to the context.11

### **6.3 Industrial Control & Power Systems**

* **Generator:** Adaptive Controllers / Reinforcement Learning agents optimizing for efficiency (e.g., Volt-Var control).  
* **Monitor:** **State Estimators / Watchdogs**. These track grid frequency, voltage stability, and physical limits (e.g., transformer temperature).  
* **Injector:** **Grid Stabilizers / Load Shedders**.  
* **Decision Rule:** **Runtime Assurance (RTA)**.  
  * *Nominal:* The RL agent manages voltage to minimize power loss.  
  * *Constraint:* If frequency deviation $\\Delta f \> 0.5$ Hz (Safety Threshold), the Decision Rule switches to a deterministic Droop Controller (Injector) to stabilize the grid immediately.52  
  * *Noise:* During stable periods, the Injector might introduce small voltage perturbations (Active Learning) to estimate the grid's impedance parameters.14

### **6.4 Mechanical Systems: Fuel Injection**

* **Generator:** The Engine Control Unit (ECU) calculating optimal fuel pulse width based on load/RPM.  
* **Monitor:** **Piezoelectric Sensors**. These measure the vibration/acoustic signature of the injector needle movement. The Monitor analyzes statistical parameters (e.g., Kurtosis, Skewness of the signal) to detect "needle lift" and "injection delay".54  
* **Injector:** The physical Solenoid Valve.  
* **Decision Rule:** **Dithering & Pulse Modulation**.  
  * *Noise Injection:* The ECU injects a high-frequency "dither" signal (current noise) into the solenoid. This creates micro-movements that break static friction (stiction), ensuring the valve responds instantly to control commands. This is "Controlled Noise for Performance".39  
  * *Constraint:* If the Monitor detects "Injection Delay" \> Threshold (indicating clogging or failure), the Decision Rule forces a "Limp Mode," constraining RPM and fuel flow to prevent engine damage.56

## ---

**7\. Synthesis and Future Directions**

The TSS architecture represents a critical evolution in systems engineering, moving from static safety buffers to dynamic, active assurance.

### **7.1 The "Monitor" as the Weak Link**

The robustness of the entire TSS relies on the **Monitor**. If the Monitor fails to detect a hazard (False Negative), the Decision Rule will not trigger the Injector, leading to failure.

* *Challenge:* Creating Monitors that are robust to "Adversarial Examples" in AI. An adversary might craft inputs that fool the Safety Shield (Monitor) into perceiving a dangerous state as safe.57  
* *Solution:* **Meta-Monitoring**. Using "Monitors for Monitors"—often via consensus mechanisms in multi-agent systems or diversity in sensor modalities (e.g., Camera \+ LiDAR \+ Radar) to cross-validate the state estimate.24

### **7.2 The "Inverse" Prompting Paradigm**

In GenAI, the concept of **Inverse Prompt Engineering (IPE)** is emerging as a powerful constraint mechanism. Instead of building general-purpose guardrails (Deny Lists), IPE derives safety constraints *directly* from the task-specific prompt engineering data. It creates an "Allow List" of behaviors, effectively constraining the Generator to *only* the capabilities required for the specific task. This represents a highly efficient form of Constraint Injection derived from the Generator's own training context.51

### **7.3 Active Learning and Safety**

The integration of **Active Learning** into the TSS allows the system to expand its own safety envelope. By strategically injecting noise in the boundary regions of the safe set (where uncertainty is high but manageable), the system "learns" that these regions are actually safe, thereby expanding the **Recoverable Region** $\\mathcal{R}\_{BC}$. This turns the Decision Rule from a static gatekeeper into a dynamic agent of growth.5

## **8\. Conclusion**

The **Triadic Stabilizer System**—comprising the Generator, Monitor, and Injector—provides the necessary architectural scaffolding to deploy autonomous systems in the real world. It acknowledges the fundamental reality that intelligence (the Generator) is prone to error and requires independent supervision (the Monitor) and correction (the Injector).

The crucial innovation is the **Uncertainty-Weighted Decision Rule**. By treating uncertainty not as noise to be filtered out, but as a signal to be heeded, the TSS dynamically shifts between exploration and safety. Whether managing the micro-second pulses of a fuel injector, the trajectory of a drone in a crowded sky, or the creative output of a massive language model, the TSS ensures that autonomy remains bounded by the physics of safety and the logic of survival.

### **Table 2: Comparative Summary of Triadic Components**

| Feature | Cyber-Physical Systems | Generative AI (LLMs) | Industrial Control | Fuel Injection |
| :---- | :---- | :---- | :---- | :---- |
| **Generator** | Neural Policy / Planner | Foundation Model | PID / MPC | ECU Pulse Logic |
| **Monitor** | Safety Shield / Perception $\\Sigma$ | Critic / Guardrail | Watchdog / Logic Solver | Piezo Sensor |
| **Injector** | Safety Controller / Filter | System Prompt / Filter | Safety Interlock / PLC | Solenoid / Dither |
| **Noise** | Excitation / Perturbation | Temperature / Sampling | Test Signals | Dithering Current |
| **Constraints** | CBF / Actuator Limits | RAG / Grammar / Refusal | Emergency Stop | Limp Mode / Governor |
| **Switch Logic** | Barrier Function $h(x)$ | Uncertainty / Toxicity Score | SIL Thresholds | Signal Kurtosis |

The future of autonomous systems lies not in making the Generator perfect, but in making the Triadic System resilient. Through the rigorous application of this architecture, we can bridge the gap between the chaotic potential of AI and the stringent requirements of safety-critical engineering.

#### **Works cited**

1. EDM MACHINES FOR: \- AAEDM Corp, accessed on December 14, 2025, [https://www.aaedmcorp.com/images/AAEDM\_Catalog.pdf](https://www.aaedmcorp.com/images/AAEDM_Catalog.pdf)  
2. Monitoring Progress and Failure in Autonomous Robot Navigation: A Case Study | Request PDF \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/395629546\_Monitoring\_Progress\_and\_Failure\_in\_Autonomous\_Robot\_Navigation\_A\_Case\_Study](https://www.researchgate.net/publication/395629546_Monitoring_Progress_and_Failure_in_Autonomous_Robot_Navigation_A_Case_Study)  
3. Real-Time Reachability for Verified Simplex Design \- Stanley Bak, accessed on December 14, 2025, [https://stanleybak.com/papers/bak2014rtss.pdf](https://stanleybak.com/papers/bak2014rtss.pdf)  
4. Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning \- Annual Reviews, accessed on December 14, 2025, [https://www.annualreviews.org/doi/pdf/10.1146/annurev-control-042920-020211](https://www.annualreviews.org/doi/pdf/10.1146/annurev-control-042920-020211)  
5. Active Learning with Safety Constraints \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/361479733\_Active\_Learning\_with\_Safety\_Constraints](https://www.researchgate.net/publication/361479733_Active_Learning_with_Safety_Constraints)  
6. A Distributed Simplex Architecture for Multi-Agent Systems, accessed on December 14, 2025, [https://par.nsf.gov/servlets/purl/10413107](https://par.nsf.gov/servlets/purl/10413107)  
7. Neural Simplex Architecture \- Nicola Paoletti, accessed on December 14, 2025, [https://nicolapaoletti.com/assets/papers/NSA\_NFM2020.pdf](https://nicolapaoletti.com/assets/papers/NSA_NFM2020.pdf)  
8. Ablation Study of How Run Time Assurance Impacts the Training and Performance of Reinforcement Learning Agents \- Taylor Johnson, accessed on December 14, 2025, [http://taylortjohnson.com/research/hamilton2023smcit.pdf](http://taylortjohnson.com/research/hamilton2023smcit.pdf)  
9. Modular and Safe Event-Driven Programming \- Berkeley EECS, accessed on December 14, 2025, [https://www2.eecs.berkeley.edu/Pubs/TechRpts/2020/EECS-2020-3.pdf](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2020/EECS-2020-3.pdf)  
10. The Simplex Architecture for Safe On-Line Control System Upgrades, accessed on December 14, 2025, [http://congres.cran.univ-lorraine.fr/1998/ACC\_98/pdffiles/papers/Vol6/fp02\_5.pdf](http://congres.cran.univ-lorraine.fr/1998/ACC_98/pdffiles/papers/Vol6/fp02_5.pdf)  
11. Building a Foundational Guardrail for General Agentic Systems via Synthetic Data \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2510.09781v1](https://arxiv.org/html/2510.09781v1)  
12. Structured Uncertainty guided Clarification for LLM Agents \- ChatPaper, accessed on December 14, 2025, [https://chatpaper.com/paper/208941](https://chatpaper.com/paper/208941)  
13. Transductive Active Learning: Theory and Applications \- NIPS papers, accessed on December 14, 2025, [https://proceedings.neurips.cc/paper\_files/paper/2024/file/e17fe6fe9990fffb637b42c98c005515-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2024/file/e17fe6fe9990fffb637b42c98c005515-Paper-Conference.pdf)  
14. Dual MPC for Active Learning of Nonparametric Uncertainties \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2511.08542v2](https://arxiv.org/html/2511.08542v2)  
15. Explicit Control Barrier Function-based Safety Filters and their Resource-Aware Computation \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2512.10118v1](https://arxiv.org/html/2512.10118v1)  
16. Control Barrier Functions \- a simple case study | Tech Notes, accessed on December 14, 2025, [https://dev10110.github.io/tech-notes/research/cbfs-simple.html](https://dev10110.github.io/tech-notes/research/cbfs-simple.html)  
17. An Uncertainty-Weighted Decision Transformer for Navigation in ..., accessed on December 14, 2025, [https://www.researchgate.net/publication/395541890\_An\_Uncertainty-Weighted\_Decision\_Transformer\_for\_Navigation\_in\_Dense\_Complex\_Driving\_Scenarios](https://www.researchgate.net/publication/395541890_An_Uncertainty-Weighted_Decision_Transformer_for_Navigation_in_Dense_Complex_Driving_Scenarios)  
18. Safe Reinforcement Learning via Probabilistic Logic Shields \- Leuven.AI, accessed on December 14, 2025, [https://ai.kuleuven.be/stories/post/2023-12-18-saferl/](https://ai.kuleuven.be/stories/post/2023-12-18-saferl/)  
19. Balance Reward and Safety Optimization for Safe Reinforcement Learning: A Perspective of Gradient Manipulation \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2405.01677v1](https://arxiv.org/html/2405.01677v1)  
20. LLM Engineering (Part II) \- Medium, accessed on December 14, 2025, [https://medium.com/@yugalnandurkar5/llm-engineering-part-ii-4404a7985776](https://medium.com/@yugalnandurkar5/llm-engineering-part-ii-4404a7985776)  
21. ChatGPT as a Tool for Biostatisticians: A Tutorial on Applications, Opportunities, and Limitations \- PMC \- PubMed Central, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12548020/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12548020/)  
22. A Simplex Architecture for Hybrid Systems using Barrier Certificates? \- Stony Brook Computer Science, accessed on December 14, 2025, [https://www3.cs.stonybrook.edu/\~stoller/papers/safecomp2017.pdf](https://www3.cs.stonybrook.edu/~stoller/papers/safecomp2017.pdf)  
23. Prompts as Code & Embedded Keys | The Hunt for LLM-Enabled Malware | SentinelOne, accessed on December 14, 2025, [https://www.sentinelone.com/labs/prompts-as-code-embedded-keys-the-hunt-for-llm-enabled-malware/](https://www.sentinelone.com/labs/prompts-as-code-embedded-keys-the-hunt-for-llm-enabled-malware/)  
24. Perception Simplex: Verifiable Collision Avoidance in Autonomous Vehicles Amidst Obstacle Detection Faults \- Ayoosh Bansal, accessed on December 14, 2025, [https://ayooshbansal.com/assets/pdf/Perception\_Simplex.pdf](https://ayooshbansal.com/assets/pdf/Perception_Simplex.pdf)  
25. MDG: Masked Denoising Generation for Multi-Agent Behavior Modeling in Traffic Environments \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2511.17496v1](https://arxiv.org/html/2511.17496v1)  
26. Generative AI for Autonomous Driving: Frontiers and Opportunities \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2505.08854v1](https://arxiv.org/html/2505.08854v1)  
27. Noise Aggregation Analysis Driven by Small-Noise Injection: Efficient Membership Inference for Diffusion Models \* Corresponding Author \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2510.21783v1](https://arxiv.org/html/2510.21783v1)  
28. Safe Reinforcement Learning with Model Uncertainty Estimates \- DSpace@MIT, accessed on December 14, 2025, [https://dspace.mit.edu/bitstream/handle/1721.1/125488/1810.08700.pdf?sequence=2\&isAllowed=y](https://dspace.mit.edu/bitstream/handle/1721.1/125488/1810.08700.pdf?sequence=2&isAllowed=y)  
29. Learning Safety Constraints from Demonstrations with Unknown Rewards, accessed on December 14, 2025, [https://proceedings.mlr.press/v238/lindner24a/lindner24a.pdf](https://proceedings.mlr.press/v238/lindner24a/lindner24a.pdf)  
30. SIS Logic Solvers: More Choices Needed \- Automation.com, accessed on December 14, 2025, [https://www.automation.com/article/sis-logic-solvers-more-choices-needed](https://www.automation.com/article/sis-logic-solvers-more-choices-needed)  
31. Safety Instrumented Systems Vs Process Control Systems \- CrossCo, accessed on December 14, 2025, [https://www.crossco.com/blog/safety-instrumented-systems-vs-process-control-systems/](https://www.crossco.com/blog/safety-instrumented-systems-vs-process-control-systems/)  
32. A Barrier Certificate-based Simplex Architecture with Application to Microgrids \- Stony Brook CS, accessed on December 14, 2025, [https://www3.cs.stonybrook.edu/\~stoller/papers/rv2022.pdf](https://www3.cs.stonybrook.edu/~stoller/papers/rv2022.pdf)  
33. From Aleatoric to Epistemic: Exploring Uncertainty Quantification Techniques in Artificial Intelligence \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2501.03282v1](https://arxiv.org/html/2501.03282v1)  
34. Evidential Deep Learning: Enhancing Predictive Uncertainty Estimation for Earth System Science Applications \- AMS Journals, accessed on December 14, 2025, [https://journals.ametsoc.org/view/journals/aies/aop/AIES-D-23-0093.1/AIES-D-23-0093.1.pdf](https://journals.ametsoc.org/view/journals/aies/aop/AIES-D-23-0093.1/AIES-D-23-0093.1.pdf)  
35. Verification-Guided Falsification for Safe RL via Explainable Abstraction and Risk-Aware Exploration \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2506.03469v1](https://arxiv.org/html/2506.03469v1)  
36. S3A: Secure System Simplex Architecture for Enhanced Security of Cyber-Physical Systems, accessed on December 14, 2025, [https://www.researchgate.net/publication/221666890\_S3A\_Secure\_System\_Simplex\_Architecture\_for\_Enhanced\_Security\_ofCyber-Physical\_Systems](https://www.researchgate.net/publication/221666890_S3A_Secure_System_Simplex_Architecture_for_Enhanced_Security_ofCyber-Physical_Systems)  
37. Bait your Hook: a Novel Detection Technique for Keyloggers \- vusec, accessed on December 14, 2025, [https://download.vusec.net/papers/raid-2010.pdf](https://download.vusec.net/papers/raid-2010.pdf)  
38. Configuring threshold based detection | FortiWeb 8.0.2 \- Fortinet Document Library, accessed on December 14, 2025, [https://docs.fortinet.com/document/fortiweb/8.0.2/administration-guide/589220/configuring-threshold-based-detection](https://docs.fortinet.com/document/fortiweb/8.0.2/administration-guide/589220/configuring-threshold-based-detection)  
39. Investigation of Active Control of Combustion Instabilities in Liquid Propellant Rocket Motors \- DTIC, accessed on December 14, 2025, [https://apps.dtic.mil/sti/tr/pdf/ADA368283.pdf](https://apps.dtic.mil/sti/tr/pdf/ADA368283.pdf)  
40. Fault Injection Techniques and Tools, accessed on December 14, 2025, [https://course.ece.cmu.edu/\~ece749/docs/faultInjectionSurvey.pdf](https://course.ece.cmu.edu/~ece749/docs/faultInjectionSurvey.pdf)  
41. ML-Based Fault Injection for Autonomous Vehicles \- Subho Sankar Banerjee, accessed on December 14, 2025, [https://ssbaner2.cs.illinois.edu/publications/dsn2019/Paper.pdf](https://ssbaner2.cs.illinois.edu/publications/dsn2019/Paper.pdf)  
42. DA-FIS: A high-speed dynamic adaptive fault injection server framework for reliable FPGA-based embedded systems \- PeerJ, accessed on December 14, 2025, [https://peerj.com/articles/cs-2996.pdf](https://peerj.com/articles/cs-2996.pdf)  
43. Noise injection | ADH for Marketers \- Google for Developers, accessed on December 14, 2025, [https://developers.google.com/ads-data-hub/marketers/guides/noise-injection](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection)  
44. Shields for Safe Reinforcement Learning \- Communications of the ACM, accessed on December 14, 2025, [https://cacm.acm.org/research/shields-for-safe-reinforcement-learning/](https://cacm.acm.org/research/shields-for-safe-reinforcement-learning/)  
45. Safe control under input limits with neural control barrier functions \- Proceedings of Machine Learning Research, accessed on December 14, 2025, [https://proceedings.mlr.press/v205/liu23e/liu23e.pdf](https://proceedings.mlr.press/v205/liu23e/liu23e.pdf)  
46. TLGLock: A New Approach in Logic Locking Using Key-Driven Charge Recycling in Threshold Logic Gates \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2508.17809](https://arxiv.org/html/2508.17809)  
47. 1 Real-Time Reachability for Verified Simplex Design \- Taylor Johnson, accessed on December 14, 2025, [http://taylortjohnson.com/research/johnson2016tecs.pdf](http://taylortjohnson.com/research/johnson2016tecs.pdf)  
48. | Safe Reinforcement Learning via Probabilistic Logic Shield \- Wen-Chi Yang, accessed on December 14, 2025, [https://wenchiyang.github.io/projects/2\_Shield/](https://wenchiyang.github.io/projects/2_Shield/)  
49. Bayesian optimization with safety constraints: safe and automatic parameter tuning in robotics \- PMC \- NIH, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10485113/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10485113/)  
50. Blending Controllers via Multi-Objective Bandits, accessed on December 14, 2025, [https://par.nsf.gov/servlets/purl/10348056](https://par.nsf.gov/servlets/purl/10348056)  
51. INVERSE PROMPT ENGINEERING FOR TASK-SPECIFIC LLM SAFETY \- OpenReview, accessed on December 14, 2025, [https://openreview.net/pdf?id=3MDmM0rMPQ](https://openreview.net/pdf?id=3MDmM0rMPQ)  
52. A Review of Safe Reinforcement Learning Methods for Modern Power Systems \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2407.00304v2](https://arxiv.org/html/2407.00304v2)  
53. Process Control & Safety Systems Logics Implementing Cycle \- Inst Tools, accessed on December 14, 2025, [https://instrumentationtools.com/process-control-safety-systems-logics/](https://instrumentationtools.com/process-control-safety-systems-logics/)  
54. Monitoring System of Fuel Injector Using Piezoelectric Sensors Mohd Anas Mohd Sabri , Mohd Zaki Nuawi , Mohd Faizal Bin Mat Tah \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/profile/Abdul-Rahim-Bahari/publication/278093637\_Monitoring\_System\_of\_Fuel\_Injector\_Using\_Piezoelectric\_Sensors/links/60e9aaf70fbf460db8f990b2/Monitoring-System-of-Fuel-Injector-Using-Piezoelectric-Sensors.pdf](https://www.researchgate.net/profile/Abdul-Rahim-Bahari/publication/278093637_Monitoring_System_of_Fuel_Injector_Using_Piezoelectric_Sensors/links/60e9aaf70fbf460db8f990b2/Monitoring-System-of-Fuel-Injector-Using-Piezoelectric-Sensors.pdf)  
55. Using the Injection System as a Sensor to Analyze the State of the Electronic Automotive System \- MDPI, accessed on December 14, 2025, [https://www.mdpi.com/1424-8220/25/18/5814](https://www.mdpi.com/1424-8220/25/18/5814)  
56. Understanding the HEUI Fuel System Without Losing Your Mind \- G2 Diesel Products, accessed on December 14, 2025, [https://www.g2dieselproducts.com/blog-resources/hydraulic-electronic-unit-injector-heui-fuel-system](https://www.g2dieselproducts.com/blog-resources/hydraulic-electronic-unit-injector-heui-fuel-system)  
57. Safe Model-Based Reinforcement Learning With an Uncertainty-Aware Reachability Certificate | Request PDF \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/375989438\_Safe\_Model-Based\_Reinforcement\_Learning\_With\_an\_Uncertainty-Aware\_Reachability\_Certificate](https://www.researchgate.net/publication/375989438_Safe_Model-Based_Reinforcement_Learning_With_an_Uncertainty-Aware_Reachability_Certificate)  
58. (PDF) STRATUS: A Multi-agent System for Autonomous Reliability Engineering of Modern Clouds \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/392371187\_STRATUS\_A\_Multi-agent\_System\_for\_Autonomous\_Reliability\_Engineering\_of\_Modern\_Clouds](https://www.researchgate.net/publication/392371187_STRATUS_A_Multi-agent_System_for_Autonomous_Reliability_Engineering_of_Modern_Clouds)