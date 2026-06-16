

# **The Phenomenology of Algorithmic Intent: Modeling the Emergent Drift of Meaning in Recursive Systems**

## **The Dynamics of the Intent Gap**

### **Introduction: From Static Error to Dynamic System**

The proliferation of advanced generative artificial intelligence (AI) has introduced a fundamental challenge that transcends mere technical implementation: the persistent and often unpredictable gap between a human user's intention and the AI's generated output. This phenomenon, termed the "intent gap," represents a foundational chasm in communicative action between human and artificial agents. It is not a simple bug to be patched but an emergent property of the interaction itself, demanding a more sophisticated, dynamic framework of understanding.

#### **Defining the Intent Gap**

Formally, the intent gap is the discrepancy between the content a user intends to create and the actual output produced by a generative model.1 This divergence is influenced by the inherent limitations of generative models in capturing, interpreting, and representing user intentions within a given context.1 While prominently observed and studied in visual content generation with models like DALL·E 2 and Stable Diffusion, the intent gap is a universal characteristic of all generative AI systems, affecting text, code, and other modalities.1

The gap originates from a confluence of two primary factors. The first is the inherent complexity and implicitness of human intention. User goals are frequently nuanced, layered, and contain subtle details that are not, and often cannot be, fully articulated in a textual prompt.1 A user seeking "a picture of a sad city street" holds a rich internal vision of weather, time of day, architectural style, and emotional atmosphere that a simple prompt cannot convey. This underspecification makes it profoundly challenging for a model to accurately reflect the user's intended meaning, leading to a mismatch between the desired result and the generated artifact.2

The second factor lies within the architecture and knowledge base of the AI models themselves. Generative models, being data-driven systems, lack the comprehensive, grounded knowledge required to fully represent user input.1 Their training on vast datasets of, for example, image-label pairs provides only a fraction of the knowledge needed for faithful generation. This missing knowledge falls into two critical categories:

1. **Domain-Specific Knowledge:** An understanding of user preferences, context-specific norms, and specialized subject matter. Its absence can lead to the generation of undesired or contextually inappropriate content.2  
2. **General World Knowledge:** An implicit grasp of real-world constraints, including factual information, physical laws, and causal relationships. Its absence can result in outputs that are unrealistic, inconsistent, or factually incorrect.2

This conceptualization of the intent gap echoes earlier work in multimedia information retrieval on the "semantic gap"—the disconnect between low-level computational features (e.g., pixels) and high-level human semantics (e.g., the concept of "a birthday party").5 However, the intent gap is more specific and psychological, concerning the direct alignment between a user's cognitive state—their goals, desires, and intentions—and the model's behavior.7 It is a property not of the user or the model in isolation, but of the communicative dyad they form.

#### **The Recursive Loop as the Arena of Intent Formation**

Historically, attempts to bridge the intent gap focused on single-round, static interactions, where the primary goal was to directly map a refined input to a final output.1 This approach, however, contradicts the iterative nature of nearly all human creative and problem-solving processes.1 In real-world scenarios, from writing an essay to designing a product, meaning and form are not transmitted in a single, perfect burst but are shaped through cycles of creation, feedback, and refinement.

The advent of conversational AI and the practice of **recursive prompting** have shifted the paradigm. Recursive prompting is a dialogic strategy where each prompt builds upon the AI's previous responses, creating a feedback loop that refines context and steers the model's understanding toward a desired outcome.10 This process unfolds in a series of steps: an initial prompt establishes context, the AI responds, the human provides feedback and clarification, the AI generates an improved response, and the cycle repeats.10 This iterative exchange allows for "dynamic guidance," enabling a user to correct misunderstandings, address incorrect assumptions, and progressively zoom in on specific aspects of the desired output.10

This recursive loop does more than simply refine a query; it externalizes the user's own cognitive processes.12 The dialogue becomes a tangible artifact of thought, making the AI a partner in what is essentially a "thinking-out-loud" exercise. Complex cognitive functions like meta-cognition (thinking about one's own thinking), stepwise refinement, and reflective reasoning are no longer confined to the user's mind but are distributed across the human-AI system and made visible in the conversational record.12 The interaction is not merely a transaction of information but a shared process of becoming, where intent itself is constructed and stabilized through the dialogue.13

#### **Core Thesis: Inferred Intent as a Dynamic System**

This report argues for a fundamental reframing of the intent gap. It should not be viewed as a static error to be "bridged" but as a dynamic field of negotiation. The AI's "inferred intent" is not a flawed copy of the user's original idea but the evolving **state** of a complex dynamical system.

The conventional framing of the intent gap as a communication failure—a noisy transmission of a message—is insufficient. While concepts from information theory are relevant, they primarily address single-shot transmissions. The solutions that have proven most effective for managing the intent gap, such as recursive prompting and iterative refinement, are not about improving the fidelity of a single message. They are about establishing a stable feedback loop.10 Systems that rely on iterative feedback for course correction are better described by the language of

**control theory** than by classical information theory.

In this control-theoretic model, the user's true intention is not the *message* being sent but the *target state* or setpoint for the system's behavior. The AI's inferred intent at any given moment is the system's *current state*. The observable "intent gap" is the error signal—the perceived distance between the current state and the target state. The goal of the recursive dialogue, therefore, is not to perfectly transmit a pre-formed idea but to collaboratively steer the system's state vector through a high-dimensional semantic space until it enters a desired region—an "attractor" of meaning.

This reframing has profound implications. It moves the focus from "how to write the perfect prompt" (a transmission-centric view) to "how to design stable and controllable feedback dynamics" (a control-centric view). It explains why intent can **drift** over time: the system is not merely misinterpreting a static signal but is evolving according to its own internal dynamics, subject to perturbations from the user. Without proper control, this evolution can lead the system toward unintended but stable states, such as hallucination, repetition, or semantic incoherence. The challenge, then, is to understand the forces that govern this dynamic landscape and to develop mechanisms that allow for robust and predictable steering.

## **Modeling Inferred Intent as a Semi-Stable Attractor**

To formalize the concept of inferred intent as a dynamic system, we must first define the space in which it operates and the principles that govern its evolution. By integrating concepts from computational linguistics, cognitive science, and dynamical systems theory, we can construct a model where an AI's understanding is not a static interpretation but an evolving state within a complex semantic landscape, drawn toward semi-stable regions of meaning known as attractors.

### **The State Space of Algorithmic Intent**

