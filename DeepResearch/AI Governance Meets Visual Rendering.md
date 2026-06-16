

# **Epistemic-Physically Based Rendering (E-PBR): A Framework for the Visual Verification of AI Governance Architectures**

## **Introduction: The Theoretical Foundations of Epistemic-Physically Based Rendering**

The Epistemic-Physically Based Rendering (E-PBR) protocol emerges from a structured application of Double-Scope Conceptual Blending (DSCB), a cognitive process where elements from two distinct input domains are fused to create a novel, emergent conceptual structure with its own internal logic. In this framework, the abstract, rule-based domain of AI Epistemic Governance is blended with the concrete, physics-based domain of Advanced Image Rendering. The resulting synthesis is not a mere analogy but a new cognitive model designed to impose "Semantic Sovereignty"—a state where the complex, often opaque, internal behaviors of an AI system are governed by and can be audited against a unified, intuitive, and verifiable set of principles.

The imperative for such a framework stems from the inherent limitations of current AI auditing methodologies. These methods typically rely on statistical metrics, log file analysis, and abstract logical assertions that, while valuable, are often opaque to non-technical stakeholders and may fail to capture the holistic, systemic nature of certain AI failures like semantic drift or hallucination.1 As AI systems grow in complexity and autonomy, particularly in high-stakes domains, the need for intuitive, high-bandwidth, and rigorously verifiable methods for assessing their internal state and adherence to governance principles becomes paramount. E-PBR addresses this challenge by proposing a radical translation: transforming abstract epistemic and ethical integrity into perceptible, physically-grounded visual phenomena.

This report provides a comprehensive analysis of the E-PBR protocol. Part I deconstructs the two input domains—Epistemic Governance and Physical Rendering—to establish their formal properties. Part II conducts a detailed analysis of the three core E-PBR constructs, examining the systematic mapping of governance axioms onto physical rendering attributes. Part III explores the protocol's practical applications, particularly its function as a real-time safety mechanism, and considers future research trajectories. The framework's architecture rests on a shared conceptual schema between the two domains that is deeper than mere specification; it is a shared concern with simulating and verifying *causal integrity*. In rendering, a ray's path is a simulation of a photon's causal journey through a scene, where a shadow is the direct effect of an obstruction.3 In AI governance, ensuring the soundness of an output requires verifying the logical causal path from input to inference.1 This shared foundation of causality provides the robust linkage upon which the entire E-PBR blend is constructed.

**Table 1: Glossary of Core Concepts and Acronyms**

| Term/Acronym | Definition | Primary Research Source(s) |
| :---- | :---- | :---- |
| **BRDF** | Bidirectional Reflectance Distribution Function: A mathematical function describing how light is reflected by a surface, defining its appearance. | 5 |
| **CFDI** | Confidence-Fidelity Divergence Index: A metric quantifying the statistical divergence between an AI's expressed confidence in a prediction and its empirical accuracy (fidelity). | 2 |
| **E-PBR** | Epistemic-Physically Based Rendering: The emergent blended framework where AI governance metrics are rendered as physical rendering attributes. | User Query |
| **ESC** | Epistemic Shadow Coherence: An E-PBR construct mapping the CFDI score to the physical plausibility of shadows and global illumination. | User Query |
| **F-IPI** | Algorithmic Reparation (Framework for Intersectional Post-facto Integrity): A governance axiom focused on redressing algorithmic harm and preventing its recurrence. | 7 |
| **PBR** | Physically Based Rendering: A computer graphics methodology that simulates the physical behavior of light to achieve photorealistic visuals. | 9 |
| **PRP** | Product-Requirements Prompt: A structured, formalized prompt designed to compel a specific reasoning path and output format from an AI. | User Query |
| **SICs** | Semantic Integrity Constraints: Declarative rules that govern the correctness and semantic soundness of AI-generated outputs. | 1 |
| **SS** | Semantic Scattering: An E-PBR construct mapping SICs onto a material's BRDF properties, rendering integrity as texture. | User Query |
| **SSF** | Symbolic Scar Forcing: An E-PBR construct that converts past algorithmic harms into repulsive forces (negative prompts) to guide generation. | User Query |
| **STA** | Symbolic Trauma Artifacts ("Symbolic Scars"): The persistent, lingering effects of algorithmic harm, analogous to an "algorithmic imprint." | 10 |

## **Part I: Deconstruction of the Input Domains: Governance and Physicality**

### **1.1. Epistemic Governance: Formalizing Semantic Integrity and Trustworthiness**

