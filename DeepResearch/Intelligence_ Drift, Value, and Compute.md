# **The Entropic Drift: A Unified Computational Physics of Thought Selection in Biological and Artificial Intelligence**

## **1\. Introduction: The Selection Problem**

The history of intelligence is the history of a single, persistent problem: selection. Whether examining the frenetic activity of a cortical column in a primate brain or the massively parallel operations of a Transformer-based Large Language Model (LLM), the fundamental challenge remains identical. From a near-infinite combinatorial space of potential neural states or semantic tokens, the system must isolate and amplify a specific trajectory—a "thought"—that maximizes adaptive value while suppressing the cacophony of irrelevant or maladaptive alternatives. This classification of thoughts into 'good' (high-value, veridical, adaptive) and 'bad' (low-value, hallucinatory, entropic) is not merely a psychological preference but a physical operation constrained by time, energy, and noise.

For decades, the disciplines studying this phenomenon have operated in isolation. Cognitive psychology modeled it as a sequential sampling process, the Drift Diffusion Model (DDM). Neuroscience approached it as a metabolic trade-off involving inhibitory control and synaptic gain. Thermodynamics framed it as a struggle against entropy, invoking the metaphor of Maxwell’s Demon. Most recently, the field of Artificial Intelligence has encountered the same constraints, formalized as the trade-offs involved in "inference-time compute" and Process Reward Models (PRMs).

This report posits that these are not separate phenomena but distinct instantiations of a universal computational mechanism: **Drift**. We argue that 'drift'—the stochastic accumulation of evidence toward a decision boundary—is the master equation of thought. It explains how biological agents convert metabolic energy (ATP) into precision, and how artificial agents convert computational energy (FLOPs) into reasoning. By integrating the mathematics of sequential sampling with the physics of non-equilibrium thermodynamics and the architecture of modern reasoning models, we reveal a unified theory of cognitive selection. In this view, a "good" thought is a low-entropy trajectory sustained by high-precision drift, while a "bad" thought is a diffusion-dominated path that fails to overcome the energetic cost of selection.

## **2\. The Kinematics of Cognition: Drift Diffusion as the Universal Algorithm**

To understand how a system classifies a thought as 'good', we must first strip away the qualitative content of the thought and examine its kinematic properties. How does a thought move through the state space of a decision-making system? The canonical answer, robust across decades of psychophysics and now resurgent in AI interpretability, is the Drift Diffusion Model (DDM).

### **2.1 The Mathematical Primacy of Sequential Sampling**

The DDM conceptualizes the selection of a thought not as an instantaneous event, but as a temporal process of integration. It assumes that the decision-maker samples noisy evidence from the environment (or internal memory) and accumulates this evidence over time until a threshold is reached. This process is mathematically defined by a Wiener process, a continuous-time stochastic process with stationary independent increments.1

The fundamental stochastic differential equation governing this evolution is:

$$dX\_t \= v \\cdot dt \+ \\sigma \\cdot dW\_t$$  
Here, $X\_t$ represents the decision variable—the accumulated evidence for a specific thought—at time $t$. The term $v$ (often denoted as $\\delta$) is the **drift rate**, representing the systematic component of the process, or the "quality" of the evidence. The term $\\sigma$ represents the diffusion coefficient, scaling the Wiener noise process $dW\_t$.1

This equation dictates that the state of a thought at any given moment is the sum of a deterministic drive ($v$) and a stochastic fluctuation ($W$). In the context of thought selection, the "decision" occurs when $X\_t$ hits one of two absorbing boundaries: $a$ (acceptance) or $0$ (rejection).

**Table 1: The Lexicon of Drift Across Domains**

| Parameter | Symbol | Cognitive Interpretation | Biological Mechanism | AI / LLM Homolog |
| :---- | :---- | :---- | :---- | :---- |
| **Drift Rate** | $v$ / $\\delta$ | Evidence Quality; Subjective Value | Synaptic Gain; Precision-weighted prediction error 3 | Logit probability; Process Reward Score |
| **Diffusion** | $\\sigma$ / $\\varsigma$ | Cognitive Noise; Ambiguity | Stochastic firing; Thermal noise | Temperature ($T$); Sampling randomness |
| **Boundary** | $a$ | Caution; Response Threshold | Cortico-striatal gating threshold 3 | Rejection Threshold; Tokenizer cutoff |
| **Bias** | $z$ | Prior Expectation; Prejudice | Resting potential; Pre-activation 4 | System Prompt; Contextual Prior |

