# **AI Development Environment Corporate Policy**

### **1.0 Purpose, Scope, and Applicability**

Standardizing AI development environments is a critical initiative for ensuring high performance, robust security, and consistent reproducibility across all engineering teams. As AI-augmented workflows become central to our operations, the need for a common, optimized, and secure foundation is paramount. This document establishes the official corporate policy for creating and maintaining such environments, designed to eliminate configuration drift, streamline collaboration, and maximize the value of our tooling investments.

**The purpose of this policy is to establish a mandatory, secure, and reproducible standard for all AI development environments.**

#### **Scope**

This policy governs the architecture, tooling, security protocols, and reproducibility standards for all software projects involving artificial intelligence (AI), machine learning (ML), or large language model (LLM) development.

#### **Applicability**

Adherence to this policy is mandatory for all personnel involved in software architecture and development, including full-time employees and contractors.

This policy begins by defining the foundational architectural requirements that serve as the bedrock for our entire standardized stack.

\--------------------------------------------------------------------------------

### **2.0 Foundational Environment Architecture: Windows Subsystem for Linux (WSL2)**

The strategic importance of the underlying operating system architecture cannot be overstated. Performance in AI development is directly and critically tied to filesystem I/O. Consequently, the decision of where project code, data, and dependencies reside is a foundational architectural choice that dictates the performance and efficiency of the entire development lifecycle.

#### **2.1 Mandatory Filesystem Policy**

**The Cardinal Rule of WSL2 Performance: Keep Linux files in Linux.**

It is an architectural mandate that for any performance-sensitive AI development, **all project files, source code, datasets, and virtual environments MUST be stored within the native Linux filesystem** (e.g., `~/projects/`).

Accessing files across the OS boundary on mounted Windows drives (e.g., `/mnt/c/`) incurs a significant performance penalty. I/O-intensive operations such as `git status`, `npm install`, creating Python virtual environments, or compiling code are dramatically slower when performed on files located on the Windows filesystem. Adherence to this policy is the single most important factor in ensuring a high-performance development environment.

#### **2.2 Network Configuration Standard**

The default WSL2 network configuration (`nat` mode) introduces unnecessary complexity and performance limitations. To ensure seamless connectivity and optimal throughput, a `mirrored` networking mode is mandated.

| Feature | NAT Mode (Default) | Mirrored Mode |
| :---- | :---- | :---- |
| **`localhost` Access** | Yes. Transparent port forwarding makes `localhost` accessible from Windows for most common web development scenarios. | Yes. More robust, bidirectional access. Services are accessible on `localhost` from both Windows and WSL. |
| **IPv6 Support** | Limited / Problematic | Yes. Full IPv6 support. |
| **VPN Compatibility** | Poor. Often requires complex workarounds. | Excellent. Mirrors the host's network state, including VPN connections. |
| **Performance/Throughput** | Lower. Subject to overhead and potential throttling from the NAT layer. | High. Near-native network performance. |

It is policy that `networkingMode=mirrored` must be configured in the global `.wslconfig` file for all development environments. This standardizes network behavior, simplifies access to local services, and maximizes network performance.

#### **2.3 VHDX File Management**

The virtual hard disk (`ext4.vhdx`) that stores the WSL2 filesystem grows automatically as data is added but does not shrink automatically when data is deleted. This can lead to the VHDX file consuming a large amount of disk space on the Windows host over time.

It is the policy and responsibility of each developer to periodically reclaim this disk space through a manual compaction process. A formal, step-by-step procedure for this maintenance task is provided in **Appendix C**.

With this performant Linux foundation established, we now turn to the standardized toolset that will operate within it: the Integrated Development Environment.

\--------------------------------------------------------------------------------

### **3.0 Standardized Integrated Development Environment (IDE): Visual Studio Code**

The Integrated Development Environment (IDE) serves as the primary control plane for all development activities. Standardizing the IDE, its extension ecosystem, and its core AI tooling is essential for creating a consistent, efficient, and conflict-free developer experience across the organization.

#### **3.1 Official AI Coding Assistant**

It is policy that **GitHub Copilot (Pro tier)** is the sole approved AI coding assistant for use within the organization.

This decision is based on a structured evaluation of the current AI assistant landscape. GitHub Copilot's key differentiators make it the optimal choice for our standardized stack:

