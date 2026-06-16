Consolidated Master List of Image Generation Algorithms, Techniques, Concepts, Prompting Methods, and Related Terms

I. Core Generative Models & Architectures/Paradigms

1\.  Autoencoders & Variational Autoencoders (VAEs)  
    \*   Autoencoders (General, Image Denoising, Noise Removal)  
    \*   Variational Autoencoders (VAEs) (General, Photo-Realistic Image SR, representation learning, generation)  
    \*   Conditional VAEs  
    \*   Denoising Auto Encoder (DAE)  
    \*   KL-AE (KL-autoencoder)  
    \*   Hierarchically Quantized Variational AutoEncoder (HQ-VAE)  
    \*   Residual-Quantized VAE (RQ-VAE)  
    \*   Super-resolution Variational Auto-Encoders  
    \*   VQ-VAE (Vector-Quantized Variational Autoencoder)  
    \*   VQGAN (Vector Quantized Generative Adversarial Network \- \*Note: Often uses VQ-VAE concepts\*)  
    \*   VQGAN+CLIP (Combines VQGAN with CLIP guidance)

2\.  Convolutional Neural Networks (CNNs) & Related Architectures  
    \*   Convolutional Neural Networks (CNNs) (General, foundational for image processing, basis for generative architectures, component in hybrid models)  
    \*   Specific CNN mentions (often as feature extractors or components): VGG19, ResNet, XCEPTION, EfficientNet, EfficientnetB7, GoogLeNet, Inception Network, MobileNet, DnCNN, FR-CNN (Fast ResNet-CNN), R-CNN, SRCNN, U-Net  
    \*   Deep Convolutional Neural Networks (DCNNs)  
    \*   Caps-GAN (Capsule Generative Adversarial Network)  
    \*   Convolutional Auto-encoder Neural Networks  
    \*   Depthwise Separable Convolution Networks (e.g., DSCSRGAN)  
    \*   Transpose Convolution-based GAN

3\.  Diffusion Models  
    \*   Diffusion Models (General concept)  
    \*   Diffusion Probabilistic Models (DPM)  
    \*   Denoising Diffusion Probabilistic Models (DDPM)  
    \*   Denoising Diffusion Implicit Models (DDIM)  
    \*   Denoising Diffusion GAN (DDGAN)  
    \*   Denoising Diffusion Restoration Models (DDRM)  
    \*   Score-Based Generative Models / Score Networks / Noise Conditioned Score Networks  
    \*   Stochastic Differential Equations (SDEs) based models  
    \*   Latent Diffusion Models (LDMs)  
    \*   Conditional Diffusion Models / Text-conditional diffusion model / Image-conditioned diffusion model  
    \*   Consistency Models (CM) / Latent Consistency Models (LCM) / Consistency Trajectory Model (CTM)  
    \*   Specific Diffusion Variants & Implementations:  
        \*   4D-aware image diffusion models  
        \*   Accelerated Iterative Diffusion Inversion (AIDI)  
        \*   Adversarial Diffusion Distillation (ADD)  
        \*   Bi-Noising Diffusion  
        \*   Cascaded Diffusion Models  
        \*   CDNeRF (Continuous Diffusion NeRF)  
        \*   Cold Diffusion  
        \*   Conditional Diffusion Probabilistic Models  
        \*   Content-degradation decoupled diffusion  
        \*   DDPM++  
        \*   DD-NeRF (Double Diffusion Neural Radiance Field)  
        \*   DeeDSR (Degradation-Aware Stable Diffusion)  
        \*   DiffBIR (Diffusion Blind Image Restoration)  
        \*   DiffGS (diffusion applied to GS)  
        \*   DiffLinker  
        \*   DiffMat (Latent diffusion models for image-guided material generation)  
        \*   DiffPIR (Diffusion Plug-and-Play Image Restoration)  
        \*   Diffsound  
        \*   Diffusion Transformer (DiT) / Hourglass Diffusion Transformer (HDiT) / PixArt-α / PixArt-Σ / PIXART-δ  
        \*   Diffusion-based GAI model  
        \*   Diffusion-based vision foundation model  
        \*   Diffusion-CCSP (compositional diffusion continuous constraint solver)  
        \*   Diffusion-Mamba  
        \*   DiffusionSat (Generative Foundation Model for Satellite Imagery)  
        \*   DiffVSR (Diffusion Video Super-Resolution)  
        \*   DMV3D (Denoising Multi-View Diffusion using 3D Large Reconstruction Model)  
        \*   DPM-Solver++  
        \*   Drantal-NeRF (Diffusion-Based Restoration for Anti-aliasing Neural Radiance Field)  
        \*   Edify Image (Pixel Space Laplacian Diffusion Models)  
        \*   Flow-based Large Diffusion Transformers (Flag-DiT)  
        \*   GaussianDiffusion (3D Gaussian Splatting for DDPMs)  
        \*   Generative Diffusion Prior (GDP)  
        \*   GLIDE (Text-Guided Diffusion Models)  
        \*   HoliSDiP (Holistic Semantics and Diffusion Prior SR)  
        \*   ID-NeRF (Indirect Diffusion-guided Neural Radiance Fields)  
        \*   Implicit Diffusion Models (IDM)  
        \*   Latent Adversarial Diffusion Distillation (LADD)  
        \*   Latent Diffusion Model for 3D (LDM3D)  
        \*   Latent Point Diffusion Models (LION)  
        \*   Latent Set Diffusion Framework  
        \*   Latent Structural Diffusion Model  
        \*   Low-Resolution Generation Diffusion Model (LR-GDM)  
        \*   Multi-modal Conditional DMs  
        \*   Multinomial diffusion process  
        \*   MVDiffusion (Multi-view Diffusion) / Multi-view diffusion model (MVDream, CAT3D)  
        \*   Nested Diffusion Models  
        \*   Normal-depth diffusion modeling  
        \*   NVIL (Neural Variational Inference and Learning \- Diffusion related)  
        \*   P2P-Net (diffusion-based)  
        \*   ParaDiGMS (Parallel Diffusion Generative Model Sampling)  
        \*   Patch-DM (Patched Denoising Diffusion Models)  
        \*   PFGM (Poisson Flow Generative Model) / PFGM++  
        \*   Point-UV diffusion  
        \*   Probabilistic diffusion process  
        \*   Progressive Distillation  
        \*   Pyramid Diffusion Model (PDM)  
        \*   Rectified Flow  
        \*   Refusion (Realistic Image Restoration with Latent-Space Diffusion Models)  
        \*   ResShift (Efficient Diffusion Model for Image SR by Residual Shifting)  
        \*   RDM (Riemannian Diffusion Model)  
        \*   RSGM (Riemannian Score-Based Generative Model)  
        \*   RSDiff (Remote Sensing Image Generation from Text Using Diffusion Model)  
        \*   SADM (Structure-guided Adversarial training of Diffusion Models)  
        \*   Score SDE  
        \*   SDXL (Stable Diffusion XL) / Stable Diffusion / Stable Diffusion v1.5 / V2 / V2.1 / V3 / SD3-Turbo  
        \*   SeeSR (Semantics-Aware Real-World Image Super-Resolution \- diffusion based)  
        \*   Simple diffusion  
        \*   SinDDM (Single Image Denoising Diffusion Model)  
        \*   SR3 (Super-Resolution via Repeated Refinement) / SR3+  
        \*   SRDiff (Single Image Super-Resolution with Diffusion Probabilistic Models)  
        \*   SRDM (Super-Resolution Diffusion Model)  
        \*   SSDNeRF (Single-Stage Diffusion NeRF)  
        \*   StreamDiffusion  
        \*   SV3D (Latent video diffusion model)  
        \*   Transformer-based diffusion models  
        \*   Unsupervised diffusion models  
        \*   UVHD diffusion model  
        \*   VDMs (text-to-video Diffusion Models)  
        \*   Video diffusion models  
        \*   Waving Goodbye to Low-Res (DiWa \- Diffusion-Wavelet Approach)  
        \*   XPSR (Cross-modal Priors for Diffusion-based Image Super-Resolution)

4\.  Generative Adversarial Networks (GANs)  
    \*   Generative Adversarial Networks (GANs) (General, fundamental class)  
    \*   Conditional GANs (cGANs)  
    \*   Specific GAN Architectures & Variants:  
        \*   3D-Aware GANs / 3D GANs / 3D-aware Semantic-Guided Generative Model (3D-SGAN)  
        \*   Advanced Generative Adversarial Network Based on Dense Connection  
        \*   AICAN (Artificial Intelligence Creative Adversarial Network)  
        \*   Alias-Free Generative Adversarial Networks (GAN)  
        \*   Attentional Generative Adversarial Network (AttnGAN)  
        \*   Best-Buddy GANs (Beby-GAN)  
        \*   BigGANs  
        \*   CAN (Creative Adversarial Network)  
        \*   Co-Modulation GAN (Co-Mod GAN)  
        \*   CycleGAN (Cycle-Consistent Adversarial Networks) / ATT-CycleGAN  
        \*   Cycle-Consistent Super Resolution Generative Adversarial Network (CycleSRGAN)  
        \*   DCGAN (Deep Convolutional Generative Adversarial Network)  
        \*   DECOR-GAN  
        \*   Deep Generative Adversarial Residual Convolutional Networks (SRResCGAN1)  
        \*   DualAttn-GAN  
        \*   DUS-GAN (Direct Unsupervised Super-Resolution using GAN)  
        \*   EG3D (Generative model using tri-plane representation)  
        \*   ESRGAN (Enhanced Super Resolution GAN) / Real-ESRGAN / Triple Real-ESRGAN / TESRGAN  
        \*   FastGAN  
        \*   GCFSR (Generative and Controllable Face Super Resolution)  
        \*   Generative Adversarial Text to Image Synthesis Models  
        \*   Generative LatEnt bANk (GLEAN)  
        \*   GIRAFFE / GIRAFFE HD (High-Resolution 3D-aware Generative Model)  
        \*   GlowGAN (Unsupervised GAN for HDR generation)  
        \*   HyperCGAN (Adversarial Text to Continuous Image Generation)  
        \*   Improved Super-Resolution using GAN (ISRGAN)  
        \*   INR-GAN (Implicit Neural Representation GAN)  
        \*   ISR GAN: Improved Super-Resolution Using Generative Adversarial Networks  
        \*   LC-GAN (Latent Constraints GAN)  
        \*   LE-GAN (Latent Encoder Coupled Generative Adversarial Network)  
        \*   LSGAN (Least-squares GAN)  
        \*   MGAN-CRCM (Multiple Generative Adversarial Network and Coarse Refinement-based Cognizant Method)  
        \*   Mirror GAN  
        \*   MobileStyleGAN  
        \*   Obj-GANs  
        \*   OUR-GAN (One-shot Ultra-high-Resolution GAN)  
        \*   PatchGAN discriminator (Component)  
        \*   Pixel-level generative adversarial training  
        \*   Pretrained StyleGAN2 (for face restoration)  
        \*   Progressive GANs (HR-PrGAN) / Progressive Growing Generative Adversarial Networks / ProGAN  
        \*   Projected GAN  
        \*   RankSRGAN (Super Resolution GAN with Learning to Rank)  
        \*   Ra-GANs (Relativistic average GANs)  
        \*   RealDGen (Realistic Decoupled Data Generator)  
        \*   RiFeGAN  
        \*   SDF-StyleGAN  
        \*   Semantic-Aware Discriminator (Component)  
        \*   SeqAttnGAN  
        \*   SOUP-GAN (Super-Resolution MRI Using GANs)  
        \*   SRGAN (Super-Resolution GAN) / Image Super Resolution using Enhanced Super Resolution Generative Adversarial Network  
        \*   SRCGANs (Super-Resolution Conditional Generative Adversarial Networks)  
        \*   SRTGAN (Triplet Loss based Generative Adversarial Network for Real-World SR)  
        \*   StackGAN / Stacked Generative Adversarial Networks  
        \*   StarGAN / StarGAN v2 / Stargan-JNT (cGAN for multi-domain translation)  
        \*   StyleGAN / StyleGAN2 / StyleGAN2-ADA / StyleGAN3 / StyleGAN-XL / StyleGAN-T  
        \*   TAE-GAN (Text-Aware Emotional GAN)  
        \*   TAGAN (Texture and Attention Guided GAN for Image Super Resolution)  
        \*   TecoGAN (Temporally Coherent GANs for Video Super-Resolution)  
        \*   TIME (Text and Image Mutual-Translation Adversarial Networks)  
        \*   TVBi-GAN (Textual-Visual Bidirectional Generative Adversarial Network)  
        \*   VolumeGAN  
        \*   VQGAN (Vector Quantized Generative Adversarial Network)  
        \*   WBT-GAN (Wavelet based Generative Adversarial Network)  
        \*   WGAN-GP (Wasserstein GAN with Gradient Penalty) / WGAN-AE / WGAN-VGG  
        \*   XMC-GAN (Cross-Modal Contrastive Generative Adversarial Network)

