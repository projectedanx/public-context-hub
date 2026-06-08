

# **The Precision Paradox: A Deep Dive into the Anthropic Claude Sampling Bug and the Fragility of Large-Scale AI Infrastructure**

## **Executive Summary**

Between August and September 2025, users of Anthropic's Claude large language model (LLM) reported a significant and perplexing degradation in response quality. The model, once lauded for its sophisticated coding and reasoning capabilities, began exhibiting erratic behavior, including logical incoherence, forgetting instructions, and generating nonsensical output. This report provides an exhaustive technical analysis of the incident, revealing its root cause not as a singular flaw in the model's logic, but as a complex, systemic failure emerging from the intricate interplay of cutting-edge hardware, compiler optimizations, and the fundamental mathematics of language generation.

The primary technical culprit was a subtle but critical issue involving mixed-precision arithmetic within Google's Tensor Processing Unit (TPU) ecosystem. Anthropic's models perform next-token probability calculations using the memory-efficient 16-bit bfloat16 (bf16) format. However, an optimization within the XLA compiler, governed by the xla\_allow\_excess\_precision flag, opportunistically up-converted some of these calculations to the hardware's native 32-bit floating-point (fp32) format for a performance boost. On the multi-chip distributed systems where Claude runs, this created a state of numerical inconsistency. Different parts of the system, which needed to agree on the single most probable next token for the top-p sampling algorithm, were operating with slightly different levels of numerical precision. This discrepancy led to a catastrophic failure in the distributed sorting mechanism, causing the most probable token to be erroneously dropped from consideration entirely. The model was then forced to select a less likely, and often incorrect, alternative, directly causing the observed degradation in quality.

This incident serves as a critical case study for the broader AI industry, illuminating the profound challenges of building and maintaining reliable AI systems at massive scale. It highlights a "precision paradox," where optimizations designed to enhance performance can introduce latent, non-obvious failure modes that undermine algorithmic correctness. The diagnostic process was further complicated by the bug's intermittent nature—manifesting only under specific configurations—and the simultaneous occurrence of two other unrelated infrastructure failures, creating a "fog of war" for engineers.

The public's reaction to the incident underscores a significant trust gap between AI developers and their user communities. Widespread skepticism met the company's technical explanation, with many users attributing the degradation to intentional, cost-cutting measures—a simpler narrative that gained traction in the absence of proactive communication. This report deconstructs the technical realities behind the failure, contextualizes it within the systemic challenges of numerical stability and hardware fallibility in high-performance computing, and concludes with a framework of actionable recommendations for building more resilient, transparent, and trustworthy AI infrastructure. The lessons from the Claude sampling bug extend far beyond a single company, offering a stark reminder of the fragility that underlies the power of modern artificial intelligence.

## **Section 1: The Architectural Foundations of Modern Language Generation**

The Anthropic Claude incident was not the result of a single faulty component but an emergent failure arising from the complex interaction of four distinct technological pillars: the probabilistic nature of language model generation, the specific sampling strategy used to select text, the specialized hardware on which the models run, and the compiler that bridges the software-hardware divide. Understanding these foundations is essential to deconstructing the bug's intricate causal chain.

### **1.1 From Probability to Prose: The Mechanics of Next-Token Prediction**

Large Language Models (LLMs) like Claude are fundamentally autoregressive systems, meaning they generate text sequentially, one unit at a time.1 This process begins with an input prompt, which is first converted into a sequence of numerical representations called tokens. The model then processes these tokens to predict the most likely

*next* token. This predicted token is appended to the sequence, and the entire process repeats, with the model using the newly extended sequence to predict the subsequent token. This iterative loop continues until a stopping condition is met, such as reaching a maximum length or generating a special "end-of-sequence" token.

The core of this prediction mechanism lies in the model's final layer. After passing the input sequence through numerous layers of complex computations (typically within a Transformer architecture), the model produces a vector of raw numerical scores known as "logits" for every possible token in its vocabulary. This vocabulary can contain tens of thousands of potential tokens, ranging from single characters and punctuation marks to common words or sub-word units.2 To transform these logits into a usable probability distribution, a softmax function is applied. The softmax function exponentiates each logit and normalizes the results so that they sum to 1, effectively converting the raw scores into a probability for each token in the vocabulary.3 The output is a probability distribution where each token is assigned a likelihood of being the correct next token in the sequence. The generation process is, therefore, not a deterministic selection but a sophisticated act of sampling from this distribution.

The initial step of converting human-readable text into these numerical tokens, known as tokenization, is itself a critical process that can influence model behavior. Different models use different tokenization algorithms, such as Byte-Pair Encoding (BPE) or WordPiece, which break text down based on the frequency of character sequences in the training data.2 This means that a single word might be represented by one or multiple tokens. This choice of representation can subtly bias the model; for instance, shorter, more common tokens that can form the beginning of many different words may be assigned a higher cumulative probability, making them more likely to be selected by certain sampling strategies.4

### **1.2 Navigating the Distribution: A Comparative Analysis of Decoding Strategies**

Once the model has produced a probability distribution over its vocabulary, a decoding strategy must be employed to select the next token. The choice of strategy profoundly impacts the quality of the generated text, requiring a delicate balance between coherence and creativity.

A simple approach is **greedy search**, which deterministically selects the single token with the highest probability at each step. While straightforward, this method often leads to repetitive, generic, and unnatural-sounding text because it commits to a single path without considering how that choice might affect future possibilities.6

To introduce more variety, stochastic (randomized) methods are used. The most common of these are top-k sampling and top-p sampling. In **top-k sampling**, the selection is restricted to a fixed number, *k*, of the most likely tokens.1 For example, with

*k*\=50, the model would only consider the 50 most probable tokens and would sample from a new distribution formed by renormalizing their probabilities. The primary drawback of top-k is its static nature. For some contexts, the probability might be sharply peaked on a single correct token, and considering *k*\=50 introduces unnecessary randomness. In other contexts, the distribution might be flat and spread across hundreds of plausible tokens, making *k*\=50 overly restrictive.1

To address this, **top-p sampling**, also known as nucleus sampling, was introduced as a more adaptive strategy.9 Instead of sampling from a fixed number of tokens, top-p sampling selects from the smallest possible set of tokens whose cumulative probability exceeds a predefined threshold,

*p*.1 This set is called the "nucleus." The process involves several steps:

1. The model's output probabilities are sorted in descending order.  
2. The cumulative probability is calculated from the top of the list downwards.  
3. The nucleus is formed by including tokens until their cumulative sum meets or exceeds the threshold *p*.  
4. The probabilities of the tokens within this nucleus are rescaled to sum to 1\.  
5. The next token is randomly sampled from this newly formed, dynamically sized distribution.

