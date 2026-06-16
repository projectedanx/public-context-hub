Core 3D Representation & Rendering Techniques

* 3D Gaussian Splatting (3DGS) & Variants/Extensions:  
  * 2D Gaussian Splatting (2DGS / 2D GS)  
  * 2DGH: 2D Gaussian-Hermite Splatting  
  * 3D Gaussian Splatting (3DGS / 3D-GS)  
  * 3D Half-Gaussian Splatting (3D-HGS)  
  * 4D Gaussian Splatting (4D-GS / 4DGS / 4DRotorGS)  
  * 6D Gaussian Splatting (6DGS)  
  * Adaptive Density Control (ADC) / Densification / Splitting / Pruning (General 3DGS concepts)  
  * AGG: Amortized Generative 3D Gaussian framework  
  * Analytic-Splatting  
  * Anchor-2D-GS / Anchor-3D-GS  
  * AtomGS (Atomized Proliferation, Geometry-Guided Optimization, Edge-Aware Normal Loss)  
  * BAD-Gaussians: Bundle Adjusted Deblur Gaussian Splatting  
  * BAGS: Blur Agnostic Gaussian Splatting (Blur Proposal Network \- BPN, Coarse-to-fine kernel optimization)  
  * Balanced 3DGS (Gaussian-wise parallel rendering, Fine-grained tiling, Inter-block dynamic workload distribution, Self-adaptive kernel selection)  
  * BoostDream (3D Model Distillation, Multi-view SDS Loss)  
  * BrightDreamer (Text-guided Shape Deformation \- TSD, Text-guided Triplane Generator \- TTG)  
  * CG-SLAM (Uncertainty-aware 3D Gaussian field, Depth uncertainty model)  
  * Characterizing Satellite Geometry via Accelerated 3DGS  
  * CityGaussian (CityGS \- Divide-and-conquer training, Block-wise LoD)  
  * CoherentGS (Regularized optimization, Depth-based initialization)  
  * Compact 3D Gaussian Splatting (Static & Dynamic) (Learnable mask strategy, Grid-based neural field for color, R-VQ for geometry/temporal)  
  * Compact3D  
  * CompGS: Compressed Gaussian Splatting (Hybrid primitive structure, Anchor primitives, Rate-constrained optimization)  
  * CoR-GS (Co-pruning, Pseudo-view co-regularization)  
  * CoSSegGaussians (Dual Feature Fusion Network, Explicit DINO feature unprojection, Point cloud spatial features)  
  * DDGS: Direction-Disentangled 3DGS  
  * Deblurring 3D Gaussian Splatting (using MLP for covariance)  
  * DiffGS (Disentangled Gaussian functions, Discretization algorithm)  
  * DisC-GS: Discontinuity-aware Gaussian Splatting (Bézier-boundary gradient approximation)  
  * DN-Splatter (Edge-aware depth loss, Monocular normal priors)  
  * DoGaussian (Scene decomposition, ADMM)  
  * DreamScene (Formation Pattern Sampling \- FPS, Progressive Camera Sampling)  
  * DreamScene360 (Panoramic Gaussian Splatting, Diffusion guidance, Geometric field init)  
  * Dynamic Gaussian Marbles (Isotropic Gaussians, Divide-and-conquer learning)  
  * EG4D (Attention Injection Strategy, Gaussian Splatting dynamic reconstruction, Diffusion refinement)  
  * EGGS: Edge Guided Gaussian Splatting  
  * EfficientGS (Selective densification, Pruning mechanism, Sparse SH order increment)  
  * Endo-4DGS (Lightweight MLPs for deformation, Depth-Anything prior, Confidence-guided learning)  
  * EndoGS / EndoGaussian (Deformation fields, Depth-guided supervision, Surface-aligned regularization)  
  * EndoGSLAM (Streamlined Gaussian representation, Differentiable rasterization)  
  * EVER: Exact Volumetric Ellipsoid Rendering (Primitive-based representation, Ray tracing)  
  * Feature Splatting (Distilling vision-language features into 3D Gaussians)  
  * Fed3DGS (Federated Learning for 3DGS, Distillation-based update, Appearance modeling)  
  * FlashGS (Redundancy elimination, Efficient rendering workflow)  
  * FreGS (Progressive frequency regularization)  
  * GALA3D (Layout-guided GS, Compositional optimization, Diffusion priors)  
  * GaMeS: Gaussian Mesh Splatting  
  * Gamba (GambaFormer, Mamba-based backbone, Gaussian Decoder)  
  * GaRField++ (Ray-Gaussian intersection, Gaussians density control, Appearance decoupling module, Refined loss)  
  * Gaussian Splashing (Underwater adaptation, Sea-thru model, Depth estimation proc.)  
  * Gaussian Time Machine (GTM \- Time embedding MLP, Decomposed color model)  
  * GaussianBody (Explicit pose-guided deformation, Physically-based prior, Pose refinement, Split-with-scale)  
  * GaussianCube (Densification-constrained GS fitting, Optimal Transport rearrangement)  
  * GaussianDreamer  
  * GaussianDreamerPro (Binding Gaussians to evolving mesh geometry)  
  * GaussianFlow (Gaussian flow concept, Splatting dynamics, Optical flow supervision)  
  * GaussianHair (Cylindrical 3D Gaussians, UE4 scattering, Strand-wise density control)  
  * GaussianImage (2D Gaussian Splatting for images, Accumulated summation rendering)  
  * GaussianObject (Visual hull, Floater elimination, Gaussian repair model, Self-generating strategy)  
  * GaussReg (Coarse-to-fine registration, Image-guided fine registration)  
  * GauStudio (Modular 3DGS framework, GauS surface reconstruction)  
  * GeoGaussian (Initialization of thin Gaussians, Densification strategy, Geometry constraints)  
  * GeoGS3D / FDGaussian (Orthogonal plane decomposition, Epipolar attention GS acceleration)  
  * GeoRGS: Geometric Regularized 3DGS (Seed patch selection, Depth similarity regularization)  
  * GES: Generalized Exponential Splatting (Generalized Exponential Function \- GEF)  
  * GGRt (Iterative Pose Optimization Network \- IPO-Net, Generalizable 3D-Gaussians \- G-3DG, Deferred back-propagation, Progressive Gaussian cache)  
  * GI-GS: Global Illumination Decomposition on GS (Deferred Shading, PBR, Path Tracing)  
  * GigaGS (Partitioning strategy, Multi-view consistency constraints, LOD representation)  
  * GoMAvatar (Gaussians-on-Mesh representation)  
  * GraspSplats (Depth supervision, Reference feature computation)  
  * GS-ID (2DGS for geometry/material, Deferred Rendering, Parametric lights, Diffusion priors)  
  * GS-Octree (Octree-based implicit surface \+ GS)  
  * GS-Pose (Segmentation-based pose estimation using 3DGS)  
  * GS-ROR (Reflective object relighting, SDF priors, SDF-aware pruning)  
  * GS^3: Triple Gaussian Splatting (Spatial/angular Gaussians, Triple splatting process)  
  * GSEdit (Text-guided editing, Diffusion guidance, SDS loss)  
  * GSDF (Dual-branch GS \+ SDF, Mutual guidance)  
  * GSSLAM  
  * GSGEN  
  * GVGEN (Structured Volumetric Representation \- GaussianVolume, Candidate Pool Strategy, Coarse-to-fine pipeline)  
  * HAC: Hash-grid Assisted Context (Binary hash grid, Context modeling, Adaptive quantization)  
  * Hard Gaussian Splatting (HGS \- Positional gradient driven, Rendering error guided)  
  * HDGS (Textured 2DGS, Per-ray depth sorting, Fisher-based pruning, Frustum sampling)  
  * HeadStudio (FLAME-based 3DGS, FLAME-based SDS)  
  * HFGS (Spatial/Temporal High-Frequency Emphasis Reconstruction \- SHF/THF, Deformation fields)  
  * HGS-Mapping (Hybrid Gaussian Representation \- Sphere/3D/2D Plane, Adaptive Update, Hybrid RGBD Rasterizer)  
  * Hierarchical 3D Gaussian Representation (LOD method)  
  * Hierarchical-GS  
  * High-Fidelity SLAM (Rendering-guided densification, Regularized optimization)  
  * Image-GS (Content-adaptive 2D Gaussians for images)  
  * InstantSplat (DUSt3R integration, Coarse Geometric Initialization \- CGI, Fast 3D-Gaussian Optimization \- F-3DGO)  
  * LE3D (Cone Scatter Initialization, Color MLP, Depth/near-far regularizations)  
  * LetsGo (LiDAR-assisted GS, Depth regularizer, Multi-resolution LOD)  
  * LightGaussian  
  * LIV-GaussMap (LiDAR-Inertial-Visual fusion, Differentiable ellipsoidal surface Gaussians)  
  * LP-3DGS: Learning to Prune 3DGS (Gumbel-Sigmoid mask)  
  * LumiGauss (2DGS for reconstruction/lighting, Spherical harmonics for shadows, PRT integration)  
  * MaGS: Mesh-adsorbed GS (Relative Deformation Field \- RDF)  
  * ManiGaussian (Gaussian world model, Future scene reconstruction)  
  * Mesh-based GS representation (general concept)  
  * MeshAnything (VQ-VAE mesh vocabulary, Shape-conditioned transformer)  
  * MeshGS: Adaptive Mesh-Aligned GS (Distance-based GS, Geometric regularization)  
  * MetaSapiens (Efficiency-aware pruning, Accelerated Foveated Rendering)  
  * Mini-Splatting (Blur Split, Depth Reinitialization, Intersection Preserving, Gaussian Sampling)  
  * Mip-Splatting  
  * Mirror-3DGS (Mirror attributes, Plane mirror imaging principle)  
  * MM-Gaussian (Multi-modal fusion, Relocalization module)  
  * MM3DGS SLAM (Multi-modal 3DGS, Keyframe-based mapping/tracking, Loss fusion)  
  * Mode-GS (Anchored Gaussian splats, Pixel-aligned anchors, Residual decoders, Scale-consistent depth loss)  
  * MS3DGS (Multi-scale 3DGS)  
  * MVG-Splatting (Multi-View Guided GS, Adaptive quantile-based densification)  
  * MVGamba (Multi-view Gaussian reconstructor, State Space Model \- SSM)  
  * MVSGaussian (MVS-derived Gaussians, Hybrid rendering, Multi-view aggregation)  
  * MVSplat (Cost Volume via Plane Sweeping, Multi-view Transformer)  
  * N-dimensional Gaussians (N-DG)  
  * Octree-GS (LOD-structured 3D Gaussians)  
  * Optimal Gaussian Splatting (projection method)  
  * Pixel-GS (Pixel-aware gradient, Scaled gradient field)  
  * PLA4D (Pixel-Level Alignment, Focal alignment, Gaussian-Mesh contrastive learning, Motion alignment, T-MV refinement)  
  * Proc-GS (Procedural code integration with 3D-GS)  
  * PSAvatar (Point-based Morphable Shape Model \- PMSM)  
  * PUP 3D-GS (Principled Uncertainty Pruning, Sensitivity pruning score, Multi-round prune-refine)  
  * PyGS (Pyramidal 3DGS, NeRF Initialization, Mini-batched K-means)  
  * R2-Gaussian (Rectified Radiative GS, Tailored kernels, X-ray rasterization, Differentiable voxelizer)  
  * RadSplat (Radiance Field prior/supervision, Pruning technique, Test-time filtering)  
  * RAIN-GS (Optimization from random points, Frequency domain analysis)  
  * RayGauss (Volumetric Gaussian ray casting, BVH structure)  
  * Regularized dipole sum (Point-based representation)  
  * RetinaGS (Model parallel training for 3DGS)  
  * Revising Densification (Pixel-error driven density control, Primitive count control, Opacity bias correction)  
  * Rig3DGS (Learnable deformations, 3DMM prior)  
  * RoGS (2DGS for roads, Trajectory-based initialization)  
  * SA-GS: Scale-Adaptive GS (2D scale-adaptive filters, Super-sampling, Integration)  
  * SAGD: Boundary-Enhanced Segment Anything in 3D Gaussian (Gaussian Decomposition)  
  * SAGS: Structure-Aware 3GS (Local-global graph representation, Mid-point interpolation)  
  * SA4D: Segment Any 4D Gaussians (Temporal identity feature field, 4D refinement)  
  * Scaffold-GS  
  * SemGauss-SLAM (Semantic feature embedding, Feature-level loss, Semantic-informed BA)  
  * Semantic Gaussians (Distilling 2D semantics, 3D semantic network)  
  * SGIA: Surfel-based Gaussian Inverse Avatar (PBR modeling, Pre-integration, Occlusion approximation, Progressive training)  
  * SGS-SLAM (Multi-channel optimization, Semantic feature loss, Semantic-guided keyframe selection)  
  * Sort-free Gaussian Splatting (Weighted Sum Rendering)  
  * Spec-Gaussian (Anisotropic Spherical Gaussian \- ASG appearance, Coarse-to-fine training)  
  * Speedy-Splat (SnugBox, AccuTile, Soft Pruning, Hard Pruning)  
  * Splat-Nav (Splat-Plan, Splat-Loc)  
  * SplatFace (3DMM guidance, Joint optimization, Splat-to-surface distance, World-space densification)  
  * SplattingAvatar (Mesh-embedded GS, Lifted Optimization)  
  * Spring-Gaus (Spring-Mass model integration with 3D Gaussians)  
  * STAG4D (Multi-view diffusion init, Fusion strategy, SDS optimization, Adaptive densification)  
  * StopThePop (Hierarchical Rasterization for GS)  
  * Street Gaussians (Point clouds with semantic logits/3D Gaussians, 4D SH appearance)  
  * StyleGaussian (Feature rendering strategy, KNN-based 3D CNN decoder)  
  * StylizedGS (GS filter, Nearest neighbor style loss, Depth preservation loss)  
  * SWAGS (Appearance-conditioned Gaussians, Transient Gaussians)  
  * Tactile-Informed 3DGS (Fusing touch data)  
  * TalkingGaussian (Deformation-based GS for faces, Face/mouth branches)  
  * Textured-GS (Spatially defined color/opacity via SH, UV mapping MLP)  
  * TGS: Triplane-Meets-Gaussian  
  * TIP-Editor (Stepwise 2D Personalization, Localization loss, GS representation)  
  * TOGS (Temporal Opacity Offset)  
  * TrAME (Trajectory-Anchored Scheme \- TAS, View-Consistent Attention Control \- VCAC)  
  * Trim 3D Gaussian Splatting (TrimGS \- Contribution-based trimming, Scale control, Normal regularization)  
  * TRIPS: Trilinear Point Splatting (Image pyramid rasterization, Neural reconstruction network)  
  * Unified Gaussian Primitives (Non-exponential transport rendering)  
  * UniGaussian (Unified representation from multiple camera models, Affine transformation rendering)  
  * VastGaussian (Progressive partitioning, Decoupled appearance modeling)  
  * VcEdit (Cross-attention Consistency Module \- CCM, Editing Consistency Module \- ECM)  
  * VCR-GauS (View Consistent Depth-Normal Regularizer, Confidence term, Densification/splitting strategy)  
  * Vidu4D (Dynamic Gaussian Surfels \- DGS, Warped-state geometric regularization)  
  * Wild-GS (Modeling material/lighting/camera variance, Triplane feature alignment, Visibility maps)  
  * X-Gaussian (Radiative Gaussian point cloud, Differentiable Radiative Rasterization \- DRR, ACUI initialization)  
  * Z-Splat (z-axis GS for sonar)  
