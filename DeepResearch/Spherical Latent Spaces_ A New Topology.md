

# **The Sphere of Possibility: Navigating Continuous Variation in Generative Latent Spaces**

---

## **Introduction: From Categories to Continua**

In the pursuit of organizing and understanding the world, human cognition has long relied on the power of categorization. We place music into genres, art into movements, and emotions into discrete boxes labeled "happy," "sad," or "angry." This categorical framework, while useful for communication and classification, fundamentally misrepresents the fluid, continuous nature of reality. The transition from rock to jazz is not an abrupt leap but a spectrum of intermediate styles; the shift from joy to melancholy is a gentle, nuanced blend. Traditional data science and machine learning have often mirrored this categorical approach, training models to place data into predefined, mutually exclusive bins. This report details a paradigm shift away from this rigid worldview, exploring a concept that replaces the "boxes" of classification with a continuous, navigable "globe" of variation: the spherical latent space.

The central metaphor is powerful and intuitive. Imagine a globe where every point on its surface represents a unique artistic style, a specific emotional tone, or a distinct musical motif. Neighboring points on this globe are gentle blends of one another. To transition from one style to another, one does not jump from box to box but simply rotates the orb, tracing a smooth, continuous path across its surface. This topological perspective reframes diversity not as a collection of separate items but as a connected, explorable landscape. It suggests a world where variations are not exceptions to be classified but inherent, navigable features of a unified whole. This conceptual shift encourages the design of entirely new kinds of interactive systems—interfaces, playlists, or digital exhibitions that empower users to explore a fluid world of possibilities rather than merely selecting from a static menu of categories.

This report will demonstrate that the spherical latent space is more than just a compelling metaphor; it is a technically robust and increasingly vital framework at the convergence of two cutting-edge fields: deep generative modeling and non-Euclidean geometry. Deep generative models, such as Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs), have provided the tools to learn compressed, meaningful representations of complex data. Simultaneously, the application of non-Euclidean geometry provides the mathematical language to structure these representations in ways that are more stable, more expressive, and more aligned with the intrinsic structure of the data itself. By curving the abstract space of features into a sphere, we unlock profound technical advantages and open up new frontiers for human-computer interaction and creative expression. This document provides an exhaustive analysis of this paradigm, from its foundational principles in machine learning to its geometric underpinnings and its transformative potential for designing the next generation of creative and exploratory tools.

---

## **Section 1: The Latent Space as a Compressed Reality**

Before exploring the unique properties of a spherical topology, it is essential to first establish a firm understanding of the foundational concept upon which it is built: the latent space. In machine learning, a latent space is a compressed, abstract representation of data that distills high-dimensional complexity into a lower-dimensional, more meaningful form. It is a learned "map" of reality, capturing not the superficial details but the essential, underlying structure that governs the data.

### **1.1 Encoding the Essence: The Foundation of Latent Space**

At its core, a latent space is the product of dimensionality reduction, a process that compresses data while preserving its most important characteristics.1 Consider a high-resolution digital image. It may be composed of millions of pixels, each representing a dimension in a vast and computationally unwieldy space. However, the perceptually meaningful information—the objects, textures, and composition—is defined by a much smaller set of core features. A machine learning model, through a process called encoding, learns to map the raw, high-dimensional data point (e.g., the pixel grid) to a vector in a much lower-dimensional latent space.3 This vector is known as an "embedding," and it represents the original data point in this new, compressed coordinate system.1

This process is more sophisticated than simple data compression. The model learns to discard irrelevant or redundant information, retaining only the features that are most salient for a given task, such as classification or generation.1 For instance, when classifying images of faces, a model might learn that the precise pixel value in the background is irrelevant, but the relative positions of the eyes, nose, and mouth are critical. The resulting latent space is therefore a compressed version of the initial

*feature space*, containing only the subset of features identified as most relevant to the data's underlying structure.1

The dimensions of this latent space correspond to what are known as "latent variables." These are the underlying, often unobservable, characteristics that inform how the data is structured and distributed.1 For a dataset of faces, these latent variables might correspond to intuitive attributes like age, gender, hair color, direction of lighting, or the degree of a smile. The process of creating a latent space, then, is not merely a technical exercise in data reduction. It is a form of automated, unsupervised representation learning, where the model attempts to discover the fundamental "factors of variation" within the data.2 It seeks to build a model of the data's generative process, uncovering the hidden axes along which the data naturally and meaningfully varies. This reframes the latent space from a simple computational artifact into a learned model of reality's essential components.

### **1.2 Learning to Generate: VAEs and GANs**

The construction of these powerful latent spaces is primarily accomplished through deep generative models, most notably Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs).3 These models do not just learn to represent data; they learn to generate new data that resembles the original training set, and in doing so, they impose a meaningful structure on the latent space.

A **Variational Autoencoder (VAE)** consists of two interconnected neural networks: an encoder and a decoder.4 The encoder takes a high-dimensional data point as input and maps it not to a single point in the latent space, but to the parameters of a probability distribution—typically a mean vector (

μ) and a standard deviation vector (σ).1 A point is then sampled from this distribution to create the latent representation. The decoder takes this latent point and attempts to reconstruct the original input data. By training the model to minimize the reconstruction error while also ensuring the learned distributions in the latent space are close to a predefined prior distribution (e.g., a standard normal distribution), the VAE learns a latent space with two critical properties for navigation:

1. **Continuity:** Nearby points in the latent space, when passed through the decoder, produce similar, smoothly varying outputs.1  
2. **Completeness:** Any point sampled from the latent space's distribution, when decoded, should yield meaningful and realistic content.1

This probabilistic approach, which maps inputs to "soft ellipsoidal regions" rather than discrete points, forces the latent space to be densely populated and smooth, making it ideal for interpolation and exploration.7

A **Generative Adversarial Network (GAN)** employs a different strategy based on a two-player game.3 It consists of a generator and a discriminator. The generator takes a random vector from a simple prior distribution (e.g., a multi-dimensional Gaussian) and attempts to transform it into a realistic data sample. The discriminator is trained to distinguish between real data samples from the training set and the "fake" samples produced by the generator. Through this adversarial process, the generator becomes progressively better at producing realistic outputs, while the discriminator becomes better at detecting fakes. In doing so, the generator implicitly learns a mapping from the simple, unstructured prior distribution to the complex, high-dimensional manifold of the real data, thereby inducing a meaningful structure on its latent space.8

