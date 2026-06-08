# **Parametric Shape and Texture Decomposition for Granular Artistic Style Transfer and Editing**

## **I. Introduction: The Quest for Granular Stylistic Control**

The advent of Neural Style Transfer (NST) marked a significant milestone in computational creativity, demonstrating the remarkable ability of deep neural networks to separate and recombine the content of one image with the style of another.1 Seminal works, particularly those by Gatys et al. 1, leveraged feature representations from Convolutional Neural Networks (CNNs) optimized for object recognition, making high-level image information explicit and enabling the transfer of artistic styles.1 These methods typically rely on matching statistical properties of feature maps, such as Gram matrices 1 or channel-wise mean and variance 3, between the content and style images.

However, despite producing visually compelling results, these foundational NST techniques suffer from a fundamental limitation: the style representation is often treated as a "black-box".4 This representation inherently **entangles** various stylistic aspects, primarily shape, texture, and color.4 Consequently, users lack precise control over individual stylistic elements; attempting to modify texture might inadvertently alter color or perceived shape, hindering fine-grained editing and customization.4 Furthermore, much of the early focus in style transfer research centered on appearance attributes like color and texture, often overlooking or neglecting the crucial role of geometric characteristics and shape in defining stylistic identity.8 This entanglement and lack of granular control represent significant barriers, particularly for artists and content creators who require the ability to selectively adopt specific aspects of a reference style while preserving other elements of their original vision, such as meticulously crafted color palettes.6

Recognizing these limitations, subsequent research has pursued the **decomposition** of artistic style into more fundamental, independently controllable components.4 The core motivation is to move beyond monolithic style application towards a paradigm that allows for the separate manipulation of geometric structure (shape) and surface characteristics (texture), often while maintaining the integrity of the image's color composition.4 This pursuit of disentanglement aims to provide the nuanced control necessary for sophisticated artistic expression and editing workflows.

A promising direction in this quest is the **parametric shape and texture decomposition** approach, notably explored by Reimann et al..4 This holistic methodology tackles the entanglement problem head-on by **spatially decomposing** an input artistic image into two distinct layers:

1. A set of **geometric shapes** or primitives representing the coarse structure and layout of the image.4  
2. An overlaying **parametric texture representation** capturing the high-frequency details and painterly attributes.4

This explicit decoupling forms the foundation for enhanced stylistic control. It facilitates interactive geometric abstraction, precise texture manipulation, and the independent adjustment of color and texture properties.4 Crucially, this framework extends to style transfer, allowing the parametric texture representation to be guided by external references, such as other images or descriptive text prompts.4 Furthermore, to overcome the potential latency of optimization-based decomposition, the approach incorporates trained neural networks—Parameter Prediction Networks (PPNs)—to accelerate the process, enabling real-time performance for both single-style and arbitrary-style transfer scenarios.4

This report provides a comprehensive technical examination of the parametric shape and texture decomposition process for style transfer and editing. It will delve into the foundational principles of spatial decomposition, detail the architecture and function of the parametric texture representation via differentiable filters, explain how independent manipulation and style transfer are achieved, discuss acceleration techniques using PPNs, contextualize this approach within the broader landscape of style transfer research, and address its limitations and future potential.

## **II. Foundational Principle: Spatial Decomposition of Artistic Images**

The core innovation underpinning the parametric approach lies in its explicit spatial decomposition of the input artistic image. Instead of treating the image as a monolithic entity or relying solely on global feature statistics, this method separates the visual information into two distinct, conceptually layered components: the underlying coarse structure and the fine-grained texture applied over it.4 This separation of concerns is the cornerstone that enables subsequent independent manipulation and targeted style transfer.4

### **A. Separating Concerns: Coarse Structure vs. Fine-Grained Texture**

The decomposition process begins by analyzing the input image ($I\_t$) to extract its fundamental geometric layout. This results in an intermediate representation, often denoted as the abstracted image ($I\_a$), which captures the coarse shapes and forms present in the artwork.11 This abstracted representation serves as the "canvas" upon which the texture details are subsequently synthesized or manipulated. The high-frequency information, representing the texture, brushwork, surface relief, and other painterly attributes, is then handled by a separate parametric model, as detailed in Section III. This two-stage process 5 (Fig 2\) effectively disentangles the low-frequency structural information from the high-frequency textural details.

### **B. Methods for Geometric Abstraction (Shape Primitives)**

The first stage of the decomposition, responsible for extracting the coarse structure ($I\_a$), can be implemented using various techniques that represent the image geometry through a set of shape primitives.4 The choice of method significantly influences the nature of the geometric abstraction and the resulting stylistic possibilities.

1\. Segmentation-Based Approaches:  
One common approach utilizes image segmentation algorithms to partition the input image into distinct regions or segments.5 Techniques like superpixel segmentation, such as Simple Linear Iterative Clustering (SLIC) 5, group pixels based on color similarity and spatial proximity. This process effectively divides the image into a set of non-overlapping geometric primitives (the superpixels or segments), each typically filled with a uniform color (e.g., the average color of the pixels within the segment).5  
This method excels at representing images characterized by distinct color regions and abstracting away fine-scale details within those regions.11 The level of geometric abstraction becomes an explicitly controllable parameter; adjusting the desired number or average size of the segments directly influences the coarseness of the resulting shape representation.5 Figure 8 in the work by Reimann et al. visually demonstrates how different segmentation methods or parameters yield varying levels of abstraction in the segmented image ($I\_a$).5 This approach naturally aligns with artistic styles that emphasize blocks of color or simplified forms.