*   
* Neural Radiance Fields (NeRF) & Implicit Representations:  
  * EG3D  
  * GIRAFFE  
  * GSDF (Dual-branch GS \+ SDF)  
  * GS-ROR (SDF priors)  
  * GS-Octree (Octree-based implicit surface \+ GS)  
  * Implicit neural representations (general concept)  
  * Instant-NGP / INGP  
  * LaRa (Gaussian Volumes, Group Attention Layers)  
  * MeshUDF  
  * Mip-NeRF 360 / M-NeRF360  
  * NeRF (Neural Radiance Fields \- general concept)  
  * NeRF-based methods/SLAM/segmentation (general references)  
  * NeRF-XL (Distributed NeRF training)  
  * NeRF-W  
  * Neural SDF / Learning Unsigned Distance Functions  
  * NeuraLight Field Refitting (ImplicitDeepfake1 \- uses NeRF/GS)  
  * Neuralangelo  
  * NeuS / Neusfacto  
  * Plenoxel / Plenoxels  
  * SDF (Signed Distance Field \- general concept)  
  * ToRF  
  * VolSDF  
  * Zip-NeRF  
*   
* Generative Models & Text-to-3D/4D:  
  * Attention Injection Strategy (for temporal consistency)  
  * BoostDream (Feed-forward \+ SDS refinement)  
  * BrightDreamer (Text-guided Shape Deformation \- TSD, Text-guided Triplane Generator \- TTG)  
  * ControlNet / Multi-view ControlNet (MVControl)  
  * Diffusion Models (general concept, used as prior/guidance)  
  * Diffusion Transformer (TransGS)  
  * DreamBooth  
  * DreamGaussian  
  * DreamGaussian4D  
  * DreamScene (Formation Pattern Sampling \- FPS)  
  * DreamScene360 (Panoramic generation, GPT-4V refinement)  
  * EG4D (Explicit generation without SDS)  
  * FDGaussian / GeoGS3D (Orthogonal plane decomposition, Epipolar attention)  
  * GANeRF (NeRF \+ GAN)  
  * GALA3D (Layout-guided generation, Compositional optimization)  
  * GaussianDreamer  
  * GaussianDreamerPro  
  * Generative AIs (general concept)  
  * GSGEN  
  * GVGEN (Structured Volumetric Representation, Candidate Pool Strategy)  
  * Hyper-3DG (Hypergraph Refiner \- HGRefiner, Patch-3DGS Hypergraph Learning)  
  * Image-conditional diffusion models  
  * IM-3D (Iterative Multiview Diffusion and Reconstruction)  
  * Latent Diffusion Models (LDMs)  
  * LGM: Large Multi-View Gaussian Model (Multi-view Gaussian features, Asymmetric U-Net)  
  * LoRA (Low-Rank Adaptation)  
  * Lotus (Diffusion-based visual foundation model)  
  * MVDream  
  * MVGamba (Multi-view Gaussian reconstructor, State Space Model \- SSM)  
  * Progressive Three-Stage Camera Sampling Strategy (DreamScene)  
  * RealmDreamer (3D inpainting, Depth diffusion)  
  * Score Distillation Sampling (SDS) / Delta Distillation Sampling (DDS)  
  * Shap-E  
  * Stable Diffusion / Stable Diffusion Inpaint  
  * STAG4D (Multi-view diffusion init, Fusion strategy, Adaptive densification)  
  * SyncTweedies (Synchronized diffusions)  
  * Text-guided Triplane Generator (TTG)  