### **2.2 The Drift Rate as the Value Signal**

The critical insight for classifying 'good' vs 'bad' thoughts lies in the drift rate $v$. In perceptual decision-making tasks, such as determining the direction of moving dots, $v$ corresponds to the objective strength of the sensory signal (e.g., motion coherence).5 However, thoughts are rarely objectively "correct" in a sensory sense. They are "good" or "bad" based on **Subjective Value**.

Research into value-based decision making (VBDM) demonstrates that the drift rate encodes the difference in value between competing options.2 If we consider a thought $T\_A$ (e.g., "I should study") and a competing thought $T\_B$ (e.g., "I should check my phone"), the drift rate of the decision process is a function of the value difference $\\Delta V \= V(T\_A) \- V(T\_B)$.

Crucially, this mapping is not linear. Biological systems do not process value differences of 100 vs 101 units the same way they process 1 vs 2 units, despite the identical difference. The relationship is **sigmoidal**.6

$$v(\\Delta V) \= v\_{max} \\cdot \\tanh(k \\cdot \\Delta V)$$

This non-linearity serves a vital computational function: Gain Control.

1. **Saturation:** For large value differences, the drift rate saturates at $v\_{max}$. This prevents the system from wasting metabolic resources on "hyper-decisions" where the outcome is obvious.  
2. **Sensitivity:** For small value differences (near zero), the function is steepest (highest gain), allowing the system to be maximally sensitive to subtle distinctions between competing thoughts.6

In this framework, a "good" thought is operationally defined as one that generates a high positive drift rate. This high drift minimizes the **First Passage Time** (time to hit the boundary), ensuring that the thought is selected rapidly and robustly against the background noise. A "bad" thought, conversely, generates a negative drift (driving the system toward the rejection boundary) or a near-zero drift.

### **2.3 The Necessity of Diffusion: Noise as a Feature**

If the drift rate encodes value, why does the diffusion term ($\\sigma$) exist? Why hasn't evolution optimized the noise out of the system? The DDM framework suggests that noise is not merely an imperfection but a computational feature essential for **exploration** and **tie-breaking**.

When the drift rate is low—meaning the system is ambivalent between two thoughts—diffusion becomes the dominant force. This dominance of noise allows the system to make a decision even in the absence of strong evidence, preventing deadlock.3 In "mind wandering" states, the drift rate toward external tasks is low, allowing diffusion to drive the system toward disparate semantic associations. This "random walk" through memory is the mechanism of creativity, allowing the system to escape local optima that a purely deterministic (noiseless) drift would never leave.7

However, this reliance on diffusion comes at a cost. In pathological states like schizophrenia or ADHD, the signal-to-noise ratio (drift-to-diffusion ratio) is degraded. If $\\sigma$ is too high relative to $v$, the system becomes impulsive, crossing decision boundaries based on random fluctuations rather than integrated value.8 This results in the selection of "bad" thoughts—hallucinations or distractions—that possess no inherent value but are selected purely due to the thermodynamics of high-temperature sampling.

## **3\. The Thermodynamics of Thought: Energy, Entropy, and the Demon**

While the DDM describes the *kinematics* of thought (how it moves), it does not explain the *dynamics* (why it moves). Movement requires energy. The selection of a single coherent thought from a chaotic neural ensemble is, fundamentally, a reduction of entropy. This binds cognitive science inextricably to the laws of non-equilibrium thermodynamics.

### **3.1 The Brain as Maxwell’s Demon**

In 1867, James Clerk Maxwell proposed a thought experiment involving a "demon" that could sort fast molecules from slow ones, creating a temperature differential without performing mechanical work, thus appearing to violate the Second Law of Thermodynamics.9 The resolution to this paradox, provided a century later by Szilard and Landauer, is that the demon must process information. The act of measuring a particle and *erasing the memory* of that measurement to prepare for the next one dissipates energy as heat.10

