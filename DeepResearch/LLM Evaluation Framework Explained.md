

# **From Generalists to Specialists: An Analysis of the LMArena Expert and Occupational Categories**

## **Introduction: The Limitations of Static Benchmarks**

The rapid evolution of large language models (LLMs) has increasingly exposed the limitations of traditional, static evaluation benchmarks. Metrics such as MMLU, while foundational, are increasingly susceptible to test set leakage and overfitting.1 More critically, these static, often multiple-choice, benchmarks fail to capture model performance on real-world, open-ended use cases, nor can they be updated frequently enough to keep pace with the weekly cadence of new model releases.1

In response, platforms like Chatbot Arena (LMArena) have emerged, offering a dynamic, crowdsourced alternative.2 By pitting two anonymous models against each other and collecting human preference votes, LMArena provides a leaderboard based on a robust Elo rating system that reflects "in-the-wild" user preferences.4

However, as model capabilities converge, a "saturation" at the top of these general leaderboards has made it difficult to differentiate flagship models. To address this, LMArena has introduced a new evaluation framework designed to probe the "next frontier" of LLM performance: expert-level reasoning across diverse, economically valuable disciplines.5 This report provides a comprehensive analysis of this new framework, which comprises two key components: the **Arena Expert** leaderboard and the **Occupational Categories**. These new evaluations are built upon a scalable, automated tagging system that leverages organic user data, providing a dynamic and high-resolution alternative to manually curated benchmarks \[User Query\].

## **A Scalable Methodology: LLM-as-a-Tagger**

The foundation of this new evaluation system is a scalable, automated pipeline that classifies the millions of organic user prompts received by the platform.6 This avoids the prohibitive cost and time of manual human expert annotation.1 The methodology is bifurcated into two distinct tagging processes.

### **Arena Expert Tagging**

To identify prompts that require advanced reasoning, LMArena employs an "LLM-as-a-Tagger" approach.

* **Objective:** To identify prompts demonstrating "advanced reasoning and domain expertise".6  
* **Model:** DeepSeek-v3-0324 is used as the classification model.6  
* **Process:** The classification is made using *only the user prompt*, not the model's response. DeepSeek-v3-0324 is prompted (using a zero-shot, tuned system prompt) to infer whether the query itself exhibits the "reasoning or knowledge patterns characteristic of domain expertise".6

### **Occupational Category Tagging**

To measure performance across specific disciplines, a separate process tags prompts into 23 distinct fields of practice.6

* **Objective:** To group all prompts by subject matter, allowing for a granular analysis of model strengths.6  
* **Taxonomy:** The 23 categories are derived from the US Bureau of Labor Statistics’ Standard Occupational Classification (SOC), which was adapted to fit the distribution of tasks observed in the Arena data.6  
* **Model:** Gemini 2.5 Flash is used for this classification task.6  
* **Process:** This model solves a zero-shot, multi-class classification problem. Each prompt can be assigned zero, one, or multiple categories to accommodate the high volume of multidisciplinary prompts.6

In conjunction with this framework, a dataset of 5,000 expert-level conversations, complete with their occupational tags, has been released on Hugging Face (lmarena-ai/arena-expert-5k), providing a critical resource for further research.6

## **Defining "Expert": A Sharper Lens than "Hard"**

This new "Expert" category is a significant refinement of LMArena's previous "Arena Hard" filter. The two are related but distinct, capturing different aspects of prompt difficulty.

"Arena Hard" is a broad filter defined by seven criteria (e.g., problem-solving, complexity, domain knowledge) and includes approximately one-third of all prompts on the platform.1

"Arena Expert," by contrast, is a much sharper and more exclusive filter, identifying only **5.5%** of all prompts.6 While the majority of expert prompts (3.8%) are also "hard," the distinction is clarified by the provided examples 6:

* **Hard but not Expert:** Prompts like "Summarize the NIST Cybersecurity Framework (CSF) 2.0 for entry-level analysts" or "Compute start and end dates in Python" are complex, specific, and require domain knowledge, but they are ultimately procedural or summarization-based tasks.6  
* **Expert but not Hard:** Prompts like "Percolation / branching process problem in probability theory" or "Kakutani's fixed point theorem question" represent a different axis of difficulty.6 They demand deep, abstract, and specialized academic knowledge, a hallmark of true expert-level reasoning.

