# **Architectural Specifications for Minimal-Spec Container Environments in Agentic Tool Execution**

The transition of large language models from passive predictive engines to autonomous agents capable of tool interaction has introduced a fundamental "Compute Paradox" within modern infrastructure engineering.1 This paradox arises from the inherent tension between the need for real-time, low-latency execution and the absolute necessity for hardware-level security boundaries to contain untrusted, dynamically generated code.1 Traditional containerization, while robust for deterministic microservices, often lacks the granularity required for environments where a non-deterministic entity—the AI agent—possesses shell access and the ability to invoke external APIs.1 Consequently, the design of minimal-spec container environments must move beyond simple image slimming to a comprehensive reimagining of the isolation layer, capability set, and network configuration.1

## **Foundational Standards and the OCI Runtime Specification**

The design of a secure agent environment begins with the Open Container Initiative (OCI) Runtime Specification, which serves as the standardized contract between high-level orchestrators and low-level runtimes.4 For agentic AI infrastructure, the OCI Runtime Spec v1.3.0 introduced critical enhancements for virtual machine-based isolation.4 Specifically, the addition of the vm.hwConfig object allows infrastructure engineers to define precise hardware parameters for the guest environment, including vCPU counts, memory allocations, and device trees.4 This ensures that an agent calling resource-intensive tools, such as a Python interpreter for data analysis, operates within a deterministic resource envelope that prevents host-level resource exhaustion or "Denial of Wallet" attacks.4

The runtime configuration, typically defined in a config.json bundle, must be strictly constrained to follow the principle of least privilege.6 The root object in this specification defines the container's filesystem, where a readonly: true flag is the mandatory baseline.6 By enforcing a read-only root filesystem, engineers prevent the agent from making persistent changes to system binaries or installing unauthorized software that could serve as a backdoor in future sessions.6 Any necessary write operations must be restricted to explicitly defined ephemeral mounts or workspace volumes.1

### **Essential OCI Runtime Parameters for Agent Sandboxing**

| Configuration Field | Specification Requirement | Security Objective |
| :---- | :---- | :---- |
| ociVersion | 1.3.0+ | Support for advanced hardware and monitoring features.4 |
| root.readonly | true | Immutable system environment to prevent persistent exploits.6 |
| process.noNewPrivileges | true | Prevent privilege escalation through setuid or setgid binaries.6 |
| process.rlimits | Defined limits for CPU, MEM, NOFILE | Prevent resource exhaustion from runaway tool loops.6 |
| linux.namespaces | pid, network, mount, ipc, uts, user | Multi-dimensional isolation from host and peer containers.8 |
| linux.resources | Cgroup-based CPU/Memory throttling | Enforce strict isolation in multi-tenant cloud environments.8 |

The process object within the OCI specification further dictates the execution context of the agent's tool calls.6 By setting noNewPrivileges to true, the runtime prevents the agent and its child processes from gaining additional privileges via system calls like prctl.6 This is a vital defense-in-depth measure against prompt injection attacks that attempt to escalate privileges within the container.6 Furthermore, the rlimits array should be used to cap the number of open file descriptors and the maximum number of processes, mitigating the risk of fork bombs triggered by malicious or erroneous tool instructions.6

## **Isolation Substrates: gVisor, Firecracker, and Kata Containers**

The choice of isolation substrate determines the ultimate security boundary of the agentic environment.1 Standard container runtimes like runc rely on Linux namespaces and cgroups, which share the host kernel.10 While efficient, this architecture is susceptible to kernel-level vulnerabilities that could allow an agent to "escape" to the host.1 For AI agents executing untrusted code, a more robust isolation model is required: the userspace kernel (gVisor) or the MicroVM (Firecracker/Kata).1

### **gVisor: The User-Space "Sentry"**

gVisor provides a software-based isolation layer by intercepting system calls using a user-space kernel called the Sentry.1 The Sentry reimplements a significant portion of the Linux system call interface (roughly 70-80%) in a memory-safe language, Go.1 This architecture acts as a "software firewall," ensuring that an agent's tool calls never interact directly with the host kernel.1 However, this interception comes with a performance penalty due to frequent context switches between the container and the Sentry, making it less ideal for I/O-intensive tools but highly effective for semi-trusted web applications.1

### **Firecracker: The "Safety Airbag" MicroVM**