*   
* SLAM & Reconstruction:  
  * 3D reconstruction (general task)  
  * ADFP  
  * CaRtGS: Computational Alignment for Real-Time GS SLAM  
  * CG-SLAM (Uncertainty-aware 3D Gaussian field)  
  * Co-SLAM  
  * COLMAP (Structure-from-Motion \- SfM)  
  * Context Capture (Oblique photography algorithms)  
  * Dense Stereo Models (e.g., DUSt3R)  
  * EndoGSLAM  
  * EN-SLAM  
  * ESLAM  
  * FMapping  
  * Gaussian-SLAM  
  * GlORIE-SLAM  
  * GO-SLAM  
  * G-ICP (Generalized Iterative Closest Point)  
  * GS-SLAM  
  * HBA (Offline map optimization tool)  
  * Hierarchical SLAM (e.g., NICE-SLAM)  
  * High-Fidelity SLAM (using GS)  
  * Hi-Map  
  * ICP (Iterative Closest Point)  
  * iMAP  
  * iMODE  
  * Keyframe selection methods  
  * LIV-GaussMap (LiDAR-Inertial-Visual fusion)  
  * LONER  
  * MM-Gaussian (Multi-modal fusion SLAM)  
  * MM3DGS SLAM (Multi-modal GS SLAM)  
  * MoD-SLAM  
  * Multi-View Stereo (MVS / MVSformer)  
  * NeRF-LOAM  
  * NeRF-VO  
  * NICE-SLAM  
  * ORB-SLAM2 (used as inspiration/backend)  
  * Orbeez-SLAM  
  * PIN-SLAM  
  * Point-SLAM  
  * Pose estimation / Refinement  
  * Q-SLAM  
  * R3LIVE (used for ground truth)  
  * Relocalization module  
  * RGBD Gs-icp Slam  
  * RNNSLAM (Recurrent Neural Network-based SLAM)  
  * SemGauss-SLAM  
  * SGS-SLAM  
  * SLAM (Simultaneous Localization and Mapping \- general concept)  
  * SplaTAM  
  * Structure-from-Motion (SfM \- general concept)  
  * ToF-SLAM  
  * TSDF (Truncated Signed Distance Function) Fusion  
  * TT-HO-SLAM  
  * VIO (Visual-inertial odometry)  
  * Vox-Fusion  
