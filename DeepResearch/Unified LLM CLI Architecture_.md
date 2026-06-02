# **U-CLI: Architectural Specification for a Unified, Auditable LLM Command-Line Framework**

## **Introduction \- The Strategic Imperative for a Unified LLM Interface**

The proliferation of Large Language Models (LLMs) has introduced a new class of developer tooling: the agentic command-line interface (CLI). Major providers, including OpenAI, Google, and Anthropic, have released powerful CLIs that allow developers to interact with their models directly from the terminal, performing complex tasks like code generation, debugging, and repository analysis.1 While powerful, this rapid, parallel evolution has resulted in a fragmented and inefficient developer experience.

### **The Fragmentation of Agentic CLIs**

Developers seeking to leverage the best model for a given task are currently faced with a disjointed ecosystem. Each provider offers a distinct CLI with its own installation method, authentication flow, command syntax, and unique feature set.

* **Installation and Dependencies:** A developer must manage separate Node.js package installations for each tool: @openai/codex, @google/gemini-cli, and @anthropic-ai/claude-code.1  
* **Authentication:** Credential management is inconsistent. OpenAI's Codex and the community Anthropic CLI rely on environment variables (export OPENAI\_API\_KEY, export ANTHROPIC\_API\_KEY), while Google's Gemini CLI uses a browser-based login flow (gemini login) or environment variables for API keys.1  
* **Command Surface:** The syntax for invoking the models, while conceptually similar, differs in implementation. A simple prompt might be executed via codex "prompt", gemini \-p "prompt", or claude "prompt".6 This inconsistency creates cognitive overhead and complicates scripting and automation across different providers.

This fragmentation inhibits a fluid workflow, forcing developers to context-switch between different tool semantics. More critically, it makes direct, apples-to-apples comparison of model performance, cost, and behavior for a specific task a manual and error-prone process.

### **Defining the Modular Intelligence Ecosystem (MIE)**

The Unified-CLI (U-CLI) framework is proposed not as a mere convenience wrapper, but as the foundational layer of a **Modular Intelligence Ecosystem (MIE)**. An MIE is a design philosophy that treats AI models as interchangeable, auditable, and verifiable components within a larger system. By abstracting the provider-specific implementations behind a coherent interface, the U-CLI enables a strategic approach to AI integration.

The core value propositions of the U-CLI are:

* **Interoperability:** A single, stable, and ergonomic command surface to access any supported LLM provider, eliminating the need to learn and manage multiple tools.  
* **Auditability:** A canonical logging schema and a dedicated "Drift-Ledger" to systematically track every interaction, including performance metrics (latency, token counts) and cost. This provides an immutable record for analysis and compliance.  
* **Extensibility:** A robust plugin architecture that allows new models and providers to be integrated seamlessly without altering the core framework, ensuring the system is future-proof.  
* **Verifiability:** The built-in capability to execute the same prompt against multiple models simultaneously and diff their outputs, enabling objective, data-driven evaluation of model capabilities, biases, and drift over time.

### **Key Architectural Principles (The "Lenses")**

The design and implementation of the U-CLI will be guided by a set of core architectural principles, referred to as "lenses." These lenses ensure that every component of the system is built with a clear purpose and adheres to the project's primary objectives.

1. **Plugin-Interface Lens:** Guarantees a stable, minimal, and consistent interface for all provider plugins.  
2. **Auth-Vault Lens:** Prioritizes the secure, cross-platform storage and management of sensitive API credentials.  
3. **Output-Normalisation Lens:** Mandates the mapping of disparate provider API responses into a single, canonical U-CLI schema.  
4. **Feature-Parity vs. Specificity Lens:** Provides a clear strategy for distinguishing between universal commands and provider-specific pass-through flags.  
5. **Drift-Ledger Lens:** Embeds auditability and verifiability as a first-class feature of the system.  
6. **Workflow-Ergonomics Lens:** Focuses on optimizing the developer experience for speed and efficiency, especially for shell-based workflows.  
7. **Security & Sandbox Lens:** Enforces a security model based on least-privilege defaults and safe execution environments.

## **Phase 0 \- Competitive Landscape & Requirements Analysis**

### **Objective**

The first phase of this project is to perform a comprehensive reconnaissance of the existing LLM CLI landscape. This analysis involves deconstructing the command surface, authentication methods, configuration hierarchies, output formats, and special features of the primary target CLIs: OpenAI Codex, Google Gemini, and Anthropic Claude Code. The goal is to identify common patterns suitable for abstraction and unique features that require a deliberate normalization strategy. This analysis forms the evidentiary basis for the U-CLI architectural design.

### **Research Synthesis: Commonalities and Divergences**

