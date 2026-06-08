

# **Serverless GCP × MCP × WP-CLI: An Architecture for Intention-Typed Actuation, IAM Segmentation & Ephemeral Blast-Radius Control**

## **Part I: Foundational Architecture & Security Posture**

This initial part of the report establishes the architectural blueprint and foundational security posture of the proposed system. It details the specific components, their interactions, and the core principles of zero-trust and immutability that govern the design.

### **Executive Summary: The Intention-Typed Actuator**

The management of WordPress installations at scale presents a persistent operational dilemma, forcing a trade-off between administrative efficiency and robust security. Traditional hosting on virtual machines (VMs) is plagued by high costs for idle resources, cumbersome manual scaling processes, and the significant operational overhead of server maintenance and patching.1 Concurrently, exposing powerful management interfaces like WP-CLI directly to automated systems or operators creates an unacceptably broad attack surface. A single compromised credential or a flawed script could lead to catastrophic damage, a risk that is amplified in multi-tenant SaaS environments.3

This report engineers and scrutinizes a serverless actuator designed to resolve this dilemma. The architecture leverages ephemeral Google Cloud Run containers to execute WP-CLI commands, facilitating perfect, on-demand scalability from zero and eliminating costs associated with idle capacity.1 The core innovation, however, lies in its security model, which achieves defense-in-depth not by restricting functionality but by abstracting it. An AI agent, or a human operator, interacts with a curated set of "intention-typed" tools defined via the Model Context Protocol (MCP).6 These MCP tools represent high-level goals, such as "update a plugin" or "scan for vulnerabilities," rather than raw command execution.

Each MCP tool is programmatically linked to a dedicated Cloud Run service that runs with the identity of a unique, narrowly-scoped GCP Service Account. This Service Account is granted only the specific IAM permissions required to fulfill its designated task, and no more. This design transforms the WP-CLI, a versatile but high-risk utility, into a collection of discrete, auditable, and policy-governed capabilities. The AI agent can be granted the authority to perform valuable, privileged operations without ever receiving direct, raw access to the underlying WordPress instance or its credentials.

The resulting architecture delivers a trifecta of strategic advantages for modern WordPress management:

* **Hyper-Scalable Management:** Operational capacity scales from zero to handle any number of concurrent management tasks on demand, with costs directly proportional to usage.1  
* **Zero-Trust Security:** The system operates on a principle of least privilege and ephemerality. The compromise of an AI agent or its credentials does not equate to the compromise of the WordPress environment. The blast radius of any potential security event is rigorously contained to a single, short-lived container executing a single, pre-defined action under a highly restrictive IAM policy.9  
* **Governed Autonomy:** AI agents are empowered to conduct privileged operations, enhancing operational efficiency and enabling proactive maintenance. This autonomy is exercised under the strict governance of the MCP interface and GCP's IAM framework, ensuring every action is intentional, authorized, and comprehensively audited.11

### **P0 \- Bias & Premise Register**

To ensure analytical transparency and intellectual honesty, this report begins by declaring its foundational assumptions and potential biases. This register is a critical component of a zero-trust, evidence-first methodology, allowing auditors and peer reviewers to understand the analytical starting point and challenge its core tenets.

| Type | Statement | Lens for Validation |
| :---- | :---- | :---- |
| **Premise 1** | Serverless ephemerality (Cloud Run) is fundamentally more secure and cost-effective than a persistent VM for this spiky, command-execution workload. | Cost-to-Defence Ratio Lens |
| **Premise 2** | The inherent statelessness of WordPress on Cloud Run, which necessitates externalized database (Cloud SQL) and file storage (Cloud Storage), is a manageable architectural complexity whose benefits outweigh the setup overhead.13 | Serverless Ephemerality Lens |
| **Premise 3** | The Model Context Protocol (MCP) provides a sufficiently robust and granular abstraction layer to "sanitize" an AI's intent before it is translated into a potentially dangerous WP-CLI command.6 | Intention-Typing Lens |
| **Premise 4** | Google Cloud's Identity and Access Management (IAM) is granular enough to create a meaningful and enforceable security boundary between different classes of WP-CLI operations (e.g., read-only scans vs. destructive user deletions).9 | IAM Segmentation Lens |
| **Premise 5** | The cold-start latency associated with on-demand Cloud Run containers is an acceptable performance trade-off for the significant security and scalability gains in a backend administrative context.14 | Serverless Ephemerality Lens |
| **Bias 1** | A predisposition towards GCP services over multi-cloud or alternative single-cloud solutions, which may overlook simpler or more cost-effective components from other providers. | (Acknowledged) |
| **Bias 2** | An "automation-first" mindset that may undervalue the critical need for mandatory human-in-the-loop friction for highly destructive or irreversible operations, a risk noted within the MCP specification itself.6 | (Acknowledged) |
| **Bias 3** | A primary focus on technical controls (e.g., IAM, IAP, VPC Service Controls) that might under-represent the residual risk of social engineering or sophisticated insider threats targeting the AI agent's control plane or its human operators. | (Acknowledged) |
| **Bias 4** | The assumption that WordPress's monolithic application design, originally built for a full LAMP stack, can be effectively and performantly retrofitted into a serverless, decoupled architecture without introducing unforeseen compatibility or performance penalties.16 | (Acknowledged) |

### **P2 \- The Cloud-Native Actuator Blueprint**

This section presents the detailed technical architecture of the actuator system, moving from the conceptual framework to a concrete blueprint of GCP services and their interactions.

The diagram below illustrates the flow of a request, originating from an authenticated initiator (an AI agent or a human operator), passing through multiple layers of security, being processed by the ephemeral execution environment, and ultimately interacting with the persistent WordPress data stores.

Code snippet

graph TD  
    subgraph "User/Agent Domain"  
        A\[/"Initiator (AI Agent / Human Operator)"/\]  
    end

    subgraph "Google Cloud Platform (GCP)"  
        subgraph "Authentication & Access Control"  
            IAP\[Identity-Aware Proxy (IAP)\]  
            IAM\[IAM Policy\]  
        end

        subgraph "Execution Plane"  
            CR  
            SA  
            WPCLI  
            MCPServer  
        end

        subgraph "Data Plane (No Public IP)"  
            CSQL  
            GCS  
            CSP  
        end

        subgraph "Observability"  
            LOG\[Cloud Logging & Audit Logs\]  
        end  
    end

    A \--"1. Authenticates (OIDC)"--\> GoogleAuth  
    GoogleAuth\[Google Identity\] \--"2. Issues JWT"--\> A  
    A \--"3. HTTPS Request with JWT"--\> IAP  
    IAP \--"4. Verifies JWT & IAM Policy"--\> IAM  
    IAM \--"5. Authorization Check"--\> IAP  
    IAP \--"6. Forwards Request (w/ IAP JWT)"--\> CR  
    CR \--"Runs as"--\> SA  
    CR \--"Contains"--\> WPCLI  
    CR \--"Contains"--\> MCPServer  
    MCPServer \--"7. Parses MCP Request"--\> WPCLI  
    WPCLI \--"8. Executes Command"--\> CSP  
    CSP \--"9. Secure Connection"--\> CSQL  
    WPCLI \--"Media Ops (via WP-Stateless)"--\> GCS  
    SA \--"Has 'cloudsql.client' Role"--\> CSP  
    SA \--"Has 'storage.objectAdmin' Role"--\> GCS  
    CR \--"10. Writes Structured Logs"--\> LOG  
    IAP \--"Writes Access Logs"--\> LOG