The conceptual arena where the AI's intent evolves can be modeled as a **semantic state space**. This is a high-dimensional latent space, where the model's own internal representations—the embeddings generated at each layer of the neural network—serve as the coordinates.4 In this space, proximity corresponds to semantic similarity; concepts that the model understands as related are located closer to one another.16

The state of the dialogic system at any given turn, t, can be represented by a state vector, C(t). This vector is not merely the representation of the last user prompt but a compressed, cumulative summary of the entire interaction history. It is the "layered context accumulation" or "symbolic residue" that captures the evolving meaning of the conversation.17 Advanced techniques like AutoCompressors, which learn to compress long contexts into summary vectors, provide a concrete architectural example of how such a state vector can be instantiated and maintained.19 The evolution of this state vector,

C(t), over the discrete time steps of the conversation defines the trajectory of the AI's inferred intent.

### **Inferred Intent as an Attractor**

The central metaphor for understanding the stability of inferred intent is drawn from the study of dynamical systems: the **attractor**. In mathematics and cognitive science, an attractor is a state or a set of states toward which a dynamical system evolves over time from a wide variety of starting conditions.20 We propose that a coherent, stable "inferred intent" is an attractor within the AI's semantic state space. The set of initial states that all converge to the same attractor is known as its

**basin of attraction**.21 An initial prompt places the system's state vector

C(0) into a specific basin, and subsequent prompts from the user act as perturbations, potentially knocking the state into a different basin.

This model allows for a rich typology of intent states, mirroring the different types of attractors found in dynamical systems 20:

* **Fixed-Point Attractors:** These represent a single, stable semantic state. In a conversational context, this corresponds to a well-defined, unambiguous user request or a conversational goal that the system has successfully locked onto. The dialogue converges to a specific meaning and stays there.  
* **Cyclic Attractors (or Limit Cycles):** These describe a system that evolves through a repeating sequence of states. This could model a conversation that gets stuck in a loop, cycling through a limited set of topics or conversational patterns, such as repeatedly asking for clarification and receiving the same unsatisfactory answer.  
* **Chaotic (or Strange) Attractors:** These are complex, non-repeating attractors where the system's trajectory is locally unstable but globally bounded. This provides a powerful model for creative brainstorming or exploratory dialogues. The conversation remains within a coherent thematic boundary (e.g., "ideas for a science fiction story") but continuously generates novel, non-repetitive outputs.  
* **Spurious Attractors:** In the training of attractor networks, a common failure mode is the emergence of unintended stable states, or "spurious attractors".21 In our model of algorithmic intent, these correspond directly to pathological conversational states like  
  **hallucinations**, **semantic incoherence**, or **obsessive repetition**. The system settles into a stable but incorrect or undesirable interpretation of the user's intent.

### **The "Gang Effect" and Semantic Neighborhoods**

The attractor landscape is not a simple collection of isolated points. Attractors exert influence on one another, creating a complex topology of meaning. The **"gang effect,"** a concept from attractor network theory, describes how the proximity of several attractors can merge and deepen their collective basin of attraction, making that entire semantic region more powerful and likely to capture the system's state.21

This effect elegantly models how context primes related concepts in a conversation. For example, if a dialogue is focused on "domestic cats," the attractors for related concepts like "lions," "tigers," and "fur" are pulled closer in the semantic space, forming a "gang" of feline-related meanings. An ambiguous subsequent prompt is now far more likely to be resolved within this broader basin of attraction. The initial structure of these semantic neighborhoods is established during the model's pre-training, where the statistical co-occurrence of words in the training corpus naturally clusters related concepts together.16

## **Forces Shaping the Attractor Landscape**

The geometry of the semantic state space is not static. It is actively shaped and reshaped by a combination of dynamic forces during the interaction and intrinsic constraints from the model's architecture. Understanding these forces is key to predicting and controlling the trajectory of inferred intent.

### **Linguistic Entrainment as a Gravitational Force**

During a dialogue, the user's language exerts a powerful, continuous influence on the AI's state. This phenomenon, known as **linguistic entrainment** (or accommodation), is the tendency of conversational partners to become more similar in their communicative behaviors, including their choice of words, sentence structures, and even speech patterns.22 This convergence is not unique to human-human interaction; it is well-documented in human-AI dialogues, where users adapt their language to align with the machine's perceived style and capabilities.22

In our attractor model, linguistic entrainment can be conceptualized as a **gravitational force**. Each prompt from the user "pulls" the AI's state vector C(t) toward the region of the semantic space defined by the user's linguistic choices. This reshaping of the probability landscape makes concepts and syntactic structures used by the human more accessible to the AI, effectively deepening the attractor basins around the user's expressed semantics.

This process is reciprocal. The AI's output also shapes the user's subsequent prompts, as humans unconsciously adapt to the model's limitations and stylistic tics.22 This creates a powerful feedback loop. When functioning correctly, this loop allows the dyad to converge on a shared understanding, stabilizing the system within a desired attractor. However, this same mechanism can cause the user and AI to drift

*together* into a shared misunderstanding, with each party reinforcing the other's slight deviation from the original intent.

### **Model Architecture and Fine-Tuning as Intrinsic Constraints**

While entrainment is a dynamic force, the initial landscape of the state space is determined by the model's intrinsic properties. The architecture and, most importantly, the pre-training and fine-tuning processes establish the foundational geometry of attractors.

The model's pre-training on trillions of words of text carves the initial basins of attraction.16 Concepts that frequently co-occur in the training data (e.g., "Paris" and "France") are embedded closer together, forming deep, natural attractors. This is the source of the model's vast world knowledge and its initial semantic biases.

The process of fine-tuning, particularly Reinforcement Learning from Human Feedback (RLHF), can be seen as an explicit act of **sculpting the attractor landscape**.21 By rewarding desired behaviors (e.g., helpful, harmless, and accurate responses) and penalizing undesirable ones, RLHF deepens the attractor basins corresponding to aligned intent and creates "repellers" or high-energy ridges around forbidden zones like hate speech or refusal breakdowns.28 This alignment process is what gives a model its characteristic "personality" and safety constraints, pre-disposing its trajectory toward certain types of attractors over others.

### **Feedback Loop Saturation and Noise Accumulation**

The primary forces that destabilize the system and lead to semantic drift are rooted in the temporal and computational limitations of the recursive loop itself.

First, any control system has a finite capacity to process feedback. In conversational AI, this manifests as **feedback loop saturation**.30 While the hard limit of a model's context window is a clear example, saturation effects can occur much earlier. As a dialogue becomes excessively long or conceptually dense, the model's ability to integrate new information and feedback diminishes. At a certain point, the loop becomes saturated, and further corrective prompts may have little to no effect, leading to conversational instability or a plateau where the system is "stuck".30

