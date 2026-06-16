 Generative Adversarial Networks (GANs)

* A. Core Concept & General Variants  
  * Generative Adversarial Networks (GANs) \- Core Concept  
  * Conditional GANs (cGANs) \- Core Concept & Applications  
    * Landmark-Guided cGAN (LGcGAN) \- Face Aging variant  
    * Recursive Conditional Generative Adversarial Networks \- Video transformation variant  
    * cGANs with Auxiliary Discriminative Classifier (ADC-GAN) \- Addresses AC-GAN issues  
    * ControlGAN \- Separates classifier for better control  
    * S2cGAN \- Semi-supervised training variant  
    * c+GAN \- Complementary fashion item recommendation  
  *   
  * Wasserstein GAN (WGAN) & Variants  
    * WGAN-GP (Gradient Penalty) \- Enhanced WGAN  
  *   
  * Least Squares GANs (LSGANs)  
    * LSGANs-GP (Gradient Penalty)  
  *   
  * Information Maximizing GAN (InfoGAN) \- For interpretable representation learning  
  * Bidirectional GANs (BiGANs) \- Learns inverse mapping (data to latent space)  
    * BigBiGAN \- Large scale version for representation learning  
  *   
  * Vari GAN, Temporal GAN (TGAN), Laplacian GAN (LAPGAN), VGAN, FCGAN \- Mentioned GAN variants  
*   
* B. Image Generation & Synthesis GANs  
  * Deep Convolutional GAN (DCGAN)  
    * BoolGAN \- DCGAN improvement with Wasserstein loss & dropout  
    * Anysize GAN \- Handles varying image sizes  
  *   
  * Progressive Growing GAN (PGGAN)  
    * D2PGGAN \- Uses two discriminators  
  *   
  * StyleGAN & Variants  
    * StyleGAN \- Core Concept & Architecture  
    * StyleGAN2 \- Improved version  
      * StyleSpace Analysis \- Disentangled control analysis  
      * StyleGAN2 Distillation \- For feed-forward manipulation  
      * KinStyle \- For kinship face synthesis  
      * StyleT2F \- Text-to-Face generation variant  
      * StyleDisentangle \- Disentangled editing  
    *   
    * StyleGAN3 \- Improved equivariance  
    * MobileStyleGAN \- Lightweight version  
    * MultiStyleGAN \- Multiple one-shot face stylizations  
    * StyleFusion \- Fuses multiple latent codes  
    * UMMGAN \- Unsupervised multi-modal styled content  
    * StyLitGAN \- Lighting and color control  
    * StyleFlow \- Attribute-conditioned exploration  
  *   
  * Multi-Scale Gradient GAN (MSG-GAN) \- Stable multi-scale synthesis  
  * Self-Attention GAN (SAGAN) \- Incorporates attention mechanisms  
  * Spatial GAN (SGAN) \- Texture synthesis focus  
    * Spatial Steerability in GANs \- Self-supervised control  
    * Spatial-Semantic Modulation GAN \- Text-to-image synthesis with spatial/semantic control  
    * GANs Spatial Control via Inference-Time Adaptive Normalization \- Test-time spatial control  
  *   
  * BigGAN \- Large scale, high-fidelity generation  
  * Text-to-Image Generation GANs  
    * AttnGAN (Attentional GAN)  
      * DenseNet architecture with AttnGAN \- Improved efficiency  
      * AttnGAN-DAMSM model \- High-resolution focus  
    *   
    * DualAttn-GAN \- Dual attention for local/global details  
    * SSA-GAN (Semantic-Spatial Aware GAN) \- Integrates spatial/semantic info  
    * TextControlGAN \- Regressor for text feature control  
  *   
  * Fine-Grained Control of Artistic Styles in Image Generation \- Technique  
  * LSN-GAN \- Least Square Gradient Normalization variant  
  * Semi-Supervised Learning with GANs \- Discriminator outputs class labels  
*   
* C. Image-to-Image Translation & Domain Adaptation GANs  
  * Pix2Pix \- Conditional GAN for paired data  
    * Pix2PixHD \- High-resolution version  
    * Differential Image Pix2Pix Model \- Enhances constraints  
    * Improved Conditional GANs (for Pix2Pix tasks)  
  *   
  * CycleGAN (Cycle-Consistent Adversarial Networks) \- For unpaired data  
    * Conditional CycleGAN \- Handles unpaired data with attribute control  
    * Enhanced CycleGAN (ECycleGAN) \- Improved architecture/loss  
    * Enhanced CycleGAN with Self-Attention \- For single-image dehazing  
    * Long CycleGAN \- Cascaded generators  
  *   
  * DualGAN \- Unsupervised dual learning  
  * DucGAN (Dual-cycle consistent GAN) \- Restrains error accumulation  
  * StarGAN \- Multi-domain translation with single model  
    * SuperstarGAN \- Handles large-scale domains  
    * LAUN improved StarGAN \- Contextual loss & Attention U-Net  
    * EStarGAN \- High-definition multi-style translation  
  *   
  * FUNIT (Few-Shot Unsupervised Image-to-Image Translation)  
  * UniTranslator \- Universal domain translation with single StyleGAN  
  * Genetic-GAN \- Synthesizing images between two domains  
  * ImaGAN \- Transfers style while preserving content structure  
