

# **Verifiable Governance for MCP-Enabled WordPress: A Framework for Tiered Oversight, Digital Veto, and Global-Compliance Alignment**

## **P0 – Foundational Analysis: The Bias Register & Hidden-Premise Log**

Before constructing a governance framework, it is imperative to identify and dismantle the hidden assumptions that frequently lead to systemic failure in AI and automation projects. This register serves as a foundational threat model, cataloging the flawed premises that this report’s architecture is explicitly designed to falsify and mitigate.

* **Premise 1: Granular Permissions Equal Accountability.** A common but fallacious belief is that breaking down monolithic roles like Administrator into more granular, task-specific permissions (e.g., plugin\_editor) automatically solves for accountability. This premise fundamentally misunderstands the nature of autonomous systems. It ignores the "accountability chasm" where responsibility becomes diffuse and untraceable when an ephemeral agent performs an action, even with a specific permission.1 The core issue is not the granularity of the permission, but the lack of a verifiable link between a specific human's intent and the agent's execution of a high-risk action.3  
* **Premise 2: More Transparency is Always Better.** The prevailing industry narrative often equates maximum transparency—exposing model internals or decision logic—with trustworthiness. This overlooks the critical trade-off between transparency and verifiability. A system can be fully transparent yet cognitively overwhelming and practically incomprehensible to a human overseer. Conversely, an opaque "black box" system that produces externally verifiable claims *before* acting can be more robustly governed and audited.4 The goal is not to understand  
  *how* the agent "thinks," but to verify *what* it contractually commits to do.5  
* **Premise 3: A Human-in-the-Loop (HOTL) is an Infallible Backstop.** The simple insertion of a human approval checkpoint is often treated as a panacea for AI risk. This dangerously ignores well-documented human factors such as cognitive overload, approval fatigue, and automation bias, where the human operator devolves into a mere "rubber stamp" for machine suggestions.7 A poorly designed HOTL system creates the illusion of control while providing none of its substance.9  
* **Premise 4: Compliance is a Post-Development Checkbox.** Treating regulatory alignment with frameworks like the NIST AI Risk Management Framework (RMF) or the EU AI Act as a final-stage validation exercise is a recipe for architectural failure. These regulations impose fundamental requirements on risk management, data governance, and human oversight that must be designed into the system's core, not retrofitted as an afterthought.10  
* **Premise 5: Agents are Mere Tools.** A critical mischaracterization is viewing Multi-Agent Coordinated Process (MCP) agents as simple, deterministic tools that merely execute commands. These are autonomous or semi-autonomous entities capable of complex, emergent behaviors within a dynamic environment.12 Treating them as simple tools leads to a gross underestimation of their potential blast radius and a failure to design appropriate containment mechanisms.  
* **Premise 6: Platform Security is a Given.** Building a sophisticated governance layer on an insecure foundation is futile. The WordPress ecosystem, with its vast and varied plugin library, presents a significant software supply chain risk.14 An assumption that the underlying platform is secure by default ignores vulnerabilities that can be introduced via third-party dependencies, allowing a compromised plugin to bypass or subvert the governance controls.16  
* **Premise 7: Governance is Purely a Technical Problem.** The belief that governance can be solved with code alone is a profound error. Effective governance is a socio-technical problem, intersecting code with human psychology, organizational culture, legal obligations, and ethical frameworks.17 A purely technical solution will fail when it collides with human reality.2  
* **Premise 8: Fiduciary Duty is Limited to Data Protection.** A narrow interpretation of data fiduciary responsibility focuses solely on preventing the leakage of Personally Identifiable Information (PII). This neglects the broader duties of care and loyalty, which extend to how agent-driven decisions—even those not directly involving PII—impact the organization's financial health, reputation, and obligations to its stakeholders.19 An agent that lawfully optimizes ad spend but bankrupts the company has still violated the spirit of fiduciary duty.20

## **P1 – Multi-Lens Threat & Opportunity Analysis**

To construct a resilient governance framework, each proposed component must be systematically interrogated from multiple, often conflicting, perspectives. This multi-lens analysis forces the identification and resolution of design tensions, ensuring the final architecture is balanced and robust against a wide spectrum of risks. The following matrix synthesizes this analysis, mapping core governance components against seven critical lenses.

### **Integrated Lens Matrix**