A detailed review of the target CLIs reveals significant commonalities in their underlying technology and interaction paradigms, alongside critical divergences in their agentic capabilities and feature sets.

**Common Ground:**

* **Technical Foundation:** All three flagship CLIs—Codex, Gemini, and Claude Code—are built upon the Node.js runtime and are distributed via npm.1 This shared technological stack presents a strong case for considering TypeScript/Node.js as a host language for U-CLI, as it would simplify integration and leverage a common ecosystem.  
* **Interaction Modes:** A universal pattern is the support for two primary modes of operation: an interactive REPL (Read-Eval-Print Loop) for conversational workflows (codex, gemini, claude) and a non-interactive, "quiet" mode designed for scripting and shell piping (codex \-q, gemini \-p, claude \-p).6 This dual-mode paradigm is a fundamental requirement for U-CLI to preserve developer flexibility.  
* **Configuration Hierarchy:** The CLIs converge on a layered configuration model that provides a cascade of settings. This typically includes global user-level configurations (in \~/.codex/, \~/.gemini/, \~/.claude/), project-specific context files (AGENTS.md, GEMINI.md, CLAUDE.md), and command-line flags for session-specific overrides.8 This battle-tested approach effectively separates user, project, and session concerns and will be adopted by U-CLI.

### **The Convergent Evolution Towards Agentic Frameworks and MCP**

A surface-level analysis shows that these CLIs are more than simple API wrappers; they are "agentic" tools capable of interacting with the local developer environment. They can read and write files, execute shell commands, and operate within a sandboxed environment to accomplish tasks.1

A deeper investigation, however, reveals a more profound architectural convergence. Both Google's Gemini CLI and Anthropic's Claude Code CLI have explicitly adopted the **Model Context Protocol (MCP)** as a core component of their architecture for tool use and external data access.5 MCP is an open, vendor-neutral protocol designed to standardize how applications provide context to LLMs, functioning like a "USB-C port for AI applications".13 It defines a client-server architecture where an AI application (the "host") can connect to various "servers" that expose tools, resources, and prompts in a standardized way.16

This industry-wide move towards a standardized protocol for agentic interaction presents a significant architectural opportunity for U-CLI. Rather than engineering complex, bespoke adapters for each provider's unique tool-calling API, U-CLI can be designed as a generic **MCP Host**. In this model, the provider plugins become dramatically simpler. Their primary responsibility shifts from translating tool-use logic to merely handling authentication and establishing a connection to the provider's backend, which itself speaks MCP. This approach not only simplifies the U-CLI's core logic and the Plugin-Interface Lens but also positions U-CLI as a native citizen in the emerging ecosystem of interoperable AI agents. Furthermore, it opens the possibility for U-CLI to allow users to connect their *own* custom MCP servers, making any tool available to *any* model through the unified interface.

### **Normalizing Irreducible Specialties**

While the CLIs share common patterns, each also possesses unique, "sticky" features that define its character and utility.

* **OpenAI Codex:** Features a granular approval-mode (suggest, auto-edit, full-auto) that gives users fine-grained control over the agent's autonomy to edit files and execute commands.1  
* **Google Gemini:** Implements a checkpointing system that saves a project snapshot before tools modify files, allowing for easy restoration.6  
* **Anthropic Claude Code:** Provides robust session management with resume and continue commands to reload previous conversations.9

A naive architectural approach would relegate these features to a generic \--provider-flags passthrough, undermining the goal of a truly unified interface. A more sophisticated strategy involves identifying the abstract concept each feature represents. Gemini's checkpointing and Claude's session resumption are both forms of **state management**. Codex's approval modes are a form of **permission control**.

This realization allows U-CLI to elevate these abstract concepts to first-class, universal commands. The framework can define a universal command set, such as u session save | load and u query \--permission-level \<plan|edit|execute\>. The core U-CLI framework implements the command syntax, while the Provider plugin interface contains optional methods (e.g., save\_session(), map\_permission\_level()) that translate the universal U-CLI command into the specific flag or API call required by the underlying provider. For instance, u query \--permission-level execute would be mapped to \--full-auto by the Codex plugin, \--yolo by the Gemini plugin, and \--dangerously-skip-permissions by the Claude plugin. This design achieves a seamless, unified user experience while respecting and leveraging the distinct capabilities of each provider.

### **Table: Comparative CLI Feature Matrix**

The following table synthesizes the key features of the target CLIs, providing the raw data for the architectural abstractions discussed.

