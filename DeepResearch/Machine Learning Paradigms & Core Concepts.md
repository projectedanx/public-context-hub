Machine Learning Paradigms & Core Concepts

* A. Supervised Learning  
  * Classification  
    * Logistic Regression  
    * Support Vector Machines (SVMs)  
    * Linear SVMs  
    * Decision Trees  
      * CART (Classification and Regression Trees)  
      * ID3  
      * Enhanced Decision Trees  
      * Optimization Techniques (MIP, SAT solvers, Stochastic Search, Dynamic Programming)  
      * GOSDT (Globally Optimal Sparse Decision Trees)  
    *   
    * Ensemble Methods  
      * Random Forests (RF)  
      * Boosting  
        * Gradient Boosting  
        * Xgboost (eXtreme Gradient Boosting)  
        * CatBoost  
      *   
      * Bagging  
    *   
    * Nearest Neighbors (k-NN)  
    * Naive Bayes  
    * Quadratic Discriminant Analysis (QDA)  
    * Artificial Neural Networks (ANNs / NNs) (See also Section II)  
  *   
  * Regression  
    * Linear Regression  
      * Ordinary Least Squares (OLS)  
    *   
    * Ridge Regression  
    * Kernel Ridge Regression (KRR)  
    * Gaussian Process Regression (GPR) (Kriging)  
    * Support Vector Regression (SVR)  
    * Neural Networks (See also Section II)  
    * Multi-output Regression  
  *   
*   
* B. Unsupervised Learning  
  * Clustering  
    * K-means clustering  
    * Hierarchical clustering  
    * Affinity Propagation  
    * Spectral Clustering  
    * Density estimation  
  *   
  * Dimensionality Reduction  
    * Principal Component Analysis (PCA)  
    * Independent Component Analysis (ICA)  
    * Nonnegative Matrix Factorization (NMF)  
    * Kernel PCA  
    * t-SNE (t-Distributed Stochastic Neighbor Embedding)  
      * BH t-SNE  
      * FIt-SNE  
    *   
    * UMAP (Uniform Manifold Approximation and Projection)  
    * LargeVis  
    * TriMAP  
    * PaCMAP  
    * Autoencoders (AEs) (See also Section II.A.3)  
  *   
  * Anomaly Detection  
    * One-class SVM  
    * Isolation Forest  
  *   
  * Representation Learning (often overlaps with other categories)  
    * Sparse coding  
  *   
*   
* C. Semi-Supervised Learning  
  * Label Propagation (LP)  
    * Transductive Multiview Hypergraph Label Propagation (TMV-HLP)  
  *   
  * Clustering-based approaches  
  * Combining labeled and unlabeled data  
*   
* D. Reinforcement Learning (RL)  
  * Q-learning  
    * Deep Q-Networks (DQN)  
  *   
  * Policy Gradient Methods  
  * Reinforcement Learning from Human Feedback (RLHF)  
  * Self-Learning Monte Carlo (SLMC) (as an application/related concept)  
  * Interactive Learning  
*   
* E. Transfer Learning & Domain Adaptation  
  * General Concepts  
  * Domain Adaptation  
    * Unsupervised Domain Adaptation (UDA)  
    * Test-time domain adaptation  
    * Subspace Alignment Domain Adaptation (SADA)  
    * Geodesic Flow Kernel (GFK)  
    * Subspace Interpolation Dictionary Learning (SIDL)  
    * Regularised sparse coding based UDA  
  *   
  * Few-Shot Learning (FSL)  
    * Generalized Few-Shot Learning  
  *   
  * Multi-Task Learning (MTL)  
    * Regularized Multi-Task Learning (RMTL)  
    * Grouping and Overlapping Multi-Task Learning (GOMTL)  
    * Explicit Multi-Task Embedding (MTE)  
  *   
  * Meta-Learning (Learning to Learn)  
    * Model-Agnostic Meta-Learning (MAML)  
  *   
