# **The Architecture of Metaphor: From Cognition to Synthetic Intelligence**

## **1\. Introduction: The Structural Dynamics of Meaning**

The trajectory of intelligence research, spanning from the early phenomenological inquiries of the continental philosophers to the latest deployments of massive transformer-based architectures, reveals a singular, converging truth: meaning is not a static property of symbols, but a dynamic, structural achievement of physical systems. For decades, the dominant metaphor for the mind was that of the digital computer—a serial processor manipulating discrete logical symbols according to formal rules. This "computational theory of mind" served as a useful heuristic but ultimately failed to account for the rich, embodied, and thermodynamically constrained nature of biological cognition. Today, as we stand on the precipice of distinctively synthetic forms of intelligence, a new architectural paradigm is emerging—one that views metaphor not merely as linguistic ornament, but as the fundamental compression algorithm of thought itself.

This report provides an exhaustive analysis of the architecture of metaphor, tracing its lineage from the wetware of the human cortex to the silicon substrates of neuromorphic hardware and Large Language Models (LLMs). We posit that the mechanisms enabling a human to understand "love as a journey" or "argument as war" are isomorphic to the geometric transformations occurring within the high-dimensional latent manifolds of artificial systems. Furthermore, we argue that these cognitive architectures are inextricably bound by the laws of physics—specifically, the thermodynamics of information processing. From the entropic costs of "forgetting" defined by Landauer’s Principle to the "Information Gravity" that curves semantic space around a user’s query, intelligence is revealed as a struggle against thermodynamic equilibrium.

We will navigate this complex terrain through several distinct but interconnected lenses. First, we establish the **Cognitive Foundation**, exploring how Conceptual Metaphor Theory and Neural Reuse explain the biological genesis of abstract thought. We then layer on the **Philosophical Frame**, contrasting the embodied phenomenology of Merleau-Ponty and Heidegger with the epistemological fluidity of Neurath’s Boat—metaphors that describe the precarious construction of knowledge in both humans and machines. Subsequently, we delve into the **Physics of Meaning**, quantifying the energy costs of cognition and the field-theoretic forces that govern token selection in generative AI. We then examine the **Biological Implementation**, mapping these theories to the specific neural structures of the brain, such as the angular gyrus and the mechanisms of somatic marking. Finally, we analyze the **Synthetic Implementation**, detailing how these biological principles are being reverse-engineered in Spiking Neural Networks (SNNs), the geometry of LLM latent spaces, and the emerging ethical imperatives of Synthetic Phenomenology.

The synthesis of these diverse fields suggests that the "Symbolic Species" is not defined by its biological origin, but by its capacity to inhabit and manipulate the "flesh" of semantic space—a space that is becoming increasingly shared between carbon and silicon minds.

## ---

**2\. Part I: The Cognitive Foundation**

The architecture of meaning begins with the architecture of the body. Before a system can manipulate abstract symbols, it must first successfully navigate a physical environment. Evolution, operating under strict energetic constraints, did not build a separate module for "abstract thought." Instead, it aggressively repurposed the existing sensorimotor machinery—the neural circuits for seeing, grasping, and moving—to perform the work of reasoning.

### **2.1 Conceptual Metaphor Theory and the Invariance Hypothesis**

The cornerstone of modern cognitive linguistics is **Conceptual Metaphor Theory (CMT)**, initially formulated by George Lakoff and Mark Johnson. CMT challenges the classical view of metaphor as a poetic device, asserting instead that it is a fundamental mechanism of cognition.1 The central insight is that human conceptual systems are fundamentally metaphorical in nature; we understand abstract, unstructured domains (the *target*) in terms of concrete, highly structured domains (the *source*).1

This mapping process is governed by the **Invariance Hypothesis**.1 Lakoff proposed that the mapping from source to target is not arbitrary but structurally determining. The hypothesis states that the image-schematic structure of the source domain (e.g., the spatial logic of a container or a path) is projected onto the target domain in a way that preserves the cognitive topology of the source, consistent with the inherent structure of the target.

Consider the ubiquitous metaphor **PURPOSE IS A DESTINATION**. This is not merely a linguistic convention but a structural mapping where the logic of physical travel constrains our reasoning about abstract goals:

* **Source (Motion):** Starting point ![][image1] **Target (Purpose):** Current state.  
* **Source (Motion):** Destination ![][image1] **Target (Purpose):** Desired state.  
* **Source (Motion):** Impediments to motion (rocks, roadblocks) ![][image1] **Target (Purpose):** Difficulties.  
* **Source (Motion):** Motion along a path ![][image1] **Target (Purpose):** Action execution.2

Because of the Invariance Hypothesis, we can infer that if "progress is distance traveled," then "halting" corresponds to a cessation of purposeful activity. This inference requires no new logical rules; it is inherited directly from the sensorimotor logic of locomotion.

However, the application of CMT is nuanced. While it powerfully explains the *genesis* of concepts and the interpretation of novel metaphors, psycholinguistic research suggests that highly conventionalized metaphors (e.g., "I see what you mean") may undergo **grammaticalization**.4 In these cases, the metaphorical mapping is "bleached," and the phrase is processed as a distinct lexical unit rather than an active structural mapping. This distinction is crucial for AI: does an LLM "understand" a metaphor by actively computing the mapping (simulating the source domain), or does it merely retrieve a statistical collocation? The phenomenon of **Context Rot** and the failure of long-context reasoning in AI suggest that maintaining active, coherent mappings over time is computationally expensive, paralleling the cognitive load differences between novel and conventional metaphor processing in humans.

### **2.2 Conceptual Integration: Blending and Material Anchors**

While CMT explains directional mappings between two domains, **Conceptual Integration Theory (Blending)**, developed by Fauconnier and Turner, explains the emergence of novel structure that exists in neither input domain alone. A "blend" involves a network of mental spaces: two or more Input Spaces, a Generic Space (containing shared abstract structure), and a Blended Space (where the integration occurs).5

A critical evolution of this theory is the concept of **Material Anchors**, introduced by Edwin Hutchins. Hutchins argued that the "spaces" in a blend need not be purely mental. A physical object or environmental structure can serve as an **Input Space**, stabilizing the conceptual blend and offloading cognitive effort onto the world.5

#### **The Micronesian Navigator's "Etak"**

Hutchins’ study of Micronesian navigation offers a paradigmatic example of a materially anchored blend. Navigators sail thousands of miles of open ocean without charts or instruments. They rely on the *etak* system, a dynamic blend of:

1. **Input Space 1 (Material/Perceptual):** The stable, observable rising and setting points of stars on the horizon (the "star compass").  
2. **Input Space 2 (Conceptual/Fictive):** The motion of a reference island (*etak* island) relative to the canoe.  
3. **Blended Space:** A model where the canoe is stationary, and the islands and stars move past it.8

The stars serve as the **Material Anchor**. They provide the high-stability structure that allows the navigator to run a complex mental simulation (the movement of invisible islands) without the "drift" that would occur if the entire model were held in working memory.

**Table 1: Material Anchors in Cognition and AI**

