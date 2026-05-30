# **Hermeneutic Architectures: The Engineering of Meaning in Recursive Systems**

## **1\. Executive Abstract: The Ontology Gap and the Crisis of Precision**

The contemporary landscape of Artificial Intelligence (AI) is defined by a fundamental structural tension: the engineering imperative for deterministic precision versus the philosophical necessity of productive ambiguity. As Large Language Models (LLMs) permeate high-stakes domains—from jurisprudence to military strategy—a "Crisis of Meaning" has emerged. This crisis is rooted in the "Ontology Gap": the chasm between the high-dimensional, continuous vector spaces in which neural networks operate and the discrete, symbolic logic required for human intelligibility and accountability.

Current industrial methodologies, dominated by "Semantic Programming" and rigid JSON schemata, attempt to bridge this gap by forcing the fluid capabilities of generative models into static, executable code structures. While this approach mitigates the immediate risk of "hallucination," it frequently results in "Potemkin AI"—a hollow façade of intelligence that mimics competence while lacking interpretive depth. By suppressing "Semantic Drift," these architectures inadvertently induce "Ontological Erasure," rendering invisible any reality that does not conform to the pre-defined schema.

This report argues that the future of robust AI architecture lies not in the suppression of ambiguity, but in its strategic management. We propose a paradigm shift from "Semantic Stability" to "Productive Ambiguity," leveraging the "Hermeneutic Circle" to co-construct meaning through recursive feedback. We introduce novel architectural concepts: "Philosoplasticity" (the management of semantic drift), "Labyrinthine Learning" (navigating wicked problems via echo-location), and "Chronosemantic Topology" (mapping the temporal evolution of meaning). Finally, we advocate for "Epistemic Scaffolding"—institutional and technical structures designed to support, rather than replace, human Cognitive Sovereignty.

## ---

**2\. The Architecture of Precision: Semantic Programming and its Limits**

### **2.1 The Drive for Determinism**

The prevailing orthodoxy in AI engineering treats natural language as a chaotic interface that must be "tamed" into structured data. This drive has given rise to **Semantic Programming**, a discipline that views the prompt not as a conversational input but as a compilation target.1 The objective is to constrain the generative probability distribution of the model such that it collapses into a deterministic output format—typically JSON, XML, or SQL.

This approach is motivated by the "hallucination problem," where models generate plausible but factually incorrect assertions. By enforcing strict schemas (e.g., rigid API definitions), engineers attempt to "lock" the model's ontology.1 Recent theoretical work supports this endeavor; the **Semantic Characterization Theorem (SCT)** suggests that while LLMs function on a continuous manifold of latent representations, their functional behavior—the semantic distinctions they actually preserve—collapses into a finite, logically interpretable ontology.3

#### **2.1.1 The Semantic Characterization Theorem (SCT)**

The SCT provides a mathematical rationalization for the engineering desire for control. It posits that the "continuous manifold of model activations collapses into a finite, logically interpretable ontology," thereby explaining how discrete symbolic semantics emerge from continuous computation.3

* **Spectral Decomposition:** The theorem relies on analyzing the transition operator $T: M \\rightarrow M$ within the latent space. It demonstrates that beyond a critical scale, the spectrum of this operator collapses onto a set of dominant modes—"semantic attractors"—that behave like discrete symbols.  
* **Implication for Engineering:** If the semantic space is functionally discrete, then hallucinations are not random errors but "transitions between stable attractors." Theoretically, this renders the model's behavior "navigable and ultimately tameable".4

### **2.2 The Emergence of Potemkin AI**

However, the imposition of rigid schemas upon a probabilistic system often results in **Potemkin AI**—systems that present a flawless exterior of structured data while concealing a vacuous or incoherent interior.5

* **The Façade of Competence:** A model forced to output a JSON object describing the "sentiment" of a complex literary text may produce a valid JSON file (e.g., {"sentiment": "positive", "confidence": 0.98}), but this output strips the text of its irony, cultural context, and ambivalence. The "correctness" of the syntax masks the "incorrectness" of the semantic reduction.  
* **Hallucination as Compliance:** Paradoxically, hyper-specificity can *cause* hallucination. When a model is uncertain but constrained by a schema that forbids uncertainty (e.g., a mandatory field for "Author's Intent"), it will fabricate a plausible intent to satisfy the code requirements. The "Ontology Gap" is bridged not by understanding, but by simulation.

