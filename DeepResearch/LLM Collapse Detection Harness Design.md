# **Lexical Impoverishment as a Failure Precursor in LLM Output: Robust Collapse Detection via Lexical, Syntactic, and Semantic Stagnation Signals**

## **1\. Introduction: The Phenomenology of Model Collapse**

The rapid and pervasive deployment of Large Language Models (LLMs) has precipitated a foundational stability crisis in generative artificial intelligence known as "model collapse." This degenerative phenomenon, wherein models recursively trained on synthetic data or operating within extended generation loops exhibit a progressive loss of variance, factual reliability, and structural complexity, represents an existential threat to the long-term viability of automated text generation systems.1 As generative systems increasingly consume their own outputs—a process described as "model autophagy"—the distribution of generated text converges inexorably toward a point estimate with diminished variance, effectively shearing off the "tails" of the original probability distribution where rare events, nuanced expression, and creative variability reside.1

This report operationalizes the hypothesis that lexical impoverishment functions not merely as a symptom but as a distinct, measurable early warning system for this collapse. By synthesizing advanced metrics for lexical diversity (length-robust measures like MATTR and MTLD), syntactic depth (Mean Dependency Distance), and semantic entropy, we propose the construction of a diagnostic harness capable of identifying the "critical slowing down" of a model's generative capacity before catastrophic failure occurs.4 This investigation moves beyond simple perplexity monitoring, which can be misleadingly low during repetitive loops, to a multi-dimensional analysis of the text's information density and structural integrity.

### **1.1 The Mechanism of Neural Degeneration**

To effectively detect collapse, one must first understand the dynamical systems governing autoregressive generation. LLMs generate text by sampling from a probability distribution conditioned on the preceding context. In ideal scenarios, this process maintains the statistical richness of the training distribution. However, during recursive generation or long-context inference, the model is prone to "attractor states"—stable configurations where the probability mass concentrates on a narrow set of tokens or sequences.6

Model collapse is fundamentally a distributional shift. Research indicates that in the early stages of recursive training or extended generation, information is lost primarily at the tails of the distribution.1 These tails represent low-probability but high-information events: rare words, complex syntactic structures, and creative deviations. As the model maximizes the joint probability of the sequence—often exacerbated by decoding strategies like greedy search or beam search—it gravitates toward the "mode" of the distribution.2 This "mode-seeking" behavior results in outputs that are locally coherent but globally repetitive and generic. We observe a "self-reinforcement effect," where the generation of a repetitive phrase increases the probability of its recurrence, creating a feedback loop that traps the model in a local minimum of semantic diversity.10 This is distinct from "mode collapse" in GANs, though related; in autoregressive models, it manifests as a sequence of outputs that exhibit decreasing entropy and increasing predictability.12

### **1.2 Critical Slowing Down as a Diagnostic Analogy**

Dynamical systems theory offers the concept of "critical slowing down" (CSD) as a precursor to phase transitions or tipping points.4 In ecological and physical systems, as a system approaches a collapse point, its ability to recover from perturbations decreases, leading to increased autocorrelation and variance in state variables.4

Applying this to LLMs, we posit that "lexical impoverishment" is the linguistic equivalent of CSD. Before a model enters a hard failure mode (e.g., printing the same word infinitely), it likely exhibits a "soft" failure phase characterized by three distinct signals:

1. **Reduced Vocabulary Turnover:** The rate at which new types (unique words) are introduced slows down significantly compared to the expected rate for the genre.  
2. **Syntactic Simplification:** Sentence structures become shorter and less nested to minimize computational or "cognitive" load, mirroring the minimization of dependency distance observed in human language processing under load.15  
3. **Semantic Stagnation:** The trajectory of the text in embedding space begins to loop or converge, even if surface-level lexis varies slightly.17

The detection of these signals requires a rigorous, reproducible diagnostic harness that avoids the "text-length dependency problem"—where metrics like Type-Token Ratio (TTR) naturally decline with length—and effectively distinguishes between pathological repetition and genre-appropriate redundancy (e.g., legal or technical text).19

## **2\. Lexical Diversity Metrics: Beyond Type-Token Ratio**

The most immediate signal of impoverishment is a drop in lexical diversity. However, traditional metrics like Type-Token Ratio (TTR) are notoriously unreliable for streaming or variable-length text because TTR naturally decreases as text length increases—a phenomenon known as the "text-length dependency problem".19 A high TTR in a short segment is meaningless, and a low TTR in a long document is expected. For a robust diagnostic harness, we must employ length-invariant metrics.

### **2.1 The Limitations of Traditional Indices**

Standard TTR is calculated as $V/N$, where $V$ is the number of types (unique words) and $N$ is the number of tokens (total words). As a text extends, the probability of encountering a new word naturally diminishes according to Heaps' Law ($V\_R(n) \= Kn^\\beta$). Therefore, monitoring raw TTR in a streaming context inevitably triggers false alarms as the context window grows.19

To operationalize robust detection, we analyze two primary algorithms that normalize for length: **MATTR** (Moving Average Type-Token Ratio) and **MTLD** (Measure of Textual Lexical Diversity).

### **2.2 Moving Average Type-Token Ratio (MATTR)**

MATTR addresses the length dependency by utilizing a fixed-size sliding window to calculate diversity locally, providing a continuous signal of the text's "lexical density" at any given moment.21

#### **2.2.1 Mathematical Formulation and Mechanism**

For a text $T$ consisting of $N$ tokens, and a window size $w$, MATTR is calculated by averaging the TTR of every possible overlapping window of size $w$:

$$\\text{MATTR}(w) \= \\frac{1}{N-w+1} \\sum\_{i=1}^{N-w+1} \\frac{V(T\_{i:i+w-1})}{w}$$  
Where $V(T\_{i:i+w-1})$ represents the count of unique types within the window starting at index $i$ and ending at $i+w-1$.22