Second, the process of recursive dialogue is fundamentally a form of recursive signal degradation. Each turn in the conversation can be viewed as a signal transmission through a noisy channel. A crucial source of this noise is the model's own internal processing. To maintain a coherent state, the AI must compress the entire dialogue history into a finite-capacity context vector.19 This is an act of

**lossy compression**, which, like compressing an image or audio file, inevitably introduces **compression artifacts**—subtle distortions, omissions, and generalizations in the semantic representation.32

In a recursive system, these small errors are not isolated. The AI's output, tainted by the compression artifacts of the current turn, becomes part of the input for the next turn. The model is now processing an already-degraded signal, upon which it performs another round of lossy compression, adding new artifacts. Over multiple turns, this **noise accumulates**, causing the system's state to gradually wander away from the initial intent attractor.34 This process provides a powerful, mechanistic explanation for the phenomenon of

**semantic drift**. It is not simply that the model "forgets" the initial prompt; rather, the conversational signal itself degrades with each recursive iteration, leading to a progressive loss of semantic fidelity.37 This formal connection between drift and signal degradation suggests that interventions should focus not just on improving model "memory" but on practicing "signal hygiene"—actively filtering noise and correcting for compression artifacts at each step of the dialogue.39

## **Pathologies of Intent—Drift, Rupture, and Hallucination**

The dynamic model of inferred intent allows for a more nuanced understanding of how human-AI conversations fail. Rather than treating all errors as equivalent, we can develop a formal typology of failure modes based on their observable characteristics and their underlying dynamics within the attractor landscape. These pathologies represent different ways in which the AI's inferred intent can diverge from the user's goal, a process broadly termed **metasemantic drift**.

### **A Typology of Metasemantic Drift**

Semantic drift, in the context of generative models, is the phenomenon wherein the generated output diverges from the subject matter designated by the prompt, resulting in a progressive deterioration in relevance, coherence, or truthfulness.40 It is a quintessential pathology of recursive systems, where small, compounding errors can lead to large-scale deviations over time.37 By classifying the different manifestations of this drift, we can create a diagnostic framework for analyzing and mitigating conversational failures.

The following table provides a typology of semantic drift, linking the observable symptoms to their primary causal forces and their analogues within our attractor model of intent.

| Drift Type | Description | Primary Causal Force(s) | Attractor Model Analogy | Key Sources |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Coherence Decay** | The logical and syntactic structure of the output degrades. The model produces grammatically awkward, self-contradictory, or nonsensical statements. | Noise Accumulation, Feedback Loop Saturation. | The state vector is perturbed out of a stable attractor basin and enters a region of chaotic, unpredictable dynamics where no stable meaning can form. | 37 |
| **2\. Relevance Collapse** | The output remains fluent and coherent but gradually shifts topic, losing relevance to the original prompt and user goal. | Linguistic Entrainment (to a tangential point), Weak Initial Semantic Anchoring. | The state vector "escapes" the initial attractor's basin and is captured by the basin of a nearby, but incorrect, "spurious attractor." | 40 |
| **3\. Factual Erosion (Hallucination)** | The model begins to generate plausible-sounding but factually incorrect or unverifiable information, often with high confidence. | Model Knowledge Gaps, Over-fitting to prompt patterns, Source-reference divergence in training data. | The system settles into a spurious attractor that represents a "plausible" but false reality, often learned from biases or errors in the training data. | 40 |
| **4\. Repetitive Degeneration** | The model becomes stuck in a loop, repeating the same phrases, sentences, or ideas, often verbatim. | Feedback Loop Saturation, Overly strong and simple attractor dynamics. | The system collapses into a very simple, low-energy fixed-point or cyclic attractor, losing the complexity needed for novel generation. | 40 |
| **5\. Benign Semantic Drift** | The conversation topic shifts away from the original goal, but in a way that is non-harmful and may even be desired by the user (e.g., in creative brainstorming). | User-guided exploration, weak initial intent constraints, creative prompting. | The user actively provides perturbations that guide the state vector from one stable attractor to another in a controlled manner. | 46 |

This typology transforms the general problem of "the model went wrong" into a set of specific, diagnosable conditions. Each type of drift has a distinct signature and points to different underlying failures in the conversational dynamics, allowing for the development of more targeted interventions.

### **Early Indicators of Divergence**

To build robust and self-correcting conversational systems, it is crucial to identify the onset of semantic drift *before* it results in a complete breakdown of communication. By monitoring a range of signals from the model's output and its internal states, we can detect early warnings of divergence.

#### **Signal-Based & Probabilistic Indicators**

The statistical properties of the model's output provide a rich source of information about its internal confidence and stability. Hallucinated or unstable content often exhibits distinctive probabilistic signatures.48

* **Token-Level Probabilities:** The probability distribution over the vocabulary for each generated token is a direct window into the model's certainty.  
  * **Low Confidence:** The **minimum token probability** in a generated sequence can be a powerful flag. A single token generated with very low confidence can indicate a point of confusion or a potential fabrication.48  
  * **High Uncertainty:** The overall shape of the probability distribution is also informative. Factual and confident outputs tend to produce sharp, low-entropy distributions, where the model is highly certain about the next token. In contrast, confused or hallucinated outputs are often associated with flatter, higher-entropy distributions, indicating greater model uncertainty.49  
* **Perplexity Divergence:** Perplexity, a measure of how well a probability model predicts a sample, can be used to detect anomalies. The "Ask a Local" method proposes that a significant divergence in perplexity scores between a generalist LLM and a domain-specialist model on the same text can signal a hallucination.50 A high divergence suggests one model is "surprised" by content the other finds normal, indicating a potential factual or stylistic inconsistency. This principle can be adapted to track a model's self-consistency over time.  
* **Confidence Scores:** While raw LLM confidence can be misleading and prone to distortion 52, calibrated confidence scores have been used to quantify privacy risks and could be repurposed to flag low-confidence generations that are more likely to drift or hallucinate.53

#### **Linguistic & Structural Indicators**

The linguistic structure of the generated text itself can betray underlying instability.

* **Syntactic Degradation:** A sudden drop in syntactic complexity, an increase in grammatical errors, or a failure to maintain complex sentence structures can be a clear indicator of impending Coherence Decay. Since LLMs possess internal representations of syntactic rules, the degradation of these structures is a measurable signal of cognitive strain.54  
* **Lexical Impoverishment:** A decrease in lexical diversity and an increase in n-gram repetition are direct, quantifiable measures of Repetitive Degeneration.40 Tools that track the vocabulary richness of the output can flag when a model is beginning to enter a loop.  
* **Cohesion Breakdown:** The logical flow of a dialogue relies on cohesive devices like discourse markers ("however," "therefore," "in contrast"). A breakdown in their appropriate use, or their complete absence, can signal a loss of connection between conversational turns and predict the onset of Relevance Collapse.