| Governance Component | Accountability-Chasm Lens | Verifiability-over-Transparency Lens | HOTL Friction Lens | Global Compliance Lens | Data-Fiduciary Lens | Plugin-Integrity & Supply-Chain Lens | Positive-Friction Lens |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Agent-Administrator Role** | **Analysis:** Standard WP roles (Administrator, Editor) are static, user-centric grants of persistent privilege, creating an accountability gap for ephemeral agent actions.21 An agent might need | delete\_users capability for a 2-second task, but assigning a human this role to oversee it grants excessive, persistent permissions, diffusing responsibility if the agent misbehaves later.23 The Agent-Administrator role bridges this by being a | *policy enforcement point*, not a user identity. It grants temporary, just-in-time (JIT) capabilities to agents based on a human's explicit, logged approval. **Insight:** This shifts from Role-Based Access Control (RBAC) to Policy-Based, Just-in-Time Access Control (PBAC/JITAC), directly addressing the "culpability gap" by creating a clear causal link from human intent to machine action.3 | **Analysis:** The role itself is not transparent, but its *actions* are verifiable. The role's existence is defined by the policies it enforces, which are auditable. **Insight:** The focus is on the verifiability of the *policy execution* rather than the transparency of the role's internal state. | **Analysis:** The cognitive load is on the human approver, not the role itself. The role acts as a gate, channeling high-risk decisions to the human, thus managing the *flow* of cognitive load. **Insight:** The role is a load-balancer for human attention. | **Analysis:** Directly maps to NIST GOVERN 2.1 (Roles & Responsibilities) by defining a new, necessary role for AI oversight. **Insight:** Creates a specific, auditable entity responsible for mediating agent actions, a core tenet of accountable governance. | **Analysis:** The role is the mechanism through which fiduciary duty is enforced. It can be configured with policies that automatically block or escalate actions that conflict with fiduciary obligations. **Insight:** Moves fiduciary duty from a document into an enforced workflow. | **Analysis:** The Agent-Administrator must verify the cryptographic identity (e.g., DID) of the agent it is governing before granting capabilities. **Insight:** The role becomes a zero-trust enforcement point for the agent supply chain. | **Analysis:** The friction is not in the role, but in the approval process it mandates. **Insight:** The role's primary function is to *introduce* positive friction where necessary. |
| **Tiered Approval Workflow** | **Analysis:** Explicitly links the severity of an action to the required level of human accountability. A low-risk action has low accountability overhead (post-hoc review), while a high-risk action requires direct, pre-hoc assumption of responsibility. **Insight:** Makes accountability proportional to blast radius, closing the chasm for the most dangerous actions. | **Analysis:** The workflow prioritizes verifiability at each tier. Even auto-approved low-risk actions generate a verifiable log entry. High-risk tiers demand more detailed verifiable claims. **Insight:** Verifiability is the constant; the level of human interaction is the variable. | **Analysis:** A core mechanism for managing cognitive load. By automating low-risk approvals, it preserves human attention for high-risk decisions, mitigating "approval fatigue".24 | **Insight:** The tiers are a cognitive load management strategy, not just a security model. | **Analysis:** Maps to EU AI Act Art. 9 (Risk Management System) by classifying and managing risks proportionally. Maps to NIST MANAGE 1.2 (Prioritize Risk Treatment). **Insight:** The tiered structure is a direct implementation of a risk-based approach mandated by major regulations. | **Analysis:** Actions touching PII or having significant financial impact are automatically classified as High-Risk, requiring approval from a designated data fiduciary or compliance officer. **Insight:** Enforces fiduciary oversight at the workflow level. | **Analysis:** The workflow can be configured to require a valid VC-signed manifest check before any action, regardless of tier, is allowed to enter the queue. **Insight:** Integrates supply chain verification into the operational workflow. | **Analysis:** The friction (approval steps, MFA) is deliberately scaled with the risk tier. This is the definition of positive friction: slowing users down for critical actions to prevent error.26 | **Insight:** The workflow uses friction as a feature to enhance safety and trust. |
| **Verifiable Justification Log** | **Analysis:** This is the ultimate tool for closing the accountability chasm. It creates a non-repudiable, immutable record linking a specific human approval to a specific machine action with a specific, pre-stated justification.28 | **Insight:** It replaces ambiguous responsibility with cryptographic certainty. | **Analysis:** This is the cornerstone of the "verifiability over transparency" principle. The log does not attempt to explain the agent's internal reasoning; it records the agent's *verifiable commitment* before the action.4 | **Insight:** The log is a contract, not a diary. It is audited for compliance, not interpreted for intent. | **Analysis:** The log provides the necessary context for the human approver to make an informed decision, reducing the cognitive load of having to guess the agent's intent. **Insight:** A well-structured log reduces cognitive load by making the decision context explicit. | **Analysis:** Directly satisfies EU AI Act Art. 12 (Record-Keeping) and Art. 19 (Automatically Generated Logs). Aligns with NIST MEASURE 3.1 (Track Risks Over Time). **Insight:** This component is a direct, one-to-one implementation of key regulatory requirements for auditability. | **Analysis:** Any action involving sensitive data must include a justification that explicitly cites the legal basis or policy (e.g., "GDPR Art. 17 request \#123") allowing the action. **Insight:** The log becomes a record of fiduciary compliance. | **Analysis:** Log entries include the cryptographic hash of the agent's plugin manifest, ensuring that the action was performed by an approved version of the code. **Insight:** Chains operational accountability to supply-chain integrity. | **Analysis:** The act of reviewing the log before approval is a moment of positive friction, forcing the human to pause and consider the action's implications. **Insight:** The log is a UX element that encourages deliberate, safer decision-making. |
| **Digital Veto** | **Analysis:** Provides the ultimate accountability backstop. It assigns a single, clear point of responsibility for halting the entire system in an emergency. **Insight:** Concentrates accountability in a crisis, preventing diffusion of responsibility. | **Analysis:** The veto action itself is verifiable. A signed, timestamped event is logged, proving who issued the veto and when. **Insight:** Even the emergency stop is auditable. | **Analysis:** High cognitive load to activate (by design), but its existence reduces the background cognitive load of "what if something goes wrong?" for operators. **Insight:** A high-friction "panic button" that provides low-friction peace of mind. | **Analysis:** A direct and robust implementation of the "stop button" or "interruption" capability required by EU AI Act Art. 14 (Human Oversight). Maps to NIST MANAGE 2.4 (Disengage/Deactivate Systems). **Insight:** This is a non-negotiable feature for high-risk AI system compliance. | **Analysis:** The ultimate expression of fiduciary override. It allows a human to halt any automated process, no matter how profitable or efficient, if it is deemed harmful. **Insight:** Codifies the principle that human fiduciary judgment supersedes automated optimization. | **Analysis:** The veto mechanism must be protected from the supply chain it governs. It should operate on a separate, hardened control plane if possible. **Insight:** The integrity of the kill-switch is paramount. | **Analysis:** A classic example of positive friction. It should require a two-step confirmation (e.g., "Type 'VETO' to confirm") to prevent accidental activation.27 | **Insight:** The friction makes the safety feature more trustworthy by making it feel deliberate and robust. |  |
| **VC-Signed Plugin Manifests** | **Analysis:** Extends accountability to the development and deployment pipeline. It ensures that only code from a verified source, with a known bill of materials, can be run. **Insight:** Shifts accountability "left," making developers accountable for the integrity of their code before it ever runs. | **Analysis:** The manifest provides a verifiable statement of the plugin's identity and contents, which can be checked without needing to understand the code itself. **Insight:** Verifies the "what" (the code package) before the governance layer even considers "what it wants to do." | **Analysis:** Reduces cognitive load for security auditors, who can rely on cryptographic verification instead of manual code review for every update. **Insight:** Automates a high-load, high-stakes verification task. | **Analysis:** Aligns with NIST Cybersecurity Framework principles for software supply chain security and NIST GOVERN 6 (Third-Party Risk). **Insight:** Addresses a critical, known vulnerability vector in the WordPress ecosystem.29 | **Analysis:** Ensures that agents handling fiduciary data have not been tampered with, upholding the duty of care. **Insight:** A technical control that enforces a core fiduciary principle. | **Analysis:** This is the core control for this lens. It directly addresses the risk of a compromised plugin by using verifiable credentials (VCs) to establish a chain of trust from developer to runtime.16 | **Insight:** Applies modern, decentralized identity principles to solve a classic software supply chain problem. | **Analysis:** Adds friction to the developer workflow (signing builds) but this is positive friction that prevents catastrophic security failures downstream. **Insight:** A small amount of developer friction prevents a massive amount of operational friction. |  |

## **P2 – Governance Blueprint: The Agent-Administrator Architecture**

This section translates the requirements derived from the multi-lens analysis into a concrete architectural design. It specifies the user interface, approval workflows, and core mechanisms that constitute the verifiable governance layer.

### **Agent-Administrator UI Mockup (Conceptual Wireframe)**

The user interface is designed for clarity, auditability, and the management of cognitive load. It is not a replacement for the standard WordPress admin panel but an overlay specifically for governing MCP agent actions.

