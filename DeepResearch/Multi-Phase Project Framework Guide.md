# **Operational Framework for Agentic Code Modernization: A Comprehensive Guide to the Multi-Phase Methodology**

## **Executive Summary**

The modernization of legacy enterprise systems has historically been categorized as a high-risk, capital-intensive necessity. Organizations managing critical infrastructure on mainframes—utilizing languages such as COBOL, PL/I, and JCL—face a compounding crisis: the attrition of subject matter experts (SMEs), the increasing cost of technical debt, and the inability of monolithic architectures to support modern digital agility. Traditional methodologies, ranging from "Big Bang" rewrites to manual "lift-and-shift" operations, have suffered from high failure rates due to the sheer complexity of undocumented business logic and the fragility of interdependencies.

However, the advent of generative AI and, more specifically, agentic coding frameworks, has introduced a paradigm shift. We are moving from a model of "computer-aided software engineering" to "AI-driven software industrialization." This report articulates a rigorous, six-phase framework for leveraging autonomous AI agents—specifically utilizing the OpenAI Codex ecosystem—to execute complex modernization projects. This methodology, rooted in the **ExecPlan** governance model and the **AGENTS.md** context protocol, provides a structured path from initial discovery to scalable industrialization. By treating AI not as a mere productivity tool but as a governed workforce operating within strict architectural guardrails, enterprises can achieve parity-verified modernization at a velocity previously unattainable.

This document serves as a detailed operational manual for enterprise architects and program directors. It dissects the lifecycle of an agentic modernization project, exploring the technical mechanics of the Codex CLI, the governance of AI-generated artifacts, and the critical "human-in-the-loop" validation strategies required to ensure that the speed of AI does not compromise the stability of mission-critical systems.

## ---

**Phase 0: Set up AGENTS and PLANS**

**Objective:** Establish team roles and initial project framework

The foundational phase of any agentic workflow is not technical implementation, but the establishment of a "constitutional" framework for the AI. Unlike human engineers who bring years of implicit cultural and technical context to a project, an AI agent begins as a tabula rasa with vast general knowledge but zero specific organizational context. Phase 0 focuses on encoding this context into persistent artifacts that govern the agent's behavior, ensuring that every subsequent action aligns with the enterprise's architectural and operational standards.

### **0.1 Establishing the Governance Architecture: AGENTS.md**

The cornerstone of this framework is the **AGENTS.md** file. This document acts as the primary directive for the AI agent, functioning as a persistent system prompt that is injected into the model's context window at the start of every session.1 It is distinct from a human-facing README.md; while a README explains *what* the software does, an AGENTS.md explains *how* the software must be built, tested, and maintained.

#### **0.1.1 Defining Agent Roles and Responsibilities**

Within the AGENTS.md file, the organization must explicitly define the persona and operational boundaries of the agent. This involves "role prompting" at a repository level.

* **The Architect Agent:** Responsible for high-level design and structural decisions. Instructions for this role might include directives to "prefer composition over inheritance" or "enforce domain-driven design boundaries."  
* **The Implementation Agent:** Tasked with writing syntax. Its constraints are tactical: "Always use Java Streams API," "Never use deprecated libraries," or "Ensure all public methods have Javadoc."  
* **The QA Agent:** Focused on validation. Its directives would be: "Assume all inputs are malicious," "Generate edge-case datasets first," and "Verify parity against the legacy output".3

By encoding these roles, we create a specialized virtual workforce. The AGENTS.md file serves as the "hiring contract" for these agents, ensuring they do not deviate from the agreed-upon engineering culture.

#### **0.1.2 Technical Constraints and Tooling**

A critical function of AGENTS.md is to bridge the gap between the AI's reasoning capabilities and the physical reality of the development environment. The file must contain precise, executable commands for the agent to orient itself.4

* **Build Commands:** The agent must know exactly how to compile the project (e.g., ./gradlew clean build or npm run build). This allows the agent to enter a self-correcting loop where it writes code, attempts to build it, reads the error log, and iterates—a process known as "agentic repair."  
* **Test Commands:** Explicit instructions on how to run specific test suites (e.g., python \-m pytest tests/parity).  
* **Directory Structure:** A map of the repository, explaining where legacy code lives versus where modern code should be generated (e.g., "Legacy COBOL resides in /src/legacy/cobol; modern Java targets /src/main/java/com/acme/modern").