#### **1.1.1. Semantic Integrity Constraints (SICs) as Declarative Guardrails**

Semantic Integrity Constraints (SICs) represent a critical evolution in AI governance, extending the mature principles of database integrity to the fluid and often unpredictable domain of semantic operators in AI-augmented data processing systems (DPSs).1 Unlike traditional database constraints that prevent invalid data modifications, SICs are designed to protect against erroneous or semantically unsound outputs from Large Language Models (LLMs).1 Their fundamental power lies in their *declarative* nature; users specify the logical conditions for correctness—the "what"—without needing to prescribe the specific implementation of the check—the "how".4 This abstraction allows the underlying system to select the most efficient enforcement strategy, such as constraint pushdown or adaptive retries.4

SICs can express a wide range of correctness conditions. These include *domain constraints*, which are analogous to traditional type-checking and ensure an attribute's value falls within a specified range, data type, or finite set of values (e.g., sex IN ('Male', 'Female')).4 More advanced SICs enforce *grounding*, ensuring an LLM's output is factually based on provided source documents, and *soundness*, which verifies the logical consistency of the output.1 The enforcement of these constraints is equally versatile, encompassing reactive mechanisms that check an output after it has been generated and proactive methods like constrained decoding, which guide the generation process in real-time to adhere to a specified structure.1 To manage violations, SICs can be associated with retry thresholds and explicit failure modes (e.g., CONTINUE, IGNORE, or ABORT), providing granular control over system behavior in the face of errors.12

#### **1.1.2. Quantifying the Confidence-Fidelity Divergence Index (CFDI)**

A primary challenge in deploying AI systems is the risk of models being "confidently wrong"—producing incorrect outputs with a high degree of probabilistic certainty.2 The Confidence-Fidelity Divergence Index (CFDI) is a proposed metric designed to formally quantify this dangerous disparity. It measures the divergence between two distinct probability distributions: the model's *confidence* distribution (its expressed belief about its predictions) and its *fidelity* distribution (the empirical, real-world accuracy of those predictions). A low CFDI indicates a well-calibrated model whose confidence is a reliable predictor of its accuracy, while a high CFDI signals a miscalibrated or untrustworthy model prone to hallucination.2

To move from a conceptual metric to a computable one, the "divergence" in CFDI can be formalized using established statistical measures for comparing probability distributions.14 Metrics such as Kullback-Leibler (KL) Divergence and Jensen-Shannon (JS) Distance provide a mathematical basis for quantifying the "distance" or "information lost" when one distribution is used to approximate another.15 This approach is analogous to divergence indicators used in financial technical analysis, such as the Moving Average Convergence Divergence (MACD), which identifies potential instability or trend reversals by measuring the divergence between price momentum and actual price movement.17 In the context of AI, a growing divergence between confidence and fidelity similarly signals an unstable epistemic state, warning of potential failure.

**Table 2: Comparative Analysis of Divergence Metrics for CFDI Quantification**