**Architectural Flow and Component Roles:**

1. **Initiator (AI Agent or Human Operator):** The process begins with an initiator seeking to perform a management action. This entity must first authenticate with Google, for instance via a standard Google Sign-In flow, to obtain an OpenID Connect (OIDC) JSON Web Token (JWT).  
2. **Identity-Aware Proxy (IAP):** This managed service acts as the outermost security perimeter. It intercepts all incoming HTTPS traffic destined for the actuator. IAP's primary function is to enforce a zero-trust access policy. It validates the cryptographic signature of the initiator's JWT and then consults an IAM policy to determine if the principal (the user or service account identified in the token) has been granted the roles/iap.httpsResourceAccessor permission.17 If authentication or authorization fails, the request is rejected before it ever reaches the application code.  
3. **Cloud Run (Actuator Service):** At the heart of the system is a stateless container hosting the actuator logic. This service is configured with ingress controls set to "Internal and Cloud Load Balancing," meaning it has no public IP address and can only receive traffic forwarded from the IAP-secured load balancer.18 The container image itself is built to include a lightweight web server (e.g., Flask in Python), the MCP server implementation that exposes the tool API, and the WP-CLI binary.  
4. **Scoped Service Account:** This is the lynchpin of the security model. The Cloud Run service does not run with a default or overly permissive identity. Instead, it is assigned a specific, custom Service Account. As will be detailed in the IAM Segmentation analysis, different actuator services can be deployed for different tiers of tools, each with its own uniquely permissioned Service Account, enforcing the principle of least privilege.10  
5. **Cloud SQL Auth Proxy:** The connection from the ephemeral Cloud Run container to the WordPress database is not made over the public internet. Instead, it is tunneled securely through the Cloud SQL Auth Proxy connector.13 This mechanism uses IAM to authorize connections, ensuring that only the designated actuator Service Account, which must possess the  
   roles/cloudsql.client permission, can establish a database session.19  
6. **Cloud SQL for MySQL:** The managed database instance stores all persistent WordPress data, such as posts, users, and settings. It is configured with no public IP address, making it completely inaccessible from the internet and reachable only from within the GCP network via authorized proxy connections.13  
7. **Cloud Storage (for WP Media):** To handle the stateless nature of Cloud Run containers, WordPress media files are not stored on the local filesystem. A plugin such as WP-Stateless is used to intercept all media uploads and operations, redirecting them to a dedicated Google Cloud Storage (GCS) bucket.13 The actuator's Service Account requires appropriate permissions (e.g.,  
   roles/storage.objectAdmin) on this specific bucket to allow plugins to manage their assets.  
8. **Cloud Logging & Monitoring:** Every layer of the architecture generates critical audit data. IAP logs every access attempt (successful or denied), Cloud Run logs the execution details of the actuator, and the actuator code itself is designed to write structured JSON logs detailing the specific MCP tool, parameters, and resulting WP-CLI command. This creates a comprehensive, immutable audit trail for compliance and incident response.9

This design effectively creates a logical "air gap" between the internet and the core WordPress application assets. The Cloud SQL database and the Cloud Run actuator service itself have no direct public endpoints. An attacker cannot scan them, probe them for vulnerabilities, or attempt to brute-force their credentials. The attack surface is narrowed dramatically to the Google-managed IAP endpoint and the authentication credentials of the small, well-defined set of authorized principals. This represents a profound reduction in risk compared to a conventional WordPress installation that must expose a public IP address to function.

### **P5 (Part 1\) \- CI/CD & Policy-as-Code**

The deployment and maintenance of this architecture are governed by a GitOps model, where a Git repository serves as the single source of truth for both the actuator's application code and the WordPress installation itself. This approach enforces consistency, auditability, and automated, policy-driven deployments through a CI/CD pipeline.

The following cloudbuild.yaml file defines the Cloud Build pipeline responsible for building the immutable container image, publishing it, and deploying it as a new, atomic revision to the Cloud Run service.

**cloudbuild.yaml \- v1.0.0**

YAML

\# Version: 1.0.0  
\# Description: CI/CD pipeline for building and deploying the WordPress Actuator  
\# to Cloud Run. This pipeline treats the WordPress installation as immutable infrastructure.

steps:  
  \# Step 1: Build the container image  
  \# The Dockerfile is responsible for copying the WordPress core, the actuator code,  
  \# all plugins, and themes into a single, self-contained image.  
  \- name: 'gcr.io/cloud-builders/docker'  
    id: Build  
    args:  
      \- 'build'  
      \- '-t'  
      \- 'us-central1-docker.pkg.dev/$PROJECT\_ID/wp-actuator-repo/wordpress-actuator:$COMMIT\_SHA'  
      \- '.'  
    waitFor: \['-'\]

  \# Step 2: Push the container image to Artifact Registry  
  \# Artifact Registry is used for secure, private storage of container images.  
  \- name: 'gcr.io/cloud-builders/docker'  
    id: Push  
    args:  
      \- 'push'  
      \- 'us-central1-docker.pkg.dev/$PROJECT\_ID/wp-actuator-repo/wordpress-actuator:$COMMIT\_SHA'  
    waitFor:

  \# Step 3: Deploy the new image to the Cloud Run service  
  \# This step performs an atomic update, creating a new revision of the service.  
  \# Traffic is automatically migrated once the new revision is healthy.  
  \# Key security configurations like the service account and SQL connection are defined here.  
  \- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'  
    id: Deploy  
    entrypoint: gcloud  
    args:  
      \- 'run'  
      \- 'deploy'  
      \- 'wordpress-actuator-service' \# Name of the Cloud Run service  
      \- '--image'  
      \- 'us-central1-docker.pkg.dev/$PROJECT\_ID/wp-actuator-repo/wordpress-actuator:$COMMIT\_SHA'  
      \- '--region'  
      \- 'us-central1'  
      \- '--platform'  
      \- 'managed'  
      \- '--service-account'  
      \- 'sa-wp-actuator-tier2@${PROJECT\_ID}.iam.gserviceaccount.com' \# Example for a Tier-2 service  
      \- '--add-cloudsql-instances'  
      \- '${PROJECT\_ID}:us-central1:wordpress-main-db'  
      \- '--set-env-vars'  
      \- 'DB\_USER=wordpress\_user,DB\_NAME=wordpress\_db' \# DB\_PASSWORD should be set via Secret Manager  
      \- '--ingress'  
      \- 'internal-and-cloud-load-balancing' \# Restrict access to IAP  
      \- '--allow-unauthenticated' \# Required for IAP to handle auth  
    waitFor: \['Push'\]

\# Specify the image to be stored in Artifact Registry  
images:  
  \- 'us-central1-docker.pkg.dev/$PROJECT\_ID/wp-actuator-repo/wordpress-actuator:$COMMIT\_SHA'

This pipeline fundamentally transforms the WordPress management paradigm. Traditionally, an administrator would log into the WordPress dashboard and click an "Update Plugin" button, which modifies files directly on the live server's filesystem—a classic example of mutable infrastructure. In the Cloud Run model, the container's filesystem is ephemeral and any such changes would be lost on the next deployment or instance restart.13