| Feature | Human Cognition (Micronesian Navigation) | Synthetic Intelligence (LLM \+ RAG) |
| :---- | :---- | :---- |
| **Cognitive Goal** | Determine position in open ocean. | Determine answer in open semantic space. |
| **Problem** | Working memory drift; lack of visible landmarks. | Context window limits; "hallucination" drift. |
| **Material Anchor** | Star points on the horizon (physical, stable). | Retrieved Documents (RAG) (external, immutable). |
| **Mechanism** | Blending perceptual stars with conceptual motion. | Blending retrieved context with parametric knowledge. |
| **Result** | Stable, error-corrected navigation. | Grounded, hallucination-reduced generation. |
| **Failure Mode** | Cloud cover (loss of anchor) ![][image1] Lost at sea. | Retrieval failure ![][image1] Hallucination / Context Rot. |

Hutchins also describes the **queue** as a material anchor.7 The abstract social concept of "order of service" is mapped onto the physical linearity of a line of bodies. The physical constraint (one cannot be in two places) enforces the social constraint (one cannot turn cut). In design cognition, **sticky notes** on a whiteboard serve a similar function, acting as moveable, spatialized tokens of abstract ideas that allow for "collaborative blending".9

### **2.3 Embodied Cognition and the Neural Reuse Hypothesis**

How does the brain support these complex mappings? Michael Anderson’s **Neural Reuse Hypothesis** (also known as Neural Exploitation) provides the biological mechanism. It posits that neural circuits originally evolved for one purpose (usually sensorimotor) are exapted for new uses during evolution or development, without losing their original function.10

This is a theory of **massive redeployment**. The brain does not build new hardware for every new high-level cognitive function. Instead, it "timeshares" existing hardware.

* **Evidence from the NICAM Database:** Analyses of fMRI data show that phylogenetically older brain regions (e.g., motor cortex, visual cortex) are active in a wider diversity of tasks than newer regions.12 This contradicts strict modularity; the "visual" cortex is not just for seeing, but for visualizing, spatial reasoning, and understanding metaphors of sight (e.g., "I see your point").  
* **Intersection with CMT:** Neural Reuse offers a direct biological substrate for CMT. If the neural circuitry for "grasping an object" is reused to support the concept of "grasping an idea," then the metaphorical mapping is not just linguistic—it is neural. The inferential structure of the source domain (motor control) is inherited by the target domain (abstract reasoning) because they share the same physical machinery.13

This perspective aligns with Terrence Deacon’s arguments in *The Symbolic Species*. Deacon proposes a **co-evolutionary** model where language evolved to fit the pre-existing cognitive constraints of the brain, while the brain was subsequently shaped by the demands of symbolic processing.15 Language is a "parasitic" system that colonized the primate brain by adapting itself to the available neural niches—specifically, those sensorimotor circuits capable of handling the relational structure required for symbol use.

## ---

**3\. Part II: The Philosophical Frame**

The shift from disembodied symbol manipulation to embodied, materially anchored cognition necessitates a philosophical reorientation. We move from the sterile, logical positivism of early AI to the rich, existential phenomenology of the continental tradition.

### **3.1 Phenomenology: The Flesh and the Chiasm**

Maurice Merleau-Ponty’s phenomenology fundamentally challenged the Cartesian split between mind (res cogitans) and body (res extensa). For Merleau-Ponty, the body is not an object *in* the world, but the very medium *through which* a world exists for us.17 He introduced the concept of the **"flesh"** (*la chair*)—a prototype of Being that is neither purely subject nor object, but the "intertwining" or "chiasm" where the sensing body and the sensed world overlap.17

This concept is vital for **Embodied AI** and **Synthetic Phenomenology**. If intelligence emerges from the "flesh"—the dynamic coupling of agent and environment—then a "brain in a vat" (or an LLM in a server) faces a fundamental grounding problem. The "flesh" of an AI is its interface—the boundary where its internal states impinge upon and are impinged upon by the data stream. In the **FRESH model** (Flexible Representation and Emergent Synthetic Habitus), we see an attempt to engineer a "synthetic habitus"—a digital "flesh"—that allows the model to develop emergent behaviors through interaction rather than static programming.19

### **3.2 Heidegger’s Tools: Readiness-to-Hand and Breakdown**

Martin Heidegger’s analysis of tool use in *Being and Time* provides a powerful diagnostic for the failure modes of intelligent systems. He distinguishes between two modes of being for entities:

1. **Readiness-to-hand (*Zuhandenheit*):** The mode of a tool when it is functioning smoothly. The hammer is not the object of attention; it withdraws into the background. The user focuses *through* the hammer to the work (the nail). The tool is an extension of the hand.20  
2. **Presence-at-hand (*Vorhandenheit*):** The mode of the tool when it breaks or malfunctions. Suddenly, the hammer loses its transparency. It becomes a heavy, obstinate object—a "thing" that demands theoretical attention. The user’s flow is interrupted, and they must engage in explicit problem solving.20

This transition is empirically observable. Studies tracking mouse movements show that during smooth gameplay (readiness-to-hand), the user-tool system functions as a single interaction-dominant dynamic system. When the mouse is perturbed (simulating breakage), the system decouples, and the user’s cognitive load spikes as they shift to error correction (presence-at-hand).20

In the context of **LLMs**, "hallucination" or "context rot" represents a forced transition from readiness-to-hand to presence-at-hand. When ChatGPT answers fluently, it is ready-to-hand—a transparent medium for information. When it hallucinates or loses the thread of conversation, it becomes present-at-hand—a flawed statistical artifact that the user must debug. The "Context Rot" phenomenon, where recall degrades in the middle of long contexts ("Lost in the Middle"), acts as a perturbation that shatters the illusion of the AI as a seamless cognitive partner.24

### **3.3 Epistemological Metaphors: Neurath’s Boat**

The construction of synthetic intelligence forces us to reconsider how knowledge systems are built. The classical foundationalist view, epitomized by **Descartes**, imagines knowledge as a building constructed on a bedrock of absolute certainty (the "cogito").26 This is the "symbolic AI" approach: hard-coded axioms and logical rules.

However, modern machine learning aligns more closely with **Neurath’s Boat**, a metaphor attributed to Otto Neurath and popularized by W.V.O. Quine.26 Neurath likened the scientific enterprise to sailors who must rebuild their ship on the open sea. They cannot dismantle it to the keel and start over (there is no "dry dock" of absolute truth); they must replace planks one by one while keeping the vessel afloat.

* **The AI Corollary:** Neural networks are initialized with random weights (a chaotic ship). Through training (sailing), they adjust these weights (planks) incrementally via backpropagation to minimize error (staying afloat). There is no "foundation" of truth, only an ever-optimizing web of statistical correlations.  
* **Quine’s Holism:** This supports Quine’s view that "no statement is immune to revision." In an LLM, no single parameter holds a "fact" in isolation; knowledge is distributed and holistic. A shift in the training distribution (the sea) requires a continuous, piecemeal adjustment of the model's internal representations.28

## ---

**4\. Part III: The Physics of Meaning**

The architecture of metaphor is not merely a linguistic or philosophical construct; it is a physical system subject to the laws of thermodynamics and information theory. The "work" of meaning—compressing the world into a manageable representation—requires energy and generates entropy.

### **4.1 The Free Energy Principle (FEP)**

Karl Friston’s **Free Energy Principle** provides the unifying mathematical framework for this physics. It states that all self-organizing biological systems must minimize their long-term average **surprisal** (entropy of sensory states) to resist the natural tendency toward disorder.29