### **0.2 The Planning Protocol: PLANS.md and the ExecPlan**

While AGENTS.md defines the "who" and "how," the **ExecPlan** defines the "what" and "when." To standardize this, we introduce **PLANS.md**, a template file that dictates the structure of every execution plan the agent generates.1

#### **0.2.1 The Concept of the "Living Document"**

In traditional project management, the plan is often a static artifact created at the beginning and updated sporadically. In an agentic workflow, the ExecPlan is a **living state file**. It is the externalized memory of the project. Because LLMs have limited context windows, they cannot "remember" a decision made 5,000 tokens ago if that part of the conversation has rolled off. The ExecPlan solves this by forcing the agent to record its progress, decisions, and discoveries in a markdown file that is re-read at the start of every interaction.5

#### **0.2.2 Structure of a Compliant ExecPlan**

The PLANS.md template mandates that every project plan must contain specific sections to ensuring rigorous tracking 5:

* **Progress:** A granular checklist of tasks. The agent updates this list autonomously, marking items as \[x\] upon verified completion.  
* **Decision Log:** A timestamped record of architectural choices (e.g., "2025-10-12: Decided to map COBOL PIC 9(7)V99 to BigDecimal to ensure precision"). This provides an audit trail for the "Legacy Custodians" to review.  
* **Surprises & Discoveries:** A dedicated section for the agent to log unexpected findings, such as undocumented dependencies or logic that contradicts the functional requirements.1

### **0.3 Operational Infrastructure and Stakeholder Assignment**

Phase 0 also involves the physical and organizational setup required to support the agents.

#### **0.3.1 The Codex CLI and Sandbox Environment**

The **Codex CLI** serves as the interface between the human operator and the AI model. It must be configured to balance autonomy with safety.

* **Sandboxing:** To mitigate the risk of the agent executing harmful commands (e.g., rm \-rf /), the framework utilizes OS-level sandboxing (such as sandbox-exec on macOS or containerization on Linux). The AGENTS.md file acts as the policy engine, defining which directories are writable and which are read-only.6  
* **Approval Modes:** For the initial phases, the CLI should be set to "Agent" or "Suggest" mode, requiring human confirmation for every file write or shell command. As the project matures and trust is established, specific low-risk tasks (like test generation) can be moved to "Autonomous" mode.6

#### **0.3.2 Assigning Stakeholders**

A successful modernization project requires a specific blend of human expertise to guide the AI.

* **The Modernization Lead (The Driver):** The engineer primarily responsible for prompting the agent and reviewing its output. They are the "Human-in-the-Loop."  
* **The Legacy Custodian (The Oracle):** A subject matter expert (SME) deeply familiar with the mainframe environment. Their role is not to write code, but to validate the agent's interpretation of the legacy logic (Phase 2\) and approve the parity test scenarios (Phase 3).  
* **The Platform Architect:** Ensures that the "Target State" designed by the agent aligns with the enterprise's broader cloud strategy (e.g., AWS, Azure).

### **0.4 Communication and Success Criteria**

Communication Protocols:  
Given the rapid pace of AI generation, traditional weekly status meetings are insufficient. We establish a daily asynchronous update protocol where the "Progress" section of the current ExecPlan is committed to the repository and pushed to a central dashboard. This allows stakeholders to see the exact state of the migration in real-time, down to the specific file being modernized.  
**Success Criteria for Phase 0:**

* A finalized AGENTS.md rooted in the repository, containing all build/test commands and architectural rules.  
* A PLANS.md template ratified by the architecture board.  
* The Codex CLI installed and authenticated on all developer workstations.8  
* The "Project Charter" delivered, defining the governance hierarchy and escalation paths for AI-induced blockers.

## ---

**Phase 1: Pick a Pilot and Create the First ExecPlan**

**Objective:** Select optimal pilot scenario and develop execution roadmap

