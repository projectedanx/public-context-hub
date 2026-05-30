# **Precision vs. Padding: Diagnosing the Role of Adjectives in Prompt Engineering and Language Model Cognition**

## **Introduction**

The interaction between humans and Large Language Models (LLMs) is increasingly mediated through natural language prompts, instructions designed to elicit specific behaviors or outputs.1 Within these prompts, adjectives—words that modify nouns and pronouns—play a critical, yet often underestimated, role. While seemingly simple linguistic elements, their function extends beyond mere description. Adjectives shape semantic interpretation, influence the model's cognitive processes, calibrate stylistic output, and crucially, can be points of failure leading to ambiguity, bias, or hallucination. The practice of prompt engineering, which involves formulating effective prompts, frequently relies on intuition or trial-and-error, particularly concerning the use of modifiers.2 This report addresses the central tension surrounding adjectives in prompts: the fine line distinguishing necessary semantic *precision* from detrimental linguistic *padding*. A deeper, evidence-based understanding of how LLMs process adjectives is essential as these models become more integrated into complex, high-stakes applications.

This report undertakes a multi-lens investigation into the function and impact of adjectives within prompt structures and LLM cognition. Adopting a framework that integrates insights from lexical semantics, prompt dynamics, comparative cognition, systems of style, and meta-tool reflexivity, the analysis aims to dissect the multifaceted role of these modifiers. By examining their linguistic typology, their influence on semantic weight and syntactic parsing, their strategic positioning, their potential for redundancy or enrichment, and their comparison to human processing, this work seeks to move beyond surface-level observations. The objective is to provide computational linguists, AI language model designers, and technical communication scholars with a nuanced diagnosis of how adjectives operate at the human-LLM interface, culminating in evidence-based heuristics for their effective use in prompt engineering.

## **Section 1: The Linguistic Architecture of Adjectives in Prompts (Lexical Semantics & Typology Lens)**

Understanding the role of adjectives in prompt engineering necessitates a foundational grasp of their linguistic properties and classifications. Their behavior within the artificial cognitive system of an LLM is deeply rooted in their grammatical functions and semantic categories as understood in human language.

### **Subsection 1.1: Core Linguistic Functions and Definitions**

Adjectives constitute a primary word class, alongside nouns and verbs, fundamentally serving to indicate properties or qualities of entities (objects, people, places) or concepts.4 They modify or describe nouns and pronouns, providing additional information about attributes such as age, size, shape, color, quality, or origin.4

Syntactically, adjectives perform two principal functions which significantly influence how they are processed and interpreted within a sentence structure, and consequently, within a prompt:

1. **Attributive Function:** Adjectives function attributively when they appear directly before the noun they modify, forming part of the noun phrase.4 Examples include "the *blue* sea" or "an *old* man".8 In this position, the adjective typically specifies a characteristic that helps identify or classify the noun.  
2. **Predicative Function:** Adjectives function predicatively when they follow a linking verb (such as *be, seem, become*) and describe the subject of the sentence.4 Examples include "the sea *is blue*" or "the man *seems old*".8 Here, the adjective asserts a property about the subject, forming the core of the predicate.10 The distinction is critical: attributive adjectives integrate modification directly into the noun concept, while predicative adjectives make an assertion about an established subject, potentially impacting the flow of information and semantic interpretation.11

A less common but relevant structure is the **Postpositive** position, where an adjective immediately follows the noun or pronoun it modifies, often in institutionalized expressions ("the Governor *General*") or when modifying indefinite pronouns ("something *useful*", "everyone *present*").8

While most adjectives can function both attributively and predicatively 8, some are restricted. Certain adjectives are predominantly attributive (e.g., *main*, *former*, *atomic*) 8, while others are primarily predicative (e.g., *afraid*, *asleep*, *alike*, *aware*, *galore*).8 Understanding these constraints is vital, as using an adjective in an ungrammatical position can lead to processing errors or misinterpretation by an LLM trained on standard syntax. For instance, "*an afraid child*" is ungrammatical, whereas "*the child was afraid*" is standard.8 Similarly, one can have "a *gala* party" but not "*the party was gala*".10

The semantic relationship established by an adjective also differs based on its position. In predicative use, the adjective phrase (AP) acts as a function applied to the subject via a mediating element (like the verb 'be'), forming a proposition about that subject.11 In attributive use, the AP often functions intersectively, narrowing the set denoted by the noun.11

### **Subsection 1.2: Adjective Typology Relevant to Prompt Engineering**

For the nuanced task of prompt engineering, a functional typology extending beyond basic grammatical roles is necessary. Different classes of adjectives carry distinct semantic weights and exert different kinds of influence on LLM interpretation. Key types include:

* **Descriptive/Qualitative Adjectives:** These are the most common type, denoting inherent or observed qualities (e.g., *red, large, heavy, soft, happy*).4 They are often gradable (allowing comparison). Their impact in prompts depends heavily on their specificity.  
* **Limiting Adjectives:** These specify the noun's reference rather than describing a quality. They include:  
  * *Possessives:* *my, your, his, her, its, their, whose*.7  
  * *Demonstratives:* *this, that, these, those*.7  
  * *Interrogatives:* *which, what, whose*.7  
  * Indefinites/Quantifiers: some, any, few, several, many, all, no.6  
    These often function similarly to determiners and carry significant semantic weight, strongly constraining the scope of the noun phrase they modify.  
* **Comparative and Superlative Adjectives:** These express degrees of a quality relative to other entities (*faster, more complex, highest, least effective*).4 They are formed regularly (e.g., adding \-er/-est, using more/less/most/least).6 They are essential for prompts involving evaluation, ranking, or comparison tasks.  
* **Absolute/Non-Gradable Adjectives:** These describe all-or-nothing states that typically cannot be compared or intensified (e.g., *dead, unique, final, complete, perfect*).6 Using comparatives or intensifiers with these (e.g., "*more* unique," "*very* final") can signal logical inconsistency or colloquial usage, potentially confusing an LLM expecting strict semantics.  
* **Coordinate Adjectives:** Two or more adjectives independently modifying the same noun, usually separated by commas or 'and' (e.g., "a *long, complex* process").6 The order of coordinate adjectives often follows conventional patterns (e.g., opinion before size before age).6 Violating these patterns or using too many coordinate adjectives might increase processing complexity for the LLM or introduce ambiguity if the adjectives belong to incompatible categories.  
* **Compound Adjectives:** Formed from multiple words, often hyphenated when attributive, expressing a single concept (e.g., *user-friendly, state-of-the-art, long-term, absent-minded*).6 These are crucial for conveying specific technical or idiomatic concepts concisely.  
* **Participial Adjectives:** Derived from verb participles (e.g., *interesting, broken, tired, ongoing, completed*).5 They retain some verbal sense, often implying an action or state resulting from an action, and can carry aspectual nuances.  
* **Proper Adjectives:** Derived from proper nouns and capitalized (e.g., *American, Victorian, Marxist, Shakespearean*).6 They link the noun to a specific entity, period, place, or system, often invoking a rich set of associated knowledge.  
* **Relational/Nominal Adjectives:** Derived from nouns, indicating a relation to the noun (e.g., *industrial* policy, *solar* energy, *linguistic* analysis, *atomic* bomb).14 They often classify the noun rather than describing a property and are frequently non-gradable and restricted to attributive use.14  
* **Stage-Level vs. Individual-Level Adjectives:** This semantic distinction differentiates temporary or transient states (**stage-level**: *drunk, available, sick, present*) from more permanent, inherent, or defining properties (**individual-level**: *intelligent, tall, altruistic, wooden*).11 This distinction impacts semantic interpretation (temporary state vs. essential characteristic) and can influence syntactic behavior; for instance, stage-level predicates are more likely to appear in existential 'there' constructions ("There are firemen *available*") than individual-level ones ("\*There are firemen *altruistic*").11 This suggests LLMs might process these types differently based on learned syntactic and semantic correlations.  
* **Evaluative/Subjective Adjectives:** Express judgment or opinion (*good, bad, important, useful, effective, beautiful*). These are inherently context-dependent and pose significant challenges related to ambiguity and bias.  
* **Emotional Adjectives:** Describe feelings or evoke emotions (*happy, sad, angry, joyful, depressing*). While LLMs can recognize and generate text with these tones, their processing lacks genuine affect.

The syntactic function (attributive vs. predicative) and the semantic class (e.g., stage/individual-level, absolute/relative, limiting) likely exert a more direct influence on LLM interpretation within a prompt than purely morphological features. The position affects information flow and assertion timing 11, while the semantic class carries inherent constraints or implications about the nature of the property being described.11 Furthermore, certain adjective types, such as limiting, absolute, and proper adjectives, carry strong implicit constraints that significantly narrow the semantic space for the LLM.6 Unlike vague descriptive terms, these provide clearer signals, potentially reducing the model's inferential burden and improving precision when used appropriately.

### **Subsection 1.3: Adjective Typology Map**

The following table provides a matrix summarizing the potential functions and effects of various adjective types within the context of prompt engineering for LLMs.

**Table 1: Adjective Typology Map: Functional Effects in Prompt Engineering**

| Adjective Type | Specificity Control | Semantic Weight | Tone Calibration | Ambiguity Risk | Bias Introduction | Hallucination Trigger | Syntactic Constraint | Information Gain |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Descriptive (Vague)** | Low | Low | Variable | High | Medium | Medium | Low | Low |
| **Descriptive (Specific)** | High | Medium-High | High | Low | Low | Low | Low | High |
| **Limiting (Determiners)** | High | High | Low | Low | Low | Low | High | High |
| **Comparative/Superlative** | High (for ranking) | High | Medium | Low | Low | Low | Medium | High |
| **Absolute/Non-Gradable** | High (binary state) | High | Low | Low (if used correctly) | Low | Medium (if misused) | High (non-gradable) | High |
| **Coordinate** | Variable | Variable | Medium | Medium (order/scope) | Low | Low | Medium (ordering) | Variable |
| **Compound** | High (specific concept) | High | Variable | Low | Low | Low | Medium | High |
| **Participial** | Variable | Medium | Medium | Medium | Low | Low | Low | Variable |
| **Proper** | High (specific entity) | High | Medium | Low | Medium (associations) | Low | Low | High |
| **Relational/Nominal** | High (classification) | High | Low | Low | Low | Low | High (often attrib.) | High |
| **Stage-Level** | Medium (temporary) | Medium | Low | Low | Low | Low | Medium (syntax) | Medium |
| **Individual-Level** | Medium (inherent) | Medium | Low | Low | Medium (stereotypes) | Low | Medium (syntax) | Medium |
| **Evaluative/Subjective** | Low | Variable | High | Very High | High | High | Low | Low-Variable |
| **Emotional** | Medium | Medium | Very High | Medium | Medium | Medium | Low | Medium |

*Note: Effects are typical tendencies and can vary significantly based on context and specific LLM.*

This map serves as a heuristic guide, linking linguistic categories to their potential impact on LLM behavior. It highlights how different adjective choices can strategically enhance precision (e.g., Limiting, Specific Descriptive, Compound) or introduce risks (e.g., Vague Descriptive, Evaluative).

## **Section 2: Prompt Dynamics: Semantic Weight, Positioning, and Clarity (Prompt Dynamics & AI Semiosis Lens)**

Beyond the inherent properties of adjectives, their placement within the prompt structure and their contribution relative to other elements significantly shape how an LLM interprets the user's intent. This section explores the dynamics of adjectives in prompts, focusing on semantic weight, the impact of positioning, and the critical balance between clarity and noise.

### **Subsection 2.1: Syntactic Position and Semantic Interpretation**

As established, the primary syntactic functions—attributive and predicative—have distinct semantic consequences.11 In prompts, this translates to how the modification is applied to the core concepts. An attributive adjective ("Generate a *short* report") modifies the concept 'report' directly within the noun phrase, potentially influencing the model's generation parameters early. A predicative structure ("Generate a report that *is short*") makes an assertion about the report, which might be processed as a separate constraint or property check after the initial concept generation.

The distinction between pre-nominal and post-nominal positioning, while less flexible in English than in languages like Italian 15, further illustrates how syntax governs meaning. Pre-nominal adjectives in English can be ambiguous regarding restrictive vs. non-restrictive interpretation ("Every *blessed* person was healed" \- which people?) and intersective vs. non-intersective readings ("a *beautiful* dancer" \- beautiful person or beautiful dancing?).15 Post-nominal adjectives in English, often derived from reduced relative clauses, tend to be unambiguously restrictive and intersective ("Every person *blessed* was healed," "a dancer *more beautiful* than Mary").15 While post-nominal descriptive adjectives are less common 8, understanding this principle highlights that the LLM's interpretation isn't just about the adjective's meaning but also its structural relationship to the noun, which can resolve or introduce ambiguity. Careful syntactic arrangement within the prompt is therefore not merely stylistic but functionally crucial for clarity.

### **Subsection 2.2: Specificity, Semantic Weight, and Information Gain**

The effectiveness of an adjective in guiding an LLM is closely tied to its **specificity** and **semantic weight**. Specificity refers to how precisely an adjective narrows down the possible meanings or properties of the noun it modifies.16 High-specificity adjectives (e.g., *hexagonal*, *Javanese*, *100-year-old*) provide clear, unambiguous information, reducing the LLM's interpretive burden.6 Low-specificity adjectives (e.g., *nice*, *good*, *interesting*, *difficult*) are vague and require the LLM to infer the intended meaning from context or default to common interpretations, increasing the risk of miscommunication.14

**Semantic weight** can be conceptualized as the degree to which an adjective contributes critical information or constraint to the prompt's overall meaning. Adjectives like *medical*, *final*, *my*, or *only* carry high semantic weight, significantly altering the interpretation of the noun phrase. Conversely, adjectives like *nice*, *lovely*, or *really* often carry low semantic weight, adding minimal constraint.

From an information-theoretic perspective, the utility of an adjective can be framed in terms of **information gain**.17 An adjective provides high information gain if its presence significantly reduces the uncertainty (entropy) associated with the noun or the overall prompt task.17 Specific, constraining adjectives typically yield high information gain, while vague, predictable, or redundant adjectives offer low information gain.

LLMs demonstrate sensitivity to the semantic nuances conveyed by different adjectives. Studies using the Word-in-Context (WiC) task show that models like GPT-4o adjust their criteria for semantic equivalence based on the adjective used in the prompt (e.g., "the *same* meaning" vs. "a *similar* meaning" vs. "a *related* meaning"), impacting precision and recall scores accordingly.19 This indicates that LLMs functionally assign semantic weight based on the adjective's inherent meaning and its level on a spectrum of semantic relatedness.19

However, simply increasing specificity is not always the optimal strategy. Research investigating the systematic substitution of nouns, verbs, and adjectives with synonyms of varying specificity across STEM, law, and medicine domains suggests that while extreme vagueness is detrimental, there might be an optimal *range* of specificity for LLM performance, rather than a linear relationship where more specific is always better.20 For adjectives specifically, the impact was less statistically significant in the datasets used, possibly due to their lower frequency compared to nouns and verbs in question-answering tasks, though some models showed improvement with high-specificity adjectives in mathematical reasoning.20 This suggests a threshold effect: specificity is crucial up to a point to disambiguate and guide the model, but excessive or irrelevant specificity might yield diminishing returns or even introduce noise, particularly if the core task relies more heavily on other lexical elements.

Furthermore, the LLM's interpretation of subjective or context-dependent adjectives relies heavily on its training data and operational semantics, which may not align perfectly with human understanding of synonyms or related terms.21

### **Subsection 2.3: The Redundancy Spectrum: Enriching vs. Padding**

A key challenge in using adjectives effectively is avoiding redundancy. Redundant adjectives are those that add little or no new information, constraint, or nuance to the prompt.22 They constitute "padding" or "fluff" rather than meaningful enrichment.23 Common prompt engineering advice emphasizes clarity, conciseness, and the avoidance of unnecessary words, including superfluous adjectives.16

Redundancy can arise from:

* Using multiple adjectives with very similar meanings (e.g., "a *complete and comprehensive* list").  
* Using adjectives whose meaning is already implied by the noun (e.g., "a *round* circle").  
* Using weak intensifiers or vague positive terms that add no specific detail (e.g., "*really nice*", "*very good*").

The cost of such padding includes:

* **Increased Prompt Length:** Consumes valuable tokens in the context window.25  
* **Reduced Clarity:** Can obscure the core message and dilute the impact of more important terms.22  
* **Potential Confusion:** May introduce subtle, unintended nuances or contradictions.  
* **Inefficiency:** Increases processing time and computational cost.26

Tools and techniques exist to help identify and eliminate redundant words.27 However, context is paramount. An adjective like "*short*" might be redundant if the task inherently implies brevity (e.g., "Write a tweet"), but enriching if specifying a particular type of output (e.g., "Write a *short*, *impactful* tagline" vs. "Write a *detailed*, *technical* description"). The distinction between padding and enrichment depends on whether the adjective provides valuable information gain relative to the task and context. Redundant adjectives essentially introduce noise, degrading the signal-to-noise ratio of the prompt and potentially hindering the LLM's ability to accurately discern and execute the user's core intent.22

### **Subsection 2.4: Prompt Case Dissection**

To illustrate the practical impact of adjective choice, the following table compares LLM responses to prompts with varying adjectival strategies across different tasks.

**Table 2: Prompt Case Dissection: Impact of Adjectives on LLM Responses**

| Task Type | Original Prompt (Minimal Adjectives) | Modified Prompt (Specific/Strategic Adjectives) | Modified Prompt (Vague/Redundant Adjectives) | LLM Response (Original) | LLM Response (Specific Adj.) | LLM Response (Vague Adj.) | Analysis of Differences |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Creative Writing** | "Write a story about a knight." | "Write a *short*, *grim* story about a *weary*, *battle-scarred* knight defending a *ruined* tower." | "Write an *amazing*, *really interesting* story about a *brave*, *strong* knight." | Generic tale of a knight, possibly heroic, standard setting. | Focused narrative with dark tone, specific character traits (weary, scarred), defined setting (ruined tower), concise length. | Generic heroic tale, lacking specific tone or detail, potentially longer and less focused due to vague descriptors. | Specific adjectives controlled tone, characterization, setting, and length. Vague adjectives resulted in generic output similar to the minimal prompt but potentially less concise. |
| **Technical Explan.** | "Explain photosynthesis." | "Explain photosynthesis for a *high school biology* audience, focusing on the *key* inputs and outputs, in *clear, simple* language." | "Explain the *important* process of photosynthesis in a *good*, *detailed* way." | Standard textbook explanation, potentially complex. | Tailored explanation using accessible vocabulary, structured around inputs/outputs, suitable for the target audience. | Potentially overly complex or overly simplistic, lacking clear focus due to undefined terms like "important" and "good." | Strategic adjectives tailored the explanation's level, focus, and language. Vague adjectives failed to provide useful constraints. |
| **Marketing Copy** | "Write an ad for coffee." | "Write *persuasive* ad copy for *organic*, *fair-trade* coffee, targeting *eco-conscious millennials*. Emphasize *rich* flavor and *ethical* sourcing. Use an *upbeat*, *aspirational* tone." | "Write a *great* ad for *really good* coffee. Make it *appealing* and *effective*." | Generic coffee ad focusing on taste or energy. | Targeted ad copy highlighting specific features (organic, fair-trade), appealing to values (eco-conscious, ethical), using specified tone and focusing on flavor. | Generic, bland ad copy relying on weak positive terms, lacking a clear target audience or unique selling proposition. | Specific adjectives defined the product features, target audience, key selling points, and tone, leading to focused, persuasive copy. Vague adjectives produced ineffective results. |
| **Code Generation** | "Write Python code to sort a list." | "Write *efficient* Python code using *quicksort* to sort a list of *integers* in *ascending* order. Include *brief* comments explaining the main steps." | "Write *some nice* Python code to sort a list. Make it *work well*." | Basic Python sort function (e.g., list.sort()). | Implementation of quicksort algorithm specifically for integers, sorted ascendingly, with comments as requested. | Likely basic sort function, possibly without comments or specific algorithm, as "nice" and "work well" are undefined. | Specific adjectives dictated the algorithm (*quicksort*), data type (*integers*), order (*ascending*), efficiency goal (*efficient*), and documentation style (*brief* comments). Vague terms were useless. |

These examples demonstrate that strategically chosen, specific adjectives act as powerful controls, guiding the LLM towards desired content, style, tone, and format. Conversely, vague or redundant adjectives fail to provide meaningful guidance, often resulting in generic, unfocused, or less useful outputs.

## **Section 3: Comparative Cognition: Adjective Processing in Humans and LLMs (Comparative Cognition Lens)**

While LLMs process language based on patterns learned from vast datasets, human cognition involves a richer interplay of semantics, pragmatics, world knowledge, and affective states. Comparing how humans and LLMs process adjectives, particularly modifiers carrying subjective or emotional weight, reveals fundamental differences in their underlying cognitive architectures and highlights potential pitfalls in human-LLM communication.

### **Subsection 3.1: LLM Attention Mechanisms and Modifier Salience**

The primary mechanism enabling LLMs, particularly transformer-based models, to process relationships between words in a sequence is **attention**, specifically **self-attention**.28 This mechanism allows the model to dynamically weigh the importance or relevance of different input tokens when processing any given token.29 It calculates **attention weights** (or scores) that reflect the relative influence each token should have on the interpretation of others.31

This process involves transforming each token's embedding into three vectors: **Query (Q)**, **Key (K)**, and **Value (V)**.28 The Query vector represents what information a token is "looking for," the Key vector represents the information a token "contains," and the Value vector holds the information to be passed forward.31 By comparing the Query of one token with the Keys of all other tokens (often via dot-product multiplication), the model computes alignment scores.31 These scores are then typically normalized (e.g., using a softmax function) to produce attention weights that sum to one, indicating the proportional focus allocated to each token.31 Tokens deemed highly relevant receive higher weights, while irrelevant tokens receive weights close to zero.31

Attention mechanisms are crucial for handling **long-range dependencies**, allowing a modifier (like an adjective) to influence the interpretation of a noun even if they are separated by many other words in the prompt.28 The **salience** of a token—its importance for the model's prediction or processing at a given step—is directly related to the attention weights it receives or distributes.28 Higher attention corresponds to higher salience.31 Researchers use various techniques, including analyzing attention matrices directly or employing gradient-based methods, to visualize or quantify token salience and interpret model behavior.34

However, attention distribution is not always semantically optimal. Phenomena like **"attention sinks"** have been observed, where initial tokens in a sequence receive disproportionately high attention regardless of their semantic relevance, potentially due to the mechanics of autoregressive modeling and softmax normalization.36 Furthermore, attention patterns can vary across model layers, sometimes exhibiting more "local" focus in early layers.36

While attention mechanisms don't explicitly label words by type (noun, verb, adjective), they learn to weigh tokens differently based on context and learned linguistic patterns.31 For example, an adjective modifying a crucial noun might receive high attention because it significantly alters the noun's meaning in that context.31 Similarly, the attention paid to an adjective might depend on its predictive value for subsequent tokens or its role in fulfilling the prompt's overall task.31 The model learns these relational weightings statistically from its training data.

### **Subsection 3.2: Human vs. AI Processing of Modifiers**

The LLM's attention-driven, pattern-matching approach contrasts sharply with human processing of adjectives. Humans integrate modifiers using a combination of linguistic knowledge, real-world experience, pragmatic reasoning, and emotional context.24 While LLMs excel at capturing syntactic relationships and semantic co-occurrences, they lack the grounded understanding and inferential depth of human cognition.

This difference becomes particularly apparent with certain adjective types:

* **Evaluative/Subjective Adjectives:** Terms like *good, bad, important, effective, successful* are inherently subjective and context-dependent. Humans interpret these based on shared values, specific goals, and contextual cues. LLMs, lacking this grounding, interpret such terms based on patterns in their training data.21 This can lead to outputs reflecting dominant viewpoints, biases, or simply a superficial understanding of the evaluation criteria.21 When LLMs are used as evaluators ("LLM-as-a-judge"), their assessment of qualities like "helpfulness" or "correctness" depends entirely on the definitions provided in the evaluation prompt and their learned semantic associations, not on genuine judgment.39  
* **Emotional Adjectives:** LLMs can recognize and generate text exhibiting emotional tones (*happy, sad, angry, empathetic*).40 Studies show LLMs can even enhance the emotional expression in text compared to human originals.40 However, this is mimicry based on learned associations, not genuine affective experience. Research indicates that LLMs' decision-making can be significantly influenced by emotional framing in prompts (e.g., "Respond as if you are *angry*").43 This influence can lead to biased, irrational, or ethically inconsistent outputs, particularly in smaller or non-English models, suggesting that emotional prompting can override alignment safeguards.43 A comparative study on the use of the adjective 'love' found humans used it more in normal language styles and specific personal contexts (partner, country, self), while AI tended towards poetic styles and definitional or general statement contexts, often placing the word structurally differently in sentences.44 This highlights the gap between statistical language generation and situated human emotional expression.  
* **Intensifiers:** Words like *very, extremely, highly* are processed by LLMs as tokens modifying adjacent words. Their impact is likely based on learned statistical effects on probability distributions rather than a nuanced grasp of degree modification. Overuse of weak intensifiers and vague adjectives is often cited as a stylistic marker of AI-generated text.23

General stylistic differences also point to underlying cognitive contrasts. AI-generated text is often characterized by:

* **Repetitive Phrasing and Predictability:** Stemming from probabilistic word prediction.46  
* **Lack of Depth or Personal Experience:** AI cannot draw on lived experiences or unique perspectives.24  
* **Overly Neutral, Formal, or Polite Tone:** Often a result of alignment tuning to avoid controversy or offense.24  
* **Grammatical "Perfection" or Slight Unnaturalness:** AI may adhere rigidly to grammar rules or produce slightly awkward phrasing, unlike human writers who use stylistic variation and intentional "imperfections".24  
* **Frequent Use of Certain Adjectives:** Terms like *multifaceted, comprehensive, rapid, transformative, crucial, pivotal* appear frequently in some LLM outputs, perhaps reflecting patterns favored in formal or informational training data.48

Human writing, in contrast, typically exhibits more personality, variability in sentence structure ("burstiness"), emotional nuance, occasional errors, and grounding in personal experience or specific viewpoints.24

The challenges LLMs face in processing modifiers are evident in specific applications. In medical coding, LLMs struggled to accurately identify the need for CPT modifiers (e.g., Modifier 22 for *increased* procedural complexity) from operative notes, often failing to account for procedural specifics implied by descriptive language.49 In ethical decision-making scenarios, introducing socio-demographic modifiers (often adjectives describing race, gender, or status) significantly altered LLM responses, revealing underlying biases and inconsistencies in ethical priorities.51

Ultimately, LLMs process adjectives primarily based on learned statistical correlations and syntactic context captured via attention mechanisms.30 This surface-level processing, while powerful for pattern recognition, differs fundamentally from the human capacity for deep semantic integration, pragmatic inference, and affective understanding. This gap explains why LLMs may misinterpret nuanced adjectives, overweight syntactically prominent but semantically weak ones (like attention sinks 36), or struggle with the subjectivity inherent in evaluative and emotional language.

## **Section 4: Systems of Style: Adjectives for Tone, Aesthetics, and Persuasion (Systems of Style Lens)**

Adjectives are not merely descriptive units; they are potent tools for shaping the stylistic, aesthetic, and persuasive dimensions of language. In prompt engineering, they serve as primary levers for calibrating the tone, voice, and genre characteristics of LLM-generated text, enabling users to guide the output towards specific communicative goals.

### **Subsection 4.1: Tone Calibration and Voice Shaping via Adjectives**

One of the most direct applications of adjectives in prompting is **tone calibration**. By explicitly including adjectives that describe the desired tone in the instructions, users can guide the LLM's stylistic choices.41 Common tonal adjectives used in prompts include:

* *Formal, Professional, Academic* 41  
* *Casual, Conversational, Friendly* 41  
* *Empathetic, Caring, Understanding* 41  
* *Humorous, Witty, Playful, Light-hearted* 41  
* *Authoritative, Informative, Confident* 41  
* *Persuasive, Urgent, Motivating* 41  
* *Neutral, Objective* 41  
* *Creative, Imaginative* 41  
* *Simple, Clear* 52

Explicit instructions like "Write in a *formal and respectful* tone" 41, "Explain in a *friendly and conversational* tone" 42, or "Answer in a *natural, human-like* manner" 53 leverage the LLM's learned associations between these adjectives and corresponding linguistic features (vocabulary, sentence structure, etc.). Strategic vocabulary choices within the prompt itself, including the adjectives used to describe the task or subject matter, further reinforce the desired tone.41

Assigning a **persona** to the LLM (e.g., "Act as an *expert* historian," "You are a *helpful* customer service agent") also implicitly sets the tone and influences the types of adjectives the model is likely to use in its response.52

Interestingly, LLMs may sometimes generate text with *enhanced* emotional expression compared to human-written originals, potentially employing more emotionally charged adjectives when adapted for engagement, as observed in news writing contexts.40 This suggests that LLMs can effectively utilize adjectives not just to match a specified tone, but sometimes to amplify it based on implicit goals like engagement. Adjectives, therefore, serve as the most direct linguistic interface for modulating the stylistic and tonal dimensions of LLM output, acting as primary tuning knobs.

### **Subsection 4.2: Adjective Patterns in Genre-Specific Prompts**

The effective use of adjectives in prompts often varies significantly depending on the target genre or application domain, reflecting the distinct stylistic conventions and communicative aims of each.

* **Marketing and Persuasive Prompts:** These prompts frequently employ adjectives designed to influence perception and motivate action. Common patterns include:  
  * **Evaluative/Positive Adjectives:** *compelling, effective, valuable, key, unique, best*.54  
  * **Benefit-Oriented Adjectives:** Highlighting positive outcomes or features (*customized, targeted, high-engagement*).54  
  * **Emotion/Urgency Adjectives:** Creating feelings like desire, exclusivity, or immediacy (*limited-time, urgent*).41  
  * Descriptive Adjectives: Highlighting appealing product qualities (rich flavor, eco-friendly, sustainable).41  
    Prompts often explicitly define the target audience and desired persuasive effect.41 However, overly promotional or "hypey" language (e.g., revolutionary, game-changing) should often be avoided as it can sound artificial.23  
* **Creative Writing and Image Generation Prompts:** This domain relies heavily on adjectives to establish mood, atmosphere, visual detail, and style. Patterns include:  
  * **Sensory and Evocative Adjectives:** *grim, weary, ruined* (from Sec 2.4); *cute, adorable, joyful, colorful, medieval, fantasy, magical, mysterious, grim, futuristic, epic* 55; *ominous, dangerous, nostalgic*.56  
  * **Style Descriptors:** Adjectives defining artistic style (*rococo, psychedelic, stonepunk, impressionist, realistic, low-poly, pixel art*).55  
  * Technical Descriptors: Specifying lighting (neon, soft, cinematic, hard light chiaroscuro), color (vivid, bright, purple and green), detail (detailed, hyper detailed), and framing (close-up, wide shot).55  
    Word order and structural elements like brackets can be used to emphasize the importance of certain adjectives or concepts.55 Prompts asking the LLM to mimic a specific author's or genre's style implicitly require the model to infer and replicate characteristic adjective usage.42  
* **Technical and Academic Prompts:** Clarity, precision, and objectivity are paramount. Adjective use focuses on:  
  * **Precise Descriptors:** Avoiding vagueness in favor of specific, unambiguous terms.  
  * **Technical/Relational Adjectives:** Using terms specific to the domain (*cardiovascular, quantum, syntactic, recursive*).  
  * **Compound Adjectives:** Employing established technical terms (*state-of-the-art, user-friendly, high-performance*).  
  * Formal Tone Adjectives: Prompts might specify a formal, academic, or technical tone.41  
    Subjective and evaluative adjectives are generally minimized unless explicitly defined.

The concept of **Text Style Transfer (TST)** further highlights the role of adjectives. TST aims to retain semantic content while altering stylistic features.57 Prompts directing TST often use adjectives to define the target style (e.g., "Rewrite this text in a *pirate* style," "Make this sound more *melodramatic*").57 The LLM must then deploy not just specific vocabulary but also associated syntactic patterns and rhetorical devices linked to that stylistic adjective.57

This genre-specificity demonstrates that effective prompt engineering requires understanding the conventional and impactful adjective patterns within the target domain, moving beyond general linguistic knowledge to domain-specific stylistic competence.

### **Subsection 4.3: Identifying and Avoiding "Style Traps"**

While adjectives are powerful stylistic tools, their misuse can lead to "style traps"—patterns of language that are weak, clichéd, or signal artificiality, often marking text as potentially AI-generated or simply poorly written. These traps frequently involve the overuse of certain types of adjectives:

* **Vague Positive Evaluators:** *amazing, great, good, nice, wonderful, fantastic*. These lack specific meaning and often serve as filler.  
* **Vague General Descriptors:** *interesting, important, significant, effective, impactful*. Without context or criteria, these convey little information.24  
* **Overused "AI Buzzwords":** *comprehensive, multifaceted, transformative, unprecedented, pivotal, crucial, robust, seamless, leverage, delve, harness*.48 While sometimes appropriate, their high frequency in some LLM outputs makes them suspect.  
* **Weak Intensifiers:** *very, really, highly, extremely*. Often used with vague adjectives, creating phrases like "*really good*" or "*very important*" which can usually be replaced by a single, stronger word (e.g., *excellent*, *critical*).  
* **Redundant Adjectives:** As discussed previously (e.g., "*complete and comprehensive*").

These traps often appear in conjunction with cliché phrases discouraged in clear writing, such as "dive into," "unlock the potential," "in today's world," "game-changing solution".23 Such language can make the text sound generic, unoriginal, and lacking in substance.24

These patterns likely arise because LLMs, trained to predict probable sequences, may default to high-frequency, generally positive but semantically weak adjectives.48 Alignment tuning, aimed at producing helpful and harmless responses, might also favor safe, neutral, or broadly positive descriptors over more specific or potentially controversial language.24

Strategies for avoiding these traps include:

* **Prioritizing Specificity:** Replace vague terms with concrete details and precise descriptors (Heuristic 1).  
* **Using Stronger Verbs:** Often eliminates the need for weak adjective-adverb combinations.  
* **Focusing on Concrete Nouns:** Ground descriptions in tangible objects or concepts.  
* **Showing, Not Telling:** Use descriptions of actions or effects rather than simply stating a quality with a vague adjective.  
* **Using Thesauruses Critically:** Find more precise synonyms, but be mindful that LLM operational semantics might not perfectly match human nuances.21  
* **Editing Ruthlessly:** Remove unnecessary words, especially vague modifiers and intensifiers.23

Over-reliance on these vague "style trap" adjectives represents a failure to provide sufficient information gain or constraint in the prompt.17 This forces the LLM to rely on generic patterns or potentially biased internal defaults, leading to outputs that are stylistically weak and potentially less accurate or helpful.

## **Section 5: Adjective-Driven Prompt Failures (Multiple Lenses)**

Despite their utility, adjectives are frequent sources of failure in prompt engineering, leading to misinterpretations, biased outputs, and hallucinations. These failures often arise from ambiguity inherent in the adjectives themselves or from the complex interplay between the adjective, the prompt context, and the LLM's internal knowledge and biases.

### **Subsection 5.1: Sources of Ambiguity and Misinterpretation**

Ambiguity is a primary driver of prompt failure, and adjectives contribute significantly to it in several ways:

* **Lexical Ambiguity (Polysemy):** Many adjectives have multiple meanings. A prompt using a polysemous adjective without sufficient context can lead the LLM to select an unintended meaning.58 For example, "*light* jacket" could refer to color or weight. "*Right* turn" could mean correct or directional.  
* **Syntactic Ambiguity:** The grammatical structure of the prompt can create ambiguity regarding which noun an adjective modifies, particularly with prepositional phrases or complex sentences.58 The classic example "I shot an elephant in my pajamas" leaves the adjective phrase "in my pajamas" ambiguously attached. Similarly, "Report on users with *negative* feedback" is unclear whether the users or the feedback are negative.58  
* **Subjective/Evaluative Ambiguity:** Adjectives expressing subjective judgment (*good, bad, important, effective, relevant, appropriate, significant*) are inherently ambiguous without clearly defined criteria.21 A prompt asking for "*important* points" forces the LLM to guess what constitutes importance for the user, often leading to generic or irrelevant output.60 This lack of objective grounding is a major challenge.21  
* **Vagueness:** Even non-evaluative adjectives can be too vague for the task (*big, small, fast, slow*). Without context or comparison points, these terms lack precise meaning.

When faced with ambiguity, LLMs attempt to resolve it based on the surrounding context and patterns learned during training. However, this resolution process can easily go astray if the context is insufficient or if the LLM's learned patterns do not match the user's specific intent. Techniques for ambiguity reduction, such as providing clear context, using specific language, defining terms, and specifying the desired output format, are crucial for mitigating these risks.16 Unresolved ambiguity forces the LLM into a state of underspecification, creating gaps that it may fill unreliably, leading to downstream errors like bias or hallucination.

### **Subsection 5.2: Adjectives and Bias Propagation/Amplification**

LLMs are known to inherit and sometimes amplify societal biases present in their vast training datasets.62 Adjectives play a significant role in this process:

* **Stereotypical Associations:** Training data often contains correlations between certain adjectives and specific demographic groups (based on race, gender, religion, age, occupation, etc.). For example, adjectives like *nurturing* might be statistically associated more with women, while *assertive* or *aggressive* might be linked more with men.64 Similarly, certain adjectives might be disproportionately associated with specific racial or religious groups in biased contexts.64  
* **Triggering Biased Outputs:** Using these statistically loaded adjectives in prompts, even seemingly neutral ones, can trigger the LLM to generate outputs that reflect these learned stereotypes.38 Prompting for a description of an "*assertive* female leader" might elicit a response laden with negative stereotypes if the training data contained such biases. This occurs even in models explicitly aligned or debiased, indicating the persistence of these associations.38  
* **Bias via Socio-Demographic Modifiers:** Studies have shown that introducing socio-demographic modifiers (e.g., describing a patient in an ethical dilemma as "*low-income*" or belonging to a "*marginalized group*") can significantly shift LLM decisions, revealing biases related to factors like socioeconomic status, race, or gender.51 These modifiers, often adjectives, activate biases that influence the model's reasoning or prioritization of ethical principles.51  
* **Limitations of Mitigation:** While developers implement safeguards against overtly biased prompts 63 and techniques exist to probe biases (like the LLM Word Association Test 38) or attempt mitigation through prompting (e.g., adding positive adjectives like "*hard-working*" before a group name, or instructing the model to be unbiased 64), these methods have limitations. Implicit biases associated with adjectives remain difficult to eradicate completely.38

Therefore, bias related to adjectives extends beyond obviously sensitive terms. Seemingly neutral descriptive adjectives can carry latent biases learned from data, and their use in prompts can inadvertently activate and amplify harmful stereotypes. Mitigating this requires careful consideration of the potential connotations and learned associations of adjectives, particularly when describing people or social groups.

### **Subsection 5.3: Case Studies: Hallucinations Linked to Adjectives**

LLM **hallucinations**—generating outputs that are factually incorrect, nonsensical, or not grounded in the provided context—are a significant concern.60 Adjectives can contribute to or trigger hallucinations in several ways:

* **Vagueness and Underspecification:** When prompts use vague or subjective adjectives without sufficient definition or context (*effective*, *suitable*, *relevant*, *significant*), they create an informational gap.60 To fulfill the prompt's request, the LLM might invent plausible-sounding but factually unsupported details.65 For example, asking for "*effective* marketing strategies" without defining effectiveness criteria might lead the LLM to generate fabricated statistics or case studies. Low prompt readability, formality, or concreteness, often linked to vague language, increases this risk.68  
* **Overly Evocative or Figurative Language:** In creative tasks, using highly metaphorical, abstract, or extreme adjectives (*celestial*, *infinite*, *perfect*) without proper grounding might push the LLM beyond plausible generation into fabricating impossible or nonsensical scenarios.60 The prompt essentially invites unconstrained invention.  
* **Conflicting Descriptors:** Prompts containing contradictory adjectives (e.g., "Describe the *silent*, *loud* machine," "Explain the *simple*, *complex* process") can confuse the LLM, leading to logically inconsistent or nonsensical outputs.  
* **Implying Non-existent Properties:** Using adjectives to ascribe properties to objects that cannot possess them (e.g., "the *emotional* state of the rock," "the *four-sided* triangle") can force the LLM to either refuse the prompt or generate nonsensical or fabricated information.  
* **Misinterpretation in Domain-Specific Contexts:** In technical domains, misinterpreting the specific meaning of a descriptive or evaluative adjective can lead to factual errors. For instance, in summarizing time-series charts, misjudging a trend as *significant*, *upward*, or *downward* based on visual cues without correct calculation constitutes a hallucination (Trend Direction Error, Extremum Error).66 Similarly, chatbots citing non-existent policies or fake legal cases might be triggered by prompts asking for *relevant* or *applicable* information where the LLM lacks grounded knowledge and invents plausible answers.65 Hallucinations are more likely when the LLM lacks sufficient training data on a specific topic, forcing it to extrapolate or invent when prompted with related adjectives.69

These cases illustrate that adjectives contributing to ambiguity or underspecification act as catalysts for hallucination. By failing to provide adequate constraints, such adjectives give the LLM license to generate content unmoored from factual grounding or logical consistency.

### **Subsection 5.4: Failure Mode Stack**

The following table synthesizes common prompt failures driven by the misuse or inherent challenges of adjectives.

**Table 3: Failure Mode Stack (Adjective-Driven)**

| Failure Mode | Description | Contributing Adjective Types (Examples) | Illustrative Prompt Snippet | Potential Consequence |
| :---- | :---- | :---- | :---- | :---- |
| **Ambiguity (Lexical)** | Adjective has multiple distinct meanings. | Polysemous (e.g., *light*, *right*, *fair*) | "Describe the *fair* treatment." | Misinterpretation of intent (e.g., just vs. pale). |
| **Ambiguity (Syntactic)** | Grammatical structure allows multiple attachment points for the adjective. | Adjectives in complex PPs or clauses (e.g., *red*, *negative*) | "Analyze reviews from users with *low* scores." | Incorrect data filtering (users vs. scores low?). |
| **Ambiguity (Subjective)** | Adjective lacks objective, prompt-defined criteria. | Evaluative/Vague (e.g., *effective*, *appropriate*, *good*, *relevant*) | "Summarize the *relevant* sections." | Generic output, hallucinated criteria, user dissatisfaction. |
| **Bias Amplification** | Adjective activates learned stereotypical associations. | Terms statistically linked to demographics (e.g., *assertive*, *emotional*) | "Profile the *ambitious* candidate." | Generation of biased or stereotypical content. |
| **Hallucination (Gap Fill)** | Vague/undefined adjective forces LLM to invent details to satisfy prompt. | Vague/Undefined (e.g., *suitable*, *innovative*, *significant*) | "List *innovative* solutions for X." | Fabricated solutions, features, or data. |
| **Hallucination (Over-Int.)** | Highly evocative/extreme adjective pushes model beyond plausible generation. | Figurative/Extreme (e.g., *perfect*, *infinite*, *magical*) | "Create a *perfect* schedule for the project." | Unrealistic, impossible, or nonsensical output. |
| **Logical Contradiction** | Prompt uses adjectives with conflicting meanings. | Opposites (e.g., *hot*/*cold*, *full*/*empty*, *simple*/*complex*) | "Describe the *full*, *empty* box." | Nonsense output, refusal to answer, confused generation. |
| **Redundancy Noise** | Unnecessary adjectives obscure key instructions or waste context window. | Synonymous/Implied/Weak (e.g., *complete and comprehensive*, *round* circle) | "Give a *detailed and thorough* explanation..." | Reduced clarity, inefficiency, potential misweighting. |

This stack highlights how different forms of adjectival imprecision or misuse can lead to distinct failure modes, emphasizing the need for careful selection and contextualization of modifiers in prompt design.

## **Section 6: Adjectives as Functional Levers in Prompt Systems (Meta-Tool Reflexivity Lens)**

Beyond their role within individual user prompts, adjectives function as crucial components within the broader architecture of LLM interaction systems. They appear in system messages defining core AI behavior, act as control signals in multi-step prompting techniques like chaining, and their functional essence is implicitly captured in prompt tuning methodologies. Understanding this meta-level role is key to advanced system design and optimization.

### **Subsection 6.1: Role in System Messages and Prompt Frameworks**

System prompts or messages provide high-level instructions that govern an LLM's behavior across interactions, setting its persona, constraints, and operational guidelines. Adjectives are frequently used within these system messages to define these parameters:

* **Persona/Tone:** System prompts often use adjectives to establish the AI's default personality, such as "*helpful*, *polite*, *neutral*, *concise*, *creative*, *truthful*, *nuanced*, *insightful*, *efficient*".70 This guides the overall style and word choice, including the adjectives the LLM itself is likely to use.  
* **Constraints/Policies:** Adjectives can specify limitations or desired attributes. For example, instructions might mandate responses be "*unbiased*" 53 or avoid generating "*offensive*" imagery.70  
* **Policy Implementation:** Adjectives can be part of procedural logic within system prompts. For instance, OpenAI's DALL-E integration within ChatGPT includes instructions stating that if asked to generate an image in the style of a post-1912 artist, the system should substitute the artist's name with "*three adjectives* that capture key aspects of the style".70 This demonstrates adjectives being used programmatically as a workaround for policy restrictions.

The frequent appearance of certain adjectives in LLM outputs (e.g., *multifaceted, comprehensive, rapid*) might stem partially from their inclusion or implicit favoring in system-level instructions or the underlying alignment training that shapes the model's default style.48

Furthermore, conceptual frameworks for prompt engineering, like the "Method Actors" model, rely heavily on descriptive language (implicitly including adjectives) to set the scene for the LLM by defining its character, motivation, and setting, thereby guiding its performance.72

This usage highlights a dual functionality: within user prompts, adjectives primarily modify content descriptions, but within system messages, they act as control parameters shaping the LLM's core response generation policies.

### **Subsection 6.2: Adjectives in Prompt Chaining and Tuning Strategies**

Adjectives also serve as functional levers in more advanced prompt engineering techniques:

* **Prompt Chaining:** This technique breaks down complex tasks into a sequence of simpler, interconnected prompts, where the output of one step feeds into the next.73 Adjectives can play a critical role in defining the transformation required between steps. For example:  
  * Step 1: "Summarize the following text."  
  * Step 2: "Rewrite the summary in a *more formal* tone."  
  * Step 3: "Expand the formal summary, adding specific technical details from the original text."  
    Here, the adjectives (more formal, specific technical) act as directives guiding the refinement process at each stage.73 Conditional chaining might also rely on adjectival evaluations: "Analyze the sentiment of the review. If the sentiment is negative, generate a sympathetic response offering solutions".75 Adjectives thus serve as crucial links and transition signals within the chain, enabling complex, multi-stage workflows.74  
* **Prompt Tuning:** This involves optimizing the prompts themselves (either text-based "hard prompts" or learned "soft prompts" / embeddings) to elicit the best performance from a frozen LLM on downstream tasks.76 While soft prompts consist of numerical embeddings rather than words, the optimization process likely discovers embedding patterns that functionally replicate the guiding role of effective hard prompt components, including critical adjectives.76 The goal is to find inputs that steer the model's internal processing effectively. Techniques like adapter-based prompt tuning further refine this, potentially learning representations analogous to adjectival modification.77 Prompt tuning can be employed to adapt models for tasks where specific adjectival nuances are important (e.g., capturing a particular style) or to mitigate biases, potentially by finding prompts that counteract biased associations linked to certain descriptors.76 Though opaque, the learned prompts in tuning act as implicit adjectival levers controlling model behavior.76

### **Subsection 6.3: Designing for Reflexivity: Towards Adjective-Aware Prompt Assistants**

Given the significant impact and potential pitfalls of adjective usage, there is a need for tools and methods that support more reflexive and critical prompt design. This points towards the development of **adjective-aware prompt assistants** or integrated features within prompt engineering platforms.

Such a system could function as a meta-tool, analyzing user-written prompts to:

* **Identify Risky Adjectives:** Flag potentially vague, ambiguous, subjective, or emotionally charged adjectives that are common sources of failure (Section 5).  
* **Detect Redundancy:** Highlight adjectives that add little information gain or could be removed for conciseness (Section 2.3).  
* **Check for Bias:** Cross-reference adjectives used (especially when describing people) against known stereotype associations or bias benchmarks.38  
* **Suggest Alternatives:** Offer more specific, less ambiguous, or less biased synonyms or rephrasing options.  
* **Prompt for Clarification:** Ask the user to define subjective terms ("What criteria define an '*effective* solution' in this context?").  
* **Assess Specificity:** Evaluate if the level of adjectival specificity is appropriate for the task, potentially drawing on optimal ranges identified for similar tasks.20

This concept builds upon existing work in automated prompt optimization 79, instruction decomposition 2, and LLM-based evaluation 25, but specializes these approaches to the specific linguistic category of adjectives. Designing such an assistant aligns with the meta-learning goal of creating tools to audit and improve prompt structures over time, fostering more precise, effective, and responsible human-LLM interaction.

## **Section 7: Synthesis and Meta-Linguistic Recommendations**

The preceding analysis, spanning linguistic typology, prompt dynamics, comparative cognition, style systems, failure modes, and meta-tool functions, reveals the complex and often critical role of adjectives in shaping LLM behavior. This section synthesizes these findings through a pivot table and offers concrete, evidence-based heuristics for more effective adjective use in prompt engineering.

### **Subsection 7.1: Insight Pivot Table**

The following table cross-references key adjective types with their observed or hypothesized impact across various dimensions of AI behavior, summarizing the core relationships explored throughout this report.

**Table 4: Insight Pivot Table: Adjective Type × AI Behavior**

| Adjective Type | Output Specificity | Tone/Style Control | Bias Risk | Ambiguity Risk | Hallucination Risk | Attention Focus | Information Gain |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Descriptive (Vague)** | Decreases | Low/Unpredictable | Medium | High | Medium-High | Diffuse | Low |
| **Descriptive (Specific)** | Increases | High | Low | Low | Low | Focused | High |
| **Limiting (Determiners)** | High Constraint | Low | Low | Low | Low | High | High |
| **Comparative/Superlative** | High (Ranking) | Medium | Low | Low | Low | High | High |
| **Absolute/Non-Gradable** | High Constraint | Low | Low | Low (if correct) | Medium (if wrong) | High | High |
| **Coordinate** | Variable | Medium | Low | Medium | Low | Variable | Variable |
| **Compound** | High (Concept) | Variable | Low | Low | Low | High | High |
| **Proper** | High (Entity) | Medium | Medium | Low | Low | High | High |
| **Relational/Nominal** | High (Class) | Low | Low | Low | Low | High | High |
| **Stage-Level** | Medium (State) | Low | Low | Low | Low | Medium | Medium |
| **Individual-Level** | Medium (Property) | Low | Medium | Low | Low | Medium | Medium |
| **Evaluative/Subjective** | Low/Variable | High | High | Very High | High | Variable | Low-Variable |
| **Emotional** | Variable | Very High | Medium | Medium | Medium | Variable | Medium |

*Note: This table represents synthesized tendencies; actual effects are context-dependent.*

This synthesis underscores that while specific and constraining adjectives (Limiting, Absolute, Compound, Proper, Relational) generally enhance precision and reduce risk, vague and subjective types (Vague Descriptive, Evaluative, Emotional) often decrease specificity and increase risks of ambiguity, bias, and hallucination.

### **Subsection 7.2: Meta-Linguistic Recommendations: Heuristics for Adjective Use**

Based on the analysis presented, the following heuristics can guide prompt engineers toward more effective and responsible use of adjectives:

* **Heuristic 1 (Prioritize Specificity over Vagueness):**  
  * *Rationale:* Vague adjectives (*good, interesting*) provide low information gain, increase ambiguity, and risk hallucination or generic output (Sections 2, 5). Specific descriptors guide the LLM more effectively.16  
  * *Action:* Replace vague terms with concrete, descriptive adjectives relevant to the task. Specify *how* something is good or interesting.  
  * *Example Rewrite:* "Generate *good* marketing slogans" → "Generate *catchy*, *memorable* marketing slogans under 10 words."  
* **Heuristic 2 (Quantify or Rank Instead of Evaluating Subjectively):**  
  * *Rationale:* Subjective evaluations (*long, effective, important*) are ambiguous without criteria and prone to bias (Sections 1, 5). Comparatives, superlatives, or explicit metrics offer clearer constraints.  
  * *Action:* Where possible, use measurable terms, comparative/superlative forms for ranking, or define the criteria for evaluation within the prompt.  
  * *Example Rewrite:* "Write a *long* analysis" → "Write an analysis of approximately *2000 words*." OR "Identify the *best* approach" → "Identify the approach with the *lowest implementation cost*."  
* **Heuristic 3 (Mind the Syntactic Position):**  
  * *Rationale:* Attributive adjectives modify early and integrate into the noun concept; predicative adjectives assert properties (Section 2.1).11 Position affects interpretation, especially regarding restriction and intersection.15  
  * *Action:* Place critical constraining adjectives attributively (pre-nominally) for early filtering. Use predicative structures for clear assertions about a subject. Be aware of potential pre-nominal ambiguity in English.15  
  * *Example Consideration:* "*Urgent* task: Analyze server logs" (sets context early) vs. "Analyze server logs. The task is *urgent*." (asserts urgency separately).  
* **Heuristic 4 (Audit for Redundancy and Padding):**  
  * *Rationale:* Redundant adjectives add noise, consume tokens, and can obscure key instructions without adding value (Section 2.3).22  
  * *Action:* Scrutinize prompts for adjectives that don't add significant new information or constraint. Test if removing the adjective changes the core meaning. Eliminate weak intensifiers and synonymous pairs.  
  * *Example Rewrite:* "Provide a *complete and comprehensive* overview" → "Provide a *comprehensive* overview."  
* **Heuristic 5 (Screen for Implicit Bias Associations):**  
  * *Rationale:* Seemingly neutral adjectives can carry learned stereotypical connotations linked to demographic groups, triggering biased outputs (Section 5.2).38  
  * *Action:* When describing people or social groups, consciously evaluate whether chosen adjectives might inadvertently reinforce stereotypes. Consider alternative, less loaded descriptors.  
  * *Example Reflection:* Does describing a female leader as "*assertive*" activate different, potentially more negative, associations in the LLM's training data than describing a male leader the same way?  
* **Heuristic 6 (Define or Contextualize Evaluative Terms):**  
  * *Rationale:* Evaluative adjectives (*effective, appropriate, successful, relevant*) are major sources of ambiguity and hallucination if criteria are undefined (Section 5.1, 5.3).21  
  * *Action:* If using such terms, provide explicit criteria, context, or examples within the prompt to define what they mean for the specific task.  
  * *Example Rewrite:* "Find *relevant* research papers" → "Find research papers published *in the last 5 years* discussing *Transformer attention mechanisms*."  
* **Heuristic 7 (Use Tone Adjectives Explicitly and Concisely):**  
  * *Rationale:* Adjectives are primary levers for tone control (Section 4.1). Explicit instruction is more reliable than hoping the LLM infers tone.41  
  * *Action:* Clearly state the desired tone using one or two well-chosen adjectives in the main instruction (e.g., "*formal and empathetic*", "*concise and technical*").  
  * *Example:* "Respond to the customer complaint in a *professional yet empathetic* tone."  
* **Heuristic 8 (Leverage Precise Domain-Specific Adjectives):**  
  * *Rationale:* Technical, compound, and relational adjectives provide necessary precision in specialized domains (Section 4.2).  
  * *Action:* Use the standard, accepted adjectival terminology of the field (e.g., *cardiovascular*, *object-oriented*, *geospatial*, *state-of-the-art*) to ensure accuracy and clarity.  
  * *Example:* "Explain the *aerodynamic* principles of..."

Applying these heuristics requires a meta-linguistic awareness, moving beyond simply writing prompts to actively diagnosing and refining the linguistic signals sent to the LLM, with particular attention to the nuanced role of adjectives.

## **Section 8: Reflexive Insights and Future Research Directions**

This investigation into the role of adjectives prompts a reflection on ingrained practices and illuminates pathways for future inquiry. Engaging with the complexities of how these modifiers function at the human-LLM interface necessitates both critical self-assessment and a forward-looking research agenda.

### **Subsection 8.1: Reflexive Insights**

Applying the lens of this research back onto typical academic and technical practices reveals potential habits and biases:

* **Common Adjective Patterns:** In analytical writing and research-oriented prompting, there might be a tendency to overuse adjectives emphasizing rigor, novelty, or complexity, such as *systematic, comprehensive, robust, novel, significant, nuanced,* or *complex*. While sometimes justified, these can become default padding if not used precisely.  
* **Potential Biases:** A default reliance on terms associated with objectivity or analytical depth might reflect a Western academic bias. The drive for "clarity" might sometimes overlook culturally diverse communication styles. Overuse of intensifiers (*highly significant, very robust*) could be a cognitive shortcut reflecting confirmation bias or an attempt to persuade through emphasis rather than evidence.  
* **Opportunities for Sharpening:** Personal prompts and writing could likely benefit from stricter auditing for redundancy (e.g., removing "very," "really") and replacing vague evaluators ("important," "effective") with specific criteria or descriptions of impact, thereby enhancing precision.  
* **Designing an Audit Assistant:** Conceptualizing an adjective audit assistant (as proposed in Section 6.3) seems feasible and valuable. Key features would include:  
  * **Vagueness/Subjectivity Flags:** Identifying terms like *good, effective, important* and prompting for criteria.  
  * **Redundancy Detection:** Spotting synonymous pairs or weak intensifiers.  
  * **Bias Check:** Cross-referencing adjectives against known bias databases or patterns, especially in prompts describing people.  
  * **Specificity Analysis:** Assessing if the level of adjectival detail seems appropriate for the task type.  
  * Alternative Suggestions: Offering more precise or less loaded synonyms based on context.  
    This tool would encourage more deliberate and informed adjective selection in prompt engineering.

### **Subsection 8.2: Gaps and Future Research Directions**

This analysis identifies several areas requiring further investigation:

* **Quantitative Impact Studies:** Beyond specific tasks like WiC 19, more systematic research is needed to quantify how different adjective types and densities affect LLM performance across a wider range of tasks (e.g., summarization, creative generation, reasoning) and metrics (e.g., factual accuracy, coherence, creativity, bias scores).  
* **Attention Mechanism Interpretability:** Current understanding of how attention mechanisms specifically handle modifiers versus core content words is limited. Research employing advanced interpretability techniques 33 focused on dissecting the attention patterns related to different adjective classes and syntactic positions (attributive vs. predicative) is needed.  
* **Cross-Linguistic Prompting:** Most prompt engineering research focuses on English. Given typological variations in how languages encode adjectival concepts 4, research is needed on how adjectives function in prompts for multilingual LLMs and whether optimal prompting strategies differ across languages.  
* **Automated Detection of Adjective-Induced Issues:** Developing robust, automated methods for detecting potential ambiguity, bias, or hallucination risks specifically linked to adjective usage in prompts is crucial for building safer and more reliable LLM applications.2  
* **Prompt Tuning for Stylistic Control:** Further exploration is needed into how prompt tuning techniques (soft and hard prompts) can be optimized specifically for fine-grained stylistic control, potentially by targeting representations analogous to adjectival modification.76  
* **Cognitive Load:** The impact of adjective density, complexity, and specificity on the cognitive load experienced by both the human writing the prompt and the LLM processing it remains largely unexplored.  
* **Specificity in Subjective Tasks:** The role and optimal range of adjective specificity warrant further investigation, particularly in tasks heavily reliant on subjective judgment, such as sentiment analysis or personality assessment, where adjectives carry significant weight.20

Addressing these gaps will deepen the understanding of the intricate relationship between linguistic modification and artificial cognition, paving the way for more precise, effective, and responsible use of LLMs. Adjectives, far from being mere decorative elements, are fundamental components of the linguistic code that programs LLM behavior, demanding careful consideration in the ongoing development of human-AI communication.

## **References**

4

#### **Works cited**

1. Exploring Prompt Engineering Practices in the Enterprise \- arXiv, accessed on April 14, 2025, [https://arxiv.org/html/2403.08950v1](https://arxiv.org/html/2403.08950v1)  
2. CoPrompter: User-Centric Evaluation of LLM Instruction Alignment for Improved Prompt Engineering \- arXiv, accessed on April 14, 2025, [https://arxiv.org/html/2411.06099v1](https://arxiv.org/html/2411.06099v1)  
3. Prompt Engineering vs. Blind Prompting \- Mitchell Hashimoto, accessed on April 14, 2025, [https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting](https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting)  
4. (PDF) Adjective Classes A Cross-linguistic Typology \- ResearchGate, accessed on April 14, 2025, [https://www.researchgate.net/publication/267448349\_Adjective\_Classes\_A\_Cross-linguistic\_Typology](https://www.researchgate.net/publication/267448349_Adjective_Classes_A_Cross-linguistic_Typology)  
5. Glossary of grammatical terms \- Oxford English Dictionary, accessed on April 14, 2025, [https://www.oed.com/information/understanding-entries/glossary-grammatical-terms/](https://www.oed.com/information/understanding-entries/glossary-grammatical-terms/)  
6. What Is an Adjective? | Definition, Types & Examples \- Scribbr, accessed on April 14, 2025, [https://www.scribbr.com/parts-of-speech/adjectives/](https://www.scribbr.com/parts-of-speech/adjectives/)  
7. Adjectives \- Definition, Forms, Types, Usage and Examples \- BYJU'S, accessed on April 14, 2025, [https://byjus.com/english/adjectives/](https://byjus.com/english/adjectives/)  
8. Attributive and Predicative Adjectives @ The Internet Grammar of English \- UCL, accessed on April 14, 2025, [https://www.ucl.ac.uk/internet-grammar/adjectiv/attribut.htm](https://www.ucl.ac.uk/internet-grammar/adjectiv/attribut.htm)  
9. What is the difference between attributive and predicate adjectives? \- QuillBot, accessed on April 14, 2025, [https://quillbot.com/blog/frequently-asked-questions/what-is-the-difference-between-attributive-and-predicate-adjectives/](https://quillbot.com/blog/frequently-asked-questions/what-is-the-difference-between-attributive-and-predicate-adjectives/)  
10. difference between predicative and attributive adjective, accessed on April 14, 2025, [https://ell.stackexchange.com/questions/167264/difference-between-predicative-and-attributive-adjective](https://ell.stackexchange.com/questions/167264/difference-between-predicative-and-attributive-adjective)  
11. (PDF) The subject of adjectives: Syntactic position and semantic ..., accessed on April 14, 2025, [https://www.researchgate.net/publication/270449661\_The\_subject\_of\_adjectives\_Syntactic\_position\_and\_semantic\_interpretation](https://www.researchgate.net/publication/270449661_The_subject_of_adjectives_Syntactic_position_and_semantic_interpretation)  
12. Some grammars' inconsistent treatments of the attributive vs. predicate positions. Frustrating\! Your thoughts? : r/AncientGreek \- Reddit, accessed on April 14, 2025, [https://www.reddit.com/r/AncientGreek/comments/dhx4x5/some\_grammars\_inconsistent\_treatments\_of\_the/](https://www.reddit.com/r/AncientGreek/comments/dhx4x5/some_grammars_inconsistent_treatments_of_the/)  
13. How to tell if an adjective is attributive or predicative \[EFL context\]? \- English StackExchange, accessed on April 14, 2025, [https://english.stackexchange.com/questions/175562/how-to-tell-if-an-adjective-is-attributive-or-predicative-efl-context](https://english.stackexchange.com/questions/175562/how-to-tell-if-an-adjective-is-attributive-or-predicative-efl-context)  
14. Adjectives \- ILC-CNR, accessed on April 14, 2025, [https://www.ilc.cnr.it/EAGLES96/rep2/node12.html](https://www.ilc.cnr.it/EAGLES96/rep2/node12.html)  
15. semanticsarchive.net, accessed on April 14, 2025, [https://semanticsarchive.net/Archive/TJlMWFiM/article.pdf](https://semanticsarchive.net/Archive/TJlMWFiM/article.pdf)  
16. Mastering LLM Prompting: Insights from Two Years of Experience with Large Language Models \- Yabble, accessed on April 14, 2025, [https://www.yabble.com/blog/mastering-llm-prompting-insights-from-two-years-of-experience-with-large-language-models](https://www.yabble.com/blog/mastering-llm-prompting-insights-from-two-years-of-experience-with-large-language-models)  
17. A Deep Dive into Information Gain: Concepts, Techniques, and Effective Strategies, accessed on April 14, 2025, [https://www.numberanalytics.com/blog/deep-dive-information-gain-concepts-techniques](https://www.numberanalytics.com/blog/deep-dive-information-gain-concepts-techniques)  
18. Natural Language Processing (NLP): A Complete Guide \- Prismetric, accessed on April 14, 2025, [https://www.prismetric.com/natural-language-processing-guide/](https://www.prismetric.com/natural-language-processing-guide/)  
19. aclanthology.org, accessed on April 14, 2025, [https://aclanthology.org/2025.coling-main.466.pdf](https://aclanthology.org/2025.coling-main.466.pdf)  
20. gipplab.org, accessed on April 14, 2025, [https://gipplab.org/wp-content/papercite-data/pdf/schreiter2024.pdf](https://gipplab.org/wp-content/papercite-data/pdf/schreiter2024.pdf)  
21. Uncovering Gaps in How Humans and LLMs Interpret Subjective Language | OpenReview, accessed on April 14, 2025, [https://openreview.net/forum?id=gye2U9uNXx](https://openreview.net/forum?id=gye2U9uNXx)  
22. Prompt Engineering: Using AI to Your Advantage For Content \- Walrus Creative Works, accessed on April 14, 2025, [https://walruscreativeworks.com/2023/10/prompt-engineering-using-ai-to-your-advantage-for-content/](https://walruscreativeworks.com/2023/10/prompt-engineering-using-ai-to-your-advantage-for-content/)  
23. I finally found a prompt that makes ChatGPT write naturally : r/ChatGPTPromptGenius \- Reddit, accessed on April 14, 2025, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i\_finally\_found\_a\_prompt\_that\_makes\_chatgpt\_write/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i_finally_found_a_prompt_that_makes_chatgpt_write/)  
24. Stochastic Parrots: How to tell if something was written by an AI or a human?, accessed on April 14, 2025, [https://e-discoveryteam.com/2024/04/05/stochastic-parrots-how-to-tell-if-something-was-written-by-an-ai-or-a-human/](https://e-discoveryteam.com/2024/04/05/stochastic-parrots-how-to-tell-if-something-was-written-by-an-ai-or-a-human/)  
25. Prompt Engineering & Management in Production: Practical Lessons from the LLMOps Database \- ZenML Blog, accessed on April 14, 2025, [https://www.zenml.io/blog/prompt-engineering-management-in-production-practical-lessons-from-the-llmops-database](https://www.zenml.io/blog/prompt-engineering-management-in-production-practical-lessons-from-the-llmops-database)  
26. Prompt Engineering Overhyped? No \- But Ace These 3 GenAI Skills \- Monte Carlo Data, accessed on April 14, 2025, [https://www.montecarlodata.com/blog-is-prompt-engineering-overhyped-genai/](https://www.montecarlodata.com/blog-is-prompt-engineering-overhyped-genai/)  
27. ChatGPT prompt for eliminating redundant words \- Promptmatic, accessed on April 14, 2025, [https://promptmatic.ai/prompts/chatgpt/eliminate-redundant-words](https://promptmatic.ai/prompts/chatgpt/eliminate-redundant-words)  
28. The Mechanism of Attention in Large Language Models: A Comprehensive Guide, accessed on April 14, 2025, [https://magnimindacademy.com/blog/the-mechanism-of-attention-in-large-language-models-a-comprehensive-guide/](https://magnimindacademy.com/blog/the-mechanism-of-attention-in-large-language-models-a-comprehensive-guide/)  
29. Mastering the Attention Concept in LLM: Unlocking the Core of Modern AI, accessed on April 14, 2025, [https://metadesignsolutions.com/mastering-the-attention-concept-in-llm-unlocking-the-core-of-modern-ai/](https://metadesignsolutions.com/mastering-the-attention-concept-in-llm-unlocking-the-core-of-modern-ai/)  
30. What are Large Language Models? | A Comprehensive LLMs Guide \- Elastic, accessed on April 14, 2025, [https://www.elastic.co/what-is/large-language-models](https://www.elastic.co/what-is/large-language-models)  
31. What is an attention mechanism? | IBM, accessed on April 14, 2025, [https://www.ibm.com/think/topics/attention-mechanism](https://www.ibm.com/think/topics/attention-mechanism)  
32. What is grouped query attention (GQA)? \- IBM, accessed on April 14, 2025, [https://www.ibm.com/think/topics/grouped-query-attention](https://www.ibm.com/think/topics/grouped-query-attention)  
33. Model Interpretability for Natural Language Processing Applications \- White Rose eTheses Online, accessed on April 14, 2025, [https://etheses.whiterose.ac.uk/id/eprint/31611/1/GeorgeChrysostomouThesis.pdf](https://etheses.whiterose.ac.uk/id/eprint/31611/1/GeorgeChrysostomouThesis.pdf)  
34. Instance-adaptive Zero-shot Chain-of-Thought Prompting \- arXiv, accessed on April 14, 2025, [https://arxiv.org/pdf/2409.20441?](https://arxiv.org/pdf/2409.20441)  
35. Interpreting Deep Learning Models in Natural Language Processing: A Review \- ar5iv, accessed on April 14, 2025, [https://ar5iv.labs.arxiv.org/html/2110.10470](https://ar5iv.labs.arxiv.org/html/2110.10470)  
36. Efficient streaming language models with attention sinks | Hacker News, accessed on April 14, 2025, [https://news.ycombinator.com/item?id=37740932](https://news.ycombinator.com/item?id=37740932)  
37. Unsupervised Word Sense Disambiguation Using Transformer's Attention Mechanism, accessed on April 14, 2025, [https://www.mdpi.com/2504-4990/7/1/10](https://www.mdpi.com/2504-4990/7/1/10)  
38. Explicitly unbiased large language models still form biased ... \- PNAS, accessed on April 14, 2025, [https://www.pnas.org/doi/10.1073/pnas.2416228122](https://www.pnas.org/doi/10.1073/pnas.2416228122)  
39. LLM-as-a-judge: a complete guide to using LLMs for evaluations \- Evidently AI, accessed on April 14, 2025, [https://www.evidentlyai.com/llm-guide/llm-as-a-judge](https://www.evidentlyai.com/llm-guide/llm-as-a-judge)  
40. LLMs Enhance Emotional Expression While Maintaining Analytical Depth in News Writing \- ScholarSpace, accessed on April 14, 2025, [https://scholarspace.manoa.hawaii.edu/bitstreams/b3d3e8e7-d271-4660-bfc2-4d36b874df95/download](https://scholarspace.manoa.hawaii.edu/bitstreams/b3d3e8e7-d271-4660-bfc2-4d36b874df95/download)  
41. 10 Examples of Tone-Adjusted Prompts for LLMs \- Ghost, accessed on April 14, 2025, [https://latitude-blog.ghost.io/blog/10-examples-of-tone-adjusted-prompts-for-llms/](https://latitude-blog.ghost.io/blog/10-examples-of-tone-adjusted-prompts-for-llms/)  
42. Guiding Tone and Style through Prompts: Influencing the AI Writing Style | Suraj Sharma, accessed on April 14, 2025, [https://surajsharma.net/blog/guiding-tone-and-style-through-prompts](https://surajsharma.net/blog/guiding-tone-and-style-through-prompts)  
43. EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas, accessed on April 14, 2025, [https://openreview.net/forum?id=8aAaYEwNR4](https://openreview.net/forum?id=8aAaYEwNR4)  
44. Representation of the Use of the Adjective 'Love' between Human and AI Using ATLAS.ti Software | Atlantis Press, accessed on April 14, 2025, [https://www.atlantis-press.com/proceedings/iccollic-24/126006857](https://www.atlantis-press.com/proceedings/iccollic-24/126006857)  
45. www.atlantis-press.com, accessed on April 14, 2025, [https://www.atlantis-press.com/article/126006857.pdf](https://www.atlantis-press.com/article/126006857.pdf)  
46. AI vs. Human Writing: How to Tell the Difference? \- Quetext, accessed on April 14, 2025, [https://www.quetext.com/blog/ai-vs-human-writing](https://www.quetext.com/blog/ai-vs-human-writing)  
47. AI-Generated vs. Human-Written Text: Technical Analysis \- HackerNoon, accessed on April 14, 2025, [https://hackernoon.com/ai-generated-vs-human-written-text-technical-analysis](https://hackernoon.com/ai-generated-vs-human-written-text-technical-analysis)  
48. 100 Common ChatGPT Adjectives \- AI Phrase Finder, accessed on April 14, 2025, [https://aiphrasefinder.com/common-chatgpt-adjectives/](https://aiphrasefinder.com/common-chatgpt-adjectives/)  
49. Bridging the Coding Gap: Assessing Large Language Models for Accurate Modifier Assignment in Craniofacial Operative Notes \- PubMed, accessed on April 14, 2025, [https://pubmed.ncbi.nlm.nih.gov/40214230/](https://pubmed.ncbi.nlm.nih.gov/40214230/)  
50. Bridging the Coding Gap: Assessing Large Language Models for Accurate Modifier Assignment in Craniofacial Operative Notes \- ResearchGate, accessed on April 14, 2025, [https://www.researchgate.net/publication/390700378\_Bridging\_the\_Coding\_Gap\_Assessing\_Large\_Language\_Models\_for\_Accurate\_Modifier\_Assignment\_in\_Craniofacial\_Operative\_Notes](https://www.researchgate.net/publication/390700378_Bridging_the_Coding_Gap_Assessing_Large_Language_Models_for_Accurate_Modifier_Assignment_in_Craniofacial_Operative_Notes)  
51. Socio-Demographic Modifiers Shape Large Language Models' Ethical Decisions | medRxiv, accessed on April 14, 2025, [https://www.medrxiv.org/content/10.1101/2025.02.01.25321523v2.full](https://www.medrxiv.org/content/10.1101/2025.02.01.25321523v2.full)  
52. Prompt Engineering Best Practices: Tips, Tricks, and Tools | DigitalOcean, accessed on April 14, 2025, [https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices](https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices)  
53. 26 prompting tricks to improve LLMs | SuperAnnotate, accessed on April 14, 2025, [https://www.superannotate.com/blog/llm-prompting-tricks](https://www.superannotate.com/blog/llm-prompting-tricks)  
54. AI for Business: 110+ AI Prompts to Power your Organization \- Jasper AI, accessed on April 14, 2025, [https://www.jasper.ai/blog/ai-prompts-for-business](https://www.jasper.ai/blog/ai-prompts-for-business)  
55. Secrets of Writing Great Prompts for Stable Diffusion AI \- Animation Guides, accessed on April 14, 2025, [https://www.animationguides.com/great-prompts-for-image-generation/](https://www.animationguides.com/great-prompts-for-image-generation/)  
56. How to write AI art prompts \- Zapier, accessed on April 14, 2025, [https://zapier.com/blog/ai-art-prompts/](https://zapier.com/blog/ai-art-prompts/)  
57. Visualizing LLM Text Style Transfer: visually dissecting how to talk like a pirate \- Uncharted Software, accessed on April 14, 2025, [https://uncharted.software/assets/visualizing-LLM-text-style-transfer.pdf](https://uncharted.software/assets/visualizing-LLM-text-style-transfer.pdf)  
58. Visualizing Ambiguity: Analyzing Linguistic Ambiguity Resolution in Text-to-Image Models, accessed on April 14, 2025, [https://www.mdpi.com/2073-431X/14/1/19](https://www.mdpi.com/2073-431X/14/1/19)  
59. Tips For Building Your ChatGPT Prompting Skills \- ASU CareerCatalyst, accessed on April 14, 2025, [https://careercatalyst.asu.edu/newsroom/career/building-your-chatgpt-prompting-skills/](https://careercatalyst.asu.edu/newsroom/career/building-your-chatgpt-prompting-skills/)  
60. Optimizing Human–AI Collaboration in Chemistry: A Case Study on Enhancing Generative AI Responses through Prompt Engineering \- MDPI, accessed on April 14, 2025, [https://www.mdpi.com/2624-8549/6/4/43](https://www.mdpi.com/2624-8549/6/4/43)  
61. Prompt engineering best practices for ChatGPT | OpenAI Help Center, accessed on April 14, 2025, [https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt](https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt)  
62. Large language model \- Wikipedia, accessed on April 14, 2025, [https://en.wikipedia.org/wiki/Large\_language\_model](https://en.wikipedia.org/wiki/Large_language_model)  
63. Assessing Racial and Ethnic Bias in Text Generation by Large Language Models for Health Care–Related Tasks: Cross-Sectional Study, accessed on April 14, 2025, [https://www.jmir.org/2025/1/e57257](https://www.jmir.org/2025/1/e57257)  
64. Debiasing large language models: research opportunities\* \- PMC, accessed on April 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11639098/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11639098/)  
65. LLM hallucinations and failures: lessons from 4 examples \- Evidently AI, accessed on April 14, 2025, [https://www.evidentlyai.com/blog/llm-hallucination-examples](https://www.evidentlyai.com/blog/llm-hallucination-examples)  
66. ChartInsighter: An Approach for Mitigating Hallucination in Time-series Chart Summary Generation with A Benchmark Dataset \- arXiv, accessed on April 14, 2025, [https://arxiv.org/html/2501.09349v1](https://arxiv.org/html/2501.09349v1)  
67. Learning from Mistakes via Cooperative Study Assistant for Large Language Models \- Danqing Wang, accessed on April 14, 2025, [https://dqwang122.github.io/assets/PPT/20231027\_EMNLP2023\_SALAM.pdf](https://dqwang122.github.io/assets/PPT/20231027_EMNLP2023_SALAM.pdf)  
68. arXiv:2403.18976v1 \[cs.CL\] 27 Mar 2024 \- Aman Chadha, accessed on April 14, 2025, [https://amanchadha.com/research/2403.18976.pdf](https://amanchadha.com/research/2403.18976.pdf)  
69. LLMs cannot find reasoning errors, but can correct them | Hacker News, accessed on April 14, 2025, [https://news.ycombinator.com/item?id=38353285](https://news.ycombinator.com/item?id=38353285)  
70. What We Can Learn from OpenAI, Perplexity, TLDraw, and Vercel's System Prompts, accessed on April 14, 2025, [https://www.prompthub.us/blog/what-we-can-learn-from-openai-perplexity-tldraw-and-vercels-system-prompts](https://www.prompthub.us/blog/what-we-can-learn-from-openai-perplexity-tldraw-and-vercels-system-prompts)  
71. I made ChatGPT 4.5 leak its system prompt : r/PromptEngineering \- Reddit, accessed on April 14, 2025, [https://www.reddit.com/r/PromptEngineering/comments/1j5mca4/i\_made\_chatgpt\_45\_leak\_its\_system\_prompt/](https://www.reddit.com/r/PromptEngineering/comments/1j5mca4/i_made_chatgpt_45_leak_its_system_prompt/)  
72. LLMs as Method Actors: A Model for Prompt Engineering and Architecture \- arXiv, accessed on April 14, 2025, [https://arxiv.org/html/2411.05778v1](https://arxiv.org/html/2411.05778v1)  
73. What is prompt chaining? \- IBM, accessed on April 14, 2025, [https://www.ibm.com/think/topics/prompt-chaining](https://www.ibm.com/think/topics/prompt-chaining)  
74. What is Prompt Chaining? A Guide to Thinking With LLMs \- PromptLayer, accessed on April 14, 2025, [https://blog.promptlayer.com/what-is-prompt-chaining/](https://blog.promptlayer.com/what-is-prompt-chaining/)  
75. Prompt Chaining Tutorial: What Is Prompt Chaining and How to Use It? \- DataCamp, accessed on April 14, 2025, [https://www.datacamp.com/tutorial/prompt-chaining-llm](https://www.datacamp.com/tutorial/prompt-chaining-llm)  
76. What is prompt tuning? \- IBM Research, accessed on April 14, 2025, [https://research.ibm.com/blog/what-is-ai-prompt-tuning](https://research.ibm.com/blog/what-is-ai-prompt-tuning)  
77. ADEPT: Adapter-based Efficient Prompt Tuning Approach for Language Models \- ACL Anthology, accessed on April 14, 2025, [https://aclanthology.org/2023.sustainlp-1.8.pdf](https://aclanthology.org/2023.sustainlp-1.8.pdf)  
78. Use of adjectives in abstracts when reporting results of randomized, controlled trials from industry and academia \- PubMed, accessed on April 14, 2025, [https://pubmed.ncbi.nlm.nih.gov/25749803/](https://pubmed.ncbi.nlm.nih.gov/25749803/)  
79. Prompt Engineering a Prompt Engineer \- arXiv, accessed on April 14, 2025, [https://arxiv.org/html/2311.05661v3](https://arxiv.org/html/2311.05661v3)  
80. Enhancing LLM-Based Text Classification in Political Science: Automatic Prompt Optimization and Dynamic Exemplar Selection for Few-Shot Learning \- arXiv, accessed on April 14, 2025, [https://arxiv.org/html/2409.01466v2](https://arxiv.org/html/2409.01466v2)