# **Lexical Cartography: Mining, Mapping & Discovering Design Pattern Lexicons Across Domains**

## **1\. The Epistemology of Design Pattern Cartography**

The practice of design, whether manifested in the tectonic arrangement of masonry or the ephemeral choreography of user interface transitions, is fundamentally linguistic. Designers do not solve problems *ex nihilo*; they employ a vocabulary of recurring solutions—patterns—that encode centuries of trial, error, and refinement. However, this vast repository of design wisdom is currently fragmented. It exists in a state of semantic entropy, locked within disparate corpora: the static PDFs of architectural treatises, the README files of software repositories, the HTML of UX case studies, and the tacit knowledge of practitioners. The challenge of the Computational Pattern Cartographer is not merely to catalogue these patterns but to engineer a system capable of *Lexical Cartography*—a computational framework that mines, synthesizes, and maps the latent lexicon of design across domains.

This report details the theoretical architecture and execution strategy for such a system. It aims to bridge the "Tower of Babel" effect where identical concepts bear different names across disciplines (e.g., the structural "Bridge" in architecture versus the "Bridge" pattern in Object-Oriented Programming) and where distinct concepts share homonymic labels. By leveraging advanced Natural Language Processing (NLP), semantic role labeling (SRL), and ontology learning, we propose a semantic engine capable of extracting not just explicit patterns, but latent design metaphors and emerging affordances.1 This system serves as a foundational substrate for "Design Memory Networks" and "Generative Design Agents," transforming static libraries into a living, evolving intelligence.3

### **1.1 The Theoretical Lineage: From Alexander to Algorithms**

The ontological foundation of this system rests on the seminal work of Christopher Alexander. In *A Pattern Language*, Alexander posited that patterns are the "atoms" of environmental structure, each consisting of a specific context, a recurring problem, and a core solution.5 This definition provides the essential scaffolding for our computational model: a pattern is not a *thing* but a *relationship* between forces.

In the software domain, the "Gang of Four" (GoF) adapted this to software engineering, codifying solutions like *Singleton* and *Observer*.6 However, a critical divergence occurred: architectural patterns remained phenomenological and human-centric, while software patterns became formal and logical. UX patterns later emerged as a hybrid, blending the functional logic of software with the cognitive affordances of architecture.8

Current computational approaches often fail to reconcile these divergent descriptive modes. A simple keyword search for "Facade" returns incompatible results: a Java class wrapping a subsystem 7 and a building's frontage.10 To construct a true multi-domain lexicon, the system must transcend keyword matching and operate at the level of *semiotic function*—identifying patterns based on the structural roles they play (e.g., "mediation," "separation," "optimization") rather than their surface nomenclature.11

### **1.2 The Semiotic Triad in Computational Extraction**

To automate the discovery of patterns, we operationalize the semiotic definition of a design pattern into three detectable components:

1. **The Context (The "When"):** The preconditions or environment in which the pattern is valid (e.g., "In a distributed system..." or "When designing a dense urban cluster...").  
2. **The Problem (The "Why"):** The conflicting forces or constraints (e.g., "coupling is too high" or "pedestrians lack shade").  
3. **The Solution (The "How"):** The configuration that resolves the forces (e.g., "introduce an abstraction layer" or "build an arcade").

Our extraction pipeline utilizes **Semantic Role Labeling (SRL)** to identify these components within unstructured text. By parsing sentences into thematic roles—Agent (the pattern), Theme (the elements acting), and Goal (the resolution)—we can algorithmically reconstruct the Alexandrian triplet from raw text.13 This allows the system to recognize that a "Load Balancer" in cloud computing and a "Foyer" in a theater perform the structurally identical function of *managing flow rate before a capacity-constrained resource*.

## ---

**2\. Corpus Ingestion and Contextual Engineering**

The first operational layer of the Lexical Cartography system is the **Corpus Ingestion Layer**. This component is responsible for aggregating, normalizing, and embedding diverse design artifacts. The heterogeneity of the input data—ranging from academic LaTeX documents to informal GitHub discussions—requires a robust, multi-modal ingestion strategy.1

### **2.1 Multi-Modal Data Aggregation**

The system must ingest three primary categories of data, each requiring distinct extraction methodologies:

**Table 1: Corpus Data Typologies and Ingestion Strategies**

| Data Source | Format Characteristics | Ingestion Strategy | Key Challenges |
| :---- | :---- | :---- | :---- |
| **Academic Corpora** (arXiv, IEEE) | Structured PDFs, formal language, dense citations. | **NLP Workbench**: PDF parsing, citation graph extraction, section segmentation (Abstract, Method, Conclusion).1 | Handling multi-column layouts; distinguishing prescriptive patterns from descriptive analysis. |
| **Code Repositories** (GitHub) | Source code, comments, READMEs (Markdown). | **AST Parsing & Doc Mining**: Extracting class structures; mining READMEs for "Problem/Solution" headers.16 | Linking abstract descriptions in READMEs to concrete implementations in code. |
| **UX Case Studies** (Blogs, Portfolios) | HTML, informal narrative, image-heavy. | **DOM Scraping & Visual OCR**: Extracting text from DOM; using OCR on UI screenshots to identify labeled components.18 | High noise-to-signal ratio; distinguishing marketing copy from design rationale. |

### **2.2 Text Preprocessing and Normalization**