This sharper filter has proven highly effective at solving the problem of leaderboard saturation. By isolating the most challenging 5.5% of prompts, the "Expert" category increases the separation between top-tier models. The average score spread among the top 30 models is 56 on the "Overall" leaderboard, but this *widens to 84* on the "Expert" leaderboard, providing significantly enhanced "discriminative power".6

## **Alignment with Curated Benchmarks: Validating the Scalable Approach**

A key claim of the new framework is that this "noisy" (i.e., LLM-tagged) crowdsourced approach can serve as a scalable alternative to "high-quality curated benchmarks" \[User Query\]. The LMArena team validates this by comparing their findings to OpenAI's **GDPval**, a meticulously curated benchmark that uses expensive, balanced, expert annotations across professional domains.6

The methodologies are starkly different. GDPval relies on a small volume of high-cost, human-expert annotations, with data carefully balanced across categories. LMArena uses high-volume, automated LLM-tagging on crowdsourced data, reflecting the "natural frequencies" of user queries.6 The LMArena team concedes their automated tags are "less strict and more noisy".6

Despite these differences, the analysis reveals a **strong alignment** in model rankings. The LMArena Expert leaderboard (at the time of the blog's writing) was "largely consistent" with the rankings published by GDPval. Both frameworks identified Claude Opus 4.1, GPT 5 high, Gemini 2.5 Pro, Grok 4, and GPT 4o as the top-performing tier, in a similar order.6 This result is significant: it demonstrates that LLM-based tagging of large-scale organic data can successfully "approximate the discriminative power" of manually curated, expert-driven benchmarks, validating the LMArena approach as a far more scalable and continuously updatable evaluation paradigm.6

## **Analysis of the Arena Expert Leaderboard**

The live Arena Expert leaderboard provides a precise snapshot of model performance on this most difficult tranche of prompts. The data reveals a clear hierarchy, distinct from the general-purpose "Overall" leaderboard.

**Table 1: Arena Expert Leaderboard (Top 10 Models, as of Nov 6, 2025\)**

| Rank (UB) | Model | Score (Elo) | 95% CI (±) | Votes |
| :---- | :---- | :---- | :---- | :---- |
| 1 | claude-sonnet-4-5-20250929-thinking-32k | 1499 | ±25 | 581 |
| 1 | claude-opus-4-1-20250805-thinking-16k | 1485 | ±17 | 1,238 |
| 1 | gemini-2.5-pro | 1465 | ±12 | 3,174 |
| 1 | qwen3-max-preview | 1464 | ±18 | 1,109 |
| Source: 8 |  |  |  |  |

Note: Table truncated to the top 4 models with over 1,000 votes or a top-tier rank for clarity in analysis. Full Top 10 includes models from Qwen, OpenAI, and Google.8

Two key observations emerge from this data.

First, the leaderboard is dominated by Anthropic's "thinking" models, which (as of this data) hold the top two spots.8 This "thinking" suffix, which is noted to engage "high reasoning" parameters 6, provides a *disproportionate* advantage on "Expert" tasks.

Second, this ranking is distinct from the "Overall" (Default Text) leaderboard. On that general board, gemini-2.5-pro holds the \#1 rank (Elo: 1452), while the two "thinking" Claude models are tied just below it (Elo: 1448).9 The inversion of this ranking on the "Expert" leaderboard demonstrates that "expert reasoning" is a specialized capability. While gemini-2.5-pro may be the top-ranked *generalist*, Anthropic's models (when their high-reasoning mode is engaged) are the *dominant specialists* for expert-level tasks.8

## **Uncovering Specialist vs. Generalist Capabilities**

The introduction of 23 Occupational Categories provides an unprecedented, granular view of the LLM competitive landscape, allowing for the empirical identification of "specialist" and "generalist" models.

### **Prevalence and Shift in Occupational Focus**

Analysis of the prompt distribution reveals a dramatic shift in user needs when moving from "All Prompts" to "Expert Prompts." This data provides the first large-scale, empirical validation of what "advanced LLM use" truly entails in the wild.

**Table 2: Distribution Shift of Occupational Categories (All Prompts vs. Expert Prompts)**

| Occupational Category | Prevalence (All Prompts) | Prevalence (Expert Prompts) | Percentage Point Change |
| :---- | :---- | :---- | :---- |
| **Software and IT Services** | 27.8% | 40.1% | **\+12.3%** |
| **Mathematical** | 10.3% | 34.3% | **\+24.0%** |
| **Life, Physical, and Social Science** | 17.0% | 27.4% | **\+10.4%** |
| **Engineering (Non-Software)** | 5.2% | 12.1% | **\+6.9%** |
| **Writing, Literature, and Language** | 24.7% | 9.5% | **\-15.2%** |
| **Entertainment, Sports, and Media** | 16.4% | 6.7% | **\-9.7%** |
| Source: 6 |  |  |  |

The data is unambiguous. "Expert" use is overwhelmingly concentrated in analytical, technical, and STEM-focused domains. The "Mathematical" category's share *more than triples* (10.3% to 34.3%), while "Software" and "Science" also see massive gains. Concurrently, the largest *general-user* categories, "Writing" and "Entertainment," collapse in representation. This indicates that while general LLM use is dominated by creative and consumer-facing tasks, expert-level use is defined by complex, analytical problem-solving.

### **Identifying "Specialist" Models by Domain**

The new, dedicated occupational leaderboards reveal that model performance is not uniform across these domains. The analysis identifies clear "specialists" 7:

* **Software and Mathematical:** The **Claude family** of models is reportedly "dominant" in the "Software and IT Services" and "Mathematical" categories. This aligns with the "Expert" leaderboard findings and the nature of prompts shown in the Appendix (e.g., "Create an HTTPS proxy using only Python standard libraries," "Yoneda lemma and Cayley theorem").7  
* **Writing and Science:** **Gemini 2.5 Pro** "excels" in the "Writing, Literature, and Language" and "Life, Physical, and Social Science" categories.7  
* **Medicine:** **OpenAI models (GPT 4o, o3)** are reported to "score highly" in "Medicine and Healthcare," a category that includes prompts like "Seminar slide for final-year anesthesiology residents".6  
* **Gaps:** The analysis does not state a clear dominant model for other major categories, such as "Legal and Government" or "Engineering (Non-Software) and Architecture".6

### **Defining the "Top Generalist" Model**

Given these specializations, identifying the best "all-rounder" model is not straightforward. A model that dominates the "Software" category (40.1% of expert data) could win an aggregate score while being weak elsewhere.

To find the true "Top Generalist," the LMArena team "solved a reweighted Bradley-Terry regression" that gave **equal weight to each of the top eight occupational categories** (Software, Writing, Science, Entertainment, Business, Math, Legal, and Medicine).6 This prevents a model from winning simply by dominating the largest categories.

The results of this reweighted "Generalist" leaderboard are 6:

1. **Gemini 2.5 Pro** (Rating: 1450\)  
2. **Claude Opus 4.1** (Rating: 1445\)  
3. **o3-2025-04-16** (Rating: 1441\)  
4. **gpt-5-high** (Rating: 1440\)

This finding is particularly nuanced. Despite the Claude family's "dominance" in the two largest expert categories (Software and Math), it *loses* the balanced generalist crown to Gemini 2.5 Pro. This implies that Gemini's first-place performance in "Writing" and "Science," combined with sufficiently high (even if not winning) scores across all other domains, results in the highest *average* performance. This provides a clear, data-driven distinction: Claude Opus 4.1 is the dominant *specialist* for technical and analytical domains, while Gemini 2.5 Pro is the superior *generalist* across all major professional fields.

## **A Critical Assessment: Methodological Limitations and Systemic Biases**

While this new framework represents a significant advancement in LLM evaluation, its automated, crowdsourced methodology introduces critical limitations and potential systemic biases that must be considered when interpreting its results.

### **The "Noisy" Tagger and Recursive Bias**

The framework's entire "ground truth" is contingent on the outputs of its LLM taggers, DeepSeek-v3-0324 and Gemini 2.5 Flash.6 The LMArena team acknowledges these automated tags are "less strict and more noisy" than human expert classifications.6

This creates a "black box evaluating a black box" scenario. The "Expert" leaderboard is not *truly* measuring expert prompts; it is measuring what DeepSeek-v3-0324 *believes* an expert prompt looks like. The validity of the 23 occupational leaderboards is entirely dependent on the *unaudited classification biases* of Gemini 2.5 Flash. Any failure of these taggers to recognize, for example, expert-level philosophy prompts \[Appendix\] at the same rate as expert-level coding prompts would *systemically and silently* bias the dataset 6 and all resulting leaderboards.

### **The Paradox of the Unqualified Judge**

The most significant methodological flaw is a central contradiction: the framework filters for *expert-level questions* but continues to rely on *non-expert votes* to judge the *answers*.

This paradox was identified by the LMArena team as far back as 2023: "...for difficult questions, it is also very hard for regular Arena users to judge which LLM has generated a better answer \-- some domain-specific questions are considered very difficult, even for 99% of non-expert humans".10

The new "Expert" framework is *explicitly* designed to filter for these 99th-percentile prompts. The provided examples are definitive: a "regular Arena user" (i.e., the "diverse user base" 2) cannot be expected to factually adjudicate the relative correctness of two model-generated answers on \[Appendix\]:

* "Metaphysical implications and rationale of variable-domain semantics in modal logic"  
* "Compare dFORCE and nano-COP in splicing"  
* "Change of the hypostasis in Orthodox theology"

Because the system uses "Expert Prompts \+ Non-Expert Judges," the "Expert" leaderboard 8 is *not* measuring which model provided the most *factually accurate* expert answer.

### **Systemic Bias: Selecting for Plausibility Over Accuracy**

If non-expert judges cannot assess *correctness*, they must be judging based on *other proxies* for quality. This creates a powerful systemic selection pressure that may favor *plausibility* and *style* over *substance* and *accuracy*.

As noted in community critiques, "the average LLM user can no longer tell which model is better".11 When faced with two incomprehensible but highly technical answers, the user is likely to "rate better short and easy to understand answers... not really the most accurate... but the one that *sounds the best*".11

A non-expert must revert to "aesthetic" or stylistic proxies: Was the answer well-formatted? Was the language confident? Was it "easy to understand"? A model that provides an answer that is *more* complex, *more* nuanced, and *more* accurate—but *harder* to understand—risks being penalized by a non-expert judge as "verbose" or "confusing."

This suggests the LMArena "Expert" leaderboard may be *actively selecting against* true, nuanced expertise. It risks becoming a "Plausibility Leaderboard," where stylistic dominance is mistaken for factual correctness.

## **Strategic Implications and Future Outlook**

Despite these limitations, the LMArena Expert and Occupational framework provides invaluable, actionable data for three key stakeholders.

### **For AI Developers (R\&D)**

The "Expert" leaderboard 8 should be adopted as the new "gold standard" benchmark for SOTA capability, replacing the saturated "Overall" leaderboard. The granular "Occupational" leaderboards 7 function as a data-driven, competitive "to-do list" for R\&D. If a model lags the Claude family in the "Software" and "Mathematical" categories, this provides a clear mandate to improve performance in those specific, high-value domains.

### **For Enterprise Adopters (Procurement)**

Monolithic leaderboards are now obsolete for serious enterprise procurement. This framework enables "specialist procurement." The optimal model choice is now *domain-specific*:

* **Technical/Analytical Verticals** (e.g., Software Engineering, Finance, R\&D): Procurement should favor models that dominate the "Software" and "Mathematical" categories (e.g., the **Claude family**).7  
* **Research/Communication Verticals** (e.g., Legal, Media, Consulting, Life Sciences): Procurement should favor the "Top Generalist" model, which has a more balanced profile and excels in "Writing" and "Science" (e.g., **Gemini 2.5 Pro**).6  
* **Healthcare Verticals:** Procurement should prioritize models that demonstrate specific strength in the "Medicine and Healthcare" category (e.g., **OpenAI models**).6

### **For Researchers (Academia)**

The most valuable asset from this initiative may not be the leaderboards, but the **lmarena-ai/arena-expert-5k** dataset.6 This 5,000-conversation "goldmine" of real-world, occupationally-tagged expert prompts is a far more dynamic and representative dataset than static benchmarks like MT-Bench.12 This dataset should be used to:

1. Train next-generation, specialized "LLM-as-a-Judge" models.  
2. Build new, high-quality, non-static expert evaluation sets.  
3. Analyze the fundamental nature of human-AI expert interaction.

## **Conclusion: The Auto-Arena and the End of the Human Bottleneck**

LMArena's new framework has successfully solved two of the three major bottlenecks in LLM evaluation: it has *scalable prompt generation* (via crowdsourcing) and *scalable prompt tagging* (via LLM-as-a-Tagger).6

The final bottleneck is *scalable voting*. The system remains dependent on slow, expensive, and (as established in Section 7\) *unqualified* human voters.4

The clear next step, already being explored in the research community, is the "Auto-Arena".13 This concept proposes a fully automated framework where "LLM-powered agents" handle every step: an "LLM examiner" generates expert questions, and a "committee of LLM judges" collaborates to decide the winner.13

This automated future would solve the "Unqualified Judge" paradox; an expert LLM *could* theoretically evaluate answers about "Kakutani's fixed point theorem." However, it would *dangerously amplify* the "Recursive Bias" risk, fully enclosing the evaluation system in a recursive, self-referential loop of "AI judging AI." LMArena's hybrid "LLMs tag, Humans judge" framework is the most advanced and scalable evaluation system to date, but it is also the definitive penultimate step toward this fully-automated, and potentially fully-biased, future.

#### **Works cited**

1. From Live Data to High-Quality Benchmarks: The Arena-Hard Pipeline | LMSYS Org, accessed on November 9, 2025, [https://lmsys.org/blog/2024-04-19-arena-hard/](https://lmsys.org/blog/2024-04-19-arena-hard/)  
2. Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference \- arXiv, accessed on November 9, 2025, [https://arxiv.org/pdf/2403.04132](https://arxiv.org/pdf/2403.04132)  
3. Best LLM Leaderboard 2025 | Comprehensive Guide \- Dextra Labs, accessed on November 9, 2025, [https://dextralabs.com/blog/best-llm-leaderboard/](https://dextralabs.com/blog/best-llm-leaderboard/)  
4. Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings | LMSYS Org, accessed on November 9, 2025, [https://lmsys.org/blog/2023-05-03-arena/](https://lmsys.org/blog/2023-05-03-arena/)  
5. LMArena Blog, accessed on November 9, 2025, [https://news.lmarena.ai/](https://news.lmarena.ai/)  
6. Arena Expert and Occupational Categories \- LMArena Blog, accessed on November 9, 2025, [https://news.lmarena.ai/arena-expert/](https://news.lmarena.ai/arena-expert/)  
7. lmarena-ai/arena-expert-5k · Datasets at Hugging Face, accessed on November 9, 2025, [https://huggingface.co/datasets/lmarena-ai/arena-expert-5k](https://huggingface.co/datasets/lmarena-ai/arena-expert-5k)  
8. Text Arena | LMArena, accessed on November 9, 2025, [https://lmarena.ai/leaderboard/text/expert](https://lmarena.ai/leaderboard/text/expert)  
9. Overview Leaderboard | LMArena, accessed on November 9, 2025, [https://lmarena.ai/leaderboard](https://lmarena.ai/leaderboard)  
10. Chatbot Arena Leaderboard Updates (Week 4\) \- LMSYS Org, accessed on November 9, 2025, [https://lmsys.org/blog/2023-05-25-leaderboard/](https://lmsys.org/blog/2023-05-25-leaderboard/)  
11. The final straw for LMSYS : r/LocalLLaMA \- Reddit, accessed on November 9, 2025, [https://www.reddit.com/r/LocalLLaMA/comments/1ean2i6/the\_final\_straw\_for\_lmsys/](https://www.reddit.com/r/LocalLLaMA/comments/1ean2i6/the_final_straw_for_lmsys/)  
12. Chatbot Arena Conversation Dataset Release \- LMSYS Org, accessed on November 9, 2025, [https://lmsys.org/blog/2023-07-20-dataset/](https://lmsys.org/blog/2023-07-20-dataset/)  
13. Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions \- ACL Anthology, accessed on November 9, 2025, [https://aclanthology.org/2025.acl-long.223/](https://aclanthology.org/2025.acl-long.223/)  
14. AUTO-ARENA:AUTOMATING LLM EVALUATIONS WITH AGENT PEER BATTLES AND COMMITTEE DISCUSSIONS \- OpenReview, accessed on November 9, 2025, [https://openreview.net/pdf?id=pMp5njgeLx](https://openreview.net/pdf?id=pMp5njgeLx)  
15. \[2405.20267\] Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions \- arXiv, accessed on November 9, 2025, [https://arxiv.org/abs/2405.20267](https://arxiv.org/abs/2405.20267)