In many state-of-the-art systems, these approaches are combined in a two-stage process. First, an autoencoder is trained to learn a compact and high-fidelity latent representation of the data. Then, a powerful generative model, such as a diffusion model, is trained not on the raw data itself, but directly on these latent representations.9 This modular strategy is computationally efficient and allows the generative model to focus its capacity on modeling the essential semantic variations of the data, rather than wasting it on imperceptible, high-frequency details.9

### **1.3 The Euclidean Assumption and Its Limits**

Implicit in the design of most standard VAEs and GANs is a crucial geometric assumption: that the latent space is **Euclidean**. This means the latent space is modeled as a flat, multi-dimensional Cartesian space, akin to the familiar 2D plane or 3D space of classical geometry, but extended to many more dimensions.10 This assumption is convenient and computationally straightforward; distances are measured with the Pythagorean theorem, and straight lines are the shortest paths between points.12

However, the real world is rarely so simple. Many datasets possess intrinsic structures that are fundamentally non-Euclidean.13 For example:

* **Cyclical Data:** Concepts like the color wheel, the cycle of seasons, or a spectrum of emotions that loop back on themselves are difficult to represent on a flat plane without creating artificial seams or discontinuities.  
* **Hierarchical Data:** The tree-like relationships found in taxonomies (e.g., Kingdom \> Phylum \> Class), language semantics, or organizational charts are severely distorted when forced into a Euclidean space.15  
* **Bounded Relationships:** Many real-world relationships are inherently bounded. In a social network, for instance, the "social distance" between individuals has practical limits. In an unbounded Euclidean space, latent positions can drift towards infinity during training, leading to numerical instability and a phenomenon known as "degeneracy," where the model produces nonsensical outputs.10

These limitations reveal that the choice of geometry is not a minor implementation detail but a critical modeling decision with profound consequences for the quality and interpretability of the learned representations. The inadequacy of the Euclidean assumption for many complex data types necessitates the exploration of alternative geometries, leading directly to the concept of curved latent spaces.

---

## **Section 2: Curving the Space: The Hypersphere as a Manifold of Styles**

The limitations of flat, Euclidean geometry motivate a shift towards a more flexible and powerful framework: manifold learning. By assuming that data lies on a curved, non-linear surface and by choosing a geometry that reflects the data's intrinsic structure, we can build generative models that are more stable, expressive, and intuitive. The hypersphere, a multi-dimensional generalization of a sphere, emerges as a particularly compelling choice for a manifold of styles, emotions, and other continuous concepts.

### **2.1 An Introduction to Manifold Learning**

The theoretical foundation for this approach is the **manifold hypothesis**, a central idea in modern machine learning which posits that high-dimensional, real-world data (like images or sounds) does not fill its ambient space uniformly. Instead, it tends to concentrate on or near a much lower-dimensional, non-linear manifold embedded within that high-dimensional space.5 A simple analogy is a coiled garden hose in a large, empty room; the hose itself is fundamentally a one-dimensional line, but it is embedded in a three-dimensional space.

From this perspective, the goal of a generative model's encoder is to learn a mapping from this complex, embedded data manifold (M) to a simpler, lower-dimensional latent representation (Z). This process effectively "unrolls" or "flattens" the manifold, making its intrinsic structure explicit and navigable.18 The decoder then learns the inverse transformation, mapping points from the simplified latent manifold back to their corresponding locations on the high-dimensional data manifold.18 The latent space, therefore, is not just a compressed representation but a learned parameterization of the data's underlying geometric structure.

### **2.2 The Geometric Properties of the Hypersphere**

The hypersphere, or n-sphere, is a manifold defined as the set of points at a constant distance from a central origin in (n+1)-dimensional space. It possesses several unique geometric properties that make it an advantageous structure for a latent space.

* **Positive Curvature:** A sphere has constant positive curvature. Unlike a flat plane (zero curvature), its surface "wraps around" on itself. This property is exceptionally well-suited for modeling cyclical or periodic data. For example, a color wheel can be mapped seamlessly onto the equator of a sphere, where moving past violet naturally leads back to red. In the context of social network analysis, this positive curvature inherently encourages the formation of transitive relationships (if A is close to B, and B is close to C, the spherical geometry constrains A and C to also be relatively close) and tight-knit communities.10  
* **Boundedness and Compactness:** A sphere is a finite, bounded, and compact space. This is perhaps its most significant practical advantage over the infinite, unbounded Euclidean space. By constraining all latent representations to lie on the surface of a unit hypersphere, the model prevents latent positions from drifting to arbitrarily large norms during training.17 This mitigates the "degeneracy issues" that plague Euclidean models, where extreme latent vector values can lead to numerical instability and nonsensical outputs.10 The bounded nature ensures that all distances are finite and well-behaved, leading to more robust and stable models.  
* **Isotropy (No Center, No Edges):** On the surface of a sphere, every point is geometrically equivalent; there is no unique center or edge. This property provides a powerful conceptual foundation for representing diversity. In a Euclidean latent space with a Gaussian prior centered at the origin, there is an implicit "default" or "average" representation at the center, with all other variations defined as deviations from it. On a sphere, however, no single style, emotion, or concept is privileged as the origin. Every point is an equally valid location on the globe, providing a more equitable and topologically sound representation of diversity.

### **2.3 Technical Advantages of Spherical Constraints in Generative Models**

Imposing a spherical structure on the latent space is not merely a representational choice; it functions as a powerful, principled form of geometric regularization that solves fundamental optimization problems in both VAEs and GANs. Regularization in machine learning refers to any modification that improves a model's ability to generalize to new data. While common techniques are often algebraic (e.g., weight decay), spherical constraints provide a geometric alternative that directly addresses core instabilities in generative models.

#### **In Variational Autoencoders (S-VAE)**

Standard VAEs with a Gaussian latent space suffer from a critical training pathology known as **KL collapse** or "posterior collapse".20 The VAE's objective function includes a Kullback-Leibler (KL) divergence term that penalizes the model if the learned posterior distribution,

q(z∣x), deviates from the prior distribution, p(z) (typically a standard normal distribution, N(0,I)). This term acts as a regularizer, but it often becomes too strong, encouraging the encoder to simply ignore the input data x and output the prior distribution for every data point. When this happens, the latent variable becomes uninformative, and the decoder is forced to generate an average of all training data, resulting in blurry, useless outputs.7

The solution lies in replacing the Gaussian prior and posterior with a distribution that is native to the sphere: the **von Mises-Fisher (vMF) distribution**.20 The vMF distribution is characterized by a mean direction vector

