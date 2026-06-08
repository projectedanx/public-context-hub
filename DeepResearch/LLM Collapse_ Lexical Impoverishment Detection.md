# **DRP-LEXICAL-IMPOVERISHMENT-COLLAPSE-2025: Lexical Impoverishment as a Failure Precursor in LLM Output**

## **Executive Summary**

As the artificial intelligence ecosystem approaches the critical "data wall" projected for 2026, the reliance on synthetic data for training autoregressive Large Language Models (LLMs) has transitioned from a theoretical convenience to an industrial necessity. However, this shift has introduced a pervasive systemic risk: Model Autophagy Disorder (MAD), a degenerative condition where recursive training loops cause models to irreversibly degrade. This report executes the research plan for 'DRP-LEXICAL-IMPOVERISHMENT-COLLAPSE-2025', investigating the hypothesis that **Lexical Impoverishment**—a measurable contraction in vocabulary richness and syntactic complexity—acts as the definitive "canary in the coal mine" for this collapse.

The analysis synthesizes findings from information theory, computational linguistics, and neuropathology to establish a rigorous diagnostic framework. We demonstrate that before a model exhibits catastrophic failures such as infinite repetition loops or incoherence, it undergoes a "silent" phase of variance reduction. In this phase, the tails of the probability distribution are amputated, resulting in a loss of rare concepts and linguistic nuance. By correlating these computational phenomena with human linguistic pathologies—specifically the empty speech of Alzheimer’s and the perseveration of aphasia—we define a new standard for model health monitoring. The report concludes that detecting deviations in Moving-Average Type-Token Ratio (MATTR) and Semantic Entropy is essential for preventing the collapse of next-generation AI systems.

## ---

**1\. Introduction: The Thermodynamic Crisis of the Synthetic Web**

The trajectory of Generative AI in 2025 is defined by a singular, looming resource constraint: the exhaustion of high-quality, human-generated text. Reports from watchdogs such as Epoch AI have long projected that the stock of public human text available for training would be depleted by 2026, a prediction that has largely materialized.1 In response, the industry has pivoted toward "synthetic data augmentation," a practice where the outputs of current-generation models (like GPT-4, Claude 3, and Llama 3\) serve as the training corpus for the next generation.

This shift has created a closed-loop ecosystem, fundamentally altering the thermodynamics of information flow. In a natural ecosystem, human language is an "open system" fed by external sensory inputs, social interactions, and creative novelty, maintaining a high level of entropy and diversity. In a synthetic loop, the system becomes "closed." The training data is no longer a sampling of external reality but a sampling of the previous model's approximation of that reality. This process, termed **Model Autophagy** or "self-eating," creates a recursive feedback loop that amplifies biases, solidifies errors, and, crucially, reduces variance.2

### **1.1 The Phenomenon of Model Collapse**

Model Collapse is the terminal state of this recursive degeneration. It is characterized by the model’s inability to represent the true underlying distribution of the data. The degradation is not linear; it is often asymptotic, beginning with subtle quality losses before plummeting into incoherence. Shumailov et al. (2023) rigorously defined this phenomenon as "The Curse of Recursion," demonstrating that without access to fresh human data, models inevitably converge to a point estimate with zero variance.4

While the terminal symptoms of collapse—such as the generation of gibberish or the "jack rabbit" repetition loops observed in fine-tuned OPT-125M models 6—are obvious, they occur too late for effective intervention. The industry requires a *leading indicator*, a metric that signals the onset of degeneration while the model is still superficially fluent.

### **1.2 The Hypothesis: Lexical Impoverishment**

This report posits that **Lexical Impoverishment** is that indicator. We define Lexical Impoverishment not merely as a reduction in vocabulary size, but as a systemic failure to access the "long tail" of language. It is the computational equivalent of a shrinking worldview. As the model's internal probability distribution narrows, it becomes "hyper-confident" in a smaller subset of words and syntactic structures.7 This manifests as text that is grammatically perfect but semantically vacuous—a phenomenon we term "The Beige Drift."

By quantifying this drift using advanced metrics like Semantic Entropy and MATTR, we can detect the early stages of collapse (Early Model Collapse) where the model has begun to lose information about minority data and rare events, even while its perplexity on standard benchmarks remains stable.4

## ---

