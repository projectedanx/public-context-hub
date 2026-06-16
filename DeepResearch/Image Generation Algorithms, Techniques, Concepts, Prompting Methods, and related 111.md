Image Generation Algorithms, Techniques, Concepts, Prompting Methods, and related terms.

**I. Core Generative Models & Architectures/Paradigms**

* Autoencoders & Variational Autoencoders (VAEs): Models using an encoder-decoder structure (often with a probabilistic latent space).  
  * Autoencoders (Image Denoising)  
  * Denoising Auto Encoder (Noise Removal from Image)  
  * KL-AE (KL-autoencoder)  
  * Super-resolution Variational Auto-Encoders  
  * Variational Autoencoders (VAEs) (Photo-Realistic Image SR, representation learning, generation)  
  * VQ-VAE (Vector-Quantized Variational Autoencoder)  
*   
* Convolutional Neural Network variants (CNNs): Foundational deep learning models for image processing, forming the basis of many generative architectures (includes specific mentions like VGG19, ResNet, XCEPTION, EfficientnetB7 when used as feature extractors).  
* Diffusion Models: Advanced generative models that iteratively refine random noise into high-quality images based on guidance.  
  * Conditional Diffusion Models  
  * Consistent Mesh Diffusion  
  * DDPM++ (Diffusion Model)  
  * DeepFloyd IF (Factorized Diffusion)  
  * Denoising diffusion probabilistic model  
  * Depth-aware diffusion model  
  * Depth-conditioned Stable Diffusion  
  * Diffusion models (general concept)  
  * Diffusion Posterior Illumination  
  * Diffusion Transformer (DiT)  
  * E-Diffusion (GenRC)  
  * Factored diffusion formulation  
  * Factored semantic diffusion  
  * Feature-correspondence-guidance diffusion process  
  * Image-conditioned diffusion model  
  * Latent Diffusion Models (LDMs)  
  * LDM3D (Latent Diffusion Model for 3D)  
  * Locally Conditioned Diffusion (LCD)  
  * Mixture of Diffusers  
  * Multi-view diffusion model (MVDream, CAT3D)  
  * MultiDiffuser  
  * Nested Diffusion Models  
  * Region-based diffusion process (Expressive Text-to-Image Generation)  
  * RGBD panorama diffusion model  
  * SDEdit (Stable Diffusion Edit)  
  * Scene-Adapted Diffusion Model Fine-Tuning  
  * Stable Diffusion / Stable Diffusion XL (general use, V1.5, V2, V2.1, depth-conditioned)  
  * StitchDiffusion  
  * Text-conditional diffusion model  
  * Text-to-image diffusion model (general concept)  
  * 3D sparse diffusion model  
*   
* Generative Adversarial Networks (GANs): A fundamental class using generator/discriminator networks.  
  * 3D-Aware GANs  
  * Conditional GANs (cGANs)  
  * CycleGAN / ATT-CycleGAN  
  * GAN (mentioned within Generative Photography)  
  * GAN (mentioned within Persistent Nature)  
  * GAN (mentioned within SceneDreamer)  
  * GAN (mentioned within Super-resolution of low-fidelity flow solutions)  
  * GAN (mentioned within Text2Tex)  
  * GAN (mentioned within What You See is What You GAN)  
  * GAN inversion (mentioned within Consistent Mesh Diffusion)  
  * GAN-based framework that substantially improves the generator network  
  * GAN-based methods (mentioned within Text2Tex)  
  * GANSharp: High-definition image reconstruction using generative adversarial networks  
  * Generative Adversarial Networks for Image Upscaling  
  * Hybrid GAN-enabled framework  
  * ISR GAN: Improved Super-Resolution Using Generative Adversarial Networks  
  * LSGAN (Least-squares GAN)  
  * Pretrained StyleGAN2 for face restoration  
  * Progressive GANs (HR-PrGAN) / Progressive Growing Generative Adversarial Networks  
  * ProGAN  
  * SRGAN (Super-Resolution GAN) / Image Super Resolution using Enhanced Super Resolution Generative Adversarial Network  
  * StyleGAN / StyleGAN2 / StyleGAN3 (mentioned within Persistent Nature, Domain-Specific Image Super-Resolution, Animatable Gaussians)  
  * Temporally Coherent GANs for Video Super-Resolution (TecoGAN)  
  * Upscale image resolution GAN  
  * VQGAN (Vector Quantized Generative Adversarial Network)  
*   
* Hierarchical Generative Models: Models generating content at multiple levels of abstraction or resolution.  
* Neural Radiance Fields (NeRF) and Variants: Implicit neural representation learning 3D scene density and view-dependent color.  
  * Accelerated/Optimized NeRF (PlenOctree, SNeRG, MobileNeRF, BakedSDF, VMesh, BOG, VaxNeRF, NerfAcc, Cicero/SpaRW, NeRF-XL)  
  * Aleth-NeRF / Thermal-NeRF  
  * ASSIST: An object-wise neural radiance field  
  * BerfScene: Bev-conditioned Equivariant Radiance Fields  
  * Block-NeRF  
  * CityNerf (BungeeNeRF)  
  * CoCo-INR  
  * Compositional Neural Radiance Fields  
  * DehazeNeRF  
  * DoF-NeRF  
  * Dynamic NeRFs (Handles moving scenes, NeRF-DS, RoDynRF, DCTNeRF, DE-NeRF, FSD-NeRF, PAC-NeRF, Nerfies, HyperNeRF, T-NeRF)  
  * ENERF (Real-Time Neural Rasterization)  
  * Grid-guided Neural Radiance Fields  
  * HDR NeRF (LE3D, LTM-NeRF)  
  * HF-NeuS  
  * HumanNeRF  
  * HybridNeRF (Combines surface and volumetric rendering)  
  * Implicit radiance field  
  * Implicit texture imitating network  
  * Instant-NGP (Instant Neural Graphics Primitives)  
  * IntrinsicNeRF  
  * IRON (Inverse Rendering Optimizing Neural SDFs)  
  * KiloNeuS  
  * Language Embedded Radiance Fields (LERFs)  
  * Latent-NeRF  
  * Mega-NeRF  
  * Mip-NeRF / Mip-NeRF 360 (Anti-aliased NeRF)  
  * NeLF-Pro: Neural Light Field Probes  
  * NeRF (Neural Radiance Fields) (general concept, baseline)  
  * NeRF Network  
  * NeRF Player  
  * NeRF in the Wild (NeRF-W)  
  * NeRF++  
  * NeRSemble  
  * NeuMesh  
  * Neural implicit surfaces with Signed Distance Function (SDF)  
  * Neural MipTexture  
  * NeuRIS (Neural Reconstruction of Indoor Scenes using Normal Priors)  
  * NeuS / NeuS2 / Geo-NeuS / RNb-NeuS / Depth-NeuS (Neural Surface representation using SDFs)  
  * Noise-Aware NeRFs (NAN)  
  * PermutoSDF  
  * Point-NeRF  
  * Prompt2NeRF-PIL  
  * PS-NeRF / S3-NeRF (Neural Inverse Rendering for Multi-view Photometric Stereo / shading cues)  
  * PyNeRF  
  * Recursive-NeRF  
  * Ref-NeRF (Handles reflective surfaces)  
  * ScaNeRF: Scalable Bundle-Adjusting Neural Radiance Fields  
  * SDF-based NeRF variants (general, VoISDF, GSDF, NeuRodin)  
  * SeaThru-NeRF  
  * SparseNeuS  
  * SpecNeRF  
  * SSR (Single-view neural implicit Shape and Radiance field)  
  * TensoRF (Tensorial Radiance Fields)  
  * Tetra-NeRF  
  * Tri-MipNeRF  
  * Tri-plane features-based NeRF  
  * Voxel-based NeRF enhancements (VDF, CVT-xRF)  
  * Zip-NeRF  