μ (a point on the unit sphere) and a concentration parameter κ (which controls how tightly the distribution is clustered around μ). The crucial technical breakthrough is that when both the prior and posterior are vMF distributions, the KL divergence between them simplifies to a function that depends *only on the concentration parameter κ* and is independent of the mean direction μ.21 This allows researchers to treat

κ as a fixed hyperparameter during training. By doing so, the optimization pressure that forces the learned mean to collapse towards the prior's mean (the origin in the Gaussian case) is completely removed.7 The model is free to place the latent representations anywhere on the sphere as needed to best reconstruct the data, while the KL term simply encourages them to be sufficiently concentrated. This simple geometric modification not only averts KL collapse but leads to more stable training, consistently better data likelihoods, and the learning of "richer and more nuanced structures" in the latent space compared to Gaussian VAEs.20

#### **In Generative Adversarial Networks (SphereGAN/CircleGAN)**

GANs are notoriously difficult to train, suffering from instability, vanishing gradients, and **mode collapse**, where the generator learns to produce only a few types of outputs, failing to capture the full diversity of the training data.8 Spherical geometry provides a robust framework for mitigating these issues.

**SphereGAN** is an Integral Probability Metric (IPM)-based GAN that operates on a hyperspherical feature space.26 Its discriminator maps input data to a feature space and then projects these features onto a hypersphere. The objective function then seeks to match the geometric moments of the real and fake distributions on this sphere. Because the space is bounded, the IPMs are naturally bounded, which dramatically improves training stability without requiring the complex and computationally expensive gradient penalty terms used in models like WGAN-GP.26 Furthermore, by matching higher-order moments, SphereGAN can capture more detailed statistical properties of the data distribution, leading to more accurate and diverse generated samples.26

**CircleGAN** introduces an even more explicit geometric mechanism for promoting diversity.28 Its novel discriminator architecture learns to structure the spherical latent space by discriminating samples based on their position relative to

**spherical circles**. The model learns to populate embeddings of real samples around a "great circle"—the longest possible circle on the sphere's surface (like the equator)—while pushing the embeddings of fake samples towards the poles, which represent the shortest possible circles.28 The underlying principle is that longer circles occupy a larger surface area on the hypersphere. By associating realism with the largest available area, the discriminator geometrically incentivizes the generator to produce a diverse range of outputs to cover this expansive "real" region. This provides a direct, geometrically-motivated defense against mode collapse, ensuring the generator explores the full breadth of the data manifold.28

In both VAEs and GANs, the spherical constraint acts as a principled regularizer. It replaces ad-hoc algebraic solutions with a fundamental geometric constraint that naturally aligns the model's structure with the desired properties of stability and diversity, solving deep-seated optimization challenges in the process.

---

## **Section 3: The Art of Navigation: Interpolation and Geodesics**

A well-structured latent space is not merely a static representation; it is a dynamic landscape meant for exploration. The ability to move smoothly between points in this space and generate coherent intermediate outputs is a key test of a generative model's understanding and a powerful tool for creative applications.29 However, the geometry of the latent space dictates the nature of this movement. The choice of interpolation method—how one travels from point A to point B—is critical, and a naive approach can easily lead to nonsensical results.

### **3.1 The Flaw of the Straight Line: Linear Interpolation (LERP)**

The most straightforward method for moving between two latent vectors, z1​ and z2​, is **linear interpolation (LERP)**. This is achieved by taking a weighted average of the two vectors:

$$z\_t \= (1-t) \\cdot z\_1 \+ t \\cdot z\_2 \\quad \\text{where } t \\in $$

This formula traces a straight line in the latent space from z1​ to z2​.29 While simple and intuitive, LERP is fundamentally flawed for navigating latent spaces that are normalized or inherently curved, such as a hypersphere.

When latent vectors are normalized to have a unit length (a common practice that improves training stability), they lie on the surface of a hypersphere. A straight line connecting two points on this surface will necessarily pass through the interior of the sphere.30 This interior region often corresponds to an area of very low probability density in the model's learned distribution. When these intermediate, low-probability vectors are passed to the decoder, they produce outputs that are often blurry, distorted, or semantically meaningless.31 This phenomenon is sometimes described as a "tentpole" effect: as the interpolation moves from one endpoint towards the middle, the magnitude of the interpolated vector decreases, dipping into an "unlikely" region, before rising again as it approaches the other endpoint.30 This failure to remain on the data manifold breaks the illusion of a smooth, coherent transformation.

### **3.2 Spherical Linear Interpolation (SLERP): The Path of "Gentle Blends"**

The geometrically correct method for interpolating between two points on the surface of a hypersphere is **Spherical Linear Interpolation (SLERP)**.29 Instead of tracing a straight line through the interior, SLERP travels along the shortest path on the surface of the sphere itself—the

**great-circle arc** connecting the two points.29 This ensures that every intermediate point also lies on the sphere, maintaining a constant norm and staying within the high-probability manifold of learned representations.

The formula for SLERP, while more complex than LERP, can be understood intuitively as a constant-speed rotation from vector z1​ to vector z2​ along this arc.30 Given two unit vectors

z1​ and z2​ separated by an angle Ω, the interpolated vector zt​ is given by:

slerp(z1​,z2​;t)=sin(Ω)sin((1−t)Ω)​z1​+sin(Ω)sin(tΩ)​z2​  
By using SLERP, the transitions between generated outputs become truly fluid and coherent. As one traverses the path from z1​ to z2​, every intermediate latent vector zt​ is a valid, high-probability representation. The resulting decoded outputs form a "gentle blend," smoothly morphing from the starting concept to the ending one without the degradation seen with LERP.31 This is the technical mechanism that enables the fluid transformations and continuous shifts in tone envisioned in the initial query. SLERP is therefore the preferred interpolation method for any generative model employing a normalized or spherical latent space, including many modern GANs and VAEs.29

### **3.3 The Shortest Path: Geodesic Distance and Riemannian Manifolds**

The concept of a shortest path can be generalized beyond a simple sphere to any curved manifold. In the field of differential geometry, this shortest path is known as a **geodesic**.33 When a generative model's latent space is treated not just as a fixed shape but as a learned

**Riemannian manifold**, the notion of distance itself becomes dynamic and data-driven.

The local geometry of this learned manifold is defined by the **pull-back metric**. This metric, Gz​=JzT​Jz​, where Jz​ is the Jacobian of the decoder network, essentially "pulls back" the Euclidean distance from the high-dimensional data space onto the low-dimensional latent space.36 It defines an infinitesimal "ruler" at every point

z in the latent space, where the length measured by the ruler depends on how much the decoder stretches or compresses space when mapping that point to the data manifold. A region in latent space that maps to a large, complex area of the data manifold will have a "longer" ruler (a larger metric) than a region that maps to a small, simple area.