*   
* Optimization, Regularization & Compression:  
  * Adaptive quantization module  
  * ADMM (Alternating Direction Method of Multipliers)  
  * Adam / AdamW Optimizer  
  * Barnes-Hut fast summation  
  * Binary entropy minimization  
  * Codebook-based quantization / Vector Quantization (VQ) / ECVQ / R-VQ  
  * Compaction techniques (general concept for 3DGS)  
  * Compression techniques (general concept for 3DGS)  
  * Confidence term (for normal consistency)  
  * Consistency loss  
  * Constrained optimization  
  * Contrastive Learning  
  * Depth distortion regularization / loss  
  * Depth regularization (general)  
  * Depth-Normal regularizer  
  * Dynamic pruning  
  * Eikonal loss  
  * Entropy coding  
  * Entropy loss  
  * Explicit geometry constraints  
  * Feature-level loss  
  * Flow-based loss function  
  * Frequency-modulated loss  
  * Geometric regularization  
  * Gradient-informed iterative pruning ("Trimming the fat")  
  * Half-float representation  
  * Importance Pruning / Score-based densification/pruning  
  * Joint Optimization  
  * L1 Loss / Regularizer  
  * Levenberg-Marquardt (LM) optimizer  
  * Localization loss  
  * Loss-adaptive density control  
  * LPIPS Loss  
  * Mask Loss  
  * MSE Loss  
  * MS-SSIM Loss  
  * Multi-view consistency modules (CCM, ECM)  
  * Near-far regularization  
  * Normal consistency regularization / loss  
  * Opacity loss (Binary Cross Entropy)  
  * Optimizer-controlled refinement  
  * Photometric Loss / Supervision  
  * Physically-based prior (for deformation)  
  * Pixel Alignment Loss  
  * Planar constraint / loss  
  * Pruning (general concept)  
  * Radial mask constraint loss  
  * Rate-Distortion Optimization (RDO) / RDO-Gaussian  
  * Regularization (general concept)  
  * Reprojection loss (for bundle adjustment)  
  * Resolution-aware primitive pruning  
  * Rigid Regularization  
  * Scale regularization loss  
  * Semantic feature loss  
  * Smooth loss  
  * Sparse all-to-all communication (for distributed training)  
  * Sparsity encouragement  
  * Spatial Regularization  
  * SSIM Loss / D-SSIM Loss  
  * Straight-Through Estimator (STE)  
  * Total variation loss  
  * Transmittance optimization  
  * TV loss (Total Variation loss for smoothness)  
  * Variance weighted depth supervised loss  