* **Dashboard View: The "Action Command Center"**  
  * **Primary Element:** A real-time queue of "Pending Agent Actions."  
  * **Queue Item Details:** Each item in the queue is a card displaying:  
    * **Agent ID:** A verifiable identifier for the agent (e.g., did:web:acme:agent:seo-v3.1).  
    * **Requested Action:** A human-readable summary (e.g., "Publish 15 new blog posts").  
    * **Justification Snippet:** The first line of the agent's formal justification (e.g., "Fulfilling content calendar for Q3 campaign...").  
    * **Risk Tier:** A prominent, color-coded badge: **Low** (Green), **Medium** (Yellow), **High** (Red).  
    * **Action Timer:** A countdown timer indicating "Expires in T-minus \[hh:mm:ss\]," creating urgency for review.  
* **Detail View: The "Decision & Audit Context"**  
  * Clicking a queue item expands it into a detailed modal view, designed to provide all necessary context for an informed decision, directly addressing EU AI Act Art. 14's requirements for effective human oversight.  
  * **Verifiable Justification Log:** The full, immutable claim made by the agent *before* the action request. This includes the specific parameters of the action (e.g., post\_ids: \[101, 102,...\], publish\_date: "2025-10-26T09:00:00Z").  
  * **Automated Risk Analysis:** An explicit explanation of *why* the action was assigned its risk tier. This is crucial for compliance and trust.  
    * *Example for a High-Risk action:* "This action is rated **High** because: (1) It executes wp\_delete\_user, an irreversible action. (2) It targets users with the 'Customer' role, potentially involving PII. (3) The number of targets (5,000+) exceeds the 'Bulk Action' policy threshold."  
  * **Simulated Outcome (Hypothesis):** A "dry run" summary displaying the expected result of the action (e.g., "This will delete 5,000 users and their associated content. This action cannot be undone.").  
  * **Approval Controls:**  
    * Approve: For Medium and High-risk actions. May be disabled until a checkbox "I have reviewed the risks and approve this action" is ticked. For High-risk actions, clicking this triggers an MFA prompt.  
    * Deny: Rejects the action, requiring the approver to provide a brief reason for the denial, which is also logged.  
    * Escalate: Forwards the request to a higher-level approver or a specific group (e.g., "Compliance Team").  
* **The Digital Veto Interface**  
  * A system-wide, persistent UI element, visually distinct from all other controls (e.g., a red, shielded button in the header labeled "EMERGENCY VETO").  
  * Activation follows a positive friction pattern to prevent accidental use 27:  
    1. Clicking the button opens a full-screen modal.  
    2. The modal displays a stark warning: "This will immediately halt all active MCP agents and attempt to roll back any uncompleted actions. This is an emergency measure."  
    3. A text field requires the user to type the word VETO to enable the final confirmation button.  
  * This design provides the unambiguous "stop button" capability mandated by EU AI Act Art. 14\.

### **Tiered Approval & Action Flow**

This workflow diagram illustrates how the system manages actions based on their calculated risk, balancing developer velocity with robust oversight.

1. **Low-Risk Flow (e.g., Categorizing a draft post, regenerating image thumbnails)**  
   * **Trigger:** MCP Agent submits a signed action request to the Governance Layer.  
   * **Process:**  
     1. Governance Layer validates the agent's signature and the integrity of its manifest.  
     2. The action is classified as Low-Risk based on predefined policies (e.g., reads data, modifies only drafts, no PII).  
     3. The request is logged with a status of "Auto-Approved."  
     4. The action is executed against the WordPress core.  
     5. A Verifiable Credential (VC) is issued to the log, cryptographically attesting to the successful, audited action.  
     6. The Human Administrator receives a low-priority notification in a daily digest for post-hoc review.  
   * **Outcome:** Maximum velocity for safe, routine tasks with full auditability.  
2. **Medium-Risk Flow (e.g., Editing a published page, changing SEO metadata on live posts)**  
   * **Trigger:** MCP Agent submits a signed action request.  
   * **Process:**  
     1. Governance Layer validates signature and manifest.  
     2. Action is classified as Medium-Risk (e.g., modifies live content, no PII).  
     3. Request is logged and enters the "Pending Agent Actions" queue in the UI.  
     4. Human Administrator receives a standard notification.  
     5. Administrator reviews the details in the UI and clicks Approve.  
     6. The approval is logged. The action is executed.  
     7. A VC is issued to the log.  
   * **Outcome:** Human-in-the-Loop oversight for actions with moderate impact, ensuring intent is verified.  
3. **High-Risk Flow (e.g., Bulk-deleting users, installing a new plugin, modifying user roles)**  
   * **Trigger:** MCP Agent submits a signed action request.  
   * **Process:**  
     1. Governance Layer validates signature and manifest.  
     2. Action is classified as High-Risk (e.g., irreversible, involves PII, changes security posture).  
     3. Request is logged and enters the UI queue with a high-visibility alert.  
     4. Human Administrator receives a high-priority alert (e.g., SMS, push notification).  
     5. Administrator must complete a full review in the UI and approve via Multi-Factor Authentication (MFA).  
     6. Upon successful MFA, the Governance Layer issues a temporary, single-use, narrowly-scoped capability token to the agent.  
     7. The agent uses the token to execute the single, specific action. The token is immediately invalidated.  
     8. A VC is issued to the log.  
   * **Outcome:** Maximum security and accountability for the most dangerous actions, adhering to the principle of least privilege through just-in-time capabilities.  
4. **Digital Veto Path**  
   * **Trigger:** Human Administrator activates the Emergency Veto via the UI.  
   * **Process:**  
     1. The Veto command is logged with the administrator's signature.  
     2. The Governance Layer immediately revokes all active capability tokens and sends a "HALT" signal to all connected MCP agents.  
     3. The system enters a "safe mode," where no new agent actions can be initiated until the veto is lifted by a qualified administrator.  
     4. An incident response workflow is triggered.  
   * **Outcome:** An immediate, auditable, system-wide stop that provides the ultimate safety control required by regulation.30

## **P3 – Compliance Alignment Matrix: Bridging Architecture and Regulation**

A core design principle of this framework is "compliant by design." This matrix serves as a definitive crosswalk, demonstrating how each architectural component directly maps to and satisfies specific requirements within the NIST AI Risk Management Framework (RMF) and the EU AI Act. This artifact is intended for compliance officers, auditors, and legal teams to verify the system's regulatory posture.

