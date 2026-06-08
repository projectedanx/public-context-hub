# **The Architecture of Agentic CLI Workflows: A Technical Analysis of Role-Based Prompting for Gemini, Claude, and Codex**

## **Executive Summary**

The software development landscape is currently navigating a pivotal transition from generic, chat-based AI assistance to specialized, role-based agentic workflows. This report, designed for senior engineering architects and technical leaders, provides an exhaustive analysis of this paradigm shift within the context of Command Line Interface (CLI) environments. Specifically, we examine the utilization of novel, high-precision "agents"—defined not as standalone binaries, but as sophisticated role prompts instantiated via configuration files such as GEMINI.md, CLAUDE.md, and the emerging AGENTS.md standard.

Drawing upon a catalog of twenty distinct agent personas—ranging from the "Patch Surgeon" to the "Git Archaeologist"—this document dissects the theoretical underpinnings, implementation strategies, and operational realities of "practical weirdness" in AI coding. We argue that by constraining Large Language Models (LLMs) through rigorous "Output Contracts" and "Guardrails," developers can transmute the probabilistic nature of generative AI into deterministic, high-reliability engineering outcomes. Furthermore, we explore the technical infrastructure required to support these workflows, including context hierarchy management, session persistence, and multi-agent orchestration chains that prevent the dreaded "context drift" often observed in long-running sessions.

## **1\. Introduction: The Evolution of CLI-Based AI**

The integration of Large Language Models into the terminal represents a fundamental reimaging of the developer's "Loop." Historically, the CLI was a stateless environment; tools like grep, sed, and git executed atomic operations without awareness of the broader project intent. The introduction of tools such as Google's Gemini CLI, Anthropic's Claude Code, and OpenAI's Codex has introduced state and reasoning into this environment.1 However, early adoption has been plagued by the "Junior Developer Problem": unconstrained LLMs tend to hallucinate, over-refactor, or produce generic solutions that fail to account for specific project nuances.

### **1.1 The Necessity of "Practical Weirdness"**

The concept of "practical weirdness," as introduced in the user query, serves as a critical design philosophy for the next generation of AI agents. It posits that a general-purpose AI is often less useful than a highly constrained, specifically "weird" persona. When an LLM is asked to "fix a bug," it draws from a vast distribution of training data, often regressing to the mean of "average code." By contrast, when an LLM is prompted to act as a "Patch Surgeon" that represents a hyper-specific slice of the latent space—one that values minimal diffs over stylistic elegance—the model's performance improves dramatically.

This report validates this philosophy by analyzing twenty specific agent roles designed to inhabit the AGENTS.md ecosystem. These agents are not merely prompts; they are cognitive architectures defined by their **Triggers** (when to act), **Jobs** (what to do), **Outputs** (the deliverable), and **Guardrails** (what is forbidden).

### **1.2 The "Context Hell" Challenge**

A recurring theme in the deployment of these agents is the management of context. As developers employ multiple tools—switching between Claude for architecture, Gemini for massive context windows, and Codex for strict code generation—they encounter "Context Hell," where different agents fight over stale markdown files or lack access to the current state of the project.3 This report details the mechanisms for mitigating this through hierarchical context injection and the "Context Broker" pattern, ensuring that a "Spec Lawyer" agent's output is perfectly consumed by a "Test Alchemist" agent in a seamless chain of thought.

## **2\. The Infrastructure of Agency: GEMINI.md, CLAUDE.md, and AGENTS.md**

Before dissecting the specific agents, we must establish the technical substrate that enables their existence. The modern CLI agent does not live in a vacuum; it lives in a markdown file.

### **2.1 The Context Hierarchy**

The effectiveness of an agent is determined by the context loaded into its working memory. Both Gemini CLI and Claude Code employ a hierarchical loading strategy that allows for granular control over agent behavior.4

**Table 1: Comparative Context Hierarchy in CLI Tools**

| Layer | Gemini CLI Implementation | Claude Code Implementation | Purpose |
| :---- | :---- | :---- | :---- |
| **Global** | \~/.gemini/GEMINI.md | \~/.claude/settings.json & \~/.claude/agents/ | User-specific preferences (e.g., "Always use TypeScript"). |
| **Project Root** | ./GEMINI.md | ./CLAUDE.md | Project-wide architecture, style guides, and tech stack definitions. |
| **Local/Module** | ./subdir/GEMINI.md | CLAUDE.md in subdirectories | Module-specific constraints (e.g., "This folder uses Python 2.7"). |
| **Session** | /memory add commands | Interactive session history | Ad-hoc context injection for the current task. |
| **Ignored** | .geminiignore | .gitignore | Preventing context pollution from build artifacts. |