*   
* D. Image Restoration & Enhancement GANs  
  * Super-Resolution GAN (SRGAN)  
    * Enhanced Super-Resolution GAN (ESRGAN)  
      * Residual-in-Residual Dense Block (RRDB) \- Key ESRGAN component  
      * ERDBNet \- Uses Enhanced Residual Dense Block  
      * CA-ESRGAN \- Channel Attention variant  
      * MSA-ESRGAN \- Multi-scale attention U-Net discriminator variant  
      * Real-ESRGAN / Real-ESRNET \- Related models/components  
    *   
    * StarSRGAN \- Blind super-resolution variant  
  *   
  * Image Inpainting GANs  
    * AOT-GAN (Aggregated Contextual-Transformation GAN) \- High-res inpainting  
    * Neural Fill \- Content-aware fill  
    * Block-wise Procedural Training GAN \- For photo-realistic inpainting  
    * Boosted GAN with Semantically Interpretable Information \- Semantic consistency focus  
    * Inpainting GAN-Based Image Blending with Adaptive Binary Mask \- Reduces unnatural edges  
  *   
  * Image Denoising GANs  
  * Image Colorization GANs  
    * ColorGAN \- Auto colorization with attention  
    * ChromaGAN \- Adversarial with semantic class distribution  
    * Colorized Latent-Based cGAN (CL-cGAN) \- Fine-tuning color  
  *   
  * Image Blending GANs  
    * GP-GAN \- Gaussian-Poisson GAN for high-res blending  
    * BlendGAN (Arbitrary Stylized Face Generation) \- Implicit blending  
    * BlendGAN (Single Image Internal Distributions) \- Spatial conditioning  
    * Blending GAN (with Rendering) \- Combines synthesis and rendering  
    * Composite GAN \- Generates parts combined via alpha blending  
    * Blender-GAN \- Multi-target conditional generation  
  *   
  * Texture Synthesis GANs  
    * Spatial GAN (SGAN) \- Well-suited for texture synthesis  
    * WBT-GAN (Wavelet-based GAN) \- Leverages wavelet representations  
    * TextureWGAN \- Preserves texture in CT inverse problems  
    * User-Controllable Multi-Texture Synthesis GAN  
    * Texturize a GAN Using a Single Image \- Adaptation technique  
  *   
  * GAN-Based Image Restoration (General)  
    * Physics-Based GANs \- For deblurring, dehazing, deraining  
    * Residual U-Net GAN (RUGAN/RUCGAN) \- For restoring damaged photos  
  *   
  * Image Enhancement GANs (General)  
    * Old Photos Restoration GAN  
  *   
*   
* E. 3D Generation & Reconstruction GANs  
  * 3D GANs \- Core Concept  
    * Voxel-based 3D GAN \- Original 3D-GAN  
    * Stacked GAN for 3D Shapes  
    * 3D-RecGAN \- Reconstruction from single depth view  
    * Volumetric Imitation GAN (VI-GAN) \- Anatomical modeling  
    * Weakly Supervised GAN (WS-GAN) \- Reduces reliance on 3D supervision  
    * Controllable Point Cloud GAN (CPCGAN) \- Generates point clouds with semantic labels  
    * SinGAN-3D \- Generation from single voxelized model  
    * SliceGAN \- Generates 3D structures from 2D slices  
    * 3D-FGAN \- Fast generation of digital core images  
    * 3D-aware GANs \- General concept for view synthesis  
      * In-N-Out GAN Inversion \- Faithful 3D GAN inversion  
    *   
    * Volumetric GAN (for SAS data)  
    * 3D DCGAN \- Used for lung tissue modeling  
    * 3D bigGAN \- Used for lung tissue modeling  
    * SDF-based 3D GANs \- Uses differentiable SDF rendering  
    * 3DGEN \- NeRF and GAN hybrid for novel 3D models  
  *   
  * 3D Face Generation & Translation GANs  
    * MeshGAN \- Operates directly on 3D face meshes  
    * 3DFaceGAN \- Models distribution of 3D facial surfaces  
    * AniFaceGAN \- Animatable 3D-aware face generation  
    * Multi-column Graph Convolutional Networks (MGCNs) for 3D Faces  
    * FaceVision-GAN \- 3D reconstruction from single image  
    * 3D-GANTex \- StyleGAN3 and 3DDFA based reconstruction  
    * Landmark-Guided cGANs (LGcGAN) \- Face aging  
  *   
  * Image-to-Voxel Model Translation GAN  
*   
* F. Hybrid GAN Approaches  
  * VAE-GAN Hybrids \- Combines VAE inference and GAN generation  
    * VAEGAN \- Core Concept  
    * CVAE-GAN \- Fine-grained image generation  
    * Self-Supervised Adversarial Variational Learning (SS-AVL)  
    * InfoVAEGAN \- Joint interpretable representations  
    * VAE-QWGAN \- Hybrid Quantum WGAN variant  
    * GAN-VAE \- Addresses GAN image sharpness issues  
    * Two-Channel VAE-GAN \- Image-to-Video translation  
    * Hybrid Deep Generative Models (VAE-GAN for PV data)  
  *   
  * GAGAN \- Hybrid optimization with Genetic Algorithms and DCGAN  
  * GANs integrated with NeRF  
  * GANs integrated with Diffusion Models  
    * DuDGAN (Dual-Diffusion GAN) \- Improves class-conditional GANs  
    * StyleGAN-Fusion \- Diffusion guided domain adaptation  
  *   