*   
* Machine Learning Architectures & Techniques:  
  * 2D U-Net  
  * 3D U-Net  
  * Asymmetric U-Net  
  * Attention / Cross-Attention / Self-Attention  
  * BiGRU (Bidirectional Gated Recurrent Unit)  
  * CLIP Image Encoder  
  * CNNs (Convolutional Neural Networks \- general)  
  * ConvKAN network  
  * Decoder-only transformer  
  * Deep Learning (general concept)  
  * DINO / DINOv2 (Feature extraction)  
  * EfficientHourglass Architecture  
  * Federated Learning  
  * Gated convolutions  
  * GPT-4 / GPT-4V / LLMs (Large Language Models)  
  * Group Attention Layers  
  * Hash Grid / Multi-resolution Hash Encodings (MHE)  
  * Image encoder  
  * Implicit convolutional decoder  
  * Knowledge Distillation (KD) / Teacher-Student Collaborative KD (TSKD)  
  * LightGlue (Feature matching)  
  * Mamba / State Space Model (SSM)  
  * MLP (Multi-Layer Perceptron \- general)  
  * Neural network (general concept)  
  * OneFormer (Segmentation)  
  * Positional encoding  
  * ResNet-like CNN  
  * RNN (Recurrent Neural Network \- general concept)  
  * Semantic feature embedding  
  * StyleGAN  
  * SuperPoint (Feature extraction)  
  * SuperGlue (Feature matching)  
  * Temporal attention mechanism (TSAM)  
  * Transformer (general architecture)  
  * Triplane representation  
  * VQ-VAE (Vector Quantized Variational Autoencoder)  