* **Unparalleled IDE Integration:** As a first-party Microsoft product, its integration with VSCode is exceptionally deep and seamless. New features are often released directly into the editor's core, providing a native-feeling experience.  
* **Rapid Pace of Innovation:** Microsoft continues to aggressively roll out agentic capabilities, advanced customization features, and deeper workflow integrations, ensuring the tool remains at the forefront of AI-augmented development.  
* **Optimal Value Proposition (Pro Tier):** The Pro tier provides the best value for professional developers by offering a balance of unlimited code completions and a generous number of "premium requests" for advanced chat and agentic tasks, all without the complexity of credit-based pricing systems.

#### **3.2 Mandated Extension Ecosystem**

To ensure stability and provide a common, powerful toolset for all developers, the following curated set of VSCode extensions is mandated. Deviation from this mandated extension list is prohibited without a formal exception granted by the Developer Experience committee. Unapproved extensions will be automatically disabled.

**Core Python & Data Science Stack**

* Python (`ms-python.python`)  
* Pylance (`ms-python.vscode-pylance`)  
* Jupyter (`ms-toolsai.jupyter`)  
* Data Wrangler (`ms-toolsai.datawrangler`)

**LLM Application Development**

* LangGraph Visualizer (`hridesh-net.LangGraph_Extension`)  
* Vex \- Vector Database Manager (`tsonglew.vecx`)  
* Semantic Code Search (`zilliz.semanticcodesearch`)

**Productivity and DevOps Tooling**

* GitLens (`eamodio.gitlens`)  
* Prettier \- Code formatter (`esbenp.prettier-vscode`)  
* Better Comments (`aaron-bond.better-comments`)  
* Todo Tree (`Gruntfuggly.todo-tree`)  
* Docker (`ms-azuretools.vscode-docker`)

#### **3.3 Extension Conflict Resolution Protocol**

The increasing power of extensions, particularly AI assistants, can lead to architectural collisions and performance issues. A common conflict pattern involves AI assistants interfering with language servers like Pylance.

To systematically diagnose and resolve these issues, the following protocol is mandated:

1. **Initial Diagnosis:** If the editor feels sluggish, use the `Developer: Show Running Extensions` command from the Command Palette. Investigate any extensions with unusually long activation times, as they are often the source of performance degradation.  
2. **Isolation:** To definitively identify a problematic extension, the `Help: Start Extension Bisect` tool must be used. This tool uses a binary search process to efficiently isolate the single extension causing the issue.

It is strictly prohibited to run more than one AI code completion assistant (e.g., GitHub Copilot and Tabnine) simultaneously in the same workspace, as this is a known cause of conflicts and performance issues.

Now that the IDE and its toolset are standardized, we must ensure these environments can be reproduced reliably across all teams and projects.

\--------------------------------------------------------------------------------

### **4.0 Reproducibility and Collaboration Standard: Dev Containers**

Reproducibility is a cornerstone of professional software engineering. To eliminate environment-based inconsistencies—the classic "works on my machine" problem—and to ensure all team members operate in identical, version-controlled setups, the organization has standardized on Dev Containers.

It is policy that for all collaborative projects, a **Dev Container** must be used as the development environment.

A `devcontainer.json` file in the project repository defines the complete environment, from the operating system and system dependencies to the required IDE extensions and post-creation setup commands.

#### **Reference Implementation: GPU-Enabled PyTorch Project**

The following `devcontainer.json` provides a reference implementation for a typical ML project requiring GPU access.

{  
    "name": "PyTorch-GPU-Dev-Container",  
    "image": "nvcr.io/nvidia/pytorch:23.10-py3",  
    "runArgs": \["--gpus=all"\],  
    "customizations": {  
        "vscode": {  
            "extensions": \[  
                "ms-python.python",  
                "ms-python.vscode-pylance",  
                "ms-toolsai.jupyter",  
                "eamodio.gitlens",  
                "github.copilot"  
            \]  
        }  
    },  
    "postCreateCommand": "pip install \-r requirements.txt",  
    "remoteUser": "root"  
}

This configuration serves as a powerful, declarative blueprint for a reproducible environment:

* **`image`**: Specifies the use of a pre-built, optimized container from NVIDIA's NGC catalog, which includes the correct versions of CUDA and PyTorch.  
* **`runArgs`**: Passes the `--gpus=all` argument to the Docker runtime, making the host machine's NVIDIA GPUs available inside the container.  
* **`customizations`**: Automatically installs the mandated VSCode extensions inside the container, ensuring a consistent and policy-compliant toolset for every developer.  
* **`postCreateCommand`**: Executes after the container is built to install project-specific Python dependencies from a `requirements.txt` file.