*   
* G. GAN Components, Techniques & Concepts  
  * Generator Network  
  * Discriminator Network  
    * PatchGAN Discriminator  
    * Spatio-temporal discriminator  
    * Multi-Scale Discriminator  
    * Lightweight ensemble discriminator  
    * Auxiliary Classifier (AC-GAN, ACGAN)  
  *   
  * Loss Functions  
    * Adversarial Loss  
    * Cycle Consistency Loss  
    * Perceptual Loss  
    * Wasserstein Loss  
    * Least Squares Loss  
    * Identity Loss (Positive/Negative)  
    * Idempotence Loss  
    * Gradient Penalty  
    * Ensemble loss function  
    * Ping-Pong loss (for temporal artifacts)  
    * Semantic consistency loss  
  *   
  * Training Techniques  
    * Adversarial Training  
    * Progressive Growing of GANs  
    * Multi-Scale Training  
    * Spectral Normalization  
    * Batch Normalization / Conditional Batch Normalization  
    * Instance Normalization / Adaptive Instance Normalization (AdaIN)  
    * Two Time-Scale Update Rule (TTUR)  
    * Label Smoothing  
    * Noise Injection  
    * Mini-batch Standard Deviation  
    * Gradient Normalization (LSN-GAN)  
    * Mode Seeking Regularization  
    * Double-cycle training strategy  
  *   
  * Architecture Components  
    * Self-Attention Mechanisms (SAGAN)  
    * Attention Mechanisms (General/Spatial/AttnGAN/DualAttn-GAN)  
    * Residual Blocks  
    * Convolutional Layers / Deep Convolutional Networks (DCGAN)  
    * Transposed Convolutions  
    * U-Net Architecture (in Generator/Discriminator)  
    * Graph Convolutional Networks (GCNs) (MeshGAN, MGCNs)  
    * Style-Based Generator (StyleGAN)  
    * Mapping Network (StyleGAN)  
  *   
  * Latent Space  
    * Latent Space Exploration / Interpolation / Arithmetic  
    * Latent Space Regularization (LSR-GAN)  
    * Disentangled Latent Space (InfoGAN, StyleGAN)  
    * StyleSpace (StyleGAN)  
    * W+ Space (StyleGAN)  
    * SS Space (StyleGAN)  
    * GAN Inversion (Projecting images to latent space)  
  *   
  * Conditioning Mechanisms  
    * Conditional Input (cGANs)  
    * Text Conditioning (Text-to-Image)  
    * Class Conditioning  
    * Attribute Conditioning  
    * Layout/Structure Conditioning  
    * Spatial Conditioning / Control  
    * Semantic Conditioning  
  *   
  * Evaluation Metrics  
    * Inception Score (IS)  
    * Fréchet Inception Distance (FID)  
    * Kernel Inception Distance (KID)  
    * Precision and Recall score  
    * Peak Signal-to-Noise Ratio (PSNR)  
    * Structural Similarity Index (SSIM)  
  *   
  * Challenges  
    * Mode Collapse  
    * Training Instability  
  *   
* 

II. Variational Autoencoders (VAEs)

* A. Core Concept & General Variants  
  * Variational Autoencoders (VAEs) \- Core Concept  
  * β-VAE \- Disentanglement focus  
  * Conditional VAE (CVAE) \- Conditioned generation  
    * CGA (Control, Generate, Augment) \- Multi-attribute text generation framework  
    * SepaCVAE \- Self-separated for dialogue response  
    * Edit-CVAE (ECVAE) \- Condition enhancing/lexical editing  
    * Conditional Subspace VAE (CSVAE) \- Extracts label-correlated features  
    * Classifying VAE (CCVAE) \- Captures label characteristics explicitly  
  *   
  * Vector Quantized VAE (VQ-VAE) & VQ-VAE-2 \- Discrete latent representations  
    * Rate-Adaptive VQ-VAE (RAQ-VAE) \- Adaptive codebook representation  
    * Diffusion bridges VQ-VAE \- End-to-end training extension  
  *   
  * Importance Weighted Autoencoder (IWAE) \- Tighter likelihood bound  
  * Ladder VAE \- Recursive generative correction  
  * Variational Denoising Autoencoder (VDAE) \- Generalizes normalizing flows  
  * Tensor-variate Gaussian Process Prior VAE (tvGP-VAE) \- Tensor-variate priors  
  * Mixtures of VAEs \- For cluster analysis  
    * Gaussian Mixture VAEs (GMVAE)  
  *   
  * Nouveau VAE (NVAE) \- Hierarchical VAE mentioned w.r.t. regularization  
  * Located-VAE (LVAE) & Prior-VAE (PVAE) \- Connects segments to known 3D objects  
  * ITL-AE \- Mentioned VAE variant  
*   
* B. VAEs with Learned/Structured Latent Spaces  
  * Variational Autoencoder with Learned Latent Structure (VAELLS) \- Learns manifold structure for prior  
  * VAEs with Jointly Optimized Latent Dependency Structure \- Learns Bayesian network structure  
  * VAEs with Latent Superstructures \- For deep multidimensional clustering  
  * Hierarchical Non-parametric VAEs \- Tree-structured Bayesian priors  
  * Tree-Structured VAE \- For tree-structured data (e.g., code)  
  * Poincaré VAEs \- Hyperbolic latent space for hierarchies  
  * Decomposable VAEs for Latent Structural Relations \- Message passing prior  
  * Hub-VAE \- Unsupervised hub-based regularization  
  * Attribute-based Regularization of VAE Latent Spaces  
  * VAEs with Sparse Labels \- Unified unsupervised/semi-supervised/supervised framework  
  * Cross-population VAEs \- Isolating shared/private factors  
  * VAEs with Automatic Latent Variable Selection  