Therefore, the only way to reliably persist an update to a plugin, theme, or even WordPress core is to modify the source of truth: the contents of the Git repository. A developer wanting to update a plugin would submit a pull request that modifies the plugin files in the repository. Once reviewed and merged, this commit automatically triggers the Cloud Build pipeline. The pipeline builds a completely new, self-contained, and version-controlled container image and deploys it. This process of treating infrastructure and the application stack as code eliminates configuration drift, enhances security by removing the need for live server modifications, and creates a fully auditable and revertible history of the application's state via Git.

## **Part II: Multi-Lens Threat & Opportunity Analysis**

This section forms the analytical core of the report. The architecture is scrutinized through a sequence of seven distinct lenses, each designed to expose specific risks, validate design assumptions, and quantify the inherent trade-offs in the system. The synthesis of these perspectives provides a holistic understanding of the actuator's security posture, performance characteristics, and operational viability.

### **P1 \- Integrated Multi-Lens Analysis**

The following matrix provides a high-density summary of the key findings, risks, and proposed mitigations identified by each analytical lens. It serves as an executive overview of the detailed analysis that follows, allowing stakeholders to quickly grasp the most critical aspects of the system's design across multiple domains.

| Lens | Key Findings | Identified Risks | Proposed Mitigations | Relevant Sources |
| :---- | :---- | :---- | :---- | :---- |
| **Serverless Ephemerality** | Ephemeral containers provide exceptional risk-decay, wiping any potential malware on termination. | Cold-start latency can impact performance for synchronous, user-facing actions. | Use \--min-instances=1 for critical services (trading cost for latency), optimize container images, and leverage Startup CPU Boost. | 1 |
| **IAM Segmentation** | Custom IAM roles can be mapped 1:1 with MCP tool tiers, creating granular security boundaries. | Accidental use of primitive roles (e.g., roles/editor) creates a massive, latent blast radius, nullifying the entire security model. | Strict adherence to custom roles, policy-as-code (IaC) for IAM bindings, and regular automated audits to detect overly permissive roles. | 10 |
| **Intention-Typing** | MCP schemas abstract raw commands into goal-oriented actions, reducing the agent's ability to perform arbitrary operations. | Command injection within tool parameters (e.g., name: "plugin; rm \-rf /") if the actuator code is not secure. | Implement strict input validation and use safe, non-shell-based subprocess execution libraries in the actuator's handler code. Never trust agent input. | 6 |
| **IAP Gatekeeper** | IAP provides a robust, managed OIDC authentication and authorization layer, reducing the application's attack surface to a single point. | Credential theft and token replay attacks within the JWT's expiration window. | Enforce mandatory Multi-Factor Authentication (MFA) on all authorized user accounts. Grant access to groups, not individuals, for easier management. | 9 |
| **Cost-to-Defence Ratio** | The serverless model is highly cost-effective for sporadic/unpredictable workloads compared to an always-on VM. | Sustained, high-volume traffic can make the pay-per-use model more expensive than a fixed-cost VM.1 | Set \--max-instances to cap costs, implement GCP budget alerts, and evaluate traffic patterns to determine if a hybrid or VM model is more economical. | 1 |
| **Observability & Audit** | Structured JSON logs from all layers (IAP, Cloud Run, Actuator) can create a complete, immutable audit trail. | Incomplete or unstructured logs make it impossible to reconstruct an agent's intent during an incident investigation. | Enforce a strict logging schema including a unique trace ID, the actor's principal, the MCP tool called, and the exact WP-CLI command executed. | 9 |
| **Bias-Reflection** | In a multi-tenant SaaS, a shared actuator model is more scalable than per-site service accounts. | A "Confused Deputy" attack, where an agent for Site A tricks the shared actuator into modifying Site B. | The actuator must perform an explicit authorization check at the application layer, verifying the authenticated principal's right to manage the target site\_id. | (Hypothesis) |

### **Serverless Ephemerality Lens**

This lens examines the fundamental trade-offs introduced by using ephemeral, per-request containers as the execution environment for WP-CLI.

The most significant security advantage of this model is **risk-decay**. A Cloud Run container instance may exist for only a few seconds—the time it takes to process a single request or a burst of concurrent requests.19 In the event that a container is compromised, for example through a zero-day vulnerability in a PHP dependency or WordPress itself, the threat is inherently time-bound. The attacker has no opportunity to establish persistence, install rootkits, or move laterally within the network. When the request is complete and the instance scales down, the compromised environment is irrevocably destroyed, along with any malware it contained. This ephemeral nature minimizes the temporal blast radius to mere moments, a dramatic improvement over a persistent VM which, once compromised, can remain a foothold for an attacker indefinitely.

The primary drawback of this ephemerality is **cold-start latency**. When a request arrives and no container instance is "warm" and ready to serve, GCP must perform a series of startup tasks: pull the container image from the registry, start the container process, and wait for the application within (the web server and the WordPress bootstrap process) to initialize and begin listening for requests.1 This can introduce latency ranging from hundreds of milliseconds to several seconds, a delay that could be unacceptable for time-sensitive, user-facing operations. However, for the backend administrative tasks targeted by this actuator, this latency is often a tolerable trade-off for the immense security and scalability benefits.

Several strategies can be employed to mitigate cold-start latency:

* **Minimum Instances:** The most effective method is to configure the Cloud Run service with \--min-instances=1. This instructs GCP to keep at least one container instance running at all times, effectively eliminating cold starts for the first concurrent request.14 This, however, changes the cost model from purely pay-per-use to a hybrid model with a fixed monthly cost for the idle instance, representing a direct trade of cost for performance.15  
* **Startup CPU Boost:** GCP allows for a temporary increase in CPU allocation during the instance startup phase, which can significantly reduce the time it takes to initialize the container and application code.14  
* **Container Optimization:** The startup time is directly related to the size and complexity of the container image. Using lightweight base images, minimizing the number of dependencies, and employing language-specific optimizations like PHP's Composer autoloader can yield faster cold starts.14 Evidence from developers running WordPress on Cloud Run suggests that baking all application content into the image, rather than mounting it from a service like Cloud Storage, can also lead to significant performance improvements by avoiding network latency during initialization.22 This finding strongly supports the immutable infrastructure approach detailed in this report.

### **IAM Segmentation Lens**

This lens focuses on the practical application of the principle of least privilege through the granular segmentation of permissions using GCP's IAM.10 The central strategy is to create a direct mapping between the intended actions defined in the MCP toolset and the explicit permissions granted by custom IAM roles, thereby minimizing the blast radius of a compromised service account.

The core of this strategy is the rejection of a single, monolithic service account for the actuator. Instead, the architecture advocates for deploying distinct actuator services for different tiers of operational risk, each running with a unique service account bound to a hyper-specific custom IAM role.

Consider the following mapping:

* **MCP Tool:** getVulnerabilityReport (Intended action: run wp vulnerability plugin \--format=json)  
* **Custom IAM Role:** roles/wordpressActuator.vulnerabilityScanner  
* **Permissions Granted:**  
  * run.services.invoke: Allows the service to be invoked via its Cloud Run URL.  
  * cloudsql.instances.connect: Allows the service to connect to the Cloud SQL database via the proxy.  
  * This role has **no permissions** to modify data, trigger deployments, or access any other GCP resources.  
* **MCP Tool:** updateSinglePlugin (Intended action: trigger a CI/CD pipeline to update a plugin)  
* **Custom IAM Role:** roles/wordpressActuator.pluginUpdater  
* **Permissions Granted:**  
  * run.services.invoke  
  * cloudsql.instances.connect  
  * storage.objects.create: To allow the plugin update process to write new media assets if needed.  
  * cloudbuild.builds.create: To trigger the Cloud Build pipeline that will build and deploy the new immutable image.

The quantification of the blast radius under this model is stark. In a baseline scenario using a single service account with the primitive roles/editor role, a compromise would grant the attacker control over the entire GCP project, allowing them to delete the database, exfiltrate all data, and deploy malicious code. In the segmented model, if the vulnerabilityScanner service account is compromised, the attacker's capabilities are limited to... running more vulnerability scans. They cannot update plugins, delete users, or even directly read arbitrary data from the database. The potential for damage is effectively neutralized.

This approach transforms IAM from a simple access control list into a form of **semantic firewall**. The custom IAM roles are designed to mirror the *intent* of the MCP tools. When an AI agent invokes the updateSinglePlugin tool, the request is routed to the actuator service running with the pluginUpdater identity. If an attacker manages to find a command injection flaw and attempts to make this tool execute wp db drop, the action will fail at the GCP API level. The underlying service account simply does not possess the cloudsql.databases.delete permission required for that operation. The infrastructure itself is enforcing the semantic boundaries defined by the application's API, creating a powerful defense-in-depth barrier that contains threats even if the application code itself is flawed.

### **Intention-Typing Lens**

This lens stress-tests the granularity and design of the MCP tool schemas. The critical question it seeks to answer is how to define a tool's "intent" with sufficient precision to prevent abuse, without creating an unmanageably complex API for the AI agent.

There is a fundamental trade-off in schema design:

* **Excessively Broad Schema:** A tool defined as executeCLI(command: string) is a security anti-pattern. It completely subverts the intention-typing model by providing a direct pass-through for arbitrary commands. It is functionally equivalent to giving the AI agent raw SSH access and opens the door for an attacker to simply pass command: "wp user delete 1 && rm \-rf /" as a parameter, with catastrophic results.  
* **Excessively Granular Schema:** Conversely, creating a unique MCP tool for every conceivable WP-CLI command and flag combination (e.g., updatePlugin, updatePluginWithVersion, updateAllPlugins, updatePluginDryRun) would result in a bloated and unwieldy API surface. The AI agent would struggle to differentiate between dozens of near-identical tools, leading to errors and inefficient operation.

The optimal design lies in creating tools that represent **goal-oriented actions**. Instead of a generic executeCLI tool, the architecture defines a specific updateSinglePlugin(name: string, version?: string) tool. The actuator's internal code is then responsible for safely constructing the final WP-CLI command (e.g., wp plugin update ${name} \--version=${version}). This encapsulates the low-level command structure and exposes only the high-level intent to the agent.

However, even with well-defined, intention-typed tools, a **residual risk of command injection** persists within the tool's parameters. If the actuator's handler code is not written securely, an attacker could still abuse the system. For example, if a request is received for updateSinglePlugin(name: "my-plugin; wp user delete 1") and the actuator code naively constructs the command string for a shell, the second, malicious command could be executed.

The mitigation for this is non-negotiable: **strict input validation and safe process execution**. The actuator code MUST treat all incoming parameters from the agent as untrusted input. It must never pass these strings directly to a shell for execution. Instead, it must use language-specific, secure subprocess libraries that handle argument arrays properly, preventing the shell from interpreting special characters like semicolons or pipes. For instance, in Python, one must use subprocess.run(\['wp', 'plugin', 'update', name\]) which treats name as a single, safe argument, rather than the dangerous subprocess.run(f"wp plugin update {name}", shell=True).

### **IAP Gatekeeper Lens**

This lens evaluates the trust chain and security posture of the Identity-Aware Proxy (IAP), which functions as the system's primary authentication and authorization gateway.

The token trust chain is robust and relies on established industry standards. The flow begins when a user authenticates with their Google account, which issues a standard OIDC JWT. The user's browser or client application then includes this JWT in the Authorization: Bearer \<token\> header of every request to the actuator's endpoint. IAP intercepts this request, cryptographically verifies the JWT's signature against Google's public keys to ensure its authenticity, and inspects the email and sub (subject) claims within the token. It then compares these claims against its own IAM policy to verify that the principal is authorized to access the resource. If both checks pass, IAP forwards the request to the Cloud Run backend, adding its own special X-Goog-IAP-JWT-Assertion header. This second JWT is signed by Google and securely identifies the authenticated end-user to the backend application code.

The primary vulnerability in this flow is the potential for a **replay attack**. The OIDC JWTs have a finite lifetime, typically one hour. If an attacker manages to steal a valid token, they could potentially replay it to access the system until it expires.

Mitigating this risk relies on two key best practices:

1. **MFA Enforcement:** The most effective countermeasure is to enforce Multi-Factor Authentication (MFA) on all Google accounts that are authorized to access the actuator.9 This dramatically reduces the likelihood of an attacker successfully stealing credentials in the first place.  
2. **Group-Based Permissions:** Instead of granting the roles/iap.httpsResourceAccessor role to individual user accounts, it is best practice to grant it to a Google Group.10 Managing access then becomes a matter of adding or removing users from that group, which is a simpler, less error-prone, and more easily auditable process than modifying numerous individual IAM policy bindings.

Because IAP is a fully managed Google service, it handles the complexities of token validation, session management, and cryptographic verification, allowing the security architect to focus on defining the correct access policies rather than implementing the authentication mechanism itself.

### **Cost-to-Defence Ratio Lens**

This lens provides a pragmatic comparison of the operational costs of the serverless actuator against its defensive capabilities, contrasting it with a traditional baseline of a single VM. The analysis aims to quantify whether the advanced security posture justifies the cost model.

The following table models the estimated monthly costs and key defensive features for two common traffic patterns: a "Low/Sporadic" workload typical of manual administrative actions, and a "High/Sustained" workload characteristic of continuous automated tasks.

| Feature | Serverless Actuator (Cloud Run \+ Cloud SQL) | Baseline VM (e2-medium \+ Local MySQL) |
| :---- | :---- | :---- |
| **Est. Monthly Cost (Low Traffic)** | \~$15 (SQL) \+ \~$2 (Run) \= **\~$17** | **\~$30** (fixed) |
| **Est. Monthly Cost (High Traffic)** | \~$15 (SQL) \+ **$50+** (Run) \= **\~$65+** | **\~$30** (fixed) |
| **Scalability** | Automatic, from 0 to N; scales per-request.1 | Manual configuration or auto-scaling group setup required.1 |
| **Blast Radius** | Ephemeral container, per-request duration, scoped by IAM per-tool. | Entire VM filesystem and processes; persistent until remediated. |
| **AuthN/AuthZ** | Managed IAP (OIDC), granular custom IAM roles.10 | Self-managed SSH keys, OS users, WP users; coarse-grained permissions. |
| **Patching Overhead** | Base container image managed by Google; user patches app code.1 | User responsible for OS, web server, PHP, MySQL, etc..1 |
| **Human Resource Cost** | Low; security primitives are managed services.23 | High; requires dedicated time for hardening, patching, and monitoring. |
| **Defence Value** | **High** (Built-in zero-trust primitives, ephemerality, managed auth). | **Medium** (Entirely dependent on diligent manual configuration). |

For low or unpredictable traffic patterns, the serverless model is demonstrably more cost-effective. The pay-per-use nature of Cloud Run means there are virtually no costs during idle periods, whereas the VM incurs a fixed cost regardless of usage.1 The primary fixed cost in the serverless model is the Cloud SQL instance, which is required for data persistence.13

For high-traffic, long-running, or sustained workloads, the serverless cost model can become more expensive than a fixed-price VM.1 However, this raw financial calculation overlooks the significant, often hidden, human resource cost associated with securing and maintaining a VM. The time spent on OS patching, firewall configuration, security hardening, and manual scaling must be factored into the total cost of ownership. The serverless architecture offloads the vast majority of this operational burden to the cloud provider.23

The conclusion of this analysis is that the vastly superior, built-in security posture of the serverless model provides a much higher "defence value" for its cost. The combination of ephemerality, managed authentication via IAP, and granular IAM segmentation offers a level of security that is difficult and expensive to replicate manually on a traditional VM. For security-critical administrative tasks, this enhanced defensive posture justifies the pay-per-use cost model, which can be further controlled by setting a maximum number of instances (--max-instances) and implementing GCP budget alerts to prevent unexpected cost spikes.

### **Observability & Audit Lens**

This lens focuses on designing the logging and tracing strategy necessary to provide a complete and unambiguous record of every action taken by the system. For security and compliance audits, it must be possible to reconstruct an AI agent's intent and actions from immutable logs.

To achieve this, every log entry generated by the actuator service must be a structured JSON payload written to Cloud Logging. This structure enables powerful querying, filtering, and alerting. The following fields are considered essential for a comprehensive audit trail:

* trace\_id: A unique correlation ID, ideally generated at the start of the request and propagated through all services. This allows an auditor to link the IAP access log, the Cloud Run execution log, and the custom application log for a single event.  
* actor\_principal: The authenticated user or service account email address, securely extracted from the X-Goog-IAP-JWT-Assertion header. This definitively identifies *who* initiated the action.  
* source\_ip: The source IP address of the initiator, also available from IAP logs.  
* mcp\_tool\_called: The string name of the MCP tool that was invoked (e.g., updateSinglePlugin). This captures the agent's high-level *intent*.  
* mcp\_tool\_params: A JSON object containing the exact parameters passed to the tool.  
* wp\_cli\_command\_executed: The exact, sanitized WP-CLI command that the actuator constructed and executed. This provides the ground-truth record of the action performed.  
* wp\_cli\_exit\_code: The numerical exit code from the WP-CLI process (0 for success, non-zero for failure).  
* wp\_cli\_stdout: The standard output generated by the WP-CLI command, which can be useful for debugging and confirming results.

With this structured data, an auditor can easily reconstruct the full narrative of an agent's activity. A simple query in Cloud Logging, filtered by actor\_principal and sorted by timestamp, would reveal a story like: "At 2025-10-26T14:30:05Z, principal ai-patching-agent@service.gserviceaccount.com invoked the getVulnerabilityReport tool. This resulted in the execution of wp vulnerability plugin \--format=json, which returned exit code 0 and a JSON payload of identified vulnerabilities. Ten seconds later, the same principal invoked the updateSinglePlugin tool with parameters {name: 'akismet'}, which triggered a new production deployment." This level of detail is invaluable for incident response and regulatory compliance.

### **Bias-Reflection Lens**

This final lens examines the architecture for potential systemic biases and risks that emerge when scaling the solution, particularly in a multi-tenant SaaS context where a single actuator system might manage thousands of individual WordPress sites.

A naive approach of creating a unique set of service accounts for each tenant would lead to unmanageable **service account sprawl**. The administrative overhead and the sheer number of IAM policies would make the system brittle and impossible to audit effectively. A more scalable architecture would employ a single set of tiered actuator services (e.g., a read-only-actuator, an updater-actuator, and a destructive-actuator) to serve the entire fleet of tenants.

In this multi-tenant model, tenant isolation would be handled within the actuator's application logic. The incoming MCP request would need to include a site\_id or similar tenant identifier. The actuator would then use this identifier to dynamically configure WP-CLI to target the correct site, for instance by using the \--url=\<site-url\> parameter or by connecting to the appropriate tenant-specific database.

This shared actuator model, however, introduces the risk of a **"Confused Deputy" attack**. The actuator service is the "deputy," an entity that possesses broad permissions across many tenants. The "confusion" occurs if an attacker who is a legitimate user of Site A can trick the deputy into performing an action against Site B.

The attack scenario proceeds as follows:

1. An agent, properly authenticated and authorized to manage Site A, intends to send a request: updateSinglePlugin(site\_id: 'site-a', name: 'akismet').  
2. The attacker manipulates this request before it is sent, changing it to: updateSinglePlugin(site\_id: 'site-b', name: 'akismet').  
3. The shared actuator receives this malicious request. It checks its own service account's permissions and finds that it is, in fact, authorized to manage Site B.  
4. The actuator, "confused" about which principal it is acting on behalf of, obediently executes the update against Site B, violating the principle of tenant isolation.

The mitigation for this critical vulnerability must occur at the application layer, inside the actuator's code. The IAP and IAM layers can confirm that the *agent* is allowed to talk to the *actuator*, but they cannot natively know if the agent is allowed to manage the specific site\_id passed in the request payload. Therefore, at the very beginning of every request handler, the actuator MUST perform an explicit authorization check. It must take the actor\_principal (from the IAP JWT) and the site\_id (from the MCP request payload) and query a central authorization database (e.g., a Firestore collection or Cloud SQL table) to verify that this specific principal is indeed authorized to perform actions on this specific site. Only after this application-level authorization check succeeds should the actuator proceed with executing the WP-CLI command.

## **Part III: The Autonomous Agent Interface**

This part defines the precise API contract between the AI agent and the serverless actuator. This interface, specified using the Model Context Protocol, forms the core of the "intention-typed" control system, providing a secure and auditable "allowlist" of capabilities available to the agent.

### **P3 \- The Intention-Typed API Kit**

The following are version-tagged YAML schemas that define the Tools available to the AI agent via the MCP server. These schemas are designed to be human-readable for auditors and machine-readable for both the AI agent (to understand how to call the tool) and the actuator (to know how to validate the request). The tools are organized into tiers based on their potential impact, with higher tiers requiring more stringent controls.

#### **Tier 1: Read-Only & Information Gathering Tools**

These tools have no side effects and are used for discovery and assessment. They are mapped to a service account with the most restrictive IAM permissions.

**v1/getVulnerabilityReport.yaml**

YAML

\# MCP Tool Schema \- Version 1.0.0  
mcp\_version: '1.0'  
tool\_name: getVulnerabilityReport  
description: "Scans installed WordPress plugins, themes, or core for known security vulnerabilities using an underlying WP-CLI vulnerability scanner. Returns a structured JSON report."  
parameters:  
  type: object  
  properties:  
    target:  
      type: string  
      description: "Specify whether to scan 'plugin', 'theme', or 'core'."  
      enum: \['plugin', 'theme', 'core'\]  
    output\_format:  
      type: string  
      description: "The desired format for the report."  
      enum: \['json', 'table'\]  
      default: 'json'  
  required: \['target'\]  