With the governance foundation laid, the organization must select a pilot project. This is a critical strategic decision. A pilot that is too simple will fail to validate the framework's capability to handle complexity; a pilot that is too intertwined with global dependencies will stall before it produces value. Phase 1 focuses on the analytical selection of this pilot and the drafting of the master execution plan.

### **1.1 Candidate Identification and Selection Criteria**

The framework utilizes the AI agent itself to assist in the selection process. By granting the agent read-access to the legacy repository (e.g., the library of JCL members and COBOL source files), we can prompt it to "Identify candidate pilot flows that are realistic but bounded."

Selection Criteria Matrix:  
We evaluate candidates against four axes:

1. **Feasibility (Isolation):** Does the flow have minimal dependencies on external systems (e.g., MQ Series, DB2 Stored Procedures) that are difficult to mock? We favor batch jobs that read a file, process it, and write a file.  
2. **Impact (Business Value):** Is the flow relevant? Modernizing a "dead" reporting job proves nothing. We seek a "Daily Reporting Flow" or a "End-of-Day Reconciliation" job that is actively used.1  
3. **Complexity (Representative Logic):** The code must contain actual business rules (computations, conditional logic), not just data movement. It needs to test the agent's ability to interpret PERFORM loops and arithmetic.  
4. **Testability (Data Availability):** Can we easily obtain input data and expected output data? Without this, the "Parity Verification" in Phase 4 is impossible.

Selected Pilot Scenario:  
For the purposes of this framework, we typically select a Daily Reporting Flow. This flow usually consists of:

* **Inventory:** 1-3 COBOL programs.  
* **Orchestration:** A JCL job with multiple steps.  
* **Data:** Sequential files (QSAM) or VSAM datasets.  
* **Logic:** Filtering records, aggregating totals (e.g., SUM TRANSACTION-AMT), and formatting a print report.

### **1.2 Developing the Pilot ExecPlan**

Once the pilot is selected, the agent is tasked with generating the pilot\_execplan.md. This is the first "live" test of the governance structure established in Phase 0\. The agent must read PLANS.md and instantiate a specific plan for the chosen flow.1

#### **1.2.1 Scope Definition and Boundaries**

The ExecPlan must explicitly define what is *in scope* and, more importantly, what is *out of scope*.

* **In Scope:** The COBOL source code, the JCL definitions, and the specific Copybooks used by the programs.  
* **Out of Scope:** Upstream data generation jobs, downstream consumption systems, and strictly "utility" subroutines that can be mocked.

This scoping prevents "Context Creep," where the agent attempts to pull in the entire mainframe estate to resolve a single variable definition.

#### **1.2.2 The Detailed Execution Roadmap**

The ExecPlan generated by the agent will outline the specific milestones for the pilot. These milestones map directly to the subsequent phases of this framework:

1. **Inventory Milestone:** Completion of the System Overview and MTR.  
2. **Design Milestone:** Approval of the OpenAPI spec and Target Architecture.  
3. **Implementation Milestone:** Code generation complete and compiling.  
4. **Verification Milestone:** Parity tests passing at 100%.

**Risk Mitigation Strategies in the Plan:**

* **Risk:** "AI Hallucination of Business Logic." **Mitigation:** Mandatory code review by the Legacy Custodian and strict Parity Testing.  
* **Risk:** "Data Encoding Issues (EBCDIC vs. ASCII)." **Mitigation:** Use of dedicated hex-dump comparison tools during Phase 4\.

Deliverable for Phase 1:  
An approved pilot\_execplan.md file committed to the repository. This file now serves as the "source of truth" for the project. The status of the pilot is no longer tracked in an external tool like Jira or Excel, but in the markdown of the ExecPlan itself.

## ---

**Phase 2: Inventory and Discovery**

**Objective:** Comprehensive assessment of current state

Phase 2 is the "Archaeology" phase. The goal is to extract a definitive understanding of the current system's behavior. In manual modernization projects, this phase is notoriously slow and error-prone, as human engineers struggle to trace logic through thousands of lines of spaghetti code. The agentic framework accelerates this by leveraging the LLM's superior ability to parse, cross-reference, and summarize syntactic structures.9