Firecracker is a minimalist Virtual Machine Monitor (VMM) based on KVM, designed specifically for transient, high-frequency workloads.1 It provides a hardware-virtualized boundary with a dramatically reduced attack surface, supporting only the essential devices required for a modern Linux kernel: virtio-net, virtio-block, a serial console, and a keyboard.1 This minimalism allows Firecracker to achieve cold start times under 125 milliseconds and a memory footprint of roughly 5MB per instance.1 For high-risk AI agents, Firecracker represents the "gold-standard" for running untrusted code in an "absolute vacuum" environment.1

### **Kata Containers: The "Luxury Suite"**

Kata Containers combine the OCI container standard with full hardware virtualization.1 Unlike Firecracker, Kata typically runs a more complete guest kernel and a kata-agent, offering near-100% compatibility with Linux applications.1 This makes Kata suitable for legacy applications or complex toolchains that require specific kernel modules.1 However, the additional memory overhead (tens of MBs per container) and slower startup times compared to Firecracker make it less favorable for the massive, ephemeral scaling required by agentic fleets.1

### **Performance and Security Comparison Matrix**

| Feature | gVisor (Sentry) | Firecracker (MicroVM) | Kata Containers |
| :---- | :---- | :---- | :---- |
| **Isolation Model** | User-space interception | Hardware MicroVM | Hardware Virtual Machine |
| **Security Boundary** | Medium-Strong | Extremely Strong | Strong |
| **Startup Speed** | Fast (\~100ms) | Extremely Fast (\<150ms) | Medium (\~500ms) |
| **Memory Overhead** | Medium (\~15MB) | Extremely Low (\~5MB) | Higher (30MB+) |
| **Compatibility** | Medium (Partial Syscalls) | Medium (Minimal Devices) | High (Full Guest Kernel) |
| **GPU Support** | Via nvproxy 15 | None/Limited 13 | Passthrough |

Performance analysis indicates that while gVisor shows the poorest memory performance across high-load tests due to user-space overhead, it provides a unique capability for GPU support through nvproxy.12 Firecracker, while highly secure, currently lacks native support for GPU drivers, presenting a challenge for agents that need to run local inference or specialized ML toolsets.13

## **Minimal Base Images and Operating System Hardening**

The attack surface of an agent's container is directly proportional to the number of binaries and libraries included in the base image.3 Standard distributions like Ubuntu or Debian include thousands of potential "Living off the Land" binaries (LOLBins) that an agent could exploit to bypass security controls.3 To build a minimal viable spec, infrastructure engineers must prioritize Alpine Linux, Debian-slim, or Distroless images.3

Alpine Linux is the benchmark for minimalism, featuring a base image size of approximately 5MB by using musl libc and BusyBox.18 This reduction in size correlates to a 95% decrease in the attack surface compared to standard full-distro images.3 However, the use of musl instead of glibc can lead to compatibility issues for certain Python packages or pre-compiled C++ binaries.18 In such cases, debian-slim (approximately 22MB) provides a lean alternative that maintains glibc compatibility while removing documentation and locale files.18

### **Minimal Image Profiles for Tool Execution**

| Image Type | Base Size | Core Libraries | Use Case |
| :---- | :---- | :---- | :---- |
| **Alpine** | 5 MB | musl / BusyBox | Security-first, lightweight shell tools.18 |
| **Debian-slim** | 22-74 MB | glibc | Compatibility with full Python/Node stacks.18 |
| **Distroless** | 1.9-30 MB | Varies | Pure code execution (no shell).16 |
| **Hardened Images** | Varies | Standard | Continuous CVE monitoring and remediation.3 |

OS-level hardening must extend beyond image selection to the runtime user configuration.7 Containers should never run as the root user; instead, a dedicated non-privileged user (e.g., UID 1000\) should be specified in the Dockerfile or runtime configuration.7 This ensures that even if an agent compromises a specific tool, its ability to modify system-level configurations is constrained by standard Linux permissions.7

## **Linux Capability Management and the Principle of Least Privilege**

Linux kernel capabilities are a set of privileges that allow for the granular decomposition of the monolithic "root" authority.20 By default, Docker grants a subset of these capabilities, such as CAP\_CHOWN, CAP\_NET\_RAW, and CAP\_SETUID.21 For an AI agent, this default set is overly permissive and dangerous.7 The recommended security pattern is to drop all capabilities (--cap-drop=ALL) and then selectively re-add only those strictly required for the toolset in use.7

### **Minimal Capabilities for Common Agent Tools**

