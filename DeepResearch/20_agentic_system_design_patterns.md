These are design patterns for agentic systems.

1. Prompt Chaining
| Component | Logic/Implementation |
|---|---|
| Orchestrator | Manages the sequence of sub-tasks. Defines the order (e.g., Step A \to Step B \to Step C). |
| Agent Module (Step N) | A focused LLM call with a simple, narrow prompt (e.g., "Extract key entities."). |
| Validator | A small function (or a separate LLM call) that checks the output of Step N against constraints (e.g., "Is the output valid JSON?" or "Did it contain PII?"). |
| Core Logic | Sequential execution with conditional progression: If the Validator fails, the Orchestrator stops the chain and reports the error; if successful, it passes the sanitized, validated output as the only context to the next Agent Module. |

2. Routing
| Component | Logic/Implementation |
|---|---|
| Router Agent | A dedicated LLM instance prompted to classify user intent into a fixed set of categories (e.g., [Sales_Query, Technical_Support, Billing_Inquiry]). |
| Confidence Score | The Router must output a confidence score (e.g., 0 to 1) for its classification. |
| Specialist Agents | Independent LLM or RAG systems highly optimized for a single topic. |
| Core Logic | Conditional Dispatch: If Confidence \ge 0.95, dispatch to Specialist Agent. If Confidence < 0.95, trigger a Clarification Prompt (e.g., "Are you asking about a new purchase or an existing one?"). Re-route based on the clarification. |

3. Parallelization
| Component | Logic/Implementation |
|---|---|
| Task Splitter | A function that divides a large input (e.g., a 100-page document or 1,000 URLs) into N equal, independent chunks. |
| Worker Agents (N) | Independent instances of the same Agent Module, each processing a single chunk simultaneously. |
| Aggregator | Collects the N outputs from the workers. |
| Core Logic | Normalization and Synthesis: The Aggregator must enforce a consistent output format (e.g., JSON list of summaries) and then synthesize the individual results into a single, cohesive final output. |

4. Reflection
| Component | Logic/Implementation |
|---|---|
| Generator Agent | Creates the initial output (Draft 1). |
| Critic Agent | A separate LLM instance that receives Draft 1 and a Rubric (a detailed set of quality standards, tone, and formatting rules). |
| Revision Loop | A counter for maximum reflection attempts (e.g., \text{Max\_Revisions} = 3). |
| Core Logic | Iterative Improvement: The Critic provides structured feedback to the Generator (e.g., "The tone is too casual. Rephrase paragraph 2."). The Generator rewrites based only on the feedback. Loop until the Critic's confidence in the output reaches a threshold or \text{Max\_Revisions} is hit. |

5. Tool Use
| Component | Logic/Implementation |
|---|---|
| Tool Selection LLM | LLM instance prompted with descriptions of available tools (e.g., search_engine(query), calculator(expression)). |
| Tool Execution Engine | A secure execution sandbox for calling external APIs/functions. |
| Observation Context | The result returned from the executed tool. |
| Core Logic | ReAct (Reasoning and Acting): The LLM must output a Thought, an Action (tool call), and a Final Answer. The Tool Execution Engine intercepts the Action, runs the function, and feeds the Observation Context back into the LLM prompt for the next turn. |

6. Planning
| Component | Logic/Implementation |
|---|---|
| Planner Agent | An LLM prompted with the Goal and a Step-by-Step Constraint (e.g., "Output a plan as a JSON dependency graph: \text{step\_name}: \text{prerequisites}"). |
| Executor Agent | Runs the individual steps defined by the Planner. |
| State Tracker | Monitors which steps are complete and which prerequisites have been met.|
| Core Logic | Dependency Graph Execution: The Planner generates the entire plan upfront. The Executor only runs a step if all of its prerequisites are marked as complete in the State Tracker. If a step fails, the Planner must be called again to generate an updated recovery plan. |

7. Multi-Agent Collaboration
| Component | Logic/Implementation |
|---|---|
| Manager Agent (Orchestrator) | Defines the overall goal, splits it into sub-goals, and assigns them to specialist agents. |
| Specialist Agents | Independent, single-purpose agents (e.g., Research Agent, Code Generation Agent). |
| Shared Scratchpad/Memory | A central location (e.g., a key-value store or document) where agents post their outputs and read the current state of the project. |
| Core Logic | Hierarchical Delegation: The Manager controls all state transitions and handoffs. Agents do not talk directly to each other; they only communicate with the Manager via the Shared Scratchpad. |

