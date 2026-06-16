Categorized Hierarchy of Concepts in Ultra-High Resolution Noise Reconstruction & Related Fields (2023-2025 Insights)  
I. Core Image/Signal Processing Techniques

* A. Filtering Methods  
  * Collaborative Filtering Approaches (Generic) \- \[Language model\]  
  * Transform-Domain Noise Variance Techniques (Specific: for stationary correlated noise) \- \[Ymir Mäkinen 2019\]  
  * Guided Filtering (Generic concept referenced by multiple methods like DSR-EI, Guided Depth Restoration Branch) \- \[e.g., Xin Qiao 2023, Kaiming He 2010\]  
  * Bilateral Filtering (Referenced concept) \- \[e.g., Zhiwei Zhong 2023\]  
  * Joint Bilateral Filtering/Upsampling (JBU) (Referenced concept) \- \[e.g., Zhiwei Zhong 2023, Hanqi Fan 2015\]  
  * Median Filtering (Specific: Weighted Median Filter) \- \[Haotian Wang 2022\]  
  * Anisotropic Diffusion Filtering (Referenced concept) \- \[e.g., Xin Qiao 2024, A. Mishra 2011\]  
  * Joint hybrid-cross guidance filter method\* (Specific novel method) \- \[K. Wang 2022\]  
  * Hybrid side window filter block\* (Component of above) \- \[K. Wang 2022\]  
  * Multi-perspective cross-guided fusion filter block\* (Component of above) \- \[K. Wang 2022\]  
  * Adaptive gradient fusion filters\* (Specific method for depth enhancement) \- \[Ting-An Chang 2018\]  
  * Low-Pass Filtering (Specific: Adaptive Content-Aware LPF for Anti-Aliasing) \- \[Xueyan Zou 2020\]  
  * Edge-Preserving Fusion Filters (Specific method for depth upsampling) \- \[Ting-An Chang 2018\]  
*   
* B. Transformation Domains  
  * Fourier Transform (Specific: Embedding Fourier for Enhancement \- UHDFour\*) \- \[Chongyi Li 2023\]  
  * Frequency Domain Processing (Specific: Gradient-Frequency Awareness \- SGNet\*) \- \[Zhengxu Wang 2023\]  
  * Discrete Cosine Transform (Specific: DCTNet\* for Guided Depth SR) \- \[Zixiang Zhao 2021\]  
  * Wavelet Transform (Specific: Adaptive Dual-Tree Discrete Wavelet Packets \- ADDWP) \- \[Jingyu Yang 2023\]  
  * Wavelet Transform (Specific: For depth SR enhancement) \- \[Chandra Shaker Balure 2016\]  
*   
* C. Interpolation & Sampling  
  * Upsampling/Super-Resolution (General concept)  
  * Downsampling (General concept)  
  * Non-Uniform Sampling (Specific: Graph Laplacian Induced Non-Uniform Sampling \- GLINUS\*) \- \[Jingyu Yang 2023\]  
  * Non-Uniform Sampling (Specific: Learning Non-Uniform-Sampling \- NSEN\*) \- \[Wei Yu 2023\]  
  * Interpolation Algorithms (Classical reference, outperformed) \- \[Tingsheng Huang 2023\]  
  * Inverse Distance Interpolation (Component of a specific SR method) \- \[Tingsheng Huang 2023\]  
  * Kriging Interpolation (Specific: For depth SR) \- \[Ting-hui Huang 2023\]  
  * Residual Interpolation (Specific: For intensity-guided depth upsampling \- RI\*) \- \[Yosuke Konno 2015\]  
  * Implicit Neural Representations / Functions (Specific: For continuous SR \- DCSR\*, JIIF\*) \- \[Yuyang Wang 2023, Jiaxiang Tang 2021\]  
  * Sub-Pixel Convolution (Specific: ESPCN\* for efficient SR) \- \[Wenzhe Shi 2016\]  
*   
* D. Regularization & Priors  
  * Graph Total Variation Regularizer\* (Component of EoP framework) \- \[Jingyu Yang 2023\]  
  * Graph Laplacian Regularizer\* (Component of EoP framework) \- \[Jingyu Yang 2023\]  
  * L0 Gradient Minimization (Specific: Super-weighted\* for depth upsampling) \- \[Shengtao Yu 2019\]  
  * L0 Gradient Minimization (Specific: For image smoothing) \- \[Li Xu 2011\]  
  * Total Generalized Variation (TGV) (Referenced regularization) \- \[e.g., Jiayi Yuan 2023, Zhiwei Zhong 2023\]  
  * Anisotropic Total Generalized Variation (ATGV) (Specific: For guided depth SR) \- \[David Ferstl 2013\]  
  * Nonconvex Potentials/Optimization (Specific: For robust guided filtering \- SD filter\*) \- \[Bumsub Ham 2018\]  
  * Sparse Representation / Dictionary Learning (General concept) \- \[e.g., Hanqi Fan 2015, Xin Deng 2020\]  
  * Multi-modal Dictionary Learning (Specific: TDL\* in RADAR algorithm) \- \[Xin Deng 2020\]  
  * Plug-and-Play (PnP) Frameworks (Specific: PnP-GAP\* for holographic imaging) \- \[Zhao Ma 2023\]  
  * Plug-and-Play (PnP) Frameworks (Specific: Graph-based\* for depth SR) \- \[Rong Chen 2018\]  
  * Deep Denoising Prior (Component of PnP method) \- \[Zhao Ma 2023\]  
*   
* E. Optimization Methods  
  * Alternating Direction Method of Multipliers (ADMM) (Solver for specific frameworks) \- \[Jingyu Yang 2023, Rong Chen 2018, Kyungsang Kim 2018\]  
  * Bayesian Least-Squares Estimation (Framework formulation) \- \[A. Mishra 2011\]  
  * Quasi-random density estimation (Component of Bayesian framework) \- \[A. Mishra 2011\]  
  * Split Bregman Method (Solver for L1 regularization) \- \[T. Goldstein 2009\]  
  * Primal-Dual Algorithms (Solver for TGV optimization) \- \[David Ferstl 2013, Gernot Riegler 2016\]  
*   
* F. Scale-Space & Multi-Scale Approaches  
  * Nonlinear volumetric scale-space framework\* (Specific method for volumetric data) \- \[A. Mishra 2011\]  
  * Exploration of Multi-Scale Approaches (General trend) \- \[Language model\]  
  * Multi-scale methods integrated into various networks (e.g., MSG-Net, PMBANet, AHMF, DCN in RSAG, MSFFRN) \- \[Multiple papers\]  
* 

II. Machine Learning & AI Approaches

* A. Neural Network Architectures  
  * Convolutional Neural Networks (CNNs) (General, backbone for many methods) \- \[Multiple papers\]  
  * U-Net Architecture (Specific: For segmentation, SR, diffusion models) \- \[O. Ronneberger 2015, Levente Baljer 2024, Hojat Asgariandehkordi 2023, Chih-Wei Chang 2024\]  
  * Encoder-Decoder Architectures (General structure) \- \[e.g., Hui Lan 2023\]  
  * Generative Adversarial Networks (GANs) (General approach) \- \[Language model\]  
    * TM-GAN\* (Specific: Transformer-based multi-modal GAN for depth SR) \- \[Jiang Zhu 2024\]  
    * IEA-GAN\* (Specific: Intra-Event Aware GAN for detector simulation) \- \[Hosein Hashemi 2023\]  
    * CDcGAN\* (Specific: Color-Depth Conditional GAN for simultaneous SR) \- \[Lijun Zhao 2019\]  
    * CoReGAN\* (Specific: Contrastive Regularized GAN for guided depth SR) \- \[Aditya Kasliwal 2023\]  
    * HD-Fusion\* (Uses GAN concepts like SDS loss) \- \[Jinbo Wu 2023\]  
  *   
  * Diffusion Probabilistic Models (General approach) \- \[Language model\]  
    * DDPM (Denoising Diffusion Probabilistic Modeling) \- \[Chih-Wei Chang 2024, Hojat Asgariandehkordi 2023\]  
    * SR3-DDPM\* (Super-Resolution variant) \- \[Chih-Wei Chang 2024\]  
    * Cascade Diffusion Models (Specific: UltraPixel\* for UHR synthesis) \- \[Jingjing Ren 2024\]  
    * Diffusion Models for Depth Estimation (Specific: ChronoDepth\*, DepthGen\*, DiffusionDepth\*) \- \[Jiahao Shao 2024, Saurabh Saxena 2023, Yiqun Duan 2023\]  
  *   
  * Transformers (General approach)  
    * Vision Transformer (ViT) (Referenced backbone) \- \[Alexey Dosovitskiy 2020, Aakash Rajpal 2023\]  
    * Pyramid Vision Transformer (PVT)\* (Backbone for dense prediction) \- \[Wenhai Wang 2021\]  
    * Restormer\* (Efficient Transformer for image restoration) \- \[Syed Waqas Zamir 2021\]  
    * Swin Transformer (Backbone, e.g., Swin-DMSR\*) \- \[Ryan Peterson 2023\]  
    * DETR\* (DEtection TRansformer) \- \[Nicolas Carion 2020\]  
  *   
  * Specific Named Networks/Models (Novel or key contributions):  
    * DSRNet\* (Depth SR guided by blurry depth/clear intensity edges) \- \[Hui Lan 2023\]  
    * LEDSRNet\* (Latent Edge Guided Depth SR) \- \[Hui Lan 2024\]  
    * IGAF\* (Incremental Guided Attention Fusion for Depth SR) \- \[Athanasios Tragakis 2024\]  
    * DSR-EI\* (Depth SR from Explicit/Implicit HF features) \- \[Xin Qiao 2023\]  
    * RSAG\* (Recurrent Structure Attention Guided Depth SR) \- \[Jiayi Yuan 2023\]  
    * SGNet\* (Structure Guided Network via Gradient-Frequency Awareness) \- \[Zhengxu Wang 2023\]  
    * PatchFusion\* (Tile-based framework for high-res monocular depth) \- \[Zhenyu Li 2023\]  
    * SSDNet\* (Spherical Space feature Decomposition Network) \- \[Zixiang Zhao 2023\]  
    * NLSPN\* (Non-Local Spatial Propagation Network for Depth Completion) \- \[Jinsun Park 2020\]  
    * PDR-Net\* (Progressive depth reconstruction network) \- \[Peng Liu 2022\]  
    * DADA\* (Deep Anisotropic Diffusion-Adjustment) \- \[Nando Metzger 2022\]  
    * AHMF\* (Attention-based Hierarchical Multi-modal Fusion) \- \[Zhiwei Zhong 2021\]  
    * FDSR\* (Fast Depth Super-Resolution) \- \[Lingzhi He 2021\]  
    * DCTNet\* (Discrete Cosine Transform Network) \- \[Zixiang Zhao 2021\]  
    * JIIF\* (Joint Implicit Image Function) \- \[Jiaxiang Tang 2021\]  
    * BridgeNet\* (Joint learning for DSR and MDE) \- \[Q. Tang 2021\]  
    * DepthSR-Net\* (Hierarchical Features Driven Residual Learning) \- \[Chunle Guo 2019\]  
    * PMBANet\* (Progressive Multi-Branch Aggregation Network) \- \[Xinchen Ye 2020\]  
    * Deep Primal-Dual Network\* (Combines FCN and PDN) \- \[Gernot Riegler 2016\]  
    * MSG-Net\* (Multi-Scale Guidance Network) \- \[Tak-Wai Hui 2016\]  
    * RCAN\* (Residual Channel Attention Networks) \- \[Yulun Zhang 2018\]  
    * Deep Variational Model\* (Integrates global/local predictions) \- \[Youngjung Kim 2018\]  
    * DKN/FDKN\* (Deformable Kernel Networks) \- \[Beomjun Kim 2019\]  
    * CU-Net\* (Common/Unique info splitting network) \- \[Xin Deng 2019\]  
    * SeaNet\* (Soft-edge assisted Network) \- \[Faming Fang 2020\]  
    * PAN\* (Pixel Attention Network) \- \[Hengyuan Zhao 2020\]  
    * MPRNet\* (Multi-Stage Progressive Image Restoration) \- \[Syed Waqas Zamir 2021\]  
    * MIRNet\* (Multi-scale Residual Network for Real Image Restoration) \- \[Syed Waqas Zamir 2020\]  
  *   
  * Deep Image Prior (DIP) (Unsupervised approach) \- \[Yilin Liu 2023\]  
  * Blind-spot networks (Concept for self-supervised denoising) \- \[C. Birnie 2022\]  
*   
* B. Learning Paradigms & Strategies  
  * Supervised Learning (Implicit in many methods)  
  * Self-supervised procedures/learning \- \[C. Birnie 2022, Xin Qiao 2023\]  
  * Unsupervised Learning (e.g., DIP) \- \[Yilin Liu 2023\]  
  * Transfer Learning (General strategy) \- \[Language model\]  
  * Pre-training (Specific: with synthetic data) \- \[C. Birnie 2022\]  
  * Contrastive Learning (Specific: For regularizing GANs \- CoReGAN\*, for self-supervised pre-training) \- \[Aditya Kasliwal 2023, Xin Qiao 2023\]  
  * Multi-task Learning (Specific: BridgeNet\* for DSR/MDE) \- \[Q. Tang 2021\]  
  * Knowledge Distillation / Transfer (Specific: Cross-task for DSR) \- \[Baoli Sun 2021\]  
  * Residual Learning (Common technique in deep networks) \- \[e.g., Kaiming He 2015, Chunle Guo 2019\]  
  * Progressive Learning/Training (Strategy for complex tasks/high-res) \- \[e.g., Syed Waqas Zamir 2021\]  
  * Iterative Refinement/Reconstruction (Strategy in diffusion, optimization) \- \[e.g., T. Wang 2016, Yiqun Duan 2023\]  
*   
* C. Feature Manipulation  
  * Feature Extraction (General concept)  
  * Feature Fusion (General concept)  
    * Multi-modal Fusion (Specific: RGB \+ Depth) \- \[e.g., Hui Lan 2024, Jiang Zhu 2024\]  
    * Hierarchical Feature Fusion/Collaboration \- \[e.g., Hui Lan 2024, Zhiwei Zhong 2021\]  
    * Attention Mechanisms (General concept) \- \[Ashish Vaswani 2017\]  
      * Multi-modal Attention Based Fusion (MMAF\* in AHMF) \- \[Zhiwei Zhong 2021\]  
      * Recurrent Structure Attention (SA\* in RSAG) \- \[Jiayi Yuan 2023\]  
      * Channel Attention (CA\* in RCAN) \- \[Yulun Zhang 2018\]  
      * Pixel Attention (PA\* in PAN) \- \[Hengyuan Zhao 2020\]  
      * Self-Attention (Core of Transformers) \- \[Ashish Vaswani 2017\]  
    *   
  *   
  * Feature Decomposition (Specific: Spherical Space\* for depth SR \- SSDNet\*) \- \[Zixiang Zhao 2023\]  
  * Feature Recombination (Specific: Adaptive module in PDR-Net\*) \- \[Peng Liu 2022\]  
*   
* D. Guidance Mechanisms  
  * Intensity/Color Guidance (Common for depth SR) \- \[Multiple papers\]  
  * Edge Guidance (Specific: DSRNet\*, LEDSRNet\*, Deep edge map guided SR\*) \- \[Hui Lan 2023, Hui Lan 2024, Zhongyu Jiang 2021\]  
  * Blurry Depth Guidance (Specific: DSRNet\*) \- \[Hui Lan 2023\]  
  * Latent Edge Guidance (Specific: LEDSRNet\*) \- \[Hui Lan 2024\]  
  * Structure Guidance (Specific: SGNet\*, RSAG\*) \- \[Zhengxu Wang 2023, Jiayi Yuan 2023\]  
  * Scene Structure Guidance (Specific: via cross-task transfer) \- \[Baoli Sun 2021\]  
* 

III. Specific Reconstruction/Enhancement Tasks

* A. Noise Reconstruction / Denoising  
  * Ultra-High Resolution Noise Reconstruction (Core topic) \- \[Elicit Topic\]  
  * Denoising (General task) \- \[Multiple papers\]  
  * Noise Suppression (Specific outcome) \- \[C. Birnie 2022\]  
  * Noise Reduction (General outcome) \- \[e.g., Achille Beysang 2024, K. Wegner 2010\]  
  * EMD noise removal approach\* (Specific method) \- \[Raghu.K Sharath.M 2016\]  
  * Exact Noise Variance Calculation (vs. approximations) \- \[Ymir Mäkinen 2019\]  
*   
* B. Super-Resolution (SR)  
  * Image Super-Resolution (General task) \- \[Multiple papers\]  
  * Depth Super-Resolution (Specific sub-task) \- \[Multiple papers\]  
  * Guided Depth Super-Resolution (Using auxiliary info, e.g., RGB) \- \[Multiple papers\]  
  * Single Depth Image Super-Resolution (No auxiliary guide) \- \[e.g., Jun Xie 2016, Baoli Sun 2021\]  
  * Video Super-Resolution \- \[Germán Mora-Martín 2022, Hongying Liu 2020\]  
*   
* C. Depth Map Processing (SR, Completion, Refinement, Estimation)  
  * Depth Map Enhancement/Refinement \- \[e.g., Y. Zuo 2021, Woo-Kyung Jung 2021\]  
  * Depth Map Restoration \- \[Haotian Wang 2022, Ying Gao 2023\]  
  * Depth Completion (Filling missing values) \- \[Xin Qiao 2024, Jinsun Park 2020\]  
  * Depth Estimation (Monocular, Stereo) \- \[e.g., Jiahao Shao 2024, Saurabh Saxena 2023, Samuel Brucker 2024\]  
  * Depth Boundary Distortion Modeling/Recovery\* \- \[Haotian Wang 2022\]  
*   
* D. Medical Image Reconstruction / Processing  
  * CT Reconstruction (General)  
    * Iterative Reconstruction (General class: AIDR 3D, ASIR-V, iDose4, Hybrid-IR, MBIR) \- \[Multiple papers\]  
    * Deep Learning Reconstruction (DLR / AiCE / TrueFidelity) (Novel class) \- \[Multiple papers\]  
    * Filtered Back Projection (FBP) (Classical reference) \- \[Multiple papers\]  
    * Deep-Learning-Based Super-Resolution Reconstruction (DLSRR)\* \- \[H. Sato 2023\]  
  *   
  * MRI Synthesis/Super-Resolution (Specific: using DDPM, U-Net) \- \[Chih-Wei Chang 2024, Levente Baljer 2024\]  
  * PET Reconstruction (Specific: Penalized ML with DOI rebinning\*) \- \[Kyungsang Kim 2018\]  
  * Ultrasound Denoising (Specific: using DDPM) \- \[Hojat Asgariandehkordi 2023\]  
*   
* E. Other Reconstruction Tasks  
  * Hologram Reconstruction (Specific: Compressed ultrafast holographic imaging) \- \[Zhao Ma 2023\]  
  * 3D Reconstruction (From images/depth) \- \[e.g., Noah Stier 2023, Zibin Liu 2021\]  
  * Shape-from-focus reconstruction\* (Specific method) \- \[Zhoumiao He 2023\]  
* 

IV. Data & Datasets

* A. Dataset Creation & Improvement  
  * Improved Training Datasets (General need) \- \[Language model\]  
  * High-Resolution Synthetic RGB-D Datasets\* (Specific contribution) \- \[Aakash Rajpal 2023\]  
  * Real-World Depth SR Benchmark Dataset (RGB-D-D)\* \- \[Lingzhi He 2021\]  
  * Ultra-High-Definition Low-Light Dataset (UHD-LL)\* \- \[Chongyi Li 2023\]  
  * High-Resolution Stereo Datasets\* (Specific contribution) \- \[D. Scharstein 2014\]  
*   
* B. Data Augmentation & Generation  
  * Enhanced Data Augmentation Techniques (General need) \- \[Language model\]  
  * Generation of additional hash-based filters\* (Specific technique) \- \[Ystallonne Alves 2019\]  
  * Synthetic Data Generation (General technique)  
*   
* C. Data Types & Characteristics  
  * Synthetic Data (Use in pre-training, evaluation) \- \[C. Birnie 2022\]  
  * Real-world Data (Use in evaluation, dataset creation) \- \[e.g., Lingzhi He 2021\]  
  * Multi-modal Data (RGB-D, etc.) \- \[Multiple papers\]  
  * Sparse Data (Specific challenge in depth completion/SR) \- \[e.g., Jinsun Park 2020\]  
  * Noisy Data (Core challenge) \- \[Multiple papers\]  
  * Data with Holes / Missing Data (Challenge in depth SR) \- \[Hanqi Fan 2015, Tingsheng Huang 2023\]  
* 

V. Evaluation & Metrics

* A. Quantitative Metrics  
  * PSNR (Peak Signal-to-Noise Ratio) \- \[e.g., Tingsheng Huang 2023\]  
  * SSIM (Structural Similarity Index) \- \[e.g., Ying Gao 2023\]  
  * RMSE (Root Mean Square Error) \- \[e.g., Hui Lan 2024\]  
  * NMSE (Normalized Mean Square Error) \- \[Raghu.K Sharath.M 2016\]  
  * NPS (Noise Power Spectrum) \- \[T. Wang 2016, J. Solomon 2020\]  
  * TTF (Task Transfer Function) \- \[H. Sato 2023, J. Greffier 2021\]  
  * Detectability Index (d') \- \[Achille Beysang 2024, H. Sato 2023\]  
  * MAE (Mean Absolute Error) \- \[e.g., Samuel Brucker 2024\]  
  * Relative root-mean-square error (Specific: for 1D-NPS) \- \[T. Wang 2016\]  
  * Computational Efficiency / Runtime / Model Parameters \- \[e.g., Hui Lan 2024\]  
*   
* B. Qualitative Assessment  
  * Visual Quality Comparison \- \[e.g., Hui Lan 2023, Hanqi Fan 2015\]  
  * Radiologist Evaluation / Subjective Scoring \- \[e.g., Achille Beysang 2024, Akiyoshi Hamada 2024\]  
*   
* C. Perceptual Quality  
  * Focus on Perceptual Quality Metrics (Future trend) \- \[Language model\]  
  * LPIPS (Learned Perceptual Image Patch Similarity) \- \[Jiaxin Gao 2023\]  
*   
* D. Benchmarking & Challenges  
  * Benchmark Datasets (Middlebury, NYU v2, KITTI, etc.) \- \[Multiple papers\]  
  * Challenges (e.g., AIM 2024, NTIRE 2023\) \- \[Marcos V. Conde 2024, Yawei Li 2023\]  
*   
* E. Specific Evaluation Findings  
  * Outperforms classical interpolation algorithms, improved PSNR by 3-10dB\* (Finding for fractional calculus/inv dist interp) \- \[Tingsheng Huang 2023\]  
  * Comprehensive quantitative comparisons show method outperforms existing approaches\* (Finding for sparse linear model) \- \[Hanqi Fan 2015\]  
  * Effectiveness under high noise levels compared to existing frameworks\* (Finding for nonlinear volumetric scale-space) \- \[A. Mishra 2011\]  
  * Improved structural separation and localization across all scales\* (Finding for nonlinear volumetric scale-space) \- \[A. Mishra 2011\]  
* 

VI. Hardware, Computing & Efficiency

* A. High-Performance Computing (HPC)  
  * Increased Use of High-Performance Computing (Trend) \- \[Language model\]  
  * GPU Acceleration (Mentioned in several papers) \- \[e.g., Germán Mora-Martín 2022\]  
*   
* B. Specialized Hardware  
  * Development of Specialized Hardware (Future trend) \- \[Language model\]  
  * SPAD Sensors (Single-Photon Avalanche Diode) (Specific hardware used) \- \[Germán Mora-Martín 2023, Germán Mora-Martín 2022\]  
*   
* C. Quantum Computing  
  * Exploration of Quantum Computing (Future trend) \- \[Language model\]  
  * Variational quantum computation for enhancing imagery\* (Specific application) \- \[Ystallonne Alves 2019\]  
  * Variational Quantum Eigensolver (VQE)\* (Specific algorithm used) \- \[Ystallonne Alves 2019\]  
*   
* D. Real-Time Processing & Efficiency  
  * Real-Time Noise Reconstruction (Future trend) \- \[Language model\]  
  * Real-Time Depth Processing (Goal of challenge) \- \[Marcos V. Conde 2024\]  
  * Computational Efficiency (Goal/Benefit of methods like RAISR, UltraPixel, ESPCN) \- \[Ystallonne Alves 2019, Jingjing Ren 2024, Wenzhe Shi 2016\]  
* 

VII. Application Domains

* Gaming & Virtual Reality (VR) \- \[Language model, Marcos V. Conde 2024, Hui Lan 2023\]  
* Augmented Reality (AR) \- \[Language model, Marcos V. Conde 2024\]  
* Medical Imaging  
  * Computed Tomography (CT) (Temporal Bone, Head & Neck, Pulmonary, Cardiac, Abdominal, Spine, etc.) \- \[Multiple papers\]  
  * Magnetic Resonance Imaging (MRI) (Brain, Prostate) \- \[Chih-Wei Chang 2024, Levente Baljer 2024\]  
  * Positron Emission Tomography (PET) \- \[Kyungsang Kim 2018\]  
  * Ultrasound (US) \- \[Hojat Asgariandehkordi 2023\]  
  * Otorhinolaryngology \- \[Christos Tsilivigkos 2023\]  
*   
* Geophysical Imaging (Specific: Full-Waveform Inversion \- FWI) \- \[I. Espin 2023\]  
* Autonomous Driving / Navigation \- \[Samuel Brucker 2024, Hui Lan 2023, Xiaozhi Chen 2016\]  
* Lithography Metrology (Specific: High NA EUV) \- \[Minjung Kim 2023\]  
* Spacecraft Reconstruction (Specific: Uncooperative spacecraft) \- \[Zibin Liu 2021\]  
* Film & Video Game Production (Environmental noise simulation) \- \[Language model\]  
* Robotics \- \[I. Gyongy 2020\]  
* Face Recognition/Tracking \- \[Gang Pan 2005, Q. Cai 2010\]

VIII. Broader Concepts & Future Directions

* A. Quality Improvement Goals  
  * Explore performance improvements, produce sharper images, learn powerful filters\* (Goal description) \- \[Ystallonne Alves 2019\]  
  * Improved structural separation and localization\* (Specific goal/outcome) \- \[A. Mishra 2011\]  
  * Provides more texture information\* (Specific goal/outcome) \- \[Tingsheng Huang 2023\]  
  * Temporal consistency (Goal in video/depth processing) \- \[K. Wegner 2010, Jiahao Shao 2024\]  
  * Increased Focus on Temporal Noise Patterns (Future trend) \- \[Language model\]  
*   
* B. Robustness & Reliability  
  * Effectiveness under high noise levels\* (Specific benefit) \- \[A. Mishra 2011\]  
  * Focus on Robustness Against Adversarial Attacks (Future trend) \- \[Language model\]  
  * Handling "Hidden Noise" in Reference Data\* (Challenge identified) \- \[Jiayang Wang 2024\]  
*   
* C. User Focus & Interaction  
  * Incorporation of User Interaction (Future trend) \- \[Language model\]  
  * User-Centric Design Principles (Future trend) \- \[Language model\]  
  * Collaborative Filtering Approaches (Leveraging user feedback) \- \[Language model\]  
*   
* D. Interdisciplinary Aspects  
  * Interdisciplinary Research Collaborations (Future trend) \- \[Language model\]  
  * Cross-Modal Learning (Future trend) \- \[Language model\]  
  * Integration of AI and Traditional Techniques (Future trend) \- \[Language model\]  
*   
* E. Ethical & Sustainability Concerns  
  * Ethical Considerations in Noise Reconstruction (Future trend) \- \[Language model\]  
  * Focus on Sustainability (Future trend) \- \[Language model\]  
*   
* F. Standardization  
  * Standardization of Noise Reconstruction Protocols (Future trend) \- \[Language model\]  
*   
* G. Foundational Research  
  * Exploration of Non-Linear Noise Models (Future trend) \- \[Language model\]  
* 