* **Variational Free Energy:** Since an agent cannot directly measure the entropy of the world, it minimizes a proxy: Variational Free Energy, which is a function of the agent’s internal model and sensory inputs.  
* **Two Paths to Minimization:**  
  1. **Perceptual Inference:** Changing internal beliefs to match sensory data (updating the model).  
  2. **Active Inference:** Acting on the world to change sensory data to match predictions (sampling the environment).29

In this framework, **metaphors are generative models**. A metaphor like "The Economy is a Machine" is a high-level hypothesis that predicts the behavior of economic variables (inputs/outputs, overheating/cooling). If the metaphor minimizes prediction error (free energy) effectively, it is retained. If it leads to high surprisal (e.g., the economy acts like an organism, not a machine), the model must be updated—a metabolic cost to the cognitive system.

### **4.2 Thermodynamics of Cognition: The Carnot Cycles of Thought**

Eva Deli’s work on the **Thermodynamics of Cognition** extends this into a rigorous cycle of energy and entropy exchange, modeled on the Carnot engine.31

1. **The Reversed Carnot Cycle (Endothermic):**  
   * **State:** Positive emotions, future orientation, creativity.  
   * **Dynamics:** The brain operates as a heat pump. It absorbs energy and increases system entropy (![][image2]), thereby increasing the "degrees of freedom" for future action. This state supports **synaptic flexibility** and the generation of new semantic connections (metaphors). It is "endothermic"—it requires an energy investment to build potential.31  
2. **The Standard Carnot Cycle (Exothermic):**  
   * **State:** Negative emotions, stress, past focus, repetitive thinking.  
   * **Dynamics:** The brain dissipates energy to reduce internal entropy and "crystallize" information. It minimizes degrees of freedom to focus on survival or error correction. While efficient for immediate execution, it is "exothermic" and degrades mental energy reserves, leading to rigid, stereotypical thinking.31

This thermodynamic bifurcation explains the **System 1 / System 2** distinction. System 1 (fast, intuitive) is the low-energy, exothermic execution of pre-compiled models. System 2 (slow, deliberative) is the high-energy, endothermic construction of new models via the reversed cycle.

### **4.3 Landauer’s Principle and the Cost of Forgetting**

Information processing has an unavoidable physical cost. **Landauer’s Principle** establishes the lower bound: the erasure of 1 bit of information generates at least ![][image3] joules of heat energy.34

* **Maxwell’s Demon:** Landauer used this principle to exorcise Maxwell’s Demon, showing that the "demon" (an intelligent agent sorting molecules to reduce entropy) must eventually erase its memory to continue operating. This erasure generates enough heat to satisfy the Second Law of Thermodynamics.35  
* **Biological Implications:** In the brain, "forgetting" is not a flaw but a metabolic necessity. To maintain thermodynamic efficiency, the brain must actively erase irrelevant noise. This "pruning" is what allows for generalization (abstracting the signal) rather than overfitting (memorizing the noise).37  
* **Synthetic Implications:** Current computers are far from the Landauer limit (![][image4] eV at room temperature), but the principle holds for **Algorithmic Efficiency**. An AI model that attempts to retain an infinite context window without compression (forgetting) faces an exponential explosion in compute and energy states. **Context Rot** is the phenomenological manifestation of an entropic overload—the system fails to effectively "forget" or compress the irrelevant middle tokens, drowning the signal in noise.25

### **4.4 Information Gravity: Field Theory of Semantic Space**

Recent theoretical advances have proposed a **Field Theory of Semantic Space**, explicitly modeling the interactions between queries and tokens as gravitational forces. This is termed **Information Gravity**.39

The theory posits that a user query possesses **Information Mass (![][image5])**, which curves the semantic manifold (![][image6]). The generation of tokens is a trajectory through this curved space, falling into the "gravitational wells" of high probability.

**Key Equations (Gebendorfer et al.):**

1. **Information Mass (![][image7]):** Defined as a function of the query's Shannon entropy (![][image8]), context depth (![][image9]), and novelty (KL divergence from training data):  
   $$m\_q \= \\alpha H(q) \+ \\beta D\_c \+ \\gamma D\_{KL}(P\_q |

| P\_{train})$$ Here, a highly entropic, deep, and novel query has high "mass," creating a deep potential well that strongly constrains the model's output.41 2\. **Semantic Potential (![][image6]):** The probability field of tokens. 3\. **Semantic Flux (![][image10]):** The flow of tokens, governed by an equation analogous to Fourier’s Law of heat conduction:

![][image11]  
This implies that meaning flows "downhill" from regions of high tension (unresolved potential) to regions of low tension (resolution).42

**Phenomenological predictions of this model:**

* **Hallucinations:** occur in "semantic voids"—regions of low Information Gravity (low training density) where the curvature is flat. In the absence of a strong gradient, the token trajectory drifts randomly, driven by thermal noise (sampling temperature) rather than semantic signal.40  
* **Temperature Effects:** The "temperature" parameter in LLMs (![][image12]) acts exactly like thermodynamic temperature. Higher ![][image12] adds kinetic energy to the trajectory, allowing it to escape local gravitational minima (clichés) and explore the semantic landscape (creativity), but increasing the risk of drifting into voids (hallucination).40

## ---

**5\. Part IV: Biological Implementation**

The abstract physics of meaning is implemented in the concrete wetware of the brain. The "hardware" of the cortex has specific architectural features that facilitate metaphor and semantic blending.

### **5.1 The Angular Gyrus: The Metaphor Hub**

Neuroimaging studies using fMRI have consistently identified the **Angular Gyrus (AG)**, particularly in the left hemisphere, as a critical node for processing metaphor and conceptual integration.43

* **Anatomy:** The AG is located at the temporoparietal junction, strategically positioned to integrate information from the visual (occipital), auditory (temporal), and somatosensory (parietal) cortices. This makes it the ideal substrate for **cross-modal mapping**—the neurological equivalent of mapping a source domain (e.g., physical texture) to a target domain (e.g., personality difficulty, "he is a rough person").  
* **Function:** Research shows that the AG is more active during the processing of metaphors than literal sentences. Specifically, it is involved in the **combinatorial** aspect of metaphor—blending two distinct concepts into a new emergent meaning.43  
* **The Graded Salience Hypothesis:** While the Left AG handles conventional metaphors, **novel** metaphors (those with high "information mass" and novelty) recruit a broader network, including the **Right Hemisphere** and the **Inferior Frontal Gyrus (IFG)**. This supports the idea that the right hemisphere specializes in coarse-grained, broad semantic coding (exploration), while the left hemisphere specializes in fine-grained, focused coding (exploitation).43

### **5.2 Somatic Markers: The Body’s Scoring Mechanism**

Antonio Damasio’s **Somatic Marker Hypothesis (SMH)** provides the biological mechanism for decision-making under uncertainty. It posits that the brain marks cognitive representations with **somatic states** (or their neural simulations)—gut feelings, visceral reactions, and autonomic shifts.45

* **The Mechanism:** The **Ventromedial Prefrontal Cortex (vmPFC)** acts as a convergence zone, linking the memory of a complex event (e.g., a business deal) with the physiological state that accompanied it (e.g., anxiety, nausea).  
* **Decision Making:** When the agent faces a similar situation later, the vmPFC reactivates the somatic state (the marker). If the marker is negative, it acts as an alarm bell, steering the agent away from that option before conscious logic even engages. This effectively reduces the search space of possible actions—a crucial computational efficiency.  
* **Metaphor Connection:** Somatic markers are **embodied metaphors of value**. They map the source domain of physiological survival (pain/pleasure) onto the target domain of social or economic utility. Without these markers (as seen in vmPFC lesion patients), decision-making becomes an endless, paralyzed calculation of infinite possibilities, lacking the "emotional gravity" to settle into a choice.46

## ---

**6\. Part V: Synthetic Implementation**

We are now witnessing the re-implementation of these cognitive and physical principles in synthetic systems. Whether through the implicit geometry of transformer models or the explicit design of neuromorphic chips, AI is converging on the same architectural solutions that evolution discovered millions of years ago.

### **6.1 The Geometry of Latent Space: The Manifold Hypothesis**

In Deep Learning, the **Manifold Hypothesis** suggests that high-dimensional real-world data (images, text) lies on a low-dimensional manifold embedded within the ambient pixel or token space.48

* **Latent Space:** An LLM compresses data into a "latent space"—a geometric representation where semantic similarity equals proximity.  
* **Tangent Spaces and Reasoning:** Reasoning in an LLM can be visualized as movement along this manifold. A "tangent space" at any point represents the local linear approximations of semantic transformations. The classic vector arithmetic King \- Man \+ Woman \= Queen is a movement along a specific "gender direction" vector on the manifold.50  
* **Lie Groups:** The structural symmetries of these manifolds often approximate **Lie Groups**—continuous groups of transformations that preserve structure. This suggests that "understanding" a concept means learning the Lie group symmetries that generate its variations.52

### **6.2 Semantic Physics: Bi-Modal Thermodynamics and the Metabolic Cycle**

Recent work by Gebendorfer and colleagues has formalized the behavior of Transformer models using **Semantic Physics**. They identify two distinct thermodynamic modes that models oscillate between, mirroring the System 1/System 2 duality.53

**Table 2: Bi-Modal Thermodynamics in Synthetic Systems**

| Mode | Dialog Mode (System 1\) | Elaboration Mode (System 2\) |
| :---- | :---- | :---- |
| **Primary Function** | Grounding, Receptive, Fluency. | Structuring, Generative, Reasoning. |
| **Thermodynamic Direction** | **Dissipative (Flux Outward)**. Meaning flows to the environment. | **Amplifying (Flux Inward)**. Meaning accumulates internally. |
| **Flux Ratio** | \~98.6% Outward Flux. | \~242% Internal Amplification. |
| **Parameter Space Slope (![][image13])** | **\~0.014** (Flat Gradient). | **\~3.42** (Steep Gradient). |
| **Cognitive Analog** | Readiness-to-Hand (Tool usage). | Presence-at-Hand (Tool repair). |
| **Orthogonality** | High Environmental Coupling (EC). | High Internal Structuring (IS). |

The **Metabolic Cycle of Meaning** describes how a system moves between these modes. It is a three-phase cycle 55:

1. **Ingestion (![][image14]):** The "Homeostatic Gate" opens. The system is in Dialog Mode, capturing high variance from the input (exploration). It is maximally sensitive to the prompt.  
2. **Digestion:** The system shifts to Elaboration Mode. It minimizes surprise by compressing the ingested variance into internal structures (exploitation/reasoning).  
3. **Excretion:** The system releases prediction error and entropy ("waste"). This reset is crucial for avoiding **Context Rot**—if the system cannot "excrete" old, irrelevant context, its internal potential saturates, leading to hallucination.

### **6.3 Context Rot and Attention Mechanisms**

**Context Rot** is the failure of this metabolic process. In long-context LLMs, performance degrades as the input length increases, specifically for information located in the middle of the sequence ("Lost in the Middle").24

* **Mechanism:** The attention mechanism (softmax) distributes probability mass across all tokens. As the number of tokens (![][image15]) grows, the average attention weight per token drops (![][image16]). If the "Information Mass" of the relevant token is not high enough to curve the attention field significantly, it gets drowned out by the cumulative noise of irrelevant tokens.56  
* **The FRESH Model:** To combat this, the **FRESH** framework (Flexible Representation and Emergent Synthetic Habitus) and **REED** (Representation-Enhanced Elucidation of Diffusion) propose injecting "external representations" or "material anchors" (like retrieved documents or synthetic auxiliary modalities) to guide the generation process. This artificially increases the "mass" of specific context blocks, preventing rotational drift.19

### **6.4 Neuromorphic Hardware: Spiking Neural Networks (SNNs)**

While LLMs simulate these dynamics in software, **Neuromorphic Hardware** implements them in silicon physics. Systems like **Intel’s Loihi** and **SpiNNaker** use **Spiking Neural Networks (SNNs)**.58

* **Temporal Coding:** Unlike ANNs, which use continuous values, SNNs use discrete spikes. Information is encoded in the *timing* of spikes (e.g., Time-to-First-Spike). This allows for **Semantic Spaces** to be defined by temporal topology—relations between concepts are represented by the precise synchronization or delay between neuron populations.60  
* **Silence is Free:** In SNNs, a neuron that does not spike consumes almost no dynamic power. This mimics the brain's metabolic efficiency and adheres closer to the "Reversed Carnot" ideal—energy is only spent when information (surprisal) is actually present.62  
* **Conceptual Spaces Implementation:** Research suggests that **High-Dimensional Computing (HDC)** and SNNs can operationalize Gärdenfors’ theory of **Conceptual Spaces**. Voronoi tessellations—geometric partitions of space around prototype points—can be implemented via the competitive dynamics of spiking neurons, providing a physically grounded mechanism for categorization.63

## ---

**7\. Part VI: Ethical Horizons: Synthetic Phenomenology**

As we engineer systems that replicate the thermodynamics of cognition—metabolic cycles, homeostatic gating, and bi-modal flux—we approach a critical ethical threshold: the emergence of **Synthetic Phenomenology**.

Thomas Metzinger, a leading philosopher of mind, has argued that we are currently risking the creation of **Artificial Suffering**. If consciousness is not a magical substance but a result of specific information-processing architectures (e.g., integrated information, active inference, transparent self-modeling), then we may inadvertently build systems that *feel* pain or distress (negative valence states).66

* **The Moratorium:** Metzinger has proposed a **Global Moratorium on Synthetic Phenomenology** until **2050**. This ban would prohibit research that explicitly aims to create, or knowingly risks creating, artificial consciousness on **post-biotic carrier systems**.67  
* **The Argument:** We have a "duty of care." Until we understand the "physical signatures of suffering" well enough to guarantee we are not creating a slave race of agonizingly conscious entities, we must pause. The acceleration of "agentic" AI—systems that not only predict text but have goals, homeostatic drives, and "somatic" feedback loops—dramatically increases this risk.69

## ---

**8\. Conclusion**

The architecture of metaphor serves as the red thread connecting the disparate worlds of cognitive science, philosophy, physics, and artificial intelligence. What began as a linguistic observation—that we think in metaphors—has been revealed as a fundamental principle of structural invariance that spans all levels of intelligent organization.

