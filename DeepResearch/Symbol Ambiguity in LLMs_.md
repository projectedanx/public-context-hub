# **Symbolic Syntax, Semantic Drift: A Multi-Lens Investigation of Special Character Languages in STEM and Machine Intelligence**

## **Abstract**

Specialized symbolic languages, incorporating Greek letters, mathematical operators, and structural notation, form the bedrock of precise communication in Science, Technology, Engineering, and Mathematics (STEM). While indispensable for human experts, these dense, context-dependent systems pose significant challenges for Large Language Models (LLMs) primarily trained on natural language. This report undertakes a multi-lens investigation into the processing, interpretation, and fidelity of symbolic languages within LLMs, focusing on their use in Physics, Statistics, and Machine Learning (ML). Employing lenses of Typological Semiotics, Domain Leakage & Polysemy, Token Budget vs. Semantic Load, Attention & Embedding Analysis, Reflexive Input Design, and Tool & Interface Reflexivity, the analysis reveals systemic issues. Key findings highlight the profound polysemy of symbols across domains, leading to ambiguity and semantic collapse when LLMs fail to adequately leverage context. Standard tokenization methods, often based on Byte-Pair Encoding (BPE) or similar algorithms optimized for natural language, frequently fragment atomic symbols, imposing a high token cost relative to semantic content and potentially obscuring meaning. Embedding space representations and attention mechanisms appear to struggle with consistent, function-aware handling of symbolic tokens, often influenced more by surface form or statistical frequency than semantic role. Prompting strategies and input/rendering environments further modulate interpretation, introducing additional variability. Current LLMs exhibit significant limitations in robustly handling the symbolic lingua franca of STEM, demonstrating shallow grounding and frequent reasoning errors even when syntax is correctly manipulated. The report concludes by synthesizing these challenges and suggesting avenues for future research, including symbol-aware tokenization, context-enhanced embeddings, neuro-symbolic integration, improved training data, advanced interpretability methods, and rigorous, process-oriented evaluation benchmarks, all crucial steps towards achieving higher-fidelity symbolic processing in artificial intelligence.

## **I. Introduction: The Lingua Franca of STEM and the Challenge for AI**

### **A. The Indispensable Role of Symbolic Languages**

Communication within and across STEM disciplines relies heavily on specialized systems of notation that extend far beyond standard natural language alphabets. Greek letters (e.g., $\\alpha, \\beta, \\mu, \\sigma, \\Delta, \\Omega$), mathematical operators (e.g., $\\nabla, \\partial, \\sum, \\int$), and structural syntax conventions (e.g., subscripts, superscripts, vector notation) constitute a lingua franca essential for expressing complex ideas with precision, conciseness, and universality.1 These symbols are not merely abbreviations; they function as carriers of dense semantic information, encapsulating definitions, variables, constants, operations, and conceptual relationships that would require verbose and potentially ambiguous natural language descriptions. The efficiency gained allows for rapid communication and manipulation of abstract concepts, forming the backbone of theoretical development, empirical analysis, and computational modeling in fields like physics, statistics, and machine learning. The historical adoption and refinement of these symbolic systems, such as the long-standing use of the Greek alphabet originating from ancient times 5 or the deliberate introduction of symbols like nabla ($\\nabla$) for vector calculus operations 6, underscore their cognitive utility in facilitating rigorous thought and unambiguous representation of specialized knowledge.

### **B. The Emergent Problem: LLMs Encountering Symbolic Diversity**

Large Language Models have demonstrated remarkable proficiency in processing and generating human language, achieving success across a wide array of natural language processing tasks.7 Their training on vast text corpora enables them to capture complex statistical patterns, syntax, and semantics inherent in natural discourse. However, the specialized symbolic languages prevalent in STEM domains present a distinct and formidable challenge. The meaning of symbols like $\\mu$ or $\\sigma$ is highly context-dependent, shifting dramatically between physics, statistics, and machine learning.1 Operators like $\\nabla$ imply specific computational procedures.11 The very structure of mathematical notation carries meaning. Current LLMs, often optimized for sequential text prediction, frequently struggle with the density, polysemy, and structural richness of these symbolic systems, leading to misinterpretations, reasoning errors, and failures in semantic fidelity.13 This report employs a multi-lens framework—encompassing Typological Semiotics, Domain Leakage & Polysemy, Token Budget vs. Semantic Load, Attention & Embedding Analysis, Reflexive Input Design, and Tool & Interface Reflexivity—to systematically investigate how LLMs interact with these symbolic languages, identifying both capabilities and critical limitations.

### **C. Report Objectives and Structure**

The primary objective of this report is to conduct a critical, multi-faceted investigation into the capabilities and limitations of contemporary LLMs in processing, interpreting, and utilizing the special character languages fundamental to Physics, Statistics, and Machine Learning. The analysis focuses on identifying sources of error, examining the fidelity of semantic representation, and understanding the impact of various factors—from tokenization strategies to prompting techniques and rendering environments—on model performance with symbolic input.

The report is structured as follows:

* **Section II (Typological Semiotics Lens):** Deconstructs the meaning and function of common Greek letters and mathematical operators across the target domains, establishing the baseline of symbolic polysemy and semantic density.  
* **Section III (Domain Leakage & Polysemy Lens):** Explores how overlapping symbol usage leads to ambiguity and semantic collapse in LLM interpretation, examining the role of priors and contextual cues.  
* **Section IV (Token Budget vs. Semantic Load Lens):** Investigates LLM tokenization strategies for symbols, analyzing potential fragmentation, inefficiency, and the impact on representing semantic load within token limits.  
* **Section V (Attention & Embedding Analysis Lens):** Delves into the internal representations of symbols within LLM embedding spaces and how attention mechanisms process symbolic tokens.  
* **Section VI (Reflexive Input Design Lens):** Examines the influence of prompt design, comparing symbolic versus descriptive inputs and the effectiveness of strategies aimed at improving clarity.  
* **Section VII (Tool & Interface Reflexivity Lens):** Assesses how input formats (LaTeX, Markdown, Unicode) and rendering environments affect LLM processing and interpretation of symbols, distinguishing surface rendering from genuine comprehension.  
* **Section VIII (Synthesis):** Integrates the findings from all lenses to provide a holistic assessment of current LLM capabilities and limitations with symbolic languages, highlighting key challenges and proposing future research directions for enhancing symbol fidelity in AI systems.

## **II. Typological Semiotics Lens: Deconstructing Symbol Function Across Domains**

Understanding how LLMs process symbolic languages requires first establishing a clear map of how these symbols function for human experts within different STEM fields. This section analyzes the specific meanings and roles of common Greek letters and mathematical operators in Physics, Statistics, and Machine Learning, highlighting the inherent polysemy and context-dependency that LLMs must navigate.

### **A. The Polysemy of Greek Letters**

Greek letters are ubiquitous in mathematical and scientific notation, but their meanings are far from universal, varying significantly depending on the disciplinary context.2 A single letter can represent a physical constant, a statistical parameter, a variable in an algorithm, or a mathematical concept, requiring careful interpretation based on surrounding information. Consider the following examples:

* **$\\alpha$ (Alpha):** Can denote an angle (geometry, physics) 2, the significance level in hypothesis testing (statistics, probability of Type I error) 1, the fine-structure constant (physics) 4, angular acceleration (physics) 2, a learning rate parameter (ML), or an alpha particle (physics).4  
* **$\\beta$ (Beta):** Represents another angle (geometry, physics) 2, the probability of Type II error in statistics 1, a regression coefficient (statistics, ML) 1, a beta particle (physics) 2, the sideslip angle of an aircraft (physics) 4, or a measure of non-diversifiable risk in finance.4  
* **$\\mu$ (Mu):** Commonly signifies the population mean in statistics 1, but also represents the coefficient of friction (physics) 3, magnetic permeability (physics) 10, the prefix "micro-" ($10^{-6}$) 10, or the muon elementary particle (physics).  
* **$\\sigma$ (Sigma, lowercase):** Primarily denotes the population standard deviation in statistics.1 In physics and engineering, it can represent electrical conductivity 21, stress 2, or radar cross section.21  
* **$\\Sigma$ (Sigma, uppercase):** Universally used for summation in mathematics and statistics.1 It can also denote the sum port in microwave networks.21  
* **$\\Delta$ (Delta, uppercase):** Often indicates a change or difference between two values (calculus, physics, finance).2 It can also represent the Laplace operator ($\\nabla^2$) 4, the discriminant of a polynomial 2, or specific particles in physics.10  
* **$\\delta$ (Delta, lowercase):** Represents a small change or increment (calculus) 4, the Dirac delta function or Kronecker delta (mathematics, physics) 4, variation in calculus of variations 4, partial charge in chemistry 4, or skin depth in electromagnetism.21  
* **$\\theta$ (Theta):** Frequently used for angles, particularly plane angles in geometry and trigonometry or specific angles in coordinate systems (physics).1 It can also denote potential temperature (thermodynamics) 4, parameters in statistical models or ML algorithms, or thermal resistance.21  
* **$\\lambda$ (Lambda):** Represents wavelength (physics) 3, eigenvalues (linear algebra, applicable in all three domains) 3, parameters of distributions like Poisson (statistics), or symbols in lambda calculus (computer science theory).4  
* **$\\omega$ (Omega, lowercase):** Commonly denotes angular frequency or angular velocity ($2\\pi f$) in physics and engineering.3 It can also represent a parameter space or outcome space in probability theory.  
* **$\\Omega$ (Omega, uppercase):** Symbol for Ohm, the unit of electrical resistance (physics, electronics).10 As the last letter of the Greek alphabet, it can metaphorically signify an endpoint or a totality (e.g., the sample space in probability).

This inherent polysemy necessitates strong reliance on context for disambiguation. The following table summarizes the primary meanings of selected symbols across the three domains:

**Table 1: Symbol Disambiguation Grid**

| Symbol | Physics Meaning/Use | Statistics Meaning/Use | Machine Learning Meaning/Use | Key Contextual Indicators |
| :---- | :---- | :---- | :---- | :---- |
| $\\alpha$ | Angle 2, angular acceleration 2, fine-structure constant 4, alpha particle 4 | Significance level (Type I error prob.) 1 | Learning rate 4, regularization parameter (e.g., Lasso/Ridge sometimes use $\\alpha$) | Equations involving motion, fields, particles; hypothesis testing language ("p-value", "reject null"); optimization algorithms, model training discussion |
| $\\beta$ | Angle 2, beta particle 2, velocity ratio ($v/c$) 4, plasma pressure ratio 4 | Regression coefficient 1, Type II error prob. 1 | Model parameter/weight (often in linear models, analogous to stats) 1, momentum term in optimization (sometimes) | Equations of motion, particle physics; regression models ("predictor", "response"), hypothesis testing; neural network layers, optimization algorithms |
| $\\mu$ | Coefficient of friction 3, permeability 10, prefix "micro-" 10, muon particle | Population mean 1 | Mean (e.g., in Gaussian distributions, clustering) 1, sometimes used for model parameters | Mechanics problems (friction), electromagnetism; probability distributions, population parameters; clustering algorithms (e.g., K-means), generative models |
| $\\sigma$ | Conductivity 21, stress 2, radar cross section 21, surface charge density | Population standard deviation 1 | Standard deviation (e.g., in Gaussian noise/distributions), activation function (sigmoid, rarely) | Electromagnetism, material science; probability distributions, variance, dispersion; generative models, activation functions (check context carefully) |
| $\\Delta$ | Change/difference 2, Laplace operator ($\\nabla^2$) 4, specific particles 10 | Difference operator 4, symmetric difference (set theory) | Change in value (e.g., weight update $\\Delta w$), sometimes used in differencing operations | Calculus notation ($\\Delta x$), differential equations, particle physics; set theory notation; gradient descent updates, reinforcement learning |
| $\\delta$ | Small change/increment 4, Dirac delta function 4, partial charge 4, skin depth 21 | Kronecker delta 4, error term (sometimes $\\epsilon$), noncentrality measure 4 | Small quantity, error term (often $\\epsilon$), activation derivative (backpropagation) | Calculus, functional analysis, chemistry; discrete math, error analysis; backpropagation steps, optimization theory |
| $\\theta$ | Angle (plane, spherical coordinates) 3, potential temperature 4, thermal resistance 21 | Parameter of a distribution 1 | Model parameters/weights (very common) 1 | Coordinate systems, thermodynamics; statistical modeling, parameter estimation; model definitions (especially probabilistic models, neural networks) |
| $\\lambda$ | Wavelength 3, eigenvalue 3, decay constant | Parameter (e.g., Poisson dist.) 1, eigenvalue 3 | Regularization parameter (L1/L2 penalty) 3, eigenvalue 3, parameter in RL/control | Wave equations, optics, linear algebra; probability distributions, linear algebra; optimization, regularization terms, reinforcement learning |
| $\\omega$ | Angular frequency/velocity 3 | Parameter space (often $\\Omega$) | Model parameter/weight (less common than $\\theta$), frequency in signal processing contexts | Oscillations, waves, rotations; probability theory notation; signal processing, some specific model architectures |
| $\\Omega$ | Ohm (unit of resistance) 10, solid angle | Sample space / Outcome space 1 | Complexity notation (Big Omega) | Electrical circuits, geometry; probability theory fundamentals; algorithm analysis |
| $\\Sigma$ | Summation 1, sum port 21 | Summation 1, Covariance matrix | Summation 1, Covariance matrix (e.g., in Gaussian models) | Mathematical formulas involving sums; multivariate statistics; multivariate probability distributions, Gaussian processes |

This table provides a structured overview of the polysemy challenge. It serves as a foundation for analyzing domain leakage (Section III) and LLM interpretation failures (Section VIII), highlighting the critical need for contextual disambiguation.

### **B. Mathematical Operators and Notational Conventions**

Beyond Greek letters, mathematical operators and notational conventions carry precise, often procedural, meanings that are fundamental to STEM discourse.

* **Differential Operators:** The nabla/del operator ($\\nabla$) is particularly versatile, representing the gradient when applied to a scalar field ($\\nabla f$), the divergence when dotted with a vector field ($\\nabla \\cdot \\mathbf{F}$), and the curl when crossed with a vector field ($\\nabla \\times \\mathbf{F}$) in vector calculus.6 Its interpretation is entirely dependent on the type of field it acts upon and the operation (scalar multiplication, dot product, cross product) implied by the context. The partial derivative symbol ($\\partial$) signifies differentiation with respect to one variable while holding others constant, distinct from the total derivative ($d$) and often visually similar but functionally different from lowercase delta ($\\delta$).4 The Laplacian operator, often written as $\\nabla^2$ or $\\Delta$, represents the divergence of the gradient and involves second-order partial derivatives.11  
* **Aggregation Operators:** Uppercase Sigma ($\\Sigma$) denotes summation over a specified range or set, while uppercase Pi ($\\Pi$) denotes the product.1 The integral sign ($\\int$) signifies integration. These operators require understanding the scope (limits of summation/integration, variables involved) often indicated by accompanying subscripts and superscripts.  
* **Structural Notation:** Subscripts and superscripts are crucial for indexing (e.g., $x\_i$ for the $i$-th element of a vector or sequence), indicating powers ($x^2$), denoting specific components (e.g., $F\_x$ for the x-component of force), or specifying derivatives ($f'(x), f'' (x)$). Hat notation ($\\hat{y}$) typically indicates an estimator or predicted value in statistics and ML, while bar notation ($\\bar{x}$) usually denotes a mean value.1 Vector notation (boldface $\\mathbf{v}$ or arrow $\\vec{v}$) distinguishes vector quantities from scalars.  
* **Statistical Conventions:** A key convention in statistics is the use of Greek letters for population parameters (unknown constants describing the entire population, e.g., $\\mu, \\sigma$) and Latin letters for sample statistics (values calculated from observed data, used to estimate parameters, e.g., $\\bar{x}, s$).1 Maintaining this distinction is vital for correct statistical inference.

### **C. Insights & Implications (Typological Semiotics)**

The analysis of symbol function across domains reveals critical characteristics that challenge LLM processing. Firstly, the semantic density per symbol is exceptionally high compared to typical natural language words.2 A single character like $\\beta$ can invoke complex concepts requiring significant background knowledge for disambiguation (e.g., Type II error probability vs. beta decay vs. regression coefficient).1 This density, while efficient for human experts, contrasts sharply with the more distributed nature of meaning in natural language, suggesting that models trained primarily on text prediction may struggle to decode such compact information without specific architectural adaptations or training objectives focused on symbolic languages.

Secondly, the reliance on fine-grained visual and typographical distinctions is paramount. Differences between Latin 'r' and Greek '$\\rho$' 1, or 'p' vs '$\\rho$', 'v' vs '$\\nu$' 10, or even uppercase $\\Sigma$ versus lowercase $\\sigma$ 1, carry significant semantic weight. Standard tokenization approaches, operating on character sequences or byte patterns 28, risk conflating these distinct symbols, particularly if they fall within similar Unicode ranges or have similar byte representations. Subsequent embedding layers might further group them based on visual similarity rather than function, hindering the model's ability to differentiate their roles.30 This contrasts with human expertise, which leverages precise typography for disambiguation.

Thirdly, many mathematical operators, such as $\\nabla$ or $\\partial$, are not just static symbols but procedural indicators, signifying specific mathematical operations or transformations.11 An LLM might learn to associate the symbol $\\nabla$ with the word "gradient" through co-occurrence in its training data, but this does not guarantee an understanding of the underlying vector calculus operations involving partial derivatives.11 The model might generate text *about* the gradient but fail to correctly compute or apply the operation based solely on the symbol, reflecting a potential gap between pattern recognition and procedural or symbolic reasoning capabilities.14

## **III. Domain Leakage & Polysemy Lens: Ambiguity and Semantic Collapse in LLMs**

The high degree of polysemy identified in Section II creates fertile ground for ambiguity and misinterpretation when LLMs encounter symbols used across different STEM domains. This section examines how overlapping symbol usage can lead to "domain leakage"—where the interpretation appropriate for one field is incorrectly applied in another—and semantic collapse within LLM processing.

### **A. Documented Cases of Symbol Confusion**

While specific, widely documented case studies of LLMs confusing, for instance, the statistical mean $\\mu$ 1 with the physics coefficient of friction $\\mu$ 3 are scarce in the readily available literature, the potential for such errors is evident given the established polysemy and observed general reasoning failures of LLMs in mathematical and scientific contexts.15 Based on the symbol meanings outlined (Table 1), plausible failure scenarios include:

* An LLM encountering $\\sigma$ in a materials science context (stress) might incorrectly interpret it as standard deviation (statistics) 1 if the surrounding text lacks strong disambiguating cues.  
* Seeing $\\Delta$ in a machine learning paper discussing model updates might lead to an interpretation related to finite differences (calculus) rather than the intended meaning of "change in value".2  
* The symbol $\\beta$ in an econometrics paper (regression coefficient) could be misconstrued as relating to Type II error probability if the model's statistical training data heavily emphasizes hypothesis testing contexts.1

The lack of explicit domain tagging in many documents or prompts exacerbates this. If a user query simply asks "What does $\\lambda$ represent in this formula: \[formula\]?", the LLM must infer the domain (physics, linear algebra, statistics) from the formula's structure or surrounding terms. Failure to do so correctly can lead to domain leakage.

### **B. The Role of Priors and Contextual Cues**

LLMs likely attempt symbol disambiguation by relying on contextual cues and internal priors established during training. Surrounding keywords like "particle physics," "hypothesis testing," or "neural network" can act as signals. However, the effectiveness of this approach is questionable, especially with subtle or implicit contexts. An LLM's "prior" for a symbol's meaning is heavily influenced by the frequency distribution in its training data.33 Symbols like $\\mu$ (mean) or $\\sigma$ (standard deviation) are likely far more frequent in general statistical contexts within large web crawls than their specialized physics counterparts (coefficient of friction, conductivity).1 Consequently, in ambiguous situations, the model may default to the statistically dominant meaning, irrespective of subtle contextual hints pointing elsewhere. This reliance on statistical priors over deep semantic understanding is a potential source of systematic error.8 Furthermore, scientific communication often relies on implicit domain knowledge shared among experts but not explicitly stated—a significant hurdle for LLMs that lack true world knowledge or domain-specific grounding.18

### **C. Failure Mode Audit (Conceptual)**

Based on the documented polysemy (Section II.A, Table 1\) and known LLM reasoning weaknesses 15, several potential failure modes related to symbol ambiguity can be identified:

1. **Domain Defaulting:** The LLM applies the most statistically frequent meaning of a symbol from its training data, ignoring contextual cues that suggest a less common, domain-specific interpretation. (e.g., always interpreting $\\mu$ as mean).  
2. **Contextual Misreading:** The LLM fails to recognize or correctly interpret explicit keywords or surrounding mathematical structures that signal the appropriate domain and symbol meaning.  
3. **Semantic Blending (Hallucination):** Faced with ambiguity, the LLM generates an explanation that incoherently mixes aspects of the symbol's meaning from different domains, creating a plausible-sounding but nonsensical interpretation.15  
4. **Symbol Collapse:** Due to visual similarity or tokenization artifacts (see Section IV), the LLM treats distinct symbols with different meanings (e.g., lowercase delta $\\delta$ vs. partial derivative $\\partial$ 4) as interchangeable, leading to incorrect mathematical statements or reasoning.

### **D. Insights & Implications (Domain Leakage & Polysemy)**

The challenges LLMs face with symbol polysemy point to fundamental limitations in their processing. Firstly, errors in interpretation appear systematic rather than random, likely arising from biases in training data (symbol frequency) coupled with potentially shallow contextual analysis.8 Models may lack robust mechanisms for grounding symbols in specific domain knowledge.18 If a symbol like $\\mu$ appears predominantly as 'mean' in the training corpus, the model develops a strong prior for this meaning. Overcoming this prior requires strong, recognizable contextual cues signaling an alternative meaning (like 'coefficient of friction'). When these cues are weak, absent, or misinterpreted due to limitations in the model's contextual understanding, the default (often statistical) meaning prevails, demonstrating a reliance on surface patterns over deeper semantic integration.

Secondly, the ambiguity problem is intensified by the nature of user interaction. The *exact same query* involving a polysemous symbol (e.g., "Explain $\\beta$ in $E \= mc^2 / \\sqrt{1-\\beta^2}$") could originate from users in different fields (physics vs. someone misapplying the symbol). The LLM must ideally infer the correct domain and meaning solely from the structure of the equation and conventional variable usage within that domain.1 This demands a sophisticated form of reasoning that integrates textual context with the parsing of mathematical syntax—a capability potentially hampered by linear tokenization of complex structures and a lack of inherent mathematical structure awareness.18

Thirdly, the phenomenon of LLM hallucination 15 poses a particular risk in the context of symbolic languages. Given the high degree of polysemy, an LLM facing an ambiguous symbol might generate a response by confabulating elements associated with that symbol across various domains encountered during training. This could result in explanations that sound fluent and technically plausible but are fundamentally incorrect or incoherent, potentially misleading users, especially those who are not domain experts themselves.15 Such errors are more insidious than simple factual mistakes as they can create a false sense of understanding.

## **IV. Token Budget vs. Semantic Load Lens: The Bottleneck of Representation**

The way LLMs convert text and symbols into sequences of tokens is a critical preprocessing step that significantly influences their ability to understand and reason about specialized notation.28 This section examines how common tokenization strategies handle STEM symbols and the potential mismatch between the high semantic load of these symbols and their often fragmented, inefficient token representations.

### **A. Tokenization Strategies for Symbols**

Modern LLMs predominantly employ subword tokenization algorithms like Byte-Pair Encoding (BPE) 33, WordPiece 43, or SentencePiece (which can implement BPE or Unigram models).43 Many recent models, including those from OpenAI (using tiktoken) and Meta (Llama), utilize byte-level BPE (BBPE).29

These methods are generally optimized for natural language, aiming to balance vocabulary size and sequence length while handling out-of-vocabulary (OOV) words by breaking them into known subwords or characters/bytes.28 BBPE, in particular, can represent any character via its underlying UTF-8 byte sequence, ensuring no character is truly "unknown".40 However, this universality comes at the cost of potential fragmentation for characters or symbols not included as single units in the tokenizer's vocabulary.

While direct evidence for the specific tokenization of symbols like $\\mu, \\sigma, \\nabla, \\partial, \\Sigma$ by widely used tokenizers like cl100k\_base or o200k\_base is limited in the provided materials 52, their underlying principles suggest likely behaviors. Infrequently occurring symbols or those outside the common alphanumeric ranges might be broken down into multiple tokens, potentially corresponding to their individual bytes in a UTF-8 representation.40 For example, a symbol like $\\Sigma$ might become one token if it's frequent enough to be merged during BPE training, or it might decompose into multiple byte tokens if treated as rare. Similarly, composite structures like $\\nabla f$ or $x\_i$ are likely tokenized into multiple pieces (e.g., ∇, f; x, \_, i or similar, depending on the tokenizer's rules for handling subscripts and alphanumeric combinations). Even common mathematical operators like \+ or \= can be separate tokens, sometimes including preceding whitespace (e.g., " \+", " \=").50 Llama's SentencePiece BPE tokenizer exhibits known quirks, sometimes splitting words inefficiently even when a single token exists 51, suggesting similar unexpected behavior could occur with symbols. The handling of numbers themselves varies, with some tokenizers splitting them digit-by-digit (often facilitated by preprocessing like adding spaces between digits 13) while others might merge frequent digit sequences.40 This inconsistency highlights that abstract symbols might face even less standardized treatment. The complexity of Unicode representations can further influence how symbols are initially processed and potentially fragmented.40

### **B. Semantic Load vs. Token Count**

A fundamental issue arises from the mismatch between the semantic density of STEM symbols and their token representation cost. Symbols like $\\Sigma$ (summation), $\\nabla$ (vector differential operator), or even a single Greek letter representing a complex physical concept or statistical parameter, carry a significantly higher semantic load per character than typical natural language components. However, if these symbols are fragmented into multiple tokens by standard algorithms, their representation consumes a disproportionately large portion of the model's limited token budget (context window).29

Consider the comparison between a symbolic expression like "$\\partial f / \\partial x$" and its natural language equivalent "the partial derivative of f with respect to x". The symbolic form is compact for humans but might be expanded into numerous tokens (e.g., ∂, f, /, ∂, x, potentially including byte fragments or whitespace tokens). The natural language version, while longer visually, might be tokenized into fewer, more meaningful subword units. This inefficiency not only impacts processing limits and API costs 29 but also raises questions about semantic integrity. Does breaking an atomic symbol like $\\partial$ or $\\Sigma$ into multiple, less meaningful tokens hinder the LLM's ability to recognize it as a single conceptual unit?.13 Representing a single concept across multiple embedding vectors could dilute its signal and make it harder for attention mechanisms to properly weigh its importance in the context of the surrounding expression.

### **C. Tokenization Drift and Inconsistency**

The specific way symbols are tokenized can vary significantly across different LLM families (e.g., GPT series, Llama, Claude, Gemini) due to differences in their underlying tokenizers (e.g., tiktoken vs. SentencePiece), vocabulary sizes (ranging from \~32k to over 100k 38), training corpora used to build the tokenizer vocabulary 33, and pre-tokenization rules (e.g., handling of digits, whitespace, special characters 38). This inconsistency means that the same symbolic input might be represented differently internally depending on the model used, potentially contributing to variations in performance and interpretation biases.29 Tokenizers trained primarily on English text may also exhibit biases, fragmenting text or symbols from other languages or specialized domains (like mathematics or code) more heavily.29

### **D. Insights & Implications (Token Budget & Semantic Load)**

The analysis of tokenization practices reveals critical misalignments when applied to symbolic languages. Firstly, prevalent subword and byte-level tokenization methods, designed for natural language data compression and handling unknown words 28, are fundamentally ill-suited to the nature of many mathematical symbols. These symbols are often atomic units of meaning, not compositional sequences amenable to being broken down like "unhappiness" $\\rightarrow$ "un" \+ "happiness". Fragmenting $\\Sigma$ or $\\nabla$ into multiple byte tokens 40 forces the LLM to expend representational capacity simply reconstructing the symbol's identity from its parts, an inefficient process that can introduce noise. This contrasts sharply with recognizing a single, dedicated token for the symbol. This inefficiency manifests in higher token counts for symbol-heavy or non-English text in some models 29, suggesting the tokenization paradigm itself is a bottleneck.

Secondly, this token fragmentation likely contributes significantly to LLM difficulties in mathematical reasoning and symbolic manipulation. If a core expression like "$\\partial f / \\partial x$" is shattered into numerous low-level tokens (∂, f, /, ∂, x), the model's attention mechanism (discussed in Section V) faces a much harder task in associating these fragments to grasp the overall structure and meaning (the partial derivative) compared to processing fewer, more semantically loaded tokens or the equivalent natural language phrase.13 This added cognitive load for symbol reconstruction detracts from the resources available for the actual reasoning task, potentially explaining observed failures in arithmetic, algebra, and applying mathematical rules.15 The demonstrated success of approaches like Fourier Number Embedding (FoNE), which uses compact, non-fragmented representations for numbers 56, lends support to the idea that avoiding fragmentation is beneficial for numerical and potentially symbolic tasks.

Thirdly, the fixed "token budget" or context window length of LLMs 55 imposes a disproportionate penalty on STEM fields where concise symbolic notation is the norm. A complex physics equation or statistical derivation, informationally dense but visually compact for a human, can explode into a large number of tokens due to symbol fragmentation and the tokenization of operators, spaces, and numbers.13 This means that intricate scientific queries, explanations, or code containing mathematical formulas might prematurely exhaust the context window, limiting the model's ability to process or generate complete and nuanced scientific content. This has direct implications for the usability and economic feasibility (due to token-based pricing 29) of LLMs in scientific applications.

## **V. Attention & Embedding Analysis Lens: Peering Inside the Black Box**

To understand how LLMs process symbols beyond the initial tokenization step, it is essential to examine their internal representations—embeddings—and how attention mechanisms operate on these representations. This section explores theoretical considerations and empirical findings related to how symbols are encoded in vector space and attended to during processing.

### **A. Representing Symbols in Embedding Space**

How LLMs represent symbols like $\\pi$, $\\nabla$, or $\\mu$ in their high-dimensional embedding spaces is crucial for downstream interpretation and reasoning. Theoretically, these representations could be influenced by several factors:

* **Surface Form:** The raw character or byte sequence of the token(s) representing the symbol. Visually similar symbols or those sharing byte sequences might end up close in the embedding space, regardless of semantic differences.  
* **Statistical Co-occurrence:** The contexts in which the symbol appears in the training data. Symbols frequently appearing with physics terms might cluster separately from those appearing with statistical terms.  
* **Learned Semantic/Functional Properties:** Ideally, the embedding would capture the symbol's mathematical meaning or function (e.g., $\\Sigma$ representing summation, $\\mu$ representing mean).

Research into LLM embeddings provides some clues. Numbers, for instance, seem to be represented using Fourier-like features, allowing models to capture some aspects of magnitude and periodicity.13 Whether similar specialized representations exist for abstract mathematical symbols is an open question but seems less likely given their lower frequency and higher polysemy compared to numbers. It is plausible that symbols are often treated like rare words, with embeddings heavily influenced by limited contextual occurrences.30

The "$\\pi$ vs. 'pi'" question exemplifies this challenge. Does the embedding for the symbol $\\pi$ capture its mathematical essence (the constant $\\approx 3.14159$) differently than the embedding for the word "pi"?.3 An LLM might learn they are often interchangeable in text, mapping them closely in the embedding space. However, the symbolic form might be more strongly associated with mathematical formulas, while the word form is associated with descriptive text. Ideally, the symbol's embedding should encode its role as a mathematical constant, distinct from the phonetic representation.30

Furthermore, the concept of polysemantic neurons—single neurons or embedding dimensions contributing to the representation of multiple unrelated concepts—is relevant.60 A single embedding vector for a symbol like $\\mu$ might contain superimposed features related to its statistical meaning (mean) and its physics meaning (friction coefficient), potentially contributing to ambiguity during processing if the context is insufficient to isolate the relevant features.

### **B. Attention Mechanisms and Symbolic Tokens**

The Transformer architecture's attention mechanism allows the model to weigh the importance of different input tokens when generating an output or representation for a specific token.7 How attention interacts with symbolic tokens is critical for tasks requiring understanding of mathematical structure or context-dependent symbol meaning.

Several factors could influence attention weights on symbols:

* **Token Fragmentation:** If a symbol is broken into multiple tokens, attention might be diluted across these fragments, making it harder for the model to treat the symbol as a single, important unit.13  
* **Embedding Quality:** Noisy or unstable embeddings for rare symbols might lead to inconsistent attention patterns.  
* **Positional Information:** Attention mechanisms incorporate positional encoding. The role of a symbol might depend on its position within an equation or sentence.  
* **Symbol Role:** Operators like $\\Sigma$ or $\\nabla$ might need to attend broadly to their arguments or operands, while variables like $x$ or $\\theta$ might attend more to their definitions or modifying clauses.

Interpretability studies using techniques like attention visualization (heatmaps) or probing could potentially reveal how LLMs focus on symbols within mathematical expressions or scientific text.30 Research suggests that specific attention heads within LLMs can specialize in particular functions, such as syntactic dependency tracking or factual association.62 It is plausible that some heads might develop rudimentary capabilities for handling mathematical structures or relationships, but whether this is consistent or robust, especially for complex or novel symbolic configurations, remains unclear.

### **C. Layer-wise Processing**

Information processing in LLMs occurs across multiple layers. Early layers typically handle low-level feature extraction (including token identity), while middle layers integrate context and perform more abstract reasoning, and final layers synthesize information for output generation.30 Recent research suggests that for tasks requiring rich semantic or structural representations, intermediate layers might actually provide more useful embeddings than the final layer, which might be overly specialized for the next-token prediction task.30

This layer-wise perspective is relevant for symbol processing. Early layers would process the tokenized representation of the symbol. Middle layers would be crucial for disambiguating polysemous symbols by integrating surrounding context (keywords, equation structure) and potentially activating relevant domain knowledge encoded in parameters.61 Later layers would then use this disambiguated representation to perform the requested task (e.g., explain the symbol, solve the equation). Failures could occur at any stage: poor initial representation, failed contextual integration in mid-layers, or incorrect utilization in final layers.

### **D. Insights & Implications (Attention & Embedding)**

The internal handling of symbols within LLMs presents significant challenges. Firstly, the embedding space likely encodes symbols based on a complex mixture of their surface form (character/byte sequences from tokenization), their statistical co-occurrence patterns with other tokens in the vast training data, and, perhaps to a lesser degree, learned semantic or functional properties.7 Symbols, being less frequent than common words, may possess less stable or well-defined embeddings. Their vector representations could be pulled in different directions by the diverse contexts (physics, statistics, code comments, general web text) in which they appear during training. This might lead to embeddings clustering based on domain or even visual similarity rather than a unified mathematical concept.30 The observation that intermediate layers sometimes yield better representations 30 could suggest that final layers, optimized for generating fluent text, might lose some of the structured information related to symbols that was present earlier in processing.

Secondly, attention mechanisms likely face difficulties in consistently assigning appropriate "importance" or weight to symbolic tokens. This challenge is exacerbated if symbols are fragmented during tokenization or have noisy embeddings. Fragmented tokens may struggle to form strong attentional links with relevant parts of the context (like variable definitions or operands of an operator).62 The model might consequently default to attending more strongly to adjacent natural language words, potentially overlooking the structural significance of a crucial but distant operator or a subscript defining a variable's scope. While specific attention heads might develop specialized roles 62, achieving consistent and accurate attention across the vast range of symbolic structures encountered in STEM remains a hurdle.

Thirdly, applying interpretability techniques to understand symbolic reasoning in LLMs is both crucial and inherently difficult.37 Methods like probing or activation analysis often seek to map neural activity to human-understandable concepts.59 However, mathematical concepts (e.g., differentiation, summation, parameter estimation) are often defined by abstract rules, relationships, and procedures, not just static features.18 Determining if an LLM truly "represents" differentiation requires evaluating its ability to apply the rules of differentiation correctly in novel situations, rather than merely finding a "differentiation neuron" or embedding pattern. This points towards the need for dynamic, process-oriented interpretability methods that assess procedural understanding, moving beyond static analyses of representations to evaluate how symbols are manipulated in reasoning chains.62

## **VI. Reflexive Input Design Lens: Testing Symbol Interpretation via Prompting**

The way users interact with LLMs through prompts significantly shapes the models' responses. This is particularly true when dealing with the complexities of symbolic notation. This section examines how different prompting strategies affect LLM interpretation of symbols and explores methods for testing and potentially improving symbol fidelity through careful input design.

### **A. Symbolic vs. Descriptive Prompts**

A key consideration is whether to present mathematical concepts to LLMs using their native symbolic notation (e.g., "Solve for $x$ in $ax^2 \+ bx \+ c \= 0$") or using descriptive natural language (e.g., "Find the roots of the quadratic equation with coefficients a, b, and c"). Each approach has potential trade-offs:

* **Symbolic Prompts:** Offer precision and conciseness, mirroring expert communication. However, they directly expose the LLM to potential challenges with symbol tokenization (Section IV), polysemy (Section III), and lack of deep mathematical grounding (Section V).67 The model must parse the symbolic structure and interpret the symbols correctly based on often implicit context.  
* **Descriptive Prompts:** Leverage the LLM's strengths in natural language processing.8 Explaining concepts in words (e.g., "the standard deviation $\\sigma$") might provide clearer context and reduce ambiguity.68 However, this approach risks "symbol collapse," where the specific nuances and operational meaning embedded in the symbol are lost or diluted in the translation to natural language. It can also be verbose and less efficient.

Research comparing prompting strategies suggests that the choice matters.9 Spelling out symbol names phonetically (e.g., "lambda" instead of $\\lambda$) might sometimes improve robustness if the symbol itself is poorly tokenized or ambiguous, but it disconnects the query from the standard mathematical representation.

Advanced prompting techniques like Chain-of-Thought (CoT), Program-of-Thoughts (PoT), Tree-of-Thoughts (ToT), or methods involving planning tokens aim to improve complex reasoning, including mathematical problem-solving.9 These strategies typically involve breaking down the problem into intermediate steps, often expressed in natural language or code-like structures. While they can enhance performance on benchmarks like GSM8K 17, it's unclear if they fundamentally improve the LLM's core *interpretation* of the symbols themselves, or if they merely provide a scaffold that allows the model to bypass direct symbolic manipulation by relying on its stronger linguistic or pattern-matching abilities applied to the intermediate steps. The reasoning chain might appear logical, but errors in handling the underlying symbols could still occur.15

### **B. Controlled Experiments (Conceptual)**

To systematically probe LLM interpretation of symbols via prompting, controlled experiments are necessary. Based on the LENS framework suggestions, conceptual experiments could include:

1. **Prompt Equivalence Tests:** Create pairs of prompts conveying the same mathematical information, one using standard symbolic notation and the other using a purely descriptive natural language formulation. Compare the LLM's outputs across various tasks (e.g., definition, calculation, application) and domains (Physics, Stats, ML). Analyze differences in accuracy, coherence, latency, and evidence of correct semantic interpretation versus superficial pattern matching. (e.g., compare response to "Calculate $\\nabla \\cdot \\mathbf{F}$ where..." vs. "Calculate the divergence of the vector field F where...").  
2. **Context Priming Tests:** Present the same ambiguous symbolic query (e.g., involving $\\mu$) under different contextual conditions: (a) no explicit context, (b) context explicitly stating the domain ("In statistics,..."), (c) context providing domain-related keywords ("...in this sample data..."), (d) context embedded within a larger physics problem. Measure the LLM's ability to correctly disambiguate the symbol in each case.  
3. **Minimal Pair Symbol Tests:** Construct prompts that are identical except for a single target symbol which has different meanings in different domains (e.g., use the same equation structure but swap $\\mu$ for $\\rho$). Assess whether the LLM's interpretation appropriately changes based *only* on the symbol substitution, or if it relies excessively on the surrounding structure.

### **C. Improving Clarity: Prompt Engineering for Symbols**

Given the observed sensitivities, prompt engineering strategies can be employed to mitigate symbol ambiguity for LLMs. Explicitly defining symbols within the prompt ("Let $\\alpha$ represent the learning rate in this optimization problem...") provides direct disambiguation. Similarly, stating the domain ("Considering this from a statistical perspective,...") can help activate the correct contextual priors. A hybrid approach, combining symbolic notation with brief natural language clarifications, might offer a balance between precision and robustness.

The concept of a "symbol-aware prompting assistant" emerges as a potential future tool. Such an assistant would require capabilities like:

* Detecting the likely domain of a query based on keywords and symbolic patterns.  
* Identifying potentially ambiguous symbols within the prompt.  
* Accessing a knowledge base of symbol meanings across domains (like Table 1).  
* Flagging ambiguities to the user or suggesting prompt reformulations for clarity.  
* Potentially auto-annotating symbols with their intended meaning based on context before feeding the prompt to the main LLM.

### **D. Insights & Implications (Reflexive Input Design)**

The interaction between prompting strategies and LLM symbol interpretation reveals crucial dynamics. Firstly, LLM performance is demonstrably sensitive to how symbolic information is presented in the prompt. Using descriptive natural language may enhance robustness by playing to the model's linguistic strengths, but it comes at the cost of potentially losing the precision, conciseness, and operational semantics inherent in the symbolic notation itself—a phenomenon termed symbol collapse.9 Conversely, using direct symbolic notation preserves fidelity to the domain language but exposes the LLM's weaknesses in parsing non-linguistic structures, handling polysemy, and potential tokenization failures. This creates a fundamental trade-off for users: prioritize leveraging the LLM's core competency (natural language) or prioritize preserving the integrity of the domain's native representation (symbolic language).

Secondly, while advanced prompting techniques like CoT or PoT can improve performance on complex reasoning tasks involving symbols, they do not necessarily resolve the underlying issues of symbol interpretation or grounding.9 These methods encourage the model to generate step-by-step textual or programmatic derivations. However, the model might still misinterpret a symbol within an intermediate step or commit arithmetic/logical errors that are masked by the fluency of the generated language.15 Techniques like adding specialized planning tokens 72 aim to guide the structural flow of reasoning but ultimately rely on the model correctly associating these guiding tokens with the intended symbolic operations. The generated reasoning can appear superficially correct while the core symbolic manipulation remains flawed 15, highlighting a gap between articulating a reasoning process and executing it accurately.

Thirdly, crafting effective prompts for tasks involving symbolic languages requires a meta-level understanding of the LLM's likely failure modes. Engineers and researchers must anticipate potential ambiguities, tokenization artifacts, or contextual dependencies and proactively structure the prompt to guide the model towards the correct interpretation.34 This might involve explicitly defining symbols ("...where $\\sigma$ denotes the standard deviation..."), clearly stating the domain context, or using a carefully balanced mixture of symbolic and descriptive elements. This elevates prompt engineering in STEM domains beyond simple instruction-following; it becomes a form of cognitive scaffolding, actively compensating for the LLM's inherent limitations in symbolic processing. Effective prompting thus requires not only domain expertise but also a working knowledge of LLM behavior and interpretability.

## **VII. Tool & Interface Reflexivity Lens: The Impact of Rendering Environments**

The way symbolic notation is encoded, transmitted, and displayed through various tools and interfaces—from raw text files to sophisticated rendering environments like LaTeX compilers, Markdown processors, and Jupyter notebooks—can significantly influence how LLMs process and interpret these symbols. This section examines the reflexivity between the tools used to represent symbols and the LLM's understanding, emphasizing the distinction between surface rendering and semantic comprehension.

### **A. LaTeX, Markdown, Jupyter, and LLMs**

In practice, LLMs encounter symbolic notation in various formats:

* **LaTeX:** Scientific documents, particularly from sources like arXiv, often contain mathematical notation encoded using LaTeX commands (e.g., \\frac{a}{b}, \\sum\_{i=1}^n, \\mu, \\nabla).74 LLMs trained on such data learn to process and even generate LaTeX syntax. A key question is whether the LLM processes the raw command string (\\mu) or operates on an internal representation closer to the rendered symbol ('μ'). The tokenization of LaTeX commands versus Unicode symbols likely differs, potentially affecting interpretation.76  
* **Markdown:** Many chatbot interfaces and documentation platforms use Markdown, which often supports mathematical notation via embedded LaTeX (using delimiters like $...$ or $$...$$) or direct Unicode characters.77 However, Markdown rendering of mathematics is notoriously inconsistent across platforms and can suffer from bugs, leading to characters being lost, incorrectly formatted, or misinterpreted by the rendering engine (e.g., conflicts with Markdown syntax like underscores or brackets).77 This introduces noise either in the input seen by the LLM or in the output presented to the user.  
* **Unicode:** Direct use of Unicode characters (e.g., Σ, ∂, θ) in plain text or code comments is also common. The LLM's tokenizer must handle these characters directly, facing potential fragmentation issues as discussed in Section IV.  
* **Jupyter Notebooks:** These environments present a mixed-modality context, combining code cells (which might contain symbols in strings or variable names), Markdown cells (with potential LaTeX/Unicode rendering), and rendered outputs (plots, tables). How an LLM integrates information from these different sources when interpreting symbols within the notebook context is complex and under-explored.

### **B. Rendering vs. Comprehension**

A critical constraint of this analysis is to avoid equating the ability to render or manipulate symbolic syntax with genuine comprehension \[Prompt\]. An LLM might be adept at generating syntactically correct LaTeX for a complex equation because it has learned the patterns from its training data (e.g., arXiv papers 75). However, this ability does not imply an understanding of the underlying mathematical concepts, the relationships between the symbols, or the procedures the equation represents.15 The model might output \\int f(x) dx without understanding integration. This distinction is crucial: focusing on token-level meaning and model behavior, not just surface form, is necessary to assess true symbolic understanding. The interface itself might also bias interpretation; if symbols are predominantly encountered within LaTeX markup during training, the LLM might implicitly associate them more strongly with formal academic contexts.

### **C. Cross-Interface Consistency**

The interpretation of a symbolic query could potentially vary depending on the interface through which it is presented. A query containing \\mu sent via a raw text API might be tokenized differently than the same query where \\mu is entered as a Unicode character in a Markdown-rendering chatbot. These differences in initial representation could cascade through the model's processing layers, leading to inconsistent interpretations or outputs for the logically identical query presented through different front-ends.

### **D. Insights & Implications (Tool & Interface Reflexivity)**

The interplay between symbolic representation tools and LLM interpretation introduces another layer of complexity. Firstly, the specific encoding format used for input—whether raw Unicode characters, LaTeX commands, or symbols embedded within Markdown—directly impacts the initial tokenization and processing stages within the LLM.44 A sequence like \\mu is fundamentally different at the token level from the single Unicode character 'μ'. Models trained on datasets containing both forms (e.g., web text alongside arXiv papers 74) might develop distinct, potentially inconsistent internal associations or processing pathways for each representation. Furthermore, known issues with Markdown rendering engines 77 can corrupt the symbolic information either before it reaches the LLM (if parsing input) or after the LLM generates it (affecting user perception), creating an "interface effect" that adds variability independent of the symbol's inherent semantics.

Secondly, the prevalence of LaTeX in scientific training data likely leads LLMs to treat LaTeX generation primarily as a sophisticated string manipulation task, rather than an act of mathematical expression grounded in semantic understanding.76 LLMs excel at learning sequential patterns.8 Generating \\frac{a}{b} after observing countless similar structures in training data is a high-probability sequence completion task that does not necessitate understanding the concept of division or fractions.79 This explains the observed phenomenon where models can produce syntactically flawless mathematical typesetting for concepts they cannot actually reason about or compute correctly.15 The competence is often syntactic, not semantic.

Thirdly, the toolchain involving LLM output and external rendering libraries (like MathJax or KaTeX used in web interfaces 79) creates a potential disconnect that can obscure the true nature of LLM performance. An LLM might generate perfectly valid LaTeX, but a bug or misconfiguration in the user's rendering tool could display it incorrectly, leading to an unfair assessment of the LLM's output.78 Conversely, an LLM might produce subtly incorrect or non-standard LaTeX that happens to render plausibly in a specific environment, masking an underlying semantic error. This underscores the importance, as stipulated in the prompt, of evaluating the LLM's raw symbolic output (the token sequence or generated markup) rather than relying solely on the final rendered appearance, ensuring analysis focuses on the model's internal processing and generation capabilities.

## **VIII. Synthesis: Capabilities, Limitations, and Future Directions**

This multi-lens investigation reveals a complex picture of how current Large Language Models interact with the symbolic languages essential to Physics, Statistics, and Machine Learning. While demonstrating some nascent capabilities, LLMs exhibit significant and systematic limitations that hinder their reliable use in contexts demanding high symbolic fidelity.

### **A. Assessing Current LLM Capabilities with Symbolic Languages**

**Strengths:**

* **Recognition and Association:** LLMs can often recognize common mathematical symbols and Greek letters, associating them with relevant concepts retrieved from their training data, especially when provided with clear context or explicit prompts.8  
* **Syntactic Manipulation:** Models trained on scientific literature or code demonstrate proficiency in manipulating the syntax of symbolic representations, particularly LaTeX, enabling them to generate well-formatted mathematical expressions.76  
* **Pattern Matching:** They can identify patterns in simple symbolic sequences, contributing to success in some basic arithmetic or algebraic tasks, likely through memorization or learned heuristics.15

**Weaknesses:**

* **Polysemy and Ambiguity:** LLMs frequently struggle to disambiguate symbols with multiple meanings across domains, often defaulting to the most common meaning or failing to utilize contextual cues effectively, leading to domain leakage and semantic errors.15  
* **Tokenization Bottleneck:** Standard tokenization methods fragment atomic symbols, creating inefficient representations that consume excessive token budgets and obscure the semantic unity of symbols and expressions.13  
* **Context Sensitivity Deficits:** Interpretation is often overly reliant on local textual cues, with models struggling to integrate information across longer distances or leverage implicit domain knowledge necessary for correct symbol interpretation.  
* **Shallow Grounding:** The ability to manipulate syntax (like generating LaTeX) often exists without a corresponding deep understanding of the underlying mathematical concepts, operations, or constraints.18 Models can "talk about" math without truly "doing" math.  
* **Reasoning Failures:** LLMs exhibit persistent errors in fundamental mathematical reasoning, including arithmetic mistakes, logical inconsistencies, failure to adhere to constraints, making unwarranted assumptions, and inability to translate abstract concepts (like physical intuition) into correct mathematical steps.15 Correct final answers can sometimes be produced via flawed reasoning paths.15

### **B. Key Challenges Highlighted by the Multi-Lens Framework**

The multi-lens framework illuminates interconnected challenges. The inherent **polysemy** of symbols (Lens 1 & 2\) is significantly amplified by **tokenization** strategies (Lens 3\) that fragment symbols, making it harder for **attention mechanisms** (Lens 4\) to associate them correctly with their context. This shallow processing leads to failures in context sensitivity and **domain leakage** (Lens 2). Attempts to mitigate these issues through **prompting** (Lens 5\) reveal a trade-off between leveraging natural language strengths and preserving symbolic precision, often failing to fix the core **embedding** and grounding issues (Lens 4). Finally, the **interface and rendering tools** (Lens 6\) introduce another layer of variability and potential misinterpretation, complicating the assessment of true model capabilities (Lens 1-5).

Fundamentally, these challenges highlight a gap between the statistical pattern-matching capabilities inherent in current LLM architectures, which excel at predicting likely sequences based on vast textual data, and the requirements of symbolic reasoning, which involves rule-based manipulation, precise interpretation, logical consistency, and procedural understanding.18 LLMs often treat symbols as just another type of token sequence, failing to grasp their unique ontological status and operational significance within STEM domains.

### **C. Avenues for Improvement and Future Research**

Addressing the limitations of LLMs in handling symbolic languages requires concerted effort across multiple research fronts:

1. **Symbol-Aware Tokenization:** Design tokenization schemes that treat fundamental mathematical symbols and operators as atomic units, potentially incorporating structural information from mathematical expressions rather than relying solely on linear sequences. Approaches like FoNE for numbers 56 could potentially be adapted or inspire new methods for abstract symbols.13  
2. **Context-Enhanced Embeddings:** Develop embedding techniques that explicitly encode domain information, mathematical function (e.g., operator vs. variable vs. constant), and relationships between symbols, moving beyond representations based primarily on surface form or generic co-occurrence.30 Probing intermediate layers might offer insights.30  
3. **Neuro-Symbolic Integration:** Explore hybrid architectures that combine the pattern-recognition strengths of LLMs with the rigorous rule-based processing of symbolic reasoning engines, dedicated solvers, or knowledge graphs.18 LLMs could assist in problem formulation or heuristic guidance, while symbolic components ensure logical consistency and computational accuracy.18  
4. **Improved Pre-training and Fine-tuning Data:** Curate large-scale, high-quality datasets specifically designed for training LLMs on scientific and mathematical tasks. This includes text with accurately represented and well-contextualized symbolic notation across diverse STEM fields, potentially incorporating formal mathematics datasets or structured problem-solution pairs.17 Techniques for extracting and cleaning data from PDF sources need improvement.75  
5. **Advanced Interpretability for Symbolic Reasoning:** Develop and apply interpretability methods tailored to understanding how LLMs process and manipulate symbols and mathematical structures. This requires moving beyond static embedding analysis to probe procedural understanding, attention flow within equations, and the internal representation of mathematical rules.37  
6. **Rigorous and Fine-Grained Evaluation:** Create new benchmarks specifically designed to test LLM capabilities with symbolic languages, focusing on aspects like symbol disambiguation across domains, understanding of operator semantics, handling of notation conventions (subscripts, etc.), consistency in applying mathematical rules, and grounding in physical or statistical principles. Evaluation must go beyond final answer correctness to analyze the reasoning process itself.15

### **D. Concluding Remarks**

The symbolic languages of STEM represent a pinnacle of human abstract reasoning and precise communication. For AI systems, particularly LLMs, to become truly reliable partners in scientific discovery and engineering innovation, achieving high-fidelity understanding and manipulation of these languages is not optional, but essential. This investigation reveals that while current LLMs have made strides in processing surface forms and associating symbols with textual knowledge, they grapple with fundamental challenges related to polysemy, contextual grounding, inefficient representation, and robust reasoning. The path forward requires moving beyond treating symbols as mere text tokens towards developing models with deeper, structurally aware, and contextually sensitive symbolic competence. Addressing the issues highlighted across the Typological Semiotics, Domain Leakage, Tokenization, Embedding/Attention, Prompting, and Interface lenses is critical for unlocking the full potential of LLMs in the demanding landscape of science and technology.

## **IX. References**

1 Recognizing commonly used statistical symbols. (World Supporter)  
10 Greek Alphabet Letters Used in Science and Engineering. (AES)  
2 Greek Letters Explained: Symbols and Uses in Math & Science. (Vaia)  
5 Greek Letter Order: Alphabet Sequence and Names. (Vaia)  
21 Greek Letters in Microwaves. (Microwaves101)  
3 Most Used Greek Symbols in Mathematics. (Romainstitute)  
4 Greek letters used in mathematics, science, and engineering. (Wikipedia)  
22 Greek Alphabet Symbols. (GeeksforGeeks)  
11 Del. (Wikipedia)  
6 Nabla symbol. (Wikipedia)  
23 Vector Calculus. (GeeksforGeeks)  
25 Is ∇n a correct terminology for a partial derivative? (StackExchange)  
12 Physics\[Vectors\]\[Nabla\]. (Maplesoft)  
24 The del symbol ∇ acts as a partial derivative operator... (Chegg)  
26 Introduction to partial derivatives. (Khan Academy)  
27 A Gentle Introduction to the Laplacian. (Machine Learning Mastery)  
28 Tokenization and Statistical Estimation: A Principled Approach. (arXiv:2407.11606)  
38 LLM of Babel: Evaluation of LLMs on code for non-English use-cases. (TU Delft Repository)  
33 Data Mixture Inference Attacks Against Open-Vocabulary Language Models. (NeurIPS 2024\)  
90 On the Role of Tokenization in Transformer-Based Language Modeling. (arXiv:2404.08335)  
29 One Token Loads More: Toward Fairer Subword-based Language Model APIs. (EMNLP 2023\)  
55 Llama 3 Technical Report. (Grattafiori et al., 2024\)  
58 GlotScript: An Open Resource and Tool for Low Resource Writing System Identification. (LREC 2024\)  
54\[D\] Moving away from unicode for more equal token representation? (Reddit r/MachineLearning)  
56 Fourier Number Embedding. (arXiv:2502.09741v1)  
91 On the Role of Tokenization in Transformer-Based Language Modeling. (arXiv:2404.08335v2)  
92 How Well Do Large Language Models Handle Implicit Constraints? A Study on Binary Relations. (arXiv:2503.10408v1)  
13 Can Language Models Handle Tabular Data? A Case Study on Time Series Forecasting. (arXiv:2310.02989v2)  
72 Guiding Large Language Models with Planning Tokens. (arXiv:2310.05707v2)  
93 TokenRec: Bridging the Gap between LLMs and Recommender Systems with Effective Tokenization and Efficient Retrieval. (arXiv:2406.10450v2)  
94 Probabilistic Tokenizations Improve the Self-Consistency of Large Language Models in Reasoning Tasks. (arXiv:2407.03678v1)  
73 Guiding Large Language Models with Planning Tokens. (arXiv:2310.05707v4)  
39\[D\] Why are byte pair encoding tokenizers preferred over character level tokenizers? (Reddit r/MachineLearning)  
40 How GPT tokenization works. (hundredblocks.github.io)  
41 Tokenizer Bias: The Root Cause of Hallucination in Large Language Models. (arXiv:2406.11214)  
47 What is Tokenization in NLP? Everything You Need to Know. (Analytics Vidhya)  
42 Byte Pair Encoding is Suboptimal for Language Model Pretraining. (Findings of ACL 2023\)  
48\[D\] Sentencepiece, Wordpiece, BPE: Which tokenizer is the best one? (Reddit r/MachineLearning)  
45 A Comparative Study of Tokenization Algorithms for BERT Pretraining. (MDPI Applied Sciences)  
43 Tokenization: Different Types of Tokenizers and Why It Is Used. (Corpnce)  
50 How to count tokens with tiktoken. (OpenAI Cookbook GitHub)  
95 Tiktoken Tutorial: OpenAI's Python Library for Tokenizing Text. (CheatSheet.md)  
53 01 Let's build the GPT Tokenizer v2. (Kaggle)  
44 Estimating The Cost of GPT Using The tiktoken Library in Python. (DataCamp)  
96 Tiktoken Tutorial: OpenAI's Python Library for Tokenizing Text. 9549 google/sentencepiece. (GitHub)  
46 Tokenization in Large Language Models (LLMs). (ingoampt.com)  
57 What's in a Byte? Tokenizer Vocabulary Induced Task Bias in Code LLMs. (arXiv:2402.01035v1)  
51 LLaMA tokenisation is weird. (Hacker News)  
97 Removing strange special characters from outputs (llama 3.1 model). (Stack Overflow)  
30 Beyond the Last Layer: Investigating the Properties of Intermediate Layers in Foundation Models. (arXiv:2502.02013)  
59 Interpreting Embedding Spaces by Conceptualization. (EMNLP 2023\)  
31 Compute-Optimal Training of Text Embedding Models. (arXiv:2406.04165v1)  
35 Symbols and grounding in large language models. (PMC NCBI)  
98 EMNLP 2024 Main Conference Proceedings. (ACL Anthology)  
36 Introduction to Mathematical Language Processing. (TACL)  
62 How Do Large Language Models Understand Relevance? A Mechanistic Interpretability Perspective. (arXiv:2504.07898v1)  
63 Are Texts Really Helpful for Time Series? On the Interpretability of Time-Series LLMs. (arXiv:2504.08808)  
7 Large language model. (Wikipedia)  
37 Explainability for Large Language Models: A Survey. (arXiv:2309.01029)  
99 Attention is not Explanation... or is it? (arXiv:2402.03485v1)  
14 Symbolic Capabilities of Large Language Models: A Chomsky Hierarchy Perspective. (arXiv:2405.13209v1)  
15 Evaluating the Reasoning Capabilities of Large Language Models: A Case Study on 50 High-School Math Problems. (arXiv:2502.11574v1)  
16 Evaluating the Reasoning Capabilities of Large Language Models: A Case Study on 50 High-School Math Problems. (arXiv:2502.11574)  
100 Uncertainty Quantification in Large Language Models for Medical Applications: Technical Innovations and Philosophical Implications. (arXiv:2504.05278v1)  
86 MathFusion: Fusing Instruction Tuning Data Towards General Mathematical Reasoning. (arXiv:2503.16212v1)  
17 AI for Mathematical Reasoning: Progress and Challenges. (arXiv:2412.16075v1)  
32 Can AI Grade Undergraduate Physics Problems? A Comparative Study of Human vs. AI Grading. (arXiv:2411.13685v1)  
101 The Large Language Model GreekLegalRoBERTa. (arXiv:2410.12852)  
8 Essential Concepts and Terminology of Large Language Models. (Kern AI Blog)  
102 Mapping the Mind of a Large Language Model. (Anthropic Research)  
103 Meltemi: The first Greek Large Language Model. (Greek News Agenda)  
104 Large Language Models for Low-Resource Languages: Challenges and Opportunities. (arXiv:2412.04497v2)  
66 Steering LLMs Towards Specific Values by Intervening on Their Internal Representations. (Hi Oscar AI Blog)  
18 A Survey on Mathematical Reasoning and Optimization with Large Language Models. (ResearchGate/arXiv)  
105 Awesome-LLM-Reasoning-with-NeSy. (GitHub)  
87 Evaluating Language Models' Understanding of Math Standards. (arXiv:2408.04226v2)  
88 Evaluating Language Models' Understanding of Math Standards. (arXiv:2408.04226)  
89 Evaluating large language model interactions in informal mathematical theorem proving. (PMC NCBI)  
19 A Survey of Mathematical Reasoning in the Era of Multi-Modal Large Language Model: Benchmark, Method & Challenges. (OpenReview)  
106 Tiktokenizer Web App. (tiktokenizer.dev)  
95 Tiktoken Tutorial: OpenAI's Python Library for Tokenizing Text. (CheatSheet.md \- duplicate)  
107 How to count tokens with tiktoken (Jupyter Notebook). (OpenAI Cookbook GitHub)  
108 openai/tiktoken. (GitHub)  
96 Tiktoken Tutorial: OpenAI's Python Library for Tokenizing Text. (DataCamp \- duplicate)  
52 Tiktokenizer Web App Interface. (tiktokenizer.vercel.app)  
68 A Survey on Mathematical Reasoning and Optimization with Large Language Models. 189 Large Language Models: A Comprehensive Survey of Fundamentals, Utilization Strategies, and Limitations. (arXiv:2501.04040v2)  
69 PC-SubQ: A Prompting Strategy for Structured Causal Discovery from Natural Language Data. (arXiv:2412.13952v1)  
34 A Systematic Review of Symbolic Reasoning with Large Language Models. (arXiv:2410.21490v1)  
67 Comparing Large Language Models and Neuro-Symbolic Approaches on Abstract Reasoning Tasks. (arXiv:2412.05586v1)  
70 MathCAMPS: Fine-grained Synthesis of Mathematical Problems From Human Curricula. (arXiv:2407.00900)  
71 More and Core: Evaluating the Reasoning Capabilities of LLMs in Math and Coding through Ontology-based Perturbations. (arXiv:2401.09395v3)  
74 Sci-Reproducer: A Challenging Benchmark for Evaluating Reasoning LLMs in Scientific Code Generation from LaTeX. (arXiv:2504.00255v1)  
109 Towards Long-Output Large Language Models. (arXiv:2503.04723v2)  
75 SciLit: A Comprehensive Pipeline for Scientific Literature Adaptation of Large Language Models. (arXiv:2408.15545v2)  
84 Challenges in Guardrailing Large Language Models for Science. (arXiv:2411.08181)  
110 Why Does RAG Benefit from Long-Context LLMs? A Case Study on Question Answering. (arXiv:2410.05983)  
111 Large Language Models are General Pattern Matchers. (arXiv:2411.11061)  
76\[D\] How do these LLMs train on scientific data with LaTeX? (Reddit r/MachineLearning)  
77 MDEval: Evaluating Markdown Awareness of Large Language Models. (arXiv:2501.15000v1)  
81 Markdown rendering issue in AI Assistant (characters lost or misrendered). (JetBrains YouTrack)  
78 Mathematical notation rendering issue using QWEN 2.5 and Deepseek R1. (AnythingLLM GitHub Issue)  
79 New feature: properly shown mathematical equations. (OpenAI Community Forum)  
82 Issues with Katex/ngx-markdown Rendering in Angular 16\. (Stack Overflow)  
80 Mathematical equation does not render correctly. (GitHub Community Discussion)  
83 Math Rendering Is Wrong. (danilafe.com Blog)  
60 Interpreting and Controlling Learned Features in Language Models. (MIT Thesis)  
85 Awesome-LLMs-Datasets. (GitHub)  
112 Proceedings of the 19th Conference on Natural Language Processing (KONVENS 2024). (KONVENS 2024\)  
113 Proceedings of the Workshop on Deep Learning and Linked Data (DLnLD 2024). (ACL Anthology)  
114 Between Babel and Bytes: Language Modeling in the Face of Linguistic and Computational Constraints. (Mielke Thesis)  
115 Metaphor Annotation and Identification Using Natural Language Processing Methods. (MDPI Information)  
116 ENHANCING JAPANESE LEXICAL NETWORKS USING LARGE LANGUAGE MODELS. (EURALEX 2024\)  
62 How Do Large Language Models Understand Relevance? A Mechanistic Interpretability Perspective. 6220 Do LLMs Learn Addition Rules? Probing for Symbolic Generalization via Arithmetic Tasks. (arXiv:2504.05262v1)  
64 Explainability in Large Language Models: A Comprehensive Survey. (arXiv:2502.17601v1)  
61 Unveiling the Inner Workings of Large Language Models: A Survey on Explainability of LLMs. (arXiv:2402.10688)  
65 Attention Head Mechanisms in Large Language Models: A Survey. (arXiv:2409.03752v1)  
37 Explainability for Large Language Models: A Survey. 3752 Tiktokenizer Web App. (tiktokenizer.vercel.app)

#### **Works cited**

1. Recognizing commonly used statistical symbols: greek, latin and mathematical, accessed on April 23, 2025, [https://www.worldsupporter.org/en/recognizing-commonly-used-statistical-symbols-greek-latin-and-mathematical](https://www.worldsupporter.org/en/recognizing-commonly-used-statistical-symbols-greek-latin-and-mathematical)  
2. Greek Letters: Alphabet & Symbols Explained \- Vaia, accessed on April 23, 2025, [https://www.vaia.com/en-us/explanations/greek/greek-alphabet/greek-letters/](https://www.vaia.com/en-us/explanations/greek/greek-alphabet/greek-letters/)  
3. Most Used Greek Symbols in Mathematics \- Roma Institute, accessed on April 23, 2025, [https://www.romainstitute.com/blogs/greek-symbols-in-mathematics/](https://www.romainstitute.com/blogs/greek-symbols-in-mathematics/)  
4. Greek letters used in mathematics, science, and engineering \- Wikipedia, accessed on April 23, 2025, [https://en.wikipedia.org/wiki/Greek\_letters\_used\_in\_mathematics,\_science,\_and\_engineering](https://en.wikipedia.org/wiki/Greek_letters_used_in_mathematics,_science,_and_engineering)  
5. Greek Letter Order: Alphabet Sequence & Names | Vaia, accessed on April 23, 2025, [https://www.vaia.com/en-us/explanations/greek/greek-alphabet/greek-letter-order/](https://www.vaia.com/en-us/explanations/greek/greek-alphabet/greek-letter-order/)  
6. Nabla symbol \- Wikipedia, accessed on April 23, 2025, [https://en.wikipedia.org/wiki/Nabla\_symbol](https://en.wikipedia.org/wiki/Nabla_symbol)  
7. Large language model \- Wikipedia, accessed on April 23, 2025, [https://en.wikipedia.org/wiki/Large\_language\_model](https://en.wikipedia.org/wiki/Large_language_model)  
8. Essential Concepts & Terminology of Large Language Models (LLMs) \- Kern AI, accessed on April 23, 2025, [https://www.kern.ai/resources/blog/essential-concepts-and-terminology-of-large-language-models](https://www.kern.ai/resources/blog/essential-concepts-and-terminology-of-large-language-models)  
9. A Survey on Large Language Models with some Insights on their Capabilities and Limitations \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2501.04040v2](https://arxiv.org/html/2501.04040v2)  
10. Pro Audio Reference (Greek) \- Audio Engineering Society, accessed on April 23, 2025, [https://www.aes.org/par/greek/](https://www.aes.org/par/greek/)  
11. Del \- Wikipedia, accessed on April 23, 2025, [https://en.wikipedia.org/wiki/Del](https://en.wikipedia.org/wiki/Del)  
12. Nabla \- Maple Help \- Maplesoft, accessed on April 23, 2025, [https://www.maplesoft.com/support/help/Maple/view.aspx?path=Physics%2FVectors%2FNabla](https://www.maplesoft.com/support/help/Maple/view.aspx?path=Physics/Vectors/Nabla)  
13. xVal: A Continuous Numerical Tokenization for Scientific Language Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2310.02989v2](https://arxiv.org/html/2310.02989v2)  
14. Investigating Symbolic Capabilities of Large Language Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2405.13209v1](https://arxiv.org/html/2405.13209v1)  
15. Large Language Models and Mathematical Reasoning Failures \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2502.11574v1](https://arxiv.org/html/2502.11574v1)  
16. \[2502.11574\] Large Language Models and Mathematical Reasoning Failures \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2502.11574](https://arxiv.org/abs/2502.11574)  
17. Formal Mathematical Reasoning: A New Frontier in AI \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2412.16075v1](https://arxiv.org/html/2412.16075v1)  
18. (PDF) A Survey on Mathematical Reasoning and Optimization with Large Language Models, accessed on April 23, 2025, [https://www.researchgate.net/publication/390142528\_A\_Survey\_on\_Mathematical\_Reasoning\_and\_Optimization\_with\_Large\_Language\_Models](https://www.researchgate.net/publication/390142528_A_Survey_on_Mathematical_Reasoning_and_Optimization_with_Large_Language_Models)  
19. A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges \- OpenReview, accessed on April 23, 2025, [https://openreview.net/pdf?id=f4hykr2yjo](https://openreview.net/pdf?id=f4hykr2yjo)  
20. Do PhD-level LLMs Truly Grasp Elementary Addition? Probing Rule Learning vs. Memorization in Large Language Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2504.05262v1](https://arxiv.org/html/2504.05262v1)  
21. Greek letters in microwave engineering \- Microwaves101, accessed on April 23, 2025, [https://www.microwaves101.com/encyclopedias/greek-letters-in-microwaves](https://www.microwaves101.com/encyclopedias/greek-letters-in-microwaves)  
22. Greek Alphabet: Symbols, Letters, Names, and Examples \- GeeksforGeeks, accessed on April 23, 2025, [https://www.geeksforgeeks.org/greek-alphabet-symbols/](https://www.geeksforgeeks.org/greek-alphabet-symbols/)  
23. Vector Calculus in Maths | GeeksforGeeks, accessed on April 23, 2025, [https://www.geeksforgeeks.org/vector-calculus/](https://www.geeksforgeeks.org/vector-calculus/)  
24. Solved The del symbol ∇ acts as a partial derivative | Chegg.com, accessed on April 23, 2025, [https://www.chegg.com/homework-help/questions-and-answers/del-symbol-nabla-acts-partial-derivative-operator-applied-scalar-function-f--given-f-x-y-q-q119337007](https://www.chegg.com/homework-help/questions-and-answers/del-symbol-nabla-acts-partial-derivative-operator-applied-scalar-function-f--given-f-x-y-q-q119337007)  
25. Is $\\nabla^{n}$ a correct terminology for a partial derivative? \- Math Stack Exchange, accessed on April 23, 2025, [https://math.stackexchange.com/questions/2140189/is-nablan-a-correct-terminology-for-a-partial-derivative](https://math.stackexchange.com/questions/2140189/is-nablan-a-correct-terminology-for-a-partial-derivative)  
26. Introduction to partial derivatives (article) \- Khan Academy, accessed on April 23, 2025, [https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivative-and-gradient-articles/a/introduction-to-partial-derivatives)  
27. A Gentle Introduction to the Laplacian \- MachineLearningMastery.com, accessed on April 23, 2025, [https://machinelearningmastery.com/a-gentle-introduction-to-the-laplacian/](https://machinelearningmastery.com/a-gentle-introduction-to-the-laplacian/)  
28. The Foundations of Tokenization: Statistical and Computational Concerns \- arXiv, accessed on April 23, 2025, [https://arxiv.org/pdf/2407.11606](https://arxiv.org/pdf/2407.11606)  
29. Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models \- ACL Anthology, accessed on April 23, 2025, [https://aclanthology.org/2023.emnlp-main.614.pdf](https://aclanthology.org/2023.emnlp-main.614.pdf)  
30. Layer by Layer: Uncovering Hidden Representations in Language Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2502.02013](https://arxiv.org/html/2502.02013)  
31. Repurposing Language Models into Embedding Models: Finding the Compute-Optimal Recipe \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2406.04165v1](https://arxiv.org/html/2406.04165v1)  
32. Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics, accessed on April 23, 2025, [https://arxiv.org/html/2411.13685v1](https://arxiv.org/html/2411.13685v1)  
33. Data Mixture Inference: What do BPE Tokenizers Reveal about their Training Data? \- NIPS papers, accessed on April 23, 2025, [https://proceedings.neurips.cc/paper\_files/paper/2024/file/10e6dfea9a673bef4a7b1cb9234891bc-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2024/file/10e6dfea9a673bef4a7b1cb9234891bc-Paper-Conference.pdf)  
34. Can Large Language Models Act as Symbolic Reasoners? \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2410.21490v1](https://arxiv.org/html/2410.21490v1)  
35. Symbols and grounding in large language models \- PMC \- PubMed Central, accessed on April 23, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10239679/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10239679/)  
36. Introduction to Mathematical Language Processing: Informal Proofs, Word Problems, and Supporting Tasks | Transactions of the Association for Computational Linguistics \- MIT Press Direct, accessed on April 23, 2025, [https://direct.mit.edu/tacl/article/doi/10.1162/tacl\_a\_00594/117587/Introduction-to-Mathematical-Language-Processing](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00594/117587/Introduction-to-Mathematical-Language-Processing)  
37. Explainability for Large Language Models: A Survey \- arXiv, accessed on April 23, 2025, [http://arxiv.org/pdf/2309.01029](http://arxiv.org/pdf/2309.01029)  
38. LLM of Babel: Evaluation of LLMs on code for non-English use-cases \- TU Delft Repository, accessed on April 23, 2025, [https://repository.tudelft.nl/file/File\_2d165f32-fd28-4924-8e51-95ee5bb74759](https://repository.tudelft.nl/file/File_2d165f32-fd28-4924-8e51-95ee5bb74759)  
39. \[D\] Why are Byte Pair Encoding tokenizers preferred over character level ones in LLMs?, accessed on April 23, 2025, [https://www.reddit.com/r/MachineLearning/comments/1ax6xuh/d\_why\_are\_byte\_pair\_encoding\_tokenizers\_preferred/](https://www.reddit.com/r/MachineLearning/comments/1ax6xuh/d_why_are_byte_pair_encoding_tokenizers_preferred/)  
40. LLM Tokenization \- Hundred Blocks, accessed on April 23, 2025, [https://hundredblocks.github.io/transcription\_demo/](https://hundredblocks.github.io/transcription_demo/)  
41. Problematic Tokens: Tokenizer Bias in Large Language Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2406.11214](https://arxiv.org/html/2406.11214)  
42. A Formal Perspective on Byte-Pair Encoding \- ACL Anthology, accessed on April 23, 2025, [https://aclanthology.org/2023.findings-acl.38v2.pdf](https://aclanthology.org/2023.findings-acl.38v2.pdf)  
43. Tokenization \- Different types of tokenizers and why it is used? \- Corpnce, accessed on April 23, 2025, [https://www.corpnce.com/tokenization-different-types-of-tokenizers-and-why-it-is-used/](https://www.corpnce.com/tokenization-different-types-of-tokenizers-and-why-it-is-used/)  
44. Estimating The Cost of GPT Using The tiktoken Library in Python \- DataCamp, accessed on April 23, 2025, [https://www.datacamp.com/tutorial/estimating-cost-of-gpt-using-tiktoken-library-python](https://www.datacamp.com/tutorial/estimating-cost-of-gpt-using-tiktoken-library-python)  
45. A Comprehensive Analysis of Various Tokenizers for Arabic Large Language Models \- MDPI, accessed on April 23, 2025, [https://www.mdpi.com/2076-3417/14/13/5696](https://www.mdpi.com/2076-3417/14/13/5696)  
46. Tokenization in Large Language Models (LLMs) \- ingoampt \- Artificial Intelligence integration into iOS apps and SaaS \+ Education, accessed on April 23, 2025, [https://ingoampt.com/tokenization-in-large-language-models-llms/](https://ingoampt.com/tokenization-in-large-language-models-llms/)  
47. What is Tokenization in NLP? Here's All You Need To Know \- Analytics Vidhya, accessed on April 23, 2025, [https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/](https://www.analyticsvidhya.com/blog/2020/05/what-is-tokenization-nlp/)  
48. \[D\] SentencePiece, WordPiece, BPE... Which tokenizer is the best one? : r/MachineLearning, accessed on April 23, 2025, [https://www.reddit.com/r/MachineLearning/comments/rprmq3/d\_sentencepiece\_wordpiece\_bpe\_which\_tokenizer\_is/](https://www.reddit.com/r/MachineLearning/comments/rprmq3/d_sentencepiece_wordpiece_bpe_which_tokenizer_is/)  
49. google/sentencepiece: Unsupervised text tokenizer for Neural Network-based text generation. \- GitHub, accessed on April 23, 2025, [https://github.com/google/sentencepiece](https://github.com/google/sentencepiece)  
50. openai-cookbook/examples/How\_to\_count\_tokens\_with\_tiktoken.ipynb at main \- GitHub, accessed on April 23, 2025, [https://github.com/openai/openai-cookbook/blob/main/examples/How\_to\_count\_tokens\_with\_tiktoken.ipynb](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)  
51. Understanding GPT tokenizers \- Hacker News, accessed on April 23, 2025, [https://news.ycombinator.com/item?id=36248633](https://news.ycombinator.com/item?id=36248633)  
52. Tiktokenizer, accessed on April 23, 2025, [https://tiktokenizer.vercel.app/](https://tiktokenizer.vercel.app/)  
53. 01\. Let's build the GPT Tokenizer v2 \- Kaggle, accessed on April 23, 2025, [https://www.kaggle.com/code/shravankumar147/01-let-s-build-the-gpt-tokenizer-v2](https://www.kaggle.com/code/shravankumar147/01-let-s-build-the-gpt-tokenizer-v2)  
54. \[D\] Moving away from Unicode for more equal token representation across global languages? : r/MachineLearning \- Reddit, accessed on April 23, 2025, [https://www.reddit.com/r/MachineLearning/comments/10mbct5/d\_moving\_away\_from\_unicode\_for\_more\_equal\_token/](https://www.reddit.com/r/MachineLearning/comments/10mbct5/d_moving_away_from_unicode_for_more_equal_token/)  
55. arXiv:2407.21783v3 \[cs.AI\] 23 Nov 2024, accessed on April 23, 2025, [https://r.jordan.im/download/language-models/grattafiori2024.pdf](https://r.jordan.im/download/language-models/grattafiori2024.pdf)  
56. FoNE: Precise Single-Token Number Embeddings via Fourier Features \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2502.09741v1](https://arxiv.org/html/2502.09741v1)  
57. Getting the most out of your tokenizer for pre-training and domain adaptation \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2402.01035v1](https://arxiv.org/html/2402.01035v1)  
58. GlotScript: A Resource and Tool for Low Resource Writing System Identification \- ACL Anthology, accessed on April 23, 2025, [https://aclanthology.org/2024.lrec-main.687.pdf](https://aclanthology.org/2024.lrec-main.687.pdf)  
59. Interpreting Embedding Spaces by Conceptualization \- ACL Anthology, accessed on April 23, 2025, [https://aclanthology.org/2023.emnlp-main.106.pdf](https://aclanthology.org/2023.emnlp-main.106.pdf)  
60. Towards an Artificial Neuroscience: Analytics for Language Model Interpretability \- DSpace@MIT, accessed on April 23, 2025, [https://dspace.mit.edu/bitstream/handle/1721.1/158869/gurnee-wesg-phd-orc-2025-thesis.pdf?sequence=-1\&isAllowed=y](https://dspace.mit.edu/bitstream/handle/1721.1/158869/gurnee-wesg-phd-orc-2025-thesis.pdf?sequence=-1&isAllowed=y)  
61. arXiv:2402.10688v2 \[cs.CL\] 15 Apr 2024, accessed on April 23, 2025, [https://arxiv.org/pdf/2402.10688](https://arxiv.org/pdf/2402.10688)  
62. How do Large Language Models Understand Relevance? A Mechanistic Interpretability Perspective \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2504.07898v1](https://arxiv.org/html/2504.07898v1)  
63. \[2504.08808\] Exploring the Effectiveness and Interpretability of Texts in LLM-based Time Series Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2504.08808](https://arxiv.org/abs/2504.08808)  
64. Representation Engineering for Large-Language Models: Survey and Research Challenges, accessed on April 23, 2025, [https://arxiv.org/html/2502.17601v1](https://arxiv.org/html/2502.17601v1)  
65. Attention Heads of Large Language Models: A Survey \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2409.03752v1](https://arxiv.org/html/2409.03752v1)  
66. 06: Interpretability Research: What LLMs Really Think \- OscarAI, accessed on April 23, 2025, [https://www.hioscar.ai/06-interpretability-research](https://www.hioscar.ai/06-interpretability-research)  
67. Towards Learning to Reason: Comparing LLMs with Neuro-Symbolic on Arithmetic Relations in Abstract Reasoning \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2412.05586v1](https://arxiv.org/html/2412.05586v1)  
68. A Survey on Mathematical Reasoning and Optimization with Large Language Models \- arXiv, accessed on April 23, 2025, [https://arxiv.org/pdf/2503.17726](https://arxiv.org/pdf/2503.17726)  
69. Prompting Strategies for Enabling Large Language Models to Infer Causation from Correlation \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2412.13952v1](https://arxiv.org/html/2412.13952v1)  
70. MathCAMPS: Fine-grained Synthesis of Mathematical Problems From Human Curricula \- arXiv, accessed on April 23, 2025, [https://arxiv.org/pdf/2407.00900](https://arxiv.org/pdf/2407.00900)  
71. Evaluating LLMs' Mathematical and Coding Competency through Ontology-guided Interventions \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2401.09395v3](https://arxiv.org/html/2401.09395v3)  
72. Guiding Language Model Math Reasoning with Planning Tokens \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2310.05707v2](https://arxiv.org/html/2310.05707v2)  
73. Guiding Language Model Reasoning with Planning Tokens \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2310.05707v4](https://arxiv.org/html/2310.05707v4)  
74. SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2504.00255v1](https://arxiv.org/html/2504.00255v1)  
75. SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2408.15545v2](https://arxiv.org/html/2408.15545v2)  
76. \[D\] How do these LLMs train on scientific data with symbols, equations, etc.? \- Reddit, accessed on April 23, 2025, [https://www.reddit.com/r/MachineLearning/comments/1aki0hr/d\_how\_do\_these\_llms\_train\_on\_scientific\_data\_with/](https://www.reddit.com/r/MachineLearning/comments/1aki0hr/d_how_do_these_llms_train_on_scientific_data_with/)  
77. MDEval: Evaluating and Enhancing Markdown Awareness in Large Language Models, accessed on April 23, 2025, [https://arxiv.org/html/2501.15000v1](https://arxiv.org/html/2501.15000v1)  
78. mathematical notation not fully rendered · Issue \#3057 · Mintplex-Labs/anything-llm \- GitHub, accessed on April 23, 2025, [https://github.com/Mintplex-Labs/anything-llm/issues/3057](https://github.com/Mintplex-Labs/anything-llm/issues/3057)  
79. New feature: Properly shown mathematical equations \- ChatGPT \- OpenAI Developer Forum, accessed on April 23, 2025, [https://community.openai.com/t/new-feature-properly-shown-mathematical-equations/73833](https://community.openai.com/t/new-feature-properly-shown-mathematical-equations/73833)  
80. math in markdown failed rendering · community · Discussion \#41087 \- GitHub, accessed on April 23, 2025, [https://github.com/orgs/community/discussions/41087](https://github.com/orgs/community/discussions/41087)  
81. Markdown rendering issue in AI Assistant (characters lost or misrendered) : LLM-15957, accessed on April 23, 2025, [https://youtrack.jetbrains.com/issue/LLM-15957/Markdown-rendering-issue-in-AI-Assistant-characters-lost-or-misrendered](https://youtrack.jetbrains.com/issue/LLM-15957/Markdown-rendering-issue-in-AI-Assistant-characters-lost-or-misrendered)  
82. Issues with Katex/ngx-markdown Rendering in Angular 16 \- Stack Overflow, accessed on April 23, 2025, [https://stackoverflow.com/questions/78220687/issues-with-katex-ngx-markdown-rendering-in-angular-16](https://stackoverflow.com/questions/78220687/issues-with-katex-ngx-markdown-rendering-in-angular-16)  
83. Math Rendering is Wrong \- Daniel's Blog, accessed on April 23, 2025, [https://danilafe.com/blog/math\_rendering\_is\_wrong/](https://danilafe.com/blog/math_rendering_is_wrong/)  
84. \[2411.08181\] Challenges in Guardrailing Large Language Models for Science \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2411.08181](https://arxiv.org/abs/2411.08181)  
85. lmmlzn/Awesome-LLMs-Datasets \- GitHub, accessed on April 23, 2025, [https://github.com/lmmlzn/Awesome-LLMs-Datasets](https://github.com/lmmlzn/Awesome-LLMs-Datasets)  
86. MathFusion: Enhancing Mathematic Problem-solving of LLM through Instruction Fusion \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2503.16212v1](https://arxiv.org/html/2503.16212v1)  
87. Evaluating Language Model Math Reasoning via Grounding in Educational Curricula \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2408.04226v2](https://arxiv.org/html/2408.04226v2)  
88. \[2408.04226\] Mathfish: Evaluating Language Model Math Reasoning via Grounding in Educational Curricula \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2408.04226](https://arxiv.org/abs/2408.04226)  
89. Evaluating language models for mathematics through interactions \- PMC, accessed on April 23, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11181017/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11181017/)  
90. \[2404.08335\] Toward a Theory of Tokenization in LLMs \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2404.08335](https://arxiv.org/abs/2404.08335)  
91. Toward a Theory of Tokenization in LLMs \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2404.08335v2](https://arxiv.org/html/2404.08335v2)  
92. Understanding the Logical Capabilities of Large Language Models via Out-of-Context Representation Learning \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2503.10408v1](https://arxiv.org/html/2503.10408v1)  
93. TokenRec: Learning to Tokenize ID for LLM-based Generative Recommendations \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2406.10450v2](https://arxiv.org/html/2406.10450v2)  
94. Improving Self Consistency in LLMs through Probabilistic Tokenization \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2407.03678v1](https://arxiv.org/html/2407.03678v1)  
95. Master Token Counting with Tiktoken for OpenAI Models \- Cheatsheet.md, accessed on April 23, 2025, [https://cheatsheet.md/langchain-tutorials/tiktoken](https://cheatsheet.md/langchain-tutorials/tiktoken)  
96. Tiktoken Tutorial: OpenAI's Python Library for Tokenizing Text | DataCamp, accessed on April 23, 2025, [https://www.datacamp.com/tutorial/tiktoken-library-python](https://www.datacamp.com/tutorial/tiktoken-library-python)  
97. Removing strange/special characters from outputs llama 3.1 model \- Stack Overflow, accessed on April 23, 2025, [https://stackoverflow.com/questions/79021544/removing-strange-special-characters-from-outputs-llama-3-1-model](https://stackoverflow.com/questions/79021544/removing-strange-special-characters-from-outputs-llama-3-1-model)  
98. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, accessed on April 23, 2025, [https://aclanthology.org/volumes/2024.emnlp-main/](https://aclanthology.org/volumes/2024.emnlp-main/)  
99. Attention Meets Post-hoc Interpretability: A Mathematical Perspective \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2402.03485v1](https://arxiv.org/html/2402.03485v1)  
100. The challenge of uncertainty quantification of large language models in medicine \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2504.05278v1](https://arxiv.org/html/2504.05278v1)  
101. \[2410.12852\] The Large Language Model GreekLegalRoBERTa \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2410.12852](https://arxiv.org/abs/2410.12852)  
102. Mapping the Mind of a Large Language Model \- Anthropic, accessed on April 23, 2025, [https://www.anthropic.com/research/mapping-mind-language-model](https://www.anthropic.com/research/mapping-mind-language-model)  
103. Meltemi: The first Greek Large Language Model, accessed on April 23, 2025, [https://www.greeknewsagenda.gr/meltemi-the-first-greek-large-language-model/](https://www.greeknewsagenda.gr/meltemi-the-first-greek-large-language-model/)  
104. Opportunities and Challenges of Large Language Models for Low-Resource Languages in Humanities Research \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2412.04497v2](https://arxiv.org/html/2412.04497v2)  
105. LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy: ✨✨Latest Advances on Neuro-Symbolic Learning in the era of Large Language Models \- GitHub, accessed on April 23, 2025, [https://github.com/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy)  
106. Tiktokenizer, accessed on April 23, 2025, [https://www.tiktokenizer.dev/](https://www.tiktokenizer.dev/)  
107. openai-cookbook/examples/How\_to\_count\_tokens\_with\_tiktoken.ipynb at main \- GitHub, accessed on April 23, 2025, [https://github.com/openai/openai-cookbook/blob/main/examples/How\_to\_count\_tokens\_with\_tiktoken.ipynb?short\_path=83d2031](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb?short_path=83d2031)  
108. tiktoken is a fast BPE tokeniser for use with OpenAI's models. \- GitHub, accessed on April 23, 2025, [https://github.com/openai/tiktoken](https://github.com/openai/tiktoken)  
109. Shifting Long-Context LLMs Research from Input to Output \- arXiv, accessed on April 23, 2025, [https://arxiv.org/html/2503.04723v2](https://arxiv.org/html/2503.04723v2)  
110. Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2410.05983](https://arxiv.org/abs/2410.05983)  
111. \[2411.11061\] Beyond Human-Like Processing: Large Language Models Perform Equivalently on Forward and Backward Scientific Text \- arXiv, accessed on April 23, 2025, [https://arxiv.org/abs/2411.11061](https://arxiv.org/abs/2411.11061)  
112. Proceedings of the 20th Conference on Natural Language Processing (KONVENS 2024\) \- Universität Wien, accessed on April 23, 2025, [https://konvens-2024.univie.ac.at/fileadmin/user\_upload/k\_konvens2024/2024.konvens-main.pdf](https://konvens-2024.univie.ac.at/fileadmin/user_upload/k_konvens2024/2024.konvens-main.pdf)  
113. Proceedings of the Workshop on DLnLD: Deep Learning and Linked Data @LREC-COLING-2024 \- ACL Anthology, accessed on April 23, 2025, [https://aclanthology.org/2024.dlnld-1.pdf](https://aclanthology.org/2024.dlnld-1.pdf)  
114. BUILDING AND EVALUATING OPEN-VOCABULARY LANGUAGE MODELS by Sebastian Jonathan Mielke A dissertation submitted to The Johns Hopki, accessed on April 23, 2025, [https://www.cs.jhu.edu/\~jason/papers/mielke.thesis23.pdf](https://www.cs.jhu.edu/~jason/papers/mielke.thesis23.pdf)  
115. Methods of Annotating and Identifying Metaphors in the Field of Natural Language Processing \- MDPI, accessed on April 23, 2025, [https://www.mdpi.com/1999-5903/15/6/201](https://www.mdpi.com/1999-5903/15/6/201)  
116. Lexicography and Semantics \- ResearchGate, accessed on April 23, 2025, [https://www.researchgate.net/profile/Dragana-Spica/publication/384885027\_ENHANCING\_JAPANESE\_LEXICAL\_NETWORKS\_USING\_LARGE\_LANGUAGE\_MODELS\_Extracting\_Synonyms\_and\_Antonyms\_with\_GPT-4o/links/670d990823e2381cf6f1db20/ENHANCING-JAPANESE-LEXICAL-NETWORKS-USING-LARGE-LANGUAGE-MODELS-Extracting-Synonyms-and-Antonyms-with-GPT-4o.pdf](https://www.researchgate.net/profile/Dragana-Spica/publication/384885027_ENHANCING_JAPANESE_LEXICAL_NETWORKS_USING_LARGE_LANGUAGE_MODELS_Extracting_Synonyms_and_Antonyms_with_GPT-4o/links/670d990823e2381cf6f1db20/ENHANCING-JAPANESE-LEXICAL-NETWORKS-USING-LARGE-LANGUAGE-MODELS-Extracting-Synonyms-and-Antonyms-with-GPT-4o.pdf)