The brain operates as a biological Maxwell’s Demon. The "gas" is the stochastic firing of billions of neurons—a high-entropy bath of potential thoughts, memories, and sensory inputs. The "Demon"—instantiated largely in the executive control networks of the prefrontal cortex (PFC)—must select the "fast" (high-value, task-relevant) neural coalitions and suppress the "slow" (irrelevant) ones.9

This selection is an **endothermic process** for information but an **exothermic process** for biology.

* **Entropy Reduction:** By selecting one thought and suppressing millions of others, the brain reduces the entropy of its internal state ($S\_{brain}$).  
* **Heat Dissipation:** To satisfy the Second Law ($\\Delta S\_{total} \\ge 0$), this local reduction in entropy must be compensated by a massive release of heat into the environment.

This explains why the brain, comprising only 2% of body mass, consumes 20% of the body's metabolic energy.13 Focused thinking is physically hot. The "Demon" burns glucose to maintain the low-entropy state of attention. When the energy supply falters—due to fatigue, hypoglycemia, or metabolic disease—the Demon loses its grip. Entropy rises, the drift process becomes dominated by noise, and the ability to classify and select "good" thoughts degrades.14

### **3.2 The Metabolic Cost of Inhibition: The Price of "No"**

The classification of a thought as "bad" implies its rejection. In the DDM, this is hitting the lower boundary. In the brain, this is **active inhibition**. One might intuitively assume that "not thinking" about something saves energy, but neurophysiological evidence suggests the exact opposite: inhibition is expensive.

The primary mechanism of thought suppression is the activity of GABAergic inhibitory interneurons, particularly the **Parvalbumin-positive (PV+) fast-spiking interneurons**.15 These cells act as the "brakes" of the cortex. To maintain the precision of neural firing and prevent runaway excitation (seizures or hallucinations), PV+ neurons must fire at extremely high frequencies (\>200 Hz).

* **The ATP Bill:** This high-frequency firing places an enormous demand on the Na+/K+ pumps to restore ionic gradients. Consequently, inhibitory interneurons have a disproportionately high density of mitochondria and consume vast quantities of ATP.14  
* **Hemodynamic Response:** Studies using the Stop-Signal Task (SST)—a behavioral paradigm where subjects must cancel an initiated action—show that the BOLD signal (a proxy for energy consumption) in the right Inferior Frontal Gyrus (rIFG) is often *higher* during successful inhibition than during action execution.16

This reveals a profound thermodynamic truth: **Rejection is Work**. To classify a thought as "bad" and prevent it from entering the stream of consciousness requires a pulse of metabolic energy. If the brain's energy budget is constrained (e.g., in insulin resistance or mitochondrial aging), the system cannot afford the "price of no." The result is a failure of inhibitory control, manifesting as impulsivity, intrusive thoughts, and the inability to filter out "bad" noise.17

### **3.3 The Free Energy Principle: Drift as Precision**

Karl Friston’s **Free Energy Principle (FEP)** bridges the gap between the thermodynamics of the Demon and the mathematics of the DDM. The FEP asserts that all self-organizing biological systems exist to minimize "variational free energy," which is an information-theoretic upper bound on surprise (entropy).18

In the FEP framework (specifically Active Inference), the brain minimizes surprise by updating its internal expectations to match sensory inputs. The rate of this update is determined by Prediction Error weighted by Precision.

$$\\dot{\\mu} \\propto \\Pi \\cdot \\epsilon$$

where $\\mu$ is the internal state (thought), $\\epsilon$ is the prediction error, and $\\Pi$ is the precision (inverse variance).20  
The Drift-Precision Equivalence:  
Mathematical derivations have demonstrated a formal equivalence between the DDM and Active Inference.20

* **Drift Rate ($v$) $\\approx$ Precision-Weighted Prediction Error.**  
* **Diffusion ($\\sigma$) $\\approx$ Inverse Precision (Uncertainty).**

This unifies the definitions of a "good" thought.

* **DDM View:** A "good" thought has a high drift rate.  
* **Thermodynamic View:** A "good" thought reduces entropy.  
* **FEP View:** A "good" thought has high precision; it explains the data with high confidence and low uncertainty.

When the brain classifies a thought as "good," it is assigning it high **Precision**. This high precision acts as a gain control on the drift rate, driving the thought rapidly toward the selection boundary. Conversely, "bad" thoughts are assigned low precision. In pathologies like schizophrenia, the brain assigns aberrant high precision to internal noise (hallucinations), effectively "drifting" toward a false reality because the thermodynamic cost function has been warped.22