*   
* F. Core Concepts  
  * Bias–variance tradeoff  
  * Overfitting / Generalization  
  * Regularization (L1, L2, ElasticNet, Dropout)  
  * Loss Functions (Cross-Entropy, Hinge Loss, Mean Squared Error, Cosine Loss, Circle Loss, FAPE, Distogram Loss, etc.)  
  * Optimization Algorithms  
    * Gradient Descent (GD)  
    * Stochastic Gradient Descent (SGD)  
    * Adam Optimizer  
    * AdaGrad  
    * Newton's Method  
    * LBFGS (Limited Memory Broyden-Fletcher-Goldfarb-Shanno)  
    * Alternating Minimization  
    * Proximal Gradient Algorithms  
    * Simplex Projection  
    * Stochastic Reconfiguration / Natural Gradient  
    * Bayesian Optimization (BO)  
  *   
  * Feature Engineering / Representation Learning  
  * Embeddings (Word Embeddings, Visual Embeddings, Semantic Embeddings, Latent Embeddings, Binary Embeddings)  
* 

II. Neural Network Architectures & Techniques

* A. Foundational Architectures  
  * Artificial Neural Networks (ANNs) / Neural Networks (NNs)  
  * Feedforward Neural Networks  
    * Multi-layer Perceptron (MLP)  
  *   
  * Deep Neural Networks (DNNs)  
    * Autoencoders (AEs)  
      * Variational Autoencoders (VAEs)  
      * Conditional VAE (CVAE)  
      * Conditional Adversarial Autoencoder (CAAE)  
    *   
    * Convolutional Neural Networks (CNNs)  
      * VGG-16  
      * ResNet-50  
      * GoogLeNet (Inception-v1)  
      * Deep U-Nets  
      * Graph Convolutional Networks (GCNs) (See also GNNs)  
    *   
    * Recurrent Neural Networks (RNNs)  
      * LSTMs (Long Short-Term Memory)  
      * GRUs (Gated Recurrent Units)  
    *   
    * Generative Adversarial Networks (GANs)  
      * Wasserstein GAN (WGAN)  
      * Conditional WGAN (CWGAN)  
      * Denoised Diffusion GAN  
      * Adversarial Autoencoders (related)  
    *   
  *   
  * Boltzmann Machines  
    * Restricted Boltzmann Machines (RBM)  
    * Deep Boltzmann Machines (DBM)  
    * Further Restricted RBM (FRRBM)  
  *   
  * Graph Neural Networks (GNNs)  
    * Message Passing Neural Networks (MPNN)  
    * Graph Convolution Networks (GCN)  
    * Graph Attention Networks  
    * EdgeConv  
    * Interaction Networks (IN)  
    * Set-to-graph neural networks  
  *   
  * Transformers  
    * Core Architecture (Self-Attention, Multi-Head Attention)  
    * Encoder-only (e.g., BERT-like)  
    * Decoder-only (Autoregressive, e.g., GPT-like)  
    * Encoder-Decoder (Sequence-to-Sequence)  
    * Positional Encodings (Absolute, Relative, Rotary \- RoPE)  
    * Attention Mechanisms (Self-Attention, Cross-Attention, Linear Attention)  
    * Layer Normalization / Residual Connections  
    * Activation Functions (ReLU, GeLU, Sigmoid)  
  *   
*   
* B. Specific Neural Models & Frameworks (Often application-specific)  
  * BERT (Bidirectional Encoder Representations from Transformers)  
    * astroBERT  
    * CodeBERT / Graph-CodeBERT / PolyGlot variants  
    * SciBERT  
    * mBERT (multilingual BERT)  
  *   
  * GPT (Generative Pre-trained Transformer) Series  
    * GPT-2  
    * GPT-3 / Codex / InstructGPT / ChatGPT  
    * GPT-4 / GPT-4o  
    * ProteinForceGPT  
    * NeoGPT-X  
  *   
  * LLaMA / Llama 2 / Llama 3  
  * PaLM / Gopher  
  * T5 (Text-to-Text Transfer Transformer)  
  * XLMR (Cross-Lingual Model with RoBERTa)  
  * Chinchilla  
  * BLOOM  
  * OPT-175B  
  * Gemini / Gemini-Pro  
  * Mixtral  
  * Qwen  
  * Aya  
  * Command R+  
  * Gemma  
  * Dolly-v2  
  * StableVicuna  
  * InCoder  
  * CodeT5  
  * ESM-2 / ESMFold (Protein Language/Structure)  
  * CrystalBERT (Materials Science)  
  * Neural Quantum States (NQS) (using RBMs, RNNs, etc.)  
  * SchNet (Materials Science)  
  * Neural Network z-Vertex Trigger (NNT) (Particle Physics)  
  * DeepJet (Particle Physics)  
*   
* C. Training & Optimization Techniques for Neural Networks  
  * Pre-training (Language Modeling, Masked LM, Next Sentence Prediction, Autoregressive Blank Infilling)  
  * Fine-tuning (Supervised Fine-Tuning \- SFT, Instruction Tuning)  
  * Parameter-Efficient Fine-Tuning (PEFT)  
    * Adapters  
    * Side-tuning  
    * Low-Rank Adaptation (LoRA) / QLoRA  
  *   
  * Zero-Shot Learning (See Section IV)  
  * Few-Shot Learning / In-Context Learning (ICL)  
  * Reinforcement Learning from Human Feedback (RLHF)  
  * Stochastic Gradient Descent (SGD) variants (Adam, AdaGrad)  
  * Loss Functions (Cross-Entropy, Ranking Loss, FAPE, Distogram Loss, etc.)  
  * Regularization (L1, L2, Dropout)  
  * Distributed Training (Data Parallelism, FSDP)  
  * Mixed Precision Training  
  * Knowledge Distillation  
* 

III. Evaluation & Interpretability

* A. Evaluation Metrics & Benchmarks  
  * Cross-Entropy Loss / Perplexity  
  * Accuracy (Top-1, Calibrated Accuracy)  
  * F1 Score  
  * ROC AUC / Precision-Recall Curves  
  * ROUGE / BLEU / SacreBLEU / ChrF++ (NLP Metrics)  
  * Mean Average Precision (mAP)  
  * Knowledge F1 / PARENT / PARENT-T (Hallucination/Faithfulness)  
  * Human Evaluation  
  * Benchmarks (GLUE, MultiNLI, SQuAD, ImageNet, HumanEval, BIG-Bench, MoleculeNet, TRECVID MED, etc.)  
  * Specialized Benchmarks (GHOSTS, miniGHOSTS, microGHOSTS, MultiQ, MLAgentBench, SciSafeEval, HaluEval, HaDes)  
*   
* B. Interpretability & Explainability (XAI)  
  * Model-Based Interpretability (inherently interpretable models)  
    * Linear Models  
    * Decision Trees  
    * Generalized Additive Models (GAMs)  
  *   
  * Post-Hoc Explanation Methods  
    * Feature Attribution / Importance  
      * Perturbation-Based Methods  
      * Gradient-Based Methods (Integrated Gradients \- IG)  
      * SHAP (Shapley Additive exPlanations) / TransSHAP  
      * LIME (Local Interpretable Model-agnostic Explanations)  
    *   
    * Surrogate Models  
    * Decomposition Techniques  
    * Attention-Based Explanations  
    * Example-Based Explanations  
    * Counterfactual Explanations  
    * Data Influence Functions  
    * Probing (Classifier-based)  
    * Concept-Based Interpretability (TCAV)  
    * Mechanistic Interpretability (Neuron/Circuit analysis)  
    * Natural Language Explanations (NLE)  
      * Self-Explanations  
      * Chain-of-Thought (CoT) Explanations  
      * Summarize and Score (SASC)  
    *   
    * Tools/Frameworks (InterpretML, LLMCheckup, TalkToModel)  
  *   
  * Interpretability Evaluation  
    * Predictive, Descriptive, Relevant (PDR) framework  
    * Evaluation on synthetic modules / ground truth  
    * Human subject evaluations  
  *   
*   
* C. Robustness & Reliability Analysis  
  * Out-of-Distribution (OOD) Generalization Tests (e.g., HANS)  
  * Adversarial Attacks (e.g., TextFooler)  
  * Randomization Ablation Methods  
  * Hallucination Detection & Mitigation  
    * Attestation Bias / Relative Frequency Bias analysis  
    * Metrics (FRANK, TRUE, PARENT, CDR, ANH Detection)  
    * Mitigation (Faithful datasets, Modeling/Inference methods, Self-Correction)  
  *   
  * Memorization Analysis (Taxonomy: verbatim, facts, ideas, algorithms, styles, etc.)  
  * Bias & Toxicity Analysis  
  * Calibration Analysis (Confidence Estimation)  
  * Safety Alignment Evaluation (SciSafeEval)  
* 

IV. Zero-Shot Learning (ZSL) & Related Paradigms

* A. Core Concepts  
  * Zero-Shot Learning (ZSL)  
  * Generalized Zero-Shot Learning (GZSL)  
  * Transductive ZSL  
  * Few-Shot Learning (FSL) / One-Shot Learning (OSL) (often related or compared)  
*   
* B. ZSL Approaches: Embedding-Based  
  * Core Idea: Mapping visual features and semantic representations (attributes, word vectors, text) to a common or related space.  
  * Mapping Directions:  
    * Visual-to-Semantic (e.g., Socher et al., CMT, SP-AEN)  
    * Semantic-to-Visual (e.g., Learning a Deep Embedding Model)  
    * Joint/Common Embedding Space (e.g., DeViSE, SJE, ALE, LatEm, SSE, JLSE, TMV-BLP, BiDiLEL, Joint Concept Matching)  
  *   
  * Specific Techniques:  
    * Bilinear Compatibility Models (ALE, DEVISE, SJE, LatEm)  
    * Linear Regression Models  
    * Deep Embedding Models (CNNs, Semantic Encoding Subnets)  
    * Autoencoder-Based (SAE, IP-SAE, LESAE, Coupled Semantic Autoencoders)  
    * Manifold Learning / Regularization (ME-ZSR, MCCA-ZSR, AMS-SFE, ZSL Multi-scale Manifold Reg, Structurally Constrained Correlation Transfer)  
    * Graph-Based Methods (Shared sparse graph, Laplacian graph, Hypergraph)  
    * Hashing / Binary Embeddings (BZSL)  
    * Low-Rank Embeddings (LESAE)  
    * Attribute-Based Methods (DAP, IAP, Preserving Semantic Relations, Hierarchical Semantic Loss)  
    * Dictionary Learning (ZSL Joint Latent Similarity, Synthesized Classifiers)  
    * Metric Learning (Improved Visual-Semantic Alignment)  
    * Information Theoretic (Mutual Information Maximization, Noise-contrastive estimation)  
    * Semantic Output Codes (SOC)  
  *   
*   
* C. ZSL Approaches: Generative  
  * Core Idea: Generating synthetic features or data for unseen classes.  
  * Generative Models Used:  
    * GANs (Generative Adversarial Networks)  
      * Conditional GANs (cGANs)  
      * Wasserstein GANs (WGAN, cWGAN)  
      * Cycle-Consistent GANs (cycle-WGAN, cycle-CLSWGAN)  
      * Specific Models: ZSL-GAN, ZSGAN KG, ZSCRGAN, SPGAN, LisGAN, Feature Generating Networks, Generative Adversarial ZSL Noisy Text  
    *   
    * VAEs (Variational Autoencoders)  
      * Conditional VAE (CVAE)  
    *   
    * VAE/GAN Hybrids (Joint Generative Model ZSL)  
    * Exponential Family Distributions  
    * Generative Latent Prototype Models  
  *   
  * Related Concepts:  
    * Synthesized Classifiers  
    * Generating Visual Representations / Exemplars  
    * Visual Data Synthesis  
  *   
*   
* D. ZSL Approaches: Other  
  * Regression-Based (Attribute Regression, ZSL Attribute Regression)  
  * Structured Prediction  
  * Knowledge Transfer (RecKT, Relational Knowledge Transfer \- RKT)  
  * Reading Comprehension Formulation  
  * Conditional Visual Classification  
  * Simple/Linear Methods (Embarrassingly Simple ZSL)  
  * Multi-cue Integration  
  * Part-based Approaches (Part-based CNN ZSL)  
  * Context-Aware Methods (CRF-based)  
  * Meta-Learning (MZSR)  
  * Active Learning (Improved Coupled Autoencoder ZSR)  
*   
* E. ZSL Applications  
  * Image Classification/Recognition  
  * Object Detection (ZSD)  
  * Scene Graph Parsing (Predicate Prediction)  
  * Image Restoration (Deblurring, Super-Resolution, Dehazing, Denoising, Inpainting, Underwater, Back-lit, Underexposed, Ancient Documents)  
  * Audio Restoration (Denoising, Inpainting)  
  * Video Restoration / Translation / Editing  
  * Point Cloud Completion  
  * Sketch-Based Image Retrieval (SBIR)  
  * Image-to-Text Generation (ZeroCap)  
  * Cross-Modal Retrieval (ZSCRGAN)  
  * Relation Extraction (NLP)  
  * Thought Recognition (fMRI decoding)  
  * Pansharpening  
*   
* F. ZSL Challenges & Mitigation  
  * Domain Shift Problem / Projection Domain Shift  
    * Domain Adaptation Techniques (UDA, Test-time adaptation, Transductive methods)  
    * Prototype Rectification  
    * Manifold Alignment / Regularization  
    * Generative Approaches  
  *   
  * Hubness Problem  
    * Hubness Correction  
    * Embedding in Visual Space  
  *   
  * Prototype Sparsity  
    * Hypergraph Label Propagation  
  *   
  * Semantic Ambiguity / Semantic Loss  
    * Semantic Relation Preservation  
    * Attribute Refinement (ARN)  
    * Semantics-Preserving AEN (SP-AEN)  
    * Visual-Semantic Ambiguity Removal (VSAR)  
  *   
  * Handling Noisy Text / Attributes  
    * Noise Suppression (l2,1-norm)  
    * Part-based methods  
  *   
  * Handling Missing Attributes  
    * Matrix Completion (Structured Matrix Completion)  
  *   
  * Evaluation Challenges (Need for unified benchmarks, GZSL setting, appropriate metrics like AUSUC)  
* 

V. Domain-Specific ML Applications & Techniques

* A. Physics & Materials Science  
  * Quantum Many-Body Physics / Quantum Matter  
    * Neural Network Quantum States (NQS) (RBMs, RNNs, DBMs)  
    * Variational Monte Carlo (VMC) / t-VMC  
    * Quantum State Tomography (using RBMs)  
    * Phase Transition Identification (CNNs, QLT, unsupervised adversarial networks)  
    * Quantum Loop Topography (QLT)  
    * Topological States Representation (RBMs, FRRBMs, Tensor Networks, MERA)  
    * Machine Learning for Fermion Sign Problem  
    * Decoding Conformal Field Theories (CFTs) (Supervised NNs, Autoencoders)  
    * Rydberg Atom Systems Simulation/Identification (SVMs, RFCs, DMRG+ML)  
  *   
  * Particle Physics (High Energy Physics \- HEP)  
    * Event Reconstruction / Pattern Recognition (GNNs, CNNs, RNNs, Tracking algorithms)  
    * Particle Identification (PID) (BDT, ProbNN, DeepNN, CatBoost)  
    * Jet Substructure / Jet Tagging (CNNs, GNNs, Deep Sets)  
    * Anomaly Detection (VAEs, Autoencoders)  
    * Fast Simulation (GANs, VAEs)  
    * Trigger Systems (CNNs, NNT)  
    * Statistical Significance Analysis (Likelihood Ratio Tests with ML outputs)  
    * Effective Field Theory (EFT) Constraints  
    * Symbolic Computation Acceleration (SYMBA \- Transformer)  
  *   
  * Condensed Matter Physics / Materials Science  
    * Machine Learning Interatomic Potentials (MLIPs) (NNPs, GAPs, SNAPs)  
    * Predicting Material Properties (CrystalBERT, Regression models)  
    * Structure Searching / Prediction (ASLA, Bayesian Optimization)  
    * Analyzing Scattering Data (ML Inversion, PCA, GPR)  
    * Electronic Structure Calculations (ML/MM, Decision Trees for active space)  
    * Origami Design (Decision Trees, Interpretable ML)  
  *   
  * General Physics & Engineering  
    * Physics-Informed Neural Networks (PINNs)  
    * Symbolic Regression (SR) for discovering physical laws/solutions  
    * Topological Data Analysis (TDA) in Physics (Mapper, Zigzag persistence)  
    * Solving Lippmann-Schwinger Equation (Recurrent Localization Networks \- RLN)  
    * Interpretable ML for Physical Insights (slisemap, Integrated Gradients)  
  *   
*   
* B. Natural Language Processing (NLP) & Large Language Models (LLMs)  
  * Foundational Models (GPT series, BERT, LLaMA, PaLM, T5, etc. \- See Section II.B)  
  * Pre-training Objectives (Language Modeling, MLM, NSP, Blank Infilling \- GLM)  
  * Fine-tuning & Adaptation (SFT, RLHF, Instruction Tuning, Prompting)  
  * Prompt Engineering & Patterns (Chain-of-Thought \- CoT, Zero-Shot-CoT, Self-Consistency, Few-Shot Prompting, Prompt Pattern Catalog)  
  * Capabilities & Evaluation  
    * Reasoning (Mathematical, Commonsense, Logical)  
    * Knowledge Storage & Retrieval (LLM-as-KB, REALM, RETA-LLM, RAG)  
    * Multilingual Capabilities (Evaluation, Alignment, Hallucination Gaps, Cross-lingual transfer, MultiQ, Language Ranker)  
    * Code Understanding & Generation (PolyCoder, Code Summarization)  
    * Dialogue Systems (LaMDA)  
    * Text-to-SQL  
  *   
  * Interpretability & Explainability (See Section III.B)  
    * Causal Analysis (Causal Mediation Analysis, DAS, Boundless DAS)  
    * Probing Internal Representations (Logit Lens, Tuned Lens)  
    * Self-Correction Strategies (Surveyed methods: Self-Refine, Reflexion, CRITIC, etc.)  
  *   
  * Challenges (Hallucination, Memorization, Bias, Safety, Robustness, Prompt Sensitivity \- FormatSpread)  
*   
* C. Computer Vision (Beyond ZSL)  
  * Image Captioning (Object Hallucination discussion)  
  * Image Generation (Diffusion Models, GANs, VAEs, Transformers)  
  * Object Detection (Faster-RCNN as baseline)  
*   
* D. Biology & Healthcare  
  * Protein Structure Prediction (AlphaFold 2, ESMFold)  
  * Genomic Sequence Modeling (GenSLMs)  
  * Intracellular Signaling Analysis (RNNs, HMMs, SLEMI)  
  * Biodiversity Science (NLP for literature mining \- TaxonGrab, etc.)  
  * Medical Diagnostics (Statistical Physics \+ ML)  
  * Clinical Note Analysis (CHiLL \- LLM feature extraction)  
  * fMRI Data Analysis (Thought Recognition, Interpreting LLM embeddings)  
  * Computational Chemistry (ML for PES, reaction prediction, etc.)  
*   
* E. Economics & Social Science  
  * Cognitive Automation for Economic Research (LLM applications)  
  * Hate Speech Detection / Product Review Analysis (LLM Agent applications)  
  * LLM Value Alignment / Cultural Representation (Hofstede dimensions analysis)  
*   
* F. Education  
  * LLMs in Education (Capabilities, Challenges, Prompting)  
  * Machine Learning Education for Physicists  
* 

VI. Other Techniques & Concepts

* A. Statistical Methods & Concepts  
  * Bayesian Inference / Bayesian Methods  
  * Maximum A Posteriori (MAP) Estimation  
  * Minimum Mean Square Error (MMSE) Estimation  
  * Monte Carlo Methods (QMC, DQMC, VMC)  
  * Histogram Reweighting  
  * Finite-Size Scaling Analysis  
  * Renormalization Group (RG) Analysis  
  * Canonical Correlation Analysis (CCA) / Multi-view CCA  
  * ANOVA (Analysis of Variance)  
*   
* B. Optimization & Search (Beyond NN optimization)  
  * Genetic Algorithms  
  * Basin-Hopping  
  * Elastic Band Methods (Doubly-nudged)  
  * Eigenvector Following  
*   
* C. Data Representation & Handling  
  * Graph Representations (Molecules, Quantum Experiments, Particle Physics Events)  
  * Feature Extraction (SIFT, Fisher Vectors, ITF, CNN features)  
  * Data Augmentation  
  * Handling Missing Data (Matrix Completion)  
  * Tokenization (WordPiece, SentencePiece, BPE \- impact analysis)  
  * Symbolic Representations (SMILES, SELFIES, Mathematical Expressions)  
*   
* D. Software & Tools  
  * TensorFlow / Keras / Theano / PyTorch / PyTorch Lightning  
  * Scikit-learn  
  * TMVA  
  * MARTY (Symbolic Computation)  
  * NetKet (Quantum Many-Body ML)  
  * PELE / GMIN / OPTIM / PATHSAMPLE (Energy Landscapes)  
  * hls4ml / FINN (ML on FPGAs/ASICs)  
  * NLTK (NLP Toolkit)  
  * LangChain / LlamaIndex (LLM Frameworks)  
  * Hugging Face Transformers/Datasets  
  * OpenAI API / Codey / GPT Models  
  * Semantic Scholar API  
  * ITensor (DMRG)  
* 

