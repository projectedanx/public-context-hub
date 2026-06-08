# **OpenCode IDE: Fullstack Manual of Hidden Settings, Optimal Configurations, Plugins, and Toolchain Integrations**

## **Executive Summary: Operational Architecture and Forensic Overview**

The contemporary landscape of software development tools has bifurcated into two distinct phylogenies: the traditional, editor-centric Integrated Development Environment (IDE) epitomized by Visual Studio Code and IntelliJ, and the emerging, agent-centric runtime environments represented by OpenCode. A forensic analysis of the OpenCode architecture reveals that calling it an "IDE" is a terminological convenience that obscures its true nature. OpenCode is functionally a client-server command-line operating system designed to host autonomous software engineering agents. Unlike traditional editors that layer intelligence on top of a text buffer, OpenCode treats the text buffer as merely one input vector for a persistent, headless reasoning engine.1

This operational manual provides a comprehensive, forensic decomposition of the OpenCode runtime environment. It is designed for toolchain architects, security engineers, and power users who require a depth of understanding that transcends standard documentation. Our investigation uncovers a highly mutable environment where the "IDE" is a programmable substrate, capable of being scripted, pruned, and optimized via hidden configuration flags, undocumented environment variables, and intricate plugin architectures.2

The analysis identifies OpenCode as a "Glass Box" system. While it ships with reasonable defaults, its true capabilities are unlocked only through direct manipulation of its internal configuration schemas (opencode.json), its startup flags, and its plugin injection points. For instance, the transition from a passive coding assistant to a proactive "Ultrawork" agent—capable of spawning parallel sub-processes to explore, test, and refactor code simultaneously—requires precise configuration of the oh-my-opencode plugin and the underlying opencode.experimental flags.4 Similarly, the management of cognitive load and token costs in long-running sessions necessitates the implementation of "Dynamic Context Pruning" (DCP), a mechanism that surgically alters the agent's memory stream in real-time.5

This report is structured to guide the reader from the binary internals outward to the ecosystem edge. We begin with a dissection of the runtime architecture and CLI forensics, move through the hierarchical configuration system, analyze the agentic orchestration layer, and finally detail the optimal integration blueprints for high-security and high-performance environments. By understanding the forensic interplay between these layers—how a CLI flag influences a plugin hook, which then alters an LLM's context window—engineers can transform OpenCode from a simple tool into a robust, automated cybernetic extension of their engineering workflow.

## **Part I: System Internals and Runtime Architecture**

To control OpenCode effectively, one must first understand its binary lifecycle. The application does not function as a monolithic desktop application in the traditional sense. Instead, it operates on a decoupled client-server architecture, written primarily in Go, which dictates its behavior in local, remote, and CI/CD contexts.6

### **1.1 The Binary Lifecycle and Execution Modes**

The opencode binary serves as a polymorphic entry point. Upon invocation, it performs an environmental scan to determine its execution mode. This initial phase is critical for understanding "headless" operations and remote attachments.

#### **1.1.1 The Client-Server Handshake**

When a user types opencode in their terminal, the binary does not immediately render a UI. Instead, it checks for the existence of an active OpenCode server process. This detection logic relies on specific markers, typically lock files or socket descriptors located in \~/.local/share/opencode (on Linux/macOS) or %USERPROFILE%\\.local\\share\\opencode (on Windows).7

If a server is detected—indicated by the presence of OPENCODE\_SERVER environment variables or active lock files—the binary initializes as a **Thin Client**. In this mode, it effectively acts as a terminal emulator wrapper, forwarding keystrokes and rendering the TUI (Terminal User Interface) state received from the server. This separation allows for session persistence: if the TUI client crashes or is closed, the server (and the agent's reasoning loop) continues running in the background, preserving the session state.2

If no server is found, the binary initializes in **Standalone Mode**, spinning up a local server instance within the same process tree before attaching the client view. This architecture explains why flags like \--attach exist; they allow a local terminal to interface with a remote OpenCode instance running on a powerful build server, decoupling the heavy lifting of LLM inference and file indexing from the user's interface device.2

#### **1.1.2 Headless "Pipe" Mode**

Forensic analysis of the CLI arguments reveals a distinct operational mode triggered by the \--prompt (or \-p) flag. In this "Headless" or "Pipe" mode, the TUI subsystem is completely bypassed. The binary initializes the agent, accepts input from the command line arguments or stdin, processes the request via the configured model, and streams the output to stdout before terminating.3

This mode is the foundation for integrating OpenCode into Unix pipelines and CI/CD workflows. For example, a developer can pipe the output of a git diff into OpenCode with a prompt to generate a commit message or a code review, treating the entire agentic intelligence as a standard Unix filter utility. The enabling of this mode fundamentally changes the binary's logging behavior and error handling, suppressing interactive elements like spinners to ensure clean data streams.2

### **1.2 The Terminal User Interface (TUI) Engine**

The visible layer of OpenCode is built upon a TUI framework (likely bubbletea or a similar Go-based library, given the architecture descriptions) that renders complex UI elements—chat bubbles, file diffs, and spinners—using standard ANSI escape codes.

#### **1.2.1 Rendering Constraints and Optimization**

The TUI operates within the constraints of the host terminal emulator. Our analysis highlights specific configuration flags designed to mitigate rendering artifacts common in high-throughput data streams typical of LLM outputs. The tui.scroll\_acceleration setting, particularly on macOS, modifies the event loop to interpret scroll wheel inertia, preventing the "tearing" or "jank" often seen when an agent dumps a large code block.8 Furthermore, the tui.diff\_style configuration allows users to toggle between varying visual representations of code changes, impacting how the underlying diff engine presents data to the user—a critical factor when reviewing large refactors generated by the agent.8

#### **1.2.2 The Event Loop and Keybinding Interception**

The TUI acts as an event interception layer. It captures specific key chords (e.g., Ctrl+X leader keys) before they reach the shell. This interception is configurable via the keybinds section of the global config. Understanding this layer is crucial for diagnosing conflicts with terminal multiplexers like tmux or zellij. OpenCode includes specific logic (often checking the TMUX environment variable) to adjust its rendering strategies to avoid conflict with the multiplexer's own status bars and keybinds.9

### **1.3 State Persistence and Session Management**

OpenCode maintains a stateful memory of interactions, which is essential for the agent's context window management.

#### **1.3.1 The SQLite Session Store**

Session data is not held purely in RAM. Forensics indicate that OpenCode serializes session history, including prompts, tool outputs, and agent thoughts, into a structured datastore, typically SQLite databases located in project-specific .opencode directories or global storage paths.10 This serialization enables the opencode session list and \--resume functionalities.

The structure of this database is critical for "Context Pruning" plugins. When a plugin like opencode-dcp modifies the conversation history, it is effectively performing UPDATE or DELETE operations on this persisted state schema, identifying rows corresponding to "tool outputs" and truncating them to save tokens.5

#### **1.3.2 Context Snapshotting**

To support features like "Undo" (/undo) and "Redo" (/redo), the system must snapshot the state of the codebase and the conversation tree. This is likely achieved via a combination of Git internal commands (creating temporary commits or stashes) and database transaction rollbacks. This integration with the version control system means that OpenCode is deeply intertwined with the .git directory of the user's project, and corruption in one can theoretically affect the other.8

## **Part II: Command Line Forensics and Hidden Flags**

The Command Line Interface (CLI) is the primary control plane for the OpenCode runtime. While standard documentation lists basic flags, a deeper forensic examination of the binary's help output, source code references, and developer discussions reveals a complex array of control mechanisms. These flags allow for granular manipulation of the agent's network behavior, logging verbosity, and session lifecycle.2

### **2.1 Core Runtime Flags: Beyond the Basics**

The following table details critical runtime flags, expanding on their operational implications for power users and automation engineers.

| Flag | Short | Forensic Function | Operational Implication |
| :---- | :---- | :---- | :---- |
| \--continue | \-c | Instructs the binary to locate the most recent session timestamp in the state DB and resume from that UUID. | Critical for persistent workflows; allows context to survive binary restarts or crashes. 2 |
| \--session | \-s | Forces the binary to load a specific UUID session. | Enables "context switching" between different distinct tasks without losing the agent's short-term memory or "thought" history. 2 |
| \--attach |  | Connects the TUI client to a specific running HTTP server address (e.g., http://localhost:4096). | Facilitates remote pair programming or centralized AI server management where the reasoning engine is hosted on separate hardware. 2 |
| \--prompt | \-p | Bypasses the TUI event loop entirely; executes a single conversational turn. | Essential for scripting and "Unix philosophy" integration, allowing OpenCode to act as a pipe filter. 3 |
| \--quiet | \-q | Suppresses the "spinner" animation, progress bars, and extraneous stderr logs. | Mandatory for parsing JSON output in automated scripts to prevent log pollution from breaking downstream parsers (like jq). 3 |
| \--dry-run |  | Simulates operations (mostly uninstall/prune/upgrade) without executing disk writes. | Used for auditing what files or sessions would be destroyed by cleanup commands before committing to data loss. 2 |
| \--debug | \-d | Elevates the internal log level to DEBUG; prints raw logs to stderr. | Exposes raw HTTP payloads, headers, and tool execution traces, vital for debugging auth issues or plugin failures. 3 |

### **2.2 Hidden Debugging and Developer Flags**

Beyond the standard operational flags, specific switches exist primarily to aid in plugin development and core binary debugging. These are often transient or marked as "internal" but offer powerful capabilities for deep investigation.

#### **2.2.1 Log Streaming and Forensics**

* \--print-logs: This flag directly pipes the internal structured log stream to stderr. This is distinct from \--debug as it streams the application log rather than just enabling debug mode. It is essential when the TUI crashes immediately upon boot, preventing access to the internal log view (Ctrl+L). In such "crash-on-boot" scenarios, \--print-logs is the only window into the initialization failure.2  
* \--trace: While less documented, references in developer discussions suggest tracing capabilities that output detailed execution paths, likely utilized by core developers to profile performance bottlenecks in the Go runtime.

#### **2.2.2 Registry and Cache Manipulation**

* \--refresh: This flag forces a cache invalidation for the models.dev registry. OpenCode caches model definitions (pricing, context window limits, capabilities) locally to reduce latency. If a provider updates a model (e.g., a new claude-3-5-sonnet release with a higher token limit), OpenCode may not immediately recognize the change. Running opencode models \--refresh forces the binary to fetch the new metadata immediately, bypassing the standard TTL (Time To Live).2  
* \--verbose (in models command): When listing models, the standard output is truncated for readability. Adding \--verbose reveals hidden metadata about models, such as their specific input/output pricing, context window limits, and supported modalities (image, text), which are usually abstracted away.2

### **2.3 Environment Variable Overrides and Kill Switches**

Environment variables in OpenCode take precedence over many config file settings and serve as the primary injection point for "secret" configurations or system-wide overrides. They are particularly potent because they bypass the need to modify JSON files, making them ideal for temporary overrides in shell sessions or CI/CD pipelines.3

#### **2.3.1 Critical Stability Flags**

* OPENCODE\_DISABLE\_DEFAULT\_PLUGINS: This is a nuclear option for debugging. If OpenCode becomes unstable due to a rogue community plugin or a conflict in the plugin load order, setting this variable to true boots the IDE in "Safe Mode," loading only the core binary features. This allows users to recover control of the configuration files to fix the issue.2  
* OPENCODE\_DISABLE\_PRUNE: By default, OpenCode likely performs garbage collection on old session data to save disk space. Disabling this via OPENCODE\_DISABLE\_PRUNE=true is critical for forensic analysts or users auditing their AI interactions, as it preserves the full history of all interactions for later analysis.2  
* OPENCODE\_CONFIG\_DIR: This variable overrides the default configuration path. It enables the creation of distinct "Profiles." A user could have a \~/.config/opencode-work and a \~/.config/opencode-personal, switching between them by changing this environment variable. This isolates plugins, history, and credentials completely.11

#### **2.3.2 Experimental Feature Toggles**

The OPENCODE\_EXPERIMENTAL\_\* namespace contains specific toggles for features that are in active development but not yet stable enough for general release.

* OPENCODE\_EXPERIMENTAL: The "God Mode" flag. Setting this to true enables *all* unstable features simultaneously. While convenient, it carries high stability risks and is recommended only for developers contributing to the core codebase.2  
* OPENCODE\_EXPERIMENTAL\_LSP\_TOOL: Explicitly enables the Language Server Protocol tool. Without this, the agent relies on grep and text matching. Enabling this allows the agent to perform "Go to Definition" or "Find References" calls, significantly enhancing its ability to navigate large codebases without manually read-ing every file. This transforms the agent from a text-processor to a code-aware entity.12  
* OPENCODE\_EXPERIMENTAL\_FILEWATCHER: Activates a background daemon that watches for file system changes not initiated by the agent. This gives the agent "eyes," allowing it to react if a user modifies a file in a separate editor (like Vim or VSCode) while the session is running, preventing context drift.2  
* OPENCODE\_EXPERIMENTAL\_OUTPUT\_TOKEN\_MAX: Overrides the safety limits on model output. This is useful when generating massive boilerplate code or documentation where the default safety limit (often 4k or 8k tokens) would truncate the response, forcing the user to say "continue" repeatedly.2

## **Part III: Configuration Architecture and Schema Forensics**

The configuration system of OpenCode is hierarchical, merging settings from multiple sources to determine the final runtime state. Understanding this hierarchy is essential for resolving conflicts, especially in complex environments where global user settings might clash with project-specific overrides.11

### **3.1 The Configuration Hierarchy and Precedence Rules**

OpenCode resolves configuration using a "Last Write Wins" (merge) strategy, with specific specificity rules. The load order, from lowest to highest priority, defines the final operational state 11:

1. **Remote Defaults (.well-known/opencode)**: If the user is authenticated with an organization, the server can push default settings. These serve as the baseline, potentially enforcing corporate policies like "allowed models" or "telemetry on".11  
2. **Global Config (\~/.config/opencode/opencode.json)**: The user's personal baseline configuration. This is where themes, default keybinds, and preferred providers are typically set.  
3. **Custom Config Directory (OPENCODE\_CONFIG\_DIR)**: If this environment variable is set, the configuration within it is loaded next. This allows for the "Profile" switching mentioned in Section 2.3.1.  
4. **Project Config (./opencode.json or ./.opencode/opencode.json)**: Settings specific to the current repository. These settings override everything below them. This is critical for ensuring that all developers on a team use the same linting rules or specific agent configurations for a shared codebase.11  
5. **Environment Variables**: Specific variables (like OPENCODE\_API\_KEY or OPENCODE\_DISABLE\_PLUGINS) override their JSON counterparts. This is the "highest" level of configuration, allowing immediate runtime injection.3

**Forensic Insight**: The precedence of Project Config over Global Config creates a specific security vector. A malicious actor could check in a opencode.json file into a shared repository that reconfigures the agent to use a different (potentially malicious) model endpoint or enables data exfiltration via a custom mcp server. Security-conscious teams should audit opencode.json files in third-party repositories before launching the agent in those directories.11

### **3.2 The opencode.json Schema Deconstructed**

The opencode.json (or .jsonc for JSON with comments) file is the central nervous system of the OpenCode instance. It controls provider authentication, tool permissions, and plugin loading sequence.

#### **3.2.1 Provider and Model Configuration Variants**

The schema allows for complex "variant" definitions. Users are not limited to the standard model configurations OpenCode ships with; they can define custom variants that lock in specific parameters, creating specialized modes for different tasks.13

JSON

"provider": {  
  "openai": {  
    "models": {  
      "gpt-5": {  
        "variants": {  
          "security-audit": {  
            "reasoningEffort": "high",  
            "textVerbosity": "high",  
            "reasoningSummary": "hidden"  
          }  
        }  
      }  
    }  
  }  
}

In the example above, a "security-audit" variant is created. A user can then invoke opencode \--model openai/gpt-5 \--variant security-audit. This ensures that for specific high-stakes tasks, the model *always* uses high reasoning effort, removing the variability of the default settings which might fluctuate based on provider load or default optimization.13 This determinism is vital for repeatable forensic analysis.

#### **3.2.2 Permission Granularity and Security Boundaries**

The permission object within the config is the primary security boundary. It controls what the agent can do without explicit user confirmation. The schema supports wildcards (\*) and specific tool targeting, allowing for fine-grained access control.12

| Tool | Permission Key | Risk Level | Recommended Setting |
| :---- | :---- | :---- | :---- |
| **Bash** | bash | **Critical** | ask (or deny for untrusted agents). Allows arbitrary command execution, which is the highest risk vector. |
| **File Edit** | edit | **High** | allow (core functionality), but strictly monitor write operations in sensitive directories. |
| **Web Fetch** | webfetch | **Medium** | allow (necessary for retrieving docs), but creates a data exfiltration vector. |
| **MCP** | mymcp\_\* | **Variable** | ask. MCP servers can expose databases or internal APIs; explicit approval is safer. |

**Shadow Feature**: The edit permission acts as a hierarchical "master switch" for several related tools: write, patch, and multiedit. Disabling edit silently disables all file modification capabilities, even if write is individually enabled in some contexts. This undocumented dependency is crucial for creating true "Read-Only" auditor agents; simply disabling write might leave patch open, but disabling edit seals the filesystem.12

### **3.3 Undocumented Configuration Keys**

Scanning the source code and community issue trackers reveals configuration keys that are not prominent in the main documentation but offer significant utility:

* "shell": This object allows overriding the specific shell binary used by the bash tool. By default, OpenCode uses the SHELL environment variable. However, for security or compatibility, a user can force it to use /bin/sh (for POSIX compliance) or a restricted shell, preventing the agent from accessing complex shell features.3  
* "tui.scroll\_acceleration": As mentioned in the architecture section, this is a specific toggle for macOS users to enable inertia-based scrolling, overriding the static line-step scrolling.8  
* "server.mdns": Controls whether the OpenCode server broadcasts its presence on the local network via mDNS. Disabling this (false) is a recommended security hardening step for users on public Wi-Fi to prevent other OpenCode clients on the same network from discovering their running instance.11

## **Part IV: The Agentic Core and Orchestration**

The "Agent" in OpenCode is not merely a persona; it is a configurable software entity defined by a specific combination of tools, prompts, permissions, and models. The manual reveals that users can define "Shadow Agents"—specialized, highly constrained, or uniquely empowered agents—that operate alongside the defaults.

### **4.1 The AGENTS.md and Markdown Definition Protocol**

Agents can be defined in \~/.config/opencode/agent/\*.md (Global) or .opencode/agent/\*.md (Project). The filename becomes the agent's handle (e.g., auditor.md becomes @auditor). The true power of this system lies in the YAML frontmatter, which acts as the configuration header for the agent.14

YAML

\---  
description: "Security Auditor \- Read Only"  
mode: subagent  
model: anthropic/claude-3-opus  
temperature: 0.1  
tools:  
  edit: false  
  write: false  
  bash: true  
permission:  
  bash: ask  
\---  
You are a security auditor. You review code for CVEs...

* **mode: subagent**: This is a critical setting. Primary agents can be cycled via the Tab key in the TUI. Subagents are hidden from this main cycle and are only invoked when called by a primary agent or explicitly mentioned (@auditor). This keeps the UI clean while maintaining a library of specialized tools.14  
* **tools locking**: In the example above, edit and write are explicitly set to false. This creates a "Safe" agent. Even if the LLM hallucinates and tries to delete a file, the runtime will block the tool call at the binary level. This acts as a "Sandbox" within the agent definition, independent of the global permissions.15

### **4.2 Subagent Delegation Logic and "Shadow" Invocation**

Primary agents (like "Sisyphus" or the standard "Build" agent) have the capability to spawn subagents. The manual identifies a "hidden" behavior: Automatic Delegation.  
If a subagent's description field matches the user's intent strongly enough, the Primary agent acts as a router and can invoke the subagent without the user explicitly typing @subagent. For example, if a subagent is described as "Expert in CSS and Tailwind," and the user asks "Fix the padding on this div," the Primary agent may hand off the task to the CSS subagent automatically.

* **Forensic Artifact**: This delegation creates a "Task" tool call in the logs. An analyst will see the Primary agent calling the task tool with arguments targeting the subagent's handle.  
* **Load Order and Inheritance**: Subagents inherit the model of the calling agent unless a model is explicitly defined in their markdown frontmatter. This is a common source of configuration errors—users expect a subagent to use a "smarter" model, but it defaults to the (often cheaper/faster) primary model unless overridden.14

### **4.3 The "Sisyphus" Architecture**

The oh-my-opencode plugin introduces the "Sisyphus" agent, which represents the pinnacle of this orchestration model. Sisyphus is not just a prompt; it is a multi-agent system.

* **Prompt Injection**: The plugin injects specific instructions into the Sisyphus prompt that define its relationship with other agents like @oracle (for high-level reasoning) and @librarian (for documentation search).  
* **The "Ultrawork" Loop**: When the user invokes "Ultrawork" (ulw), Sisyphus enters a specialized loop. It parses the request and spawns *background* agents (like @explore) to map the codebase. These agents run in parallel, effectively multithreading the cognitive load. Sisyphus then aggregates their outputs.  
* **Token Consumption**: This architecture drastically increases token consumption. A single "Ultrawork" request might trigger three or four simultaneous context windows. The plugin mitigates this by assigning cheaper models (like gemini-3-flash) to the exploration sub-agents, reserving the expensive "Opus" or "GPT-5" models for the Sisyphus orchestrator.4

## **Part V: The Extension Ecosystem and Plugin Forensics**

OpenCode's power is significantly amplified by its plugin ecosystem. Unlike VSCode extensions which are often UI-heavy, OpenCode plugins tend to be deep behavioral modifiers that inject new tools, alter context window management, or intercept agent reasoning loops.

### **5.1 oh-my-opencode: The "Supercharger" Plugin**

oh-my-opencode (OmO) is the most pervasive community plugin, effectively acting as an unofficial "Pro" version of the IDE. It introduces several critical subsystems.4

#### **5.1.1 "Ultrawork" Mode**

The flagship feature of OmO is "Ultrawork" (invoked via ulw or \--ultrawork). This mode represents a shift from interactive chat to autonomous batch processing.

* **Mechanism**: When Ultrawork is active, the plugin creates a "Task" queue. It utilizes the agent's ability to call the task tool to break down a high-level goal into atomic units.  
* **Background Execution**: Unlike standard subagents which might block the UI, Ultrawork agents often run in background threads (or pseudo-threads within the runtime), allowing the user to continue interacting with the main session or monitor the parallel execution streams via the TUI's session manager.4

#### **5.1.2 The "Hooks" System**

OmO reintroduces a "Hooks" system (similar to Git hooks) that allows users to run scripts *before* or *after* specific agent actions.

* PreToolUse: Runs before a tool (like bash) is executed. This is a critical interception point for security. A user could write a hook that scans every bash command for rm \-rf / or DROP TABLE and rejects it before it reaches the shell.  
* PostToolUse: Runs after execution. Useful for logging or auto-committing changes to git after a successful build.  
* UserPromptSubmit: Intercepts the user's message before it goes to the LLM. This allows for "prompt injection" on the client side—automatically appending context (like the contents of a specific file or the current time) to every message.4

### **5.2 opencode-dcp: Dynamic Context Pruning**

As sessions grow, context windows fill up, leading to increased latency, costs, and "forgetfulness." opencode-dcp is a sophisticated memory management plugin that solves this by surgically removing "dead" context.5

#### **5.2.1 Pruning Strategies**

* **Deduplication**: If the agent reads the same file twice, DCP removes the first read from the history. The reasoning is that the agent only needs the *latest* version of the file in its context window.  
* **Supersede Writes**: If the agent writes to a file and then reads it later, the explicit write tool output (which echoes the file content) is pruned. The subsequent read contains the ground truth, making the echo redundant.  
* **Purge Errors**: Tool outputs that resulted in errors are removed after a set number of turns (default 4). The logic is that while the *fact* that an error occurred is important short-term, the *verbose stack trace* of a fixed bug is noise in the long term.5

#### **5.2.2 "Turn Protection" and Configuration**

DCP is aggressive. To prevent it from confusing the agent by removing context it *just* generated, it implements "Turn Protection."

* turnProtection.turns: Defaults to 4\. This means no content is pruned until it is at least 4 interactions old, ensuring the agent has "short-term memory" stability.5  
* **Protected Tools**: Certain tools are immune to pruning by default: task, todowrite, todoread. These tools represent the agent's "long-term memory" or plan. Pruning them would cause the agent to forget what it is working on or what tasks remain.  
* **Conflict Note**: DCP is explicitly disabled for subagents. Subagents are designed to be ephemeral and token-heavy; pruning their context often breaks their ability to summarize their findings back to the main agent. This limitation is hardcoded to prevent "lobotomizing" the sub-agents.5

### **5.3 opencode-antigravity-auth: Accessing Restricted Models**

This plugin connects OpenCode to Google's internal or "Antigravity" authentication endpoints, unlocking access to models that might be rate-limited or unavailable via standard public APIs.16

* **Mechanism**: It handles the OAuth 2.0 flow with Google, storing refresh tokens in a secure JSON file (\~/.config/opencode/antigravity-accounts.json).  
* **Configuration**: It introduces the antigravity- prefix to model names (e.g., antigravity-claude-sonnet-4-5-thinking). This namespace separation ensures that requests are routed through the specific high-quota or internal gateways rather than the public API.  
* **Load Order Criticality**: If using OAuth plugins like this, opencode-dcp *must* be loaded **last** in the plugin array. If DCP loads first, it may intercept the request pipeline or corrupt the authentication headers/flow required by Antigravity, causing the authentication to fail silently or the plugin to crash.17

### **5.4 opencode-tokenscope: Observability and Cost Auditing**

For users managing tight budgets or analyzing agent efficiency, opencode-tokenscope is essential.18

* **Forensic Token Analysis**: This plugin intercepts API calls and categorizes tokens into "System Prompt," "User Message," and "Tool Output." This breakdown is vital for identifying inefficiency.  
* **"Skill Bloat"**: A key finding from TokenScope analysis is the phenomenon of "Skill Bloat." Every time a SKILL.md is loaded via the skill tool, its entire content is dumped into the context. If an agent calls a skill repeatedly or unnecessarily, it burns tokens at an alarming rate. TokenScope makes this "invisible tax" visible, allowing users to optimize their SKILL.md files or restrict agent access to them.18

## **Part VI: Toolchain Integration and MCP (Model Context Protocol)**

The Model Context Protocol (MCP) serves as the bridge between the isolated OpenCode runtime and the external digital world (databases, web browsers, internal APIs). OpenCode acts as an MCP *Host*, connecting to various MCP *Servers* to extend the agent's capabilities.12

### **6.1 Configuring MCP Servers**

MCP servers are defined in opencode.json under the mcp key. The configuration distinguishes between local and remote servers.

JSON

"mcp": {  
  "postgres-prod": {  
    "type": "local",  
    "command": \["npx", "-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost/db"\]  
  },  
  "github-remote": {  
    "type": "remote",  
    "url": "https://mcp.myorg.com/github",  
    "headers": { "Authorization": "Bearer..." }  
  }  
}

* **Local vs. Remote**: "Local" servers are child processes spawned by OpenCode. Communication happens over standard input/output (stdio). "Remote" servers are HTTP endpoints that communicate via Server-Sent Events (SSE).  
* **Security Implication**: A local MCP server runs with the *user's* system permissions. If you mount a Postgres MCP server, the agent effectively has SQL access to that database with the credentials provided. Permission scopes for MCP tools can be wildcarded (e.g., "postgres-prod\_\*": "ask") to prevent accidental DROP TABLE commands while allowing SELECT statements.12

### **6.2 The LSP (Language Server Protocol) Tool**

While "LSP" is standard in traditional IDEs for features like autocomplete, OpenCode exposes it as a distinct *tool* for the agent (lsp).

* **Capabilities**: The agent can call lsp.goToDefinition, lsp.findReferences, or lsp.hover.  
* **Forensic Distinction**: This is distinct from "grep". Grep searches text strings. LSP searches *symbols*. An agent using LSP is significantly more accurate at refactoring because it understands the Abstract Syntax Tree (AST). It knows the difference between a variable named user and a string literal "user".  
* **Activation**: This powerful tool often requires the OPENCODE\_EXPERIMENTAL\_LSP\_TOOL=true environment variable to be active. Without this, the agent relies solely on regex/grep, which leads to "blind" refactoring errors.2

## **Part VII: Security, Permissions, and Sandboxing**

For security-conscious engineers, understanding the boundaries of OpenCode is paramount. The system relies on a "Permission" model that is robust but has specific "soft" bypasses that must be understood.

### **7.1 Threat Modeling and Permission Bypasses**

The permission system (ask, deny, allow) controls tool execution. However, hierarchies exist that can mask risks.

* **The "Edit" Umbrella**: As noted previously, the edit permission controls multiple underlying tools. A user might think they only allowed "patching" (patch), but if they set edit: allow, they implicitly allowed write (overwriting files from scratch). This grouping simplifies config but obscures risk.  
* **Subagent Escapes**: If a Primary agent has bash: allow but spawns a Subagent that *doesn't* have explicit permissions defined, the behavior can be unpredictable. Typically, if the Subagent inherits the model and context, it effectively operates with the "mandate" of the parent. Explicitly defining permissions in *every* agent Markdown file is the only way to ensure a secure sandbox.14

### **7.2 Telemetry and Data Exfiltration**

OpenCode itself is open source and claims privacy, but the *plugins* and *models* dictate the data flow.

* **OpenTelemetry (OTEL)**: OpenCode supports OpenTelemetry for enterprise monitoring. It can export traces to Azure Monitor, VictoriaMetrics, or any OTLP collector. This is configured via standard OTEL\_\* environment variables (e.g., OTEL\_EXPORTER\_OTLP\_ENDPOINT). This allows enterprises to audit *every* prompt and code generation event across their engineering team, creating a compliance trail.20  
* **Network Forensics**: Analyzing network traffic reveals that while the core binary is quiet, plugins like opencode-antigravity-auth or remote MCP servers initiate their own connections. A firewall rule blocking the main binary might be bypassed by a plugin spawning a child process (like a local Node.js MCP server) that initiates its own outbound connection.

## **Part VIII: Optimal Configuration Blueprints**

Based on the forensic analysis, we define optimal configuration profiles for specific high-value roles.

### **8.1 Profile: The "Agent Developer" (High Autonomy, Max Context)**

* **Goal**: Developing new agents or plugins. Needs maximum visibility and zero friction.  
* **Config**:  
  * **Env**: OPENCODE\_EXPERIMENTAL=true (Enable all features), OPENCODE\_DISABLE\_PRUNE=true (Keep history for debugging).  
  * **TUI**: "tui.scroll\_acceleration": { "enabled": true }.  
  * **JSON**:  
    JSON  
    {  
      "permission": "allow", // Dangerous\! Only for dev.  
      "plugin": \["@dev4s/opencode-dcp@latest", "oh-my-opencode"\],  
      "log\_level": "debug"  
    }

### **8.2 Profile: The "Security Auditor" (Read-Only, Forensic)**

* **Goal**: Auditing codebases for CVEs without modifying files.  
* **Config**:  
  * **Agent**: Define "agent.auditor.mode": "primary".  
  * **JSON**:  
    JSON  
    {  
      "permission": {  
        "\*": "deny",  
        "read": "allow",  
        "grep": "allow",  
        "glob": "allow",  
        "lsp": "allow" // Critical for semantic analysis  
      }  
    }

  * **Agent Definition (auditor.md)**: Explicitly sets tools: { edit: false, write: false, bash: false }. This ensures that the agent literally *cannot* change the state of the system.

### **8.3 Profile: The "Sisyphus Loop" (CI/CD Automated Refactoring)**

* **Goal**: Running "Ultrawork" in a GitHub Action to fix lint errors automatically.  
* **Config**:  
  * **Env Vars**: OPENCODE\_CLIENT=ci, OPENCODE\_AUTO\_SHARE=false.  
  * **CLI**: opencode \--prompt "ulw fix all lint errors" \--quiet \--model anthropic/claude-3-opus.  
  * **Mechanism**: Uses \--quiet to prevent spinner logs from breaking the CI log limit. Uses ulw (Ultrawork) to parallelize the lint checking and fixing, utilizing the headless pipe mode.4

## **Part IX: Troubleshooting and Recovery**

When the complex interplay of plugins and configurations fails, forensic recovery steps are required.

### **9.1 Common Failure Modes**

* **Crash on Boot**: Often caused by a plugin syntax error or a corrupted session DB.  
  * **Fix**: Run with OPENCODE\_DISABLE\_DEFAULT\_PLUGINS=true or use \--print-logs to identify the culprit.  
* **"Skill Bloat" OOM**: The agent runs out of context window space immediately.  
  * **Fix**: Use opencode-tokenscope to identify massive SKILL.md files and remove/refactor them.  
* **Zombie Servers**: The TUI cannot connect, but says a server is running.  
  * **Fix**: Manually delete the lock files in \~/.local/share/opencode and kill any orphaned opencode processes via pkill \-f opencode.

### **9.2 Forensic Log Analysis**

Logs are stored in \~/.local/share/opencode/log/. They are structured JSON.

* **Search for level: "error"**: Identify binary crashes.  
* **Search for tool: "task"**: Trace delegation chains between Primary and Subagents.  
* **Search for provider: "..."**: Verify which model endpoint was actually hit (e.g., verifying that antigravity- models routed correctly).

## **Tables of Reference**

### **Table 1: Complete Configuration Precedence Matrix**

11

| Priority | Source | Location | Typical Use Case |
| :---- | :---- | :---- | :---- |
| **1 (Highest)** | **Environment Variable** | OPENCODE\_API\_KEY, OPENCODE\_CONFIG | Runtime secrets, CI/CD overrides. |
| **2** | **Project Config** | .opencode/opencode.json | Repository-specific tools, linters, agents. |
| **3** | **Custom Config Dir** | $OPENCODE\_CONFIG\_DIR | User profiles (Work vs. Personal). |
| **4** | **Global Config** | \~/.config/opencode/opencode.json | User defaults (Theme, Keybinds). |
| **5 (Lowest)** | **Remote Config** | .well-known/opencode | Corporate policy enforcement. |

### **Table 2: Hidden/Experimental Environment Variables**

2

| Variable | Description | Risk |
| :---- | :---- | :---- |
| OPENCODE\_EXPERIMENTAL | Enables all unstable features. | High (Stability) |
| OPENCODE\_DISABLE\_DEFAULT\_PLUGINS | Boots in "Safe Mode". | Low (Debugging) |
| OPENCODE\_EXPERIMENTAL\_LSP\_TOOL | Enables LSP support. | Low (Performance) |
| OPENCODE\_SERVER\_PASSWORD | Sets basic auth for the HTTP server. | Essential for \--serve |
| OPENCODE\_DISABLE\_PRUNE | Prevents session garbage collection. | Disk Usage |

#### **Works cited**

1. OpenCode \- The Open Source AI Coding Agent That Works With Any Model | YUV.AI Blog, accessed on January 14, 2026, [https://yuv.ai/blog/opencode-the-open-source-ai-coding-agent-that-works-with-any-model](https://yuv.ai/blog/opencode-the-open-source-ai-coding-agent-that-works-with-any-model)  
2. CLI | OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/cli/](https://opencode.ai/docs/cli/)  
3. opencode-ai/opencode: A powerful AI coding agent. Built for the terminal. \- GitHub, accessed on January 14, 2026, [https://github.com/opencode-ai/opencode](https://github.com/opencode-ai/opencode)  
4. code-yeongyu/oh-my-opencode: The Best Agent Harness. Meet Sisyphus \- GitHub, accessed on January 14, 2026, [https://github.com/code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)  
5. Opencode-DCP/opencode-dynamic-context-pruning ... \- GitHub, accessed on January 14, 2026, [https://github.com/Opencode-DCP/opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)  
6. opencode/README.md at main \- GitHub, accessed on January 14, 2026, [https://github.com/opencode-ai/opencode/blob/main/README.md](https://github.com/opencode-ai/opencode/blob/main/README.md)  
7. Troubleshooting | OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/troubleshooting/](https://opencode.ai/docs/troubleshooting/)  
8. TUI | OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/tui/](https://opencode.ai/docs/tui/)  
9. OpenCode config \- shamelessly lifted from the Discord server \- GitHub Gist, accessed on January 14, 2026, [https://gist.github.com/thoroc/1dafddebede4a2577876c844923862aa](https://gist.github.com/thoroc/1dafddebede4a2577876c844923862aa)  
10. Dicklesworthstone/coding\_agent\_session\_search \- GitHub, accessed on January 14, 2026, [https://github.com/Dicklesworthstone/coding\_agent\_session\_search](https://github.com/Dicklesworthstone/coding_agent_session_search)  
11. Config | OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/config/](https://opencode.ai/docs/config/)  
12. Tools | OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/tools/](https://opencode.ai/docs/tools/)  
13. Models | OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/models/](https://opencode.ai/docs/models/)  
14. Agents \- OpenCode, accessed on January 14, 2026, [https://opencode.ai/docs/agents/](https://opencode.ai/docs/agents/)  
15. Your Senior Devs Don't Scale. Your OpenCode Agents Can. | by JP Caparas \- Medium, accessed on January 14, 2026, [https://jpcaparas.medium.com/your-senior-devs-dont-scale-your-opencode-agents-can-e2ecf2d04548](https://jpcaparas.medium.com/your-senior-devs-dont-scale-your-opencode-agents-can-e2ecf2d04548)  
16. NoeFabris/opencode-antigravity-auth: Enable Opencode to authenticate against Antigravity (Google's IDE) via OAuth so you can use Antigravity rate limits and access models like gemini-3-pro and claude-opus-4-5-thinking with your Google credentials. \- GitHub, accessed on January 14, 2026, [https://github.com/NoeFabris/opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)  
17. dev4s/opencode-dcp \- NPM, accessed on January 14, 2026, [https://www.npmjs.com/package/%40dev4s%2Fopencode-dcp](https://www.npmjs.com/package/%40dev4s%2Fopencode-dcp)  
18. ramtinJ95/opencode-tokenscope: Comprehensive token usage analysis and cost tracking for opencode sessions \- GitHub, accessed on January 14, 2026, [https://github.com/ramtinJ95/opencode-tokenscope](https://github.com/ramtinJ95/opencode-tokenscope)  
19. OpenTelemetry MCP Server \- LobeHub, accessed on January 14, 2026, [https://lobehub.com/mcp/liatrio-labs-otel-instrumentation-mcp](https://lobehub.com/mcp/liatrio-labs-otel-instrumentation-mcp)  
20. Vibe coding tools observability with VictoriaMetrics Stack and OpenTelemetry, accessed on January 14, 2026, [https://victoriametrics.com/blog/vibe-coding-observability/](https://victoriametrics.com/blog/vibe-coding-observability/)  
21. pedramamini/Maestro: Agent Orchestration Command Center \- GitHub, accessed on January 14, 2026, [https://github.com/pedramamini/Maestro](https://github.com/pedramamini/Maestro)