The **geodesic distance** between two points is then the length of the shortest possible path, calculated by integrating these local distances along the curve.37 This path represents the most efficient and "natural" transformation between two concepts as learned by the model. A key property of these learned manifolds is that regions of high data density correspond to areas of lower "effective distance" or "curvature." Consequently, the geodesic path between two points will naturally bend to pass through these high-density regions, effectively finding "shortcuts" through the valleys of the probability landscape.39 While a straight line (LERP) might cut across a "desert" of low probability, a geodesic will intelligently navigate through the most plausible intermediate states.39 Therefore, computing and traversing geodesics on the learned Riemannian manifold represents the ultimate method for achieving meaningful, high-fidelity interpolations, capturing the true semantic structure of the generative model's world.

---

## **Section 4: Designing for Exploration: Interfaces for a Spherical World**

The conceptual power and technical elegance of a spherical latent space can only be fully realized through interfaces that allow for intuitive human interaction. Translating the abstract, high-dimensional geometry of a learned manifold into a tangible, explorable user experience is a significant design challenge. The most relevant precedents for this task come from the field of spatial computing (Augmented and Virtual Reality), which has developed a rich set of principles for designing interactions within three-dimensional, non-flat environments.

### **4.1 Principles of Spatial UI/UX for Abstract Spaces**

Navigating a spherical latent space requires a departure from the 2D paradigms of windows, icons, menus, and pointers. Instead, designers must think in terms of space, embodiment, and physical intuition. By adapting principles from AR/VR design, we can create interfaces that make the abstract feel concrete and the complex feel navigable.41

Key principles for designing these interfaces include:

* **Direct Manipulation:** The most intuitive way to interact with a 3D object is to manipulate it directly. Instead of using abstract sliders or numerical inputs, an interface for a spherical latent space should allow users to "grab" the sphere with a mouse or VR controller and "rotate" it in 3D space.44 This one-to-one mapping between physical action and digital result is crucial for creating a feeling of direct engagement and control.  
* **Spatial Awareness and Ergonomics:** A 3D interface must respect the user's physical context. Important interactive elements should be placed within a comfortable field of view (typically within 30 degrees of the center) and a comfortable range of motion to avoid physical strain or disorientation, especially in immersive VR settings.44 The design must account for whether the user is sitting, standing, or moving, and ensure interactions remain comfortable and accessible.43  
* **Minimizing Abstract UIs and Leveraging Affordances:** The interface should rely on visual cues—or affordances—that suggest how an object can be used. The sphere itself is a powerful affordance; its roundness invites rotation and exploration. The goal is to minimize the need for abstract buttons and menus that clutter the view and increase cognitive load. If something looks like it can be grabbed, it should be grabbable.44  
* **Immersive Feedback:** To make an abstract space feel tangible, interaction must be met with immediate and clear feedback. This can be visual (e.g., highlighting the selected point on the sphere, showing a preview of the generated output), auditory (e.g., a subtle sound that changes in pitch as the user moves across the sphere's surface), or even haptic (e.g., a vibration in the controller when a point of interest is crossed).41 This multi-sensory feedback reinforces the user's actions and enhances the sense of presence within the data landscape.

A significant challenge in designing such interfaces is the inherent **dimensionality mismatch**. A machine learning model's latent space may have hundreds or even thousands of dimensions, while a human user can only directly perceive and interact with three.1 Therefore, any visual representation of the latent space, including a 3D sphere, is necessarily a

*projection* or a low-dimensional *embedding* of a much higher-dimensional reality.5 The success and intuitiveness of the interface depend critically on the quality of this projection. A well-designed projection, likely using dimensionality reduction techniques like t-SNE or UMAP adapted for spherical geometries, will place perceptually similar styles close to each other in the 3D view, creating a faithful and navigable map of the high-dimensional space.6 The user interface is thus not a passive "viewer" but an active participant in the interpretation of the model, working to present its complex internal world in a human-understandable form.49

### **4.2 Interaction Paradigms and Application Concepts**

By combining these spatial UI principles with the geometric properties of the sphere, we can envision a new class of creative tools and exploratory experiences.

* **The "Orb" Metaphor (for Exploration):** This is the most direct implementation of the core concept. A user is presented with a 3D sphere, either on a 2D screen or in an immersive VR environment. Every point on the sphere's surface corresponds to a unique latent vector. The user can directly rotate the orb. As they do, the generated output—be it an image, a piece of music, or a text style—updates in real-time to reflect the latent vector at the point currently facing the user. This interaction model perfectly captures the idea of "rotating the orb to shift the tone" and provides a powerful tool for serendipitous discovery and creative exploration.  
* **Geodesic Pathfinding (for Transition):** Building on the orb metaphor, an interface could allow a user to select two distinct points on the sphere's surface (e.g., by "pinning" them). The system would then compute and visualize the geodesic path between them as a glowing arc on the sphere. The user could then "play" this path, generating a smooth, high-fidelity morph or transition between the two selected styles.29 This could be used to create animations that blend artistic movements, musical pieces that transition seamlessly between genres, or text that gradually shifts its emotional tone.  
* **Constrained Exploration (for Control):** For more directed tasks like style transfer, the interface could provide more constrained forms of navigation. After analyzing the latent space, certain meaningful axes of variation (e.g., "brushstroke size," "color saturation," "vocal intensity") might be identified. The UI could present these as controls that, instead of moving along a simple linear slider, trace constrained arcs on the sphere's surface. This would allow for fine-grained, interpretable control over specific attributes while ensuring that any combination of edits remains on the manifold of plausible and coherent styles.50

These interaction paradigms can be deployed in a variety of compelling applications:

* **Application Concept 1: Interactive Digital Exhibitions:** Artists like Refik Anadol have already begun to explore the aesthetic potential of latent spaces in large-scale installations.52 An interactive exhibition could feature a large physical sphere or a shared virtual one that visitors can collaboratively manipulate. As the audience rotates the sphere, the generative art projected onto the gallery walls would shift and evolve, allowing for a collective exploration of the "latent dreams" or "collective unconscious" embedded within the model's training data.54 This transforms the passive viewing of art into an active, participatory experience of co-creation with the AI.  
* **Application Concept 2: Navigable Music Playlists:** A music streaming service could move beyond rigid, genre-based playlists by representing its catalog on a vast spherical manifold. Proximity on this "sonic landscape" would correspond to sonic and emotional similarity.10 A user could start with a song they enjoy and, instead of being served a discrete list of similar tracks, could simply "drag" their listening position across the surface of the sphere. This would create a continuous, user-guided journey through music, enabling serendipitous discovery of adjacent genres and novel blends, effectively creating a personalized, infinitely variable playlist in real time.48

---

## **Section 5: A Comparative Topology of Latent Spaces**

The decision to use a spherical latent space is a deliberate choice among several geometric options, each with distinct properties and ideal use cases. The geometry of the latent space should be aligned with the underlying structure of the data being modeled; a mismatch can lead to poor performance and distorted representations.13 A comparative analysis of the three primary geometries used in machine learning—Euclidean, spherical, and hyperbolic—provides a clear framework for making this critical architectural decision.

### **5.1 Euclidean vs. Spherical vs. Hyperbolic: A Geometric Triad**

These three geometries can be distinguished by their curvature, a fundamental property that dictates how distances and shapes behave within the space.14

* **Euclidean Space (Zero Curvature):** This is the familiar "flat" space of classical geometry. It is the default assumption for many machine learning models due to its simplicity and the ease of computation.12 In Euclidean space, the shortest distance between two points is a straight line, and the sum of angles in a triangle is always 180 degrees. It is well-suited for data where the primary relationships are based on attribute similarity in a vector space, but it is an inefficient and often distorting choice for data with more complex intrinsic structures.15  
* **Spherical Space (Positive Curvature):** This is a "closed" or "wrapping" space where straight lines (geodesics) are great circles, and any two lines will eventually intersect.57 The sum of angles in a triangle on a sphere is always greater than 180 degrees. Its positive curvature and bounded nature make it ideal for representing data with cyclical patterns, community structures, or inherent directional properties.10 The finite "real estate" on a sphere's surface naturally encourages related data points to cluster together tightly.16  
* **Hyperbolic Space (Negative Curvature):** This is an "open" or "expanding" space. It can be visualized as a saddle shape that curves away from itself at every point. In hyperbolic space, parallel lines can diverge, and the sum of angles in a triangle is always less than 180 degrees.57 Its most important property is that its volume grows exponentially with its radius, in stark contrast to the polynomial growth of Euclidean space.15 This makes it uniquely suited for representing data with a hierarchical or tree-like structure.15

### **5.2 The Power of Negative Curvature: Hyperbolic Spaces for Hierarchies**

The unique advantage of hyperbolic geometry lies in its ability to embed hierarchical data with minimal distortion. Many real-world datasets are inherently hierarchical, including biological taxonomies, organizational charts, file systems, and the semantic relationships in language (e.g., the hypernymy of WordNet, where "dog" is a type of "canine," which is a type of "mammal").58

Attempting to represent a tree structure in a flat Euclidean space inevitably creates a geometric conflict. To maintain the correct distances between nodes at the same level of the tree, the distances between different levels must be compressed. Conversely, to maintain the correct distances between parents and children, nodes at the same level (siblings) must be pushed far apart.15 This distortion becomes exponentially worse as the tree grows deeper. Spherical space, with its finite volume, is even less suitable for embedding such an infinitely branching structure.15

Hyperbolic space, with its exponential expansion, provides a perfect geometric analogue to a tree.60 In the common Poincaré disk model of hyperbolic geometry, the root of the hierarchy can be placed at the center of the disk. As one moves outwards towards the boundary, the available space expands exponentially, allowing the increasing number of nodes at each successive level of the hierarchy to be placed without crowding or distortion.59 This makes hyperbolic latent spaces the superior, and often necessary, choice for generative models that aim to learn and represent data with a strong underlying hierarchical organization.

### **Table 1: A Comparative Analysis of Latent Space Geometries**

The following table summarizes the key characteristics, strengths, weaknesses, and ideal applications of the three primary latent space geometries, providing a practical guide for model selection.

| Characteristic | Euclidean Space | Spherical Space | Hyperbolic Space |
| :---- | :---- | :---- | :---- |
| **Curvature** | Zero | Positive | Negative |
| **Key Property** | Flat, Unbounded | Curved, Bounded, Compact | Curved, Unbounded, Expansive |
| **Natural Data Structure** | Unstructured, attribute-based data | Cyclical, periodic, community-based, directional data | Hierarchical, tree-like data |
| **Strengths** | Simplicity, familiarity, default for many models | Models communities/cycles, numerical stability, bounded distances | Embeds hierarchies with low distortion, vast capacity |
| **Weaknesses** | Distorts non-Euclidean data, can be unstable (unbounded) | Distorts hierarchical data, limited capacity | Less intuitive, more complex mathematics |
| **Example Applications** | Basic image classification, simple regression | Social network analysis, style/emotion globes, protein structure, word embeddings | Language semantics (WordNet), taxonomies, phylogenetic trees, recommendation systems |

---

## **Conclusion: The Future is Non-Euclidean**

The exploration of spherical latent spaces marks a pivotal evolution in generative artificial intelligence, moving the field from simplistic, flat representations of data towards richer, geometrically-informed models of reality. This shift is more than a technical refinement; it is a conceptual leap that redefines our understanding of diversity, variation, and creativity within AI systems. By embracing the topology of a continuous, bounded globe, we have developed models that are not only more stable and robust but also more aligned with the fluid nature of the concepts they seek to represent.

However, the journey into non-Euclidean AI is just beginning. The true potential of these geometric frameworks may extend far beyond the smooth interpolation and "gentle blends" that currently define their utility. The future lies in leveraging more complex and dynamic geometries to achieve true **conceptual emergence**. By designing latent manifolds that are not just curved but can also contain discontinuities, branches, or regions of varying curvature, we may enable AI systems to make "logical leaps"—to generate outputs that are not merely plausible interpolations between known training examples but are genuinely novel and out-of-distribution (OOD).62 This would represent a move from generative models that remix to models that can invent, bridging the gap between statistical pattern matching and genuine creativity.

Ultimately, this report returns to the initial premise: the power of viewing diversity as a topology rather than a set of boxes. The geometric structure of a model's latent space is not an incidental feature but a fundamental architectural choice that directly governs its capacity to represent the rich diversity of the world and to generate novelty.63 As artificial intelligence becomes an increasingly integral partner in creative endeavors and scientific discovery, our ability to design, shape, and navigate these intricate, non-Euclidean "spaces of possibility" will become as important as the learning algorithms themselves.65 The future of AI will be defined not just by the scale of its models, but by the sophistication, elegance, and expressiveness of their internal geometries. The sphere of possibility is vast, and we have only just begun to explore its surface.

#### **Works cited**

1. What Is Latent Space? \- IBM, accessed on August 31, 2025, [https://www.ibm.com/think/topics/latent-space](https://www.ibm.com/think/topics/latent-space)  
2. What Is Latent Space? | Coursera, accessed on August 31, 2025, [https://www.coursera.org/articles/what-is-latent-space](https://www.coursera.org/articles/what-is-latent-space)  
3. Latent Space in Deep Learning | Baeldung on Computer Science, accessed on August 31, 2025, [https://www.baeldung.com/cs/dl-latent-space](https://www.baeldung.com/cs/dl-latent-space)  
4. A Comprehensive Guide to Latent Space | by AI Maverick \- Medium, accessed on August 31, 2025, [https://samanemami.medium.com/a-comprehensive-guide-to-latent-space-9ae7f72bdb2f](https://samanemami.medium.com/a-comprehensive-guide-to-latent-space-9ae7f72bdb2f)  
5. Latent space \- Wikipedia, accessed on August 31, 2025, [https://en.wikipedia.org/wiki/Latent\_space](https://en.wikipedia.org/wiki/Latent_space)  
6. Latent Space | Saturn Cloud, accessed on August 31, 2025, [https://saturncloud.io/glossary/latent-space/](https://saturncloud.io/glossary/latent-space/)  
7. SPHERICAL LATENT SPACES FOR STABLE VARIATIONAL AUTOENCODERS \- Jiacheng Xu, accessed on August 31, 2025, [https://jiacheng-xu.github.io/material/vmf-vae-emnlp18-slides.pdf](https://jiacheng-xu.github.io/material/vmf-vae-emnlp18-slides.pdf)  
8. Generative Adversarial Networks (GANs): Challenges, Solutions, and Future Directions, accessed on August 31, 2025, [https://ira.lib.polyu.edu.hk/bitstream/10397/94420/1/COMP-0061\_Saxena\_Generative\_Adversarial\_Networks.pdf](https://ira.lib.polyu.edu.hk/bitstream/10397/94420/1/COMP-0061_Saxena_Generative_Adversarial_Networks.pdf)  
9. Generative modelling in latent space \- Sander Dieleman, accessed on August 31, 2025, [https://sander.ai/2025/04/15/latents.html](https://sander.ai/2025/04/15/latents.html)  
10. Spherical latent space models for social network analysis \- arXiv, accessed on August 31, 2025, [https://arxiv.org/html/2508.16556v1](https://arxiv.org/html/2508.16556v1)  
11. (PDF) Spherical latent space models for social network analysis, accessed on August 31, 2025, [https://www.researchgate.net/publication/394921095\_Spherical\_latent\_space\_models\_for\_social\_network\_analysis](https://www.researchgate.net/publication/394921095_Spherical_latent_space_models_for_social_network_analysis)  
12. The Geometry of Continuous Latent Space Models for Network Data \- PMC, accessed on August 31, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7682928/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7682928/)  
13. Neural Latent Geometry Search: Product Manifold Inference via Gromov-Hausdorff-Informed Bayesian Optimization, accessed on August 31, 2025, [https://proceedings.neurips.cc/paper\_files/paper/2023/hash/78efbc5386c5a7c241e7fcc482d3c3dc-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2023/hash/78efbc5386c5a7c241e7fcc482d3c3dc-Abstract-Conference.html)  
14. Machine Learning in Non-Euclidean Spaces: Revolutionizing Data Representation and Analysis | by Siddhartha Pramanik | Medium, accessed on August 31, 2025, [https://medium.com/@siddharthapramanik771/machine-learning-in-non-euclidean-spaces-revolutionizing-data-representation-and-analysis-bfc1e2d3c764](https://medium.com/@siddharthapramanik771/machine-learning-in-non-euclidean-spaces-revolutionizing-data-representation-and-analysis-bfc1e2d3c764)  
15. Visualizing High-Dimensional Hyperbolic Data \- UC Berkeley EECS, accessed on August 31, 2025, [https://www2.eecs.berkeley.edu/Pubs/TechRpts/2022/EECS-2022-127.pdf](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2022/EECS-2022-127.pdf)  
16. NBER WORKING PAPER SERIES IDENTIFYING THE LATENT SPACE GEOMETRY OF NETWORK MODELS THROUGH ANALYSIS OF CURVATURE Shane Lubold Aru, accessed on August 31, 2025, [https://www.nber.org/system/files/working\_papers/w28273/w28273.pdf](https://www.nber.org/system/files/working_papers/w28273/w28273.pdf)  
17. arxiv.org, accessed on August 31, 2025, [https://arxiv.org/html/2508.16556v1\#:\~:text=The%20spherical%20formulation%20yields%20a,degeneracy%20and%20improving%20numerical%20stability.](https://arxiv.org/html/2508.16556v1#:~:text=The%20spherical%20formulation%20yields%20a,degeneracy%20and%20improving%20numerical%20stability.)  
18. Proof of the existence of the latent space in deep learning \- Mathematics Stack Exchange, accessed on August 31, 2025, [https://math.stackexchange.com/questions/4461156/proof-of-the-existence-of-the-latent-space-in-deep-learning](https://math.stackexchange.com/questions/4461156/proof-of-the-existence-of-the-latent-space-in-deep-learning)  
19. \[2508.16556\] Spherical latent space models for social network analysis \- arXiv, accessed on August 31, 2025, [https://arxiv.org/abs/2508.16556](https://arxiv.org/abs/2508.16556)  
20. Spherical Latent Spaces for Stable Variational Autoencoders \- ACL ..., accessed on August 31, 2025, [https://aclanthology.org/D18-1480/](https://aclanthology.org/D18-1480/)  
21. \[1808.10805\] Spherical Latent Spaces for Stable Variational Autoencoders \- arXiv, accessed on August 31, 2025, [https://arxiv.org/abs/1808.10805](https://arxiv.org/abs/1808.10805)  
22. Spherical Latent Spaces for Stable Variational Autoencoders | Request PDF \- ResearchGate, accessed on August 31, 2025, [https://www.researchgate.net/publication/334115730\_Spherical\_Latent\_Spaces\_for\_Stable\_Variational\_Autoencoders](https://www.researchgate.net/publication/334115730_Spherical_Latent_Spaces_for_Stable_Variational_Autoencoders)  
23. jiacheng-xu/vmf\_vae\_nlp: Code for EMNLP18 paper "Spherical Latent Spaces for Stable Variational Autoencoders" \- GitHub, accessed on August 31, 2025, [https://github.com/jiacheng-xu/vmf\_vae\_nlp](https://github.com/jiacheng-xu/vmf_vae_nlp)  
24. Generative Adversarial Networks (GANs): Challenges, Solutions, and Future Directions \- arXiv, accessed on August 31, 2025, [https://arxiv.org/vc/arxiv/papers/2005/2005.00065v1.pdf](https://arxiv.org/vc/arxiv/papers/2005/2005.00065v1.pdf)  
25. Common Problems | Machine Learning \- Google for Developers, accessed on August 31, 2025, [https://developers.google.com/machine-learning/gan/problems](https://developers.google.com/machine-learning/gan/problems)  
26. Sphere Generative Adversarial Network Based on Geometric ..., accessed on August 31, 2025, [http://cau.ac.kr/\~jskwon/paper/SphereGAN\_CVPR2019.pdf](http://cau.ac.kr/~jskwon/paper/SphereGAN_CVPR2019.pdf)  
27. Sphere Generative Adversarial Network Based on Geometric Moment Matching \- CVF Open Access, accessed on August 31, 2025, [https://openaccess.thecvf.com/content\_CVPR\_2019/papers/Park\_Sphere\_Generative\_Adversarial\_Network\_Based\_on\_Geometric\_Moment\_Matching\_CVPR\_2019\_paper.pdf](https://openaccess.thecvf.com/content_CVPR_2019/papers/Park_Sphere_Generative_Adversarial_Network_Based_on_Geometric_Moment_Matching_CVPR_2019_paper.pdf)  
28. CircleGAN: Generative Adversarial Learning across Spherical Circles, accessed on August 31, 2025, [https://papers.neurips.cc/paper\_files/paper/2020/file/f14bc21be7eaeed046fed206a492e652-Paper.pdf](https://papers.neurips.cc/paper_files/paper/2020/file/f14bc21be7eaeed046fed206a492e652-Paper.pdf)  
29. Latent Space Interpolation Is Powering the Next Wave of Generative AI | HackerNoon, accessed on August 31, 2025, [https://hackernoon.com/latent-space-interpolation-is-powering-the-next-wave-of-generative-ai](https://hackernoon.com/latent-space-interpolation-is-powering-the-next-wave-of-generative-ai)  
30. Spherical Interpolation | Minibatch AI, accessed on August 31, 2025, [https://minibatchai.com/2022/04/24/Slerp.html](https://minibatchai.com/2022/04/24/Slerp.html)  
31. Z-SASLM: Zero-Shot Style-Aligned SLI Blending Latent Manipulation \- Qeios, accessed on August 31, 2025, [https://www.qeios.com/read/JC1N8C](https://www.qeios.com/read/JC1N8C)  
32. Sampling Generative Networks \- arXiv, accessed on August 31, 2025, [https://arxiv.org/vc/arxiv/papers/1609/1609.04468v2.pdf](https://arxiv.org/vc/arxiv/papers/1609/1609.04468v2.pdf)  
33. Geodesic versus planar distance—ArcGIS Pro | Documentation, accessed on August 31, 2025, [https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/geodesic-versus-planar-distance.htm](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/geodesic-versus-planar-distance.htm)  
34. GEODESICS ON SURFACES BY VARIATIONAL CALCULUS J Villanueva Florida Memorial University 15800 NW 42nd Ave Miami, FL 33054 jvillan \- Pearson, accessed on August 31, 2025, [https://www.pearson.com/content/dam/one-dot-com/one-dot-com/us/en/files/Jay%20Villanueva%20-%20geodesics9.pdf](https://www.pearson.com/content/dam/one-dot-com/one-dot-com/us/en/files/Jay%20Villanueva%20-%20geodesics9.pdf)  
35. Geodesic Distance Function Learning via Heat Flow on Vector Fields, accessed on August 31, 2025, [http://proceedings.mlr.press/v32/linb14.pdf](http://proceedings.mlr.press/v32/linb14.pdf)  
36. Decoder ensembling for learned latent geometries \- DTU Orbit, accessed on August 31, 2025, [https://orbit.dtu.dk/files/379854471/decoder\_ensembling\_for\_learned.pdf](https://orbit.dtu.dk/files/379854471/decoder_ensembling_for_learned.pdf)  
37. Geometrical Aspects of Manifold Learning \- DTU Orbit, accessed on August 31, 2025, [https://orbit.dtu.dk/files/181135439/gear\_phd\_thesis\_final.pdf](https://orbit.dtu.dk/files/181135439/gear_phd_thesis_final.pdf)  
38. Learning Riemannian Manifolds for Geodesic Motion Skills \- DTU Orbit, accessed on August 31, 2025, [https://orbit.dtu.dk/files/263986943/rss2021.pdf](https://orbit.dtu.dk/files/263986943/rss2021.pdf)  
39. Probability Density Geodesics in Image Diffusion Latent Space \- CVF Open Access, accessed on August 31, 2025, [https://openaccess.thecvf.com/content/CVPR2025/papers/Yu\_Probability\_Density\_Geodesics\_in\_Image\_Diffusion\_Latent\_Space\_CVPR\_2025\_paper.pdf](https://openaccess.thecvf.com/content/CVPR2025/papers/Yu_Probability_Density_Geodesics_in_Image_Diffusion_Latent_Space_CVPR_2025_paper.pdf)  
40. Enforcing Latent Euclidean Geometry in VAEs for Statistical Manifold Interpolation, accessed on August 31, 2025, [https://openreview.net/forum?id=a72vorQK8v](https://openreview.net/forum?id=a72vorQK8v)  
41. Spatial UI/UX Design: A Detailed Overview | by Hasitha Lakshan | Bootcamp \- Medium, accessed on August 31, 2025, [https://medium.com/design-bootcamp/spatial-ui-ux-design-a-detailed-overview-428b8835fd94](https://medium.com/design-bootcamp/spatial-ui-ux-design-a-detailed-overview-428b8835fd94)  
42. UI/UX designing: Knowing all about Spatial UI-The Future of User Interaction in Design | by roopika chari | Medium, accessed on August 31, 2025, [https://medium.com/@roopikachari/ui-ux-designing-knowing-all-about-spatial-ui-the-future-of-user-interaction-in-design-229c3ad4504e](https://medium.com/@roopikachari/ui-ux-designing-knowing-all-about-spatial-ui-the-future-of-user-interaction-in-design-229c3ad4504e)  
43. Spatial UI: Redefining Interaction in 3D Space — A UX Designer's Perspective \- Medium, accessed on August 31, 2025, [https://medium.com/@kirancrypto09/exploring-spatial-ui-the-future-of-immersive-interaction-a52587942d02](https://medium.com/@kirancrypto09/exploring-spatial-ui-the-future-of-immersive-interaction-a52587942d02)  
44. Spatial UI Design: Tips and Best Practices | IxDF, accessed on August 31, 2025, [https://www.interaction-design.org/literature/article/spatial-ui-design-tips-and-best-practices](https://www.interaction-design.org/literature/article/spatial-ui-design-tips-and-best-practices)  
45. Interactive Exploration and Refinement of Facial Expression using Manifold Learning \- Dynamic Graphics Project, accessed on August 31, 2025, [https://www.dgp.toronto.edu/projects/face-manifold/facemanifoldpaper.pdf](https://www.dgp.toronto.edu/projects/face-manifold/facemanifoldpaper.pdf)  
46. Virtual Reality for Data Visualisation, accessed on August 31, 2025, [https://dwbproject.org/virtual-reality-for-data-visualisation/](https://dwbproject.org/virtual-reality-for-data-visualisation/)  
47. Visualizing High Dimensional Data \- Naturalistic Data Analysis, accessed on August 31, 2025, [https://naturalistic-data.org/content/hypertools.html](https://naturalistic-data.org/content/hypertools.html)  
48. A Music Recommendation System Based on Sound Content \- GitHub, accessed on August 31, 2025, [https://github.com/rollingstorms/Sound-Content-Music-Recommendation-System](https://github.com/rollingstorms/Sound-Content-Music-Recommendation-System)  
49. Manifold Explorer: Satellite Image Labelling and Clustering Tool with Using Deep Convolutional Autoencoders \- MDPI, accessed on August 31, 2025, [https://www.mdpi.com/1999-4893/16/10/469](https://www.mdpi.com/1999-4893/16/10/469)  
50. Generative Human Motion Stylization in Latent Space \- OpenReview, accessed on August 31, 2025, [https://openreview.net/forum?id=daEqXJ0yZo¬eId=pXgDXPxULJ](https://openreview.net/forum?id=daEqXJ0yZo&noteId=pXgDXPxULJ)  
51. \[2203.13470\] Interactive Style Transfer: All is Your Palette \- arXiv, accessed on August 31, 2025, [https://arxiv.org/abs/2203.13470](https://arxiv.org/abs/2203.13470)  
52. Machine Hallucinations — Sphere \- Refik Anadol, accessed on August 31, 2025, [https://refikanadol.com/works/machine-hallucinations-sphere/](https://refikanadol.com/works/machine-hallucinations-sphere/)  
53. Modern Dream: How Refik Anadol Is Using Machine Learning and NFTs to Interpret MoMA's Collection | Magazine, accessed on August 31, 2025, [https://www.moma.org/magazine/articles/658](https://www.moma.org/magazine/articles/658)  
54. Latent Spaces \- Illusionaries, accessed on August 31, 2025, [https://www.illusionaries.com/latent-spaces](https://www.illusionaries.com/latent-spaces)  
55. New Art City: Virtual Art Space, accessed on August 31, 2025, [https://newart.city/](https://newart.city/)  
56. A music recommendation algorithm based on clustering and latent factor model \- MATEC Web of Conferences, accessed on August 31, 2025, [https://www.matec-conferences.org/articles/matecconf/pdf/2020/05/matecconf\_cscns2020\_03009.pdf](https://www.matec-conferences.org/articles/matecconf/pdf/2020/05/matecconf_cscns2020_03009.pdf)  
57. Confused About Different Types of Geometry : r/learnmath \- Reddit, accessed on August 31, 2025, [https://www.reddit.com/r/learnmath/comments/10wbwrc/confused\_about\_different\_types\_of\_geometry/](https://www.reddit.com/r/learnmath/comments/10wbwrc/confused_about_different_types_of_geometry/)  
58. NeurIPS Poster Hyperbolic Space with Hierarchical Margin Boosts Fine-Grained Learning from Coarse Labels, accessed on August 31, 2025, [https://neurips.cc/virtual/2023/poster/71461](https://neurips.cc/virtual/2023/poster/71461)  
59. MHCN: A Hyperbolic Neural Network Model for Multi-view Hierarchical Clustering \- CVF Open Access, accessed on August 31, 2025, [https://openaccess.thecvf.com/content/ICCV2023/papers/Lin\_MHCN\_A\_Hyperbolic\_Neural\_Network\_Model\_for\_Multi-view\_Hierarchical\_Clustering\_ICCV\_2023\_paper.pdf](https://openaccess.thecvf.com/content/ICCV2023/papers/Lin_MHCN_A_Hyperbolic_Neural_Network_Model_for_Multi-view_Hierarchical_Clustering_ICCV_2023_paper.pdf)  
60. Hyperbolic Diffusion Embedding and Distance for Hierarchical Representation Learning, accessed on August 31, 2025, [https://proceedings.mlr.press/v202/lin23b/lin23b.pdf](https://proceedings.mlr.press/v202/lin23b/lin23b.pdf)  
61. "Hyperbolic Geometry and Hierarchical Representation Learning" by William Grisaitis, accessed on August 31, 2025, [https://stars.library.ucf.edu/etd2023/301/](https://stars.library.ucf.edu/etd2023/301/)  
62. (PDF) "A Non-Euclidean Approach to Generative AI and Out-of-Distribution Reasoning", accessed on August 31, 2025, [https://www.researchgate.net/publication/393805470\_A\_Non-Euclidean\_Approach\_to\_Generative\_AI\_and\_Out-of-Distribution\_Reasoning](https://www.researchgate.net/publication/393805470_A_Non-Euclidean_Approach_to_Generative_AI_and_Out-of-Distribution_Reasoning)  
63. Topology Applied to Machine Learning: From Global to Local \- Frontiers, accessed on August 31, 2025, [https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.668302/full](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.668302/full)  
64. Why Topology for Machine Learning and Knowledge Extraction? \- MDPI, accessed on August 31, 2025, [https://www.mdpi.com/2504-4990/1/1/6](https://www.mdpi.com/2504-4990/1/1/6)  
65. Towards Non-Euclidean Foundation Models: Advancing AI Beyond Euclidean Frameworks, accessed on August 31, 2025, [https://arxiv.org/html/2505.14417v1](https://arxiv.org/html/2505.14417v1)  
66. \[2505.14417\] Towards Non-Euclidean Foundation Models: Advancing AI Beyond Euclidean Frameworks \- arXiv, accessed on August 31, 2025, [https://arxiv.org/abs/2505.14417](https://arxiv.org/abs/2505.14417)