For example, if *p* is set to 0.9, the model considers the most likely tokens until their combined probability accounts for 90% of the total probability mass.6 This method is highly flexible. When the model is very confident and one token has a probability of 0.95, the nucleus will contain only that single token, effectively behaving like greedy search. When the model is uncertain and the probability is spread thinly, the nucleus will expand to include many tokens, allowing for more creative and diverse outputs.1 The purpose of this technique is to truncate the long, "unreliable tail" of the probability distribution, which contains thousands of very low-probability tokens that, if sampled, would likely produce nonsensical text.9 For models like Claude, this threshold is typically set very high (e.g., 0.99 or 0.999) to aggressively filter out improbable tokens and prevent incoherent outputs.11 While top-p is a powerful and widely adopted technique, it is an active area of research, with alternatives like min-p sampling being developed to better handle the trade-off between creativity and coherence, particularly at higher "temperatures" (a parameter that adjusts the shape of the probability distribution).8

### **1.3 The Silicon Engine: An Overview of Tensor Processing Unit (TPU) Architecture**

The immense computational demands of training and running large language models necessitate the use of specialized hardware. Google's Tensor Processing Units (TPUs) are Application-Specific Integrated Circuits (ASICs) custom-designed to accelerate the large-scale matrix and tensor operations that form the backbone of modern machine learning workloads.13 Unlike general-purpose CPUs or even GPUs, which must balance flexibility with performance, TPUs are purpose-built for AI, allowing for significant efficiency gains.15

A TPU chip contains several key components, but two are central to its operation: the **Matrix Multiply Unit (MXU)** and the **Vector Processing Unit (VPU)**.17 The MXU is a systolic array, a grid of thousands of arithmetic logic units (ALUs) optimized for performing massive matrix multiplications and convolutions with extreme speed and efficiency. This is where the bulk of a neural network's computation occurs. The VPU, on the other hand, handles all other types of operations, such as activations (e.g., ReLU), softmax calculations, and other element-wise vector and scalar math.17 This architectural division is a crucial piece of the puzzle in the Anthropic bug, as the VPU is fp32-native, meaning its internal operations are most efficient when performed with 32-bit precision, a fact that would have significant downstream consequences.11

A key feature of modern TPUs is their native support for the **bfloat16 (bf16)** numerical format.17 This 16-bit floating-point format offers a compromise between the high precision of 32-bit floats (fp32) and the memory and speed advantages of lower-precision arithmetic. Using bf16 halves the memory footprint of model parameters and activations and significantly increases computational throughput on the MXU.19 This hardware-level optimization is a primary reason why running large models on TPUs is economically and computationally feasible.

Furthermore, TPUs are designed for massive parallelism. A single model's execution is often distributed across multiple TPU chips, which are connected via high-speed interconnects. These groups of chips, known as "slices" or "pods," work in concert to process the model.13 This distributed nature means that computations that might seem monolithic from a software perspective, such as calculating the probability distribution for the next token, are physically occurring in different locations and must be carefully coordinated \[User Query\]. The decision to leverage the performance of TPUs thus introduces a set of architectural constraints and characteristics—a distributed environment, a hardware-level preference for bf16, and a compiler designed to exploit these features—that form the environment in which the sampling bug emerged.

### **1.4 The Bridge Between Code and Hardware: The XLA Compiler**

The raw power of TPU hardware would be inaccessible without a sophisticated software layer to translate high-level machine learning code into optimized machine instructions. This is the role of the **Accelerated Linear Algebra (XLA) compiler**.20 XLA acts as a just-in-time (JIT) compiler for ML frameworks like PyTorch, TensorFlow, and JAX.13 When a model is run on a TPU, XLA takes the computational graph defined by the framework and performs a series of powerful optimizations before compiling it into machine code specifically tailored for the TPU architecture.14

XLA is far more than a simple code translator. Its primary function is to perform high-level, domain-specific optimizations on the entire computational graph. For example, it can analyze the sequence of operations and "fuse" multiple individual operations (like a multiplication, an addition, and an activation function) into a single, highly optimized kernel. This reduces memory access overhead and allows the hardware to be used more efficiently.13 Another critical optimization is "tiling," where XLA breaks down large matrix multiplications into smaller chunks that perfectly fit the physical dimensions of the TPU's MXU systolic array (e.g., 128x128), minimizing wasted computation and padding.13

To enable these global optimizations, frameworks like PyTorch when used with XLA adopt a **lazy execution** model.21 Instead of executing each operation immediately as it is defined in the code (eager execution), the operations are first recorded as a graph. Only when a result is explicitly needed (e.g., to print a value to the console or at the end of a training step) is the entire graph passed to XLA for compilation and execution. This deferred execution is generally invisible to the developer but is fundamental to how XLA achieves its performance gains, as it gives the compiler a complete view of the computation to be performed, allowing for more holistic optimizations.21

This architecture establishes a clear causal chain of dependencies. The need for performance at scale drives the choice of specialized hardware (TPUs). This hardware choice mandates the use of a specific compiler (XLA) and strongly encourages a particular numerical format (bf16). This creates a tightly coupled technology stack where a seemingly low-level detail, such as a compiler optimization flag, can have a direct and non-obvious impact on a high-level algorithmic component like top-p sampling. The bug was not a failure of any single technology in isolation, but a failure at the seams where they connect. Top-p sampling is a high-level, abstract algorithm, but its correct implementation in a distributed, mixed-precision environment is anything but abstract. It depends critically on the assumption that fundamental operations, like comparing two numbers to find the maximum, are deterministic and consistent across the system. The bug represents a "leaky abstraction," where this assumption was violated by the underlying compiler's optimization choices, exposing the messy reality of the hardware below.

## **Section 2: The Perils and Promises of Mixed-Precision Computing**

At the core of the Anthropic Claude incident lies the concept of mixed-precision computing—a technique that has become indispensable for training and deploying large-scale neural networks. It offers profound performance benefits but introduces a new class of subtle numerical risks. The bug was a direct consequence of the trade-offs inherent in this approach, specifically the interaction between the standard 32-bit floating-point format (fp32) and the specialized 16-bit bfloat16 (bf16) format favored by TPUs.

### **2.1 A Tale of Two Floats: A Technical Comparison of FP32 and BF16**

To understand the failure mechanism, one must first understand how computers represent real numbers using floating-point formats, as defined by the IEEE 754 standard.22 A floating-point number is composed of three parts: a sign bit (indicating positive or negative), an exponent (determining the magnitude or range of the number), and a mantissa or significand (determining the precision or significant digits).24

**FP32 (Single-Precision Floating-Point):** This has long been the default format for scientific computing and deep learning.25 It uses 32 bits, allocated as follows:

* **Sign:** 1 bit  
* **Exponent:** 8 bits  
* **Mantissa:** 23 bits

This allocation provides a wide dynamic range (it can represent both very large and very small numbers) and a high degree of precision (approximately 7 decimal digits). This makes it numerically stable and reliable for a vast array of calculations.27 However, its 32-bit size makes it memory-intensive and computationally slower on hardware optimized for lower precisions.

**BF16 (Bfloat16 or Brain Floating-Point):** Developed by Google specifically for machine learning applications, bf16 is a 16-bit format with a unique design philosophy.27 It is allocated as follows:

* **Sign:** 1 bit  
* **Exponent:** 8 bits  
* **Mantissa:** 7 bits

