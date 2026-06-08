# **The Pattern Ledger: An Exhaustive Analysis of Lexical and Semantic Metrics in the Age of Generative Intelligence**

## **1\. Executive Introduction: The Metrics of Synthetic Cognition**

The proliferation of Large Language Models (LLMs) has precipitated a crisis in the evaluation of linguistic output. As generative systems scale to trillions of parameters and context windows extend into the millions of tokens, the ability to distinguish between genuine semantic depth and stochastic mimicry has become the central challenge of computational linguistics. We are witnessing a shift from the evaluation of static text to the auditing of "synthetic cognition"—a dynamic process where the health of the system is defined by its ability to maintain lexical diversity, semantic coherence, and epistemic certainty over extended interactions.

This report establishes the "Pattern Ledger," a comprehensive analytical framework comprising six foundational metrics: Type-Token Ratio (TTR), Moving-Average Type-Token Ratio (MATTR), Measure of Textual Lexical Diversity (MTLD), Distinct-N, Semantic Entropy, and Compression Ratio. These metrics serve as the auditing tools for the "black box" of neural generation. They provide the quantitative means to detect "model autophagy" (the collapse of diversity due to recursive training), "hallucination" (the decoupling of confidence and truth), and "visual drift" (the gradual degradation of coherence in long-context generation).

The necessity of this ledger is underscored by the limitations of traditional psychometrics. The TTR, once the gold standard for analyzing aphasia and child language acquisition, has crumbled under the weight of "infinite context" streams, necessitating length-invariant alternatives like MATTR and MTLD. Simultaneously, the rise of Reinforcement Learning from Human Feedback (RLHF) has introduced an "alignment tax," a phenomenon where safety optimization actively suppresses the entropic variance of the model, measurable only through granular Distinct-N analysis and semantic clustering.

This document synthesizes findings from clinical aphasiology, information theory, patent law, and game theory to construct a unified theory of generative evaluation. It posits that the future of AI reliability lies not in the "vibe checks" of human evaluation, but in the rigorous, mathematical surveillance of the Pattern Ledger.

## ---

**2\. The Legacy of Lexical Counting: Type-Token Ratio (TTR) and its Collapse**

### **2.1 The Theoretical Basis of TTR**

The Type-Token Ratio (TTR) represents the primordial metric of lexical diversity. Defined algebraically as $TTR \= V / N$, where $V$ represents the number of unique types (vocabulary) and $N$ represents the total number of tokens (text length), TTR was historically championed by researchers such as Templin (1957) and Chotlos (1944) as a proxy for vocabulary richness.1 In the context of human speech pathology, a high TTR was indicative of robust cognitive function, while a low TTR signaled deficits such as anomic aphasia or developmental language disorder.

However, the utility of TTR is intrinsically bound by the statistical properties of natural language distributions, specifically Heaps’ Law and Zipf’s Law. Heaps’ Law dictates that vocabulary size grows sublinearly with text length ($V \= kN^\\beta$, where $\\beta \< 1$). Consequently, as $N$ increases towards infinity—a distinct possibility with modern "infinite stream" LLMs—the TTR inevitably approaches zero.3 This mathematical inevitability renders TTR useless for comparing texts of disparate lengths. A 100-word abstract will almost always possess a higher TTR than a 100,000-word novel, not because of superior lexical diversity, but because the denominator $N$ dilutes the ratio faster than the numerator $V$ can grow.5

### **2.2 TTR in the Era of Infinite Context**

The advent of "infinite context" models—such as those utilizing Ring Attention or infinite streaming architectures—has exposed the catastrophic failure of raw TTR as a metric. When evaluating models capable of processing 10 million tokens 7, TTR ceases to measure diversity and instead measures the asymptotic limits of the model's vocabulary.

Recent empirical studies on LLM-generated text have revealed that Zipf’s and Heaps’ laws hold only within narrow temperature ranges. At high temperatures, models hallucinate non-existent words, artificially inflating $V$ and thus TTR. At low temperatures, models suffer from "mode collapse," entering repetitive loops (e.g., "yes yes yes") that drive $V$ to stagnation while $N$ increases, causing TTR to plummet precipitously.6 This "U-shaped" failure curve confirms that TTR is less a measure of quality and more a measure of the model's sampling temperature and decoding strategy.

### **2.3 The Failure of Algebraic Corrections**

Attempts to salvage TTR through algebraic transformations—such as Root TTR ($V/\\sqrt{N}$) or Log TTR ($\\log V / \\log N$)—have largely failed to achieve true length invariance. The "Maas Index" and "Herdan’s C" attempt to linearize the TTR curve by assuming a logarithmic relationship, but these corrections break down at the extremes of text length common in AI pre-training corpora.10 Consequently, the field has pivoted toward algorithmic, rather than algebraic, solutions: specifically, the window-based (MATTR) and sequential (MTLD) approaches.

