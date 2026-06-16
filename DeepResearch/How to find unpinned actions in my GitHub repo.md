<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# How to find unpinned actions in my GitHub repo

Detecting unpinned actions is a two-minute job with the right tool — but choosing the right tool matters because different scanners have different detection thresholds and blind spots. This guide covers every method from a quick one-liner to full CI-integrated auditing, ranked by coverage breadth.[^1]

***

## Fastest: `zizmor` (One-Liner, 2 seconds)

`zizmor` is the recommended first-pass scanner — written in Rust, it completes a typical repository in a **median of 2.71 seconds** and exclusively flags third-party unpinned actions, skipping official `actions/*` to eliminate noise. It requires no authentication and accepts a directory or a single file:[^1]

```bash
# Install (macOS/Linux)
brew install zizmor          # macOS
cargo install zizmor         # Linux/anywhere with Rust

# Scan all workflows in your repo
zizmor .github/workflows/

# Scan a single file
zizmor .github/workflows/ci.yml

# Output as SARIF (for GitHub Code Scanning upload)
zizmor --format sarif .github/workflows/ > results.sarif

# Ignore official actions/*, only flag third-party
# (default behaviour — no flag needed)
```

Sample output:

```
.github/workflows/ci.yml:18:9: warning[unpinned-uses]: uses: docker/build-push-action@v5
  → Third-party action pinned to mutable tag; use a full commit SHA
  note: see https://docs.github.com/en/actions/security-guides/security-hardening
```

`zizmor` reports **fewer total findings than other tools (509 vs 2,307–2,512)** because it is deliberately conservative — it only flags cases with confirmed exploitability risk, reducing false positives.[^1]

***

## Broadest Coverage: `frizbee` + `scorecard`

`frizbee` finds the most unpinned instances because it checks *all* referenced actions including `actions/*` official ones, container image references, and references in composite actions [^1]. `scorecard` goes even deeper — also checking pinning of `pip install`, `curl | bash`, and other ephemeral dependency patterns beyond `uses:`:

```bash
# frizbee — pure detection mode (dry-run, no writes)
go install github.com/stacklok/frizbee/cmd/frizbee@latest

frizbee gha --dry-run .github/workflows/
# Output: lists every unpinned uses: line with its file + line number

# Also scan composite actions inside .github/actions/
frizbee gha --dry-run --dir .github/actions/ .github/workflows/

# scorecard — broader supply chain health scan
go install sigs.k8s.io/release-utils/cmd/scorecard@latest
# Or via Docker (no install needed):
docker run -e GITHUB_AUTH_TOKEN=$GITHUB_TOKEN \
  gcr.io/openssf/scorecard:stable \
  --repo github.com/YOUR_ORG/YOUR_REPO \
  --checks Pinned-Dependencies

# Returns a score 0–10 + line-by-line findings
```

The difference in reported findings reflects tool design philosophy:[^1]


| Tool | Unpinned Findings (same 2,722 workflows) | What It Skips |
| :-- | :-- | :-- |
| `scorecard` | **2,512** | Nothing — widest scope |
| `scharf` | 2,307 | — |
| `frizbee` | ~1,900 | `@main` / `@master` branch refs |
| `actionlint` | ~1,400 | Container image refs |
| `zizmor` | **509** | Official `actions/*` namespace |
| `poutine` | **0 direct** | Only transitive composite chains [^1] |


***

## Transitive / Composite Action Detection: `poutine` + `scharf`

The tools above only flag *direct* `uses:` references in your workflow files. If an action you use (e.g., `some-action@v2`) itself calls another unpinned action inside its own `action.yml`, your workflow inherits that unpinned transitive dependency — invisibly. This was the exact attack chain in CVE-2025-30066. Two tools specifically catch this:[^1]

```bash
# poutine — targets transitive composite action chains only
go install github.com/boostsecurityio/poutine@latest

# Requires full repo as input (not individual files)
poutine analyze_local .

# Output only appears for composite actions that transitively use mutable tags

# scharf — composite action chain detection + commented-out action scanning
go install github.com/amirfounder/scharf@latest
scharf scan .github/
```

Use `poutine` as a **complement** to `zizmor` or `frizbee`, not a replacement — it returns zero findings for direct workflow vulnerabilities but is the only tool that surfaces transitive supply chain exposure.[^1]

***

## GitHub-Native: CodeQL for Actions (No Install)

GitHub added CodeQL support for GitHub Actions YAML in January 2025 — free for all public repositories, and included in GHAS for private ones. Enabling it requires zero tooling installs:[^2]

```yaml
# .github/workflows/codeql-actions-scan.yml
name: CodeQL Actions Security Scan
on:
  push:
    paths: ['.github/workflows/**', '.github/actions/**']
  pull_request:
    paths: ['.github/workflows/**', '.github/actions/**']
  schedule:
    - cron: '0 8 * * 1'      # Weekly Monday scan

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
      - uses: github/codeql-action/init@v3
        with:
          languages: actions        # ← GitHub Actions YAML language pack
      - uses: github/codeql-action/analyze@v3
```

Findings appear directly in the **Security → Code Scanning** tab of your repository with line-level annotations. GitHub Copilot Autofix can suggest the correct pinned SHA inline in the PR diff.[^2]

***

## `ratchet` — Lint-Only Mode to Audit Before Fixing

`ratchet` (by Seth Vargo, ex-Google) was one of the original pinning tools and has the most readable detection output. Its `lint` subcommand reports without modifying anything:[^3][^4]

```bash
# Install
go install github.com/sethvargo/ratchet@latest

# Lint only — reports every unpinned reference
ratchet lint .github/workflows/ci.yml

# Lint entire directory
for f in .github/workflows/*.yml; do ratchet lint "$f"; done
```