## **4\. Neural Substrates: The Hardware of Selection**

Where does this "Drift" happen? And more importantly, where is the value function trained that determines the drift rate? The interaction between the **Default Mode Network (DMN)** and the **Executive Control Network** provides the neural hardware for this process.

### **4.1 The Default Mode Network: The Offline Simulator**

For years, the DMN was dismissed as a "task-negative" system, active only when the brain was "doing nothing." We now understand that the DMN is the engine of **offline compute**. It is metabolically expensive, consuming significantly more glucose than other networks even during rest.23

The DMN acts as the brain’s "World Model." While the executive networks handle online decision-making (the DDM process itself), the DMN handles the **calibration of the parameters**.

* **Simulation:** The DMN supports "autobiographical planning" and the simulation of hypothetical scenarios.25 It runs Monte Carlo simulations of potential futures ("What if I do X?").  
* **Value Update:** By simulating these futures and retrieving past memories, the DMN updates the subjective value ($V$) associated with different thoughts and actions. This updated value $V$ determines the drift rate $v$ for future online decisions.

### **4.2 Replay: The Gradient Descent of the Brain**

The specific mechanism for this value update is **Neural Replay**. Occurring primarily during sleep and waking rest (within DMN activation windows), replay involves the compressed, high-speed reactivation of neural sequences associated with recent experiences.27

Snippet 29 and 30 describe this as a form of **Prioritized Experience Replay** (a technique also used in Reinforcement Learning). The brain does not replay everything. It preferentially replays events that were associated with high **Reward Prediction Error**—events that were "surprising."

This replay process allows the brain to perform **Offline Reinforcement Learning**. By replaying the trajectory of a thought and its outcome, the brain backpropagates the reward signal to update the synaptic weights (the value function).

* If a thought led to a reward, replay strengthens the synapses, increasing the future drift rate for that thought.  
* If a thought led to punishment, replay weakens the synapses (or strengthens inhibitory connections), decreasing the drift rate.

This offline computation is essential. Without it, the "drift" would never improve. The "goodness" of a thought is not intrinsic; it is learned through this iterative cycle of online exploration and offline replay.31

### **4.3 Mind Wandering as Entropic Search**

"Mind wandering," often viewed as a failure of focus, is re-contextualized here as a functional Temperature Scaling.  
When the environment is stable and predictable, the brain operates at "low temperature"—high precision, narrow boundaries, minimal diffusion. This is efficient for exploiting known "good" thoughts.  
However, when the environment changes or the current task yields low reward, the "Demon" unlocks the gates. It increases the "temperature" (diffusion) and lowers the drift rates of prepotent thoughts. This is mind wandering.7  
Snippet 32 provides a crucial insight: spontaneous mind wandering is positively associated with **probabilistic learning**. By allowing the decision variable to drift diffusively (high entropy), the brain explores the state space of memory, finding non-obvious associations.

* **Exploitation (Focus):** High Drift / Low Diffusion. (Selecting the best *known* thought).  
* **Exploration (Mind Wandering):** Low Drift / High Diffusion. (Searching for *new* good thoughts).

Pathology arises when this switch is stuck.

* **Depression:** The DMN gets stuck in a "low temperature" loop on negative thoughts. The drift rate for negative rumination is so high that the brain cannot diffuse away from it.33  
* **ADHD:** The "temperature" is permanently too high. The diffusion coefficient $\\sigma$ is so large that no single thought can sustain a drift trajectory to the threshold; the system constantly jumps between attractors.3

## **5\. The Silicon Homolog: Inference-Time Compute in AI**

The principles of Drift, Entropy, and Offline Replay are not exclusive to biology. They are emerging, almost identically, in the architecture of modern Artificial Intelligence. The shift from "System 1" (fast, heuristic) AI to "System 2" (reasoning) AI is essentially the implementation of **Inference-Time Compute**—a drift diffusion process in silicon.

### **5.1 Chain of Thought as Evidence Accumulation**

Standard Large Language Models (LLMs) operate autoregressively. They predict the next token based on the previous ones. In simple generation, this is a "race to threshold" where the threshold is hit instantly. The token with the highest logit (drift rate) is selected.