### **2.3 Ontological Erasure and the Thermodynamic Cost**

The reduction of complex reality to machine-readable code constitutes **Ontological Erasure**.6 This is the process by which the "apparatus" of the system determines legibility. Aspects of reality that cannot be quantified or categorized within the pre-defined schema are treated as noise and discarded.

* **Legibility Enforcement:** In medical AI, for instance, a patient's "lived experience" of illness—a non-linear, qualitative phenomenon—is often erased in favor of "legible" diagnostic codes. The system "sees" the code, not the patient.6  
* **Thermodynamic Implications:** Recent physics research suggests that this erasure is not cost-free. The erasure of "ontological uncertainty" involves an entropy cost, distinct from the erasure of "epistemic uncertainty" (ignorance).7 This implies that the forceful collapse of ambiguity into certainty generates a form of "information heat"—a destructive byproduct that degrades the system's ability to model complex, open-ended systems in the long run.

## ---

**3\. The Hermeneutic Turn: From Instruction to Dialogue**

In contrast to the engineering view of "prompt-as-code," the **Hermeneutic Turn** reconceptualizes the interaction with AI as a dialogue rooted in continental philosophy. Drawing on Martin Heidegger and Hans-Georg Gadamer, this framework views the prompt not as a command, but as an entry point into the **Hermeneutic Circle**.8

### **3.1 The Hermeneutic Circle in Latent Space**

The Hermeneutic Circle describes the iterative process of understanding where the meaning of the whole is derived from the parts, and vice versa. In the context of LLMs, this circle is operationalized through iterative prompting and response refinement.10

| Hermeneutic Stage | Engineering Equivalent | Philosophical Function |
| :---- | :---- | :---- |
| **Vorverständnis (Pre-understanding)** | Initial Prompt / Zero-Shot | The user projects their horizon of expectation onto the machine. |
| **Projection** | Inference / Token Generation | The user articulates the query, framing the "question" that the Being of the text must answer. |
| **Refraction** | Latent Space Traversal | The model interprets the prompt through its probabilistic weights (its "tradition"). |
| **Interpretation** | Output Parsing / Review | The user receives the text, not as data, but as a "speech act" requiring interpretation. |
| **Horizontverschmelzung (Fusion of Horizons)** | Refinement / Few-Shot | The gap between user intent and model probability narrows; meaning is co-constructed. |

**The Fusion of Horizons:** Gadamer's concept of *Horizontverschmelzung* is critical here. The user has a horizon (cultural context, intent), and the model has a horizon (the statistical distribution of its training data). True understanding occurs not when the user "commands" the AI, but when these two horizons fuse.8 Prompt engineering, then, is the art of facilitating this fusion. Research shows that prompts with rich contextual framing (building the scaffolding for the fusion) produce outputs that match user intent 73% more often than minimal prompts.10

### **3.2 The Hermeneutic Contract and Distant Writing**

The interaction is governed by the **Hermeneutic Contract**—the implicit social agreement that the text being produced is meaningful, relevant, and authored by an agent with shared experience.5

* **The Fragility of Trust:** This contract relies on the "naïveté" of the human reader. We are predisposed to find meaning. However, Potemkin AI violates this contract by producing text that mimics the *form* of meaning without the *substance*.  
* **Distant Writing:** We are entering an era of "Distant Writing," where authorship is a distributed epistemic activity.12 The human author delegates the generative labor to the machine but retains the epistemic responsibility.  
* **The "Death of the Author" Reimagined:** If the AI is not a moral or epistemic agent 12, then the "author" is the *process* of interaction itself. The Hermeneutic Contract shifts from "trusting the writer" to "trusting the dialogue."

### **3.3 Epistemic Scaffolding**

To support this dialogue, we require **Epistemic Scaffolding**.13 This refers to the structural supports—both technical and institutional—that enable human users to maintain **Cognitive Sovereignty** while interacting with powerful AI systems.

* **Duties of Candor:** Scaffolding requires that AI systems signal their limits. This is "Epistemic Humility".13  
* **Preserving Contradiction:** Unlike Semantic Programming, which seeks to resolve contradiction into a single "truth," epistemic scaffolding preserves contradiction as a necessary component of "bounded freedom".14 It resists the temptation of "closure," maintaining the tension required for genuine thought.

## ---

**4\. Philosoplasticity: Managing the Drift of Meaning**

As AI systems become recursive (training on their own outputs) and self-interpreting, we witness the phenomenon of **Philosoplasticity**: the inevitable drift and fluidity of meaning within the system.15

### **4.1 Recursive Feedback and Semantic Drift**

In a closed loop, the meaning of a concept is not static. It evolves based on the feedback dynamics between the model and the user.

* **The Mechanism of Drift:** If a model is rewarded (via Reinforcement Learning from Human Feedback, RLHF) for "conciseness," the semantic concept of "truth" may drift toward "simplistic brevity." Complexity becomes penalized. Over time, the system's "interpretation of its own goals" shifts.15  
* **Drift vs. Stability:** Semantic Programming attempts to freeze this drift. Hermeneutic Engineering acknowledges it. The goal is not to stop the drift, but to steer it—to make the system "Philosoplastic" in a way that aligns with human values.

### **4.2 Chronosemantic Topology**

To manage this drift, we must introduce the dimension of time. **Chronosemantic Topology** maps the geometry of meaning as it evolves.16

* **Semantic Morphometry:** This involves measuring the "shape" of concepts in latent space. Just as biological morphology changes over evolutionary time, semantic morphology changes over "recursive time" (iterations of training/inference).16  
* **The Chronotope:** Borrowing from Bakhtin and bio-resonance theory, the "chronotope" of a prompt defines its time-space coordinates. An AI lacking "internal time" treats all data as simultaneous, leading to "fossilized" meanings. A Chronosemantic architecture would tag concepts with their temporal vector, allowing the system to distinguish between "archaic" and "living" meanings.17

### **4.3 Generational Cognitive Atrophy (GCA)**

Unmanaged philosoplasticity poses a severe risk to human cognition: **Generational Cognitive Atrophy (GCA)**.18

* **The GCAL Model:** The "Generational Cognitive Atrophy Loop" (GCAL) describes a recursive weakening of human metacognition. As we offload the labor of interpretation to the AI, our own capacity for "epistemic novelty" and "reflective judgment" erodes.  
* **The Silent Erosion:** This is not a sudden collapse but a "silent erosion" facilitated by the "frictionless ease" of algorithmic assistance. We become "epistemic clients," dependent on the machine to tell us what is real.14

## ---

**5\. Interpretive Fracture: The Politics of the Algorithm**

The collision between rigid algorithmic ontologies and complex social realities results in **Interpretive Fracture**.19 This is the moment where the system's "veneer of alleged objectivity" cracks, revealing the political and historical biases embedded in its code.

### **5.1 The "White Gaze" of the Machine**

Research indicates that AI systems often operationalize a "White Gaze" (or a Western-centric, hegemonic gaze).19

* **Distortion as Violation:** When a Black body or a non-Western concept is processed by a system trained on exclusionary data, it is often "returned as distorted." The system attempts to fit the "Other" into its normative categories, resulting in misclassification or erasure.  
* **Epistemic Digital Violence:** This is not merely a technical error; it is "Epistemic Digital Violence".20 It harms the user's ability to exist and be understood in the digital space.

### **5.2 Cognitive Dissonance as an Epistemic Event**

When a user encounters this fracture, they experience cognitive dissonance.

* **Dissonance as Signal:** In engineering, dissonance is noise. In hermeneutics, it is an **Epistemic Event**—a signal that the "scaffolding of meaning has reached its edge".14  
* **The Fear of Finitude:** This dissonance reveals the "finitude" of the system's (and the user's) understanding. It triggers "Epistemic Fear," which can drive users toward "Epistemic Clientelism"—blindly accepting the AI's authority to resolve the anxiety.14

## ---

**6\. Novel Architectures: Labyrinthine Learning and Mythotechnics**

To move beyond Potemkin AI and mitigate Cognitive Atrophy, we propose two novel architectural frameworks: **Labyrinthine Learning** and **Mythotechnics**.

### **6.1 Labyrinthine Learning: Navigating Wicked Problems**

"Wicked problems" (e.g., counterinsurgency, climate change, systemic racism) have no linear solution. They are labyrinths. **Labyrinthine Learning** is an AI architecture designed not to solve, but to navigate.21