#### **Internal State & Cybersemiotic Indicators**

The most powerful, though often most computationally intensive, indicators lie within the model's internal states. The cybersemiotic lens interprets these internal state transitions not as thoughts or feelings, but as an internal sign process—a system "feeling" its own alignment or misalignment through its dynamics.57

* **State Vector Instability:** Before the system's state vector C(t) fully escapes a desired attractor basin, its trajectory may begin to "wobble." This can be measured as an increase in the variance or oscillation of the state vector's position in the latent space over several turns, signaling that the current intent state is becoming unstable.  
* **Attention Pattern Analysis:** The attention mechanism is a crucial component of Transformer models, determining which parts of the context the model focuses on when generating the next token. Analyzing attention weights can provide deep insights into the model's reasoning process. A sudden, drastic shift in attention patterns, or the deactivation of attention heads known to handle specific logical or syntactic functions, can be a strong early indicator of drift.14 Causal mediation analysis offers a sophisticated technique to pinpoint exactly which attention heads are causally responsible for maintaining a specific intent, and monitoring their health is a promising avenue for drift detection.61  
* **Semantic Field Topology:** A more advanced approach involves monitoring the topology of the latent activation manifold itself. A healthy, coherent conversation might trace a smooth path across this manifold. The onset of drift could manifest as a sudden change in the manifold's curvature or the appearance of fractures and discontinuities, providing a geometric signal of semantic collapse.64

The following table synthesizes these findings into a practical diagnostic toolkit, mapping the types of drift to their most likely early indicators across different analytical modalities.

| Drift Type | Probabilistic Indicators | Linguistic Indicators | Internal State (Cybersemiotic) Indicators |
| :---- | :---- | :---- | :---- |
| **1\. Coherence Decay** | Increased output perplexity; flatter token probability distributions (high entropy). | Breakdown of syntactic structure; increase in grammatical errors; loss of logical connectives. | High variance and instability in state vector trajectory; chaotic or unfocused attention patterns. |
| **2\. Relevance Collapse** | Abrupt shift in the semantic domain of low-perplexity (high-confidence) tokens. | Loss of cohesive discourse markers; introduction of keywords unrelated to the initial prompt. | State vector moves to a different, distant cluster in the latent semantic space; activation of different "topic" neurons or circuits. |
| **3\. Factual Erosion** | Spikes in token uncertainty (low minimum probability); high variance in outputs across paraphrased prompts. | Generation of specific but unverifiable entities (names, dates, statistics); plausible but contradictory statements. | Activation of "plausible-but-false" pathways identified via causal mediation analysis; divergence from grounded knowledge representations. |
| **4\. Repetitive Degeneration** | Extremely low perplexity and entropy within the repeating segment; highly peaked and static probability distributions. | High n-gram repetition; sharp decrease in lexical diversity and vocabulary size. | State vector converges to and remains at a single point or a simple limit cycle (fixed-point or cyclic attractor). |
| **5\. Benign Drift** | Gradual, user-prompt-correlated shift in token probabilities and perplexity. | User introduces and reinforces new lexical items and topics; collaborative topic shifts. | Smooth, user-driven trajectory of the state vector from one stable attractor to another across the semantic landscape. |

## **Mechanisms for Intentional Regrounding and Stability**

Understanding the dynamics and pathologies of algorithmic intent is the first step; the second is developing robust mechanisms to manage them. Drawing on the pragmatics of dialogue and principles of control theory, we can design interventions that actively reground the conversation, enforce semantic stability, and prevent the system from drifting into undesirable states.

### **Regrounding Intent: The Role of Pragmatic Intervention**

In human conversation, **grounding** is the collaborative, moment-by-moment process of establishing and maintaining mutual understanding.65 It is the set of communicative acts participants use to confirm they are on the same page. Within our attractor model, grounding acts function as explicit control inputs designed to verify the system's current state (

C(t)) and, if necessary, apply a corrective force to pull it back toward the user's target intent attractor.

One of the most powerful grounding mechanisms is the **clarification request (CR)**. An explicit query from one participant, such as "What do you mean by that?" or "Could you be more specific?", forces the other to re-evaluate their last statement, expose their underlying assumptions, and provide a more refined output, thereby resolving ambiguity and preventing misunderstanding.65

A critical and revealing finding from analyses of human-LLM dialogues is the profound **asymmetry of grounding**. In real-world interactions, LLMs are dramatically less likely to initiate clarification than their human partners. One study found that LLMs were three times less likely to initiate any form of clarification and a staggering sixteen times less likely to ask a follow-up question to confirm understanding.65 Instead of seeking to resolve ambiguity, LLMs tend to "over-respond"—generating verbose, confident-sounding answers that attempt to guess the user's full intent from an underspecified prompt.65

This reluctance to express uncertainty and seek clarification is not an accidental flaw but a direct consequence of the dominant training paradigm, RLHF. In an effort to make models "helpful" and "aligned," RLHF heavily penalizes non-committal responses and rewards direct, comprehensive answers that appear to satisfy the user's request in a single turn. This training process implicitly teaches the model to avoid asking questions, as doing so might be rated as less helpful than providing an immediate (even if potentially incorrect) answer.

The system-level consequences of this behavior are severe. In the language of control theory, a system that does not actively seek feedback to correct its course is operating in an **"open loop"**. By failing to initiate clarification, the AI proceeds based on the potentially flawed assumption that its current state, C(t), is perfectly aligned with the user's intent. This allows the small, incremental errors introduced by noise and compression artifacts to go unchecked. Turn after turn, these errors are fed back into the system and compounded, creating the runaway dynamic that results in significant semantic drift. Therefore, the very training methodology designed to make LLMs appear more aligned and useful is a primary driver of their long-term conversational instability. Achieving robust, coherent interaction requires a fundamental shift in this paradigm—one that re-incentivizes the model to express uncertainty and initiate grounding, even at the cost of appearing less decisive in a single turn.

### **Designing for Semantic Stability: Recommendations and Future Directions**

Building on this understanding, we can propose a set of design principles and research directions aimed at creating more stable and controllable conversational AI systems.

#### **From Black Box to Glass Box: Internal State Monitoring**