*   
* Rendering & Visualization Techniques:  
  * Accumulated summation rendering  
  * Alpha Blending / Alpha Compositing  
  * Anti-aliasing techniques  
  * Appearance modeling  
  * BVH (Bounding Volume Hierarchy)  
  * Deferred Neural Rendering  
  * Deferred Shading  
  * Differentiable Rasterization / Renderer  
  * Differentiable rendering (general concept)  
  * G-buffer rendering  
  * Global illumination  
  * Image-based lighting (IBL)  
  * LOD (Level of Detail) strategies / representation  
  * Marching Cubes / Marching Tetrahedra  
  * Mipmapping (related to Mip-Splatting)  
  * Monte Carlo path tracing  
  * Multi-view rendering  
  * Novel view synthesis (general task)  
  * Occlusion approximation/handling  
  * Path Tracing  
  * PBR (Physically-based Rendering)  
  * Precomputed Radiance Transfer (PRT)  
  * Ray casting / Ray tracing  
  * Real-time rendering (general goal)  
  * Rendering (general concept)  
  * Shading methods (e.g., Lambertian, Cook-Torrance BRDF)  
  * Spherical Harmonics (SH)  
  * Splatting (general concept)  
  * Tile-based rasterizer / sorting  
  * Tone mapping  
  * UV mapping  
  * View synthesis (general task)  
  * Visibility map / filtering  
  * Volumetric cutting method  
  * Volumetric rendering  
*   
* Traditional CV/Graphics Algorithms:  
  * Bundle adjustment / Global bundle adjustment  
  * COLMAP (SfM pipeline)  
  * Depth completion algorithm  
  * Epipolar attention / geometry  
  * FPFH (Fast Point Feature Histograms) descriptors  
  * LBP (Local Binary Patterns)  
  * Mask2Former (Segmentation)  
  * Mesh decimation / simplification  
  * Optical flow  
  * Perspective-n-Point (PnP)  
  * Plane sweeping stereo  
  * Point cloud registration / processing  
  * Poisson Surface Reconstruction / Screened Poisson Reconstruction (SPSR)  
  * Polytope corridors / Bézier curves (for planning)  
  * RANSAC (Random Sample Consensus)  
  * Segment Anything Model (SAM)  
  * Shadow mapping  
  * Stereo Matching (e.g., DLNR, RAFT)  
  * Umeyama's method (Point-cloud registration)  
  * Voxel-fusion  
*   
* Domain-Specific Algorithms (Science/Engineering):  
  * 3D Spring-Mass model  
  * Brock–Bird model  
  * Chapman–Enskog–Brokaw model  
  * CIMA (Computer-based Infant Movement Assessment) model  
  * Clausius–Clapeyron equation  
  * Depth Anything / Depth Anything V2 (Monocular Depth Estimation)  
  * Edge partitioning (for topological indices)  
  * FLAME (3D Morphable Model) / SMPL-X  
  * Gunn–Yamada model  
  * Hyperspectral imaging  
  * Joback group contribution method  
  * Letsou–Stiel model  
  * Marigold Depth / Marigold Normal  
  * Marschner Hair Model / UE4 Approximated Scattering  
  * MMFF94 force field  
  * Particle filter (PF)  
  * Particle-based physics simulation  
  * Physics engine integration  
  * Position-based dynamics (PBD) / XPBD  
  * QSPR (Quantitative Structure-Property Relationship) modeling  
  * Regression models (Linear, Logarithmic, Quadratic)  
  * Riedel model  
  * Sato–Riedel model  
  * SDLM (Solar Deep Learning Model)  
  * Sensor fusion (Camera, LiDAR, IMU, Sonar)  
  * Stiel–Thodos model  
  * Superstructure-based modeling (Process Engineering)  
  * Surface molecular imprinting / MIPs (Sensor tech)  
  * Temperature-based topological indices / Graphical temperature indices  
  * Topomer CoMFA (QSAR)  
  * Topological Indices (general concept in chemistry)  
*   
* Frameworks & Libraries:  
  * anipose Library  
  * Blendify  
  * CUDA  
  * GauStudio  
  * gsplat library  
  * Kaolin library  
  * Mitsuba (Renderer for simulation)  
  * Mixamo (Auto-rigging)  
  * NerfBaselines  
  * NerfStudio  
  * Pillow/PIL  
  * Potamoi (Unified streaming architecture)  
  * PyTorch  
  * scikit-image  
  * SIBR viewer  
  * SPSS (Statistical software)  
* 

