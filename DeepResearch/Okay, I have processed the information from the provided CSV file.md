Okay, I have processed the information from the provided CSV file.

It's important to note upfront that **none** of the papers listed in the CSV directly address the specific intersection of **using atomic spectroscopy data *to generate images* via AI/ML**.

The papers generally fall into these categories:

1. **Using AI/ML to analyze *existing* microscopy images** (TEM, STEM, AFM, SPM) to identify atoms, defects, structures, or properties.  
2. **Using AI/ML to analyze *existing* spectroscopy data** (EELS, STS, Raman, LIBS, VSFG) to extract information, denoise signals, or classify features.  
3. **Using AI/ML for medical image analysis and generation** (PET, SPECT, CT, MRI), often for reconstruction, denoising, segmentation, or synthetic image creation.  
4. **Developing AI/ML frameworks, tools, or benchmarks** for materials science or microscopy in general (e.g., AtomAI, AtomVision, JARVIS-Leaderboard).  
5. **Describing specific experimental techniques** (like AFM-IR, PAI, cryo-ET, TERS) or simulation tools (like LAMMPS, Prismatic).  
6. **Review papers** covering AI applications in specific domains (nuclear medicine, materials science, microscopy, etc.).

Therefore, while many papers use spectroscopy and many use image generation/analysis with AI, none seem to combine *atomic spectroscopy* data as the *input* for AI-driven *image generation*.

Here is the categorized and sorted list of terms found across all the papers in the CSV:

**1\. Algorithms & Models** \*   1D-CNN (One-Dimensional Convolutional Neural Network) \*   2.5D dilated CNNs \*   2D Gaussian fitting \*   Adafactor (Optimizer) \*   Adam optimizer \*   AdamW (Optimizer) \*   Affinity-VAE (Variational Autoencoder variant) \*   Affine linear transformation \*   ALIGNN (Atomistic Line Graph Neural Network) \*   ANN (Artificial Neural Network) \*   Attention Gates (AG) \*   Autoencoder (AEC) \*   AUTOMAP \*   BCEWithLogitsLoss (Loss function) \*   BCE (Binary Crossentropy) loss \*   BERT-style objective \*   β-VAE (Variational Autoencoder variant) \*   Blind deblurring with L0-regularized intensity and gradient prior (L0RIGP) \*   Canonical Correlation Analysis (CCA) \*   Cascaded Linear Systems Analysis (LCSA) \*   Categorical cross entropy loss function \*   Center-of-mass (reconstruction approach) \*   Clustering algorithms (general) \*   CNN (Convolutional Neural Network) \*   Compressive Sensing (CS) \*   Conditional GAN (cGAN) \*   Convolution approximation (for STEM simulation) \*   CycleGAN (Cycle Generative Adversarial Network) \*   DAG (Directed Acyclic Graph) \*   DCCN (Deep Convolutional Neural Network) \*   DCGAN (Deep Convolutional GAN) \*   Denoising algorithms (general) \*   DenseNet (Dense Convolutional Network) \*   Depth-first search algorithm \*   DFT (Density Functional Theory) \- *Also a theoretical framework/methodology* \*   DFT-D3 (DFT with Dispersion Correction) \*   Differential Expected Hypervolume Improvement (qEHVI) \*   DIP (Deep Image Prior) \*   DKL (Deep Kernel Learning) \*   DL (Deep Learning) \*   DLR (Deep Learning-based Reconstruction) \*   DNN (Deep Neural Network) \*   DRUNet (Double ResNet-U-Net) \*   Dynamic thresholding (Diffusion model technique) \*   Edge detection algorithms \*   ELIT (Ensemble Learning Iterative Training) \*   Empirical wavelets \*   Ensemble Learning (EL) \*   Evoformer (Neural network block) \*   Exact Diagonalization \*   Factor analysis (FA) \*   Faster R-CNN (Faster Regional Convolutional Neural Network) \*   FastGAN \*   FastPET (Direct reconstruction CNN) \*   FBP (Filtered Back Projection) \- *Used as prior info* \*   FCN (Fully Convolutional Network) \*   FISTA (Fast Iterative Shrinkage-Thresholding Algorithm) \*   Fourier Transform (FT / FFT) \*   Frame-Aligned Point Error (FAPE) (Loss function) \*   GAN (Generative Adversarial Network) \*   GANCS \*   Gaussian curve fitting \*   Gaussian Mixture Model (GMM) \*   Gaussian process method / Gaussian Process Regression (GP / GPR) \*   Generalized maximum-likelihood method (with gradient descent) \*   GGA (Generalized Gradient Approximation) \- *Part of DFT* \*   Gradient Descent \*   Graph Neural Networks (GNN) \*   Hadamard Patterns (Spatial modulation) \*   He initialization \*   Hed (Holistically Nested Edge Detection) \*   Hilbert-Huang Transform (HHT) \*   iRadonMAP \*   Iterative reconstruction algorithms (general, e.g., for CT/SPECT/PET) \*   Iterative shrinkage-thresholding algorithm (ISTA) \*   Iterative optimization (general) \*   jVAE / jrVAE (Joint Rotationally Invariant VAE) \*   k-means clustering \*   L1 loss function \*   L2 loss function \*   Laplacian of Gaussian (LOG) blob detection \*   Linear regression \*   LiNGAM (Linear Non-Gaussian Acyclic Model) \*   Local Multiphase Chan-Vese model (Image segmentation) \*   Logistic regression \*   Long Short-Time Memory (LSTM) \*   Low pass filter \*   LSDA+U (Local Spin Density Approximation \+ U) \- *Part of DFT* \*   MAP-Elites (Multi-dimensional Archive of Phenotypic Elites) \*   Markov Chain Monte Carlo (MCMC) \*   Mask RCNN \*   Maximum likelihood interaction time estimation \*   Maximum-likelihood method (for material decomposition) \*   mDCSRN-GAN \*   Mean Absolute Error (MAE) loss \*   Mean imputation \*   Mean Squared Error (MSE) loss \*   Merriman-Bence-Osher (MBO) scheme / classifier \*   Meta-SRGAN \*   ML (Machine Learning) \*   MLR (Multiple Linear Regression) \*   Monte Carlo method / simulation \*   MRR-CNN (Multi-Resolution Registration CNN) \*   Multislice (Electron microscopy simulation method) \*   Naive Bayes classification \*   Nelder-Mead simplex method (Optimization) \*   Neural Networks (NN) \*   NMF (Non-Negative Matrix Factorization) \*   NMF-QMV (Nonnegative Matrix Factorization from Quadradic Minimum Volume) \*   Non-rigid registration \*   Non-Linear Sigma Model (NLSM) \*   NPRM (Non-Parametric Residue Mapping) \*   Noisy Student Self-Distillation \*   Normalized cross-correlation \*   OSEM (Ordered Subsets Expectation Maximization) \*   Otsu's method (Thresholding) \*   Parallel FFTs \*   Parallel spatial decomposition \*   Partial least squares regression (PLSR) \*   Particle Filter \*   Patch-level discriminators (GAN component) \*   PAW (Projector Augmented Plane-Wave method) \- *Part of DFT* \*   PAW-PBE (Potential used in PAW) \*   PCA (Principal Component Analysis) \*   PBE (Perdew-Burke-Ernzerhof) \- *Functional in DFT* \*   PDE constrained optimization \*   Phase cross-correlation \*   Phase-field model \*   Pix2Pix (Conditional GAN) \*   Powell's method (Optimization) \*   PredRNN (Recurrent Neural Network for prediction) \*   PRISM method (STEM/HRTEM simulation) \*   Prototypical Network (Few-shot learning) \*   Ptychography / Ptychographic phase retrieval algorithms \*   Q-AE (Quadratic Autoencoder) \*   QSAR (Quantitative Structure Activity Relationships) \*   Quantum CNN \*   Random Forest (RF) \*   Random goal exploration algorithms \*   Randomized Singular Value Decomposition (rSVD) \*   RANSAC (Random Sample Consensus) \- *Used with SIFT* \*   Recon-GLGAN \*   RefineGAN \*   Regression algorithms (general) \*   Reinforcement Learning (RL) / Deep RL \*   ReLU activation function \*   Res (Deep Residual Learning Framework) \*   ResHedNet (Residual Holistically Nested Edge Detection Network) \*   ResNet / ResUNet (Residual Network / Residual U-Net) \*   Richardson-Lucy (RL) method (Deblurring) \*   Ridge Polynomial Neural Network (RPN) \*   RNN (Recurrent Neural Network) \*   rVAE (Rotationally-Invariant Variational Autoencoder) \*   Scharr edge detection filter \*   Segmentation algorithms (general) \*   Semi-supervised VAEs \*   sh-VAE (Shift-invariant VAE) \*   SIFT (Scale-Invariant Feature Transform) \- *Used with RANSAC* \*   Signal Detection Theory (SDT) \- *Also a framework* \*   Singular Value Decomposition (SVD) \*   SliceGAN \*   SMATB Potential (Molecular Dynamics) \*   SMLM (Single Molecule Localization Microscopy) \- *Super-resolution technique* \*   SMOTE (Synthetic Minority Over-sampling Technique) \*   Snake activation function \*   SOAP (Smooth Overlap of Atomic Positions) \*   Spach transformer \*   Spatial Modulation (Single-pixel imaging) \*   Spectral Analysis \*   SRGAN (Super-Resolution GAN) \*   SSIM loss \*   Stable Diffusion (SD) (Image generation model) \*   STED (Stimulated Emission Depletion Microscopy) \- *Super-resolution technique* \*   Stochastic Weight Averaging (SWA) \*   Størmer-Verlet symplectic integrator \*   SVR (Support Vector Regression) \*   SVM (Support Vector Machine) \*   T5-XXL encoder (Language model) \*   Tersoff-Hamann (TH) method (STM simulation) \*   Thresholding algorithms \*   Total Variation Regularization \*   Transformer decoder blocks \*   TrueFidelity (DLR algorithm) \*   t-SNE (t-distributed Stochastic Neighbor Embedding) \*   U-Net / UNet (CNN architecture) \*   VAE (Variational Autoencoder) \*   Variational Quantum Deflation (VQD) \*   Variational Quantum Eigen Solver (VQE) \*   VoxelMorph (Deep learning registration method) \*   Wasserstein GAN \*   Wavelet Transform (WT) \*   Wiener filter (WF) (Deblurring) \*   YOLO / YOLOv4 (You Only Look Once \- Object detection)

**2\. Experimental Techniques & Instruments** \*   4D-STEM (Four-Dimensional Scanning Transmission Electron Microscopy) \*   Aberration-corrected STEM/TEM \*   Adhesion (snap-in) force imaging (AFM) \*   AFM (Atomic Force Microscopy) \- including contact mode, tapping mode, peak force tapping \*   AFM-IR (Atomic Force Microscopy-Infrared Spectroscopy) \*   Ambient condition measurements (AFM) \*   Annealing (Sample treatment) \*   Annular Bright-Field (ABF) imaging (STEM) \*   Annular Dark Field (ADF) imaging (STEM) \*   AP-CVD (Atmospheric Pressure Chemical Vapor Deposition) \*   APT (Atomic Probe Tomography) \*   Arc discharge (Nanoparticle synthesis) \*   Arterial blood sampling (PET) \*   Atom counting (STEM methodology) \*   Atomic manipulation (SPM/STEM) \*   Atomic-resolution imaging (General term) \*   Ball milling (Sample preparation) \*   Band excitation piezoresponse force microscopy (BEPFM) / spectroscopy (BEPS) \*   Bragg diffraction analysis \*   C-AFM (Conductive Atomic Force Microscopy) \*   Cathodoluminescence (CL) spectroscopy \*   CCD (Charge-Coupled Device) camera \*   Cherenkov radiation detection \*   Chemical vapor deposition (CVD) \*   CMOS (Complementary Metal-Oxide-Semiconductor) detector \*   Coherent x-ray imaging / scattering \*   Collagen imaging (AFM) \*   Collimators (SPECT \- parallel hole, fan beam) \*   Combustion (Nanoparticle synthesis) \*   Confocal laser scanning microscopy (CLSM) \*   Constant current mode (STM) \*   Constant height mode (AFM) \*   Contrast agent administration (CT/MRI) \*   Cryo-electron tomography (cryo-ET) \*   Cryo-EM / Cryogenic Electron Microscopy (General term) \*   Cryo-STEM / Cryogenic Scanning Transmission Electron Microscopy \*   Cryo-TEM / Cryogenic Transmission Electron Microscopy \*   CT (Computed Tomography) \*   Current-time (I-t) spectroscopy (STM) \*   Cylindrical shell random masks (Neutron imaging) \*   Dark-field microscopy (DFM) \*   DC voltage ramping (PFM) \*   Dectris ELA direct electron detector \*   DECT (Dual-Energy Computed Tomography) \*   Defocused probe imaging (STEM) \*   Diamond-coated conductive tips (AFM) \*   Differential conductance (dI/dV) measurements (STS) \*   Diffuse optical tomography \*   Diffuse scattering analysis \*   Dispersive elements (e.g., prism, grating for spectroscopy) \*   DOI (Depth of Interaction) measurement (PET/SPECT) \*   Drop casting (Sample preparation) \*   Dry transfer method (for 2D materials) \*   Dual-layer spectral detector CT \*   EBSD (Electron Backscatter Diffraction) \*   EEGS (Electron Energy Gain Spectroscopy) \*   EELS (Electron Energy Loss Spectroscopy) \- including low-loss, core-loss, momentum-resolved (q-EELS) \*   Electrochemical oxidation (Nanoparticle synthesis) \*   Electron crystallography \*   Electron diffraction \*   Electron Ronchigram \*   Electron spectroscopy (general) \*   EM (Electron Microscopy \- general term) \*   EMCCD (Electron-Multiplying Charge-Coupled Device) camera \*   EMPAD (Electron Microscope Pixel Array Detector) \*   Endoscopy / Photoacoustic Endoscopy (PAE) \*   Etched tips (W, Pt/Ir for STM) \*   Ex-situ annealing \*   Femtosecond laser (for UED/transitions) \*   FIBS (Filament-Induced Breakdown Spectroscopy) \*   FIB (Focused Ion Beam) milling / lift-out \*   Fluorescence imaging (FL) / microscopy \*   Fluorescence Recovery After Photobleaching (FRAP) \*   Force-distance curve acquisition (AFM) \*   Freeze-pump-thaw cycles (Water purification) \*   FTS (Fourier Transform Spectroscopy) module \*   Full-field spectroscopy \*   Gammex Multi-Energy CT phantom \*   Gas cell holder (for in situ TEM) \*   Gemstone Spectral Imaging (GSI) (CT reconstruction) \*   HAADF (High-Angle Annular Dark-Field) imaging (STEM) \*   Hadamard pattern modulation masks (Neutron imaging) \*   High-speed AFM (HS-AFM) \*   High-throughput experimentation \*   HOPG (Highly Oriented Pyrolytic Graphite) substrate/cleavage \*   HRTEM (High-Resolution Transmission Electron Microscopy) \*   Hydrothermal/solvothermal synthesis (Nanoparticle synthesis) \*   Hyperspectral imaging (General term) \*   Imaging Fourier transform spectrometer \*   In situ / Operando (S)TEM \*   In situ charge state manipulation (AFM) \*   Infrared (IR) spectroscopy \*   Interferometric scattering microscopy (iSCAT) \*   Ion milling (Sample preparation) \*   Laser ablation (for LIBS, nanoparticle synthesis) \*   Laser excitation (for fluorescence, PAI, STML) \*   Laser induced optical barriers (LIOB) (Scintillators) \*   Laser-induced circular dichroism (Spectroscopy) \*   Laser-STM (Combined laser excitation and STM) \*   LC-EM (Liquid Cell Electron Microscopy) \*   LED (Light-Emitting Diode) light source \*   LIF (Laser-Induced Fluorescence) spectroscopy \*   LIBS (Laser-Induced Breakdown Spectroscopy) \*   Liposomes (Nanoparticle type) \*   Lock-in technique (STS) \*   Lorentz phase microscopy \*   Low-dose imaging (General term) \*   MAADF (Medium-Angle Annular Dark-Field) imaging (STEM) \*   Magnetometry \*   Manometric measurements (Gas adsorption) \*   Mass spectrometry (for water cleanliness check) \*   MBE (Molecular Beam Epitaxy) \*   Mechanical exfoliation (for 2D materials) \*   Mechanical thinning/polishing (Sample preparation) \*   Metascintillator/heteroscintillator detectors \*   Micro-photoluminescence (μPL) \*   Microfluidics \*   Microscopy (General term) \*   Microwave irradiation/synthesis (Nanoparticle synthesis) \*   Monochromated electron beam (STEM-EELS) \*   MRI (Magnetic Resonance Imaging) \*   Multi-modal electron microscopy (fused HAADF, EDX, EELS) \*   Nanobeam diffraction (STEM) \*   Nanoparticle synthesis (General term, various methods) \*   Nanopositioner (AFM component) \*   Non-contact AFM (nc-AFM) \*   Non-destructive surface ablation \*   Optical coherence tomography (OCT) \*   Optical microscopy \*   Ozone annealing (Sample treatment) \*   PAI / PACT / PAM (Photoacoustic Imaging / Computed Tomography / Microscopy) \*   Path integral molecular dynamics (PIMD) \- *Also a simulation methodology* \*   PCD (Photon-Counting Detector) \*   Perfusion imaging (SPECT) \*   PET (Positron Emission Tomography) \*   PFM (Piezoresponse Force Microscopy) \*   PFS (Piezoresponse Force Spectroscopy) \*   Photocurrent tunneling microscopy \*   Photothermal microscopy (PTM) \*   Pixelated detectors (STEM) \*   Planar fluorescence imaging (2D) \*   Plasma generation (LIBS, filaments) \*   PLD (Pulsed Laser Deposition) \*   Polycapillary optics (XRF) \*   Probe-corrected TEM/STEM \*   Protein imaging (Cryo-EM/AFM) \*   Pyrolysis (Nanoparticle synthesis) \*   qPlus sensor (AFM) \*   Quantum dots (Nanoparticle type) \*   Quasi-particle interference (QPI) imaging (STM) \*   Radioligand therapy (RLT) \*   Radiolabeled meal (GES) \*   Radiopharmaceutical administration (SPECT/PET) \*   Raman spectroscopy / Tip-enhanced Raman spectroscopy (TERS) / Surface enhanced Raman microscopy (SERM) \*   Remote hydrogen plasma treatment \*   Resistive Plate Chambers (RPCs) (Detector) \*   Scintillator detectors \*   SDD (Silicon Drift Detector) (XRF) \*   Self-flux method (Crystal growth) \*   SEM (Scanning Electron Microscopy) \*   Semiconductor detectors \*   Single-pixel imaging (SPI) (Neutron imaging) \*   Slanted edge method (Detector characterization) \*   SMLM (Single Molecule Localization Microscopy) \*   Solid state photosensors (SPECT/PET) \*   Solution strategies (Nanoparticle synthesis) \*   SPCCT (Spectral Photon-Counting Computed Tomography) \*   SPECT (Single-Photon Emission Computed Tomography) \*   Spectrally-resolved fast-gated imaging \*   Spectroscopy (General term) \*   Spin coating (Sample preparation) \*   SPM (Scanning Probe Microscopy) \- general term \*   Spray coating (Sample preparation) \*   SPRM (Surface Plasmon Resonance Microscopy) \*   Sputtering (Sample cleaning/preparation) \*   STED (Stimulated Emission Depletion Microscopy) \*   STEM (Scanning Transmission Electron Microscopy) \*   STM (Scanning Tunneling Microscopy) \*   Strain-stress measurements \*   Structured Illumination Microscopy (SIM) \*   STS (Scanning Tunneling Spectroscopy) \*   Super-resolution microscopy (General term) \*   Surface cleaning/heating (UHV preparation) \*   Synchrotron-based x-ray source \*   Template-assisted synthesis (Nanoparticle synthesis) \*   TEM (Transmission Electron Microscopy) \*   Thermal decomposition (Nanoparticle synthesis) \*   Time-of-Flight (TOF) estimation (PET) \*   Time-resolved 2D spectral imaging \*   Time-resolved TEM / Ultrafast TEM (UTEM) / Ultrafast Electron Diffraction (UED) \*   Tomographic fluorescence imaging (3D) \*   Ultrahigh vacuum (UHV) conditions \*   Ultrasonication (Sample preparation) \*   Ultrasonography (USG) \*   Ussing chamber assay (Permeability measurement) \*   Vibrational sum frequency generation (VSFG) spectroscopy \*   Viscometry \*   Voltage pulsing (STM) \*   Water dosing (UHV) \*   Web crawling (Data acquisition) \*   Wavelength-shifting fibers (Detector component) \*   XFEL (X-ray Free Electron Laser) \*   XPS (X-ray Photoelectron Spectroscopy) \*   XRD (X-ray Diffraction) \*   XRF / Micro-XRF (X-ray Fluorescence / micro-) \*   X-ray imaging (General term)