### **2.1 Automated Mapping of Systems and Workflows**

The agent is instructed to scan the files identified in the ExecPlan. It parses the **Identification Division**, **Environment Division**, and **Data Division** of the COBOL programs to build a dependency graph.

**Key Activities:**

* **JCL Parsing:** The agent reads the JCL to understand the execution sequence. It identifies the DD (Data Definition) statements to map inputs to outputs. "Job Step 1 reads FILE-A, produces FILE-B. Job Step 2 reads FILE-B...".1  
* **Copybook Expansion:** The agent expands all COPY statements to see the full data structure. It identifies redefinitions (REDEFINES), which are common sources of logic errors during migration.  
* **Flow Visualization:** The agent generates a text-based diagram (using Mermaid.js or ASCII art) within the pilot\_reporting\_overview.md file, visually representing the data lineage.

### **2.2 The Modernization Technical Report (MTR)**

The primary artifact of this phase is the **Modernization Technical Report (MTR)**, which is embedded directly into the pilot\_reporting\_overview.md file. This report bridges the gap between the technical code and the business reality.1

#### **2.2.1 Business Logic Extraction**

The agent translates the COBOL PROCEDURE DIVISION into plain English business rules.

* *Legacy Code:* IF TRX-TYPE \= 'D' AND TRX-AMT \> 1000 PERFORM LARGE-DEBIT-ROUTINE.  
* *MTR Entry:* "The system identifies any Debit transaction over $1,000 as a 'Large Debit' and routes it for special handling."

This translation allows the "Legacy Custodians" (the human SMEs) to verify that the AI has correctly understood the *intent* of the code, not just the syntax.

#### **2.2.2 Documenting Pain Points and Inefficiencies**

The agent is prompted to identify "technical debt" patterns:

* **Hardcoded Values:** "Found tax rate hardcoded as 0.05 in paragraph CALC-TAX."  
* **Obsolete Logic:** "Code references a 'Y2K' remediation check that is no longer relevant."  
* **Data Constraints:** "Field CUSTOMER-NAME is limited to 20 characters, causing truncation."

### **2.3 Identifying Dependencies and Constraints**

A critical part of discovery is identifying what *cannot* be easily moved. The agent scans for:

* **External Calls:** CALL 'DB2STORE' implies a database dependency.  
* **System Utilities:** Uses of SORT or IDCAMS (IBM utilities) which must be replaced by modern equivalents (e.g., Java Collections.sort() or SQL ORDER BY).

Deliverable for Phase 2:  
A comprehensive pilot\_reporting\_overview.md containing the Inventory and the MTR. The ExecPlan is updated to mark "Inventory" as complete. The "Surprises" section of the ExecPlan is populated with any unexpected findings (e.g., "Discovered that the program relies on the physical sorting order of EBCDIC, which differs from ASCII").1

## ---

**Phase 3: Design, Spec, and Validation Plan**

**Objective:** Create future state design with validation approach

Phase 3 is the pivot point. We move from analyzing "what is" to defining "what will be." The agentic framework enforces a strict **"Spec-First"** and **"Test-First"** approach. We do not allow the agent to start generating code until the target architecture and the validation strategy are rigorously defined and approved.

### **3.1 Target State Architecture and Solution Design**

The agent assists the Architect in drafting the pilot\_reporting\_design.md. This document outlines how the monolithic legacy flow will be mapped to the modern stack.

**Key Design Decisions:**

* **Service Granularity:** Will the COBOL program become a standalone Microservice, a Serverless Function, or a module within a larger Monolith? For a batch reporting pilot, we often design a **Spring Batch** (Java) or **FastAPI** (Python) application containerized in **Docker**.10  
* **Data Modernization:** The agent proposes a mapping from the legacy file system (VSAM/QSAM) to a modern data store (PostgreSQL/S3). It defines the schema: "The CUSTOMER-RECORD copybook maps to the customers table. The packed-decimal COMP-3 fields map to DECIMAL(10,2) columns".1

### **3.2 Detailed Specifications: The OpenAPI Contract**