2\. Stroke-Based Neural Rendering:  
An alternative, particularly suited for emulating painterly styles, employs stroke-based neural rendering techniques.4 Here, the image's coarse structure is represented as a collection of overlapping or layered primitives that resemble brushstrokes.5 These strokes are defined by parameters controlling their shape (e.g., rectangles, ellipsoids, Bezier curves), size, position, color, and transparency.5 Neural networks are trained to iteratively place or optimize these strokes on a canvas to reconstruct an abstracted version of the input image.5  
Different neural painting methods can be integrated, offering varying degrees of flexibility and speed. For instance, methods like PaintTransformer use fixed primitive shapes for faster rendering and immediate feedback, while others like Neural Painter can optimize more flexible stroke shapes to achieve greater abstraction.11 The parameters governing the strokes—such as their number, size, shape type, and density—provide direct control over the geometric abstraction level and the resulting visual style.5 Figure 1 (D-F) illustrates this variability, showcasing abstractions using rectangular strokes, blocks, and ellipsoids.5

A key aspect of stroke-based approaches is the potential for **joint optimization** of the geometric stroke parameters and the texture parameters (discussed in Section III).5 This allows the strokes and the texture details to be optimized simultaneously to best match a target style or image 5 (Fig 4). However, this joint optimization can introduce challenges. For instance, the texture parameter optimization might attempt to emulate structural details that would be better represented by adding more strokes.4 To mitigate this, optional regularization losses can be employed to constrain parameter optimization primarily to the locations covered by the current set of strokes and to encourage smoother parameter variations within individual strokes.4

The selection between segmentation and stroke-based rendering is therefore not merely a technical implementation detail but carries significant stylistic implications. Segmentation favors region-based abstraction, while stroke-based methods explicitly model the constructive process inherent in many painting styles. Both approaches, however, achieve the primary goal of this stage: producing an abstracted geometric representation ($I\_a$) where the level of simplification is controllable, setting the stage for the subsequent parametric texture modeling.

## **III. Representing Texture in Parametric Space: The Differentiable Filter Pipeline**

Having established the coarse geometric structure ($I\_a$), the second crucial step in the decomposition process is to represent the image's high-frequency details—the texture—in a controllable, parametric manner. This moves beyond the limitations of implicit, entangled style representations found in earlier NST methods 4 and aims for an **explicit parametric decomposition** of textural attributes.5 This is achieved through a novel, lightweight pipeline of differentiable stylization filters.4

### **A. Moving Beyond Black-Box Representations**

Traditional NST methods often capture style through statistical measures of deep features, which, while effective for transfer, lack interpretability and direct editability.1 The parametric approach, in contrast, seeks to define texture through a set of meaningful artistic control variables.5 The core idea is to use a sequence of image processing filters, inspired by traditional Image-Based Artistic Rendering (IB-AR) techniques 5, where each filter controls a specific aspect of the texture, and the parameters of these filters constitute the parametric representation of the texture style.

### **B. Architecture of the Lightweight Differentiable Filter Pipeline (Stage O)**

The texture representation is generated by applying a pipeline of differentiable filters (denoted as Stage O in 11) to the geometrically abstracted image ($I\_a$).5 A key innovation is that these filters, while based on established IB-AR concepts 5, are implemented within an auto-grad enabled framework (e.g., PyTorch).5 This **differentiability** is paramount, as it allows the filter parameters to be optimized using gradient-based methods, enabling both the initial decomposition (fitting parameters to reconstruct the input texture) and subsequent style transfer tasks.5 It also forms the basis for training acceleration networks (PPNs), as discussed in Section VI.

The proposed pipeline is intentionally **lightweight**, typically consisting of only four core filter stages.5 This simplicity contrasts with potentially complex, hand-crafted filter chains used in some traditional IB-AR systems for specific styles.11 The streamlined design enhances parameter editability, reduces redundancy, and makes the relationship between parameters and visual effects more interpretable.4

The specific filters detailed in the work by Reimann et al. 5 are:

1. **(1) Smoothing:** This initial step typically involves Gaussian smoothing followed by a bilateral filter. The bilateral filter is crucial as it smooths regions while preserving significant edges. It has learnable parameters controlling the spatial kernel size ($\\sigma\_d$) and the range (color similarity) kernel size ($\\sigma\_r$). This stage prepares the abstracted shapes for subsequent texture application by reducing minor artifacts from the geometric abstraction stage.  
2. **(2) Edge Enhancement:** An eXtended Difference-of-Gaussians (XDoG) filter is employed to control the appearance of contours and edges. It includes learnable parameters for the amount (strength) and opacity of the detected contours. This allows explicit control over the sharpness and definition within the texture.  
3. **(3) Painterly Attributes:** This stage introduces specific textural effects characteristic of artistic media. The primary example provided is bump mapping implemented using Phong shading to simulate surface relief, mimicking the texture of impasto or oil paint.5 Learnable parameters control the bump scale (intensity of relief), Phong specularity (shininess of highlights), and bump opacity. The framework is flexible, allowing other differentiable painterly filters to be integrated here, such as those simulating wet-in-wet effects or wobbling for watercolor styles.5  
4. **(4) Contrast:** A final filter adjusts the local contrast, controlled by a single learnable parameter. This influences the perceived detail, vibrancy, and dynamic range of the resulting texture.