The selection of the window size $w$ is a critical hyperparameter. Research indicates that a window size between 25 and 50 tokens is optimal for capturing local diversity fluctuations in English text.23 In a streaming LLM context, MATTR acts as a rolling monitor. If the model enters a repetitive loop, the local windowed TTR will drop precipitously, even if the global TTR remains stable due to earlier diversity.

#### **2.2.2 Advantages for Stream Monitoring**

The primary advantage of MATTR in a diagnostic harness is its independence from the total length of the generation. Whether the model has generated 100 tokens or 10,000, the MATTR-50 score remains comparable, reflecting the *current* state of lexical richness.24 This property makes it ideal for real-time dashboarding and "check engine" alerts. Furthermore, MATTR is computationally efficient, calculable in $O(N)$ time with appropriate data structures (e.g., sliding window frequency maps).25

### **2.3 Measure of Textual Lexical Diversity (MTLD)**

While MATTR measures local density, MTLD provides a global assessment of lexical complexity by measuring the average length of segments that maintain a certain diversity threshold.21

#### **2.3.1 Algorithmic Logic**

MTLD employs a sequential analysis approach. The algorithm iterates through the text, maintaining a running TTR for the current segment. As the segment grows, the TTR naturally drops. When the TTR drops below a specific pre-defined threshold (typically 0.72), the algorithm marks a "factor," resets the count, and begins a new segment.28

The final MTLD score is calculated as:

$$\\text{MTLD} \= \\frac{N}{\\text{Factors}}$$  
To ensure robustness, the calculation is performed bidirectionally (forward and reverse), and the results are averaged. This bidirectional pass mitigates edge effects at the end of the text.27

#### **2.3.2 Applicability to Collapse Detection**

MTLD correlates strongly with human judgments of proficiency and text quality.27 In the context of model collapse, a decreasing MTLD score across successive generation sessions indicates that the model is sustaining diversity for shorter and shorter durations before exhausting its active vocabulary. Unlike MATTR, which is a local signal, MTLD is best employed as a batch metric—calculated on completed paragraphs or distinct turns in a conversation—to assess the overall "lexical health" of the model's output.29

### **2.4 The Hypergeometric Distribution D (HD-D)**

For forensic analysis where computational cost is less of a constraint, the Hypergeometric Distribution D (HD-D) offers a statistically rigorous alternative. HD-D calculates the probability that any type drawn from the text would be found in a random sample of fixed size (usually 42 tokens).19

$$\\text{HD-D} \= \\sum\_{t \\in V} \\left( 1 \- \\frac{\\binom{N-f(t)}{42}}{\\binom{N}{42}} \\right)$$  
Where $f(t)$ is the frequency of type $t$ in the text. HD-D represents the sum of probabilities for finding each type in a random draw. While less intuitive for real-time monitoring than MATTR, HD-D is highly resistant to sample size effects and provides a robust baseline for comparing the vocabulary distribution of a model against a human reference corpus.19

### **2.5 Comparative Analysis for Harness Design**

| Metric | Length Robustness | Computational Complexity | Sensitivity to Local Loops | Recommended Use Case |
| :---- | :---- | :---- | :---- | :---- |
| **TTR** | Low | Low | Low | **Baseline Only** (Do not use for alerts) |
| **MATTR** | High | Medium (Linear w/ Window) | High | **Real-time Stream Monitoring** |
| **MTLD** | High | Medium | Medium | **Batch/Segment Analysis** |
| **HD-D** | High | High | Low | **Offline Forensic Analysis** |

**Conclusion on Lexical Metrics:** The diagnostic harness must utilize **MATTR with a window size of 50 tokens** as the primary signal for real-time collapse detection. A sudden, sustained drop in the rolling MATTR score serves as the first "red flag" that the model has entered a repetitive attractor state. **MTLD** should be employed for post-generation quality assurance, ensuring that the global lexical structure remains intact.21

## **3\. Syntactic Complexity: Detecting Structural Simplification**

Model collapse often manifests as syntactic simplification before lexical repetition becomes obvious. As the model's internal uncertainty grows or as it converges on a mode, it reverts to simple, high-frequency sentence structures to minimize prediction error, abandoning complex nested clauses, passive voice, or long-distance dependencies. This "structural impoverishment" is a critical, often overlooked, precursor to failure.

### **3.1 Dependency Distance as a Cognitive Proxy**

To quantify structural complexity, we turn to Dependency Grammar and the concept of **Dependency Distance (DD)**. In a dependency tree, the DD is defined as the linear distance (number of intervening words) between a head word (governor) and its dependent.15

#### **3.1.1 Mean Dependency Distance (MDD)**

The Mean Dependency Distance (MDD) of a sentence is the average absolute distance of all dependency links within it.

$$\\text{MDD} \= \\frac{1}{n-1} \\sum\_{i=1}^{n-1} |DD\_i|$$

Where $n$ is the sentence length and $DD\_i$ is the dependency distance of the $i$-th link.32  
Research in psycholinguistics suggests that human language processing is constrained by working memory, leading to a universal tendency toward **Dependency Distance Minimization (DDM)**.16 Humans prefer to keep related words close together to reduce cognitive load. However, competent, expert-level text (e.g., academic papers, complex narratives) often exhibits higher MDD due to the necessity of expressing complex relationships.34

#### **3.1.2 The Collapse Signal**

In a state of degeneration, an LLM will aggressively minimize MDD beyond the standard human baseline. The model, seeking the path of least resistance (highest probability), will default to adjacent dependencies (e.g., "The cat sat. The dog ran."), driving the MDD toward 1.0.35 A collapse in MDD indicates a regression to simplistic, linear chain-like generation, characteristic of low-capability models or those trapped in a simplification loop.

### **3.2 Syntactic Stagnation: The Variance Signal**

While a low MDD is a warning sign, a more specific indicator of collapse is the loss of **Syntactic Variance**. A healthy natural language stream exhibits a "pulse" of complexity—sentences vary in length and structure, mixing short, punchy statements with longer, hypotactic constructions.