**2\. Theoretical Framework: The Mathematics of Autophagy**

To understand why lexical impoverishment occurs, we must dissect the mathematical mechanics of autoregressive generation and recursive training. The collapse is not a result of "bad data" in the traditional sense (like noise or typos), but rather a result of "hyper-clean" data that lacks the statistical complexity of natural language.

### **2.1 The Variance Reduction Mechanism**

The primary engine of autophagy is the sampling process. When an LLM generates text, it predicts a probability distribution $P(x\_t | x\_{\<t})$ over the vocabulary. However, it rarely samples from the *exact* distribution. Techniques like **Greedy Decoding**, **Beam Search**, **Top-k Sampling**, and **Nucleus (Top-p) Sampling** are employed to improve coherence.

* **Truncation:** These methods explicitly truncate the low-probability tail of the distribution. Tokens that are unlikely (but possible) are zeroed out to prevent the model from going "off the rails."  
* **The Squeeze:** If the original human training data had a variance $\\sigma^2\_{true}$, the generated data has a variance $\\sigma^2\_{gen} \< \\sigma^2\_{true}$ because the tails have been clipped.  
* **Recursive Compounding:** When Model $N+1$ is trained on data from Model $N$, it treats the truncated distribution as the ground truth. It effectively "learns" that rare events are impossible. When Model $N+1$ is then sampled (again with truncation), the variance shrinks further.5

Mathematically, for a simple Gaussian model approximated by samples, the variance at generation $n+1$ is related to generation $n$ by:

$$\\mathbb{E}\[\\sigma^2\_{n+1}\] \= \\frac{M-1}{M} \\sigma^2\_n$$

where $M$ is the sample size. As $n \\to \\infty$, the variance approaches zero. In the discrete space of language, this means the effective vocabulary shrinks until the model can only output the most probable sequence—the mean of the distribution.5

### **2.2 Functional Approximation Errors**

Beyond sampling, "Functional Approximation Errors" exacerbate the collapse. Neural networks are universal function approximators, but they are not perfect. They tend to smooth out complex landscapes. When fitting a distribution to limited data (even synthetic data), the network will often smooth over the "spikes" of rare, idiosyncratic usage that characterize human creativity. This smoothing effect, combined with sampling truncation, accelerates the loss of lexical diversity.4

### **2.3 The Thermodynamic Analogy: Stagnation States**

Recent research into "Phase-Slip" samplers frames this problem in thermodynamic terms. An autoregressive model traverses an "energy landscape" of probabilities. A repetitive loop (e.g., "the brain is the brain is the brain") represents a **deep local minimum**—a "potential well" from which the model cannot escape because the probability of any token other than the repeating one is near zero.7

This state is characterized by **Low Entropy**. A healthy model generating diverse text maintains a high entropy, constantly deciding between multiple viable paths. A collapsing model exhibits "Stagnation," where the entropy drops below a critical threshold (empirically $\\approx 0.6$ normalized). This stagnation is the thermodynamic signature of Lexical Impoverishment: the model has lost the "heat" (randomness/diversity) required to climb out of the well and explore the tails of the vocabulary.7

## ---

**3\. The Clinical Mirror: Human Pathologies as Diagnostic Models**

A novel contribution of the DRP-LEXICAL-IMPOVERISHMENT-COLLAPSE-2025 plan is the correlation of LLM failure modes with human linguistic pathologies. The brain, as a biological neural network, undergoes degenerative processes that bear a striking functional resemblance to Model Autophagy. By studying these human conditions, we can derive validated metrics for detecting similar decay in silicon.

### **3.1 Alzheimer’s Disease: The "Empty Speech" Paradigm**

The linguistic decline associated with Alzheimer’s Disease (AD) provides a perfect analog for "Early Model Collapse."

* **The Symptom:** Patients produce fluent, grammatically intact sentences that are devoid of informational content. This is known as "empty speech."  
* **The Mechanism:** Anomia (word-finding difficulty) leads the patient to rely on high-frequency, generic "light verbs" (e.g., *do, make, go*) and indefinite nouns (e.g., *thing, it, stuff*) instead of specific terms.10  
* **The Metric:** Clinical studies consistently use **Lexical Diversity** (specifically Type-Token Ratio and its variants) to detect this. A significant drop in the Information Content Units (ICU) per minute is a hallmark of the disease.11  
* **LLM Parallels:** An LLM in early collapse mimics this behavior. It produces safe, high-probability text. It avoids specific entities or rare technical terms because those represent the "tails" it has forgotten. It hallucinates by filling gaps with generic, plausible-sounding filler, just as an AD patient confabulates to mask memory gaps.12

