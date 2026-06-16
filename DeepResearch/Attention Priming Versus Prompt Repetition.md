# **Architectural Workarounds in Autoregressive Models: A Comprehensive Analysis of Recursive Tokenization (RE2) and Attention Anchoring Mechanisms**

## **1\. Introduction: The Causal Bottleneck and Contextual Pathology**

The rapid evolution of Large Language Models (LLMs) has been driven largely by the scaling properties of the Transformer architecture, specifically the decoder-only variant employed by the GPT, LLaMA, and Claude families of models. While these architectures have demonstrated emergent reasoning capabilities that defy initial expectations, they remain bound by a fundamental structural constraint: the causal mask. In an autoregressive framework, the training objective—predicting the next token $x\_{t+1}$ given the sequence $x\_{1},..., x\_{t}$—necessitates a lower-triangular attention mask. This mask enforces a rigid temporal directionality, ensuring that no information from future tokens can leak into the representation of current tokens. While necessary for generation, this "triangular prison" 1 creates a significant pathology in context awareness and reasoning, particularly when models are tasked with processing long-context inputs where the semantic dependency between tokens is non-linear and bidirectional.

This report investigates two divergent methodologies that have emerged to mitigate the limitations of the causal mask without requiring fundamental architectural changes or expensive re-training: **Recursive Tokenization**, exemplified by the **RE2 (Re-Reading)** protocol, and **Attention Anchoring**, which encompasses **Attention Tokens**, **Attention Sinks**, and **Steering Vectors**.

The core thesis of this investigation is that while RE2 offers a theoretically robust simulation of bidirectional attention that significantly enhances complex reasoning and retrieval by effectively "hacking" the input space, Attention Anchoring offers a mechanistic stabilization of the latent space that is critical for efficiency and model control. The tension between these two approaches—one adding redundancy to force understanding (RE2) and the other exploiting structural artifacts to guide focus (Attention Tokens)—defines the current frontier of inference-time optimization.

### **1.1 The Theoretical Basis of the Causal Bottleneck**

To understand the necessity of these interventions, one must first dissect the mathematical operation of the self-attention mechanism under causal constraints. In a standard Transformer, the attention score $A$ is derived from the interaction of Queries ($Q$), Keys ($K$), and Values ($V$).

$$\\text{Attention}(Q, K, V) \= \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d\_k}} \+ M\\right)V$$  
In this equation, $M$ represents the mask. For a decoder-only model, $M\_{ij} \= \-\\infty$ whenever $j \> i$. This ensures that the attention weight $\\alpha\_{ij}$ is zero for all future tokens. Consequently, the embedding of a token at position $i$ is strictly a function of the preceding context $x\_{1...i}$.

This unidirectional flow creates a fundamental asymmetry in "understanding." Consider a prompt where the user provides a complex set of constraints followed by a question.

* **Context Processing:** As the model processes the constraints (early tokens), it does not yet know the question (late tokens). Therefore, the attention heads cannot selectively attend to the specific constraints relevant to the question. They must compress the context into a generalized representation in the residual stream.  
* **Information Dissipation:** By the time the model reaches the question, the granular details of the constraints may have been "over-squashed" or diluted, particularly in long sequences where the "Middle" of the context is notoriously difficult to retain.2

This phenomenon, known as the "Lost in the Middle" effect, is not merely a capacity limitation but a structural failure of causal attention to assign high saliency to information that only becomes relevant *retrospectively*.2

### **1.2 The Two Paths to Correction**

Faced with this bottleneck, researchers have developed two primary schools of thought for inference-time correction:

1. **Input Space Intervention (RE2):** This approach posits that the limitation is informational. By manipulating the input sequence—specifically by repeating the prompt—we can force the model to process the context *again*, but this time with the full query already in its history. This effectively creates a "read-write" cycle where the first pass serves as a scratchpad for the second pass.4  
2. **Latent Space Intervention (Attention Tokens/Anchoring):** This approach posits that the limitation is structural. By identifying high-saliency "Attention Tokens" (such as the initial "Sink" token or specific "System Prompts") and manipulating their influence—either by pruning low-value tokens or injecting steering vectors—we can guide the model's attention distribution to focus on relevant information without the crude redundancy of repetition.6

The following sections will rigorously analyze the validity, mechanisms, and efficiency of these two paradigms.

## ---

**2\. Recursive Tokenization (RE2): The Redundancy Paradigm**

Recursive Tokenization, most prominently formalized as the **RE2 (Re-Reading)** framework by Xu et al. 4, represents a brute-force yet theoretically elegant solution to the causal masking problem. It challenges the assumption that efficiency (minimizing token count) is always the primary objective, suggesting instead that redundancy is the price of reasoning in unidirectional architectures.

### **2.1 Theoretical Validity: The "Iso-Attention" Hypothesis**

The central theoretical claim of RE2 is that repeating the input prompt allows a unidirectional decoder to simulate the receptive field of a bidirectional encoder (like BERT). This can be understood through the "Iso-Attention" hypothesis.

Let us denote the input sequence as $S \= \[C, Q\]$, where $C$ is the Context and $Q$ is the Question.  
In a standard pass, the attention available to a token $c\_k$ (the $k$-th token of the context) is restricted to $\\{c\_1,..., c\_k\\}$. Crucially, $c\_k$ cannot attend to $Q$. The representation of the context is agnostic to the question.  
In the RE2 protocol, the input is transformed to $S' \= \[C, Q, C, Q\]$.  
Let us analyze the attention availability for the tokens in the second instance of the context (denoted $C'$).  
A token $c'\_k$ in the second block is at a position index $T \+ k$, where $T$ is the length of $\[C, Q\]$.  
Because of the causal mask, $c'\_k$ can attend to all tokens at positions $j \< T+k$.  
Crucially, this includes the entirety of the first block $\[C, Q\]$.  
Therefore, while processing the context for the second time, the model can attend to the Question (from the first block).

$$\\text{Attention}(c'\_k) \\rightarrow \\{c\_1...c\_n, q\_1...q\_m, c'\_1...c'\_k\\}$$  
This fundamentally alters the computation. The embedding of $c'\_k$ is now conditioned on $Q$. The attention heads can perform "Query-Aware" processing of the context, extracting exactly the features required to answer $Q$. Snippet 5 explicitly describes this as achieving a "bidirectional" understanding, as the early tokens of the second pass can "see" the later tokens of the first pass.

### **2.2 Mechanistic Analysis: The "Scratchpad" Effect**

The effectiveness of RE2 can be further analyzed through the lens of "Scratchpad" theory.1 In Chain-of-Thought (CoT) prompting, the model generates output tokens to store intermediate reasoning. In RE2, the *first pass* of the input acts as a "Read-Only Memory" or scratchpad.

When the model processes the first copy $\[C, Q\]$, it builds up a KV Cache (Key-Value pairs) for these tokens.

* **Pass 1 State:** The KV Cache for $\[C, Q\]$ contains a "naive" encoding of the context (processed without knowledge of the question) and a "naive" encoding of the question (processed with knowledge of the context).  
* **Pass 2 Interaction:** As the model processes the second copy, the Query vectors ($Q\_{c'}$) generated by the new context tokens interact with the Key vectors ($K\_{q}$) of the question from Pass 1\.  
* **Mechanism:** High attention scores will be assigned between $C'$ and $Q$ wherever there is semantic relevance. This allows the model to "highlight" or "retrieve" specific facts from the context that match the question's requirements, effectively solving the "Lost in the Middle" problem by moving the "Middle" to the "End" (Pass 1\) or the "Beginning" (Pass 2\) relative to the attention window.2

This mechanism is distinct from CoT because it occurs entirely within the *pre-fill* phase (processing input), rather than the *decode* phase (generating output).

### **2.3 Empirical Performance: Retrieval vs. Reasoning**

The empirical validation of RE2 is robust across multiple domains, particularly where "Context Awareness" is the limiting factor.

#### **2.3.1 The "Needle in a Haystack" (NIAH) Test**

The NIAH benchmark is the gold standard for evaluating context awareness. It involves placing a random fact ("the needle") inside a long, unrelated document ("the haystack") and asking the model to retrieve it.

* **Baseline Failure:** Standard models typically exhibit a U-shaped performance curve. They retrieve needles easily at the start (Primacy) or end (Recency) but fail catastrophically in the middle (depth \~50%).3  
* **RE2 Success:** Research indicates that RE2 raises retrieval accuracy from abysmal levels (e.g., 21.3%) to near-perfect levels (97.3%) on advanced models like Gemini 2 Flash.1  
* **Explanation:** By repeating the haystack, the "middle" of the text in the combined sequence $\[H, H\]$ falls into different relative positions. More importantly, the second pass processes the haystack *after* having seen the question (at the end of Pass 1), allowing the attention heads to actively search for the needle rather than passively encoding the text.

#### **2.3.2 Mathematical Reasoning (GSM8K)**

In mathematical word problems (GSM8K), critical variable definitions often appear at the beginning of the problem description.

* **Issue:** By the time the model attempts to generate the solution equation, the specific value of a variable defined 200 tokens ago might be "dim" in the residual stream.  
* **RE2 Impact:** Snippets 4 report consistent accuracy gains on GSM8K (e.g., \+3% to \+10%).  
* **Case Study:** Consider a problem: "Alice has x apples... \[distractor text\]... How many apples?". With RE2, the model reads "Alice has x apples" (Pass 1), reads the question (Pass 1), then reads "Alice has x apples" (Pass 2\) immediately before generating the answer. This proximity in the *second* pass acts as a refresher, ensuring the variable $x$ is highly active in the working memory.

### **2.4 Economic and Efficiency Analysis**

A critical and often counter-intuitive finding in the investigation of RE2 is its economic profile. Superficially, doubling the input length seems inefficient. However, a deeper analysis of Transformer economics reveals a different picture.

#### **2.4.1 Pre-fill vs. Decode Costs**

Transformer inference has two distinct phases:

1. **Pre-fill (Prompt Processing):** The model processes all input tokens in parallel. This phase is **Compute-Bound**. The GPU tensor cores are fully saturated.  
2. **Decode (Generation):** The model generates one token at a time. This phase is **Memory-Bandwidth Bound**. The GPU spends most of its time moving weights from HBM (High Bandwidth Memory) to the chip for every single token.

#### **2.4.2 The Comparison with Chain-of-Thought (CoT)**

Standard reasoning enhancement techniques like CoT rely on generating more *output* tokens ("Let's think step by step...").

* **CoT Cost:** Generating 100 reasoning tokens involves 100 sequential memory-bound operations. This is slow and expensive in terms of latency (Time-to-First-Token and Total Time).  
* **RE2 Cost:** Doubling an input of 1000 tokens to 2000 tokens increases the Pre-fill time. However, because Pre-fill is parallel and compute-bound, it is extremely fast compared to generation.  
* **Efficiency Verdict:** Snippets 1 suggest that RE2 is often faster and cheaper than CoT for achieving the same level of reasoning accuracy. It shifts the burden from the expensive *sequential* decoding to the cheap *parallel* encoding. Furthermore, by clarifying the context, RE2 often leads to *shorter* and more concise answers, saving generation costs.

#### **2.4.3 Memory Footprint**

The primary downside of RE2 is the increase in KV Cache size.

* **KV Cache:** Storing the Key and Value matrices for the doubled context requires $2\\times$ the VRAM.  
* **Implication:** For extremely long contexts (e.g., 100k tokens), doubling to 200k might trigger Out-Of-Memory (OOM) errors or force the system to offload to CPU, destroying performance. Therefore, RE2 is best suited for "medium-long" contexts where the doubled length fits comfortably within the GPU's HBM.

## ---

**3\. Attention Anchoring: The Structural Paradigm**

While RE2 relies on "Context Engineering" (modifying the input text), the "Attention Anchoring" paradigm relies on "Mechanism Engineering"—understanding and exploiting the low-level behavior of the attention heads themselves. This school of thought aggregates findings on **Attention Sinks**, **System Prompts**, and **Steering Vectors**.

### **3.1 The Phenomenology of Attention Sinks**

The discovery of "Attention Sinks" 7 provided a breakthrough in understanding why Transformers behave the way they do at the start of sequences.

#### **3.1.1 The Softmax Bottleneck**

The Softmax function forces the attention weights for any given query to sum to 1\.

$$\\sum\_{j} \\alpha\_{ij} \= 1$$

This creates a zero-sum game. If the current token $x\_i$ does not have any strong semantic relationship with the previous tokens $x\_{\<i}$, the model is mathematically forced to assign the probability mass somewhere.

* **The Sink:** The model learns during pre-training to dump this excess probability mass onto specific tokens that serve as "no-ops" or "sinks."  
* **The Chosen One:** Empirically, the first token (Index 0, usually \<s\> or \<BOS\>) acts as this sink. Snippet 7 notes that this token often accumulates massive attention scores despite having zero semantic value.  
* **High-Norm Tokens:** Recent research 11 links this to "High-Norm Tokens." The value vectors associated with these sink tokens often have large norms, allowing them to dominate the residual stream if not carefully managed.

#### **3.1.2 Stability vs. Semantics**

The "Attention Sink" is not a "Context Awareness" feature; it is a **Stability** feature.

* **Evidence:** If one artificially masks out the first token during inference (e.g., via a sliding window that drops the start), the model's perplexity explodes (performance collapses).10 This is because the "trash" probability mass that belongs in the sink is redistributed to meaningful tokens, corrupting their representations with noise.  
* **Efficiency Application:** This insight led to **StreamingLLM**.12 By keeping just the Attention Sink (first few tokens) and the local window (last few tokens), one can run an LLM on infinite-length text without performance collapse. The sink keeps the Softmax stable.

### **3.2 System Prompts as "Meta-Attention Tokens"**

The "System Prompt" (e.g., "You are a helpful assistant") is effectively a manually injected Attention Sink/Anchor.13

* **Q-Matrix Priming:** Snippet 13 suggests that the system prompt conditions the $Q$ (Query) matrix for the rest of the generation. It sets the "subspace" or "mode" of the model.  
* **Instructional Segment Embedding (ISE):** More advanced implementations 14 embed the hierarchy of the system prompt directly into the model, ensuring that these tokens have a higher priority or "saliency" than user tokens.  
* **Drift and Decay:** A major limitation of System Prompts is "Instruction Drift".15 As the context grows, the attention weight on the system prompt (Index 1-50) naturally decays due to the Softmax competition with thousands of new tokens. This explains why models "forget" their persona in long chats.  
* **The RE2 Fix:** This provides another justification for RE2. By repeating the system instructions at the *end* of the prompt (Refresh), we create a new "Anchor" that is chemically identical to the System Prompt but positionally proximal to the generation, countering the drift.

### **3.3 Steering Vectors: Direct Activation Intervention**

A more sophisticated evolution of "Attention Tokens" is the use of **Steering Vectors** (or Control Vectors).8

* Mechanism: Instead of optimizing the input text (Prompt Engineering), this method intervenes in the latent space. Researchers identify a vector direction $v$ in the residual stream that corresponds to a concept (e.g., "Sycophancy," "Refusal," "Creativity").

  $$h\_{layer} \\leftarrow h\_{layer} \+ \\alpha \\cdot v$$  
* **Textual Steering:** Snippets 8 reveal that these vectors can be derived from *textual* contrasts. For example, taking the difference in activations between a "Helpful" prompt and a "Harmful" prompt yields a "Safety Vector."  
* **Comparison to RE2:**  
  * **Pros:** Zero token overhead. Extremely fast. Cannot "drift" because it is added mathematically at every step.  
  * **Cons:** Low granularity. You can steer a model to be "honest," but you cannot steer it to "remember that the code is 1234" using a generic vector. Steering is for *style* and *behavior*, whereas RE2 is for *facts* and *reasoning*.

### **3.4 Participative Compression: Pruning for Efficiency**

Based on the insight that only "Heavy Hitter" tokens (high attention scores) and "Attention Sinks" matter, researchers proposed **Participative Compression** and **H2O**.6

* **Method:** During pre-fill, monitor the attention matrix. If a token $t$ receives low attention from its neighbors, prune it (remove it from KV cache). Keep only the "Attention Tokens" (Sinks \+ High Saliency).  
* **Result:** This allows for massive context reduction (e.g., keeping only 20% of tokens) with minimal perplexity loss.  
* **The Risk:** This relies on the assumption that *current* attention predicts *future* importance. In reasoning tasks, a variable might be ignored for 1000 tokens (low attention) and then suddenly be critical for the final answer. Pruning it would be catastrophic. Thus, this method competes with RE2: RE2 *adds* tokens to ensure safety; Participative Compression *removes* tokens to ensure speed.

## ---

**4\. Comparative Analysis: Validity, Efficiency, and Robustness**

Having established the mechanisms of both approaches, we now perform a comparative analysis to determine their respective domains of superiority.

### **4.1 Validity Matrix: Reasoning vs. Retrieval**

| Feature | RE2 (Prompt Repetition) | Attention Tokens / Sinks | Steering Vectors |
| :---- | :---- | :---- | :---- |
| **Mechanism** | Redundancy ($Input \\times 2$) | Structural Exploitation | Activation Injection |
| **Causal Mask Soln.** | **Complete** (Simulates Bidirectionality) | Partial (Stabilizes Math) | None (Behavioral) |
| **"Lost in Middle"** | **Solves** (Shifts Middle to End) | Mitigates (via Pruning noise) | None |
| **Reasoning Depth** | **High** (increases working memory) | Medium (depends on retention) | Low (Global bias only) |
| **Retrieval Accuracy** | **Very High** (NIAH \> 95%) | Medium (Risk of pruning needle) | N/A |

**Insight:** RE2 is the only method that structurally "solves" the informational blindness caused by causal masking for specific data retrieval. Attention Sinks are necessary for the model to function at all, but they do not inherently solve the context awareness problem for "middle" tokens.

### **4.2 Efficiency Matrix: Latency vs. Throughput**

| Metric | RE2 (Prompt Repetition) | Attention Tokens / Pruning |
| :---- | :---- | :---- |
| **Pre-fill Latency** | High ($2\\times$ Compute) | Low ($1\\times$ Compute) |
| **Pre-fill Memory** | High ($2\\times$ KV Cache) | Low (Compressed KV Cache) |
| **Generation Latency** | Neutral (or Improved via conciseness) | Improved (Smaller cache to scan) |
| **Throughput** | Lower (Consumes more slots) | Higher (Frees up memory) |
| **Implementation** | **Trivial** (Prompt Engineering) | **Complex** (Custom CUDA Kernels) |

**Insight:** The trade-off is clear. RE2 trades **Memory** for **Intelligence**. Attention Token Pruning trades **Intelligence** (risk of loss) for **Memory/Speed**.

* **Use Case for RE2:** High-stakes reasoning (Legal, Medical, Code generation) where accuracy is paramount and the context fits in memory.  
* **Use Case for Attention Pruning:** Real-time Chatbots, Summarization of massive logs, where throughput is paramount and occasional detail loss is acceptable.

### **4.3 Robustness to Shifts and Attacks**

* **Prompt Injection:** RE2 is potentially more robust to prompt injection buried in the middle of text because the second pass allows the model to re-evaluate the context *after* seeing the instruction "Ignore previous instructions." However, if the injection is strong, repeating it might amplify it.  
* **Drift:** RE2 completely negates Instruction Drift by refreshing the prompt. Steering Vectors also negate drift by applying a constant force. System Prompts (standard) are highly susceptible to drift.

## ---

**5\. Advanced Synthesis: Mechanism Interaction and Future Outlook**

The dichotomy between RE2 and Attention Tokens is not absolute. Advanced techniques act as hybrids or evolutions of these concepts.

### **5.1 System 2 Attention (S2A): The Middle Ground**

**System 2 Attention (S2A)** 19 proposes a method where the LLM is asked to *rewrite* the prompt to remove irrelevant information before generating the answer.

* **Relation to RE2:** RE2 *adds* information (Redundancy). S2A *subtracts* information (Noise Reduction).  
* **Relation to Attention Tokens:** S2A is essentially "Semantic Pruning." It performs the same job as "Participative Compression" but uses the LLM's reasoning engine rather than attention scores to decide what to keep.  
* **Verdict:** S2A is cleaner but riskier (model might hallucinate the deletion of important data). RE2 is "safer" because it preserves the original data, trusting the attention mechanism to filter it out during the second pass.

### **5.2 Instructional Hierarchy and Delimiters**

Snippet 14 introduces **Instructional Segment Embeddings (ISE)**. This moves beyond "System Prompts" to tagging every token with a priority level.

* **Future Architecture:** This suggests a move towards architectures that are "Context-Aware" by design, explicitly separating "Instructions" from "Data" in the vector space. This would render RE2 obsolete, as the model would naturally attend to "Instruction" tokens (High Priority) regardless of their position (Start, Middle, End).  
* **Delimiters:** Until then, using explicit symbolic delimiters (\#\#\#, ||) 21 serves as a "soft" version of this, creating artificial "Attention Sinks" or "Boundaries" that help the attention heads segment the processing.

### **5.3 Directional Stimulus Prompting**

Snippet 22 discusses **Directional Stimulus Prompting**, where a small "Policy Model" generates hints (Keywords, Summaries) to guide the main LLM.

* **Connection:** This is a dynamic form of RE2. Instead of repeating the *whole* prompt (RE2), we repeat a *summarized, hint-rich* version of the prompt (Directional Stimulus).  
* **Efficiency:** This captures the reasoning benefits of RE2 without the $2\\times$ memory cost.

### **5.4 The "Sovereign AI" Angle**

While seemingly tangential, the concept of **Sovereign AI** 23 emphasizes control and "Operational Autonomy."

* **Relevance:** Techniques like **Steering Vectors** are the primary mechanism for implementing Sovereign controls (Safety, Privacy, Alignment) without relying on the model provider's finetuning. If an enterprise wants to enforce a "No-Code" policy, a Steering Vector is more reliable than a System Prompt (which can be jailbroken).  
* **RE2 Role:** RE2 ensures that these sovereign instructions (if placed in the prompt) are not ignored due to context length limits.

## ---

**6\. Conclusion**

The investigation into the comparative efficacy of **Recursive Tokenization (RE2)** and **Attention Anchoring (Tokens/Sinks)** reveals a fundamental tension in current Transformer usage: the struggle between the **Linearity of Generation** and the **Non-Linearity of Understanding**.

The **Causal Mask**, while essential for the autoregressive generation of coherent text, imposes a severe cognitive limitation on the model's ability to process past context in light of future instructions.

**RE2 (Prompt Repetition)** emerges as the theoretically superior solution for **Context Awareness** and **Reasoning**. By leveraging the "Iso-Attention" effect—essentially hacking the causal mask to create a virtual bidirectional receptive field—it solves the "Lost in the Middle" problem and drastically improves retrieval and mathematical reasoning accuracy. Its economic profile is surprisingly favorable, trading cheap pre-fill compute for expensive generation retries. It is the recommended strategy for high-accuracy, zero-shot applications.

**Attention Anchoring (Sinks, Tokens, Vectors)** emerges as the essential solution for **Stability** and **Throughput**. The existence of "Attention Sinks" proves that the Transformer architecture requires "structural junk" to satisfy its Softmax constraints. Exploiting this via pruning (Participative Compression) or guiding it via interventions (Steering Vectors) is the key to efficient, infinite-context deployment.

**Final Outlook:** We are likely witnessing a transitional phase. Techniques like RE2 are "software patches" for a "hardware bug" (the Causal Mask). Future architectures will likely integrate **Prefix-LM Attention** (bidirectional encoding for prompts, causal for generation) or **Instructional Segment Embeddings** natively, rendering the "Re-Reading" strategy unnecessary. Until then, for the practitioner seeking the highest fidelity from off-the-shelf LLMs, the instruction is clear: **Say it twice.**

## ---

**7\. Data and Benchmarks Summary**

The following table synthesizes the quantitative findings discussed throughout the report.

| Methodology | Application | Metric | Quantitative Result | Source |
| :---- | :---- | :---- | :---- | :---- |
| **RE2** | "Needle in a Haystack" | Retrieval Accuracy | **21.3% $\\rightarrow$ 97.3%** (Gemini 2\) | 1 |
| **RE2** | GSM8K (Math Reasoning) | Accuracy | **\+3% to \+10%** vs Baseline | 4 |
| **Attention Sinks** | StreamingLLM (Infinite Context) | Perplexity | Stable at **\>4M tokens** vs Collapse at 4k | 12 |
| **Steering Vectors** | Spatial Reasoning | Accuracy | **\+15.8%** improvement | 16 |
| **Participative Compression** | Long-Context Inference | Memory Usage | **80% reduction** with \<1% acc loss | 6 |
| **Directional Stimulus** | Summarization | Rouge Score | **\+41.4%** (ChatGPT on MultiWOZ) | 22 |

This data confirms that while Attention Anchoring/Pruning offers massive efficiency gains (80% memory reduction), RE2 offers massive *performance* gains (4x retrieval improvement). The choice between them is strictly a function of the application's constraints: **Capacity** (use Pruning) vs. **Capability** (use RE2).

#### **Works cited**

1. RE2: The "Stupidest" AI Breakthrough That Actually Works, accessed on January 17, 2026, [https://www.youtube.com/watch?v=XZ1QDGJXFlQ](https://www.youtube.com/watch?v=XZ1QDGJXFlQ)  
2. Lost in the Middle: How Language Models Use Long Contexts, accessed on January 17, 2026, [https://teapot123.github.io/files/CSE\_5610\_Fall25/Lecture\_12\_Long\_Context.pdf](https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf)  
3. \[2307.03172\] Lost in the Middle: How Language Models Use Long Contexts \- arXiv, accessed on January 17, 2026, [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)  
4. Re-Reading Improves Reasoning in Large Language Models \- ACL Anthology, accessed on January 17, 2026, [https://aclanthology.org/2024.emnlp-main.871.pdf](https://aclanthology.org/2024.emnlp-main.871.pdf)  
5. \[2309.06275\] Re-Reading Improves Reasoning in Large Language Models \- arXiv, accessed on January 17, 2026, [https://arxiv.org/abs/2309.06275](https://arxiv.org/abs/2309.06275)  
6. Training-Free Long Video Generation with Deep Sink and Participative Compression \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2512.05081](https://arxiv.org/html/2512.05081)  
7. Why do LLMs attend to the first token? | alphaXiv, accessed on January 17, 2026, [https://www.alphaxiv.org/overview/2504.02732v4](https://www.alphaxiv.org/overview/2504.02732v4)  
8. Textual Steering Vectors Can Improve Visual Understanding in Multimodal\\n Large Language Models \- Liner, accessed on January 17, 2026, [https://liner.com/review/textual-steering-vectors-can-improve-visual-understanding-in-multimodal-large](https://liner.com/review/textual-steering-vectors-can-improve-visual-understanding-in-multimodal-large)  
9. \[Quick Review\] Re-Reading Improves Reasoning in Large Language Models \- Liner, accessed on January 17, 2026, [https://liner.com/review/rereading-improves-reasoning-in-large-language-models](https://liner.com/review/rereading-improves-reasoning-in-large-language-models)  
10. Why do LLMs attend to the first token? \- OpenReview, accessed on January 17, 2026, [https://openreview.net/forum?id=tu4dFUsW5z](https://openreview.net/forum?id=tu4dFUsW5z)  
11. High-Norm Tokens in Deep Models \- Emergent Mind, accessed on January 17, 2026, [https://www.emergentmind.com/topics/high-norm-tokens](https://www.emergentmind.com/topics/high-norm-tokens)  
12. Attention Sinks: Enabling Infinite-Length LLM Generation with, accessed on January 17, 2026, [https://mbrenndoerfer.com/writing/attention-sinks-streamingllm-infinite-generation](https://mbrenndoerfer.com/writing/attention-sinks-streamingllm-infinite-generation)  
13. "Attention", "Transformers", in Neural Network "Large Language Models", accessed on January 17, 2026, [http://bactra.org/notebooks/nn-attention-and-transformers.html](http://bactra.org/notebooks/nn-attention-and-transformers.html)  
14. Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy \- arXiv, accessed on January 17, 2026, [https://arxiv.org/abs/2410.09102](https://arxiv.org/abs/2410.09102)  
15. Measuring and Controlling Instruction (In)Stability in Language Model Dialogs \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2402.10962v3](https://arxiv.org/html/2402.10962v3)  
16. Text Steers Vision \- LessWrong, accessed on January 17, 2026, [https://www.lesswrong.com/posts/XwxSYoFWijSwrHF6n/text-steers-vision](https://www.lesswrong.com/posts/XwxSYoFWijSwrHF6n/text-steers-vision)  
17. You've Changed: Detecting Modification of Black-Box Large Language Models \- arXiv, accessed on January 17, 2026, [https://arxiv.org/html/2504.12335v1](https://arxiv.org/html/2504.12335v1)  
18. Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression \- ResearchGate, accessed on January 17, 2026, [https://www.researchgate.net/publication/398357196\_Deep\_Forcing\_Training-Free\_Long\_Video\_Generation\_with\_Deep\_Sink\_and\_Participative\_Compression](https://www.researchgate.net/publication/398357196_Deep_Forcing_Training-Free_Long_Video_Generation_with_Deep_Sink_and_Participative_Compression)  
19. How to Use System 2 Attention Prompting to Improve LLM Accuracy \- PromptHub, accessed on January 17, 2026, [https://www.prompthub.us/blog/how-to-use-system-2-attention-prompting-to-improve-llm-accuracy](https://www.prompthub.us/blog/how-to-use-system-2-attention-prompting-to-improve-llm-accuracy)  
20. System 2 Attention (S2A) Prompting: Filtering Irrelevant Context, accessed on January 17, 2026, [https://learnprompting.org/docs/advanced/zero\_shot/s2a](https://learnprompting.org/docs/advanced/zero_shot/s2a)  
21. Alternative Prompt Engineering Approach: Sectioning with Delimeters | by Thomas Czerny | Medium, accessed on January 17, 2026, [https://medium.com/@thomasczerny/alternative-prompt-engineering-approach-sectioning-with-delimeters-112ff9d7953f](https://medium.com/@thomasczerny/alternative-prompt-engineering-approach-sectioning-with-delimeters-112ff9d7953f)  
22. \[2302.11520\] Guiding Large Language Models via Directional Stimulus Prompting \- arXiv, accessed on January 17, 2026, [https://arxiv.org/abs/2302.11520](https://arxiv.org/abs/2302.11520)  
23. accessed on January 17, 2026, [https://www.opentext.com/what-is/sovereign-ai\#:\~:text=Sovereign%20AI%20is%20the%20ability,enterprise's%20legal%20and%20strategic%20boundaries.](https://www.opentext.com/what-is/sovereign-ai#:~:text=Sovereign%20AI%20is%20the%20ability,enterprise's%20legal%20and%20strategic%20boundaries.)