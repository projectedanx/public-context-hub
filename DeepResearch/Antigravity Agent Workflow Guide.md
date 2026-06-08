# **DRP-ANTIGRAVITY-WORKFLOW-ENGINEERING-2026: Antigravity Deep Guide & Novel Workflow Generation with Agent-First Development**

## **1\. The Agent-First Paradigm: Redefining Software Engineering**

The history of software development tools can be charted as a progression of increasing abstraction. We moved from punch cards to assembly, from assembly to high-level languages, and from text editors to Integrated Development Environments (IDEs) that offered syntax highlighting and intelligent completion. However, until late 2025, the fundamental interaction model remained unchanged: the human developer was the sole driver, manually inputting logic character by character, while the machine served as a passive assistant. The release of **Google Antigravity** marks a definitive phase transition in this history, introducing the era of **Agent-First Development**.1

Antigravity is not merely a feature update or an extension; it is a fundamental reimagining of the developer's cockpit. It presupposes that the Artificial Intelligence is no longer just a "copilot" that suggests lines of code, but an autonomous actor—a digital coworker capable of planning complex architectures, executing multi-file refactors, navigating the web to verify functionality, and iterating on its own work based on feedback.2 This shift requires a corresponding shift in the mental models of the developer, moving from a "writer of syntax" to an "architect of systems" and an "orchestrator of agents".1

### **1.1 The Core Philosophy: Trust, Autonomy, and Feedback**

The architecture of Antigravity is built upon three pillars designed to solve the primary friction points of agentic coding: the lack of visibility into the AI's reasoning, the inability of chat-based agents to perform end-to-end tasks, and the difficulty of steering an autonomous system.

**Trust via Artifacts** In traditional chat-based coding assistants, the AI outputs ephemeral blocks of code that vanish into the chat history. This lack of permanence makes it difficult to verify the AI's intent before it alters the codebase. Antigravity addresses this by treating the agent's thought process as a first-class citizen. Agents generate **Artifacts**—structured, persistent deliverables such as **Task Lists**, **Implementation Plans**, and **Walkthroughs**.2 These Artifacts serve a dual purpose: they allow the agent to organize its own reasoning, and they provide a surface for the human developer to audit the strategy before execution begins. By reviewing an Implementation Plan, a developer can catch architectural flaws early, turning the interaction from a "hope and pray" dynamic into a rigorous engineering review process.2

**Autonomy via the Three Surfaces**

The limitations of previous AI tools often stemmed from their isolation; a chatbot in a browser tab cannot run a terminal command or see a local file. Antigravity dissolves these boundaries by integrating three distinct surfaces into a single platform:

1. **The Agent Manager:** A dedicated mission control dashboard for spawning and orchestrating agents.1  
2. **The Editor:** A state-of-the-art code editing environment (based on a fork of VS Code) that allows for manual intervention and real-time observation of agent activity.7  
3. **The Browser Runtime:** A fully integrated, controllable Chrome instance that allows agents to deploy web applications locally, interact with the UI, and verify functionality exactly as a human user would.1

**Feedback as a Control Mechanism** The transition to autonomous agents introduces the risk of "runaway" processes where the AI deviates from the user's intent. Antigravity mitigates this through a tight feedback loop rooted in the Artifact system. Developers can leave Google Docs-style comments directly on an Implementation Plan or a Code Diff.6 The agent treats these comments as high-priority constraints, adjusting its plan and regenerating code to align with the feedback. This mechanism transforms the developer's role from writing code to steering the intelligence that writes the code.

## ---

**2\. Architecture and Mental Models**

To master Antigravity, one must understand the specific architectural components that drive its operation and the mental models required to utilize them effectively. The platform is not a single tool but a system of interacting parts designed to support the **Planner-Executor** workflow.

### **2.1 The Agent Manager: Mission Control for Code**

The Agent Manager is the primary interface for the "Agent-First" developer. Unlike the traditional file explorer which focuses on static assets, the Agent Manager focuses on *tasks* and *processes*. It provides a high-level view of what the agents are doing, their current status, and their generated artifacts.2

This surface enables **asynchronous development**. A developer can spawn multiple agents to work on parallel tracks—one agent refactoring a legacy module, another investigating a security vulnerability, and a third updating documentation—while the developer focuses on high-level architecture or code review.1 This capability effectively multiplies the developer's throughput, provided they can effectively manage the orchestration overhead.

### **2.2 Agent Modes: The Cognitive Throttle**

Antigravity exposes two distinct modes of operation for its agents, allowing the developer to trade off between speed and depth of reasoning. These modes—**Planning Mode** (often referred to as "Deep Think") and **Fast Mode**—represent the "cognitive throttle" of the system.4

| Feature | Planning Mode (Deep Think) | Fast Mode |
| :---- | :---- | :---- |
| **Primary Goal** | Architectural correctness, comprehensive understanding, risk mitigation. | Speed, immediate execution, low latency. |
| **Workflow** | Generates a "Task List" and "Implementation Plan" Artifact *before* writing any code. Recursively scans the codebase to build a dependency graph. | Skips the planning phase. Immediately executes commands or generates code. |
| **Best Use Case** | New feature implementation, complex refactoring, multi-file migrations, "greenfield" projects. | "Fix this typo," "Rename this variable," "Run the tests," simple single-file edits. |
| **Artifacts** | Heavily relies on Plan Artifacts for user approval. | Produces minimal artifacts; relies on direct Code Diffs. |
| **Token Cost** | High (due to extensive context gathering and reasoning steps). | Low (direct input-to-output generation). |