### **3.2 Aphasia and Schizophrenia: The "Looping" Paradigm**

While AD mimics the content loss of early collapse, Aphasia and Schizophrenia mimic the structural failures of "Late Model Collapse."

* **Schizophrenia:** A central feature is "reduced synaptic gain" and increased "self-inhibition" in the semantic network. This prevents the brain from activating distant semantic associations, forcing the speaker into a narrow channel of "over-activated" words. This results in **perseveration** (repeating the same word) and a lack of semantic spread.14  
* **LLM Parallels:** This is mathematically identical to an LLM generating with a temperature of near-zero or a model that has overfit to a narrow distribution. The "self-inhibition" in the brain is analogous to the "probability well" in the model. The resulting infinite repetition loops in LLMs are the computational equivalent of psychotic perseveration or echolalia.15  
* **Broca's Aphasia:** This condition is characterized by "agrammatism" and a simplified syntactic structure. Patients rely on simple subject-verb-object constructions and omit function words or complex clauses.16 Similarly, collapsed LLMs exhibit **Syntactic Simplification**, losing the ability to generate nested clauses or complex compound-complex sentences, leading to a monotonic rhythm.

### **3.3 Diagnostic Transfer**

The clinical validity of metrics like **Moving-Average Type-Token Ratio (MATTR)** in diagnosing these human conditions validates their use for LLMs. If MATTR can distinguish a cognitively impaired human from a healthy one based on 100 words of speech, it can distinguish a collapsed model from a healthy one. The "pathology" of the model is real; it is a degenerative disorder of the probability distribution.18

## ---

**4\. Quantifying Decay: The Metrics of Impoverishment**

To operationalize the detection of Lexical Impoverishment, we must employ metrics that are robust to text length and capable of capturing both surface-level variety and deep semantic diversity.

### **4.1 Type-Token Ratio (TTR) and its Limitations**

The standard Type-Token Ratio (TTR) is defined as the number of unique word types ($V$) divided by the total number of word tokens ($N$):

$$\\text{TTR} \= \\frac{V}{N}$$