Once raw text is extracted, it undergoes rigorous preprocessing to reduce noise and standardize the input for the embedding models.

* **Tokenization and Lemmatization:** Utilizing libraries such as spaCy or NLTK, the system breaks text into tokens and reduces them to their root forms (lemmas). This ensures that "optimizing," "optimization," and "optimized" are treated as the same semantic concept.20  
* **Stop-Word and Stop-Phrase Removal:** Beyond standard stop words (e.g., "the," "and"), domain-specific stop phrases must be filtered. In design corpora, phrases like "cutting-edge solution" or "user-centric approach" are often marketing fluff that dilutes the extraction of functional patterns. We employ TF-IDF (Term Frequency-Inverse Document Frequency) to identify and down-weight these ubiquitous but low-information terms.22  
* **Section Segmentation:** Pattern descriptions often follow a specific rhetorical structure. The system utilizes heuristic rules and machine learning classifiers to segment documents into "Problem," "Context," and "Solution" zones. For example, paragraphs following headers like "Challenges" or "Pain Points" are tagged as *Problem Space*, while those following "Implementation" or "Design" are tagged as *Solution Space*.23

### **2.3 Contextual Embedding and Vectorization**

The core of the ingestion layer is the transformation of text into high-dimensional vector space. We move beyond simple "Bag of Words" models 22 to **Contextual Embeddings** using Large Language Models (LLMs) such as BERT or GPT-4.3

* **Transformer-Based Encodings:** Unlike static embeddings (e.g., Word2Vec), transformer models capture the context of a word. This is crucial for disambiguation. The vector for "Stream" in the context of "Java Stream API" will be mathematically distinct from "Stream" in "Urban Water Stream," allowing the system to separate software patterns from landscape architecture patterns immediately.25  
* **Document Concept Vectors:** To further refine the representation, we generate Document Concept Vectors.26 This technique leverages external knowledge bases (like Wikipedia or specialized design ontologies) to enrich the text. If a document mentions "Factory," "Builder," and "Singleton," the Concept Vector enriches the representation with the meta-concept "Creational Patterns," even if that term is not explicitly present.26

## ---

**3\. The Extraction Engine: NLP & Semiotics**

The **Pattern Extraction Pipeline** is the analytical heart of the system. It processes the prepared embeddings to identify, isolate, and classify design patterns. This engine employs a hybrid approach combining unsupervised clustering for discovery and supervised classification for categorization.

### **3.1 Unsupervised Pattern Discovery via LDA and Clustering**

To discover *emergent* patterns—those that have not yet been named—the system employs unsupervised learning techniques.

* **Latent Dirichlet Allocation (LDA):** We utilize LDA for topic modeling across the corpus. LDA assumes that each document is a mixture of topics and each topic is a mixture of words.25 By analyzing millions of design documents, LDA reveals clusters of co-occurring terms (e.g., "modal," "overlay," "dismiss," "background"). These clusters represent latent patterns.  
* **Pattern Frequency and Saliency:** The system calculates a Saliency Matrix based on the frequency and distinctiveness of these clusters.22 A cluster that appears frequently across diverse documents (high frequency) but contains specific, technical vocabulary (high distinctiveness) is a strong candidate for a design pattern.

### **3.2 Semantic Role Labeling (SRL) for Structure Extraction**

While LDA identifies *themes*, it cannot understand *structure*. To extract the "Problem-Solution" scaffolding, we employ **Semantic Role Labeling (SRL)**.13

* **The "TakeFive" Algorithm:** Drawing on the "TakeFive" method, the system transforms text into a frame-oriented knowledge graph. It parses sentences to identify the *predicate* (the action) and its *arguments* (the roles).13  
* **FrameNet Integration:** The system maps these arguments to FrameNet frames. For instance, a sentence describing the *Observer* pattern might be mapped to a Notification frame:  
  * **Agent (Sender):** The Subject (e.g., "The Subject object").  
  * **Action:** "Notifies".  
  * **Theme (Message):** "State change".  
  * Beneficiary (Receiver): "Dependent Observers".  
    By standardizing these roles, the system can compare the Observer pattern in software to a "Signal-Slot" mechanism in industrial design, verifying if they share the same semantic frame.29

### **3.3 Contrastive Learning for Signal Isolation**

Design texts are noisy, often mixing pattern definitions with general narrative. To isolate the pattern itself, the system uses **Contrastive Learning**.30

* **Mechanism:** The model is trained to minimize the distance between positive pairs (e.g., a formal definition of "MVC" and a code example of "MVC") and maximize the distance between negative pairs (e.g., "MVC" and a general discussion of "web development").30  
* **Application:** This technique creates a "Pattern Space" within the vector embedding. In this space, valid pattern descriptions cluster tightly together, separated from the diffuse cloud of general design commentary. This significantly improves the precision of extraction, ensuring that the system captures the *definition* of the pattern, not just mentions of it.31

### **3.4 Mining Affordances for Latent Discovery**

A key innovation of this DRP is the mining of **Affordances**—the action possibilities latent in an object.32 Many design solutions exist as "proto-patterns": functional behaviors that are widely used but unnamed.