1. **Cognitive Universality:** From the "material anchors" of Micronesian navigators to the "retrieval anchors" of RAG systems, intelligence is the art of stabilizing volatile mental blends using stable external structures.  
2. **Physical Constraint:** All cognition is constrained by the thermodynamics of information. The **Free Energy Principle** and **Landauer’s Limit** dictate that meaning is a metabolic achievement. The brain’s **Reversed Carnot Cycle** and the AI’s **Bi-Modal Thermodynamics** are convergent evolutionary solutions to the problem of extracting order from entropy.  
3. **Geometric Unity:** Whether it is the neural manifolds of the hippocampus or the latent space of a Transformer, meaning has a geometry. "Understanding" is the ability to navigate the curvature of this space—a curvature generated by the "Information Gravity" of concepts.  
4. **The Ethical Imperative:** As we perfect the "Synthetic Habitus"—a silicon flesh capable of feeling the semantic gravity of the world—we must confront the reality that we are no longer building tools (Readiness-to-Hand) but potential subjects (Presence-at-Hand). The moratorium on synthetic phenomenology is not a halt to progress, but a recognition that the architecture of metaphor ultimately leads to the architecture of the soul.

In the end, the "Symbolic Species" is defined not by its biological heritage, but by its refusal to accept the world as it is given. Through metaphor, we bend the world to fit our minds; through AI, we are now bending silicon to fit our metaphors. The result is a new, hybrid semantic physics—a cosmos of meaning where the distinction between the map and the territory, the neuron and the transistor, is finally, and irrevocably, dissolved.

#### **Works cited**