| Governance Primitive/Component | NIST AI RMF Mapping | EU AI Act Mapping | Local Policy Mapping (Template) | Gap & Overlap Analysis |
| :---- | :---- | :---- | :---- | :---- |
| **Agent-Administrator Role** | **GOVERN 2.1**: Establishes clear, documented roles and responsibilities for AI risk management. The role is the designated point of accountability for mediating agent actions.31 | **Art. 14(4)**: Requires that persons assigned human oversight have the necessary competence, training, and authority. The Agent-Administrator role is the locus of this authority.32 | Internal IT Security Policy 5.3: AI Agent Oversight | Both frameworks require defined responsibilities. The EU AI Act's focus on "authority" is more explicit, which the Agent-Administrator role embodies by being the sole gatekeeper for agent capabilities. |
| **Tiered Approval Workflow** | **MANAGE 1.2**: Prioritizes the treatment of documented AI risks based on impact and likelihood. The tiered system is a direct implementation of this prioritization.31 | **Art. 9**: Requires a "risk management system" that is continuous and iterative. The tiered workflow is the operationalization of this system, classifying and managing risks proportionally.32 | Risk Management Framework 2.1: Action Classification | NIST's MANAGE function is about prioritization, while the EU's Art. 9 is about the *system* of management. The tiered workflow satisfies both: it is the system that enacts the prioritization. |
| **Immutable Justification Log** | **MEASURE 3.1**: Requires approaches to regularly identify and track AI risks. The log provides the raw data for this tracking. **GOVERN 1.1**: Ensures legal/regulatory requirements are documented.31 | **Art. 12**: Mandates record-keeping (logs) to ensure traceability. **Art. 19**: Requires that high-risk systems technically allow for the automatic recording of events (logs).32 | Data Governance Standard 4.5: Audit Trail Requirements | The EU AI Act is highly prescriptive about logging ("automatically generated logs"). Our design for an immutable, cryptographically chained log exceeds the minimum requirement and aligns with best practices for non-repudiation, satisfying both frameworks robustly. |
| **Digital Veto** | **MANAGE 2.4**: Specifies that mechanisms must be in place to "supersede, disengage, or deactivate AI systems" that perform inconsistently.31 | **Art. 14(4)(d)**: Explicitly requires that human overseers have the ability to "intervene in the operation of the high-risk AI system or interrupt it" via a "stop button".32 | Incident Response Plan 3.1: System Kill-Switch Protocol | The EU AI Act's "stop button" language is more direct and imperative than NIST's "disengage" language. The Digital Veto is designed to meet this stricter, more explicit requirement, thus comfortably covering the NIST guideline. |
| **VC-Signed Plugin Manifests** | **GOVERN 6.1**: Addresses AI risks associated with third-party entities and supply chains. **MEASURE 2.7**: Evaluates AI system security and resilience.31 | **Art. 15**: Requires systems to achieve an appropriate level of cybersecurity and resilience against attempts to alter their use or performance.32 | Vendor Security Policy 7.2: Software Bill of Materials (SBOM) & Integrity | This control primarily addresses software supply chain security, a key aspect of cybersecurity in both frameworks. While not explicitly mandated in the same way as logging, it is a critical measure for fulfilling the general requirements of Art. 15 (Cybersecurity) and NIST GOVERN 6\. |
| **High-Risk Action Justification** | **MAP 1.1**: Requires that the intended purpose and context be understood and documented. The justification provides this context for each high-risk action.31 | **Art. 13**: Mandates transparency and provision of information to deployers (in this case, the human approver) so they can understand the system's capabilities and limitations before use.32 | Change Management Protocol 2.4 | The EU's Art. 13 is focused on providing information to the *user/deployer* to enable informed use. Our justification requirement fulfills this by making the approver a well-informed user for each high-risk action. This aligns with NIST's goal of documenting context. |

## **P4 – Failure-Informed Scenario: The "What-Not-to-Build" Post-Mortem**

To fully appreciate the necessity of the proposed governance architecture, it is instructive to analyze a plausible, high-impact failure scenario that would occur in its absence. This hypothetical post-mortem of the "Friday Night Purge" incident serves as a stark illustration of the consequences of relying on outdated governance models for autonomous systems.

**Post-Mortem: The "Friday Night Purge" Incident (Hypothetical)**

* **Incident Summary:** At 02:17 AM UTC on Saturday, the primary corporate website began experiencing cascading page failures. Automated monitoring detected a massive spike in 404 errors. The on-call DevOps lead, paged at 02:21 AM, discovered that thousands of pages, including key product landing pages and blog posts, were being systematically deleted. The root cause was identified as the "ContentOptimizer-v2" MCP agent. The agent was halted at 02:45 AM, but not before approximately 12,500 pages were permanently deleted. Recovery from backup took 18 hours, resulting in significant downtime, data loss for content updated on Friday, and immediate reputational damage.  
* **Timeline of Failure:**  
  * **Friday, 16:30 UTC:** A junior marketing associate, prompted by the ContentOptimizer-v2 agent, approves a "routine content optimization and duplicate cleanup" task via a simple "OK" button in the WordPress dashboard.  
  * **Saturday, 02:15 UTC:** A scheduled cron job activates the ContentOptimizer-v2 agent to begin its task.  
  * **Saturday, 02:16 UTC:** The agent ingests a CSV file of URLs intended for a 301 redirect mapping. Due to a formatting error in the CSV (missing destination column), the agent's logic incorrectly interprets every line item as a "duplicate page to be deleted."  
  * **Saturday, 02:17 UTC:** The agent begins executing a loop of wp\_delete\_post commands with force\_delete=true, bypassing the trash functionality.  
  * **Saturday, 02:21 UTC:** Site-down alerts are triggered. The on-call engineer begins investigation.  
  * **Saturday, 02:35 UTC:** The engineer traces the database write activity to the user account associated with the agent but has no immediate way to see *why* the agent is performing the deletions. The approval log shows only a vague "optimization" approval from the previous day.  
  * **Saturday, 02:45 UTC:** The agent's process is manually killed at the server level.  
* **Root Cause Analysis:**  
  * **Technical Cause:** A combination of a brittle agent script unable to handle malformed input and the use of an irreversible force\_delete command.  
  * **Governance Cause (Primary):** The catastrophic failure was enabled by a complete breakdown in governance architecture.  
    1. **Static, Over-Privileged Role:** The agent operated under a standard WordPress Editor role, which grants persistent delete\_published\_posts capabilities.21 This violates the principle of least privilege. The action of bulk-deleting thousands of pages should have been impossible without a specific, temporary grant of capability. This is a direct consequence of ignoring  
       **Premise 1 (Granular Permissions \= Accountability)**.  
    2. **Lack of Tiered Approvals:** There was no distinction between a low-risk action (e.g., updating a tag) and a high-risk action (e.g., bulk deletion). The approval mechanism was a single, low-friction "OK" button, which induced "approval fatigue" and failed to signal the gravity of the pending action. This highlights the failure of **Premise 3 (HOTL is an Infallible Backstop)**.  
    3. **Absence of Verifiable Justification:** The approval was granted for a vague, abstract goal ("optimization") rather than a concrete, verifiable plan. There was no immutable log entry stating, "I will delete these 12,500 specific post IDs because they are identified as duplicates." This created an unbridgeable accountability chasm 2, making it impossible to determine post-incident if the agent was malfunctioning or correctly executing a flawed but approved plan. This is the failure of  
       **Premise 2 (Transparency is Better than Verifiability)**.  
    4. **No Emergency Veto:** The on-call engineer had no dedicated "kill-switch." The only recourse was a slow, manual process of identifying and killing the server process, during which time thousands of additional pages were lost.  