Ensuring reproducibility establishes a consistent baseline; now we must secure it. The following section details mandatory protocols for protecting sensitive data within these environments.

\--------------------------------------------------------------------------------

### **5.0 Security and Data Privacy Protocols**

Security is of critical importance in all AI development activities. The management of sensitive data, including API keys, credentials, and proprietary source code, must adhere to the highest standards of data privacy and governance.

#### **5.1 Secrets Management Policy**

**Hardcoding secrets (API keys, tokens, credentials) into source code is strictly forbidden.**

This is a major security vulnerability and a violation of company policy. The following practices are mandated:

* **Application Code:** All secrets required by application code must be managed through environment variables.  
* **VSCode Extensions:** For extensions that require authentication, developers should leverage VSCode's built-in `SecretStorage` API. This API provides a secure way to store sensitive information by using the host operating system's native credential management system (e.g., Windows Credential Manager, macOS Keychain).

#### **5.2 AI Assistant Data Governance**

The use of our officially mandated AI assistant is governed by the specific data handling policies of the **GitHub Copilot for Business** plan. All personnel must be aware of and adhere to these protections:

* **Data Transmission:** Code snippets transmitted from the editor to the GitHub Copilot service are encrypted in transit.  
* **Data Retention and Training:** Under the Copilot for Business plan, transmitted code snippets are discarded immediately after a suggestion is returned. This data is **not** retained and is **not** used to train the public models.  
* **Content Exclusion:** Administrators can configure content exclusion policies to prevent Copilot from processing files in specific repositories that contain sensitive or proprietary information.

With a secure and reproducible environment established, we now codify the exact workflows developers must follow to maximize its value.

\--------------------------------------------------------------------------------

### **6.0 Standard AI-Augmented Workflow**

To maximize the value of our standardized tooling, developers must move beyond ad-hoc, unstructured interactions with AI assistants. This section codifies a formal, efficient, and reproducible workflow for AI-augmented development.

#### **6.1 The AI-Augmented Development Cycle**

The following iterative development cycle is the official, mandated workflow for leveraging AI assistance in software development:

1. **Prompt (Specification):** Begin not with code, but with a high-level comment in a source file or a detailed prompt in the Copilot Chat view. Describe the desired functionality, inputs, and outputs with clarity and precision.  
2. **Generate (First Draft):** Use the AI to generate the initial code block or function. This serves as the first-draft scaffolding for the feature.  
3. **Run & Debug (Validation):** Immediately execute the generated code. Use VSCode's integrated debugger and testing tools to validate its functionality and identify any errors.  
4. **Explain & Refine (AI Dialogue):** If the code is incorrect or its logic is unclear, use inline chat (`Ctrl+I`) or the "Fix with Copilot" action to engage the AI. Ask for explanations, suggest refactorings, or request corrections.  
5. **Test (Quality Assurance):** Once the code is functional, prompt the AI to generate unit tests for it using the project's testing framework (e.g., pytest).  
6. **Refactor (Optimization):** With functional code and passing tests, ask the AI for final optimizations, adherence to style guides, or improvements to idiomatic structure.  
7. **Commit (Version Control):** After staging the changes, use the AI to help generate a clear, descriptive, and conventional commit message based on the code diff.

#### **6.2 Mandatory AI Customization for Project Consistency**

To ensure the AI assistant produces code that is consistent with project-specific standards, every project repository **must** include a `.github/copilot-instructions.md` file.

This file provides persistent, high-level context to Copilot for all chat interactions. It should be used to define the project's coding standards, preferred libraries, naming conventions, and core architectural principles. Copilot will automatically apply these guidelines when generating code, ensuring consistency across the entire codebase.

The following template should be used as a starting point:

* Use PyTorch for all neural network implementations.  
* Adhere to PEP 8 for Python styling. Use ruff for formatting.  
* All functions must have Google-style docstrings and full type hints.  
* Prefer functional programming concepts where possible; avoid mutable state.

To ensure immediate and consistent adoption of this policy, the following appendices provide the actionable artifacts required to bootstrap a compliant environment from scratch.

\--------------------------------------------------------------------------------

### **7.0 Appendices: Standard Implementation Artifacts**

The following appendices contain codified, ready-to-use artifacts to ensure the rapid, consistent, and compliant bootstrapping of the development environment on any new machine.

#### **Appendix A: Extension Installation Script**

This shell script automates the installation of all mandated VSCode extensions from the command line. Save this file as `install_extensions.sh` and execute it in a shell.

\#\!/bin/bash  
\# Script to install all mandatory VSCode extensions for the corporate AI development environment.

echo "Installing Core Python & Data Science Stack..."  
code \--install-extension ms-python.python  
code \--install-extension ms-python.vscode-pylance  
code \--install-extension ms-toolsai.jupyter  
code \--install-extension ms-toolsai.datawrangler

echo "Installing LLM Application Development Stack..."  
code \--install-extension hridesh-net.LangGraph\_Extension  
code \--install-extension tsonglew.vecx  
code \--install-extension zilliz.semanticcodesearch

echo "Installing Productivity and DevOps Tooling..."  
code \--install-extension eamodio.gitlens  
code \--install-extension esbenp.prettier-vscode  
code \--install-extension aaron-bond.better-comments  
code \--install-extension Gruntfuggly.todo-tree  
code \--install-extension ms-azuretools.vscode-docker

echo "All mandated extensions installed."

#### **Appendix B: Standard `settings.json` Configurations**

It is critical to scope VSCode settings correctly to prevent configuration conflicts. Settings should be applied at the appropriate level: User (global look-and-feel), Remote (environment-specific), or Workspace (project-specific).

**User `settings.json` (for UI/Editor Appearance on Windows)** *This file defines personal preferences and should not contain project-specific logic.*

{  
    "workbench.colorTheme": "Catppuccin Macchiato",  
    "workbench.iconTheme": "vscode-icons",  
    "editor.fontFamily": "'Fira Code', 'JetBrains Mono', Consolas, 'Courier New', monospace",  
    "editor.fontLigatures": true,  
    "workbench.sideBar.location": "right",  
    "editor.minimap.enabled": false,  
    "explorer.openEditors.visible": 1,  
    "workbench.startupEditor": "none",  
    "terminal.integrated.defaultProfile.windows": "PowerShell"  
}

**Remote `settings.json` (for WSL Environment)** *This file contains settings specific to the WSL environment, such as performance tuning for language servers.*

{  
    "python.analysis.typeCheckingMode": "basic",  
    "python.analysis.useLibraryCodeForTypes": false,  
    "python.analysis.packageIndexDepths": \[  
        {  
            "name": "langchain\_core",  
            "depth": 5  
        }  
    \]  
}

**Workspace `.vscode/settings.json` (for Project-Specific Formatting & Linting)** *This file must be committed to the project repository to ensure consistent behavior for all collaborators.*

{  
    "editor.formatOnSave": true,  
    "python.formatting.provider": "black",  
    "python.linting.enabled": true,  
    "python.linting.ruffEnabled": true,  
    "python.testing.pytestEnabled": true,  
    "python.testing.unittestEnabled": false,  
    "files.exclude": {  
        "\*\*/\_\_pycache\_\_": true,  
        "\*\*/.pytest\_cache": true,  
        "\*\*/.venv": true,  
        "\*\*/venv": true  
    },  
    "search.exclude": {  
        "\*\*/.venv": true,  
        "\*\*/venv": true,  
        "\*\*/\_\_pycache\_\_": true  
    },  
    "\[python\]": {  
        "editor.defaultFormatter": "ms-python.black-formatter",  
        "editor.codeActionsOnSave": {  
            "source.organizeImports": "explicit"  
        }  
    }  
}

#### **Appendix C: VHDX Compaction Procedure**

The following formal procedure must be followed to reclaim disk space from the WSL2 virtual hard disk (`ext4.vhdx`).

1. **Clean Up Inside WSL:**  
   * Open your WSL terminal.  
   * Remove unnecessary files, clear package manager caches (`sudo apt clean`), and prune any unused Docker objects (`docker system prune -a`).  
2. **Shut Down WSL from PowerShell:**  
   * Open a PowerShell terminal as an administrator on Windows.  
   * Execute the command `wsl --shutdown` to ensure the VHDX file is not in use.  
3. **Compact the VHDX File:**  
   * In the same PowerShell terminal, run `Optimize-VHD -Path <PathToYourVHDXFile> -Mode Full`.  
   * You can find the path to your `ext4.vhdx` file in your user's `AppData` directory (e.g., `C:\Users\<YourUsername>\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\ext4.vhdx`).  
   * Alternatively, you can use the `DiskPart` utility by running `diskpart`, then selecting the vdisk file (`select vdisk file="<PathToVHDX>"`), and finally compacting it (`compact vdisk`).

