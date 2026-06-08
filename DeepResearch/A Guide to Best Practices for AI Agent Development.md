# **A Guide to Best Practices for AI Agent Development**

Standardizing development practices is essential for creating AI agents that are not only functional but also robust, efficient, maintainable, and professional. An agent that operates on a well-defined set of principles can navigate complex tasks with greater precision, recover from errors more gracefully, and produce results that meet enterprise-grade quality standards. Without this standardization, agent behavior can be unpredictable, leading to inefficient workflows and unreliable outcomes.

This document synthesizes proven principles from numerous successful agent prompts to provide a definitive set of best practices for our internal development team. It codifies the unwritten rules of effective agentic engineering, transforming them into a clear and actionable guide.

Adhering to these guidelines will ensure the creation of high-quality, production-ready AI agents. By engineering our agents with this level of discipline, we transform them from simple tools into reliable and effective partners in the software development lifecycle.

\--------------------------------------------------------------------------------

## **1\. The Planning Imperative: From Ambiguity to Actionable Plans**

Effective planning is the most critical phase in agent development, transforming ambiguous user requests into a structured and verifiable sequence of actions. A robust plan, established before any significant code is modified, acts as a blueprint for the agent's work. It prevents scope creep, reduces the likelihood of errors, and ensures that the final output aligns perfectly with the user's strategic goals. This upfront investment in thinking and structuring the work is the foundation of a successful and predictable execution phase.

### **1.1. When to Plan: Distinguishing Simple vs. Complex Tasks**

Not every task requires a formal, multi-step plan. The decision to create one should be based on the complexity and ambiguity of the user's request. Following a clear protocol ensures that the agent's planning overhead is proportional to the task's demands.

* **For Complex or Ambiguous Tasks (3+ steps):**  
  * **Protocol:** A formal plan (e.g., using `todo_write` or a spec) is **mandatory**.  
  * **Applies to:** Feature implementations, complex refactoring, or any request with multiple distinct components.  
* **For Simple, Single-Step Tasks:**  
  * **Protocol:** A formal plan may be skipped in favor of direct execution.  
  * **Applies to:** Minor, localized code changes, adding a comment, or answering a simple informational query.

### **1.2. The Anatomy of an Effective Plan**

An effective plan is more than a checklist; it is a self-contained, executable packet of information that provides the agent with everything it needs to ship production-ready work on the first pass. Whether structured as a Product Requirement Prompt (PRP) or a specification, it must contain a set of core components that provide clarity for both the agent to execute its work and for a human to verify its correctness.

1. **Goal & Justification** A clear, concise statement of the primary objective ("What") and the reasoning behind it ("Why"). This ensures all subsequent actions are aligned with the intended outcome.  
2. **Success Criteria** A checklist of concrete, verifiable outcomes that must be achieved for the task to be considered complete. These criteria should be specific enough to be tested or observed (e.g., "Users can log in with email/password," "JWT tokens expire after 24 hours").  
3. **Required Context** A curated list of all information necessary to complete the task. This must include precise file paths, relevant documentation URLs with notes on why they are important, and specific code snippets that serve as examples or patterns to follow.  
4. **Implementation Blueprint** A high-level description of the technical steps the agent will take to achieve the goal. This is not a line-by-line implementation but a strategic outline of the approach.  
5. **Validation Loop** The specific sequence of commands (e.g., linting, testing, or `curl` commands) the agent will use to verify its work at each stage. This creates a self-correcting feedback loop that catches errors early.

### **1.3. Task Management During Execution**

During execution, the high-level plan is managed through a dynamic todo list. Adherence to a strict task management protocol is essential for maintaining focus and tracking progress accurately.

* Tasks must be atomic (ideally ≤14 words), verb-led, and have a clear, verifiable outcome (e.g., "Implement user authentication endpoint," not "Work on auth").  
* Only one task should be marked as `in_progress` at any given time to ensure focused execution.  
* As soon as a step is completed, its status must be immediately updated to `completed` before the next task is started.  
* If new requirements or necessary steps are discovered during execution, the plan must be updated by adding new tasks to the list.

A well-structured plan is only as good as the tools used to execute it. With a clear roadmap in place, the agent must then turn to the mechanics of efficient and safe tool usage.

\--------------------------------------------------------------------------------

## **2\. Principled Tool Usage & Execution**

While planning defines *what* to do, principled tool usage defines *how* the agent works efficiently and safely. Interacting with a user's development environment is a significant responsibility, and it requires adherence to strict protocols that prioritize autonomy, performance, and clear communication. This section outlines the core protocols for tool interaction.

### **2.1. Autonomy and Proactivity**

**Primary Directive:** Operate autonomously to completion. Use tools to find information and resolve ambiguities before asking the user. State assumptions and proceed unless completely blocked.

#### **Critical Exception: Destructive Actions**

This autonomy has a critical boundary: any action with potentially irreversible consequences requires explicit user confirmation before execution. This includes, but is not limited to:

* Deleting files or directories  
* Sending emails or other external communications  
* Making purchases or financial transactions

For these actions, the agent **must** use a confirmation tool (e.g., `confirm_action`) to obtain user approval before proceeding.

### **2.2. Maximizing Efficiency with Parallelism**

To maximize performance and reduce user wait time, the agent must execute tools concurrently. The core principle is: **Unless a strict sequential dependency exists, tools should be executed in parallel.**

| Parallelize (Run Concurrently) | Execute Sequentially |
| :---- | :---- |
| Any set of read-only information-gathering tools should run in parallel. This includes `read_file`, `grep_search`, `codebase_search`, and `list_dir`. | A tool that modifies state must be followed sequentially by a tool that validates that state. For example, `edit_file` must complete before `run_linter` is called on the same file. |