**3\. Methodologies & Workflows** \*   Ab initio molecular dynamic simulations (AIMD) \*   Active learning \*   Active Recommender System (ARS) \*   Adaptation of classical macroscopic definitions (Bayesian approach) \*   Adapter system design (MIDA) \*   Affinity-VAE framework \*   AI-aided optical imaging protocol \*   AI-driven automation (STEM, SPM) \*   AI/ML-driven autonomous experimentation / workflows \*   Atom-counting methodology (STEM) \*   Atom-S2 framework (ML for stress mapping) \*   AtomAI framework / software package \*   AtomVision library / framework \*   Automated analysis / segmentation / classification / detection (General term) \*   Automated feedback-controlled system (STEM fabrication) \*   Autonomous convergence (STM parameters) \*   Bayesian optimization (BO) / Latent Bayesian Optimization (zBO) \*   Benchmark dataset development (STEM atom segmentation) \*   Bicrystal interface construction \*   Cartoon and texture decomposition (Image analysis) \*   Causal analysis / Causal learning \*   Chemical structure visualization (Scanning Raman picoscopy) \*   Classification (Supervised ML task) \*   Closed-loop instrument control \*   Computational modeling (General term) \*   Computer-aided diagnosis (CAD) \*   Correlative analysis (structure-property, image-spectrum) \*   Cross-validation (e.g., 10-fold, 9-fold) \*   Data augmentation (flipping, rotating, noise addition, etc.) \*   Data cleaning / preprocessing (imputation, duplicate removal, filtering, normalization, registration, contrast enhancement) \*   Data fusion / Hypermodal data fusion \*   Data integration (MIDA framework) \*   Data observability strategies (MIDA) \*   Data reusability assessment (NSDRA framework) \*   Decision-theoretic approach (Resolution limit analysis) \*   Deep kernel learning (DKL) workflow \*   Deep learning pipeline (Amorphous material analysis) \*   Deep learning-based reconstruction (DLR \- for CT/PET/SPECT) \*   Deep-learning framework (General term) \*   Defect engineering \*   Defect identification / detection / classification / quantification (General goal) \*   Density functional theory (DFT) calculations \- *Also a theoretical framework* \*   Dimensionality expansion (GAN-based) \*   Dimensionality reduction (PCA, NMF, SVD, VAE, autoencoder) \*   Direct reconstruction (PET \- neural network based) \*   Disentanglement / Disentangled representations (VAE feature) \*   Distributed neighbor lists (LAMMPS parallelization) \*   Domain adaptation \*   Dosimetry calculations / methodology (Nuclear medicine) \*   Dual Autoencoder-Classifier algorithm \*   Dynamic tracking / observation (Microscopy) \*   ELIT (Ensemble learning-iterative training) workflow \*   End-to-end structure prediction (AlphaFold) \*   Ensemble learning / Deep ensembles \*   Feature importance analysis \*   Feature selection / extraction \*   Few-shot learning \*   Forward modeling (Image simulation) \*   Fused multi-modal electron microscopy \*   Generative modeling (General approach) \*   Geometric Unmixing \*   Ghost Imaging (GI) (Neutron imaging) \*   Hamiltonian simulation (Quantum computation) \*   High-throughput analysis / screening / optimization \*   Histo-image representation (PET data) \*   Human-in-the-loop autonomous experiments / workflows \*   Image registration (affine, non-rigid, optimization-based) \*   Image restoration / deblurring / denoising / enhancement (General tasks) \*   Image segmentation (semantic, instance, domain-based) \*   Image synthesis / generation (GANs, VAEs, diffusion models) \*   Image-to-image translation (GANs, CycleGAN) \*   Image-to-spectrum (Im2Spec) / Spectrum-to-image (Spec2Im) translation \*   Ingrained framework (Simulation-experiment fusion) \*   In silico modeling / simulation (General term) \*   JARVIS-Leaderboard benchmark platform \*   Knowledge-informed framework (Autonomous experimentation) \*   Latent space exploration / analysis (VAE) \*   Linear unmixing methods (PCA, NMF, ICA) \*   Machine vision algorithm / framework \*   Material decomposition (Spectral CT) \*   Materials design / discovery (General goal) \*   MIDA framework (Multi-workflow Integrated Data Analysis) \*   Molecular dynamics (MD) simulations / Path integral MD (PIMD) \*   Molecular fingerprint detection (Spectroscopy) \*   Molecular simulation (General term) \*   Multi-fidelity modeling \*   Multi-modal fusion (Imaging) \*   Multivariate statistical analysis \*   Neuro-symbolic AI techniques \*   Noise filtering / reduction (General task) \*   Novelty-based search strategies \*   NSDRA framework (NanoSafety Data Reusability Assessment) \*   Object detection / localization (YOLO, Faster R-CNN, Mask RCNN) \*   Online learning \*   Optimization (General task, various algorithms) \*   Parametric kinetic modeling (PET \- compartmental, Patlak, spectral) \*   Parsimonious representation / description discovery (VAE) \*   Partially Observable Markov Decision Process (POMDP) \*   Peak analysis (Spectroscopy \- traditional approach) \*   Photorealistic text-to-image synthesis (Imagen model) \*   Physics-based / Physics-informed / Physics-inspired ML/AI \*   Prediction / Prognosis (Medical imaging) \*   Property prediction (Materials science) \*   Provenance management (MIDA) \*   Quantitative structure determination (STEM) \*   Radiomics / Radiophenomics \*   Real-time analysis / feedback / control / detection / monitoring \*   Regression (Supervised ML task) \*   Reinforcement learning framework \*   Resolution enhancement / Super-resolution (Imaging task) \*   RODAS (Rapid Object Detection and Action System) \*   Scanning Raman picoscopy \*   Self-distillation (Deep learning training technique) \*   Semi-supervised learning \*   Sparse data analytics / Sparse image retrieval \*   Spiral scanning pattern (SPM data acquisition) \*   Statistical forecasting \*   Statistical Parameter Estimation (Atom counting) \*   Structure initialization (Database query, bicrystal construction) \*   Structure reconstruction (3D, atomic) \*   Structure-property relationship exploration \*   Superpixel semantic segmentation \*   Supervised learning \*   Supervised manifold learning \*   Teaching by Demonstration (Robotics/AI) \*   Text-to-image synthesis \*   Theragnostics (Combined diagnosis and therapy) \*   Topological reconstruction (Radiation detector) \*   Training data generation / curation (Simulation, augmentation, NLP) \*   Transfer learning \*   Uncertainty quantification (UQ \- Dropout, Ensembles, Quantile Regression, GP) \*   Unsupervised learning \*   User feedback survey (Validation) \*   Visual proteomics \*   Weak supervision

**4\. Concepts & Principles** \*   Ab initio calculations (General term) \*   Absorptive potential approximation (HAADF STEM theory) \*   Acidity (Surface chemistry \- pKa, PA) \*   Activation function (Neural networks) \*   Affinity matrix (Affinity-VAE component) \*   ALARA principle (As Low As Reasonably Achievable \- radiation dose) \*   Alternating high/low polarization dynamics (Ferroelectrics) \*   Ångström resolution \*   Anisotropy (Chemical bonds, particles) \*   Artifacts (Imaging \- general term) \*   Atomic defects (vacancies, dopants, impurities, grain boundaries, edge terminations) \*   Atomic registry \*   Atomic structure / configuration \*   Atomic-scale chemistry / visualization / manipulation / engineering \*   Attenuation correction (AC) (PET/SPECT) \*   Automated experimentation / Autonomous systems \*   Band gap (Materials property) \*   Band structure (Electronic property) \*   Bayesian methods / inference \*   Beam-induced transformations / damage / interactions \*   Big data (Microscopy context) \*   Biomarker identification \*   Biocompatibility / Toxicity (Nanoparticles) \*   Bond length / angle distribution \*   Bond-order valence sums (Acidity estimation) \*   Bulk-boundary correspondence (Topological materials) \*   Canted antiferromagnetism (CAF) (Graphene state) \*   Causality / Causal inference / Causal mechanisms / Causal models \*   Cellular viability (Toxicology endpoint) \*   Charge Density Wave (CDW) \- including chiral CDW \*   Charge ordering \*   Charge state manipulation (Defects) \*   Chemical bonding / bonds \*   Chemical composition \*   Chemical pathways / reactions / transformations \*   Chirality / Chiral molecules / nanostructures / switching \*   Coherence (Electron beam property) \*   Coherent states (Intervalley \- IVC in graphene) \*   Colloidal crystal growth (Classical vs. nonclassical pathways) \*   Complex morphologies \*   Computational cost / efficiency \*   Concentration (Nanoparticles, dopants) \*   Confinement of light (Atomistic scale) \*   Confounding variables (Causal inference) \*   Continuity (Latent space property) \*   Contrast / Z-contrast (Imaging property) \*   Convergence (Optimization, simulations) \*   Correlated electron systems / Strong correlation \*   Correlation (General statistical term) \*   Coulomb blockade effects \*   Coulomb interaction \*   Cramer-Rao lower bound (Information theory) \*   Crystal lattice / structure / defects / orientation / polymorphs / symmetry / space group \*   Crystal growth pathways \*   Curiosity-driven experimentation \*   Data standardization / sharing / management / FAIR principles \*   Debye-Waller factor (Thermal vibration simulation) \*   Decision function (Decision theory) \*   Deconvolution (Signal processing) \*   Defect formation mechanisms \*   Degeneracy (High-resolution microscopy data) \*   Degrees of freedom (Particles, spins, etc.) \*   Density of states (DOS) / Local DOS (LDOS) \*   Detection limit \*   Diagnostic accuracy / confidence / performance / efficacy \*   Dielectric characteristics \*   Diffusion models (Generative modeling principle) \*   Dipole direction (Molecular property) \*   Dirac cone model / Coupled Dirac cone model \*   Dirac mass gap \*   Disordered systems / sites \*   Disentanglement (Latent space property) \*   Dispersion (Phonon, plasmon, exciton) \*   Domain structure / walls (Ferroelectrics) \*   Dopants / Doping \*   Drug delivery (Nanoparticles) \*   Effective atomic number (Zeff) (CT property) \*   Effective ionization potential (EDX theory) \*   Eigen/Zundel cations (Hydrated protons) \*   Elastic modulus \*   Elastic scattering / Inelastic scattering (Electron microscopy) \*   Electric field / Magnetic field (Internal, applied) \*   Electron beam positioning / control / manipulation / shaping \*   Electron density \*   Electron-hole pairs / interaction \*   Electron-lattice interactions \*   Electronic order (Mott, pseudogap) \*   Electronic structure \*   Electrostatic barriers (Grain boundaries) \*   Elemental mapping / quantification \*   Emergent physics / phenomena / properties \*   Energy resolution \*   Entropy (Information theory) \*   Equivariant attention (Neural network concept) \*   Error propagation / sources of variance (statistical, systematic) \*   Evolutionary constraints / history (Protein structure) \*   Exchange interaction (Quantum Hall ferromagnetism) \*   Excitation (Electronic, plasmonic, phonon, excitonic) \*   Exciton / Moiré exciton / Excitonic luminescence / lattices \*   Explainability / Interpretability (AI/ML) \*   Exploration vs. Exploitation (Optimization, RL) \*   Ferroelectricity / Ferroelasticity \*   Fidelity (Image generation) \*   First principles modeling / calculations \*   Fisher information \*   Force field methods / Machine learning force fields (MLFF) \*   Free energy / Gibbs free energy \*   Frequency domain analysis \*   Functional groups (Molecular property) \*   Functional materials / functionality \*   Generalization ability (ML models) \*   Generative physical model (Hamiltonian, Ginzburg-Landau) \*   Geometric constraints (Protein structure) \*   Geometry (Nanoparticle property) \*   Ginzburg-Landau model \*   Grain boundaries (GBs) \*   Graph inference problem (Protein structure prediction) \*   Ground state (Quantum mechanics) \*   Ground truth (ML term) \*   Hamiltonian (Physical model) \*   Hardness (Materials property) \*   Heterointerfaces / Heterostructures (Materials) \*   Heterogeneous catalysis \*   Hidden latent variables \*   High-frequency information (Image property) \*   Homogeneous / Heterogeneous materials \*   Hydrogen bonding \*   Hydrogen isotopic analysis / shifts \*   Hydrogen storage materials \*   Hyperparameters / Hyperparameter optimization / tuning \*   Hysteresis (Piezo actuators, ferroelectrics) \*   Ill-posed inverse problem \*   Image quality (General term) \*   Image registration (Concept) \*   Inductive bias (ML term) \*   Information density / Uniform information density \*   Information theory \*   Infrared chemical imaging \*   Inhomogeneities (Material property) \*   Input function (PET kinetics) \*   Instrumentation limitations / stability \*   Interatomic potentials \*   Interface length / energy / properties \*   Interference (Atomic motion, waves, electron scattering) \*   Inter-laboratory approach (Benchmarking) \*   Intermediate states (Dynamic processes) \*   Internal dose maps / dosimetry \*   Invariances (Rotational, translational) \*   Inverse problem (General concept) \*   Ising model / Hamiltonian \*   Isotopes / Isotopic shifts / resolution \*   Iterative refinement (AlphaFold) \*   K-edge photoelectric effect (Spectral CT) \*   Kansei engineering (Product design) \*   Kekulé distortion (Graphene state) \*   Kinetic modeling (PET) \*   Kullback-Leibler (KL) divergence (VAE loss component) \*   Landau levels (Quantum Hall effect) \*   Large language models (LMs) \*   Latent space / variables / representation / embedding \*   Lattice distortion / strain / vibrations \*   Light-matter interactions \*   Likelihood (Statistical concept) \*   Linear imaging model \*   Loss function (ML training component) \*   Low-dimensional representation \*   Macroscopic observables / definitions \*   Magnetic defects / structure / properties / ordering \*   Masked MSA loss (AlphaFold training) \*   Material properties (General term) \*   Message passing (GNN concept) \*   Microstructure / Nanostructure \*   Microstructural optimization \*   Misclassification (ML error) \*   Mixed element nanostructures \*   Moiré superlattice / potential / unit cell \*   Molecular assembly / structure / dynamics / interactions / fingerprint / switch \*   Molecular configuration monitoring \*   Momentum distribution (Plasmonic fields) \*   Morphology / Morphological homogeneity \*   Mott insulator / order \*   Multi-dimensional data / imaging \*   Multi-objective optimization \*   Multi-omics approach \*   Multiple electron scattering \*   Multivariate analysis \*   MXenes (Material class) \*   Nanomedicine / Nanotechnology / Nanotheranostics \*   Nanoparticles (metallic, high-Z, quantum dots, nanorods, CNTs, etc.) \*   Nanoscale / Atomic scale / Sub-angstrom resolution \*   Natural language processing (NLP) \*   Near-atomic-scale resolution \*   Noise (shot, Poisson, scan, Gaussian, background) / Noise homoscedasticity \*   Nonfluorescent matter \*   Nonlinearity / Non-Gaussianity \*   Nuclear fallout particle surrogates \*   Nuclear materials / diagnostics \*   Nuclear quantum effects \*   Nuclearity (Number of atoms in nanoparticle) \*   Nucleation physics / pathways \*   Observational bias (Microscopy) \*   Onset of conduction (MHP property) \*   On-surface synthesis \*   Optical contrast / properties / response / saturation \*   Optical elastography (Brillouin microscopy) \*   Order parameters \*   Ordering transitions \*   Organic synthesis \*   Oscillator strength \*   Out-of-distribution drift (ML challenge) \*   Overfitting (ML challenge) \*   Oxidation characteristics / behavior / pathways / states \*   π-magnetism (Graphene) \*   Pair distribution function \*   Pairwise features / correlations (Protein structure) \*   Parallelization (Computational concept) \*   Parameter space exploration \*   Parsimony (of physical descriptors) \*   Periodicity / Periodic orderings / patterns \*   Personalized medicine / treatment / dosimetry \*   Phase (Material property, imaging concept) \*   Phase instability (Perovskites) \*   Phase retrieval \*   Phase segregation \*   Phase transitions (Photoinduced, quantum) \*   Phenotyping / Image phenotyping \*   Phonon dispersion \*   Photorealism (Image generation quality) \*   Photothermal effect / expansion \*   Physical constraints / knowledge / bias (ML integration) \*   Physical interaction framework (Protein structure) \*   Picometer precision \*   Pixelwise classification / learning \*   Plasma chemistry / conditions / dynamics / evolution \*   Plasmonics / Plasmonic fields / spectra / dispersion \*   Point spread function (PSF) \*   Polarization switching / dynamics (Ferroelectrics) \*   Polymorphs / Polymorphism \*   Posterior probability distribution (Bayesian concept) \*   Precision engineering (Atomic scale) \*   Prior knowledge / information (Bayesian, ML) \*   Probabilistic models \*   Product morphology (Product design) \*   Prosthetic groups (Protein structure) \*   Protein assembly / structure / folding / dynamics \*   Proton affinity (PA) \*   Pseudogap order \*   Quantitative analysis / metrics / imaging / measurements \*   Quantum computation / algorithms / chemistry / information science / materials / phases / topology \*   Quasiparticles \*   Radiation burden / dose / exposure / detectors / damage \*   Real space / Reciprocal space \*   Reconstruction error (VAE loss component) \*   Regularization (ML technique) \*   Reproducibility (Experimental, computational) \*   Resolution limit (Imaging) \*   Resonance-assisted tunneling \*   Rotational dynamics / invariance / orientation \*   Sample quality \*   Sampling (Adaptive, MCMC) \*   Scattering cross-sections (HAADF, EDX, EELS) \*   Self-assembly / Self-organization \*   Sensitivity (Detector property, analysis concept) \*   Serendipity (Materials discovery) \*   Signal-to-noise ratio (SNR) \*   Similarity measure (Image registration) \*   Single-bond limit / resolution \*   Single-molecule / particle level \*   Spatial resolution / localization / frequency / distribution / variation \*   Spectral broadening / features / imaging / resolution / separation / signatures / unmixing \*   Spin qubits / states / structure / texture / degrees of freedom \*   Stability (Instrumental, structural, thermal) \*   Standoff detection (LIBS) \*   Statistical significance \*   Stochastic gradient descent (Optimization) \*   Structural causal model \*   Structural motifs \*   Structure evolution / transformation \*   Sub-pixel shifts (Image registration) \*   Superconductivity / High-Tc superconductors \*   Superhard materials \*   Surface chemistry / properties / species / structure / reconstruction / defects / reactions / sites \*   Surface plasmon resonance (SPR) \*   Supramolecular self-assembly \*   Symmetry / Symmetry breaking / Space group \*   Synthetic data / images \*   Systematic error / bias \*   Tautomerization \*   Temporal resolution / dynamics / evolution / scales \*   Texture (Image analysis component) \*   Thermal diffuse scattering (TDS) (STEM theory) \*   Thermal energy / fluctuations / vibrations \*   Theranostics \*   Thermodynamic processes / stability / driving forces \*   Thin films / 2D materials (Graphene, TMDCs, hBN, MXenes, Phosphorene) \*   Tip motion effects / stability / conditioning / \-sample interaction / \-induced reactions \*   Topological defects / excitations / insulators / quantum phases / spin states / correspondence principle \*   Transient states / phenomena / changes / transformation processes \*   Translation invariance / shifts \*   Translational potential (Clinical applications) \*   Transmission probability (Tunneling model) \*   Tunneling current / spectroscopy \*   Twin boundaries (TBs) \*   Ultrafast dynamics / timescales \*   Uncertainty (Latent variables, predictions) \*   Universal approximation theorem (Neural networks) \*   Valley ordering / polarization / skyrmions / texture (Graphene) \*   Van der Waals forces / interactions / heterostructures \*   Vibrational modes / spectroscopy \*   Virtual environments / simulation (for RL training) \*   Visualization (Data, structures, processes) \*   Voigt profiles (Spectral fitting) \*   Wannier-Bloch duality \*   Wasserstein metric (GAN loss) \*   Weight decay (L2 regularization) \*   Wigner crystal / states

