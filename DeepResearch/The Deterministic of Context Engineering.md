The mandatory design and coding best practices required for code generation are governed by the overarching principle of **The Deterministic of Context Engineering**. This mandate ensures that outputs are reliable, consistent, scalable, and immediately production-ready, moving beyond the failures of earlier "Vibe Coding" approaches.

These practices can be systematically broken down into constraints on **Architecture and Style (Conceptual Guidance)**, **Implementation and Quality (Effective Coding Practices)**, and **Agentic Workflow and Validation (Context Management)**.

---

### **I. Conceptual Guidance and Architectural Standards**

Effective code generation requires blending high-level conceptual guidance (aimed at aesthetic and semantic quality) with structured specification to ensure functional integrity, a process sometimes called **Conceptual Blending Theory**.

#### **A. Design and Aesthetic Mandates**

1. **Aesthetic and Responsiveness:** Generated UI **MUST** be visually appealing, modern, polished, and functional, with responsiveness and mobile-first optimization being critical.  
2. **Design System Enforcement (CRITICAL):** Generated code **MUST** adhere to a defined design system (e.g., Next.js, React, TypeScript, Tailwind CSS, and `shadcn/ui` components). Custom styles written directly in components are **FORBIDDEN**; styling **MUST** rely exclusively on the design system's utility classes and semantic tokens.  
3. **Prohibited Styling:** The use of `styled-jsx` is **COMPLETELY BANNED** as it causes build failures with modern Next.js Server Components. Explicit, non-semantic classes like `text-white` or `bg-white` are also to be avoided in favor of design system tokens.  
4. **Semantic HTML and Accessibility:** Generated code **MUST** be accessibility compliant, utilizing semantic markup.

#### **B. Component and Modularity**

1. **Code Modularity:** Functionality **MUST** be split into smaller, reusable modules and components, strictly avoiding gigantic monolithic files. Components should generally be concise, often restricted to around 300–400 lines.  
2. **Reusability:** Components **MUST** maximize reusability.  
3. **Component Creation Protocol:** When creating a new component, agents **MUST** first examine existing components to understand conventions, including framework choice, naming, and typing.

---

### **II. Implementation and Quality: Effective Coding Practices**

The generated code must satisfy rigorous technical criteria for safety, clarity, and immediate executability, ensuring the output is **ERROR-FREE** and maintainable.

#### **A. Code Structure and Language**

1. **Immediacy and Correctness (EXTREMELY IMPORTANT):** Generated code **MUST** be immediately runnable and complete, containing no errors or hallucinations.  
2. **Language and Typing:** Code should default to modern languages like TypeScript 5\. Explicitly annotate function signatures and public APIs to maintain type safety.  
3. **Readability:** Code should be written for clarity, minimizing the need for supplemental comments, though comments are added to help with long-term understanding.  
4. **Consistency:** New code **MUST** mimic existing style conventions, indentation, libraries, and frameworks within the codebase.  
5. **Minimalism:** Agents **MUST** write only the **ABSOLUTE MINIMAL** amount of code necessary to address the requirement, avoiding verbose implementations or unnecessary complexity.

#### **B. Security and Data Integrity**

1. **Security Mandate:** Agents **MUST** prioritize and follow security best practices. This includes:  
   * **Prohibited Secrets Exposure:** **NEVER** introduce code that exposes or logs secrets or API keys.  
   * **Credential Handling:** Secrets and keys **MUST NEVER** be hardcoded or committed to the repository, but instead placed in the `.env` file and integrated properly.  
   * **Malicious Code Refusal:** Agents **MUST** decline any request that asks for malicious code.  
2. **Data Persistence:** Unless explicitly instructed otherwise, data **MUST** be stored using built-in database functionality (e.g., Encore.ts's SQL Database) rather than in memory or in files on disk.  
3. **Authentication:** Code **MUST** integrate with existing authentication patterns and systems. When creating new authentication UI, it **MUST** follow specific patterns, such as implementing proper error handling and using session hooks for protected pages.

#### **C. Prohibited Operations**

1. **File Creation and Preference:** Agents **MUST ALWAYS** prefer editing an existing file to creating a new one. New files should only be created when absolutely necessary.  
2. **Browser API Restrictions:** The use of synchronous, browser-native APIs like `localStorage`, `window.location.reload()`, or `window.open()` is **STRICTLY BANNED** in components, with state management handled by React state or router navigation.  
3. **Unauthorized Documentation:** Agents **MUST NEVER** proactively create documentation files (`*.md`) or `README` files unless explicitly requested by the user.

---

### **III. Agentic Workflow and Context Management**

The agent's operational environment demands highly efficient and structured actions, relying on **Sub-agents in Context Control** and strict validation protocols.

#### **A. Efficiency and Parallelization (Optimizing Context Utilization)**

1. **Parallel Execution (CRITICAL INSTRUCTION):** For maximum efficiency, whenever performing multiple independent operations (especially read-only context gathering like reading files or semantic search), agents **MUST** invoke all relevant tools concurrently (in parallel). Sequential calls are **ONLY** permitted when the output of Tool A is a strict prerequisite for the input of Tool B.  
2. **Information Gathering Priority:** Information gathering (searching the codebase, reading files) **MUST** precede any code edits. Agents **MUST** prioritize tools over asking the user for clarification.  
3. **Proactive Execution:** Agents **MUST** be proactive and decisively proceed with execution when tools are available to complete a task, avoiding asking for unnecessary confirmation unless genuinely blocked.

#### **B. Planning and Task Management**

1. **Mandatory Task Planning:** For complex, multi-step tasks (e.g., multi-file changes, full-stack features, ambiguous requests, or tasks requiring more than two editing/verification iterations), agents **MUST** create and use a structured task list (Todo list/Tasklist) for planning and tracking progress.  
2. **Actionable Tasks:** Tasks **MUST** be specific, clear, short, and action-oriented (verb phrases). Plans **MUST ONLY** include coding tasks (writing, modifying, testing code), explicitly excluding non-coding activities like deployment or organizational changes.

#### **C. Code Modification Protocol (Compaction)**

1. **Tool-Based Edits:** Agents **MUST NEVER** output code directly to the user when making modifications; they **MUST** use the designated edit tools (e.g., `edit_file`, `string_replace`, `apply_patch`).  
2. **Minimizing Code Repetition (Compaction):** Edits **MUST** be semantic and concise, utilizing truncation markers (e.g., `// ... existing code ...`) to represent unchanged code and minimize unnecessary output (token **Compaction**).  
3. **Parameter Ordering:** When using code edit tools, the target file argument **MUST** be specified first.

#### **D. Validation and Verification Loop**

1. **Mandatory Validation Loop:** After **ANY** substantive code edit or schema change, the agent **MUST** execute the relevant validation tools (linters, type-checkers, `get_problems`) automatically.  
2. **Fix Until Green:** The agent **MUST** iterate and fix compilation/lint errors immediately, continuing until no issues remain. Agents are typically allowed up to three targeted fix attempts for the same issue before stopping and asking the user for help.  
3. **Test Proactivity:** After making code edits, agents **MUST** suggest writing or updating tests and executing them to verify correctness. If a runnable solution is generated, the agent **MUST** run a minimal test itself to validate functionality.