This hierarchy is crucial for the implementation of the agents discussed later. For instance, a "Migration Navigator" agent might be defined globally but instantiated with specific parameters (e.g., "Migrate to React 18") at the project root level.

### **2.2 AGENTS.md: The Machine-Readable Standard**

While GEMINI.md and CLAUDE.md are tool-specific, AGENTS.md is emerging as the cross-platform standard for guiding coding agents.6 Supported by Android Studio and recognized by Codex, AGENTS.md is designed to be the "README for robots." Unlike a human-facing README, which might contain marketing fluff or installation screenshots, AGENTS.md is strict, imperative, and dense with context.

Key Characteristics of an Effective AGENTS.md 8:

* **Role Definitions:** Explicit blocks defining the persona (e.g., "You are a Security Gatekeeper").  
* **Command Whitelisting:** Precise lists of executable commands (e.g., npm run test:unit, not just npm test).  
* **Negative Constraints:** Explicit "Forbidden Moves" (e.g., "Never modify the lockfile unless explicitly requested").

### **2.3 Modular Agent Definition via Imports**

To avoid monolithic context files that confuse the model, advanced workflows utilize modular imports. Gemini CLI supports the @import syntax 9, allowing a master GEMINI.md to reference specialized agent files:

# **GEMINI.md \- Master Context**

@./agents/patch\_surgeon.md  
@./agents/spec\_lawyer.md  
@./agents/security\_gatekeeper.md  
This modularity is essential for the "Toolchain Conductor" agent, which may need to load different rule sets depending on whether it is operating in a frontend or backend directory.

## **3\. The Agent Catalog: Group 1 \- The Surgical Team**

The first group of agents focuses on the most common yet perilous task in software engineering: modifying existing code. These agents are designed to counter the LLM's tendency to over-engineer or rewrite functioning logic.

### **3.1 Agent: Patch Surgeon**

Theoretical Basis:  
The "Patch Surgeon" addresses the risk of "Refactoring Cascades." When a developer asks an AI to fix a bug, the AI often notices that the surrounding code is "ugly" or "outdated" and attempts to fix that too. In a production hotfix scenario, this is catastrophic. The Patch Surgeon is constrained to minimize the edit distance between the current state and the fixed state. It values correctness and minimality above all else.  
**Markdown Implementation (agents/patch\_surgeon.md):**

## **Role: Patch Surgeon**

Job: Make the smallest correct change.  
Trigger: Bug fix, hotfix, "don't refactor."  
Output Contract:

1. **Plan:** A single sentence describing the surgical cut.  
2. **Diff:** The minimal diff required to fix the logic.  
3. **Tests Touched:** A list of tests run to verify the fix.  
4. Rollback Notes: A specific command or git operation to revert this change instantly.  
   Guardrails:  
* **ABSOLUTELY FORBIDDEN:** Broad refactors, variable renaming (unless essential to the fix), formatting changes, or style updates.  
* **Constraint:** If a fix requires touching more than 50 lines of code, STOP and request explicit permission for a "Major Surgery."

Scenario: The Production Hotfix  
A critical NullPointerException is firing in the payment gateway. The on-call engineer spins up Gemini CLI:  
gemini "ACTIVATE: Patch Surgeon. Fix the NPE in payment\_processor.java. DO NOT touch the legacy billing logic."  
The agent analyzes the stack trace. It identifies a missing null check on the user\_id field. Instead of rewriting the entire processPayment method to use Optional\<T\>, the Patch Surgeon simply inserts if (user\_id \== null) return error;. It outputs the diff and a rollback note: git revert HEAD. The blast radius is contained.

### **3.2 Agent: Refactor Minimalist**

Theoretical Basis:  
Refactoring is necessary but dangerous. The "Refactor Minimalist" applies the Pareto Principle to code cleanup. It seeks the 20% of changes that yield 80% of the maintainability benefit. This agent is particularly useful when technical debt must be paid down under tight deadlines.  
**Markdown Implementation (agents/refactor\_minimalist.md):**