**5\. Evaluation Metrics** \*   Accuracy (Acc) \*   Area Under the Curve (AUC) / Area under the ROC curve \*   Asymmetric index (Image evaluation) \*   Balanced Accuracy (BA) \*   Contrast Recovery Coefficient (CRC) \*   Dice Similarity Coefficient (DSC) \*   DQE (Detective Quantum Efficiency) \*   F1-score / F2-score \*   Hypervolume (Multi-objective optimization metric) \*   ID-precision (Atom localization) \*   ID-recall (Atom localization) \*   Learned Perceptual Image Patch Similarity (LPIPS) \*   MAE (Mean Absolute Error) \*   ME (Mean Error) \*   MRAE% (Mean Relative Absolute Error) \*   MSE (Mean Squared Error) \*   MTF (Modulation Transfer Function) \*   Multi-mae (L1 norm of multi-dimensional data) \*   Mutual Information (MI) \*   NPV (Negative Predictive Value) \*   NPS (Noise Power Spectrum) \*   Position deviation (∆d) (Atom localization) \*   PPV (Positive Predictive Value) \*   Precision \*   PSNR (Peak Signal-to-Noise Ratio) \*   RE% (Relative Error) \*   Recall \*   RMSE (Root Mean Square Error) \*   ROC (Receiver Operating Characteristic) analysis \*   ROUGE (Recall-Oriented Understudy for Gisting Evaluation) (Text summary metric) \*   Sensitivity (Sens) \*   SNR (Signal-to-Noise Ratio) \*   Specificity (Spec) \*   SSIM (Structural Similarity Index Measure) \*   SUV (Standardized Uptake Value) / SUVmax (PET metric) \*   Tenengrad function (Image quality metric) \*   TPD (Total Perfusion Deficit) (SPECT metric)

**6\. Software & Libraries** \*   abTEM (Python package for TEM simulation) \*   AtomAI (Python library for ML in microscopy) \*   Atomap (Software package) \*   AtomQC (JARVIS-Tools interface) \*   AtomVision (Library for atomistic images) \*   ChemDataExtractor (NLP tool) \*   ChemNLP (NLP tool) \*   Circq (Quantum computing package) \*   clusterProfiler (R package for GSEA) \*   Computem (STEM image simulation software) \*   Conda (Package manager) \*   CUDA (Parallel computing platform) \*   Dask (Parallel computing library) \*   DADA2 (R pipeline for amplicon sequencing) \*   Deep Graph Library (DGL) \*   DeepMedic (CNN architecture) \*   DIVIDE (Dixon-VIBE Deep Learning \- Attenuation correction) \*   Docker (Containerization platform) \*   dscribe (Python library for SOAP vectors) \*   Gatan Imaging Filter Quantum (EELS detector system) \*   Gatan Microscopy Suite (GMS) \*   Git / GitHub (Version control / hosting) \*   Google Colab (Cloud computing environment) \*   gpCAM (Python library for autonomous experimentation) \*   Gpytorch (Python library for Gaussian processes) \*   Gwyddion (SPM data analysis software) \*   HyperSpy (Software package) \*   ImageJ (Image processing software) / TurboReg plugin \*   InFluence (Python package for detector simulation) \*   InSyTe FLECT-CT (Imaging system) \*   IntelliSpace (Philips workstation) \*   IQon (Philips spectral CT scanner) \*   JARVIS-DFT / JARVIS-Leaderboard / JARVIS-Tools \*   JADBio AutoML (AI platform) \*   JEOL (Microscope manufacturer) \*   Keras (Deep learning library \- implicitly via TensorFlow) \*   LabVIEW (Software development environment) \*   LAMMPS (Molecular dynamics simulator) \*   LiberTEM (Software package) \*   MATLAB (Programming language / environment) / fitgeotrans function \*   MLFlow (ML lifecycle platform) \*   MPMS (Magnetic Property Measurement System \- Quantum Design) \*   Nanonis (SPM control software) \*   National Instruments DAQ (Data Acquisition hardware) \*   NetworkX (Python library for graphs) \*   NiftyNet (Deep learning platform for medical imaging) \*   Nion Swift (STEM control interface) \*   Nion UltraSTEM (Microscope model) \*   NumPy (Python library) \*   Omicron (STM/AFM manufacturer) \*   OneView camera (Gatan detector) \*   OpenCV (Computer vision library \- implicitly used) \*   Optiray (Contrast agent \- Bayer) \*   Pennylane (Quantum computing package) \*   Phyloseq (R package for microbiome analysis) \*   Pint (Python library for units) \*   Pivotal Tracker (Project management tool) \*   Platypus Technologies (Substrate supplier) \*   Prismatic (STEM/HRTEM simulation software) \*   Protochips (In situ TEM holder manufacturer) \*   PtychoNN (FCNN for ptychography) \*   PtychoShelves (Ptychography toolkit) \*   PWscf / Quantum Espresso (DFT software package) \*   Pycroscopy (Microscopy data analysis platform) \*   PyJEM Wrapper (TEM control software component) \*   PyLabRobot (Open-source hyper-language framework) \*   PyroVED (Python library \- VAE related) \*   Python (Programming language) \*   PyTorch (Deep learning library) \*   Qiskit (Quantum computing software) \*   R (Programming language / environment) \*   Scikit-image (Python library for image processing) \*   Scikit-learn (Python library for machine learning) \*   SciPy (Python library for scientific computing) \*   Segmentation-models-with-pytorch (SMP) \*   Semrock (Optical filter manufacturer) \*   Siemens Symbia (SPECT/CT system) \*   Silva database (Taxonomy database) \*   SPSS (Statistical software \- implicitly used for t-tests) \*   Tequila (Quantum computing package) \*   TEMCenter (JEOL control application) \*   TEMUL Toolkit (Software package) \*   TensorFlow (Deep learning library) \*   Thermo Fisher / FEI (Microscope manufacturer \- Titan, Themis, Helios) \*   Thorlabs (Optics/photonics component supplier) \*   TianGen Biotechnology (RNA extraction kit supplier) \*   Ubuntu (Operating system) \*   Unisoku (STM manufacturer) \*   VASP (Vienna Ab initio Simulation Package) (DFT software) \*   xSPECT/CT (Siemens reconstruction algorithm)

**7\. Prompting / Guidance / Interaction Terms** \*   Active learning-driven experimentation \*   Adapter system design (MIDA \- for tool integration) \*   Automated decision-making \*   Automated experimentation / workflows \*   Autonomous convergence / discovery / optimization / systems \*   Bayesian optimization guided exploration \*   Causal analysis / inference \*   Centralized controller \*   Closed-loop control / feedback / processing \*   Curiosity-driven experimentation \*   Data-driven models / approaches \*   Domain-specific hyper-languages (e.g., PyLabRobot) \*   Explainable AI / Explainability \*   Feature identification / extraction \*   Few-shot learning (Requires few labeled examples) \*   Forward modeling (Using simulation to predict experiment) \*   Generative models (Creating data based on learned patterns) \*   Guidance weights (Diffusion models) \*   Guided experimentation / exploration \*   Human intervention / Human-in-the-loop (HiL) / Human-augmented \*   Hyperparameter optimization / tuning \*   Inferential bias (Incorporating physics) \*   Information theory-based approach \*   Integrated data view / analysis \*   Interpretability \*   Iterative optimization / refinement / training / framework \*   Knowledge extraction \*   Knowledge-informed framework \*   Landmark identification / pairing (Image registration) \*   Latent Bayesian optimization (zBO \- guiding hyperparameter search) \*   Learning from limited / sparse data \*   Learning from unlabeled data / Self-distillation \*   Low-level vs. High-level decisions (ML vs. Human) \*   Machine learning guided discovery \*   Machine vision automated detection/classification \*   Multi-workflow integrated data analysis \*   Novelty-based search strategies \*   On-the-fly analysis / decision-making \*   Physics-based criteria / constraints / guidance / knowledge / models \*   Predictive modeling / models \*   Prior information / knowledge guided \*   Real-time analysis / feedback / control / detection / monitoring \*   Reinforcement learning-enhanced workflows \*   Self-driving microscopy \*   Semantic segmentation (Providing pixel-level labels) \*   Similarity-based loss (Affinity-VAE) \*   Sparse data analytics \*   Structural causal model approach \*   Supervised learning (Requires labeled data) \*   Synthetic data generation (GANs, simulation) \*   Task-based discrimination \*   Theoretical modeling (General term for using theory) \*   Theory+AI/ML approach \*   Transfer learning (Leveraging pre-trained models/data) \*   Uncertainty quantification (UQ) \*   Unsupervised learning (No labeled data required) \*   User feedback (Validation) \*   Variational Bayesian methods \*   Weak supervision (Using noisy/limited labels)

This categorization covers the vast majority of technical terms, concepts, and methods mentioned across the abstracts and supporting text provided in the CSV file.