*   
* C. VAEs for Specific Data Types & Tasks  
  * Variational Graph Auto-Encoder (VGAE) \- For graph-structured data  
    * Semi-Implicit Graph VAE (SIG-VAE) \- More flexible graph modeling  
  *   
  * VAE-RNNLM \- Text generation  
  * Stable VAE for Text Modelling  
  * 3D Voxel Generation VAEs  
    * Voxel-based Variational Autoencoders \- Core concept  
    * 3D ShapeNets \- Early VAE-like model for 3D shapes  
    * VoxGen \- Based on autoencoder framework  
    * Variational Shape Learner (VSL) \- Hierarchical latent model for voxels  
    * Contour-based 3D Modeling VAE \- Joint embedding of shapes/contours  
    * Sparse AutoEncoder (SAE) for 3D Voxel Reconstruction  
  *   
  * Multi-Modal VAEs  
    * Associative VAE (AVAE) \- Distributed latent spaces with associators  
    * Disentangled Multi-modal VAE (DMVAE) \- Separates private/shared spaces  
    * Mixture-of-Experts Multi-Modal VAE (MMVAE) \- Expert-based learning  
    * Multimodal Generative Models (General VAE/GAN/Flow based)  
    * Conditional generation of multi-modal data using constrained embedding space mapping  
  *   
  * Variational Transfer Learning using Cross-Domain Latent Modulation  
  * Contrastive VAE (cVAE) \- Enhances salient features  
  * VAEs for Temporal Point Processes with Dynamic Latent Graphs  
  * TE-based VAEs \- Transfer entropy in loss for IoT data  
  * VAE for Molecular Simulation Analysis  
*   
* D. VAE Components, Techniques & Concepts  
  * Encoder-Decoder Architecture  
  * Latent Space / Latent Variables / Latent Representations  
    * Latent Space Characterization (CAE, DAE, VAE)  
    * Latent Space Arithmetic (LSA)  
    * Disentangled Representations  
    * Hierarchical Latent Representations  
    * Discrete Latent Representations (VQ-VAE)  
    * Continuous Latent Representations  
  *   
  * Loss Function (ELBO \- Evidence Lower Bound)  
    * Reconstruction Loss  
    * KL Divergence Regularization  
    * Mutual Information Regularization  
    * Attribute Regularization Loss  
  *   
  * Prior Distribution (e.g., Gaussian, Mixture of Gaussians, Hyperbolic)  
  * Posterior Distribution / Variational Distribution  
  * Regularization Techniques  
    * Consistency Regularization  
    * Hub-based Contrastive Loss  
    * Sparsity Enforcement (Spike and Slab)  
    * Minimum Information Constraint  
  *   
  * Variational Inference  
  * Reparameterization Trick  
  * Recognition Network  
  * Generative Model / Decoder  
  * Codebook (VQ-VAE)  
  * Commitment Loss (VQ-VAE)  
  * Skip Connections (Generative Skip Models)  
* 

III. Diffusion Models

* A. Core Concepts & Foundational Models  
  * Diffusion Models \- Core Concept  
  * Denoising Diffusion Probabilistic Models (DDPMs)  
  * Denoising Diffusion Implicit Models (DDIMs)  
    * Generalized DDIM (gDDIM)  
  *   
  * Score-Based Generative Models (related via SDE formulation)  
  * Latent Diffusion Models (LDMs) \- Operate in latent space  
*   
* B. Specific Diffusion Model Variants & Architectures  
  * Stable Diffusion \- Widely used text-to-image LDM  
  * Imagen \- Text-to-image, emphasizes photorealism  
  * DALL-E 2 \- Text-to-image, diffusion-based  
  * GLIDE (Guided Language to Image Diffusion) \- Text-guided generation/editing  
  * DeepFloyd-IF \- Pixel-based text-to-image  
  * Paella \- Mentioned text-to-image model  
  * SODA \- Self-supervised diffusion for representation learning  
  * Hierarchical Diffusion Autoencoders (HDAE) \- Coarse-to-fine latent hierarchy  
  * Diffusion Vision Transformers (DiffiT) \- ViT architecture for diffusion  
  * GenTron \- Transformer-based diffusion for image/video  
  * VQ-Diffusion \- Combines VQ-VAE latent space with DDPM  
  * Blurring Diffusion Models (BDM) \- Alternative to Gaussian diffusion  
  * Critically-damped Langevin diffusion model (CLD) \- Augments with velocity  
  * Simple diffusion \- End-to-end high-resolution diffusion  
  * Nested diffusion models \- Hierarchical generative framework  
  * Vector Quantized Diffusion (VQ-Diffusion)  
  * JVID (Joint Video-Image Diffusion) \- Combines image and video diffusion  
  * Hierarchically branched diffusion models \- Class-conditional generation  
  * Text2Earth \- For remote sensing scenes  
  * Factorized Diffusion Architectures \- Unsupervised generation/segmentation  
  * ControlMol \- Sub-structure control for molecule generation  
*   
* C. Diffusion Model Techniques & Concepts  
  * Denoising Process / Reverse Diffusion  
  * Noise Schedule / Time Step Sampling (Beta Sampling)  
  * Guidance Techniques  
    * Classifier Guidance  
    * Classifier-Free Guidance  
    * Self-Attention Guidance (SAG)  
    * CLIP Guidance  
    * Semantic Guidance (SEGA)  
    * Geometric guidance (GeoGuide)  
    * Feature-guided score diffusion  
    * Self-Guided Diffusion Models  
  *   
  * Conditional Generation  
    * Text Conditioning (Text-to-Image)  
    * Class Conditioning  
    * Attribute Conditioning  
    * Mask Conditioning  
    * Anatomically-Controllable Generation (Medical Imaging)  
  *   
  * Image Restoration & Enhancement  
    * Residual Denoising Diffusion Models  
    * Restoration by Generation with Constrained Priors  
    * Pixel-Aware Stable Diffusion (PASD) \- Super-resolution/stylization  
    * ADORE (Adaptive Diffusion Optimized Restoration) \- Facial imagery  
  *   
  * Image Manipulation & Editing  
    * DiffusionCLIP \- Text-guided manipulation  
    * Imagen Editor \- Text-guided inpainting  
    * VIPaint \- Inpainting via variational inference  
    * Noise Crystallization / Liquid Noise \- Zero-shot video generation  
    * DIFF-NST \- Deformable neural style transfer  
    * Plug-and-Play Diffusion Features \- Text-driven image-to-image  
  *   
  * Training & Optimization  
    * Compensation Sampling \- Improved convergence  
    * Constrained Diffusion Models (via Dual Training) \- Bias reduction  
    * RL Fine-tuning for Diversity  
  *   
  * Latent Space (in LDMs)  
  * Stochastic Differential Equations (SDE) Formulation  
*   
* D. Control Mechanisms (often used with Diffusion Models)  
  * ControlNet & Variants  
    * ControlNet \- Core Concept  
    * ControlNet++ \- Improved conditional controls  
    * LooseControl \- Generalized depth conditioning  
    * VideoControlNet \- Motion-guided video translation  
    * Music ControlNet \- Time-varying music control  
    * Depth-conditional ControlNet  
    * ControlNet Hough Model \- Interior design application  
  *   
  * Conditioning Inputs (Segmentation masks, Depth maps, Edge maps, Pose, Sketch)  
  * Spatial Control Techniques  
  * Semantic Control  
  * Attribute Control  
  * Style Control (PARASOL)  
  * Pose Control (Text-to-Pose)  
  * Expression Control (EmojiDiff)  
  * Lighting Control (LumiSculpt)  
  * Melody Control (Music Generation)  
  * Sub-structure Control (ControlMol)  
  * Continuous 3D Words \- Token-based control  
  * TICondition \- Multi-modal condition control  
  * Adaptively Controllable Diffusion (AC-Diff) Model \- Automatic process control  
* 

IV. Autoregressive Models

* A. Core Concepts & Foundational Models  
  * Autoregressive Models \- Core Concept  
  * PixelCNN \- Image generation  
    * Conditional PixelCNN  
    * Latent Variable PixelCNNs  
    * Spatial PixelCNN  
  *   
  * PixelSNAIL \- PixelCNN with attention  
  * WaveNet \- Audio generation  
  * Neural Autoregressive Distribution Estimator (NADE)  
  * Recurrent Neural Networks (RNNs) / LSTMs / GRUs \- Sequential data  
*   
* B. Transformer-based Autoregressive Models  
  * Transformer-XL \- Longer context via recurrence  
  * GPT Series (GPT, GPT-2, GPT-3, GPT-4) \- Language modeling & generation  
    * ImageGPT \- GPT applied to image generation  
    * VL-GPT \- Vision-Language GPT  
    * Lumina-mGPT \- Multimodal autoregressive model  
    * DistilGPT \- Distilled version  
    * Control-GPT \- Guides diffusion models via GPT-4 sketches  
  *   
  * BERT (adapted for generation)  
    * BERTGen \- Multimodal/multilingual extension  
  *   
  * T5 (Text-to-Text Transfer Transformer)  
  * XLNet \- Permutation-based bidirectional context  
  * Transformer (General use in vision/time series)  
    * Colorization Transformer  
    * Hierarchical Transformer with probabilistic decomposition \- Time series  
    * Temporal Fusion Transformer (TFT) \- Multivariate time series  
  *   
  * DiGIT (Discrete Image Tokenizer for Autoregressive Models)  
    * Spectral Image Tokenizer \- Alternative tokenization  
  *   
  * DART (Denoising Autoregressive Transformer) \- Scalable text-to-image  
  * CART (Compositional Auto-Regressive Transformer) \- Image generation  
  * 2-Dimensional Autoregression (DnD) Transformer \- Fine-grained image generation  
  * Stackformer \- Predicts code & position (used with VQ-VAE)  
  * RQ-Transformer \- Predicts code stacks (used with RQ-VAE)  
    * Contextual RQ-Transformer \- Considers global context  
  *   
*   
* C. Autoregressive Techniques & Concepts  
  * Next Token Prediction (NTP) / Next Pixel Prediction  
  * Next Patch Prediction (NPP) \- More efficient paradigm  
  * Relative Pixel Prediction \- Predicts relative changes  
  * Hierarchical Autoregressive Image Models  
  * Reinforced Adversarial Learning (RAL) \- Addresses limitations  
  * Visual Tokenization  
  * Conditional Generation (Text-to-Image, Class-Conditional)  
    * VAR-CLIP \- Visual Auto-Regressive with CLIP  
    * LlamaGen \- LLM paradigm for image generation  
  *   
  * Applications: Image Generation, Video Generation, Image Editing, Motion Generation, Colorization, Super-Resolution, Text Generation, Time Series Forecasting  
* 

V. Transformers for Vision (Non-Autoregressive Focus)

* A. Core Vision Transformer (ViT) & Variants  
  * Vision Transformer (ViT) \- Core Concept  
  * Data-Efficient Image Transformer (DeiT)  
    * DeiT-LT \- Training on long-tailed datasets  
  *   
  * Pyramid Vision Transformer (PVT)  
  * Swin Transformer \- Shifted windows  
    * Swin UNETR \- Medical image segmentation  
    * FSwin Transformer \- Feature-space window attention  
    * Swinv2-Imagen \- Used in text-to-image diffusion  
  *   
  * Multiscale Vision Transformers (MViT) \- Hierarchical features  
  * CrossViT \- Dual-branch multi-scale attention  
  * Tokens-to-Token Vision Transformer (T2T-ViT) \- Progressive tokenization  
  * CSWin Transformer \- Cross-Shaped windows  
  * Efficient Vision Transformer (MLVT) \- Dynamic multi-scale embedding  
  * Segmenter \- ViT for semantic segmentation  
  * SegFormer \- Hierarchical transformer with MLP decoder  
  * Semantic Vision Transformers (sViT) \- Leverages segmentation/semantics  
  * Vision Conformer (ViC) \- Incorporates convolutions  
  * Residual Vision Transformer (Res-Vit) \- Introduces residual connections  
  * Simple3D-Former \- Minimalist 3D adaptation  
  * Foveated Transformer (FoveaTer) \- Models foveated vision  
  * Laplacian-Former \- Enhances self-attention with frequency info  
  * EfficientFormer \- Low-cost alternative  
  * ICViT \- Integrates decomposition strategies  
  * 3DTextureTransformer \- Geometry-aware texture generation  