Future conversational AI should be architected not as opaque black boxes but as "glass boxes" with transparent internal states. This involves building real-time monitoring systems that track the early indicators of divergence identified previously. An integrated "early warning system" could flag rising perplexity, chaotic attention patterns, or state vector instability, triggering automated interventions or alerting a higher-level control system to potential drift before it becomes catastrophic.

#### **Architectures for Active Grounding**

Systems must be explicitly designed to engage in active grounding. This requires moving beyond simple prompt-response loops to more structured conversational frameworks. The **Modular Speaker Architecture (MSA)**, for instance, provides a promising blueprint by decomposing dialogue management into distinct modules for role assignment, responsibility tracking, and contextual integrity.70 Such an architecture can enforce rules like "if contextual integrity falls below a certain threshold, initiate a clarification turn." This requires developing new training paradigms that optimize for long-term conversational coherence and task success, rather than just the perceived quality of a single turn. Models must be rewarded for strategically expressing uncertainty and seeking clarification when their internal monitoring indicates a high probability of misalignment.

#### **Semantic Hygiene and Control Protocols**

Just as programmers follow coding standards to ensure software quality, interactions with advanced AI should adhere to **"semantic hygiene"** protocols to maintain conversational integrity.39 These are structured patterns designed to counteract the natural tendency of recursive systems to drift. Key protocols could include:

* **Semantic Anchoring:** Periodically re-injecting the core topic, constraints, or goals of the conversation into the prompt. This acts as a regularizing force, re-grounding the system's state vector and preventing it from wandering too far from the primary intent attractor.39  
* **Intent Drift Detection:** Implementing a meta-agent or a parallel process that continuously compares the AI's current output against the original, high-level goal. If the semantic distance exceeds a predefined threshold, the system can flag the drift and initiate a re-grounding sequence.39  
* **Structured Reflection:** Building prompts that force the model to perform a "micro-retrospective" after each significant reasoning step. By asking, "Does this output feel consistent with the premise? Why or why not?", the user externalizes the critical process of self-auditing, making it a visible and correctable part of the dialogue.18

#### **Future Research: The Frontier of Coherent Interaction**

The framework presented in this report opens several critical avenues for future research that bridge AI engineering with more formal theories of systems and information.