However, for complex reasoning, this "System 1" approach fails. The model needs to "think." Chain of Thought (CoT) prompting allows the model to generate intermediate tokens—reasoning steps—before producing the final answer.34  
This process is isomorphic to the DDM.

* **The Chain:** The sequence of intermediate tokens $t\_1, t\_2,..., t\_n$ acts as the accumulation of evidence.  
* **The Drift:** Each step should ideally increase the probability of the correct final answer.  
* **The Bound:** The generation of the final answer or an "End of Sequence" token represents the decision boundary.

Recent research into **Diffusion-of-Thought (DoT)** and **DiffCoT** 35 makes this link explicit. These models treat the reasoning process not as a discrete jump but as a continuous diffusion process that starts from noise (high entropy) and is iteratively "denoised" (drifted) toward a coherent thought. This allows for **self-correction**: if the drift trajectory heads toward a hallucination ("bad" thought), the diffusion mechanism can steer it back toward the manifold of truth.

### **5.2 Process Reward Models (PRM): The Silicon Demon**

In standard Reinforcement Learning from Human Feedback (RLHF), models are trained with an **Outcome Reward Model (ORM)**. The model gets a reward only at the end. This is sparse and inefficient—like training a rat by only feeding it after it solves a complex maze, with no feedback along the way.36

**Process Reward Models (PRMs)** introduce a "Demon" that monitors the drift in real-time. A PRM assigns a score (value) to *each step* of the reasoning chain.37

* **Drift Modulation:** If a reasoning step is "good" (logically sound), the PRM assigns a high score. This acts as a precision weight, signaling the system to continue drifting in this direction.  
* **Inhibition:** If a step is "bad" (hallucination or error), the PRM assigns a low/negative score.

This enables sophisticated search algorithms like **Beam Search** or **Tree of Thoughts**.

* **Beam Search:** The model maintains $K$ active reasoning chains ("beams"). At each step, it generates potential next steps for all beams. The PRM scores them. The system then "prunes" the low-scoring beams—effectively exerting **Inhibitory Control** to kill "bad" thoughts before they propagate.38

**Table 2: The Computational Physics of Selection**

| Feature | Biological Brain | Artificial Intelligence (LLM) |
| :---- | :---- | :---- |
| **Generation Mechanism** | Synaptic Noise / Spontaneous Firing | Temperature Sampling / Generator Policy |
| **Selection Force** | Drift Rate ($v$) derived from Value | Process Reward Score / Logits |
| **The "Demon"** | Prefrontal Cortex (Inhibitory Control) | Process Reward Model (Verifier) |
| **Search Strategy** | Mind Wandering / Associative Search | Beam Search / Best-of-N Sampling |
| **Rejection Cost** | Metabolic (ATP for GABA interneurons) | Computational (FLOPs for rejected tokens) |
| **Offline Update** | Hippocampal Replay (DMN) | Post-Training (RLHF / Gradient Descent) |

### **5.3 The Thermodynamic Cost of AI Reasoning**

Just as the brain pays a metabolic cost for precision, AI pays a computational cost. **Inference-Time Compute** refers to the paradigm where a model is allowed to "think longer" (consume more FLOPs) to improve accuracy.40

Snippet 41 and 39 demonstrate a scaling law: **Compute \= Accuracy**.

* **Rejection Sampling (Best-of-N):** The model generates $N$ solutions. The PRM (Demon) scores them and selects the best one. This is a "brute force" thermodynamic cycle. The system generates high entropy ($N$ variance) and expends work to collapse it to low entropy (1 answer).  
* **Efficiency:** A smaller model (less "brain mass") using rejection sampling can outperform a larger model that answers instantly. This mirrors biology: a crow (small brain) with high active inference capabilities can solve problems that a larger but "reflexive" organism cannot.

However, there is a limit. Snippet 40 notes that simply scaling test-time compute has diminishing returns. There is an "optimal" amount of drift. Too little, and the thought is shallow (error-prone). Too much, and the system wastes energy on negligible gains (analysis paralysis). This mirrors the **Speed-Accuracy Trade-off** in the DDM: widening the boundaries ($a$) improves accuracy but costs time and energy linearly.

