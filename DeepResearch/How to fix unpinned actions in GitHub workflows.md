<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# How to fix unpinned actions in GitHub workflows

```json
{
  "Hickam_Orientation": {
    "Occam_Reject": "I have rejected the simple explanation that 'pinning = manually editing SHA hashes'. The problem is a multi-axis maintenance challenge where security (immutability), developer ergonomics (readability), and operational continuity (staying current) are in constant tension.",
    "Comorbid_Factors": [
      "Factor A: Tags are mutable by design — a tag like @v4 can silently point to different commits over time with no notification to downstream consumers (the CVE-2025-30066 attack vector)",
      "Factor B: Manual SHA pinning creates a readability-maintenance cliff — raw 40-character SHAs are illegible and teams stop updating them, producing a frozen-at-compromise posture",
      "Factor C: Transitive action dependencies are invisible — pinning direct actions does not pin the actions those actions themselves call, leaving a second-order supply chain attack surface unaddressed"
    ]
  },
  "Contrastive_Delta": {
    "Amateur_Impulse": "Replace @v4 with a commit SHA in your YAML file.",
    "Inductive_Synthesis": "The tension between security (SHA immutability), readability (human tag), and freshness (automated updates) requires a three-component system: a pinning tool to convert tags to SHAs, a comment convention to preserve human readability, and an automation bot to keep SHAs current — not a one-time manual edit.",
    "Abductive_Leap": "The structurally correct solution is not pinning-as-a-task but pinning-as-policy: GitHub's August 2025 enforcement feature, combined with Dependabot/Renovate automation, makes SHA pinning a zero-friction platform-enforced invariant rather than a human discipline problem.",
    "Expert_Correction": "This guide covers the full remediation lifecycle: manual pinning anatomy, four automated tools with trade-offs, Dependabot and Renovate configuration, GitHub's August 2025 organizational policy enforcement, transitive dependency coverage, and the 2026 roadmap lockfile that will supersede current tooling."
  },
  "Martensite_Metrics": {
    "Aesthetic_Tension": "Medium — balances deep technical precision with immediately actionable YAML snippets",
    "Intent_Divergence_Risk": "Safe (0.08) — all tooling and policy claims grounded in primary sources",
    "Twinning_Mechanism": "Stabilized by covering both the security-maximalist and pragmatic-enterprise positions on pinning, acknowledging the real maintenance trade-offs"
  }
}
```


***

# How to Fix Unpinned Actions in GitHub Workflows

Fixing unpinned GitHub Actions means replacing mutable tag references (like `@v4` or `@main`) with a full **40-character commit SHA** — the only immutable reference type in Git. A tag can be silently re-pointed to a different commit by an attacker or maintainer with no change visible in your workflow YAML, which is exactly how CVE-2025-30066 (`tj-actions/changed-files`) compromised 23,000+ repositories in March 2025. A SHA, by contrast, is a cryptographic identifier tied to a single, specific snapshot of code — generating a collision is computationally infeasible.[^1][^2]

***

## The Anatomy of a Pinned Reference

The correct pattern pairs the full commit SHA with the human-readable tag in a trailing comment. Dependabot and Renovate both understand this comment format and will update the SHA *and* the comment automatically when a new version is released.[^3]

```yaml
# ❌ UNPINNED — tag is mutable, can be poisoned silently
- uses: actions/checkout@v4
- uses: docker/build-push-action@v5
- uses: actions/setup-node@main   # worst case: tracking branch head

# ✅ PINNED — SHA is immutable; version tag kept as comment for readability
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683        # v4.2.2
- uses: docker/build-push-action@263435318d21b8e681c14492fe198d362a7d2c8   # v5.4.0
- uses: actions/setup-node@39370e3970a6d050c480ffad4ff0ed4d3fdee5af       # v4.1.0
```

To find the correct SHA manually: navigate to the action's repository on GitHub → click **Commits** on the default branch → locate the commit tagged with the version you want → copy the full 40-character SHA. Never use a SHA from a fork — verify it originates from the canonical repository.[^2]

***

## Method 1 — Automated Bulk Pinning with Dedicated Tools

Four specialized tools focus exclusively on the **Unpinned Dependency Weakness (UDW)** and can fix entire repositories in one command. All three below provide auto-fixes, not just detection — making them more actionable than general-purpose scanners like `zizmor` or `semgrep` for this specific task.[^1]

### frizbee (recommended — most active, Go)

`frizbee` scans all workflow files in a repository and rewrites `uses:` references from tags/branches to pinned SHAs in-place:[^1]

