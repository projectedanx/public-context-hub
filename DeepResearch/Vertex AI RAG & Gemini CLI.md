

# **Vertex AI Capability Audit and Custom RAG Implementation Blueprint**

## **Executive Summary and Strategic Recommendation**

This report details a comprehensive research and implementation plan for leveraging Google's Vertex AI platform to build a secure, queryable knowledge base from private research documents. It begins with a functional audit of the Vertex AI ecosystem for a technically proficient developer, followed by a specific, step-by-step blueprint for implementing a custom Retrieval-Augmented Generation (RAG) system accessible via a command-line interface (CLI).

### **The Core Decision: The RAG Spectrum**

Navigating Google Cloud's generative AI offerings requires understanding the "spectrum of abstraction"—a trade-off between managed simplicity and granular control.1 For RAG, this spectrum is defined by three primary services:

1. **Vertex AI Search (The "Fully-Assembled Car"):** This is a turnkey, enterprise-grade application.1 It provides an "out-of-the-box RAG solution" that allows a developer to create a "Google-quality search app" in just a few clicks, typically by pointing it at a data source.2 This path prioritizes speed-to-value and abstracts nearly all complexity, but offers the least control over the underlying retrieval and chunking logic. Its pricing model is based on data storage (per GiB) and query volume.4  
2. **Vertex AI RAG Engine (The "Customizable Chassis"):** This is a flexible, managed framework.1 It provides the ideal balance for this project, abstracting the complex *infrastructure* (like the managed vector database 5) while giving the developer explicit control over the RAG components. With the RAG Engine, one can define chunking strategies, select specific embedding models, and fine-tune retrieval parameters.6 This component-based approach is reflected in its pricing, which is disaggregated across the components used (e.g., embedding model, Spanner instance for indexing, reranking API).7  
3. **Vertex AI Vector Search (The "Engine Block"):** This is the powerful, low-level component for developers who need maximum control to build a "Fully DIY RAG" system from the ground up.1 It is a high-scale, low-latency vector database.9 This path requires the developer to manually manage data parsing, chunking, embedding generation, index creation, and all orchestration logic.

### **Strategic Recommendation**

The **Vertex AI RAG Engine** (Custom Path) is the recommended solution. This decision is a direct consequence of the project's foundational requirements for "Practical Application & Data Sovereignty."

Vertex AI Search is too much of a "black box," ingesting data into its own managed app. The "Fully DIY" path using Vector Search is an unnecessary engineering burden.

The RAG Engine aligns perfectly with the project's goals. It allows the private research corpus to remain in a sovereign Google Cloud Storage (GCS) bucket, with the RAG Engine granted read-access. The developer retains full control over how this data is parsed, chunked, and indexed into a distinct RagCorpus asset.11 This combination of infrastructure management and component-level control makes it the optimal choice for a researcher building a production-ready, secure tool.

The following plan provides an end-to-end implementation roadmap:

* **Phase 1:** An audit of the Vertex AI platform components.  
* **Phase 2:** A complete, code-level guide to building the custom RAG system.  
* **Phase 3:** A practical strategy for creating a "CLI-First" wrapper.  
* **Phase 4:** Enterprise-grade automation and security enhancements.

## **Part 1: Vertex AI Platform Audit: A Developer's Glossary**

For a developer new to the ecosystem, mapping existing MLOps and GenAI concepts to Google's specific product names is the first hurdle. The following table serves as a functional "Rosetta Stone" for the key services relevant to this project.