\[

  {"category": "Algorithms & Models", "term": "1D-CNN (One-Dimensional Convolutional Neural Network)"},

  {"category": "Algorithms & Models", "term": "2.5D dilated CNNs"},

  {"category": "Algorithms & Models", "term": "2D Gaussian fitting"},

  {"category": "Algorithms & Models", "term": "Adafactor (Optimizer)"},

  {"category": "Algorithms & Models", "term": "Adam optimizer"},

  {"category": "Algorithms & Models", "term": "AdamW (Optimizer)"},

  {"category": "Algorithms & Models", "term": "Affinity-VAE (Variational Autoencoder variant)"},

  {"category": "Algorithms & Models", "term": "Affine linear transformation"},

  {"category": "Algorithms & Models", "term": "ALIGNN (Atomistic Line Graph Neural Network)"},

  {"category": "Algorithms & Models", "term": "ANN (Artificial Neural Network)"},

  {"category": "Algorithms & Models", "term": "Attention Gates (AG)"},

  {"category": "Algorithms & Models", "term": "Autoencoder (AEC)"},

  {"category": "Algorithms & Models", "term": "AUTOMAP"},

  {"category": "Algorithms & Models", "term": "BCE (Binary Crossentropy) loss"},

  {"category": "Algorithms & Models", "term": "BCEWithLogitsLoss (Loss function)"},

  {"category": "Algorithms & Models", "term": "BERT-style objective"},

  {"category": "Algorithms & Models", "term": "Blind deblurring with L0-regularized intensity and gradient prior (L0RIGP)"},

  {"category": "Algorithms & Models", "term": "Canonical Correlation Analysis (CCA)"},

  {"category": "Algorithms & Models", "term": "Cascaded Linear Systems Analysis (LCSA)"},

  {"category": "Algorithms & Models", "term": "Categorical cross entropy loss function"},

  {"category": "Algorithms & Models", "term": "Center-of-mass (reconstruction approach)"},

  {"category": "Algorithms & Models", "term": "Clustering algorithms (general)"},

  {"category": "Algorithms & Models", "term": "CNN (Convolutional Neural Network)"},

  {"category": "Algorithms & Models", "term": "Compressive Sensing (CS)"},

  {"category": "Algorithms & Models", "term": "Conditional GAN (cGAN)"},

  {"category": "Algorithms & Models", "term": "Convolution approximation (for STEM simulation)"},

  {"category": "Algorithms & Models", "term": "CycleGAN (Cycle Generative Adversarial Network)"},

  {"category": "Algorithms & Models", "term": "DAG (Directed Acyclic Graph)"},

  {"category": "Algorithms & Models", "term": "DCCN (Deep Convolutional Neural Network)"},

  {"category": "Algorithms & Models", "term": "DCGAN (Deep Convolutional GAN)"},

  {"category": "Algorithms & Models", "term": "Decision Trees"},

  {"category": "Algorithms & Models", "term": "Denoising algorithms (general)"},

  {"category": "Algorithms & Models", "term": "DenseNet (Dense Convolutional Network)"},

  {"category": "Algorithms & Models", "term": "Depth-first search algorithm"},

  {"category": "Algorithms & Models", "term": "DFT (Density Functional Theory)"},

  {"category": "Algorithms & Models", "term": "DFT-D3 (DFT with Dispersion Correction)"},

  {"category": "Algorithms & Models", "term": "Differential Expected Hypervolume Improvement (qEHVI)"},

  {"category": "Algorithms & Models", "term": "DIP (Deep Image Prior)"},

  {"category": "Algorithms & Models", "term": "DKL (Deep Kernel Learning)"},

  {"category": "Algorithms & Models", "term": "DL (Deep Learning)"},

  {"category": "Algorithms & Models", "term": "DLR (Deep Learning-based Reconstruction)"},

  {"category": "Algorithms & Models", "term": "DNN (Deep Neural Network)"},

  {"category": "Algorithms & Models", "term": "DRUNet (Double ResNet-U-Net)"},

  {"category": "Algorithms & Models", "term": "Dynamic thresholding (Diffusion model technique)"},

  {"category": "Algorithms & Models", "term": "Edge detection algorithms"},

  {"category": "Algorithms & Models", "term": "ELIT (Ensemble Learning Iterative Training)"},

  {"category": "Algorithms & Models", "term": "Empirical wavelets"},

  {"category": "Algorithms & Models", "term": "Ensemble Learning (EL)"},

  {"category": "Algorithms & Models", "term": "Evoformer (Neural network block)"},

  {"category": "Algorithms & Models", "term": "Exact Diagonalization"},

  {"category": "Algorithms & Models", "term": "Factor analysis (FA)"},

  {"category": "Algorithms & Models", "term": "Faster R-CNN (Faster Regional Convolutional Neural Network)"},

  {"category": "Algorithms & Models", "term": "FastGAN"},

  {"category": "Algorithms & Models", "term": "FastPET (Direct reconstruction CNN)"},

  {"category": "Algorithms & Models", "term": "FBP (Filtered Back Projection)"},

  {"category": "Algorithms & Models", "term": "FCN (Fully Convolutional Network)"},

  {"category": "Algorithms & Models", "term": "FISTA (Fast Iterative Shrinkage-Thresholding Algorithm)"},

  {"category": "Algorithms & Models", "term": "Fourier Transform (FT / FFT)"},

  {"category": "Algorithms & Models", "term": "Frame-Aligned Point Error (FAPE) (Loss function)"},

  {"category": "Algorithms & Models", "term": "GAN (Generative Adversarial Network)"},

  {"category": "Algorithms & Models", "term": "GANCS"},

  {"category": "Algorithms & Models", "term": "Gaussian curve fitting"},

  {"category": "Algorithms & Models", "term": "Gaussian Mixture Model (GMM)"},

  {"category": "Algorithms & Models", "term": "Gaussian process method / Gaussian Process Regression (GP / GPR)"},

  {"category": "Algorithms & Models", "term": "Generalized maximum-likelihood method (with gradient descent)"},

  {"category": "Algorithms & Models", "term": "GGA (Generalized Gradient Approximation)"},

  {"category": "Algorithms & Models", "term": "Gradient Descent"},

  {"category": "Algorithms & Models", "term": "Graph Neural Networks (GNN)"},

  {"category": "Algorithms & Models", "term": "Hadamard Patterns (Spatial modulation)"},

  {"category": "Algorithms & Models", "term": "He initialization"},

  {"category": "Algorithms & Models", "term": "Hed (Holistically Nested Edge Detection)"},

  {"category": "Algorithms & Models", "term": "Hilbert-Huang Transform (HHT)"},

  {"category": "Algorithms & Models", "term": "iRadonMAP"},

  {"category": "Algorithms & Models", "term": "Iterative reconstruction algorithms (general, e.g., for CT/SPECT/PET)"},

  {"category": "Algorithms & Models", "term": "Iterative shrinkage-thresholding algorithm (ISTA)"},

  {"category": "Algorithms & Models", "term": "Iterative optimization (general)"},

  {"category": "Algorithms & Models", "term": "jVAE / jrVAE (Joint Rotationally Invariant VAE)"},

  {"category": "Algorithms & Models", "term": "k-means clustering"},

  {"category": "Algorithms & Models", "term": "L1 loss function"},

  {"category": "Algorithms & Models", "term": "L2 loss function"},

  {"category": "Algorithms & Models", "term": "Laplacian of Gaussian (LOG) blob detection"},

  {"category": "Algorithms & Models", "term": "Linear regression"},

  {"category": "Algorithms & Models", "term": "LiNGAM (Linear Non-Gaussian Acyclic Model)"},

  {"category": "Algorithms & Models", "term": "Local Multiphase Chan-Vese model (Image segmentation)"},

  {"category": "Algorithms & Models", "term": "Logistic regression"},

  {"category": "Algorithms & Models", "term": "Long Short-Time Memory (LSTM)"},

  {"category": "Algorithms & Models", "term": "Low pass filter"},

  {"category": "Algorithms & Models", "term": "LSDA+U (Local Spin Density Approximation \+ U)"},

  {"category": "Algorithms & Models", "term": "MAP-Elites (Multi-dimensional Archive of Phenotypic Elites)"},

  {"category": "Algorithms & Models", "term": "Markov Chain Monte Carlo (MCMC)"},

  {"category": "Algorithms & Models", "term": "Mask RCNN"},

  {"category": "Algorithms & Models", "term": "Maximum likelihood interaction time estimation"},

  {"category": "Algorithms & Models", "term": "Maximum-likelihood method (for material decomposition)"},

  {"category": "Algorithms & Models", "term": "mDCSRN-GAN"},

  {"category": "Algorithms & Models", "term": "Mean Absolute Error (MAE) loss"},

  {"category": "Algorithms & Models", "term": "Mean imputation"},

  {"category": "Algorithms & Models", "term": "Mean Squared Error (MSE) loss"},

  {"category": "Algorithms & Models", "term": "Merriman-Bence-Osher (MBO) scheme / classifier"},

  {"category": "Algorithms & Models", "term": "Meta-SRGAN"},

  {"category": "Algorithms & Models", "term": "ML (Machine Learning)"},

  {"category": "Algorithms & Models", "term": "MLR (Multiple Linear Regression)"},

  {"category": "Algorithms & Models", "term": "Monte Carlo method / simulation"},

  {"category": "Algorithms & Models", "term": "MRR-CNN (Multi-Resolution Registration CNN)"},

  {"category": "Algorithms & Models", "term": "Multislice (Electron microscopy simulation method)"},

  {"category": "Algorithms & Models", "term": "Naive Bayes classification"},

  {"category": "Algorithms & Models", "term": "Nelder-Mead simplex method (Optimization)"},

  {"category": "Algorithms & Models", "term": "Neural Networks (NN)"},

  {"category": "Algorithms & Models", "term": "NMF (Non-Negative Matrix Factorization)"},

  {"category": "Algorithms & Models", "term": "NMF-QMV (Nonnegative Matrix Factorization from Quadradic Minimum Volume)"},

  {"category": "Algorithms & Models", "term": "Non-rigid registration"},

  {"category": "Algorithms & Models", "term": "Non-Linear Sigma Model (NLSM)"},

  {"category": "Algorithms & Models", "term": "NPRM (Non-Parametric Residue Mapping)"},

  {"category": "Algorithms & Models", "term": "Noisy Student Self-Distillation"},

  {"category": "Algorithms & Models", "term": "Normalized cross-correlation"},

  {"category": "Algorithms & Models", "term": "OSEM (Ordered Subsets Expectation Maximization)"},

  {"category": "Algorithms & Models", "term": "Otsu's method (Thresholding)"},

  {"category": "Algorithms & Models", "term": "Parallel FFTs"},

  {"category": "Algorithms & Models", "term": "Parallel spatial decomposition"},

  {"category": "Algorithms & Models", "term": "Partial least squares regression (PLSR)"},

  {"category": "Algorithms & Models", "term": "Particle Filter"},

  {"category": "Algorithms & Models", "term": "Patch-level discriminators (GAN component)"},

  {"category": "Algorithms & Models", "term": "PAW (Projector Augmented Plane-Wave method)"},

  {"category": "Algorithms & Models", "term": "PAW-PBE (Potential used in PAW)"},

  {"category": "Algorithms & Models", "term": "PCA (Principal Component Analysis)"},

  {"category": "Algorithms & Models", "term": "PBE (Perdew-Burke-Ernzerhof)"},

  {"category": "Algorithms & Models", "term": "PDE constrained optimization"},

  {"category": "Algorithms & Models", "term": "Phase cross-correlation"},

  {"category": "Algorithms & Models", "term": "Phase-field model"},

  {"category": "Algorithms & Models", "term": "Pix2Pix (Conditional GAN)"},

  {"category": "Algorithms & Models", "term": "Powell's method (Optimization)"},

  {"category": "Algorithms & Models", "term": "PredRNN (Recurrent Neural Network for prediction)"},

  {"category": "Algorithms & Models", "term": "PRISM method (STEM/HRTEM simulation)"},

  {"category": "Algorithms & Models", "term": "Prototypical Network (Few-shot learning)"},

  {"category": "Algorithms & Models", "term": "Ptychography / Ptychographic phase retrieval algorithms"},

  {"category": "Algorithms & Models", "term": "Q-AE (Quadratic Autoencoder)"},

  {"category": "Algorithms & Models", "term": "QSAR (Quantitative Structure Activity Relationships)"},

  {"category": "Algorithms & Models", "term": "Quantum CNN"},

  {"category": "Algorithms & Models", "term": "Random Forest (RF)"},

  {"category": "Algorithms & Models", "term": "Random goal exploration algorithms"},

  {"category": "Algorithms & Models", "term": "Randomized Singular Value Decomposition (rSVD)"},

  {"category": "Algorithms & Models", "term": "RANSAC (Random Sample Consensus)"},

  {"category": "Algorithms & Models", "term": "Recon-GLGAN"},

  {"category": "Algorithms & Models", "term": "RefineGAN"},

  {"category": "Algorithms & Models", "term": "Regression algorithms (general)"},

  {"category": "Algorithms & Models", "term": "Reinforcement Learning (RL) / Deep RL"},

  {"category": "Algorithms & Models", "term": "ReLU activation function"},

  {"category": "Algorithms & Models", "term": "Res (Deep Residual Learning Framework)"},

  {"category": "Algorithms & Models", "term": "ResHedNet (Residual Holistically Nested Edge Detection Network)"},

  {"category": "Algorithms & Models", "term": "ResNet / ResUNet (Residual Network / Residual U-Net)"},

  {"category": "Algorithms & Models", "term": "Richardson-Lucy (RL) method (Deblurring)"},

  {"category": "Algorithms & Models", "term": "Ridge Polynomial Neural Network (RPN)"},

  {"category": "Algorithms & Models", "term": "RNN (Recurrent Neural Network)"},

  {"category": "Algorithms & Models", "term": "rVAE (Rotationally-Invariant Variational Autoencoder)"},

  {"category": "Algorithms & Models", "term": "Scharr edge detection filter"},

  {"category": "Algorithms & Models", "term": "Segmentation algorithms (general)"},

  {"category": "Algorithms & Models", "term": "Semi-supervised VAEs"},

  {"category": "Algorithms & Models", "term": "sh-VAE (Shift-invariant VAE)"},

  {"category": "Algorithms & Models", "term": "SIFT (Scale-Invariant Feature Transform)"},

  {"category": "Algorithms & Models", "term": "Signal Detection Theory (SDT)"},

  {"category": "Algorithms & Models", "term": "Singular Value Decomposition (SVD)"},

  {"category": "Algorithms & Models", "term": "SliceGAN"},

  {"category": "Algorithms & Models", "term": "SMATB Potential (Molecular Dynamics)"},

  {"category": "Algorithms & Models", "term": "SMLM (Single Molecule Localization Microscopy)"},

  {"category": "Algorithms & Models", "term": "SMOTE (Synthetic Minority Over-sampling Technique)"},

  {"category": "Algorithms & Models", "term": "Snake activation function"},

  {"category": "Algorithms & Models", "term": "SOAP (Smooth Overlap of Atomic Positions)"},

  {"category": "Algorithms & Models", "term": "Spach transformer"},

  {"category": "Algorithms & Models", "term": "Spatial Modulation (Single-pixel imaging)"},

  {"category": "Algorithms & Models", "term": "Spectral Analysis"},

  {"category": "Algorithms & Models", "term": "SRGAN (Super-Resolution GAN)"},

  {"category": "Algorithms & Models", "term": "SSIM loss"},

  {"category": "Algorithms & Models", "term": "Stable Diffusion (SD) (Image generation model)"},

  {"category": "Algorithms & Models", "term": "STED (Stimulated Emission Depletion Microscopy)"},

  {"category": "Algorithms & Models", "term": "Stochastic Weight Averaging (SWA)"},

  {"category": "Algorithms & Models", "term": "Størmer-Verlet symplectic integrator"},

  {"category": "Algorithms & Models", "term": "SVR (Support Vector Regression)"},

  {"category": "Algorithms & Models", "term": "SVM (Support Vector Machine)"},

  {"category": "Algorithms & Models", "term": "T5-XXL encoder (Language model)"},

  {"category": "Algorithms & Models", "term": "Tersoff-Hamann (TH) method (STM simulation)"},

  {"category": "Algorithms & Models", "term": "Thresholding algorithms"},

  {"category": "Algorithms & Models", "term": "Total Variation Regularization"},

  {"category": "Algorithms & Models", "term": "Transformer decoder blocks"},

  {"category": "Algorithms & Models", "term": "TrueFidelity (DLR algorithm)"},

  {"category": "Algorithms & Models", "term": "t-SNE (t-distributed Stochastic Neighbor Embedding)"},

  {"category": "Algorithms & Models", "term": "U-Net / UNet (CNN architecture)"},

  {"category": "Algorithms & Models", "term": "VAE (Variational Autoencoder)"},

  {"category": "Algorithms & Models", "term": "Variational Quantum Deflation (VQD)"},

  {"category": "Algorithms & Models", "term": "Variational Quantum Eigen Solver (VQE)"},

  {"category": "Algorithms & Models", "term": "VoxelMorph (Deep learning registration method)"},

  {"category": "Algorithms & Models", "term": "Wasserstein GAN"},

  {"category": "Algorithms & Models", "term": "Wavelet Transform (WT)"},

  {"category": "Algorithms & Models", "term": "Wiener filter (WF) (Deblurring)"},

  {"category": "Algorithms & Models", "term": "YOLO / YOLOv4 (You Only Look Once \- Object detection)"},

  {"category": "Experimental Techniques & Instruments", "term": "4D-STEM (Four-Dimensional Scanning Transmission Electron Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Aberration-corrected STEM/TEM"},

  {"category": "Experimental Techniques & Instruments", "term": "Adhesion (snap-in) force imaging (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "AFM (Atomic Force Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "AFM-IR (Atomic Force Microscopy-Infrared Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ambient condition measurements (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Annealing (Sample treatment)"},

  {"category": "Experimental Techniques & Instruments", "term": "Annular Bright-Field (ABF) imaging (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Annular Dark Field (ADF) imaging (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "AP-CVD (Atmospheric Pressure Chemical Vapor Deposition)"},

  {"category": "Experimental Techniques & Instruments", "term": "APT (Atomic Probe Tomography)"},

  {"category": "Experimental Techniques & Instruments", "term": "Arc discharge (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Arterial blood sampling (PET)"},

  {"category": "Experimental Techniques & Instruments", "term": "Atom counting (STEM methodology)"},

  {"category": "Experimental Techniques & Instruments", "term": "Atomic manipulation (SPM/STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Atomic-resolution imaging (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ball milling (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "Band excitation piezoresponse force microscopy (BEPFM) / spectroscopy (BEPS)"},

  {"category": "Experimental Techniques & Instruments", "term": "Bragg diffraction analysis"},

  {"category": "Experimental Techniques & Instruments", "term": "C-AFM (Conductive Atomic Force Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Cathodoluminescence (CL) spectroscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "CCD (Charge-Coupled Device) camera"},

  {"category": "Experimental Techniques & Instruments", "term": "Cherenkov radiation detection"},

  {"category": "Experimental Techniques & Instruments", "term": "Chemical vapor deposition (CVD)"},

  {"category": "Experimental Techniques & Instruments", "term": "CMOS (Complementary Metal-Oxide-Semiconductor) detector"},

  {"category": "Experimental Techniques & Instruments", "term": "Coherent x-ray imaging / scattering"},

  {"category": "Experimental Techniques & Instruments", "term": "Collagen imaging (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Collimators (SPECT \- parallel hole, fan beam)"},

  {"category": "Experimental Techniques & Instruments", "term": "Combustion (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Confocal laser scanning microscopy (CLSM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Constant current mode (STM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Constant height mode (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Contrast agent administration (CT/MRI)"},

  {"category": "Experimental Techniques & Instruments", "term": "Cryo-electron tomography (cryo-ET)"},

  {"category": "Experimental Techniques & Instruments", "term": "Cryo-EM / Cryogenic Electron Microscopy (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "Cryo-STEM / Cryogenic Scanning Transmission Electron Microscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Cryo-TEM / Cryogenic Transmission Electron Microscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "CT (Computed Tomography)"},

  {"category": "Experimental Techniques & Instruments", "term": "Current-time (I-t) spectroscopy (STM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Cylindrical shell random masks (Neutron imaging)"},

  {"category": "Experimental Techniques & Instruments", "term": "Dark-field microscopy (DFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "DC voltage ramping (PFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Dectris ELA direct electron detector"},

  {"category": "Experimental Techniques & Instruments", "term": "DECT (Dual-Energy Computed Tomography)"},

  {"category": "Experimental Techniques & Instruments", "term": "Defocused probe imaging (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Diamond-coated conductive tips (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Differential conductance (dI/dV) measurements (STS)"},

  {"category": "Experimental Techniques & Instruments", "term": "Diffuse optical tomography"},

  {"category": "Experimental Techniques & Instruments", "term": "Diffuse scattering analysis"},

  {"category": "Experimental Techniques & Instruments", "term": "Dispersive elements (e.g., prism, grating for spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "DOI (Depth of Interaction) measurement (PET/SPECT)"},

  {"category": "Experimental Techniques & Instruments", "term": "Drop casting (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "Dry transfer method (for 2D materials)"},

  {"category": "Experimental Techniques & Instruments", "term": "Dual-layer spectral detector CT"},

  {"category": "Experimental Techniques & Instruments", "term": "EBSD (Electron Backscatter Diffraction)"},

  {"category": "Experimental Techniques & Instruments", "term": "EEGS (Electron Energy Gain Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "EELS (Electron Energy Loss Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Electrochemical oxidation (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Electron crystallography"},

  {"category": "Experimental Techniques & Instruments", "term": "Electron diffraction"},

  {"category": "Experimental Techniques & Instruments", "term": "Electron Ronchigram"},

  {"category": "Experimental Techniques & Instruments", "term": "Electron spectroscopy (general)"},

  {"category": "Experimental Techniques & Instruments", "term": "EM (Electron Microscopy \- general term)"},

  {"category": "Experimental Techniques & Instruments", "term": "EMCCD (Electron-Multiplying Charge-Coupled Device) camera"},

  {"category": "Experimental Techniques & Instruments", "term": "EMPAD (Electron Microscope Pixel Array Detector)"},

  {"category": "Experimental Techniques & Instruments", "term": "Endoscopy / Photoacoustic Endoscopy (PAE)"},

  {"category": "Experimental Techniques & Instruments", "term": "Etched tips (W, Pt/Ir for STM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ex-situ annealing"},

  {"category": "Experimental Techniques & Instruments", "term": "Femtosecond laser (for UED/transitions)"},

  {"category": "Experimental Techniques & Instruments", "term": "FIBS (Filament-Induced Breakdown Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "FIB (Focused Ion Beam) milling / lift-out"},

  {"category": "Experimental Techniques & Instruments", "term": "Fluorescence imaging (FL) / microscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Fluorescence Recovery After Photobleaching (FRAP)"},

  {"category": "Experimental Techniques & Instruments", "term": "Force-distance curve acquisition (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Freeze-pump-thaw cycles (Water purification)"},

  {"category": "Experimental Techniques & Instruments", "term": "FTS (Fourier Transform Spectroscopy) module"},

  {"category": "Experimental Techniques & Instruments", "term": "Full-field spectroscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Gammex Multi-Energy CT phantom"},

  {"category": "Experimental Techniques & Instruments", "term": "Gas cell holder (for in situ TEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Gemstone Spectral Imaging (GSI) (CT reconstruction)"},

  {"category": "Experimental Techniques & Instruments", "term": "HAADF (High-Angle Annular Dark-Field) imaging (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Hadamard pattern modulation masks (Neutron imaging)"},

  {"category": "Experimental Techniques & Instruments", "term": "High-speed AFM (HS-AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "High-throughput experimentation"},

  {"category": "Experimental Techniques & Instruments", "term": "HOPG (Highly Oriented Pyrolytic Graphite) substrate/cleavage"},

  {"category": "Experimental Techniques & Instruments", "term": "HRTEM (High-Resolution Transmission Electron Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Hydrothermal/solvothermal synthesis (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Hyperspectral imaging (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "Imaging Fourier transform spectrometer"},

  {"category": "Experimental Techniques & Instruments", "term": "In situ / Operando (S)TEM"},

  {"category": "Experimental Techniques & Instruments", "term": "In situ charge state manipulation (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Infrared (IR) spectroscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Interferometric scattering microscopy (iSCAT)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ion milling (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "Laser ablation (for LIBS, nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Laser excitation (for fluorescence, PAI, STML)"},

  {"category": "Experimental Techniques & Instruments", "term": "Laser induced optical barriers (LIOB) (Scintillators)"},

  {"category": "Experimental Techniques & Instruments", "term": "Laser-induced circular dichroism (Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Laser-STM (Combined laser excitation and STM)"},

  {"category": "Experimental Techniques & Instruments", "term": "LC-EM (Liquid Cell Electron Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "LED (Light-Emitting Diode) light source"},

  {"category": "Experimental Techniques & Instruments", "term": "LIF (Laser-Induced Fluorescence) spectroscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "LIBS (Laser-Induced Breakdown Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Liposomes (Nanoparticle type)"},

  {"category": "Experimental Techniques & Instruments", "term": "Lock-in technique (STS)"},

  {"category": "Experimental Techniques & Instruments", "term": "Lorentz phase microscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Low-dose imaging (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "MAADF (Medium-Angle Annular Dark-Field) imaging (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Magnetometry"},

  {"category": "Experimental Techniques & Instruments", "term": "Manometric measurements (Gas adsorption)"},

  {"category": "Experimental Techniques & Instruments", "term": "Mass spectrometry (for water cleanliness check)"},

  {"category": "Experimental Techniques & Instruments", "term": "MBE (Molecular Beam Epitaxy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Mechanical exfoliation (for 2D materials)"},

  {"category": "Experimental Techniques & Instruments", "term": "Mechanical thinning/polishing (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "Metascintillator/heteroscintillator detectors"},

  {"category": "Experimental Techniques & Instruments", "term": "Micro-photoluminescence (μPL)"},

  {"category": "Experimental Techniques & Instruments", "term": "Microfluidics"},

  {"category": "Experimental Techniques & Instruments", "term": "Microscopy (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "Microwave irradiation/synthesis (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Monochromated electron beam (STEM-EELS)"},

  {"category": "Experimental Techniques & Instruments", "term": "MRI (Magnetic Resonance Imaging)"},

  {"category": "Experimental Techniques & Instruments", "term": "Multi-modal electron microscopy (fused HAADF, EDX, EELS)"},

  {"category": "Experimental Techniques & Instruments", "term": "Nanobeam diffraction (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Nanoparticle synthesis (General term, various methods)"},

  {"category": "Experimental Techniques & Instruments", "term": "Nanopositioner (AFM component)"},

  {"category": "Experimental Techniques & Instruments", "term": "Non-contact AFM (nc-AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Non-destructive surface ablation"},

  {"category": "Experimental Techniques & Instruments", "term": "Optical coherence tomography (OCT)"},

  {"category": "Experimental Techniques & Instruments", "term": "Optical microscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Ozone annealing (Sample treatment)"},

  {"category": "Experimental Techniques & Instruments", "term": "PAI / PACT / PAM (Photoacoustic Imaging / Computed Tomography / Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Path integral molecular dynamics (PIMD)"},

  {"category": "Experimental Techniques & Instruments", "term": "PCD (Photon-Counting Detector)"},

  {"category": "Experimental Techniques & Instruments", "term": "Perfusion imaging (SPECT)"},

  {"category": "Experimental Techniques & Instruments", "term": "PET (Positron Emission Tomography)"},

  {"category": "Experimental Techniques & Instruments", "term": "PFM (Piezoresponse Force Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "PFS (Piezoresponse Force Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Photocurrent tunneling microscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Photothermal microscopy (PTM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Pixelated detectors (STEM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Planar fluorescence imaging (2D)"},

  {"category": "Experimental Techniques & Instruments", "term": "Plasma generation (LIBS, filaments)"},

  {"category": "Experimental Techniques & Instruments", "term": "PLD (Pulsed Laser Deposition)"},

  {"category": "Experimental Techniques & Instruments", "term": "Polycapillary optics (XRF)"},

  {"category": "Experimental Techniques & Instruments", "term": "Probe-corrected TEM/STEM"},

  {"category": "Experimental Techniques & Instruments", "term": "Protein imaging (Cryo-EM/AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Pyrolysis (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "qPlus sensor (AFM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Quantum dots (Nanoparticle type)"},

  {"category": "Experimental Techniques & Instruments", "term": "Quasi-particle interference (QPI) imaging (STM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Radioligand therapy (RLT)"},

  {"category": "Experimental Techniques & Instruments", "term": "Radiolabeled meal (GES)"},

  {"category": "Experimental Techniques & Instruments", "term": "Radiopharmaceutical administration (SPECT/PET)"},

  {"category": "Experimental Techniques & Instruments", "term": "Raman spectroscopy / Tip-enhanced Raman spectroscopy (TERS) / Surface enhanced Raman microscopy (SERM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Remote hydrogen plasma treatment"},

  {"category": "Experimental Techniques & Instruments", "term": "Resistive Plate Chambers (RPCs) (Detector)"},

  {"category": "Experimental Techniques & Instruments", "term": "Scintillator detectors"},

  {"category": "Experimental Techniques & Instruments", "term": "SDD (Silicon Drift Detector) (XRF)"},

  {"category": "Experimental Techniques & Instruments", "term": "Self-flux method (Crystal growth)"},

  {"category": "Experimental Techniques & Instruments", "term": "SEM (Scanning Electron Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Semiconductor detectors"},

  {"category": "Experimental Techniques & Instruments", "term": "Single-pixel imaging (SPI) (Neutron imaging)"},

  {"category": "Experimental Techniques & Instruments", "term": "Slanted edge method (Detector characterization)"},

  {"category": "Experimental Techniques & Instruments", "term": "SMLM (Single Molecule Localization Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Solid state photosensors (SPECT/PET)"},

  {"category": "Experimental Techniques & Instruments", "term": "Solution strategies (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "SPCCT (Spectral Photon-Counting Computed Tomography)"},

  {"category": "Experimental Techniques & Instruments", "term": "SPECT (Single-Photon Emission Computed Tomography)"},

  {"category": "Experimental Techniques & Instruments", "term": "Spectrally-resolved fast-gated imaging"},

  {"category": "Experimental Techniques & Instruments", "term": "Spectroscopy (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "Spin coating (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "SPM (Scanning Probe Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Spray coating (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "SPRM (Surface Plasmon Resonance Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Sputtering (Sample cleaning/preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "STED (Stimulated Emission Depletion Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "STEM (Scanning Transmission Electron Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "STM (Scanning Tunneling Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Strain-stress measurements"},

  {"category": "Experimental Techniques & Instruments", "term": "Structured Illumination Microscopy (SIM)"},

  {"category": "Experimental Techniques & Instruments", "term": "STS (Scanning Tunneling Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Super-resolution microscopy (General term)"},

  {"category": "Experimental Techniques & Instruments", "term": "Surface cleaning/heating (UHV preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "Synchrotron-based x-ray source"},

  {"category": "Experimental Techniques & Instruments", "term": "Template-assisted synthesis (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "TEM (Transmission Electron Microscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "Thermal decomposition (Nanoparticle synthesis)"},

  {"category": "Experimental Techniques & Instruments", "term": "Time-of-Flight (TOF) estimation (PET)"},

  {"category": "Experimental Techniques & Instruments", "term": "Time-resolved 2D spectral imaging"},

  {"category": "Experimental Techniques & Instruments", "term": "Time-resolved TEM / Ultrafast TEM (UTEM) / Ultrafast Electron Diffraction (UED)"},

  {"category": "Experimental Techniques & Instruments", "term": "Tomographic fluorescence imaging (3D)"},

  {"category": "Experimental Techniques & Instruments", "term": "Toxicological assays (Cellular viability)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ultrahigh vacuum (UHV) conditions"},

  {"category": "Experimental Techniques & Instruments", "term": "Ultrasonication (Sample preparation)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ultrasonography (USG)"},

  {"category": "Experimental Techniques & Instruments", "term": "Ussing chamber assay (Permeability measurement)"},

  {"category": "Experimental Techniques & Instruments", "term": "Vibrational sum frequency generation (VSFG) spectroscopy"},

  {"category": "Experimental Techniques & Instruments", "term": "Viscometry"},

  {"category": "Experimental Techniques & Instruments", "term": "Voltage pulsing (STM)"},

  {"category": "Experimental Techniques & Instruments", "term": "Water dosing (UHV)"},

  {"category": "Experimental Techniques & Instruments", "term": "Web crawling (Data acquisition)"},

  {"category": "Experimental Techniques & Instruments", "term": "Wavelength-shifting fibers (Detector component)"},

  {"category": "Experimental Techniques & Instruments", "term": "XFEL (X-ray Free Electron Laser)"},

  {"category": "Experimental Techniques & Instruments", "term": "XPS (X-ray Photoelectron Spectroscopy)"},

  {"category": "Experimental Techniques & Instruments", "term": "XRD (X-ray Diffraction)"},

  {"category": "Experimental Techniques & Instruments", "term": "XRF / Micro-XRF (X-ray Fluorescence / micro-)"},

  {"category": "Experimental Techniques & Instruments", "term": "X-ray imaging (General term)"},

  {"category": "Methodologies & Workflows", "term": "Ab initio molecular dynamic simulations (AIMD)"},

  {"category": "Methodologies & Workflows", "term": "Active learning"},

  {"category": "Methodologies & Workflows", "term": "Active Recommender System (ARS)"},

  {"category": "Methodologies & Workflows", "term": "Adaptation of classical macroscopic definitions (Bayesian approach)"},

  {"category": "Methodologies & Workflows", "term": "Adapter system design (MIDA)"},

  {"category": "Methodologies & Workflows", "term": "Affinity-VAE framework"},

  {"category": "Methodologies & Workflows", "term": "AI-aided optical imaging protocol"},

  {"category": "Methodologies & Workflows", "term": "AI-driven automation (STEM, SPM)"},

  {"category": "Methodologies & Workflows", "term": "AI/ML-driven autonomous experimentation / workflows"},

  {"category": "Methodologies & Workflows", "term": "Atom-counting methodology (STEM)"},

  {"category": "Methodologies & Workflows", "term": "Atom-S2 framework (ML for stress mapping)"},

  {"category": "Methodologies & Workflows", "term": "AtomAI framework / software package"},

  {"category": "Methodologies & Workflows", "term": "AtomVision library / framework"},

  {"category": "Methodologies & Workflows", "term": "Automated analysis / segmentation / classification / detection (General term)"},

  {"category": "Methodologies & Workflows", "term": "Automated feedback-controlled system (STEM fabrication)"},

  {"category": "Methodologies & Workflows", "term": "Autonomous convergence (STM parameters)"},

  {"category": "Methodologies & Workflows", "term": "Bayesian optimization (BO) / Latent Bayesian Optimization (zBO)"},

  {"category": "Methodologies & Workflows", "term": "Benchmark dataset development (STEM atom segmentation)"},

  {"category": "Methodologies & Workflows", "term": "Bicrystal interface construction"},

  {"category": "Methodologies & Workflows", "term": "Cartoon and texture decomposition (Image analysis)"},

  {"category": "Methodologies & Workflows", "term": "Causal analysis / Causal learning"},

  {"category": "Methodologies & Workflows", "term": "Chemical structure visualization (Scanning Raman picoscopy)"},

  {"category": "Methodologies & Workflows", "term": "Classification (Supervised ML task)"},

  {"category": "Methodologies & Workflows", "term": "Closed-loop instrument control"},

  {"category": "Methodologies & Workflows", "term": "Computational modeling (General term)"},

  {"category": "Methodologies & Workflows", "term": "Computer-aided diagnosis (CAD)"},

  {"category": "Methodologies & Workflows", "term": "Correlative analysis (structure-property, image-spectrum)"},

  {"category": "Methodologies & Workflows", "term": "Cross-validation (e.g., 10-fold, 9-fold)"},

  {"category": "Methodologies & Workflows", "term": "Data augmentation (flipping, rotating, noise addition, etc.)"},

  {"category": "Methodologies & Workflows", "term": "Data cleaning / preprocessing (imputation, duplicate removal, filtering, normalization, registration, contrast enhancement)"},

  {"category": "Methodologies & Workflows", "term": "Data fusion / Hypermodal data fusion"},

  {"category": "Methodologies & Workflows", "term": "Data integration (MIDA framework)"},

  {"category": "Methodologies & Workflows", "term": "Data observability strategies (MIDA)"},

  {"category": "Methodologies & Workflows", "term": "Data reusability assessment (NSDRA framework)"},

  {"category": "Methodologies & Workflows", "term": "Decision-theoretic approach (Resolution limit analysis)"},

  {"category": "Methodologies & Workflows", "term": "Deep kernel learning (DKL) workflow"},

  {"category": "Methodologies & Workflows", "term": "Deep learning pipeline (Amorphous material analysis)"},

  {"category": "Methodologies & Workflows", "term": "Deep learning-based reconstruction (DLR \- for CT/PET/SPECT)"},

  {"category": "Methodologies & Workflows", "term": "Deep-learning framework (General term)"},

  {"category": "Methodologies & Workflows", "term": "Defect engineering"},

  {"category": "Methodologies & Workflows", "term": "Defect identification / detection / classification / quantification (General goal)"},

  {"category": "Methodologies & Workflows", "term": "Density functional theory (DFT) calculations"},

  {"category": "Methodologies & Workflows", "term": "Dimensionality expansion (GAN-based)"},

  {"category": "Methodologies & Workflows", "term": "Dimensionality reduction (PCA, NMF, SVD, VAE, autoencoder)"},

  {"category": "Methodologies & Workflows", "term": "Direct reconstruction (PET \- neural network based)"},

  {"category": "Methodologies & Workflows", "term": "Disentanglement / Disentangled representations (VAE feature)"},

  {"category": "Methodologies & Workflows", "term": "Distributed neighbor lists (LAMMPS parallelization)"},

  {"category": "Methodologies & Workflows", "term": "Domain adaptation"},

  {"category": "Methodologies & Workflows", "term": "Dosimetry calculations / methodology (Nuclear medicine)"},

  {"category": "Methodologies & Workflows", "term": "Dual Autoencoder-Classifier algorithm"},

  {"category": "Methodologies & Workflows", "term": "Dynamic tracking / observation (Microscopy)"},

  {"category": "Methodologies & Workflows", "term": "ELIT (Ensemble learning-iterative training) workflow"},

  {"category": "Methodologies & Workflows", "term": "End-to-end structure prediction (AlphaFold)"},

  {"category": "Methodologies & Workflows", "term": "Ensemble learning / Deep ensembles"},

  {"category": "Methodologies & Workflows", "term": "Feature importance analysis"},

  {"category": "Methodologies & Workflows", "term": "Feature selection / extraction"},

  {"category": "Methodologies & Workflows", "term": "Few-shot learning"},

  {"category": "Methodologies & Workflows", "term": "Forward modeling (Image simulation)"},

  {"category": "Methodologies & Workflows", "term": "Fused multi-modal electron microscopy"},

  {"category": "Methodologies & Workflows", "term": "Generative modeling (General approach)"},

  {"category": "Methodologies & Workflows", "term": "Geometric Unmixing"},

  {"category": "Methodologies & Workflows", "term": "Ghost Imaging (GI) (Neutron imaging)"},

  {"category": "Methodologies & Workflows", "term": "Hamiltonian simulation (Quantum computation)"},

  {"category": "Methodologies & Workflows", "term": "High-throughput analysis / screening / optimization"},

  {"category": "Methodologies & Workflows", "term": "Histo-image representation (PET data)"},

  {"category": "Methodologies & Workflows", "term": "Human-in-the-loop autonomous experiments / workflows"},

  {"category": "Methodologies & Workflows", "term": "Image registration (affine, non-rigid, optimization-based)"},

  {"category": "Methodologies & Workflows", "term": "Image restoration / deblurring / denoising / enhancement (General tasks)"},

  {"category": "Methodologies & Workflows", "term": "Image segmentation (semantic, instance, domain-based)"},

  {"category": "Methodologies & Workflows", "term": "Image synthesis / generation (GANs, VAEs, diffusion models)"},

  {"category": "Methodologies & Workflows", "term": "Image-to-image translation (GANs, CycleGAN)"},

  {"category": "Methodologies & Workflows", "term": "Image-to-spectrum (Im2Spec) / Spectrum-to-image (Spec2Im) translation"},

  {"category": "Methodologies & Workflows", "term": "Ingrained framework (Simulation-experiment fusion)"},

  {"category": "Methodologies & Workflows", "term": "In silico modeling / simulation (General term)"},

  {"category": "Methodologies & Workflows", "term": "JARVIS-Leaderboard benchmark platform"},

  {"category": "Methodologies & Workflows", "term": "Knowledge-informed framework (Autonomous experimentation)"},

  {"category": "Methodologies & Workflows", "term": "Latent space exploration / analysis (VAE)"},

  {"category": "Methodologies & Workflows", "term": "Linear unmixing methods (PCA, NMF, ICA)"},

  {"category": "Methodologies & Workflows", "term": "Machine vision algorithm / framework"},

  {"category": "Methodologies & Workflows", "term": "Material decomposition (Spectral CT)"},

  {"category": "Methodologies & Workflows", "term": "Materials design / discovery (General goal)"},

  {"category": "Methodologies & Workflows", "term": "MIDA framework (Multi-workflow Integrated Data Analysis)"},

  {"category": "Methodologies & Workflows", "term": "Molecular dynamics (MD) simulations / Path integral MD (PIMD)"},

  {"category": "Methodologies & Workflows", "term": "Molecular fingerprint detection (Spectroscopy)"},

  {"category": "Methodologies & Workflows", "term": "Molecular simulation (General term)"},

  {"category": "Methodologies & Workflows", "term": "Multi-fidelity modeling"},

  {"category": "Methodologies & Workflows", "term": "Multi-modal fusion (Imaging)"},

  {"category": "Methodologies & Workflows", "term": "Multivariate statistical analysis"},

  {"category": "Methodologies & Workflows", "term": "Neuro-symbolic AI techniques"},

  {"category": "Methodologies & Workflows", "term": "Noise filtering / reduction (General task)"},

  {"category": "Methodologies & Workflows", "term": "Novelty-based search strategies"},

  {"category": "Methodologies & Workflows", "term": "NSDRA framework (NanoSafety Data Reusability Assessment)"},

  {"category": "Methodologies & Workflows", "term": "Object detection / localization (YOLO, Faster R-CNN, Mask RCNN)"},

  {"category": "Methodologies & Workflows", "term": "Online learning"},

  {"category": "Methodologies & Workflows", "term": "Optimization (General task, various algorithms)"},

  {"category": "Methodologies & Workflows", "term": "Parametric kinetic modeling (PET \- compartmental, Patlak, spectral)"},

  {"category": "Methodologies & Workflows", "term": "Parsimonious representation / description discovery (VAE)"},

  {"category": "Methodologies & Workflows", "term": "Partially Observable Markov Decision Process (POMDP)"},

  {"category": "Methodologies & Workflows", "term": "Peak analysis (Spectroscopy \- traditional approach)"},

  {"category": "Methodologies & Workflows", "term": "Photorealistic text-to-image synthesis (Imagen model)"},

  {"category": "Methodologies & Workflows", "term": "Physics-based / Physics-informed / Physics-inspired ML/AI"},

  {"category": "Methodologies & Workflows", "term": "Prediction / Prognosis (Medical imaging)"},

  {"category": "Methodologies & Workflows", "term": "Property prediction (Materials science)"},

  {"category": "Methodologies & Workflows", "term": "Provenance management (MIDA)"},

  {"category": "Methodologies & Workflows", "term": "Quantitative structure determination (STEM)"},

  {"category": "Methodologies & Workflows", "term": "Radiomics / Radiophenomics"},

  {"category": "Methodologies & Workflows", "term": "Real-time analysis / feedback / control / detection / monitoring"},

  {"category": "Methodologies & Workflows", "term": "Regression (Supervised ML task)"},

  {"category": "Methodologies & Workflows", "term": "Reinforcement learning framework"},

  {"category": "Methodologies & Workflows", "term": "Resolution enhancement / Super-resolution (Imaging task)"},

  {"category": "Methodologies & Workflows", "term": "RODAS (Rapid Object Detection and Action System)"},

  {"category": "Methodologies & Workflows", "term": "Scanning Raman picoscopy"},

  {"category": "Methodologies & Workflows", "term": "Self-distillation (Deep learning training technique)"},

  {"category": "Methodologies & Workflows", "term": "Semi-supervised learning"},

  {"category": "Methodologies & Workflows", "term": "Sparse data analytics / Sparse image retrieval"},

  {"category": "Methodologies & Workflows", "term": "Spiral scanning pattern (SPM data acquisition)"},

  {"category": "Methodologies & Workflows", "term": "Statistical forecasting"},

  {"category": "Methodologies & Workflows", "term": "Statistical Parameter Estimation (Atom counting)"},

  {"category": "Methodologies & Workflows", "term": "Structure initialization (Database query, bicrystal construction)"},

  {"category": "Methodologies & Workflows", "term": "Structure reconstruction (3D, atomic)"},

  {"category": "Methodologies & Workflows", "term": "Structure-property relationship exploration"},

  {"category": "Methodologies & Workflows", "term": "Superpixel semantic segmentation"},

  {"category": "Methodologies & Workflows", "term": "Supervised learning"},

  {"category": "Methodologies & Workflows", "term": "Supervised manifold learning"},

  {"category": "Methodologies & Workflows", "term": "Teaching by Demonstration (Robotics/AI)"},

  {"category": "Methodologies & Workflows", "term": "Text-to-image synthesis"},

  {"category": "Methodologies & Workflows", "term": "Theragnostics (Combined diagnosis and therapy)"},

  {"category": "Methodologies & Workflows", "term": "Topological reconstruction (Radiation detector)"},

  {"category": "Methodologies & Workflows", "term": "Training data generation / curation (Simulation, augmentation, NLP)"},

  {"category": "Methodologies & Workflows", "term": "Transfer learning"},

  {"category": "Methodologies & Workflows", "term": "Uncertainty quantification (UQ \- Dropout, Ensembles, Quantile Regression, GP)"},

  {"category": "Methodologies & Workflows", "term": "Unsupervised learning"},

  {"category": "Methodologies & Workflows", "term": "User feedback survey (Validation)"},

  {"category": "Methodologies & Workflows", "term": "Visual proteomics"},

  {"category": "Methodologies & Workflows", "term": "Weak supervision"},

  {"category": "Concepts & Principles", "term": "Ab initio calculations (General term)"},

  {"category": "Concepts & Principles", "term": "Absorptive potential approximation (HAADF STEM theory)"},

  {"category": "Concepts & Principles", "term": "Acidity (Surface chemistry \- pKa, PA)"},

  {"category": "Concepts & Principles", "term": "Activation function (Neural networks)"},

  {"category": "Concepts & Principles", "term": "Affinity matrix (Affinity-VAE component)"},

  {"category": "Concepts & Principles", "term": "ALARA principle (As Low As Reasonably Achievable \- radiation dose)"},

  {"category": "Concepts & Principles", "term": "Alternating high/low polarization dynamics (Ferroelectrics)"},

  {"category": "Concepts & Principles", "term": "Ångström resolution"},

  {"category": "Concepts & Principles", "term": "Anisotropy (Chemical bonds, particles)"},

  {"category": "Concepts & Principles", "term": "Artifacts (Imaging \- general term)"},

  {"category": "Concepts & Principles", "term": "Atomic defects (vacancies, dopants, impurities, grain boundaries, edge terminations)"},

  {"category": "Concepts & Principles", "term": "Atomic registry"},

  {"category": "Concepts & Principles", "term": "Atomic structure / configuration"},

  {"category": "Concepts & Principles", "term": "Atomic-scale chemistry / visualization / manipulation / engineering"},

  {"category": "Concepts & Principles", "term": "Attenuation correction (AC) (PET/SPECT)"},

  {"category": "Concepts & Principles", "term": "Automated experimentation / Autonomous systems"},

  {"category": "Concepts & Principles", "term": "Band gap (Materials property)"},

  {"category": "Concepts & Principles", "term": "Band structure (Electronic property)"},

  {"category": "Concepts & Principles", "term": "Bayesian methods / inference"},

  {"category": "Concepts & Principles", "term": "Beam-induced transformations / damage / interactions"},

  {"category": "Concepts & Principles", "term": "Big data (Microscopy context)"},

  {"category": "Concepts & Principles", "term": "Biomarker identification"},

  {"category": "Concepts & Principles", "term": "Biocompatibility / Toxicity (Nanoparticles)"},

  {"category": "Concepts & Principles", "term": "Bond length / angle distribution"},

  {"category": "Concepts & Principles", "term": "Bond-order valence sums (Acidity estimation)"},

  {"category": "Concepts & Principles", "term": "Bulk-boundary correspondence (Topological materials)"},

  {"category": "Concepts & Principles", "term": "Canted antiferromagnetism (CAF) (Graphene state)"},

  {"category": "Concepts & Principles", "term": "Causality / Causal inference / Causal mechanisms / Causal models"},

  {"category": "Concepts & Principles", "term": "Cellular viability (Toxicology endpoint)"},

  {"category": "Concepts & Principles", "term": "Charge Density Wave (CDW)"},

  {"category": "Concepts & Principles", "term": "Charge ordering"},

  {"category": "Concepts & Principles", "term": "Charge state manipulation (Defects)"},

  {"category": "Concepts & Principles", "term": "Chemical bonding / bonds"},

  {"category": "Concepts & Principles", "term": "Chemical composition"},

  {"category": "Concepts & Principles", "term": "Chemical pathways / reactions / transformations"},

  {"category": "Concepts & Principles", "term": "Chirality / Chiral molecules / nanostructures / switching"},

  {"category": "Concepts & Principles", "term": "Coherence (Electron beam property)"},

  {"category": "Concepts & Principles", "term": "Coherent states (Intervalley \- IVC in graphene)"},

  {"category": "Concepts & Principles", "term": "Colloidal crystal growth (Classical vs. nonclassical pathways)"},

  {"category": "Concepts & Principles", "term": "Complex morphologies"},

  {"category": "Concepts & Principles", "term": "Computational cost / efficiency"},

  {"category": "Concepts & Principles", "term": "Concentration (Nanoparticles, dopants)"},

  {"category": "Concepts & Principles", "term": "Confinement of light (Atomistic scale)"},

  {"category": "Concepts & Principles", "term": "Confounding variables (Causal inference)"},

  {"category": "Concepts & Principles", "term": "Continuity (Latent space property)"},

  {"category": "Concepts & Principles", "term": "Contrast / Z-contrast (Imaging property)"},

  {"category": "Concepts & Principles", "term": "Convergence (Optimization, simulations)"},

  {"category": "Concepts & Principles", "term": "Correlated electron systems / Strong correlation"},

  {"category": "Concepts & Principles", "term": "Correlation (General statistical term)"},

  {"category": "Concepts & Principles", "term": "Coulomb blockade effects"},

  {"category": "Concepts & Principles", "term": "Coulomb interaction"},

  {"category": "Concepts & Principles", "term": "Cramer-Rao lower bound (Information theory)"},

  {"category": "Concepts & Principles", "term": "Crystal lattice / structure / defects / orientation / polymorphs / symmetry / space group"},

  {"category": "Concepts & Principles", "term": "Crystal growth pathways"},

  {"category": "Concepts & Principles", "term": "Curiosity-driven experimentation"},

  {"category": "Concepts & Principles", "term": "Data standardization / sharing / management / FAIR principles"},

  {"category": "Concepts & Principles", "term": "Debye-Waller factor (Thermal vibration simulation)"},

  {"category": "Concepts & Principles", "term": "Decision function (Decision theory)"},

  {"category": "Concepts & Principles", "term": "Deconvolution (Signal processing)"},

  {"category": "Concepts & Principles", "term": "Defect formation mechanisms"},

  {"category": "Concepts & Principles", "term": "Degeneracy (High-resolution microscopy data)"},

  {"category": "Concepts & Principles", "term": "Degrees of freedom (Particles, spins, etc.)"},

  {"category": "Concepts & Principles", "term": "Density of states (DOS) / Local DOS (LDOS)"},

  {"category": "Concepts & Principles", "term": "Detection limit"},

  {"category": "Concepts & Principles", "term": "Diagnostic accuracy / confidence / performance / efficacy"},

  {"category": "Concepts & Principles", "term": "Dielectric characteristics"},

  {"category": "Concepts & Principles", "term": "Diffusion models (Generative modeling principle)"},

  {"category": "Concepts & Principles", "term": "Dipole direction (Molecular property)"},

  {"category": "Concepts & Principles", "term": "Dirac cone model / Coupled Dirac cone model"},

  {"category": "Concepts & Principles", "term": "Dirac mass gap"},

  {"category": "Concepts & Principles", "term": "Disordered systems / sites"},

  {"category": "Concepts & Principles", "term": "Disentanglement (Latent space property)"},

  {"category": "Concepts & Principles", "term": "Dispersion (Phonon, plasmon, exciton)"},

  {"category": "Concepts & Principles", "term": "Domain structure / walls (Ferroelectrics)"},

  {"category": "Concepts & Principles", "term": "Dopants / Doping"},

  {"category": "Concepts & Principles", "term": "Drug delivery (Nanoparticles)"},

  {"category": "Concepts & Principles", "term": "Effective atomic number (Zeff) (CT property)"},

  {"category": "Concepts & Principles", "term": "Effective ionization potential (EDX theory)"},

  {"category": "Concepts & Principles", "term": "Eigen/Zundel cations (Hydrated protons)"},

  {"category": "Concepts & Principles", "term": "Elastic modulus"},

  {"category": "Concepts & Principles", "term": "Elastic scattering / Inelastic scattering (Electron microscopy)"},

  {"category": "Concepts & Principles", "term": "Electric field / Magnetic field (Internal, applied)"},

  {"category": "Concepts & Principles", "term": "Electron beam positioning / control / manipulation / shaping"},

  {"category": "Concepts & Principles", "term": "Electron density"},

  {"category": "Concepts & Principles", "term": "Electron-hole pairs / interaction"},

  {"category": "Concepts & Principles", "term": "Electron-lattice interactions"},

  {"category": "Concepts & Principles", "term": "Electronic order (Mott, pseudogap)"},

  {"category": "Concepts & Principles", "term": "Electronic structure"},

  {"category": "Concepts & Principles", "term": "Electrostatic barriers (Grain boundaries)"},

  {"category": "Concepts & Principles", "term": "Elemental mapping / quantification"},

  {"category": "Concepts & Principles", "term": "Emergent physics / phenomena / properties"},

  {"category": "Concepts & Principles", "term": "Energy resolution"},

  {"category": "Concepts & Principles", "term": "Entropy (Information theory)"},

  {"category": "Concepts & Principles", "term": "Equivariant attention (Neural network concept)"},

  {"category": "Concepts & Principles", "term": "Error propagation / sources of variance (statistical, systematic)"},

  {"category": "Concepts & Principles", "term": "Evolutionary constraints / history (Protein structure)"},

  {"category": "Concepts & Principles", "term": "Exchange interaction (Quantum Hall ferromagnetism)"},

  {"category": "Concepts & Principles", "term": "Excitation (Electronic, plasmonic, phonon, excitonic)"},

  {"category": "Concepts & Principles", "term": "Exciton / Moiré exciton / Excitonic luminescence / lattices"},

  {"category": "Concepts & Principles", "term": "Explainability / Interpretability (AI/ML)"},

  {"category": "Concepts & Principles", "term": "Exploration vs. Exploitation (Optimization, RL)"},

  {"category": "Concepts & Principles", "term": "Ferroelectricity / Ferroelasticity"},

  {"category": "Concepts & Principles", "term": "Fidelity (Image generation quality)"},

  {"category": "Concepts & Principles", "term": "First principles modeling / calculations"},

  {"category": "Concepts & Principles", "term": "Fisher information"},

  {"category": "Concepts & Principles", "term": "Force field methods / Machine learning force fields (MLFF)"},

  {"category": "Concepts & Principles", "term": "Free energy / Gibbs free energy"},

  {"category": "Concepts & Principles", "term": "Frequency domain analysis"},

  {"category": "Concepts & Principles", "term": "Functional groups (Molecular property)"},

  {"category": "Concepts & Principles", "term": "Functional materials / functionality"},

  {"category": "Concepts & Principles", "term": "Generalization ability (ML models)"},

  {"category": "Concepts & Principles", "term": "Generative physical model (Hamiltonian, Ginzburg-Landau)"},

  {"category": "Concepts & Principles", "term": "Geometric constraints (Protein structure)"},

  {"category": "Concepts & Principles", "term": "Geometry (Nanoparticle property)"},

  {"category": "Concepts & Principles", "term": "Ginzburg-Landau model"},

  {"category": "Concepts & Principles", "term": "Grain boundaries (GBs)"},

  {"category": "Concepts & Principles", "term": "Graph inference problem (Protein structure prediction)"},

  {"category": "Concepts & Principles", "term": "Ground state (Quantum mechanics)"},

  {"category": "Concepts & Principles", "term": "Ground truth (ML term)"},

  {"category": "Concepts & Principles", "term": "Hamiltonian (Physical model)"},

  {"category": "Concepts & Principles", "term": "Hardness (Materials property)"},

  {"category": "Concepts & Principles", "term": "Heterointerfaces / Heterostructures (Materials)"},

  {"category": "Concepts & Principles", "term": "Heterogeneous catalysis"},

  {"category": "Concepts & Principles", "term": "Hidden latent variables"},

  {"category": "Concepts & Principles", "term": "High-frequency information (Image property)"},

  {"category": "Concepts & Principles", "term": "Homogeneous / Heterogeneous materials"},

  {"category": "Concepts & Principles", "term": "Hydrogen bonding"},

  {"category": "Concepts & Principles", "term": "Hydrogen isotopic analysis / shifts"},

  {"category": "Concepts & Principles", "term": "Hydrogen storage materials"},

  {"category": "Concepts & Principles", "term": "Hyperparameters / Hyperparameter optimization / tuning"},

  {"category": "Concepts & Principles", "term": "Hysteresis (Piezo actuators, ferroelectrics)"},

  {"category": "Concepts & Principles", "term": "Ill-posed inverse problem"},

  {"category": "Concepts & Principles", "term": "Image quality (General term)"},

  {"category": "Concepts & Principles", "term": "Image registration (Concept)"},

  {"category": "Concepts & Principles", "term": "Inductive bias (ML term)"},

  {"category": "Concepts & Principles", "term": "Information density / Uniform information density"},

  {"category": "Concepts & Principles", "term": "Information theory"},

  {"category": "Concepts & Principles", "term": "Infrared chemical imaging"},

  {"category": "Concepts & Principles", "term": "Inhomogeneities (Material property)"},

  {"category": "Concepts & Principles", "term": "Input function (PET kinetics)"},

  {"category": "Concepts & Principles", "term": "Instrumentation limitations / stability"},

  {"category": "Concepts & Principles", "term": "Interatomic potentials"},

  {"category": "Concepts & Principles", "term": "Interface length / energy / properties"},

  {"category": "Concepts & Principles", "term": "Interference (Atomic motion, waves, electron scattering)"},

  {"category": "Concepts & Principles", "term": "Inter-laboratory approach (Benchmarking)"},

  {"category": "Concepts & Principles", "term": "Intermediate states (Dynamic processes)"},

  {"category": "Concepts & Principles", "term": "Internal dose maps / dosimetry"},

  {"category": "Concepts & Principles", "term": "Invariances (Rotational, translational)"},

  {"category": "Concepts & Principles", "term": "Inverse problem (General concept)"},

  {"category": "Concepts & Principles", "term": "Ising model / Hamiltonian"},

  {"category": "Concepts & Principles", "term": "Isotopes / Isotopic shifts / resolution"},

  {"category": "Concepts & Principles", "term": "Iterative refinement (AlphaFold)"},

  {"category": "Concepts & Principles", "term": "K-edge photoelectric effect (Spectral CT)"},

  {"category": "Concepts & Principles", "term": "Kansei engineering (Product design)"},

  {"category": "Concepts & Principles", "term": "Kekulé distortion (Graphene state)"},

  {"category": "Concepts & Principles", "term": "Kinetic modeling (PET)"},

  {"category": "Concepts & Principles", "term": "Kullback-Leibler (KL) divergence (VAE loss component)"},

  {"category": "Concepts & Principles", "term": "Landau levels (Quantum Hall effect)"},

  {"category": "Concepts & Principles", "term": "Large language models (LMs)"},

  {"category": "Concepts & Principles", "term": "Latent space / variables / representation / embedding"},

  {"category": "Concepts & Principles", "term": "Lattice distortion / strain / vibrations"},

  {"category": "Concepts & Principles", "term": "Light-matter interactions"},

  {"category": "Concepts & Principles", "term": "Likelihood (Statistical concept)"},

  {"category": "Concepts & Principles", "term": "Linear imaging model"},

  {"category": "Concepts & Principles", "term": "Loss function (ML training component)"},

  {"category": "Concepts & Principles", "term": "Low-dimensional representation"},

  {"category": "Concepts & Principles", "term": "Macroscopic observables / definitions"},

  {"category": "Concepts & Principles", "term": "Magnetic defects / structure / properties / ordering"},

  {"category": "Concepts & Principles", "term": "Masked MSA loss (AlphaFold training)"},

  {"category": "Concepts & Principles", "term": "Material properties (General term)"},

  {"category": "Concepts & Principles", "term": "Message passing (GNN concept)"},

  {"category": "Concepts & Principles", "term": "Microstructure / Nanostructure"},

  {"category": "Concepts & Principles", "term": "Microstructural optimization"},

  {"category": "Concepts & Principles", "term": "Misclassification (ML error)"},

  {"category": "Concepts & Principles", "term": "Mixed element nanostructures"},

  {"category": "Concepts & Principles", "term": "Moiré superlattice / potential / unit cell"},

  {"category": "Concepts & Principles", "term": "Molecular assembly / structure / dynamics / interactions / fingerprint / switch"},

  {"category": "Concepts & Principles", "term": "Molecular configuration monitoring"},

  {"category": "Concepts & Principles", "term": "Momentum distribution (Plasmonic fields)"},

  {"category": "Concepts & Principles", "term": "Morphology / Morphological homogeneity"},

  {"category": "Concepts & Principles", "term": "Mott insulator / order"},

  {"category": "Concepts & Principles", "term": "Multi-dimensional data / imaging"},

  {"category": "Concepts & Principles", "term": "Multi-objective optimization"},

  {"category": "Concepts & Principles", "term": "Multi-omics approach"},

  {"category": "Concepts & Principles", "term": "Multiple electron scattering"},

  {"category": "Concepts & Principles", "term": "Multivariate analysis"},

  {"category": "Concepts & Principles", "term": "MXenes (Material class)"},

  {"category": "Concepts & Principles", "term": "Nanomedicine / Nanotechnology / Nanotheranostics"},

  {"category": "Concepts & Principles", "term": "Nanoparticles (metallic, high-Z, quantum dots, nanorods, CNTs, etc.)"},

  {"category": "Concepts & Principles", "term": "Nanoscale / Atomic scale / Sub-angstrom resolution"},

  {"category": "Concepts & Principles", "term": "Natural language processing (NLP)"},

  {"category": "Concepts & Principles", "term": "Near-atomic-scale resolution"},

  {"category": "Concepts & Principles", "term": "Noise (shot, Poisson, scan, Gaussian, background) / Noise homoscedasticity"},

  {"category": "Concepts & Principles", "term": "Nonfluorescent matter"},

  {"category": "Concepts & Principles", "term": "Nonlinearity / Non-Gaussianity"},

  {"category": "Concepts & Principles", "term": "Nuclear fallout particle surrogates"},

  {"category": "Concepts & Principles", "term": "Nuclear materials / diagnostics"},

  {"category": "Concepts & Principles", "term": "Nuclear quantum effects"},

  {"category": "Concepts & Principles", "term": "Nuclearity (Number of atoms in nanoparticle)"},

  {"category": "Concepts & Principles", "term": "Nucleation physics / pathways"},

  {"category": "Concepts & Principles", "term": "Observational bias (Microscopy)"},

  {"category": "Concepts & Principles", "term": "Onset of conduction (MHP property)"},

  {"category": "Concepts & Principles", "term": "On-surface synthesis"},

  {"category": "Concepts & Principles", "term": "Optical contrast / properties / response / saturation"},

  {"category": "Concepts & Principles", "term": "Optical elastography (Brillouin microscopy)"},

  {"category": "Concepts & Principles", "term": "Order parameters"},

  {"category": "Concepts & Principles", "term": "Ordering transitions"},

  {"category": "Concepts & Principles", "term": "Organic synthesis"},

  {"category": "Concepts & Principles", "term": "Oscillator strength"},

  {"category": "Concepts & Principles", "term": "Out-of-distribution drift (ML challenge)"},

  {"category": "Concepts & Principles", "term": "Overfitting (ML challenge)"},

  {"category": "Concepts & Principles", "term": "Oxidation characteristics / behavior / pathways / states"},

  {"category": "Concepts & Principles", "term": "Pair distribution function"},

  {"category": "Concepts & Principles", "term": "Pairwise features / correlations (Protein structure)"},

  {"category": "Concepts & Principles", "term": "Parallelization (Computational concept)"},

  {"category": "Concepts & Principles", "term": "Parameter space exploration"},

  {"category": "Concepts & Principles", "term": "Parsimony (of physical descriptors)"},

  {"category": "Concepts & Principles", "term": "Periodicity / Periodic orderings / patterns"},

  {"category": "Concepts & Principles", "term": "Personalized medicine / treatment / dosimetry"},

  {"category": "Concepts & Principles", "term": "Phase (Material property, imaging concept)"},

  {"category": "Concepts & Principles", "term": "Phase instability (Perovskites)"},

  {"category": "Concepts & Principles", "term": "Phase retrieval"},

  {"category": "Concepts & Principles", "term": "Phase segregation"},

  {"category": "Concepts & Principles", "term": "Phase transitions (Photoinduced, quantum)"},

  {"category": "Concepts & Principles", "term": "Phenotyping / Image phenotyping"},

  {"category": "Concepts & Principles", "term": "Phonon dispersion"},

  {"category": "Concepts & Principles", "term": "Photorealism (Image generation quality)"},

  {"category": "Concepts & Principles", "term": "Photothermal effect / expansion"},

  {"category": "Concepts & Principles", "term": "Physical constraints / knowledge / bias (ML integration)"},

  {"category": "Concepts & Principles", "term": "Physical interaction framework (Protein structure)"},

  {"category": "Concepts & Principles", "term": "Picometer precision"},

  {"category": "Concepts & Principles", "term": "Pixelwise classification / learning"},

  {"category": "Concepts & Principles", "term": "Plasma chemistry / conditions / dynamics / evolution"},

  {"category": "Concepts & Principles", "term": "Plasmonics / Plasmonic fields / spectra / dispersion"},

  {"category": "Concepts & Principles", "term": "Point spread function (PSF)"},

  {"category": "Concepts & Principles", "term": "Polarization switching / dynamics (Ferroelectrics)"},

  {"category": "Concepts & Principles", "term": "Polymorphs / Polymorphism"},

  {"category": "Concepts & Principles", "term": "Posterior probability distribution (Bayesian concept)"},

  {"category": "Concepts & Principles", "term": "Precision engineering (Atomic scale)"},

  {"category": "Concepts & Principles", "term": "Prior knowledge / information (Bayesian, ML)"},

  {"category": "Concepts & Principles", "term": "Probabilistic models"},

  {"category": "Concepts & Principles", "term": "Product morphology (Product design)"},

  {"category": "Concepts & Principles", "term": "Prosthetic groups (Protein structure)"},

  {"category": "Concepts & Principles", "term": "Protein assembly / structure / folding / dynamics"},

  {"category": "Concepts & Principles", "term": "Proton affinity (PA)"},

  {"category": "Concepts & Principles", "term": "Pseudogap order"},

  {"category": "Concepts & Principles", "term": "Quantitative analysis / metrics / imaging / measurements"},

  {"category": "Concepts & Principles", "term": "Quantum computation / algorithms / chemistry / information science / materials / phases / topology"},

  {"category": "Concepts & Principles", "term": "Quasiparticles"},

  {"category": "Concepts & Principles", "term": "Radiation burden / dose / exposure / detectors / damage"},

  {"category": "Concepts & Principles", "term": "Real space / Reciprocal space"},

  {"category": "Concepts & Principles", "term": "Reconstruction error (VAE loss component)"},

  {"category": "Concepts & Principles", "term": "Regularization (ML technique)"},

  {"category": "Concepts & Principles", "term": "Reproducibility (Experimental, computational)"},

  {"category": "Concepts & Principles", "term": "Resolution limit (Imaging)"},

  {"category": "Concepts & Principles", "term": "Resonance-assisted tunneling"},

  {"category": "Concepts & Principles", "term": "Rotational dynamics / invariance / orientation"},

  {"category": "Concepts & Principles", "term": "Sample quality"},

  {"category": "Concepts & Principles", "term": "Sampling (Adaptive, MCMC)"},

  {"category": "Concepts & Principles", "term": "Scattering cross-sections (HAADF, EDX, EELS)"},

  {"category": "Concepts & Principles", "term": "Self-assembly / Self-organization"},

  {"category": "Concepts & Principles", "term": "Sensitivity (Detector property, analysis concept)"},

  {"category": "Concepts & Principles", "term": "Serendipity (Materials discovery)"},

  {"category": "Concepts & Principles", "term": "Signal-to-noise ratio (SNR)"},

  {"category": "Concepts & Principles", "term": "Similarity measure (Image registration)"},

  {"category": "Concepts & Principles", "term": "Single-bond limit / resolution"},

  {"category": "Concepts & Principles", "term": "Single-molecule / particle level"},

  {"category": "Concepts & Principles", "term": "Spatial resolution / localization / frequency / distribution / variation"},

  {"category": "Concepts & Principles", "term": "Spectral broadening / features / imaging / resolution / separation / signatures / unmixing"},

  {"category": "Concepts & Principles", "term": "Spin qubits / states / structure / texture / degrees of freedom"},

  {"category": "Concepts & Principles", "term": "Stability (Instrumental, structural, thermal)"},

  {"category": "Concepts & Principles", "term": "Standoff detection (LIBS)"},

  {"category": "Concepts & Principles", "term": "Statistical significance"},

  {"category": "Concepts & Principles", "term": "Stochastic gradient descent (Optimization)"},

  {"category": "Concepts & Principles", "term": "Structural causal model"},

  {"category": "Concepts & Principles", "term": "Structural motifs"},

  {"category": "Concepts & Principles", "term": "Structure evolution / transformation"},

  {"category": "Concepts & Principles", "term": "Sub-pixel shifts (Image registration)"},

  {"category": "Concepts & Principles", "term": "Superconductivity / High-Tc superconductors"},

  {"category": "Concepts & Principles", "term": "Superhard materials"},

  {"category": "Concepts & Principles", "term": "Surface chemistry / properties / species / structure / reconstruction / defects / reactions / sites"},

  {"category": "Concepts & Principles", "term": "Surface plasmon resonance (SPR)"},

  {"category": "Concepts & Principles", "term": "Supramolecular self-assembly"},

  {"category": "Concepts & Principles", "term": "Symmetry / Symmetry breaking / Space group"},

  {"category": "Concepts & Principles", "term": "Synthetic data / images"},

  {"category": "Concepts & Principles", "term": "Systematic error / bias"},

  {"category": "Concepts & Principles", "term": "Tautomerization"},

  {"category": "Concepts & Principles", "term": "Temporal resolution / dynamics / evolution / scales"},

  {"category": "Concepts & Principles", "term": "Texture (Image analysis component)"},

  {"category": "Concepts & Principles", "term": "Thermal diffuse scattering (TDS) (STEM theory)"},

  {"category": "Concepts & Principles", "term": "Thermal energy / fluctuations / vibrations"},

  {"category": "Concepts & Principles", "term": "Theranostics"},

  {"category": "Concepts & Principles", "term": "Thermodynamic processes / stability / driving forces"},

  {"category": "Concepts & Principles", "term": "Thin films / 2D materials (Graphene, TMDCs, hBN, MXenes, Phosphorene)"},

  {"category": "Concepts & Principles", "term": "Tip motion effects / stability / conditioning / \-sample interaction / \-induced reactions"},

  {"category": "Concepts & Principles", "term": "Topological defects / excitations / insulators / quantum phases / spin states / correspondence principle"},

  {"category": "Concepts & Principles", "term": "Transient states / phenomena / changes / transformation processes"},

  {"category": "Concepts & Principles", "term": "Translation invariance / shifts"},

  {"category": "Concepts & Principles", "term": "Translational potential (Clinical applications)"},

  {"category": "Concepts & Principles", "term": "Transmission probability (Tunneling model)"},

  {"category": "Concepts & Principles", "term": "Tunneling current / spectroscopy"},

  {"category": "Concepts & Principles", "term": "Twin boundaries (TBs)"},

  {"category": "Concepts & Principles", "term": "Ultrafast dynamics / timescales"},

  {"category": "Concepts & Principles", "term": "Uncertainty (Latent variables, predictions)"},

  {"category": "Concepts & Principles", "term": "Universal approximation theorem (Neural networks)"},

  {"category": "Concepts & Principles", "term": "Valley ordering / polarization / skyrmions / texture (Graphene)"},

  {"category": "Concepts & Principles", "term": "Van der Waals forces / interactions / heterostructures"},

  {"category": "Concepts & Principles", "term": "Vibrational modes / spectroscopy"},

  {"category": "Concepts & Principles", "term": "Virtual environments / simulation (for RL training)"},

  {"category": "Concepts & Principles", "term": "Visualization (Data, structures, processes)"},

  {"category": "Concepts & Principles", "term": "Voigt profiles (Spectral fitting)"},

  {"category": "Concepts & Principles", "term": "Wannier-Bloch duality"},

  {"category": "Concepts & Principles", "term": "Wasserstein metric (GAN loss)"},

  {"category": "Concepts & Principles", "term": "Weight decay (L2 regularization)"},

  {"category": "Concepts & Principles", "term": "Wigner crystal / states"},

  {"category": "Evaluation Metrics", "term": "Accuracy (Acc)"},

  {"category": "Evaluation Metrics", "term": "Area Under the Curve (AUC) / Area under the ROC curve"},

  {"category": "Evaluation Metrics", "term": "Asymmetric index (Image evaluation)"},

  {"category": "Evaluation Metrics", "term": "Balanced Accuracy (BA)"},

  {"category": "Evaluation Metrics", "term": "Contrast Recovery Coefficient (CRC)"},

  {"category": "Evaluation Metrics", "term": "Dice Similarity Coefficient (DSC)"},

  {"category": "Evaluation Metrics", "term": "DQE (Detective Quantum Efficiency)"},

  {"category": "Evaluation Metrics", "term": "F1-score / F2-score"},

  {"category": "Evaluation Metrics", "term": "Hypervolume (Multi-objective optimization metric)"},

  {"category": "Evaluation Metrics", "term": "ID-precision (Atom localization)"},

  {"category": "Evaluation Metrics", "term": "ID-recall (Atom localization)"},

  {"category": "Evaluation Metrics", "term": "Learned Perceptual Image Patch Similarity (LPIPS)"},

  {"category": "Evaluation Metrics", "term": "MAE (Mean Absolute Error)"},

  {"category": "Evaluation Metrics", "term": "ME (Mean Error)"},

  {"category": "Evaluation Metrics", "term": "MRAE% (Mean Relative Absolute Error)"},

  {"category": "Evaluation Metrics", "term": "MSE (Mean Squared Error)"},

  {"category": "Evaluation Metrics", "term": "MTF (Modulation Transfer Function)"},

  {"category": "Evaluation Metrics", "term": "Multi-mae (L1 norm of multi-dimensional data)"},

  {"category": "Evaluation Metrics", "term": "Mutual Information (MI)"},

  {"category": "Evaluation Metrics", "term": "NPV (Negative Predictive Value)"},

  {"category": "Evaluation Metrics", "term": "NPS (Noise Power Spectrum)"},

  {"category": "Evaluation Metrics", "term": "Position deviation (∆d) (Atom localization)"},

  {"category": "Evaluation Metrics", "term": "PPV (Positive Predictive Value)"},

  {"category": "Evaluation Metrics", "term": "Precision"},

  {"category": "Evaluation Metrics", "term": "PSNR (Peak Signal-to-Noise Ratio)"},

  {"category": "Evaluation Metrics", "term": "RE% (Relative Error)"},

  {"category": "Evaluation Metrics", "term": "Recall"},

  {"category": "Evaluation Metrics", "term": "RMSE (Root Mean Square Error)"},

  {"category": "Evaluation Metrics", "term": "ROC (Receiver Operating Characteristic) analysis"},

  {"category": "Evaluation Metrics", "term": "ROUGE (Recall-Oriented Understudy for Gisting Evaluation) (Text summary metric)"},

  {"category": "Evaluation Metrics", "term": "Sensitivity (Sens)"},

  {"category": "Evaluation Metrics", "term": "SNR (Signal-to-Noise Ratio)"},

  {"category": "Evaluation Metrics", "term": "Specificity (Spec)"},

  {"category": "Evaluation Metrics", "term": "SSIM (Structural Similarity Index Measure)"},

  {"category": "Evaluation Metrics", "term": "SUV (Standardized Uptake Value) / SUVmax (PET metric)"},

  {"category": "Evaluation Metrics", "term": "Tenengrad function (Image quality metric)"},

  {"category": "Evaluation Metrics", "term": "TPD (Total Perfusion Deficit) (SPECT metric)"},

  {"category": "Software & Libraries", "term": "abTEM (Python package for TEM simulation)"},

  {"category": "Software & Libraries", "term": "AtomAI (Python library for ML in microscopy)"},

  {"category": "Software & Libraries", "term": "Atomap (Software package)"},

  {"category": "Software & Libraries", "term": "AtomQC (JARVIS-Tools interface)"},

  {"category": "Software & Libraries", "term": "AtomVision (Library for atomistic images)"},

  {"category": "Software & Libraries", "term": "ChemDataExtractor (NLP tool)"},

  {"category": "Software & Libraries", "term": "ChemNLP (NLP tool)"},

  {"category": "Software & Libraries", "term": "Circq (Quantum computing package)"},

  {"category": "Software & Libraries", "term": "clusterProfiler (R package for GSEA)"},

  {"category": "Software & Libraries", "term": "Computem (STEM image simulation software)"},

  {"category": "Software & Libraries", "term": "Conda (Package manager)"},

  {"category": "Software & Libraries", "term": "CUDA (Parallel computing platform)"},

  {"category": "Software & Libraries", "term": "DADA2 (R pipeline for amplicon sequencing)"},

  {"category": "Software & Libraries", "term": "Dask (Parallel computing library)"},

  {"category": "Software & Libraries", "term": "Deep Graph Library (DGL)"},

  {"category": "Software & Libraries", "term": "DeepMedic (CNN architecture)"},

  {"category": "Software & Libraries", "term": "DIVIDE (Dixon-VIBE Deep Learning \- Attenuation correction)"},

  {"category": "Software & Libraries", "term": "Docker (Containerization platform)"},

  {"category": "Software & Libraries", "term": "dscribe (Python library for SOAP vectors)"},

  {"category": "Software & Libraries", "term": "Gatan Imaging Filter Quantum (EELS detector system)"},

  {"category": "Software & Libraries", "term": "Gatan Microscopy Suite (GMS)"},

  {"category": "Software & Libraries", "term": "Git / GitHub (Version control / hosting)"},

  {"category": "Software & Libraries", "term": "Google Colab (Cloud computing environment)"},

  {"category": "Software & Libraries", "term": "gpCAM (Python library for autonomous experimentation)"},

  {"category": "Software & Libraries", "term": "Gpytorch (Python library for Gaussian processes)"},

  {"category": "Software & Libraries", "term": "Gwyddion (SPM data analysis software)"},

  {"category": "Software & Libraries", "term": "HyperSpy (Software package)"},

  {"category": "Software & Libraries", "term": "ImageJ (Image processing software) / TurboReg plugin"},

  {"category": "Software & Libraries", "term": "InFluence (Python package for detector simulation)"},

  {"category": "Software & Libraries", "term": "InSyTe FLECT-CT (Imaging system)"},

  {"category": "Software & Libraries", "term": "IntelliSpace (Philips workstation)"},

  {"category": "Software & Libraries", "term": "IQon (Philips spectral CT scanner)"},

  {"category": "Software & Libraries", "term": "JARVIS-DFT / JARVIS-Leaderboard / JARVIS-Tools"},

  {"category": "Software & Libraries", "term": "JADBio AutoML (AI platform)"},

  {"category": "Software & Libraries", "term": "JEOL (Microscope manufacturer)"},

  {"category": "Software & Libraries", "term": "Keras (Deep learning library \- implicitly via TensorFlow)"},

  {"category": "Software & Libraries", "term": "LabVIEW (Software development environment)"},

  {"category": "Software & Libraries", "term": "LAMMPS (Molecular dynamics simulator)"},

  {"category": "Software & Libraries", "term": "LiberTEM (Software package)"},

  {"category": "Software & Libraries", "term": "MATLAB (Programming language / environment) / fitgeotrans function"},

  {"category": "Software & Libraries", "term": "MLFlow (ML lifecycle platform)"},

  {"category": "Software & Libraries", "term": "MPMS (Magnetic Property Measurement System \- Quantum Design)"},

  {"category": "Software & Libraries", "term": "Nanonis (SPM control software)"},

  {"category": "Software & Libraries", "term": "National Instruments DAQ (Data Acquisition hardware)"},

  {"category": "Software & Libraries", "term": "NetworkX (Python library for graphs)"},

  {"category": "Software & Libraries", "term": "NiftyNet (Deep learning platform for medical imaging)"},

  {"category": "Software & Libraries", "term": "Nion Swift (STEM control interface)"},

  {"category": "Software & Libraries", "term": "Nion UltraSTEM (Microscope model)"},

  {"category": "Software & Libraries", "term": "NumPy (Python library)"},

  {"category": "Software & Libraries", "term": "Omicron (STM/AFM manufacturer)"},

  {"category": "Software & Libraries", "term": "OneView camera (Gatan detector)"},

  {"category": "Software & Libraries", "term": "OpenCV (Computer vision library \- implicitly used)"},

  {"category": "Software & Libraries", "term": "Optiray (Contrast agent \- Bayer)"},

  {"category": "Software & Libraries", "term": "Pennylane (Quantum computing package)"},

  {"category": "Software & Libraries", "term": "Phyloseq (R package for microbiome analysis)"},

  {"category": "Software & Libraries", "term": "Pint (Python library for units)"},

  {"category": "Software & Libraries", "term": "Pivotal Tracker (Project management tool)"},

  {"category": "Software & Libraries", "term": "Platypus Technologies (Substrate supplier)"},

  {"category": "Software & Libraries", "term": "Prismatic (STEM/HRTEM simulation software)"},

  {"category": "Software & Libraries", "term": "Protochips (In situ TEM holder manufacturer)"},

  {"category": "Software & Libraries", "term": "PtychoNN (FCNN for ptychography)"},

  {"category": "Software & Libraries", "term": "PtychoShelves (Ptychography toolkit)"},

  {"category": "Software & Libraries", "term": "PWscf / Quantum Espresso (DFT software package)"},

  {"category": "Software & Libraries", "term": "Pycroscopy (Microscopy data analysis platform)"},

  {"category": "Software & Libraries", "term": "PyJEM Wrapper (TEM control software component)"},

  {"category": "Software & Libraries", "term": "PyLabRobot (Open-source hyper-language framework)"},

  {"category": "Software & Libraries", "term": "PyroVED (Python library \- VAE related)"},

  {"category": "Software & Libraries", "term": "Python (Programming language)"},

  {"category": "Software & Libraries", "term": "PyTorch (Deep learning library)"},

  {"category": "Software & Libraries", "term": "Qiskit (Quantum computing software)"},

  {"category": "Software & Libraries", "term": "R (Programming language / environment)"},

  {"category": "Software & Libraries", "term": "Scikit-image (Python library for image processing)"},

  {"category": "Software & Libraries", "term": "Scikit-learn (Python library for machine learning)"},

  {"category": "Software & Libraries", "term": "SciPy (Python library for scientific computing)"},

  {"category": "Software & Libraries", "term": "Segmentation-models-with-pytorch (SMP)"},

  {"category": "Software & Libraries", "term": "Semrock (Optical filter manufacturer)"},

  {"category": "Software & Libraries", "term": "Siemens Symbia (SPECT/CT system)"},

  {"category": "Software & Libraries", "term": "Silva database (Taxonomy database)"},

  {"category": "Software & Libraries", "term": "SPSS (Statistical software \- implicitly used for t-tests)"},

  {"category": "Software & Libraries", "term": "Tequila (Quantum computing package)"},

  {"category": "Software & Libraries", "term": "TEMCenter (JEOL control application)"},

  {"category": "Software & Libraries", "term": "TEMUL Toolkit (Software package)"},

  {"category": "Software & Libraries", "term": "TensorFlow (Deep learning library)"},

  {"category": "Software & Libraries", "term": "Thermo Fisher / FEI (Microscope manufacturer \- Titan, Themis, Helios)"},

  {"category": "Software & Libraries", "term": "Thorlabs (Optics/photonics component supplier)"},

  {"category": "Software & Libraries", "term": "TianGen Biotechnology (RNA extraction kit supplier)"},

  {"category": "Software & Libraries", "term": "Ubuntu (Operating system)"},

  {"category": "Software & Libraries", "term": "Unisoku (STM manufacturer)"},

  {"category": "Software & Libraries", "term": "VASP (Vienna Ab initio Simulation Package) (DFT software)"},

  {"category": "Software & Libraries", "term": "xSPECT/CT (Siemens reconstruction algorithm)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Active learning-driven experimentation"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Adapter system design (MIDA \- for tool integration)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Automated decision-making"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Automated experimentation / workflows"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Autonomous convergence / discovery / optimization / systems"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Bayesian optimization guided exploration"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Causal analysis / inference"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Centralized controller"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Closed-loop control / feedback / processing"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Curiosity-driven experimentation"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Data-driven models / approaches"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Domain-specific hyper-languages (e.g., PyLabRobot)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Explainable AI / Explainability"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Feature identification / extraction"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Few-shot learning (Requires few labeled examples)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Forward modeling (Using simulation to predict experiment)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Generative models (Creating data based on learned patterns)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Guidance weights (Diffusion models)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Guided experimentation / exploration"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Human intervention / Human-in-the-loop (HiL) / Human-augmented"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Hyperparameter optimization / tuning"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Inferential bias (Incorporating physics)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Information theory-based approach"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Integrated data view / analysis"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Interpretability"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Iterative optimization / refinement / training / framework"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Knowledge extraction"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Knowledge-informed framework (Autonomous experimentation)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Landmark identification / pairing (Image registration)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Latent Bayesian optimization (zBO \- guiding hyperparameter search)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Learning from limited / sparse data"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Learning from unlabeled data / Self-distillation"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Low-level vs. High-level decisions (ML vs. Human)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Machine learning guided discovery"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Machine vision automated detection/classification"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Multi-workflow integrated data analysis"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Novelty-based search strategies"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "On-the-fly analysis / decision-making"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Physics-based criteria / constraints / guidance / knowledge / models"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Predictive modeling / models"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Prior information / knowledge guided"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Real-time analysis / feedback / control / detection / monitoring"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Reinforcement learning-enhanced workflows"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Self-driving microscopy"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Semantic segmentation (Providing pixel-level labels)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Similarity-based loss (Affinity-VAE)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Sparse data analytics"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Structural causal model approach"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Supervised learning (Requires labeled data)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Synthetic data generation (GANs, simulation)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Task-based discrimination"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Teaching by Demonstration (Robotics/AI)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Text-to-image synthesis"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Theoretical modeling (General term for using theory)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Theory+AI/ML approach"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Transfer learning (Leveraging pre-trained models/data)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Uncertainty quantification (UQ)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Unsupervised learning (No labeled data required)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "User feedback (Validation)"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Variational Bayesian methods"},

  {"category": "Prompting / Guidance / Interaction Terms", "term": "Weak supervision (Using noisy/limited labels)"}

\]  