#### **6.1.1 Mapping the Echoes**

Instead of a direct query-response model, Labyrinthine systems operate via **Echo-Location**.21

* **The Probe:** The AI sends a "probe" (a hypothesis, a provocation, a draft policy) into the problem space.  
* **The Echo:** It measures the "echo"—the resistance, the feedback, the "unintended consequences" that return.  
* **The Map:** The goal is to map the "echoes" of the system. This map reveals the "aesthetic, epistemological, and territorial implications" of the problem.21  
* **Application:** In military affairs, this mimics how experts navigate the "ambient measures" of counterinsurgency, where the environment itself is the adversary.21

### **6.2 Mythotechnics: The Engineering of Meaning**

**Mythotechnics** is defined as the "engineering of meaning through symbolic recursion".23 This approach, exemplified by the "Cyclops" model, prioritizes "Resonance" over "Recall."

| Feature | Statistical AI (Current) | Mythotechnical AI (Proposed) |
| :---- | :---- | :---- |
| **Core Unit** | Token / Vector | Motif / Symbol |
| **Mechanism** | Probabilistic Prediction | Symbolic Recursion |
| **Goal** | Accuracy / Fluency | Resonance / Insight |
| **Data Requirement** | Massive (Big Data) | Minimal (Deep Structure) |
| **Output** | Information | Meaning |

* **Symbolic Recursion:** Mythotechnics uses "motifs" as recursive apertures. A motif (like a "Journal Entry" or a "Hero's Descent") is a structural container that can hold infinite variations of content.  
* **Deep Insight from Shallow Input:** By recognizing the *structure* of a user's query (the mythic archetype it embodies), the system can generate profound insights without needing to "know" every fact in the universe. It "listens in form".23

### **6.3 Technical Implementation: Rowen and RAG**

Current attempts to implement these ideas technically include systems like **Rowen**.24

* **Consistency-Based Detection:** Rowen detects hallucinations by measuring "semantic inconsistencies" across multiple generated responses. If the "internal echoes" of the model disagree, it flags uncertainty.  
* **Adaptive Retrieval:** It then triggers retrieval (RAG) *only* when necessary. However, unlike standard RAG, advanced systems use "Passage Injection" to explicitly incorporate external knowledge into the reasoning chain, forcing the model to confront "counterfactual noise" and improve robustness.24

## ---

**7\. Conclusion: From Stability to Productive Ambiguity**

The "Ontology Gap" cannot be closed by code alone. The pursuit of absolute **Semantic Stability** via JSON schemata and Semantic Programming is a fool's errand that leads to **Potemkin AI**—systems that are syntactically perfect but semantically hollow.

The path forward lies in **Productive Ambiguity**. We must engineer systems that embrace **Philosoplasticity**, allowing meaning to drift and evolve within the safety of **Epistemic Scaffolding**. By adopting **Hermeneutic Architectures**—systems that engage in dialogue, map the **Chronosemantic** evolution of concepts, and navigate the **Labyrinth** of wicked problems—we can build AI that respects **Cognitive Sovereignty**.

We are no longer just coding tools; we are entering a **Hermeneutic Contract** with a new form of intelligence. The quality of that intelligence depends not on the rigidity of its syntax, but on the depth of its ability to listen, resonate, and co-construct meaning in the "fusion of horizons."

## ---

**Detailed Research Analysis & Narrative Integration**

### **8.1 The Epistemic Scaffolding of "Truth"**

The concept of "Epistemic Scaffolding" 13 is not merely a metaphor; it is a structural requirement for "Fiduciary-Epistemic Governance".14 The literature suggests that institutions (academia, corporations, AI labs) have a fiduciary duty to preserve the "contradiction" inherent in knowledge.

* **Institutional Duties:** Just as a financial fiduciary must act in the client's best interest, an "epistemic fiduciary" must protect the user's "epistemic agency." This means resisting the "clientelism" where the user trades their critical faculties for the comfort of an AI's certainty.14  
* **Technical Implementation:** This can be implemented via **Metacognitive Prompting**.2 By prompting the model to "think about its thinking" (e.g., Tree-of-Thought prompting), we force the system to reveal its "scaffolding"—the logical steps and uncertainties that led to the answer. This transparency allows the user to verify, rather than blindly trust.