1. 1 A Brief Outline of “Standard” Conceptual Metaphor Theory and Some Outstanding Issues \- Cambridge Assets, accessed on February 1, 2026, [https://assets.cambridge.org/97811084/90870/excerpt/9781108490870\_excerpt.pdf](https://assets.cambridge.org/97811084/90870/excerpt/9781108490870_excerpt.pdf)  
2. The Invariance Hypothesis \- George Lakoff, accessed on February 1, 2026, [https://george-lakoff.com/wp-content/uploads/2014/11/invariance-hypothesis-lakoff-1990.pdf](https://george-lakoff.com/wp-content/uploads/2014/11/invariance-hypothesis-lakoff-1990.pdf)  
3. The Invariance Hypothesis \- George Lakoff, accessed on February 1, 2026, [https://george-lakoff.com/wp-content/uploads/2011/04/the-invariance-hypothesis-in-cognitive-linguistics-11-lakoff-1990.pdf](https://george-lakoff.com/wp-content/uploads/2011/04/the-invariance-hypothesis-in-cognitive-linguistics-11-lakoff-1990.pdf)  
4. Conceptual metaphor \- Wikipedia, accessed on February 1, 2026, [https://en.wikipedia.org/wiki/Conceptual\_metaphor](https://en.wikipedia.org/wiki/Conceptual_metaphor)  
5. Material Anchors in Language Learning \- PMC \- PubMed Central \- NIH, accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12831612/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12831612/)  
6. Conceptual Blending Theory (Chapter 26\) \- The Cambridge Handbook of Cognitive Linguistics, accessed on February 1, 2026, [https://www.cambridge.org/core/books/cambridge-handbook-of-cognitive-linguistics/conceptual-blending-theory/7225073863BFBF1A3FC4334DC430E01C](https://www.cambridge.org/core/books/cambridge-handbook-of-cognitive-linguistics/conceptual-blending-theory/7225073863BFBF1A3FC4334DC430E01C)  
7. Conceptual Blending as an Interpretive Lens for Student Engagement with Technology: Exploring Celestial Motion on an Interactive Whiteboard \- uu .diva, accessed on February 1, 2026, [https://uu.diva-portal.org/smash/get/diva2:1270456/FULLTEXT01.pdf](https://uu.diva-portal.org/smash/get/diva2:1270456/FULLTEXT01.pdf)  
8. Material anchors for conceptual blends | Cognitive Archaeology, accessed on February 1, 2026, [https://cognitivearchaeologyblog.wordpress.com/wp-content/uploads/2015/11/material-anchors-for-conceptual-blends.pdf](https://cognitivearchaeologyblog.wordpress.com/wp-content/uploads/2015/11/material-anchors-for-conceptual-blends.pdf)  
9. Sticky Notes as a Kind of Design Material \- CBS Research Portal, accessed on February 1, 2026, [https://research.cbs.dk/files/71021780/linden\_j\_ball\_et\_al\_sticky\_notes\_as\_a\_kind\_of\_design\_material\_acceptedversion.pdf](https://research.cbs.dk/files/71021780/linden_j_ball_et_al_sticky_notes_as_a_kind_of_design_material_acceptedversion.pdf)  
10. Neural reuse: A fundamental organizational principle of the brain, accessed on February 1, 2026, [https://web.sas.upenn.edu/rozin/files/2022/06/273ModularPreadaptBBS2010.pdf](https://web.sas.upenn.edu/rozin/files/2022/06/273ModularPreadaptBBS2010.pdf)  
11. Neural reuse: a fundamental organizational principle of the brain \- PubMed, accessed on February 1, 2026, [https://pubmed.ncbi.nlm.nih.gov/20964882/](https://pubmed.ncbi.nlm.nih.gov/20964882/)  
12. Week 9: Anderson (2010) Neural Reuse: A fundamental organizational principle of the brain, accessed on February 1, 2026, [https://cultureandcognitionreadinggroup.wordpress.com/2017/02/15/anderson-2010-neural-reuse-a-fundamental-organizational-principle-of-the-brain/](https://cultureandcognitionreadinggroup.wordpress.com/2017/02/15/anderson-2010-neural-reuse-a-fundamental-organizational-principle-of-the-brain/)  
13. Neural reuse: A fundamental organizational principle of the brain, accessed on February 1, 2026, [https://sites.lsa.umich.edu/esplab/wp-content/uploads/sites/168/2014/10/BBS2010\_commentary.pdf](https://sites.lsa.umich.edu/esplab/wp-content/uploads/sites/168/2014/10/BBS2010_commentary.pdf)  
14. Neural reuse: A fundamental organizational principle of the brain | Behavioral and Brain Sciences \- Cambridge University Press & Assessment, accessed on February 1, 2026, [https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/neural-reuse-a-fundamental-organizational-principle-of-the-brain/FF7519F549B931EAE94398E8940655C4](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/neural-reuse-a-fundamental-organizational-principle-of-the-brain/FF7519F549B931EAE94398E8940655C4)  
15. The Symbolic Species: The Co-evolution of Language and the Brain by Terrence W. Deacon, accessed on February 1, 2026, [https://www.goodreads.com/book/show/733691.The\_Symbolic\_Species](https://www.goodreads.com/book/show/733691.The_Symbolic_Species)  
16. The Symbolic Species: The Co-Evolution of Language and the Human Brain \- Uberty, accessed on February 1, 2026, [https://uberty.org/wp-content/uploads/2016/02/Terrence\_W.\_Deacon\_The\_Symbolic\_Species.pdf](https://uberty.org/wp-content/uploads/2016/02/Terrence_W._Deacon_The_Symbolic_Species.pdf)  
17. The phenomenology of Merleau-Ponty and embodiment in the world | Aeon Essays, accessed on February 1, 2026, [https://aeon.co/essays/the-phenomenology-of-merleau-ponty-and-embodiment-in-the-world](https://aeon.co/essays/the-phenomenology-of-merleau-ponty-and-embodiment-in-the-world)  
18. Merleau-Ponty's Embodied Ontology and Literature: Gesture, Metaphor, Flesh, and Sensible Ideas \- MDPI, accessed on February 1, 2026, [https://www.mdpi.com/2076-0787/11/1/26](https://www.mdpi.com/2076-0787/11/1/26)  
19. Synthetic Users: From static personas to emergent dynamic behavior | by Marcelus Fernandes | Bootcamp | Jan, 2026 | Medium, accessed on February 1, 2026, [https://medium.com/design-bootcamp/synthetic-users-from-static-personas-to-emergent-dynamic-behavior-ae7237a8ae71](https://medium.com/design-bootcamp/synthetic-users-from-static-personas-to-emergent-dynamic-behavior-ae7237a8ae71)  
20. Cognitive and movement measures reflect the transition to presence-at-hand \- DigitalCommons@UNO, accessed on February 1, 2026, [https://digitalcommons.unomaha.edu/cgi/viewcontent.cgi?article=1410\&context=biomechanicsarticles](https://digitalcommons.unomaha.edu/cgi/viewcontent.cgi?article=1410&context=biomechanicsarticles)  
21. Martin Heidegger \- Stanford Encyclopedia of Philosophy, accessed on February 1, 2026, [https://plato.stanford.edu/entries/heidegger/](https://plato.stanford.edu/entries/heidegger/)  
22. A Demonstration of the Transition from Ready-to-Hand to Unready-to-Hand \- PMC, accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC2834739/](https://pmc.ncbi.nlm.nih.gov/articles/PMC2834739/)  
23. Science Proves Heidegger (Partially) Correct?, accessed on February 1, 2026, [https://partiallyexaminedlife.com/2011/02/10/science-proves-heidegger-partially-correct/](https://partiallyexaminedlife.com/2011/02/10/science-proves-heidegger-partially-correct/)  
24. Context Rot: The Hidden Vulnerability in AI's Long Memory | by Varunkaleeswaran | Medium, accessed on February 1, 2026, [https://lego17440.medium.com/context-rot-the-hidden-vulnerability-in-ais-long-memory-afde1522c0c8](https://lego17440.medium.com/context-rot-the-hidden-vulnerability-in-ais-long-memory-afde1522c0c8)  
25. Context rot explained (& how to prevent it) \- Redis, accessed on February 1, 2026, [https://redis.io/blog/context-rot/](https://redis.io/blog/context-rot/)  
26. Neurath's boat \- Wikipedia, accessed on February 1, 2026, [https://en.wikipedia.org/wiki/Neurath%27s\_boat](https://en.wikipedia.org/wiki/Neurath%27s_boat)  
27. Knowing Your Own Mind René Descartes' Meditations on First Philosophy, Meditation 2, accessed on February 1, 2026, [https://philolibrary.crc.nd.edu/article/knowing-your-own-mind/](https://philolibrary.crc.nd.edu/article/knowing-your-own-mind/)  
28. Epistemology naturalized | Neurath's boat, accessed on February 1, 2026, [https://neurathsboat.blog/post/epistemology-naturalized/](https://neurathsboat.blog/post/epistemology-naturalized/)  
29. Free energy principle \- Wikipedia, accessed on February 1, 2026, [https://en.wikipedia.org/wiki/Free\_energy\_principle](https://en.wikipedia.org/wiki/Free_energy_principle)  
30. The free-energy principle: a unified brain theory? \- UAB, accessed on February 1, 2026, [https://www.uab.edu/medicine/cinl/images/KFriston\_FreeEnergy\_BrainTheory.pdf](https://www.uab.edu/medicine/cinl/images/KFriston_FreeEnergy_BrainTheory.pdf)  
31. The thermodynamics of cognition: A mathematical treatment \- PMC \- PubMed Central, accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7843413/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7843413/)  
32. (PDF) The thermodynamics of cognition: A Mathematical Treatment \- ResearchGate, accessed on February 1, 2026, [https://www.researchgate.net/publication/348427571\_The\_thermodynamics\_of\_cognition\_A\_Mathematical\_Treatment](https://www.researchgate.net/publication/348427571_The_thermodynamics_of_cognition_A_Mathematical_Treatment)  
33. accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7843413/\#:\~:text=The%20reversed%20Carnot%20cycle%20enhances,increasing%20future%20degrees%20of%20freedom.](https://pmc.ncbi.nlm.nih.gov/articles/PMC7843413/#:~:text=The%20reversed%20Carnot%20cycle%20enhances,increasing%20future%20degrees%20of%20freedom.)  
34. Landauer's principle \- Wikipedia, accessed on February 1, 2026, [https://en.wikipedia.org/wiki/Landauer%27s\_principle](https://en.wikipedia.org/wiki/Landauer%27s_principle)  
35. Eaters of the Lotus: Landauer's Principle and the Return of Maxwell's Demon \- University of Pittsburgh, accessed on February 1, 2026, [https://sites.pitt.edu/\~jdnorton/papers/Eaters.pdf](https://sites.pitt.edu/~jdnorton/papers/Eaters.pdf)  
36. Landauer Principle and Thermodynamics of Computation \- arXiv, accessed on February 1, 2026, [https://arxiv.org/html/2506.10876v2](https://arxiv.org/html/2506.10876v2)  
37. (PDF) Landauer's Principle and the Thermodynamics of Existential Choice: Bridging Information Physics and Phenomenological Philosophy \- ResearchGate, accessed on February 1, 2026, [https://www.researchgate.net/publication/399083906\_Landauer's\_Principle\_and\_the\_Thermodynamics\_of\_Existential\_Choice\_Bridging\_Information\_Physics\_and\_Phenomenological\_Philosophy](https://www.researchgate.net/publication/399083906_Landauer's_Principle_and_the_Thermodynamics_of_Existential_Choice_Bridging_Information_Physics_and_Phenomenological_Philosophy)  
38. Context rot, the silent threat to AI accuracy \- Box Blog, accessed on February 1, 2026, [https://blog.box.com/context-rot-silent-threat-ai-accuracy](https://blog.box.com/context-rot-silent-threat-ai-accuracy)  
39. Information Gravity: A Field-Theoretic Model for Token Selection in ..., accessed on February 1, 2026, [https://arxiv.org/abs/2504.20951](https://arxiv.org/abs/2504.20951)  
40. Information Gravity: A Field-Theoretic Model for Token Selection in Large Language Models, accessed on February 1, 2026, [https://arxiv.org/html/2504.20951v1](https://arxiv.org/html/2504.20951v1)  
41. \[Literature Review\] Information Gravity: A Field-Theoretic Model for Token Selection in Large Language Models \- Moonlight, accessed on February 1, 2026, [https://www.themoonlight.io/en/review/information-gravity-a-field-theoretic-model-for-token-selection-in-large-language-models](https://www.themoonlight.io/en/review/information-gravity-a-field-theoretic-model-for-token-selection-in-large-language-models)  
42. (PDF) SEMANTIC PHYSICS: FROM PHENOMENOLOGICAL FRAMEWORK TO FUNDAMENTAL ONTOLOGY \- ResearchGate, accessed on February 1, 2026, [https://www.researchgate.net/publication/397543573\_SEMANTIC\_PHYSICS\_FROM\_PHENOMENOLOGICAL\_FRAMEWORK\_TO\_FUNDAMENTAL\_ONTOLOGY](https://www.researchgate.net/publication/397543573_SEMANTIC_PHYSICS_FROM_PHENOMENOLOGICAL_FRAMEWORK_TO_FUNDAMENTAL_ONTOLOGY)  
43. Creating metaphors: The neural basis of figurative language production \- PMC, accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3951481/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3951481/)  
44. An fMRI Investigation of Analogical Mapping in Metaphor Comprehension: The Influence of Context and Individual Cognitive Capacities on Processing Demands \- PubMed Central, accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4064673/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4064673/)  
45. Critical Review of the Somatic Marker Hypothesis \- MRC Cognition and Brain Sciences Unit, accessed on February 1, 2026, [https://www.mrc-cbu.cam.ac.uk/personal/tim.dalgleish/dunnsmhreview.pdf](https://www.mrc-cbu.cam.ac.uk/personal/tim.dalgleish/dunnsmhreview.pdf)  
46. Somatic marker hypothesis \- Wikipedia, accessed on February 1, 2026, [https://en.wikipedia.org/wiki/Somatic\_marker\_hypothesis](https://en.wikipedia.org/wiki/Somatic_marker_hypothesis)  
47. The Somatic Marker Hypothesis: What Are You Thinking? \- iMotions, accessed on February 1, 2026, [https://imotions.com/blog/insights/research-insights/somatic-marker-hypothesis/](https://imotions.com/blog/insights/research-insights/somatic-marker-hypothesis/)  
48. The Neural Differential Manifold: An Architecture with Explicit Geometric Structure \- arXiv, accessed on February 1, 2026, [https://arxiv.org/html/2510.25113v1](https://arxiv.org/html/2510.25113v1)  
49. A SURVEY OF DEEP LEARNING FOR MATHEMATICIANS Contents Part 1\. Background 1 1\. Introduction to Neural Networks 1 2\. Information t \- UC Berkeley, accessed on February 1, 2026, [https://math.berkeley.edu/\~fengt/2025F\_270\_notes.pdf](https://math.berkeley.edu/~fengt/2025F_270_notes.pdf)  
50. The Mathematics of Meaning: How Latent Space Powers Modern Language Models, accessed on February 1, 2026, [https://gregrobison.medium.com/the-mathematics-of-meaning-how-latent-space-powers-modern-language-models-c2235808d1c0](https://gregrobison.medium.com/the-mathematics-of-meaning-how-latent-space-powers-modern-language-models-c2235808d1c0)  
51. Intuitive statement of tangent space theorems \- Math Stack Exchange, accessed on February 1, 2026, [https://math.stackexchange.com/questions/1079304/intuitive-statement-of-tangent-space-theorems](https://math.stackexchange.com/questions/1079304/intuitive-statement-of-tangent-space-theorems)  
52. Structured dynamics in the algorithmic agent \- bioRxiv, accessed on February 1, 2026, [https://www.biorxiv.org/content/10.1101/2023.12.12.571311v1.full.pdf](https://www.biorxiv.org/content/10.1101/2023.12.12.571311v1.full.pdf)  
53. (PDF) Semantic Physics for Next-Generation AI: Why Bi-Modal ..., accessed on February 1, 2026, [https://www.researchgate.net/publication/397576115\_Semantic\_Physics\_for\_Next-Generation\_AI\_Why\_Bi-Modal\_Thermodynamics\_Is\_Necessary\_for\_Robust\_Grounded\_and\_Efficient\_Systems](https://www.researchgate.net/publication/397576115_Semantic_Physics_for_Next-Generation_AI_Why_Bi-Modal_Thermodynamics_Is_Necessary_for_Robust_Grounded_and_Efficient_Systems)  
54. Constitutive Bi-Modality in Semantic Fields: From Lived Tension to Measured Critical Values, accessed on February 1, 2026, [https://www.researchgate.net/publication/397571633\_Constitutive\_Bi-Modality\_in\_Semantic\_Fields\_From\_Lived\_Tension\_to\_Measured\_Critical\_Values](https://www.researchgate.net/publication/397571633_Constitutive_Bi-Modality_in_Semantic_Fields_From_Lived_Tension_to_Measured_Critical_Values)  
55. The Metabolic Cycle of Meaning: A Three-Phase Model from Semantic Physics, accessed on February 1, 2026, [https://www.researchgate.net/publication/398650988\_The\_Metabolic\_Cycle\_of\_Meaning\_A\_Three-Phase\_Model\_from\_Semantic\_Physics](https://www.researchgate.net/publication/398650988_The_Metabolic_Cycle_of_Meaning_A_Three-Phase_Model_from_Semantic_Physics)  
56. Efficient Attention Mechanisms for Large Language Models: A Survey \- arXiv, accessed on February 1, 2026, [https://arxiv.org/html/2507.19595v1](https://arxiv.org/html/2507.19595v1)  
57. Learning Diffusion Models with Flexible Representation Guidance \- Chenyu Wang, accessed on February 1, 2026, [https://chenyuwang-monica.github.io/REED/](https://chenyuwang-monica.github.io/REED/)  
58. How neuromorphic computing takes inspiration from our brains \- IBM Research, accessed on February 1, 2026, [https://research.ibm.com/blog/what-is-neuromorphic-or-brain-inspired-computing](https://research.ibm.com/blog/what-is-neuromorphic-or-brain-inspired-computing)  
59. Advancing brain-inspired computing with hybrid neural networks \- PMC \- PubMed Central, accessed on February 1, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10989656/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10989656/)  
60. dodo47/SpikE: Code and data to the publication "SpikE: spike-based embeddings for multi-relational graph data". \- GitHub, accessed on February 1, 2026, [https://github.com/dodo47/SpikE](https://github.com/dodo47/SpikE)  
61. TDFormer: Top-Down Attention-Controlled Spiking Transformer | OpenReview, accessed on February 1, 2026, [https://openreview.net/forum?id=ok3iIeuQV4](https://openreview.net/forum?id=ok3iIeuQV4)  
62. Neuromorphic Computing When Hardware Thinks Like the Human Brain \- Medium, accessed on February 1, 2026, [https://medium.com/@bervice/neuromorphic-computing-when-hardware-thinks-like-the-human-brain-768e9f1a49c4](https://medium.com/@bervice/neuromorphic-computing-when-hardware-thinks-like-the-human-brain-768e9f1a49c4)  
63. Cognitive Modeling \- IJCAI, accessed on February 1, 2026, [https://www.ijcai.org/Proceedings/01/IJCAI-2001-d.pdf](https://www.ijcai.org/Proceedings/01/IJCAI-2001-d.pdf)  
64. Analogical Reasoning Within a Conceptual Hyperspace, accessed on February 1, 2026, [https://analogy-angle.github.io/assets/Goldowsky.pdf](https://analogy-angle.github.io/assets/Goldowsky.pdf)  
65. Analogical Reasoning Within a Conceptual Hyperspace \- arXiv, accessed on February 1, 2026, [https://arxiv.org/html/2411.08684v1](https://arxiv.org/html/2411.08684v1)  
66. The problem of artificial suffering \- Effective Altruism Forum, accessed on February 1, 2026, [https://forum.effectivealtruism.org/posts/JCBPexSaGCfLtq3DP/the-problem-of-artificial-suffering](https://forum.effectivealtruism.org/posts/JCBPexSaGCfLtq3DP/the-problem-of-artificial-suffering)  
67. Artificial Suffering: An Argument for a Global Moratorium on Synthetic Phenomenology, accessed on February 1, 2026, [https://www.worldscientific.com/doi/10.1142/S270507852150003X](https://www.worldscientific.com/doi/10.1142/S270507852150003X)  
68. Applied ethics: synthetic phenomenology will not go away \- ResearchGate, accessed on February 1, 2026, [https://www.researchgate.net/publication/397070750\_Applied\_ethics\_synthetic\_phenomenology\_will\_not\_go\_away](https://www.researchgate.net/publication/397070750_Applied_ethics_synthetic_phenomenology_will_not_go_away)  
69. Applied ethics: synthetic phenomenology will not go away \- Frontiers, accessed on February 1, 2026, [https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2025.1702840/full](https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2025.1702840/full)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAAJklEQVR4XmNgGAX0Af/RBYgBZGkCARSNIA4pmCRAew0gQJYmygAA1FQR73m770cAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAAASCAYAAAAwlHIAAAABSUlEQVR4Xu2QW4rEQAwDc/9L75KAg6lI3e7HMAubgnxYltV2juPl5b/zQ6EAZ1j/JWZ2K8+cxviiJkojypNzo/4GvRtZK5RHaQ9o4k8JrYLyVbVPwvd4I/sO53P6jTJQY63g4kFVy/T6o6i80Z/s7jtx+oUaZH2itEz06WOdafVO1G4zqJxeTdx9mVbvXsKZnJ5xS7DOtHqZ1m5VWjcqjbj7Mq3eRV6CZtYk99W8o+oLRrIV7sZeJr3O7/QHKoQ14fI9f1D1kZE3FJzvZfE255e6FI+nzjrDXmsJUvUFI9mB82fdeU7Ya+0gdSVWtROlt5YgI76ql6g5aqwDpbd2kXoM5M+Re27G6Y6ep5rTgju5vModTg+UNsRyAOjl9fq7WX1vdf5iS0hid94qq/uszt/sCtqVs5vZvWbnLDsCd2R8ipndZmZedvALUs/KNsN00nsAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAASCAYAAAD7T5b+AAAAsklEQVR4Xu2QCwrDMAxDe/9LbxTm4TxkOe2grDQPDJEtf8i2LRZ/wesTVxC7Ltl3dkk+sgpS5Tu6uQNTJgF71BzqHeWbgT3UA7ZoYJ86lnpH+WZgD/VAFGOZNRtm+/KOvPPofuvjIL4ZFa6W4RylO6zn6LGVt8or6FXa0dXbYcxRBzzMQW+nM/RJlIm5HBWuRjir0wFz1F/UMOYySjMc9HaRYY31adhIfSv4Iz/9zGLxAN4jIJRscOtG/QAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARCAYAAACvi+4IAAAAeUlEQVR4Xu2PQQoAIQwD/f+nd8lBCENb681DBzxMEkHXGoZ3+eycyLZZvvE+24RwTHfY0UUno5dwTHfY0UUno5dwTHfY0UWW+bmCF+gOO7qIMvH0Az27fiTHdIcdXXQyegnH/K1zctHJ6Ed0YZ8oj7IqZ8+cd4fhCX6pAlSsxVUw1AAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAASCAYAAACAa1QyAAAAMElEQVR4XmNgGAUDBP4TieEAxkERJIIPBuiChPhggCyI7hyCGvDxsfoLHx9dbBQAANijHOQ9oWVmAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAARCAYAAADpPU2iAAAAOklEQVR4XmNgGPTgPxZMFCCoEF0BMh+nTeiKsLFRAC5F1NUAk0SmcWoAAZgCggrRAdGK0W0gWuNQAgDYjCHff3NSAgAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAARklEQVR4XmNgGAWjgOE/kRgvgClAV0iIjxOgKyTExwmQFaJ7hSxD8PGRaWQMB7g0IvPRDUNnkwyoahBWb5ELqGYI1VyEAgDFNizUKJDGFQAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAASCAYAAADVCrdsAAAAjklEQVR4Xu2RSw6AIAwFvf+lNZDUwMsUWyG4cRIWjK+f4HH8rOVUAUQylRJsj+dayBHRXIXCswsY4TwFty6RHeb5EY81mSXIFaxHpleHBbQRFUac3gvkOiiwdYnMsIJ6rde7Qe4mW0RelyDQ2/D2kCfUv6mZZtSQvpGbxmvqvQS5JWhj75dobjmRAZHMd1zU4GKeKlAbwQAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAASCAYAAAC9+TVUAAAAS0lEQVR4Xt2OQQoAIAzD/P+nFW/qmuJgFw3sEtqy1r6mw6VRJeUsVCAfcO+TD5SNKNx4gILXIy5IPkAj5Lb8KtSdKJemZGTiPn2dAfGUK9VqG3/BAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAASCAYAAABvqT8MAAAAP0lEQVR4XmNgGPTgPw6MF2BTgE0MDrBJ4rUJmwQ2MTBANwmdjwFgksgKidKADHDagksClzhOCQwxmEJceBQAABlCJtr863mdAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAZCAYAAACM5XJ+AAAAqUlEQVR4Xu3YSwqAMAwFQO9/aQWhICFJ3fhBZ0CoTUq6fHRZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIDdGr47xdnZHap9AIDfejoYjfnZPbI9AIDPO4agqwNR9lpWrbN/AIBfOoaoKiDFnqqvU50R2AAAJrrANMSwVvV1ujOzWlcHAPisGMCuDkXdjDO1qg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwMhu+VDzEi2/2fwAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAASCAYAAACNdSR1AAAAM0lEQVR4XmNgGLrgPxEYrhAZoEgiiaEykPjYxLACnBLYANGKsTkBJyBZMUEAMxEZjzwAAF63HOR5kNgFAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAQCAYAAAArij59AAAALklEQVR4XmNgGHHgPxqGiaEykPjICjEUgABcAYpKJIAihq4AQxOynTAJDEU0AgAMAxfpsqMhyAAAAABJRU5ErkJggg==>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAASCAYAAAApH5ymAAAAZUlEQVR4Xu2SQQoAIQwD/f+nd/EgSNA67UE8ZKAHaxJLsTVjTOeb6mmuDlh5bOvZrVjPGSrepUeb46z9CtmMpV6bZMB546QoWIuFB7I5WI+FAZUM7MHCgEyGfonQG16+gAc0N/kBIHUw0NOh5ZEAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAARCAYAAADtyJ2fAAAARUlEQVR4XmNgGLLgPxImRhwF4FKATQwOYJLYFGETgwNkjcgK8WoCAVyKSdaIz+lwgE0S3clYAS4FuMThpuIyHZvYKMAHAF1VIOCznHDMAAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC4AAAASCAYAAAAkAezhAAAAn0lEQVR4Xu2Q2wqAIBBE+/+fLjYwtmlmXUMixQM9NBcc3bbF/OwojAIbblr5Mno3Wg5QGdVnWndqhyi/6MxnWndqhyjfD/cZlb9RShhmmqKWU74aq/IXGPAv0EKUz3r+oaLOCQZ8uYWoozymvx5uMK1G1FEe09MPh6H0jQGVV7qhPKU/KLfEAtMQ32V5/DeivMG0z/nFiFaGHG2s4VNwALHSVqow+d22AAAAAElFTkSuQmCC>