## ---

**3\. The Length-Invariant Revolution: Moving-Average Type-Token Ratio (MATTR)**

### **3.1 The Algorithmic Mechanics of MATTR**

The Moving-Average Type-Token Ratio (MATTR), formalized by Covington and McFall (2010), resolves the length-dependency of TTR by abandoning the global measurement in favor of a local, sliding-window approach.3 The algorithm operates as follows:

1. Define a window size $w$ (typically 50 tokens).  
2. Calculate the TTR for the window spanning tokens $1$ to $w$.  
3. Shift the window one token to the right ($2$ to $w+1$) and recalculate TTR.  
4. Repeat until the window reaches the end of the text.  
5. Compute the mean of all windowed TTR values.

$$MATTR(w) \= \\frac{1}{N \- w \+ 1} \\sum\_{i=1}^{N \- w \+ 1} \\frac{V\_i}{w}$$  
This method acts as a low-pass filter, smoothing out local irregularities while remaining completely independent of the total text length $N$ (provided $N \> w$).3 It effectively measures the *density* of new vocabulary introduced at any given moment, rather than the total inventory.

### **3.2 Clinical Sensitivity: The Aphasia Connection**

MATTR has proven exceptionally sensitive in clinical linguistics. In studies of Primary Progressive Aphasia (PPA), MATTR-50 successfully differentiated between non-fluent agrammatic PPA, semantic variants, and neurotypical controls, often outperforming standardized batteries like the Western Aphasia Battery.2

The metric captures the "micro-diversity" of speech. Patients with anomic aphasia may struggle to retrieve specific nouns, substituting them with generic fillers ("thing," "stuff") or repeating the same verbs. While these substitutions might not drastically affect a global TTR over a long conversation, they cause localized drops in the moving average, which MATTR detects with high fidelity.2 This sensitivity makes MATTR a prime candidate for monitoring "neural aphasia" in LLMs—instances where a model, restricted by safety alignment or quantization, loses access to its full vocabulary and reverts to safe, high-frequency tokens.

### **3.3 The Transferability Proxy in Patent Law**

Beyond linguistics, MATTR has found a novel application in the economic analysis of intellectual property. A study analyzing over 1.7 million U.S. patents identified MATTR as a robust proxy for "transferability"—the ease with which knowledge can be transferred between firms.12

* **High MATTR:** Indicates a patent description that uses precise, varied terminology to distinguish concepts clearly. This correlates with a 4-to-8 times higher likelihood of the patent being licensed.  
* **Low MATTR:** Suggests repetitive, vague, or obfuscated language, which increases "information frictions" and reduces the asset's value.

This finding suggests that lexical diversity is not merely a stylistic flourish but a marker of *information quality* and *codifiability*. In the context of LLMs, a high MATTR score in technical generation (e.g., summarizing a research paper) implies a higher fidelity of information transfer.12

### **3.4 Window Size and the "Visual Drift" Phenomenon**

The choice of window size in MATTR is critical. While 50 is the standard for general text, different windows reveal different pathologies:

* **Small Windows (10-20):** Crucial for detecting "Visual Drift" or "Motor Drift" in generative systems. In human motor control, "visual drift" refers to the decay of proprioceptive accuracy without feedback.13 In LLMs, this manifests as immediate repetition loops (e.g., "the the the") or loss of local coherence. Voynichese manuscript analysis utilized small windows to detect "abnormal small-scale repetition" distinct from natural languages.15  
* **Large Windows (500+):** Approximate global diversity. In the analysis of the Voynich manuscript, large-window MATTR values aligned with natural languages, while small-window values plummeted, revealing the manuscript's unnatural "micro-repetition" structure.15

For code generation, smaller windows are often more diagnostic. A sudden drop in MATTR-20 during a Python function generation often signals that the model has begun looping a variable assignment or failed to close a recursion, a common failure mode in lower-parameter models.16

## ---

**4\. The Sequential Assessment: Measure of Textual Lexical Diversity (MTLD)**

### **4.1 The Stabilization Threshold Algorithm**

While MATTR fixes the window length, the Measure of Textual Lexical Diversity (MTLD) fixes the diversity threshold. Developed by McCarthy and Jarvis (2010), MTLD calculates the average length of a text segment required for the TTR to drop to a localized value of 0.720.3

The algorithm proceeds sequentially:

1. Initialize TTR \= 1.0.  
2. Add words one by one, updating TTR.  
3. When TTR $\\le$ 0.720, increment the "factor count" by 1 and reset TTR.  
4. At the end of the text, calculate the "partial factor" for the remaining words.  
5. Score \= Total Tokens / Total Factors.  
6. Repeat the process in reverse (backward calculation) and average the two scores.10