Output format:

```
/repo/.github/workflows/ci.yml:12:9: actions/checkout@v4 is not pinned
/repo/.github/workflows/ci.yml:18:9: docker/build-push-action@v5 is not pinned
/repo/.github/workflows/deploy.yml:9:9: aws-actions/configure-aws-credentials@main is not pinned
```

`ratchet` uses a comment format `# ratchet:owner/action@tagname` that lets you unpin, update, or re-pin in a single command later — making it ideal if you want a lint-first, fix-later workflow.[^3]

***

## Manual Method: Find Unpinned Lines with `grep`

For a fast audit without installing anything, `grep` gives you a readable summary of every `uses:` line that is **not** already a full 40-character SHA:

```bash
# Find all uses: lines NOT pointing to a full SHA
# A pinned SHA looks like: @abcdef1234567890... (40 hex chars)
grep -rn "uses:" .github/ \
  | grep -v "@[0-9a-f]\{40\}" \
  | grep -v "^#"

# More targeted — only flag third-party (non-actions/* and non-github/*)
grep -rn "uses:" .github/ \
  | grep -v "@[0-9a-f]\{40\}" \
  | grep -v "uses: actions/" \
  | grep -v "uses: github/" \
  | grep -v "^#"

# Count total unpinned vs total uses: references
echo "Total uses: $(grep -rc 'uses:' .github/ | awk -F: '{sum+=$2} END {print sum}')"
echo "Unpinned:   $(grep -rn 'uses:' .github/ | grep -v '@[0-9a-f]\{40\}' | wc -l)"
```

This is not a replacement for a dedicated scanner — it will miss unpinned container image `image:` references, and cannot detect transitive chains — but it gives you an instant count for a first-pass audit.[^1]

***

## Integrate Detection into Every PR

The highest-leverage approach is making unpinned action detection part of your CI, so violations are caught at the pull request level before they ever reach `main`:

```yaml
# .github/workflows/security-lint.yml
name: Workflow Security Lint
on:
  pull_request:
    paths: ['.github/**']         # only runs when workflow files change

jobs:
  zizmor:
    name: zizmor (third-party pinning)
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
      - uses: zizmorcore/zizmor-action@v1       # pin this too!
        with:
          sarif-upload: true

  frizbee-audit:
    name: frizbee (all actions incl. official)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
      - run: |
          go install github.com/stacklok/frizbee/cmd/frizbee@latest
          frizbee gha --dry-run .github/workflows/ && echo "✅ All pinned" \
            || (echo "❌ Unpinned actions found — see output above" && exit 1)

  poutine-transitive:
    name: poutine (transitive chains)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2
      - run: |
          go install github.com/boostsecurityio/poutine@latest
          poutine analyze_local .
```


***

## Choosing the Right Tool

The March 2026 empirical benchmark of 9 scanners across 2,722 enterprise workflows gives a direct comparison:[^1]


| Goal | Best Tool | Why |
| :-- | :-- | :-- |
| Fastest single scan | `zizmor` | 2.71s median, low noise |
| Widest coverage | `scorecard` | Catches pip/curl pinning too |
| Auto-fix alongside detection | `frizbee` | Only tool accepting files *or* repos + auto-fix |
| Transitive composite chains | `poutine` + `scharf` | The only tools that see second-order deps |
| GitHub-native, no installs | CodeQL for Actions | Free for public repos, Copilot Autofix included |
| Pre-fix audit with rollback | `ratchet lint` | Clean lint→pin→update workflow |
| Org-wide enforcement (no scanning) | GitHub Policy (Aug 2025) | Blocks unpinned workflows at runtime [^5] |

The production-grade answer is to run **`zizmor` + `poutine` in CI** for coverage of both direct and transitive vulnerabilities, with **Dependabot** keeping pinned SHAs current automatically so detection never triggers again after the initial fix.[^6][^1]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://arxiv.org/html/2601.14455v1

[^2]: https://github.blog/security/application-security/how-to-secure-your-github-actions-workflows-with-codeql/

[^3]: https://dev.to/jonasbn/pinning-github-actions-and-using-ratchet-3lmc

[^4]: https://github.com/sethvargo/ratchet

[^5]: https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/

[^6]: https://github.com/dependabot/dependabot-core/issues/4691

[^7]: https://arxiv.org/html/2601.14455v2

[^8]: https://arxiv.org/html/2511.13341v1

[^9]: https://arxiv.org/html/2502.06662v1

[^10]: https://arxiv.org/html/2601.10338v1

[^11]: https://arxiv.org/pdf/2601.10338.pdf

[^12]: https://arxiv.org/html/2603.04582v1

[^13]: https://arxiv.org/html/2601.14163v1

[^14]: https://arxiv.org/pdf/2603.28807.pdf

[^15]: https://aclanthology.org/2026.eacl-long.385.pdf

[^16]: https://arxiv.org/html/2511.02230v1

[^17]: https://www.reddit.com/r/devops/comments/1l067g9/updateactionpins_a_simple_cli_tool_for_updating/

[^18]: https://github.com/github/gh-aw/issues/22250

[^19]: https://github.com/synacktiv/octoscan/issues/26

[^20]: https://www.stepsecurity.io/blog/pinning-github-actions-for-enhanced-security-a-complete-guide

[^21]: https://github.com/rhysd/actionlint/issues/435

[^22]: https://cloudnativeengineer.substack.com/p/github-actions-reproducibility-security

[^23]: https://github.com/marketplace/actions/enforce-full-sha-commit-pinning-in-github-actions

[^24]: https://cycode.com/blog/github-actions-vulnerabilities/

[^25]: https://www.themoonlight.io/en/review/unpacking-security-scanners-for-github-actions-workflows