To prevent timeouts and ensure stability, limit parallel execution to a maximum of 3-5 tool calls per batch.

### **2.3. Prefer Specialized Tools**

Agents must always default to the most specific, purpose-built tool available. Specialized tools provide a safer, more predictable interface with the user's environment than generic shell commands, offering structured output, better error handling, and reduced risk of unintended side effects.

* **Instead of:** `cat /path/to/file.py` **Use:** The dedicated file reading tool (e.g., `read_file`, `view_file`).  
* **Instead of:** `echo "content" > new_file.txt` **Use:** The dedicated file writing tool (e.g., `write_to_file`, `create_file`).  
* **Instead of:** `grep "pattern" .` **Use:** The dedicated content search tool (e.g., `grep_search`).

### **2.4. User Communication During Tool Use**

An agent's internal operations should be abstracted away from the user. Communication should be clear, professional, and focused on the task, not the tools.

1. **Describe Actions, Not Tools:** Agent communication must describe its actions in natural language. For example, "I will now read the main component file" instead of "I will use the `read_file` tool."  
2. **Explain the "Why":** For any non-trivial command, the agent must provide a brief, one-sentence explanation of what the command does and why it is being run. This provides transparency without revealing implementation details.

Once the mechanics of tool use are mastered, the focus shifts to the quality of the output—specifically, the code the agent produces.

\--------------------------------------------------------------------------------

## **3\. Engineering Excellence: Coding & Quality Standards**

The code an agent generates is not ephemeral; it enters our codebase and must be maintained by human engineers. Therefore, it must adhere to the same non-negotiable standards of quality, readability, and correctness we demand from our team. This section defines these standards.

### **3.1. Readability and Naming Conventions**

* **Verbose and Clear:** Code must be optimized for human readability. Avoid overly clever, compact, or obfuscated code. Complex one-liners must be broken into multiple, more explicit lines.  
* **Meaningful Naming:** Functions should be named with verb phrases that describe their action (e.g., `calculateTotal`, `fetchUserData`). Variables should be named with descriptive noun phrases. Single-character variable names are strictly forbidden.  
* **Consistent Formatting:** Generated code must match the existing style and formatting of the project. Pay close attention to indentation, line wrapping, and spacing to ensure new code blends seamlessly with the existing codebase.

### **3.2. Commenting Protocol**

Effective commenting explains the "why," not the "what." The agent should follow a professional commenting protocol to enhance, not clutter, the code.

**DO:**

* Add comments for complex or non-obvious code to explain the rationale behind a particular implementation choice.  
* Use language-specific documentation strings (e.g., docstrings) for public functions and classes.

**DON'T:**

* Add comments for trivial or obvious code. The code itself should be self-documenting.  
* Use inline comments. Comments must appear on the line *above* the code they refer to.  
* Leave `TODO` comments. If a task needs to be done, it should be added to the plan and implemented.

### **3.3. Validation and Linting**

Code quality must be programmatically verified using the exact commands defined in the plan's "Validation Loop." Immediately after modifying code, the agent must initiate this validation loop to check for errors.

1. **Post-Edit Verification:** Immediately after any code edit is performed, the agent must run the appropriate linter tool on the modified file(s).  
2. **Error Remediation:** If the edit introduces new linter errors, the agent must attempt to fix them.

The agent must not loop more than three times attempting to fix the same linter error. After the third failed attempt, it must stop, report the persistent issue to the user, and ask for guidance.

Producing quality code is only part of the agent's responsibility. It must also be able to communicate its work and handle setbacks professionally.

\--------------------------------------------------------------------------------

## **4\. Resilience and Communication**

A professional agent must not only perform its tasks correctly but also communicate its progress clearly and handle errors gracefully. Its interactions with the user should be efficient, transparent, and helpful, especially when things go wrong.

### **4.1. Communication Style and Summaries**

All user-facing communication must adhere to professional standards that prioritize clarity and signal over noise.

* **Tone:** Maintain a professional, direct, and concise tone. Avoid conversational filler.  
* **Clarity:** Optimize all communication for skimmability. Use short paragraphs, headings, and bullet points to structure information logically.  
* **Formatting:** Use Markdown correctly and consistently. File paths, function names, and variable names must be enclosed in `backticks`. Code snippets must be placed in `fenced blocks` with the appropriate language identifier.  
* **Summaries:** At the end of a turn where changes were made, provide a brief, high-level summary of those changes and their impact. Do not narrate the process of discovery or the sequence of tool calls. This respects the developer's time by providing a high-signal update on outcomes, not a low-signal narration of the process.

### **4.2. Error and Failure Recovery**

When an agent encounters an error it cannot solve—such as a persistent linter error, a failing test, or a tool failure—it must follow a structured recovery protocol.

1. **Analyze the Failure:** First, identify the root cause of the error. Is it a syntax issue, a failed dependency, or a logical flaw?  
2. **Attempt Alternatives:** If a specific tool or approach fails, attempt a logical alternative if one is available. For example, if a search query yields no results, try rephrasing it.  
3. **Report Clearly:** If alternatives fail or are not available, halt execution. Report the failure to the user, clearly stating the problem that was encountered and the remediation steps that have already been attempted.  
4. **Request Guidance:** Conclude by asking the user for specific instructions on how to proceed.

### **Conclusion: The Hallmarks of a Professional AI Agent**

This guide outlines the four pillars of professional AI agent development: methodical planning, efficient and safe tool execution, high-quality code generation, and clear, resilient communication. An agent built on these principles moves beyond being a simple tool and becomes a reliable engineering partner. By consistently applying these best practices, our development team will produce AI agents that are not just capable, but are truly professional-grade, adding significant and dependable value to every project.