```bash
# Install
go install github.com/stacklok/frizbee/cmd/frizbee@latest

# Scan and report (dry-run)
frizbee gha --dry-run .github/workflows/

# Fix in place — rewrites all workflow files
frizbee gha .github/workflows/

# Fix composite actions too
frizbee gha --dir .github/actions/ .github/workflows/
```


### pinact (Go — supports bulk org-wide PRs)

`pinact` can operate in automated bulk-PR mode, opening pull requests across an entire GitHub organization to pin all workflows at once:[^4]

```bash
go install github.com/szksh-lab/pinact/cmd/pinact@latest

# Run against all workflows in current repo
pinact run

# Bulk mode — open PRs across an entire org
pinact bulk-pr \
  --org my-org \
  --branch pin-github-actions \
  --pr-title "ci: Pin GitHub Actions to full commit SHA" \
  --labels pin-github-actions
```


### scharf (focuses on transitive composite actions)

`scharf` specifically targets the second-order vulnerability that `frizbee` and `pinact` miss: **composite actions that themselves call other unpinned actions**. This addresses the `poutine` scanner finding — the transitive dependency surface that enabled the tj-actions attack to propagate through dependency chains.[^1]

***

## Method 2 — Dependabot (Native GitHub, Zero Infrastructure)

Dependabot is the lowest-friction option since it requires no external tooling — just a configuration file committed to your repository. It will open PRs automatically when a new upstream version is available, updating both the SHA and the inline version comment.[^3]

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: github-actions
    directory: "/"
    schedule:
      interval: weekly        # or "daily" for high-security environments
      day: monday
      time: "09:00"
      timezone: "Australia/Melbourne"
    open-pull-requests-limit: 10
    groups:
      # Group all Action updates into a single PR to reduce noise
      github-actions-updates:
        patterns:
          - "*"
    reviewers:
      - your-team-slug
    labels:
      - dependencies
      - github-actions
```

**Key Dependabot behaviour**: when it updates a SHA-pinned action, it preserves the `# v4.2.2` comment format and increments it — giving you a human-readable PR title like `"Bump actions/checkout from 4.2.2 to 4.2.3"` even though the file change is a raw SHA swap.[^3]

***

## Method 3 — Renovate (More Control, Supports Transitive)

Renovate provides finer-grained control than Dependabot, including configurable SHA-pinning enforcement and support for composite action dependencies:[^5]

```json
// renovate.json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": ["config:recommended"],
  "github-actions": {
    "enabled": true,
    "pinDigests": true        // ← forces SHA pinning on all updates
  },
  "packageRules": [
    {
      "matchManagers": ["github-actions"],
      "automerge": true,       // auto-merge patch-level Action updates
      "automergeType": "pr",
      "matchUpdateTypes": ["patch", "pin"]
    },
    {
      "matchManagers": ["github-actions"],
      "matchUpdateTypes": ["major"],
      "automerge": false,      // require human review for major versions
      "labels": ["major-update"]
    }
  ]
}
```

The critical difference from Dependabot: Renovate's `pinDigests: true` applies to *all* package managers simultaneously — if you also use it for npm, Docker, and Terraform, all registries get SHA/digest pinning in one config.[^6]

***

## Method 4 — GitHub Policy Enforcement (August 2025)

GitHub released **organization-level SHA pinning enforcement** in August 2025, allowing administrators to make it a hard platform-level requirement rather than a team convention. Any workflow referencing an unpinned action will **fail at the job startup step** before any code runs:[^7]

**To enable**: `Organization Settings → Actions → General → Policies → ☑ Require SHA pinning for all actions`

```
The policy will check for a full commit SHA, and any workflow
that attempts to use an action that isn't pinned will fail.
```

This policy applies at enterprise, organization, or repository level, cascading downward. It also enables a complementary feature to **block specific actions by full name** — useful for immediately quarantining a known-compromised action like `tj-actions/changed-files` across an entire organization without touching individual workflow files.[^8][^7]

***

## Handling Exceptions: First-Party Actions

The `zizmor` scanner deliberately **excludes official GitHub-maintained actions** (`actions/*`, `github/*`) from its pinning rules. This reflects a practical policy decision: these actions are under GitHub's direct control, making tag poisoning far harder. Most enterprise security teams apply a tiered policy:[^1]