| Developer Need | Vertex AI Service(s) | Function & Analysis |
| :---- | :---- | :---- |
| **Model Prototyping** | **Vertex AI Studio** | The Google Cloud console UI for "rapidly prototyping and testing" generative AI models.12 This is the primary sandbox for prompt design, iteration, and tuning.12 |
| **Model Access** | **Model Garden** | The central library to "discover, test, customize, and deploy" over 200 models 13, including Google's Gemini, as well as partner models like Llama and Claude.6 |
| **Development IDE** | **Vertex AI Workbench** | The managed, Jupyter-based development environment. It is the recommended runtime for official quickstarts and notebooks.14 |
| **ML Orchestration** | **Vertex AI Pipelines** | The serverless MLOps workflow orchestrator for automating, monitoring, and governing ML workflows.16 It runs pipelines defined using the Kubeflow Pipelines (KFP) or TensorFlow Extended (TFX) SDKs.16 |
| **DIY Vector Storage** | **Vertex AI Vector Search** | The underlying "engine block".1 This is the high-scale, low-latency approximate nearest neighbor (ANN) service (formerly Matching Engine) used to build custom semantic search from scratch.9 |
| **Managed RAG App** | **Vertex AI Search** | The "fully-assembled car".1 A managed service to build a "Google-quality search app" 3 with "out-of-the-box RAG" capabilities.2 |
| **Custom RAG Framework** | **Vertex AI RAG Engine** | The "customizable chassis".1 A managed service to *build and deploy* RAG implementations, providing control over parsing, chunking, and retrieval components.6 **This is the core component for this project.** |
| **Agentic Framework** | **Vertex AI Agent Builder** | A "full-stack" platform for building, scaling, and governing multi-step, enterprise-grade AI agents.2 It can orchestrate multiple tools, including custom RAG systems.19 |

## **Part 2: The Core Blueprint: Building Your Custom RAG System**

This section provides a complete, step-by-step implementation guide for building the RAG system using the recommended Vertex AI RAG Engine, based on the official quickstart documentation.11

### **Step 2.1: Environment Setup and Authentication**

First, the local environment must be configured with the necessary Python libraries and Google Cloud credentials.

1. **Install the Vertex AI SDK:** The google-cloud-aiplatform library contains the modules for interacting with the RAG Engine.  
   Bash  
   pip install google-cloud-aiplatform

2. **Authenticate for Application Default Credentials (ADC):** This is a critical step. The Vertex AI SDK (like other Google Cloud libraries) automatically finds credentials using a strategy called Application Default Credentials (ADC).20  
   * **The Common "Gotcha":** Running gcloud auth login *only* authenticates the gcloud CLI tool itself. It does *not* create the ADC file that Python libraries look for.21  
   * **The Correct Command:** Use gcloud auth application-default login. This command generates a JSON credential file in a well-known location on your filesystem (e.g., $HOME/.config/gcloud/application\_default\_credentials.json), which the Python SDK will automatically detect and use.20

Bash  
gcloud auth application-default login

3. **Grant IAM Roles:** For the setup phase, the user account needs permissions to create resources. These commands grant the necessary roles to your user account.  
   Bash  
   \# (Replace with your project ID and email)  
   export PROJECT\_ID="your-project-id"  
   export USER\_EMAIL="your-email@example.com"

   \# Grants permissions to use Vertex AI services  
   gcloud projects add-iam-policy-binding $PROJECT\_ID \\  
       \--member="user:$USER\_EMAIL" \\  
       \--role="roles/aiplatform.user"

   \# Grants permissions to read/write to GCS buckets  
   gcloud projects add-iam-policy-binding $PROJECT\_ID \\  
       \--member="user:$USER\_EMAIL" \\  
       \--role="roles/storage.objectAdmin"

   The roles/aiplatform.user role is required by the RAG quickstart 11, and roles/storage.objectAdmin is needed to upload the research files.23

### **Step 2.2: Data Ingestion (Your Research Corpus)**

This step physically manifests the "Data Sovereignty" requirement. The research documents will be stored in a standard GCS bucket under your full control.

1. **Create a GCS Bucket:**  
   Bash  
   \# (Replace with your project ID, location, and a unique bucket name)  
   export LOCATION="us-central1"  
   export BUCKET\_NAME="your-private-research-bucket"

   gsutil mb \-p $PROJECT\_ID \-l $LOCATION gs://$BUCKET\_NAME

2. **Upload Your Research Documents:**  
   Bash  
   \# (Upload one or more files from your local machine)  
   gsutil cp /path/to/local/research-paper-01.pdf gs://$BUCKET\_NAME/  
   gsutil cp /path/to/local/research-paper-02.docx gs://$BUCKET\_NAME/