* **Affordance Extraction:** The system scans for "Object $\\rightarrow$ Affordance" tuples (e.g., "Card $\\rightarrow$ Swipeable," "Header $\\rightarrow$ Sticky"). It utilizes dependency parsing to find Subject-Verb relationships where the verb indicates capability (e.g., "allows," "enables," "provides").29  
* **The Affordance of Absence:** A subtle but powerful class of patterns involves the deliberate *removal* of features (e.g., "White Space" or "Minimalism"). The system identifies "Affordance of Absence" by detecting negative constraints (e.g., "removes clutter," "hides details," "prevents error").34 This allows the system to codify "Negative Patterns" or "Constraint Patterns" that are crucial for safety-critical and minimalist design domains.

## ---

**4\. Ontological Scaffolding and Lexicon Builder**

The extracted patterns must be organized into a coherent, machine-readable structure. The **Lexicon Builder** organizes these patterns into a formal ontology, resolving the polysemy and synonymy issues identified in Section 1\.

### **4.1 The Three-Layer Ontology Model**

To manage the complexity of cross-domain knowledge, we adopt a **Three-Layer Ontology Design**.36 This structure allows for both high-level abstraction and low-level specificity.

**Table 2: The Three-Layer Ontology Architecture**

| Layer | Function | content | Example (Pattern: "Container") |
| :---- | :---- | :---- | :---- |
| **1\. Primitive Layer** | Taxonomy of atomic domain terms. | Raw vocabulary, simple hierarchy (is-a). | class, div, room, box. |
| **2\. Complex Layer** | Meta-patterns and semantic definitions. | Necessary & sufficient conditions; logical constraints. | Container: An entity that holds other entities and constrains their position. |
| **3\. Application Layer** | Domain-specific implementations. | Code snippets, specific material constraints, platform rules. | Docker Container (Software), Flexbox (CSS), Storage Unit (Industrial Design). |

### **4.2 JSON-LD and Linked Data Specifications**

To ensure the lexicon is interoperable with the Semantic Web and generative AI agents, the system outputs data in **JSON-LD (JavaScript Object Notation for Linked Data)**.37

* **Context (@context):** Each pattern definition includes a reference to standard vocabularies (e.g., Schema.org, Dublin Core). This maps local terms to global identifiers. For instance, problem in our lexicon is mapped to schema:Question or schema:Challenge, ensuring that a machine reading the data understands the semantic weight of the field.39  
* **Universal Identifiers (@id):** Every pattern is assigned a unique IRI (Internationalized Resource Identifier). This solves the homonym problem. The software "Bridge" pattern gets http://lexicon.design/software/Bridge, while the architectural "Bridge" gets http://lexicon.design/architecture/Bridge.  
* **Type Coercion:** JSON-LD allows for strict typing. We define a custom type DesignPattern that extends schema:CreativeWork, adding properties for context, forces, and solution.40

### **4.3 Schema Matching and Cross-Domain Alignment**

Connecting patterns across domains requires **Schema Matching**—the algorithmic identification of semantic correspondences between different data models.41

* **Adversarial Alignment:** The system uses adversarial autoencoders to align the feature spaces of different domains. It trains a model to map the "Problem" vectors of UX patterns to the "Problem" vectors of Architectural patterns. If the vectors for "User Disorientation" (UX) and "Wayfinding" (Architecture) align, the system infers a semantic bridge.42  
* **Subsumption Analysis:** Using hierarchical clustering, the system identifies when specific patterns in one domain are subsets of a general pattern in another.43 For example, it might identify that "Pagination," "Infinite Scroll," and "Load More" (UX) are all subsumed by the architectural concept of "Sequence of Spaces."

### **4.4 Pattern Language Markup Language (PLML) Support**

While JSON-LD is the modern standard, the system maintains backward compatibility with **PLML (Pattern Language Markup Language)**, an XML-based format developed for HCI patterns.44 This allows the system to ingest legacy pattern libraries that use this specific DTD, ensuring that historical design wisdom is not lost in the transition to modern formats. The system includes an XSLT transformation layer to convert PLML XML into JSON-LD on the fly.

## ---

**5\. Semantic Drift and Pattern Evolution Tracker**

Patterns are temporal entities; their meanings shift as technologies and cultures evolve. A "Dashboard" in 1890 (a mud-guard on a carriage) differs radically from a "Dashboard" in 2025 (a data visualization interface). The **Pattern Evolution Tracker** monitors this **Semantic Drift**.

### **5.1 Quantifying Semantic Drift**

We utilize **Diachronic Word Embeddings** to quantify how a pattern's position in vector space changes over time.45

* **Methodology:** The system creates time-sliced corpora (e.g., Corpus$\_ {2010}$, Corpus$*{2015}$, Corpus$*{2020}$). It trains separate embedding models for each slice.  
* **Cosine Similarity Shift:** We calculate the cosine similarity between the vector for a pattern (e.g., $V\_{mobile\\\_menu}$) in 2010 and 2020\. A low similarity score indicates high drift.  
* **Drift Categorization:**  
  * **Broadening:** The pattern applies to more contexts (e.g., "Canvas" moving from art to HTML5).  
  * **Narrowing:** The pattern becomes more specialized.  
  * **Pejoration:** The pattern acquires negative connotations (shifting to an *Anti-Pattern*).

### **5.2 OntoDrift and Structural Change**

Beyond vector drift, we employ the **OntoDrift** algorithm to measure structural changes in the pattern ontology.47

* **Concept Signatures:** OntoDrift assigns a "signature" to each concept based on its relationships (superclasses, subclasses, properties). Even if the pattern name remains the same, if its structural relationships change (e.g., "Singleton" losing its relationship to "Global State" in newer frameworks), OntoDrift detects this as a *Structural Drift*.47  
* **Evolutionary Deltas:** The system generates pattern\_diff.json files that record these changes, allowing researchers to replay the evolution of a pattern set. This supports the "Research Substrate" goal of the DRP.

### **5.3 Anti-Pattern Detection and Sentiment Analysis**

A critical aspect of evolution is the degradation of successful patterns into **Anti-Patterns**.

* **Sentiment Correlation:** The system correlates pattern mentions with sentiment scores extracted via NLP. If a pattern like "Carousel" begins to co-occur frequently with negative sentiment terms ("confusing," "slow," "ignored"), the system flags it as a potential Anti-Pattern.49  
* **Contextual Inversion:** The system detects when the "Solution" of a pattern becomes the "Problem" of another. For example, "Table Layouts" were a solution for web design in 1998; by 2005, they were the problem solved by "CSS Layouts." Tracking this inversion allows the system to build genealogy maps of design obsolescence.50

## ---

**6\. Visualization: The Lexical Map**

To render the mined lexicon accessible to human designers, the system generates a **Visual Lexicon**—a dynamic, topographic map of design knowledge.

### **6.1 Force-Directed Graph Visualization**

We utilize **D3.js** to create interactive, force-directed graph visualizations of the pattern ontology.51

* **Node Semantics:** Nodes represent patterns. The radius of a node represents its **Saliency Score** (frequency $\\times$ centrality).  
* **Edge Semantics:** Edges represent semantic relationships.  
  * *Solid Line:* "Is-A" (Taxonomic relationship).  
  * *Dashed Line:* "Related-To" (Cross-domain bridge).  
  * *Red Line:* "Conflicts-With" (Incompatible patterns).  
* **Clustering:** Nodes are clustered by domain (UX, Architecture, Code) using color coding. This allows users to visually inspect the overlap between domains. A tight intermingling of nodes indicates high cross-pollination (e.g., between UX and Frontend Dev), while isolated clusters indicate siloed knowledge.54

### **6.2 Topological Analysis and White Space Discovery**

The visualization serves as an analytical tool for **White Space Discovery**.

* **Gap Analysis:** By visualizing the "Pattern Space," we can identify sparse regions—areas where patterns exist in one domain but not in an adjacent one. For instance, if the "Security" cluster is dense in Software Engineering but sparse in UX, this visual gap suggests a need to import or discover UX-specific security patterns (e.g., "Trust Indicators").55  
* **Semantic Zoom:** The interface supports semantic zooming. At a high level, it shows meta-patterns ("Navigation"). Zooming in reveals domain specifics ("Mega Menu" in UX, "Wayfinding Signage" in Architecture).54

### **6.3 Glyph and Icon Generation**

To support rapid categorization, the system includes a **Visual Lexicon Generator**.

* **Generative Iconography:** Using simple geometric primitives (geons) and generative adversarial networks (GANs), the system generates unique glyphs for patterns based on their structural characteristics.9 A "Centralized" pattern might be represented by a circle with converging arrows. This visual shorthand aids in the rapid "Semi-supervised tagging" of case studies required by the prompt.

## ---

**7\. Generative Design and Computational Creativity**

The ultimate utility of the Lexical Cartography system lies in its integration with **Generative Design Agents**. The lexicon serves as a structured "prior" or knowledge base that guides AI generation, preventing hallucination and ensuring adherence to proven design wisdom.

### **7.1 PatternGPT: Patterns as Prompts**

We leverage the framework of **PatternGPT**, using the mined lexicon to engineer prompts for Large Language Models.3

* **Retrieval-Augmented Generation (RAG):** When an agent is tasked with designing a "User Onboarding Flow," it queries the Lexicon API. The system retrieves relevant patterns (e.g., "Progressive Disclosure," "Wizard," "Empty State") and injects their structured definitions (Context, Problem, Solution) into the context window of the LLM.  
* **Result:** The LLM generates a design solution that explicitly references and utilizes these patterns, rather than generating generic or incoherent text. This transforms the LLM from a probabilistic token predictor into a *pattern-aware design assistant*.57

### **7.2 Algorithmic Evolution and Combinatorial Creativity**

The system supports **Computational Creativity** by simulating the evolution of new patterns.

* **AlphaEvolve Integration:** Inspired by DeepMind's AlphaEvolve, the system treats patterns as algorithmic primitives.58 It runs evolutionary simulations where patterns are mutated (parameters changed), crossed over (combined), or selected based on fitness functions (e.g., "minimize user clicks" or "maximize structural stability").  
* **Combinatorial Synthesis:** The system proposes novel pattern combinations. What happens if we combine "Lazy Loading" (Software) with "Open Floor Plan" (Architecture)? The system might propose a "Dynamic Partitioning" system for flexible office spaces that adapts based on occupancy sensors—a novel pattern discovered through cross-domain synthesis.59

## ---

**8\. System Architecture and Execution Plan**

The implementation of the Lexical Cartography system is designed as a modular, microservices-based architecture, referred to as the **Pattern Engine**.

### **8.1 Architecture Components**

The system leverages the **NLP Workbench** architecture 1 for scalability and extensibility.

1. **Ingestion Service:** A distributed crawler and document parser (Python/Tesseract).  
2. **Embedding Service:** GPU-accelerated cluster running BERT/RoBERTa models for vectorization.24  
3. **Graph Database:** A Neo4j or RDF store (e.g., Jena) to store the Three-Layer Ontology and pattern relationships.62  
4. **API Gateway:** A GraphQL interface allowing precise querying of the lexicon (e.g., getPatterns(domain="UX", type="Navigation")).63  
5. **Visualization Frontend:** A React/D3.js application for the Pattern Playground and Map.62

### **8.2 Self-Test and Reflexive Check Protocols**

To ensure the integrity of the mined data, the system implements automated validation loops.

**Table 3: Validation Protocols**

| Test Condition | Protocol | Expected Result |
| :---- | :---- | :---- |
| **Emergence Verification** | **The "Rule of Three":** A candidate pattern must be identified in at least 3 distinct, unconnected corpora (e.g., a blog, a GitHub repo, and a paper). | Filter out "one-off" solutions; ensure generalizability. |
| **Lexical Overlap** | **Jaccard Similarity Check:** If two patterns share \>90% lexical overlap in their "Solution" fields. | Merge into a single entry; flag for synonymy resolution. |
| **Cross-Domain Validity** | **Reflexive Check:** If \>30% of patterns fail to find a bridge in an adjacent domain. | Trigger "Overfitting Alert"; re-calibrate the adversarial alignment model to broaden search parameters. |
| **Drift Safety** | **Semantic Drift Threshold:** If a pattern's drift score \> 0.4 over 5 years. | Flag for manual review; likely a homonym collision or radical conceptual shift.45 |

### **8.3 Output Formats**

The system supports diverse output formats to serve different stakeholders:

* **pattern\_lexicon.jsonld**: The canonical, machine-readable ontology for AI agents.  
* **pattern\_map.graphml**: Graph definition file for visualization tools like Gephi or Cytoscape.  
* **pattern\_diff.json**: A log of evolutionary changes for researchers studying design history.  
* **pattern\_logbook.md**: A human-readable compilation of case studies tagged with the mined patterns.

## ---

**9\. Future Trajectories and Conclusion**

The **Lexical Cartography System** represents a paradigm shift in the management of design knowledge. By moving from static repositories to a dynamic, computational engine, we unlock the ability to see design not as a collection of isolated disciplines, but as a unified language of problem-solving.

### **9.1 Relational Inclusions**

The system is designed to integrate with adjacent DRPs:

* **DRP-DESIGN-MEMORY-NETWORKS:** The lexicon provides the vocabulary for indexing organizational design memory.  
* **DRP-CODE-UX-BRIDGE:** The semantic alignment engine directly links UX patterns (e.g., "Card") to code components (e.g., Card.jsx), facilitating "design-to-code" automation.

### **9.2 Conclusion**

We are currently operating in a state of design amnesia, where solutions are constantly reinvented because they are locked in inaccessible linguistic silos. This system cures that amnesia. By mining affordances, tracking drift, and bridging domains, the Computational Pattern Cartographer reveals the deep, invariant structures of design. It provides the necessary infrastructure for the next generation of AI-augmented design, ensuring that as our tools become more autonomous, they remain rooted in the accumulated wisdom of human practice. The resulting lexicon is not a static map, but a living territory—a digital nervous system for the built and virtual world.

## ---

**Appendix: Implementation Details & Schemas**

**Artifact 1: pattern\_lexicon.jsonld (Detailed Schema)**

JSON

{  
  "@context": {  
    "schema": "http://schema.org/",  
    "lex": "http://lexicon.design/ontology/",  
    "pattern": "lex:Pattern",  
    "problem": "schema:question",  
    "solution": "schema:acceptedAnswer",  
    "forces": "lex:forces",  
    "affordances": "lex:affordances"  
  },  
  "@id": "http://lexicon.design/pattern/structural/bridge",  
  "@type": "pattern",  
  "name": "Bridge Pattern",  
  "domain":,  
  "problem": "An abstraction needs to be decoupled from its implementation so the two can vary independently.",  
  "context": "Systems where inheritance creates a combinatorial explosion of class hierarchies.",  
  "forces": \["Coupling", "Extensibility", "Complexity"\],  
  "solution": {  
    "@type": "schema:Answer",  
    "text": "Place the abstraction and implementation in separate class hierarchies and connect them with a reference."  
  },  
  "affordances":,  
  "related\_patterns": \[  
    {"@id": "http://lexicon.design/pattern/structural/adapter", "relation": "similar\_to"},  
    {"@id": "http://lexicon.design/pattern/structural/facade", "relation": "distinguished\_from"}  
  \],  
  "drift\_history": {  
    "2010\_vector": \[0.12, 0.45, 0.88\],  
    "2020\_vector": \[0.11, 0.46, 0.87\],  
    "cosine\_similarity": 0.99  
  }  
}

**Artifact 2: pattern\_diff.json (Drift Analysis)**

JSON

{  
  "pattern\_id": "hamburger\_menu",  
  "interval": "2015-2025",  
  "status": "Contested",  
  "metrics": {  
    "frequency\_change": "+15%",  
    "sentiment\_change": "-0.30",  
    "context\_shift": "Desktop \-\> Mobile Only"  
  },  
  "emergent\_affordances":,  
  "deprecated\_affordances":  
}

#### **Works cited**

1. arXiv:2303.01410v1 \[cs.CL\] 2 Mar 2023, accessed on December 14, 2025, [https://arxiv.org/pdf/2303.01410](https://arxiv.org/pdf/2303.01410)  
2. Ontology Design Patterns \- Emergent Mind, accessed on December 14, 2025, [https://www.emergentmind.com/topics/ontology-design-patterns-odps](https://www.emergentmind.com/topics/ontology-design-patterns-odps)  
3. PatternGPT: A Pattern-Driven Framework for Large Language Model Text Generation \- arXiv, accessed on December 14, 2025, [https://arxiv.org/pdf/2307.00470](https://arxiv.org/pdf/2307.00470)  
4. An Exploration of Pattern Mining with ChatGPT \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2412.16814v1](https://arxiv.org/html/2412.16814v1)  
5. Christopher Alexander Pattern Language \- Cornell | ARL, accessed on December 14, 2025, [https://arl.human.cornell.edu/linked%20docs/Alexander\_A\_Pattern\_Language.pdf](https://arl.human.cornell.edu/linked%20docs/Alexander_A_Pattern_Language.pdf)  
6. Design Patterns \- Refactoring.Guru, accessed on December 14, 2025, [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)  
7. Design Patterns \- SourceMaking, accessed on December 14, 2025, [https://sourcemaking.com/design\_patterns](https://sourcemaking.com/design_patterns)  
8. Patterns in UX Writing course lesson \- Uxcel, accessed on December 14, 2025, [https://app.uxcel.com/courses/ux-writing/patterns-313](https://app.uxcel.com/courses/ux-writing/patterns-313)  
9. How to Use Pattern Recognition and Perception in UX Design 4.8K \- Intechnic, accessed on December 14, 2025, [https://www.intechnic.com/blog/how-to-use-pattern-recognition-and-perception-in-ux-design/](https://www.intechnic.com/blog/how-to-use-pattern-recognition-and-perception-in-ux-design/)  
10. Archives \- A Pattern Language, accessed on December 14, 2025, [https://www.patternlanguage.com/archive/archive.html](https://www.patternlanguage.com/archive/archive.html)  
11. A Design Pattern Detection Approach Based on Semantics | Request PDF \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/286950528\_A\_Design\_Pattern\_Detection\_Approach\_Based\_on\_Semantics](https://www.researchgate.net/publication/286950528_A_Design_Pattern_Detection_Approach_Based_on_Semantics)  
12. Semantic Role Labeling \- Stanford University, accessed on December 14, 2025, [https://web.stanford.edu/\~jurafsky/slp3/21.pdf](https://web.stanford.edu/~jurafsky/slp3/21.pdf)  
13. Semantic role labeling for knowledge graph extraction from text, accessed on December 14, 2025, [https://d-nb.info/1234221632/34](https://d-nb.info/1234221632/34)  
14. Semantic Role Labeling: A Systematical Survey \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2502.08660v1](https://arxiv.org/html/2502.08660v1)  
15. \[2303.01410\] NLP Workbench: Efficient and Extensible Integration of State-of-the-art Text Mining Tools \- arXiv, accessed on December 14, 2025, [https://arxiv.org/abs/2303.01410](https://arxiv.org/abs/2303.01410)  
16. 17 Best Free GitHub Repositories to Crack System Design Interviews 🛠️ \- DEV Community, accessed on December 14, 2025, [https://dev.to/kumarkalyan/17-best-free-github-repositories-to-crack-system-design-interviews-h5p](https://dev.to/kumarkalyan/17-best-free-github-repositories-to-crack-system-design-interviews-h5p)  
17. ashishps1/awesome-low-level-design: Learn Low Level Design (LLD) and prepare for interviews using free resources. \- GitHub, accessed on December 14, 2025, [https://github.com/ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)  
18. How to Extract Quotes for UX Research Decks \- Insight7 \- Call Analytics & AI Coaching for Customer Teams, accessed on December 14, 2025, [https://insight7.io/how-to-extract-quotes-for-ux-research-decks/](https://insight7.io/how-to-extract-quotes-for-ux-research-decks/)  
19. Activities \- Output or Screen Scraping Methods \- UiPath Documentation, accessed on December 14, 2025, [https://docs.uipath.com/activities/other/latest/ui-automation/output-or-screen-scraping-methods](https://docs.uipath.com/activities/other/latest/ui-automation/output-or-screen-scraping-methods)  
20. Text Mining in Data Mining \- GeeksforGeeks, accessed on December 14, 2025, [https://www.geeksforgeeks.org/nlp/text-mining-in-data-mining/](https://www.geeksforgeeks.org/nlp/text-mining-in-data-mining/)  
21. What is NLP in Data Mining: Easy Explanation (with Examples) \- Hevo Data, accessed on December 14, 2025, [https://hevodata.com/learn/nlp-in-data-mining/](https://hevodata.com/learn/nlp-in-data-mining/)  
22. The changing landscape of text mining: a review of approaches for ecology and evolution, accessed on December 14, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11289731/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11289731/)  
23. On Matching Schemas Automatically \- Microsoft, accessed on December 14, 2025, [https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2001-17.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2001-17.pdf)  
24. Natural Language Processing Technology \- Azure Architecture Center | Microsoft Learn, accessed on December 14, 2025, [https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/natural-language-processing](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/natural-language-processing)  
25. 7 NLP Techniques for Extracting Information from Unstructured Text using Algorithms, accessed on December 14, 2025, [https://www.width.ai/post/extracting-information-from-unstructured-text-using-algorithms](https://www.width.ai/post/extracting-information-from-unstructured-text-using-algorithms)  
26. Knowledge-based document embedding for cross-domain text classification \- IEEE Xplore, accessed on December 14, 2025, [https://ieeexplore.ieee.org/document/7966016/](https://ieeexplore.ieee.org/document/7966016/)  
27. 18 Effective NLP Algorithms You Need to Know \- Shelf.io, accessed on December 14, 2025, [https://shelf.io/blog/18-effective-nlp-algorithms-you-need-to-know/](https://shelf.io/blog/18-effective-nlp-algorithms-you-need-to-know/)  
28. A Systematic Review on Semantic Role Labeling for Information Extraction in Low-Resource Data \- IEEE Xplore, accessed on December 14, 2025, [https://ieeexplore.ieee.org/iel7/6287639/10380310/10506493.pdf](https://ieeexplore.ieee.org/iel7/6287639/10380310/10506493.pdf)  
29. NLP Digest: What can you do with a rock? Affordance extraction via word embeddings | by Leonard Adolphs | Medium, accessed on December 14, 2025, [https://medium.com/@leonard.adolphs.95/nlp-digest-what-can-you-do-with-a-rock-affordance-extraction-via-word-embeddings-e3a4090b7362](https://medium.com/@leonard.adolphs.95/nlp-digest-what-can-you-do-with-a-rock-affordance-extraction-via-word-embeddings-e3a4090b7362)  
30. \[2503.11101\] A Survey on Self-supervised Contrastive Learning for Multimodal Text-Image Analysis \- arXiv, accessed on December 14, 2025, [https://arxiv.org/abs/2503.11101](https://arxiv.org/abs/2503.11101)  
31. What is Contrastive Learning? Applications & Frameworks \- Deepchecks, accessed on December 14, 2025, [https://www.deepchecks.com/glossary/contrastive-learning/](https://www.deepchecks.com/glossary/contrastive-learning/)  
32. identifying affordances | The Design Society, accessed on December 14, 2025, [https://www.designsociety.org/download-publication/25748/identifying\_affordances](https://www.designsociety.org/download-publication/25748/identifying_affordances)  
33. Text2Afford: Probing Object Affordance Prediction abilities of Language Models solely from Text \- arXiv, accessed on December 14, 2025, [https://arxiv.org/html/2402.12881v2](https://arxiv.org/html/2402.12881v2)  
34. Three methods for identifying novel affordances | Request PDF \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/282557360\_Three\_methods\_for\_identifying\_novel\_affordances](https://www.researchgate.net/publication/282557360_Three_methods_for_identifying_novel_affordances)  
35. Three methods for identifying novel affordances | AI EDAM | Cambridge Core, accessed on December 14, 2025, [https://www.cambridge.org/core/journals/ai-edam/article/three-methods-for-identifying-novel-affordances/D9997C0570380D899EDD55AD500A2309](https://www.cambridge.org/core/journals/ai-edam/article/three-methods-for-identifying-novel-affordances/D9997C0570380D899EDD55AD500A2309)  
36. Three-Layer OWL Ontology Design \- CEUR-WS.org, accessed on December 14, 2025, [https://ceur-ws.org/Vol-315/paper3.pdf](https://ceur-ws.org/Vol-315/paper3.pdf)  
37. What is JSON-LD? \- Fluree, accessed on December 14, 2025, [https://flur.ee/fluree-blog/what-is-json-ld/](https://flur.ee/fluree-blog/what-is-json-ld/)  
38. JSON-LD \- Wikipedia, accessed on December 14, 2025, [https://en.wikipedia.org/wiki/JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)  
39. What is JSON-LD?. Future-Proof Your Data with JSON-LD | by Kevin Doubleday | Fluree PBC | Medium, accessed on December 14, 2025, [https://medium.com/fluree/what-is-json-ld-e6ddaf1611f7](https://medium.com/fluree/what-is-json-ld-e6ddaf1611f7)  
40. JSON-LD Best Practices, accessed on December 14, 2025, [https://w3c.github.io/json-ld-bp/](https://w3c.github.io/json-ld-bp/)  
41. Schema matching and mapping-based data integration \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/266980963\_Schema\_matching\_and\_mapping-based\_data\_integration](https://www.researchgate.net/publication/266980963_Schema_matching_and_mapping-based_data_integration)  
42. Cross-Domain Adversarial Alignment for Network Anomaly Detection Through Behavioral Embedding Enrichment \- MDPI, accessed on December 14, 2025, [https://www.mdpi.com/2073-431X/14/11/450](https://www.mdpi.com/2073-431X/14/11/450)  
43. Domain taxonomy learning from text: The subsumption method versus hierarchical clustering \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/257026247\_Domain\_taxonomy\_learning\_from\_text\_The\_subsumption\_method\_versus\_hierarchical\_clustering](https://www.researchgate.net/publication/257026247_Domain_taxonomy_learning_from_text_The_subsumption_method_versus_hierarchical_clustering)  
44. PLML: Pattern Language Markup Language, accessed on December 14, 2025, [https://www.cs.kent.ac.uk/people/staff/saf/patterns/plml.html](https://www.cs.kent.ac.uk/people/staff/saf/patterns/plml.html)  
45. Drift Detection in Large Language Models: A Practical Guide | by Tony Siciliani | Medium, accessed on December 14, 2025, [https://medium.com/@tsiciliani/drift-detection-in-large-language-models-a-practical-guide-3f54d783792c](https://medium.com/@tsiciliani/drift-detection-in-large-language-models-a-practical-guide-3f54d783792c)  
46. (PDF) Semantic Drift in Ontologies. \- ResearchGate, accessed on December 14, 2025, [https://www.researchgate.net/publication/220724415\_Semantic\_Drift\_in\_Ontologies](https://www.researchgate.net/publication/220724415_Semantic_Drift_in_Ontologies)  
47. OntoDrift: a Semantic Drift Gauge for Ontology Evolution Monitoring \- CEUR-WS, accessed on December 14, 2025, [https://ceur-ws.org/Vol-2821/paper1.pdf](https://ceur-ws.org/Vol-2821/paper1.pdf)  
48. OntoDrift: a Semantic Drift Gauge for Ontology Evolution Monitoring, accessed on December 14, 2025, [https://www.semanticscholar.org/paper/OntoDrift%3A-a-Semantic-Drift-Gauge-for-Ontology-Capobianco-Cavaliere/1dc583f45d751b46704388e45b52549ee2eca3ca](https://www.semanticscholar.org/paper/OntoDrift%3A-a-Semantic-Drift-Gauge-for-Ontology-Capobianco-Cavaliere/1dc583f45d751b46704388e45b52549ee2eca3ca)  
49. Extracting Information from Unstructured Text with NLP – (6 Ways) \- Accern, accessed on December 14, 2025, [https://www.accern.com/resources/extracting-information-from-unstructured-text-with-nlp---6-ways](https://www.accern.com/resources/extracting-information-from-unstructured-text-with-nlp---6-ways)  
50. Using Machine Learning to Detect Design Patterns \- Software Engineering Institute, accessed on December 14, 2025, [https://www.sei.cmu.edu/blog/using-machine-learning-to-detect-design-patterns/](https://www.sei.cmu.edu/blog/using-machine-learning-to-detect-design-patterns/)  
51. How to Create Effective Network Visualization with D3.js \- Elijah Meeks, accessed on December 14, 2025, [http://elijahmeeks.com/networkviz/](http://elijahmeeks.com/networkviz/)  
52. D3 by Observable | The JavaScript library for bespoke data visualization, accessed on December 14, 2025, [https://d3js.org/](https://d3js.org/)  
53. D3.js Made Simple: Easy Data Visualizations Guide \- Semantic Arts, accessed on December 14, 2025, [https://www.semanticarts.com/d3-the-easy-way/](https://www.semanticarts.com/d3-the-easy-way/)  
54. An Ontology and Brain Model-based Semantic Discovery and Visualization System \- SciSpace, accessed on December 14, 2025, [https://scispace.com/pdf/an-ontology-and-brain-model-based-semantic-discovery-and-2ltlwmqy7w.pdf](https://scispace.com/pdf/an-ontology-and-brain-model-based-semantic-discovery-and-2ltlwmqy7w.pdf)  
55. Feature analysis of ontology visualization methods and tools, accessed on December 14, 2025, [https://csit.iaesprime.org/index.php/csit/article/download/50/40/76](https://csit.iaesprime.org/index.php/csit/article/download/50/40/76)  
56. Computational Creativity | Towards Data Science, accessed on December 14, 2025, [https://towardsdatascience.com/computational-creativity-6a5d77b3ed12/](https://towardsdatascience.com/computational-creativity-6a5d77b3ed12/)  
57. Design Patterns After the Singularity: Rethinking the Gang of Four for an AI-Driven Stack, accessed on December 14, 2025, [https://dev.to/tawe/design-patterns-after-the-singularity-rethinking-the-gang-of-four-for-an-ai-driven-stack-462e](https://dev.to/tawe/design-patterns-after-the-singularity-rethinking-the-gang-of-four-for-an-ai-driven-stack-462e)  
58. Computational Creativity and Artificial Evolution: Implications of AlphaEvolve \- Medium, accessed on December 14, 2025, [https://medium.com/@sergiosear/computational-creativity-and-artificial-evolution-implications-of-alphaevolve-0ea828710fd9](https://medium.com/@sergiosear/computational-creativity-and-artificial-evolution-implications-of-alphaevolve-0ea828710fd9)  
59. Computational creativity \- Wikipedia, accessed on December 14, 2025, [https://en.wikipedia.org/wiki/Computational\_creativity](https://en.wikipedia.org/wiki/Computational_creativity)  
60. Computational Creativity: AI's Role in Generating New Ideas, accessed on December 14, 2025, [https://www.wgu.edu/blog/computational-creativity-ai-role-generating-new-ideas2411.html](https://www.wgu.edu/blog/computational-creativity-ai-role-generating-new-ideas2411.html)  
61. What Is NLP (Natural Language Processing)? \- IBM, accessed on December 14, 2025, [https://www.ibm.com/think/topics/natural-language-processing](https://www.ibm.com/think/topics/natural-language-processing)  
62. A curated list of awesome JSON libraries and resources. \- GitHub, accessed on December 14, 2025, [https://github.com/burningtree/awesome-json](https://github.com/burningtree/awesome-json)  
63. Implementations \- JSON:API, accessed on December 14, 2025, [https://jsonapi.org/implementations/](https://jsonapi.org/implementations/)