To ensure the modern system is modular and decoupled, we mandate the creation of an API specification—even for batch jobs (which can be triggered via API). The agent generates a **modern/openapi/pilot.yaml** file.

This OpenAPI spec defines the "Contract" that the new code must fulfill. It forces the agent to think about strong typing, inputs, and outputs before it writes a single line of logic. This file acts as the "Requirements Document" for the Implementation Phase.

### **3.3 Designing the Validation Methodology: Parity Testing**

The most significant risk in modernization is **Functional Divergence**—where the new system produces slightly different results (e.g., rounding errors) than the old system. To mitigate this, Phase 3 focuses heavily on designing a **Parity Testing Strategy**.11

#### **3.3.1 The Parity Test Harness**

The agent is tasked with designing a test harness (e.g., modern/tests/pilot\_parity\_test.py) that will:

1. **Execute the Legacy System:** Run the JCL (or an emulator) with a specific input file.  
2. **Capture Legacy Output:** Store the resulting report or dataset.  
3. **Execute the Modern System:** Call the new API or Batch Job with the *exact same input*.  
4. **Compare Outputs:** Perform a bit-level or semantic comparison of the results.

#### **3.3.2 Defining Acceptance Criteria and KPIs**

The pilot\_reporting\_validation.md file defines the success metrics:

* **Functional Parity:** 100% match on business data (ignoring timestamps or headers).  
* **Performance KPI:** The modern job must complete within 110% of the legacy job's time (allowing for some overhead) or faster.  
* **Rollback Procedure:** If the parity test fails in production, the system must fallback to the legacy mainframe job immediately.

Deliverable for Phase 3:  
A detailed Design Package (.md), API Specification (.yaml), and a skeleton Validation Plan (.md). The stakeholders review these documents. The Legacy Custodian confirms that the test scenarios cover the critical business cases.

## ---

**Phase 4: Implement and Compare**

**Objective:** Execute pilot and measure results

Phase 4 is the implementation engine. In traditional development, this is often the longest phase. In the agentic framework, it is characterized by high-velocity iteration. We utilize the agent to generate code, run the parity tests, analyze failures, and self-correct—a loop known as **"Agentic Repair."**

### **4.1 Implementation According to Specs**

The agent is now given the command to "Implement the spec." It uses the context from Phase 2 (Legacy Logic) and Phase 3 (Target Design) to generate the modern code.

Prompting Strategy:  
"Using pilot\_reporting\_design.md and the COBOL programs in pilot\_reporting\_overview.md, generate the Java Spring Boot implementation. Ensure that the logic for 'Large Debit' calculation matches the CALC-DEBIT paragraph exactly."  
The agent generates the Entity classes, the Repository layers, and the Service logic. Crucially, it injects comments linking the new code back to the old: // Reference: COBOL Paragraph CALC-TAX-ROUTINE.1 This traceability is vital for future maintenance.

### **4.2 Execution of Validation Testing**

As soon as the code compiles, the **Parity Test Harness** is triggered.

* **Initial Run:** The test will almost certainly fail. The legacy system might round "Half Down," while the default Java library rounds "Half Up." Or the legacy system might use EBCDIC sorting (where numbers come after letters), while the modern system uses ASCII.  
* **The Feedback Loop:** The error log ("Expected 10.50, Got 10.51") is fed back to the agent.  
* **Agentic Repair:** The agent analyzes the discrepancy. "The COBOL code uses COMPUTE ROUNDED, which implies a specific rounding mode. I will update the BigDecimal math context to match."

This loop continues until the parity tests pass. This is **Test-Driven Modernization**.12

### **4.3 Comparison and Documentation**

Once parity is achieved, the results are documented in the **Implementation Results Report**.

* **Baseline Comparison:** We compare the performance. Did the Java version run faster? Did it consume more memory?  
* **Issue Resolution Log:** We document the specific nuances discovered. "We learned that the legacy system allows invalid dates (e.g., 000000\) in the database. The modern system threw an exception. We decided to implement a 'sanitize' filter to handle this data quality issue".1

Deliverable for Phase 4:  
A codebase that compiles and passes the Parity Test Suite. A pilot\_reporting\_validation.md update that logs the successful test run. The ExecPlan is updated to show 100% completion of the pilot scope.