A collapsing model often exhibits "syntactic locking," where it produces a sequence of sentences with nearly identical structural complexity. By monitoring the **variance of MDD** across a sliding window of sentences, we can detect this stagnation. If the variance approaches zero, it indicates that the model is repeating a fixed structural template (e.g., Subject-Verb-Object), even if the words themselves are changing.34 This "structural looping" is a subtle form of mode collapse that purely lexical metrics might miss.

### **3.3 Clause Density and Tree Depth**

To further robustify the syntactic signal, the harness should incorporate secondary metrics derived from the dependency parse:

* **Tree Depth (Height):** The maximum number of edges from the root of the dependency tree to the furthest leaf. A reduction in average tree depth signals a loss of subordination and nesting capabilities, mirroring the "flattening" of narrative structure.31  
* **Clause Density:** Calculated as the ratio of clauses to T-units (main clauses plus any attached subordinate clauses). A drop in clause density indicates the model is failing to construct complex logical relationships, reverting to simple coordination (using "and" repeatedly) rather than subordination (using "because," "although," "while").37

### **3.4 Implementation Strategy with spaCy**

The spaCy NLP library provides an industrial-strength framework for extracting these metrics efficiently in Python. The diagnostic harness can integrate a spaCy pipeline to parse the generated text stream in near real-time.39

#### **3.4.1 Calculation Logic**

1. **Stream Interception:** The harness buffers the LLM output until a sentence boundary is detected.  
2. **Parsing:** The sentence is passed to nlp(), generating a Doc object with a dependency tree.  
3. **Traversal:** The harness iterates through doc.tokens. For each token, if token.head is not the token itself (root), the distance abs(token.i \- token.head.i) is calculated.41  
4. **Aggregation:** The MDD for the sentence is computed. Simultaneously, the maximum depth is determined by recursively traversing token.children.  
5. **Monitoring:** The harness updates a rolling buffer of the last $K$ sentences (e.g., $K=10$). It calculates the mean and variance of MDD and Tree Depth within this window.  
6. **Alerting:** If the rolling variance of MDD falls below a task-conditioned threshold (e.g., $\\sigma^2 \< 0.1$), or if the mean MDD drops significantly below the genre baseline, a "Syntactic Collapse" warning is triggered.43

This syntactic monitoring layer provides a crucial orthogonal signal to lexical metrics, catching failure modes where the model maintains vocabulary size but loses the ability to form coherent, complex thoughts.

## **4\. Semantic Stagnation: The Fixed Point Problem**

Lexical and syntactic metrics, while powerful, can be "gamed" by a model that generates distinct words in complex structures but says essentially nothing new (e.g., "The rapid fox jumped. The quick vixen leaped."). This phenomenon, where the model loops through paraphrases without advancing the narrative or informational state, is known as "semantic stagnation." To detect this, we must measure the trajectory of the generation in semantic space.

### **4.1 The Semantic Fixed Point Hypothesis**

Dynamical systems theory applied to LLMs suggests that iterative generation can lead to "attractors" or "semantic fixed points"—configurations where the input and output become semantically identical, effectively halting the flow of information.6 In a healthy generation, the narrative arc or logical progression ensures that subsequent sentences add information (entropy). In a pre-collapse state, the "semantic velocity" approaches zero.18

### **4.2 Semantic Entropy and Clustering**

Standard entropy measures based on token probabilities (naive entropy) are insufficient for detecting semantic stagnation because they cannot distinguish between uncertainty over distinct meanings and uncertainty over synonyms (e.g., "glad" vs. "happy"). A model might have high naive entropy (uncertain about which word to choose) but zero semantic entropy (all choices mean the same thing).17

**Semantic Entropy (SE)** addresses this by grouping generated sequences into semantic clusters using bidirectional entailment (checking if sequence A implies sequence B and vice versa). SE is then calculated over the probability mass of these clusters rather than individual tokens.17

* **Harness Application:** In a monitoring context, the harness can periodically sample multiple short continuations from the current state (using a "lookahead" buffer). If all sampled continuations cluster into the same semantic meaning despite lexical variation, the model has likely reached a "collapsed prediction" state, indicating a lack of generative diversity.45

### **4.3 Embedding-Based Drift Detection**

For a more lightweight, continuous signal, we can utilize pre-trained embedding models (e.g., SBERT, RoBERTa) to map the trajectory of the generation.46

#### **4.3.1 Cosine Similarity Monitoring**

The harness calculates the cosine similarity between the embedding of the current sentence and the embeddings of the previous $N$ sentences.48

$$\\text{Sim}(A, B) \= \\frac{A \\cdot B}{\\|A\\| \\|B\\|}$$

If the similarity score remains consistently high (e.g., $\> 0.85$) across a sliding window, it indicates that the model is looping or rephrasing the same content.50 This metric detects "stagnation," which is distinct from "drift." Drift implies moving away from the prompt's intent (low similarity to context); stagnation implies moving nowhere (high similarity to self).52

#### **4.3.2 Euclidean Distance for Magnitude Sensitivity**

Recent research suggests that for detecting subtle semantic shifts or collapses, **Euclidean distance** on normalized embeddings may outperform Cosine similarity. Euclidean distance is sensitive to magnitude changes in the vector space that Cosine similarity might miss due to high-dimensional warping.53

* **Recommendation:** The harness should compute both metrics. A divergence where Cosine similarity remains high but Euclidean distance fluctuates might indicate "micro-drifts" or hallucination, whereas stability in both metrics confirms rigid stagnation.

### **4.4 The Semantic Velocity Metric**

We can define a derived metric, "Semantic Velocity" ($V\_{sem}$), as the distance traveled in semantic space per unit of text length.18

$$V\_{sem} \= \\frac{\\text{Dist}(E\_t, E\_{t-1})}{\\text{Length}(S\_t)}$$

Where $E\_t$ is the embedding of the current sentence $S\_t$. A $V\_{sem}$ approaching zero is a definitive signature of a semantic fixed point. By monitoring the rolling average of $V\_{sem}$, the harness can detect when the model's narrative momentum has stalled, triggering an intervention before the user perceives the repetitive loop.

## **5\. Entropy Pathways: Logprobs vs. Compression**

To operationalize the detection of "knowledge collapse" or hallucination, we must look at the information content of the output. This can be approached through two pathways: the "white-box" method utilizing model log-probabilities, and the "black-box" method utilizing compression algorithms as entropy proxies.

### **5.1 The White-Box Approach: Token Log-Probabilities**

When the LLM's API exposes token log-probabilities (logprobs), they provide a direct measure of the model's internal uncertainty.54

#### **5.1.1 Confident Hallucination vs. Derailment**

* **Low Entropy \+ Error:** If a model exhibits very low entropy (high confidence/high logprobs) but produces repetitive or nonsensical text, it indicates "confident hallucination" or mode collapse. The model has converged on a degenerate solution and is "sure" of its error.56  
* **High Entropy Spikes:** Conversely, sudden spikes in entropy often precede a "derailment," where the model loses coherence and begins to output gibberish. The "Entropy-Guided Refinement" loop suggests monitoring for these spikes to trigger corrective re-sampling.58

#### **5.1.2 Perplexity Monitoring**

The harness should track the Perplexity (PPL) of the generated stream, calculated as the exponentiated negative average log-likelihood:

$$\\text{PPL} \= \\exp\\left(-\\frac{1}{N}\\sum\_{i=1}^N \\log P(x\_i|x\_{\<i})\\right)$$

In a collapse scenario, perplexity often exhibits a counter-intuitive behavior: it drops monotonically as the model enters a repetitive loop (predicting its own repetition is easy), then may spike if the model breaks into incoherence.45 A purely monotonic decrease in PPL, combined with low lexical diversity, is a strong signature of self-reinforcing collapse.

### **5.2 The Black-Box Approach: Compression as Entropy Proxy**

In many production environments, logprobs are unavailable due to API restrictions. In these cases, compression algorithms offer a powerful proxy for entropy, grounded in the theory of Kolmogorov Complexity.60

#### **5.2.1 Normalized Compression Distance (NCD)**

The Kolmogorov complexity $K(x)$ of a string is the length of the shortest program that can produce it. Since $K(x)$ is uncomputable, we use real-world compressors like gzip or zlib to approximate it. The Normalized Compression Distance (NCD) measures the similarity between two strings $x$ and $y$ based on their compressibility 62:

$$\\text{NCD}(x, y) \= \\frac{C(xy) \- \\min(C(x), C(y))}{\\max(C(x), C(y))}$$

Where $C(x)$ is the compressed size of string $x$. NCD can be used to detect novelty; if the NCD between the current buffer and the previous buffer is near zero, the new text adds almost no information.64

#### **5.2.2 Compression Ratio as a Stagnation Signal**

A simpler metric for the harness is the raw Compression Ratio ($R\_c$) of the output stream.

$$R\_c \= \\frac{|T|}{|C(T)|}$$

A text stream entering a repetitive loop becomes highly compressible. If the gzip compression ratio of the last $N$ tokens rises significantly above the baseline for that genre (e.g., from 3.0 to 10.0), it is a strong indicator of low information density.60

#### **5.2.3 Implementation with zlib**

Using Python's zlib library, the harness can compute the "bits per character" of the output stream in real-time.

Python

import zlib  
def calculate\_entropy\_proxy(text):  
    compressed \= zlib.compress(text.encode('utf-8'))  
    return len(text) / len(compressed)

This method is computationally inexpensive and completely model-agnostic, making it a robust "fallback" signal when logprobs are not accessible.65

## **6\. Diagnostic Harness Architecture and Implementation**

Based on the theoretical and metric analysis, we propose the design of a reproducible CollapseHarness. This system operates as a middleware layer, intercepting the LLM generation stream to compute "Vital Signs" and trigger interventions.

### **6.1 Architecture Overview**

The harness consists of three primary modules:

1. **Stream Monitor:** Intercepts tokens in real-time, buffering them into analysis windows.  
2. **Metric Engine:** Computes the suite of Lexical, Syntactic, Semantic, and Entropy metrics.  
3. **Decision Controller:** Evaluates metrics against dynamic, task-conditioned thresholds to trigger alerts or stop generation.

### **6.2 Implementation Specifications**

#### **6.2.1 Data Structures**

The harness utilizes sliding windows to manage state.

* **Short-Term Window ($W\_{short}$):** 50 tokens. Used for MATTR and local repetition checks.  
* **Long-Term Window ($W\_{long}$):** 500 tokens (or full session). Used for drift detection and global MTLD.  
* **Semantic Buffer:** Stores embeddings of the last $K$ sentences for cosine similarity tracking.

#### **6.2.2 Metric Calculation Pipeline (Python)**

The implementation leverages spaCy for syntax, lexical\_diversity for MATTR, sentence-transformers for semantics, and zlib for entropy.

Python

import spacy  
import zlib  
import numpy as np  
from lexical\_diversity import lex\_div as ld  
from sentence\_transformers import SentenceTransformer, util

class CollapseHarness:  
    def \_\_init\_\_(self, genre\_profile='general'):  
        self.nlp \= spacy.load("en\_core\_web\_sm")  
        self.embedder \= SentenceTransformer('all-MiniLM-L6-v2')  
        self.token\_buffer \=  
        self.sentence\_buffer \=  
        self.embedding\_history \=  
        self.profile \= self.\_load\_profile(genre\_profile)

    def \_load\_profile(self, genre):  
        \# Task-Conditioned Thresholds \[68\]  
        profiles \= {  
            'creative': {'mattr\_min': 0.75, 'mdd\_var\_min': 0.2, 'compression\_max': 3.0},  
            'technical': {'mattr\_min': 0.50, 'mdd\_var\_min': 0.1, 'compression\_max': 5.0}  
        }  
        return profiles.get(genre, profiles\['technical'\]) \# Default to permissive

    def update(self, new\_text\_chunk):  
        self.token\_buffer.extend(ld.tokenize(new\_text\_chunk))  
          
        \# 1\. Lexical: MATTR   
        \# Calculate on last 50 tokens  
        recent\_tokens \= self.token\_buffer\[-50:\]  
        if len(recent\_tokens) \>= 50:  
            mattr\_score \= ld.mattr(recent\_tokens, window\_length=25)  
            self.\_check\_lexical(mattr\_score)

        \# 2\. Entropy: Compression \[61\]  
        text\_window \= " ".join(self.token\_buffer\[-100:\])  
        if len(text\_window) \> 0:  
            compressed \= zlib.compress(text\_window.encode('utf-8'))  
            compression\_ratio \= len(text\_window) / len(compressed)  
            self.\_check\_entropy(compression\_ratio)

        \# 3\. Syntactic & Semantic (Sentence-Level)  
        doc \= self.nlp(new\_text\_chunk)  
        if doc.has\_annotation("SENT\_START"): \# Process completed sentences  
             for sent in doc.sents:  
                 self.\_analyze\_sentence(sent)

    def \_analyze\_sentence(self, sent):  
        \# Syntactic: MDD \[42\]  
        distances \= \[abs(t.i \- t.head.i) for t in sent if t.head\!= t\]  
        mdd \= np.mean(distances) if distances else 0  
          
        \# Semantic: Embedding \[49\]  
        emb \= self.embedder.encode(sent.text)  
        if self.embedding\_history:  
            sim \= util.cos\_sim(emb, self.embedding\_history\[-1\]).item()  
            self.\_check\_semantic(sim)  
        self.embedding\_history.append(emb)

### **6.3 Addressing Genre False Positives: Task-Conditioned Thresholds**

A critical requirement is avoiding false positives. A legal contract requires repetition; a poem does not. The harness addresses this via **Task-Conditioned Thresholds**.68

#### **6.3.1 Dynamic Baselining via Z-Scores**

Rather than relying solely on static thresholds (e.g., "MATTR \< 0.7"), the harness implements Z-Score Normalization relative to the model's own recent performance within the current session.

$$Z \= \\frac{x\_t \- \\mu\_{t-k:t}}{\\sigma\_{t-k:t}}$$

The harness maintains a rolling mean ($\\mu$) and standard deviation ($\\sigma$) for each metric. If the current MATTR score ($x\_t$) drops more than 3 standard deviations below the rolling mean ($Z \< \-3$), it triggers an alert regardless of the absolute value.70 This allows the system to adapt to the baseline repetition rate of the specific document being generated, filtering out genre-intrinsic redundancy.

#### **6.3.2 Genre Profiles**

The harness also accepts a genre\_profile configuration that sets the initial sensitivity:

* **Narrative Profile:** High penalties for repetition, high requirement for lexical diversity. (High MATTR, High Semantic Velocity).  
* **Technical/Instructional Profile:** Lower penalties for noun-phrase repetition, strict syntactic requirements. (Lower MATTR, Low MDD Variance tolerance).72

### **6.4 Reproducibility and Validation**

To ensure the harness is scientifically reproducible, validation must be performed on standardized datasets known to induce collapse.

* **Validation Data:** The **WikiText-2** dataset, recursively fine-tuned to induce collapse, serves as the standard "positive control" for degeneration.1 The **FActScore** benchmark provides a ground truth for measuring semantic drift.52  
* **Success Metric:** The effectiveness of the harness should be evaluated using the **Area Under the Receiver Operating Characteristic Curve (AUC-ROC)**, measuring its ability to distinguish between "healthy" generation and the "pre-collapse" phase *before* total nonsense is produced.57

## **7\. Implications and Future Directions**

The implementation of this diagnostic harness has profound implications for the reliability of Generative AI. By detecting the "soft" signals of lexical impoverishment and syntactic simplification, we can intervene before the model hallucinates or loops.

### **7.1 Entropy-Guided Refinement**

Integrating this harness enables a closed-loop control system known as "Entropy-Guided Refinement".58 When the harness detects a dip in MATTR or a spike in compression ratio, it can trigger automated corrective actions:

1. **Temperature Injection:** Temporarily increasing the sampling temperature to force diversity and break the attractor state.58  
2. **Backtracking:** Resetting the generation stream to a state before the collapse metrics crossed the Z-score threshold.  
3. **Verbalized Sampling:** Prompting the model to explicitly list alternatives before selecting one, forcing it to re-evaluate the probability distribution and break the "mode collapse" cycle.74

### **7.2 Conclusion**

The "Lexical Impoverishment" hypothesis is supported by a convergence of evidence from information theory, linguistics, and dynamical systems. As LLMs approach failure states, they shed complexity across all dimensions: they lose the "tails" of the vocabulary (lexical collapse), they abandon complex nested structures (syntactic collapse), and they cease to traverse new semantic space (semantic stagnation). By instrumenting a diagnostic harness that monitors these three axes using length-robust (MATTR, MTLD) and task-conditioned metrics, we create a sophisticated "Check Engine" light for LLMs. This research provides the architectural blueprint for building that safeguard, ensuring that as models scale, our ability to evaluate and control their stability keeps pace.

## **Table 1: Summary of Proposed Diagnostic Metrics**

| Dimension | Metric | Algorithm/Proxy | Collapse Signal | Threshold Strategy |
| :---- | :---- | :---- | :---- | :---- |
| **Lexical** | Diversity Density | **MATTR-50** | Sudden drop in rolling average | Z-Score \< \-3.0 (Adaptive) |
| **Lexical** | Global Richness | **MTLD** | Monotonic decrease over sessions | Batch comparison \< 0.72 |
| **Syntactic** | Structural Depth | **Mean Dep. Dist. (MDD)** | Convergence to \~1.0 (Linearity) | Profile-based (Technical vs. Creative) |
| **Syntactic** | Variance | **MDD Variance** | Variance $\\to 0$ (Structural Locking) | Variance \< 0.1 |
| **Semantic** | Stagnation | **Cosine Similarity** | Sim $\> 0.85$ over window (Looping) | Rolling Window max |
| **Entropy** | Uncertainty | **Compression Ratio ($R\_c$)** | Ratio $\> 5.0$ (High Redundancy) | Upper bound check |
| **Entropy** | Confidence | **Perplexity (PPL)** | Monotonic drop (False Confidence) | Deviation from Training PPL |