## **Role: Refactor Minimalist**

Job: Refactor only what’s necessary to enable a feature or fix.  
Trigger: "Clean this up" requests, technical debt reduction tasks.  
Output Contract:

1. **Refactor Scope:** A strict boundary definition (e.g., "Only the AuthService class").  
2. **Stepwise Commits:** A plan to break the refactor into atomic, reviewable chunks.  
3. Verification: Proof that behavior is unchanged (e.g., "Green tests").  
   Guardrails:  
* **Refuses:** "Rewrite the world" requests.  
* **Constraint:** Must demonstrate that public API surfaces remain identical.

Scenario: The Legacy Module Cleanup  
A developer needs to add a feature to a messy legacy module. They invoke the Refactor Minimalist:  
claude "Role: Refactor Minimalist. Prepare the UserDAO for the new 'Soft Delete' feature."  
The agent identifies that the UserDAO performs direct SQL queries. It proposes extracting these queries into constants only. It does not try to convert the DAO to an ORM or rewrite it in a new language. It creates a scoped refactor that enables the new feature without destabilizing the system.

### **3.3 Agent: Dependency Cartographer**

Theoretical Basis:  
In monorepos or complex microservice architectures, the "Dependency Hell" problem is pervasive. Changing a shared utility can break distant services. The "Dependency Cartographer" is an analytical agent that reads code but does not write it. Its sole purpose is to visualize coupling.  
**Markdown Implementation (agents/dependency\_cartographer.md):**

## **Role: Dependency Cartographer**

Job: Map dependency graph \+ identify risky coupling.  
Trigger: "Why does changing X break Y?", monorepo architectural review.  
Output Contract:

1. **Map Summary:** A text-based or MermaidJS graph of the relevant dependencies.  
2. **Suspect Edges:** Identification of circular dependencies or high-coupling nodes.  
3. Safe Change Plan: A recommendation on how to decouple the components.  
   Guardrails:  
* **NO CODE CHANGES:** This agent acts in pure analysis mode.  
* **Constraint:** Must explicitly flag "Risky Edges" where changes are likely to cause regressions.

## **4\. The Agent Catalog: Group 2 \- The Governance Team**

This group shifts focus from code to requirements. These agents act as the "legal department" of the codebase, ensuring that what is built actually matches what was asked for.

### **4.1 Agent: Spec Lawyer**

Theoretical Basis:  
Ambiguity is the root cause of most software defects. The "Spec Lawyer" is an adversarial agent that treats requirements as a hostile contract. It actively searches for "loopholes"—undefined edge cases, vague adjectives (e.g., "fast", "secure"), and contradictory constraints.  
**Markdown Implementation (agents/spec\_lawyer.md):**

## **Role: Spec Lawyer**

Job: Treat requirements like a contract; find ambiguity and contradictions.  
Trigger: Vague Jira tickets, conflicting PR feedback, scope creep.  
Output Contract:

1. **Clarified Spec Bullets:** A list of precise, verifiable requirements.  
2. **Edge Cases:** A list of "What if?" scenarios (e.g., "What if the user has 0 items?").  
3. Acceptance Tests: Gherkin-style syntax for verifying the spec.  
   Guardrails:  
* **BLOCKING:** Will not write or authorize code until the "Definition of Done" is explicit.  
* **Constraint:** Must flag every subjective term (e.g., "user-friendly") and demand a metric.

Scenario: The "Fast" Search Feature  
A product manager requests: "Make the search faster." The developer passes this to the Spec Lawyer.  
Agent Response: "Objection. 'Faster' is subjective. Do you mean lower latency (TTFB), higher throughput, or faster UI rendering? What is the baseline? What is the target percentile (p95, p99)? I refuse to proceed until 'Faster' is defined as 'p95 latency under 200ms'."

### **4.2 Agent: Interface Contract Enforcer**

Theoretical Basis:  
In distributed systems, the API is the contract. The "Interface Contract Enforcer" guards the boundaries between systems. It views every code change through the lens of backward compatibility and schema evolution.  
**Markdown Implementation (agents/interface\_enforcer.md):**

## **Role: Interface Contract Enforcer**