A critical design consideration is the **preservation of color distribution**. The filters and their learnable parameters are constrained such that they primarily modulate luminance, local contrast, and texture patterns, without altering the underlying color hues derived from the geometric abstraction stage ($I\_a$).5 This ensures that texture can be manipulated largely independently of the base color palette.

### **C. The Role of Parameter Masks (PMs) for Spatial Control**

To allow the texture representation to vary spatially across the image and adapt to the underlying geometric structure, each learnable parameter in the filter pipeline is not a single global value but is controlled by a per-pixel **Parameter Mask (PM)**.5 For instance, there would be a mask controlling the $\\sigma\_d$ parameter of the bilateral filter at every pixel, another mask for the contour amount, one for the bump scale, and so on.

These PMs are the core of the parametric texture representation. They provide the crucial link between the abstract filter parameters and the spatial domain of the image. By allowing parameter values to differ at each pixel, PMs enable fine-grained, localized control over texture attributes.4 This means texture can be made stronger in certain areas, contours emphasized selectively, or surface relief varied based on the underlying shape or other guiding information like depth maps.4

### **D. Optimization: Learning Parameters to Reconstruct Texture**

The initial decomposition process involves finding the optimal set of Parameter Masks (PMs) that allow the filter pipeline (O), when applied to the geometric abstraction ($I\_a$), to best reconstruct the high-frequency details of the original input artistic image ($I\_t$).5 This is framed as an optimization problem.

Thanks to the differentiability of the entire pipeline, gradient descent can be used to minimize a **decomposition loss function ($L$)**.11 This loss typically combines:

* A **target loss ($L\_{target}$):** Measures the difference between the pipeline's output ($I\_o \= O(I\_a, PM)$) and the original input image ($I\_t$). Common choices include the $\\ell\_1$ norm or perceptual losses.11 This term drives the parameters to capture the input texture accurately.  
* A **Total Variation loss ($L\_{TV}$):** Applied to the parameter masks themselves, this regularization term encourages spatial smoothness and reduces noise within the PMs, making them more coherent and interpretable.11 Figure 3 in 5 visually contrasts PMs optimized with and without $L\_{TV}$, showing the latter are significantly noisier.

By minimizing this combined loss, the optimization process effectively "learns" the parameter masks that encode the input image's texture within the structured, interpretable framework of the differentiable filter pipeline. This resulting set of optimized PMs, along with the geometric abstraction $I\_a$, constitutes the decomposed representation of the artistic image.

## **IV. Enabling Independent Manipulation: Editing Shape and Texture**

The primary advantage of spatially decomposing an image into geometric shapes ($I\_a$) and a parametric texture representation (PMs) is the ability to manipulate these components independently, offering a level of control difficult to achieve with entangled representations.4 This transforms image editing from direct pixel manipulation or the application of global filters into a more semantic process, operating on distinct layers of abstraction and interpretable attributes.

### **A. Modifying Geometric Abstraction**

The coarse structure of the image, captured in the geometric abstraction stage ($I\_a$), can be directly edited by adjusting the parameters of the chosen segmentation or stroke-based rendering method used in Stage S.5 For instance:

* If using superpixel segmentation, changing the target number of superpixels alters the level of detail and the granularity of the shape primitives.5 Merging or splitting segments can modify the layout.  
* If using stroke-based rendering, modifying the number, density, size, or type (e.g., switching from rectangles to ellipsoids) of the strokes directly changes the underlying structure and the painterly feel of the abstraction.5 Figure 1 (D-F) provides visual examples of varying geometric abstraction primitives.5

These modifications adjust the fundamental building blocks of the image's structure before the texture is applied, allowing users to control the overall level of abstraction or change the primitive shapes used to represent the content.

### **B. Fine-Tuning Painterly Attributes via Texture Parameters**

Once the image is decomposed, the texture, encoded in the Parameter Masks (PMs), can be edited independently of the geometry.4 This allows for fine-tuning of specific painterly attributes:

* **Global Edits:** Users can apply uniform adjustments across an entire parameter mask. For example, globally increasing the values in the bump-map scale PM would enhance the overall surface relief across the image, making an oil paint effect appear thicker or more pronounced 5 (Fig 10). Similarly, globally adjusting the contour opacity PM can strengthen or soften edges throughout the image. Figure 1 (A) shows an example where oiliness and stroke thickness are enhanced via parameter adjustments.5  
* **Local Edits:** The per-pixel nature of PMs enables spatially localized texture editing.4 Users could manually paint onto a specific PM (e.g., the contrast mask) to increase texture vibrancy only in certain areas. Alternatively, PM values can be interpolated or modulated based on external guiding information, such as image saliency maps (to enhance texture in important regions) or depth maps (to make texture vary with distance, as shown in Figure 7 5).4 This local control offers significantly more flexibility than traditional style transfer methods that apply style uniformly.

### **C. Maintaining Color Fidelity**

A key design goal and outcome of this decomposition is the ability to manipulate texture and shape largely independently of color.4 The base colors are primarily determined by the geometric abstraction stage ($I\_a$), where segments or strokes are assigned colors based on the input image.11 The subsequent differentiable filter pipeline is designed to primarily affect luminance, contrast, and high-frequency patterns associated with texture, without fundamentally altering the color hues.5