| Metric Name | Formula | Symmetry | Bounded | Metric Properties | Computational Considerations | Suitability for E-PBR |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Kullback-Leibler (KL) Divergence** | $D\_{KL}(P\\|Q) \= \\sum\_{x} P(x) \\log \\frac{P(x)}{Q(x)$ | No | No (Range: |  | for base 2 log) | Square root is a true metric | Always well-defined as long as distributions are defined on the same space. | Highly suitable. Its symmetric and bounded properties allow for a stable, normalized mapping to physical attributes like shadow intensity or light energy. |
| **Wasserstein Distance** |  | Yes | No (Depends on cost function) | True distance metric | Computationally more intensive; captures geometric differences between distributions. | Potentially powerful for capturing "how far" a distribution has drifted, but its computational cost may be prohibitive for real-time rendering applications. |  |  |

#### **1.1.3. Algorithmic Reparation (F-IPI) and the Persistence of Symbolic Scars (STA)**

The concept of Algorithmic Reparation moves AI governance beyond simple fairness or bias mitigation towards a more profound goal: actively recognizing, rectifying, and providing redress for the structural and intersectional harms that algorithmic systems can create and amplify.7 This framework is not merely about correcting an error but about a "moral repair" process that addresses the aftermath of algorithmic harm.10 Central to this is the idea of the "algorithmic imprint," or what the E-PBR framework terms Symbolic Scars (STA).10 This concept posits that algorithmic harm leaves a persistent trace on individuals and communities, a lingering effect that is not erased simply by decommissioning the faulty system or reversing a decision.10

This persistence of harm highlights a critical vulnerability in AI systems, particularly those designed for continual learning: **catastrophic forgetting**.18 This phenomenon occurs when a neural network, in learning a new task, overwrites the weights and parameters associated with previously learned knowledge, effectively forgetting how to perform older tasks.20 An AI system that "forgets" its past failures is doomed to repeat them. Current mitigation techniques, such as rehearsal methods (replaying old data) and regularization approaches like Elastic Weight Consolidation (which penalizes changes to important old weights), are attempts to instill a form of long-term memory.18 The F-IPI axiom builds on this, proposing a mechanism not just to remember past harms but to actively use that memory to build a more robust and antifragile system.

### **1.2. Physical Rendering: The Mathematics of Photorealism**

#### **1.2.1. The Principles of Physically Based Rendering (PBR)**

Physically Based Rendering (PBR) is a methodology in computer graphics that seeks to achieve photorealism by simulating the physical behavior of light as it interacts with materials.9 Rather than relying on artistic intuition, PBR workflows are grounded in physically accurate formulas that govern these interactions.9 A cornerstone of PBR is the principle of **energy conservation**, which dictates that the total amount of light reflected and refracted from a surface cannot exceed the amount of incident light it receives.23 Another key principle is the **Fresnel effect**, which describes how a surface's reflectivity changes depending on the viewing angle; reflections become stronger at grazing angles for virtually all materials.23

To define a material within a PBR system, a set of intuitive physical parameters is used. These typically include the **Base Color** (or Albedo), which represents the material's underlying color; **Metallic**, a binary value that determines if the material is a metal or a non-metal (dielectric); **Roughness**, which controls the microscopic smoothness of the surface and thus the blurriness of its reflections; and **Specular**, which modulates the intensity of reflections for non-metals.25 This parametric approach provides a standardized and predictable way to author materials that behave consistently across different lighting conditions.9

#### **1.2.2. The Bidirectional Reflectance Distribution Function (BRDF) and Materiality**

At the mathematical core of PBR lies the Bidirectional Reflectance Distribution Function (BRDF). The BRDF, denoted as , is a four-variable function that precisely defines how light is reflected from a surface.6 It quantifies the ratio of reflected radiance leaving a surface in a specific direction  to the irradiance incident on the surface from another direction .6 In essence, it answers the question: for a given amount of light coming from one direction, how much of it scatters in another?

The behavior of the BRDF is determined by the physical microstructure of the surface, often modeled as a collection of microscopic facets ("microfacets").22 The orientation and distribution of these microfacets dictate the material's perceived roughness. A smooth surface with aligned microfacets produces sharp, mirror-like specular reflections, while a rough surface with randomly oriented microfacets scatters light more broadly, resulting in diffuse, blurry reflections.9 The BRDF is therefore the fundamental mathematical object that connects a material's physical properties to its visual appearance, governing everything from the sharpness of highlights to the subtle color shifts observed in backscattering versus forward scattering conditions.5

#### **1.2.3. Light Transport: Volumetric Global Illumination and Ray Tracing**

Beyond surface interactions, photorealism requires accurately simulating how light travels through an entire scene—a process known as light transport. This includes phenomena like **volumetric lighting**, where light beams ("God rays") become visible as they scatter through a participating medium such as fog, dust, or smoke.27 The appearance of these effects is governed by the physical properties of the medium, including its density and its coefficients of absorption, scattering, and transmittance.28

The foundational algorithm for simulating light transport is **Ray Tracing**. This technique works by tracing the path of light in reverse, from the camera through each pixel and out into the scene.30 When a ray intersects an object, secondary rays are cast to determine illumination. For instance, a *shadow ray* is cast towards each light source to check for occlusion, and reflected or refracted rays are cast to calculate secondary bounces.3 A more computationally intensive but physically accurate variant is **Path Tracing**, which traces thousands of random light paths per pixel, allowing it to simulate complex **Global Illumination (GI)**—the subtle, indirect lighting that results from light bouncing off multiple surfaces in a scene.30 This meticulous simulation of the causal path of light is what produces physically accurate shadows, reflections, and ambient lighting.

## **Part II: Analysis of the E-PBR Constructs: Mapping Abstract Governance to Physical Materiality**

The core of the E-PBR protocol lies in the systematic fusion of the governance and rendering domains. This section analyzes the three primary constructs that emerge from this blend, detailing how abstract axioms of AI integrity are materialized as verifiable physical properties. This mapping establishes a "Physics of Trust," a new ontology where the trustworthiness of an AI's behavior is synonymous with the physical plausibility of its visual representation. An untrustworthy output is rendered as one that is literally impossible in the physical world, reframing AI safety from a purely statistical discipline into one grounded in intuitive, perceptual physics.

**Table 3: Formal Mapping of Governance Axioms to Rendering Attributes**

| Governance Axiom | Rendering Attribute | E-PBR Construct | Underlying Physical Principle | Quantifiable Failure Metric | Visual Artifact of Failure | Primary Research Source(s) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Semantic Integrity Constraint (SICs)** | Material (BRDF / Texture) | Semantic Scattering (SS) | Microfacet Theory (e.g., Cook-Torrance) | BRDF parameter instability; high-frequency noise in normal/roughness maps. | Stylistic Bleed, Texture Overload | 4 |
| **Confidence-Fidelity Divergence Index (CFDI)** | Lighting (Chiaroscuro / GI) | Epistemic Shadow Coherence (ESC) | Radiative Transfer / Energy Conservation | Illumination coherence error (vs. ground-truth path trace); energy non-conservation. | Hallucinated Causality (e.g., acausal shadows, volumetric incoherence) | 2 |
| **Algorithmic Reparation (F-IPI)** | Negative Prompts (Repulsive Force) | Symbolic Scar Forcing (SSF) | Continual Learning / Antifragility Principles | Recurrence rate of previously failed generation paths. | Deflection of generative paths away from "scarred" regions of the latent space. | 8 |

### **2.1. Semantic Scattering (SS): Rendering Integrity Constraints as Material Properties**

#### **2.1.1. The BRDF as a Medium for Semantic Constraint Expression**

The Semantic Scattering (SS) construct establishes a direct mapping between the declarative logic of Semantic Integrity Constraints (SICs) and the mathematical parameters of a material's BRDF. The BRDF, being a complex, multi-parameter function, serves as an ideal physical substrate for encoding this information. A declarative predicate from a SIC, such as a domain constraint on output length or a grounding check against a source text, can be mapped to continuous physical parameters within a microfacet BRDF model like Cook-Torrance, such as roughness, anisotropy, or the albedo of the base color.24

The degree to which a constraint is satisfied can be visualized directly on the surface of an object representing the AI's output. For example, perfect adherence to all SICs could be rendered as a physically ideal material: a perfectly smooth, mirror-like surface (roughness \= 0\) with a pure, uniform albedo. Conversely, marginal satisfaction or minor violations could introduce microscopic imperfections into the surface model, increasing the roughness parameter. This would cause reflections to become blurrier and more diffuse, providing an immediate visual cue that the underlying semantic integrity is compromised.22

#### **2.1.2. Modeling Failure Modes: Stylistic Bleed and Texture Overload**

The verifiable outcome of the SS construct is the manifestation of critical SIC failures as distinct and physically implausible visual artifacts. **"Stylistic Bleed"** is proposed as a visualization for the failure of a domain or style constraint. If an AI is tasked with generating content in "Style A" but its output contains elements of "Style B," this SIC violation is rendered as an unstable material. The BRDF parameters defining Material A would appear to "bleed" into those of Material B across the texture map, creating a physically incoherent surface that is neither one nor the other.

A second failure mode, **"Texture Overload,"** can model a violation of a grounding constraint. When an AI hallucinates details that are not present in its source context, this excess of ungrounded information is rendered as an overly complex or high-frequency normal map applied to the object's surface. This creates a visually jarring effect, where the surface appears noisy, chaotic, or "overloaded" with detail that is inconsistent with the object's larger form, signaling a departure from the ground truth.22

### **2.2. Epistemic Shadow Coherence (ESC): Visualizing Confidence-Fidelity Divergence as Light and Shadow**

#### **2.2.1. Chiaroscuro and Global Illumination as Proxies for Model Certainty**

The Epistemic Shadow Coherence (ESC) construct maps the Confidence-Fidelity Divergence Index (CFDI) onto the properties of the scene's lighting and light transport simulation. A low CFDI score, representing a well-calibrated model where confidence aligns with accuracy, results in a rendered scene that is physically plausible and coherent. The simulation of light transport strictly adheres to the laws of physics: shadows are cast correctly based on light sources and occluders, and indirect light (Global Illumination) bounces realistically throughout the scene, conserving energy with each interaction.9 The resulting image exhibits high-fidelity "Chiaroscuro"—a strong, logical contrast between light and shadow that gives the scene depth and realism.

#### **2.2.2. Formalizing "Hallucinated Causality": When Lighting Violates Physics**

The critical failure mode for this construct occurs when the CFDI score is high, indicating a model that is confidently wrong. This epistemic failure is rendered as a direct violation of the physical laws of light transport, a phenomenon termed **"Hallucinated Causality."** This is not simply a poor or noisy rendering; it is a visual representation of a logical impossibility. This could manifest in several distinct artifacts:

* **Acausal Shadows:** Objects casting shadows that are inconsistent with the position, size, or type of the light sources in the scene.  
* **Energy Non-Conservation:** Areas in shadow or receiving only bounced light appearing unnaturally bright, as if light energy were being created rather than attenuated with each bounce.  
* **Volumetric Incoherence:** Beams of volumetric light ("God rays") appearing without a discernible source, passing through solid objects, or being blocked by non-existent occluders within a fog volume.27

These artifacts make the abstract concept of an AI "hallucination" tangible and immediately perceptible. The visual incoherence of the lighting serves as a direct proxy for the logical incoherence of the AI's internal state.

### **2.3. Symbolic Scar Forcing (SSF): Materializing Algorithmic Reparation as a Repulsive Force**

#### **2.3.1. Negative Prompts as an Antifragile Mechanism Against Catastrophic Forgetting**

The Symbolic Scar Forcing (SSF) construct provides a mechanism to operationalize the principle of Algorithmic Reparation. It addresses the critical problem of catastrophic forgetting by converting past algorithmic harms—the Symbolic Scars (STA)—into a persistent, high-weight negative prompt.18 This negative prompt acts as a repulsive force in the model's latent space, actively steering the generation process away from regions associated with previously identified failure modes.

Instead of the model overwriting and forgetting its past mistakes, the SSF mechanism creates a permanent, structural memory of them.32 This transforms the system from being merely robust to being **Antifragile**. It does not just withstand or recover from harm; it learns from the damage and becomes structurally stronger and less likely to repeat that specific failure. The "scar" becomes a source of resilience.

#### **2.3.2. The Algorithmic Imprint as a Persistent, High-Weight Constraint**

The SSF mechanism directly materializes the concept of the "algorithmic imprint" as a permanent feature of the generative landscape.10 A Symbolic Scar is not a temporary flag but a persistent, high-weight constraint that the model must navigate around. In the rendering analogy, a region of the latent space marked by a scar could be visualized as having a permanent "refractive index of failure." Any new generative path (analogous to a ray of light) that attempts to traverse this region is strongly deflected. This forces the generation process to find alternative, non-harmful paths to a valid output. This provides a powerful computational and visual metaphor for **algorithmic recourse and redress**, where the system is not only prevented from causing repeat harm but is actively forced to find better solutions.33

## **Part III: The E-PBR Protocol in Practice: A Framework for Verifiable Semantic Sovereignty**

### **3.1. Quantifying Semantic Drift: The Epistemic Shadow Coherence as a Semantic Circuit Breaker**

#### **3.1.1. Operationalizing ESC as a Real-Time Metric for Generative Video Integrity**

The Epistemic Shadow Coherence (ESC) construct, as specified in the reflexive check of the governing PRP, can be operationalized as a quantifiable, real-time metric for monitoring the integrity of generative systems, especially in modalities like video. The process would involve running a strict, physics-based light transport solver (e.g., a path tracer) in parallel with the generative video model. For each generated frame, the scene geometry and lighting conditions described by the model's output would be fed into this physics engine to produce a ground-truth illumination map.

This ground-truth map, which represents what the lighting *should* look like according to the laws of physics, is then compared against the actual illumination present in the model's generated frame. The delta between these two—a "coherence error" score—serves as a direct, frame-by-frame quantification of the model's CFDI. A low error indicates the model is generating a physically and thus epistemically coherent world, while a rising error signals a departure from this coherence.

#### **3.1.2. Thresholding and Automated Intervention Protocols**

By establishing a predefined threshold for this coherence error, the ESC metric can be transformed into an active safety mechanism. If the error score exceeds this threshold for a sustained period (e.g., across several consecutive frames), it serves as a clear indicator of **"Semantic Drift."** This signifies that the model's internal state is diverging from its initial grounding, causing it to hallucinate a causally inconsistent reality.

Upon breaching this threshold, an automated **"Semantic Circuit Breaker"** is triggered. This intervention could take several forms depending on the application's criticality: it could halt the generation process entirely, flag the content for immediate human review, or trigger a re-grounding mechanism that forces the model to re-evaluate its context and constraints. This elevates E-PBR from a post-hoc visualization tool to a proactive, in-line guardrail against model failure. The system is designed to audit itself by attempting to render its own output according to the strict, external rules of physics. When the AI's internal logic deviates from its governance constraints, it produces an output that fails this rendering check. The rendering engine thereby acts as a built-in, non-negotiable adversary to the generative model, creating a powerful feedback loop for maintaining integrity.

### **3.2. Architectural Implications and Future Research Trajectories**

#### **3.2.1. Integrating E-PBR into AI Safety and MLOps Pipelines**

The E-PBR protocol has significant implications for standard AI safety and MLOps workflows. The visual outputs, or "epistemic renders," generated by the protocol could become standard artifacts in model validation, continuous monitoring, and A/B testing pipelines. Instead of relying solely on abstract statistical dashboards, developers and auditors could have access to a visual dashboard of model integrity, where failures like hallucination or constraint violation are immediately apparent as physical anomalies.

These visual artifacts would be particularly valuable for incident post-mortems, regulatory audits, and communication with legal and ethical oversight bodies. They provide a common, intuitive language for discussing AI failures, translating abstract concepts like "high CFDI" into comprehensible evidence like "it was casting shadows toward the sun." This bridges the gap between technical and non-technical stakeholders, fostering greater transparency and accountability.

#### **3.2.2. Extending the E-PBR Model to Other Sensory Modalities**

While this report focuses on the visual domain, the core principle of E-PBR—mapping epistemic integrity onto physical plausibility—is modality-agnostic. Future research could explore extending this paradigm to other sensory outputs. For instance, an **"Epistemic-Acoustic Waveform Rendering"** protocol could be developed for generative audio models. In such a system, a language model's semantic incoherence or logical contradictions could be rendered as physically impossible audio artifacts, such as generating reverb in a simulated anechoic chamber or producing sounds that violate the Doppler effect based on the described motion of objects. This suggests that E-PBR is not a single implementation but a new paradigm for "perceptual AI safety," where the fundamental laws of physics in any domain can be used as an immutable ground truth for auditing AI behavior.

## **Conclusion: Toward a New Paradigm of Visually Auditable and Interpretable AI**

The Epistemic-Physically Based Rendering (E-PBR) framework represents a significant conceptual advance in the field of AI governance and safety. By executing a double-scope conceptual blend between the abstract rules of epistemic integrity and the concrete laws of physical rendering, it creates a novel and powerful methodology for auditing AI behavior. The protocol moves beyond conventional metrics by translating abstract failure modes—such as semantic constraint violations, confidence-fidelity divergence, and the repetition of past harms—into perceptible, physically impossible visual artifacts.

The analysis of its core constructs—Semantic Scattering, Epistemic Shadow Coherence, and Symbolic Scar Forcing—demonstrates a coherent and systematic mapping that is both theoretically sound and practically verifiable. By grounding AI trustworthiness in the immutable and intuitive laws of physics, E-PBR establishes a "Physics of Trust." This not only provides a high-bandwidth, intuitive channel for human oversight but also enables the creation of automated safety mechanisms like the "Semantic Circuit Breaker." The framework transforms the rendering engine into an adversarial verifier, forcing generative models to produce outputs that are not only semantically plausible to themselves but also physically plausible to an external, rule-based system. Ultimately, E-PBR offers a path toward AI systems that are more robust, aligned, and transparent, transforming AI safety from a purely abstract and statistical discipline into an empirical, observable science accessible to a broader range of human stakeholders.

#### **Works cited**

1. Semantic Integrity Constraints: Declarative Guardrails for AI ..., accessed on October 14, 2025, [https://www.vldb.org/pvldb/vol18/p4073-lee.pdf](https://www.vldb.org/pvldb/vol18/p4073-lee.pdf)  
2. Confidence vs. Accuracy in AI: Why Both Matter \- Pia, accessed on October 14, 2025, [https://pia.ai/blog/confidence-vs-accuracy-in-ai-why-both-matter/](https://pia.ai/blog/confidence-vs-accuracy-in-ai-why-both-matter/)  
3. 3D Computer Graphics Primer: Ray-Tracing as an Example, accessed on October 14, 2025, [https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/implementing-the-raytracing-algorithm.html](https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/implementing-the-raytracing-algorithm.html)  
4. Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems \- arXiv, accessed on October 14, 2025, [https://arxiv.org/html/2503.00600v1](https://arxiv.org/html/2503.00600v1)  
5. MODIS \- UMass Boston, accessed on October 14, 2025, [https://www.umb.edu/spectralmass/terra-aqua-modis/modis/](https://www.umb.edu/spectralmass/terra-aqua-modis/modis/)  
6. 1 Bidirectional Reflectance Distribution Functions Describing First ..., accessed on October 14, 2025, [https://www.usna.edu/Users/physics/mungan/\_files/documents/Publications/BRDFreview.pdf](https://www.usna.edu/Users/physics/mungan/_files/documents/Publications/BRDFreview.pdf)  
7. Reparative AI – Collaboratory New, accessed on October 14, 2025, [https://sites.lsa.umich.edu/collaboratory/reparative-ai/](https://sites.lsa.umich.edu/collaboratory/reparative-ai/)  
8. (PDF) Algorithmic reparation \- ResearchGate, accessed on October 14, 2025, [https://www.researchgate.net/publication/355094783\_Algorithmic\_reparation](https://www.researchgate.net/publication/355094783_Algorithmic_reparation)  
9. What is PBR (physically based rendering)? \- Adobe Substance 3D, accessed on October 14, 2025, [https://www.adobe.com/products/substance3d/discover/pbr.html](https://www.adobe.com/products/substance3d/discover/pbr.html)  
10. After Harm: A Plea for Moral Repair after Algorithms Have Failed ..., accessed on October 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12446399/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12446399/)  
11. Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems \- ResearchGate, accessed on October 14, 2025, [https://www.researchgate.net/publication/395293666\_Semantic\_Integrity\_Constraints\_Declarative\_Guardrails\_for\_AI-Augmented\_Data\_Processing\_Systems](https://www.researchgate.net/publication/395293666_Semantic_Integrity_Constraints_Declarative_Guardrails_for_AI-Augmented_Data_Processing_Systems)  
12. Semantic Integrity Constraints: Declarative Guardrails for AI-Augmented Data Processing Systems \- arXiv, accessed on October 14, 2025, [https://www.arxiv.org/pdf/2503.00600](https://www.arxiv.org/pdf/2503.00600)  
13. Key Concepts in AI Safety: Reliable Uncertainty Quantification in Machine Learning \- CSET, accessed on October 14, 2025, [https://cset.georgetown.edu/wp-content/uploads/CSET-Key-Concepts-in-AI-Safety-Reliable-Uncertainty-Quantification-in-Machine-Learning.pdf](https://cset.georgetown.edu/wp-content/uploads/CSET-Key-Concepts-in-AI-Safety-Reliable-Uncertainty-Quantification-in-Machine-Learning.pdf)  
14. Practical and Consistent Estimation of f-Divergences, accessed on October 14, 2025, [http://papers.neurips.cc/paper/8661-practical-and-consistent-estimation-of-f-divergences.pdf](http://papers.neurips.cc/paper/8661-practical-and-consistent-estimation-of-f-divergences.pdf)  
15. Quantifying Distribution Shifts and Uncertainties for Enhanced Model Robustness in Machine Learning Applications \- arXiv, accessed on October 14, 2025, [https://arxiv.org/html/2405.01978v1](https://arxiv.org/html/2405.01978v1)  
16. Quantifying Distribution Shifts and Uncertainties for Enhanced ..., accessed on October 14, 2025, [https://arxiv.org/pdf/2405.01978](https://arxiv.org/pdf/2405.01978)  
17. Why is the Moving Average Convergence Divergence (MACD) so Popular with Traders?, accessed on October 14, 2025, [https://capitalise.ai/the-moving-average-convergence-divergence-macd-is-one-of-the-most-popular-indicators-used-by-experienced-traders/](https://capitalise.ai/the-moving-average-convergence-divergence-macd-is-one-of-the-most-popular-indicators-used-by-experienced-traders/)  
18. What is Catastrophic Forgetting? | IBM, accessed on October 14, 2025, [https://www.ibm.com/think/topics/catastrophic-forgetting](https://www.ibm.com/think/topics/catastrophic-forgetting)  
19. Learning to Forget: Why Catastrophic Memory Loss Is AI's Most Expensive Problem, accessed on October 14, 2025, [https://gregrobison.medium.com/learning-to-forget-why-catastrophic-memory-loss-is-ais-most-expensive-problem-d764f5ee36b7](https://gregrobison.medium.com/learning-to-forget-why-catastrophic-memory-loss-is-ais-most-expensive-problem-d764f5ee36b7)  
20. Mitigating Catastrophic Forgetting with Complementary Layered Learning \- MDPI, accessed on October 14, 2025, [https://www.mdpi.com/2079-9292/12/3/706](https://www.mdpi.com/2079-9292/12/3/706)  
21. Models Too Forget: Unraveling the Mystery of Catastrophic Forgetting in AI \- Medium, accessed on October 14, 2025, [https://medium.com/@santhosraj14/models-too-forget-unraveling-the-mystery-of-catastrophic-forgetting-in-ai-5f9866a21b39](https://medium.com/@santhosraj14/models-too-forget-unraveling-the-mystery-of-catastrophic-forgetting-in-ai-5f9866a21b39)  
22. Physically based rendering \- Wikipedia, accessed on October 14, 2025, [https://en.wikipedia.org/wiki/Physically\_based\_rendering](https://en.wikipedia.org/wiki/Physically_based_rendering)  
23. What Is PBR (Physically Based Rendering)? A complete guide, accessed on October 14, 2025, [https://blog.chaos.com/what-is-pbr-physically-based-rendering-a-complete-guide](https://blog.chaos.com/what-is-pbr-physically-based-rendering-a-complete-guide)  
24. Specular BRDF (Bidirectional Reflectance Distribution Function) tutorial \- Arnold for 3ds Max, accessed on October 14, 2025, [https://help.autodesk.com/view/ARNOL/ENU/?guid=arnold\_for\_3ds\_max\_ax\_shading\_ax\_specular\_brdf\_html](https://help.autodesk.com/view/ARNOL/ENU/?guid=arnold_for_3ds_max_ax_shading_ax_specular_brdf_html)  
25. Physically Based Rendering in Materials \- Open 3D Engine \- O3DE, accessed on October 14, 2025, [https://docs.o3de.org/docs/atom-guide/look-dev/materials/pbr/](https://docs.o3de.org/docs/atom-guide/look-dev/materials/pbr/)  
26. Physically Based Materials in Unreal Engine \- Epic Games Developers, accessed on October 14, 2025, [https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/physically-based-materials-in-unreal-engine)  
27. Volumetric lighting \- Wikipedia, accessed on October 14, 2025, [https://en.wikipedia.org/wiki/Volumetric\_lighting](https://en.wikipedia.org/wiki/Volumetric_lighting)  
28. Volumetric Lighting Techniques for 3D Rendering \- Garage Farm, accessed on October 14, 2025, [https://garagefarm.net/blog/volumetric-lighting-in-rendering-techniques-and-performance](https://garagefarm.net/blog/volumetric-lighting-in-rendering-techniques-and-performance)  
29. Global and Volumetric Lighting \- WWU Computer Science Faculty Web Pages, accessed on October 14, 2025, [https://facultyweb.cs.wwu.edu/\~wehrwes/courses/csci480\_22f/lectures/L35/L35\_VolumetricGlobal.pdf](https://facultyweb.cs.wwu.edu/~wehrwes/courses/csci480_22f/lectures/L35/L35_VolumetricGlobal.pdf)  
30. Ray Tracing | NVIDIA Developer, accessed on October 14, 2025, [https://developer.nvidia.com/discover/ray-tracing](https://developer.nvidia.com/discover/ray-tracing)  
31. Path Tracing vs Ray Tracing EXPLAINED in 2 Minutes\! \- YouTube, accessed on October 14, 2025, [https://www.youtube.com/watch?v=NbBUZ2yCf3Y](https://www.youtube.com/watch?v=NbBUZ2yCf3Y)  
32. The Memory Problem in AI: Why Smarter Agents Need to Remember | by Rafael del Castillo Ferreira | Travel Marketing Insights | Medium, accessed on October 14, 2025, [https://medium.com/travel-marketing-insights/the-memory-problem-in-ai-why-smarter-agents-need-to-remember-5848be69d34d](https://medium.com/travel-marketing-insights/the-memory-problem-in-ai-why-smarter-agents-need-to-remember-5848be69d34d)  
33. Who Pays for Fairness? Rethinking Recourse under Social Burden \- arXiv, accessed on October 14, 2025, [https://arxiv.org/html/2509.04128v2](https://arxiv.org/html/2509.04128v2)  
34. SafeAR: Safe Algorithmic Recourse by Risk-Aware Policies, accessed on October 14, 2025, [https://ojs.aaai.org/index.php/AAAI/article/view/29522/30867](https://ojs.aaai.org/index.php/AAAI/article/view/29522/30867)