This bidirectional averaging is crucial for stabilizing the metric against "start-up" effects, where the introduction of a topic might artificially inflate diversity in the first few sentences.1

### **4.2 Agglutinative Languages and Baseline Shifts**

MTLD is highly sensitive to the morphological typology of the language. In analytic languages like English, a concept is often expressed through multiple tokens (e.g., "I am going to school" \= 5 tokens). In agglutinative languages like Turkish or Finnish, the same concept is expressed via suffixes on a single root (e.g., "Okula gidiyorum" \= 2 tokens).20

Because agglutinative languages pack more semantic information into fewer unique types (via morphology), their TTR drops much slower than in English. Consequently, the "segment length" required to reach TTR=0.720 is much longer.

* **English MTLD:** Typically ranges from 40 to 100\.  
* **Turkish MTLD:** Can exceed 150-200 for comparable texts.20

This discrepancy is vital for evaluating Multilingual LLMs. If an LLM translates Turkish to English, a massive drop in relative MTLD (adjusting for baseline) suggests "lexical simplification"—the model is stripping away the morphological nuance of the source and rendering it into impoverished, repetitive English.23 Conversely, a failure to generate high-MTLD Turkish suggests the model treats the language as analytic, failing to utilize the complex suffix structures that characterize native fluency.21

### **4.3 MTLD as the Canary for Model Autophagy**

MTLD has emerged as a primary detector for "Model Autophagy" or "Model Collapse." This phenomenon occurs when generative models are trained recursively on synthetic data.25 As the model consumes its own output, the probability distribution narrows; the "tails" of the distribution (rare words, complex structures) are pruned in favor of the "mode" (average, high-probability words).

Empirical studies show that while global TTR might remain stable due to noise, MTLD scores exhibit a secular decline across recursive generations.27 The model loses the "lexical stamina" to maintain diversity over long segments. It might start a paragraph with diverse vocabulary, but it quickly exhausts its active retrieval pool, causing the TTR to crash to 0.720 in shorter and shorter intervals. This "shortening of the diversity span" is the hallmark of early-stage model collapse.25

## ---

**5\. The Repetition Penalty: Distinct-N and the Alignment Tax**

### **5.1 The Distinct-N Metric and Phrasal Diversity**

Distinct-N, introduced to the NLG community by Li et al. (2016), addresses the issue of *phrasal* redundancy.29 Unlike MATTR/MTLD, which focus primarily on unigrams (words), Distinct-N evaluates the diversity of n-grams (sequences of length $N$).

* **Distinct-1:** Unigram diversity (similar to TTR).  
* **Distinct-2:** Bigram diversity (measures collocation variety).  
* **Distinct-3:** Trigram diversity (measures phrase/cliché variety).

The metric is calculated as:

$$\\text{Distinct-}N \= \\frac{\\text{Count}(\\text{unique } n\\text{-grams})}{\\text{Total } n\\text{-grams}}$$  
Low Distinct-N scores are highly correlated with "safe" generative strategies, where models default to generic responses like "I don't know" or "That is interesting" to minimize training loss.29

### **5.2 The "Visual Drift" of Distinct-3**

In long-context generation, Distinct-3 serves as a sensitive barometer for "Visual Drift" or "Concept Drift".13 As a model generates a long story or code block, its attention mechanism may begin to "attend" disproportionately to its own recent output. This creates a feedback loop where phrases generated in paragraph 1 are repeated in paragraph 3, and then again in paragraph 5\.

While the unigram count (Distinct-1) might look healthy, the Distinct-3 score will decay asymptotically as the model recycles entire phrasal structures. This "structural drift" often precedes the complete collapse into infinite repetition loops. Advanced monitoring systems use a rolling Distinct-3 check as a "kill switch"—if the score drops below a critical threshold, the generation is halted to prevent resource waste.33

### **5.3 The Alignment Tax: RLHF vs. Diversity**

The most significant finding regarding Distinct-N is the quantification of the "Alignment Tax." Reinforcement Learning from Human Feedback (RLHF) aligns models to human preferences, which typically favor safety, clarity, and typicality over novelty.35

* **Mode Collapse:** RLHF optimization drives the model toward the "mode" of the distribution—the most likely, most "average" response that minimizes the risk of downvoting.  
* **The Metric Gap:** Empirical comparisons show that unaligned "Base" models often exhibit significantly higher Distinct-N scores than their "Chat" or "Instruct" counterparts. The process of making a model "safe" involves pruning the linguistic tails where diversity (and hallucination) lives.35