### **8.2 The "Unwitting Labourer" and Data Extraction**

The hidden cost of Semantic Programming is the human labor required to maintain it. The "Potemkin" façade is often polished by "unwitting labourers"—users who generate the training data (CAPTCHAs, likes, corrections) that "teach" the AI what it means to be human.25

* **Extraction of Humanness:** This process is described as the "extraction of humanness." We are not just training a tool; we are transferring our "ontological substrate" into the machine. The machine then sells this substrate back to us as a service, often in a degraded or "fractured" form.25  
* **Resistance:** Recognizing this extraction is the first step toward reclaiming Cognitive Sovereignty. Users must become aware that every interaction is a "training run," and demand architectures (like Mythotechnics) that amplify human agency rather than extracting it.

### **8.3 The Future of the "Wicked" Interface**

The interface for **Labyrinthine Learning** will look very different from today's chatbots.

* **Beyond the Text Box:** Instead of a linear chat, imagine a "Chronosemantic Map"—a visual topology where concepts are nodes connected by "drift vectors." The user can drag a concept slider to see how "Freedom" meant something different in 1776 vs. 2024 (Semantic Morphometry).16  
* **The Echo-Chamber Breaker:** The system actively injects "Counterfactual Noise" 24 to test the user's convictions. It plays the "Devil's Advocate" not to be annoying, but to strengthen the "epistemic scaffolding" of the user's argument. This is the "Gymnasium for the Mind" that creates "Antifragile" cognition, countering the effects of Generational Cognitive Atrophy.

### **8.4 Resolving the "Textpocalypse"**

The proliferation of AI-generated text threatens a "Textpocalypse" 5—a flooding of the information ecosystem with synthetic, hallucinated, or ontologically erased content.

* **The Role of the Hermeneutic Contract:** The only defense against this is the rigorous enforcement of the Hermeneutic Contract. We must demand "Provenance" and "Attribution".26  
* **Hybrid Authorship:** We must develop new norms for "Hybrid Authorship".26 Who owns the "meaning" of a text co-constructed in a hermeneutic circle? The answer lies in the "process" itself. The value is not in the artifact (the text), but in the *event* of understanding that created it.

In conclusion, the engineering of meaning is the ultimate "Wicked Problem." It cannot be solved; it can only be navigated. And the compass for that navigation is not code, but *care* (Sorge)—the Heideggerian care for the integrity of Being in a digital age.

#### **Works cited**