### **5.4 Offline vs. Online RL in AI**

The parallel extends to learning. AI systems are now adopting the "two-stage" compute model of the brain:

1. **Online (Inference):** The model uses its current weights (drift rates) and PRM (Demon) to navigate a problem.  
2. **Offline (Post-Training):** The "experiences" (prompts and responses) are collected. High-quality traces (verified by humans or strong models) are used to update the weights via **Reinforcement Learning** (e.g., PPO or GRPO).42

This offline step is the AI equivalent of **Replay**. The system "dreams" on its past data, updating its value functions (PRMs) so that the *next* time it runs inference, the drift rates are more accurate. Snippet 38 emphasizes that "Process Advantage Verifiers" (PAVs) trained in this offline manner provide much denser, higher-quality signals than simple outcome rewards, just as prioritized replay in the brain accelerates learning.

## **6\. Synthesis: A General Theory of Drift**

We are now positioned to formulate a unified theory. Thought selection, in any substrate, is a **Resource-Constrained Drift Diffusion Process**.

### **6.1 The Master Equation**

The "Goodness" $G$ of a thought $T$ can be defined dynamically:

$$G(T) \= \\int\_{0}^{\\tau} (v(t) \- \\lambda \\cdot C(t)) dt$$  
Where:

* $v(t)$ is the **Drift Rate** (evidence accumulation/value).  
* $C(t)$ is the **Cost** of computation (Metabolic rate in Watts or Compute rate in FLOPs).  
* $\\lambda$ is the **Shadow Price** of energy (how much the system values energy conservation vs. accuracy).  
* $\\tau$ is the time to decision.

A "good" thought is one that maximizes this integral. It accumulates value ($v$) fast enough to justify the cost ($C$) of the time spent processing it.

### **6.2 The Three Failure Modes**

This equation reveals the three fundamental pathologies of thought, applicable to both brains and bots:

1. **The Drift Failure (The "Stupid" Demon):** $v$ is poorly calibrated. The system drifts toward "bad" thoughts because its value function (DMN or PRM) is malformed.  
   * *Bio:* Delusions, bad habits.  
   * *AI:* Hallucinations, logic errors.  
2. **The Precision Failure (The "Weak" Demon):** The diffusion $\\sigma$ is too high relative to $v$. The system cannot hold a trajectory.  
   * *Bio:* ADHD, distractibility.  
   * *AI:* High-temperature incoherence.  
3. **The Metabolic Failure (The "Starved" Demon):** The system cannot pay the cost $C$. It lowers $\\lambda$, accepting "good enough" thoughts prematurely (low boundary) or failing to inhibit "bad" ones.  
   * *Bio:* Fatigue, "Hangry" impulsivity, metabolic syndrome.  
   * *AI:* Latency constraints, insufficient compute budget.

## **7\. Conclusion**

The investigation of 'drift' as a mechanism for thought selection uncovers a profound convergence. The **Drift Diffusion Model** is not just a psychological abstraction; it is the physical law governing how information is extracted from noise.

In biological systems, this law dictates that the brain must operate as a thermodynamic engine. It spends ATP to buy Precision. It utilizes the **Prefrontal Cortex** as a Maxwell’s Demon to inhibit entropic drift and the **Default Mode Network** as an offline simulator to calibrate the value functions that guide that drift. The cost of "good" thinking is literally heat—the metabolic price of inhibitory control.

In artificial systems, the same law has re-emerged from the constraints of silicon. **Inference-Time Compute** is the realization that intelligence requires the time-integration of evidence. **Chain of Thought** is the implementation of drift. **Process Reward Models** are the implementation of the Demon. The move from "System 1" generation to "System 2" reasoning in LLMs is, effectively, the evolution of a digital cortex capable of paying the energetic price (FLOPs) to reduce the entropy of its outputs.

Ultimately, whether the substrate is carbon or silicon, the definition of a "good" thought remains the same: it is a low-entropy trajectory, carved out of the chaotic possibility space by a high-precision drift, paid for with energy. Intelligence is the efficiency of this carving.

#### **Works cited**