8. Memory Management
| Component | Logic/Implementation |
|---|---|
| Short-Term Memory (STM) | The current session's conversation history (last K turns). |
| Long-Term Memory (LTM) | A Vector Database containing embeddings of past knowledge, user preferences, or past sessions (episodic memory). |
| Context Summarizer | An agent that, at a predefined interval, summarizes the STM and stores the summary in the LTM. |
| Core Logic | Retrieval-Augmented Context: For every new prompt, a small query is run against the LTM/Vector DB to retrieve the N most relevant knowledge chunks. These chunks are prepended to the user's prompt before the STM, maximizing context relevance. |

9. Learning and Adaptation
| Component | Logic/Implementation |
|---|---|
| Feedback Collector | Gathers explicit user ratings (e.g., Thumbs Up/Down) or implicit signals (e.g., time spent reading). |
| Denoising Agent | A simple classifier that checks feedback for quality, malicious intent, or irrelevance (filtering out "noise"). |
| Policy Updater | Periodically adjusts the system prompts or few-shot examples based on the aggregated, validated positive feedback. |
| Core Logic | Validated Reinforcement: Only high-quality, positive signals that pass the Denoising Agent are used to subtly adjust the agent's behavior to prevent "model poisoning."|

10. Goal Setting and Monitoring
| Component | Logic/Implementation |
|---|---|
| Goal Definition | A well-defined, measurable objective (e.g., "Increase conversion rate by 10\%"). |
| Metric Tracker | Real-time monitoring of key metrics (KPIs) relevant to the goal. |
| Anomaly Detector | A component that flags if the agent's performance is significantly deviating from the target or a baseline. |
| Core Logic | Continuous Alignment: If the Anomaly Detector flags a deviation, the Agent uses its Planning pattern (or calls a human) to analyze why the goal is missed and propose corrective actions (e.g., "Run a new A/B test"). |

11. Exception Handling and Recovery
| Component | Logic/Implementation |
|---|---|
| Error Classifier | Logic that differentiates errors into Temporary (e.g., rate limits, network timeout) or Permanent (e.g., invalid schema, authentication failure). |
| Retry Policy | Configuration defining the Exponential Backoff strategy: Wait X seconds, then 2X, then 4X, up to a maximum number of retries (N). |
| Escalation Logic | If an error is classified as Permanent or exceeds the N retry limit, trigger an alert to a human or the Goal Setting Agent. |
| Core Logic | Triage and Self-Correction: Attempts to resolve temporary issues autonomously using the backoff strategy. Only externalizes control when the problem is determined to be persistent or systemic. |

12. Human in the Loop (HITL)
| Component | Logic/Implementation |
|---|---|
| Confidence Threshold | A pre-defined minimum confidence score (e.g., 0.7) for a decision. |
| Approval Queue/Interface | A web interface or messaging channel where the agent posts its proposed action, full context, and confidence score. |
| Decision Gates | Code that pauses execution and awaits one of three human signals: \text{Approve}, \text{Reject}, or \text{Edit/Take Over}. |
| Core Logic | Conditional Veto: If the agent's internal confidence is below the threshold, or if the task is intrinsically high-risk (e.g., processing a patient's PII), the Decision Gate is triggered, and execution halts until external approval is received. |

13. Knowledge Retrieval (RAG)
| Component | Logic/Implementation |
|---|---|
| Document Indexer | Processes raw data (PDFs, documents) and converts them into text chunks stored as vector embeddings in a Vector Database. |
| Retriever | Takes the user's prompt, converts it into an embedding, and queries the Vector DB to retrieve the K most semantically similar text chunks. |
| Generator LLM | Receives the user prompt AND the retrieved chunks as context. |
| Core Logic | Grounded Generation: The Generator is prompted to answer the user's question using only the provided context chunks and to cite its sources if possible, significantly reducing hallucinations. |