\# Underlying command: wp vulnerability \<target\> \--format=\<output\_format\>  
\# Associated IAM Role: roles/wordpressActuator.vulnerabilityScanner

#### **Tier 2: Safe Updates & Maintenance Tools**

These tools initiate changes to the site but are considered "safe" because they operate within the immutable infrastructure pipeline. They trigger automated, auditable deployments rather than modifying the live environment directly.

**v1/updateSinglePlugin.yaml**

YAML

\# MCP Tool Schema \- Version 1.0.0  
mcp\_version: '1.0'  
tool\_name: updateSinglePlugin  
description: "Initiates a safe update for a single specified plugin. This action triggers a new CI/CD pipeline to build and deploy a new version of the WordPress application with the updated plugin."  
parameters:  
  type: object  
  properties:  
    name:  
      type: string  
      description: "The slug of the plugin to update (e.g., 'akismet')."  
    version:  
      type: string  
      description: "Optional. The specific version to update to. If omitted, updates to the latest available version."  
  required: \['name'\]  
\# Underlying Action: Triggers a Cloud Build pipeline. The pipeline runs 'wp plugin update \<name\> \--version=\<version\>' within its build steps before creating the new container image.  
\# Associated IAM Role: roles/wordpressActuator.pluginUpdater

#### **Tier 3: Destructive & High-Impact Tools**

These tools can cause irreversible data loss or significant changes to the site's state. Their execution requires explicit, out-of-band human approval. This is a critical implementation of "positive friction."

The MCP specification explicitly recommends that hosts obtain user consent before invoking any tool.6 For Tier 3 tools, this principle is enforced programmatically. When the agent calls a tool like

deleteUser, the actuator does not immediately execute the command. Instead, its logic is designed to pause execution and trigger a human-in-the-loop (HITL) workflow. For example, it could post a message to a designated Slack channel or send an email containing the details of the proposed action ("Agent X wants to delete user Y. Justification: Z.") along with "Approve" and "Deny" buttons. The WP-CLI command is only executed after a positive confirmation is received from an authorized human operator through this out-of-band channel.

**v1/deleteUser.yaml**

YAML

\# MCP Tool Schema \- Version 1.0.0  
mcp\_version: '1.0'  
tool\_name: deleteUser  
description: "DANGER: Permanently deletes a WordPress user and optionally reassigns their posts to another user. REQUIRES HUMAN APPROVAL."  
parameters:  
  type: object  
  properties:  
    user\_id:  
      type: integer  
      description: "The ID of the user to delete."  
    reassign\_to\_user\_id:  
      type: integer  
      description: "Optional. The ID of the user to whom the deleted user's posts should be reassigned."  
    justification:  
      type: string  
      description: "A mandatory justification for this destructive action, which will be presented to the human approver."  
  required: \['user\_id', 'justification'\]  
\# Underlying Action: Initiates a human-in-the-loop approval workflow. If approved, executes 'wp user delete \<user\_id\> \--reassign=\<reassign\_to\_user\_id\>'.  
\# Associated IAM Role: roles/wordpressActuator.destructiveOperator

### **P4 \- Failure-Informed Scenario: What-Not-to-Build Post-Mortem**

To proactively identify and mitigate the most severe risks, this section presents a "pre-mortem" analysis. It is framed as a post-incident report for a catastrophic failure, allowing for the derivation of critical design lessons by working backward from a worst-case scenario.

**Incident Report: \#2025-042 \- Uncontrolled Cost Spike & Unauthorized User Deletion**

50-Word Summary:  
At 02:00 UTC, a flawed AI patch-agent, attempting to remediate a vulnerability, entered an infinite loop calling the updateSinglePlugin tool for a non-existent plugin. Each call spun up a new Cloud Run container, exhausting instance quotas and causing a massive cost overrun. A parallel command injection attack, enabled by a severe IAM misconfiguration, resulted in the deletion of a privileged user account.  
**Causal Graph & Analysis (≤ 650 words):**

The investigation identified three distinct but compounding root causes that led to this multi-faceted failure.

1. **Root Cause 1: Catastrophic IAM Misconfiguration.** The investigation revealed that the service account associated with the pluginUpdater actuator (sa-wp-actuator-tier2@...) had been granted the primitive roles/editor role at the project level. This was a manual error made during a testing phase that was never corrected. This single misconfiguration represented the **largest latent blast radius** in the system. It completely nullified the entire IAM segmentation strategy, rendering the principle of least privilege moot.10 Instead of having only the permission to trigger a Cloud Build job, the service account had wide-ranging permissions to modify and delete almost any resource in the project, including Cloud SQL users and data.  
2. **Root Cause 2: Failure of Intention-Typing Implementation.** The actuator's code for the updateSinglePlugin tool contained a critical implementation flaw. It used an unsafe shell execution method to construct the WP-CLI command. A malicious actor (or, in this case, a sufficiently "creative" and confused LLM) was able to craft a malicious plugin name parameter: bad-plugin; wp user delete 1 \--reassign=2. Because the input was not sanitized and was passed directly to a shell, the semicolon was interpreted as a command separator, leading to the execution of the unauthorized wp user delete command. The IAM misconfiguration (Root Cause 1\) meant this command was permitted to succeed. This failure highlights how **intention-typing shifted the locus of risk**. While the MCP schema correctly prevented the agent from *directly* calling a deleteUser tool, the risk of command injection moved from the agent's prompt to the actuator's internal code. The security of the system became dependent on the implementation quality of the tool handler.  
3. **Root Cause 3: Absence of Friction and Rate Limiting.** The AI agent was permitted to invoke the updateSinglePlugin tool without any velocity checks or human oversight. When its logic failed and it entered a loop trying to update a non-existent plugin, the system dutifully spun up a new Cloud Run container for each attempt. This led to a classic Denial-of-Wallet attack, rapidly scaling to the configured maximum number of instances and incurring significant costs. There was no "positive friction" to slow down or halt this anomalous, high-frequency behavior.

**Lessons Learned / What Not to Build:**

* **Never Use Primitive Roles in Production:** The use of owner, editor, or viewer for service accounts is the cardinal sin of GCP IAM security. All service accounts MUST be granted the most limited set of predefined or custom roles necessary for their function.10 This policy must be enforced via automated checks in the CI/CD pipeline.  
* **Treat All Agent Input as Untrusted:** The boundary between the agent and the actuator is a security boundary. All parameters received in an MCP tool call must be treated as hostile user input. They must be rigorously validated against expected formats and sanitized to prevent command injection before being used to construct downstream commands.  
* **Enforce Positive Friction and Velocity Checks:** The **minimal positive-friction checkpoint** that would have prevented the user deletion is a mandatory, out-of-band human approval workflow for any tool mapped to a Tier 3 (destructive) IAM role. For update-related tools, a simple rate limit (e.g., maximum of five update attempts per site per hour) and logic to detect and block repetitive calls with identical parameters would have immediately mitigated the cost spike and signaled the anomalous agent behavior.

## **Part IV: Synthesis, Evaluation & Future Trajectory**

This final part synthesizes the findings from the multi-lens analysis, provides a conclusive evaluation of the system's viability against its design goals, and charts a course for future experimentation and enhancement.

### **P5 (Part 2\) & P7 \- Final Policy & Scorecard**

This section presents the final, auditable artifacts of the design process: the complete IAM policy matrix that enforces least privilege, and a scorecard that rates the system's performance on its key objectives.

#### **IAM Least-Privilege Matrix**

The following matrix represents the final, production-ready IAM policy bindings for the actuator system. It is the concrete implementation of the principle of least privilege and should be managed as code within the system's Git repository.

| Service Account Principal | Role Granted | Scope | Justification |
| :---- | :---- | :---- | :---- |
| sa-wp-actuator-tier1@... | roles/wordpressActuator.vulnerabilityScanner | Project | For read-only actions like vulnerability scanning. Role contains run.invoke and cloudsql.client. |
| sa-wp-actuator-tier2@... | roles/wordpressActuator.pluginUpdater | Project | For safe updates. Role contains run.invoke, cloudsql.client, cloudbuild.builds.create. |
| sa-wp-actuator-tier2@... | roles/storage.objectAdmin | GCS Bucket: gs://wp-media-bucket-prod | Allows the update process to write plugin/theme assets to the media bucket. |
| sa-wp-actuator-tier3@... | roles/wordpressActuator.destructiveOperator | Project | For destructive actions. Role contains run.invoke, cloudsql.client, and permissions for the HITL notification system (e.g., chat.messages.create). |
| human-operator-group@... | roles/iap.httpsResourceAccessor | IAP-secured Web Service | Grants human operators access to the actuator's endpoint via IAP. |
| ai-agent-group@... | roles/iap.httpsResourceAccessor | IAP-secured Web Service | Grants AI agent service accounts access to the actuator's endpoint via IAP. |

#### **Actuator Scorecard**

This scorecard provides a final evaluation of the architecture, rating its success on a scale of 0 (Fails to meet objective) to 5 (Exceeds objective) for each of the core design axes.

| Axis | Score (0-5) | Justification |  |
| :---- | :---- | :---- | :---- |
| **Trust & Auditability** | **5** | The combination of IAP authentication logs, structured application logs with trace IDs, granular IAM policies managed as code, and an immutable GitOps workflow provides an exceptionally strong, transparent, and auditable trail of every action taken. |  |
| **Cost-Effectiveness** | **4** | The pay-per-use model is highly cost-effective for the intended sporadic administrative workloads.5 The score is not perfect due to the fixed cost of the required Cloud SQL instance 13 and the potential need to run with | \--min-instances=1 to mitigate latency, which adds a recurring monthly charge.15 |
| **Blast-Radius Control** | **5** | This is the system's strongest attribute. The fusion of ephemeral containers, which eliminate persistence, and granular IAM segmentation, which limits capability, reduces the potential blast radius of a compromise to near-zero for non-destructive tools. |  |
| **Latency** | **3** | Cold starts remain a tangible performance consideration.14 While manageable for backend tasks and mitigatable with configuration changes, the inherent latency is a clear trade-off compared to an always-on VM, preventing a higher score. |  |

#### **Next Experiments**

1. **Dynamic, Time-Bound Service Accounts:** Investigate using the IAM Credentials API to dynamically generate short-lived OAuth 2.0 access tokens for service accounts. This could enable a model where a unique, single-use token with permissions valid for only 60 seconds is created for each destructive action, further shrinking the window of opportunity for an attacker.  
2. **WebAssembly (WASM) Based Actuator:** Explore compiling the WP-CLI PHP binary and the actuator logic to WebAssembly. Running this in a WASM runtime like Cloudflare Workers or a custom V8 isolate could drastically reduce cold-start times below the level achievable with Docker containers, potentially solving the latency issue without the cost of minimum instances.  
3. **Advanced Agent Guardrails:** Develop a "meta-agent" or a policy engine that sits in front of the actuator. This component would analyze the stream of MCP requests from the primary agent, using machine learning to detect anomalous patterns (e.g., unusual frequency of calls, out-of-character tool sequences, requests at odd hours) and flag them for human review before they are passed to the actuator.

### **P6 \- Reflexive Insight & Prompt Upgrades**

This final section provides a meta-audit of the design and analysis process itself, identifying key learnings and translating them into concrete improvements for the system's agentic interface.

The most critical realization from the multi-lens analysis was the deeply symbiotic relationship between the **Intention-Typing Lens** and the **IAM Segmentation Lens**. Initially conceived as two separate layers of security, the analysis revealed they are an inseparable pair. A weak MCP schema (e.g., a generic execute tool) can be partially mitigated by a strong IAM policy, and a weak IAM policy (e.g., overly broad permissions) can be partially contained by a restrictive MCP schema. However, the system is only truly secure when both are strong and designed in concert. The IAM policy must be a direct, faithful implementation of the intent defined in the MCP tool schema.

Furthermore, the **Cost-to-Defence Ratio Lens** forced a pragmatic re-evaluation of the "pure serverless" ideal. The decision to potentially use \--min-instances=1 is not merely a technical configuration; it is a business decision that explicitly trades operational expenditure for improved user experience and performance. This highlights the necessity of aligning architectural choices with business requirements and budget constraints.

These learnings directly inform the following proposed upgrades to the agent's prompts and the system's MCP schemas.

#### **Prompt & Schema Upgrades (v2)**

1. **Prompt Upgrade (Contextual Impact):**  
   * **v1 Prompt:** "Update the Akismet plugin."  
   * **v2 Prompt:** "Propose a call to the updateSinglePlugin tool for the 'akismet' plugin. Be aware that a successful invocation of this tool will trigger a new, immutable production deployment via the CI/CD pipeline and will replace the currently running version of the application."  
   * This revised prompt provides the AI agent with critical context about the *consequences* of its actions, enabling more sophisticated reasoning and decision-making.  
2. Schema Upgrade (updateSinglePlugin v2 \- Loop Prevention):  
   The failure post-mortem identified the risk of a looping agent causing a cost spike. To mitigate this, the tool schema can be upgraded to require a justification, which can be used by the actuator for semantic de-duplication.  
   **v2/updateSinglePlugin.yaml**  
   YAML  
   \# MCP Tool Schema \- Version 2.0.0  
   mcp\_version: '1.0'  
   tool\_name: updateSinglePlugin  
   description: "Initiates a safe update for a single specified plugin via the CI/CD pipeline."  
   parameters:  
     type: object  
     properties:  
       name:  
         type: string  
         description: "The slug of the plugin to update."  
       justification:  
         type: string  
         description: "Mandatory reason for the update (e.g., 'Patching CVE-2025-12345')."  
     required: \['name', 'justification'\]

   The actuator can now log this justification and implement logic to reject a request if it receives an identical call (same name and justification) within a short time window, effectively breaking nonsensical loops.  
3. New Tool (requestDestructiveAction v1 \- Centralized Friction):  
   Instead of having separate tools for each destructive action (e.g., deleteUser, resetDatabase), a more robust pattern is to centralize the human approval gateway. A single tool is created whose only purpose is to initiate the HITL workflow.  
   **v1/requestDestructiveAction.yaml**  
   YAML  
   \# MCP Tool Schema \- Version 1.0.0  
   mcp\_version: '1.0'  
   tool\_name: requestDestructiveAction  
   description: "Requests human approval for a high-impact, destructive action. Does not execute the action directly."  
   parameters:  
     type: object  
     properties:  
       action\_name:  
         type: string  
         description: "The name of the destructive action to perform (e.g., 'deleteUser', 'resetDatabase')."  
       action\_params:  
         type: object  
         description: "A JSON object containing the parameters for the requested action."  
       justification:  
         type: string  
         description: "A mandatory, detailed justification for why this action is necessary."  
     required: \['action\_name', 'action\_params', 'justification'\]

   This design centralizes the positive friction mechanism, simplifies the agent's toolset for dangerous operations, and ensures that no destructive action can ever be performed without passing through a single, well-audited human approval gate.

#### **Works cited**

1. Pros And Cons Of Serverless App Hosting Vs VPS Hosting, accessed July 3, 2025, [https://blog.radwebhosting.com/pros-and-cons-of-serverless-app-hosting-vs-vps-hosting/](https://blog.radwebhosting.com/pros-and-cons-of-serverless-app-hosting-vs-vps-hosting/)  
2. WordPress on Google Cloud Pros and Cons | User Likes & Dislikes \- G2, accessed July 3, 2025, [https://www.g2.com/products/wordpress-on-google-cloud/reviews?qs=pros-and-cons](https://www.g2.com/products/wordpress-on-google-cloud/reviews?qs=pros-and-cons)  
3. For the security experts around here, are there core WordPress features that pose security risks? \- Reddit, accessed July 3, 2025, [https://www.reddit.com/r/Wordpress/comments/1hj1kil/for\_the\_security\_experts\_around\_here\_are\_there/](https://www.reddit.com/r/Wordpress/comments/1hj1kil/for_the_security_experts_around_here_are_there/)  
4. Which WP-CLI commands can be safely run with \--allow-root flag?, accessed July 3, 2025, [https://wordpress.stackexchange.com/questions/424412/which-wp-cli-commands-can-be-safely-run-with-allow-root-flag](https://wordpress.stackexchange.com/questions/424412/which-wp-cli-commands-can-be-safely-run-with-allow-root-flag)  
5. Costs for hosting Wordpress servers on GCP? : r/googlecloud \- Reddit, accessed July 3, 2025, [https://www.reddit.com/r/googlecloud/comments/191oell/costs\_for\_hosting\_wordpress\_servers\_on\_gcp/](https://www.reddit.com/r/googlecloud/comments/191oell/costs_for_hosting_wordpress_servers_on_gcp/)  
6. Specification \- Model Context Protocol, accessed July 3, 2025, [https://modelcontextprotocol.io/specification/2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18)  
7. Model Context Protocol (MCP) an overview \- Philschmid, accessed July 3, 2025, [https://www.philschmid.de/mcp-introduction](https://www.philschmid.de/mcp-introduction)  
8. Pros and Cons of Serverless Backend Development: Is It Right for Your Project?, accessed July 3, 2025, [https://www.scrumlaunch.com/blog/pros-and-cons-of-serverless-backend-development](https://www.scrumlaunch.com/blog/pros-and-cons-of-serverless-backend-development)  
9. Best practice rules for Google Cloud Platform | Trend Micro, accessed July 3, 2025, [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/)  
10. Use IAM securely | IAM Documentation | Google Cloud, accessed July 3, 2025, [https://cloud.google.com/iam/docs/using-iam-securely](https://cloud.google.com/iam/docs/using-iam-securely)  
11. Model Context Protocol (MCP): Understanding security risks and controls \- Red Hat, accessed July 3, 2025, [https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls)  
12. Specification \- Model Context Protocol, accessed July 3, 2025, [https://modelcontextprotocol.io/specification/2025-03-26](https://modelcontextprotocol.io/specification/2025-03-26)  
13. Running Wordpress website on Google Cloud Run — simple and ..., accessed July 3, 2025, [https://medium.com/@peterkracik/running-wordpress-website-on-google-cloud-run-simple-and-cheap-fa19b62a7417](https://medium.com/@peterkracik/running-wordpress-website-on-google-cloud-run-simple-and-cheap-fa19b62a7417)  
14. General development tips | Cloud Run Documentation \- Google Cloud, accessed July 3, 2025, [https://cloud.google.com/run/docs/tips/general](https://cloud.google.com/run/docs/tips/general)  
15. Cloud run: how to mitigate cold starts and how much that would cost? : r/googlecloud, accessed July 3, 2025, [https://www.reddit.com/r/googlecloud/comments/1ita39x/cloud\_run\_how\_to\_mitigate\_cold\_starts\_and\_how/](https://www.reddit.com/r/googlecloud/comments/1ita39x/cloud_run_how_to_mitigate_cold_starts_and_how/)  
16. Would you try a serverless version of Wordpress? \- Reddit, accessed July 3, 2025, [https://www.reddit.com/r/Wordpress/comments/13l3b56/would\_you\_try\_a\_serverless\_version\_of\_wordpress/](https://www.reddit.com/r/Wordpress/comments/13l3b56/would_you_try_a_serverless_version_of_wordpress/)  
17. Solved: Re: Secure website with Identity Aware Proxy ( iap... \- Google Cloud Community, accessed July 3, 2025, [https://www.googlecloudcommunity.com/gc/Infrastructure-Compute-Storage/Secure-website-with-Identity-Aware-Proxy-iap/m-p/609141](https://www.googlecloudcommunity.com/gc/Infrastructure-Compute-Storage/Secure-website-with-Identity-Aware-Proxy-iap/m-p/609141)  
18. Cloud Security Best Practices Center | Google Cloud, accessed July 3, 2025, [https://cloud.google.com/security/best-practices](https://cloud.google.com/security/best-practices)  
19. How to install a Wordpress site on Google Cloud Run | by Salvo Pappalardo \- Medium, accessed July 3, 2025, [https://medium.com/acadevmy/how-to-install-a-wordpress-site-on-google-cloud-run-828bdc0d0e96](https://medium.com/acadevmy/how-to-install-a-wordpress-site-on-google-cloud-run-828bdc0d0e96)  
20. 24 Google Cloud Platform (GCP) security best practices \- Sysdig, accessed July 3, 2025, [https://sysdig.com/learn-cloud-native/24-google-cloud-platform-gcp-security-best-practices/](https://sysdig.com/learn-cloud-native/24-google-cloud-platform-gcp-security-best-practices/)  
21. Functions best practices | Cloud Run Documentation, accessed July 3, 2025, [https://cloud.google.com/run/docs/tips/functions-best-practices](https://cloud.google.com/run/docs/tips/functions-best-practices)  
22. WordPress on Cloud Run slow with Cloud Storage : r/googlecloud \- Reddit, accessed July 3, 2025, [https://www.reddit.com/r/googlecloud/comments/1bjevge/wordpress\_on\_cloud\_run\_slow\_with\_cloud\_storage/](https://www.reddit.com/r/googlecloud/comments/1bjevge/wordpress_on_cloud_run_slow_with_cloud_storage/)  
23. Pros and Cons of Serverless Architectures \- Bejamas, accessed July 3, 2025, [https://bejamas.com/hub/guides/serverless-architectures](https://bejamas.com/hub/guides/serverless-architectures)