The **Planner-Executor** mental model suggests that complex tasks should always begin in Planning Mode to establish a robust strategy, while iterative refinements and minor bug fixes can be handled in Fast Mode to maintain velocity.4

### **2.3 The Artifact Lifecycle**

Artifacts are not static documents; they are dynamic objects that evolve throughout the task lifecycle. Understanding this lifecycle is key to effective collaboration with the agent.4

1. **Generation:** The agent analyzes the prompt and the codebase to generate an initial Artifact (e.g., an Implementation Plan).  
2. **Review & Annotation:** The developer reviews the Artifact. Using the commenting interface, they can flag specific sections—"This library is deprecated, use pydantic instead"—or approve the plan as is.2  
3. **Iteration:** The agent ingests the feedback, modifies the Artifact, and presents the revised version.  
4. **Execution:** Once approved, the Artifact becomes the "specification" for the agent's execution phase. The agent refers back to the Task List, checking off items as they are completed.  
5. **Verification:** Upon completion, the agent generates a "Walkthrough" Artifact, often containing screenshots or video recordings of the browser session, proving that the requirements have been met.6

### **2.4 The Browser Runtime: Closing the Loop**

The integration of a headless (or headed) Chrome browser is what allows Antigravity to perform **Closed-Loop Verification**. In a traditional workflow, an AI might generate code that looks correct but fails at runtime due to a UI logic error. In Antigravity, the agent can:

1. Write the code.  
2. Start the local development server (e.g., npm run dev).  
3. Launch the browser instance.  
4. Navigate to localhost:3000.  
5. Interact with the page (click buttons, fill forms).  
6. Analyze the visual output and console logs.  
7. **Self-Correct:** If an error occurs, the agent captures the stack trace, correlates it with the source code, and initiates a fix—all without human intervention.1

This capability transforms the agent from a code generator into a full-stack developer capable of QA and debugging.

## ---

**3\. The Antigravity Ecosystem: Setup and Configuration**

Before diving into complex workflows, it is essential to establish a properly configured environment. Antigravity operates as a local application with deep hooks into the operating system, requiring specific setup steps to ensure security and performance.

### **3.1 Installation and System Requirements**

Antigravity is built on a fork of VS Code, making the installation process familiar to most developers. However, because it runs local models and resource-intensive browser agents, the system requirements are higher than a standard text editor.8

* **macOS:** Requires Monterey (version 12\) or later. Optimization is heavily skewed towards Apple Silicon (M1/M2/M3/M4) due to the unified memory architecture required for efficient local inference.8  
* **Windows:** Requires a 64-bit version of Windows 10 or 11\. Installing on the primary system drive (C:) is recommended to avoid permission issues with terminal commands.8  
* **Linux:** Supports modern distributions like Ubuntu (20.04+), Debian (10+), and Fedora (36+), requiring glibc 2.28 or higher.8

**Initial Setup Flow:** Upon first launch, users are guided through a setup flow that allows for importing settings from existing VS Code or Cursor installations. This creates a seamless transition, preserving keybindings, themes, and extensions.4 Users must also sign in with a Google Account to authenticate and access the cloud-based model inference (Gemini 3 Pro).1

### **3.2 Autonomy Policies and Security**

Giving an AI agent access to the terminal and file system carries inherent risks. Antigravity mitigates this through configurable **Autonomy Policies** that define the boundaries of the agent's freedom.9

**Terminal Execution Policy:**

* **Off:** The agent can never execute terminal commands automatically. Every command requires explicit approval.  
* **Auto (Recommended):** The agent decides whether a command is safe. For benign commands like ls or grep, it proceeds. For potentially destructive commands (e.g., rm, git push), it pauses and requests user review.  
* **Turbo:** The agent acts with full autonomy, executing commands immediately. This is efficient but risky and should be used only in sandboxed environments or with trusted workflows.

**Global vs. Workspace Rules:**

Configuration is managed via Markdown files, following the "Configuration as Code" philosophy.

* **Global Rules (\~/.gemini/GEMINI.md):** Apply to every project on the machine. Useful for setting universal standards (e.g., "Always use strict type checking," "Never commit secrets").4  
* **Workspace Rules (.agent/rules/):** Specific to a single project. Useful for enforcing project-specific architecture patterns or linting rules.11

**Security Best Practices:**

To secure the agent environment, it is highly recommended to add specific rules to GEMINI.md:

1. **Strictly Disable Auto-Execute:** For sensitive environments.  
2. **Limit File Access:** Explicitly forbid access to system directories (e.g., /etc, \~/.ssh).  
3. **Confirm Dangerous Commands:** Require a specific warning prefix for destructive actions.10

## ---

**4\. Deep Dive: Agent Skills (The Knowledge Layer)**