1. How attention influences perceptual decision making: Single-trial EEG correlates of drift-diffusion model parameters \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5397902/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5397902/)  
2. The Drift Diffusion Model can account for the accuracy and reaction time of value-based choices under high and low time pressure | Judgment and Decision Making, accessed on January 17, 2026, [https://www.cambridge.org/core/journals/judgment-and-decision-making/article/drift-diffusion-model-can-account-for-the-accuracy-and-reaction-time-of-valuebased-choices-under-high-and-low-time-pressure/7C303AE6153F7DAF7FCF4FDFFCAFE11C](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/drift-diffusion-model-can-account-for-the-accuracy-and-reaction-time-of-valuebased-choices-under-high-and-low-time-pressure/7C303AE6153F7DAF7FCF4FDFFCAFE11C)  
3. A practical introduction to using the drift diffusion model of decision-making in cognitive psychology, neuroscience, and health sciences \- Frontiers, accessed on January 17, 2026, [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1039172/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1039172/full)  
4. The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks \- PMC, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC2474742/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2474742/)  
5. Testing the drift-diffusion model | PNAS, accessed on January 17, 2026, [https://www.pnas.org/doi/10.1073/pnas.2011446117](https://www.pnas.org/doi/10.1073/pnas.2011446117)  
6. The drift diffusion model as the choice rule in inter-temporal and risky choice: A case study in medial orbitofrontal cortex lesion patients and controls \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7192518/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7192518/)  
7. Why does the mind wander? \- PMC \- PubMed Central, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6804478/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6804478/)  
8. Active inference, evidence accumulation and the urn task \- PMC \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4426890/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4426890/)  
9. Maxwell's demon \- Wikipedia, accessed on January 17, 2026, [https://en.wikipedia.org/wiki/Maxwell%27s\_demon](https://en.wikipedia.org/wiki/Maxwell%27s_demon)  
10. Maxwell's Demon | The Oxford Handbook of Topics in Philosophy, accessed on January 17, 2026, [https://academic.oup.com/edited-volume/42642/chapter/358144458](https://academic.oup.com/edited-volume/42642/chapter/358144458)  
11. Brain activity and cognition: a connection from thermodynamics and information theory, accessed on January 17, 2026, [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.00818/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.00818/full)  
12. Maxwell's Demon: A Tale of Two Entropies | by Kameron Sanzo, Ph.D. \- Medium, accessed on January 17, 2026, [https://medium.com/@kameron.sanzo/maxwells-demon-a-tale-of-two-entropies-fe8404f6e5bd](https://medium.com/@kameron.sanzo/maxwells-demon-a-tale-of-two-entropies-fe8404f6e5bd)  
13. Brain Entropy During Aging Through a Free Energy Principle Approach \- Frontiers, accessed on January 17, 2026, [https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.647513/full](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.647513/full)  
14. Metabolic cost as a unifying principle governing neuronal biophysics \- PubMed Central, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC2901447/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2901447/)  
15. Evolutionary neuroeconomic adaptations of fast-spiking neurons in the human neocortex, accessed on January 17, 2026, [https://www.frontiersin.org/journals/synaptic-neuroscience/articles/10.3389/fnsyn.2026.1741452/full](https://www.frontiersin.org/journals/synaptic-neuroscience/articles/10.3389/fnsyn.2026.1741452/full)  
16. Individual differences in stop‐related activity are inflated by the adaptive algorithm in the stop signal task \- PMC \- PubMed Central, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6045976/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6045976/)  
17. The metabolic costs of cognition \- Gwern.net, accessed on January 17, 2026, [https://gwern.net/doc/psychology/neuroscience/2025-jamadar.pdf](https://gwern.net/doc/psychology/neuroscience/2025-jamadar.pdf)  
18. Free energy principle \- Wikipedia, accessed on January 17, 2026, [https://en.wikipedia.org/wiki/Free\_energy\_principle](https://en.wikipedia.org/wiki/Free_energy_principle)  
19. Free-energy and the brain \- PMC \- PubMed Central \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC2660582/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2660582/)  
20. Action understanding and active inference \- PMC \- PubMed Central, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3491875/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3491875/)  
21. Perceptual decision making: drift-diffusion model is equivalent to a Bayesian model \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3935359/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3935359/)  
22. Knowing when to stop: Aberrant precision and evidence accumulation in schizophrenia, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6020132/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6020132/)  
23. The Brain's Default Network and its Adaptive Role in Internal Mentation \- PMC \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3553600/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3553600/)  
24. Dark control: The default mode network as a reinforcement learning agent \- PubMed Central, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7375062/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7375062/)  
25. Back to the future: Autobiographical planning and the functionality of mind-wandering \- UC Santa Barbara, accessed on January 17, 2026, [https://labs.psych.ucsb.edu/schooler/jonathan/sites/labs.psych.ucsb.edu.schooler.jonathan/files/pubs/back\_to\_the\_future.pdf](https://labs.psych.ucsb.edu/schooler/jonathan/sites/labs.psych.ucsb.edu.schooler.jonathan/files/pubs/back_to_the_future.pdf)  
26. The Journey of the Default Mode Network: Development, Function, and Impact on Mental Health \- PMC \- PubMed Central, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12025022/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12025022/)  
27. Reduced coupling between offline neural replay events and default mode network activation in schizophrenia | Brain Communications | Oxford Academic, accessed on January 17, 2026, [https://academic.oup.com/braincomms/article/5/2/fcad056/7068825](https://academic.oup.com/braincomms/article/5/2/fcad056/7068825)  
28. Developmental Emergence of Replay–DMN Coordination Predicts Entorhinal Grid Codes, accessed on January 17, 2026, [https://www.biorxiv.org/content/10.1101/2025.04.02.646732v3.full-text](https://www.biorxiv.org/content/10.1101/2025.04.02.646732v3.full-text)  
29. Dark Control: Towards a Unified Account of Default Mode Function by Markov Decision Processes | bioRxiv, accessed on January 17, 2026, [https://www.biorxiv.org/content/10.1101/148890v2.full-text](https://www.biorxiv.org/content/10.1101/148890v2.full-text)  
30. Offline replay supports planning in human reinforcement learning \- eLife, accessed on January 17, 2026, [https://elifesciences.org/articles/32548](https://elifesciences.org/articles/32548)  
31. Offline replay supports planning in human reinforcement learning \- PMC \- NIH, accessed on January 17, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC6303108/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6303108/)  
32. MIND WANDERING DURING IMPLICIT LEARNING IS ASSOCIATED WITH INCREASED PERIODIC EEG ACTIVITY AND IMPROVED EXTRACTION OF HIDDEN PROBABILISTIC PATTERNS | bioRxiv, accessed on January 17, 2026, [https://www.biorxiv.org/content/10.1101/2024.07.30.605743.full](https://www.biorxiv.org/content/10.1101/2024.07.30.605743.full)  
33. Linking offline learning mechanisms to anxiety traits \- bioRxiv, accessed on January 17, 2026, [https://www.biorxiv.org/content/10.1101/2023.06.21.546031v2.full](https://www.biorxiv.org/content/10.1101/2023.06.21.546031v2.full)  
34. Learning to reason with LLMs | OpenAI, accessed on January 17, 2026, [https://openai.com/index/learning-to-reason-with-llms/](https://openai.com/index/learning-to-reason-with-llms/)  
35. DiffCoT: Diffusion-styled Chain-of-Thought Reasoning in LLMs \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2601.03559v1](https://arxiv.org/html/2601.03559v1)  
36. Process Reward Models \- Stephen Diehl, accessed on January 17, 2026, [https://www.stephendiehl.com/posts/process\_reward/](https://www.stephendiehl.com/posts/process_reward/)  
37. Process Reward Models for LLM Agents: Practical Framework and Directions \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2502.10325v1](https://arxiv.org/html/2502.10325v1)  
38. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning \- arXiv, accessed on January 17, 2026, [https://arxiv.org/pdf/2410.08146](https://arxiv.org/pdf/2410.08146)  
39. Reward-Guided Speculative Decoding for Efficient LLM Reasoning \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2501.19324v3](https://arxiv.org/html/2501.19324v3)  
40. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview, accessed on January 17, 2026, [https://openreview.net/forum?id=4FWAwZtd2n](https://openreview.net/forum?id=4FWAwZtd2n)  
41. A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce \- arXiv, accessed on January 17, 2026, [https://arxiv.org/pdf/2504.11343?](https://arxiv.org/pdf/2504.11343)  
42. A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2504.11343v1](https://arxiv.org/html/2504.11343v1)