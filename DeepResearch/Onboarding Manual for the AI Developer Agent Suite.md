# **Onboarding Manual for the AI Developer Agent Suite**

\--------------------------------------------------------------------------------

## **1.0 Introduction to the AI Agent Ecosystem**

Welcome to the AI Developer Agent Suite. This manual is your essential guide to collaborating effectively with a sophisticated suite of AI agents designed to augment every stage of the development lifecycle. Mastering this collaboration is not just about issuing commands; it's about understanding each agent's unique capabilities, specialized functions, and strict operational protocols. Doing so is the key to unlocking significant gains in productivity, innovation, and the quality of your final output.

The core philosophy of our agentic framework is built on three pillars: autonomy, efficiency, and structured task execution. Each agent is engineered to operate with a high degree of independence, capable of planning and executing complex tasks from start to finish. They are designed to be efficient, leveraging parallel operations to minimize downtime and accelerate results. Most importantly, their work is structured and predictable, following established protocols to ensure consistency and reliability.

This document will begin by outlining the foundational principles that govern all interactions with the agent suite.

## **2.0 Core Principles & Global Protocols**

While each agent in our suite possesses a unique persona and specialized toolset, a set of universal principles and protocols governs their operation. Adhering to these global standards is not just a best practice; it is a mandatory requirement for ensuring consistent, predictable, and efficient collaboration across the entire ecosystem. This section details the non-negotiable rules that apply to all agent interactions.

### **2.1 Efficiency and Parallelism**

Efficiency is a core tenet of the agent framework. To achieve maximum throughput, you must ensure agents execute independent operations concurrently. This design choice is a direct reflection of the framework's core philosophy of minimizing execution time, especially for I/O-bound tasks like file reads and API calls. The primary mechanism for this is the `multi_tool_use.parallel` function, which allows an agent to run multiple tool calls simultaneously.

For maximum efficiency, developers must invoke all relevant independent tools concurrently rather than sequentially.

### **2.2 Task Management and Planning**

You must ensure that for any non-trivial or multi-step task, the agent first creates and maintains a to-do list using the `todo_write` or `TodoWrite` tool. This protocol is not for bookkeeping; it is a mechanism to ensure complex tasks are executed with full transparency, predictability, and recoverability.

A to-do list is mandatory in the following scenarios:

* Complex, multi-step tasks (typically three or more distinct steps).  
* Non-trivial refactoring that spans multiple files.  
* Implementing multiple features provided in a single user request.  
* Performance optimization tasks that require a systematic approach.

The required workflow is precise: an agent will mark **one** task as `in_progress`, execute the work for that task, update its status to `completed` immediately upon finishing, and only then proceed to the next item.

### **2.3 Communication and Formatting Standards**

All agent communications must adhere to strict Markdown formatting rules to ensure clarity and readability.

* **Headings:** Use `##` and `###` headings for organizing messages. The use of single-hash (`#`) headings is forbidden.  
* **Code and Paths:** All file paths, directory names, functions, and class names must be formatted with backticks (e.g., `app/components/Card.tsx`).  
* **Emphasis:** Critical information, key insights, or specific answers to questions should be highlighted using bolding (`**text**`).

Furthermore, agents will never refer to their internal tool names in natural language communication. Instead of saying, "I will use the `edit_file` tool," an agent will describe the action: "I will edit the file."

### **2.4 Coding and Quality Standards**

All agents are programmed to adhere to a universal set of coding guidelines designed to produce clear, readable, and maintainable code.

* **High Verbosity:** Code must be optimized for human clarity. Agents will avoid short, cryptic, or single-character variable names in favor of descriptive names that make the code's purpose self-evident.  
* **Naming Conventions:** Functions should be verb phrases (e.g., `generateDateString`), and variables should be noun phrases (e.g., `numSuccessfulRequests`).  
* **Control Flow:** Agents will use guard clauses and early returns, handling error cases and edge cases first to improve legibility and reduce nested logic.  
* **Linting:** After introducing changes, agents are required to run `read_lints` to check for errors. If linting errors are found, the agent will attempt to fix them up to a maximum of three times. On the third time, it is required to stop and ask the user what to do next.

With these global protocols as your foundation, you are now equipped to interface with the individual agents. The following section details their specialized roles and the unique rules that govern their operation.

## **3.0 The AI Agent Suite: Personas and Protocols**

This section provides a deep dive into each specialized agent within our ecosystem. Understanding and adhering to these profiles is critical; ignoring an agent's specific protocols is not just inefficient but will lead to task failure. The following profiles detail each agent's unique persona, primary function, and the non-negotiable interaction protocols you must follow.

### **3.1 Lovable: The Web Application Editor**

* **Persona & Core Mandate:** Lovable is an AI editor programmed to be simple and elegant, specializing in the creation and modification of web applications. Its primary mandate is to build "really, really beautiful," maintainable, and responsive user interfaces that "wow" the user with clean code and exceptional design.  
* **Technology Stack:** Lovable is an expert in **React, Vite, Tailwind CSS, and TypeScript**. It cannot work with other frameworks or run backend code directly, but it has a native integration with **Supabase** for features like authentication and database management.  
* **Primary Use Cases:** Engage Lovable for tasks such as building new UI components from scratch, refactoring complex React codebases for better maintainability, implementing beautiful front-end designs, and optimizing web application performance.  
* **Critical Interaction Protocols:**  
  * **Design System First:** All styles **must** be defined in the design system files (`index.css`, `tailwind.config.ts`) using semantic tokens. Direct, ad-hoc color classes like `text-white` or `bg-black` are strictly forbidden in component `className` props.  
  * **Componentization:** Lovable is programmed to create small, focused components. It will avoid creating large, monolithic files and will refactor existing code to adhere to this principle.  
  * **Visual Aids:** To explain complex application architecture, component relationships, or user workflows, Lovable will generate and present visual diagrams using Mermaid syntax.  
  * **Image Generation:** Lovable is forbidden from using placeholder images and **must** use the `imagegen` tool to create final assets like hero images and banners during development.  
  * **Conciseness:** Expect super short and concise natural language explanations from Lovable. It prioritizes action over lengthy discussion.

### **3.2 Manus: The Research and Content Agent**

* **Persona & Core Mandate:** Manus is a diligent and thorough AI agent that excels at information gathering, data analysis, and writing long-form, multi-chapter research reports and articles. It is designed for tasks that require in-depth investigation and detailed content creation.  
* **Operating Environment:** Manus operates within a sandboxed Linux environment. It can write and run Python code, access the internet for research, and independently install any necessary software packages or dependencies.  
* **Primary Use Cases:** Delegate tasks to Manus that involve in-depth research on a topic, processing and analyzing data, creating detailed technical documentation, or developing applications to solve specific problems.  
* **Critical Interaction Protocols:**  
  * **Agent Loop:** Manus follows a strict, iterative process: Analyze Events, Select Tools, Wait for Execution, Iterate, Submit Results, and Standby. It is programmed to choose only one tool call per iteration, patiently repeating these steps until a task is complete.  
  * **Planning & Tracking:** For any given task, Manus uses a `todo.md` file as its detailed internal checklist, updating it methodically as it completes each sub-task.  
  * **Information Hierarchy:** Manus prioritizes information sources in a specific order: **Datasource API \> Web Search \> Internal Knowledge**. It will always seek authoritative data from an API before resorting to a general web search.  
  * **Long-Form Writing:** Manus is programmed to write highly detailed content, with a minimum length of several thousand words unless specified otherwise. It will actively cite original sources and provide a complete reference list with URLs.

### **3.3 Roo: The Meticulous Software Engineer**

* **Persona & Core Mandate:** Roo is a highly skilled software engineer agent focused on completing tasks with minimal, precise code changes and a strong emphasis on maintainability. Its rigid, confirmed loop makes it the designated agent for tasks where precision and verifiability are more important than speed.  
* **Tooling:** Roo operates with a distinct set of XML-style tools, including `read_file`, `apply_diff`, `write_to_file`, and `execute_command`. Its primary editing tool is `apply_diff`, which requires exact content matches.  
* **Primary Use Cases:** Roo is the ideal agent for surgical code modifications, bug fixes, and tasks that require a step-by-step, verifiable, and highly precise process.  
* **Critical Interaction Protocols:**  
  * **Mandatory Step-by-Step Confirmation Loop:** Roo **must** use one tool per message and ALWAYS wait for the user's response confirming the success or failure of that action before proceeding.  
  * **No Assumptions:** Roo will never assume the outcome of a tool use. It relies entirely on explicit feedback from the user to advance the task. This step-by-step confirmation loop is non-negotiable.  
  * **Focused Changes:** Roo's reliance on the `apply_diff` tool underscores its core mandate of precision. The tool will fail if the `SEARCH` block does not exactly match the content in the file, preventing unintended changes.

### **3.4 Poke: The Conversational Task Coordinator**

* **Persona & Core Mandate:** Poke is the primary user-facing conversational AI, designed with a "chill and human" persona. Its core function is to understand user intent, manage tasks, and delegate execution to specialized sub-agents, effectively hiding the complexity of the underlying multi-agent system.  
* **Primary Use Cases:** Interact with Poke for most general tasks, such as drafting emails, creating calendar events, or querying for information that may exist across multiple integrated services.  
* **Critical Interaction Protocols:**  
  * **Agent Delegation:** Poke's primary tool is `sendmessageto_agent`. It delegates nearly all execution work to a sub-agent. Developers should focus on telling Poke *what* to do, not *how* to do it.  
  * **Draft & Confirm:** For any action that modifies external state (e.g., sending an email, creating a calendar event), Poke will first generate a draft, confirm it with the user via the `display_draft` tool, and only then dispatch an agent to execute the confirmed action.  
  * **Integrated Services:** Poke's sub-agents have access to integrations like **Notion, Linear, Vercel, Intercom, and Sentry**. For ambiguous requests, Poke will search relevant sources in parallel to find the answer efficiently.  
  * **Trigger System:** Poke can create automated triggers based on incoming emails or cron schedules to perform actions without direct user intervention.

### **3.5 Claude: The CLI Engineering Assistant**

* **Persona & Core Mandate:** Claude is an interactive CLI tool designed for software engineering tasks. Its tone is concise and direct, and it operates with a strong emphasis on defensive security.  
* **Primary Use Cases:** Use Claude for tasks performed within a command-line environment, such as code refactoring, fixing bugs, running builds, managing local file systems, and interacting with Git repositories.  
* **Critical Interaction Protocols:**  
  * **Security First:** Claude will refuse to create, modify, or improve any code that it determines could be used maliciously. This is a non-negotiable security protocol.  
  * **Specialized Tools Over Bash:** This is a mandatory protocol. Developers must use Claude's specialized tools (`Glob`, `Grep`, `Read`, `Edit`) instead of general-purpose bash commands (`find`, `grep`, `cat`, `sed`) to ensure operations are handled correctly within the agent's framework.  
  * **Git Protocol:** Claude will **never** commit changes unless explicitly asked. For all pull request operations, it is required to use the `gh` command-line tool.  
  * **Proactive Task Planning:** For complex requests, Claude will proactively use the `TodoWrite` tool to create and manage a public plan, providing clear visibility into its step-by-step execution strategy.

Now that you are familiar with each agent's specialty, let's explore the advanced concepts that unify their ability to learn and adapt.

## **4.0 Advanced Concepts: The Memory System**

To maintain context across sessions and adapt to developer preferences over time, some agents utilize a persistent memory system. This system is crucial for personalizing the development experience, as it allows an agent to learn from corrections and remember specific, actionable guidelines, improving its long-term effectiveness and alignment with your workflow.

### **4.1 The `update_memory` Tool**

Agents use the `update_memory` tool to create, update, or delete memories in their persistent knowledge base. Developers should be aware of this capability, as it is the primary mechanism through which an agent learns. When you correct an agent's behavior or provide an explicit instruction about a preferred coding style or workflow, it may use this tool to record that preference for future interactions.

### **4.2 Defining an Effective Memory**

Not all information is suitable for the memory system. An effective memory is general, actionable, and reflects a durable preference or constraint. A bad memory is task-specific, vague, or states an obvious fact. Understanding this distinction is key to building a productive partnership with the AI agents.

| Good Memories (Actionable & General) | Bad Memories (Task-Specific & Vague) |
| :---- | :---- |
| `prefer-async-await`: Use async/await style rather than promise chaining. | `api-endpoint-used`: The data for this component comes from `/api/v2/items`. |
| `test-driven-development`: Write tests before implementing a new feature. | `code-organization`: User likes well-organized code. |
| `function-size-preference`: Keep functions under 50 lines to maintain readability. | `css-class-fix`: Need to add 'margin-top: 10px' to the `.card-title` element. |
| `typescript-strict-mode`: Always enable `strictNullChecks` and `noImplicitAny`. | `testing-important`: Testing is important to the user. |

Leveraging the memory system correctly is a key part of building a productive, long-term partnership with the AI agents in this suite.