### **Step 2.3: Building the RagCorpus (The Indexing)**

With the data in GCS, the next step is to create a RagCorpus. This Python script initializes the RAG Engine, defines the embedding model, and instructs the engine to ingest, parse, chunk, and embed the documents from the GCS bucket.

Python

import vertexai  
from vertexai import rag  
from vertexai.generative\_models import GenerativeModel, Tool

\# \--- 1\. Initialization \---  
\# (Update with your project details)  
PROJECT\_ID \= "your-project-id"  
LOCATION \= "us-central1"  \# Note: RAG Engine is regional   
GCS\_BUCKET\_URI \= "gs://your-private-research-bucket" \# From Step 2.2

\# Initialize the Vertex AI SDK  
vertexai.init(project=PROJECT\_ID, location=LOCATION)

\# \--- 2\. Configure and Create the RagCorpus \---  
print("Creating RagCorpus...")

\# Configure the embedding model to use, e.g., text-embedding-005  
embedding\_model\_config \= rag.RagEmbeddingModelConfig(  
    vertex\_prediction\_endpoint=rag.VertexPredictionEndpoint(  
        publisher\_model="publishers/google/models/text-embedding-005"  
    )  
)

\# Create the corpus. This provisions the underlying vector database.  
\# This operation returns a long-running operation (LRO).  
create\_corpus\_lro \= rag.create\_corpus(  
    display\_name="Private Research Corpus",  
    backend\_config=rag.RagVectorDbConfig(  
        rag\_embedding\_model\_config=embedding\_model\_config  
    ),  
)

\# Wait for the corpus to be created  
rag\_corpus \= create\_corpus\_lro.result()  
corpus\_name \= rag\_corpus.name  
print(f"Created RagCorpus: {corpus\_name}")

\# \--- 3\. Import Files and Run Indexing \---  
print(f"Importing files from {GCS\_BUCKET\_URI}...")

\# This call ingests, parses, chunks, and embeds your documents.  
\# This is where you can fine-tune parsing and chunking.  
import\_files\_lro \= rag.import\_files(  
    rag\_corpus.name,  
   ,  
    transformation\_config=rag.TransformationConfig(  
        chunking\_config=rag.ChunkingConfig(  
            chunk\_size=1024,     \# Size of each text chunk  
            chunk\_overlap=200,   \# Overlap between chunks  
        ),  
    ),  
    max\_embedding\_requests\_per\_min=1000,  
)

\# Wait for the import to complete  
import\_files\_lro.result()  
print("File import and indexing complete.")

### **Step 2.4: Querying (The RagRetrievalTool)**

This is the final and most important script. It demonstrates the modern, "tool-based" approach to RAG. Instead of building a complex, manual chain, the RagCorpus is simply exposed to the Gemini model as a RagRetrievalTool. The model itself will then intelligently decide when to call this tool to retrieve context to answer a query.

This script (saved as query\_research.py) forms the core of the final CLI tool.

Python

import vertexai  
from vertexai import rag  
from vertexai.generative\_models import GenerativeModel, Tool  
import sys

\# \--- 1\. Initialization \---  
PROJECT\_ID \= "your-project-id"  
LOCATION \= "us-central1"  
\#\!\! IMPORTANT: Use the corpus\_name from the output of the Step 2.3 script  
CORPUS\_NAME \= "projects/YOUR\_PROJECT\_NUMBER/locations/us-central1/ragCorpora/YOUR\_CORPUS\_ID"

vertexai.init(project=PROJECT\_ID, location=LOCATION)

\# \--- 2\. Create the RAG Retrieval Tool \---  
\# Point the tool directly to the RagCorpus created previously   
rag\_retrieval\_tool \= Tool.from\_retrieval(  
    retrieval=rag.Retrieval(  
        source=rag.VertexRagStore(  
            rag\_resources=  
        )  
    )  
)