While the underlying Large Language Model (LLM) possesses general knowledge of programming languages and libraries, it lacks the specific context of a developer's unique environment, proprietary tools, and organizational standards. **Skills** are the mechanism Antigravity uses to bridge this gap. A Skill is a modular, reusable package of knowledge and capabilities that an agent can "equip" dynamically to handle specific tasks.12

### **4.1 The Anatomy of a Skill**

Unlike a simple system prompt, a Skill is a structured directory containing metadata, instructions, and often executable scripts. This structure ensures portability and allows the agent to use tools deterministically.9

**Standard Directory Structure:**

my-skill/

├── SKILL.md \# The "Brain": Metadata and Instructions (Required)

├── scripts/ \# The "Hands": Executable scripts (Optional)

│ ├── run.py

│ └── util.sh

├── examples/ \# The "Context": Few-shot examples (Optional)

│ ├── input.json

│ └── output.py

└── resources/ \# The "Knowledge": Static templates/docs (Optional)

└── license\_header.txt

### **4.2 The SKILL.md File**

The SKILL.md file is the core interface between the agent's router and the skill's logic. It uses YAML frontmatter to define *when* the skill should be triggered and Markdown body to define *how* it should be executed.12

**Case Study: The postgres-migration-assistant Skill**

This skill is designed to handle database schema changes safely, enforcing a strict protocol that prevents raw SQL execution in favor of a migration framework.

## ---

**name: postgres-migration-assistant description: Use this skill when the user asks to create, update, or verify database schemas, or when a SQL migration is required. It ensures safe migration practices using Alembic.**

# **PostgreSQL Migration Assistant**

## **Goal**

To safely generate and apply SQL migrations using the project's specific Alembic setup, avoiding direct database manipulation.

## **Constraints**

* **NEVER** execute raw SQL directly in the terminal via psql.  
* **ALWAYS** create a migration file using the generation script.  
* **ALWAYS** verify the schema state before applying changes.

## **Instructions**

1. **Analyze**: Check the current SQLAlchemy model definitions in src/models/.  
2. **Generate**: Use the scripts/generate\_migration.py tool to create a new revision.  
   * Usage: python scripts/generate\_migration.py \--message "description of change"  
3. **Verify**: Read the content of the generated migration file. Ensure it accurately reflects the user's intent and does not drop tables unexpectedly.  
4. **Apply**: If the verification passes, run alembic upgrade head.

## **Scripts**

* scripts/generate\_migration.py: A wrapper around the alembic revision command that ensures correct environment variables are set.

**Key Analysis:**

* **Trigger Phrase (description):** The agent's router uses semantic similarity matching on this field. It must be precise and action-oriented ("Use this skill when...") to ensure the agent selects it correctly from the library of available skills.13  
* **Progressive Disclosure:** The detailed instructions in the Markdown body are *not* loaded into the agent's context window until the skill is activated. This keeps the context clean and focused, preventing "Tool Bloat" and reducing token costs.12  
* **Deterministic Execution:** By wrapping the Alembic command in a Python script (scripts/generate\_migration.py), the skill developer ensures that the command is run with the correct flags and environment variables every time, removing the variability of LLM-generated CLI commands.12

### **4.3 Skill Scopes and Locations**

Skills can be deployed at two different levels, allowing for a hierarchy of capabilities.9

1. **Workspace Scope (\<workspace-root\>/.agent/skills/):** These skills are specific to a single project. They are ideal for project-specific deployment scripts, database migration tools, or proprietary testing frameworks. They are checked into version control (Git) and shared with the entire team.  
2. **Global Scope (\~/.gemini/antigravity/skills/):** These skills are available across all projects on the user's machine. They are best suited for personal productivity tools, general-purpose git utilities, or "Personal Assistant" capabilities like a Pomodoro timer.13

### **4.4 The sickn33 Repository: A Standard Library**

The community has rapidly coalesced around shared skill libraries, most notably the sickn33/antigravity-awesome-skills repository, which aggregates over 200 battle-tested skills.16 This repository serves as a *de facto* standard library for Antigravity, offering skills for:

* **Security Auditing:** Skills like Ethical Hacking Methodology and Cross-Site Scripting Testing that guide agents through rigorous security checks.16  
* **DevOps:** Skills for Deployment Procedures and Docker management.16  
* **Development:** Skills for React Design Patterns, TDD Workflows, and File Organization.

Installing these skills is as simple as cloning the repository into the .agent/skills directory, instantly upgrading the agent's capabilities from a generalist coder to a specialized engineering team.17

## ---

**5\. Deep Dive: Workflows and Rules (The Procedural Layer)**

While Skills provide the *capabilities* (tools), **Workflows** and **Rules** provide the *procedure* (SOPs) and *governance* (laws). Understanding the distinction between these three primitives is vital for designing robust agentic systems.11

### **5.1 Rules: Passive Governance**

Rules are persistent constraints that the agent must always obey. They are "passive" because they do not require user invocation; they are injected into the system prompt and are always "on" (or triggered by context).11

**Syntax and Features:**

Rules are defined in Markdown files within .agent/rules/.

* **Triggering:** Rules can be set to trigger always, or only when specific files are edited using glob patterns.  
  * trigger: src/\*\*/\*.ts ensures that a TypeScript-specific rule is only active when the agent is working on TypeScript files.11  