The critical design choice here is that **bf16 retains the same 8-bit exponent as fp32**.19 This gives it an identical dynamic range, meaning it can represent numbers of the same magnitude as fp32. This is a crucial advantage over the other common 16-bit format, fp16 (which uses only 5 exponent bits), as it dramatically reduces the risk of "overflow" (numbers becoming too large) or "underflow" (numbers becoming too small and rounding to zero) during training.19 Consequently, training with bf16 often does not require complex techniques like loss scaling, which are frequently necessary with fp16 to keep gradients within its limited representable range.19

However, this benefit comes at a steep price: precision. With only 7 bits for the mantissa, bf16 can only represent numbers with about 2-3 decimal digits of precision, a significant reduction from fp32's 23 mantissa bits.19 This means that while bf16 can represent the number 123,456.789 just as easily as fp32 can in terms of magnitude, it will have to perform a much coarser rounding. This inherent imprecision—the source of rounding errors—is the direct physical mechanism that can cause two numbers that are very close in fp32 to become identical in bf16, or vice versa, setting the stage for algorithmic failures.

**Table 1: Comparison of Floating-Point Formats (FP32, BF16, and FP16)**

| Feature | FP32 (Single Precision) | BF16 (Brain Float) | FP16 (Half Precision) |
| :---- | :---- | :---- | :---- |
| **Total Bits** | 32 | 16 | 16 |
| **Sign Bits** | 1 | 1 | 1 |
| **Exponent Bits** | 8 | 8 | 5 |
| **Mantissa (Fraction) Bits** | 23 | 7 | 10 |
| **Exponent Bias** | 127 | 127 | 15 |
| **Dynamic Range (Approx.)** | 10−38 to 1038 | 10−38 to 1038 | 10−5 to 104 |
| **Decimal Precision (Approx.)** | \~7 digits | \~2-3 digits | \~3-4 digits |

### **2.2 The Need for Speed: Why Mixed Precision is Essential for Large Models**

Despite the risks of reduced precision, the AI industry has overwhelmingly adopted mixed-precision training as a standard practice for one simple reason: performance.31 The computational and memory costs of training state-of-the-art models using only fp32 are prohibitive. Mixed precision offers a pragmatic solution by combining the speed of lower-precision formats with the stability of fp32, yielding several key benefits:

1. **Faster Computations:** Modern accelerators like Google's TPUs and NVIDIA's GPUs (with their Tensor Cores) are architecturally designed to perform mathematical operations on 16-bit numbers far more quickly than on 32-bit numbers. An NVIDIA A100 GPU, for example, can achieve over 15 times more floating-point operations per second (FLOPs) using fp16/bf16 compared to fp32.31 This translates directly into dramatically shorter training times.  
2. **Reduced Memory Usage:** Every parameter, activation, and gradient stored in bf16 occupies half the memory of its fp32 counterpart. This reduction is critical. It allows engineers to either train much larger models with billions more parameters on the same hardware or increase the training batch size, which can improve hardware utilization and sometimes lead to faster model convergence.31  
3. **Lower Memory Bandwidth and Power Consumption:** Moving 16-bit values between different levels of memory or across the network in a distributed system requires half the bandwidth of 32-bit values. This reduces data transfer bottlenecks, which are often a limiting factor in large-scale training, and leads to lower power consumption and, consequently, lower operational costs.31

To manage the risks of reduced precision, frameworks like PyTorch and TensorFlow have implemented **Automatic Mixed Precision (AMP)** features.25 With AMP, a developer can enable mixed precision with just a few lines of code. The framework then automatically identifies which operations in the model's computational graph are safe to run in bf16 or fp16 (typically matrix multiplications and convolutions) and which require the stability of fp32. To maintain accuracy, a master copy of the model's weights is often kept in fp32, and the small gradient updates are accumulated in this higher-precision format before being cast back down to 16-bit for the next training step.29

### **2.3 Ghosts in the Machine: The Latent Risks of Numerical Instability**

The widespread adoption of bf16 is predicated on an implicit assumption: that the statistical nature of neural network training is resilient to the format's lower precision.31 For many parts of the training process, such as the aggregation of thousands of gradients in a batch update, this holds true. The random noise introduced by bf16's rounding errors can be seen as a form of regularization and often does not impede the model's ability to converge.

However, the Anthropic bug exposes a critical flaw in this assumption. Not all operations within a deep learning pipeline are fuzzy, statistical processes. Some are deterministic, discrete algorithms where correctness depends on exact numerical comparisons. Operations like sorting a list of probabilities or finding the single maximum value—both essential steps in top-p and top-k sampling—are highly sensitive to precision.36 A minute rounding error, completely inconsequential for a gradient update, can be the difference between a token being ranked \#1 or \#2, fundamentally altering the outcome of the sampling algorithm. The system, in this case, treated a deterministic selection algorithm with the same numerical nonchalance as a statistical optimization process, and this is where the failure occurred.

This incident was not caused by using bf16 alone, but by the *inconsistent* application of precision across a distributed system. The xla\_allow\_excess\_precision flag, intended as a performance optimization, created a state where different parts of the system held slightly different numerical truths. This reveals a deeper principle of complex numerical systems: optimizations that introduce inconsistency are a primary source of instability. It is often safer for a system to be consistently low-precision than to be inconsistently and unpredictably precise. The bug was not an anomaly but a manifestation of a known class of problems—numerical instability—appearing in a novel and subtle way through the unexpected interaction of a hardware feature, a compiler optimization, and an application-level algorithm.

## **Section 3: Anatomy of a Systemic Failure: Deconstructing the Claude Incident**

The degradation of Claude's performance in late 2025 was not a simple bug but a complex systemic failure. Its deconstruction requires tracing a causal chain from a low-level compiler flag through the intricacies of distributed, mixed-precision computation to its ultimate impact on the model's generated output. Anthropic's public postmortem provides a rare and valuable look into the anatomy of such a failure and the formidable challenges of diagnosing it in a live, large-scale production environment.11

### **3.1 The Official Postmortem: A Cascade of Interacting Failures**

A key finding from Anthropic's investigation was that the widespread issues users experienced were not attributable to a single root cause. Instead, three distinct and overlapping infrastructure bugs occurred simultaneously, creating a "fog of war" that made diagnosis exceptionally difficult.11 The symptoms of these bugs were varied and appeared at different rates on different platforms, presenting a confusing and seemingly random pattern of degradation to both users and engineers.11

The three concurrent issues were:

1. **Context Window Routing Error:** Introduced on August 5, this bug incorrectly routed some requests intended for standard context-window servers to a new cluster configured for an upcoming 1-million-token context window. A routine load-balancing change on August 29 dramatically increased the volume of misrouted traffic, amplifying the bug's impact from affecting 0.8% of Sonnet 4 requests to a peak of 16%.11  
2. **Output Corruption:** A misconfiguration deployed on August 25 caused a runtime optimization error that would occasionally assign a very high probability to an incorrect token. This resulted in bizarre outputs, such as random Thai or Chinese characters appearing in the middle of an English response or obvious syntax errors in generated code.11  
3. **Approximate top-k XLA:TPU Miscompilation:** This was the most subtle and technically complex of the three bugs and the focus of this analysis. It was a latent issue in the XLA compiler that was triggered by a code change on August 25, intended to improve token selection. This bug was at the heart of the logical and coherence failures reported by users.11