To counter this, techniques like "Verbalized Sampling" have been proposed. By explicitly prompting the model to explore the distribution of possible answers before committing, researchers can artificially restore the Distinct-N scores to pre-alignment levels without sacrificing safety.36

### **5.4 Expectation-Adjusted Distinct (EAD)**

A critical critique of raw Distinct-N is its dependence on text length (similar to TTR). To address this, "Expectation-Adjusted Distinct" (EAD) scales the observed distinct count against the *expected* count for a random sample of that length.29 This correction allows for the fair comparison of short, concise answers against long, verbose chains of thought. Without EAD, verbose models are unfairly penalized for their length, incentivizing "terse" generation that maximizes distinctness at the expense of detail.30

## ---

**6\. The Semantic Turn: Semantic Entropy and the Detection of Hallucination**

### **6.1 From Token Matching to Meaning Clustering**

The metrics discussed so far—MATTR, MTLD, Distinct-N—are fundamentally *syntactic*. They measure the variety of symbols. However, a model can be syntactically diverse while being semantically repetitive (tautology) or syntactically diverse while being factually wrong (hallucination). "Semantic Entropy," introduced by Kuhn et al. (2023), represents the shift to *semantic* auditing.39

The core insight is "Semantic Equivalence." In natural language, "Paris is the capital of France" and "The French capital is Paris" are different token sequences but identical semantic units. Standard entropy calculations (on tokens) would treat these as competing alternatives, indicating high uncertainty. Semantic Entropy clusters them together, revealing that the model is actually certain about the *fact*, just uncertain about the *phrasing*.40

### **6.2 The Bi-Directional Entailment Algorithm**

The calculation of Semantic Entropy involves:

1. **Sampling:** Generate $M$ sequences from the model for a single prompt.  
2. **Clustering:** Use a Natural Language Inference (NLI) model to check bidirectional entailment. If $A \\implies B$ and $B \\implies A$, they belong to the same semantic cluster $C$.  
3. Entropy Calculation: Compute the entropy over the probability mass of the clusters.

   $$SE \= \- \\sum\_{c \\in C} p(c) \\log p(c)$$  
* **Low Semantic Entropy:** The model generates many variations, but they all mean the same thing. (High Reliability).  
* **High Semantic Entropy:** The model generates variations that have mutually exclusive meanings (e.g., "The capital is Paris" vs. "The capital is Lyon"). (High Hallucination Risk).39

### **6.3 Semantic Energy and the Thermodynamic Law of Dignity**

Recent theoretical work extends this concept into "Semantic Physics," proposing the "Thermodynamic Law of Dignity." This framework posits that intelligent systems (biological or artificial) maintain a "semantic viscosity" that prevents the collapse of the semantic field.43

* **High Viscosity ($v\_D$):** Prevents runaway error propagation (hallucination) and maintains coherent flow (laminar semantic flow).  
* **Low Viscosity ($v\_D \\to 0$):** leads to "turbulent" dynamics (incoherence) or "singular" dynamics (repetitive loops).

"Semantic Energy" incorporates the model’s internal confidence (logits) into the entropy calculation, utilizing a Boltzmann-inspired distribution to detect "confabulations"—cases where the model is confident (low token entropy) but semantically fractured (high semantic entropy).41 This metric is currently the most advanced predictor of "factuality" in the Pattern Ledger.

### **6.4 Application in Code Generation**

In code generation, Semantic Entropy is adapted using "Symbolic Execution." Since NLI is ill-suited for code, researchers execute the generated code snippets on a set of test cases. Snippets that produce the same output for all inputs are clustered as "functionally equivalent."

* If a model generates 10 different code snippets (high syntactic diversity) but they all pass the same tests, Semantic Entropy is low (Good).  
* If the snippets produce different outputs or crash with different errors, Semantic Entropy is high, signaling that the model is guessing at the algorithm.45

## ---

**7\. The Thermodynamic and Information Limits: Compression Ratio**

### **7.1 Compression as a Proxy for Information Density**

The Compression Ratio serves as the thermodynamic gauge of the Pattern Ledger. It leverages the "Entropy-Memorization Law," which states that there is a linear correlation between the entropy (compressibility) of training data and the difficulty of memorizing it.47

$$\\text{Compression Ratio} \= \\frac{\\text{Size}(\\text{Compressed})}{\\text{Size}(\\text{Raw})}$$

* **Low Compression Ratio (High Compressibility):** Indicates redundancy. A text consisting of "A A A A..." is perfectly compressible.  
* **High Compression Ratio (Low Compressibility):** Indicates high information density (or random noise).

### **7.2 The Entropy-Memorization Law and Data Selection**