*   
* Gaussian Splatting (3DGS / 2DGS / 4DGS) and Variants: Explicit scene representation using Gaussian primitives.  
  * 2DGS (2D Gaussian Splatting)  
  * 360-GS (Layout-guided Panoramic Gaussian Splatting)  
  * 3D Gaussian Splatting (3DGS) (general concept)  
  * 4D Gaussian Splatting (4D-GS) / 4DGF (Dynamic 3D Gaussian Fields)  
  * AbsGS  
  * BAD-Gaussians  
  * BIGS  
  * BlockGS  
  * CAO  
  * CityGaussian  
  * CoherentGS  
  * Color-cued Densification  
  * Compressed 3D Gaussian Splatting (General technique)  
  * Deblurring 3DGS  
  * DeferredGS  
  * DN-Splatter  
  * EAGLES (Efficient Accelerated 3D Gaussians)  
  * EGGS  
  * EndoGSLAM / EndoGaussian  
  * EVER  
  * F-3DGS  
  * Feature 3DGS (GS rendering semantic features)  
  * Flash3D / FlashGS  
  * FLoD  
  * FreGS  
  * GaMeS (Gaussian Mesh Splatting)  
  * GaRField++  
  * Gaussian Frosting (Mesh-based editing layer on GS)  
  * Gaussian Splashing (Physics-integrated 3DGS for fluids/solids)  
  * Gaussian Splatting Radiance Field  
  * Gaussian surfels (Point-based representation related to GS)  
  * GaussianBody  
  * GaussianCube  
  * GaussianDreamer / DreamGaussian (Generative Gaussian Splatting models)  
  * GaussianEditor (Editing with GS)  
  * GaussianHair (Uses cylindrical 3D Gaussians)  
  * GaussianHead (Deformable 3D Gaussians for head avatars)  
  * GaussianObject  
  * GaussianPro  
  * Gaussian Pancakes  
  * Gaussian Shader (Applies shading functions)  
  * GeoGaussian (Geometry-aware Gaussian Splatting)  
  * GigaVoxels DP  
  * GIR: 3D Gaussian Inverse Rendering / GS-IR / Relightable 3D Gaussians / GS-IR / GIR (Inverse rendering with 3DGS)  
  * GPS-Gaussian (Generalizable Pixel-Wise 3D Gaussians)  
  * GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting  
  * GS-Octree  
  * GSDF (3DGS Meets SDF)  
  * HDGS: Textured 2D Gaussian Splatting  
  * HFGS  
  * HiFi4G (Compact Gaussian Splatting for human performance)  
  * HUGS (Human Gaussian Splats) / HumanGaussian  
  * Hybrid Representations with GS (GauMesh, SUNDAE)  
  * Language Embedded 3D Gaussians  
  * LetsGo (LiDAR-assisted Gaussian Splatting)  
  * LightGaussian (Compressed 3DGS)  
  * Lightweight Predictive 3DGS  
  * LP-3DGS  
  * MCMC-based 3DGS  
  * MeshGS (Mesh-aligned Gaussian Splatting)  
  * Mini-Splatting  
  * Mipmap-GS / Mip-Splatting  
  * MirrorGaussian  
  * MoSca  
  * Multi-Scale 3D Gaussian Splatting (Anti-aliased GS)  
  * MVPGS  
  * NGM-SLAM  
  * Octree-GS  
  * Panoramic Gaussian Splatting  
  * Per-Gaussian Embedding Deformation  
  * PGSR (Planar-based Gaussian Splatting Reconstruction)  
  * PhysGaussian (Integrates physics simulation)  
  * Pyramidal 3D Gaussian Splatting (PyGS)  
  * Query-based Generalizable 3DGS  
  * RaDe-GS  
  * RadSplat  
  * Rig3DGS  
  * RTG-SLAM  
  * SA-GS (Scale-Adaptive Gaussian Splatting for Anti-Aliasing)  
  * SAGS  
  * SA4D  
  * Scaffold-GS (Anchor-based view-adaptive GS)  
  * SCube  
  * SGS-SLAM  
  * SolidGS  
  * Spec-Gaussian  
  * StopThePop  
  * Street Gaussians  
  * SuGaR: Surface-Aligned Gaussian Splatting  
  * SWAG  
  * TCLC-GS  
  * Textured-GS  
  * TRIPS (Trilinear Point Splatting \- combines GS ideas)  
  * V^3 (2D dynamic Gaussians)  
  * VastGaussian (3DGS for large scenes)  
  * VCR-GauS  
  * Vidu4D (DGS)  
  * VR-Splatting (foveated)  
  * Wild-GS / Splatfacto-W  
  * X-Gaussian  
  * 3DGStream  
  * 3DGSR  
  * 3iGS  
  * 6DGS  
*   
* Transformer architectures: Foundational architecture, often used within other models.  
  * Autoregressive Models / Transformers (General, sequence modeling)  
  * Cross-Scale Querying Transformer  
  * Texture Refinement Transformer  
  * Vision Transformer (ViT)  
*   
* Other Neural Rendering/Representation Models:  
  * Explicit/Hybrid Representations (Meshes, Planes combined with neural elements)  
  * FLAGS (Fast Layered Gaussian Surfels)  
  * FlashAvatar / HHAvatar / HQ3DAvatar (Head avatar reconstruction)  
  * Frequency-Modulated Point Cloud Rendering  
  * Hybrid Voxel/Surface Representations (NeuMesh)  
  * Image-Based Rendering (IBR) / View Synthesis (General technique)  
  * Implicit Neural Representations (INR) (General term)  
  * Instant-NSR (Fast neural surface reconstructor)  
  * Intrinsic PAPR  
  * K-Planes  
  * Layered Depth Maps (LDMs)  
  * LIRF (Local Implicit Ray Function)  
  * Multiplane Images (MPI) / AdaMPI / NeX (Enhanced MPI)  
  * Neural Assets (Volumetric object capture)  
  * Neural Light Spheres  
  * Neural Mesh-Based Graphics  
  * Neural Microfacet Fields  
  * Neural Pixel Composition (NPC)  
  * Neural Point Catacaustics  
  * Neural Point-Based Graphics (NPBG) / NPBG++ (Accelerated NPBG)  
  * Neural Point-based Volumetric Avatar (NPVA) / PointAvatar  
  * Neural Spline Fields  
  * NVS-Solver (Video diffusion for novel view synthesis)  
  * PAPR (Proximity Attention Point Rendering)  
  * PlenopticPoints (Point-based neural rendering)  
  * Point2Pix (Point renderer using NeRF pipeline)  
  * Point-Based Neural Rendering (General category)  
  * Textured Polygons  
  * TriVol (Triple volume point cloud representation)  
  * UV Volumes  
  * ViewFormer (Transformer-based view synthesis)  
  * VOctree (Video Octree)  
*   
* Procedural Generation:  
  * Generative node graph models (Generating Procedural Materials)  
  * Infinigen (Procedural Generator)  
  * Procedural Material Modeling (TexPro)  
  * Transformer-based conditional generative model (Generating Procedural Materials)  
* 

**II. Specific Model Implementations (Selected Standouts / Hybrids)**

* AttGAN: Specific cGAN architecture for attribute manipulation.  
* Custom Diffusion / E4T: Personalization/fine-tuning of text-to-image models.  
* DALL-E 2: Advanced text-to-image model (utilizes diffusion concepts).  
* DeepMasterPrints: Specific GAN application mentioned.  
* DreamBooth: Personalization/fine-tuning of text-to-image models.  
* DreamFusion / Magic3D / DreamGaussian: Text-to-3D generation using 2D diffusion priors.  
* EG3D: Generative model using tri-plane representation (basis for TriPlaneNet).  
* GIRAFFE / GIRAFFE HD: 3D-aware controllable generative models.  
* InstructPix2Pix: Image editing from instructions via diffusion.  
* Mirror GAN: Mentioned as a distinct technique.  
* Muse: Efficient Transformer-based text-to-image model.  
* OUR-GAN (One-shot Ultra-high-Resolution GAN): Generates UHR images from a single training image.  
* Pix2Pix models (incl. Pix2PixHD): cGANs for image-to-image translation.  
* Stargan variants (incl. Stargan-JNT): cGAN architectures for multi-domain image translation.  
* StyleGAN: (Implied by StyleSpace, Text Guided Facial Image Synthesis) Known for high-quality, style-controllable generation.  
* Text Guided Facial Image Synthesis Using StyleGAN and Variational Autoencoder Trained CLIP: Specific method combining multiple architectures.  
* Text2Room / Text2Scene / TEXTure: Text-guided 3D scene/texture generation.  
* VQGAN \+ CLIP: Combines Vector Quantized GANs with CLIP for text-guided generation.

**III. Image/Scene Enhancement, Restoration & Post-Processing**

* Super-Resolution (SR) Techniques: Increasing image resolution.  
  * A non-local approach for image super-resolution using intermodality priors  
  * An Improved Super Resolution Image Reconstruction Using SVD based Fusion and Blind Deconvolution Techniques  
  * Blind deconvolution techniques (for SR)  
  * Contourlet-based image super-resolution approach  
  * Deep Learned Super Resolution (General term)  
  * Deep Learning Super Sampling (DLSS) / MC-DLSS4 (Nvidia tech)  
  * Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution (LapSRN)  
  * Domain Transfer in Latent Space (DTLS)  
  * Edge preserving single image super-resolution  
  * Efficient Upsampling of Natural Images  
  * Enhanced Context Attention Network for Image Super Resolution (EASR)  
  * Enhanced Deep Super Resolution (EDSR)  
  * EpiMISR: Multi-image SR handling large disparities using epipolar geometry.  
  * ESRGAN (Enhanced Super-Resolution Generative Adversarial Network)  
  * Fine-grained video super-resolution (FGVSR)  
  * Hybrid approach of interpolations and CNN (for SR)  
  * Hybrid-SR: Combining traditional and ML-based SR techniques.  
  * Image Super-Resolution With Content-Aware Feature Processing  
  * Image super resolution using fusion of images  
  * Image super-resolution using gradient profile prior  
  * Incremental Residual Learning (IRL) framework  
  * IRE: Improved Image Super-Resolution Based on Real-ESRGAN  
  * Learning-Based Super-Resolution for Image Upscaling Using Sparse Representation  
  * MAŠA-SR (Reference-based Super-Resolution method)  
  * Multi-frame super-resolution  
  * Multi-Modal Image Super-Resolution (MISR)  
  * Multi-scale feature fusion residual network for Single Image Super-Resolution (MSFFRN)  
  * Multiple Residual Learning Network for Single Image Super-Resolution (MRLN)  
  * Neural Network-based Image Super-Resolution Techniques  
  * Neural Volume Super-Resolution  
  * Patch-Based Progressive 3D Point Set Upsampling  
  * Pixel Recursive Super Resolution  
  * Polynomial methods for upscaling  
  * Real-ESRGAN / Triple Real-ESRGAN: Advanced GAN-based SR.  
  * Residual Learning techniques (for SR)  
  * Single Image Super-Resolution (SISR)  
  * Singular Value Decomposition (SVD) based Fusion (for SR)  
  * Sparse Block Fusion Network (SBFN)  
  * Sparse representation methods (for SR)  
  * SRCNN: Super-Resolution Convolutional Neural Network.  
  * Sub-Pixel Convolution (for SR) / Sub-pixel convolution layer (for upscaling)  
  * Super resolution using edge prior and single image detail synthesis  
  * Super-Resolution (SR) (general concept)  
  * Super-Resolution Based Image Reconstruction  
  * Super-Resolution of Light Field Images Using Linear Subspace Projection of Patch-Volumes  
  * Super-resolution Image Processing Pipeline  
  * Super-resolution reconstruction of single image based on Res-Net and Sub-Pixel  
  * Super-Resolution using Sub-pixel Recursive Adversarial Network with Perceptual Loss  
  * TECHNOLOGY A SURVEY ON SUPER RESOLUTION TECHNIQUES  
  * Upsampling attention network (UAN)  
  * Upsampling Techniques (using compressed sensing)  
  * Very Deep Super Resolution Neural Network (VDSR)  
*   
* Denoising Techniques: Reducing noise.  
  * AI-Only Denoising: General term for AI-based denoising.  
  * Anisotropic Diffusion forPreservation ofLine-edges  
  * DWT Thresholding Techniques for Denoising of Images  
  * Efficient Edge Preserving Image Denoising using Non-Local Algorithms  
  * Fuzzy Filter Based on Fuzzy Logic for noise reduction  
  * Image Denoising using Autoencoders  
  * Multiscale Blind Denoising Algorithm  
  * NLM Variants and Extensions  
  * Noise Reconstruction / Iterative Noise Reconstruction: General term for reconstructing images by modeling/removing noise.  
  * Noise Removal from the Image Using Convolutional Neural Networks-Based Denoising Auto Encoder  
  * Noise-Aware NeRFs (NAN): NeRF variant specifically designed for burst denoising.  
  * Noise-Based Reconstruction Techniques  
  * Non-Local Means Denoising (NLM)  
  * Robust Average Networks for Monte Carlo Denoising  
  * Self-Supervised Deep Image Denoising  
  * Single Image Denoising through Downsampling and Self-Resolution Restoration Learning (NLR2NSR)  
  * Thresholding Techniques (Bayes Shrink, Normal Shrink, Neigh Shrink)  
*   
* Inpainting & Completion: Filling missing parts.  
  * Blended Diffusion  
  * Depth Inpainting (LayerPano3D)  
  * Egocentric refinement and inpainting (AnyHome)  
  * Hybrid Inpainting Scheme (DATENERF)  
  * Image Inpainting (PromptCharm) / Filling in missing or corrupted parts of an image.  
  * Inpainting an Image based on Enhanced Resolution  
  * LAMA (pre-trained inpainting model) (ASSIST)  
  * Mask-guided image editing (Ctrl-Room)  
  * Novel view inpainting (VividDream, FastScene)  
  * SUPER-RESOLUTION BASED IMAGE INPAINTING  
  * Text-conditioned inpainting model (Text2Room)  
*   
* Deblurring & Sharpening: Correcting blur and enhancing edges.  
  * Adaptive Image Restoration Based on Local Robust Blur Estimation  
  * Blind deconvolution techniques  
  * De-blurring algorithm (IMAGE SUPER RESOLUTION USING SPARSE NEIGHBOR EMBEDDING)  
  * Residual image sharpening  
*   
* HDR Imaging & Fusion: Handling high dynamic range.  
  * GlowGAN: Unsupervised GAN for generating HDR from LDR images.  
  * HDR Multi-Exposure Fusion  
  * HDR Panorama Generation (StyleLight)  
  * HDRSplat / HDR-GS / HDR-Plenoxels: Gaussian Splatting or Plenoxel variants for HDR.  
*   
* Other Enhancement & Post-Processing:  
  * Adaptive Contrast Enhancement (ACE)  
  * AI-powered upscaling techniques: Using AI to increase image resolution.  
  * Al Upscaling Techniques  
  * Anti-Aliasing Techniques (Mip-Splatting, Analytic-Splatting, SA-GS, Temporal Anti-Aliasing)  
  * BeyondScene: Framework for generating high-resolution (8K+) scenes.  
  * Color Adjustment Techniques  
  * Color Grading: Adjusting the overall color palette and mood.  
  * Color correction algorithms (Hierarchical Color Correction)  
  * Colorization Algorithms: Automatically adding color to grayscale images.  
  * Contrast Enhancement of Images Using Partitioned Iterated Function Systems  
  * Demosaicing  
  * Depth of Field (DoF) Simulation / Bokeh (Dr.Bokeh)  
  * Detail Me More: Technique using a "broker" module to improve GAN photo-realism.  
  * Edge detection (Canny, Laplacian)  
  * FFT upsampling in feature space using deformable convolutions  
  * Filtering (Gaussian, Bilateral, Shock, Low-pass, High-pass)  
  * FreeScale: Tuning-free inference paradigm using scale fusion.  
  * GAN Inversion: Techniques (like Cyclic Reverse Generator \- CRG) to find latent codes.  
  * High-resolution image generation techniques: General term for methods exceeding standard resolutions.  
  * Image Enhancement Techniques (general)  
  * Image Filtering & Enhancement (General adjustments)  
  * Image Illumination based on Tone Mapping for uneven illumination  
  * Image Upscaling Techniques Analysis  
  * Interpolation techniques (Bicubic, Bilinear, Nearest Neighbor, EASE)  
  * Lens shading correction  
  * Marching Cubes (related to post-processing/extraction)  
  * Mesh simplification (Quadric error metrics)  
  * Motion Blur Simulation: Adding blur to represent movement.  
  * Multiple-level residual and dense structure: Architectural design for enhancing upscaling.  
  * Photomontage: Combining elements from multiple photographs.  
  * Poisson reconstruction (SuGaR)  
  * progressive growing: Training technique starting with low resolution and increasing it.  
  * Quantization (EAGLES, Language Embedded 3D Gaussians)  
  * Random down-sampling method: Technique used in an 8K HDR upscaling approach.  
  * Real-Time depth Map Up sampling for Stereoscopic Video shows  
  * ResMaster: Training-free method for high-resolution generation.  
  * Scale fusion: Combining information from different receptive scales.  
  * Segmentation (general, semantic, panoptic, instance)  
  * Space contraction (ScaNeRF, MERF)  
  * UV Mapping / Smart UV projection  
* 

**IV. 3D Reconstruction, Representation & Rendering Techniques**

* 3D Reconstruction & Representation: Creating 3D models from data.  
  * ConceptGraphs: Open-Vocabulary 3D Scene Graphs  
  * CVXNet (convex decomposition)  
  * Davidsonian Scene Graph (DSG)  
  * Deep Marching Tetrahedra (DMTet)  
  * Depth Estimation (MiDaS, DPT)  
  * DMTet (Deformable Mesh Tetrahedra)  
  * Editable Primitives  
  * Explicit mesh representation (SuGaR, BakedSDF, FEGR, Traditional polygon meshes)  
  * FlexiCubes: Gradient-based mesh extraction method.  
  * Holistic scene code parameterization  
  * Hybrid 3D representation (Explicit objects, Implicit scenes)  
  * Learnable structured scene graph (DIScene)  
  * Level of Detail (LOD) Management (Voxel-Based LOD, Dynamic LOD, Adaptive LOD, Octree-GS)  
  * Marching Cubes / Marching Tetrahedra (Surface extraction)  
  * Mesh Reconstruction (General) / Surface Reconstruction (General)  
  * Multi-View Stereo (MVS): Used for depth/geometry estimation.  
  * Neural Implicit Surface Reconstruction (NeuS, NeuS2, MonoSDF, etc.)  
  * Object Scene Representation Transformer (OSRT) / Object Slots  
  * Photogrammetry / Structure from Motion (SfM) (COLMAP)  
  * Poisson Surface Reconstruction  
  * Pose Estimation: Determining position and orientation.  
  * QUADify: Method for extracting quad-dominant meshes.  
  * Simultaneous Localization and Mapping (SLAM) (NeRF-SLAM, SplaTAM, Droid-SLAM, Photo-SLAM)  
*   
* Rendering Techniques: Creating 2D images from 3D data.  
  * Ambient Occlusion (AO)  
  * BEV (Bird's-Eye View) scene representation  
  * BRDF (Bidirectional Reflectance Distribution Function) modeling  
  * Deferred Shading/Rendering  
  * Differentiable Rendering: General class enabling gradient-based optimization.  
    * Conditional Mixture Path Guiding for Differentiable Rendering  
    * Differentiable Signed Distance Function (SDF) Rendering  
    * Differentiable splat-based rasterizer (used in point-based methods)  
    * Differentiable volume rendering (used in NeRF)  
    * Monte Carlo differentiable rendering  
    * Parameter-space ReSTIR for Differentiable and Inverse Rendering  
    * Path-space differentiable rendering  
    * Physically-based differentiable rendering (PBDR)  
    * PSDR-Room (Single Photo to Scene using Differentiable Rendering)  
    * Recursive Control Variates for Inverse Rendering  
    * Variance-aware inverse rendering  
  *   
  * Fast Layered Gaussian Surfels (FLAGS)  
  * Global Illumination (GI)  
  * Image-Based Lighting (IBL)  
  * Inverse Rendering (General concept, decomposing images; NeILF, NeMF, PhyIR, TensoIR, IRON, PS-NeRF, GIR, Neural Microfacet Fields)  
  * Layered 3D Panorama (LayerPano3D)  
  * Lighting (General concept)  
  * Light Probes  
  * Multiresolution Texture Field  
  * Neural Shading / Neural Textures  
  * Neural Street Scene Renderer (NSSR)  
  * Panoptic neural radiance field  
  * Physically Based Rendering (PBR)  
  * Rasterization (Traditional graphics pipeline component; triangle, tile-based)  
  * Ray Tracing / Ray Marching / Sphere Tracing (Core rendering technique)  
    * Monte Carlo Ray Tracing / Path Tracing  
    * Photon Mapping / Photon-Tracing  
    * Real-Time Path Guiding  
  *   
  * Scene Language (Programs, Words, Embeddings)  
  * Scene node data structure  
  * Shading & Materials (General concept)  
  * Spherical Harmonic Latent Texture Map / Spherical Harmonics / Spherical Gaussians  
  * Stroke-Based Rendering (Simulated brush strokes, texture bombing)  
  * Subsurface Scattering (SSS)  
  * Texture Mapping & Synthesis (General concept)  
    * PBR Material Generation (DreamMat)  
    * Procedural Texture Generation / Generating Procedural Materials from Text or Image Prompts (TexPro)  
    * Text-to-Texture Synthesis (Paint-it, TEXTure, Text2Tex, InstanceTex, SceneTex, TextMesh, TEXGen)  
  *   
  * UV texture maps  
  * Volumetric Rendering (Simulating light interaction within a volume)  
  * Voxelization Algorithms: Converting representations to voxels.  
* 

**V. Techniques for Controlling Generation & Guidance**

* Conditional Input Guidance: Using various inputs to guide generation.  
  * Bounding box guidance  
  * Class/text conditional generation  
  * CLIP-Guided Techniques  
  * Conditional Inputs (labels, text, etc. \- general method)  
  * Depth guidance  
  * Explicit geometry guidance  
  * Geometric constraints  
  * Geometry-aware score distillation  
  * Integration of conditional inputs  
  * Layout guidance (SceneCraft, GALA3D, Ctrl-Room)  
  * Mask guidance  
  * Normal guidance  
  * Reference images (StyleCity, TEXTure, etc.)  
  * Semantic segmentation guidance  
  * Structural and fine-grained guidance  
*   
* Style & Attribute Control:  
  * LAFITE: Technique potentially related to style control.  
  * Latent Space Exploration: Manipulating latent vectors to control image attributes.  
  * Latent Space Interpolation/Manipulation (character blending)  
  * Neural Style Transfer: Merging content from one image with the style of another.  
  * SEMSTYLE: Technique potentially related to semantic style control.  
  * StyleSpace Analysis: Method for finding disentangled controls within StyleGAN's latent space.  
*   
* Semantic Control:  
  * Semantic Image Editing: Few-shot approach to control synthesized image semantics.  
  * Semantic Segmentation for Image Generation: Using semantic maps to guide content placement.  
  * Semantic-Conditional Sampling: Few-shot approach to generate images based on a semantic layout.  
*   
* Text & Embedding Control:  
  * Embedding inversion: Optimizing latent embeddings to match an image.  
  * Prompt inversion: Deriving text prompts from a given image.  
  * Text-to-Image Generation Techniques: Overall category for generating images from text prompts.  
  * Textual Inversion: Creating custom tokens for specific concepts/styles.  
*   
* Model Adaptation & Tuning:  
  * Fine-Tuning Pretrained Models: Adapting models to specific styles or domains.  
  * LoRa Model Fine-tuning: Technique for adapting large pre-trained models.  
*   
* Sampling Strategies & Control Variates: Controlling output randomness and properties during generation.  
  * Adaptive sampling strategy (Gaussian in the Wild)  
  * Adaptive Temperature (AdapT) sampling  
  * Asynchronous Score Distillation (ASD)  
  * Classifier Score Distillation (CSD)  
  * Coarse-to-fine sampling process (LiveScene)  
  * Control Variates (general concept)  
  * DDIM sampling/scheduler  
  * Expressive sampling algorithms  
  * Formation Pattern Sampling (FPS)  
  * Frequency and presence penalties  
  * Frustum-based sampling method (HDGS)  
  * GRIS (Generalized Resampled Importance Sampling)  
  * Guided Sampling (SceneControl)  
  * Hybrid sampling strategy (Spiral \+ Ray sampling)  
  * Joint multi-scale diffusion sampling approach  
  * Karras scheduler  
  * Low-entropy sampling strategies  
  * Maximum number of tokens / Stop sequences  
  * Object-centric camera pose sampling  
  * Positivization (Parameter-space ReSTIR)  
  * PRIS (Positivized Resampled Importance Sampling)  
  * Progressive Three-Stage Camera Sampling Strategy  
  * Proposal Sampler Strategy (ASSIST)  
  * Recursive Control Variate  
  * Sampling techniques for generative AI / Sampling algorithms (general; top-k, nucleus/Top P, tempered)  
  * Score Distillation Sampling (SDS) / Geometry-aware score distillation / Structure-Aware SDS  
  * Score debiasing  
  * Temperature Sampling Strategies / Temperature control techniques (temperature parameter)  
  * Truncation sampling heuristics / Truncation methods  
  * Variational Score Distillation (VSD)  
* 

**VI. Prompting Methods, Techniques & Optimization**

* Core Prompting Concepts:  
  * Prompt Engineering: The general practice of crafting effective prompts.  
  * Prompt Engineering Resources: Tools and guidelines for prompt optimization.  
  * Prompt Fidelity: Degree to which output matches the input prompt.  
  * Text prompts (general use)  
*   
* Prompt Types & Modalities:  
  * Enriched textual prompts / Tailored image prompts  
  * Few-Shot Prompting / Few-shot learning / In-context learning (ICL)  
  * Geometric/Spatial Prompts (bounding boxes, segmentation masks, scribbles, depth, normal, layout)  
  * Hard Prompts Made Easy (gradient-based optimization)  
  * Image Prompts (Single or multiple images)  
  * Joint Text/Image Prompts  
  * Language Instructions (for Agents)  
  * Layout & Geometric Guidance (as prompt input)  
  * Multi-modal Prompting (general concept)  
  * Negative Prompt Guidance  
  * Rich Text prompts (Expressive Text-to-Image Generation)  
  * Text Prompts (Natural language descriptions)  
  * Trajectory Prompts (Specifying motion paths)  
  * View-dependent text prompting  
  * Visual Prompts (Image Guidance, Style Guidance)  
  * Zero-Shot Prompting  
*   
* Prompt Generation & Optimization:  
  * AI-enhanced prompt generations: Using AI to help create or refine prompts.  
  * Algorithmic Prompting Techniques (GPTDrawer): Iteratively refining prompts.  
  * AutoPrompt (Hard Prompts Made Easy)  
  * Automatic prompt optimization framework  
  * FluentPrompt (Hard Prompts Made Easy)  
  * LLM-based prompt generation/interpretation  
  * Metadata expansion: Enhancing prompts with additional context.  
  * NLP analysis of a large prompt database  
  * Optimized prompts: The output of prompt optimization efforts / desired outcome.  
  * Paragraph Extraction using Zeros (PEZ) (Hard Prompts Made Easy)  
  * Prompt Exploration & Analysis (PromptLandscape, PrompTHis)  
  * Prompt Expansion (Prompt Expansion for Adaptive T2I)  
  * Prompt Mixing (Localizing Object-level Shape Variations)  
  * Prompt Refinement (PromptMagician, PrompTHis)  
  * Prompt Spectrum Space P\* / ProSpect (Prompt Spectrum representation)  
  * Prompt Suggestion (PromptMagician, Promptify)  
  * Prompt template design: Creating structured prompts.  
  * Prompt tuning (DreamDistribution)  
*   
* Advanced Prompting Frameworks/Techniques:  
  * Automatic Chain of Thought Prompting (Auto-CoT)  
  * Chain-of-Thought (CoT) Prompting  
  * Continuous Prompts (context/coherence)  
  * delayed projection scheme (used within prompt inversion)  
  * Feedback Prompting  
  * Instruction Tuning  
  * Interactive Prompt Exploration (PromptMagician)  
  * Iterative refinement process: Developing prompts through testing and refinement.  
  * Prompt debiasing (Debiasing Scores and Prompts)  
  * Prompting state-of-the-art (SOTA) LLMs (e.g., ChatGPT specific techniques)  
  * Prompting techniques: General term covering various methods (zero-shot, few-shot, feedback, chain-of-thought, tree of thoughts, instruction tuning, RAG, ReAct)  
  * ReAct / Reaction & Act Prompting  
  * Reflection: Evaluating and refining responses based on prompts/critiques.  
  * Retrieval Augmented Generation (RAG)  
  * Sequential testing: Iterative prompt testing.  
  * Tree of Thoughts  
  * Universal Self-Adaptive Prompting (USP)  
* 

**VII. Architectural Components, Training Strategies & Evaluation**

* Network Architectures & Modules:  
  * Attention Blocks (general, Multi-level, Pixel, Channel, CAFD, HAFFB, RFAB)  
  * Attention Mechanisms / attention model based on transformers (General concept)  
  * BERT encoder  
  * Color correction network  
  * Compact weighting network  
  * Consistency-controlling super-resolution module  
  * Convolutional feature renderer  
  * Convolutional Neural Networks (CNNs) (as components)  
  * Cross-attention (general use in diffusion models)  
  * Cross-attention decoder  
  * Differential Camera Encoder  
  * Discriminator network (GANs)  
  * Encoder-Decoder Architectures  
  * Feature Fusion with Attention  
  * Feature Pyramid Networks (FPN)  
  * Gaussian selector module  
  * Generator network (GANs)  
  * Graph Neural Networks (GNNs) (Triplet-GCN, Lane Graph GNN)  
  * Hybrid 2D-3D network/block  
  * Information Echo Scheme  
  * Layout Refinement Module  
  * Mapping network  
  * Mixture of Expert (MoE) modules / Shared Expert  
  * MLPs (Multi-Layer Perceptrons)  
  * Multi-resolution hash encoding / Hash Grids  
  * Multi-scale Networks  
  * Parallel Attention Module (PAM)  
  * Pixel and Channel Attention Blocks  
  * pre-trained visual encoder: Component used to extract features.  
  * Proximity Attention (PAPR)  
  * Residual Dense Block (RRDB)  
  * Residual Learning / ResNet  
  * Self-attention (general use in diffusion models)  
  * Self-attention re-weighting  
  * Semantic-Aware Discriminator  
  * Sparse Block (SBFN)  
  * Super Resolution (SR) module  
  * Transformers (general, self-attention-based reasoning, spatial)  
  * U-Net  
  * Variation Network  
  * vertical positional embeddings: Specific architectural feature.  
*   
* Training Strategies & Optimization Algorithms:  
  * Adafactor  
  * Adam Optimizer / AdamW  
  * ADMM (Alternating Direction Method of Multipliers)  
  * Adversarial Training  
  * Clustering (for pruning/organizing primitives)  
  * Coarse-to-fine optimization/training strategy  
  * Contrastive Learning  
  * Data Augmentation Techniques  
  * Deferred backpropagation  
  * Differentiable Optimization (General concept)  
  * Ensemble learning  
  * Fine-tuning (general)  
  * Gradient checkpointing  
  * Gradient descent: Core optimization algorithm.  
  * HDBSCAN  
  * Hierarchical agglomerative clustering  
  * In-context learning (SceneTeller)  
  * Kernel Principal Component Analysis (Kernel-PCA)  
  * Levenberg-Marquardt (LM)  
  * Mini-batched K-means algorithm  
  * Mixed-precision training  
  * multi-task learning: Training strategy.  
  * Noise Injection / dimensionality reduction (during training or within architectures)  
  * Noise Sampling Technique  
  * Optimization Algorithms (General: ADAM, LM, ADMM, SGLD)  
  * Particle Swarm Optimization (PSO)  
  * Powell algorithm  
  * Progressive training strategy  
  * Regularization (general, Identity, View consistency, Eikonal, Curvature, Smoothness, Light, Density, Shape, L1, L2)  
  * Regularized sampling  
  * Reparameterization trick  
  * Self-Supervised Learning  
  * Self-training (Invisible Stitch)  
  * SGLD (Stochastic Gradient Langevin Dynamics)  
  * Stochastic Gradient Descent (SGD)  
  * Teacher distillation (Invisible Stitch)  
  * Transfer Learning  
  * Two-stage approach / learning curriculum  
  * Union-sampling training strategy  
  * Welford's Algorithm  
*   
* Loss Functions & Metrics:  
  * AbsRel (Absolute Relative Error)  
  * Adversarial loss function  
  * AMBE (Absolute Mean Brightness Error)  
  * Attention-based localization loss  
  * BER (Bit Error Rate)  
  * BRISQUE  
  * CA (Contextual Alignment)  
  * CD (Chamfer Distance)  
  * CIQA  
  * CLIP Loss / Similarity / CLIP Score  
  * Contrastive Loss  
  * Depth Loss  
  * Difference loss (L\_diff)  
  * EQT (Equivariance Test)  
  * Evaluation Metrics (General)  
  * F-Score  
  * FID (Fréchet Inception Distance)  
  * FVD (Fréchet Video Distance)  
  * Human Evaluation / User Studies  
  * Hybrid Objective Function (GAN loss, MSE loss, Perceptual loss)  
  * Inception Score (IS)  
  * KID (Kernel Inception Distance)  
  * KVD (Kernel Video Distance)  
  * L1 Loss  
  * Local-rigidity loss (L\_rigid)  
  * Loss function optimization / network architecture improvements: General areas of development.  
  * Loss on cross-attention maps  
  * MAE (Mean Absolute Error)  
  * Masked diffusion loss  
  * Mean Precision / Recall  
  * mIoU (mean Intersection over Union)  
  * MSE (Mean Squared Error) Loss  
  * NC (Normal Consistency)  
  * NIQE  
  * Normal Consistency Loss  
  * Perceptual loss function: Loss based on perceptual similarity (often includes Adversarial loss, Content loss). / LPIPS (Learned Perceptual Image Patch Similarity)  
  * PSNR (Peak Signal-to-Noise Ratio)  
  * Q-Align  
  * R-Precision  
  * Reconstruction Loss  
  * Regularization Losses (Eikonal, Curvature, Volume, Density, R1 gradient, Identity, View consistency, Orthogonal, Penetration)  
  * RMSE (Root Mean Squared Error)  
  * Rotational loss (L\_rot)  
  * Smoothness Loss  
  * SSIM (Structural Similarity Index Measure) / D-SSIM Loss  
  * x0-reconstruction loss  
*   
* Datasets & Benchmarks:  
  * 3RScan  
  * ARKitScenes  
  * Blender Synthetic Dataset  
  * BlendedMVS  
  * Carla  
  * CLEVR  
  * Deep Blending dataset  
  * DiffusionDB  
  * Front-3D  
  * High-Resolution Image Reconstruction Datasets  
  * HM3D  
  * HoliCity  
  * ImageNet  
  * InterReal dataset  
  * LAION-400M  
  * Make3D Range Image Dataset  
  * Mip-NeRF 360 dataset  
  * MultiScan  
  * MultiShapeNet  
  * NeRF-OSR dataset  
  * NYUv2  
  * Objaverse  
  * OmniSim dataset  
  * Pix3D dataset  
  * ProcTHOR  
  * ScanNet  
  * SceneVerse  
  * Street View  
  * Structured3D  
  * Tanks and Temples dataset  
  * Upright360 dataset  
  * Waymo Open Dataset  
  * YCB-V dataset  
*   
* Core Concepts:  
  * Coherent global structure: Desired output property.  
  * latent variables / hierarchical latent variables: Core concept of the compressed representation space.  
  * semantic information: The meaning/context captured by the model.  
  * Vision-language model: Models bridging vision and text (e.g., CLIP).  
* 

**VIII. Data Handling & Representation Concepts**

* Dimensionality Reduction: Reducing the number of variables.  
  * Kernel Methods (for non-linear manipulation, e.g., Kernel t-SNE)  
  * PCA (Principal Component Analysis): Linear dimensionality reduction.  
  * t-SNE (t-distributed Stochastic Neighbor Embedding): Non-linear visualization.  
  * UMAP (Uniform Manifold Approximation and Projection): Non-linear visualization.  
*   
* Feature Representation & Extraction: How data features are encoded/identified.  
  * CLIP embeddings  
  * DINOv2 features  
  * Explicit Representation (meshes, point clouds, voxels)  
  * Facial Recognition and Manipulation  
  * Feature Vectors / Embeddings: Numerical representations.  
  * Hash Grids / Multi-resolution Hash Encoding  
  * Histograms of oriented gradients (HOG)  
  * Implicit Representation (shapes/scenes via functions like SDF, NeRF)  
  * Instance-aligned features  
  * Kernel Principal Component Analysis (Kernel-PCA) (as feature extraction)  
  * Latent Space: Compressed representation learned by models.  
  * Latent Space Representation (as output of extraction)  
  * Pattern Recognition for Graphic Elements  
  * Pixel-aligned features  
  * Sentence-BERT embeddings  
  * Sparse representation  
  * SuperPixels / SuperTexels: Grouping pixels/texels into meaningful regions.  
*   
* Data Handling:  
  * Data Fusion & Integration: Combining data from different sources/modalities.  
  * Data Validation (TFX): Ensuring data quality and consistency.  
  * HDR Multi-Exposure Fusion (as data fusion)  
  * Multi-Modal Fusion Techniques (text, images, LiDAR, audio)  
  * Tensor-Based Techniques: Using tensors for data representation/processing.  
* 

**IX. Related Applications, Use Cases, Editing & AI Design**

* Editing Techniques & Frameworks:  
  * Concept removal: Specific editing task enabled by prompt inversion/optimization.  
  * DIFF EDIT: Technique for editing images using diffusion.  
  * Editing Frameworks: Pipelines specifically designed for editing existing 3D representations based on prompts (GSEdit, TIP-Editor, TrAME).  
  * Face Manipulation: Altering facial features in images.  
  * Image-to-Image-Translation (Covered by Pix2Pix, cGANs)  
  * Instruct-NeRF2NeRF (IN2N)  
  * Object-level scene editing (DORSal)  
  * ReplaceAnything3D (RAM3D)  
*   
* Specific Applications & Use Cases:  
  * 3D Asset Creation (games, VR/AR, film)  
  * 3D Image Synthesis (Mentioned as a GAN application area)  
  * 3D Scene Generation Frameworks (Scene123, VividDream, Text2VRScene, etc.)  
  * AR Integration: Potential application area.  
  * Artistic Styles (Surrealism, Cubism, etc. as application output)  
  * Automated Layout Generation  
  * Autonomous Driving: Scene rendering, simulation, sensor modeling (NeuRAD).  
  * Character Rendering/Avatars (GVA, FlashAvatar, HQ3DAvatar, IntrinsicAvatar, EyeNeRF)  
  * Collaborative art projects  
  * Controllable Generation: Generating 3D content with specific controls.  
  * Cultural Heritage Documentation: 3D reconstruction of artifacts/sites.  
  * Generative Design Algorithms  
  * Graphic Design (logo, icon, layout, font generation)  
  * Image restoration / facial restoration: Applications focused on improving existing images.  
  * Image-to-3D Asset Generation: Reconstructing 3D assets from images.  
  * Language-Guided Medical Image Analysis (segmentation, quantitative analysis)  
  * Language-Guided Robotic Manipulation  
  * Medical Imaging: Visualization and super-resolution for medical volume data.  
  * Personalized art generation / art restoration  
  * Rendering Qualities (Hyperrealism, Photorealism, etc. as application goal)  
  * Scene Reconstruction: Creating 3D models of real-world environments.  
  * Semantic Scene Understanding/Segmentation: Using language or VLMs.  
  * Specific Visual Motifs/Themes (Skulls, Dragons, etc. as application output)  
  * Style Transfer Algorithms (Neural Style Transfer, Arbitrary Style Transfer)  
  * Text-to-3D Asset Generation (objects, avatars, portraits, scenes) / Text-to-3D Synthesis  
  * Text/Image-Guided 3D Editing  
  * Video generation: Related field of generating sequences of images.  
*   
* AI-Driven Design & Decision Making:  
  * AI-Driven Decision Making: General term for AI making operational choices.  
  * Autonomous Navigation Systems: AI for self-driving/piloting.  
  * Elk Herd Optimizer (EHO): Specific optimization algorithm for design.  
  * Evolutionary Algorithms: Optimization inspired by biological evolution for design.  
  * Gradient Projection Methods: Iterative optimization schemes for design.  
  * Iterative Linearized Graphic Design (iLGD): Specific algorithm for graphic design optimization.  
  * Optimization Methods: Algorithms for finding the best solution within constraints (for design).  
  * Reinforcement Learning: Learning through trial-and-error with rewards (for design optimization).  
  * Target Recognition AI: AI for identifying targets.  
* 

**X. Literary Character Description Techniques (from Portraits.csv)**  
*(Note: Describes characters in narrative, not image generation algorithms/prompts)*

* Physical Appearance Description:  
  * Age Indicators  
  * Attractive appearance of positive characters  
  * Distinctive Marks  
  * Grooming Habits  
  * Hair Color Descriptions  
  * Hair Texture and Style  
  * Height and Build  
  * Physical Condition  
  * Physical traits (looks, dress, movement)  
  * Skin Tone and Condition  
  * Specific features of the exterior  
  * Symmetry and Asymmetry  
  * Ugliness in character portrayal  
*   
* Facial Features & Expressions:  
  * Eye Color and Expression  
  * Facial Descriptions  
  * Facial expressions signalling emotional states / behavioral intentions  
  * Gaze direction  
  * Stereotypic beliefs (related to facial appearance)  
*   
* Body Language & Gestures:  
  * Body Language  
  * Gesture  
  * Physical Quirks  
  * Posture and Movement  
  * Grace and plastic movements in women's portraits  
*   
* Clothing & Accessories:  
  * Character Accessories  
  * Clothing Style  
  * Cultural Markers (clothing, hairstyles)  
*   
* Voice & Speech:  
  * Characters' speech  
  * Voice and Speech Patterns  
*   
* Figurative Language:  
  * Comparisons  
  * Epithets (general, Affective, Figurative, Эпитеты персонажа, эпитеты, описывающие одежду, яркие портретные эпитеты)  
  * Figurative language in character portrayal  
  * Metaphors (Метафоры)  
  * Similes (Сравнения)  
*   
* Psychological & Emotional Reflection:  
  * Behavior/actions  
  * Bright feature of the person  
  * Change (character development)  
  * Character Appearance Transformation  
  * Character Portrait Techniques (general)  
  * Character's psychological reaction to events  
  * Complex/simple personality  
  * Contrast  
  * Descriptive names (Говорящие имена, Прямые наименования)  
  * Direct characterization  
  * Dreams  
  * Emotional elements in portraits  
  * Evaluative connotation (Оценочная коннотация в детерминантах)  
  * Features revealing emotional/mental condition  
  * History and background  
  * Moral constitution  
  * Motivation  
  * Portrait as a reflection of inner world  
  * Psychological/personality traits  
  * Relationships with other characters  
  * Repetitive Character Descriptions  
  * Strengths/virtues  
  * Weaknesses/faults  
* 

**XI. Creative Prompting Examples (from \_Random Stupid Stuff... file)**

* Divine DIY Disasters (Renaissance scenes with mishaps)  
* Mona Lisa's Secret Pizza Recipe  
* The Arnolfini Portrait: Pet Extravaganza  
* The Birth of Venus: Spa Day Extravaganza  
* The Garden of Earthly Delights: Reality TV Show  
* The Girl with a Pearl Earring: Social Media Maven  
* The Kiss of Judas: Awkward First Date  
* The Last Judgment: Everyday Nonsense Edition (Biblical scene with mundane elements)  
* The Last Supper: Fast Food Showdown  
* The Madonna of the Pinks: Flower Shop Drama  
* The Night Watch: Office Shenanigans  
* The Persistence of Memory: Alarm Clock Meltdown  
* The School of Athens: Modern Mayhem (Philosophers in modern scenarios)

This consolidated list covers the diverse range of topics found in the provided text, organized logically while removing exact duplicates within each section.