## ---

**Phase 5: Turn the Pilot into a Scalable Motion**

**Objective:** Industrialize and scale the solution

A successful pilot is only the beginning. Phase 5 is about taking the artisanal process of the pilot and turning it into a "Modernization Factory." This phase focuses on efficiency, repeatability, and organizational transformation.

### **5.1 Extracting Lessons and Building the Playbook**

The agent is tasked with conducting a **Retrospective Analysis** of the pilot. It analyzes the Decision Log and Surprises sections of the ExecPlan to identify recurring patterns.

* **Pattern Extraction:** "We consistently encountered issues with COMP-3 packed decimals. We should create a shared library LegacyUtils to handle this standardly."  
* **Template Creation:** The agent generates a **template\_modernization\_execplan.md**. This template pre-populates the standard tasks (Inventory, Spec, Test) so that future squads don't have to reinvent the wheel.1

### **5.2 Scaling Roadmap and The Factory Model**

To scale, the organization adopts a "Squad" model.

* **The Factory:** Multiple pods of developers, each equipped with the Codex CLI and the standard templates.  
* **The Strangler Fig Pattern:** We utilize the Strangler Fig pattern to roll out the modernization. We do not replace the mainframe overnight. Instead, we place an "Anti-Corruption Layer" (ACL) or API Gateway in front of the legacy system. We incrementally route traffic for specific flows (like the Pilot flow) to the new modern service, while the rest of the traffic continues to the mainframe.13

### **5.3 Training, Enablement, and Change Management**

The shift to agentic modernization requires a fundamental shift in the skills of the workforce.

* **From Coders to Reviewers:** Developers spend less time writing syntax and more time reviewing the agent's logic and designing validation tests.  
* **Enablement Materials:** We use the agent to generate "Onboarding Guides" for new developers, explaining how to use AGENTS.md and the Codex CLI.  
* **Change Management:** We must address the cultural resistance. Mainframers may fear obsolescence. We reframe their role as "Validation Architects"—the only people who understand the *business truth* well enough to certify the AI's work.14

### **5.4 Governance and Maintenance**

As the number of modernized services grows, governance becomes critical.

* **Continuous Governance:** The AGENTS.md file is version-controlled and centrally managed. If the Architecture Board decides to change a logging standard, they update the root AGENTS.md. All agents in all squads immediately "learn" this new rule in their next session.  
* **Drift Detection:** We establish ongoing monitoring to ensure that the modernized services do not drift from the legacy behavior over time. The Parity Tests are integrated into the nightly CI/CD pipeline.9

Deliverable for Phase 5:  
A "Scalability Framework" document, a library of reusable code templates (LegacyUtils), and a "Rollout Plan" for the next 10 flows.

## ---

**Cross-Phase Considerations**

### **Governance Checkpoints**

The framework implements rigorous **Phase Gates**. The project cannot proceed from Phase 2 (Discovery) to Phase 3 (Design) without a formal review of the MTR by the Legacy Custodian.

* **Go/No-Go Decisions:** At the end of Phase 3, if the Parity Test Strategy is deemed insufficient (e.g., "We can't replicate the input data"), the project enters a "Halt" state.  
* **Escalation Paths:** If the agent consistently fails to produce working code (e.g., due to extreme complexity), the "Modernization Lead" escalates to the "Architect" to decide if the flow should be rewritten manually or re-scoped.

### **Risk Management**

* **Continuous Risk Assessment:** The ExecPlan's "Surprises" section acts as a real-time risk register.  
* **Mitigation Strategies:**  
  * *Hallucination Risk:* Mitigated by the "Concrete Steps" requirement in Plans and strict Compilation checks.16  
  * *Security Risk:* Mitigated by the Sandbox environment and the AGENTS.md rule "Never commit credentials."  
  * *Dependency Risk:* Mitigated by the thorough Inventory analysis in Phase 2\.17

### **Communication**