In the context of "Model Autophagy," compression ratios are used to curate training data. The "ZIP" method selects data subsets that exhibit low compression ratios (high diversity) to maximize the "effective information" fed to the model.49 Data that is too compressible is discarded as "empty calories" that contribute to overfitting without improving generalization. Conversely, data that is incompressible is often noise. The "Goldilocks zone" of compressibility defines high-quality human text.48

### **7.3 Optical Compression and Future Architectures**

DeepSeek’s "Optical Compression" represents a radical shift in this metric. By treating text as images (visual tokens) rather than discrete symbols, DeepSeek-OCR achieves compression ratios of 10:1 or 20:1 while maintaining semantic retrievability.50 This suggests that the future of the Pattern Ledger may involve "Visual Entropy"—measuring the diversity of the *visual representation* of text—to bypass the token-limit bottlenecks of current transformers.

### **7.4 Infinite Loop Detection**

In runtime environments, the Compression Ratio is the ultimate guardrail against infinite loops. A model stuck in a repetition loop (e.g., repeating the last sentence forever) will see its localized compression ratio drop precipitously. Monitoring systems track the sliding-window compression ratio; if it breaches a lower bound, the generation is forcibly terminated, identifying the output as a failure of the stopping criteria.33

## ---

**8\. Synthesis: The Pattern Ledger in the Age of Autophagy**

### **8.1 The Threat of Model Autophagy**

The synthesis of these metrics reveals the existential threat of "Model Autophagy" or "Model Collapse." As generative models saturate the internet with synthetic content, the "training commons" is being poisoned. Synthetic data is statistically "cleaner" and closer to the mode than human data; it lacks the "tails" of diversity.25

* **MATTR/MTLD Signal:** Recursive training leads to a secular decline in these metrics, indicating a shrinking vocabulary.  
* **Distinct-N Signal:** The loss of unique phraseology and the rise of "cliché" structures.  
* **Compression Signal:** Synthetic data becomes increasingly compressible (redundant) over generations.

The Pattern Ledger is the only tool capable of detecting this radioactive decay of the linguistic ecosystem.

### **8.2 The Unified Ledger Table**

The following table summarizes the operational role of each metric in the unified Pattern Ledger:

| Metric | Primary Dimension | Length Invariant? | Key Application | Failure Mode |
| :---- | :---- | :---- | :---- | :---- |
| **MATTR** | Lexical Density (Local) | Yes (Windowed) | Aphasia, Visual Drift, Code Quality | Inflated by gibberish/noise |
| **MTLD** | Lexical Stamina (Global) | Yes (Sequential) | Agglutinative Languages, Collapse Detection | Sensitive to threshold (0.72) |
| **Distinct-N** | Phrasal Variety | No (Needs EAD) | RLHF Alignment Tax, Repetition | Penalizes necessary technical repetition |
| **Semantic Entropy** | Epistemic Uncertainty | N/A (Cluster) | Hallucination Detection, Truthfulness | Computational Cost (NLI/Execution) |
| **Compression Ratio** | Information Density | Yes (Ratio) | Memorization, Infinite Loop Guardrail | Confuses randomness with diversity |
| **TTR** | Vocabulary Baseline | No | Historical Analysis (Short Texts) | Fails on Infinite Context (Heaps' Law) |

### **8.3 Conclusion: The Shift from Counting to Auditing**

The era of evaluating AI based on "perceived fluency" is over. The "Pattern Ledger" represents the rigorous, mathematical auditing of synthetic intelligence. It moves beyond the naive counting of words (TTR) to the measurement of "lexical stamina" (MTLD), "phrasal originality" (Distinct-N), and "epistemic integrity" (Semantic Entropy).

As models evolve towards "infinite context" and "recursive self-improvement," the Pattern Ledger must evolve with them. The integration of "Thermodynamic Dignity" and "Optical Compression" metrics points toward a future where we evaluate not just the text, but the *physics* of the intelligence that produced it. Until then, these six metrics remain our primary defense against the homogenization of the digital word.

#### **Works cited**

1. Measuring Lexical Diversity in Narrative Discourse of People With Aphasia \- PMC \- NIH, accessed on December 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3813439/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3813439/)  
2. Measuring Lexical Diversity for Discourse Analysis in Aphasia: Moving-Average Type–Token Ratio and Word Information Measure \- TalkBank, accessed on December 15, 2025, [https://talkbank.org/aphasia/publications/2020/Cunningham20.pdf](https://talkbank.org/aphasia/publications/2020/Cunningham20.pdf)  
3. accessed on December 15, 2025, [https://www.researchgate.net/publication/220469242\_Cutting\_the\_Gordian\_knot\_The\_moving-average\_type-token\_ratio\_MATTR\#:\~:text=The%20MATTR%20is%20the%20average,McCarthy%20%26%20Jarvis%2C%202010).](https://www.researchgate.net/publication/220469242_Cutting_the_Gordian_knot_The_moving-average_type-token_ratio_MATTR#:~:text=The%20MATTR%20is%20the%20average,McCarthy%20%26%20Jarvis%2C%202010\).)  
4. Cutting the Gordian knot: The moving-average type-token ratio (MATTR) | Request PDF, accessed on December 15, 2025, [https://www.researchgate.net/publication/220469242\_Cutting\_the\_Gordian\_knot\_The\_moving-average\_type-token\_ratio\_MATTR](https://www.researchgate.net/publication/220469242_Cutting_the_Gordian_knot_The_moving-average_type-token_ratio_MATTR)  
5. Back to basics: how measures of lexical diversity can help discriminate between CEFR levels \- CentAUR, accessed on December 15, 2025, [https://centaur.reading.ac.uk/54410/3/Backtobasics\_accepted.pdf](https://centaur.reading.ac.uk/54410/3/Backtobasics_accepted.pdf)  
6. Type Token Ratio in NLP \- Medium, accessed on December 15, 2025, [https://medium.com/@rajeswaridepala/empirical-laws-ttr-cc9f826d304d](https://medium.com/@rajeswaridepala/empirical-laws-ttr-cc9f826d304d)  
7. Scaling to Millions of Tokens with Efficient Long-Context LLM Training \- NVIDIA Developer, accessed on December 15, 2025, [https://developer.nvidia.com/blog/scaling-to-millions-of-tokens-with-efficient-long-context-llm-training/](https://developer.nvidia.com/blog/scaling-to-millions-of-tokens-with-efficient-long-context-llm-training/)  
8. Infinite Context Length in LLMs — The Next Big Advantage in AI | by Aloy Banerjee | Medium, accessed on December 15, 2025, [https://medium.com/@aloy.banerjee30/infinite-context-length-in-llms-the-next-big-advantage-in-ai-2550e9e6ce9b](https://medium.com/@aloy.banerjee30/infinite-context-length-in-llms-the-next-big-advantage-in-ai-2550e9e6ce9b)  
9. Zipf's and Heaps' Laws for Tokens and LLM-generated Texts \- ACL Anthology, accessed on December 15, 2025, [https://aclanthology.org/2025.findings-emnlp.837.pdf](https://aclanthology.org/2025.findings-emnlp.837.pdf)  
10. Psychometric Evaluation of Lexical Diversity Indices: Assessing Length Effects \- PMC \- NIH, accessed on December 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4490052/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4490052/)  
11. (PDF) Lexical diversity in bilingual speakers of Croatian and Italian \- ResearchGate, accessed on December 15, 2025, [https://www.researchgate.net/publication/338007160\_Lexical\_diversity\_in\_bilingual\_speakers\_of\_Croatian\_and\_Italian](https://www.researchgate.net/publication/338007160_Lexical_diversity_in_bilingual_speakers_of_Croatian_and_Italian)  
12. Transferability MATTRs: Towards Understanding Antecedents of Strategic Licensing \- Harvard Business School, accessed on December 15, 2025, [https://www.hbs.edu/ris/download.aspx?name=25-042.pdf](https://www.hbs.edu/ris/download.aspx?name=25-042.pdf)  
13. Adaptation to sensory–motor reflex perturbations is blind to the source of errors | JOV, accessed on December 15, 2025, [https://jov.arvojournals.org/article.aspx?articleid=2192148](https://jov.arvojournals.org/article.aspx?articleid=2192148)  
14. Movement speed effects on limb position drift \- PMC \- NIH, accessed on December 15, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10709820/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10709820/)  
15. Type-Token Ratio III: Language Clouds and a Rebel Quire \- The Voynich Temple, accessed on December 15, 2025, [https://herculeaf.wordpress.com/2019/07/18/type-token-ratio-iii-language-clouds-and-a-rebel-quire/](https://herculeaf.wordpress.com/2019/07/18/type-token-ratio-iii-language-clouds-and-a-rebel-quire/)  
16. Between Lines of Code: Unraveling the Distinct Patterns of Machine and Human Programmers \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2401.06461v1](https://arxiv.org/html/2401.06461v1)  
17. compute\_mattr: Compute the Moving-Average Type-Token Ratio (MATTR) \- rdrr.io, accessed on December 15, 2025, [https://rdrr.io/github/quanteda/quanteda.textstat/man/compute\_mattr.html](https://rdrr.io/github/quanteda/quanteda.textstat/man/compute_mattr.html)  
18. MTLD function \- Lexical diversity \- RDocumentation, accessed on December 15, 2025, [https://www.rdocumentation.org/packages/koRpus/versions/0.13-8/topics/MTLD](https://www.rdocumentation.org/packages/koRpus/versions/0.13-8/topics/MTLD)  
19. Example of measure of textual lexical diversity (MTLD) calculation using the Gramulator (2). \- ResearchGate, accessed on December 15, 2025, [https://www.researchgate.net/figure/Example-of-measure-of-textual-lexical-diversity-MTLD-calculation-using-the-Gramulator\_fig1\_272876507](https://www.researchgate.net/figure/Example-of-measure-of-textual-lexical-diversity-MTLD-calculation-using-the-Gramulator_fig1_272876507)  
20. Lexical Density, Lexical Diversity and Academic Vocabulary Use: Differences in Dissertation Abstracts \- ERIC, accessed on December 15, 2025, [https://files.eric.ed.gov/fulltext/EJ1406507.pdf](https://files.eric.ed.gov/fulltext/EJ1406507.pdf)  
21. Turkish as an immigrant and heritage language in the UK: Effects of exposure and age at onset of bilingualism on grammatical and \- Essex Research Repository, accessed on December 15, 2025, [https://repository.essex.ac.uk/22392/1/Karayayla\_January\_2018\_PhDthesis.pdf](https://repository.essex.ac.uk/22392/1/Karayayla_January_2018_PhDthesis.pdf)  
22. Measuring morphological complexity \- arXiv, accessed on December 15, 2025, [https://arxiv.org/pdf/2204.05056](https://arxiv.org/pdf/2204.05056)  
23. Constraints to neural machine translation quality, human and automated evaluation, and quality improvement across language pairs: A systematic literature review, accessed on December 15, 2025, [https://jrlt.ksu.edu.sa/sites/jrlt.ksu.edu.sa/files/users/user975/SI-1/JRLT%20Special%20Issue%20Dr%20AlGhamedi.pdf](https://jrlt.ksu.edu.sa/sites/jrlt.ksu.edu.sa/files/users/user975/SI-1/JRLT%20Special%20Issue%20Dr%20AlGhamedi.pdf)  
24. Other Workshops and Events (2025) \- ACL Anthology, accessed on December 15, 2025, [https://aclanthology.org/events/ws-2025/](https://aclanthology.org/events/ws-2025/)  
25. What Is Model Collapse? | Digital Bricks, accessed on December 15, 2025, [https://www.digitalbricks.ai/blog-posts/what-is-model-collapse](https://www.digitalbricks.ai/blog-posts/what-is-model-collapse)  
26. Future of AI Models: A Computational perspective on Model collapse \- arXiv, accessed on December 15, 2025, [https://www.arxiv.org/pdf/2511.05535](https://www.arxiv.org/pdf/2511.05535)  
27. models get dumb with no monitoring we risk humans \- GitHub Gist, accessed on December 15, 2025, [https://gist.github.com/bigsnarfdude/c05c5838498a97095dbb3158778f2e2e](https://gist.github.com/bigsnarfdude/c05c5838498a97095dbb3158778f2e2e)  
28. Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2510.05133v1](https://arxiv.org/html/2510.05133v1)  
29. Rethinking and Refining the Distinct Metric \- ACL Anthology, accessed on December 15, 2025, [https://aclanthology.org/2022.acl-short.86.pdf](https://aclanthology.org/2022.acl-short.86.pdf)  
30. arXiv:2202.13587v3 \[cs.CL\] 3 Apr 2022, accessed on December 15, 2025, [https://arxiv.org/pdf/2202.13587](https://arxiv.org/pdf/2202.13587)  
31. Evaluating the Evaluation of Diversity in Natural Language Generation \- ACL Anthology, accessed on December 15, 2025, [https://aclanthology.org/2021.eacl-main.25.pdf](https://aclanthology.org/2021.eacl-main.25.pdf)  
32. dwmeclust: a hybrid unsupervised framework for concept drift detection in high- dimensional medical, accessed on December 15, 2025, [https://www.jatit.org/volumes/Vol103No20/20Vol103No20.pdf](https://www.jatit.org/volumes/Vol103No20/20Vol103No20.pdf)  
33. When Do LLMs Stop Talking? Understanding Stopping Criteria | by HafsaOuaj \- Medium, accessed on December 15, 2025, [https://medium.com/@hafsaouaj/when-do-llms-stop-talking-understanding-stopping-criteria-6e96ef01835c](https://medium.com/@hafsaouaj/when-do-llms-stop-talking-understanding-stopping-criteria-6e96ef01835c)  
34. Combining Large and Small LLMs to Boost Inference Time and Quality, accessed on December 15, 2025, [https://towardsdatascience.com/combining-large-and-small-llms-for-inference-time-and-quality-boosts-1779b6b5100b/](https://towardsdatascience.com/combining-large-and-small-llms-for-inference-time-and-quality-boosts-1779b6b5100b/)  
35. Diverse Preference Learning for Capabilities and Alignment \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2511.08594v1](https://arxiv.org/html/2511.08594v1)  
36. Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity, accessed on December 15, 2025, [https://www.researchgate.net/publication/396095169\_Verbalized\_Sampling\_How\_to\_Mitigate\_Mode\_Collapse\_and\_Unlock\_LLM\_Diversity](https://www.researchgate.net/publication/396095169_Verbalized_Sampling_How_to_Mitigate_Mode_Collapse_and_Unlock_LLM_Diversity)  
37. Evaluating the Diversity and Quality of LLM Generated Content \- OpenReview, accessed on December 15, 2025, [https://openreview.net/pdf?id=O7bF6nlSOD](https://openreview.net/pdf?id=O7bF6nlSOD)  
38. Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity \- Rivista AI, accessed on December 15, 2025, [https://www.rivista.ai/wp-content/uploads/2025/10/2510.01171v3-1.pdf](https://www.rivista.ai/wp-content/uploads/2025/10/2510.01171v3-1.pdf)  
39. Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs | alphaXiv, accessed on December 15, 2025, [https://www.alphaxiv.org/overview/2406.15927v1](https://www.alphaxiv.org/overview/2406.15927v1)  
40. Linguistic Invariances for Uncertainty Estimation in Natural Language Generation \- Sebastian Farquhar, accessed on December 15, 2025, [https://sebastianfarquhar.com/assets/papers/kuhnSemantic2023.pdf](https://sebastianfarquhar.com/assets/papers/kuhnSemantic2023.pdf)  
41. Semantic Energy: Detecting LLM Hallucination Beyond Entropy \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2508.14496v3](https://arxiv.org/html/2508.14496v3)  
42. What Are AI Hallucinations? \[+ Protection Tips\] \- Palo Alto Networks, accessed on December 15, 2025, [https://www.paloaltonetworks.com/cyberpedia/what-are-ai-hallucinations](https://www.paloaltonetworks.com/cyberpedia/what-are-ai-hallucinations)  
43. Bio-Semantic Physics: The Thermodynamic Law of Dignity in Neural Systems, accessed on December 15, 2025, [https://www.researchgate.net/publication/397870842\_Bio-Semantic\_Physics\_The\_Thermodynamic\_Law\_of\_Dignity\_in\_Neural\_Systems](https://www.researchgate.net/publication/397870842_Bio-Semantic_Physics_The_Thermodynamic_Law_of_Dignity_in_Neural_Systems)  
44. Semantic Energy: Detecting LLM Hallucination Beyond Entropy \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2508.14496v1](https://arxiv.org/html/2508.14496v1)  
45. Assessing Correctness in LLM-Based Code Generation via Uncertainty Estimation \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2502.11620v1](https://arxiv.org/html/2502.11620v1)  
46. IMPROVING UNCERTAINTY ESTIMATION THROUGH SEMANTICALLY DIVERSE LANGUAGE GENERATION \- ICLR Proceedings, accessed on December 15, 2025, [https://proceedings.iclr.cc/paper\_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)  
47. Entropy Proxy for LLM Memorization Score \- OpenReview, accessed on December 15, 2025, [https://openreview.net/forum?id=9qA5cpZmJh](https://openreview.net/forum?id=9qA5cpZmJh)  
48. Entropy Law: The Story Behind Data Compression and LLM Performance \- ResearchGate, accessed on December 15, 2025, [https://www.researchgate.net/publication/382111467\_Entropy\_Law\_The\_Story\_Behind\_Data\_Compression\_and\_LLM\_Performance](https://www.researchgate.net/publication/382111467_Entropy_Law_The_Story_Behind_Data_Compression_and_LLM_Performance)  
49. Entropy Law: The Story Behind Data Compression and LLM Performance \- arXiv, accessed on December 15, 2025, [https://arxiv.org/html/2407.06645v1](https://arxiv.org/html/2407.06645v1)  
50. TAI \#176: DeepSeek's Optical Compression: A Cheaper OCR or a New Path for LLMs?, accessed on December 15, 2025, [https://towardsai.net/p/machine-learning/tai-176-deepseeks-optical-compression-a-cheaper-ocr-or-a-new-path-for-llms](https://towardsai.net/p/machine-learning/tai-176-deepseeks-optical-compression-a-cheaper-ocr-or-a-new-path-for-llms)  
51. Daily Papers \- Hugging Face, accessed on December 15, 2025, [https://huggingface.co/papers?q=Neural%20codec%20language%20models](https://huggingface.co/papers?q=Neural+codec+language+models)