\# \--- 3\. Initialize the Generative Model \---  
\# Pass the RAG tool to the model upon initialization   
model \= GenerativeModel(  
    model\_name="gemini-2.5-pro",  \# Or other supported models \[24\]  
    tools=\[rag\_retrieval\_tool\]  
)

\# \--- 4\. Define Main Query Function \---  
def execute\_grounded\_query(query\_text):  
    """  
    Sends the query to the Gemini model. The model will automatically  
    execute the rag\_retrieval\_tool, get grounded context, and  
    synthesize a final answer.  
    """  
    print("Sending grounded query...")  
    response \= model.generate\_content(query\_text)  
    return response.text

\# \--- 5\. CLI Execution Logic \---  
if \_\_name\_\_ \== "\_\_main\_\_":  
    if len(sys.argv) \> 1:  
        \# Combine all command-line arguments into a single query string  
        query \= " ".join(sys.argv\[1:\])  
          
        \# Get the grounded answer  
        answer \= execute\_grounded\_query(query)  
        print("\\n--- Answer \---\\n")  
        print(answer)  
    else:  
        print("Usage: python query\_research.py")

This script directly fulfills the project's SELF-TEST conditions. A question about the research papers will trigger the rag\_retrieval\_tool and return a grounded answer. An off-topic question (e.g., "What is the capital of France?") will not trigger the tool, and the model will answer from its general-purpose knowledge.

### **Step 2.5: A Note on LangChain**

As a proficient developer, a natural inclination might be to use an orchestration framework like LangChain. However, this path must be chosen carefully.

The popular langchain-google-vertexai package 25 provides a VertexAISearchRetriever.26 This retriever is designed to work with **Vertex AI Search** ("the car"), not the **Vertex AI RAG Engine** ("the chassis").1

While LangChain integration with the RAG Engine is possible 29, the native vertexai.rag.Tool.from\_retrieval method shown in Step 2.4 11 is the most direct, SDK-supported, and robust method for integrating a RagCorpus with a Gemini model. For this project's defined goal, the native SDK is the superior and simpler path.

## **Part 3: The CLI-First Workflow: Accessing Your RAG System**

This section bridges the gap from a Python script to a seamless, CLI-first workflow.

### **Step 3.1: Connecting the *Standard* gemini-cli to Vertex AI**

For general, *un-grounded* queries, the official gemini-cli tool 30 can be pointed to your Vertex AI project. This provides enterprise-grade security, higher rate limits, and integration with your Google Cloud infrastructure.30

This requires the gcloud auth application-default login to be run (as in Step 2.1) and two environment variables:

Bash

\# Authenticate for ADC (if not already done)  
gcloud auth application-default login

\# Set environment variables for gemini-cli  
export GOOGLE\_GENAI\_USE\_VERTEXAI=true   
export GOOGLE\_CLOUD\_PROJECT="your-project-id"

\# Test a standard, non-RAG query  
gemini "What is the capital of France?"  
\# This query is now routed through your Vertex AI project endpoint \[30, 31\]

### **Step 3.2: The "Integration Gap" and Custom CLI Solution**

A critical clarification is necessary: The official gemini-cli **cannot** natively use the Python-based RagRetrievalTool built in Part 2\. The gemini-cli's tool system is built on a different protocol (MCP, Model Context Protocol) for custom extensions.30

Therefore, to achieve the "Gemini CLI for your research" goal, we must create a *new, custom CLI wrapper* around the query\_research.py script from Step 2.4.

### **Step 3.3: Implementation Strategy 1 (Simple): The Bash Function**

The fastest and most direct method is to create a bash function that executes the Python script.

1. Ensure the query\_research.py script from Step 2.4 is saved in a permanent location (e.g., $HOME/scripts/query\_research.py) and is executable.  
2. Add the following function to your \~/.bashrc or \~/.zshrc file 32:  
   Bash  
   \# Defines a new shell command 'query\_research'  
   \# This function passes all its arguments ("$@")  
   \# directly to the python script.\[33\]  
   query\_research() {  
       \# (Ensure this path points to the Python venv  
       \#  where google-cloud-aiplatform is installed)  
       /path/to/your/venv/bin/python $HOME/scripts/query\_research.py "$@"  
   }