The overlapping timelines of these failures were central to the diagnostic challenge. A user reporting nonsensical code could have been a victim of any of the three issues, making it nearly impossible to isolate a single cause from individual reports.

**Table 2: Chronological Timeline of the Anthropic Claude Incident (August-September 2025\)**

| Date | Event | Impact/Significance |
| :---- | :---- | :---- |
| **Aug 5** | Context window routing error introduced. | Initially affects a small fraction (\~0.8%) of Sonnet 4 requests.11 |
| **Aug 25** | Output corruption misconfiguration deployed. | Affects Opus and Sonnet models, causing random incorrect characters in responses.11 |
| **Aug 25** | New token selection code deployed. | This change inadvertently triggers the latent XLA compiler bug related to mixed precision.11 |
| **Aug 29** | Routine load balancing change implemented. | Unintentionally increases traffic to misconfigured servers, dramatically worsening the impact of the routing error.11 User reports spike. |
| **Sep 2** | Output corruption issue identified and rolled back. | One of the three sources of error is eliminated, helping to narrow the investigation.11 |
| **Sep 4** | Fix for context window routing logic deployed. | Begins to resolve the routing error, a major source of user-facing degradation.11 |
| **Sep 4** | Approximate top-k bug observed on Haiku 3.5 and rolled back. | First concrete identification and mitigation of the sampling bug on a specific model.11 |
| **Sep 12** | Approximate top-k bug rolled back for Opus 3\. | The fix is extended to another model based on compatible user reports.11 |
| **Sep 16-18** | Full rollout of the routing logic fix completed. | The last of the three major bugs is fully resolved across all platforms.11 |

### **3.2 The Root Cause: A Collision of Optimization and Precision**

The core of the sampling bug lay in the interaction between mixed-precision arithmetic and a specific XLA compiler optimization flag: xla\_allow\_excess\_precision. This boolean flag, which defaults to true, grants the compiler permission to increase the precision of floating-point operations beyond what is specified in the code if doing so can improve performance.11

The scenario at Anthropic was a textbook case for this optimization. Their models compute next-token probabilities in the bf16 format. These computations run on TPUs, whose Vector Processing Units (VPUs)—responsible for non-matrix operations—are fp32-native.11 With

xla\_allow\_excess\_precision enabled, the XLA compiler would identify operations destined for the VPU and opportunistically "up-cast" them from bf16 to fp32 to leverage the VPU's native speed. Crucially, Anthropic's postmortem notes that this is the *expected and intended behavior* of the flag, not a bug in the flag itself.11

The problem arose because Claude's inference runs on a distributed system of multiple TPU chips. The calculation of the full probability distribution for the next token was sharded, with different parts of the calculation happening in different physical locations \[User Query\]. Due to the JIT compiler's opportunistic optimization, some of these parallel computations remained in bf16 while others were up-cast to fp32. This created a critical **precision mismatch**: different parts of a single, logical operation were being executed with different levels of numerical precision.11

### **3.3 The Critical Consequence: Vanishing of the Most Probable Token**

This state of inconsistent precision had a catastrophic effect on the deterministic algorithm used to identify the most probable tokens for top-p sampling. The process of forming the sampling nucleus requires, as a first step, sorting all token probabilities to identify the most likely candidates. In a distributed system, this requires all chips to agree on the relative ordering of probabilities.

However, due to the precision mismatch, this agreement broke down. A token's probability value, when represented in the less precise bf16 format, might be rounded slightly differently than its fp32 representation on another chip. For two tokens with very similar probabilities, this tiny difference could be enough to flip their relative ranking.

For instance, consider two tokens, A and B:

* On a chip using fp32, their probabilities might be calculated as: P(A)=0.10000001 and P(B)=0.10000000. Here, P(A)\>P(B).  
* On a chip using bf16, these values might be rounded to: P(A)=0.1000 and P(B)=0.1000. Here, P(A)=P(B).

When the distributed algorithm attempted to reconcile these conflicting views to find the single highest-probability token, the disagreement could cause the true top token to be discarded entirely from the candidate set.11 This meant that before the top-p nucleus was even formed, the most logical and contextually appropriate next word was sometimes removed from consideration. The model was then forced to sample from a pool of less likely, and often incorrect, alternatives. This is the direct causal link between the low-level numerical inconsistency and the high-level degradation in model quality, coherence, and reliability that users observed.4

### **3.4 The Diagnostic Quagmire: Why the Bug Proved So Elusive**

Identifying this root cause proved to be an immense engineering challenge, making the incident a powerful case study in the difficulties of debugging modern AI systems. Several factors contributed to this "diagnostic quagmire":

* **The "Heisenbug" Phenomenon:** The bug was a classic "Heisenbug"—an issue that alters or disappears when one tries to observe it. Its manifestation was dependent on a specific combination of batch size, model configuration, and even whether debugging tools were enabled.11 These factors can change low-level system properties like memory layout, data alignment, or the specific optimizations chosen by the JIT compiler, meaning the exact conditions for the failure were rare and difficult to reproduce deliberately.  
* **Technical Debt and Latent Risk:** The investigation revealed that a workaround had been implemented in December 2024 to patch a symptom of the same underlying problem (an unexpected dropped token when sampling with temperature=0).11 This patch addressed the symptom without fixing the root cause, creating a form of technical debt. When the new sampling code was deployed on August 25, it interacted with this latent, unaddressed issue in the compiler's  
  *approximate* top-k operation, triggering a more severe and widespread failure.11 This demonstrates how quick fixes in complex numerical systems can mask deeper risks that inevitably resurface.  
* **Evaluation and Observability Gaps:** Anthropic candidly admitted that their internal evaluation suites were not sensitive enough to detect this kind of qualitative degradation. The model would often recover quickly from a single bad token choice, meaning standard benchmark scores were not significantly affected.11 Furthermore, their internal privacy policies, while important, restricted engineers' ability to inspect the specific user interactions that triggered the bug, creating a critical observability gap.11  
* **The Compounding Effect of Failures:** The simultaneous occurrence of the routing error and the output corruption bug created a storm of confusing and contradictory symptoms. This made it nearly impossible to attribute any single user report to a specific cause, multiplying the diagnostic complexity. The signal from the sampling bug was drowned out by the noise from the other two failures.

The final solution was multi-faceted. Anthropic rolled back the problematic code changes and worked with the XLA:TPU team on a compiler fix. More importantly, they made a strategic architectural change: they switched from the performance-optimized *approximate* top-k algorithm to a more robust *exact* top-k implementation and standardized more operations on fp32. They explicitly stated that "model quality is non-negotiable," accepting a "minor efficiency impact" in exchange for numerical stability and correctness.11

## **Section 4: The Human Dimension: User Impact and Corporate Transparency**

The technical complexities of the Claude incident ultimately translated into a tangible and frustrating experience for its users. The public-facing dimension of the failure—from user reports of degraded performance to the community's reaction to the official explanation—provides crucial insights into the challenges of communication, transparency, and trust in the rapidly evolving AI landscape.

### **4.1 From "Skill Issue" to Systemic Bug: A Chronicle of User Experience**

In the weeks leading up to Anthropic's official acknowledgment, a growing chorus of users on platforms like Reddit and Twitter began documenting a noticeable decline in Claude's capabilities.41 Initially, these reports were often met with skepticism from other community members, who dismissed them as user error or a "skill issue"—a common dynamic where the perceived stochasticity of AI models leads to the assumption that poor outputs are the user's fault.41

However, as reports mounted, a clear pattern of specific, repeatable failures emerged. These were not subtle drops in quality but fundamental breakdowns in the model's core competencies:

* **Degradation in Coding and Logic:** Users who relied on Claude for software development reported the most dramatic changes. One user described how the model, which previously could analyze and refactor multi-page, complex stored procedures in a single pass, was now failing to fix basic SQL queries after multiple attempts.41 Another noted that the model had gone from proactively improving code to forgetting instructions mid-task and introducing buggy fallbacks instead of correct solutions.41  
* **Logical Incoherence and Repetition:** The model exhibited signs of getting "stuck." It would repeatedly generate the same erroneous code or text, seemingly unable to break out of a failure loop.41 In conversational contexts, users found the model would sometimes ignore the most recent prompt and instead generate a response to the  
  *previous* one, indicating a breakdown in its ability to correctly process conversational history.43  
* **General Unreliability:** The overarching sentiment was one of frustration and lost productivity. Users felt they were spending more time correcting the model's mistakes than benefiting from its assistance, with one lamenting that they were now acting as a "QA team" for a product they were paying for.41

When Anthropic published its postmortem on September 17, 2025, it provided a sense of validation for these users. The detailed technical explanation confirmed that the perceived degradation was real and rooted in a series of complex infrastructure bugs, not user error.11

**Table 3: Categorization of User-Reported Model Degradations**

| Category of Degradation | User-Provided Description (Quote) | Likely Technical Cause(s) |
| :---- | :---- | :---- |
| **Incorrect Code Generation** | "I'm running tests with basic SQL Server queries, and it failed over 6 times — literally rewriting the exact same query with the exact same error." 41 | **Approximate top-k Sampling Bug:** Dropping the most likely (correct) token forces the model to choose a suboptimal, often syntactically or logically incorrect, alternative. |
| **Logical Incoherence / Repetition** | "The answers will be repetitive, ignoring the current prompt and repeating the last answer. Other times it will answer the previous prompt and then answer the new question." 43 | **Approximate top-k Sampling Bug:** A failure in token selection can break the logical flow of generation. **Context Window Routing Error:** Being routed to the wrong server could corrupt context handling. |
| **Ignoring Instructions** | "Now it goes off to fix 'x', forgets 'y', and then decides 'x' is too complicated so it adds a fallback for when 'x' fails..." 41 | **Approximate top-k Sampling Bug:** The model's ability to follow complex, multi-part instructions is compromised when its core generation mechanism is flawed. |
| **Nonsensical / Foreign Language Output** | A small subset of users asking a question in English might have seen "สวัสดี" (Thai for "hello") in the middle of the response. 11 | **Output Corruption Misconfiguration:** A specific runtime optimization error that incorrectly assigned high probability to random, out-of-context tokens. |

### **4.2 The Trust Equation: Public Skepticism and the Challenge of Technical Communication**

While the detailed postmortem was appreciated by many technically-minded users, it did not fully quell the skepticism within the broader community. The incident highlighted a significant challenge for AI companies: communicating complex technical failures to a public that is often predisposed to simpler, economically-motivated explanations.

A prevalent alternative theory that circulated widely was that the degradation was not a bug at all, but a deliberate, unannounced "nerfing" of the model's capabilities to reduce operational costs.41 This narrative was fueled by several factors:

* **A History of "Silent" Changes:** Users across the AI ecosystem have grown accustomed to models changing their behavior without formal announcements, leading to a general atmosphere of distrust.  
* **Perceived Performance Variation:** Some users reported that Claude's performance seemed to fluctuate depending on the time of day, which they interpreted as evidence of dynamic resource allocation to manage costs, rather than a bug.41  
* **Delayed Acknowledgment:** Anthropic's initial silence on the issue, while engineers were likely working to diagnose the complex problem, allowed the cost-cutting narrative to take root and spread. By the time the official explanation was released, many had already settled on their own conclusions.41

This situation reveals a critical perceptual gap between a system's operator and its end-users. From Anthropic's perspective, the initial routing bug affected only 0.8% of requests—a minor, low-priority issue from a global systems standpoint.11 However, for a user who was unlucky enough to be affected by the "sticky" routing and experienced failures on multiple consecutive prompts, the model was perceived as being 100% broken.11 The company's communication of a "small percentage" of affected requests, while statistically accurate, failed to resonate with the lived experience of those most impacted, further fueling feelings of being dismissed.41

The community's immediate jump to the cost-cutting explanation is indicative of a deep-seated public narrative that AI companies are constantly balancing a trade-off between model quality and the immense cost of computation. In the absence of proactive, transparent, and real-time communication, any perceived degradation in performance will inevitably be interpreted through this economic lens. The actual technical cause—a "mixed-precision approximate top-k miscompilation"—is far too complex and nuanced for a general audience, making the simpler, economically-driven narrative more compelling and harder to dislodge. This incident demonstrates that for AI companies, building and maintaining user trust requires not only technical excellence but also a sophisticated and empathetic communication strategy.

## **Section 5: Broader Implications and Future-Proofing AI Systems**

The Anthropic Claude incident, while specific in its technical details, is a microcosm of the macro-level challenges facing the entire field of artificial intelligence as it moves from research into production at a global scale. The failure was not an isolated anomaly but an exemplar of the emergent risks inherent in highly complex, distributed computing systems. The lessons learned from its diagnosis and resolution offer a valuable framework for building the more resilient, reliable, and trustworthy AI infrastructure of the future.

### **5.1 A Microcosm of Macro Challenges: Numerical Integrity in Distributed Deep Learning**

The collision between bf16 and fp32 precision at the heart of the Claude bug is emblematic of a field-wide struggle with numerical integrity.32 The relentless drive for performance has pushed the industry toward lower-precision numerical formats, a trend enabled by hardware advancements in TPUs and GPUs.32 While this move is essential for making large models computationally tractable, it comes with the constant threat of numerical instability.37

The deep learning community has developed a set of best practices to mitigate the most common risks. Techniques like **loss scaling**—where the loss value is artificially multiplied before backpropagation to prevent small gradients from underflowing to zero in fp16, and then divided out before the weight update—are standard practice.33 Similarly, maintaining a

**master copy of the model weights in fp32** while performing the forward and backward passes in 16-bit precision is a common strategy to ensure that small, incremental updates are not lost to rounding errors.33