| Feature | OpenAI Codex | Google Gemini | Anthropic Claude Code |
| :---- | :---- | :---- | :---- |
| **Installation** | npm install \-g @openai/codex 1 | npm install \-g @google/gemini-cli 6 | npm install \-g @anthropic-ai/claude-code 5 |
| **Authentication** | export OPENAI\_API\_KEY or codex login (Plus/Pro) 8 | gemini login (OAuth) or export GEMINI\_API\_KEY 4 | export ANTHROPIC\_API\_KEY or claude config 11 |
| **Interaction Mode** | Interactive REPL (codex) & Non-interactive (codex exec) 8 | Interactive REPL (gemini) & Non-interactive (gemini \-p) 6 | Interactive REPL (claude) & Non-interactive (claude \-p) 9 |
| **Piped Input** | Yes, can be piped to commands 20 | Yes, \`echo "..." | gemini\` 6 |
| **Context Files** | AGENTS.md (global, repo, local) 8 | GEMINI.md (global, project, sub-dir) 6 | CLAUDE.md 21, settings.json 11 |
| **Agentic Actions** | Read/write files, run shell commands 1 | Read/write files, run shell commands, web search 12 | Read/write files, run commands, web search, MCP tools 5 |
| **Sandboxing** | OS-native (macOS Seatbelt, Linux Landlock/seccomp) 8 | Docker or Podman required for sandbox mode (--sandbox) 6 | Not explicitly detailed, relies on permission model 9 |
| **Permission Control** | \--approval-mode (suggest, auto-edit, full-auto) 1 | \--yolo (auto-accept all) 10 | \--dangerously-skip-permissions, \--allowedTools 9 |
| **State Management** | None natively mentioned | \--checkpointing flag and /restore command 6 | \--resume and \--continue flags for sessions 9 |
| **Multimodality** | Yes, can accept images/screenshots 8 | Yes, can generate apps from PDFs/sketches 4 | Yes, can read images and URLs 24 |
| **Structured Output** | API supports json\_schema response format 25 | API supports response\_mime\_type: "application/json" 26 | \--output-format json flag for SDK/print mode 9 |
| **Tool Integration** | Function calling in API, shell/patch tools in CLI 27 | Explicit MCP support, custom slash commands 12 | Explicit MCP support, subagents, SDK hooks 5 |

### **Table: Provider Specialty to U-CLI Abstraction Mapping**

This table provides a concrete specification for how U-CLI will unify the disparate features identified above into a coherent command set.

| Provider Feature | Abstract Concept | Proposed U-CLI Command / Flag | Implementation Notes |
| :---- | :---- | :---- | :---- |
| codex \--approval-mode full-auto 1, gemini \--yolo 10, claude \--dangerously-skip-permissions 9 | Permission Control | \--permission-level execute | The plugin maps this universal level to the provider's specific "full auto" flag. |
| codex \--approval-mode auto-edit 1 | Permission Control | \--permission-level edit | The plugin maps this to the provider's flag for auto-approving file edits but not command execution. Gemini/Claude plugins may treat this as a no-op or map to a similar concept if available. |
| codex \--approval-mode suggest (default) 1 | Permission Control | \--permission-level plan (default) | The default mode for all providers. The agent makes a plan and requires confirmation for every action. |
| gemini \--checkpointing 6 | State Management | u session save \[--message "Initial state"\] | The Gemini plugin will trigger its native checkpointing. Other plugins can implement a manual state save (e.g., creating a git commit or storing session history). |
| claude \--resume \<id\> 9, gemini /chat resume \<tag\> 6 | State Management | u session load \<session\_id\> | The plugin maps this command to the provider's native session resumption mechanism. |
| gemini \--sandbox 6 | Secure Execution | \--sandbox | This flag will be a universal U-CLI flag. The core framework will manage the sandbox (e.g., via Docker), and plugins can indicate if they support a native sandbox that should be used instead. |
| codex AGENTS.md 8, gemini GEMINI.md 6, claude CLAUDE.md 21 | Project Context | u-cli.md in project root | U-CLI reads this single file. The active plugin is responsible for formatting its content and passing it to the model API in the correct format (e.g., as a system prompt). |
| All providers support MCP 9 or tool calling 27 | Tool Integration | u config add-mcp-server... | U-CLI acts as an MCP Host. The core framework manages MCP connections, and plugins simply pass the context through to the model API. This creates a unified tool ecosystem. |

#### **Works cited**

1. OpenAI Codex CLI – Getting Started, accessed August 3, 2025, [https://help.openai.com/en/articles/11096431](https://help.openai.com/en/articles/11096431)  
2. Google announces Gemini CLI: your open-source AI agent, accessed August 3, 2025, [https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)  
3. Claude Code: Deep coding at terminal velocity \\ Anthropic, accessed August 3, 2025, [https://www.anthropic.com/claude-code](https://www.anthropic.com/claude-code)  
4. google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal. \- GitHub, accessed August 3, 2025, [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
5. Claude Code overview \- Anthropic API, accessed August 3, 2025, [https://docs.anthropic.com/en/docs/claude-code/overview](https://docs.anthropic.com/en/docs/claude-code/overview)  
6. Google Gemini CLI Cheatsheet \- Philschmid, accessed August 3, 2025, [https://www.philschmid.de/gemini-cli-cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)  
7. dvcrn/anthropic-cli: CLI for interacting with Anthropic Claude \- GitHub, accessed August 3, 2025, [https://github.com/dvcrn/anthropic-cli](https://github.com/dvcrn/anthropic-cli)  
8. openai/codex: Lightweight coding agent that runs in your terminal \- GitHub, accessed August 3, 2025, [https://github.com/openai/codex](https://github.com/openai/codex)  
9. CLI reference \- Anthropic API, accessed August 3, 2025, [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
10. Gemini CLI Tutorial Series — Part 2 : Gemini CLI Command line parameters | by Romin Irani | Google Cloud \- Medium, accessed August 3, 2025, [https://medium.com/google-cloud/gemini-cli-tutorial-series-part-2-gemini-cli-command-line-parameters-e64e21b157be](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-2-gemini-cli-command-line-parameters-e64e21b157be)  
11. Claude Code settings \- Anthropic API, accessed August 3, 2025, [https://docs.anthropic.com/en/docs/claude-code/settings](https://docs.anthropic.com/en/docs/claude-code/settings)  
12. Gemini CLI | Gemini for Google Cloud, accessed August 3, 2025, [https://cloud.google.com/gemini/docs/codeassist/gemini-cli](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)  
13. Introduction \- Model Context Protocol, accessed August 3, 2025, [https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)  
14. Understanding the Model Context Protocol (MCP): Architecture \- Nebius, accessed August 3, 2025, [https://nebius.com/blog/posts/understanding-model-context-protocol-mcp-architecture](https://nebius.com/blog/posts/understanding-model-context-protocol-mcp-architecture)  
15. What is Model Context Protocol? | A Practical Guide \- K2view, accessed August 3, 2025, [https://www.k2view.com/what-is-model-context-protocol/](https://www.k2view.com/what-is-model-context-protocol/)  
16. Architecture Overview \- Model Context Protocol, accessed August 3, 2025, [https://modelcontextprotocol.io/docs/learn/architecture](https://modelcontextprotocol.io/docs/learn/architecture)  
17. A beginners Guide on Model Context Protocol (MCP) \- OpenCV, accessed August 3, 2025, [https://opencv.org/blog/model-context-protocol/](https://opencv.org/blog/model-context-protocol/)  
18. Understanding OpenAI Codex CLI Commands \- MachineLearningMastery.com, accessed August 3, 2025, [https://machinelearningmastery.com/understanding-openai-codex-cli-commands/](https://machinelearningmastery.com/understanding-openai-codex-cli-commands/)  
19. Claude Code SDK \- Anthropic API, accessed August 3, 2025, [https://docs.anthropic.com/en/docs/claude-code/sdk](https://docs.anthropic.com/en/docs/claude-code/sdk)  
20. peterdemin/openai-cli: Command-line client for OpenAI APIs \- GitHub, accessed August 3, 2025, [https://github.com/peterdemin/openai-cli](https://github.com/peterdemin/openai-cli)  
21. Anthropic Claude Code CLI: Prompts & Tool Definitions \- AI Engineer Guide, accessed August 3, 2025, [https://aiengineerguide.com/blog/claude-code-prompt/](https://aiengineerguide.com/blog/claude-code-prompt/)  
22. Gemini CLI Full Tutorial \- DEV Community, accessed August 3, 2025, [https://dev.to/proflead/gemini-cli-full-tutorial-2ab5](https://dev.to/proflead/gemini-cli-full-tutorial-2ab5)  
23. OpenAI Codex CLI Tutorial \- DataCamp, accessed August 3, 2025, [https://www.datacamp.com/tutorial/open-ai-codex-cli-tutorial](https://www.datacamp.com/tutorial/open-ai-codex-cli-tutorial)  
24. Claude Code: Best practices for agentic coding \- Anthropic, accessed August 3, 2025, [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)  
25. Structured Outputs \- OpenAI API, accessed August 3, 2025, [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)  
26. Structured output | Gemini API | Google AI for Developers, accessed August 3, 2025, [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)  
27. Developer quickstart \- OpenAI API, accessed August 3, 2025, [https://platform.openai.com/docs/quickstart](https://platform.openai.com/docs/quickstart)  
28. OpenAI Codex CLI, how does it work? \- Philschmid, accessed August 3, 2025, [https://www.philschmid.de/openai-codex-cli](https://www.philschmid.de/openai-codex-cli)  
29. Gemini CLI: Custom slash commands | Google Cloud Blog, accessed August 3, 2025, [https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands](https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands)