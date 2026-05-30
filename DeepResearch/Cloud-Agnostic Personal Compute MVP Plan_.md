

# **A CxEP-Aligned MVP Deployment Plan for the Cloud-Agnostic Personal Compute (CAPC) System**

This document presents a comprehensive Minimum Viable Product (MVP) deployment plan for the Cloud-Agnostic Personal Compute (CAPC) system. The plan is architected according to the principles of Context Engineering 2.0 Design, prioritizing the socio-technical context of its intended users: low-income individuals seeking a viable alternative to purchasing new personal computers. The core objective is to deliver a system that is not only technically functional but also economically sustainable, cognitively accessible, and fundamentally empowering. By transforming older, underutilized local hardware into secure "Digital Sovereignty Shells," CAPC aims to provide equitable access to modern computational resources, fostering digital inclusion while respecting user autonomy and data integrity.

The following blueprint details the technical stack, economic framework, user experience design, and security protocols necessary for a successful pilot deployment. It includes quantifiable metrics for evaluating success, a reflexive critique of the system's inherent risks and limitations, and a proposed experiment to validate the plan's most critical assumption. This report is intended to serve as an expert-level strategic and tactical guide for the project's initial implementation phase.

## **Section 1: MVP Technical Architecture & Stack**

The technical architecture of the CAPC system is founded on a principle of radical minimalism and strategic software selection. The design balances the need for extremely low resource consumption on legacy hardware with the imperative for a responsive, secure, and user-friendly experience. Every component choice is weighed against its potential impact on cost, performance, and the cognitive load placed upon a non-technical user. This section specifies the precise hardware and software configurations for the local client (the 'Digital Sovereignty Shell') and the remote cloud compute node.

### **The 'Digital Sovereignty Shell': Local Client Specifications**

The user's local machine, often a decade-old PC or laptop, is repurposed not merely as a thin client but as a 'Digital Sovereignty Shell'. This shell is a user-controlled, secure environment from which they access their cloud resources. The configuration must be lightweight enough to run smoothly on aging hardware but robust enough to handle the necessary networking and encryption tasks without introducing frustrating latency or complexity.

A thorough analysis of lightweight Linux distributions reveals a spectrum of options, from ultra-minimalist distributions like Puppy Linux, which can run on as little as 300MB of RAM 1, to more full-featured options. While a purely technical assessment might favor the absolute most minimal option, this approach fails to account for the user's context. The target user is likely migrating from a Windows environment and will experience significant cognitive friction with an unfamiliar user interface paradigm. Distributions like Puppy Linux, while technically impressive, can present a "challenging" installation and user experience for novices.1

Therefore, the selection of the operating system is treated as a primary user experience decision. The analysis points decisively toward **Linux Lite**, a distribution explicitly designed as a "gateway operating system" for former Windows users.2 It leverages a customized XFCE desktop to create an interface that is immediately familiar, described as "very user-friendly" and ideal for those new to the open-source ecosystem.1 By prioritizing cognitive familiarity, the system reduces one of the largest barriers to adoption. The hardware and software stack for this shell is detailed below.

| Component | Minimum Requirement | Recommended Specification | Justification |
| :---- | :---- | :---- | :---- |
| **CPU** | 1.0 GHz Processor (Single Core, 64-bit) | 1.5 GHz Dual-Core Processor (64-bit) | Provides a responsive desktop experience that goes beyond simply booting the OS, ensuring that local applications and the VNC/SSH connection run without frustrating lag.1 |
| **RAM** | 1 GB | 2 GB | This is a critical specification. While the OS can run on less, 1 GB is the realistic minimum for smoothly operating the desktop environment, the VNC client, the SSH tunnel, and potential client-side encryption software concurrently. 2 GB is recommended to handle modern web content within the remote session without local system strain.5 |
| **Storage** | 15 GB Free Space | 20 GB Free Space | Sufficiently accommodates the Linux Lite OS, essential applications, and provides space for a small, encrypted local cache for sensitive files before they are transferred to the cloud.6 |
| **OS** | Linux Lite 7.x | Linux Lite 7.x | Chosen for its explicit design as a "gateway" for Windows users. It uses the familiar and lightweight XFCE desktop and is fully functional out-of-the-box, drastically reducing cognitive friction for non-technical users.1 |
| **VNC Client** | TigerVNC Viewer | TigerVNC Viewer | A high-performance, open-source, and platform-neutral VNC client. It is actively maintained and includes support for TLS encryption and advanced authentication extensions, aligning with the system's security requirements.8 |
| **SSH Client** | OpenSSH Client | OpenSSH Client | The de facto standard for secure shell connections, it is robust, secure, and pre-installed on virtually all Linux distributions, including Linux Lite. |
| **Encryption** | Cryptomator | Cryptomator | A user-friendly, open-source tool for client-side encryption. It creates a password-protected "vault" that appears as a simple folder, abstracting the complexity of encryption and aligning perfectly with the Digital Sovereignty principle of user-controlled security.9 |

### **The Cloud Compute Node: Cost-Optimized Google Cloud VM Configuration**

The remote compute node is hosted on Google Cloud Platform (GCP), engineered for maximum cost-efficiency to make the service accessible. The configuration leverages GCP's free tier and lowest-cost instance types to ensure that for many users, the service can be operated at a near-zero monthly cost.

The cornerstone of this strategy is the GCP "Always Free" tier, which provides one e2-micro virtual machine (VM) instance per month at no charge, subject to usage limits and regional availability.11 The

e2-micro instance, with its 2 burstable vCPUs and 1 GB of RAM, is sufficient for basic productivity tasks like web browsing and word processing, making it the ideal default for the MVP.12

For users who find the e2-micro's performance limiting, a clear and cost-effective upgrade path is necessary. The e2-small instance (1 vCPU, 2GB RAM) offers a significant performance improvement. By leveraging Spot VM pricing for this upgrade, users can access this additional power at a discount of 60-91% compared to on-demand rates, albeit with the caveat that the instance can be preempted by GCP.14 This trade-off will be clearly communicated during the upgrade process.

| Component | Default Configuration (Free Tier) | Low-Cost Upgrade | Justification |  |
| :---- | :---- | :---- | :---- | :---- |
| **Machine Type** | e2-micro | e2-small (Spot VM) | The e2-micro is included in the Always Free tier, making the base service potentially free.12 | e2-small Spot VMs provide a substantial performance boost for a minimal, albeit variable, cost, representing the most logical next step.14 |
| **vCPU** | 2 (burstable, shared-core) | 1 (burstable, shared-core) | Sufficient for the target workload of basic productivity, including web browsing, email, and document editing.13 |  |
| **RAM** | 1 GB | 2 GB | 1 GB of RAM is the absolute minimum for a modern lightweight desktop experience. 2 GB provides a much smoother and more capable environment, especially when using multiple browser tabs or applications.16 |  |
| **Storage** | 30 GB Standard Persistent Disk | 30 GB Standard Persistent Disk | The first 30 GB of standard persistent disk storage is included in the Always Free tier, providing ample space for the operating system and a standard suite of user applications.12 |  |
| **Region** | us-west1, us-central1, or us-east1 | us-west1, us-central1, or us-east1 | The free tier e2-micro instance is restricted to these US regions.12 Standardizing on these regions simplifies management, support, and cost prediction for all users. |  |
| **OS** | Ubuntu 22.04 LTS (Server) | Ubuntu 22.04 LTS (Server) | A stable, long-term support release with extensive community support and comprehensive documentation for setting up the required VNC and desktop environment components.18 |  |
| **Desktop Env.** | XFCE | XFCE | XFCE is a well-established lightweight desktop environment known for being fast, stable, and low on system resources. This makes it the ideal choice for a remote desktop hosted on a resource-constrained VM.19 |  |
| **VNC Server** | TightVNC Server | TightVNC Server | TightVNC is a lightweight and performant VNC server that integrates seamlessly with the XFCE desktop environment, as demonstrated in numerous setup guides.18 |  |

### **The Software Ecosystem: A Unified Open-Source Stack**

To create a cohesive and manageable system, a standardized stack of open-source software will be deployed on both the local shell and the cloud VM. This unification simplifies development, documentation, and user support.

#### **Local Shell Software Stack**

The software on the user's local machine is designed for simplicity and security.

* **Linux Lite:** The foundational operating system, providing a familiar desktop experience.2  
* **TigerVNC Viewer:** The client application used to view and interact with the remote desktop.8  
* **Cryptomator:** The tool for creating a secure, encrypted local folder for storing sensitive files before upload or for offline use.9  
* **capc-setup Script:** This custom bash script is the linchpin of the user experience. The technical process of establishing an SSH tunnel requires a complex command-line entry (e.g., ssh \-L 59001:localhost:5901 \-C \-N \-l \<user\> \<ip\_address\>) that is a non-starter for non-technical users.18 The  
  capc-setup script, represented by a single desktop icon labeled "Start My Cloud PC," abstracts this complexity entirely. It will provide simple prompts for the user's server address and username, then construct and execute the necessary command in the background. This script transforms an arcane technical barrier into a simple, accessible action, making it one of the most critical components in the entire system for reducing cognitive friction and ensuring user success.

#### **Cloud VM Software Stack**

The cloud VM is pre-configured with a suite of software to provide a fully functional desktop environment out of the box.

* **Ubuntu Server 22.04 LTS:** The stable, secure, and well-supported base operating system.  
* **XFCE Desktop Environment:** The xfce4 and xfce4-goodies packages provide the complete graphical user interface.18  
* **TightVNC Server:** The tightvncserver package hosts the user's desktop session, making it available for remote connection.18  
* **Essential Applications:** To ensure immediate utility, the VM image will include a curated set of lightweight yet powerful applications, including the Firefox web browser, the LibreOffice suite for productivity 2, the GIMP for image editing 2, and the VLC media player.2  
* **AIDE (Advanced Intrusion Detection Environment):** A lightweight, non-resident, host-based intrusion detection system (HIDS). AIDE works by creating a cryptographic checksum database of critical system files and reports any unauthorized modifications, providing a crucial layer of security with minimal performance overhead.23

## **Section 2: Economic Framework for Sustainable & Predictable Access**

For the CAPC system to be a truly viable alternative for its target audience, its economic model must be designed with two core principles in mind: radical affordability and absolute predictability. The fear of unexpected and uncontrollable cloud bills is a significant barrier to adoption for low-income users. This framework addresses that fear directly through transparent cost simulation and automated governance mechanisms.

### **Pay-As-You-Go Simulation: A Transparent and Predictable Cost Model**

To demystify cloud pricing, it is essential to provide a clear, tangible example of what a typical user can expect to pay. This simulation breaks down costs into their constituent parts: compute time, storage, and network egress. Network egress—the cost of data leaving the GCP network—is a particularly critical component to highlight, as it is often a "hidden" cost that leads to bill shock.25

For this simulation, a "typical user" profile is defined as someone using the service for 4 hours per day, 20 days a month (80 hours total), for basic productivity tasks. This usage is estimated to generate approximately 150 MB of network egress per hour, totaling 12 GB for the month. The simulation uses the low-cost e2-small Spot VM as its basis to demonstrate the affordability of the upgraded tier.

| Cost Component | Unit | Unit Cost (USD) | Monthly Usage | Monthly Cost (USD) | Source/Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Compute (e2-small Spot)** | Hour | \~$0.0067 | 80 hours | $0.54 | Based on average Spot VM pricing for the us-central1 region. This price is variable but serves as a realistic estimate.16 |
| **Storage (Standard PD)** | GB-Month | $0.04 | 30 GB | $1.20 | Standard Persistent Disk pricing. While the first 30GB is free for e2-micro users, it is modeled here for users who upgrade, ensuring transparency.12 |
| **Network Egress** | GB | $0.12 | 11 GB | $1.32 | The first 1 GB of egress per month is free. The subsequent rate for usage up to 1 TB is $0.12 per GB for traffic to North America.12 |
| **Total Estimated Monthly Cost** |  |  |  | **$3.06** | This demonstrates a realistic monthly cost well under the target of $10, providing a powerful computing experience for the price of a cup of coffee. |

This transparent model is the foundation of building trust. For a user on a fixed income, knowing that their monthly cost will be in the range of $3-$5, rather than an unknown and potentially catastrophic figure, is paramount.

### **The 'Epistemic Green Budget': A Framework for User-Centric Cost Certainty**

To move beyond mere transparency and provide active control, the CAPC system introduces the 'Epistemic Green Budget'. This framework reframes the concept of a budget from a restrictive limit to an empowering tool for knowledge and control. During onboarding, each user sets their own budget (e.g., $10 per month), which represents a "green zone" of pre-approved, comfortable spending. The term "epistemic" underscores the system's primary goal: to provide the user with clear, actionable *knowledge* about their consumption patterns.

This framework is implemented using the native Google Cloud Budgets feature, which can be configured programmatically for each user's project.28 These budgets can trigger alerts at specified thresholds based on both actual and forecasted spending, creating a multi-layered notification system.28

| Threshold (% of Budget) | Trigger | User Notification (Email/SMS) | System Action / "Positive Friction" |
| :---- | :---- | :---- | :---- |
| **50%** | Actual Spend | "You have used half of your $\[X\] monthly compute budget. Click here to see your usage dashboard." | None. This is a purely informational nudge designed to build awareness without causing alarm. |
| **90%** | Actual Spend | "**WARNING:** You have used 90% of your $\[X\] budget. To prevent extra charges, your Cloud PC may be stopped automatically if you exceed 100%." | A one-time, non-dismissible modal dialog appears within the VNC session: "You are close to your monthly budget. Continue session?" \[Yes/No\]. This introduces a moment of deliberate, "positive friction." |
| **100%** | Actual Spend | "**ACTION REQUIRED:** You have reached your $\[X\] budget. Your Cloud PC will be stopped in 15 minutes to protect you from unexpected charges." | A persistent banner appears at the top of the VNC session. The system schedules the VM for an automatic shutdown, providing a hard safety net. |
| **100%** | Forecasted Spend | "**HEADS-UP:** Based on your usage so far, you are on track to go over your $\[X\] budget this month. Click here to review your usage patterns." | None. This is a proactive, informational alert designed to encourage early behavior modification. |

### **Automated Cost Governance: Proactive Control and Positive Friction Mechanisms**

The 'Epistemic Green Budget' is enforced through a set of automated mechanisms that provide proactive control and prevent cost overruns. This system design acknowledges that while the primary goal is to reduce cognitive friction in accessing the service, a small amount of *deliberate economic friction* is a necessary and responsible feature to promote user agency and prevent financial harm.

* **Programmatic Shutdowns via Pub/Sub:** The GCP Budgets feature can be configured to publish a notification message to a Pub/Sub topic when a threshold is met.30 A serverless Cloud Function is subscribed to this topic. When the 100% "Actual Spend" message is received, the Cloud Function is triggered, which then executes an API call to stop the user's VM instance.29 This creates an automated, reliable "circuit breaker" that guarantees a user cannot accidentally spend more than their pre-defined budget.  
* **Scheduled Shutdowns for Idle Prevention:** A common source of unexpected cloud costs is forgetting to turn off a VM.32 To mitigate this, every CAPC VM will be configured with a default instance schedule using GCP's "Instance Schedules" feature.33 This schedule will automatically stop the VM every night (e.g., at 2 AM in the user's local time zone). This provides a crucial safety net against prolonged idle usage, while still allowing the user to override the schedule if they need to run a long-running process. This default-off policy is a key tenet of cost-conscious design.

The careful balance between reducing access friction and introducing economic friction is a sophisticated design choice. It moves beyond a simplistic "friction is bad" mindset and recognizes that in different contexts, friction can be a valuable tool for empowerment and protection.

## **Section 3: User Experience (UX) and Support Architecture**

The user experience is architected to minimize cognitive friction for a non-technical user at every stage, from initial setup to daily use. The design philosophy is to abstract away all underlying technical complexity, provide proactive education to prevent common problems, and offer a clear, tiered support pathway when help is needed.

### **A Phased Onboarding Sequence for Minimal Cognitive Friction**

The onboarding process is the user's first interaction with the CAPC system and is critical for building trust and ensuring success. It is designed as a phased, guided journey that prioritizes immediate value delivery and minimizes points of confusion.35 The process leverages established UX patterns like checklists and progress indicators to motivate users and provide a clear sense of accomplishment.37

* **Phase 1: Welcome & Setup (Web Portal):** The journey begins on a simple, accessible web portal. A user signs up and is immediately guided through a single-page setup wizard. This wizard asks for the absolute minimum required information: their desired 'Epistemic Green Budget' (presented as a simple slider), their general geographic region (e.g., "USA \- West"), and their agreement to the terms. Behind the scenes, this simple interaction triggers a powerful automation sequence that provisions their entire GCP environment: the project is created, the VM is configured, and the budget alerts are set.  
* **Phase 2: Local Shell Configuration (Guided Instructions):** Once the cloud environment is ready, the user is directed to a set of clear, step-by-step instructions for preparing their local machine. This guide will use large fonts, clear language, and annotated screenshots to walk them through downloading a custom "CAPC Installer" (a pre-packaged ISO of Linux Lite), creating a bootable USB drive, and running the simplified installer. Upon completion, their old PC boots into a clean desktop with a single, prominent icon: "Start My Cloud PC". All other complexity is hidden.  
* **Phase 3: First Connection and the "Aha\!" Moment:** This is the culmination of the setup process.  
  1. The user double-clicks the "Start My Cloud PC" icon.  
  2. The capc-setup script launches, prompting them with two simple questions: "Please enter the server address from your welcome email:" and "Please enter your username:".  
  3. The script transparently establishes the secure SSH tunnel.  
  4. The TigerVNC client launches automatically, pre-configured to connect to the local end of the tunnel (localhost:59001).  
  5. The user is prompted only for their VNC password (which they set during the web portal setup).  
  6. The connection is established, and the user is presented with their new, fast, and fully functional remote desktop. This moment of seeing a snappy, modern desktop running on their old hardware is the critical "Aha\!" moment that demonstrates the system's value.

### **Proactive Education: Semantic Risk Cartography and the Intent Delta Dashboard**

Instead of reacting to user problems, the CAPC system is designed to anticipate them. This is achieved through a "Semantic Risk Cartography," a process of mapping the potential gaps between the system's technical reality and a user's mental model. By identifying these likely points of confusion, the system can proactively provide education and context.

| Semantic Risk (User Misinterpretation) | System Mitigation (Proactive Education) | 'Intent Delta Dashboard' Visualization |
| :---- | :---- | :---- |
| "My internet is fine, why is the PC so slow?" (Misunderstanding of Latency) | On the user's first login, a welcome tooltip explains: "Your new Cloud PC lives in a data center that might be far away\! A slow or unstable internet connection at home can sometimes make it feel laggy." | A simple "Connection Quality" widget (displaying Green/Yellow/Red) is prominently featured on the dashboard, providing real-time feedback on network stability. |
| "Why was I charged $2 when I barely used it?" (Misunderstanding of Egress Costs) | The dashboard includes a section titled "What am I paying for?" that uses simple language to explain the difference between charges for "Time Used" (the VM running) and "Data Transferred" (egress). | A clear pie chart visualizes the monthly bill, showing the proportion of costs derived from Compute vs. Network Egress. This makes the "hidden" cost of egress visible. |
| "I didn't use it yesterday, why was I charged?" (Misunderstanding of Idle VM Costs) | The default daily shutdown schedule is explained during onboarding. The dashboard clearly displays the "Next Scheduled Shutdown Time" for the user's VM. | A simple timeline view shows blocks of time when the VM was running versus when it was stopped, providing a clear history of usage. |
| "The system stopped me\! It's broken." (Misinterpreting Budget Limit Shutdown) | The email and in-session notifications for the 90% and 100% budget thresholds explicitly state the reason for the action: "This is happening to protect you from extra charges." | A large, clear progress bar shows "Budget Used" vs. "Total Budget," visually framing the shutdown as the successful enforcement of a user-set limit, not a system failure. |

This proactive education is delivered through the **'Intent Delta Dashboard'**. Recognizing that tools like Grafana can be overwhelming for non-technical users 40, the dashboard will be built using

**Metabase**. Metabase is an open-source business intelligence tool specifically designed to allow non-technical users to easily explore and visualize data without needing to write code.40 A read-only Metabase dashboard, accessible via a desktop icon, will present the visualizations from the table above, helping to close the "delta" between the user's intended usage and their actual, billable usage patterns.

### **The Human-in-the-Loop Support Escalation Pathway**

While automation and proactive education can handle most issues, a clear path to human support is essential. The CAPC support model is tiered to provide help efficiently and sustainably.

* **Tier 1: Automated & Self-Service Support:** The primary support tool is the 'Intent Delta Dashboard' itself, which is designed to answer the most common questions about cost and performance. This is supplemented by a "Help" icon on the desktop that links to a simple, clearly written FAQ page.  
* **Tier 2: Community Support:** A moderated online forum (e.g., using a platform like Discourse) will be established for the pilot. This allows users to help one another, fostering a sense of community and ownership while reducing the support load on the core team.  
* **Tier 3: Human Technician Support:** Direct escalation to a human technician is a managed process, triggered by specific, monitored events. These include a user failing to complete the onboarding sequence (tracked via portal analytics), a user-submitted security concern, or a direct request for help via a "Contact Support" form after the user has first consulted the FAQ.

## **Section 4: Protocol for Security and Digital Sovereignty**

The security architecture for CAPC is built on the foundational principles of zero-trust, user-centric control, and verifiable integrity. The goal is to protect the user's data and session integrity while reinforcing the concept of digital sovereignty, ensuring the user remains in control of their digital identity and assets.

### **Mutual Authentication via a Lightweight Verifiable Credential Framework**

A central security challenge is establishing mutual trust: the system must verify the user is legitimate, and the user must be assured they are connecting to the correct system. Standard SSH public key authentication effectively handles client-to-server identity 43, but the CAPC model requires an additional layer of attestation that confirms a user's status as an authorized participant in the program.

While a full implementation of Decentralized Identifiers (DIDs) and W3C Verifiable Credentials (VCs) is too complex for an MVP, the core concepts of the VC model—an issuer, a holder, and a verifier exchanging a tamper-proof credential—can be implemented in a lightweight, practical manner.45

The proposed lightweight framework is as follows:

1. **Issuer:** The automated CAPC Onboarding Service.  
2. **Holder:** The User.  
3. **Verifier:** The user's provisioned Cloud VM.  
4. **The Credential:** The user's SSH public key.  
5. **The Attestation:** During the web-based onboarding, after the user generates their local SSH key pair, the public key is submitted to the CAPC service. The service then acts as a Certificate Authority (CA) and *signs* the user's public key with a master CAPC private key. This signed public key is then returned to the user.  
6. **Verification:** The SSH server on the cloud VM is configured, via the cert-authority directive in the \~/.ssh/authorized\_keys file, to *only* accept connections from clients presenting a public key that has a valid signature from the master CAPC CA key.

This mechanism creates a strong cryptographic link between a user's key and their legitimate, registered status within the CAPC ecosystem. It prevents unauthorized keys from being added to the VM and ensures the server only communicates with clients that have been explicitly "blessed" by the system, effectively hardening the primary access vector.

### **Enforcing Client-Side Encryption for Data at Rest and in Transit**

Protecting user data is non-negotiable and is handled at two distinct levels:

* **Data in Transit:** All communication between the local 'Digital Sovereignty Shell' and the cloud VM is secured by default. The entire VNC session, including all graphical data, keyboard inputs, and mouse movements, is tunneled through an OpenSSH connection. SSH provides robust, end-to-end encryption for the entire data stream, protecting it from eavesdropping or manipulation on the network.22  
* **Data at Rest (Local Shell):** To uphold the principle of digital sovereignty, the user must have a simple and secure way to manage sensitive files on their local machine. The chosen tool for this is **Cryptomator**. Cryptomator is an open-source, client-side encryption application that is exceptionally user-friendly.9 It allows a user to create a password-protected "vault," which is then mounted as a virtual drive. Any file placed into this drive is automatically encrypted on the fly. This approach is vastly more intuitive for a non-technical user than command-line tools like  
  encfs or gocryptfs.49 Cryptomator will be pre-installed on the Linux Lite shell, and the onboarding process will include a simple, guided step for creating and password-protecting their first secure vault.

### **A Reflexive Failure-Informed Mechanism for Intrusion Detection and Auditing**

The system must be able to monitor its own integrity and report deviations from a known-good state. This is achieved through a "Reflexive Failure-Informed" mechanism. "Reflexive" indicates that the system reports on itself, and "Failure-Informed" means that the reporting is designed to highlight failures and unexpected changes, operating on a "silence is golden" principle.

* **Lightweight Host-Based Intrusion Detection (HIDS):** The core of this mechanism is the **Advanced Intrusion Detection Environment (AIDE)**. On a resource-constrained VM like the e2-micro, a heavy HIDS agent like OSSEC or Wazuh would be inappropriate.50 AIDE is a perfect fit; it is a lightweight, non-resident file integrity checker that operates by comparing the current state of the filesystem against a previously generated cryptographic database.23  
* **Implementation:**  
  1. AIDE is installed on the base VM image. During provisioning, an initial database of file checksums for the clean system is generated.  
  2. This "known-good" AIDE database is stored in an immutable location, such as a separate, read-only Google Cloud Storage bucket, to prevent a potential attacker from tampering with it.  
  3. A cron job is scheduled to run an AIDE check (aide \--check) on the VM daily.  
  4. The output of this check is piped to a notification script. If the output is empty (meaning no files have changed), no action is taken. If *any* output is generated, indicating a change in a monitored file, the script immediately emails the full report to a system administrator and raises a high-priority alert in a central monitoring dashboard. This ensures that any potential compromise or unauthorized modification of the core system is investigated immediately.

## **Section 5: MVP Deployment Roadmap & Success Metrics**

This section outlines an actionable, phased roadmap for deploying the CAPC MVP and defines the specific, quantifiable metrics that will be used to evaluate its success. The metrics are aligned with the CxEP framework, focusing not only on technical performance but also on the economic and cognitive impact on the end-user.

### **Phased Deployment Plan: From Controlled Pilot to Scaled Rollout**

The deployment will proceed in three distinct phases to allow for iterative development, risk mitigation, and user-centered refinement.

* **Phase 1 (Months 1-2): Internal Alpha & Tooling Development.** This initial phase is focused on building and testing the core technical components of the system.  
  * **Deliverables:** A finalized base VM image with all necessary software (XFCE, TightVNC, AIDE, essential apps); a functional version of the capc-setup local script; a working web onboarding portal with backend automation for GCP project and VM provisioning; a prototype of the Metabase 'Intent Delta Dashboard'.  
  * **Testing:** The complete system will be tested internally by a team of 5-10 technical users to identify and resolve major bugs and architectural issues.  
* **Phase 2 (Months 3-4): Controlled Pilot with Target Users.** The system is introduced to its intended audience in a controlled, high-support environment.  
  * **Activities:** Recruit a cohort of 20-30 non-technical users through a partnership with a local community organization. Provide hands-on assistance for the initial local shell installation.  
  * **Monitoring:** Closely monitor all aspects of the system: user activity, GCP costs, support requests, and dashboard usage.  
  * **Feedback:** Gather extensive qualitative feedback through post-onboarding surveys and semi-structured interviews to understand the user experience and identify points of friction.  
* **Phase 3 (Months 5-6): Iteration and Expansion.** The data and feedback from the pilot are used to refine and scale the system.  
  * **Actions:** Analyze all quantitative and qualitative data from the pilot. Refine the onboarding flow, the capc-setup script, and the dashboard visualizations to address identified pain points.  
  * **Expansion:** Expand the pilot to a larger group of 100+ users to test scalability. Formalize the community support forum and begin building a base of user-generated documentation and mutual assistance.

### **Key Performance Indicators and CxEP-Aligned Evaluation Metrics**

The success of the CAPC MVP will be measured against a set of specific, quantifiable metrics. These KPIs are designed to provide a holistic view of the project's performance, assessing its technical stability, economic viability, and, most importantly, its effectiveness in providing an accessible and empowering experience for its users.

| Metric | Target | How to Measure | Rationale |
| :---- | :---- | :---- | :---- |
| **User Onboarding Completion Rate** | \>80% | Measured via analytics on the web portal, tracking the percentage of users who successfully progress from initial signup to their first VNC connection. | This is a direct and critical measure of the effectiveness of the cognitive friction reduction strategies, particularly the simplified setup process.35 A low rate indicates a fundamental failure in the UX design. |
| **Monthly Average Cost Per User** | \<$10/month | Calculated from GCP Billing reports, averaged across all active users in the pilot. | This metric validates the core economic hypothesis of the system: that it can provide a powerful computing experience at a price point that is a feasible alternative to new hardware for the target audience. |
| **Cost Overrun Incidents** | \<2% | The number of users whose final monthly bill exceeds their self-selected 'Epistemic Green Budget' by more than 10%. | This directly measures the efficacy of the automated cost governance framework (alerts, positive friction, and programmatic shutdowns) in preventing financial harm and building user trust. |
| **User-Reported Cognitive Friction Score** | \<2.5 | Assessed via a post-onboarding survey using a 1-5 Likert scale, where 1 represents "Very Difficult/Confusing" and 5 represents "Very Easy/Clear". | This is a direct CxEP metric that captures the user's subjective experience of the system's complexity.35 It quantifies how well the design has abstracted away technical barriers. |
| **Security Incident Rate** | 0 | Monitored through the automated AIDE alerts and any user-reported security concerns. | The target is zero critical incidents (e.g., unauthorized VM access, data breach) during the pilot phase, measuring the robustness of the security protocols. |
| **Support Ticket Escalation Rate** | \<10% | The percentage of active users who require Tier 3 (human technician) support during their first month of use. | This metric evaluates the success of the Tier 1 (self-service dashboard, FAQ) and Tier 2 (community forum) support structures in empowering users to solve common problems independently. |

## **Section 6: Reflexive Critique: Addressing Semantic Gaps and Potential for Algorithmic Trauma**

A core practice of Context Engineering 2.0 is reflexive critique: a rigorous self-assessment of a system's potential to cause unintended harm or create new forms of exclusion. While the CAPC system is designed with benevolent intentions, it is crucial to acknowledge its inherent limitations and the potential for negative second-order effects on its vulnerable user base.

* **Dependence on Internet Reliability and the Latency Barrier:** The system's functionality is fundamentally tethered to the quality and reliability of the user's internet connection. For many low-income households, internet service can be inconsistent, metered, or of low bandwidth. This reality creates a significant risk. High latency can make the remote desktop feel sluggish and unresponsive, transforming the promised "powerful PC" into a frustrating and unusable experience. This could inadvertently create a new digital divide, where only those with sufficiently high-quality internet can benefit from the program. The "Connection Quality" widget on the dashboard is a mitigating measure to provide context, but it does not solve the underlying infrastructure problem.  
* **The "Algorithmic Trauma" of Cost Friction:** The 'Epistemic Green Budget' and its associated "positive friction" mechanisms are designed as responsible safeguards against financial harm. However, for a user experiencing financial precarity, the psychological impact of these mechanisms could be negative. Constant notifications about budget usage, warnings of an impending shutdown, and the experience of being automatically "cut off" could induce a state of persistent, low-level anxiety. The system, in its attempt to be a protective guardian, might instead feel like a punitive monitor, creating a stressful user experience. This is a subtle but significant form of "algorithmic trauma" that must be carefully monitored through qualitative user feedback.  
* **The Risk of Skill Degradation and Fostering Dependency:** A key design goal is to abstract away complexity. The capc-setup script, for example, intentionally hides the workings of SSH tunneling. While this lowers the barrier to entry, it also carries the risk of inhibiting learning and skill acquisition. If the system is *too* seamless, it becomes an opaque "magic box." Users may become dependent on the CAPC ecosystem without gaining any transferable knowledge about Linux, cloud computing, or command-line interfaces. This creates a tension between the goals of immediate access and long-term digital literacy and empowerment.  
* **The Semantic Gap: 'Cloud-Agnostic' vs. GCP-Dependent:** The project is named the 'Cloud-Agnostic Personal Compute' system, which implies portability and freedom from vendor lock-in. However, the MVP as designed is deeply intertwined with Google Cloud Platform. It relies specifically on GCP's e2-micro free tier, its budget and alerting APIs, its Pub/Sub and Cloud Functions for automation, and its Instance Scheduling features. Achieving true cloud-agnosticism would require a significant engineering effort to build an abstraction layer over multiple cloud providers' APIs. The MVP's name creates a "semantic gap" with its reality, and it is critical to be transparent with users and stakeholders about this dependency.  
* **Digital Sovereignty vs. Data Gravity:** The 'Digital Sovereignty Shell' provides the user with control over their local hardware. However, as users migrate their workflows and data to the cloud VM, they become subject to the forces of "data gravity." The more data and personalized configuration they build up within their GCP environment, the more difficult and costly it becomes to migrate to another provider or back to a fully local solution. The system, while promoting local sovereignty, may inadvertently lead to a long-term dependency on a single cloud vendor, potentially undermining the very principle of user autonomy it seeks to champion.

## **Section 7: Next Steps: A Proposal for Validating the Highest-Risk Assumption**

Before committing to a full-scale pilot, it is imperative to test the single most critical and uncertain assumption upon which the entire CAPC model rests. This section proposes a targeted, resource-efficient experiment designed to validate this assumption before significant investment is made.

* **The Highest-Risk Assumption:** The central hypothesis of this project is that **a non-technical user can be successfully guided through the process of setting up and using a VNC-over-SSH connection to a cloud VM, and that they will perceive the resulting experience as valuable enough to overcome the inherent challenges of latency, cost management, and the initial setup friction.** If this assumption is false, the entire technical approach is non-viable, regardless of how well the backend systems are architected.  
* **Proposed Experiment: The "Aha\! vs. Annoyance" Sandbox**  
  * **Objective:** To quantitatively measure the user's journey through the onboarding funnel and to qualitatively assess the trade-off between the "Aha\!" moment of accessing a powerful remote PC and the "Annoyance" factors of the setup process, network latency, and cost-related anxiety.  
  * **Methodology:**  
    1. **Recruitment:** Recruit two distinct cohorts (N=15 per cohort) of users who match the target demographic (low-income, non-technical, owners of older PCs).  
    2. **Cohort A (Guided Experience):** This cohort will follow the full, high-touch, phased onboarding plan as detailed in Section 3.1. They will use the web portal, the guided installer, and the simplified capc-setup script.  
    3. **Cohort B (Minimalist Control):** This cohort will act as a control group to validate the necessity of the extensive UX abstractions. They will be given a more traditional, text-based tutorial with the raw ssh command and minimal graphical aids.  
    4. **Data Collection:**  
       * **Quantitative:** Track the onboarding completion time and success rate for every user in both cohorts.  
       * **Quantitative:** Administer post-session surveys to measure the Cognitive Friction Score, the perceived value of the service, and frustration levels with any experienced latency.  
       * **Qualitative:** Conduct short, semi-structured interviews with five users from each cohort to probe their mental model of the system. Key questions will focus on what they think is happening, what they are paying for, and what their primary concerns are.  
  * **Success Criteria for the Experiment:** For the project to be considered viable for a larger pilot, the following outcomes must be achieved:  
    * The onboarding completion rate for Cohort A must be statistically and significantly higher (target: \>30% higher) than that of Cohort B, proving the value of the UX abstractions.  
    * The average User-Reported Cognitive Friction Score for Cohort A must be below the pre-defined target of 2.5 on a 5-point scale.  
    * Qualitative feedback from Cohort A must confirm that users grasp the basic value proposition (fast PC for low cost) and are not expressing undue anxiety or confusion about the cost model and budget alerts.

This experiment serves as the most critical "semantic verification sandbox" for the project. Its results will provide the definitive data needed to either proceed with confidence to the controlled pilot, or to pivot the entire technical strategy toward a different, less complex approach if the core assumption is invalidated.

#### **Works cited**

1. Want to save your old computer? Try one of these 8 Linux distros for free \- ZDNet, accessed July 13, 2025, [https://www.zdnet.com/article/want-to-save-your-old-computer-try-one-of-these-8-linux-distros-for-free/](https://www.zdnet.com/article/want-to-save-your-old-computer-try-one-of-these-8-linux-distros-for-free/)  
2. This free Linux distro is the easiest way to revive your old computer. How it works | ZDNET, accessed July 13, 2025, [https://www.zdnet.com/article/this-free-linux-distro-is-the-easiest-way-to-revive-your-old-computer-how-it-works/](https://www.zdnet.com/article/this-free-linux-distro-is-the-easiest-way-to-revive-your-old-computer-how-it-works/)  
3. Linux Lite Easy to Use Free Linux Operating System, accessed July 13, 2025, [https://www.linuxliteos.com/](https://www.linuxliteos.com/)  
4. 5 Linux Distributions to Breathe New Life Into Old Hardware \- How-To Geek, accessed July 13, 2025, [https://www.howtogeek.com/linux-distributions-to-breathe-new-life-into-old-hardware/](https://www.howtogeek.com/linux-distributions-to-breathe-new-life-into-old-hardware/)  
5. Best lightweight Linux distro of 2025 \- TechRadar, accessed July 13, 2025, [https://www.techradar.com/news/best-lightweight-linux-distro](https://www.techradar.com/news/best-lightweight-linux-distro)  
6. Best Lightweight Linux Distributions for Older Computers \[With System Requirements\], accessed July 13, 2025, [https://itsfoss.com/lightweight-linux-beginners/](https://itsfoss.com/lightweight-linux-beginners/)  
7. 9 Best Linux Distros in 2025 \- RunCloud, accessed July 13, 2025, [https://runcloud.io/blog/best-linux-distros](https://runcloud.io/blog/best-linux-distros)  
8. TigerVNC, accessed July 13, 2025, [https://tigervnc.org/](https://tigervnc.org/)  
9. Cryptomator \- Free & Open-Source Cloud Storage Encryption, accessed July 13, 2025, [https://cryptomator.org/](https://cryptomator.org/)  
10. Cryptomator for Windows, macOS, and Linux: Secure client-side encryption for your cloud storage, ensuring privacy and control over your data. \- GitHub, accessed July 13, 2025, [https://github.com/cryptomator/cryptomator](https://github.com/cryptomator/cryptomator)  
11. Free Trial and Free Tier Services and Products \- Google Cloud, accessed July 13, 2025, [https://cloud.google.com/free](https://cloud.google.com/free)  
12. Free cloud features and trial offer | Google Cloud Free Program, accessed July 13, 2025, [https://cloud.google.com/free/docs/free-cloud-features](https://cloud.google.com/free/docs/free-cloud-features)  
13. GCP Instance Types: Summary, Comparison & Recommendations \- CloudBolt, accessed July 13, 2025, [https://www.cloudbolt.io/gcp-cost-optimization/gcp-instance-types/](https://www.cloudbolt.io/gcp-cost-optimization/gcp-instance-types/)  
14. VM instance pricing | Google Cloud, accessed July 13, 2025, [https://cloud.google.com/compute/vm-instance-pricing](https://cloud.google.com/compute/vm-instance-pricing)  
15. Google Cloud Pricing: The Complete Guide \- Spot.io, accessed July 13, 2025, [https://spot.io/resources/google-cloud-pricing/google-cloud-pricing-the-complete-guide/](https://spot.io/resources/google-cloud-pricing/google-cloud-pricing-the-complete-guide/)  
16. Google Compute Engine Machine Type e2-small, accessed July 13, 2025, [https://gcloud-compute.com/e2-small.html](https://gcloud-compute.com/e2-small.html)  
17. Analysis of Linux Distributions : r/linux4noobs \- Reddit, accessed July 13, 2025, [https://www.reddit.com/r/linux4noobs/comments/1fkamqs/analysis\_of\_linux\_distributions/](https://www.reddit.com/r/linux4noobs/comments/1fkamqs/analysis_of_linux_distributions/)  
18. How to Install and Configure VNC on Ubuntu 20.04 | DigitalOcean, accessed July 13, 2025, [https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-20-04)  
19. Top 10 Best light weight desktop environments (Linux) for low end pc and laptop in 2025, accessed July 13, 2025, [https://theserverhost.com/blog/post/best-light-weight-linux-desktop-environments](https://theserverhost.com/blog/post/best-light-weight-linux-desktop-environments)  
20. The Best Linux Desktop Environments for Productivity \- SkySilk, accessed July 13, 2025, [https://www.skysilk.com/blog/linux-desktop-environments/](https://www.skysilk.com/blog/linux-desktop-environments/)  
21. 13 Lightweight Linux Desktop Environments for Old Computers \- Tecmint, accessed July 13, 2025, [https://www.tecmint.com/top-best-linux-lightweight-desktop-environments/](https://www.tecmint.com/top-best-linux-lightweight-desktop-environments/)  
22. Simple VNC control with vncctl \- The Zone Manager, accessed July 13, 2025, [http://www.thezonemanager.com/2012/01/simple-vnc-control-with-vncctl.html](http://www.thezonemanager.com/2012/01/simple-vnc-control-with-vncctl.html)  
23. AIDE \- Lightweight Linux Host Intrusion Detection \- Darknet, accessed July 13, 2025, [https://www.darknet.org.uk/2025/05/aide-lightweight-linux-host-intrusion-detection/](https://www.darknet.org.uk/2025/05/aide-lightweight-linux-host-intrusion-detection/)  
24. The Best Host-Based Intrusion Detection Systems (HIDS) Tools & Software \- Websentra, accessed July 13, 2025, [https://www.websentra.com/host-based-intrusion-detection-systems-hids-tools-and-software/](https://www.websentra.com/host-based-intrusion-detection-systems-hids-tools-and-software/)  
25. The Ultimate GCP Pricing Guide: Models, Tiers and Services Explained \- Economize Cloud, accessed July 13, 2025, [https://www.economize.cloud/blog/gcp-pricing-guide-models-tiers-services/](https://www.economize.cloud/blog/gcp-pricing-guide-models-tiers-services/)  
26. GCP Egress Cost: Everything you should Know \- Tata Communications, accessed July 13, 2025, [https://www.tatacommunications.com/knowledge-base/gcp-egress-cost/](https://www.tatacommunications.com/knowledge-base/gcp-egress-cost/)  
27. Network pricing | Google Cloud, accessed July 13, 2025, [https://cloud.google.com/vpc/network-pricing](https://cloud.google.com/vpc/network-pricing)  
28. Create, edit, or delete budgets and budget alerts | Cloud Billing \- Google Cloud, accessed July 13, 2025, [https://cloud.google.com/billing/docs/how-to/budgets](https://cloud.google.com/billing/docs/how-to/budgets)  
29. Google Cloud — Billing Budgets and Alerts | by Allan Alfonso \- Medium, accessed July 13, 2025, [https://medium.com/google-cloud/google-cloud-billing-budgets-and-alerts-fc707ac1c2e4](https://medium.com/google-cloud/google-cloud-billing-budgets-and-alerts-fc707ac1c2e4)  
30. Set up programmatic notifications | Cloud Billing, accessed July 13, 2025, [https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications)  
31. Set up advanced billing alerts and logic | Firebase Documentation \- Google, accessed July 13, 2025, [https://firebase.google.com/docs/projects/billing/advanced-billing-alerts-logic](https://firebase.google.com/docs/projects/billing/advanced-billing-alerts-logic)  
32. Google Cloud Free Tier | Sam Currie, accessed July 13, 2025, [https://samscloudblog.dev/posts/blog-free-tier/](https://samscloudblog.dev/posts/blog-free-tier/)  
33. Scheduling a VM instance to start and stop | Compute Engine Documentation, accessed July 13, 2025, [https://cloud.google.com/compute/docs/instances/schedule-instance-start-stop](https://cloud.google.com/compute/docs/instances/schedule-instance-start-stop)  
34. Solved: schedule starting and stopping VM \- Google Cloud Community, accessed July 13, 2025, [https://www.googlecloudcommunity.com/gc/Infrastructure-Compute-Storage/schedule-starting-and-stopping-VM/td-p/796361](https://www.googlecloudcommunity.com/gc/Infrastructure-Compute-Storage/schedule-starting-and-stopping-VM/td-p/796361)  
35. User Onboarding Best Practices To Boost Success | Skilljar, accessed July 13, 2025, [https://www.skilljar.com/blog/7-user-onboarding-best-practices](https://www.skilljar.com/blog/7-user-onboarding-best-practices)  
36. Here's What Makes a User Onboarding Successful (5 Examples) \- UserGuiding, accessed July 13, 2025, [https://userguiding.com/blog/successful-user-onboarding](https://userguiding.com/blog/successful-user-onboarding)  
37. 9 Best Practices for User Onboarding That Gives Results | Userflow Blog, accessed July 13, 2025, [https://www.userflow.com/blog/9-best-practices-for-user-onboarding](https://www.userflow.com/blog/9-best-practices-for-user-onboarding)  
38. User onboarding: best practices and 20 good examples \- Justinmind, accessed July 13, 2025, [https://www.justinmind.com/ux-design/user-onboarding](https://www.justinmind.com/ux-design/user-onboarding)  
39. User Onboarding Best Practices, Examples, Metrics & Tools \- Userpilot, accessed July 13, 2025, [https://userpilot.com/blog/user-onboarding/](https://userpilot.com/blog/user-onboarding/)  
40. What Are the Top 10 Open-Source Dashboard Tools for 2025? \- InetSoft, accessed July 13, 2025, [https://www.inetsoft.com/info/top-10-open-source-dashboard-tools/](https://www.inetsoft.com/info/top-10-open-source-dashboard-tools/)  
41. The Best Open-Source Dashboard Tools for 2025: Expert Guide to Choosing the Right One, accessed July 13, 2025, [https://www.metricfire.com/blog/top-8-open-source-dashboards/](https://www.metricfire.com/blog/top-8-open-source-dashboards/)  
42. Open source Business Intelligence and Embedded Analytics, accessed July 13, 2025, [https://www.metabase.com/](https://www.metabase.com/)  
43. How to verify SSH server credentials \- LabEx, accessed July 13, 2025, [https://labex.io/tutorials/linux-how-to-verify-ssh-server-credentials-434599](https://labex.io/tutorials/linux-how-to-verify-ssh-server-credentials-434599)  
44. Use SSH keys to communicate with GitLab, accessed July 13, 2025, [https://docs.gitlab.com/user/ssh/](https://docs.gitlab.com/user/ssh/)  
45. What are verifiable credentials? \- Digital Impact Alliance, accessed July 13, 2025, [https://dial.global/verifiable-credentials-how-they-work/](https://dial.global/verifiable-credentials-how-they-work/)  
46. Verifiable Credentials Data Model v2.0 \- W3C, accessed July 13, 2025, [https://www.w3.org/TR/vc-data-model-2.0/](https://www.w3.org/TR/vc-data-model-2.0/)  
47. Verifiable Credentials: The Ultimate Guide 2025 \- Dock Labs, accessed July 13, 2025, [https://www.dock.io/post/verifiable-credentials](https://www.dock.io/post/verifiable-credentials)  
48. How to set up VNC to be accessed from outside CSAIL, accessed July 13, 2025, [https://tig.csail.mit.edu/network-wireless/vnc-setup/](https://tig.csail.mit.edu/network-wireless/vnc-setup/)  
49. Folder encryption system for linux : r/linuxquestions \- Reddit, accessed July 13, 2025, [https://www.reddit.com/r/linuxquestions/comments/1iodvdf/folder\_encryption\_system\_for\_linux/](https://www.reddit.com/r/linuxquestions/comments/1iodvdf/folder_encryption_system_for_linux/)  
50. OSSEC \- World's Most Widely Used Host Intrusion Detection System \- HIDS, accessed July 13, 2025, [https://www.ossec.net/](https://www.ossec.net/)  
51. Top 5 open-source HIDS systems \- Logz.io, accessed July 13, 2025, [https://logz.io/blog/open-source-hids/](https://logz.io/blog/open-source-hids/)