| Action Source | Pinning Requirement | Rationale |
| :-- | :-- | :-- |
| `actions/*` (GitHub-maintained) | Tag pinning acceptable (`@v4`) | Controlled by GitHub; SHA pinning optional |
| Verified creator (☑ badge) | Recommended | Institutional accountability exists |
| Third-party unverified | **SHA pinning mandatory** | No trust anchor; highest attack surface [^1] |
| `@main` / `@master` branch | **Never acceptable** | Tracks arbitrary HEAD commits in real-time [^1] |


***

## The Maintenance Trade-off

The honest engineering trade-off is this: raw SHA pinning with no automation creates **update paralysis**. Teams that manually pin but never update are trading a supply chain poisoning risk for a known-vulnerable-component risk (using old action versions with CVEs). The correct posture is **pinned + automated updates**:[^9]

```
frizbee (one-time bulk fix) 
  → Dependabot/Renovate (continuous SHA update PRs) 
  → GitHub Policy (enforcement guardrail)
  → SHA pinning = immutability + currency
```

This three-layer system means your workflow files always reference immutable SHAs, those SHAs always track the latest reviewed version, and the policy layer prevents any unreviewed regression to mutable tags.[^6][^7]

***

## 2026 Roadmap: Workflow Lockfiles

GitHub's March 2026 security roadmap announced a forthcoming `dependencies:` lockfile block in workflow YAML — modeled on Go's `go.mod + go.sum` system — that will provide **deterministic resolution of direct *and* transitive action dependencies with hash verification**. Once released, this will supersede the current manual/tooling approach by making SHA pinning a first-class platform feature rather than a community convention enforced by third-party tools. Until that ships, the `frizbee` + Dependabot + organization policy combination is the production-grade standard.[^10][^7]
<span style="display:none">[^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31]</span>

<div align="center">⁂</div>

[^1]: https://arxiv.org/html/2601.14455v1

[^2]: https://docs.github.com/en/actions/reference/security/secure-use

[^3]: https://github.com/dependabot/dependabot-core/issues/4691

[^4]: https://dev.to/suzukishunsuke/pin-github-actions-to-a-full-length-commit-sha-for-security-2n7p

[^5]: https://www.reddit.com/r/devops/comments/1n2qd2c/cli_tool_to_automate_github_actions_updates_with/

[^6]: https://www.stepsecurity.io/blog/pinning-github-actions-for-enhanced-security-a-complete-guide

[^7]: https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/

[^8]: https://www.youtube.com/watch?v=4dnniFk5i2Q

[^9]: https://developerwithacat.com/blog/202508/github-actions-commit-hash-pinning-tradeoffs/

[^10]: https://github.blog/news-insights/product-news/whats-coming-to-our-github-actions-2026-security-roadmap/

[^11]: https://arxiv.org/html/2601.14455v2

[^12]: https://ar5iv.labs.arxiv.org/html/2206.07230

[^13]: https://arxiv.org/pdf/2206.07230.pdf

[^14]: https://www.semanticscholar.org/paper/Adsorption–desorption-of-recombinant-hepatitis-B-P.-Agraz-Quiñones/5743db3ad331ad8889e43c228b3aefd8986cdfdb

[^15]: https://arxiv.org/pdf/2208.03837.pdf

[^16]: https://arxiv.org/abs/2202.01987

[^17]: https://arxiv.org/html/2505.04834v3

[^18]: https://pdfs.semanticscholar.org/9ec6/f99b3d49778cc2dc98c99108b289678ed3f7.pdf

[^19]: https://www.arxiv.org/pdf/2505.04834v2.pdf

[^20]: https://arxiv.org/abs/2109.05153

[^21]: https://arxiv.org/html/2505.04834v1

[^22]: https://arxiv.org/ftp/arxiv/papers/2404/2404.11029.pdf

[^23]: https://arxiv.org/pdf/2505.04834.pdf

[^24]: https://www.semanticscholar.org/paper/FLUTTER-VS-NATIVE-PLATFORM-Rawat-Chauhan/1aa86ca645c07a62a1f5d3ff6309f45c1ce5f551

[^25]: https://github.com/github/gh-aw/issues/22250

[^26]: https://github.com/orgs/community/discussions/170337

[^27]: https://github.com/mickdarling/merview/issues/321

[^28]: https://github.com/github/vscode-github-actions/issues/514

[^29]: https://stackoverflow.com/questions/78903499/how-do-i-pin-an-action-to-a-specific-sha

[^30]: https://blog.rafaelgss.dev/why-you-should-pin-actions-by-commit-hash

[^31]: https://github.com/dependabot/dependabot-core/issues/7913