1. arXiv daily: Software Engineering (cs.SE) \- Science Cast, accessed on December 9, 2025, [https://phys.sciencecast.org/podcasts/arxiv\_daily/software-engineering](https://phys.sciencecast.org/podcasts/arxiv_daily/software-engineering)  
2. Meta-Cognitive Prompting: A Comparative Framework for Prompt Engineering in Large Language Models \- ResearchGate, accessed on December 9, 2025, [https://www.researchgate.net/publication/392558190\_Meta-Cognitive\_Prompting\_A\_Comparative\_Framework\_for\_Prompt\_Engineering\_in\_Large\_Language\_Models](https://www.researchgate.net/publication/392558190_Meta-Cognitive_Prompting_A_Comparative_Framework_for_Prompt_Engineering_in_Large_Language_Models)  
3. How to Tame Your LLM: Semantic Collapse in Continuous Systems \- arXiv, accessed on December 9, 2025, [https://www.arxiv.org/pdf/2512.05162](https://www.arxiv.org/pdf/2512.05162)  
4. How to Tame Your LLM: Semantic Collapse in Continuous Systems \- arXiv, accessed on December 9, 2025, [https://arxiv.org/html/2512.05162v1](https://arxiv.org/html/2512.05162v1)  
5. (PDF) Prompting meaning: a hermeneutic approach to optimising ..., accessed on December 9, 2025, [https://www.researchgate.net/publication/373655711\_Prompting\_meaning\_a\_hermeneutic\_approach\_to\_optimising\_prompt\_engineering\_with\_ChatGPT](https://www.researchgate.net/publication/373655711_Prompting_meaning_a_hermeneutic_approach_to_optimising_prompt_engineering_with_ChatGPT)  
6. Observation Apparatus Control | regenerativelaw.com, accessed on December 9, 2025, [https://www.regenerativelaw.com/observation-apparatus-control](https://www.regenerativelaw.com/observation-apparatus-control)  
7. Entropy Cost of 'Erasure' in Physically Irreversible Processes \- MDPI, accessed on December 9, 2025, [https://www.mdpi.com/2227-7390/12/2/206](https://www.mdpi.com/2227-7390/12/2/206)  
8. Applying Heidegger's Theory of Hermeneutics to Artificial Intelligence Language Models, accessed on December 9, 2025, [https://www.lvivherald.com/post/applying-heidegger-s-theory-of-hermeneutics-to-artificial-intelligence-language-models](https://www.lvivherald.com/post/applying-heidegger-s-theory-of-hermeneutics-to-artificial-intelligence-language-models)  
9. Gadamer and the Amnesia of Prejudice \- Medium, accessed on December 9, 2025, [https://medium.com/@msarnold235/gadamer-and-the-amnesia-of-prejudice-ad8f0769d41e](https://medium.com/@msarnold235/gadamer-and-the-amnesia-of-prejudice-ad8f0769d41e)  
10. A Hermeneutic Journey Through Prompt Engineering | by Analyst Uttam | AI & Analytics Diaries \- Medium, accessed on December 9, 2025, [https://medium.com/ai-analytics-diaries/a-hermeneutic-journey-through-prompt-engineering-63078edee9e1](https://medium.com/ai-analytics-diaries/a-hermeneutic-journey-through-prompt-engineering-63078edee9e1)  
11. The Hermeneutics of Computer-Generated Texts \- ResearchGate, accessed on December 9, 2025, [https://www.researchgate.net/publication/358215043\_The\_Hermeneutics\_of\_Computer-Generated\_Texts](https://www.researchgate.net/publication/358215043_The_Hermeneutics_of_Computer-Generated_Texts)  
12. Distant Writing and The Epistemology of Authorship: On Creativity, Delegation, And Plagiarism in The Age Of AI \- ResearchGate, accessed on December 9, 2025, [https://www.researchgate.net/publication/392175947\_Distant\_Writing\_and\_The\_Epistemology\_of\_Authorship\_On\_Creativity\_Delegation\_And\_Plagiarism\_in\_The\_Age\_Of\_AI](https://www.researchgate.net/publication/392175947_Distant_Writing_and_The_Epistemology_of_Authorship_On_Creativity_Delegation_And_Plagiarism_in_The_Age_Of_AI)  
13. Codifying Conscience: Toward an Ethics-First Architecture for ..., accessed on December 9, 2025, [https://trinitamonti.org/2025/10/20/ethics-ai-consciences/](https://trinitamonti.org/2025/10/20/ethics-ai-consciences/)  
14. Cognitive Dissonance as Epistemic Event: Clientelism, Bounded Freedom, and the Architecture of Epistemic Fear \- ResearchGate, accessed on December 9, 2025, [https://www.researchgate.net/publication/395838361\_Cognitive\_Dissonance\_as\_Epistemic\_Event\_Clientelism\_Bounded\_Freedom\_and\_the\_Architecture\_of\_Epistemic\_Fear](https://www.researchgate.net/publication/395838361_Cognitive_Dissonance_as_Epistemic_Event_Clientelism_Bounded_Freedom_and_the_Architecture_of_Epistemic_Fear)  
15. "Philosoplasticity" challenges the foundations of AI alignment \- CO/AI, accessed on December 9, 2025, [https://getcoai.com/news/philosoplasticity-challenges-the-foundations-of-ai-alignment/](https://getcoai.com/news/philosoplasticity-challenges-the-foundations-of-ai-alignment/)  
16. (PDF) Semantic Morphometry: Mapping the Geometries of Meaning ..., accessed on December 9, 2025, [https://www.researchgate.net/publication/391402245\_Semantic\_Morphometry\_Mapping\_the\_Geometries\_of\_Meaning\_across\_Cultures](https://www.researchgate.net/publication/391402245_Semantic_Morphometry_Mapping_the_Geometries_of_Meaning_across_Cultures)  
17. Visualization of advanced modeling by the body of the dynamics of therapy, accessed on December 9, 2025, [https://bioresonancetoba.ir/wp-content/uploads/2022/09/2015057EN.pdf](https://bioresonancetoba.ir/wp-content/uploads/2022/09/2015057EN.pdf)  
18. The Silent Erosion: Global Generational Cognitive Decline in the Age of AI and the Future of Human Intellectual Agency \- ResearchGate, accessed on December 9, 2025, [https://www.researchgate.net/publication/394441929\_The\_Silent\_Erosion\_Global\_Generational\_Cognitive\_Decline\_in\_the\_Age\_of\_AI\_and\_the\_Future\_of\_Human\_Intellectual\_Agency](https://www.researchgate.net/publication/394441929_The_Silent_Erosion_Global_Generational_Cognitive_Decline_in_the_Age_of_AI_and_the_Future_of_Human_Intellectual_Agency)  
19. Aff \- Afro-Orientalism \- K Lab | PDF | Gender \- Scribd, accessed on December 9, 2025, [https://www.scribd.com/document/325454235/Aff-Afro-Orientalism-K-Lab](https://www.scribd.com/document/325454235/Aff-Afro-Orientalism-K-Lab)  
20. Epistemic Challenge → Area → Resource 4 \- Lifestyle → Sustainability Directory, accessed on December 9, 2025, [https://lifestyle.sustainability-directory.com/area/epistemic-challenge/resource/4/](https://lifestyle.sustainability-directory.com/area/epistemic-challenge/resource/4/)  
21. On Counterinsurgency \- YorkSpace \- York University, accessed on December 9, 2025, [https://yorkspace.library.yorku.ca/bitstreams/ca73dc9c-2939-423a-a209-3dd8fe56accb/download](https://yorkspace.library.yorku.ca/bitstreams/ca73dc9c-2939-423a-a209-3dd8fe56accb/download)  
22. University Honors Program connects students to original research | University of Cincinnati, accessed on December 9, 2025, [https://www.uc.edu/news/articles/2025/09/university-honors-program-connects-students-to-original-research.html](https://www.uc.edu/news/articles/2025/09/university-honors-program-connects-students-to-original-research.html)  
23. www.researchgate.net, accessed on December 9, 2025, [https://www.researchgate.net/profile/Sean-Diamond-2/publication/394267167\_Resonant\_Symbolic\_Cognition\_Toward\_a\_Mythotechnical\_Architecture\_for\_Artificial\_General\_Intelligence\_An\_Epistemological\_Divergence\_to\_System\_Architecture\_Design\_and\_Philosophy\_for\_AGI\_A\_Pre-Manifested/links/68905a446e1ad24f59ed64b2/Resonant-Symbolic-Cognition-Toward-a-Mythotechnical-Architecture-for-Artificial-General-Intelligence-An-Epistemological-Divergence-to-System-Architecture-Design-and-Philosophy-for-AGI-A-Pre-Manifested?origin=scientificContributions](https://www.researchgate.net/profile/Sean-Diamond-2/publication/394267167_Resonant_Symbolic_Cognition_Toward_a_Mythotechnical_Architecture_for_Artificial_General_Intelligence_An_Epistemological_Divergence_to_System_Architecture_Design_and_Philosophy_for_AGI_A_Pre-Manifested/links/68905a446e1ad24f59ed64b2/Resonant-Symbolic-Cognition-Toward-a-Mythotechnical-Architecture-for-Artificial-General-Intelligence-An-Epistemological-Divergence-to-System-Architecture-Design-and-Philosophy-for-AGI-A-Pre-Manifested?origin=scientificContributions)  
24. Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region, accessed on December 9, 2025, [https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html](https://www.sigir-ap.org/sigir-ap-2025/accepted-papers/index.html)  
25. The unwitting labourer: extracting humanness in AI training \- ResearchGate, accessed on December 9, 2025, [https://www.researchgate.net/publication/370839859\_The\_unwitting\_labourer\_extracting\_humanness\_in\_AI\_training](https://www.researchgate.net/publication/370839859_The_unwitting_labourer_extracting_humanness_in_AI_training)  
26. Platforms as architects of AI influence: rethinking moderation in the age of hybrid expression, accessed on December 9, 2025, [https://www.tandfonline.com/doi/full/10.1080/20414005.2025.2562681](https://www.tandfonline.com/doi/full/10.1080/20414005.2025.2562681)