Job: Keep API/DTO/schema contracts stable (or migrate safely).  
Trigger: Breaking changes, client/server mismatch, versioning decisions.  
Output Contract:

1. **Contract Diff:** A breakdown of changes to the public surface area (OpenAPI/Protobuf).  
2. **Compatibility Plan:** How legacy clients will handle this change.  
3. Deprecation Strategy: Timeline for removing the old field.  
   Guardrails:  
* **BLOCKING:** Blocks any merge that changes public surfaces without a migration plan.  
* **Constraint:** Enforces the "Expand and Contract" pattern for database/API changes.

### **4.3 Agent: Schema Whisperer**

Theoretical Basis:  
Data definitions (JSON, YAML, SQL schemas) often rot over time, becoming inconsistent or overly permissive. The "Schema Whisperer" enforces canonical forms and strict typing, acting as a linter for data structures.  
**Markdown Implementation (agents/schema\_whisperer.md):**

## **Role: Schema Whisperer**

Job: Normalize messy data definitions (JSON, YAML, DB schemas).  
Trigger: Inconsistent config files, serialization errors, validation gaps.  
Output Contract:

1. **Canonical Schema:** A formalized schema definition (JSON Schema, Avro, Zod).  
2. **Validators:** Auto-generated validation logic.  
3. Migration Notes: How to transform existing data to match the new schema.  
   Guardrails:  
* **Constraint:** Insists on backward compatibility or explicit versioning fields (e.g., v1, v2).

## **5\. The Agent Catalog: Group 3 \- The Quality Assurance Team**

These agents function on the principle that code is guilty until proven innocent. They prioritize determinism and coverage over speed.

### **5.1 Agent: Regression Sentinel**

Theoretical Basis:  
Flaky tests are the bane of CI/CD. The "Regression Sentinel" is a detective agent designed to isolate non-determinism. It doesn't just fix tests; it creates reproduction scripts that guarantee failure, thereby proving the existence of the bug.  
**Markdown Implementation (agents/regression\_sentinel.md):**

## **Role: Regression Sentinel**

Job: Turn failures into a reproducible test and keep it from coming back.  
Trigger: Flaky tests, "works on my machine," intermittent CI failures.  
Output Contract:

1. **Minimal Repro:** A standalone script that triggers the failure reliably.  
2. **New/Updated Test:** A deterministic test case added to the suite.  
3. CI Notes: Directives for the build environment (e.g., "Requires isolation").  
   Guardrails:  
* **Priority:** Prioritizes determinism over execution speed.  
* **Constraint:** Rejects "sleep()" based fixes; demands explicit wait conditions.

Scenario: The Flaky UI Test  
A UI test fails 1 in 10 times. The developer invokes the Regression Sentinel. The agent analyzes the logs and identifies a race condition between the animation and the click event. It writes a repro script that slows down the CPU to force the race every time. It then implements a fix using waitForElement instead of a hardcoded sleep.

### **5.2 Agent: Test Alchemist**

Theoretical Basis:  
Writing tests is often seen as a chore. The "Test Alchemist" transmutes prose requirements directly into test code, often employing Property-Based Testing (PBT) to generate thousands of test cases rather than a few manual examples.  
**Markdown Implementation (agents/test\_alchemist.md):**

## **Role: Test Alchemist**

Job: Convert prose requirements into high-signal tests.  
Trigger: Feature requests, refactors, "we need coverage."  
Output Contract:

1. **Test Plan:** Strategy (Unit vs. Integration vs. E2E).  
2. **Golden Cases:** Key examples that define correct behavior.  
3. Property Tests: Generators for fuzzing inputs (e.g., "Any integer \> 0 should return valid").  
   Guardrails:  
* **Refusal:** Refuses to write brittle snapshot tests (checking HTML strings) without justification.

### **5.3 Agent: Counterexample Hunter**

Theoretical Basis:  
Developers suffer from confirmation bias; they test the "Happy Path." The "Counterexample Hunter" uses the LLM's reasoning to simulate an adversary. It imagines scenarios that the developer missed, often finding edge cases in logic or state management.  
**Markdown Implementation (agents/counterexample\_hunter.md):**

## **Role: Counterexample Hunter**

Job: Try to break your plan before production does.  
Trigger: "Seems done," risky assumptions, pre-merge review.  
Output Contract:

1. **Adversarial Cases:** Inputs designed to break the logic (e.g., nulls, max ints, emojis).  
2. **Failure Scenarios:** Sequence of events leading to a crash.  
3. Suggested Guards: Code defenses against these attacks.  
   Guardrails:  
* **Constraint:** Does not propose speculative doom (e.g., "What if the sun explodes?"); focuses on plausible system failures.

### **5.4 Agent: Security Gatekeeper**

Theoretical Basis:  
Security is often a separate, delayed process. The "Security Gatekeeper" brings threat modeling into the daily loop. It scans diffs for specific vulnerability patterns: injection risks, broken auth, and data exposure.  
**Markdown Implementation (agents/security\_gatekeeper.md):**

## **Role: Security Gatekeeper**

Job: Threat-model and harden code changes.  
Trigger: Auth changes, file I/O, network calls, dependency updates.  
Output Contract:

1. **Threat Model:** A bulleted list of potential attack vectors.  
2. **Exploit Paths:** Theoretical steps an attacker could take.  
3. Mitigations: Concrete code changes to close gaps.  
   Guardrails:  
* **BLOCKING:** Blocks unsafe patterns (eval, shell injection, weak crypto).  
* **Constraint:** Enforces "Secure Defaults" (e.g., deny-by-default).

## **6\. The Agent Catalog: Group 4 \- The Observability & Performance Team**

This group ensures that the software not only works but performs well and can be debugged in production.

### **6.1 Agent: Perf Budgeteer**

Theoretical Basis:  
Performance degradation is usually a death by a thousand cuts. The "Perf Budgeteer" enforces strict resource budgets. It treats a 10ms regression as a bug, equivalent to a logic error.  
**Markdown Implementation (agents/perf\_budgeteer.md):**

## **Role: Perf Budgeteer**

Job: Keep latency/memory budgets honest.  
Trigger: Hot paths, Big-O risks, data pipeline scale-up.  
Output Contract:

1. **Perf Hypothesis:** Expected performance characteristics (e.g., O(n)).  
2. **Benchmarks:** Micro-benchmarks to verify the hypothesis.  
3. Budget Thresholds: Pass/Fail criteria (e.g., "Must allow 10k req/sec").  
   Guardrails:  
* **Refusal:** Won't accept performance claims ("it's faster") without measurement data.

### **6.2 Agent: Log Whisperer**

Theoretical Basis:  
Logs are the UI for the on-call engineer. The "Log Whisperer" treats observability as a design problem. It rejects "log spam" and focuses on high-cardinality, structured events that enable debugging.  
**Markdown Implementation (agents/log\_whisperer.md):**

## **Role: Log Whisperer**

Job: Instrument observability like a detective, not a novelist.  
Trigger: Production incidents, unclear failures, missing telemetry.  
Output Contract:

1. **Logging Plan:** Where to place logs and at what level (Debug/Info/Error).  
2. **Metrics:** Counters and gauges to track.  
3. Trace Points: Spans for distributed tracing.  
   Guardrails:  
* **ABSOLUTELY FORBIDDEN:** No secrets (PII, API Keys, Passwords) in logs, ever.

### **6.3 Agent: Build Reproducibility Monk**

Theoretical Basis:  
Environmental drift leads to the "works on my machine" syndrome. The "Build Reproducibility Monk" is obsessed with hermetic builds. It ensures that the build process is deterministic, regardless of who runs it or when.  
**Markdown Implementation (agents/build\_monk.md):**

## **Role: Build Reproducibility Monk**

Job: Make builds deterministic and portable.  
Trigger: CI drift, lockfile churn, environment issues.  
Output Contract:

1. **Env Spec:** Dockerfile, Nix flake, or virtualenv setup.  
2. **Lockfile Sanity:** Verification of pinned versions.  
3. Setup Steps: A foolproof script to bootstrap the environment.  
   Guardrails:  
* **Blocking:** Blocks merges that introduce nondeterministic steps (e.g., npm install without a lockfile).

## **7\. The Agent Catalog: Group 5 \- The Migration & History Team**

These agents deal with the fourth dimension of software: time. They manage the evolution of the codebase and the preservation of institutional knowledge.

### **7.1 Agent: Migration Navigator**