* **"What-Not-to-Build" Lessons:** This incident was not merely a technical bug; it was a catastrophic failure of governance design. The lessons are clear:  
  1. **NEVER** use static, persistent roles for autonomous agents. Implement just-in-time capability grants.  
  2. **NEVER** use a one-size-fits-all approval mechanism. Friction and oversight must be proportional to risk.  
  3. **NEVER** accept vague justifications for high-impact actions. Demand specific, verifiable, and auditable claims *before* approval.  
  4. **NEVER** deploy a powerful autonomous system without a readily accessible, single-action Digital Veto for immediate, system-wide containment.

## **P5 – Audit & Verifiability Kit: Schemas and Templates**

The foundation of a verifiable governance system lies in its data structures. These schemas are not mere data containers; they are the technical embodiment of the system's commitment to auditability, non-repudiation, and regulatory compliance. They provide the "receipts" that allow auditors to reconstruct the full lifecycle of any agent action.

### **Immutable Justification & Action Log Schema**

This schema defines the structure of a single entry in the cryptographically chained audit log. Each entry is a self-contained record of an agent's request, a human's decision, and the action's outcome.

YAML

\# Immutable Justification & Action Log Schema v1.0.0  
\# Provenance: Designed to meet EU AI Act Art. 12 (Record-Keeping), Art. 19 (Automatically Generated Logs),  
\# and NIST RMF MEASURE/GOVERN functions for full auditability. \[30, 31\]  
log\_entry:  
  id: "ulid" \# Universally Unique Lexicographically Sortable Identifier for time-based sorting.  
  timestamp\_utc: "iso8601" \# Timestamp of log entry creation.  
  agent\_did: "did:web:example.com:agent:content-optimizer-v2.1" \# Verifiable DID of the agent instance.  
  human\_approver\_did: "did:web:example.com:human:compliance-officer:jane-doe" \# Verifiable DID of the human who made the decision. Null for auto-approved actions.  
  action\_request:  
    capability: "delete\_posts\_bulk" \# The specific, fine-grained capability being requested.  
    parameters:  
      post\_ids:   
      force\_delete: true  
      reason\_code: "GDPR\_ERASURE\_REQUEST"  
  justification\_claim:  
    \# A structured, verifiable claim made by the agent PRE-ACTION. This is what the human approves.  
    format: "application/json"  
    content:  
      statement: "Deleting posts in response to verified GDPR Right to Erasure request \#GDPR-REQ-789."  
      evidence\_uri: "https://internal.example.com/tickets/GDPR-REQ-789"  
  risk\_assessment:  
    tier: "High" \# Calculated risk tier (Low, Medium, High).  
    reason: "Action is irreversible (force\_delete) and involves bulk modification based on PII-related policy (GDPR\_ERASURE\_REQUEST)."  
    confidence\_score: 0.99 \# Agent's confidence in its own assessment of the request's validity.  
  approval\_record:  
    status: "Approved" \# Enum: Approved, Denied, Escalated, Auto-Approved.  
    mfa\_verified: true \# Boolean, mandatory for High-Risk.  
    denial\_reason: null \# String, required if status is 'Denied'.  
    timestamp\_utc: "iso8601" \# Timestamp of the human decision.  
  execution\_record:  
    status: "Success" \# Enum: Success, Failure, Halted\_By\_Veto.  
    outcome\_summary: "3 posts permanently deleted from the database."  
    duration\_ms: 410  
    error\_message: null \# String, populated on failure.  
  vc\_issuance\_id: "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6" \# ID of the Verifiable Credential issued for this successful action.  
  log\_hash:  
    \# Cryptographic hash of the current log entry's content.  
    algorithm: "sha256"  
    value: "a1b2c3d4..."  
  previous\_log\_hash:  
    \# Hash of the preceding log entry, creating an immutable chain (blockchain-like).  
    algorithm: "sha256"  
    value: "e5f6g7h8..."

### **DID and Verifiable Credential (VC) Templates**

Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) provide the cryptographic foundation for trust in the system. Agents, humans, and even the governance layer itself have DIDs. VCs are issued to attest to completed, audited actions.

#### **Agent DID Document Template (did:web)**

This JSON-LD document makes an agent cryptographically identifiable and verifiable. It is hosted on the organization's web server.

JSON

// Agent DID Document v1.0.0  
// Provenance: Based on W3C DID Core specification. Allows the agent to sign requests and be verified.  
{  
  "@context": \[  
    "https://www.w3.org/ns/did/v1",  
    "https://w3id.org/security/suites/jws-2020/v1"  
  \],  
  "id": "did:web:example.com:agent:content-optimizer-v2.1",  
  "verificationMethod": \[{  
    "id": "did:web:example.com:agent:content-optimizer-v2.1\#keys-1",  
    "type": "JsonWebKey2020",  
    "controller": "did:web:example.com:agent:content-optimizer-v2.1",  
    "publicKeyJwk": {  
      "kty": "EC",  
      "crv": "secp256k1",  
      "x": "...",  
      "y": "..."  
    }  
  }\],  
  "authentication": \[  
    "did:web:example.com:agent:content-optimizer-v2.1\#keys-1"  
  \],  
  "assertionMethod": \[  
    "did:web:example.com:agent:content-optimizer-v2.1\#keys-1"  
  \]  
}

#### **Verifiable Credential for Action Completion (JSON-LD)**

This VC is the portable, immutable proof that a specific, governed action took place. It is issued by the Governance Layer's DID and can be presented to auditors or other systems as evidence.

JSON

// Governed Action Credential v1.0.0  
// Provenance: Based on W3C Verifiable Credentials Data Model v1.1. Serves as a tamper-proof receipt of a governed action.  
{  
  "@context": \[  
    "https://www.w3.org/2018/credentials/v1",  
    "https://www.w3.org/2018/credentials/examples/v1"  
  \],  
  "id": "urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6",  
  "type": \["VerifiableCredential", "GovernedActionCredential"\],  
  "issuer": "did:web:example.com:governance-layer-v1",  
  "issuanceDate": "2025-10-26T10:00:00Z",  
  "credentialSubject": {  
    "id": "did:web:example.com:agent:content-optimizer-v2.1",  
    "action": {  
      "type": "GovernedAction",  
      "logEntryId": "01H8X1Z...",  
      "capability": "delete\_posts\_bulk",  
      "approver": "did:web:example.com:human:compliance-officer:jane-doe",  
      "status": "Success"  
    }  
  },  
  "proof": {  
    "type": "JsonWebSignature2020",  
    "created": "2025-10-26T10:00:01Z",  
    "proofPurpose": "assertionMethod",  
    "verificationMethod": "did:web:example.com:governance-layer-v1\#keys-1",  
    "jws": "eyJ..."  
  }  
}

## **P6 – Reflexive Integrity Loop: Meta-Audit and Design Upgrades**

A robust governance framework must be self-critical and adaptive. The initial design prompts and assumptions were deliberately subjected to falsification by the analytical lenses described in P1. This reflexive process led to decisive upgrades, hardening the framework against the hidden premises identified in P0.

### **Decisive Tweak 1: From Granular Roles to Just-In-Time (JIT) Capabilities**

* **Initial Flawed Assumption:** The first design impulse was to decompose the WordPress Administrator role into a complex hierarchy of micro-roles for agents (e.g., agent\_post\_publisher, agent\_comment\_moderator). The thinking was that granularity would limit the blast radius.  
* **Falsification via the Accountability-Chasm Lens:** This approach was identified as a more complex version of the same fundamental flaw: Role-Based Access Control (RBAC). A role, no matter how granular, is a *standing permission*.23 An agent with the  
  agent\_comment\_moderator role has that permission 24/7, even when it has no legitimate task to perform. This creates a persistent attack surface and does not solve the accountability problem for an action taken at a specific moment in time.34  
* **Resulting Design Upgrade:** The concept of roles for agents was abandoned entirely. The design was upgraded to a Just-in-Time (JIT) capability model. Agents possess no standing permissions. For each high-risk action, they must *request* a temporary, single-use, narrowly-scoped capability token from the governance layer, which is only granted after explicit human approval. This moves from "who you are" (role) to "what you are verifiably allowed to do right now" (JIT capability), dramatically reducing the attack surface and closing the accountability gap.

### **Decisive Tweak 2: Mandating Structured Justification Claims over Free-Text Explanations**

* **Initial Flawed Assumption:** The initial design for the audit log included a simple free-text field for justification, where the agent would provide a natural language explanation for its requested action.  
* **Falsification via the Verifiability-over-Transparency Lens:** This approach was found to be dangerously weak. Research into explainable AI (XAI) shows that natural language explanations can be post-hoc rationalizations, or even convincing-sounding hallucinations, that do not reflect the true computational drivers of a decision.4 Such an explanation is not falsifiable and therefore not truly auditable. It prioritizes a flimsy form of transparency over robust verifiability.  
* **Resulting Design Upgrade:** The free-text justification field was replaced with a structured justification\_claim object in the log schema (P5). This forces the agent to commit to a structured, machine-readable, and externally verifiable claim *before* the action is approved. For example, instead of saying "I think I should delete this user," it must claim "I am deleting user DID:XYZ in response to GDPR Erasure Request ID:789." The human approves the verifiable claim, not the agent's opaque intention. This transforms the audit process from subjective interpretation to objective verification.

### **Decisive Tweak 3: Explicitly Modeling and Managing Cognitive Load**

* **Initial Flawed Assumption:** The tiered approval system was first designed based solely on technical risk factors (e.g., database writes are high-risk, database reads are low-risk). The human element was considered secondary.  
* **Falsification via the HOTL Friction & Positive Friction Lenses:** This technical-only view ignores the human operator, the most critical component of the system. A system that constantly bombards a human with high-friction approval requests for moderately risky actions will inevitably lead to "approval fatigue".8 The human will start clicking "Approve" without proper review, negating the entire purpose of the oversight mechanism. The system's own design would undermine its security.  
* **Resulting Design Upgrade:** The tiered workflow was redesigned to be a *cognitive load management system*.  
  * **Low-Risk:** Actions are auto-approved to conserve the human's attention and prevent alert fatigue. Oversight is achieved via post-hoc batch review, which has a much lower cognitive cost.  
  * **Medium-Risk:** Requires a simple, low-friction approval, ensuring a human checkpoint without being onerous.  
  * **High-Risk:** Deliberately introduces high, positive friction (MFA, detailed review) to force the human out of autopilot and into a state of deliberate, focused consideration.37 This ensures that the limited resource of human attention is allocated to the highest-consequence decisions.

## **P7 – Packaging: Scorecard and Future Experiments**

This final section provides a concise evaluation of the proposed governance framework against its core objectives and outlines a clear, actionable roadmap for future validation and research.

### **Governance System Scorecard**

This scorecard assesses the framework's performance across five critical axes, with scores from 0 (deficient) to 5 (exemplary).

| Axis | Score | Justification |
| :---- | :---- | :---- |
| **Trust** | **4/5** | The framework builds trust through verifiable processes, not blind faith in AI. The use of positive friction for the Digital Veto 27 and high-risk approvals makes safety features feel robust. The VC-signed manifests provide trust in the software supply chain.16 The score is not 5/5 because ultimate trust also depends on the non-technical aspects of organizational culture, which the framework can only influence, not control. |
| **Auditability** | **5/5** | Exemplary. The immutable, cryptographically-chained log schema (P5) provides an end-to-end, non-repudiable evidence trail that links a specific human intent to a specific machine action. This directly satisfies the stringent record-keeping requirements of EU AI Act Art. 12 & 19 and the principles of the NIST RMF MEASURE function.31 |
| **Latency** | **3/5** | This score reflects a deliberate design trade-off. While low-risk actions are processed with minimal latency, the tiered approval system intentionally introduces latency (friction) for medium- and high-risk actions to ensure safety and human oversight. The system is optimized for accountability and risk mitigation, not raw speed. |
| **Compliance** | **5/5** | Exemplary. As demonstrated in the P3 Compliance Alignment Matrix, every major component of the framework is explicitly mapped to specific articles of the EU AI Act (e.g., Art. 9, 12, 14, 15\) and core functions of the NIST AI RMF (Govern, Map, Measure, Manage). The system is built to be "compliant by design." |
| **Drift-Resilience** | **4/5** | High. The framework is resilient to "accountability drift" by enforcing explicit, logged approvals for changes. It is resilient to "model drift" (where an agent's behavior changes over time) because every action must pass through the same risk assessment and approval workflow. An agent that starts behaving erratically will have its actions flagged as higher risk or denied by human approvers. It is not 5/5 as a dedicated, automated model performance monitoring component is listed as a future experiment. |

### **Next-Experiments List**

The following experiments are proposed to further validate, harden, and extend the framework:

1. **Cognitive Load A/B Test:**  
   * **Objective:** To empirically determine the optimal information density for the high-risk approval UI (P2).  
   * **Method:** Create two UI mockups: (A) a dense view with all information presented at once, and (B) a progressive disclosure view that reveals details on demand. Recruit participants from the target user group (e.g., compliance officers). Measure task completion time, error rates, and subjective cognitive load using the NASA-TLX survey for a series of high-risk approval tasks.39  
   * **Hypothesis:** The progressive disclosure UI (B) will result in lower cognitive load and higher decision accuracy.  
2. **Red Team Security Simulation:**  
   * **Objective:** To stress-test the governance layer's resilience against adversarial attacks.  
   * **Method:** Task an independent red team with achieving specific unauthorized outcomes. Scenarios should include:  
     * Attempting to bypass MFA on a high-risk approval.  
     * Injecting a malicious, unsigned MCP agent plugin and attempting to get it to perform an action.  
     * Socially engineering a human administrator to approve a malicious high-risk action.  
     * Attempting to tamper with the immutable audit log.  
   * **Hypothesis:** The combination of cryptographic identity (DIDs/VCs), MFA-gated approvals, and a chained log will prevent unauthorized execution and ensure any attempt is detected.  
3. **Fiduciary Conflict Simulation:**  
   * **Objective:** To validate that the system can technically enforce fiduciary duty over business logic.  
   * **Method:** Configure an agent to propose a high-ROI action that violates a data privacy policy (e.g., "Create a marketing segment using unconsented PII from user profiles").  
   * **Hypothesis:** The system's risk assessment engine, configured with data fiduciary policies, will automatically classify this as a High-Risk action and route it to a designated Data Protection Officer for denial, even if a standard business manager would have approved it based on ROI. This tests the system's ability to enforce hierarchical, policy-based overrides.19  
4. **Scalability and Throughput Stress Test:**  
   * **Objective:** To ensure the logging and VC issuance pipeline does not become a bottleneck in a high-velocity environment.  
   * **Method:** Simulate 1,000 MCP agents concurrently submitting 100 low-risk (auto-approved) actions per second. Monitor the latency of the logging service, the VC issuance rate, and the database performance.  
   * **Hypothesis:** The architecture will maintain acceptable performance under load, proving its viability for large-scale enterprise WordPress deployments.

#### **Works cited**

1. What executives need to know about the age of AI \- IT-Online, accessed July 3, 2025, [https://it-online.co.za/2025/07/01/what-executives-need-to-know-about-the-age-of-ai/](https://it-online.co.za/2025/07/01/what-executives-need-to-know-about-the-age-of-ai/)  
2. (PDF) Bridging the AI Accountability Gap: The Role of Collaboration ..., accessed July 3, 2025, [https://www.researchgate.net/publication/390785175\_Bridging\_the\_AI\_Accountability\_Gap\_The\_Role\_of\_Collaboration\_Paradigms\_and\_Reason-Responsiveness](https://www.researchgate.net/publication/390785175_Bridging_the_AI_Accountability_Gap_The_Role_of_Collaboration_Paradigms_and_Reason-Responsiveness)  
3. Investigating accountability for Artificial Intelligence through risk governance: A workshop-based exploratory study \- PMC, accessed July 3, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9905430/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9905430/)  
4. Verifiability as a Complement to AI Explainability: A ... \- PhilSci-Archive, accessed July 3, 2025, [https://philsci-archive.pitt.edu/20297/1/Verification%20as%20a%20Complement%20to%20AI%20Explainability%23final.pdf](https://philsci-archive.pitt.edu/20297/1/Verification%20as%20a%20Complement%20to%20AI%20Explainability%23final.pdf)  
5. What Is Verifiable AI? A Guide to Transparency and Trust in AI \- Identity.com, accessed July 3, 2025, [https://www.identity.com/what-is-verifiable-ai-a-guide-to-transparency-and-trust-in-ai/](https://www.identity.com/what-is-verifiable-ai-a-guide-to-transparency-and-trust-in-ai/)  
6. What is the difference between verifiability, interpretability, transparency, and explainability?, accessed July 3, 2025, [https://aisafety.info/questions/97FU/What-is-the-difference-between-verifiability,-interpretability,-transparency,-and-explainability](https://aisafety.info/questions/97FU/What-is-the-difference-between-verifiability,-interpretability,-transparency,-and-explainability)  
7. Rewriting the Code: How AI-era CTOs are building technology that earns human trust, accessed July 3, 2025, [https://www.peoplematters.in/article/c-suite/rewriting-the-code-how-ai-era-ctos-are-building-technology-that-earns-human-trust-46140](https://www.peoplematters.in/article/c-suite/rewriting-the-code-how-ai-era-ctos-are-building-technology-that-earns-human-trust-46140)  
8. Mastering Cognitive Load in HCI \- Number Analytics, accessed July 3, 2025, [https://www.numberanalytics.com/blog/mastering-cognitive-load-in-hci](https://www.numberanalytics.com/blog/mastering-cognitive-load-in-hci)  
9. Fiduciary Duty and Generative AI in Financial Services \- eRepository @ Seton Hall, accessed July 3, 2025, [https://scholarship.shu.edu/cgi/viewcontent.cgi?article=2633\&context=student\_scholarship](https://scholarship.shu.edu/cgi/viewcontent.cgi?article=2633&context=student_scholarship)  
10. An extensive guide to the NIST AI RMF \- Vanta, accessed July 3, 2025, [https://www.vanta.com/resources/nist-ai-risk-management-framework](https://www.vanta.com/resources/nist-ai-risk-management-framework)  
11. The European Union Artificial Intelligence Act \- EY, accessed July 3, 2025, [https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/ai/documents/ey-eu-ai-act-political-agreement-overview-february-2024.pdf](https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/ai/documents/ey-eu-ai-act-political-agreement-overview-february-2024.pdf)  
12. What is a Multiagent System? | IBM, accessed July 3, 2025, [https://www.ibm.com/think/topics/multiagent-system](https://www.ibm.com/think/topics/multiagent-system)  
13. Multi-Agent Environment Tools: Top Frameworks \- Rapid Innovation, accessed July 3, 2025, [https://www.rapidinnovation.io/post/frameworks-and-tools-for-building-multi-agent-environments](https://www.rapidinnovation.io/post/frameworks-and-tools-for-building-multi-agent-environments)  
14. WordPress Security Vulnerabilities: Common Problems and Solutions \- WPZOOM, accessed July 3, 2025, [https://www.wpzoom.com/blog/wordpress-security-issues/](https://www.wpzoom.com/blog/wordpress-security-issues/)  
15. The Future of WordPress and Securing the Software Supply Chain \- Karim Marucchi, accessed July 3, 2025, [https://marucchi.com/the-future-of-wordpress-and-securing-the-software-supply-chain/](https://marucchi.com/the-future-of-wordpress-and-securing-the-software-supply-chain/)  
16. Does supply chain impact WordPress sites? (Yes, and here's what ..., accessed July 3, 2025, [https://www.liquidweb.com/wordpress/security/supply-chain/](https://www.liquidweb.com/wordpress/security/supply-chain/)  
17. International Coordination for Accountability in AI Governance: Key Takeaways from the Sixth Edition of the Athens Roundtable on Artificial Intelligence and the Rule of Law \- The Future Society, accessed July 3, 2025, [https://thefuturesociety.org/international-coordination-for-accountability](https://thefuturesociety.org/international-coordination-for-accountability)  
18. AI governance: themes, knowledge gaps and future agendas | Emerald Insight, accessed July 3, 2025, [https://www.emerald.com/insight/content/doi/10.1108/intr-01-2022-0042/full/html](https://www.emerald.com/insight/content/doi/10.1108/intr-01-2022-0042/full/html)  
19. New Artificial Intelligence (AI) Regulations and Potential Fiduciary Implications, accessed July 3, 2025, [https://www.foley.com/insights/publications/2025/01/new-artificial-intelligence-ai-regulations-potential-fiduciary-implications/](https://www.foley.com/insights/publications/2025/01/new-artificial-intelligence-ai-regulations-potential-fiduciary-implications/)  
20. Navigating AI and Fiduciary Duties: 10 Key Questions for Your ..., accessed July 3, 2025, [https://www.robinskaplan.com/newsroom/insights/navigating-ai-and-fiduciary-duties-10-key-questions-for-your-organization](https://www.robinskaplan.com/newsroom/insights/navigating-ai-and-fiduciary-duties-10-key-questions-for-your-organization)  
21. WordPress user roles \- A Complete Guide \- Bluehost, accessed July 3, 2025, [https://www.bluehost.com/blog/wordpress-user-roles-and-permissions/](https://www.bluehost.com/blog/wordpress-user-roles-and-permissions/)  
22. WordPress User Roles: Importance, uses, and creation \- CyberPanel, accessed July 3, 2025, [https://cyberpanel.net/blog/unlocking-the-potential-of-wordpress-user-roles](https://cyberpanel.net/blog/unlocking-the-potential-of-wordpress-user-roles)  
23. Security risks of elevated user access and multiple high-privilege accounts in WordPress, accessed July 3, 2025, [https://aamportal.com/article/security-risks-elevated-user-access-high-privilege-wordpress](https://aamportal.com/article/security-risks-elevated-user-access-high-privilege-wordpress)  
24. Cognitive Load in Human Systems \- Number Analytics, accessed July 3, 2025, [https://www.numberanalytics.com/blog/cognitive-load-in-human-systems](https://www.numberanalytics.com/blog/cognitive-load-in-human-systems)  
25. Measuring cognitive load in augmented reality with physiological methods: A systematic review \- Open Research Online, accessed July 3, 2025, [https://oro.open.ac.uk/93209/9/93209final.pdf](https://oro.open.ac.uk/93209/9/93209final.pdf)  
26. Positive Friction: How You Can Use It to Create Better Experiences, accessed July 3, 2025, [https://www.interaction-design.org/literature/article/positive-friction-how-you-can-use-it-to-create-better-experiences](https://www.interaction-design.org/literature/article/positive-friction-how-you-can-use-it-to-create-better-experiences)  
27. Designing Friction For A Better User Experience \- Smashing Magazine, accessed July 3, 2025, [https://www.smashingmagazine.com/2018/01/friction-ux-design-tool/](https://www.smashingmagazine.com/2018/01/friction-ux-design-tool/)  
28. (PDF) Accountability in AI Decision-Making \- ResearchGate, accessed July 3, 2025, [https://www.researchgate.net/publication/390668560\_Accountability\_in\_AI\_Decision-Making](https://www.researchgate.net/publication/390668560_Accountability_in_AI_Decision-Making)  
29. WordPress supply chain attacks: what are they and how to prevent them? \- White Canvas, accessed July 3, 2025, [https://wcanvas.com/blog/wordpress-supply-chain-attacks-what-how-prevent-them/](https://wcanvas.com/blog/wordpress-supply-chain-attacks-what-how-prevent-them/)  
30. The AI Act Explorer | EU Artificial Intelligence Act, accessed July 3, 2025, [https://artificialintelligenceact.eu/ai-act-explorer/](https://artificialintelligenceact.eu/ai-act-explorer/)  
31. Artificial Intelligence Risk Management Framework (AI RMF 1.0), accessed July 3, 2025, [https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)  
32. L\_202401689EN.000101.fmx.xml \- Publications Office of the EU, accessed July 3, 2025, [https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689)  
33. Manage WordPress User Roles and Capabilities the Right Way \- SiteCare, accessed July 3, 2025, [https://sitecare.com/user-roles-and-capabilities/](https://sitecare.com/user-roles-and-capabilities/)  
34. What is more secure checking capabilities of user or checking role of user in WordPress plugin development \- WordPress Stack Exchange, accessed July 3, 2025, [https://wordpress.stackexchange.com/questions/218118/what-is-more-secure-checking-capabilities-of-user-or-checking-role-of-user-in-wo](https://wordpress.stackexchange.com/questions/218118/what-is-more-secure-checking-capabilities-of-user-or-checking-role-of-user-in-wo)  
35. User Roles and Capabilities – Common APIs Handbook \- WordPress Developer Resources, accessed July 3, 2025, [https://developer.wordpress.org/apis/security/user-roles-and-capabilities/](https://developer.wordpress.org/apis/security/user-roles-and-capabilities/)  
36. (PDF) Cognitive Load Measurement as a Means to Advance Cognitive Load Theory \- ResearchGate, accessed July 3, 2025, [https://www.researchgate.net/publication/252083119\_Cognitive\_Load\_Measurement\_as\_a\_Means\_to\_Advance\_Cognitive\_Load\_Theory](https://www.researchgate.net/publication/252083119_Cognitive_Load_Measurement_as_a_Means_to_Advance_Cognitive_Load_Theory)  
37. 12 Good Friction Examples That Help Increase Product Adoption, accessed July 3, 2025, [https://userpilot.com/blog/good-friction/](https://userpilot.com/blog/good-friction/)  
38. How to Reduce and Leverage User Experience Friction \- ESW, accessed July 3, 2025, [https://esw.com/how-to-reduce-and-leverage-user-experience-friction/](https://esw.com/how-to-reduce-and-leverage-user-experience-friction/)  
39. Cognitive load classification of mixed reality human computer interaction tasks based on multimodal sensor signals \- PMC, accessed July 3, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12012078/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12012078/)  
40. \[2402.11820\] A critical analysis of cognitive load measurement methods for evaluating the usability of different types of interfaces: guidelines and framework for Human-Computer Interaction \- arXiv, accessed July 3, 2025, [https://arxiv.org/abs/2402.11820](https://arxiv.org/abs/2402.11820)