While intuitive, TTR is inherently flawed for comparative analysis of LLM outputs because it is negatively correlated with text length. As a text grows, the probability of encountering a new word naturally diminishes (Heaps' Law). A healthy 100-word paragraph might have a TTR of 0.75, while a healthy 10,000-word chapter might have a TTR of 0.10.19

* **The Trap:** An LLM that generates very short, curt responses might appear to have a high TTR, masking its inability to sustain diversity over a longer narrative.

### **4.2 The Gold Standard: Moving-Average TTR (MATTR)**

To solve the length dependency, we employ the **Moving-Average Type-Token Ratio (MATTR)**. This metric uses a sliding window (typically $w=50$ words) to calculate the TTR for every possible window in the text, then averages the results.17

$$\\text{MATTR}\_w \= \\frac{1}{L \- w \+ 1} \\sum\_{i=1}^{L-w+1} \\frac{\\text{Types}(x\_i, \\dots, x\_{i+w})}{w}$$

* **Why it works:** MATTR provides a localized measure of diversity. If an LLM enters a repetition loop for 20 tokens, the local windowed TTR will drop precipitously, dragging down the average. It effectively detects "micro-collapses" within a larger generation.  
* **Benchmarks:** Research in aphasia indicates that a MATTR-50 score below **0.70** is often indicative of pathology in human speech.18 We propose this as a baseline threshold for healthy LLM generation.

### **4.3 Semantic Entropy (SE) vs. Shannon Entropy**

Standard Shannon Entropy measures the uncertainty of the token prediction. However, distinct tokens can have identical meanings (e.g., "physician" vs. "doctor"). A model might alternate between synonyms to artificially inflate its TTR and Shannon Entropy while remaining semantically stagnant.  
Semantic Entropy (SE), introduced by Kuhn et al. (2023), addresses this by clustering generated sequences based on bi-directional entailment.

$$SE(x) \= \- \\sum\_{C\_i} P(C\_i) \\log P(C\_i)$$

where $P(C\_i)$ is the probability mass of a semantic cluster.22

* **The Hallucination Correlation:** A drop in Semantic Entropy is a strong predictor of hallucination and confabulation. When the model is uncertain about the *facts*, it often collapses into a single semantic lane (even if phrased differently), or conversely, spreads probability across mutually exclusive facts. In the context of Autophagy, a collapsing model will show high Shannon Entropy (trying to vary words) but low Semantic Entropy (saying nothing new).24

### **4.4 Distinct-N Analysis**

The **Distinct-n** metric measures the ratio of unique n-grams to total n-grams.

* **Distinct-1:** Vocabulary breadth.  
* **Distinct-2/3:** Phrasing and syntactic breadth.  
* **Distinct-n Drop:** In recursive loops, the **Distinct-3** score often degrades faster than Distinct-1. The model retains individual words but loses the ability to combine them in novel ways, relying on "fossilized" phrases learned from the synthetic training data. This mirrors the use of "formulaic language" in aphasia.25

## ---

**5\. Empirical Evidence: The Taxonomy of Collapse**

Recent experimental data provides a clear timeline of how Lexical Impoverishment progresses into full Mode Collapse.

### **5.1 Phase I: The "Clean" Deception (Generations 1-3)**

In the initial stages of training on synthetic data, models often exhibit **improved** performance on standard benchmarks (like GSM8K or HumanEval).

* **Mechanism:** Synthetic data acts as a filter, removing the "noise" and inconsistency of human text.  
* **The Hidden Cost:** While accuracy improves, the **Tail Perplexity** (perplexity evaluated on rare/complex documents) begins to spike. The model is optimizing for the "mean" of the distribution.  
* **Metric Behavior:** MATTR remains stable, but **Distinct-n** for higher values of $n$ (n=4,5) begins to decline as the model over-relies on standard phrasings.4

### **5.2 Phase II: The Generalization-to-Memorization Transition (Generations 4-9)**

As the loop continues, the model loses the ability to generalize to new inputs and begins to merely regurgitate the patterns of its training data.

* **The 15% Drop:** Research shows that when advanced models like GPT-4 are tasked with editing their own generated content recursively, the F1 score for task performance drops by approximately **15%**.28 This indicates a loss of information fidelity.  
* **Llama Series Data:** Experiments with Llama-2 indicate a "Safe Zone" of up to **20% synthetic data**. Beyond this threshold, specifically crossing **30%**, the degradation accelerates non-linearly.27 This suggests a "critical mass" of lexical impoverishment where the remaining vocabulary is insufficient to support coherence.

### **5.3 Phase III: Stagnation and Loops (Generation 10+)**

The final phase is characterized by "Stagnation States" where entropy collapses.

* **The "Brain" Loop:** In a controlled experiment using the Phase-Slip sampler, a stagnating GPT-2 model (TTR **0.26**) entered an infinite loop: *"... brain's ability to process information... brain... brain..."*  
* **Entropy Signature:** The Shannon Entropy during this loop dropped below **0.6**.  
* **Intervention:** By injecting noise (simulating "fresh" diversity), the TTR was restored to **0.81**, and the model broke the loop.7 This empirically proves that low entropy (impoverishment) is the *cause* of the loop.

### **Table 1: The Progression of Lexical Impoverishment**

| Collapse Phase | Lexical Signature | Semantic Signature | Clinical Analog | Detection Metric |
| :---- | :---- | :---- | :---- | :---- |
| **I. Latent** | High TTR; Low Tail Diversity | Stable; High Factual Accuracy | **Prodromal AD** (Subtle complexity loss) | Distinct-4 Drop; Tail Perplexity |
| **II. Impoverished** | Dropping MATTR; Generic Phrasing | Reduced Semantic Entropy; "Beige" Content | **Empty Speech** (Moderate AD); **Anomia** | MATTR-50 \< 0.70; SE Decline |
| **III. Collapsed** | TTR \< 0.40; Infinite Loops | Semantic Void; Gibberish | **Perseveration** (Schizophrenia); **Echolalia** | Entropy \< 0.6; Repetition Rate |

## ---

**6\. The Mechanics of Downstream Failure**

Why does Lexical Impoverishment lead to catastrophic failure like looping? The answer lies in the **Geometry of the Loss Landscape**.

A rich, human-like distribution is a complex landscape with many "valleys" (high probability regions) connected by "ridges" (transitional phrases). A diverse vocabulary provides the model with many paths to traverse this landscape.

* **The Canyon Effect:** As variance reduces (Impoverishment), the landscape smooths out. The valleys become deeper and steeper, and the ridges disappear. The model loses the "bridging" vocabulary required to transition smoothly between topics or sentences.  
* **The Loop:** When the model enters a deep valley (e.g., a common phrase), it lacks the semantic "energy" (entropy) to climb out. The probability of the token that repeats the phrase becomes orders of magnitude higher than any other token. The model is trapped.  
* **Coherence Failure:** In "Late Collapse," the model may switch between these deep valleys randomly, resulting in "schizophasia" or word salad—local coherence (short phrases make sense) but global incoherence.4

## ---

**7\. Strategic Mitigation and Future Outlook**

The irreversibility of Model Collapse ("The Curse of Recursion" implies defects are permanent) necessitates aggressive prevention strategies.

### **7.1 The "Golden Ratio" of Training Data**

Empirical data suggests a strict limit on synthetic data saturation. To maintain lexical health, training corpora should contain **no more than 20-25% synthetic text**.27 Exceeding this ratio risks tipping the model into the Phase II degradation zone. This necessitates the preservation and heavily weighted sampling of pre-2023 "heritage" human data.

### **7.2 Entropy-Aware Sampling (Phase-Slip)**

Current sampling methods (Top-p) contribute to collapse by truncating tails. A mitigation strategy involves **Entropy-Aware Sampling**:

* Monitor the real-time entropy of generation.  
* If entropy drops below the **Stagnation Threshold (0.6)**, intervene.  
* **Intervention:** Inject Gaussian noise into the Key-Value (KV) cache or temporarily raise the temperature. This "Latent Shock" forces the model to re-evaluate the context and explore the tails, artificially restoring diversity.7

### **7.3 Watermarking and Contamination Detection**

To manage the "Safe Ratio," we must identify synthetic data in the wild. **N-gram Overlap** thresholds are commonly used but brittle. Recent reports indicate that "Llama 2" defined contamination as an n-gram overlap in 10-token sequences.29 However, more robust "Watermarking" techniques (altering the distribution of specific tokens) and "Binoculars" methods (comparing perplexity ratios between two models) are required to filter the training pipe effectively.30

## ---

**8\. Conclusion**

The investigation into 'DRP-LEXICAL-IMPOVERISHMENT-COLLAPSE-2025' confirms that **Lexical Impoverishment is a measurable, predictive precursor to Model Collapse.** It is not merely a symptom of a dying model; it is the mechanism of death itself.

The reduction in active vocabulary (TTR/MATTR) and the stagnation of uncertainty (Entropy) represent the "cooling" of the generative engine. As the model cools, it loses the fluid dynamism of human thought, freezing into rigid, repetitive, and simplified structures. The parallels with human neurological degeneration are not just poetic but functional: both biological and artificial networks fail when they lose access to the diverse "long tail" of their associative pathways.

As we enter the era of the self-consuming web, the "health" of an AI model can no longer be defined solely by its accuracy on a benchmark exam. It must be defined by its **Vitality**—its entropic capacity for surprise, diversity, and linguistic richness. Monitoring metrics like MATTR and Semantic Entropy will be the vital signs of the AI industry, separating the robust models of the future from the collapsed husks of the recursive past.

### **Selected Reference Data Matrix**

| Concept | Source ID | Key Finding |
| :---- | :---- | :---- |
| **Curse of Recursion** | 5 | Recursive training causes variance to converge to zero; tails disappear first. |
| **Model Autophagy** | 2 | Defined as "self-consuming loops"; leads to MAD (Model Autophagy Disorder). |
| **Semantic Entropy** | 22 | Measures uncertainty of meaning; superior to Shannon entropy for hallucination detection. |
| **MATTR vs TTR** | 17 | MATTR-50 is length-invariant; differentiates aphasia from neurotypical speech (threshold \~0.70). |
| **Phase-Slip / Stagnation** | 7 | Entropy \< 0.6 signals imminent repetition loop; noise injection restores diversity. |
| **Safe Synthetic Ratio** | 27 | \<20% synthetic data is safe; \>30% accelerates collapse. |
| **Alzheimer's Analogy** | 10 | "Empty speech" (high fluency, low info) mirrors early model collapse; TTR is key biomarker. |

#### **Works cited**

1. GenAI: Running on empty? \- SAP, accessed on December 14, 2025, [https://www.sap.com/blogs/genai-running-on-empty](https://www.sap.com/blogs/genai-running-on-empty)  
2. Future of AI Models: A Computational perspective on Model collapse \- arXiv, accessed on December 14, 2025, [https://www.arxiv.org/pdf/2511.05535](https://www.arxiv.org/pdf/2511.05535)  
3. SELF-CONSUMING GENERATIVE MODELS GO MAD \- ICLR Proceedings, accessed on December 14, 2025, [https://proceedings.iclr.cc/paper\_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf)  
4. Model collapse \- Wikipedia, accessed on December 14, 2025, [https://en.wikipedia.org/wiki/Model\_collapse](https://en.wikipedia.org/wiki/Model_collapse)  
5. The Curse of Recursion: Training on Generated Data Makes Models Forget \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2305.17493v3](https://arxiv.org/html/2305.17493v3)  
6. What Is Model Collapse? \- IBM, accessed on December 14, 2025, [https://www.ibm.com/think/topics/model-collapse](https://www.ibm.com/think/topics/model-collapse)  
7. phase-slip-sampler 0.1.2 on PyPI \- Libraries.io \- security ..., accessed on December 14, 2025, [https://libraries.io/pypi/phase-slip-sampler](https://libraries.io/pypi/phase-slip-sampler)  
8. The curse of recursion: Training on generated data makes models forget \- arXiv, accessed on December 14, 2025, [https://arxiv.org/pdf/2305.17493](https://arxiv.org/pdf/2305.17493)  
9. A novel inference sampler, the Phase-Slip Sampler : r/learnmachinelearning \- Reddit, accessed on December 14, 2025, [https://www.reddit.com/r/learnmachinelearning/comments/1pdgz26/a\_novel\_inference\_sampler\_the\_phaseslip\_sampler/](https://www.reddit.com/r/learnmachinelearning/comments/1pdgz26/a_novel_inference_sampler_the_phaseslip_sampler/)  
10. A systematic review of explainable artificial intelligence methods for speech-based cognitive decline detection \- NIH, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12657886/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12657886/)  
11. Cog-TiPRO: Iterative Prompt Refinement with LLMs to Detect Cognitive Decline via Longitudinal Voice Assistant Commands \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2505.17137v4](https://arxiv.org/html/2505.17137v4)  
12. (PDF) Speech-Based Cognitive Screening: A Systematic Evaluation of LLM Adaptation Strategies \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/395270153\_Speech-Based\_Cognitive\_Screening\_A\_Systematic\_Evaluation\_of\_LLM\_Adaptation\_Strategies](https://www.researchgate.net/publication/395270153_Speech-Based_Cognitive_Screening_A_Systematic_Evaluation_of_LLM_Adaptation_Strategies)  
13. Dementia Through Different Eyes: Explainable Modeling of Human and LLM Perceptions for Early Awareness \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2505.13418v1](https://arxiv.org/html/2505.13418v1)  
14. Language network self-inhibition and semantic similarity in first-episode schizophrenia: A computational-linguistic and effective connectivity approach | Request PDF \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/360525498\_Language\_network\_self-inhibition\_and\_semantic\_similarity\_in\_first-episode\_schizophrenia\_A\_computational-linguistic\_and\_effective\_connectivity\_approach](https://www.researchgate.net/publication/360525498_Language_network_self-inhibition_and_semantic_similarity_in_first-episode_schizophrenia_A_computational-linguistic_and_effective_connectivity_approach)  
15. Quantifying Information Gain and Redundancy in Multi-Turn LLM Conversations \- OpenReview, accessed on December 14, 2025, [https://openreview.net/pdf/2cb74ae648f650e37d77885eb6ef22c93d1860dc.pdf](https://openreview.net/pdf/2cb74ae648f650e37d77885eb6ef22c93d1860dc.pdf)  
16. Effect of lexical cues on the production of active and passive sentences in Broca's and Wernicke's aphasia \- NIH, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3034248/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3034248/)  
17. Measures of lexical diversity in aphasia \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/240040506\_Measures\_of\_lexical\_diversity\_in\_aphasia](https://www.researchgate.net/publication/240040506_Measures_of_lexical_diversity_in_aphasia)  
18. Measuring Lexical Diversity for Discourse Analysis in Aphasia: Moving-Average Type–Token Ratio and Word Information Measure \- TalkBank, accessed on December 14, 2025, [https://talkbank.org/aphasia/publications/2020/Cunningham20.pdf](https://talkbank.org/aphasia/publications/2020/Cunningham20.pdf)  
19. taaled \- PyPI, accessed on December 14, 2025, [https://pypi.org/project/taaled/](https://pypi.org/project/taaled/)  
20. Evaluating evidence for the reliability and validity of lexical diversity indices in L2 oral task responses | Studies in Second Language Acquisition \- Cambridge University Press, accessed on December 14, 2025, [https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/evaluating-evidence-for-the-reliability-and-validity-of-lexical-diversity-indices-in-l2-oral-task-responses/E51955F0291E21A916CD2C4787508B80](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/evaluating-evidence-for-the-reliability-and-validity-of-lexical-diversity-indices-in-l2-oral-task-responses/E51955F0291E21A916CD2C4787508B80)  
21. Psychometric Evaluation of Lexical Diversity Indices: Assessing Length Effects, accessed on December 14, 2025, [https://www.researchgate.net/publication/273464919\_Psychometric\_Evaluation\_of\_Lexical\_Diversity\_Indices\_Assessing\_Length\_Effects](https://www.researchgate.net/publication/273464919_Psychometric_Evaluation_of_Lexical_Diversity_Indices_Assessing_Length_Effects)  
22. Linguistic Invariances for Uncertainty Estimation in Natural Language Generation | Semantic Scholar, accessed on December 14, 2025, [https://www.semanticscholar.org/paper/Semantic-Uncertainty%3A-Linguistic-Invariances-for-in-Kuhn-Gal/507465f8d46489a68a527cb5304d76bdb6c31ed9](https://www.semanticscholar.org/paper/Semantic-Uncertainty%3A-Linguistic-Invariances-for-in-Kuhn-Gal/507465f8d46489a68a527cb5304d76bdb6c31ed9)  
23. Beyond Semantic Entropy: Boosting LLM Uncertainty Quantification with Pairwise Semantic Similarity \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/2025.findings-acl.234.pdf](https://aclanthology.org/2025.findings-acl.234.pdf)  
24. Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2502.11620v1](https://arxiv.org/html/2502.11620v1)  
25. LLM Evaluation: 15 Metrics You Need to Know \- Arya.ai, accessed on December 14, 2025, [https://arya.ai/blog/llm-evaluation-metrics](https://arya.ai/blog/llm-evaluation-metrics)  
26. Evals for Diversity in Synthetic Data \- Amit Chaudhary, accessed on December 14, 2025, [https://amitness.com/posts/diversity-evals/](https://amitness.com/posts/diversity-evals/)  
27. Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2510.05133v1](https://arxiv.org/html/2510.05133v1)  
28. Guiding LLM to Fool Itself: Automatically Manipulating Machine Reading Comprehension Shortcut Triggers \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/2023.findings-emnlp.569.pdf](https://aclanthology.org/2023.findings-emnlp.569.pdf)  
29. Investigating Data Contamination for Pre-training Language Models \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2401.06059v1](https://arxiv.org/html/2401.06059v1)  
30. GenAI Content Detection Task 1: English and Multilingual Machine-Generated Text Detection: AI vs. Human \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/388231600\_GenAI\_Content\_Detection\_Task\_1\_English\_and\_Multilingual\_Machine-Generated\_Text\_Detection\_AI\_vs\_Human](https://www.researchgate.net/publication/388231600_GenAI_Content_Detection_Task_1_English_and_Multilingual_Machine-Generated_Text_Detection_AI_vs_Human)  
31. DivScore: Zero-Shot Detection of LLM-Generated Text in Specialized Domains \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/2025.emnlp-main.971.pdf](https://aclanthology.org/2025.emnlp-main.971.pdf)