14. Inter-Agent Communication
| Component | Logic/Implementation |
|---|---|
| Communication Channel | A shared queue or message broker (e.g., Redis, Kafka) where agents can post structured messages. |
| Messaging Protocol | A defined JSON schema for messages (\text{Sender\_ID}, \text{Recipient\_ID}, \text{Topic}, \text{Payload}). |
| Turn-Taking Logic | Strict rules enforced to prevent infinite loops (e.g., Agent A cannot respond to Agent B's message on the same topic until Agent B has acknowledged it). |
| Core Logic | Structured Dialogue: Agents are programmed to listen to the channel for messages addressed to them and respond according to the protocol, ensuring orderly information exchange without centralized control. |

15. Resource-Aware Optimization
| Component | Logic/Implementation |
|---|---|
| Complexity Classifier | A small, fast LLM or heuristic function that analyzes the input length and subject matter (e.g., "Is this a simple summary or does it require multi-step math?"). |
| Model Router | A dispatch function that maps complexity scores to available models (e.g., Simple \to GPT-4o-mini; Complex \to GPT-4o). |
| Budget Monitor | Tracks API calls and token usage against a predefined cost ceiling. |
| Core Logic | Cost-Effective Dispatch: Routes the query to the cheapest model capable of maintaining the required quality level for that complexity. If the Budget Monitor flags an overuse, it might temporarily downgrade the Model Router's choice. |

16. Reasoning Techniques
| Component | Logic/Implementation |
|---|---|
| Initial Proposer | Generates an initial hypothesis or thought. |
| Reasoner Loop (e.g., CoT) | Prompts the LLM to output its Thought process before the Answer, allowing self-correction and external verification. |
| Tree Builder (e.g., ToT) | Generates multiple parallel reasoning paths (like branches on a tree). |
| Core Logic | Path Selection: For Tree of Thoughts, a separate Evaluator Agent ranks the quality/plausibility of each branch's conclusion, and the best path is selected as the final answer. |

17. Evaluation and Monitoring
| Component | Logic/Implementation |
|---|---|
| Golden Test Set | A static, manually verified set of challenging inputs and their expected perfect outputs. |
| Drift Detector | A system that periodically runs a portion of production queries against a baseline model and compares the output quality (using an LLM or metric) to detect performance degradation. |
| Quality Gate | A pre-deployment check that ensures the agent performs above a threshold (e.g., \ge 90\% accuracy) on the Golden Test Set. |
| Core Logic | Continuous Quality Assurance: Ensures that new data, model updates, or prompt changes do not cause "regressions" in quality, alerting engineers when the live model's performance significantly deviates from the benchmark. |

18. Guardrails and Safety Patterns
| Component | Logic/Implementation |
|---|---|
| Input Filter | A lightweight model or rule-based system that uses regex or PII detection APIs to scan and redact inputs before they hit the main agent. |
| Prompt Injection Classifier | A small LLM trained specifically to classify if an input is attempting to override the system prompt. |
| Output Moderator | Scans the final generated response for harmful, non-compliant, or profane content before it reaches the user. |
| Core Logic | Pre- and Post-Filtering: The system is protected on both ends. Malicious or sensitive content is blocked/redacted at the door (Input Filter) and inappropriate outputs are sanitized before delivery (Output Moderator). |

19. Prioritization
| Component | Logic/Implementation |
|---|---|
| Scoring Matrix | A function that assigns a score to each task based on weighted factors (e.g., Urgency \times 0.4, Business Value \times 0.3, Estimated Effort \times 0.3). |
| Priority Queue | A queue that dynamically sorts tasks based on the highest calculated score. |
| Re-Triage Trigger | Logic that recalculates the scores for all waiting tasks if a high-priority event (like an emergency system alert) occurs. |
| Core Logic | Dynamic Resource Allocation: The agent always picks the top item from the Priority Queue to work on, ensuring that resources are always dedicated to the highest-value, most urgent work first. |

20. Exploration and Discovery
| Component | Logic/Implementation |
|---|---|
| Initial Hypothesis Generator | An agent that creates a wide range of potential research questions or avenues based on a broad goal. |
| Explorer Agents | Multiple parallel agents tasked with researching different hypotheses using RAG and Tool Use. |
| Synthesis Agent | Aggregates the findings from the Explorer Agents, looking for patterns, conflicts, or promising leads. |
| Core Logic | Broad to Narrow Funnel: The agent starts with a very wide search (Exploration) and uses the Synthesis Agent to narrow the focus to a few high-signal avenues, which can then be fed back into the Planning or Reasoning patterns. |