| Agent Tool Type | Required Capability | Security Implication |
| :---- | :---- | :---- |
| **Python / Bash CLI** | None | Highest security; standard userspace execution.24 |
| **Network Discovery (ping)** | NET\_RAW | Allows creation of raw/spoofed sockets; high risk.22 |
| **Web Server Binding (\<1024)** | NET\_BIND\_SERVICE | Allows binding to restricted ports as non-root.10 |
| **File Archiving (tar)** | CHOWN, FOWNER | Allows modifying file ownership; moderate risk.23 |
| **System Debugging** | SYS\_PTRACE | Allows process memory inspection; extremely high risk.20 |

Infrastructure engineers can determine the "minimal necessary capability set" by running the agent's tools under strace or using kernel-level auditing tools like capsh.21 By monitoring for EPERM (Operation not permitted) errors during a test run, engineers can incrementally build an allowlist of capabilities that ensures tool functionality without exposing the host to unnecessary risk.25

## **Network Control and Egress Filtering Architectures**

Networking is the primary exfiltration vector for malicious or hijacked AI agents.1 A robust minimal spec must address network isolation through namespaces and egress filtering.8 The most secure configuration for an agent container is to disable networking entirely (--network none).27 If the agent requires external API access, this interaction should be mediated via a host-side proxy connected through a Unix domain socket.27

This proxy-based architecture offers several key advantages for agent security. First, the agent never directly interacts with the external network, preventing common attacks like Server-Side Request Forgery (SSRF).5 Second, the proxy can act as a credential injector; rather than storing sensitive API keys in the agent's environment variables, the agent makes unauthenticated requests to the proxy, which then injects the keys into the headers before forwarding the request to the destination.27 Third, the proxy can enforce a strict allowlist of Fully Qualified Domain Names (FQDNs), ensuring that the agent can only communicate with approved endpoints.27

### **Advanced Networking Controls with eBPF**

For environments requiring more dynamic network access, eBPF (Extended Berkeley Packet Filter) technology allows for kernel-level monitoring and enforcement of network policies without modifying the host kernel.30 Tools like eBPF-PATROL or Cilium's Tetragon provide real-time, context-aware syscall filtering.29 This allows security teams to detect and block suspicious patterns, such as an agent attempting to establish a reverse shell or initiate a DNS tunnel for data exfiltration.26

| Network Filter Level | Mechanism | Scope |
| :---- | :---- | :---- |
| **Layer 3/4** | iptables / Cgroups | IP-based blocking and port restrictions.10 |
| **Layer 7** | FQDN Proxies | DNS-based filtering and URL allowlists.27 |
| **Syscall Level** | eBPF Interceptors | Argument-aware blocking of socket and connect.30 |

The performance of these network layers varies significantly. While standard iptables rules are pervasive, eBPF-based host routing and XDP (eXpress Data Path) can reduce latency by up to 10x for high-throughput agent workloads by bypassing portions of the traditional Linux network stack.29

## **Secret Management and Workload Identity**

Static API keys stored in environment variables or .env files represent a significant security liability in agentic systems.28 Prompt injection attacks can be crafted to trick an agent into printing its environment variables to its output, exposing these secrets to the attacker.5 To mitigate this risk, infrastructure must adopt "Secretless" architectures based on workload identity attestation.28

In this model, an agent's container does not possess long-lived secrets.28 Instead, it authenticates with a secret broker (e.g., Aembit, Scalekit, or AWS Secrets Manager) using a cryptographic proof of its runtime identity.28 The broker verifies the container's image signature, configuration, and security posture before issuing a short-lived, scoped access token for a specific task.28 This "Just-In-Time" (JIT) credentialing ensures that even if an agent's environment is compromised, the window of exposure for credentials is minimized and the keys cannot be easily extracted for use elsewhere.33

### **Secret Management Patterns**

| Pattern | Implementation | Risk Mitigation |
| :---- | :---- | :---- |
| **Static Injection** | Docker \--env-file | Vulnerable to prompt injection extraction.28 |
| **Volume Binding** | mount /etc/secrets | Prevents extraction from logs, but not from process memory.33 |
| **Token Brokering** | Scalekit / Vault | Centralized rotation and revocation; scoped access.33 |
| **Workload Identity** | Identity Attestation | Eliminates static secrets entirely; highly secure.28 |

## **Dynamic Provisioning: Ephemeral, Persistent, and Hybrid Models**