* **Use Cases:** Enforcing coding standards (e.g., "Always use strict mode"), preventing dangerous actions (e.g., "Never hardcode secrets"), or enforcing architectural patterns (e.g., "Always use the Repository pattern for database access").18

### **5.2 Workflows: Active Orchestration**

Workflows are user-triggered sequences of instructions that guide the agent through a specific multi-step process. They are the "macros" of the agent world, invoked via slash commands (e.g., /release, /test).4

**Syntax (workflow.md):**

A workflow file defines a series of steps that the agent must execute sequentially.

## ---

**description: Run a comprehensive unit test generation and execution cycle.**

# **Unit Test Generation Workflow**

## **Step 1: Analysis**

* Analyze the file currently open in the editor.  
* Identify all public methods and classes.  
* Create a plan to test purely logic-based functions first.

## **Step 2: Generation**

* Create a new test file named tests/test\_{filename}.py.  
* Generate pytest test cases for each identified method, covering happy paths and edge cases.  
* **Constraint:** Ensure test function names follow the test\_\<method\>\_\<condition\> pattern.

## **Step 3: Execution**

* Run pytest tests/test\_{filename}.py.  
* If tests fail, analyze the failure, fix the **test code** (do not modify source code yet), and re-run.  
* Repeat until green.

## **Step 4: Report**

* Output a summary of the tests created and their pass/fail status.

**Execution:** To run this workflow, the developer types /unit-test (assuming the file is named unit-test.md) in the chat. The agent then takes over, executing the steps one by one.19 This ensures consistency in repetitive tasks and prevents the developer from having to type out long, complex prompts manually.

### **5.3 Workflows vs. Skills**

* **Workflow:** Linear, user-driven, procedural. Best for "Standard Operating Procedures" like deployment, release, or PR review.20  
* **Skill:** Dynamic, agent-driven, functional. Best for "Tools" that might be needed ad-hoc, like "Search documentation," "Query database," or "Check syntax".21

A powerful pattern is to have a **Workflow** that *calls* a **Skill**. For example, a /deploy workflow might include a step that says "Execute the deployment-safety-check Skill to verify the build before pushing".12

## ---

**6\. Connectivity and Integration: The Model Context Protocol (MCP)**

In a modern enterprise environment, code does not live in a vacuum; it interacts with databases, cloud services, and issue trackers. Antigravity utilizes the **Model Context Protocol (MCP)** to standardize these connections, effectively acting as a "USB-C for AI".22

### **6.1 Architecture of MCP**

MCP is an open protocol that standardizes how AI models interact with external data and tools. It consists of **MCP Clients** (like Antigravity) and **MCP Servers** (which expose data sources).

* **No Glue Code:** Developers do not need to write custom Python scripts to query a PostgreSQL database. They simply "plug in" the official PostgreSQL MCP Server.22  
* **Security:** MCP servers run locally or in controlled environments. Credentials are managed securely, and the agent accesses the *capabilities* of the tool (e.g., "list\_tables") without needing raw access to connection strings in the chat context.22

### **6.2 Configuring MCP in Antigravity**

Connections are managed via the mcp\_config.json file, accessible through the Agent Manager UI.23

**Example Configuration:**

JSON

{  
  "mcpServers": {  
    "postgres-prod": {  
      "command": "npx",  
      "args": \["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/db"\]  
    },  
    "github": {  
      "command": "npx",  
      "args": \["-y", "@modelcontextprotocol/server-github"\],  
      "env": {  
        "GITHUB\_TOKEN": "ghp\_..."  
      }  
    }  
  }  
}

Once configured, the agent gains new tools. It can now answer questions like "What is the schema of the users table?" or "Are there any open issues related to the login page?" by directly querying the database or GitHub API.24

## ---

**7\. Advanced Orchestration: The Swarm Protocol**

For complex, enterprise-grade tasks, a single agent context is often insufficient. The **Swarm Protocol** (pioneered in the study8677/antigravity-workspace-template repository) introduces a **Router-Worker** architecture for multi-agent orchestration, enabling true parallel development.25

### **7.1 The Router-Worker Pattern**

The core concept is to decompose a large "Mission" into smaller sub-tasks and route them to specialized agents.

* **The Orchestrator (swarm.py):** A master script that acts as the "Project Manager." It does not write code. It analyzes the user's high-level request, breaks it down into component tasks, and assigns them to workers.25  
* **Specialist Workers:** The swarm consists of pre-configured agents with specific roles:  
  * **Researcher:** Equipped with browser tools and documentation skills. Responsible for information gathering.  
  * **Coder:** Equipped with the file system and language-specific skills. Responsible for implementation.  
  * **Reviewer:** Equipped with linting and security audit skills. Responsible for QA.9

**Conceptual Logic (swarm.py):**

Python

\# Conceptual Synthesis of Swarm Logic  
class SwarmOrchestrator:  
    def execute(self, mission: str):  
        \# Phase 1: Planning  
        plan \= self.workers\["researcher"\].ask(f"Analyze: {mission}")  
          
        \# Phase 2: Execution (Parallel)  
        frontend\_task \= self.workers\["frontend\_coder"\].ask\_async(plan.frontend\_spec)  
        backend\_task \= self.workers\["backend\_coder"\].ask\_async(plan.backend\_spec)  
          
        \# Phase 3: Synthesis  
        results \= await asyncio.gather(frontend\_task, backend\_task)  
          
        \# Phase 4: Review  
        final\_review \= self.workers\["reviewer"\].ask(results)  
        return final\_review

### **7.2 "Loki Mode" and Autonomous Deployment**

The community has extended this pattern into "Loki Mode," a fully autonomous pipeline that takes a Product Requirement Document (PRD) and attempts to drive it all the way to production.26

1. **Product Agent:** Parses the request and generates a detailed PRD Artifact.  
2. **Architect Agent:** Converts the PRD into an Implementation Plan and Schema.  
3. **Swarm Execution:** Spawns concurrent Coder agents to build the frontend and backend in isolation.  
4. **Integrator Agent:** Merges the codebases, runs integration tests, and generates a final report.

This pattern demonstrates the potential of Antigravity to function not just as an IDE, but as an **Agent OS** for software generation.27

## ---

**8\. Tutorial: Building the Antigravity To-Do App**

This section provides a practical, step-by-step guide to building a functional web application using the Antigravity **Planner-Executor** workflow. We will build a "To-Do" list with a Python Flask backend and a persistent SQLite database.

### **Phase 1: Setup & Initialization**

1. **Initialize Workspace:** Open Antigravity and create a new folder: mkdir antigravity-todo. Open this folder as a workspace.  
2. **Configure Environment:** Ensure Python is installed.  
3. **Install Skills:** (Optional but recommended) Clone the sickn33 skills repo into .agent/skills to give the agent basic engineering capabilities.

### **Phase 2: The Planning Prompt (Deep Think)**

Select **Planning Mode** in the Agent Manager. This is crucial for establishing the architecture.4

**Prompt:**

"I want to build a robust To-Do list web application.

**Stack:** Python (Flask), SQLite, HTML/CSS (Tailwind via CDN).

**Features:** Add task, toggle completion, delete task, persist data.

**Constraint:** Use the Repository pattern for database access.

Please plan the architecture, file structure, and implementation steps."

**The Agent's Response (Artifacts):**

The agent will pause and generate two key artifacts:

1. **Task List:** A checklist of 5-7 steps (e.g., "Setup venv," "Create schema," "Implement Repository," "Create Routes," "Create Templates," "Test").  
2. **Implementation Plan:** A detailed document proposing the directory structure (src/models.py, src/app.py, templates/index.html) and the SQL schema (TodoItem table with id, title, done).

**User Action:** Review the Implementation Plan. If the schema looks correct, click **"Approve Plan"**.

### **Phase 3: Execution (The "Fast" Mode)**

Switch to **Fast Mode** to execute the plan efficiently.

**Command:** "Execute the approved plan. Start with the database setup."

* **Observation:** The agent will run terminal commands to create the virtual environment (python \-m venv venv) and install Flask. It will then create the models.py and repository.py files.  
* **Verification:** You can see the files appearing in the File Explorer.

**Command:** "Now implement the routes and the HTML template."

* **Observation:** The agent writes app.py and templates/index.html. It automatically includes the Tailwind CSS CDN link as requested.

### **Phase 4: Closed-Loop Verification**

**Command:** "Verify the application works."

* **Agent Action:** The agent starts the Flask server (python src/app.py). It then launches the **Browser Runtime** and navigates to http://127.0.0.1:5000.  
* **Autonomous QA:** The agent inputs "Test Task 1" into the input field and clicks "Add". It verifies that the task appears in the list. It clicks the "Done" checkbox and verifies the visual state change.  
* **Artifact:** The agent generates a **Walkthrough** artifact containing a recording or screenshots of this session, proving the app functions correctly.4

### **Phase 5: Iterative Refinement**

**User Feedback:** "The delete button is too small. Make it a red icon."

* **Agent Action:** The agent edits templates/index.html, applying Tailwind classes (text-red-500, hover:text-red-700). It creates a **Code Diff**.  
* **User Action:** Review the diff side-by-side with the original code. Accept the change.

## ---

**9\. Novel Workflow Generation: QA and Deployment**

To satisfy the request for novel workflows, we present two advanced pipelines: **Hyper-QA** and **Cloud Deployment**.

### **9.1 The "Hyper-QA" Pipeline**

This workflow combines static analysis, security auditing, and visual regression testing into a single command.

**Workflow Definition (.agent/workflows/hyper-qa.md):**

## ---

**description: Run a comprehensive QA suite including security, visual, and style checks.**

# **Hyper-QA Pipeline**

## **Step 1: Static Analysis (The "Linter" Agent)**

* **Action:** Activate the code-style-enforcer skill.  
* **Command:** Run flake8. and mypy..  
* **Logic:** If errors exist, attempt to **auto-fix** them. If unfixable, list them in a report and STOP.

## **Step 2: Security Audit (The "Hacker" Agent)**

* **Action:** Activate the security-audit skill.26  
* **Command:** Run safety check to scan requirements.txt for known vulnerabilities.  
* **Command:** Grep codebase for "TODO", "FIXME", and regex patterns for hardcoded secrets (API keys).  
* **Constraint:** If *High Severity* issues are found, HALT the workflow immediately.