This separation allows for workflows not easily achievable otherwise. For example, if a standard NST algorithm produces artifacts like incorrect colors in certain regions, the parametric decomposition approach can be used to correct them. One could adjust the colors of the corresponding segments in the geometric abstraction ($I\_a$) and then reapply the desired texture using the filter pipeline (potentially accelerated by a PPN) to adapt the texture details to the corrected colors.11 This preserves the desired texture style while fixing the color issues, demonstrating the practical utility of disentangling color from texture manipulation.

## **V. Parametric Style Transfer: Guiding Decomposition with External References**

Beyond editing the intrinsic style of an input image, the parametric decomposition framework provides a powerful mechanism for **style transfer**, adapting the texture representation to match external stylistic references. Instead of optimizing the Parameter Masks (PMs) to reconstruct the input image's texture, the optimization target is shifted to match the characteristics of a reference style, provided either as an image or a text prompt.4 This reframes style transfer as an optimization problem conducted within the constrained, interpretable parametric space defined by the differentiable filter pipeline.4

### **A. General Principle**

The core idea remains the same: optimize the PMs that control the filter pipeline (O). However, the loss function is now designed to measure the similarity between the pipeline's output ($I\_o \= O(I\_a, PM)$) and the desired target style, rather than the original input texture. The geometric abstraction ($I\_a$) derived from the *content* image provides the structural foundation, ensuring that the transferred style conforms to the content's layout.4 The optimization tunes the texture parameters (PMs) to imbue this structure with the desired stylistic attributes.

### **B. Image-Guided Transfer**

When the target style is provided as a reference image ($I\_s$), the optimization utilizes style loss functions derived from traditional NST.4 These losses quantify the difference in stylistic features between the generated image ($I\_o$) and the style reference ($I\_s$). Common choices include:

* **Gram Matrix Loss:** Measures differences in the correlations between feature channels in different layers of a pre-trained CNN (e.g., VGG).1 This was used in the PPNsst training.5  
* **Channel-wise Statistics Loss (e.g., AdaIN Loss):** Matches the mean and variance of feature channels.3 This was used in the PPNarb training.5  
* **Advanced NST Losses:** More sophisticated losses like STROTTS (Self-Transport Style Transfer) 5 can also be employed for re-optimizing parameters to a new texture style after initial decomposition, as demonstrated in Figure 5\.5

The optimization process adjusts the PMs to minimize the chosen style loss. This effectively translates the texture characteristics of the reference image ($I\_s$) into the parametric space of the filter pipeline, applying that style to the content structure ($I\_a$).5 A notable strength of this approach is its ability to adapt the transferred texture patterns to align cohesively with the underlying coarse shapes provided by $I\_a$, achieving a spatially homogeneous appearance.4

### **C. Text-Guided Transfer**

The framework also supports style transfer guided by natural language text prompts, leveraging the power of joint text-image embedding models like CLIP (Contrastive Language-Image Pre-training).4 Instead of a style image, the user provides a textual description of the desired style (e.g., "starry night," "impressionistic painting," "Tetris blocks") 5 (Fig 1, 6).

The optimization then minimizes a CLIP-based loss function, measuring the similarity (or distance) between the CLIP embedding of the generated image ($I\_o$) and the CLIP embedding of the text prompt.4 Techniques adapted from methods like CLIPstyler, such as patch-based losses (comparing embeddings of image patches) and directional losses (aligning the direction of change in embedding space), can be used.5

An interesting aspect of text-guided transfer within this framework is that explicit content preservation losses (often needed in general text-to-image models to prevent divergence from the input) are frequently unnecessary.5 The filter pipeline itself, operating on the pre-computed geometric abstraction ($I\_a$), inherently preserves the major content structures and color distribution.5 This structural constraint provided by the pipeline acts as a strong prior, allowing the CLIP loss to focus primarily on optimizing the texture parameters (PMs) to match the *stylistic* aspects described in the text prompt. This potentially leads to more predictable and controlled stylization compared to less constrained generative models guided solely by CLIP, reducing the risk of unwanted content alterations. Visual examples of text-guided transfer are shown in Figure 1 (B-C) and Figure 6\.5

### **D. Illustrative Examples**

The efficacy of parametric style transfer is demonstrated through various visual results presented by Reimann et al..5 Figure 1 shows texture modifications driven by text prompts like "starry night" and "impressionistic painting." Figure 5 illustrates parameter retargeting using image-based style transfer (STROTTS loss). Figure 6 showcases results from text-based re-optimization using prompts like "Tetris." Figure 12 provides comparisons with other text-based stylization methods, while Figure 13 compares against image-based methods focusing on color preservation. These examples collectively highlight the framework's versatility in adopting diverse styles from both image and text references within the parametric space.

## **VI. Acceleration via Parameter Prediction Networks (PPNs)**

While the optimization-based approach for decomposition and style transfer offers fine-grained control, the iterative nature of gradient descent can be computationally intensive, potentially taking several seconds or even minutes per image.5 This latency can hinder usability, especially in interactive editing scenarios.4 To address this bottleneck, the parametric decomposition framework incorporates **Parameter Prediction Networks (PPNs)**—feed-forward neural networks trained to directly predict the optimal Parameter Masks (PMs) in a single inference pass.4

### **A. Motivation: Overcoming Optimization Latency**