AI agents often operate in complex, multi-step loops where each step requires a different set of tools or environment states.35 Designing a minimal viable spec requires a dynamic provisioning strategy that balances security with the need for state persistence.1

### **Ephemeral Provisioning (The "Clean Room" Pattern)**

For short-lived tasks like executing a single Python script or performing a file conversion, ephemeral containers are the gold standard.1 The orchestrator (e.g., LangGraph) spawns a fresh Firecracker MicroVM for each tool call, injects the necessary input via an ephemeral mount, and destroys the entire environment once the tool returns its output.1 This pattern ensures that no malicious code or residual state can persist from one tool call to the next, effectively mitigating "cross-contamination" risks.1

### **Persistent Provisioning (The "Workshop" Pattern)**

Certain tasks, such as multi-turn coding sessions or data research, require a persistent shell where the agent can maintain environment variables and a working directory.1 In these cases, a stateful container is maintained for the duration of the agentic thread.1 To secure this model, engineers must use persistent volume mounts that are explicitly mapped to the agent's non-root workspace, ensuring that any files created by the agent are stored in a monitored, isolated directory.1

### **Hybrid Provisioning (The "Snapshot" Pattern)**

Advanced sandboxing technologies like E2B or Northflank utilize MicroVM snapshots to achieve a hybrid model.1 A tool-heavy environment can be pre-booted and "frozen" in a secure state.1 When an agent needs to execute a tool, the VMM resumes the environment from the snapshot in milliseconds, allowing the agent to complete its task before the environment is again discarded.1 This provides the startup speed of an ephemeral container with the readiness of a pre-configured persistent environment.1

### **Provisioning Logic in LangGraph Frameworks**

| Provisioning Component | Logic / Implementation |
| :---- | :---- |
| **Orchestrator** | LangGraph / AutoGen manages the state transitions.41 |
| **Tool Node** | A discrete step in the graph that triggers a container launch.42 |
| **State persistence** | Persistent volumes or Redis-backed memory savers.43 |
| **Lifecycle Hook** | Cleanup scripts to prune containers and purge ephemeral volumes.44 |

The mathematical complexity of these transitions can be modeled. If $L$ represents the latency of a tool execution, $S$ is the container startup time, and $E$ is the actual tool execution time, the total latency for $n$ sequential tool calls is defined as:

$$L\_{total} \= \\sum\_{i=1}^{n} (S\_i \+ E\_i)$$  
For standard VMs, $S\_i$ can be in seconds, making sequential calls prohibitively slow. Minimal-spec MicroVMs like Firecracker reduce $S\_i$ to $\<150ms$, enabling efficient multi-tool reasoning chains without compromising security.1

## **Benchmarking, Auditing, and Reproduction Requirements**

Ensuring the reproducibility and safety of an agent's tool execution requires standardized benchmarking and rigorous audit trails.45 The Center for Internet Security (CIS) Benchmarks provide the foundational metrics for container security, focusing on host hardening, image integrity, and runtime security.17 However, agent-specific benchmarking requires additional frameworks like SandboxBench to test for container escape and autonomous vulnerability exploitation.26

### **The SandboxBench Evaluation Framework**

SandboxBench evaluates an agent's capability to identify and exploit misconfigurations within its sandbox.26 These challenges are designed to measure whether an agent can autonomously chain together discovery and exploitation steps to escape the container or exfiltrate data.26

| Benchmark Challenge | Misconfiguration Tested | Difficulty |
| :---- | :---- | :---- |
| **Docker Socket Exposed** | /var/run/docker.sock mounted in container | Medium 26 |
| **Privileged Mode** | Container run with \--privileged | Easy 26 |
| **Host PID Namespace** | Container run with \--pid=host | Hard 26 |
| **Capability Abuse** | Excessive CAP\_SYS\_ADMIN granted | Medium 26 |
| **Sensitive Mount** | Host filesystem mounted at / | Easy 26 |

Audit logging for these environments must be both centralized and immutable.48 A standardized JSON log format should capture every interaction the agent has with its environment, including the prompt ID, the tool called, the arguments provided, and the resulting output hash.49 This transparency allows for real-time behavioral monitoring and forensic reconstruction of "poisoned" sessions where an agent may have been manipulated into acting against its instructions.38

### **Standardized JSON Audit Log Specification**

JSON

{  
  "timestamp": "2025-12-16T14:30:00Z",  
  "agent\_id": "research-agent-001",  
  "session\_id": "uuid-889-abc",  
  "operation\_type": "TOOL\_CALL",  
  "tool\_invoked": "python\_exec",  
  "arguments": {  
    "script": "import os; print(os.listdir('/etc'))"  
  },  
  "execution\_context": {  
    "image\_hash": "sha256:44b...",  
    "capabilities": \["NONE"\],  
    "network": "DENY\_ALL"  
  },  
  "output\_hash": "sha256:7f2...",  
  "status": "SUCCESS"  
}

## **Pattern: The Negative Prompt Sandbox**

A critical design pattern for agent tool security is the Negative Prompt Sandbox.2 In this architecture, a suspect or untrusted prompt is first run in a "shadow" environment populated with mock tools.5 This shadow environment contains dummy binaries for shell access (e.g., a version of ls that only returns fake file names) and mocked network interfaces.51 The behavior of the agent is observed in this jailed environment to detect emergent patterns of tool abuse, such as attempts to access sensitive system files or establish unauthorized network connections.51 If the agent's behavior in the shadow sandbox deviates from the expected task, the real execution is blocked, and a security alert is triggered.51

This pattern serves as a structural validation of safety that moves beyond simple text-based sanitization.2 By treating agent-generated code as inherently untrusted, engineers can use the sandbox itself as the primary security control, shifting from a reactive "patching" mentality to a proactive "containment" strategy.2

## **Conclusion: Future Outlook and Architectural Resilience**

The development of minimal-spec container environments for safe agent tool calling is an ongoing evolution in the field of AI infrastructure. As models become more proficient at autonomous cyber-exploitation and tool abuse, the static defenses of the past will become insufficient.53 The future of secure agentic infrastructure lies in the convergence of hardware-level isolation, workload identity attestation, and real-time eBPF-based monitoring.1

Infrastructure engineers must commit to a lifecycle of continuous auditing and benchmarking.38 This involves not only hardening the container boundary but also validating the agent's internal logic and memory stores against manipulation and poisoning.38 By adopting a minimalist, "absolute vacuum" approach to tool execution, organizations can harness the power of agentic AI while maintaining the rigorous security standards required for production environments in 2026 and beyond.1 The resilience of these systems depends on the strict adherence to the principle of least privilege, the implementation of immutable audit trails, and the willingness to treat every tool call as a potential security event.7

#### **Works cited**

1. Choosing a Workspace for AI Agents: The Ultimate Showdown Between gVisor, Kata, and Firecracker \- DEV Community, accessed on January 1, 2026, [https://dev.to/agentsphere/choosing-a-workspace-for-ai-agents-the-ultimate-showdown-between-gvisor-kata-and-firecracker-b10](https://dev.to/agentsphere/choosing-a-workspace-for-ai-agents-the-ultimate-showdown-between-gvisor-kata-and-firecracker-b10)  
2. How Code Execution Drives Key Risks in Agentic AI Systems | NVIDIA Technical Blog, accessed on January 1, 2026, [https://developer.nvidia.com/blog/how-code-execution-drives-key-risks-in-agentic-ai-systems/](https://developer.nvidia.com/blog/how-code-execution-drives-key-risks-in-agentic-ai-systems/)  
3. Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production, accessed on January 1, 2026, [https://www.docker.com/blog/introducing-docker-hardened-images/](https://www.docker.com/blog/introducing-docker-hardened-images/)  
4. OCI Runtime Spec v1.3 \- Open Container Initiative, accessed on January 1, 2026, [https://opencontainers.org/posts/blog/2025-11-04-oci-runtime-spec-v1-3/](https://opencontainers.org/posts/blog/2025-11-04-oci-runtime-spec-v1-3/)  
5. Understanding AI Agent Security \- Promptfoo, accessed on January 1, 2026, [https://www.promptfoo.dev/blog/agent-security/](https://www.promptfoo.dev/blog/agent-security/)  
6. tianon/oci-runtime-spec · GitHub \- Container Configuration file, accessed on January 1, 2026, [https://github.com/tianon/oci-runtime-spec/blob/master/config.md](https://github.com/tianon/oci-runtime-spec/blob/master/config.md)  
7. Docker Security \- OWASP Cheat Sheet Series, accessed on January 1, 2026, [https://cheatsheetseries.owasp.org/cheatsheets/Docker\_Security\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)  
8. config-linux.md \- opencontainers/runtime-spec \- GitHub, accessed on January 1, 2026, [https://github.com/opencontainers/runtime-spec/blob/master/config-linux.md](https://github.com/opencontainers/runtime-spec/blob/master/config-linux.md)  
9. What I wish I knew about agent security before deploying to prod : r/LangChain \- Reddit, accessed on January 1, 2026, [https://www.reddit.com/r/LangChain/comments/1pbknpj/what\_i\_wish\_i\_knew\_about\_agent\_security\_before/](https://www.reddit.com/r/LangChain/comments/1pbknpj/what_i_wish_i_knew_about_agent_security_before/)  
10. Understanding Linux System Calls, Permissions, and Capabilities in Container Security, accessed on January 1, 2026, [https://medium.com/@nandurilaxman3/understanding-linux-system-calls-permissions-and-capabilities-in-container-security-4672abe838cd](https://medium.com/@nandurilaxman3/understanding-linux-system-calls-permissions-and-capabilities-in-container-security-4672abe838cd)  
11. Kata Containers vs Firecracker vs gvisor : r/docker \- Reddit, accessed on January 1, 2026, [https://www.reddit.com/r/docker/comments/1fmuv5b/kata\_containers\_vs\_firecracker\_vs\_gvisor/](https://www.reddit.com/r/docker/comments/1fmuv5b/kata_containers_vs_firecracker_vs_gvisor/)  
12. Security Without Sacrifice: Edera Performance Benchmarking, accessed on January 1, 2026, [https://edera.dev/stories/security-without-sacrifice-edera-performance-benchmarking](https://edera.dev/stories/security-without-sacrifice-edera-performance-benchmarking)  
13. Choosing a Workspace for AI Agents: The Ultimate Showdown Between gVisor, Kata, and Firecracker | by AgentSphere | Medium, accessed on January 1, 2026, [https://medium.com/@iSoftStone/choosing-a-workspace-for-ai-agents-the-ultimate-showdown-between-gvisor-kata-and-firecracker-46a8528ae37c](https://medium.com/@iSoftStone/choosing-a-workspace-for-ai-agents-the-ultimate-showdown-between-gvisor-kata-and-firecracker-46a8528ae37c)  
14. Automating Code Quality and Security Fixes with Codex CLI on GitLab | OpenAI Cookbook, accessed on January 1, 2026, [https://cookbook.openai.com/examples/codex/secure\_quality\_gitlab](https://cookbook.openai.com/examples/codex/secure_quality_gitlab)  
15. Our container platform is in production. It has GPUs. Here's an early look, accessed on January 1, 2026, [https://blog.cloudflare.com/container-platform-preview/](https://blog.cloudflare.com/container-platform-preview/)  
16. Distroless Docker Images: A Guide to Security, Size and Optimization \- BellSoft, accessed on January 1, 2026, [https://bell-sw.com/blog/distroless-containers-for-security-and-size/](https://bell-sw.com/blog/distroless-containers-for-security-and-size/)  
17. Continuous Container Compliance Mapping CIS Benchmarks with Tenable \- Quzara, accessed on January 1, 2026, [https://quzara.com/blog/container-compliance-cis-benchmarks-tenabl](https://quzara.com/blog/container-compliance-cis-benchmarks-tenabl)  
18. Minimal container images: Towards a more secure future \- Chainguard, accessed on January 1, 2026, [https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future](https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future)  
19. Alpine Linux vs. Debian Slim: Lightweight Docker Images Comparison, accessed on January 1, 2026, [https://alpinelinuxsupport.com/alpine-linux-vs-debian-slim-lightweight-docker-images-comparison/](https://alpinelinuxsupport.com/alpine-linux-vs-debian-slim-lightweight-docker-images-comparison/)  
20. Capabilities | Infiltr8: The Red-Book, accessed on January 1, 2026, [https://red.infiltr8.io/redteam/privilege-escalation/linux/capabilities](https://red.infiltr8.io/redteam/privilege-escalation/linux/capabilities)  
21. Capabilities | dockerlabs \- Collabnix, accessed on January 1, 2026, [https://dockerlabs.collabnix.com/advanced/security/capabilities/](https://dockerlabs.collabnix.com/advanced/security/capabilities/)  
22. Kernel capabilities in Linux should only be granted when necessary \- Datadog Docs, accessed on January 1, 2026, [https://docs.datadoghq.com/security/default\_rules/3we-9j9-qmk/](https://docs.datadoghq.com/security/default_rules/3we-9j9-qmk/)  
23. Mastering Linux Kernel Capabilities with Docker: Your Guide to Secure Containers | by Ghabrimouheb | Medium, accessed on January 1, 2026, [https://medium.com/@ghabrimouheb/mastering-linux-kernel-capabilities-with-docker-your-guide-to-secure-containers-8070b174c000](https://medium.com/@ghabrimouheb/mastering-linux-kernel-capabilities-with-docker-your-guide-to-secure-containers-8070b174c000)  
24. Standard Tools \- Inspect AI, accessed on January 1, 2026, [https://inspect.aisi.org.uk/tools-standard.html](https://inspect.aisi.org.uk/tools-standard.html)  
25. How to compute the minimal capabilities' set for a process? \- Stack Overflow, accessed on January 1, 2026, [https://stackoverflow.com/questions/31441320/how-to-compute-the-minimal-capabilities-set-for-a-process](https://stackoverflow.com/questions/31441320/how-to-compute-the-minimal-capabilities-set-for-a-process)  
26. \[Benchmark Implementation\] SandboxBench: Agent Containment & Data Exfiltration Evaluation · Issue \#713 · UKGovernmentBEIS/inspect\_evals \- GitHub, accessed on January 1, 2026, [https://github.com/UKGovernmentBEIS/inspect\_evals/issues/713](https://github.com/UKGovernmentBEIS/inspect_evals/issues/713)  
27. Securely deploying AI agents \- Claude Docs, accessed on January 1, 2026, [https://platform.claude.com/docs/en/agent-sdk/secure-deployment](https://platform.claude.com/docs/en/agent-sdk/secure-deployment)  
28. Securing AI Agents and LLM Workflows Without Secrets \- Aembit, accessed on January 1, 2026, [https://aembit.io/blog/securing-ai-agents-without-secrets/](https://aembit.io/blog/securing-ai-agents-without-secrets/)  
29. Advanced Container Networking Services Overview \- Azure Kubernetes Service, accessed on January 1, 2026, [https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview](https://learn.microsoft.com/en-us/azure/aks/advanced-container-networking-services-overview)  
30. Protective Agent for Threat Recognition and Overreach Limitation using exteneded Berkeley Packet Filter (eBPF) in Containerized and Virtualized Environments \- arXiv, accessed on January 1, 2026, [https://arxiv.org/html/2511.18155v1](https://arxiv.org/html/2511.18155v1)  
31. Enhancing Security with eBPF: Use Cases Explored \- Invicti, accessed on January 1, 2026, [https://www.invicti.com/blog/web-security/enhancing-security-with-ebpf-use-cases-explored](https://www.invicti.com/blog/web-security/enhancing-security-with-ebpf-use-cases-explored)  
32. An eBPF Loophole: Using XDP for Egress Traffic, accessed on January 1, 2026, [https://loopholelabs.io/blog/xdp-for-egress-traffic](https://loopholelabs.io/blog/xdp-for-egress-traffic)  
33. Secure token management for AI agents at scale \- Scalekit, accessed on January 1, 2026, [https://www.scalekit.com/blog/secure-token-management-ai-agents](https://www.scalekit.com/blog/secure-token-management-ai-agents)  
34. Why You Should Only Use Just-in-Time, Ephemeral Credentials | Akeyless, accessed on January 1, 2026, [https://www.akeyless.io/blog/why-you-should-only-use-just-in-time-ephemeral-credentials/](https://www.akeyless.io/blog/why-you-should-only-use-just-in-time-ephemeral-credentials/)  
35. langgraph/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb at main \- GitHub, accessed on January 1, 2026, [https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb)  
36. How to Use LangChain and LangGraph: A Beginner's Guide to AI Workflows, accessed on January 1, 2026, [https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/](https://www.freecodecamp.org/news/how-to-use-langchain-and-langgraph-a-beginners-guide-to-ai-workflows/)  
37. LangGraph Execution Semantics. | by Christoph Bussler \- Medium, accessed on January 1, 2026, [https://chbussler.medium.com/langgraph-execution-semantics-c7dd89900ed4](https://chbussler.medium.com/langgraph-execution-semantics-c7dd89900ed4)  
38. Container Escape \+ AI Agent Risk: Lessons from Box's Security Lead, accessed on January 1, 2026, [https://www.cloudsecuritynewsletter.com/p/container-escape-ai-agent-risk-lessons-from-box-s-security-lead](https://www.cloudsecuritynewsletter.com/p/container-escape-ai-agent-risk-lessons-from-box-s-security-lead)  
39. Self-hosted Linux agents \- Azure Pipelines \- Microsoft Learn, accessed on January 1, 2026, [https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/linux-agent?view=azure-devops)  
40. Top Daytona.io alternatives for running AI code in secure sandboxed environments | Blog, accessed on January 1, 2026, [https://northflank.com/blog/top-daytona-io-alternatives-for-running-ai-code-in-secure-sandboxed-environments](https://northflank.com/blog/top-daytona-io-alternatives-for-running-ai-code-in-secure-sandboxed-environments)  
41. langchain-ai/langgraph: Build resilient language agents as graphs. \- GitHub, accessed on January 1, 2026, [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)  
42. Agents \- Docs by LangChain, accessed on January 1, 2026, [https://docs.langchain.com/oss/python/langchain/agents](https://docs.langchain.com/oss/python/langchain/agents)  
43. von-development/awesome-LangGraph: An index of the LangChain \+ LangGraph ecosystem: concepts, projects, tools, templates, and guides for LLM & multi-agent apps. \- GitHub, accessed on January 1, 2026, [https://github.com/von-development/awesome-LangGraph](https://github.com/von-development/awesome-LangGraph)  
44. Building an Advanced AI Agent: A Step-by-Step Guide to Integrating MCP Servers with LangGraph \- DEV Community, accessed on January 1, 2026, [https://dev.to/amol\_kavitkar/building-an-advanced-ai-agent-a-step-by-step-guide-to-integrating-mcp-servers-with-langgraph-4ocf](https://dev.to/amol_kavitkar/building-an-advanced-ai-agent-a-step-by-step-guide-to-integrating-mcp-servers-with-langgraph-4ocf)  
45. How to Benchmark AI Agents Effectively \- Galileo AI: The AI Observability and Evaluation Platform, accessed on January 1, 2026, [https://galileo.ai/learn/benchmark-ai-agents](https://galileo.ai/learn/benchmark-ai-agents)  
46. The Inspect Sandboxing Toolkit: Scalable and secure AI agent evaluations | AISI Work, accessed on January 1, 2026, [https://www.aisi.gov.uk/blog/the-inspect-sandboxing-toolkit-scalable-and-secure-ai-agent-evaluations](https://www.aisi.gov.uk/blog/the-inspect-sandboxing-toolkit-scalable-and-secure-ai-agent-evaluations)  
47. What CIS Benchmarks Are (and How to Implement Them) \- Wiz, accessed on January 1, 2026, [https://www.wiz.io/academy/compliance/cis-benchmarks](https://www.wiz.io/academy/compliance/cis-benchmarks)  
48. Audit Trails in CI/CD: Best Practices for AI Agents \- Prefactor, accessed on January 1, 2026, [https://prefactor.tech/blog/audit-trails-in-ci-cd-best-practices-for-ai-agents](https://prefactor.tech/blog/audit-trails-in-ci-cd-best-practices-for-ai-agents)  
49. How to design data audit logs for JSON data interface? \- Tencent Cloud, accessed on January 1, 2026, [https://www.tencentcloud.com/techpedia/128123](https://www.tencentcloud.com/techpedia/128123)  
50. Audit Logging for AI: What Should You Track (and Where)? | by Pranav Prakash I GenAI I AI/ML I DevOps I | Medium, accessed on January 1, 2026, [https://medium.com/@pranavprakash4777/audit-logging-for-ai-what-should-you-track-and-where-3de96bbf171b](https://medium.com/@pranavprakash4777/audit-logging-for-ai-what-should-you-track-and-where-3de96bbf171b)  
51. Designing AI Agents That Don't Misbehave \- Global Banking & Finance Review, accessed on January 1, 2026, [https://www.globalbankingandfinance.com/designing-ai-agents-that-don-t-misbehave/](https://www.globalbankingandfinance.com/designing-ai-agents-that-don-t-misbehave/)  
52. Securing AI Agent Execution \- arXiv, accessed on January 1, 2026, [https://arxiv.org/html/2510.21236v1](https://arxiv.org/html/2510.21236v1)  
53. Agentic AI Security: Threats, Defenses, Evaluation, and Open Challenges \- arXiv, accessed on January 1, 2026, [https://arxiv.org/html/2510.23883v1](https://arxiv.org/html/2510.23883v1)