The Claude bug, however, represents a more insidious class of numerical problem. It was not a classic case of gradients vanishing or exploding, but a failure of a deterministic algorithm (sorting) due to inconsistent precision. This highlights that as AI systems incorporate more complex, multi-step logic beyond simple matrix multiplication, the surface area for numerical bugs expands. It is no longer sufficient to ensure that the training process as a whole converges; one must also guarantee the numerical correctness of every discrete algorithmic component within the pipeline.

### **5.2 The Inevitability of Emergent Failures at Scale**

The nature of the Claude bug—intermittent, dependent on specific configurations, and arising from an unforeseen interaction between multiple system layers—is characteristic of failures in other large-scale, high-performance computing (HPC) environments.45 Research into the reliability of supercomputers and massive data centers has shown that as the number of components in a system grows, the probability of rare and complex failures approaches certainty.48

A single high-end GPU may have a mean time between failures (MTBF) of several years, but in a cluster of 100,000 GPUs, a failure can be expected every 30 minutes.49 While many of these are straightforward hardware faults, a subset are "emergent" failures that cannot be traced to a single broken component. They arise from the complex interplay of hardware, firmware, drivers, operating systems, compilers, and application logic.50 The Claude bug is a perfect example of this class of failure. The hardware was functioning as designed. The compiler flag was behaving as intended. The sampling algorithm was logically correct. The failure occurred only when all three were combined in a specific configuration within a distributed environment.

This reality suggests that a paradigm shift is needed in how AI infrastructure is designed and tested. A "component-level" approach to quality assurance, where each part is tested in isolation, is no longer sufficient. Systems must be designed and validated with the assumption that these complex, multi-layer interactions will produce unexpected and undesirable behaviors.

### **5.3 Toward More Resilient AI Infrastructure: A Framework of Recommendations**

The analysis of the Claude incident yields a set of actionable best practices that can help the industry build more robust AI systems. These recommendations span the full stack, from compiler design to operational culture.

**Compiler and Runtime:**

* **Adopt the Principle of Least Astonishment:** Compiler optimizations that carry a risk of breaking numerical determinism or correctness, such as xla\_allow\_excess\_precision, should not be enabled by default. Performance-enhancing flags with potential side effects should be opt-in, forcing developers to consciously evaluate the trade-offs rather than unknowingly inheriting risk.  
* **Implement Precision-Aware Testing:** AI development pipelines need a new class of tests that specifically target numerical stability in distributed environments. This includes integration tests that run identical computations across multiple devices and assert bit-for-bit consistency for deterministic operations. Techniques like "numerical fuzzing," where inputs are perturbed with tiny variations to check for divergent outputs, can help uncover sensitivities to rounding errors before they become production incidents.

**Monitoring and Evaluation:**

* **Move Beyond Benchmarks:** While standard academic benchmarks are useful for measuring model capabilities, they are often insensitive to the kinds of intermittent, qualitative degradations seen in this incident. Organizations must invest in more sophisticated evaluation suites that include adversarial testing, consistency checks (e.g., does the model give the same answer to the same question multiple times?), and statistical monitoring of output token distributions to detect anomalies that might indicate an underlying problem.  
* **Develop Privacy-Preserving Observability:** The tension between user privacy and the need for engineers to debug production failures is a critical challenge.11 The industry must invest in privacy-enhancing technologies—such as differential privacy and on-device logging—that allow for the collection of the necessary diagnostic data without exposing sensitive user content.

**Operations and Culture:**

* **Proactive Management of Technical Debt:** Workarounds for numerical issues, like the one Anthropic implemented in December 2024, should be treated as high-priority technical debt. They are signals of a deeper, poorly understood problem. Instead of being left in place, they should trigger a thorough root cause analysis to ensure a latent risk is not allowed to fester.  
* **Embrace Radical Transparency:** In the event of a user-facing degradation, the default should be to communicate early and often, even before a full root cause is understood. Acknowledging a problem quickly builds trust and preempts the spread of speculation and misinformation. The technical details can follow, but the initial act of acknowledgment is critical for managing community perception.

Ultimately, the most significant lesson from the Claude incident may be a philosophical one about the maturation of AI engineering. The final fix involved a deliberate choice to prioritize resilience over peak performance by switching to an "exact" top-k algorithm and accepting a minor efficiency hit for "non-negotiable" model quality.11 This reflects a shift from a research-oriented mindset, focused on maximizing performance at all costs, to a production engineering mindset, focused on guaranteeing reliability, determinism, and correctness. As AI systems become more deeply embedded in the critical functions of business and society, this trade-off in favor of resilience will become not just a best practice, but a fundamental requirement.

## **Conclusion**

The Anthropic Claude sampling bug of 2025 stands as a seminal case study in the field of large-scale AI systems engineering. It was not a simple coding error but a profound systemic failure, born from the volatile intersection of distributed computing, mixed-precision arithmetic, and automated compiler optimization. The incident's root cause—a precision mismatch triggered by the xla\_allow\_excess\_precision flag that led to the erroneous deletion of the most probable next token—demonstrates with stark clarity how a seemingly innocuous, low-level performance enhancement can cascade through a complex system to produce a catastrophic failure in high-level algorithmic logic.

This analysis has revealed several critical, industry-wide truths. First, the pursuit of computational efficiency through lower-precision formats like bfloat16, while necessary, creates a new and subtle class of numerical risks. The assumption that all parts of a deep learning pipeline are equally tolerant of imprecision is a dangerous fallacy; deterministic algorithms embedded within these systems require a higher standard of numerical guarantees. Second, as AI infrastructure scales to tens or hundreds of thousands of processors, the probability of rare, emergent failures arising from unforeseen interactions between system layers approaches certainty. This necessitates a paradigm shift in testing and validation, moving beyond component-level checks to holistic, system-wide stress testing that anticipates these complex interactions. The compiler, in particular, has emerged as a new and critical frontier for reliability engineering, as its optimization heuristics can become a primary source of instability.

Furthermore, the human dimension of the incident highlights an urgent need for greater transparency and more sophisticated communication strategies within the AI industry. The gap between the statistical reality of an intermittent bug and the lived experience of an affected user, combined with a pre-existing climate of distrust, creates fertile ground for speculation that can erode public confidence. Proactive acknowledgment and clear, honest communication are as vital to managing a crisis as the engineering work required to fix it.

Ultimately, the resolution of the bug—Anthropic's decision to favor the correctness of an "exact" algorithm over the speed of an "approximate" one—signals a necessary maturation of the field. As AI transitions from a domain of experimental research to one of critical production infrastructure, the engineering calculus must evolve. The relentless pursuit of peak performance must be tempered by a disciplined commitment to resilience, determinism, and reliability. The precision paradox, where the tools of optimization become the agents of failure, serves as a powerful lesson: in the complex and fragile world of large-scale AI, the most important measure of performance is not speed, but trust.

#### **Works cited**

1. Top-p sampling \- Wikipedia, accessed on September 27, 2025, [https://en.wikipedia.org/wiki/Top-p\_sampling](https://en.wikipedia.org/wiki/Top-p_sampling)  
2. Large language model \- Wikipedia, accessed on September 27, 2025, [https://en.wikipedia.org/wiki/Large\_language\_model](https://en.wikipedia.org/wiki/Large_language_model)  
3. 4.8. Numerical Stability and Initialization \- Dive into Deep Learning, accessed on September 27, 2025, [https://classic.d2l.ai/chapter\_multilayer-perceptrons/numerical-stability-and-init.html](https://classic.d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html)  
4. Shorter Tokens Are More Likely — LessWrong, accessed on September 27, 2025, [https://www.lesswrong.com/posts/iZPKuuWsDXAcQWbLJ/shorter-tokens-are-more-likely](https://www.lesswrong.com/posts/iZPKuuWsDXAcQWbLJ/shorter-tokens-are-more-likely)  
5. Why Your AI Outputs Are Wrong: The Hidden Impact of Tokenization | by John Munn, accessed on September 27, 2025, [https://medium.com/@johnmunn/why-your-ai-outputs-are-wrong-the-hidden-impact-of-tokenization-e0ee443affcc](https://medium.com/@johnmunn/why-your-ai-outputs-are-wrong-the-hidden-impact-of-tokenization-e0ee443affcc)  
6. Nucleus Sampling (top\_p) \- Dreamsavior, accessed on September 27, 2025, [https://dreamsavior.net/docs/add-on/chatgpt-translator/parameters/nucleus-sampling-top\_p/](https://dreamsavior.net/docs/add-on/chatgpt-translator/parameters/nucleus-sampling-top_p/)  
7. LLM Basics: Top-p vs. Top-K Sampling Explained for Beginners \- YouTube, accessed on September 27, 2025, [https://www.youtube.com/watch?v=\_3DWwb96exY](https://www.youtube.com/watch?v=_3DWwb96exY)  
8. Min-p Sampling for Creative and Coherent LLM Outputs \- arXiv, accessed on September 27, 2025, [https://arxiv.org/pdf/2407.01082?](https://arxiv.org/pdf/2407.01082)  
9. arXiv:1904.09751v2 \[cs.CL\] 14 Feb 2020, accessed on September 27, 2025, [https://arxiv.org/pdf/1904.09751](https://arxiv.org/pdf/1904.09751)  
10. Top P Sampling Explained: Fine-Tune Language Model Outputs \- promptmate.io, accessed on September 27, 2025, [https://promptmate.io/top-p/](https://promptmate.io/top-p/)  
11. A postmortem of three recent issues \- Anthropic, accessed on September 27, 2025, [https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues)  
12. Min P Sampling: Balancing Creativity and Coherence at High Temperature \- arXiv, accessed on September 27, 2025, [https://arxiv.org/html/2407.01082v1](https://arxiv.org/html/2407.01082v1)  
13. Introduction to Cloud TPU | Google Cloud, accessed on September 27, 2025, [https://cloud.google.com/tpu/docs/intro-to-tpu](https://cloud.google.com/tpu/docs/intro-to-tpu)  
14. AI Hypercomputer TPUs \- TPU overview | Google Cloud Skills Boost, accessed on September 27, 2025, [https://www.cloudskillsboost.google/paths/2806/course\_templates/1405/documents/568752](https://www.cloudskillsboost.google/paths/2806/course_templates/1405/documents/568752)  
15. TPU architecture | Google Cloud, accessed on September 27, 2025, [https://cloud.google.com/tpu/docs/system-architecture-tpu-vm](https://cloud.google.com/tpu/docs/system-architecture-tpu-vm)  
16. Learn about TPUs — PyTorch/XLA master documentation, accessed on September 27, 2025, [https://docs.pytorch.org/xla/release/r2.7/accelerators/tpu.html](https://docs.pytorch.org/xla/release/r2.7/accelerators/tpu.html)  
17. Pytorch-XLA: Understanding TPU's and XLA \- Kaggle, accessed on September 27, 2025, [https://www.kaggle.com/code/tanulsingh077/pytorch-xla-understanding-tpu-s-and-xla](https://www.kaggle.com/code/tanulsingh077/pytorch-xla-understanding-tpu-s-and-xla)  
18. AI Hypercomputer TPUs \- Best practices for model development | Google Cloud Skills Boost, accessed on September 27, 2025, [https://www.cloudskillsboost.google/paths/2806/course\_templates/1405/documents/568759](https://www.cloudskillsboost.google/paths/2806/course_templates/1405/documents/568759)  
19. \[D\] Mixed Precision Training: Difference between BF16 and FP16 : r/MachineLearning, accessed on September 27, 2025, [https://www.reddit.com/r/MachineLearning/comments/vndtn8/d\_mixed\_precision\_training\_difference\_between/](https://www.reddit.com/r/MachineLearning/comments/vndtn8/d_mixed_precision_training_difference_between/)  
20. XLA \- OpenXLA Project, accessed on September 27, 2025, [https://openxla.org/xla](https://openxla.org/xla)  
21. PyTorch on XLA Devices, accessed on September 27, 2025, [https://docs.pytorch.org/xla/release/2.0/index.html](https://docs.pytorch.org/xla/release/2.0/index.html)  
22. IEEE 754 \- Wikipedia, accessed on September 27, 2025, [https://en.wikipedia.org/wiki/IEEE\_754](https://en.wikipedia.org/wiki/IEEE_754)  
23. IEEE Arithmetic, accessed on September 27, 2025, [https://docs.oracle.com/cd/E19957-01/806-3568/ncg\_math.html](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_math.html)  
24. IEEE Standard 754 Floating Point Numbers \- GeeksforGeeks, accessed on September 27, 2025, [https://www.geeksforgeeks.org/computer-organization-architecture/ieee-standard-754-floating-point-numbers/](https://www.geeksforgeeks.org/computer-organization-architecture/ieee-standard-754-floating-point-numbers/)  
25. Mixed Precision vs Standard Precision in AI Training | SabrePC Blog, accessed on September 27, 2025, [https://www.sabrepc.com/blog/deep-learning-and-ai/mixed-precision-vs-standard-precision-in-ai-training](https://www.sabrepc.com/blog/deep-learning-and-ai/mixed-precision-vs-standard-precision-in-ai-training)  
26. Understanding FP32, FP16, and INT8 Precision in Deep Learning Models: Why INT8 Calibration is Essential | by Vishalindev | Medium, accessed on September 27, 2025, [https://medium.com/@vishalindev/understanding-fp32-fp16-and-int8-precision-in-deep-learning-models-why-int8-calibration-is-5406b1c815a8](https://medium.com/@vishalindev/understanding-fp32-fp16-and-int8-precision-in-deep-learning-models-why-int8-calibration-is-5406b1c815a8)  
27. What is FP64, FP32, FP16? Defining Floating Point | Exxact Blog, accessed on September 27, 2025, [https://www.exxactcorp.com/blog/hpc/what-is-fp64-fp32-fp16](https://www.exxactcorp.com/blog/hpc/what-is-fp64-fp32-fp16)  
28. Floating points in deep learning: Understanding the basics | by Krinal Joshi | Medium, accessed on September 27, 2025, [https://medium.com/@krinaljoshi/floating-points-in-deep-learning-understanding-the-basics-93459f77a266](https://medium.com/@krinaljoshi/floating-points-in-deep-learning-understanding-the-basics-93459f77a266)  
29. BF16 vs FP16: A Comparison of Performance and Efficiency \- Beam Cloud, accessed on September 27, 2025, [https://www.beam.cloud/blog/bf16-vs-fp16](https://www.beam.cloud/blog/bf16-vs-fp16)  
30. A Study of BFLOAT16 for Deep Learning Training \- arXiv, accessed on September 27, 2025, [https://arxiv.org/pdf/1905.12322](https://arxiv.org/pdf/1905.12322)  
31. How can using FP16, BF16, or FP8 mixed precision speed up my ..., accessed on September 27, 2025, [https://www.runpod.io/articles/guides/fp16-bf16-fp8-mixed-precision-speed-up-my-model-training](https://www.runpod.io/articles/guides/fp16-bf16-fp8-mixed-precision-speed-up-my-model-training)  
32. Lower Numerical Precision Deep Learning Inference and Training \- Intel, accessed on September 27, 2025, [https://www.intel.com/content/dam/develop/external/us/en/documents/lower-numerical-precision-deep-learning-jan2018-754765.pdf](https://www.intel.com/content/dam/develop/external/us/en/documents/lower-numerical-precision-deep-learning-jan2018-754765.pdf)  
33. Train With Mixed Precision \- NVIDIA Docs \- NVIDIA Docs Hub, accessed on September 27, 2025, [https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html)  
34. Low-Precision Training of Large Language Models: Methods, Challenges, and Opportunities \- arXiv, accessed on September 27, 2025, [https://arxiv.org/html/2505.01043v1](https://arxiv.org/html/2505.01043v1)  
35. Numerical stability of DeepGOPlus inference | PLOS One, accessed on September 27, 2025, [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296725](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296725)  
36. A postmortem of three recent issues \- Hacker News, accessed on September 27, 2025, [https://news.ycombinator.com/item?id=45281139](https://news.ycombinator.com/item?id=45281139)  
37. DeepStability: a study of unstable numerical methods and their solutions in deep learning, accessed on September 27, 2025, [https://www.researchgate.net/publication/362968232\_DeepStability\_a\_study\_of\_unstable\_numerical\_methods\_and\_their\_solutions\_in\_deep\_learning](https://www.researchgate.net/publication/362968232_DeepStability_a_study_of_unstable_numerical_methods_and_their_solutions_in_deep_learning)  
38. tensorflow/compiler/xla/xla.proto \- platform/external/tensorflow \- Git at Google, accessed on September 27, 2025, [https://android.googlesource.com/platform/external/tensorflow/+/632ff3f6169ef18a6947c53bd6f3cb5bf7fc26a6/tensorflow/compiler/xla/xla.proto](https://android.googlesource.com/platform/external/tensorflow/+/632ff3f6169ef18a6947c53bd6f3cb5bf7fc26a6/tensorflow/compiler/xla/xla.proto)  
39. All XLA Options \- guides.lw1.at, accessed on September 27, 2025, [https://guides.lw1.at/all-xla-options/](https://guides.lw1.at/all-xla-options/)  
40. Don't Ever Drop the First Token.. A gentle introduction to LLM streaming… \- Medium, accessed on September 27, 2025, [https://medium.com/@crclq2018/dont-ever-drop-the-first-token-here-s-why-cf86a5013800](https://medium.com/@crclq2018/dont-ever-drop-the-first-token-here-s-why-cf86a5013800)  
41. Now that Claude admitted the performance bug… : r/Anthropic \- Reddit, accessed on September 27, 2025, [https://www.reddit.com/r/Anthropic/comments/1nc5kwv/now\_that\_claude\_admitted\_the\_performance\_bug/](https://www.reddit.com/r/Anthropic/comments/1nc5kwv/now_that_claude_admitted_the_performance_bug/)  
42. Claude Code is BACK? Anthropic FINALLY Fixes it (Apparently) \- YouTube, accessed on September 27, 2025, [https://www.youtube.com/watch?v=PljZOdMYYr0](https://www.youtube.com/watch?v=PljZOdMYYr0)  
43. Bug report: Claude replying to both current and previous user message : r/Anthropic \- Reddit, accessed on September 27, 2025, [https://www.reddit.com/r/Anthropic/comments/1f3ntdg/bug\_report\_claude\_replying\_to\_both\_current\_and/](https://www.reddit.com/r/Anthropic/comments/1f3ntdg/bug_report_claude_replying_to_both_current_and/)  
44. Low Precision Training in Distributed ML Systems \- Shangdi Yu, accessed on September 27, 2025, [https://yushangdi.github.io/publication/lowprecision](https://yushangdi.github.io/publication/lowprecision)  
45. Understanding and Mitigating Hardware Failures in Deep Learning ..., accessed on September 27, 2025, [https://www.researchgate.net/publication/371666411\_Understanding\_and\_Mitigating\_Hardware\_Failures\_in\_Deep\_Learning\_Training\_Systems](https://www.researchgate.net/publication/371666411_Understanding_and_Mitigating_Hardware_Failures_in_Deep_Learning_Training_Systems)  
46. A large-scale study of failures in high-performance computing systems \- ResearchGate, accessed on September 27, 2025, [https://www.researchgate.net/publication/4243381\_A\_large-scale\_study\_of\_failures\_in\_high-performance\_computing\_systems](https://www.researchgate.net/publication/4243381_A_large-scale_study_of_failures_in_high-performance_computing_systems)  
47. Failure prediction for HPC systems and applications: Current situation and open issues \- Marc Snir, accessed on September 27, 2025, [https://snir.cs.illinois.edu/listed/J54.pdf](https://snir.cs.illinois.edu/listed/J54.pdf)  
48. What Can We Learn from Four Years of Data Center Hardware Failures?, accessed on September 27, 2025, [https://people.iiis.tsinghua.edu.cn/\~weixu/Krvdro9c/dsn17-wang.pdf](https://people.iiis.tsinghua.edu.cn/~weixu/Krvdro9c/dsn17-wang.pdf)  
49. Hardware Failures Won't Limit AI Scaling, accessed on September 27, 2025, [https://epoch.ai/blog/hardware-failures-wont-limit-ai-scaling](https://epoch.ai/blog/hardware-failures-wont-limit-ai-scaling)  
50. Predicting GPU Failures With High Precision Under Deep Learning Workloads \- Cheng Tan, accessed on September 27, 2025, [https://naizhengtan.github.io/doc/papers/liu23predicting.pdf](https://naizhengtan.github.io/doc/papers/liu23predicting.pdf)  
51. Revisiting Reliability in Large-Scale Machine Learning Research Clusters \- arXiv, accessed on September 27, 2025, [https://arxiv.org/html/2410.21680v1](https://arxiv.org/html/2410.21680v1)