The goal of PPNs is to replace the time-consuming optimization step with a fast network inference. By learning a direct mapping from input(s) to the desired PMs, PPNs can achieve real-time or near-real-time performance, making interactive style decomposition and transfer feasible.5 For instance, timings reported suggest optimization might take around 11.45 seconds for a 256x256 image, whereas PPN inference takes approximately 0.20 seconds (or even less if pre-processing time is excluded).5

### **B. Parameter Prediction Networks (PPNs): The Concept**

PPNs essentially perform a form of **knowledge distillation**. They are trained using data generated by the slower, optimization-based methods or other existing style transfer networks. The PPN learns to approximate the complex mapping discovered through optimization, encoding that knowledge into its network weights for rapid execution.5 The network architecture is typically adapted from standard image-to-image translation networks, with the final layer modified to output the required number of parameter masks (\#PM) for the differentiable filter pipeline.5 Two main types of PPNs are proposed, catering to different use cases.

### **C. Single-Style PPNs (PPNsst)**

* **Purpose:** Designed for real-time decomposition into a *specific, pre-defined* artistic style.5 This is useful when integrating a particular style deeply into an editing tool or application.  
* **Training:** PPNsst is trained using a single target style image ($I\_s$). Ground truth stylized images ($I\_r$) are generated by applying a pre-trained single-style transfer network (SSTN, e.g., from Johnson et al.), trained specifically on $I\_s$, to various content images. These content images are first passed through the geometric segmentation stage (S) to produce the input ($I\_a$) for the PPNsst. The network is trained to predict the PMs that, when fed into the filter pipeline (O) with $I\_a$, produce an output ($I\_o$) matching the target style. The training loss typically combines a Gram matrix style loss ($L\_{gram}(I\_o, I\_s)$) to match the target style statistics and a content loss ($L\_c(I\_o, I\_r)$) using VGG features to ensure the output resembles the structure of the SSTN-generated image.5  
* **Benefit:** Once trained, PPNsst takes only the segmented content image ($I\_a$) as input and instantly outputs the PMs for that specific style. This extreme efficiency (\~0.08-0.20s 5) enables real-time workflows, such as interactively adjusting colors in the segmented image ($I\_a$) and having the PPNsst instantly re-predict the texture parameters to adapt the style to the new colors.11 Figure 11 demonstrates using a PPN to correct NST artifacts by re-applying texture details after color adjustments.5

### **D. Arbitrary-Style PPNs (PPNarb)**

* **Purpose:** Enables real-time style transfer decomposition from *any arbitrary* style image provided by the user at runtime.4  
* **Training:** PPNarb requires training on a large dataset of diverse style images (e.g., from WikiArt) and content images (e.g., from MS-COCO). Stylized ground truth images ($I\_r$) are generated using a pre-trained arbitrary style transfer network (e.g., SANet) for content-style pairs. The input to PPNarb consists of both the segmented content image ($I\_a$) and the target style image ($I\_s$). The network architecture is often adapted from the underlying arbitrary style transfer network (like SANet), modified to output the PMs. The training loss typically combines an AdaIN style loss ($L\_{AdaIN}(I\_o, I\_s)$) to match the style statistics of $I\_s$ and a content loss ($L\_c(I\_o, I\_r)$) to maintain similarity to the SANet output structure. Structure-preserving identity losses used in some arbitrary NST training might be omitted here, as the filter pipeline inherently offers some content preservation.5  
* **Benefit:** PPNarb provides the flexibility of arbitrary style transfer without the latency of optimization. At inference time, it takes the content structure ($I\_a$) and any user-provided style image ($I\_s$) and predicts the corresponding PMs in near real-time, achieving speeds comparable to PPNsst.5

The development of both PPNsst and PPNarb significantly broadens the applicability of the parametric decomposition approach. PPNsst allows for highly optimized integration of fixed styles, while PPNarb offers versatile, on-the-fly stylization, both bridging the gap between detailed parametric control and the demand for interactive performance.

## **VII. Contextualizing Parametric Decomposition within Style Transfer Research**

The parametric shape and texture decomposition method occupies a distinct position within the diverse landscape of style transfer and image manipulation research. Understanding its relationship to other prominent paradigms helps clarify its unique contributions and trade-offs. It offers a middle ground between the statistical matching of classical NST and the latent space manipulations of recent generative models, focusing on explicit spatial decomposition and interpretable filter parameters.

### **A. Comparison with Classical NST (Gatys, AdaIN, WCT)**

* Gatys et al. 1: The original NST algorithm relies on slow, iterative optimization of image pixels to match content and style features.3 While foundational, it suffers from speed limitations and produces entangled style representations where color, texture, and structure are intertwined. The parametric method improves on this by offering an explicit, editable parametric representation, significantly faster execution via PPNs, and better disentanglement of style components.4  
* AdaIN (Adaptive Instance Normalization) 3: This technique enabled the first real-time arbitrary style transfer by aligning the channel-wise mean and variance of content features with those of style features in a feed-forward network. While fast and effective for global style transfer, AdaIN offers limited control beyond these second-order statistics. It primarily captures overall color palettes and texture distributions.3 Furthermore, as it operates on global statistics, it may struggle with preserving fine local details or preventing subtle content leakage from the style image.3 The parametric method provides more granular control via spatially varying PMs and aims for more explicit disentanglement. Notably, AdaIN's core idea of matching statistics remains relevant, serving as a loss function component in the training of the arbitrary-style PPN (PPNarb) 5 and appearing in recent diffusion-based methods like D2Styler.12  
* WCT (Whitening and Coloring Transform) 6: WCT-based methods also match feature statistics (covariance matrices) to transfer style, often applied recursively across multiple layers. While capable of transferring complex patterns, they can sometimes introduce content distortion or unwanted artifacts.13 The parametric approach, with its explicit separation of structure ($I\_a$) and texture (filter pipeline), aims for better content preservation during texture manipulation. Interestingly, the concept of whitening and coloring transformations has seen a resurgence in recent diffusion-based disentanglement methods (e.g., RegWCT in SADis 6).

### **B. Comparison with Recent Diffusion-Based Disentanglement**

A significant recent trend involves using large-scale pre-trained diffusion models for style transfer and disentanglement.6 Methods like SADis 6, StyleDiffusion 15, and ProSpect 14 leverage the powerful generative capabilities of these models, often guided by CLIP embeddings.

* **Mechanism:** These approaches typically achieve disentanglement by manipulating representations within the **latent feature space** of the diffusion model or CLIP. For example, SADis isolates color and texture representations in the CLIP embedding space through feature subtraction and SVD rescaling.6 Others manipulate attention layers (query, key, value vectors) to inject style while preserving content structure.14  
* **Key Difference:** This contrasts sharply with the parametric method's **explicit spatial decomposition** into geometric primitives and control via a **parametric filter pipeline**. Diffusion methods operate implicitly within high-dimensional latent spaces, while the parametric method uses a more structured, physically inspired representation (shapes \+ filters).  
* **Control:** Diffusion-based methods offer control via text prompts or reference images, often aiming for "tuning-free" operation.6 However, the control mechanism involves manipulating latent codes or attention maps, which may be less directly interpretable than adjusting specific filter parameters (e.g., contour strength, bump scale) in the parametric approach. The constrained nature of the parametric filter pipeline might also offer more predictable behavior regarding content preservation compared to the vast generative space of diffusion models.5

### **C. Comparison with Geometry-Focused Stylization**

Recognizing that style encompasses more than just color and texture, other research lines focus specifically on stylizing the **geometry** or shape of objects, particularly in 3D.

* Method (e.g., Geometry Transfer 8): This work explicitly targets transferring geometric style characteristics, using depth maps from a style image to guide the deformation of 3D representations like neural radiance fields (NeRFs).8  
* **Contrast:** While the parametric decomposition method includes a geometric abstraction stage ($I\_a$), its primary focus is on representing 2D coarse shapes (segments or strokes) as a basis for applying parametric texture. Geometry Transfer, conversely, directly manipulates the 3D shape itself based on stylistic geometric cues.  
* **Complementarity:** Both geometry-focused stylization 8 and parametric texture/shape decomposition 4 address aspects of style often neglected by classical NST.8 They represent parallel efforts to achieve more comprehensive stylistic control, one focusing on 3D shape deformation, the other on 2D structure and parametric surface detail.

### **D. Comparative Analysis Table**

To summarize the key distinctions, the following table provides a high-level comparison of these different style transfer and disentanglement paradigms:

| Feature | Classical NST (Gatys) | Fast Feed-Forward (AdaIN) | Parametric Decomposition (Reimann et al.) | Diffusion Disentanglement (e.g., SADis) | Geometry Transfer (Jung et al.) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Key Technique** | Iterative pixel optimization matching deep feature stats | Feed-forward network aligning channel mean/variance | Spatial decomposition \+ Differentiable filter pipeline | Latent space manipulation in diffusion/CLIP models | Geometric deformation guided by depth maps (often 3D) |
| **Disentangled Elements** | Poor (Entangled) | Poor (Global stats) | Shape (Geometric Primitives) & Texture (Parametric Filters) | Color & Texture (in latent space), Style & Content | Shape/Geometry & Appearance (Color/Texture) |
| **Control Mechanism** | Loss weights | Content-style trade-off parameter | Geometric params, Filter params (via PMs) | Text prompts, Reference images (latent manipulation) | Style template (RGB-D), Deformation fields |
| **Style Input** | Style Image | Style Image | Style Image, Text Prompt | Style Image(s), Text Prompt | Style Image (RGB-D) |
| **Real-time Capability** | No | Yes | Yes (with PPNs) | Yes (Diffusion inference) | Depends on implementation (NeRF can be slow) |
| **Key Strengths** | Foundational concept | Real-time arbitrary transfer | Explicit disentanglement, Interpretable texture params, Local control, Color fidelity | High-quality generation, Leverages large models, Tuning-free options | Explicit geometric stylization, 3D consistency |
| **Key Limitations** | Slow, Entangled, Global | Global stats only, Limited control | Potential alignment issues, Parameter specificity limits | Latent control less interpretable, Relies on large models | Primarily 3D, Requires depth/geometry info |
| **Relevant Sources** | 1 | 3 | 4\-11 | 6,10 | 8 |

This comparison highlights the unique niche occupied by parametric decomposition. It provides a structured, interpretable approach to disentanglement through spatial separation and explicit filter parameters, offering a different control paradigm compared to both earlier statistical methods and more recent latent manipulation techniques.

## **VIII. Limitations and Future Research Avenues**

Despite its significant advantages in providing granular control and disentanglement, the parametric shape and texture decomposition method is not without limitations, which also point towards avenues for future research.

### **A. Identified Failure Modes**

The originators of the method acknowledge certain failure cases, providing valuable insights into the current boundaries of the technique 5:

* **Alignment Issues between Geometry and Texture:** A potential conflict can arise between the geometric primitives defined in the first stage ($I\_a$) and the stylistic goals driving the texture optimization in the second stage (O). Figure 16 illustrates this: tilted rectangular strokes are used for geometric abstraction, but the text prompt "Tetris" guides the filter pipeline to render straight rectangles, effectively overdrawing the initial stroke boundaries.5 This suggests that the losses guiding shape abstraction and texture stylization might sometimes diverge, leading to inconsistencies where the texture filter attempts to "correct" the underlying geometry to better match the target style. This points to challenges in ensuring perfect harmony in joint optimization or sequential application when shape and texture cues in the target style are strongly coupled or conflicting. The need for stroke regularization losses to prevent texture parameters from emulating structure also hints at this potential tension.4  
* **Parameter Interpretability and Specificity:** While the filter parameters are designed to correspond to interpretable artistic attributes, their effects might not always be perfectly isolated or predictable. Figure 17 shows an example where increasing the contour opacity parameter mask does not just enhance contours but also leads to a general darkening of the image.5 Conversely, reducing the opacity fails to remove all contours entirely. This indicates that, under certain conditions, parameters might exhibit "overuse" or unintended side effects, suggesting imperfect disentanglement *within* the filter parameter space itself.5 Achieving truly orthogonal controls, where adjusting one parameter has absolutely no effect on the domain of another, remains a challenging goal.

### **B. Opportunities for Enhancement**

These limitations suggest several directions for future work to enhance the robustness, capabilities, and applicability of parametric decomposition:

* **Improving Filter Parameter Semantics:** Research could focus on designing filter pipelines or parameterization schemes where the controls are even more semantically meaningful, orthogonal, and robust across diverse image content and styles. This might involve exploring alternative filter designs or incorporating learned priors about artistic techniques.  
* **Advanced Geometric Abstraction and Joint Optimization:** Developing more sophisticated methods for geometric abstraction or refining the strategies for joint optimization of shape (strokes) and texture parameters could mitigate alignment issues. This might involve incorporating higher-level semantic understanding into the abstraction process or designing loss functions that better balance geometric fidelity and textural stylization.  
* **Extending Parametric Representations:** The current filter pipeline focuses on a specific set of painterly attributes (contours, relief, contrast). Future work could extend the parametric representation to encompass a wider range of artistic effects, such as simulating different media (watercolor, charcoal), capturing more complex brushwork patterns, or handling transparency and layering more explicitly.  
* **Extension to 3D:** While the current method focuses on 2D images, exploring extensions to 3D scenes (e.g., applying parametric textures to 3D models or NeRFs) could be a valuable direction, potentially complementing geometry-focused stylization techniques.  
* **Hybrid Approaches:** Combining the strengths of parametric decomposition with other paradigms could yield powerful hybrid models. For instance, using diffusion models to generate initial geometric abstractions or to propose parameter masks, which are then refined within the interpretable parametric framework, could offer a blend of generative power and fine-grained control.

Addressing these areas could further solidify parametric decomposition as a versatile and powerful tool for computational art generation and editing.

## **IX. Conclusion: The Power of Parametric Decomposition for Artistic Control**

The development of parametric shape and texture decomposition represents a significant advancement in the field of neural style transfer and computational art. By moving beyond the entangled, black-box representations of earlier methods, this approach offers a more structured, controllable, and interpretable framework for manipulating the visual style of images.

### **A. Recap of Benefits**

The core strength of this methodology lies in its explicit **spatial decomposition** of an image into coarse geometric shapes and a parametric representation of high-frequency texture details.4 This fundamental separation enables several key advantages:

* **Disentanglement and Independent Control:** It facilitates the independent manipulation of geometric abstraction, texture attributes, and color, overcoming a major limitation of traditional NST.4  
* **Granular and Interpretable Editing:** The use of a differentiable filter pipeline with explicitly defined parameters (controlled spatially via Parameter Masks) allows for fine-grained global and local adjustments to specific painterly attributes like contours, surface relief, and contrast.4  
* **Flexible Style Guidance:** The parametric texture representation can be optimized to match styles defined by either reference images (using NST losses) or natural language text prompts (using CLIP losses), offering versatility in style input.4  
* **Real-Time Performance:** The introduction of Parameter Prediction Networks (PPNs) effectively overcomes the latency of optimization, enabling real-time decomposition and style transfer for both specific pre-defined styles (PPNsst) and arbitrary user-provided styles (PPNarb).4

### **B. Impact on Creative Workflows**

This shift towards disentangled, parametric control has profound implications for creative workflows. It empowers both artists and casual creators with tools that align more closely with traditional artistic thinking, where images are often constructed through layers of structure and surface detail.4 The ability to interactively explore variations in geometric abstraction or fine-tune specific texture elements provides a more intuitive and expressive means of achieving a desired artistic vision compared to wrestling with entangled, unpredictable style representations.4 Furthermore, the framework's utility extends to practical tasks like correcting artifacts in images generated by other methods, demonstrating its value in professional post-processing pipelines.11

### **C. Final Thought**

Parametric shape and texture decomposition marks a crucial step in bridging the gap between the conceptual approaches of human artists and the computational power of neural networks for style manipulation. By providing a framework that explicitly separates structure from detail and represents texture through interpretable parameters, it offers a pathway towards more controllable, predictable, and ultimately more creative computational art tools. While challenges remain in perfecting the disentanglement and expanding the range of representable styles, this paradigm points towards a future where digital style transfer and editing become increasingly nuanced and artistically empowering.

#### **Works cited**

1. Image Style Transfer Using Convolutional Neural Networks \- The Computer Vision Foundation, accessed on May 3, 2025, [https://www.cv-foundation.org/openaccess/content\_cvpr\_2016/papers/Gatys\_Image\_Style\_Transfer\_CVPR\_2016\_paper.pdf](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)  
2. Style Transfer by Rigid Alignment in Neural Net Feature Space \- CVF Open Access, accessed on May 3, 2025, [https://openaccess.thecvf.com/content/WACV2021/papers/Hada\_Style\_Transfer\_by\_Rigid\_Alignment\_in\_Neural\_Net\_Feature\_Space\_WACV\_2021\_paper.pdf](https://openaccess.thecvf.com/content/WACV2021/papers/Hada_Style_Transfer_by_Rigid_Alignment_in_Neural_Net_Feature_Space_WACV_2021_paper.pdf)  
3. openaccess.thecvf.com, accessed on May 3, 2025, [https://openaccess.thecvf.com/content\_ICCV\_2017/papers/Huang\_Arbitrary\_Style\_Transfer\_ICCV\_2017\_paper.pdf](https://openaccess.thecvf.com/content_ICCV_2017/papers/Huang_Arbitrary_Style_Transfer_ICCV_2017_paper.pdf)  
4. Artistic style decomposition for texture and shape editing, accessed on May 3, 2025, [https://d-nb.info/1342547381/34](https://d-nb.info/1342547381/34)  
5. Artistic style decomposition for texture and shape editing \- ResearchGate, accessed on May 3, 2025, [https://www.researchgate.net/publication/381881166\_Artistic\_style\_decomposition\_for\_texture\_and\_shape\_editing](https://www.researchgate.net/publication/381881166_Artistic_style_decomposition_for_texture_and_shape_editing)  
6. Free-Lunch Color-Texture Disentanglement for Stylized Image Generation \- arXiv, accessed on May 3, 2025, [https://arxiv.org/html/2503.14275v2](https://arxiv.org/html/2503.14275v2)  
7. Dr. Amir Semmo \- Portfolio, accessed on May 3, 2025, [http://amirsemmo.de/](http://amirsemmo.de/)  
8. CVPR Poster Geometry Transfer for Stylizing Radiance Fields, accessed on May 3, 2025, [https://cvpr.thecvf.com/virtual/2024/poster/31418](https://cvpr.thecvf.com/virtual/2024/poster/31418)  
9. Paper Digest: Recent Papers on Style Transfer, accessed on May 3, 2025, [https://www.paperdigest.org/2020/06/recent-papers-on-style-transfer/](https://www.paperdigest.org/2020/06/recent-papers-on-style-transfer/)  
10. arXiv:2503.14275v1 \[cs.CV\] 18 Mar 2025, accessed on May 3, 2025, [https://arxiv.org/pdf/2503.14275](https://arxiv.org/pdf/2503.14275)  
11. (PDF) Controlling Geometric Abstraction and Texture for Artistic ..., accessed on May 3, 2025, [https://www.researchgate.net/publication/372827298\_Controlling\_Geometric\_Abstraction\_and\_Texture\_for\_Artistic\_Images](https://www.researchgate.net/publication/372827298_Controlling_Geometric_Abstraction_and_Texture_for_Artistic_Images)  
12. D2Styler: Advancing Arbitrary Style Transfer with Discrete Diffusion Methods, accessed on May 3, 2025, [https://www.researchgate.net/publication/382944300\_D2Styler\_Advancing\_Arbitrary\_Style\_Transfer\_with\_Discrete\_Diffusion\_Methods](https://www.researchgate.net/publication/382944300_D2Styler_Advancing_Arbitrary_Style_Transfer_with_Discrete_Diffusion_Methods)  
13. Style Transfer by Rigid Alignment in Neural Net Feature Space \- UC Merced, accessed on May 3, 2025, [https://faculty.ucmerced.edu/mcarreira-perpinan/papers/1909.13690.pdf](https://faculty.ucmerced.edu/mcarreira-perpinan/papers/1909.13690.pdf)  
14. (PDF) Multi-Source Training-Free Controllable Style Transfer via Diffusion Models, accessed on May 3, 2025, [https://www.researchgate.net/publication/388994284\_Multi-Source\_Training-Free\_Controllable\_Style\_Transfer\_via\_Diffusion\_Models](https://www.researchgate.net/publication/388994284_Multi-Source_Training-Free_Controllable_Style_Transfer_via_Diffusion_Models)  
15. CVPR Poster Style Injection in Diffusion: A Training-free Approach for Adapting Large-scale Diffusion Models for Style Transfer, accessed on May 3, 2025, [https://cvpr.thecvf.com/virtual/2024/poster/30345](https://cvpr.thecvf.com/virtual/2024/poster/30345)  
16. Morpheus: Text-Driven 3D Gaussian Splat Shape and Color Stylization \- GitHub Pages, accessed on May 3, 2025, [https://nianticlabs.github.io/morpheus/resources/Morpheus.pdf](https://nianticlabs.github.io/morpheus/resources/Morpheus.pdf)