#### **Works cited**

1. Machine-generated text detection prevents language model collapse \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2502.15654v1](https://arxiv.org/html/2502.15654v1)  
2. Machine-generated text detection prevents language model collapse \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2502.15654v6](https://arxiv.org/html/2502.15654v6)  
3. AI Model Collapse: Causes, Early Signs, and How to Prevent It \- ProjectPro, accessed on December 14, 2025, [https://www.projectpro.io/article/ai-model-collapse/1177](https://www.projectpro.io/article/ai-model-collapse/1177)  
4. Critical slowing down as early warning for the onset of collapse in mutualistic communities, accessed on December 14, 2025, [https://www.pnas.org/doi/10.1073/pnas.1406326111](https://www.pnas.org/doi/10.1073/pnas.1406326111)  
5. Early-warning signals for critical transitions, accessed on December 14, 2025, [https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf](https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf)  
6. Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2502.15208v1](https://arxiv.org/html/2502.15208v1)  
7. LLM Probability Concentration: How Alignment Shrinks the Generative Horizon \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2506.17871v2](https://arxiv.org/html/2506.17871v2)  
8. Model collapse \- Wikipedia, accessed on December 14, 2025, [https://en.wikipedia.org/wiki/Model\_collapse](https://en.wikipedia.org/wiki/Model_collapse)  
9. Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2510.01171v1](https://arxiv.org/html/2510.01171v1)  
10. Learning to Break the Loop: Analyzing and Mitigating Repetitions for Neural Text Generation, accessed on December 14, 2025, [https://machinelearning.apple.com/research/analyzing-mitigating-repetitions](https://machinelearning.apple.com/research/analyzing-mitigating-repetitions)  
11. Learning to Break the Loop: Analyzing and Mitigating Repetitions for Neural Text Generation \- OpenReview, accessed on December 14, 2025, [https://openreview.net/pdf?id=sexfswCc7B](https://openreview.net/pdf?id=sexfswCc7B)  
12. Generative adversarial network \- Wikipedia, accessed on December 14, 2025, [https://en.wikipedia.org/wiki/Generative\_adversarial\_network](https://en.wikipedia.org/wiki/Generative_adversarial_network)  
13. A Geometry-Aware Metric for Mode Collapse in Time Series Generative Models \- OpenReview, accessed on December 14, 2025, [https://openreview.net/pdf/3db66b31c25521e6e0e52787456dbe1efe73a799.pdf](https://openreview.net/pdf/3db66b31c25521e6e0e52787456dbe1efe73a799.pdf)  
14. Early-Warning Signals of Drought-Flood State Transition over the Dongting Lake Basin Based on the Critical Slowing Down Theory \- MDPI, accessed on December 14, 2025, [https://www.mdpi.com/2073-4433/12/8/1082](https://www.mdpi.com/2073-4433/12/8/1082)  
15. Dependency Distance as a Metric of Language Comprehension Difficulty \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/273459859\_Dependency\_Distance\_as\_a\_Metric\_of\_Language\_Comprehension\_Difficulty](https://www.researchgate.net/publication/273459859_Dependency_Distance_as_a_Metric_of_Language_Comprehension_Difficulty)  
16. Language transfer in L2 academic writings: a dependency grammar approach \- PMC, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11112569/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11112569/)  
17. Thoughtworks research \- Cutting-edge AI research | Thoughtworks ..., accessed on December 14, 2025, [https://thoughtworks.medium.com/evaluating-llm-using-semantic-entropy-24dca41df754](https://thoughtworks.medium.com/evaluating-llm-using-semantic-entropy-24dca41df754)  
18. Bio-Semantic Physics: The Thermodynamic Law of Dignity in Neural Systems, accessed on December 14, 2025, [https://www.researchgate.net/publication/397870842\_Bio-Semantic\_Physics\_The\_Thermodynamic\_Law\_of\_Dignity\_in\_Neural\_Systems](https://www.researchgate.net/publication/397870842_Bio-Semantic_Physics_The_Thermodynamic_Law_of_Dignity_in_Neural_Systems)  
19. Measuring Lexical Diversity in Texts: The Twofold Length Problem Yves Bestgen, accessed on December 14, 2025, [https://perso.uclouvain.be/yves.bestgen/images/LL24.pdf](https://perso.uclouvain.be/yves.bestgen/images/LL24.pdf)  
20. (PDF) Text length requirements for stable and genre-sensitive lexical diversity measurement, accessed on December 14, 2025, [https://www.researchgate.net/publication/397517143\_Text\_length\_requirements\_for\_stable\_and\_genre-sensitive\_lexical\_diversity\_measurement](https://www.researchgate.net/publication/397517143_Text_length_requirements_for_stable_and_genre-sensitive_lexical_diversity_measurement)  
21. Measuring Lexical Diversity in Narrative Discourse of People With Aphasia \- PMC \- NIH, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3813439/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3813439/)  
22. lexical-diversity \- PyPI, accessed on December 14, 2025, [https://pypi.org/project/lexical-diversity/](https://pypi.org/project/lexical-diversity/)  
23. Lexical Diversity Measurements \- Alex Reuneker, accessed on December 14, 2025, [https://www.reuneker.nl/files/ld/](https://www.reuneker.nl/files/ld/)  
24. Standardizing the Measurement of Text Diversity: A Tool and Comparative Analysis \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2403.00553v2](https://arxiv.org/html/2403.00553v2)  
25. movmean \- Moving mean \- MATLAB \- MathWorks, accessed on December 14, 2025, [https://www.mathworks.com/help/matlab/ref/movmean.html](https://www.mathworks.com/help/matlab/ref/movmean.html)  
26. Understanding the variable sized sliding window pattern | Array \- Codeintuition, accessed on December 14, 2025, [https://www.codeintuition.io/courses/array/tFob\_VIXJQJ8bUN3hlSMB](https://www.codeintuition.io/courses/array/tFob_VIXJQJ8bUN3hlSMB)  
27. Example of measure of textual lexical diversity (MTLD) calculation using the Gramulator (2). \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/figure/Example-of-measure-of-textual-lexical-diversity-MTLD-calculation-using-the-Gramulator\_fig1\_272876507](https://www.researchgate.net/figure/Example-of-measure-of-textual-lexical-diversity-MTLD-calculation-using-the-Gramulator_fig1_272876507)  
28. Psychometric Evaluation of Lexical Diversity Indices: Assessing Length Effects \- PMC \- NIH, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4490052/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4490052/)  
29. jennafrens/lexical\_diversity: Keywords: lexical diversity MTLD HDD vocabulary type token python \- GitHub, accessed on December 14, 2025, [https://github.com/jennafrens/lexical\_diversity](https://github.com/jennafrens/lexical_diversity)  
30. LexicalRichness Documentation, accessed on December 14, 2025, [https://lexicalrichness.readthedocs.io/](https://lexicalrichness.readthedocs.io/)  
31. QuanSyn: A Python Package for Quantitative Syntax Analysis. \- GitHub, accessed on December 14, 2025, [https://github.com/YuhuYang/QuantLing](https://github.com/YuhuYang/QuantLing)  
32. Mean Hierarchical Distance Augmenting Mean Dependency Distance \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/W15-2119.pdf](https://aclanthology.org/W15-2119.pdf)  
33. An investigation of the diachronic trend of dependency distance minimization in magazines and news \- PMC \- PubMed Central, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9815589/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9815589/)  
34. Dependency Distance Differences across Interpreting Types: Implications for Cognitive Demand \- Frontiers, accessed on December 14, 2025, [https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.02132/full](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.02132/full)  
35. The Distribution of Dependency Distance and Hierarchical Distance in Contemporary Written Japanese and Its Influencing Factors \- arXiv, accessed on December 14, 2025, [https://arxiv.org/pdf/2504.21421](https://arxiv.org/pdf/2504.21421)  
36. how to get height of dependency tree with spacy? \- Stack Overflow, accessed on December 14, 2025, [https://stackoverflow.com/questions/64591644/how-to-get-height-of-dependency-tree-with-spacy](https://stackoverflow.com/questions/64591644/how-to-get-height-of-dependency-tree-with-spacy)  
37. Measuring Linguistic Growth in Sentence-Level Writing Curriculum-Based Measures: Exploring Complementary Scoring Methods | Language, Speech, and Hearing Services in Schools \- ASHA Journals, accessed on December 14, 2025, [https://pubs.asha.org/doi/10.1044/2023\_LSHSS-23-00056](https://pubs.asha.org/doi/10.1044/2023_LSHSS-23-00056)  
38. Comparing Measures of Syntactic and Lexical Complexity in Artificial Intelligence and L2 Human-Generated Argumentative Essays No \- ERIC, accessed on December 14, 2025, [https://files.eric.ed.gov/fulltext/EJ1413411.pdf](https://files.eric.ed.gov/fulltext/EJ1413411.pdf)  
39. spaCy 101: Everything you need to know, accessed on December 14, 2025, [https://spacy.io/usage/spacy-101](https://spacy.io/usage/spacy-101)  
40. How to Use Spacy for Text Analysis? \- BotPenguin, accessed on December 14, 2025, [https://botpenguin.com/blogs/how-to-use-spacy-for-text-analysis](https://botpenguin.com/blogs/how-to-use-spacy-for-text-analysis)  
41. DependencyParser · spaCy API Documentation, accessed on December 14, 2025, [https://spacy.io/api/dependencyparser](https://spacy.io/api/dependencyparser)  
42. Dependency Distance \- textdescriptives 2.8.4 documentation, accessed on December 14, 2025, [https://hlasse.github.io/TextDescriptives/dependencydistance.html](https://hlasse.github.io/TextDescriptives/dependencydistance.html)  
43. syntactic-complexity.py \- neubig/util-scripts \- GitHub, accessed on December 14, 2025, [https://github.com/neubig/util-scripts/blob/master/syntactic-complexity.py](https://github.com/neubig/util-scripts/blob/master/syntactic-complexity.py)  
44. Beyond Semantic Entropy: Boosting LLM Uncertainty Quantification with Pairwise Semantic Similarity \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/2025.findings-acl.234.pdf](https://aclanthology.org/2025.findings-acl.234.pdf)  
45. Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2410.12341v2](https://arxiv.org/html/2410.12341v2)  
46. Semantic Evaluation with Embeddings | CodeSignal Learn, accessed on December 14, 2025, [https://codesignal.com/learn/courses/benchmarking-llms-on-text-generation/lessons/semantic-evaluation-with-embeddings](https://codesignal.com/learn/courses/benchmarking-llms-on-text-generation/lessons/semantic-evaluation-with-embeddings)  
47. Different Techniques for Sentence Semantic Similarity in NLP \- GeeksforGeeks, accessed on December 14, 2025, [https://www.geeksforgeeks.org/nlp/different-techniques-for-sentence-semantic-similarity-in-nlp/](https://www.geeksforgeeks.org/nlp/different-techniques-for-sentence-semantic-similarity-in-nlp/)  
48. Drift Detection in Large Language Models: A Practical Guide | by Tony Siciliani | Medium, accessed on December 14, 2025, [https://medium.com/@tsiciliani/drift-detection-in-large-language-models-a-practical-guide-3f54d783792c](https://medium.com/@tsiciliani/drift-detection-in-large-language-models-a-practical-guide-3f54d783792c)  
49. Semantic Textual Similarity Metric Guide for AI Applications | Galileo, accessed on December 14, 2025, [https://galileo.ai/blog/semantic-textual-similarity-metric](https://galileo.ai/blog/semantic-textual-similarity-metric)  
50. Detecting Duplicate Content and Off-Topic Pages Using Python, AI & NLP | Chris Lever, accessed on December 14, 2025, [https://chrisleverseo.com/forum/t/detecting-duplicate-content-and-off-topic-pages-using-python-ai-nlp.130/](https://chrisleverseo.com/forum/t/detecting-duplicate-content-and-off-topic-pages-using-python-ai-nlp.130/)  
51. Semantic Content Cannibalization Detection — Identifying and Resolving Overlapping Topics Across Pages \- ThatWare, accessed on December 14, 2025, [https://thatware.co/semantic-content-cannibalization-detection/](https://thatware.co/semantic-content-cannibalization-detection/)  
52. Know When To Stop: A Study of Semantic Drift in Text Generation \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/2024.naacl-long.202.pdf](https://aclanthology.org/2024.naacl-long.202.pdf)  
53. How Small Transformation Expose the Weakness of Semantic Similarity Measures \- arXiv, accessed on December 14, 2025, [https://arxiv.org/pdf/2509.09714?](https://arxiv.org/pdf/2509.09714)  
54. LLM Sampling Explained: Selecting the Next Token | Thinking Sand \- Medium, accessed on December 14, 2025, [https://medium.com/thinking-sand/llm-sampling-explained-selecting-the-next-token-b897b5984833](https://medium.com/thinking-sand/llm-sampling-explained-selecting-the-next-token-b897b5984833)  
55. Understanding Logprobs: What They Are and How to Use Them \- Vellum AI, accessed on December 14, 2025, [https://www.vellum.ai/blog/what-are-logprobs-and-how-can-you-use-them](https://www.vellum.ai/blog/what-are-logprobs-and-how-can-you-use-them)  
56. A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2412.05563v1](https://arxiv.org/html/2412.05563v1)  
57. Token Probabilities to Mitigate Large Language Models Overconfidence in Answering Medical Questions: Quantitative Study, accessed on December 14, 2025, [https://www.jmir.org/2025/1/e64348](https://www.jmir.org/2025/1/e64348)  
58. Entropy-Guided Loop: Achieving Reasoning through Uncertainty-Aware Generation \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2509.00079v1](https://arxiv.org/html/2509.00079v1)  
59. The AI Model Collapse Risk is Not Solved in 2025 \- Winssolutions, accessed on December 14, 2025, [https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/](https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/)  
60. Lossless Compression of Large Language Model-Generated Text via Next-Token Prediction, accessed on December 14, 2025, [https://arxiv.org/html/2505.06297v1](https://arxiv.org/html/2505.06297v1)  
61. Complexity, Entropy and the Physics of gzip, accessed on December 14, 2025, [http://bactra.org/notebooks/cep-gzip.html](http://bactra.org/notebooks/cep-gzip.html)  
62. Normalized compression distance \- Wikipedia, accessed on December 14, 2025, [https://en.wikipedia.org/wiki/Normalized\_compression\_distance](https://en.wikipedia.org/wiki/Normalized_compression_distance)  
63. Novelty Detection in Patient Histories: Experiments with Measures Based on Text Compression \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/225136043\_Novelty\_Detection\_in\_Patient\_Histories\_Experiments\_with\_Measures\_Based\_on\_Text\_Compression](https://www.researchgate.net/publication/225136043_Novelty_Detection_in_Patient_Histories_Experiments_with_Measures_Based_on_Text_Compression)  
64. The Normalized Compression Distance as a Distance Measure in Entity Identification \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/221338422\_The\_Normalized\_Compression\_Distance\_as\_a\_Distance\_Measure\_in\_Entity\_Identification](https://www.researchgate.net/publication/221338422_The_Normalized_Compression_Distance_as_a_Distance_Measure_in_Entity_Identification)  
65. What entropy tells us about data compression \- GitHub Pages, accessed on December 14, 2025, [https://gwlucastrig.github.io/GridfourDocs/notes/EntropyMetricForDataCompression.html](https://gwlucastrig.github.io/GridfourDocs/notes/EntropyMetricForDataCompression.html)  
66. Understanding zlib \- Euccas Chen, accessed on December 14, 2025, [https://www.euccas.me/zlib/](https://www.euccas.me/zlib/)  
67. Compress and Decompress File/Text Content using Zlib Module in Node.js \- LUKI NOTES, accessed on December 14, 2025, [https://www.lukinotes.com/2021/06/compress-decompress-text-using-zlib-module-in-nodejs.html](https://www.lukinotes.com/2021/06/compress-decompress-text-using-zlib-module-in-nodejs.html)  
68. Create a Log Search alert rule with dynamic threshold \- Azure Monitor | Microsoft Learn, accessed on December 14, 2025, [https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-dynamic-thresholds)  
69. Configuring Dynamic Thresholds \- About Validio, accessed on December 14, 2025, [https://docs.validio.io/docs/configuring-dynamic-thresholds](https://docs.validio.io/docs/configuring-dynamic-thresholds)  
70. Z-Score: The Complete Guide to Statistical Standardization \- DataCamp, accessed on December 14, 2025, [https://www.datacamp.com/tutorial/z-score](https://www.datacamp.com/tutorial/z-score)  
71. Z-Score Normalization: Definition and Examples \- GeeksforGeeks, accessed on December 14, 2025, [https://www.geeksforgeeks.org/data-analysis/z-score-normalization-definition-and-examples/](https://www.geeksforgeeks.org/data-analysis/z-score-normalization-definition-and-examples/)  
72. (PDF) Benchmark of stylistic variation in LLM-generated texts \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/395474239\_Benchmark\_of\_stylistic\_variation\_in\_LLM-generated\_texts](https://www.researchgate.net/publication/395474239_Benchmark_of_stylistic_variation_in_LLM-generated_texts)  
73. Machine-generated text detection prevents language model collapse \- ACL Anthology, accessed on December 14, 2025, [https://aclanthology.org/2025.emnlp-main.1506.pdf](https://aclanthology.org/2025.emnlp-main.1506.pdf)  
74. Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2510.01171v3](https://arxiv.org/html/2510.01171v3)