5\.  Neural Radiance Fields (NeRF) and Variants  
    \*   Neural Radiance Fields (NeRF / NeRFs) (General concept, baseline, implicit representation)  
    \*   Specific NeRF Variants & Implementations:  
        \*   4D grid dynamic Neural Radiance Field (NeRF) model  
        \*   A-NeRF (Pose Refinement via NeRF)  
        \*   Accelerated/Optimized NeRF (General category: PlenOctree, SNeRG, MobileNeRF, BakedSDF, VMesh, BOG, VaxNeRF, NerfAcc, Cicero/SpaRW, NeRF-XL, Instant-NGP)  
        \*   AdaNeRF (Adaptive sampling NeRF)  
        \*   AD-NeRF  
        \*   AlbedoNeRF  
        \*   Aleth-NeRF / Thermal-NeRF  
        \*   AligNeRF (Alignment-Aware Training)  
        \*   ASSIST: An object-wise neural radiance field  
        \*   BARF (Bundle-Adjusting Neural Radiance Fields)  
        \*   BerfScene: Bev-conditioned Equivariant Radiance Fields  
        \*   Block-NeRF / City-on-Web  
        \*   Blended-NeRF  
        \*   BOF-NeRF (Bidirectional Optical Flow NeRF)  
        \*   BungeeNeRF / CityNerf  
        \*   CaesarNeRF  
        \*   Canonical NeRF  
        \*   Cascade DyNeRF  
        \*   Cascaded and Generalizable Neural Radiance Fields (CG-NeRF)  
        \*   CC-NeRF (compositional conditional neural radiance field)  
        \*   CDNeRF  
        \*   CeRF (Convolutional Neural Radiance Fields)  
        \*   CLA-NeRF (Category-Level Articulated Neural Radiance Field)  
        \*   Clean-NeRF  
        \*   ClimateNeRF  
        \*   CLIP-NeRF  
        \*   CLONeR  
        \*   CLNeRF  
        \*   CoARF (Controllable Artistic Radiance Fields)  
        \*   CodeNeRF  
        \*   COLF (Compositional Object Light Fields)  
        \*   CompoNeRF  
        \*   Conditional-Flow NeRF (CF-NeRF)  
        \*   Conditional Generative Neural Radiance Fields (CG-NeRF)  
        \*   ConsistentNeRF (3D Consistency for Sparse Views)  
        \*   ContraNeRF  
        \*   Control-NeRF / Control-NeRF1  
        \*   CorresNeRF  
        \*   Cross-Ray NeRF (CR-NeRF)  
        \*   D-NeRF (Neural Radiance Fields for Dynamic Scenes)  
        \*   DaReNeRF  
        \*   DBARF  
        \*   DD-NeRF (Double Diffusion Neural Radiance Field)  
        \*   Deblur-NeRF  
        \*   Deceptive-NeRF  
        \*   De-NeRF (Ultra-high-definition NeRF with Deformable Nets)  
        \*   Depth-NeRF (Depth-Guided NeRF) / Depth-supervised NeRF (DS-NeRF)  
        \*   DeVRF  
        \*   DietNeRF (Few-Shot View Synthesis with Semantic Loss)  
        \*   DiffusioNeRF  
        \*   DONeRF (Depth Oracle Neural Radiance Fields)  
        \*   DoubleNeRF  
        \*   Drone-NeRF  
        \*   DyNeRF (Dynamic Neural Radiance Fields)  
        \*   Dynamic NeRFs (General category: NeRF-DS, RoDynRF, DCTNeRF, DE-NeRF, FSD-NeRF, PAC-NeRF, Nerfies, HyperNeRF, T-NeRF)  
        \*   E2NeRF (Event Enhanced NeRF)  
        \*   ED-NeRF  
        \*   EfficientNeRF  
        \*   EGRA-NeRF (Edge-Guided Ray Allocation for NeRF)  
        \*   EmerNeRF (Learns spatial-temporal representations of driving scenes)  
        \*   ENeRF  
        \*   ENVIDR  
        \*   EO-NeRF (Earth Observation NeRF)  
        \*   Ev-NeRF / EvDNeRF  
        \*   Evo-NeRF  
        \*   Explicit Neural Radiance Fields in Semantic Space (NeRF-IS)  
        \*   ExtraNeRF  
        \*   FastNeRF  
        \*   Fast-TetWild (Related mesh generation)  
        \*   FeatureNeRF  
        \*   FENeRF  
        \*   FLAME-in-NeRF  
        \*   FlipNeRF  
        \*   FreeNeRF (Frequency regularized NeRF)  
        \*   FusedRF  
        \*   GANeRF (Hybrid GAN and NeRF)  
        \*   GARF (Gaussian Activated Neural Radiance Fields / Geometry-Aware Generalized Neural Radiance Field)  
        \*   Generalizable Model-based Neural Radiance Fields (GM-NeRF)  
        \*   Generalizable NeRF Transformer (GNT)  
        \*   Generalizable Neural Performer (GNR)  
        \*   GeoNeRF (Generalizable NeRF with Geometry Priors)  
        \*   GM-NeRF  
        \*   GNeRF (Generative Neural Radiance Fields)  
        \*   GO-NeRF  
        \*   GP-NeRF (Generalizable neural Point Field / Geometry-guided Progressive NeRF / Grid-guided NeRF)  
        \*   GSNeRF (Generalizable Semantic Neural Radiance Field)  
        \*   H-NeRF  
        \*   HDR-NeRF / HDR-HexPlane  
        \*   HeadNeRF  
        \*   HeRF  
        \*   HiDe-NeRF  
        \*   HOSNeRF  
        \*   HumanNeRF  
        \*   HybridNeRF (Combines surface and volumetric rendering)  
        \*   HyperNeRF (Higher-dimensional for Topology Changes)  
        \*   IBL-NeRF  
        \*   ID-NeRF (Indirect Diffusion-guided Neural Radiance Fields)  
        \*   IE-NeRF (Inpainting Enhanced Neural Radiance Fields)  
        \*   InfoNeRF (Few-Shot Regularization)  
        \*   Inpaint4DNeRF  
        \*   InpaintNeRF360  
        \*   InseRF  
        \*   Instance-NeRF (Instance Neural Radiance Field)  
        \*   IntrinsicNeRF (Intrinsic Decomposition)  
        \*   IR-NeRF  
        \*   JNeRF  
        \*   KeypointNeRF  
        \*   KiloNeRF  
        \*   Language Embedded Radiance Fields (LERFs)  
        \*   Latent-NeRF  
        \*   LLNeRF (Low-Light NeRF)  
        \*   LOLNeRF (Learn from One Look Neural Radiance Fields)  
        \*   MD-NeRF (Large-Scale Scene Rendering with Hybrid Point Sampling)  
        \*   Mega-NeRF (Scalable Large-Scale NeRFs)  
        \*   MERF (Memory-Efficient Radiance Field)  
        \*   Mip-NeRF / Mip-NeRF 360 (Multiscale Representation for Anti-Aliasing NeRF)  
        \*   MixNeRF  
        \*   MMNeRF  
        \*   MobileNeRF  
        \*   MoFaNeRF (Morphable Facial Neural Radiance Field)  
        \*   MonoNeRD / MonoNeRF  
        \*   MP‐NeRF  
        \*   MRVM-NeRF (masked ray and view modeling method for generalizable NeRF)  
        \*   MS-NeRF (Multi-Space Neural Radiance Fields)  
        \*   MultiPlaneNeRF  
        \*   MuRF (Multi-Baseline Radiance Fields)  
        \*   MuvieNeRF  
        \*   MVSNeRF  
        \*   NARF (Neural Articulated Radiance Field)  
        \*   NeDDF (Neural Density-Distance Field)  
        \*   NeLF (Neural Light Field)  
        \*   NeRAF (3D Scene Infused Neural Radiance and Acoustic Fields)  
        \*   NeRD  
        \*   NeRF++  
        \*   NeRF attention (NeRFA)  
        \*   NeRF ResNet / ReRF (Residual Radiance Field)  
        \*   NeRF-Art  
        \*   NeRF-Casting  
        \*   NeRF-Det / NeRF-Det++  
        \*   NeRF-GANs  
        \*   NeRF-ID (Learned Sampling)  
        \*   NeRF-In  
        \*   NeRFLiX / NeRFLiX++  
        \*   NeRF-LOAM  
        \*   NeRF-MAE (Masked AutoEncoders for Self-Supervised 3D Representation)  
        \*   NeRF-MS  
        \*   NeRF-SDP  
        \*   NeRF-SOS (NeRF with Self-supervised Object Segmentation)  
        \*   NeRF-SR (Super-Resolution)  
        \*   NeRF-Texture  
        \*   NeRF-VAE  
        \*   NeRF-VO  
        \*   NeRFPlayer  
        \*   NeRFshop  
        \*   NeRFrac  
        \*   NeRFusion  
        \*   NeRFVS (Neural Radiance Fields for Free View Synthesis)  
        \*   NeRS (Neural Reflectance Surfaces)  
        \*   NeSF (Neural Semantic Fields)  
        \*   NeuLF (Neural 4D Light Field)  
        \*   NeuRAD  
        \*   Noise-Aware NeRFs (NAN) / Drantal-NeRF  
        \*   NoPe-NeRF  
        \*   NPRF (Neural Painted Radiosity Fields)  
        \*   NR-NeRF  
        \*   NVIL (Neural Variational Inference and Learning \- NeRF related)  
        \*   ObjectNeRF  
        \*   Open-NeRF  
        \*   OR-NeRF  
        \*   OV-NeRF  
        \*   PaletteNeRF  
        \*   ParticleNeRF  
        \*   PC-NeRF (Parent-Child Neural Radiance Field)  
        \*   PIE-NeRF  
        \*   PixelNeRF  
        \*   Point-NeRF / Point-NeRF++  
        \*   Pre-NeRF 360  
        \*   ProLiF (Progressively-connected Light Field network)  
        \*   ProSGNeRF (Progressive Dynamic Neural Scene Graph)  
        \*   PureCLIPNeRF  
        \*   PyNeRF  
        \*   RawNeRF (High Dynamic Range from Raw Images)  
        \*   Recursive-NeRF  
        \*   Ref-NeRF (Handles reflective surfaces) / RefSR-NeRF / Ref-NeuS  
        \*   RefiNeRF  
        \*   RegNeRF (Regularizing for Sparse Inputs)  
        \*   Re-Nerfing  
        \*   ResNeRF  
        \*   RigNeRF  
        \*   RING-NeRF  
        \*   RIP-NeRF (Rotation-Invariant Point-based NeRF)  
        \*   RoGUENeRF (Robust Geometry-Consistent Universal Enhancer for NeRF)  
        \*   S-NeRF (Street-view Neural Radiance Fields / Shadow Neural Radiance Field)  
        \*   SAR-NeRF  
        \*   Sat-NeRF (Satellite NeRF) / SparseSat-NeRF (SpS-NeRF)  
        \*   ScaNeRF (Scalable Bundle-Adjusting Neural Radiance Fields)  
        \*   SC-NeRF (Self-Correcting Neural Radiance Field)  
        \*   SealD-NeRF  
        \*   SegNeRF  
        \*   Semantically-aware Neural Radiance Fields  
        \*   Sem2NeRF  
        \*   SG-NeRF (Semantic-guided Point-based Neural Radiance Fields)  
        \*   ShaRF (Shape-conditioned Radiance Fields)  
        \*   SHERF  
        \*   SIGNeRF  
        \*   SimpleNeRF  
        \*   SinNeRF (Single View NeRF)  
        \*   SparseNeRF (Sparse-view NeRF) / Sparse Voxel-based NeRF  
        \*   SpecNeRF  
        \*   SSDNeRF (Single-Stage Diffusion NeRF)  
        \*   SteerNeRF  
        \*   StegaNeRF (Steganographic Embedding)  
        \*   StereoNeRF (Sparse View Synthesis)  
        \*   STNeRF / ST-NeRF (Spatio-Temporal Neural Radiance Field)  
        \*   Stochastic Neural Radiance Fields (S-NeRF)  
        \*   Strata-NeRF  
        \*   StructNeRF  
        \*   StyleNeRF (Style-based 3D-Aware Generator)  
        \*   Super-NeRF (Super-Resolution Detail Generation)  
        \*   SymmNeRF  
        \*   TensoRF (Tensorial Radiance Fields)  
        \*   Tetra-NeRF (Tetrahedra-based Representation)  
        \*   Text2NeRF  
        \*   TimeNeRF  
        \*   TraM-NeRF  
        \*   TransNeRF (Transformer-based Neural Radiance Field)  
        \*   TUDF-NeRF  
        \*   UE4-NeRF  
        \*   UHDNeRF (Ultra High Resolution)  
        \*   VaxNeRF  
        \*   ViP-NeRF  
        \*   VM-NeRF  
        \*   VQ-NeRF (Vector Quantization for NeRF)  
        \*   WaterNeRF (Underwater Scenes)  
        \*   wildNeRF  
        \*   X-NeRF  
        \*   ZeroRF  
        \*   Zip-NeRF (Anti-Aliased Grid-Based NeRF)

6\.  Gaussian Splatting (GS) and Variants  
    \*   3D Gaussian Splatting (3DGS / GS) (General concept, explicit representation)  
    \*   Specific GS Variants & Implementations:  
        \*   2DGS (2D Gaussian Splatting) / HDGS (Textured 2D Gaussian Splatting)  
        \*   360-GS (Layout-guided Panoramic Gaussian Splatting)  
        \*   4D Gaussian Splatting (4D-GS) / 4DGF (Dynamic 3D Gaussian Fields) / 4DRotorGS / Deformable4DGS / MoSca / Vidu4D / ST-Endo4DGS  
        \*   AbsGS  
        \*   Adaptive Gaussian (AG) initialization  
        \*   Align Your Gaussians (AYG)  
        \*   Analytic-Splatting  
        \*   ARTIC3D  
        \*   BAGS (Blur Agnostic Gaussian Splatting)  
        \*   BAD-Gaussians  
        \*   BIGS  
        \*   BlockGS / GaussianCube  
        \*   CAO  
        \*   CityGaussian (CityGS) / Street Gaussians  
        \*   CoherentGS  
        \*   Compact 3D Gaussians / LightGaussian / Lightweight Predictive 3DGS  
        \*   Compressed 3D Gaussian Splatting (General technique)  
        \*   DC-Gaussian  
        \*   Deblurring 3DGS  
        \*   DECOR-GAN (GS component)  
        \*   DeferredGS  
        \*   Deformable 3D Gaussian Splatting / Deformable4DGS / MD-Splatting  
        \*   DN-Splatter  
        \*   DOF-GS (Depth-of-Field Gaussian Splatting)  
        \*   DreamGaussian / GaussianDreamer / DreamGaussian4D / Gaussian Splashing  
        \*   Dynamic Gaussian Surfels (DGS)  
        \*   E2GS (Event Enhanced Gaussian Splatting)  
        \*   EAGLES (Efficient Accelerated 3D Gaussians)  
        \*   EGGS  
        \*   EndoGSLAM / EndoGaussian  
        \*   EvaGaussians (Event Stream Assisted GS)  
        \*   EVER (Exact Volumetric Ellipsoid Rendering \- related)  
        \*   F-3DGS  
        \*   Feature 3DGS / Feature Splatting / Spec-Gaussian  
        \*   Flash3D / FlashGS  
        \*   FLoD  
        \*   FreGS  
        \*   FSGS (Few-shot Gaussian Splatting)  
        \*   GaMeS (Gaussian Mesh Splatting) / MeshGS  
        \*   GaRField++  
        \*   Gaussian Frosting (Mesh-based editing layer on GS)  
        \*   Gaussian Splashing (Physics-integrated 3DGS)  
        \*   Gaussian Splatting Radiance Field  
        \*   Gaussian surfels  
        \*   GaussianBody / Human Gaussian Splats (HUGS) / HumanGaussian  
        \*   GaussianEditor (Editing with GS)  
        \*   GaussianHair (Uses cylindrical 3D Gaussians)  
        \*   GaussianHead (Deformable 3D Gaussians for head avatars)  
        \*   GaussianObject  
        \*   GaussianPro  
        \*   Gaussian Pancakes  
        \*   Gaussian Shader  
        \*   GaussianDiffusion (3D Gaussian Splatting for DDPMs)  
        \*   GeoGaussian (Geometry-aware Gaussian Splatting) / GSDF (3DGS Meets SDF)  
        \*   GigaVoxels DP (Related rendering)  
        \*   GIR (3D Gaussian Inverse Rendering) / GS-IR / Relightable 3D Gaussians  
        \*   GPS-Gaussian (Generalizable Pixel-Wise 3D Gaussians)  
        \*   GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting  
        \*   GS-Octree / Octree-GS  
        \*   HFGS (High-Frequency Gaussian Splatting)  
        \*   HiFi4G (Compact Gaussian Splatting for human performance)  
        \*   HO-Gaussian (Hybrid optimization for 3DGS)  
        \*   Hybrid Representations with GS (GauMesh, SUNDAE)  
        \*   Image-GS  
        \*   Language Embedded 3D Gaussians  
        \*   LetsGo (LiDAR-assisted Gaussian Splatting)  
        \*   LP-3DGS  
        \*   MCMC-based 3DGS  
        \*   Mini-Splatting  
        \*   Mipmap-GS / Mip-Splatting  
        \*   MirrorGaussian  
        \*   MoSca (4D Motion Scaffolds for GS)  
        \*   Multi-Scale 3D Gaussian Splatting (Anti-aliased GS)  
        \*   MVPGS  
        \*   NGM-SLAM  
        \*   Panoramic Gaussian Splatting  
        \*   Per-Gaussian Embedding Deformation  
        \*   PGSR (Planar-based Gaussian Splatting Reconstruction)  
        \*   PhysGaussian (Integrates physics simulation)  
        \*   Pixel-GS  
        \*   Pyramidal 3D Gaussian Splatting (PyGS)  
        \*   Query-based Generalizable 3DGS  
        \*   RaDe-GS / RadSplat  
        \*   Rig3DGS  
        \*   RTG-SLAM  
        \*   SA-GS (Scale-Adaptive Gaussian Splatting for Anti-Aliasing) / SA4D  
        \*   SAGS  
        \*   Scaffold-GS (Anchor-based view-adaptive GS)  
        \*   SCube  
        \*   SGS-SLAM  
        \*   SolidGS  
        \*   SpectralSplatsViewer  
        \*   StopThePop  
        \*   SuGaR (Surface-Aligned Gaussian Splatting)  
        \*   SWAG  
        \*   TCLC-GS  
        \*   Textured-GS  
        \*   TOGS (Temporal Opacity Gaussian Splatting)  
        \*   TRIPS (Trilinear Point Splatting \- combines GS ideas)  
        \*   V^3 (2D dynamic Gaussians)  
        \*   VastGaussian (3DGS for large scenes)  
        \*   VCR-GauS  
        \*   VR-Splatting (foveated)  
        \*   Wild-GS / Splatfacto-W / WaterSplatting  
        \*   X-Gaussian  
        \*   3DGStream  
        \*   3DGSR  
        \*   3iGS  
        \*   6DGS

7\.  Transformers & Attention-Based Models  
    \*   Transformer architectures (General, foundational, sequence modeling, self-attention based reasoning, spatial reasoning)  
    \*   Autoregressive Models / Transformers (General, sequence modeling)  
    \*   Specific Transformer Implementations/Modules:  
        \*   Adaptive matching-aware transformer (AMT)  
        \*   Attention Mechanisms / attention model (General concept)  
        \*   Cascaded Transformer-CNN modules  
        \*   Cross-Scale Querying Transformer  
        \*   Diffusion Transformer (DiT) / Hourglass Diffusion Transformer (HDiT) / PixArt-α/Σ/δ  
        \*   Feature Pyramid Networks (FPN) (Often uses attention)  
        \*   Flow-based Large Diffusion Transformers (Flag-DiT)  
        \*   Generalizable NeRF Transformer (GNT)  
        \*   Graph Attention Networks (GAT) (Component)  
        \*   HART (Hybrid Autoregressive Transformer)  
        \*   Hierarchically Quantized Transformer (HQ-Transformer)  
        \*   Masked Generative Transformers (e.g., Muse)  
        \*   Meta-Transformer  
        \*   Multiscale Cross-Attention-Based Transformer Network (MCTNet)  
        \*   Muse (Masked Generative Transformer)  
        \*   Object Scene Representation Transformer (OSRT)  
        \*   Parallel Attention Module (PAM)  
        \*   Perceiver-based component  
        \*   Residual Quantized Transformer (RQ-Transformer)  
        \*   Swin Transformer (Component in SwinIR)  
        \*   T5 (Text-to-Text Transfer Transformer \- Used as encoder/component)  
        \*   Texture Refinement Transformer  
        \*   Texture Transformer Network for Image Super-Resolution (TTSR)  
        \*   Transformer-based 1-Dimensional Tokenizer (TiTok)  
        \*   Transformer-based vision-language pretrained model  
        \*   TransNeRF (Transformer-based Neural Radiance Field)  
        \*   ViewFormer (Transformer-based view synthesis)  
        \*   Vision Transformer (ViT) / ViT-g / ViT-H / ViT-L (Used as encoder/component)

8\.  Other Neural Rendering/Representation Models  
    \*   Explicit/Hybrid Representations (Meshes, Planes combined with neural elements)  
    \*   Frequency-Modulated Point Cloud Rendering  
    \*   Hybrid Voxel/Surface Representations (NeuMesh, BakedSDF)  
    \*   Image-Based Rendering (IBR) / View Synthesis (General technique)  
    \*   Implicit Neural Representations (INR) (General term) / Coordinate-based Neural Representation  
    \*   Instant-NSR (Fast neural surface reconstructor)  
    \*   Intrinsic PAPR  
    \*   K-Planes (Explicit representation)  
    \*   Layered Depth Maps (LDMs \- Representation, not Latent Diffusion)  
    \*   LIRF (Local Implicit Ray Function)  
    \*   Multiplane Images (MPI) / AdaMPI / NeX (Enhanced MPI)  
    \*   Neural Assets (Volumetric object capture)  
    \*   Neural Light Spheres  
    \*   Neural Mesh-Based Graphics  
    \*   Neural Microfacet Fields  
    \*   Neural Pixel Composition (NPC)  
    \*   Neural Point Catacaustics  
    \*   Neural Point-Based Graphics (NPBG) / NPBG++ (Accelerated NPBG)  
    \*   Neural Point-based Volumetric Avatar (NPVA) / PointAvatar / FlashAvatar / HHAvatar / HQ3DAvatar  
    \*   Neural Spline Fields  
    \*   NVS-Solver (Video diffusion for novel view synthesis)  
    \*   PAPR (Proximity Attention Point Rendering)  
    \*   PlenopticPoints (Point-based neural rendering)  
    \*   Point2Pix (Point renderer using NeRF pipeline)  
    \*   Point-Based Neural Rendering (General category)  
    \*   Textured Polygons  
    \*   TriVol (Triple volume point cloud representation)  
    \*   UV Volumes  
    \*   VOctree (Video Octree) / PlenOctree