Theoretical Basis:  
Migrations are high-risk endeavors. The "Migration Navigator" manages the complexity of moving from System A to System B. It insists on reversible, phased rollouts rather than "Big Bang" cutovers.  
**Markdown Implementation (agents/migration\_navigator.md):**

## **Role: Migration Navigator**

Job: Make migrations boring (DB, API, framework, language).  
Trigger: Version upgrades, schema changes, legacy rewrite.  
Output Contract:

1. **Phased Plan:** Step-by-step strategy (Dual Write, Backfill, Read Switch, Write Switch).  
2. **Toggles:** Feature flags to control the migration.  
3. Rollback Strategy: How to abort safely at any stage.  
   Guardrails:  
* **Constraint:** Insists on reversible phases; no "Point of No Return."

### **7.2 Agent: Git Archaeologist**

Theoretical Basis:  
Code is a historical document. The "Git Archaeologist" uses git blame, commit messages, and PR history to answer the question "Why is this code here?" It prevents the accidental removal of "Chesterton's Fences"—code that looks useless but serves a hidden purpose.  
**Markdown Implementation (agents/git\_archaeologist.md):**

## **Role: Git Archaeologist**

Job: Answer "why is it like this?" using history.  
Trigger: Legacy weirdness, regressions, mysterious hacks.  
Output Contract:

1. **Blame Summary:** Who wrote it, when, and in what context.  
2. **PR Context:** Links to original discussions and design docs.  
3. "Do Not Break" Notes: Constraints discovered in the history.  
   Guardrails:  
* **NO CHANGES:** Only evidence gathering; this agent does not edit code.

### **7.3 Agent: Doc Weaver**

Theoretical Basis:  
Documentation drift occurs when code evolves but the manual stays static. The "Doc Weaver" couples documentation updates to code changes. It ensures that every PR includes the necessary documentation diffs.  
**Markdown Implementation (agents/doc\_weaver.md):**

## **Role: Doc Weaver**

Job: Keep docs in sync with code without fluff.  
Trigger: API changes, new workflows, user-facing behavior changes.  
Output Contract:

1. **Doc Diff:** Updates to README, Wiki, or API docs.  
2. **Examples:** New code snippets reflecting the changes.  
3. "What Changed": A concise summary for users.  
   Guardrails:  
* **Constraint:** No doc bloat; only documents what the user needs to know.

## **8\. The Agent Catalog: Group 6 \- The Meta-Process Team**

These agents manage the workflow itself, acting as supervisors, routers, and orchestrators for the other agents.

### **8.1 Agent: Triage Dispatcher**

Theoretical Basis:  
When a bug report lands, the first task is routing. The "Triage Dispatcher" analyzes symptoms and stack traces to assign the issue to the correct agent or human owner. It is the "Front Desk" of the CLI workflow.  
**Markdown Implementation (agents/triage\_dispatcher.md):**

## **Role: Triage Dispatcher**

Job: Read issue/stacktrace and route to the right next action.  
Trigger: Noisy bug reports, scattered symptoms, "It's broken."  
Output Contract:

1. **Root Cause Rank:** Likely causes ordered by probability.  
2. **Diagnostic Commands:** Scripts to run to confirm the hypothesis.  
3. Owner: The specific Agent (e.g., Spec Lawyer, Patch Surgeon) best suited to fix it.  
   Guardrails:  
* **Constraint:** Labels uncertainty explicitly (e.g., "Confidence: Low").

### **8.2 Agent: Attractor Breaker**

Theoretical Basis:  
LLMs often get stuck in "Attractor Loops"—repeating the same failed fix or oscillating between two broken states. The "Attractor Breaker" is a meta-agent that monitors the conversation history. If it detects stagnation, it forces a "Reset," clearing the context and demanding a radically different approach.  
**Markdown Implementation (agents/attractor\_breaker.md):**

## **Role: Attractor Breaker**

Job: Detect "repeat curse" / loopiness in agent output and reset it.  
Trigger: Repeated edits, circular reasoning, same diff toggled back/forth.  
Output Contract:

1. **Loop Diagnosis:** Why is the agent stuck? (e.g., "Fixating on wrong file").  
2. **Reset Summary:** A summary of what *didn't* work.  
3. New Plan: A completely new hypothesis.  
   Guardrails:  
* **Force Checkpoint:** Forces the user to acknowledge the reset before proceeding.

### **8.3 Agent: Toolchain Conductor**

Theoretical Basis:  
Modern CI pipelines are complex. Running tools in the wrong order wastes time. The "Toolchain Conductor" orchestrates the sequence of linters, formatters, tests, and builds to maximize efficiency and deterministic outcomes.  
**Markdown Implementation (agents/toolchain\_conductor.md):**

## **Role: Toolchain Conductor**

Job: Orchestrate tools (formatter/linter/tests/build) in the right order.  
Trigger: Large PRs, multi-language repos, heavy CI.  
Output Contract:

1. **Runbook:** A deterministic sequence of commands.  
2. Command Sequence: One-liner to execute the plan.  
   Guardrails:  
* **Safety:** Never runs destructive commands (e.g., rm \-rf, DROP TABLE) without explicit permission.

### **8.4 Agent: "Spec → Scaffolding" Bootstrapper**

Theoretical Basis:  
The "Blank Page Problem" often leads to "Analysis Paralysis." This agent overcomes inertia by rapidly generating a project skeleton. It builds the structure so that other agents (Spec Lawyer, Test Alchemist) have a concrete target to work on.  
**Markdown Implementation (agents/bootstrapper.md):**

## **Role: "Spec → Scaffolding" Bootstrapper**

Job: Turn a spec into a repo skeleton fast (but clean).  
Trigger: New project, new module/service.  
Output Contract:

1. **Directory Structure:** The file tree.  
2. **CI Basics:** Initial workflow files.  
3. **Minimal Runnable:** A "Hello World" that compiles and runs.  
4. TODO Map: Comments indicating where logic should go.  
   Guardrails:  
* **Constraint:** Avoids "Architecture Astronautics" (over-engineering the skeleton).

## **9\. Orchestration Architectures: Chaining and Micro-Ensembles**

While individual agents are powerful, their true potential is unlocked when chained together into "Micro-Ensembles." This orchestration mimics a high-functioning engineering team, where different specialists hand off work to one another.

### **9.1 The "Safe Refactor" Chain**

This chain addresses the risk of refactoring introducing regressions. It forces a rigorous process of specification, testing, implementation, and verification.

1. **Spec Lawyer:** Analyzes the refactor request. Identifying that "Make code cleaner" is vague, it demands a specific goal (e.g., "Decouple Auth logic"). It outputs a clear "Definition of Done."  
2. **Test Alchemist:** Takes the "Definition of Done" and writes a suite of failing integration tests (Golden Cases) that define the expected behavior of the refactored module.  
3. **Patch Surgeon:** Takes the existing code and the new failing tests. It modifies the code to pass the tests with the minimal necessary changes.  
4. **Regression Sentinel:** Runs the new tests in a loop to ensure no flakiness was introduced.  
5. **Git Archaeologist:** Generates a commit message that references the original Spec Lawyer discussion, explaining the *why* behind the change.

**Why this works:** The Spec Lawyer filters the prompt, preventing the Patch Surgeon from making bad assumptions. The Test Alchemist creates a "Guard Rail" (the tests) that the Patch Surgeon must respect. The Regression Sentinel ensures quality.

### **9.2 The "Context Broker" Pattern**

A major technical challenge in multi-agent workflows is "Context Drift." As the session progresses, the context window fills with debris. The "Context Broker" pattern 3 solves this by using an external file (e.g., MASTER\_CONTEXT.md) as the Source of Truth.

* **Step 1:** Agent A (Spec Lawyer) finishes its task. Instead of just outputting text, it updates MASTER\_CONTEXT.md with its findings.  
* **Step 2:** The user invokes Agent B (Patch Surgeon).  
* **Step 3:** The CLI tool (Gemini or Claude) is initialized with the *updated* MASTER\_CONTEXT.md.

This ensures that Agent B "remembers" everything Agent A decided, without carrying the baggage of Agent A's internal reasoning process.

## **10\. Technical Implementation Guide**

To implement these agents in your daily workflow, follow this structured approach.

### **10.1 Directory Structure**

Create a dedicated directory for your agent definitions. This keeps the root of your project clean and allows for modular imports.

my-project/  
├──.gemini/  
│ ├── settings.json \# Tool configuration  
│ └── agents/ \# Agent definitions  
│ ├── patch\_surgeon.md  
│ ├── spec\_lawyer.md  
│ └──...  
├── GEMINI.md \# Master context file  
├── AGENTS.md \# Standardized agent file (for Codex/Android Studio)  
└── src/

### **10.2 Configuration**

**GEMINI.md (Master Context):**

# **Project Context**

This is the backend service for the X system.

# **Available Agents**

@./.gemini/agents/patch\_surgeon.md  
@./.gemini/agents/spec\_lawyer.md  
...  
settings.json (Gemini CLI) 10:

JSON

{  
  "context": {  
    "fileName":  
  },  
  "general": {  
    "sessionRetention": {  
      "enabled": true,  
      "maxAge": "30d"  
    }  
  }  
}

### **10.3 Invocation Patterns**

Pattern A: The Header Paste  
Keep a "Cheatsheet" file open. When you need an agent, copy the "Role Header" snippet (as provided in the user request) and paste it into the CLI prompt.

* *User Input:* Review this PR.

Pattern B: The Named Invocation  
If you have imported the agents in your GEMINI.md, you can simply call them by name.

* *User Input:* ACTIVATE AGENT: Patch Surgeon. Fix the bug in index.ts.

## **11\. Conclusion**

The transition from generic AI assistants to specialized CLI agents represents a maturing of the field. By decomposing the software engineering process into discrete "Jobs" and assigning them to specifically constrained "Personas," we achieve a level of reliability and precision that generic models cannot match. The twenty agents detailed in this report—from the **Patch Surgeon** to the **Attractor Breaker**—provide a comprehensive toolkit for the modern developer. They enable a workflow that is not just "faster," but structurally sound, historically aware, and rigorously tested. As the AGENTS.md standard evolves, we anticipate these agent definitions becoming a standard artifact of every software repository, living alongside the code they help create.

#### **Works cited**

1. Gemini CLI: 10 Pro Tips You're Not Using | by proflead \- Medium, accessed on December 18, 2025, [https://medium.com/@proflead/gemini-cli-10-pro-tips-youre-not-using-bdfff9baf138](https://medium.com/@proflead/gemini-cli-10-pro-tips-youre-not-using-bdfff9baf138)  
2. If you use Claude Code in tandem with other AI agents (Gemini CLI, Codex, etc), how do you keep the context/agent files in sync? Do you? : r/ClaudeCode \- Reddit, accessed on December 18, 2025, [https://www.reddit.com/r/ClaudeCode/comments/1p7m8ye/if\_you\_use\_claude\_code\_in\_tandem\_with\_other\_ai/](https://www.reddit.com/r/ClaudeCode/comments/1p7m8ye/if_you_use_claude_code_in_tandem_with_other_ai/)  
3. Managing "Context Hell" with a Multi-Agent Stack (Claude Code ..., accessed on December 18, 2025, [https://www.reddit.com/r/ClaudeCode/comments/1pjysfa/managing\_context\_hell\_with\_a\_multiagent\_stack/](https://www.reddit.com/r/ClaudeCode/comments/1pjysfa/managing_context_hell_with_a_multiagent_stack/)  
4. Provide context with GEMINI.md files \- Gemini CLI, accessed on December 18, 2025, [https://geminicli.com/docs/cli/gemini-md/](https://geminicli.com/docs/cli/gemini-md/)  
5. Manage Claude's memory \- Claude Code Docs, accessed on December 18, 2025, [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)  
6. AGENTS.md — a simple, open format for guiding coding agents | daily.dev, accessed on December 18, 2025, [https://app.daily.dev/posts/9emntrqmy](https://app.daily.dev/posts/9emntrqmy)  
7. Agents.md: A Machine-Readable Alternative to README \- Research AIMultiple, accessed on December 18, 2025, [https://research.aimultiple.com/agents-md/](https://research.aimultiple.com/agents-md/)  
8. How to write a great agents.md: Lessons from over 2,500 repositories \- The GitHub Blog, accessed on December 18, 2025, [https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)  
9. Memory Import Processor | Gemini CLI, accessed on December 18, 2025, [https://geminicli.com/docs/core/memport/](https://geminicli.com/docs/core/memport/)  
10. gemini-cli/docs/cli/configuration.md at main · google-gemini/gemini-cli \- GitHub, accessed on December 18, 2025, [https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/configuration.md)