## **Step 3: Visual Verification (The "User" Agent)**

* **Action:** Activate the browser-automation skill.  
* **Command:** Launch the application locally.  
* **Execution:**  
  1. Navigate to Home Page. Capture screenshot: artifacts/qa/home\_pre\_release.png.  
  2. Navigate to Login. Verify inputs exist.  
  3. Perform "Happy Path" login. Capture screenshot: artifacts/qa/dashboard\_load.png.

## **Step 4: Report Generation**

* **Action:** Compile all findings (Linter output, Security scan results, Screenshots) into a Markdown artifact: QA\_REPORT\_v{timestamp}.md.  
* **Output:** Present the report to the user for final sign-off.

### **9.2 The "Cloud Deployment" Workflow**

This workflow automates the deployment of the application to a cloud provider (e.g., Google Cloud Run or Netlify), utilizing the Deployment Procedures skill.16

**Workflow Definition (.agent/workflows/deploy-prod.md):**

## ---

**description: Deploy the application to production after passing QA.**

# **Production Deployment Protocol**

## **Step 1: Pre-flight QA**

* **Call Workflow:** /hyper-qa.  
* **Logic:** Only proceed if the QA report shows zero critical issues.

## **Step 2: Containerization (Docker Skill)**

* **Action:** Check for a Dockerfile. If missing, generate one optimized for Python/Flask.  
* **Action:** Build the container locally to verify integrity: docker build. \-t todo-app:latest.

## **Step 3: Cloud Deployment (Deployment Skill)**

* **Action:** Activate deployment-procedures skill.  
* **Command:** Use the gcloud CLI (via run\_command tool) to deploy to Cloud Run.  
  * gcloud run deploy todo-app \--source. \--region us-central1 \--allow-unauthenticated  
* **Constraint:** Ensure output logs are captured to artifacts/deploy/deploy\_logs.txt.

## **Step 4: Live Verification**

* **Action:** Extract the URL from the deployment logs.  
* **Action:** Use the **Browser Runtime** to visit the live Production URL.  
* **Verification:** Perform a "Smoke Test" (load page, check title).  
* **Artifact:** Generate RELEASE\_NOTES.md with the live URL and deployment timestamp.

## ---

**10\. Comparative Landscape: Antigravity vs. The Field**

The "Agentic IDE" market is rapidly evolving. It is crucial to understand how Antigravity compares to its primary competitors: **Cursor** and **Windsurf**.

| Feature | Google Antigravity | Cursor | Windsurf |
| :---- | :---- | :---- | :---- |
| **Core Philosophy** | **Agent-First:** The agent is the primary interface (Manager). You orchestrate tasks. 28 | **Code-First:** The editor is primary. AI is an autocomplete/chat "sidecar" that edits code. 29 | **Hybrid:** "Cascade" agent observes workflow and suggests changes. Focus on deep context. 30 |
| **Agent Autonomy** | **High:** Agents run asynchronously, control browser, have distinct "Planning" phase. | **Medium:** "Composer" mode allows multi-file edits, but requires constant user prompting. | **Medium-High:** Deep context awareness ("Flow") but less autonomous orchestration than AG. |
| **Interface** | **Three Surfaces:** Editor, Agent Manager, Browser. | **Single Surface:** Standard VS Code with Chat pane. | **Single Surface:** Standard VS Code with "Cascade" pane. |
| **Verification** | **Native Browser Runtime:** Agents can self-test via Chrome integration. 7 | **None:** User must manually run and verify apps. | **None:** User must manually run and verify apps. |
| **Extensibility** | **Skills & Workflows:** Structured, file-based extension system (SKILL.md). | **Rules:** .cursorrules file for system prompt context only. | **Context:** Strong RAG-based context, but less procedural extensibility. |
| **Deployment Readiness** | **Preview/Experimental:** Powerful but can be unstable. | **Production Ready:** Mature, stable, widely used. | **Production Ready:** Focus on enterprise stability. |
| **Best For...** | Architects, System Builders, Complex Refactoring, "Greenfield" projects. | "Vibe Coders," fast iteration, daily coding tasks. | Enterprise Monorepos, existing codebases requiring deep context. |

**Key Insight:** Cursor is the tool you use to *write* code faster. Antigravity is the tool you use to *delegate* the writing of code entirely.28

## ---

**11\. Operational Excellence and Governance**

Deploying autonomous agents in a production environment requires strict operational discipline to ensure security, cost control, and code quality.

### **11.1 Security Governance**

* **Sandboxing:** For Python execution, the default local subprocess model is risky. It is recommended to configure the **Docker Sandbox** (SANDBOX\_TYPE=docker) in mcp\_config.json. This ensures that any code the agent executes runs inside an isolated container, preventing accidental file system damage.25  
* **Secret Management:** Agents should never have access to raw .env files containing production secrets. Use the **Deny List** in GEMINI.md to block read access to \*\*/.env\*. Instead, secrets should be injected via environment variables in the terminal session where Antigravity is launched.10

### **11.2 Managing "Context Rot"**

As an agent session continues, its context window fills with logs, diffs, and chat history. This leads to "Context Rot," where the agent becomes confused or hallucinates.12

* **The Handoff Pattern:** Implement a /handoff workflow. This workflow instructs the agent to:  
  1. Summarize the current state and next steps into a STATUS.md file.  
  2. Clear its memory (simulated by the user starting a new chat).  
  3. Read STATUS.md to resume work. This effectively "garbage collects" the context window while preserving the mission state.31

### **11.3 Token Economics**

Agentic development is computationally expensive. A "Planning Mode" session can consume tens of thousands of tokens before writing a line of code.

* **Strategy:** Reserve **Planning Mode** for complex, ambiguous tasks (architecture, migrations). Use **Fast Mode** for deterministic tasks (linting, tests).  
* **Model Selection:** Antigravity supports model optionality. Use **Gemini 3 Pro** for deep integration and large context windows (2M+ tokens), but consider smaller, faster models for simple "Fast Mode" iterations if available.2

## ---

**12\. Conclusion**

Google Antigravity represents a seminal moment in the history of software engineering. By elevating the AI from a text predictor to a task orchestrator, it challenges the very definition of what it means to be a "developer." The skill set of the future engineer will shift from memorizing syntax to designing **Skills**, creating **Workflows**, and managing **Swarms** of autonomous agents.

The power of Antigravity lies not just in its models, but in its *system architecture*—the interplay of Artifacts for trust, Skills for specialization, and the Browser Runtime for verification. Mastery of these primitives allows a single developer to operate with the throughput of a small team, turning the IDE into a genuine force multiplier.

However, this power requires a disciplined approach. Without the mental models of the **Planner-Executor** and strict governance via **Rules**, an agentic system can easily become chaotic. By adopting the patterns and workflows outlined in this guide—from the basic To-Do app to the complex Hyper-QA pipeline—developers can harness this new gravity to build better software, faster, and with greater confidence than ever before.

#### **Works cited**

1. Antigravity IDE Hands-On: Google's Agent-First Future — Are we ready? \- Medium, accessed on January 23, 2026, [https://medium.com/@visrow/antigravity-ide-hands-on-googles-agent-first-future-are-we-ready-a6d991025082](https://medium.com/@visrow/antigravity-ide-hands-on-googles-agent-first-future-are-we-ready-a6d991025082)  
2. Build with Google Antigravity, our new agentic development platform, accessed on January 23, 2026, [https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/](https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/)  
3. Google Antigravity, accessed on January 23, 2026, [https://antigravity.google/](https://antigravity.google/)  
4. Getting Started with Google Antigravity, accessed on January 23, 2026, [https://codelabs.developers.google.com/getting-started-google-antigravity](https://codelabs.developers.google.com/getting-started-google-antigravity)  
5. Coding Without Gravity: A Deep Dive into Google’s Antigravity Agent-First Development Platform, accessed on January 23, 2026, [https://medium.com/@vignarajj/coding-without-gravity-a-deep-dive-into-googles-antigravity-agent-first-development-platform-3b02eb1e69fd](https://medium.com/@vignarajj/coding-without-gravity-a-deep-dive-into-googles-antigravity-agent-first-development-platform-3b02eb1e69fd)  
6. Artifacts \- Google Antigravity Documentation, accessed on January 23, 2026, [https://antigravity.google/docs/artifacts](https://antigravity.google/docs/artifacts)  
7. How to Set Up and Use Google Antigravity \- Codecademy, accessed on January 23, 2026, [https://www.codecademy.com/article/how-to-set-up-and-use-google-antigravity](https://www.codecademy.com/article/how-to-set-up-and-use-google-antigravity)  
8. Google Antigravity: AI-First Development with This New IDE \- KDnuggets, accessed on January 23, 2026, [https://www.kdnuggets.com/google-antigravity-ai-first-development-with-this-new-ide](https://www.kdnuggets.com/google-antigravity-ai-first-development-with-this-new-ide)  
9. Tutorial : Getting Started with Google Antigravity | by Romin Irani \- Medium, accessed on January 23, 2026, [https://medium.com/google-cloud/tutorial-getting-started-with-google-antigravity-b5cc74c103c2](https://medium.com/google-cloud/tutorial-getting-started-with-google-antigravity-b5cc74c103c2)  
10. Antigravity's GEMINI.md File : r/GoogleAntigravityIDE \- Reddit, accessed on January 23, 2026, [https://www.reddit.com/r/GoogleAntigravityIDE/comments/1pgf6dt/antigravitys\_geminimd\_file/](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1pgf6dt/antigravitys_geminimd_file/)  
11. Rules / Workflows \- Google Antigravity Documentation, accessed on January 23, 2026, [https://antigravity.google/docs/rules-workflows](https://antigravity.google/docs/rules-workflows)  
12. Tutorial : Getting Started with Google Antigravity Skills, accessed on January 23, 2026, [https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d](https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d)  
13. Agent Skills \- Google Antigravity Documentation, accessed on January 23, 2026, [https://antigravity.google/docs/skills](https://antigravity.google/docs/skills)  
14. Authoring Google Antigravity Skills, accessed on January 23, 2026, [https://codelabs.developers.google.com/getting-started-with-antigravity-skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)  
15. Google Antigravity Tutorial for Beginners: Build Your First App (Step-by-Step), accessed on January 23, 2026, [https://www.youtube.com/watch?v=-0Irz8G0PEE](https://www.youtube.com/watch?v=-0Irz8G0PEE)  
16. sickn33/antigravity-awesome-skills: The Ultimate Collection of 200+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel. \- GitHub, accessed on January 23, 2026, [https://github.com/sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills)  
17. AI Agent Skills: Complete Tutorials, Implementation Guide, and Best Practices for 2026, accessed on January 23, 2026, [https://medium.com/@gemQueenx/ai-agent-skills-complete-tutorials-implementation-guide-and-best-practices-for-2026-860e1ee9b7b8](https://medium.com/@gemQueenx/ai-agent-skills-complete-tutorials-implementation-guide-and-best-practices-for-2026-860e1ee9b7b8)  
18. The Future of Coding? I Tested Google Gemini 3 and Its Antigravity IDE and Here's What Blew My Mind | by Sanjay Nelagadde | Write A Catalyst \- Medium, accessed on January 23, 2026, [https://medium.com/write-a-catalyst/the-future-of-coding-i-tested-google-gemini-3-and-its-antigravity-ide-and-heres-what-blew-my-mind-33a70011259c](https://medium.com/write-a-catalyst/the-future-of-coding-i-tested-google-gemini-3-and-its-antigravity-ide-and-heres-what-blew-my-mind-33a70011259c)  
19. Customize Google Antigravity with rules and workflows \- Mete Atamel, accessed on January 23, 2026, [https://atamel.dev/posts/2025/11-25\_customize\_antigravity\_rules\_workflows/](https://atamel.dev/posts/2025/11-25_customize_antigravity_rules_workflows/)  
20. New: Skills : r/google\_antigravity \- Reddit, accessed on January 23, 2026, [https://www.reddit.com/r/google\_antigravity/comments/1qcawsb/new\_skills/](https://www.reddit.com/r/google_antigravity/comments/1qcawsb/new_skills/)  
21. rule vs skills : r/google\_antigravity \- Reddit, accessed on January 23, 2026, [https://www.reddit.com/r/google\_antigravity/comments/1qgkfln/rule\_vs\_skills/](https://www.reddit.com/r/google_antigravity/comments/1qgkfln/rule_vs_skills/)  
22. Connect Google Antigravity IDE to Google's Data Cloud services | Google Cloud Blog, accessed on January 23, 2026, [https://cloud.google.com/blog/products/data-analytics/connect-google-antigravity-ide-to-googles-data-cloud-services](https://cloud.google.com/blog/products/data-analytics/connect-google-antigravity-ide-to-googles-data-cloud-services)  
23. Antigravity Editor: MCP Integration, accessed on January 23, 2026, [https://antigravity.google/docs/mcp](https://antigravity.google/docs/mcp)  
24. 🚀 The Modern Developer’s Blueprint: Integrating Documentation-Aware Agents in Google Antigravity, accessed on January 23, 2026, [https://medium.com/google-cloud/the-modern-developers-blueprint-integrating-documentation-aware-agents-in-google-antigravity-016b87327867](https://medium.com/google-cloud/the-modern-developers-blueprint-integrating-documentation-aware-agents-in-google-antigravity-016b87327867)  
25. study8677/antigravity-workspace-template: The ultimate starter kit for Google Antigravity IDE. Optimized for Gemini 3 Agentic Workflows, "Deep Think" mode, and auto-configuring .cursorrules. \- GitHub, accessed on January 23, 2026, [https://github.com/study8677/antigravity-workspace-template](https://github.com/study8677/antigravity-workspace-template)  
26. Antigravity \- Reddit, accessed on January 23, 2026, [https://www.reddit.com/r/google\_antigravity/](https://www.reddit.com/r/google_antigravity/)  
27. 06T/CursorSetup: Default Cursor Setup Fork \- GitHub, accessed on January 23, 2026, [https://github.com/06T/CursorSetup](https://github.com/06T/CursorSetup)  
28. Cursor vs Google AntiGravity : Best AI IDE for Vibe Coders? | by Mehul Gupta \- Medium, accessed on January 23, 2026, [https://medium.com/data-science-in-your-pocket/cursor-vs-google-antigravity-best-ai-ide-for-vibe-coders-f3ecbd02f161](https://medium.com/data-science-in-your-pocket/cursor-vs-google-antigravity-best-ai-ide-for-vibe-coders-f3ecbd02f161)  
29. Cursor vs Google Antigravity: Which Fits Your Enterprise Team's Reality? | Augment Code, accessed on January 23, 2026, [https://www.augmentcode.com/tools/cursor-vs-google-antigravity](https://www.augmentcode.com/tools/cursor-vs-google-antigravity)  
30. Agentic IDE Comparison: Cursor vs Windsurf vs Antigravity | Codecademy, accessed on January 23, 2026, [https://www.codecademy.com/article/agentic-ide-comparison-cursor-vs-windsurf-vs-antigravity](https://www.codecademy.com/article/agentic-ide-comparison-cursor-vs-windsurf-vs-antigravity)  
31. jerrygoha/dotfiles-for-antigravity \- GitHub, accessed on January 23, 2026, [https://github.com/jerrygoha/dotfiles-for-antigravity](https://github.com/jerrygoha/dotfiles-for-antigravity)