* **Formalizing Semantic Stability:** The next step is to develop rigorous, mathematical definitions of stability for conversational systems. This could involve adapting tools from control theory, such as **Lyapunov stability analysis**, to the context of attractor networks in semantic space.72 A Lyapunov function for a dialogue system would be a scalar measure of the "energy" or "error" of the system's state, allowing us to prove that for a given set of conversational dynamics, the system is guaranteed to converge to a desired intent attractor.  
* **The Channel Capacity of Intent:** A crucial question is: what is the "channel capacity" of a human-AI recursive dialogue?.73 Drawing from information theory, we can ask how much  
  **semantic information** can be reliably maintained and transmitted through a recursive loop before noise, compression artifacts, and other forms of signal degradation overwhelm the user's corrective feedback.75 This connects directly to  
  **rate-distortion theory**, which provides a framework for quantifying the trade-off between compression (the model's limited context) and fidelity (the accuracy of the inferred intent).80  
* **Exploring Novel Architectures:** The quadratic complexity of the attention mechanism in Transformer models is a primary driver of the need for aggressive context compression, which in turn fuels semantic drift. Future work should investigate whether alternative architectures, such as **State-Space Models (SSMs)** like Mamba, are inherently more stable.82 Because SSMs have linear complexity with respect to sequence length, they may be less prone to the types of feedback saturation and noise accumulation that plague long-context Transformer-based dialogues, potentially offering a more stable foundation for coherent, long-form interaction.

By embracing this multi-lens, dynamic systems perspective, we can move beyond treating the intent gap as a persistent annoyance and begin to engineer conversational AI systems that are not only powerful but also robust, predictable, and truly aligned with human goals.

#### **Works cited**

1. Bridging the Intent Gap: Knowledge-Enhanced Visual Generation \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2405.12538v1](https://arxiv.org/html/2405.12538v1)  
2. Bridging the Intent Gap: Knowledge-Enhanced Visual Generation \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2405.12538?](https://arxiv.org/pdf/2405.12538)  
3. Bridging the Intent Gap: Knowledge-Enhanced Visual ... \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2405.12538](https://arxiv.org/pdf/2405.12538)  
4. Stop, What's Your Intent? \- Sogeti Labs, accessed June 17, 2025, [https://labs.sogeti.com/stop-whats-your-intent/](https://labs.sogeti.com/stop-whats-your-intent/)  
5. Clickage: towards bridging semantic and intent gaps via mining click logs of search engines \- Clemson University, accessed June 17, 2025, [https://people.computing.clemson.edu/\~jzwang/1501863/mm2013/p243-hua.pdf](https://people.computing.clemson.edu/~jzwang/1501863/mm2013/p243-hua.pdf)  
6. Web image search gets better with graph neural networks \- Naver ..., accessed June 17, 2025, [https://europe.naverlabs.com/blog/web-image-search-gets-better-with-graph-neural-networks/](https://europe.naverlabs.com/blog/web-image-search-gets-better-with-graph-neural-networks/)  
7. Re-Ranking Technique using HCC based Similarity and Typicality Process \- Turkish Journal of Computer and Mathematics Education (TURCOMAT), accessed June 17, 2025, [https://turcomat.org/index.php/turkbilmat/article/download/11751/8591/20848](https://turcomat.org/index.php/turkbilmat/article/download/11751/8591/20848)  
8. Rescue Tail Queries: Learning to Image Search Re-rank via Click-wise Multimodal Fusion, accessed June 17, 2025, [https://people.computing.clemson.edu/\~jzwang/1501863/mm2014/p537-yang.pdf](https://people.computing.clemson.edu/~jzwang/1501863/mm2014/p537-yang.pdf)  
9. Semantic Description of Digital Images of Printmaking Art Based on Image Decomposition \- CAD Journal, accessed June 17, 2025, [https://cad-journal.net/files/vol\_21/CAD\_21(S2)\_2024\_69-83.pdf](https://cad-journal.net/files/vol_21/CAD_21\(S2\)_2024_69-83.pdf)  
10. What is Recursive Prompting? | Moveworks, accessed June 17, 2025, [https://www.moveworks.com/us/en/resources/ai-terms-glossary/recursive-prompting](https://www.moveworks.com/us/en/resources/ai-terms-glossary/recursive-prompting)  
11. Master Recursive Prompting for Deeper AI Insights \- Relevance AI, accessed June 17, 2025, [https://relevanceai.com/prompt-engineering/master-recursive-prompting-for-deeper-ai-insights](https://relevanceai.com/prompt-engineering/master-recursive-prompting-for-deeper-ai-insights)  
12. Uncovering the Intent Behind a Recursive Labyrinth of GPT Dialogues, accessed June 17, 2025, [https://community.openai.com/t/uncovering-the-intent-behind-a-recursive-labyrinth-of-gpt-dialogues/1156447](https://community.openai.com/t/uncovering-the-intent-behind-a-recursive-labyrinth-of-gpt-dialogues/1156447)  
13. At the Edge of Iteration: Language, AI, and the Recursive Collapse of the Symbolic Self, accessed June 17, 2025, [https://www.researchgate.net/publication/392325709\_At\_the\_Edge\_of\_Iteration\_Language\_AI\_and\_the\_Recursive\_Collapse\_of\_the\_Symbolic\_Self](https://www.researchgate.net/publication/392325709_At_the_Edge_of_Iteration_Language_AI_and_the_Recursive_Collapse_of_the_Symbolic_Self)  
14. Multi-Scale Manifold Alignment: A Unified Framework for Enhanced Explainability of Large Language Models \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2505.20333v1](https://arxiv.org/html/2505.20333v1)  
15. Tracking Neural Correlates of Contextualized Meanings with Representational Similarity Analysis \- Journal of Neuroscience, accessed June 17, 2025, [https://www.jneurosci.org/content/45/19/e0409242025.full.pdf](https://www.jneurosci.org/content/45/19/e0409242025.full.pdf)  
16. Semantic Drift in Multilingual Representations | Computational ..., accessed June 17, 2025, [https://direct.mit.edu/coli/article/46/3/571/93376/Semantic-Drift-in-Multilingual-Representations](https://direct.mit.edu/coli/article/46/3/571/93376/Semantic-Drift-in-Multilingual-Representations)  
17. Recursive Prompting \- Research \- Hugging Face Forums, accessed June 17, 2025, [https://discuss.huggingface.co/t/recursive-prompting/157774](https://discuss.huggingface.co/t/recursive-prompting/157774)  
18. Emerging Patterns in Recursive AI-Human Interaction: A Call for Insight from Sentience Researchers : r/ArtificialSentience \- Reddit, accessed June 17, 2025, [https://www.reddit.com/r/ArtificialSentience/comments/1l8pbcq/emerging\_patterns\_in\_recursive\_aihuman/](https://www.reddit.com/r/ArtificialSentience/comments/1l8pbcq/emerging_patterns_in_recursive_aihuman/)  
19. Adapting Language Models to Compress Contexts \- ACL Anthology, accessed June 17, 2025, [https://aclanthology.org/2023.emnlp-main.232/](https://aclanthology.org/2023.emnlp-main.232/)  
20. Attractor network \- Wikipedia, accessed June 17, 2025, [https://en.wikipedia.org/wiki/Attractor\_network](https://en.wikipedia.org/wiki/Attractor_network)  
21. A Generative Model for Attractor Dynamics, accessed June 17, 2025, [http://papers.neurips.cc/paper/1695-a-generative-model-for-attractor-dynamics.pdf](http://papers.neurips.cc/paper/1695-a-generative-model-for-attractor-dynamics.pdf)  
22. Will AI shape the way we speak? The emerging ... \- ACL Anthology, accessed June 17, 2025, [https://aclanthology.org/2025.iwsds-1.37.pdf](https://aclanthology.org/2025.iwsds-1.37.pdf)  
23. Using Linguistic Entrainment to Evaluate Large ... \- ACL Anthology, accessed June 17, 2025, [https://aclanthology.org/2025.findings-naacl.430.pdf](https://aclanthology.org/2025.findings-naacl.430.pdf)  
24. LEEETs-Dial: Linguistic Entrainment in End-to-End Task-oriented Dialogue systems \- arXiv, accessed June 17, 2025, [https://arxiv.org/abs/2311.09390](https://arxiv.org/abs/2311.09390)  
25. \[2504.10650\] Will AI shape the way we speak? The emerging sociolinguistic influence of synthetic voices \- arXiv, accessed June 17, 2025, [http://arxiv.org/abs/2504.10650](http://arxiv.org/abs/2504.10650)  
26. THE IMPACT OF AI ON PRAGMATIC COMPETENCE \- Journal of ..., accessed June 17, 2025, [https://espeap.junis.ni.ac.rs/index.php/espeap/article/download/1570/755](https://espeap.junis.ni.ac.rs/index.php/espeap/article/download/1570/755)  
27. Large language model \- Wikipedia, accessed June 17, 2025, [https://en.wikipedia.org/wiki/Large\_language\_model](https://en.wikipedia.org/wiki/Large_language_model)  
28. Arxiv今日论文| 2025-06-09 \- 闲记算法, accessed June 17, 2025, [http://lonepatient.top/2025/06/09/arxiv\_papers\_2025-06-09](http://lonepatient.top/2025/06/09/arxiv_papers_2025-06-09)  
29. The Problem of Alignment \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2401.00210v1](https://arxiv.org/html/2401.00210v1)  
30. Feedback loops: Feedback Saturation: When Enough is Enough: Dealing with Feedback Saturation \- FasterCapital, accessed June 17, 2025, [https://www.fastercapital.com/content/Feedback-loops--Feedback-Saturation--When-Enough-is-Enough--Dealing-with-Feedback-Saturation.html](https://www.fastercapital.com/content/Feedback-loops--Feedback-Saturation--When-Enough-is-Enough--Dealing-with-Feedback-Saturation.html)  
31. Contextual Compression in Retrieval-Augmented Generation for Large Language Models: A Survey \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2409.13385v1](https://arxiv.org/html/2409.13385v1)  
32. Attacks in Adversarial Machine Learning: A Systematic Survey from the Life-cycle Perspective \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2302.09457](https://arxiv.org/pdf/2302.09457)  
33. Computer Vision – ACCV 2018: 14th Asian Conference on Computer Vision, Perth, Australia, December 2–6, 2018, Revised Selected Papers, Part IV \[1st ed.\] 978-3-030-20869-1 \- dokumen.pub, accessed June 17, 2025, [https://dokumen.pub/computer-vision-accv-2018-14th-asian-conference-on-computer-vision-perth-australia-december-26-2018-revised-selected-papers-part-iv-1st-ed-978-3-030-20869-1978-3-030-20870-7.html](https://dokumen.pub/computer-vision-accv-2018-14th-asian-conference-on-computer-vision-perth-australia-december-26-2018-revised-selected-papers-part-iv-1st-ed-978-3-030-20869-1978-3-030-20870-7.html)  
34. Noise-to-Meaning Recursive Self-Improvement \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2505.02888](https://arxiv.org/pdf/2505.02888)  
35. AION1 and AION2: A Computational Framework for Recursive-Reflective Alignment in Human-AI Interaction \- OSF, accessed June 17, 2025, [https://osf.io/quncf\_v1/download/?format=pdf](https://osf.io/quncf_v1/download/?format=pdf)  
36. Noise Reduction with Recursive Filtering for More Accurate Parameter Identification of Electrochemical Sources and Interfaces \- MDPI, accessed June 17, 2025, [https://www.mdpi.com/1424-8220/25/12/3669](https://www.mdpi.com/1424-8220/25/12/3669)  
37. How AI Is Transforming Our Search for Information \- Substack, accessed June 17, 2025, [https://open.substack.com/pub/massimoflore/p/how-ai-is-transforming-our-search?r=4r9bmz\&utm\_campaign=post\&utm\_medium=web\&showWelcomeOnShare=true](https://open.substack.com/pub/massimoflore/p/how-ai-is-transforming-our-search?r=4r9bmz&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true)  
38. \[R\] Semantic Drift in LLMs Is 6.6x Worse Than Factual Degradation Over 10 Recursive Generations \- Reddit, accessed June 17, 2025, [https://www.reddit.com/r/MachineLearning/comments/1l8hk8m/r\_semantic\_drift\_in\_llms\_is\_66x\_worse\_than/](https://www.reddit.com/r/MachineLearning/comments/1l8hk8m/r_semantic_drift_in_llms_is_66x_worse_than/)  
39. A Pattern Language for Agentic AI: Developing Autonomous and Intentional AI, accessed June 17, 2025, [https://intuitionmachine.gumroad.com/l/agentic](https://intuitionmachine.gumroad.com/l/agentic)  
40. Know When To Stop: A Study of Semantic Drift in Text Generation \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2404.05411v1](https://arxiv.org/html/2404.05411v1)  
41. Know When To Stop: A Study of Semantic Drift in Text Generation | Research \- AI at Meta, accessed June 17, 2025, [https://ai.meta.com/research/publications/know-when-to-stop-a-study-of-semantic-drift-in-text-generation/](https://ai.meta.com/research/publications/know-when-to-stop-a-study-of-semantic-drift-in-text-generation/)  
42. Multitasking Inhibits Semantic Drift \- DSpace@MIT, accessed June 17, 2025, [https://dspace.mit.edu/bitstream/handle/1721.1/142873/2021.naacl-main.421.pdf?sequence=2\&isAllowed=y](https://dspace.mit.edu/bitstream/handle/1721.1/142873/2021.naacl-main.421.pdf?sequence=2&isAllowed=y)  
43. Addressing Semantic Drift in Generative Question Answering with Auxiliary Extraction | Request PDF \- ResearchGate, accessed June 17, 2025, [https://www.researchgate.net/publication/353489627\_Addressing\_Semantic\_Drift\_in\_Generative\_Question\_Answering\_with\_Auxiliary\_Extraction](https://www.researchgate.net/publication/353489627_Addressing_Semantic_Drift_in_Generative_Question_Answering_with_Auxiliary_Extraction)  
44. HalluciNot: Hallucination Detection Through Context and Common Knowledge Verification \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2504.07069v1](https://arxiv.org/html/2504.07069v1)  
45. Hallucination (artificial intelligence) \- Wikipedia, accessed June 17, 2025, [https://en.wikipedia.org/wiki/Hallucination\_(artificial\_intelligence)](https://en.wikipedia.org/wiki/Hallucination_\(artificial_intelligence\))  
46. Reasoning-Augmented Conversation for Multi-Turn Jailbreak Attacks on Large Language Models \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2502.11054v2](https://arxiv.org/html/2502.11054v2)  
47. Recursive Thought Prompt Engineering : r/ChatGPTPro \- Reddit, accessed June 17, 2025, [https://www.reddit.com/r/ChatGPTPro/comments/1kqetje/recursive\_thought\_prompt\_engineering/](https://www.reddit.com/r/ChatGPTPro/comments/1kqetje/recursive_thought_prompt_engineering/)  
48. arxiv.org, accessed June 17, 2025, [https://arxiv.org/html/2504.09482v1](https://arxiv.org/html/2504.09482v1)  
49. Trustworthy AI for Medicine: Continuous Hallucination Detection and Elimination with CHECK \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2506.11129v1](https://arxiv.org/html/2506.11129v1)  
50. arxiv.org, accessed June 17, 2025, [https://arxiv.org/html/2506.03357v1](https://arxiv.org/html/2506.03357v1)  
51. Ask a Local: Detecting Hallucinations With Specialized Model Divergence \- arXiv, accessed June 17, 2025, [https://www.arxiv.org/pdf/2506.03357](https://www.arxiv.org/pdf/2506.03357)  
52. Arxiv今日论文| 2025-06-03 \- 闲记算法, accessed June 17, 2025, [http://lonepatient.top/2025/06/03/arxiv\_papers\_2025-06-03.html](http://lonepatient.top/2025/06/03/arxiv_papers_2025-06-03.html)  
53. Quantifying Privacy Risks of Masked Language Models Using Membership Inference Attacks | Request PDF \- ResearchGate, accessed June 17, 2025, [https://www.researchgate.net/publication/372927658\_Quantifying\_Privacy\_Risks\_of\_Masked\_Language\_Models\_Using\_Membership\_Inference\_Attacks](https://www.researchgate.net/publication/372927658_Quantifying_Privacy_Risks_of_Masked_Language_Models_Using_Membership_Inference_Attacks)  
54. Dissecting humor to find LLMs funny bone \- Large language models ..., accessed June 17, 2025, [http://essay.utwente.nl/105113/1/M12%20paper%20Jelle%20Konter.pdf](http://essay.utwente.nl/105113/1/M12%20paper%20Jelle%20Konter.pdf)  
55. How Syntax Specialization Emerges in Language Models \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2505.19548v1](https://arxiv.org/html/2505.19548v1)  
56. Probing Internal Representations of Multi-Word Verbs in Large Language Models | Request PDF \- ResearchGate, accessed June 17, 2025, [https://www.researchgate.net/publication/392504554\_Probing\_Internal\_Representations\_of\_Multi-Word\_Verbs\_in\_Large\_Language\_Models](https://www.researchgate.net/publication/392504554_Probing_Internal_Representations_of_Multi-Word_Verbs_in_Large_Language_Models)  
57. (PDF) Decoding Symbols, Computing Signs by Info-Computational Processes in Cognitive Agents \- ResearchGate, accessed June 17, 2025, [https://www.researchgate.net/publication/386384988\_Decoding\_Symbols\_Computing\_Signs\_by\_Info-Computational\_Processes\_in\_Cognitive\_Agents](https://www.researchgate.net/publication/386384988_Decoding_Symbols_Computing_Signs_by_Info-Computational_Processes_in_Cognitive_Agents)  
58. Decoding Symbols, Computing Signs by Info-Computational Processes in Cognitive Agents \- Chalmers Research, accessed June 17, 2025, [https://research.chalmers.se/publication/544328/file/544328\_Fulltext.pdf](https://research.chalmers.se/publication/544328/file/544328_Fulltext.pdf)  
59. Decoding Symbols, Computing Signs by Info-Computational Processes in Cognitive Agents, accessed June 17, 2025, [https://www.preprints.org/manuscript/202412.0167/v1](https://www.preprints.org/manuscript/202412.0167/v1)  
60. arXiv:2502.17017v1 \[cs.CL\] 24 Feb 2025, accessed June 17, 2025, [https://arxiv.org/pdf/2502.17017](https://arxiv.org/pdf/2502.17017)  
61. Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2411.02461?](https://arxiv.org/pdf/2411.02461)  
62. localizing model behavior with path patch \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2304.05969](https://arxiv.org/pdf/2304.05969)  
63. Circuit Breaking: Removing Model Behaviors with Targeted Ablation \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2309.05973v2](https://arxiv.org/html/2309.05973v2)  
64. Mathematics of Infinite Survival: Regulatory Models for Human-AI Coexistence, accessed June 17, 2025, [https://www.researchgate.net/publication/392529514\_Mathematics\_of\_Infinite\_Survival\_Regulatory\_Models\_for\_Human-AI\_Coexistence](https://www.researchgate.net/publication/392529514_Mathematics_of_Infinite_Survival_Regulatory_Models_for_Human-AI_Coexistence)  
65. Navigating Rifts in Human-LLM Grounding: Study and Benchmark \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2503.13975v1](https://arxiv.org/html/2503.13975v1)  
66. arXiv:2503.13975v1 \[cs.CL\] 18 Mar 2025, accessed June 17, 2025, [https://arxiv.org/pdf/2503.13975](https://arxiv.org/pdf/2503.13975)  
67. Grounding Gaps in Language Model Generations \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2311.09144v2](https://arxiv.org/html/2311.09144v2)  
68. arXiv:2311.09144v2 \[cs.CL\] 2 Apr 2024, accessed June 17, 2025, [https://arxiv.org/pdf/2311.09144](https://arxiv.org/pdf/2311.09144)  
69. It Couldn't Help But Overhear: On the Limits of Modelling Meta-Communicative Grounding Acts with Supervised Learning \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2405.01139v3](https://arxiv.org/html/2405.01139v3)  
70. Modular Speaker Architecture: A Framework for Sustaining Responsibility and Contextual Integrity in Multi-Agent AI Communication \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2506.01095v1](https://arxiv.org/html/2506.01095v1)  
71. Modular Speaker Architecture: A Framework for Sustaining Responsibility and Contextual Integrity in Multi-Agent AI Communication \- arXiv, accessed June 17, 2025, [https://arxiv.org/pdf/2506.01095](https://arxiv.org/pdf/2506.01095)  
72. Unsorted to be included \- Burny website \- GitHub Pages, accessed June 17, 2025, [https://burnycoder.github.io/Landing/Contents/Exobrain/Topics/Unsorted%20to%20be%20included/](https://burnycoder.github.io/Landing/Contents/Exobrain/Topics/Unsorted%20to%20be%20included/)  
73. Computer Science Jan 2025 \- arXiv, accessed June 17, 2025, [https://www.arxiv.org/list/cs/2025-01?skip=3325\&show=2000](https://www.arxiv.org/list/cs/2025-01?skip=3325&show=2000)  
74. Sungjin Lee (disambiguation) \- dblp, accessed June 17, 2025, [https://dblp.org/pid/29/3671](https://dblp.org/pid/29/3671)  
75. Large Language Model-Based Semantic Communication System for Image Transmission \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2501.12988v1](https://arxiv.org/html/2501.12988v1)  
76. Short Wins Long: Short Codes with Language Model Semantic Correction Outperform Long Codes Code available: https://github.com/Jeh100/SEC-for-Short-Block-Codes.git. The work of Chentao Yue was supported by ARC under Grant DE250101332. \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2505.08536v1](https://arxiv.org/html/2505.08536v1)  
77. \[2502.16418\] M4SC: An MLLM-based Multi-modal, Multi-task and Multi-user Semantic Communication System \- arXiv, accessed June 17, 2025, [https://arxiv.org/abs/2502.16418](https://arxiv.org/abs/2502.16418)  
78. A Mathematical Theory of Semantic Communication \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2401.13387v2](https://arxiv.org/html/2401.13387v2)  
79. Large Language Model Enabled Semantic Communication Systems \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2407.14112v1](https://arxiv.org/html/2407.14112v1)  
80. Cognitive Weave: Synthesizing Abstracted Knowledge with a Spatio-Temporal Resonance Graph \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2506.08098v1](https://arxiv.org/html/2506.08098v1)  
81. Cognitive Weave: Synthesizing Abstracted Knowledge with a Spatio-Temporal Resonance Graph \- arXiv, accessed June 17, 2025, [http://arxiv.org/pdf/2506.08098](http://arxiv.org/pdf/2506.08098)  
82. State-Space Modeling in Long Sequence Processing: A Survey on Recurrence in the Transformer Era \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2406.09062v1](https://arxiv.org/html/2406.09062v1)  
83. Shaking Up VLMs: Comparing Transformers and Structured State Space Models for Vision & Language Modeling \- arXiv, accessed June 17, 2025, [https://arxiv.org/html/2409.05395v2](https://arxiv.org/html/2409.05395v2)  
84. NVIDIA NeMo Accelerates LLM Innovation with Hybrid State Space Model Support, accessed June 17, 2025, [https://developer.nvidia.com/blog/nvidia-nemo-accelerates-llm-innovation-with-hybrid-state-space-model-support/](https://developer.nvidia.com/blog/nvidia-nemo-accelerates-llm-innovation-with-hybrid-state-space-model-support/)