*   
* B. Multi-Modal & Cross-Modal Transformers  
  * Multi-Level Transformers (ML-Trans) \- Component of MSFNet  
  * Crossmodal Fusion Transformer (CFTrans) \- Component of MSFNet  
  * Global-Context Augmented Transformer (GCATrans) \- Component of MSFNet  
  * Multi-modal Transformer (MT) \- General concept for video/image captioning  
  * Hierarchical Multi-modal Transformer (HMT) \- Cross-modal long document classification  
  * Hierarchical Multimodal Transformer (Video Summarization)  
  * Cross-modal Memory Transformer (CMT) \- Medical report generation  
  * Cross-Attention Contextual Transformer (CACT-MCL-MMC) \- Image-text classification  
  * Multimodal Graph Transformer \- Multimodal QA  
  * Cross-Attentive Multi-modal Fusion framework (CAMF) \- fMRI/sMRI fusion  
  * TransFusion (Transformer-Based End-to-End Fusion) \- Medical image fusion  
  * Adaptive Fusion Transformer (AFTR) \- Multi-sensor fusion for 3D object detection  
  * Multi-way Multimodal Transformer (MMT) \- Simultaneous multiway correlations  
  * Multi-Scale Interactive Transformer (MSIT) \- Remote sensing cross-modal retrieval  
  * Deep Fusion Transformer (DFT) \- Image captioning  
  * Multi-Level Multimodal Transformer (MLMM-Trans) \- Multimodal recipe comprehension  
  * Crossmodal Multiscale Fusion Network (CMTrans/MCATrans) \- Remote sensing segmentation  
  * Multilevel Transformer (Multimodal Emotion Recognition)  
  * Multi-modal Transformer (MTrans) \- Accelerated MR imaging  
  * Multi-Modal Fusion Transformer (Video Retrieval) \- Modality agnostic  
  * Cross-Modal Transformers (CMTFusion) \- Infrared/visible image fusion  
  * Multi-scale Cooperative Multimodal Transformer (MCMulT) \- Multimodal sentiment analysis  
  * Exchanging-based Multimodal Fusion with Transformer (MuSE/CrossTransformer)  
  * FTransUNet \- Multilevel multimodal fusion for segmentation  
  * ViSTA (Vision and Scene Text Aggregation) \- Cross-modal retrieval  
  * Cascading Fusion Cross-attention Model (CFCM) \- Visual-textual retrieval  
  * MMT4 (Multi Modality To Text Transfer Transformer) \- Generative text/vision  
  * MultiFuser \- Multimodal driver action recognition  
*   
* C. Transformer Components & Techniques for Vision  
  * Patch Embedding / Tokenization  
  * Self-Attention / Multi-Head Attention  
    * Linear Self-Attention  
    * Local Attention Enhancement  
    * Shifted Window Multi-Head Self-Attention (SW-MSA)  
    * Cross-Shaped Window Self-Attention  
    * Hydra Attention \- Efficient many-headed attention  
    * Multi-head Mutual Self-attention (MHMSA) \- Texture synthesis  
    * U-Attention Mechanism \- Texture synthesis  
  *   
  * Positional Encoding  
  * Transformer Encoder / Decoder Blocks  
  * Feed-Forward Networks (within Transformer blocks)  
  * Layer Normalization  
  * Residual Connections  
  * Classification Token (CLS Token)  
  * Hierarchical Architectures  
  * Vision and Scene Text Aggregation  
* 

VI. Neural Radiance Fields (NeRF) & Novel View Synthesis

* A. Core NeRF Concept & Components  
  * Neural Radiance Fields (NeRF) \- Core Concept  
  * Continuous Volumetric Scene Function  
  * 5D Coordinate Input (Spatial Location \+ Viewing Direction)  
  * Volume Density Prediction  
  * View-Dependent Emitted Radiance Prediction  
  * Volume Rendering / Ray Marching / Ray Casting  
  * Positional Encoding  
  * Hierarchical Sampling / Coarse-to-Fine Sampling  
  * Differentiable Rendering  
*   
* B. NeRF Variants & Enhancements  
  * Mip-NeRF & Variants \- Anti-aliasing & multi-scale  
    * Mip-NeRF 360 \- Unbounded scenes  
    * Mip-Grid \- Grid-based anti-aliasing  
    * Mip-VoG \- Explicit multi-scale voxel grid  
  *   
  * Voxel-based NeRF Variants  
    * Neural Sparse Voxel Fields (NSVF)  
    * Sparse Voxel-based NeRF (Camera/LiDAR fusion)  
    * Vox-Surf \- Voxel-based implicit surface  
    * VaxNeRF \- Voxel-accelerated with visual hull  
    * DeepVoxels / DeepVoxels++ (related concept)  
    * CVT-xRF \- Contrastive in-voxel transformer for sparse inputs  
  *   
  * Grid-based NeRF Acceleration  
    * PlenOctrees \- Octree-based real-time rendering  
    * Sparse Neural Radiance Grid (SNeRG) \- Baked NeRF for real-time  
    * TensoRF (mentioned w.r.t. Mip-Grid)  
    * K-Planes (mentioned w.r.t. Mip-Grid)  
  *   
  * Hybrid Representation NeRF  
    * Tetra-NeRF \- Tetrahedra-based representation  
    * MobileNeRF \- Textured polygons for mobile rendering  
    * PyNeRF \- Pyramidal representation  
  *   
  * NeRF for Dynamic Scenes  
    * D-NeRF  
    * DoubleNeRF \- Superposition of NeRFs  
  *   
  * Conditional & Controllable NeRF  
    * NeRF in the Wild (NeRF-W) \- Unconstrained photo collections  
    * CP-NeRF \- Conditionally parameterized for cross-scene  
    * GSNeRF \- Generalizable Semantic NeRF  
    * Ref-NeRF \- Structured view-dependent appearance/reflection  
    * NeRV \- Neural Reflectance/Visibility for Relighting  
    * NeRF-Art \- Text-driven stylization  
    * Ray Deformation Networks \- For refractive objects  
    * NeRFrac \- Handles refractive surfaces  
    * ConsistentNeRF \- Depth consistency for sparse views  
    * RegNeRF \- Regularization for sparse views  
    * DS-NeRF \- Depth-supervised  
    * Mega-NeRF / Mega-NeRF++ \- Scalable for large scenes  
    * MixNeRF \- Mixture density for sparse inputs  
  *   
  * Efficient NeRF Variants  
    * FastNeRF \- 200FPS rendering  
    * KiloNeRF \- Thousands of tiny MLPs  
    * NeuSample \- Neural sample field for efficiency  
    * Re-ReND \- Real-time rendering across devices  
    * NeRDF (Neural Radiance Distribution Field) \- Efficient view synthesis  
  *   
  * NeRF for Specific Data  
    * BungeeNeRF \- Extreme multi-scale scenes  
    * NeRF from Sparse RGB-D Images  
    * Surf-NeRF / S-NeRF (Shadow NeRF) \- Satellite imagery  
    * MVG-NeRF \- Combines Multi-View Geometry  
    * SfMNeRF \- Depth-aware optimization  
  *   
  * Anti-Aliasing Techniques for NeRF  
    * FreqMipAA \- Frequency Mip Representation  
    * Tri-MipRF \- Tri-Mip Representation  
    * Rip-NeRF \- Ripmap-Encoded Platonic Solids  
    * SA-GS \- Scale-Adaptive Gaussian Splatting (related)  
    * Drantal-NeRF \- Diffusion-based restoration  
    * PVRF \- Mipmap encoding with sparse grid  
    * MD-NeRF \- Hybrid point sampling  
    * Mip-Grid \- Anti-aliased grid representations  
  *   
*   
* C. Related Concepts & Techniques  
  * Novel View Synthesis  
  * Scene Representation Networks (SRNs) \- Continuous 3D-aware representation  
  * Photorealistic Rendering  
  * Multi-View Stereo (MVS)  
  * Visual Hulls  
  * Gaussian Splatting (related technique)  
  * Signed Distance Functions (SDF) (related concept)  
  * Delaunay Triangulation (Tetra-NeRF)  
  * Triangle-based Rendering (Tetra-NeRF)  
  * Polygon Rasterization Pipeline (MobileNeRF)  
* 

VII. 3D Representation & Generation (General Concepts & Techniques)

* A. Data Representations  
  * Voxel-based representations  
    * Voxel Grid Sampling  
  *   
  * Point Cloud Representation  
  * Mesh Representation  
    * Hierarchical mesh representation  
  *   
  * Implicit Surface Representation  
  * Signed Distance Functions (SDF)  
*   
* B. Core Tasks & Applications  
  * 3D Shape Synthesis / Generation  
  * 3D Shape Completion  
  * 3D Shape Reconstruction (from Image/Depth/Multi-view)  
  * 3D Object Classification  
  * Semantic Segmentation in 3D  
  * Shape Analysis  
  * Shape Interpolation  
  * Interactive Shape Editing  
*   
* C. Learning Techniques & Architectures  
  * Self-Supervised 3D Representation Learning  
    * Generative-Contrastive Learning  
    * Semantic-aware Contrastive Learning (GroupContrast)  
    * Contrastive Autoencoders  
  *   
  * 3D Convolutional Neural Networks (3D CNNs)  
  * PointNet classifier (Point Cloud Processing)  
  * Recursive Neural Net (RvNN) based autoencoder (GRASS)  
  * Deep 3D Convolutional Energy-Based Model (Generative VoxelNet)  
  * 3D Shape Descriptor Network  
  * Probabilistic generative model (for shape families)  
  * Disentangled structured & geometric mesh representation (DSG-Net)  
*   
* D. Specific Concepts & Components  
  * Latent Space Representations for 3D  
  * Global-to-local (G2L) approach  
  * Hierarchical Representation Learning  
  * Feature Disentanglement  
  * Shared encoder / Shared head network  
  * Implicit Information Integration  
  * Dynamic switching scheme for encoder training  
  * Stop gradient operation on a random branch  
  * Additional reconstruction loss  
  * Shape Correspondence  
  * Segment grouping  
  * Part correlation modeling  
  * Generative model of plausible structures (GRASS)  
  * MCMC Techniques for 3D Shape Synthesis (Langevin dynamics)  
  * Analysis by synthesis scheme  
  * Shape Handles Prediction (Learning Generative Models of Shape Handles)  
* 

VIII. Texture Synthesis & Analysis

* A. Core Task  
  * Texture Synthesis  
  * Style Transfer (Texture context)  
*   
* B. Models & Architectures  
  * U-Attention vision Transformer for universal texture synthesis  
    * Hierarchical hourglass backbone  
    * Hierarchical U-Attention architecture  
  *   
  * Transformer-Based Neural Texture Synthesis and Style Transfer  
  * WBT-GAN (Wavelet-based GAN) \- Also relevant here  
  * Spatial GAN (SGAN) \- Also relevant here  
  * Multi-head Mutual Self-attention Generative Adversarial Network (Texture Synthesis)  
  * Optimal Textures (Optimal Transport based)  
  * 3DTextureTransformer \- Geometry aware  
  * User-Controllable Multi-Texture Synthesis GAN  
*   
* C. Techniques & Concepts  
  * Wavelet Transform Techniques  
    * Wavelet Packet Tree (TSWPT)  
    * Wavelet Coefficient Fitting  
  *   
  * Patch-based Texture Synthesis  
    * Adaptive patch based texture synthesis using wavelet  
    * Gaussian-based patch blending technique  
  *   
  * Novel texture description metric (Transformer feature space)  
  * Pixel-level and patch-level smoothing regularizations  
  * Texture modeling and synthesis using joint statistics of complex wavelet coefficients  
  * Photometric Stereo (PS) technique (for 3D surface texture)  
  * Surface representation maps (gradient, albedo, height)  
  * Stochastic and structured textures  
  * Texture Manifolds  
* 

IX. Core Concepts & Techniques (Cross-cutting)

* A. Learning Paradigms  
  * Self-Supervised Learning  
    * Contrastive Learning  
    * Contrastive Predictive Coding (CPC)  
  *   
  * Unsupervised Learning  
  * Supervised Learning  
  * Semi-Supervised Learning  
  * Transfer Learning  
  * Multi-Modal Learning  
  * Cross-Domain Adaptation / Learning  
  * Zero-Shot Learning  
  * Few-Shot Learning  
  * Reinforcement Learning (RL) \- Mentioned for Diffusion diversity  
*   
* B. Model Components & Architectures (General)  
  * Encoder-Decoder Architecture  
  * Attention Mechanisms (General, Self-Attention, Cross-Attention, Multi-Head Attention, Spatial Attention)  
  * Convolutional Neural Networks (CNNs)  
  * Recurrent Neural Networks (RNNs), LSTMs, GRUs  
  * Transformers (as a general architecture)  
  * Graph Neural Networks (GNNs)  
  * Mixture-of-Experts (MoE)  
*   
* C. Training & Optimization  
  * Loss Functions (General)  
    * Adversarial Loss  
    * Reconstruction Loss (e.g., L1, L2, MSE)  
    * KL Divergence Loss  
    * Perceptual Loss  
    * Contrastive Loss (e.g., Triplet Loss)  
    * Cycle Consistency Loss  
    * Commitment Loss (VQ-VAE)  
    * Gradient Penalty  
    * Feature Matching Loss  
  *   
  * Optimization Algorithms (e.g., Adam, SGD)  
  * Regularization Techniques  
    * Dropout  
    * Weight Decay (L2 Regularization)  
    * Batch Normalization / Layer Normalization / Instance Normalization  
    * Spectral Normalization  
    * Early Stopping  
    * Consistency Regularization (VAEs)  
    * Sparsity Enforcement (Spike and Slab)  
  *   
  * Data Augmentation  
  * Fine-tuning  
  * Distillation  
  * Hyperparameter Optimization  
*   
* D. Representation & Features  
  * Latent Space / Latent Variables / Latent Representations  
    * Latent Space Exploration / Interpolation / Arithmetic  
    * Disentangled Representations  
    * Hierarchical Representations  
  *   
  * Feature Extraction / Feature Learning  
  * Feature Fusion  
  * Embeddings (Patch Embedding, Voxel Embedding, etc.)  
  * Prior Distributions  
*   
* E. Specific Techniques & Concepts  
  * Differentiable Rendering  
  * Anti-Aliasing Techniques  
  * Multi-Scale Processing / Hierarchical Approaches  
  * Probabilistic Modeling  
  * Generative Modeling (General concept)  
  * Deep Image Prior (Uses network structure as prior)  
  * Controlled Generation (General concept)  
  * Semantic Understanding / Representation  
  * Style Control / Style Transfer  
  * Image Compositing / Blending  
  * Denoising  
  * Inpainting / Completion  
* 

X. Evaluation & Benchmarking

* A. Metrics  
  * Fréchet Inception Distance (FID)  
  * Inception Score (IS)  
  * Kernel Inception Distance (KID)  
  * Peak Signal-to-Noise Ratio (PSNR)  
  * Structural Similarity Index (SSIM)  
  * Learned Perceptual Image Patch Similarity (LPIPS)  
  * Chamfer Distance (3D)  
  * Earth Mover's Distance (EMD) (3D)  
  * Intersection over Union (IoU) (3D)  
  * Angular Error (Colorization)  
  * CLIP Score / CLIPI-I / CLIPT-I / CCIP (Multimodal)  
  * BLEU Score (Text/Captioning)  
  * NIQE / AG (Image Quality)  
*   
* B. Datasets & Benchmarks  
  * ImageNet  
  * CIFAR-10 / CIFAR-100  
  * CelebA / FFHQ (Faces)  
  * LSUN Bedroom  
  * ModelNet / ShapeNet / Pix3D (3D Shapes)  
  * S3DIS (3D Scenes)  
  * Synthetic Blender benchmark (NeRF)  
  * LLFF-NeRF scenes (NeRF)  
  * DTU (NeRF)  
  * AFHQ / BAAT / Food-101 (GAN Evaluation)  
  * BraTS2020 (Medical Segmentation)  
  * CDnet-2014 (Change Detection)  
  * EditBench (Image Inpainting)  
  * DrawBench (Text-to-Image)  
  * MNIST / SVHN (Digits)  
  * CUB (Birds)  
  * LAION-COCO (Text-Image)  
  * VTAB (Vision Benchmark)  
*   
* C. Evaluation Techniques  
  * Ablation Studies  
  * User Studies / Human Evaluation  
  * Qualitative Analysis (Visual inspection)  
  * Quantitative Analysis (Using metrics)  
  * Comparative Analysis (vs. Baselines/State-of-the-art)

  