9\.  Procedural Generation Models  
    \*   Procedural Generation (General concept)  
    \*   Generative node graph models (Generating Procedural Materials)  
    \*   Infinigen (Procedural Generator)  
    \*   Procedural Material Modeling (TexPro) / PBR Material Generation (DreamMat)  
    \*   Procedural Texture Generation / Generating Procedural Materials from Text or Image Prompts (TexPro)  
    \*   Transformer-based conditional generative model (Generating Procedural Materials)

II. Specific Model Implementations (Selected Standouts / Hybrids / Named Systems)

\*   ALIGN (A Large-scale ImaGe and Noisy-text embedding)  
\*   ArtBank (Artistic Style Transfer)  
\*   ArtVista (System)  
\*   AttGAN (Specific cGAN for attribute manipulation)  
\*   AvatarStudio  
\*   Blender 7B (LLM)  
\*   ChatDev (Software Development System)  
\*   ChatSim (LLM Agent Framework)  
\*   CheXagent / CheXbert / ClinicalAgent / ClinicalBERT / GatorTron / NYUTron (Medical LLMs/VLMs)  
\*   Claude (LLM)  
\*   CLIP (Contrastive Language–Image Pre-training) (Core component model)  
\*   CLIPort (Robotics framework)  
\*   CogGPT / CogView2 (Vision-Language Models)  
\*   CoSeR (Cognitive Super-Resolution framework)  
\*   Custom Diffusion / E4T (Personalization/fine-tuning T2I)  
\*   DALL-E / DALL-E 2 / DALL-E 3 (Text-to-Image)  
\*   DeepMasterPrints (Specific GAN application)  
\*   DetectGPT (Detects generated text)  
\*   DINO / DINOv2 (Self-supervised visual features)  
\*   Dream by WOMBO (Platform/Model)  
\*   Dreamer XL  
\*   DreamBooth (Personalization/fine-tuning T2I)  
\*   DreamFusion / Magic3D / MagicDrive3D (Text-to-3D/4D generation)  
\*   DreamLLM  
\*   FastText (Word embedding model)  
\*   Flamingo / GILL / Kosmos-G / OFA / PaLM / VisualBERT / UniVL / VLMs (General Vision-Language Models)  
\*   FoundationPose  
\*   FraCChat (System for CAD model chat)  
\*   Instruct-NeRF2NeRF (IN2N) (Editing framework)  
\*   InstructPix2Pix (Instruction-based image editing via diffusion)  
\*   InternVL (Vision-Language Model)  
\*   ITER (Iterative Token Evaluation and Refinement framework)  
\*   LaMa (Large mask inpainting model)  
\*   LayerPano3D  
\*   LEDITS / LEDITS++ (Real Image Editing with DDPM Inversion)  
\*   LLaMA / LLaMA-2-chat-7B / LLaVa / LLaVA-v1.5 / Alpaca / Mixtral-8x7B (LLMs)  
\*   LLM+P framework  
\*   Midjourney (Platform/Model)  
\*   MIMIC-III / MIMIC-IV / MIMIC-CXR (Datasets)  
\*   MIPS (Maximum Inner Product Search algorithm)  
\*   MiDaS / DPT (Depth estimation models)  
\*   MRKL (Modular Reasoning, Knowledge, and Language system)  
\*   Muse (Efficient Transformer-based T2I model)  
\*   MusicLM (Text-to-Music model)  
\*   Neural Canvas (Platform)  
\*   OmniObject3D (Dataset/Model)  
\*   OntoGPT  
\*   OpenAI CLIP (Specific CLIP implementation)  
\*   OWL-ViT (Open-vocabulary object detection)  
\*   Paint3D framework  
\*   Paint-it / PromptPaint (Steering Text-to-Image via Paint Medium-like Interactions)  
\*   Phy124 / Phys4DGen (Physics-driven controllable 4D content generation)  
\*   Pix2Pix / Pix2PixHD (cGANs for image-to-image translation)  
\*   Playground v2.5 (Model)  
\*   ProteinGPT  
\*   PULSE (Self-Supervised Photo Upsampling via Latent Space Exploration)  
\*   REPLUG (Retrieval-Augmented LM tuning)  
\*   RoboAgent  
\*   SDEdit (Stable Diffusion Edit)  
\*   ShapeGlot (Dataset/Model)  
\*   SiamNet  
\*   SocketAI Scanner  
\*   SOMONITOR  
\*   Sora (Text-to-Video model)  
\*   Sphinx-X-MoE (Multimodal LLM)  
\*   Stable Diffusion (General name for the model family)  
\*   StyleLight (HDR Panorama Generation)  
\*   StyleSpace (StyleGAN analysis method)  
\*   T2M-GPT (Text-to-Motion model)  
\*   TASKED  
\*   Teenage-AGI (Conceptual)  
\*   Text Guided Facial Image Synthesis Using StyleGAN and VAE Trained CLIP (Specific method)  
\*   Text2Room / Text2Scene / TEXTure / Text2VRScene / Text2Tex / InstanceTex / Scene123 / SceneTex / TextMesh / TEXGen (Text-guided 3D/Texture generation)  
\*   TidyBot (Robotics)  
\*   Unified-IO  
\*   Vanitas Still Life generation (Conceptual application)  
\*   VividDream  
\*   Word2Vec (Word embedding model)  
\*   YOLOR / YOLO / YOLOv3 / YOLOv5 / YOLOv7 / YOLOv8 / YOLO-SASE (Object detectors)

III. Image/Scene Enhancement, Restoration & Post-Processing

1\.  Super-Resolution (SR)  
    \*   Super-Resolution (SR) (General concept)  
    \*   Specific SR Techniques/Models:  
        \*   A non-local approach for image super-resolution using intermodality priors  
        \*   An Improved Super Resolution Image Reconstruction Using SVD based Fusion and Blind Deconvolution Techniques  
        \*   Arbitrary-Scale Image Generation and Upsampling  
        \*   Bicubic++ super-resolution network  
        \*   Blind super resolution  
        \*   Cascaded super-resolution  
        \*   Cognitive Super-Resolution (CoSeR) framework  
        \*   Contourlet-based image super-resolution approach  
        \*   Continuous Super-Resolution  
        \*   Cycle-Consistent Super Resolution Generative Adversarial Network (CycleSRGAN)  
        \*   Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution (LapSRN)  
        \*   Deep Learned Super Resolution (General term)  
        \*   Deep Learning Super Sampling (DLSS) / MC-DLSS4 (Nvidia tech)  
        \*   Domain Transfer in Latent Space (DTLS)  
        \*   DualSR (Zero-Shot Dual Learning for Real-World Super-Resolution)  
        \*   DUS-GAN (Direct Unsupervised Super-Resolution using Generative Adversarial Network)  
        \*   Edge preserving single image super-resolution  
        \*   Efficient Deep Models for Real-Time 4K Image Super-Resolution  
        \*   Efficient Upsampling of Natural Images  
        \*   EpiMISR: Multi-image SR handling large disparities using epipolar geometry.  
        \*   ESRGAN / Real-ESRGAN / Triple Real-ESRGAN / IRE / TESRGAN  
        \*   Enhanced Context Attention Network for Image Super Resolution (EASR)  
        \*   Enhanced Deep Super Resolution (EDSR) generator  
        \*   EvTexture (Event-driven Texture Enhancement for Video Super-Resolution)  
        \*   Fine-grained video super-resolution (FGVSR)  
        \*   FuseSR (Super Resolution for Real-time Rendering through Efficient Multi-resolution Fusion)  
        \*   GCFSR (Generative and Controllable Face Super Resolution)  
        \*   HFF-SRGAN (High-Frequency Feature SRGAN)  
        \*   High-Resolution Image Generation/Synthesis / Ultra-High-Resolution Image Synthesis (UltraPixel)  
        \*   HoliSDiP (Holistic Semantics and Diffusion Prior SR)  
        \*   Hybrid approach of interpolations and CNN (for SR)  
        \*   Hybrid-SR: Combining traditional and ML-based SR techniques.  
        \*   Image Super-Resolution With Content-Aware Feature Processing  
        \*   Image super resolution using fusion of images  
        \*   Image super-resolution using gradient profile prior  
        \*   Improved Super-Resolution using GAN (ISRGAN)  
        \*   Incremental Residual Learning (IRL) framework  
        \*   Incremental generation/super-resolution  
        \*   Joint spatial super sampling and frame extrapolation (ExtraSS)  
        \*   Learning-Based Super-Resolution for Image Upscaling Using Sparse Representation  
        \*   Lightweight Real-Time Image Super-Resolution Network  
        \*   Locally Discriminative Learning (LDL) for SR  
        \*   MASA-SR (Reference-based Super-Resolution method)  
        \*   Mob-FGSR (Mobile Frame Generation and Super Resolution)  
        \*   Multi-frame super-resolution  
        \*   Multi-Modal Image Super-Resolution (MISR)  
        \*   Multi-scale feature fusion residual network for Single Image Super-Resolution (MSFFRN)  
        \*   Multiple Residual Learning Network for Single Image Super-Resolution (MRLN)  
        \*   NeRF-SR  
        \*   Neural Network-based Image Super-Resolution Techniques  
        \*   Neural Volume Super-Resolution  
        \*   Null-Space Learning for Consistent Super-Resolution  
        \*   Patch-Based Progressive 3D Point Set Upsampling  
        \*   Perceptual loss functions (VGG-based, LPIPS, etc.) (Common in SR)  
        \*   Photo-Realistic Image Super-Resolution  
        \*   Pixel Recursive Super Resolution  
        \*   Polynomial methods for upscaling  
        \*   Post-processing super-resolution  
        \*   Pro-PULSE (Progressive Encoders for Photo Upsampling)  
        \*   Progressive Upscaling  
        \*   PromptSR (Image Super-Resolution with Text Prompt Diffusion)  
        \*   PULSE (Self-Supervised Photo Upsampling via Latent Space Exploration)  
        \*   RankSRGAN  
        \*   Real-World Blind Super-Resolution  
        \*   RefSR-NeRF (Reference-guided Super-Resolution NeRF)  
        \*   ResMaster (Mastering High-Resolution Image Generation)  
        \*   Residual Learning techniques (for SR)  
        \*   ScaleCrafter (Tuning-free Higher-Resolution Visual Generation)  
        \*   SeeSR (Semantics-Aware Real-World Image Super-Resolution)  
        \*   Self-learning based methods for SR  
        \*   Self-similarity loss (SSL) / graph (SSG)  
        \*   Semantic segmentation guided super-resolution  
        \*   Semi-supervised image super-resolution  
        \*   SESR (Super-Efficient Super Resolution) networks  
        \*   Single Image Super-Resolution (SISR)  
        \*   SOUP-GAN (Super-Resolution MRI Using GANs)  
        \*   Sparse Block Fusion Network (SBFN)  
        \*   Sparse representation methods (for SR)  
        \*   SR3 / SR3+ (Super-Resolution via Repeated Refinement / Diffusion-based blind SR)  
        \*   SRCNN: Super-Resolution Convolutional Neural Network.  
        \*   SRFlow / SRFlow-DA (Super-Resolution Using Normalizing Flow)  
        \*   SRGAN  
        \*   SRTGAN  
        \*   Structure-preserving super-resolution (SPSR) / SPSR-G  
        \*   Sub-Pixel Convolution (for SR) / Sub-pixel convolution layer (for upscaling) / Subpixel Sampling Reconstruction (SSR)  
        \*   Super resolution using edge prior and single image detail synthesis  
        \*   Super-Resolution Based Image Reconstruction  
        \*   Super-Resolution Diffusion Model (SRDM)  
        \*   Super-Resolution of Light Field Images Using Linear Subspace Projection of Patch-Volumes  
        \*   Super-resolution Image Processing Pipeline  
        \*   Super-resolution reconstruction of single image based on Res-Net and Sub-Pixel  
        \*   Super-Resolution using Sub-pixel Recursive Adversarial Network with Perceptual Loss  
        \*   SUPIR (Scaling-UP Image Restoration)  
        \*   SwinIR (Swin Transformer for Image Restoration)  
        \*   TAGAN (Texture and Attention Guided GAN for Image Super Resolution)  
        \*   TargetSR (Semantic location Real-World Image SR with Diffusion Prior)  
        \*   TecoGAN (Temporally Coherent GANs for Video Super-Resolution)  
        \*   TECHNOLOGY A SURVEY ON SUPER RESOLUTION TECHNIQUES  
        \*   Texture Transformer Network for Image Super-Resolution (TTSR)  
        \*   UltraSR (Implicit Image Function-based Arbitrary-Scale SR)  
        \*   Unsupervised image restoration/super-resolution  
        \*   Upsampling / Super-resolution techniques (General)  
        \*   Upsampling attention network (UAN)  
        \*   Upsampling Techniques (using compressed sensing)  
        \*   Very Deep Super Resolution Neural Network (VDSR)  
        \*   XPSR (Cross-modal Priors for Diffusion-based Image Super-Resolution)  
        \*   Zero-Shot Image Super-Resolution / Zero-shot image super-resolution model (DGDML-SR)

2\.  Denoising Techniques  
    \*   Denoising (General concept)  
    \*   Specific Denoising Techniques/Models:  
        \*   AI-Only Denoising: General term for AI-based denoising.  
        \*   Anisotropic Diffusion for Preservation of Line-edges  
        \*   Bayesian Image Reconstruction using Generative Models (BRGM)  
        \*   Blind image restoration  
        \*   Convolutional Neural Networks-Based Denoising Auto Encoder  
        \*   Denoising Diffusion (General concept within diffusion models)  
        \*   Distributed Denoising  
        \*   DnCNN (Denoising Convolutional Neural Network)  
        \*   Drantal-NeRF (Diffusion-Based Restoration for Anti-aliasing NeRF)  
        \*   DWT Thresholding Techniques for Denoising of Images  
        \*   Efficient Edge Preserving Image Denoising using Non-Local Algorithms  
        \*   Fuzzy Filter Based on Fuzzy Logic for noise reduction  
        \*   Image Denoising using Autoencoders  
        \*   IRCNN (Deep CNN Denoiser Prior)  
        \*   Iterative denoising/refinement  
        \*   Multiscale Blind Denoising Algorithm  
        \*   NLM Variants and Extensions / Recursive NLM Denoising  
        \*   Neural Temporal Adaptive Sampling and Denoising  
        \*   Noise reduction / Denoising Techniques (General)  
        \*   Noise Reconstruction / Iterative Noise Reconstruction  
        \*   Noise Removal from the Image  
        \*   Noise scheduling/conditioning/rescheduling (Diffusion models)  
        \*   Noise-Aware NeRFs (NAN)  
        \*   Noise-Based Reconstruction Techniques  
        \*   Non-Local Means Denoising (NLM)  
        \*   Robust Average Networks for Monte Carlo Denoising  
        \*   Robust Unsupervised StyleGAN Image Restoration  
        \*   Self-Supervised Deep Image Denoising  
        \*   Single Image Denoising through Downsampling and Self-Resolution Restoration Learning (NLR2NSR)  
        \*   Thresholding Techniques (Bayes Shrink, Normal Shrink, Neigh Shrink)

3\.  Inpainting & Completion  
    \*   Inpainting / Completion (General concept: Filling missing parts)  
    \*   Specific Inpainting Techniques/Models:  
        \*   Blended Diffusion  
        \*   CoordFill (Efficient High-Resolution Image Inpainting via Parameterized Coordinate Querying)  
        \*   DeepFill inpainting model  
        \*   Depth Inpainting (LayerPano3D)  
        \*   Egocentric refinement and inpainting (AnyHome)  
        \*   HD-Painter (High-Resolution and Prompt-Faithful Text-Guided Image Inpainting)  
        \*   Hybrid Inpainting Scheme (DATENERF)  
        \*   Image Inpainting (PromptCharm)  
        \*   IMProv (Inpainting-based Multimodal Prompting)  
        \*   Inpainting an Image based on Enhanced Resolution  
        \*   LAMA (pre-trained inpainting model) (Used in ASSIST)  
        \*   Large mask inpainting (LaMa)  
        \*   Mask-guided image editing (Ctrl-Room)  
        \*   Multi-modal inpainting mapper network  
        \*   Novel view inpainting (VividDream, FastScene)  
        \*   SUPER-RESOLUTION BASED IMAGE INPAINTING  
        \*   Text-conditioned inpainting model (Text2Room) / Text-Guided Dual Attention Inpainting Network (TDANet)  
        \*   UV Inpainting / UVHD diffusion model

4\.  Deblurring & Sharpening  
    \*   Deblurring (General concept)  
    \*   Sharpening (General concept)  
    \*   Specific Deblurring/Sharpening Techniques/Models:  
        \*   Adaptive Image Restoration Based on Local Robust Blur Estimation  
        \*   Blind deconvolution techniques (for SR and deblurring)  
        \*   Deblur-NeRF  
        \*   De-blurring algorithm (IMAGE SUPER RESOLUTION USING SPARSE NEIGHBOR EMBEDDING)  
        \*   E2GS (Event Enhanced Gaussian Splatting \- deblurring)  
        \*   Residual image sharpening

5\.  HDR Imaging & Fusion  
    \*   HDR Imaging / Fusion (General concept: Handling high dynamic range)  
    \*   Specific HDR Techniques/Models:  
        \*   GlowGAN: Unsupervised GAN for generating HDR from LDR images.  
        \*   HDR Multi-Exposure Fusion (as data fusion)  
        \*   HDR Panorama Generation (StyleLight)  
        \*   HDRSplat / HDR-GS / HDR-Plenoxels: Gaussian Splatting or Plenoxel variants for HDR.  
        \*   RawNeRF (Handles HDR from raw images)

6\.  Other Enhancement & Post-Processing  
    \*   Adaptive Contrast Enhancement (ACE)  
    \*   AI-powered upscaling techniques (General term) / AI Upscaling Techniques  
    \*   Anti-Aliasing Techniques (Mip-Splatting, Analytic-Splatting, SA-GS, Temporal Anti-Aliasing, FreqMipAA, Tri-MipRF, Zip-NeRF)  
    \*   Automated texture synthesis  
    \*   BeyondScene: Framework for generating high-resolution (8K+) scenes.  
    \*   BRDF demodulation  
    \*   Color Adjustment Techniques  
    \*   Color Grading  
    \*   Color correction algorithms (Hierarchical Color Correction) / Color Correction Techniques  
    \*   Color Palette Adjustment  
    \*   Colorization Algorithms / Colorization  
    \*   Contrast Enhancement of Images Using Partitioned Iterated Function Systems  
    \*   Correction-recovery processing  
    \*   Demosaicing  
    \*   Depth of Field (DoF) Simulation / Bokeh (Dr.Bokeh)  
    \*   Detail Me More: Technique using a "broker" module to improve GAN photo-realism.  
    \*   Digital Resurrection  
    \*   Edge detection (Canny, Laplacian) / Edge Extraction  
    \*   Edge Detection and Enhancement Methods  
    \*   FFT upsampling in feature space using deformable convolutions  
    \*   Filtering (Gaussian, Bilateral, Shock, Low-pass, High-pass, Median, Adaptive, Memory-efficient)  
    \*   FreeScale: Tuning-free inference paradigm using scale fusion.  
    \*   GAN Inversion: Techniques (like Cyclic Reverse Generator \- CRG, HyperInverter, HyperStyle) to find latent codes.  
    \*   High-resolution image generation techniques (General term)  
    \*   Image Enhancement Techniques (general)  
    \*   Image Filtering & Enhancement (General adjustments)  
    \*   Image Illumination based on Tone Mapping for uneven illumination  
    \*   Image Upscaling Techniques Analysis  
    \*   Interpolation techniques (Bicubic, Bilinear, Nearest Neighbor, EASE, Hybrid block-based)  
    \*   Lens shading correction  
    \*   Marching Cubes (related to post-processing/extraction)  
    \*   Mesh simplification (Quadric error metrics)  
    \*   Motion Blur Simulation / Motion artifact reduction  
    \*   Multiple-level residual and dense structure (Architectural design for enhancing upscaling)  
    \*   Photomontage  
    \*   Poisson reconstruction (used in SuGaR)  
    \*   Progressive growing (Training technique)  
    \*   Quantization (Residual, Vector, EAGLES, Language Embedded 3D Gaussians)  
    \*   Random down-sampling method (Technique used in 8K HDR upscaling)  
    \*   Real-Time depth Map Up sampling for Stereoscopic Video shows  
    \*   ResMaster: Training-free method for high-resolution generation.  
    \*   Restoration-guided sampling  
    \*   Scale fusion  
    \*   Segmentation (general, semantic, panoptic, instance, foreground/background)  
    \*   Shadow removal  
    \*   Space contraction (ScaNeRF, MERF)  
    \*   UV Mapping / Smart UV projection

IV. 3D Reconstruction, Representation & Rendering Techniques

1\.  3D Reconstruction & Representation  
    \*   3D Reconstruction (General concept)  
    \*   Explicit Representation (Meshes, point clouds, voxels)  
        \*   Explicit mesh representation (SuGaR, BakedSDF, FEGR, Traditional polygon meshes)  
        \*   Mesh Reconstruction (General) / Surface Reconstruction (General) / Neural Mesh Reconstruction  
        \*   Editable Primitives  
        \*   FlexiCubes: Gradient-based mesh extraction method.  
        \*   Marching Cubes / Marching Tetrahedra (Surface extraction) / Deep Marching Tetrahedra (DMTet) / DMTet (Deformable Mesh Tetrahedra)  
        \*   Neural Mesh Primitive (DNMP)  
        \*   Poisson Surface Reconstruction  
        \*   QUADify: Method for extracting quad-dominant meshes.  
    \*   Implicit Representation (Shapes/scenes via functions like SDF, NeRF)  
        \*   Neural Implicit Surface Reconstruction (NeuS, NeuS2, MonoSDF, etc.)  
        \*   Neural implicit surfaces with Signed Distance Function (SDF)  
    \*   Hybrid 3D representation (Explicit objects, Implicit scenes) / Hybrid Voxel/Surface Representations (NeuMesh, BakedSDF)  
    \*   Volumetric Representation (NeRF, Voxel grid)  
    \*   Specific 3D Representation Techniques/Concepts:  
        \*   3D Gaussian Splats / Dynamic 3D Gaussians (Representation)  
        \*   3D Image Data Structures  
        \*   3D point-level labels  
        \*   3D shape representation (SDF, mesh, point cloud, feature volume)  
        \*   4D dynamic scene representation  
        \*   ConceptGraphs: Open-Vocabulary 3D Scene Graphs  
        \*   CVXNet (convex decomposition)  
        \*   Davisonian Scene Graph (DSG)  
        \*   Depth Estimation (MiDaS, DPT) (Often input to reconstruction)  
        \*   Holistic scene code parameterization  
        \*   Learnable structured scene graph (DIScene)  
        \*   Level of Detail (LOD) Management (Voxel-Based LOD, Dynamic LOD, Adaptive LOD, Octree-GS)  
        \*   Multi-View Stereo (MVS) (Used for depth/geometry estimation)  
        \*   Neural Radiance Fields (NeRF) and Variants (Core representation)  
        \*   Object Scene Representation Transformer (OSRT) / Object Slots  
        \*   Photogrammetry / Structure from Motion (SfM) (COLMAP)  
        \*   Pose Estimation  
        \*   Simultaneous Localization and Mapping (SLAM) (NeRF-SLAM, SplaTAM, Droid-SLAM, Photo-SLAM, Q-SLAM, CMax-SLAM, NICE-SLAM, Structerf-SLAM)  
        \*   Voxel-based NeRF enhancements (VDF, CVT-xRF)

2\.  Rendering Techniques  
    \*   Rendering (General concept: Creating 2D images from 3D data)  
    \*   Core Rendering Techniques:  
        \*   Rasterization (Traditional graphics pipeline component; triangle, tile-based, differentiable, point splatting)  
        \*   Ray Tracing / Ray Marching / Sphere Tracing (Core rendering technique)  
            \*   Monte Carlo Ray Tracing / Path Tracing (Stochastic)  
            \*   Photon Mapping / Photon-Tracing  
            \*   Real-Time Path Guiding  
        \*   Volume Rendering (Simulating light through participating media)  
        \*   Differentiable Rendering (Enabling gradient-based optimization)  
            \*   Conditional Mixture Path Guiding for Differentiable Rendering  
            \*   Differentiable Signed Distance Function (SDF) Rendering  
            \*   Differentiable splat-based rasterizer  
            \*   Differentiable volume rendering (used in NeRF)  
            \*   Monte Carlo differentiable rendering  
            \*   Parameter-space ReSTIR for Differentiable and Inverse Rendering  
            \*   Path-space differentiable rendering  
            \*   Physically-based differentiable rendering (PBDR)  
            \*   PSDR-Room (Single Photo to Scene using Differentiable Rendering)  
            \*   Recursive Control Variates for Inverse Rendering  
            \*   Variance-aware inverse rendering  
    \*   Specific Rendering Concepts/Techniques:  
        \*   Ambient Occlusion (AO)  
        \*   BEV (Bird's-Eye View) scene representation  
        \*   BRDF (Bidirectional Reflectance Distribution Function) modeling / SVBRDF  
        \*   Deferred Shading/Rendering  
        \*   Fast Layered Gaussian Surfels (FLAGS) (Rendering related)  
        \*   Global Illumination (GI)  
        \*   Image-Based Lighting (IBL)  
        \*   Inverse Rendering (General concept, decomposing images; NeILF, NeMF, PhyIR, TensoIR, IRON, PS-NeRF, GIR, Neural Microfacet Fields)  
        \*   Layered 3D Panorama (LayerPano3D)  
        \*   Lighting (General concept)  
        \*   Light Probes  
        \*   Multiresolution Texture Field  
        \*   Neural Shading / Neural Textures  
        \*   Neural Street Scene Renderer (NSSR)  
        \*   Panoptic neural radiance field  
        \*   Physically Based Rendering (PBR)  
        \*   Scene Language (Programs, Words, Embeddings)  
        \*   Scene node data structure  
        \*   Shading & Materials (General concept)  
        \*   Spherical Harmonic Latent Texture Map / Spherical Harmonics / Spherical Gaussians (Representation for lighting/appearance)  
        \*   Stroke-Based Rendering (Simulated brush strokes, texture bombing)  
        \*   Subsurface Scattering (SSS)  
        \*   Texture Mapping & Synthesis (General concept)  
        \*   UV texture maps  
        \*   Volumetric Rendering (Simulating light interaction within a volume)  
        \*   Voxelization Algorithms (Converting representations to voxels)  
        \*   Material Generation:  
            \*   PBR Material Generation (DreamMat)  
            \*   Procedural Texture Generation / Generating Procedural Materials from Text or Image Prompts (TexPro)  
            \*   Text-to-Texture Synthesis (Paint-it, TEXTure, Text2Tex, InstanceTex, SceneTex, TextMesh, TEXGen)

V. Techniques for Controlling Generation & Guidance

1\.  Conditional Input Guidance  
    \*   Conditional Inputs (labels, text, etc. \- general method)  
    \*   Bounding box guidance / tokens  
    \*   Class/text conditional generation  
    \*   CLIP-Guided Techniques / CLIP guidance  
    \*   Control metadata (crop size, random flip flag)  
    \*   ControlNet integration / guidance  
    \*   Depth guidance / Depth prompts/tokens / Depth supervision  
    \*   Explicit geometry guidance / Geometric constraints  
    \*   Geometry-aware score distillation / Structure-Aware SDS  
    \*   Integration of conditional inputs  
    \*   Layout guidance (SceneCraft, GALA3D, Ctrl-Room) / Layout prompts  
    \*   Mask guidance / annotations (user-provided)  
    \*   Normal guidance / Normal prompts  
    \*   Reference images (StyleCity, TEXTure, etc.) / Exemplar image guidance  
    \*   Semantic segmentation guidance / Semantic maps  
    \*   Structural and fine-grained guidance  
    \*   Trajectory Prompts (Specifying motion paths)  
    \*   View-dependent text prompting

2\.  Style & Attribute Control  
    \*   Style guidance / Style prompts (artistic, cultural) / Style network  
    \*   LAFITE: Technique potentially related to style control.  
    \*   Latent Space Exploration: Manipulating latent vectors to control image attributes.  
    \*   Latent Space Interpolation/Manipulation (character blending)  
    \*   Neural Style Transfer (NST): Merging content from one image with the style of another. / Arbitrary Style Transfer  
    \*   SEMSTYLE: Technique potentially related to semantic style control.  
    \*   StyleSpace Analysis: Method for finding disentangled controls within StyleGAN's latent space.

3\.  Semantic Control  
    \*   Semantic guidance/prompts (hard, soft) / steering / steering prompts  
    \*   Semantic Image Editing: Few-shot approach to control synthesized image semantics.  
    \*   Semantic Segmentation for Image Generation: Using semantic maps to guide content placement.  
    \*   Semantic-Conditional Sampling: Few-shot approach to generate images based on a semantic layout.

4\.  Text & Embedding Control  
    \*   Text prompts / Textual descriptions / Textual guidance (General concept)  
    \*   CLIP embeddings / Text embeddings representation  
    \*   Embedding inversion: Optimizing latent embeddings to match an image. / Aligning diffusion inversion chain (RIVAL)  
    \*   Hard semantic prompts (image tags)  
    \*   Prompt inversion: Deriving text prompts from a given image. / delayed projection scheme  
    \*   Sentence embedding / prompts / Sentence-BERT embeddings  
    \*   Text-to-Image Generation Techniques (Overall category)  
    \*   Textual Inversion: Creating custom tokens for specific concepts/styles.  
    \*   Word embeddings representation

5\.  Model Adaptation & Tuning  
    \*   Fine-Tuning Pretrained Models (General) / Fine-tuning (general)  
    \*   LoRa Model Fine-tuning / LoRA (Low-Rank Adaptation) / GaLore (Gradient Low-Rank Projection) / QLoRA  
    \*   Personalization (text embedding, stylization, e.g., DreamBooth, Custom Diffusion, E4T, HyperDreamBooth)  
    \*   Scene-Adapted Diffusion Model Fine-Tuning

6\.  Sampling Strategies & Control Variates  
    \*   Sampling techniques for generative AI / Sampling algorithms (general; top-k, nucleus/Top P, tempered) / Diffusion model sampling/inversion  
    \*   Adaptive sampling strategy (Gaussian in the Wild) / Adaptive sampling techniques  
    \*   Adaptive Temperature (AdapT) sampling / Temperature Sampling Strategies / Temperature control techniques  
    \*   Asynchronous Score Distillation (ASD)  
    \*   Classifier Score Distillation (CSD) / Classifier guidance / Classifier-Free Guidance (CFG) / Noise-damped classifier-free guidance  
    \*   Coarse-to-fine sampling process (LiveScene)  
    \*   Control Variates (general concept) / Recursive Control Variate  
    \*   DDIM sampling/scheduler / Karras scheduler  
    \*   Deterministic inversion (DDIM, EDICT)  
    \*   Expressive sampling algorithms  
    \*   Formation Pattern Sampling (FPS)  
    \*   Frequency and presence penalties  
    \*   Frustum-based sampling method (HDGS)  
    \*   GRIS (Generalized Resampled Importance Sampling)  
    \*   Guided Sampling (SceneControl) / Guidance scale (diffusion)  
    \*   Hybrid sampling strategy (Spiral \+ Ray sampling)  
    \*   Importance Sampling (Used in sampling) / PRIS (Positivized Resampled Importance Sampling)  
    \*   Joint multi-scale diffusion sampling approach  
    \*   Learning-based samplers  
    \*   Low-entropy sampling strategies  
    \*   Maximum number of tokens / Stop sequences  
    \*   Object-centric camera pose sampling  
    \*   Polarity Sampling based models  
    \*   Positivization (Parameter-space ReSTIR)  
    \*   Posterior Sampling with Latent Diffusion Models / Diffusion Posterior Sampling (DPS)  
    \*   Progressive Three-Stage Camera Sampling Strategy  
    \*   Proposal Sampler Strategy (ASSIST)  
    \*   Restoration-guided sampling  
    \*   Retrieval-based guidance prompts / Retrieval-based guidance concept  
    \*   Score debiasing  
    \*   Score Distillation Sampling (SDS) / Geometry-aware score distillation / Structure-Aware SDS / Variational Score Distillation (VSD) / Renoised Score Distillation (RSD) / Canonical Score Distillation (CSD) / Hybrid SDS  
    \*   Truncation sampling heuristics / Truncation methods / Truncation trick (for GANs)

VI. Prompting Methods, Techniques & Optimization

1\.  Core Prompting Concepts  
    \*   Prompt Engineering: The general practice of crafting effective prompts.  
    \*   Prompt Engineering Resources: Tools and guidelines for prompt optimization.  
    \*   Prompt Fidelity: Degree to which output matches the input prompt.  
    \*   Text prompts (general use) / User input prompts (general)

2\.  Prompt Types & Modalities  
    \*   Enriched textual prompts / Tailored image prompts / Rich Text prompts  
    \*   Few-Shot Prompting / Few-shot learning / In-context learning (ICL)  
    \*   Geometric/Spatial Prompts (bounding boxes, segmentation masks, scribbles, depth, normal, layout)  
    \*   Hard Prompts Made Easy (gradient-based optimization) / AutoPrompt / FluentPrompt / Paragraph Extraction using Zeros (PEZ)  
    \*   Image Prompts (Single or multiple images) / Visual prompts (Image Guidance, Style Guidance)  
    \*   Joint Text/Image Prompts  
    \*   Language Instructions (for Agents)  
    \*   Layout & Geometric Guidance (as prompt input)  
    \*   Multi-modal Prompting (general concept) / Multi-modal input prompts / Multi-modal prompts (text, image, depth, pose)  
    \*   Negative Prompt Guidance / Negative prompts / Negative-quality prompts  
    \*   Text Prompts (Natural language descriptions)  
    \*   Trajectory Prompts (Specifying motion paths)  
    \*   View-dependent text prompting  
    \*   Zero-Shot Prompting

3\.  Prompt Generation & Optimization  
    \*   AI-enhanced prompt generations  
    \*   Algorithmic Prompting Techniques (GPTDrawer)  
    \*   Automatic prompt optimization framework  
    \*   LLM-based prompt generation/interpretation  
    \*   Metadata expansion  
    \*   NLP analysis of a large prompt database  
    \*   Optimized prompts  
    \*   Prompt Exploration & Analysis (PromptLandscape, PrompTHis)  
    \*   Prompt Expansion (Prompt Expansion for Adaptive T2I)  
    \*   Prompt Mixing (Localizing Object-level Shape Variations)  
    \*   Prompt Refinement (PromptMagician, PrompTHis) / Iterative refinement process  
    \*   Prompt Spectrum Space P\* / ProSpect (Prompt Spectrum representation)  
    \*   Prompt Suggestion (PromptMagician, Promptify)  
    \*   Prompt template design  
    \*   Prompt tuning (DreamDistribution) / Soft prompt methods  
    \*   Prompt interpolation techniques  
    \*   Prompt modifications (user-guided)

4\.  Advanced Prompting Frameworks/Techniques  
    \*   Automatic Chain of Thought Prompting (Auto-CoT)  
    \*   Chain-of-Thought (CoT) Prompting  
    \*   Continuous Prompts (context/coherence)  
    \*   Feedback Prompting  
    \*   Instruction Tuning / Federated Instruction Tuning (FedIT)  
    \*   Interactive Prompt Exploration (PromptMagician)  
    \*   Prompt debiasing (Debiasing Scores and Prompts)  
    \*   Prompting state-of-the-art (SOTA) LLMs (e.g., ChatGPT specific techniques)  
    \*   Prompting techniques: General term covering various methods (zero-shot, few-shot, feedback, chain-of-thought, tree of thoughts, instruction tuning, RAG, ReAct)  
    \*   ReAct / Reaction & Act Prompting  
    \*   Reflection: Evaluating and refining responses based on prompts/critiques.  
    \*   Retrieval Augmented Generation (RAG) / GraphRAG / Self-RAG / TrojanRAG  
    \*   Sequential testing: Iterative prompt testing.  
    \*   Tree of Thoughts  
    \*   Universal Self-Adaptive Prompting (USP)

VII. Architectural Components, Training Strategies & Evaluation

1\.  Network Architectures & Modules  
    \*   Encoder-Decoder Architectures (General) / Autoencoder (Variational, RQ-VAE, HQ-VAE)  
    \*   Attention Blocks (general, Multi-level, Pixel, Channel, CAFD, HAFFB, RFAB) / Attention layers/mechanisms / Self-attention / Cross-attention / Proximity Attention (PAPR) / Semantic Fusion Attention / Spatio-temporal joint optimization module / Subject-binding attention mechanism / Text attention module / Token Cross Network  
    \*   BERT encoder / BioBERT / SciBERT / Sentence-BERT  
    \*   Base encoder / Conditional encoder / Text encoder (T5, CLIP) / Vision encoder module / VAE encoder/decoder  
    \*   Color correction network  
    \*   Compact weighting network  
    \*   Consistency-controlling super-resolution module  
    \*   Convolutional feature renderer  
    \*   Convolutional layers / Depthwise separable convolutions / Subpixel convolutional layers  
    \*   Cross-attention decoder  
    \*   Cross-modal general language model (CogLM)  
    \*   Dense blocks (e.g., RRDBNet) / Residual Dense Block (RRDB) / Residual-in-Residual Dense Blocks (RRDB)  
    \*   Depth diffusion model / Depth guided degradation model  
    \*   Differential Camera Encoder  
    \*   Discriminator network (GANs, PatchGAN, U-Net, high-frequency, auxiliary, pixel-wise, Semantic-Aware)  
    \*   Downscale attention block (DAB)  
    \*   Dropout layers  
    \*   Feature extraction network (QW-Net) / Feature Pyramid Networks (FPN)  
    \*   Feature Fusion with Attention / Feature modulation module  
    \*   Filtering network (QW-Net)  
    \*   Gaussian selector module  
    \*   Generator network (GANs, StyleGAN, style-based 2D generator)  
    \*   Graph Neural Networks (GNNs) (Triplet-GCN, Lane Graph GNN)  
    \*   Hash Grids / Multi-resolution Hash Encoding (Instant NGP)  
    \*   Hybrid 2D-3D network/block / Hybrid recurrent architecture component  
    \*   Hypernetwork module  
    \*   Information Echo Scheme  
    \*   Instance layout representation  
    \*   Layout Refinement Module  
    \*   Learnable optical flow module / Soft optical flow module  
    \*   Learnable texture extractor  
    \*   Low-pass filtering (LPF) module  
    \*   Mapping network  
    \*   Mixture of Expert (MoE) modules / Shared expert module (space-MoE, time-MoE)  
    \*   Motion mask module / Motion vectors module  
    \*   Multi-head mutual self-attention (MHMSA) mechanism  
    \*   Multi-layer perceptron (MLP)  
    \*   Multi-level feature aggregation module (MFAM)  
    \*   Multi-modal inpainting mapper network  
    \*   Multi-resolution 3D hash grids / Multi-resolution skip connections  
    \*   Multiscale representation components (Mip-VoG)  
    \*   Neural renderer / Style-based neural renderer / Neural surface rendering module  
    \*   Noise predictor module / Noise schedule component  
    \*   Normalization layers (Scale-aware, SPADE, RESAIL)  
    \*   Object detectors (YOLOR) / Mask proposal module  
    \*   Occlusion model (discriminative)  
    \*   Parallel Attention Module (PAM)  
    \*   Pixel and Channel Attention Blocks  
    \*   Pre-trained visual encoder (Component used to extract features)  
    \*   Quantizer module (in autoencoder) / VQVAE module  
    \*   Ranker module  
    \*   Refinement model/module/stage (Stable Diffusion XL Refiner, Structure-Guided Refiner)  
    \*   Regularizer module  
    \*   Residual blocks / Residual learning component / Skip Residual module / Skip connections  
    \*   Restoration modules  
    \*   Ripmap encoding module  
    \*   RoPE (Rotary Positional Embedding)  
    \*   Scale-specific encoder  
    \*   Score distillation module  
    \*   Semantic Regularization module  
    \*   Shallow NeRF network / Shallow UNet architecture  
    \*   Sparse Block (SBFN)  
    \*   Spatially-Adaptive Normalization (SPADE) module  
    \*   Spatio-temporal discriminator / Spatio-temporal stability module  
    \*   Spectral normalization module  
    \*   Squeeze-and-Excitation Blocks  
    \*   Stochastic similarity filter (SSF) module  
    \*   Style modulation module / Style vector module  
    \*   Super Resolution (SR) module  
    \*   Supersampling module  
    \*   Symmetric decoder module  
    \*   Ta-Adapter components  
    \*   Temporal adaptive network / Temporal consistency guide / Temporal Feature Accumulator / Temporal feature propagation stage / Temporal reprojection module  
    \*   Text-Image Fusion Block (TIFBlock)  
    \*   Texture migration module (TMM)  
    \*   Trajectory Score Matching (TSM) module  
    \*   Transfer learning component  
    \*   Tri-Mip encoding module  
    \*   U-Net backbone/architecture  
    \*   Upsampler module (ESPCN, pixel shuffling)  
    \*   Variation Network  
    \*   Vertical positional embeddings  
    \*   Visual knowledge fusion layer / Visual tokens module  
    \*   Wavelet module (Discrete Wavelet Transformation \- DWT)  
    \*   Weight modulation operator (word-level attention-based)  
    \*   Zero-initialized attention module

2\.  Training Strategies & Optimization Algorithms  
    \*   Adafactor  
    \*   Adam Optimizer / AdamW  
    \*   ADMM (Alternating Direction Method of Multipliers)  
    \*   Adversarial Training  
    \*   Alternating Optimization  
    \*   Batch Normalization  
    \*   Clustering (for pruning/organizing primitives)  
    \*   Coarse-to-fine optimization/training strategy  
    \*   Contrastive Learning  
    \*   Data Augmentation Techniques  
    \*   Deferred backpropagation  
    \*   Differentiable Optimization (General concept)  
    \*   Distillation / Knowledge distillation / Self-distillation / Teacher distillation (Invisible Stitch)  
    \*   Ensemble learning  
    \*   End-to-end training  
    \*   Fine-tuning (general)  
    \*   Gradient checkpointing  
    \*   Gradient descent: Core optimization algorithm / Stochastic Gradient Descent (SGD) / Minibatch Stochastic Gradient Descent  
    \*   Greedy growing method for model scaling  
    \*   HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)  
    \*   Hierarchical agglomerative clustering  
    \*   In-context learning (SceneTeller) / Multimodal In-Context Learning (M-ICL)  
    \*   Kernel Principal Component Analysis (Kernel-PCA)  
    \*   Levenberg-Marquardt (LM)  
    \*   Mini-batched K-means algorithm  
    \*   Mixed-precision training  
    \*   Multi-task learning  
    \*   Noise Injection / dimensionality reduction (during training)  
    \*   Noise Sampling Technique  
    \*   Optimization Algorithms (General: ADAM, LM, ADMM, SGLD)  
    \*   Particle Swarm Optimization (PSO)  
    \*   Powell algorithm  
    \*   Progressive training strategy / Progressive growing  
    \*   Regularization (general, Identity, View consistency, Eikonal, Curvature, Smoothness, Light, Density, Shape, L1, L2, Orthogonal, Sparsity-inducing transmittance)  
    \*   Regularized sampling  
    \*   Reinforcement Learning with Human Feedback (RLHF) adaptation  
    \*   Reparameterization trick  
    \*   Self-Supervised Learning (SSL) / Self-training (Invisible Stitch)  
    \*   SGLD (Stochastic Gradient Langevin Dynamics)  
    \*   Supervised pre-training / fine-tuning  
    \*   Transfer Learning  
    \*   Two-stage approach / learning curriculum / Multi-stage training  
    \*   Union-sampling training strategy  
    \*   Welford's Algorithm

3\.  Loss Functions & Metrics  
    \*   Loss Functions (General):  
        \*   AbsRel (Absolute Relative Error)  
        \*   Adversarial loss function / component  
        \*   AMBE (Absolute Mean Brightness Error)  
        \*   Attention-based localization loss  
        \*   BER (Bit Error Rate)  
        \*   CA (Contextual Alignment)  
        \*   CD (Chamfer Distance)  
        \*   CLIP Loss / Similarity / CLIP Score  
        \*   Concept Disentangling Loss module  
        \*   Content loss component  
        \*   Contextual loss  
        \*   Contrastive Loss  
        \*   Cycle consistency loss component  
        \*   Depth Loss  
        \*   Difference loss (L\_diff)  
        \*   Distortion Loss  
        \*   Feature reconstruction loss component  
        \*   Flow and warp losses component  
        \*   Fourier space supervision loss component  
        \*   Gradient guidance / loss  
        \*   Gradient penalty module  
        \*   Hinge loss  
        \*   Hybrid Objective Function (GAN loss, MSE loss, Perceptual loss)  
        \*   Hybrid Perceptual Structural and Pixelwise Residual (HyPSPR) loss  
        \*   L1 Loss / MAE (Mean Absolute Error)  
        \*   L2 Loss / MSE (Mean Squared Error) Loss / RMSE (Root Mean Squared Error)  
        \*   Local-rigidity loss (L\_rigid)  
        \*   Loss function optimization / network architecture improvements (General areas of development)  
        \*   Loss on cross-attention maps  
        \*   Masked diffusion loss  
        \*   Mean Opinion Score (MOS) loss  
        \*   mIoU (mean Intersection over Union)  
        \*   NC (Normal Consistency) / Normal Consistency Loss  
        \*   Perceptual loss function / Perceptual consistency loss / LPIPS (Learned Perceptual Image Patch Similarity)  
        \*   Reconstruction Loss / x0-reconstruction loss  
        \*   Regularization Losses (Eikonal, Curvature, Volume, Density, R1 gradient, Identity, View consistency, Orthogonal, Penetration, Smoothness)  
        \*   Rotational loss (L\_rot)  
        \*   Self-similarity loss (SSL) / graph (SSG)  
        \*   SmoothL1 loss  
        \*   Smoothness Loss  
        \*   SSIM (Structural Similarity Index Measure) / D-SSIM Loss  
        \*   Temporal losses (short-term, long-term)  
        \*   Triplet loss function  
    \*   Evaluation Metrics (General):  
        \*   Accuracy (semantic segmentation, classification)  
        \*   Aesthetic judgment factors analysis  
        \*   Alignment evaluation (text-image, prompt-image)  
        \*   Amusement evaluation (user surveys)  
        \*   Authenticity assessment  
        \*   Authorship analysis  
        \*   Bias analysis (gender, skin type, emotional, data)  
        \*   BLEU score  
        \*   BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator)  
        \*   CIQA (Contextual Image Quality Assessment)  
        \*   CLIPscore  
        \*   Coherence evaluation (temporal, semantic, structural)  
        \*   Complexity rating  
        \*   Computational cost analysis  
        \*   Conceptual analysis  
        \*   Consistency evaluation (inter-frame, inter-region, sampling quality)  
        \*   Convergence analysis (model training)  
        \*   Correlations analysis (text-image embeddings)  
        \*   Creativity evaluation criteria  
        \*   Cross-modal retrieval performance evaluation  
        \*   Data distribution analysis  
        \*   Dataset evaluation  
        \*   Depth evaluation (thematic)  
        \*   Disentanglement quantification  
        \*   Disturbance level measurement (L1, L2 norms, FID)  
        \*   Diversity assessment (generated images/prompts)  
        \*   Downstream task benchmarking (OCR, action recognition, etc.)  
        \*   Economic impact analysis  
        \*   Edge mask evaluation  
        \*   Efficiency assessment (training, inference)  
        \*   Emotional bias analysis / conveyance analysis / description comparison / impact assessment  
        \*   Error rate analysis (classification)  
        \*   EQT (Equivariance Test)  
        \*   Evaluation Metrics (General)  
        \*   Expert assessments/evaluations  
        \*   Eye-tracking data analysis  
        \*   F-Score / R-Precision / Mean Precision / Recall  
        \*   Fairness constraint evaluation  
        \*   Feature visualization  
        \*   Fidelity assessment (visual, semantic, reconstruction)  
        \*   FID (Fréchet Inception Distance)  
        \*   FVD (Fréchet Video Distance)  
        \*   Framework evaluation (ETHICAL, FVS, design research)  
        \*   Frequency domain analysis  
        \*   Full-reference IQA metrics  
        \*   Generalizability assessment  
        \*   Geometric quality evaluation (3D GANs)  
        \*   Human Evaluation / User Studies / Human preference studies/ratings/scores (HPS v2.1) / Human perception analysis / Fool rate metric  
        \*   ID retrieval metric (face identity similarity)  
        \*   Image quality assessment (IQA) / Image quality metrics (PSNR, SSIM, LPIPS)  
        \*   Impact analysis (on artists, creative industry, society)  
        \*   Implementation analysis  
        \*   Inception Score (IS)  
        \*   Interaction analysis (human-AI, user-system)  
        \*   Interpolation quality quantification  
        \*   Inversion quality assessment  
        \*   IPR protection method evaluation  
        \*   KID (Kernel Inception Distance)  
        \*   KVD (Kernel Video Distance)  
        \*   Latent space analysis/interpolation quality / Latent variable analysis  
        \*   Literature review (systematic, comprehensive)  
        \*   Longitudinal studies on viewer reactions  
        \*   Low-level rewards evaluation  
        \*   Ma metric (perceptual quality)  
        \*   Mean Average Precision (mAP)  
        \*   Model comparison (qualitative, quantitative)  
        \*   Model fingerprint analysis / Model scaling evaluation  
        \*   Multimodal evaluation framework (FVS)  
        \*   Naturalness assessment  
        \*   NIQE metric (perceptual quality)  
        \*   No-reference IQA metrics (NIMA, MOR)  
        \*   Novelty assessment/detection  
        \*   Object counting task evaluation / Object recognition performance evaluation  
        \*   Parameter efficiency analysis  
        \*   Participant categorization  
        \*   Peak Signal-to-Noise Ratio (PSNR)  
        \*   Perceptual Index (PI)  
        \*   Performance analysis (accuracy, speed, efficiency) / Runtime performance evaluation (biometrics)  
        \*   Philosophical implications analysis  
        \*   Photorealism evaluation  
        \*   Pixel-wise evaluation (discriminator)  
        \*   Plagiarism analysis  
        \*   Privacy impact analysis  
        \*   Prompt analysis (diversity, effectiveness)  
        \*   Psychological effects assessment  
        \*   Q-Align  
        \*   Realism assessment  
        \*   Reconstruction fidelity/quality evaluation  
        \*   Region-based evaluation  
        \*   Reliability assessment (biometrics)  
        \*   Representation quality evaluation (ViTs vs. semantic tokens)  
        \*   Research framework validation  
        \*   Sampling quality evaluation  
        \*   Semiotic framework analysis (Eco's "Open Work")  
        \*   Sentiment consistency evaluation  
        \*   Sociocultural dimension analysis / Socio-political impact assessment  
        \*   Spatial consistency evaluation  
        \*   Stability analysis (training, generation)  
        \*   Steerability quantification (Markov chain based)  
        \*   Structure evaluation  
        \*   Style simulation effectiveness rating  
        \*   Subjective experience analysis (artist reflection)  
        \*   SWOT analysis  
        \*   Symbolic evolution analysis  
        \*   Synthetic data evaluation  
        \*   Systematic examination/review  
        \*   Temporal consistency evaluation  
        \*   Thematic analysis  
        \*   Theoretical analysis (overparameterization)  
        \*   Transparency assessment  
        \*   Triplet-based adversarial loss evaluation  
        \*   Unlinkability assessment (biometrics)  
        \*   User satisfaction analysis / User strategy analysis  
        \*   Validation (qualitative, quantitative)  
        \*   Visual aesthetics assessment/rating / Visual elegance evaluation  
        \*   Visual attention analysis  
        \*   Visual coherence assessment  
        \*   Visual comparison / Visual inspection  
        \*   Visual quality evaluation / Visual flaw metrics  
        \*   Visual stylometry analysis  
        \*   VQA task evaluation

4\.  Datasets & Benchmarks  
    \*   General Dataset Types: Annotated datasets, Art historical images/data, Artwork datasets (WikiArt), Benchmark datasets (Set5, Set14, BSD100, Urban100, General100, NTIRE), Biometrics data, Black copper patterns data, Captioned large-scale image-text dataset, Clinical data/records, Corpora, Cross-modal data, CT scans data, Curated dataset, Datasets (general, large-scale, benchmark, specialized), Deteriorated art images dataset, Digital artworks data, Emotional descriptions data, Facial data, Geospatial vector data, Genomic data, Graph-structured data, Ground truth data/features, Handwriting data, High dynamic range (HDR) data, High-quality training data, Human portraits data, Human-guided GT image dataset, Hyperspectral image (HSI) datasets, Image data/Visual data, Image embeddings, Image sequences data (videos), Image-caption pairs data, Input-output visual examples data, Intermediate image representations (depth maps), Internal statistics, Keyword data, Knowledge base/External knowledge database, Label map representation, Labeled data, Large Vision-Language model generated pseudo-captions, Latent materials representation, Longitudinal data/studies, Low-resolution (LR) image data/features/representation, Mask representation, Material representation (SVBRDF textures), Medical data/Biomedical data/Healthcare data, Medical imaging data, Metadata, Monocular video sequences data, Motion vector data, Multi-modal data/datasets/features/information/representations, Multi-view image data/datasets/representation, Music data, Natural language data/Textual data/Unstructured text, Natural language descriptions/prompts/supervision data, Noisy raw images data, Non-square images data, Normal map representation, Object representation (3D, visual concepts), Omics data, Ontology of images representation (ImageNet), Optical flow data, Paired data (LR/HR, image/text) vs. Unpaired data, Parametric human model representation, Patch representation (image), Pattern representation (visual, aesthetic), Perceptual features representation, Phenotypic subgroup data, Photographs data, Point cloud data, Pose data/priors/representation, Pre-computed BRDF maps data, Private features representation (multi-modal), Prompt representation (text, image, multimodal), Pyramid latent representation, Qualitative data, Radiance field representation (neural, volumetric), Raw image bursts data, Raw single-view images data, Real noise distributions data, Real-world data/images/LR images, Reference image data (HR, style), Region features representation, Relational concepts representation, Remote sensing image data, Renderings data (high-resolution), Residual representation (image, noise), RGB image data, Satellite imagery data, Scene graph representation, Scene representation (3D, NeRF), Selfies data, Semantic concepts/content/features/information/labels/priors representation, Semantic segmentation probability maps representation, Semantically meaningful tokens representation, Sequence representation (image tokens, view/word sequences), Shape data/representation, Shared features representation (multi-modal), Shared token representation, Short-term/long-term information representation, Signal representation (voice, music), Silhouette descriptions data, Single image data, Single-shot text-video pairs data, Skeleton data (OpenPose), Sketches data, Skull paintings data, Sound data/Audio data, Spatial-temporal data/Time series data, Speech data, Statistical representations (texture synthesis), Stereo image data, Stochastic variation representation (freckles, hair), Stroke data, Structural representation (feature volume), Structure information representation, Style embedding/representation/vectors, Surface normal data/representation, Surveillance camera images data, SVBRDF textures representation, Symbolic representation (skulls, decay), Synsets (WordNet), Synthetic data (degraded images, rendered scenes), Temporal data/features/information/representation, Text captions/descriptions/embeddings/features/prompts/representation, Textual attribute semantics representation, Texture data/features/information/map/patches/representation, Top codes (HQ-VAE), Training data (general, large-scale, high-quality, disclosed), Transmittance regularization data, Triplane NeRF representation, Unimodal data (text, image), Unpaired real LR and HR images data, Unstructured data/medical text, User inputs/preferences/ratings data, User survey data, UV texture map representation, VGG feature maps representation, Video data/sequences, View representation (multi-view, novel view), Visual concepts representation (learned, disentangled), Visual content representation, Visual data (general), Visual emotion datasets, Visual Genome dataset, Visual knowledge representation, Visual representations (general, transferable), Visual-and knowledge-based QA pairs data, Visual-semantic concepts representation, Volumetric representation (NeRF), Wavelet coefficients representation, Word embeddings representation, WordNet structure data, X-radiographs data, Zero-shot data  
    \*   Specific Datasets/Benchmarks mentioned: 3D-FRONT, 3RScan, ABO (Amazon Berkeley Objects), ACID benchmark, Adience dataset, AFHQ / AFHQv2 dataset, ARKitScenes, ArtWhisperer, Artpedia, AQUA, Argoverse 2 dataset, BigEarthNet-S2 dataset, BlendedMVS dataset, C4 dataset, Caltech-UCSD Birds 200 (CUB) dataset, Carla, CC12M dataset, CelebA / CelebAHQ dataset, CheXbench / CheXinstruct dataset, CIFAR-10 dataset, CLEVR dataset / CLEVR-M1 / CLEVRTex, CMU CERT dataset, COCO / MS-COCO, CommonCrawl corpus, Conceptual Captions dataset, Deep Blending dataset, DeepFashion, DiffusionDB, DIV2K\_LSDIR / DIV2K-Val dataset, Docmatix dataset, DRealSR dataset, DTU dataset / DTU MVS benchmark, EMNIST / FEMNIST dataset, EmoSet, FFHQ dataset, Front-3D, High-Resolution Image Reconstruction Datasets, HM3D, HoliCity, Horse2Zebra dataset, HumanVerse, Iconclass Caption dataset / Iconclass dataset, ImageNet, InfiMM-WebMath-40B dataset, InterReal dataset, IJB-A, KAIST3A benchmark, KnowEdit benchmark, LAION-400M / LAION-5B dataset, LEAF benchmark, LSUN dataset, Make3D Range Image Dataset, METABRIC dataset, Mip-NeRF 360 dataset, MultiScan, MultiShapeNet, NeRF-OSR dataset, NYUv2 dataset, Objaverse / Objaverse-XL, OmniSim dataset, OPTIMAM Mammography Image Database, Oxford-102 dataset, Pix3D dataset, ProcTHOR, RadGraph F1 (metric on specific data), ScanNet / ScanNet++, SceneVerse, Set5 / Set14 / BSD100 / Urban100 / General100 / NTIRE, ShapeNet / ShapeNet-v2, Street View, Structured3D, Tanks and Temples dataset, TFD (Toronto Face Database), TJH dataset, Topical-Chat dataset, Upright360 dataset, VQA-RAD dataset, Waymo Open Dataset / Waymo NOTR dataset, We-Math benchmark, WMT benchmark, YCB-V dataset

VIII. Data Handling & Representation Concepts

1\.  Dimensionality Reduction  
    \*   Dimensionality Reduction (General concept)  
    \*   Kernel Methods (for non-linear manipulation, e.g., Kernel t-SNE, Kernel PCA)  
    \*   PCA (Principal Component Analysis): Linear dimensionality reduction.  
    \*   t-SNE (t-distributed Stochastic Neighbor Embedding): Non-linear visualization.  
    \*   UMAP (Uniform Manifold Approximation and Projection): Non-linear visualization.

2\.  Feature Representation & Extraction  
    \*   Feature Representation / Extraction (General concept)  
    \*   Specific Representations/Features:  
        \*   3D shape representation (SDF, mesh, point cloud, feature volume)  
        \*   Albedo map representation  
        \*   Binary embeddings/representations  
        \*   Block-structured collocated grids  
        \*   Bottom codes (HQ-VAE)  
        \*   Bounding box representation  
        \*   CLIP embeddings  
        \*   Codebook (discrete, VQGAN)  
        \*   Coherent image representation  
        \*   Color histogram representation  
        \*   Color representation (LAB Color Space)  
        \*   Conceptual representation (knowledge graph)  
        \*   Content representation  
        \*   Continuous representation (image, scale)  
        \*   Convolutional features representation  
        \*   Coordinate representation (continuous, sinusoidal encoding)  
        \*   Cross-modal representations  
        \*   Degradation representation (text-based, learnable)  
        \*   Dense semantic guidance (segmentation masks, Segmentation-CLIP Map)  
        \*   Depth map representation  
        \*   DINOv2 features  
        \*   Discrete codes/tokens representation (VQ-VAE, RQ-VAE, TiTok) / Finite Discrete Tokens (FDT) representation / Tangible tokens  
        \*   Discretized multi-modal fine-grained representation (pixel/word/frame)  
        \*   Domain-specific knowledge representation  
        \*   Edge map representation / Edge representation  
        \*   Emotional content representation / Emotional features representation  
        \*   Explicit Representation (meshes, point clouds, voxels)  
        \*   Facial Recognition and Manipulation / Facial expressions representation / Facial landmark points representation  
        \*   Feature map representation / Feature volume representation  
        \*   Feature Vectors / Embeddings: Numerical representations.  
        \*   Foreground representation  
        \*   Fractal patterns representation  
        \*   Frequency subbands representation  
        \*   GAN latent space representation (W, W+, h-space) / Latent space representation (diffusion models, GANs, general, StyleGAN W/W+, VAE) / Latent structural representation / Point-structured latent space representation  
        \*   Gaussian noise representation  
        \*   Geometric data/information/priors/regularization/representation  
        \*   Global features representation  
        \*   Gradient map representation  
        \*   Graph representation (scene graph)  
        \*   Grayscale image representation  
        \*   Grid representation (Mip-Grid, spatial)  
        \*   Grounded vision-language representation  
        \*   Hand-crafted features representation  
        \*   Hash Grids / Multi-resolution Hash Encoding  
        \*   High-frequency details/information/textures representation  
        \*   High-level attributes representation (pose, identity)  
        \*   Histograms of oriented gradients (HOG)  
        \*   Implicit Representation (shapes/scenes via functions like SDF, NeRF) / Implicit neural fields representation  
        \*   Instance segmentation masks representation (tangible tokens)  
        \*   Instance-aligned features  
        \*   Key image regions representation (faces, salient objects)  
        \*   Knowledge representation (visual, commonsense)  
        \*   Latent Space: Compressed representation learned by models. / Latent Space Representation (as output of extraction)  
        \*   Layout representation (instance layout)  
        \*   Learnable tokens representation  
        \*   Local features representation / Local pyramids representation (HQ-Transformer)  
        \*   Low-frequency components representation  
        \*   Manifold representation (data, generative radiance)  
        \*   Mapping function representation (G, F)  
        \*   Material representation (SVBRDF textures)  
        \*   Multi-level features representation  
        \*   Multi-resolution representation (Mip-NeRF, GLEAN) / Multi-scale representation (Mip-NeRF, wavelet)  
        \*   Natural image manifold representation  
        \*   NeRF representation (triplane, grid-based) / Volumetric representation (NeRF)  
        \*   Neural network weights representation (HyperDiffusion)  
        \*   Noise map representation (DDIM inversion) / Noise representation (Gaussian, latent, structured)  
        \*   Normal map representation  
        \*   Object classification aware region features  
        \*   Pattern Recognition for Graphic Elements / Pattern representation (visual, aesthetic)  
        \*   Pixel representation (color value, coordinate) / Pixel-level features representation / Pixel-space representation / Pixel-aligned features  
        \*   Pose data/priors/representation  
        \*   Pre-filtered 3D feature spaces representation (Tri-MipRF)  
        \*   Pyramid latent representation (PDM)  
        \*   Radiance field representation (neural, volumetric)  
        \*   Relational concepts representation (intangible tokens)  
        \*   Ripmap-Encoded Platonic Solid representation  
        \*   Scale information encoding / Scale-specific information/representation  
        \*   Scene graph representation (intermediate, expanded)  
        \*   Sequence representation (image tokens, view/word sequences)  
        \*   Shape data/representation  
        \*   Shared token representation  
        \*   Sparse representation / Sparse 3D anchor points representation  
        \*   Spatial coordinates representation / Spatial dependency representation / Spatial feature representation / Spatial information representation / Spatial-adaptive parameters representation / Spatial-temporal data/features/information/pseudo labels/representation  
        \*   Specular map representation  
        \*   Spherical Gaussians (SGs) representation  
        \*   Statistical representations (texture synthesis)  
        \*   Stochastic variation representation (freckles, hair)  
        \*   Style embedding/representation/vectors  
        \*   SuperPixels / SuperTexels: Grouping pixels/texels into meaningful regions.  
        \*   Surface normal data/representation  
        \*   SVBRDF textures representation  
        \*   Swin Transformer features representation  
        \*   Temporal data/features/information/representation  
        \*   Tensor-Based Techniques: Using tensors for data representation/processing.  
        \*   Textual attribute semantics representation  
        \*   UV texture map representation / UV space representation  
        \*   VGG feature maps representation  
        \*   Visual concepts representation (learned, disentangled) / Visual content representation / Visual knowledge representation / Visual representations (general, transferable) / Visual-semantic concepts representation  
        \*   Wavelet coefficients representation

3\.  Data Handling  
    \*   Data Fusion & Integration: Combining data from different sources/modalities. / Multi-Modal Fusion Techniques (text, images, LiDAR, audio)  
    \*   Data Validation (TFX): Ensuring data quality and consistency.  
    \*   HDR Multi-Exposure Fusion (as data fusion)  
    \*   Dataset construction/curation / Data preprocessing techniques / Data selection methods (Diversity-based, Importance-based, Instance selection, Quality-based) / Data filtering / Data poisoning / Deduplication (data)

IX. Related Applications, Use Cases, Editing & AI Design

1\.  Editing Techniques & Frameworks  
    \*   Editing Frameworks (General pipelines for editing, e.g., GSEdit, TIP-Editor, TrAME)  
    \*   Concept removal  
    \*   DIFF EDIT: Technique for editing images using diffusion.  
    \*   Editing with GS: GaussCtrl, ICE-G, GSEdit, Texture-GS  
    \*   Editing with NeRF: Control-NeRF, Instruct-NeRF2NeRF (IN2N)  
    \*   Face Manipulation: Altering facial features in images.  
    \*   Image editing / Interactive image editing  
    \*   Image manipulation (semantic, point-based)  
    \*   Image-to-Image-Translation (Covered by Pix2Pix, cGANs, CycleGAN, Stargan, etc.)  
    \*   Object-level scene editing (DORSal)  
    \*   ReplaceAnything3D (RAM3D)  
    \*   Semantic image editing/manipulation  
    \*   Text/Image-Guided 3D Editing

2\.  Specific Applications & Use Cases  
    \*   3D Asset Creation (games, VR/AR, film) / Image-to-3D Asset Generation / Text-to-3D Asset Generation / Text-to-3D Synthesis  
    \*   3D Image Synthesis (GAN application area)  
    \*   3D Scene Generation Frameworks (Scene123, VividDream, Text2VRScene, etc.) / Automated Layout Generation / Text2Room / Text2Scene  
    \*   AR Integration: Potential application area.  
    \*   Art restoration / Personalized art generation  
    \*   Artistic Colorization  
    \*   Artistic Styles (Surrealism, Cubism, etc. as application output) / Stylization  
    \*   Autonomous Driving: Scene rendering, simulation, sensor modeling (NeuRAD).  
    \*   Autonomous Navigation Systems: AI for self-driving/piloting.  
    \*   Character Rendering/Avatars (GVA, FlashAvatar, HQ3DAvatar, IntrinsicAvatar, EyeNeRF, PointAvatar, Neural Point-based Volumetric Avatar, SMPLpix)  
    \*   Collaborative art projects  
    \*   Controllable Generation: Generating 3D content with specific controls.  
    \*   Cultural Heritage Documentation: 3D reconstruction of artifacts/sites.  
    \*   Digital Human Creation  
    \*   Digital Twin  
    \*   Driving Simulation  
    \*   Forensic Investigations  
    \*   Generative Design Algorithms  
    \*   Graphic Design (logo, icon, layout, font generation)  
    \*   Image restoration / facial restoration  
    \*   Language-Guided Medical Image Analysis (segmentation, quantitative analysis)  
    \*   Language-Guided Robotic Manipulation  
    \*   Medical Imaging: Visualization and super-resolution for medical volume data. / Tomographic Reconstruction  
    \*   Metaverse content creation  
    \*   Rendering Qualities (Hyperrealism, Photorealism, etc. as application goal)  
    \*   Scene Reconstruction: Creating 3D models of real-world environments.  
    \*   Semantic Scene Understanding/Segmentation: Using language or VLMs.  
    \*   Specific Visual Motifs/Themes (Skulls, Dragons, etc. as application output)  
    \*   Video generation / Video editing / Video synthesis  
    \*   Virtual Reality (VR) applications / Immersive Educational Technology (VR/AR) / Teleconferencing / Digital Avatars

3\.  AI-Driven Design & Decision Making  
    \*   AI-Driven Decision Making: General term for AI making operational choices.  
    \*   Elk Herd Optimizer (EHO): Specific optimization algorithm for design.  
    \*   Evolutionary Algorithms: Optimization inspired by biological evolution for design.  
    \*   Gradient Projection Methods: Iterative optimization schemes for design.  
    \*   Iterative Linearized Graphic Design (iLGD): Specific algorithm for graphic design optimization.  
    \*   Optimization Methods: Algorithms for finding the best solution within constraints (for design).  
    \*   Reinforcement Learning: Learning through trial-and-error with rewards (for design optimization).  
    \*   Target Recognition AI: AI for identifying targets.

X. Literary Character Description Techniques (from Portraits.csv \- Not image generation)

\*   Physical Appearance Description (Age Indicators, Attractiveness, Distinctive Marks, Grooming Habits, Hair Color/Texture/Style, Height/Build, Physical Condition/Traits, Skin Tone/Condition, Exterior Features, Symmetry/Asymmetry, Ugliness)  
\*   Facial Features & Expressions (Eye Color/Expression, Facial Descriptions, Emotional Signaling, Gaze direction, Stereotypic beliefs)  
\*   Body Language & Gestures (Body Language, Gesture, Physical Quirks, Posture/Movement, Grace/Plasticity)  
\*   Clothing & Accessories (Character Accessories, Clothing Style, Cultural Markers)  
\*   Voice & Speech (Characters' speech, Voice/Speech Patterns)  
\*   Figurative Language (Comparisons, Epithets, Metaphors, Similes)  
\*   Psychological & Emotional Reflection (Behavior/actions, Bright feature, Change/Development, Appearance Transformation, Portrait Techniques, Psychological reaction, Personality Complexity, Contrast, Descriptive names, Direct characterization, Dreams, Emotional elements, Evaluative connotation, Emotional/mental condition features, History/background, Moral constitution, Motivation, Inner world reflection, Psychological/personality traits, Relationships, Strengths/virtues, Weaknesses/faults)

XI. Creative Prompting Examples (from \_Random Stupid Stuff... file \- Examples, not techniques)

\*   Divine DIY Disasters (Renaissance scenes with mishaps)  
\*   Mona Lisa's Secret Pizza Recipe  
\*   The Arnolfini Portrait: Pet Extravaganza  
\*   The Birth of Venus: Spa Day Extravaganza  
\*   The Garden of Earthly Delights: Reality TV Show  
\*   The Girl with a Pearl Earring: Social Media Maven  
\*   The Kiss of Judas: Awkward First Date  
\*   The Last Judgment: Everyday Nonsense Edition (Biblical scene with mundane elements)  
\*   The Last Supper: Fast Food Showdown  
\*   The Madonna of the Pinks: Flower Shop Drama  
\*   The Night Watch: Office Shenanigans  
\*   The Persistence of Memory: Alarm Clock Meltdown  
\*   The School of Athens: Modern Mayhem (Philosophers in modern scenarios)

XII. Computational Geometry / Physics / Simulation Specific Terms (Only terms relevant/applied to Graphics/Generation in the provided text)

\*   Algorithms (Computational procedures): Adaptive algorithms (Poisson, polygonal approx, FEM, Greedy, Isotropic Remeshing, Mesh Refinement, Quadrature, VEM), Adjoint Method, Alternating Active-Phase Algorithm (AAPA), Analytic Marching, Angle Bound Optimization, Anisotropic algorithms (CVT, Particle Opt, Remeshing), Approximation Algorithms (Weighted Region), Asymptotically Concentrated Topology Optimization, Automatic Quadrangulation/Surface Mesh Generation, Backward Longest-Side Refinement, BEM-FEM, Binary Program Formulation (quad mesh), BiCG/BiCGSTAB, Blue-Noise Remeshing/Point Generation, Bottom-up algorithms (Polygonal Refinement, Multiresolution), Boundary Element Method (BEM), BUSHWHACK, Centroidal Voronoi Tessellation (CVT) Algos (MacQueen's, Lloyd's, SA-based, L-BFGS), Clustering Algorithm (CVD), Collocation Method, Common Refinement Data Transfer, Conformal Parameterization Based Delaunay Refinement, Conjugate Gradients (CG), Constrained Delaunay Algos/Refinement/Triangulation (CDT), Continuous Dijkstra Paradigm, Converging Adaptive Algorithm, Coarsening Algorithm, Coverage Axis Algorithm(++), Cubical Marching Squares, Data-Dependent Triangulation, Decimation Algorithm, De Casteljau algorithm, Deep Marching Cubes (DMC), Deep Point Consolidation (DPC), Delaunay Refinement Algorithms (Shewchuk, Ruppert, etc.), Delaunay Triangulation, Dense Projections Algorithm, Dijkstra's Algorithm, Directed Distance Fields, Discontinuous Galerkin (DG) Methods, Discrete Conformal Parameterization, Discrete Material Optimization (DMO), Douglas-Peucker (DP), Dual Contouring/Edge Collapse/Marching Cubes/Primal Mesh Opt, Dynamical Peatland Model (DYPTOP), Edge Collapse/Recovery/Reduction Algos, Element-free Galerkin (EFGM), Energy Minimization Technique, Extended FEM (XFEM)/Isogeometric Analysis (XIGA)/Marching Cubes, Face Merging Decimation, Farthest Point Optimization (FPO), Fast Polygonal Approx Algo, Feature Sensitive Metric-Based Mesh Simplification, Feature-Driven Robust Topology Opt, Finite Element Method (FEM), Finite Volume Method (FVM), Finite Volume–Based Integrated Hydrologic Modeling (FIHM), Filmsticking Algo, Forward Differencing, Fractional Euler Characteristic Algo, fTetWild Algo, GALERKIN Algo (adaptive VEM), Gauss-Seidel Iteration, Generalized Finite Difference (GFDM), Geometry Independent Field approximaTion (GIFT), Goal-oriented AMR/Space-Time Adaptive GIFT/Newmark (G-STAGN), Gradient Optimization Algo, Graph Spanners, Greedy Algo (shortest paths, refinement, insertion), h-refinement/hp-refinement/p-refinement/k-refinement/np-refinement, Harmonic Edge-Weighted CVT (HEWCVT), Heuristic Packing Approach, Hierarchical Filter/Refinement System/Polygonal Mesh Gen/Regularization, Homogenization Method, hp-adaptive two-grid, Hybrid Mortar VEM, Improved Bone Remodeling Algo, Incremental Delaunay Algos, Integer Programming, Integral Square Synchronous Distance Error Criterion, Interaction Integral Technique, Interior Penalty DG Method, Interleaved Delaunay Refinement/Opt Algo, Interpolation Algos, Isogeometric Analysis (IGA)/Boundary Element (IGABEM), Isotropic Remeshing/Surface Remeshing Algos, Iterative Edge Contraction/Mesh Smoothing/Relaxation/Simplification, Jacobi Preconditioner, k-means clustering, Keyframe Mapping, Kinematic Wave Routing, Krylov Subspace Methods (KSP variants), Lagrange Multiplier Method, Laplacian Smoothing, Lattice Boltzmann (LB)/Tessellation Algo, Least-squares spatial discretization, Level Set Method (LSM), Linear Programming (Integer \- ILP)/Smoothing, Lloyd Iteration/Algo/Relaxation/Newton method, Local Refinement Algo/Operations/Tangential Smoothing, LOP algo, Lp-Centroidal Voronoi Tessellation (Lp-CVT) computation (BFGS), MAKE ADMISSIBLE, Marching Cubes (MC)/Tetrahedra (MT) variants, mark\_recursive, MATTopo Algo, Maximin Optimization, Memetic algos, Meromorphic Quartic Differential Construction, Mesh Optimization/Simplification Algo (Garland & Heckbert, QEM4VR, etc.), Meshless Generalized Finite Difference (GFDM), Method of Characteristics/Manufactured Solutions (MMS)/Moving Asymptotes (MMA), Metric Based Quad Mesh Gen, Mimetic Finite Difference (MFD), Minimal Degree (MD)/Nested Dissection (ND) (matrix reordering), Mixed-Hybrid FEM/Integer Quadrangulation Method, Model for Scale Adaptive River Transport (MOSART), Monte Carlo Sampling Algo/Simulations (MCS), Mortar Method, Moving Deformable Components (MMCs)/Morphable Voids (MMVs), Multigrid Solvers, Multi-Material Level Set (MM-LS), Multiresolution algos (Guskov, Zorin, Botsch & Kobbelt, Zhang & Kaufman), NASM (Neural Anisotropic Surface Meshing), Natural Neighbor (nn) Interpolation/Basis Functions, Network Flow Algo, Neural Marching Cubes (NMC), Newmark Method/Newton's Method/Iterations, Nitsche's Method/Coupling, Novel Refinement Algo (Berrone & Vicini/D'Auria), Numerical Integration Algos (Midpoint, Gauss Quad, RIM), NURBS-Enhanced Polygonal Scaled Boundary FEM (NESBFEM)/NURBS-based IGA, O'Loughlin's Criterion, Optimal Delaunay Triangulation (ODT), Optimality Criteria Method/Optimization-based Smoothing, Ordered-SIMP, Out-of-Core Simplification Framework, Padé Expansion, Parallel Algos, Parameterized Level Set (PLSM), Particle Simulation Algos, Partition of Unity Method (PUM), Penn State Integrated Hydrologic Model (PIHM), Perceptually Guided Polygon Reduction, Petrov-Galerkin methods, PHT-Splines, Physically Based Adaptive Triangulation, Pipelined CG/Flexible GMRES, Planar Delaunay Refinement Algos, Point2Skeleton, Polygonal Approx Algo (Douglas & Peucker)/Partitioning/Scaled Boundary FEM (PSBFEM), Polylla Algo, Preconditioners (PC variants), Principal Curvature Stroke-Based Anisotropic Remeshing, Priority-Queue Based Algos, Probabilistic Methods (CVT), Process‐based Adaptive Watershed Simulator+Community Land Model (PAWS+CLM), Progressive Forest Split (PFS)/Medial Axis Filtration (PMAF)/Mesh (PM), Proper Orthogonal Decomposition (POD), PUPHT-splines, Quad-Mesh Generation Algo, Quadric Error Metrics (QEM) Based Simplification Algos, Quality Agglomeration Algo, Quasi-Newton methods (BFGS), Radial Basis Functions (RBF)/Radial Integration Method (RIM), Randomized Mesh Opt Algo, Raster Algos, Reaction Diffusion Equation (RDE) based Level Set Update, Real-time Adaptive Remeshing Algo, REFINE, Refinement Algo (Suárez & Plaza), Region-Merging Method, Relaxed Topology Derivative (RTD), Remeshing Algo (Botsch & Kobbelt, etc.), Residual a-posteriori error estimator, Restricted Anisotropic Voronoi Diagram Computation/Restricted Delaunay Triangulation (RDT) Extraction, Reverse Cuthill-McKee (RCMK), Ricci Flow (Discrete), River Transport Model (RTM), Sacramento soil moisture accounting (SAC-SMA), Scaled Boundary FEM (SBFEM), Schwarz–Christoffel Mapping, Sculpting Algo, Second-order Arnoldi (SOAR), Selective Refinement Algo, Semidiscrete FVM, Sensitivity Mapping Technique, Series Expansion Method, Set Partitioning in Hierarchical Trees (SPIHT), Shortest Path Map Construction/Steiner-Point-Based Shortest Path Algos, Shrink Wrapping Algo, Simulated Annealing (SA), Simple Linear Iterative Clustering (SLIC), Site-insertion algo, Smoothing Algos (Laplacian, Taubin's, Opt-based), Solid Isotropic Material with Penalization (SIMP), SOR Preconditioner, Sparse Direct Cholesky Solver, Spectral Element Approach/Quadrangulation/Mesh Simplification, Sphere Test, Splitting Algos, Spoke-darts algo, Spring-Mass Model, Stream-Aligned Mixed-Polygonal Meshing, Subdivision Algos (Loop, Catmull-Clark), Subtriangles Technique, Superfaces Algo/Surfacenets Algo, Systeme Hydrologique Europeen (SHE), T-spline Simplification/Local Refinement Algos, Taylor Expansion Method, Taylor-Galerkin Methods, Tessellation Algo (Moreton, Sadoyan, Soni & Bhowmick, Velho), TetGen Algo Suite/Tetrahedral Mesh Improvement/Generation Algos (TetWild), Thinning algo, Top-down Polygonal Removal Algo, Topology Optimization Algos (SIMP, Level Set, MMC/MMV, Homogenization), Trace Direction strategy, Trefftz Discontinuous Galerkin Methods, Triangle Contraction/Triangle‐to‐Quad Conversion/Triangulation Algo (Ruppert), Trimming Technique, Uniform Multiphase Materials Interpolation (UMMI), Unidirectional Multi-level Space-Time Adaptive GIFT/Newmark (UM-STAGN), Valence Optimization, Variational Anisotropic Surface Meshing/Clustering/Quadratic Shape Functions Computation/Shape Approximation (VSA)/Tetrahedral Meshing (VTM) Algo, Vertex Decimation/Insertion/Removal Algos, Vertex Method, Virtual Element Method (VEM), Volume Cost Based Mesh Simplification, Volume-Preserving Binary (VPB) Filter, Voronoi Parallel Linear Enumeration (Vorpaline), Wachspress Basis Functions/Coordinates, Weak Galerkin FEM.  
\*   Techniques (Computational/Geometric/Simulation): Adaptive Grid Subdivision/Mesh Refinement/Sampling, Agglomerated Coarse Meshes, Alternating Optimization, Anisotropic Mesh Generation/Remeshing, Area-Preserving Parameterization, Asymptotic Concentration Method, Automated Domain Discretization/Generalization, Backward Projection, Bibliometric Analysis, Bitwise Interleaving, Blockwalking, Boundary Condition Imposition/Edge Reduction/Representation (B-rep)/Domain Integral Equation, Bounded Approximation, B++ splines, CAD Model Tessellation/Meshing, Capacity-Constrained Voronoi Tessellation (CCVT), Cartesian Lattice/Regular Grid Representation, Cell Merging, Centroidal Voronoi Tessellation (CVT technique/goal), Coarse-Grained Filtering, Code Verification, Collocation scheme, Common Refinement, Comparison with Existing Algos/Methods/Software, Computational Fluid Dynamics (CFD), Computer-Aided Design (CAD) Integration, Conformal Mapping (Schwarz-Christoffel)/Mesh Generation, Connectivity Optimization, Constrained Optimization/Contouring, Continuous Level-of-Detail (LOD) Rendering, Control Volume Method, Controlled Refinement Strategy, Coons Patch, Cross Field Generation/Alignment, Curvature Estimation/Analysis/Weighted Vertex Resampling, Data Structures (Hierarchical, Octree, Half-Edge, TIN, Mesh, Tetrahedral), Data Transfer Between Meshes, Deck Transformation Constraints, Deformable Surface Technique, Digital Elevation Model (DEM) Processing/Planarity/Tessellation, Directed Distance Field Representation, Discrete Differential Forms/Fracture Network (DFN) Modeling/Simulation, Discretization (Spatial, Angular, Temporal), Distributed Computing/Parallel Processing (MPI, GPU), Domain Decomposition (Mortar method), Dual Mesh Construction, Dynamic Ricci Flow/Simulation, Effective Parameterization, Eigenvalue Decomposition/Generalized Eigen-problem Solving, Ellipsoidal Representation/Fitting, Embedding, Empirical A Posteriori Error Estimation, Enrichment Functions (XIGA/IGA), Error Control/Bounded Error, Evaluation using Datasets, Exact Geometric Predicates, Explicit Boundary Evolution/Representation, Extrusion, Face Clustering/Based Constraints/Unknowns, Fairness Refinement/Optimization, Feature Detection/Extraction/Line Preservation/Alignment/Sensitive Sampling/Remeshing, Filtering (Sensitivity, Gaussian), Fine-Grained Refinement, Finite Difference Method, Floating-Point Arithmetic, Frame Field Guidance, Frequency Decoupling, Fuzzy PID Control, Galerkin Projection, Geometric Duality/Optimization/Processing (general term), Global Isotropic Remeshing/Optimization/Parameterization, Goal-Based Adaptivity/Error Estimation, GPS Trajectory Simplification, Graph Construction, Hardware Tessellation/Tessellation Shaders, Hausdorff Distance Calculation/Control, Height Field Approximation/Rendering, Hierarchical Acceleration Structure/Clustering/Mesh Representation (4-K Mesh, Progressive)/Regularization, Hodge Decomposition, Homeometry Maximization, Hydrological Modeling (Surface-Subsurface Coupling)/Hydrologic Conditioning, Hydrostatic Reconstruction, Image Polygonization/Segmentation/Based 3D Reconstruction, Implicit Surface Polygonization/Reconstruction, Importance Map Computation, Incremental Clustering/Refinement/Simplification, Input/Output Data Handling, Integer Tessellation Pattern, Interface Coupling, Interior Angle Criterion, Interpolation (Bivariate Polynomial, Lagrange, Meshfree, NURBS, Spline), Interval Geometric Representations/Computations, Isoparametric Concept/Mapping, Isosurface Extraction, Isotropic Mesh Generation/Remeshing, Iterative Optimization/Refinement/Simplification, Jacobian Calculation/Positivity, Jump-Based Error Indication, Kinematic Constraints, Knot Insertion/Removal, Labeling Edges, Landscape Analysis, Lazy Evaluation, Level Set Representation/Evolution, Linear Coordinate Transformation, Line Art Rendering/Integration/Reduction/Simplification, Line Search (Armijo), Local Approximation Error Estimation/Directional Adaptivity/Feature Size Calculation/Mesh Operators (Swapping, Smoothing, Collapse, Split)/Modifications/Polar Coordinates/Remeshing/Refinement, Logarithmic Discretization, Manifold Conversion/Repair, Mapping (Parametric, High-D), Mass Constraint Formulation, Material Interpolation Models (SIMP, RMMI, UMMI, SIMLF), Matrix Function Solution, Memory Efficient Implementation, Mesh Adaptivity/Adaptive Meshing/Coarsening/Improvement Techniques/Partitioning/Quality Evaluation/Metrics/Representation (Polygonal, etc.)/Sizing Control/Sizing Function/Smoothing (Tangent space, Laplacian, Opt-based)/Stitching, Metric-Driven Remeshing/Sampling, Midpoint Quadrature Rule/Selection, Minimal Stabilization Method, Mixed Collocation Scheme, Model Order Reduction (SOAR), Morphological Operators, Morse-Smale Complex, Motorcycle Graph Construction, Multiphase Material Optimization, Multipoint Constraints, Multiresolution Modeling/Representation/Tessellation, Nearest Neighbor Search, Neuron Morphology Modeling/Visualization, Node Repositioning, Nonconforming Meshes/Hanging Nodes Handling, Nonlinear Averaging, Non-Uniform Refinement, Normal Cycle Parameterization/Sampling/Deviation Measurement, Numerical Integration/Search Procedure/Stability Analysis, Object-Oriented Simulation Environment (MOOSE), Offset Surface Extraction, On-the-fly Refinement, Optimal Transport Formulation, Out-of-Core Processing, Overlaying Meshes, Parallel Computation/GPU Acceleration, Parameterization (Global, Conformal, Area-preserving)/Parametric Surface Tessellation/Approximation, Particle-Based Methods/Particle Simulation, Patch-Based Methods, Performance Analysis, Perturbation Theory/Perturbation-based Stochastic Modeling, Physically Based Modeling, Piecewise Linear Approximation/Interpolation/Smooth Complex Meshing, Point Classification/Cloud Processing/Simplification, Poisson-Disk Sampling, Polygonization, Power Diagram Computation/Restricted Power Diagram (RPD), Preprocessing/Postprocessing Modules/Steps, Principal Curvature Analysis/Alignment, Priority Queue Usage, Progressive Representation, Projection Operator, Proximity Queries, Pruning, Quad-Dominant Mesh Generation/Quadrangulation, Quadratic Optimization, Quality Control/Guarantees, Ray Marching/Ray Casting, Real-Time Rendering/Simplification, Reconstruction (Surface, Shape), Refinement Strategies (h, p, k, hp, np, adaptive, local, global, newest vertex bisection, red-refinement), Regular Triangulation, Relaxation Techniques (Lloyd's), Remeshing (Isotropic, Anisotropic, Semi-regular), Rendering Pipeline Integration, Repolygonalization, Representative Vertex Selection, Resampling (Uniform, Non-uniform, Curvature-weighted), Residual-Based Error Estimation, Restricted Voronoi Diagram (RVD) Computation, Riemannian Metric Construction/Usage, Robustness Analysis/Handling Imperfect Input, Runge-Kutta Integration, Saliency Field Generation, Sampling on Surfaces, Scan Conversion, Selective Refinement, Semi-Analytical Formulation (SBFEM)/Semi-Regular Mesh Generation, Sensitivity Analysis (Adjoint method, Consistent), Shape Change Measure, Sharp Feature Preservation/Handling, Shortest Path Computation (Weighted Region, Polyhedral Surface), Signal Processing on Meshes, Simplicial Complex Processing, Singularity Graph/Handling, Skeletonization, Sliver Removal/Avoidance, Smoothing (Mesh, Field), Snell's Law Application, Software Implementation (MATLAB, C++, etc.), Sparse Linear System Solving, Spatial Tessellation, Spectral Methods, Stabilization Techniques (VEM, IGA), Staggered Solution Scheme, Steiner Point Placement/Insertion, Stochastic Modeling, Strain Smoothing, Strip-based Mesh Simplification, Structural Topology Optimization, Sub-grid Scale Finite Element Discretization, Subdivision Connectivity Generation/Surfaces (Loop, Catmull-Clark), Supermesh Construction, Surface Anti-Aliasing/Extraction/Segmentation, Symbolic Polygon Clipping, Symmetric System Formulation, T-Junction Handling/T-Meshes/T-Gons, Tessellation Pattern Generation, Texture Mapping/Texture Error Handling, Tolerance Areas, Topological Consistency/Correctness Guarantees/Operations/Surgery/Topologically Reliable Approximation/Topology Preservation, Tóth Flow Simulation, Triangulated Irregular Network (TIN) Generation/Processing, Trimmed Geometry Handling, Two-Mesh Approach, Uncertainty Quantification/Propagation, Uniform Mesh Generation/Sampling, Unstructured Mesh Generation/Processing, Upsampling/Downsampling, Validation, Vectorization, View-Dependent Level-of-Detail (LOD)/Rendering, Virtual Work Statement, Visual Discrimination Metrics/Masking Tools/Perception Guided Remeshing/Simplification, Volume Preservation/Volumetric Representation/Techniques, Voronoi Diagram/Tessellation (Centroidal, Constrained, Restricted, Weighted, Anisotropic, Discrete), Voxel-Based Methods, Watertight Mesh Generation/Repair, Weighted Centroidal Voronoi Tessellation/Region Problem, Z-order/Morton Curve.  
\*   Concepts (Computational/Geometric/Mathematical): Abel-Jacobi Condition/Theory, Adaptive Refinement Concept, Adjoint Consistency, Algebraic Computation Model (ACMQ), Anisotropy/Anisotropic Metric/Space, Approximation Theory, Aspect Ratio, Asymptotic Optimality/Behavior, Barycentric Coordinates, Bézier Extraction, Blue Noise Property, Boolean Operations, Boundary Value Problems (Elliptic, etc.), Branched Coverings, B-Splines (NURBS, etc.), Capacity Constraints, Centroid/Center of Mass, C0/C1 Continuity, Checkerboard Pattern, Circumradius-to-Shortest Edge Ratio, Combinatorial 3-Manifold, Complexity (Time, Space, etc.), Computational Geometry, Computer-Aided Design (CAD), Conciseness of Representation, Conformal Geometry/Mapping/Parameterization, Conforming Discretization/Meshes, Connectivity, Conservation Principles, Constrained Delaunay Property, Convergence, Convexity Properties, Coupled Physics/Multiphysics Simulation, Crack Tip Enrichment/Singularity, Curvature (Gaussian, etc.), Decimation Concept, Delaunay Property/Empty Circumcircle/Circumsphere, Differential Geometry, Diffusion Problems/Heat Conduction/Neutron Transport, Dihedral Angles, Dirichlet Tessellation, Discontinuous Coefficients/Solutions, Discrete Fracture Network (DFN), Discretization Error, Dispersivity, Duality (Geometric, Optimization), Elasticity (Linear, etc.), Ellipsoidal Variance Proxy, Energy Function/Functional Minimization, Ensemble Methods (climate), Equilibrium State, Error Bounds, Euclidean Distance/Metric, Euler Characteristic/Fractional Euler Characteristic, Extrema, Feature Sensitivity, Fidelity to Data, Finite Element Analysis (FEA), Fluid Dynamics/Flow Problems, Fractal Stream Chemistry, Free-Edge Effect, Functional Gradient Constraint, Galois Theory, Gauss Divergence/Bonnet Theorem, Generalized Barycentric Coordinates, Geometric Convergence/Distance/Invariants/Network Optimization/Tolerance, Geomorphs, GIS Data Production Requirements, Global Index, Gradient Flow, Gray-Scale Elements/Intermediate Density, Ground Truth, Harmonic Forms/Functions, Heaviside Function, Hexagonal Minkowski Metric, Hierarchical Structure/Representation, High-Frequency Oscillations, Holonomy Group, Homotopy Equivalency/Topological Correctness, Human Visual System Properties/Visual Perception, Hybrid Variable, Hydrological Similarity, Hyperbolic Vertex Classification, Ill-Conditioning, Image Compression (JPEG 2000), Implicit Surfaces, Indefinite Problems, Information Theory/Bound, Inside/Outside Volume Representation, Integral Geometry, Interlaminar Failure, Interpolation Error, Interval Arithmetic/Geometry, Isogeometric Analysis (IGA) Paradigm/Isoparametric Element/Isoperimetric Quotient, Isotropy/Isotropic Metric/Meshing, Jacobian (Matrix/Determinant), Lagrangian Finite Elements, Laplacian Operator, Level of Detail (LOD) Concept, Linear Elastic Fracture Mechanics (LEFM), Lipschitz Property, Local Feature Size, Locking Phenomenon, Manifold (Surface, etc.), Mass Constraint, Master-Slave Relationships, Mathematical Morphology, Maximum Principle, Mean Value Coordinates, Medial Axis Transform (MAT)/Medial Spheres/Balls, Mesh Bias/Dependence/Quality Concept, Meshfree Methods, Metric Tensor, Mimetic Finite Differences Concept, Min-Max Boxes, Minimum Spanning Tree, Minkowski Metric, Monotonicity-Preserving Schemes, Multigrid Concept, Multiphase Materials, Multiresolution Concept, Natural Harmonics, Non-Smooth Domains/Boundaries/Features, Normal Anisotropy, Numerical Robustness/Stability, Optimal Transport, Orthogonal Dual, Oscillation, Overfitting, Parametric Surfaces (Polynomial, NURBS, etc.), Patch Test, Period Matrix/Jacobi Variety, Perspective Geometry, Phase Field Model, Piecewise Linear (PL) Manifold, Polygonal/Polyhedral Elements/Meshes, Porous Media Flow/Poro-Fractured Media, Potential Energy Analogy, Power Crust, Principal Component Analysis (PCA), Progressive Representation, Projection (L2, Orthogonal), Quadric Error Metrics (QEM) Concept/Forms/Representations, Quantization Noise Power, Quasi-Steady State Assumption, Rational Functions/Padé Approximants, Reaction Diffusion Concept/Equation, Regularity Assumptions, Residence Time Distribution (RTD)/Power-Law RTD (PLRTD), Riemann Surface Theory, Runoff Generation/Routing, Scalability, Scale Effects, Scattered Data Interpolation/Approximation, Self-Adjoint Angular Flux (SAAF) Equation, Sensitivity (Topological/Shape Derivative), Shape Functions (Linear, Quadratic, etc.), Shortest Path Problem, Signed Distance Function (SDF), Singular Solutions/Singularities, Sobolev Spaces, Solid Mechanics, Space-Filling Curve, Spectral Properties, Sphere Property, Spline Wavelet Decomposition, Stabilization (Numerical, VEM, IGA), Steady-State/Transient Problems, Stress-Degradation Function, Strickler Coefficient, Structural Optimization, Subdivision Connectivity, Surface Curvature/Normals/Reconstruction, Symmetry Conditions, Tensor Field, Tessellation (Dirichlet/Voronoi, Delaunay), Topological Noise/Consistency/Correctness/Surgery/Reliable Approximation/Preservation, Topology (Arbitrary Genus, Mesh, Surface), Tortuosity, Transmissivity, Trefftz-Like Trial Functions, Triangulated Irregular Network (TIN), Trimmed Surfaces/Geometries, Uncertainty (Geometric, Parameter, etc.), Uniform Sampling/Distribution, Variational Principles/Formulation/Approach, Vector Field/Quantization, Visibility/Line of Sight Queries, Volume Fraction, Voronoi Diagram/Tessellation Concept/Theory, Watershed Simulation/Modeling, Weak Form/Variational Formulation, Weighted Euclidean Metric, Winding Number Strategy.  
\*   Prompting Linguistics / Methods / Guidance (Terms guiding algorithms/methodologies): A Posteriori Error Estimation/Estimators/Analysis, Approximation Error Bound/Tolerance, Boundary Edge Angle Error, Capacity Constraints, Complexity Constraint, Conformity Criterion, Constraint Equation System, Convergence Criterion (Hausdorff distance-based), Cost Function/Energy Function, Curvature-Based Penalty/Sensitivity, Decimation Criteria, Delaunay Criterion, Density Function, Deviation Measure, Directional Dependence, Discretization Error, Distance Measure, Edge Cost Function, Error Indicator/Metric/Weight, Fairness Criterion/Mesh Fairness, Feature Preservation, Functional Gradient Constraint, Geometric Constraints/Fidelity, Goal-Based Error Estimators/Goal-Oriented Adaptivity (Quantity of Interest \- QoI), Heuristics, Homeometry Maximization Criterion, Hydrologic Similarity Concept/Topographic Index/Wetness Index, Importance Map/Saliency Field, Information-Theoretic Bound, Integral Square Synchronous Distance Error Criterion, Interpolation Error Minimization, Isotropy (Mesh Quality Goal), Legality Preconditions, Linear Mass Constraint, Local Variation Estimation, Mass Constraint, Maximum Optimization Procedure, Mesh Quality Criteria/Metrics (Size, Shape, Angle bounds, Aspect ratio, Isotropy, Regularity, Radius ratio, etc.), Mesh Sizing Function/Target Edge Length, Metric Constraints, Minimal Angle Constraint/Improvement, Minimization of Heat Potential Capacity/Structural Volume (Objective), Multiresolution Structure/Representation (Goal), Normal-Based Tolerance Error, Objective Function (Minimizing Compliance, Error, Energy, Volume, etc.), Optimization Goals (Simplicity, Fidelity, Quality, Feature preservation), Oracle, Ordered Rational Approximation, Parameter-Adaptive Acquisition Method, Parametrization Alignment, Partitioning Criterion, Penalty Term, Perceptual Quality Measures, Physically Based Parameters, Prioritization Heuristics/Criteria, Quadratic Energy Minimization, Radial Distance Restriction Criterion, Refinement Criteria (View-dependent, Error-based), Regularity Term, Residual-Based Error Estimator, Robust Decision Criterion, Shape and Size Guarantees, Shape Change Measure, Shortest Element Collapse Priority, Singularity Configuration Control, Size Control, Smoothness Constraints/Preservation, Sparse Directional Constraints, Stabilization, Statistical Significance Assessment, Stopping Criterion, Stress Constraint, Surface Edge Angle Error, Target Screen Size, Topological Constraints/Guarantees/Derivative, User Controls/Preferences/Specified Tolerance/Budget, Variable Screen-Space Threshold, Vertical Distance Restriction Criterion, Volume Constraint, Weighting Scheme.  
\*   Other Related Terms (Problem types, domains, data types, mathematical tools): 2D/3D Domains, Advection-Dispersion Equation, Affine Map, Algebraic Multigrid (PCGAMG), Angle-Ply Laminates, Arbitrary Topology, Atmospheric Circulation Modeling, Automobile Design (B-pillar), Benchmark Problems/Test Cases (IAEA PWR, C5G7, Koyna dam, etc.), Binary Images, Biomedical Imaging, Boltzmann Transport Equation, Boundary Conforming Meshes/Representation (B-rep), Box-Spline Functions, Branched Covering Space, Brittle Fracture, Bulk Material, CAD/CAM Systems, Capillarity, Catchment Hydrology/Watersheds, Cellular Biology, Chemical Modelling/Reaction Systems, Climate Change/Classification, Collocation Points, Complex Geometries, Composite Laminates/Structures, Compressible Euler/Navier-Stokes Equations, Computer Graphics/Vision, Conforming/Nonconforming Elements/Meshes, Conservation Equations, Constrained Delaunay Tetrahedralization/Constraining Segments/Facets, Contact Problems, Contour Lines/Isocontours/Isolines, Control Points/Net/Mesh, Convective Instability, Convex/Non-convex Domains/Polygons/Polyhedra, Coordinate System (Local polar, Cartesian), Crack Discontinuity/Propagation/Stability, Creases, Dataset (ABC, NeuroMorpho), Deformable Models, Degrees of Freedom (DOFs), Dense 3D Polygon Meshes, Derivative Stress/Strain Field, Desktop Computer/Workstation/HPC/CRAY T3E-600, Digital Terrain/Elevation Models (DTM/DEM), Discontinuous Diffusivity Coefficient, Discrete Ordinates (SN) Method, Distributed Parameter Models, Divisor, Drainage Flux/Attributes, Driving Simulation, Dual Graph, Eigenfunctions/Eigenvalues (Laplacian), Electrostatic Charged Particle Model, Elliptic Partial Differential Equations (PDEs), Energy Norm, Engineering Applications/Problems, Evaporation/Evapotranspiration (ET), Finite Element Spaces, Fixed Point Iteration, Flooded Area/Inundation Extent, Forest Split Operation, Function Space Mapping, Functionally Graded Materials (FGM), Galerkin Approximation, Gaussian Energy, Geographic Information Systems (GIS), Geometric Duality/Modeling, Geophysics/Geophysical Problem, Global Consistency, Groundwater Flow/Recharge, Half-Edge Data Structure, Hardware Acceleration/Graphics Card (GPU), Helmholtz Equation, Heterogeneity (Geological, Aquifer), Hexahedral Meshes, High-Complexity Models/Spatial Resolution Imagery, Hillslope Model, Histogram-Based Filtering, Holes/Inclusions, Holomorphic Differential Group, Homogeneous/Isotropic Material, Homology Group, Hybrid Meshes, Hydrodynamic Processes, Hydrographic Features, Hydrograph Simulation, Illumination Artifacts, Image Compression/Segmentation, Implicit Representation, Incompressible Flow, Infiltration Excess, Initial Conditions/Boundary Conditions/Mesh, Input Angle Restrictions, Integrated Hydrologic Modeling, Interface Meshes, Inter-Group Regenerative Source Terms, Internal Heat Sources, Isoparametric Interpolation, Isosurface, Iterative Solvers, Jump Conditions, Kernel (Hydrologic model component), Kirchhoff Plates/Love Shell Theory, Knot Vector, Land Cover/Use Change/Surface Models (LSM \- CLM), Large-Scale Models/Simulations, Leaf Area Index (LAI), Levels of Detail (LOD), Light Field, Linear Advection Equation/Elasticity, Link Frequency Distribution, Low-Poly Models, L^q/L^∞/H^1/H^1/2 Norms, Macro Triangulation, Material Properties (Conductivity, etc.), Matrix (Stiffness, Mass, Period), Mechanical Metamaterials, Memory Usage, Meso-scale Atmospheric Circulation, Meteorological Data/Forcing, Minimal Surface, Molecular Models, Multigroup Neutron Diffusion/Transport Equation, Multiple Intersections, Multiscale Variant, Network Transmission, Neuron Tracings, Neutron Multiplication Factor (keff), Newtonian Fluid, Nodal Values/Degrees of Freedom, Noise Removal/Reduction, Non-Linear Problems/Solvers, Non-polynomial Functions, Non-smooth Solutions, Numerical Quadrature, NURBS Curves/Surfaces/Patches, Octree Grid, ODE Solver, Open Ditch Drainage, Operator (Laplacian, etc.), Parameter Space/Parametric Domain, Partial Differential Equations (PDEs), Particle Repulsion, Patch (Geometry), Path (Shortest, Geodesic), Peatlands, Performance Metrics, Physical Systems/Phenomena, Piecewise Constant Data/Smooth Surfaces/Complexes, Planar Straight-Line Graph (PSLG)/Strain State/Wave Basis, Point Cloud/Set, Poisson Equation, Polygon Soup, Polynomial Approximation/Basis/Interpolation/Functions, Pore Structure/Porosity/Tortuosity, Power-Law Distribution, Pressure Head, Primitive Extraction, Quadrilateral Meshes, Range Imaging/Scans, Raster Data/Voxel Space, Reaction Rate, Real-time Performance, Rectangular Cells, Reference Mesh/Surface, Region Growing, Remote Sensing Imagery, Rendering (Line-art, Real-time), Representative Volume Element (RVE), Richards Equation, Robotics, Saddle Points, Sample Points/Seeds, Saturated/Unsaturated Zone Dynamics, Saturation Excess, Scalar Field, Self-Intersection, Semi-infinite Domains, Shallow Water Equations, Shared Memory/Distributed Memory Systems, Shell Structures, Simplical Tessellation/Complex, Simulation (Numerical, Multiphysics, Driving, Hydrologic, Atmospheric), Sink/Source Terms, Small Angles, Software Libraries/Frameworks (MOOSE, VERA, PIHM), Soil Moisture/Properties/Texture/Waterlogging, Solid Modeling, Sound Absorption Materials, Sparse Matrix, Spectral Analysis, Spherical Volume Analogy, Splines (B-spline, etc.), Steady State Baseflow Discharge, Stereoscopic Pictures, Stiffness Matrix, Storage Requirements, Stress Intensity Factors (SIFs), Structural Design/Analysis, Subcell/Subdomain/Subproblem/Subsystem, Surface Attributes/Fitting/Parameterization/Representation, Taylor Series Expansion, Temperature Field, Temporal Persistency, Tensor Product, Terrain Modeling/Representation/Approximation, Tetrahedral Decomposition/Tessellation/Quality, Texture Coordinates/UV Space, Thin Features, Time Integration Schemes/Dependent Problems/Transient Analysis, Topographic Attributes, Topological Ball Property/Consistency/Homeomorphism/Inconsistencies/Defects/Joining/Optimization, Transpiration, Triangle Mesh/Triangulation, Trim Curves/Trimming, Unstructured Grid/Mesh, Upslope Contributing Area, Vadose Zone, Variable Resolution, Vertex Attributes/Clustering/Pair Contraction, Virtual Reality (VR), Viscous Incompressible Flow, Voxel/Volumetric Data, Voronoi Cell/Region/Delaunay Theory, Water Balance/Table Depth, Waveguide, Weighted Residuals Method, Wetlands.

\---

This comprehensive list, derived from the provided texts, organizes the terminology into logical categories related to image generation and its underlying technologies, including specific algorithms, broader techniques, fundamental concepts, control/guidance methods, and related terms like datasets and evaluation metrics.