* **Progress Dashboards:** By parsing the markdown ExecPlans across the repository, we can generate a programmatic dashboard showing the status of every flow (e.g., "Flow A: Phase 2 \- 80%", "Flow B: Phase 4 \- 10%").  
* **Feedback Loops:** The "Decision Logs" are aggregated and reviewed monthly by the Center of Excellence to improve the global AGENTS.md prompt, ensuring that the entire organization learns from the experiences of individual squads.

### ---

**Table 1: Artifact Summary and Owner Mapping**

| Phase | Artifact | Primary Purpose | Key Owner | AI Role |
| :---- | :---- | :---- | :---- | :---- |
| **0** | AGENTS.md | Governance & Context | Chief Architect | Consumer |
| **0** | PLANS.md | Process Standardization | Program Lead | Consumer |
| **1** | pilot\_execplan.md | State Tracking & Roadmap | Project Manager | Creator/Updater |
| **2** | pilot\_reporting\_overview.md | Inventory & Business Logic | Legacy Custodian | Archaeologist |
| **3** | pilot\_reporting\_design.md | Target Architecture | Modernization Architect | Designer |
| **3** | modern/openapi/pilot.yaml | Interface Contract | API Developer | Author |
| **3** | pilot\_reporting\_validation.md | Test Strategy | QA Lead | Strategist |
| **4** | modern/tests/pilot\_parity\_test.py | Verification Harness | QA Engineer | Test Writer |
| **5** | template\_modernization\_execplan.md | Scaling Pattern | Center of Excellence | Pattern Extractor |

### **Table 2: Risk Mitigation Matrix**

| Risk Category | Specific Threat | Mitigation Strategy | Phase Addressed |
| :---- | :---- | :---- | :---- |
| **Cognitive** | AI Hallucination of Libraries | Sandbox Execution & Compilation Checks | 4 |
| **Functional** | Subtle Logic Divergence (Rounding) | Bit-level Parity Testing Strategy | 3 & 4 |
| **Security** | Injection of Vulnerabilities | AGENTS.md Constraints & SAST Tools | 0 & 4 |
| **Operational** | "Black Box" Code | Requirement for Comments Linking to Legacy | 4 |
| **Cultural** | Resistance from Legacy Team | Rebranding roles to "Validation Architects" | 5 |

### **Table 3: Comparative Analysis of Modernization Approaches**

| Feature | Manual Rewrite | Lift & Shift | Agentic Framework |
| :---- | :---- | :---- | :---- |
| **Speed** | Low (Years) | High (Weeks) | **High (Months)** |
| **Cost** | Very High | Low | **Moderate** |
| **Debt Reduction** | High | None | **High** |
| **Risk of Failure** | High | Low | **Low (via Parity)** |
| **Documentation** | Often Skipped | N/A | **Automated (MTR)** |
| **Scalability** | Linear (More Humans) | Instant | **Exponential (More Compute)** |

## ---

**Conclusion**

The Multi-Phase Project Framework for agentic code modernization offers a definitive path out of the legacy trap. By combining the governance of AGENTS.md, the continuity of ExecPlans, and the rigor of Parity Testing, organizations can harness the power of AI to industrialize what was once a bespoke craft. This is not merely about writing code faster; it is about creating a self-documenting, self-verifying modernization engine that scales with the enterprise's ambition. As the framework evolves from the Pilot (Phase 1\) to the Factory (Phase 5), it transforms not just the technology stack, but the engineering culture itself, positioning the organization to thrive in the AI-native future.

#### **Works cited**

1. Modernizing your Codebase with Codex | OpenAI Cookbook, accessed on December 14, 2025, [https://cookbook.openai.com/examples/codex/code\_modernization](https://cookbook.openai.com/examples/codex/code_modernization)  
2. AGENTS.md \- Factory Documentation, accessed on December 14, 2025, [https://docs.factory.ai/cli/configuration/agents-md](https://docs.factory.ai/cli/configuration/agents-md)  
3. AGENTS.md File Optimization \- Coding with ChatGPT \- OpenAI Developer Community, accessed on December 14, 2025, [https://community.openai.com/t/agents-md-file-optimization/1369152](https://community.openai.com/t/agents-md-file-optimization/1369152)  
4. AGENTS.md, accessed on December 14, 2025, [https://agents.md/](https://agents.md/)  
5. openai-cookbook/articles/codex\_exec\_plans.md at main \- GitHub, accessed on December 14, 2025, [https://github.com/openai/openai-cookbook/blob/main/articles/codex\_exec\_plans.md](https://github.com/openai/openai-cookbook/blob/main/articles/codex_exec_plans.md)  
6. ymichael/open-codex: Lightweight coding agent that runs in your terminal \- GitHub, accessed on December 14, 2025, [https://github.com/ymichael/open-codex](https://github.com/ymichael/open-codex)  
7. Codex IDE extension \- OpenAI for developers, accessed on December 14, 2025, [https://developers.openai.com/codex/ide/](https://developers.openai.com/codex/ide/)  
8. How do I install Codex CLI on my machine? \- Milvus, accessed on December 14, 2025, [https://milvus.io/ai-quick-reference/how-do-i-install-codex-cli-on-my-machine](https://milvus.io/ai-quick-reference/how-do-i-install-codex-cli-on-my-machine)  
9. Migrating Cobol Projects in 2025 \- overcast blog, accessed on December 14, 2025, [https://overcast.blog/migrating-cobol-projects-in-2025-efe2744c0b86](https://overcast.blog/migrating-cobol-projects-in-2025-efe2744c0b86)  
10. AI Agents Are Rewriting the App Modernization Playbook | Microsoft Community Hub, accessed on December 14, 2025, [https://techcommunity.microsoft.com/blog/appsonazureblog/ai-agents-are-rewriting-the-app-modernization-playbook/4470162](https://techcommunity.microsoft.com/blog/appsonazureblog/ai-agents-are-rewriting-the-app-modernization-playbook/4470162)  
11. Testing Legacy Systems with AI: Automated QA, Regression & Edge Cases, accessed on December 14, 2025, [https://dev.to/himani\_0b4c9fc3c2ab3a1700/testing-legacy-systems-with-ai-automated-qa-regression-edge-cases-j1l](https://dev.to/himani_0b4c9fc3c2ab3a1700/testing-legacy-systems-with-ai-automated-qa-regression-edge-cases-j1l)  
12. Test Automation Implementation Guide: From Legacy Systems to AI-Native Success, accessed on December 14, 2025, [https://www.virtuosoqa.com/post/test-automation-implementation-guide-from-legacy-systems-to-ai-native-success](https://www.virtuosoqa.com/post/test-automation-implementation-guide-from-legacy-systems-to-ai-native-success)  
13. Legacy System Modernization and Migration: Key Strategies, Services, and Costs \- Bitcot, accessed on December 14, 2025, [https://www.bitcot.com/legacy-system-modernization-and-migration/](https://www.bitcot.com/legacy-system-modernization-and-migration/)  
14. Legacy Code AI Accelerates Mainframe Modernization \- AI CERTs News, accessed on December 14, 2025, [https://www.aicerts.ai/news/legacy-code-ai-accelerates-mainframe-modernization/](https://www.aicerts.ai/news/legacy-code-ai-accelerates-mainframe-modernization/)  
15. Best Practices for Legacy Modernization | StackSpot AI, accessed on December 14, 2025, [https://stackspot.com/en/blog/best-practices-for-legacy-modernization/](https://stackspot.com/en/blog/best-practices-for-legacy-modernization/)  
16. From Zero to Codex Hero: Everything You Need to Know About OpenAI's Coding Agent, accessed on December 14, 2025, [https://www.theneuron.ai/explainer-articles/from-zero-to-codex-hero-everything-you-need-to-know-about-openais-coding-agent](https://www.theneuron.ai/explainer-articles/from-zero-to-codex-hero-everything-you-need-to-know-about-openais-coding-agent)  
17. Best Practices for Migrating Legacy COBOL Code to Modern Standards \- MoldStud, accessed on December 14, 2025, [https://moldstud.com/articles/p-best-practices-for-migrating-legacy-cobol-code-to-modern-standards-streamline-your-transition](https://moldstud.com/articles/p-best-practices-for-migrating-legacy-cobol-code-to-modern-standards-streamline-your-transition)