3. Reload your shell: source \~/.bashrc  
4. **Test:** You can now query your private RAG system from anywhere in your terminal.  
   Bash  
   query\_research "What was the key finding in the 2024 paper on mitochondrial efficiency?"

### **Step 3.4: Implementation Strategy 2 (Robust): The Packaged Python CLI**

For a more robust, "production-ready" tool that can be versioned and distributed, the script can be packaged as a proper Python CLI application using a pyproject.toml file.34

1. **Project Structure** 35:  
   research\_cli/  
   ├── pyproject.toml  
   └── research\_cli/  
       ├── \_\_init\_\_.py  
       └── main.py

2. pyproject.toml 34:  
   This file defines the project and creates the command-line script.  
   Ini, TOML  
   \[project\]  
   name \= "research\_cli"  
   version \= "0.1.0"  
   dependencies \= \[  
       "google-cloud-aiplatform",  
       "click"  \# Using the 'click' library for easier CLI parsing 

   \[project.scripts\]  
   \# This creates a shell command 'query\_research' that calls  
   \# the 'cli' function in the 'research\_cli.main' module.  
   query\_research \= "research\_cli.main:cli"

3. research\_cli/main.py:  
   This file contains the logic from Step 2.4, adapted for the click library.36  
   Python  
   import click  
   import vertexai  
   from vertexai import rag  
   from vertexai.generative\_models import GenerativeModel, Tool

   \# \--- 1\. Initialization (Hardcode or pull from env) \---  
   PROJECT\_ID \= "your-project-id"  
   LOCATION \= "us-central1"  
   CORPUS\_NAME \= "projects/YOUR\_PROJECT\_NUMBER/locations/us-central1/ragCorpora/YOUR\_CORPUS\_ID"

   vertexai.init(project=PROJECT\_ID, location=LOCATION)

   \# \--- 2\. Create Tool and Model (as in Step 2.4) \---  
   rag\_retrieval\_tool \= Tool.from\_retrieval(  
       retrieval=rag.Retrieval(  
           source=rag.VertexRagStore(  
               rag\_resources=  
           )  
       )  
   )  
   model \= GenerativeModel(  
       model\_name="gemini-2.5-pro",  
       tools=\[rag\_retrieval\_tool\]  
   )

   \# \--- 3\. Define Click CLI Command \---  
   @click.command()  
   @click.argument('query\_text', nargs=-1) \# Accepts a variable-length query  
   def cli(query\_text):  
       """Queries your private research RAG on Vertex AI."""  
       if not query\_text:  
           click.echo("Usage: query\_research")  
           return

       query \= " ".join(query\_text)  
       click.echo("Sending grounded query...")  
       response \= model.generate\_content(query)  
       click.echo("\\n--- Answer \---\\n")  
       click.echo(response.text)

   if \_\_name\_\_ \== "\_\_main\_\_":  
       cli()

4. Installation:  
   From within the root research\_cli/ directory, install the package.  
   Bash  
   pip install \-e.

5. **Test:** A robust, system-wide CLI command is now available.  
   Bash  
   query\_research "What was the key finding in my 2024 paper?"

## **Part 4: From Tool to System: Enterprise Automation and Security**

The final phase transforms the developer tool into a robust, automated, and secure enterprise system.

### **Step 4.1: Automation: The Automatic Re-indexing Pipeline**

A RAG system's knowledge can become "stale." An automated MLOps process is required to re-index the corpus whenever new research is added.37 The most robust, serverless architecture for this is: **GCS \-\> Eventarc \-\> Vertex AI Pipelines**.

1. **The Event (GCS):** A new file (e.g., new-paper.pdf) is uploaded to the gs://your-private-research-bucket/ bucket.  
2. **The Trigger (Eventarc):** An Eventarc trigger is configured to listen for the google.cloud.storage.object.v1.finalized event from that specific bucket.38  
3. **The Action (Vertex AI Pipelines):** The Eventarc trigger will invoke a Vertex AI Pipeline.40 This pipeline will be a simple, one-step component (defined via KFP) that runs a container. This container will execute a Python script that calls rag.import\_files(CORPUS\_NAME, \[event.data.file\_path\]), dynamically adding the new paper to the existing RagCorpus.

This event-driven architecture 41 ensures the research RAG system is always synchronized with the latest documents, with no manual intervention required.

### **Step 4.2: Security: Least-Privilege IAM for Querying**

The roles/aiplatform.user role used for setup is too permissive for a production service.11 It grants broad permissions to create, delete, and modify resources. For a production CLI tool or backend service, a custom IAM role with least-privilege permissions is required.42

A custom role, RagQueryOnly, should be created and assigned to a dedicated service account. This role needs only the permissions to find the RagCorpus and invoke the model for a prediction.

**Custom IAM Role: RagQueryOnly**

| Permission | Justification | Source |
| :---- | :---- | :---- |
| aiplatform.ragCorpora.get | Allows the service to find and retrieve the RagCorpus resource by name. | 44 |
| aiplatform.endpoints.predict | Allows the service to call the underlying Gemini model endpoint to generate the final response. The RAG tool ultimately calls this. | 45 |

This minimal set of permissions 42 ensures the service account can *only* execute queries, fulfilling the principle of least privilege and enhancing the system's security posture.

### **Step 4.3: Expansion: The RAG-Powered Agent**

This custom RAG system is not an endpoint, but a modular component. The next logical step is to use this system as a "tool" within **Vertex AI Agent Builder**.2

Agent Builder is designed to orchestrate complex, multi-step tasks using multiple tools.19 By registering the RAG system as a custom tool 2, a more advanced agent can be built.

Example Use Case:  
An agent could be prompted: "Compare the findings in my 2024 paper on 'X' with the latest public research on Google Search."  
This agent would then execute a multi-step plan:

1. **Call Tool 1 (Custom RAG Tool):** Queries the RagCorpus to retrieve grounded information on the 2024 paper.  
2. **Call Tool 2 (Built-in Google Search Tool):** Queries Google Search for the latest public research on "X".19  
3. **Synthesize:** The Gemini model receives the context from *both* tools and generates a novel, comprehensive answer that compares the private, sovereign data with public, real-time data.

This demonstrates the true power of the Vertex AI ecosystem: building modular, specialized tools that can be composed into sophisticated, agentic systems.

#### **Works cited**

1. The GCP RAG Spectrum: Vertex AI Search, RAG Engine, and Vector Search — Which one should you use? | by Saurabh Pandey | Google Cloud \- Medium, accessed on November 7, 2025, [https://medium.com/google-cloud/the-gcp-rag-spectrum-vertex-ai-search-rag-engine-and-vector-search-which-one-should-you-use-f56d50720d5a](https://medium.com/google-cloud/the-gcp-rag-spectrum-vertex-ai-search-rag-engine-and-vector-search-which-one-should-you-use-f56d50720d5a)  
2. Vertex AI Agent Builder | Google Cloud, accessed on November 7, 2025, [https://cloud.google.com/products/agent-builder](https://cloud.google.com/products/agent-builder)  
3. What is Vertex AI Search? | Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction)  
4. Vertex AI Search pricing \- Google Cloud, accessed on November 7, 2025, [https://cloud.google.com/generative-ai-app-builder/pricing](https://cloud.google.com/generative-ai-app-builder/pricing)  
5. Vertex AI RAG Engine overview \- Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)  
6. Vertex AI RAG Engine: Build & deploy RAG implementations with ..., accessed on November 7, 2025, [https://cloud.google.com/blog/products/ai-machine-learning/introducing-vertex-ai-rag-engine](https://cloud.google.com/blog/products/ai-machine-learning/introducing-vertex-ai-rag-engine)  
7. Vertex AI RAG Engine billing \- Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-engine-billing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-engine-billing)  
8. Vertex AI RAG Engine: A developers tool, accessed on November 7, 2025, [https://developers.googleblog.com/en/vertex-ai-rag-engine-a-developers-tool/](https://developers.googleblog.com/en/vertex-ai-rag-engine-a-developers-tool/)  
9. Google Vertex AI Vector Search \- Docs by LangChain, accessed on November 7, 2025, [https://docs.langchain.com/oss/python/integrations/vectorstores/google\_vertex\_ai\_vector\_search](https://docs.langchain.com/oss/python/integrations/vectorstores/google_vertex_ai_vector_search)  
10. Vector Search | Vertex AI | Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)  
11. RAG quickstart | Generative AI on Vertex AI \- Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-quickstart)  
12. Vertex AI Platform | Google Cloud, accessed on November 7, 2025, [https://cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai)  
13. Overview of Model Garden | Generative AI on Vertex AI | Google ..., accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)  
14. Vector Search quickstart | Vertex AI \- Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/docs/vector-search/quickstart](https://docs.cloud.google.com/vertex-ai/docs/vector-search/quickstart)  
15. Intro to Vertex Pipelines \- Google Codelabs, accessed on November 7, 2025, [https://codelabs.developers.google.com/vertex-pipelines-intro](https://codelabs.developers.google.com/vertex-pipelines-intro)  
16. Build a pipeline | Vertex AI | Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/docs/pipelines/build-pipeline](https://docs.cloud.google.com/vertex-ai/docs/pipelines/build-pipeline)  
17. MLOps on Vertex AI \- Google Cloud, accessed on November 7, 2025, [https://cloud.google.com/vertex-ai/docs/start/introduction-mlops](https://cloud.google.com/vertex-ai/docs/start/introduction-mlops)  
18. More ways to build and scale AI agents with Vertex AI Agent Builder | Google Cloud Blog, accessed on November 7, 2025, [https://cloud.google.com/blog/products/ai-machine-learning/more-ways-to-build-and-scale-ai-agents-with-vertex-ai-agent-builder](https://cloud.google.com/blog/products/ai-machine-learning/more-ways-to-build-and-scale-ai-agents-with-vertex-ai-agent-builder)  
19. Vertex AI Agent Builder overview | Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/agent-builder/overview](https://docs.cloud.google.com/agent-builder/overview)  
20. How Application Default Credentials works | Authentication, accessed on November 7, 2025, [https://docs.cloud.google.com/docs/authentication/application-default-credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials)  
21. Authenticate for using the gcloud CLI, accessed on November 7, 2025, [https://docs.cloud.google.com/docs/authentication/gcloud](https://docs.cloud.google.com/docs/authentication/gcloud)  
22. Best Practice: Set Up gcloud auth and Application Default Credentials (ADC), accessed on November 7, 2025, [https://dev.to/jajera/best-practice-set-up-gcloud-auth-and-application-default-credentials-adc-3dhk](https://dev.to/jajera/best-practice-set-up-gcloud-auth-and-application-default-credentials-adc-3dhk)  
23. Building Vertex AI RAG Engine with Gemini 2 Flash LLM | by Arjun Prabhulal | Google Cloud, accessed on November 7, 2025, [https://medium.com/google-cloud/building-vertex-ai-rag-engine-with-gemini-2-flash-llm-79c27445dd48](https://medium.com/google-cloud/building-vertex-ai-rag-engine-with-gemini-2-flash-llm-79c27445dd48)  
24. Google \- Docs by LangChain, accessed on November 7, 2025, [https://docs.langchain.com/oss/python/integrations/providers/google](https://docs.langchain.com/oss/python/integrations/providers/google)  
25. Google Vertex AI Search \- Docs by LangChain, accessed on November 7, 2025, [https://docs.langchain.com/oss/python/integrations/retrievers/google\_vertex\_ai\_search](https://docs.langchain.com/oss/python/integrations/retrievers/google_vertex_ai_search)  
26. Google Vertex AI Search | 🦜️ LangChain, accessed on November 7, 2025, [https://python.langchain.com/docs/integrations/retrievers/google\_vertex\_ai\_search/](https://python.langchain.com/docs/integrations/retrievers/google_vertex_ai_search/)  
27. Building a Powerful GCP RAG System with LangChain, Vertex AI, and Ensemble Retrieval, accessed on November 7, 2025, [https://blog.dtdl.in/building-a-powerful-gcp-rag-system-with-langchain-vertex-ai-and-ensemble-retrieval-5bc53dbd4c20](https://blog.dtdl.in/building-a-powerful-gcp-rag-system-with-langchain-vertex-ai-and-ensemble-retrieval-5bc53dbd4c20)  
28. Problems With Rag Engine \- Custom ML & MLOps \- Google Developer forums, accessed on November 7, 2025, [https://discuss.google.dev/t/problems-with-rag-engine/192095](https://discuss.google.dev/t/problems-with-rag-engine/192095)  
29. google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal. \- GitHub, accessed on November 7, 2025, [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
30. How to create a custom alias to run a python script with a parameter? \- Reddit, accessed on November 7, 2025, [https://www.reddit.com/r/learnpython/comments/r40lhl/how\_to\_create\_a\_custom\_alias\_to\_run\_a\_python/](https://www.reddit.com/r/learnpython/comments/r40lhl/how_to_create_a_custom_alias_to_run_a_python/)  
31. How can I create a command line tool and execute it like a script in Python \- Reddit, accessed on November 7, 2025, [https://www.reddit.com/r/learnpython/comments/182cdyz/how\_can\_i\_create\_a\_command\_line\_tool\_and\_execute/](https://www.reddit.com/r/learnpython/comments/182cdyz/how_can_i_create_a_command_line_tool_and_execute/)  
32. The easy (and nice) way to do CLI apps in Python | Thomas Stringer, accessed on November 7, 2025, [https://trstringer.com/easy-and-nice-python-cli/](https://trstringer.com/easy-and-nice-python-cli/)  
33. Let's Create A CLI With Python — Part 1 | by Stav Shamir \- Medium, accessed on November 7, 2025, [https://medium.com/@shamir.stav\_83310/lets-create-a-cli-with-python-part-1-ae4fe9e0258b](https://medium.com/@shamir.stav_83310/lets-create-a-cli-with-python-part-1-ae4fe9e0258b)  
34. How to Update Vector Count for an Existing Index in Vertex AI? \- Stack Overflow, accessed on November 7, 2025, [https://stackoverflow.com/questions/78006902/how-to-update-vector-count-for-an-existing-index-in-vertex-ai](https://stackoverflow.com/questions/78006902/how-to-update-vector-count-for-an-existing-index-in-vertex-ai)  
35. Trigger functions from Cloud Storage using Eventarc | Cloud Run, accessed on November 7, 2025, [https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage)  
36. Introducing Eventarc triggers for Workflows | Google Cloud Blog, accessed on November 7, 2025, [https://cloud.google.com/blog/topics/developers-practitioners/introducing-eventarc-triggers-workflows](https://cloud.google.com/blog/topics/developers-practitioners/introducing-eventarc-triggers-workflows)  
37. Trigger a pipeline run with Pub/Sub | Vertex AI \- Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/docs/pipelines/trigger-pubsub](https://docs.cloud.google.com/vertex-ai/docs/pipelines/trigger-pubsub)  
38. Using remote and event-triggered AI Platform Pipelines | Google Cloud Blog, accessed on November 7, 2025, [https://cloud.google.com/blog/products/ai-machine-learning/using-remote-and-event-triggered-ai-platform-pipelines](https://cloud.google.com/blog/products/ai-machine-learning/using-remote-and-event-triggered-ai-platform-pipelines)  
39. Vertex AI access control with IAM | Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/vertex-ai/docs/general/access-control](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)  
40. Access control | Generative AI on Vertex AI \- Google Cloud, accessed on November 7, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/access-control](https://cloud.google.com/vertex-ai/generative-ai/docs/access-control)  
41. Package google.cloud.aiplatform.v1beta1 | Generative AI on Vertex AI, accessed on November 7, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc/google.cloud.aiplatform.v1beta1)  
42. Vertex AI roles and permissions | Identity and Access Management (IAM) | Google Cloud Documentation, accessed on November 7, 2025, [https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform)