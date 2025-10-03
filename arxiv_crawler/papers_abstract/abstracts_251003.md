# Abstracts of Papers

## Physics
### Inferring Dynamic Physical Properties from Video Foundation Models
**Authors**: Guanqi Zhan, Xianzheng Ma, Weidi Xie, Andrew Zisserman

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02311v1](http://arxiv.org/pdf/2510.02311v1)

**Abstract**: We study the task of predicting dynamic physical properties from videos. More
specifically, we consider physical properties that require temporal information
to be inferred: elasticity of a bouncing object, viscosity of a flowing liquid,
and dynamic friction of an object sliding on a surface. To this end, we make
the following contributions: (i) We collect a new video dataset for each
physical property, consisting of synthetic training and testing splits, as well
as a real split for real world evaluation. (ii) We explore three ways to infer
the physical property from videos: (a) an oracle method where we supply the
visual cues that intrinsically reflect the property using classical computer
vision techniques; (b) a simple read out mechanism using a visual prompt and
trainable prompt vector for cross-attention on pre-trained video generative and
self-supervised models; and (c) prompt strategies for Multi-modal Large
Language Models (MLLMs). (iii) We show that video foundation models trained in
a generative or self-supervised manner achieve a similar performance, though
behind that of the oracle, and MLLMs are currently inferior to the other
models, though their performance can be improved through suitable prompting.


### Astrophysical Consequences of an Electroweak $\etaw$ Pseudo-Scalar
**Authors**: Hooman Davoudiasl

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02310v1](http://arxiv.org/pdf/2510.02310v1)

**Abstract**: Recently, it has been suggested that the spectrum of physical states in the
Standard Model may include an ultralight pseudo-scalar, denoted by $\eta_w$, in
analogy with the $\eta'$ state arising from the strong interactions. We find
that typical expectations for the properties of $\eta_w$ get challenged by
astrophysical constraints on the couplings of ultralight bosons. Our strongest
limit sets a lower bound of O(1000 TeV) on the decay constant of the
hypothesized pseudo-scalar. We also briefly discuss whether $\eta_w$ could be a
dark matter candidate, or the origin of dark energy, but conclude that those
identifications appear unlikely. Given the important implications of a
potentially overlooked $\eta_w$ state for a more complete understanding of the
electroweak interactions and a fundamental description of Nature, further
theoretical and phenomenological investigations of this possibility and its
associated physics are warranted.


### Learning to Generate Object Interactions with Physics-Guided Video Diffusion
**Authors**: David Romero, Ariana Bermudez, Hao Li, Fabio Pizzati, Ivan Laptev

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02284v1](http://arxiv.org/pdf/2510.02284v1)

**Abstract**: Recent models for video generation have achieved remarkable progress and are
now deployed in film, social media production, and advertising. Beyond their
creative potential, such models also hold promise as world simulators for
robotics and embodied decision making. Despite strong advances, however,
current approaches still struggle to generate physically plausible object
interactions and lack physics-grounded control mechanisms. To address this
limitation, we introduce KineMask, an approach for physics-guided video
generation that enables realistic rigid body control, interactions, and
effects. Given a single image and a specified object velocity, our method
generates videos with inferred motions and future object interactions. We
propose a two-stage training strategy that gradually removes future motion
supervision via object masks. Using this strategy we train video diffusion
models (VDMs) on synthetic scenes of simple interactions and demonstrate
significant improvements of object interactions in real scenes. Furthermore,
KineMask integrates low-level motion control with high-level textual
conditioning via predictive scene descriptions, leading to effective support
for synthesis of complex dynamical phenomena. Extensive experiments show that
KineMask achieves strong improvements over recent models of comparable size.
Ablation studies further highlight the complementary roles of low- and
high-level conditioning in VDMs. Our code, model, and data will be made
publicly available.


### Transformers Discover Molecular Structure Without Graph Priors
**Authors**: Tobias Kreiman, Yutong Bai, Fadi Atieh, Elizabeth Weaver, Eric Qu, Aditi S. Krishnapriyan

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02259v1](http://arxiv.org/pdf/2510.02259v1)

**Abstract**: Graph Neural Networks (GNNs) are the dominant architecture for molecular
machine learning, particularly for molecular property prediction and machine
learning interatomic potentials (MLIPs). GNNs perform message passing on
predefined graphs often induced by a fixed radius cutoff or k-nearest neighbor
scheme. While this design aligns with the locality present in many molecular
tasks, a hard-coded graph can limit expressivity due to the fixed receptive
field and slows down inference with sparse graph operations. In this work, we
investigate whether pure, unmodified Transformers trained directly on Cartesian
coordinates$\unicode{x2013}$without predefined graphs or physical
priors$\unicode{x2013}$can approximate molecular energies and forces. As a
starting point for our analysis, we demonstrate how to train a Transformer to
competitive energy and force mean absolute errors under a matched training
compute budget, relative to a state-of-the-art equivariant GNN on the OMol25
dataset. We discover that the Transformer learns physically consistent
patterns$\unicode{x2013}$such as attention weights that decay inversely with
interatomic distance$\unicode{x2013}$and flexibly adapts them across different
molecular environments due to the absence of hard-coded biases. The use of a
standard Transformer also unlocks predictable improvements with respect to
scaling training resources, consistent with empirical scaling laws observed in
other domains. Our results demonstrate that many favorable properties of GNNs
can emerge adaptively in Transformers, challenging the necessity of hard-coded
graph inductive biases and pointing toward standardized, scalable architectures
for molecular modeling.


### The (PXP)$^2$ model: long-range quantum scars in optical cavities
**Authors**: Hossein Hosseinabadi, Riccardo J. Valencia-Tortora, Aleksandr N. Mikheev, Darrick E. Chang, Johannes Zeiher, Roderich Moessner, Jamir Marino

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02246v1](http://arxiv.org/pdf/2510.02246v1)

**Abstract**: Rydberg-cavity systems are emerging as promising platforms for quantum
simulation and quantum information processing. These hybrid architectures
combine two complementary interaction mechanisms: cavity photons mediate
collective long-range couplings, while Rydberg excitations generate strong
short-range interactions. Together, they offer a setting for engineering
many-body phases characterized by a hierarchy of interactions across widely
different length scales. In this work, we introduce a minimal and scalable
model for such systems. Focusing on the strong Rydberg blockade regime, we
restrict the Hilbert space to the subspace enforced by the blockade, yielding a
kinetically constrained long-range model in one spatial dimension. This
approach both captures the physics of Rydberg-cavity experiments in the regime
of strong Rydberg interactions and provides a conceptually transparent
framework for studying the interplay of long-range and short-range
interactions. At equilibrium, in addition to paramagnetic and N\'eel-ordered
phases, the system supports a blockaded ferromagnetic/superradiant phase,
distinct from the conventional superradiant phase. Out of equilibrium, we
identify long-range quantum many-body scars, which are atypical nonthermal
eigenstates that evade the eigenstate thermalization hypothesis, and giving
rise to slow entanglement growth. In contrast to the linear-in-time
entanglement growth characteristic of short-range scarred models, these
long-range scars exhibit logarithmic entanglement dynamics. Our results
establish a minimal yet versatile framework for Rydberg-cavity systems, and
provide a stepping stone for future theoretical and experimental studies of
this frontier platform in quantum many-body physics.


### PUL-Inter-slice Defender: An Anomaly Detection Solution for Distributed Slice Mobility Attacks
**Authors**: Ricardo Misael Ayala Molina, Hyame Assem Alameddine, Makan Pourzandi, Chadi Assi

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02236v1](http://arxiv.org/pdf/2510.02236v1)

**Abstract**: Network Slices (NSs) are virtual networks operating over a shared physical
infrastructure, each designed to meet specific application requirements while
maintaining consistent Quality of Service (QoS). In Fifth Generation (5G)
networks, User Equipment (UE) can connect to and seamlessly switch between
multiple NSs to access diverse services. However, this flexibility, known as
Inter-Slice Switching (ISS), introduces a potential vulnerability that can be
exploited to launch Distributed Slice Mobility (DSM) attacks, a form of
Distributed Denial of Service (DDoS) attack. To secure 5G networks and their
NSs against DSM attacks, we present in this work, PUL-Inter-Slice Defender; an
anomaly detection solution that leverages Positive Unlabeled Learning (PUL) and
incorporates a combination of Long Short-Term Memory Autoencoders and K-Means
clustering. PUL-Inter-Slice Defender leverages the Third Generation Partnership
Project (3GPP) key performance indicators and performance measurement counters
as features for its machine learning models to detect DSM attack variants while
maintaining robustness in the presence of contaminated training data. When
evaluated on data collected from our 5G testbed based on the open-source
free5GC and UERANSIM, a UE/ Radio Access Network (RAN) simulator;
PUL-Inter-Slice Defender achieved F1-scores exceeding 98.50% on training
datasets with 10% to 40% attack contamination, consistently outperforming its
counterpart Inter-Slice Defender and other PUL based solutions combining
One-Class Support Vector Machine (OCSVM) with Random Forest and XGBoost.


### Constraints on New Physics from decays of polarized $Λ_b^0$ baryons at the FCC-ee
**Authors**: Anja Beck, Mero Elmarassy, Asher Sabbagh, Michal Kreps, Eluned Smith

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02225v1](http://arxiv.org/pdf/2510.02225v1)

**Abstract**: The $Z^0$ bosons produced in electron-positron collisions at the potential
Future Circular Collider (FCC-ee) provide unique opportunities for flavour
physics. The non-zero polarization of \Lb baryons produced in $Z^0$ decays
enables access to a much larger set of observables than at the LHC, where the
\Lb baryons are produced unpolarized. This paper presents a toy angular
analysis of $\Lambda_b^0\to \Lambda(\to p\pi^-)\mu^+\mu^-$ decays using
simulation samples of collisions at the FCC-ee reconstructed using the IDEA
detector concept and assuming a dataset of $6\times 10^{12}$ $Z^0$ bosons.
While the statistical sensitivity achieved for individual angular observables
is not expected to significantly exceed that from the LHCb Upgrade II
experiment, the addition of the polarized observables leads to a significant
improvement of the knowledge on the Wilson coefficients $C_9$ and $C_{10}$.


### Multimessenger consistency relations bridging gravitational wave and large scale structure observations
**Authors**: Antonio Enea Romano

**Published Date**: 2025-04-06

**Updated Date**: 2025-10-02

**PDF Url**: [2504.04574v4](http://arxiv.org/pdf/2504.04574v4)

**Abstract**: We show that for Horndeski theories it is possible to derive mathematically
compact consistency relations (CR) between physically observable quantities,
valid for different classes of theories defined by the behavior of the brading
function $\alpha_B$, independent of all other property functions. The CRs
establish a parametrization independent direct relation between the effective
gravitational constant, the slip parameter, the gravitational and
electromagnetic waves (EMW) luminosity distances, the speed of gravitational
waves (GW) and the sound speed. The no-brading CR is also satisfied by general
relativity (GR), and allows to estimate the gravitational coupling from GWs
observations, independently from large scale structure (LSS) observations. A
general, less mathematically compact, consistency condition is also derived,
valid for any form of the function $\alpha_B$ and the other property functions.
We apply the CRs to map the large scale structure observational constraints on
the effective gravitational constant and the slip parameter to GW-EMW distance
ratio constraints, showing that LSS and GWs give independent constraints
consistent with no-brading. Beside allowing to perform parametrization and
model independent tests of the consistency between different constraints on
modified gravity, the CRs allow to probe the value of the effective
gravitational constant with multimessenger observations, independently from LSS
observations.


### Phonon Spin Selective One-Way Axial Phonon Transport in Chiral Nanohelix
**Authors**: Jia Li, Yu-Tao Tan, Yizhou Liu, Jie Ren

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02221v1](http://arxiv.org/pdf/2510.02221v1)

**Abstract**: Selectively exciting and manipulating phonons at nanoscale becomes more and
more important but still remains challenging in modern nano-energy control and
information sensing. Here, we show that the phonon spin angular momentum
provides an extra degree of freedom to achieve versatile manipulation of axial
phonons in nanomaterials via coupling to spinful multi-physical fields, such as
circularly polarized infrared absorption. In particular, we demonstrate the
nanoscale one-way axial phonon excitation and routing in chiral nanomaterials,
by converting the photon spin in circularly polarized optical fields into the
collective interference phonon spin. As exemplified in the smallest chiral
carbon nanotube, we show that the rectification rate can reach nearly 100\%,
achieving an ideal one-way phonon router, which is verified by molecular
dynamics simulations. Our results shed new light on the flexible phonon
manipulation via phonon spin degree of freedom, paving the way for future spin
phononics.


### Quantum Fisher information matrices from Rényi relative entropies
**Authors**: Mark M. Wilde

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02218v1](http://arxiv.org/pdf/2510.02218v1)

**Abstract**: Quantum generalizations of the Fisher information are important in quantum
information science, with applications in high energy and condensed matter
physics and in quantum estimation theory, machine learning, and optimization.
One can derive a quantum generalization of the Fisher information matrix in a
natural way as the Hessian matrix arising in a Taylor expansion of a smooth
divergence. Such an approach is appealing for quantum information theorists,
given the ubiquity of divergences in quantum information theory. In contrast to
the classical case, there is not a unique quantum generalization of the Fisher
information matrix, similar to how there is not a unique quantum generalization
of the relative entropy or the R\'enyi relative entropy. In this paper, I
derive information matrices arising from the log-Euclidean, $\alpha$-$z$, and
geometric R\'enyi relative entropies, with the main technical tool for doing so
being the method of divided differences for calculating matrix derivatives.
Interestingly, for all non-negative values of the R\'enyi parameter $\alpha$,
the log-Euclidean R\'enyi relative entropy leads to the Kubo-Mori information
matrix, and the geometric R\'enyi relative entropy leads to the
right-logarithmic derivative Fisher information matrix. Thus, the resulting
information matrices obey the data-processing inequality for all non-negative
values of the R\'enyi parameter $\alpha$ even though the original quantities do
not. Additionally, I derive and establish basic properties of $\alpha$-$z$
information matrices resulting from the $\alpha$-$z$ R\'enyi relative
entropies. For parameterized thermal states, I establish formulas for their
$\alpha$-$z$ information matrices and hybrid quantum-classical algorithms for
estimating them, with applications in quantum Boltzmann machine learning.


## Diffusion
### NoiseShift: Resolution-Aware Noise Recalibration for Better Low-Resolution Image Generation
**Authors**: Ruozhen He, Moayed Haji-Ali, Ziyan Yang, Vicente Ordonez

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02307v1](http://arxiv.org/pdf/2510.02307v1)

**Abstract**: Text-to-image diffusion models trained on a fixed set of resolutions often
fail to generalize, even when asked to generate images at lower resolutions
than those seen during training. High-resolution text-to-image generators are
currently unable to easily offer an out-of-the-box budget-efficient alternative
to their users who might not need high-resolution images. We identify a key
technical insight in diffusion models that when addressed can help tackle this
limitation: Noise schedulers have unequal perceptual effects across
resolutions. The same level of noise removes disproportionately more signal
from lower-resolution images than from high-resolution images, leading to a
train-test mismatch. We propose NoiseShift, a training-free method that
recalibrates the noise level of the denoiser conditioned on resolution size.
NoiseShift requires no changes to model architecture or sampling schedule and
is compatible with existing models. When applied to Stable Diffusion 3, Stable
Diffusion 3.5, and Flux-Dev, quality at low resolutions is significantly
improved. On LAION-COCO, NoiseShift improves SD3.5 by 15.89%, SD3 by 8.56%, and
Flux-Dev by 2.44% in FID on average. On CelebA, NoiseShift improves SD3.5 by
10.36%, SD3 by 5.19%, and Flux-Dev by 3.02% in FID on average. These results
demonstrate the effectiveness of NoiseShift in mitigating resolution-dependent
artifacts and enhancing the quality of low-resolution image generation.


### Diffusion Models and the Manifold Hypothesis: Log-Domain Smoothing is Geometry Adaptive
**Authors**: Tyler Farghly, Peter Potaptchik, Samuel Howard, George Deligiannidis, Jakiw Pidstrigach

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02305v1](http://arxiv.org/pdf/2510.02305v1)

**Abstract**: Diffusion models have achieved state-of-the-art performance, demonstrating
remarkable generalisation capabilities across diverse domains. However, the
mechanisms underpinning these strong capabilities remain only partially
understood. A leading conjecture, based on the manifold hypothesis, attributes
this success to their ability to adapt to low-dimensional geometric structure
within the data. This work provides evidence for this conjecture, focusing on
how such phenomena could result from the formulation of the learning problem
through score matching. We inspect the role of implicit regularisation by
investigating the effect of smoothing minimisers of the empirical score
matching objective. Our theoretical and empirical results confirm that
smoothing the score function -- or equivalently, smoothing in the log-density
domain -- produces smoothing tangential to the data manifold. In addition, we
show that the manifold along which the diffusion model generalises can be
controlled by choosing an appropriate smoothing.


### Equilibrium Matching: Generative Modeling with Implicit Energy-Based Models
**Authors**: Runqian Wang, Yilun Du

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02300v1](http://arxiv.org/pdf/2510.02300v1)

**Abstract**: We introduce Equilibrium Matching (EqM), a generative modeling framework
built from an equilibrium dynamics perspective. EqM discards the
non-equilibrium, time-conditional dynamics in traditional diffusion and
flow-based generative models and instead learns the equilibrium gradient of an
implicit energy landscape. Through this approach, we can adopt an
optimization-based sampling process at inference time, where samples are
obtained by gradient descent on the learned landscape with adjustable step
sizes, adaptive optimizers, and adaptive compute. EqM surpasses the generation
performance of diffusion/flow models empirically, achieving an FID of 1.90 on
ImageNet 256$\times$256. EqM is also theoretically justified to learn and
sample from the data manifold. Beyond generation, EqM is a flexible framework
that naturally handles tasks including partially noised image denoising, OOD
detection, and image composition. By replacing time-conditional velocities with
a unified equilibrium landscape, EqM offers a tighter bridge between flow and
energy-based models and a simple route to optimization-driven inference.


### Continual Personalization for Diffusion Models
**Authors**: Yu-Chien Liao, Jr-Jen Chen, Chi-Pin Huang, Ci-Siang Lin, Meng-Lin Wu, Yu-Chiang Frank Wang

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02296v1](http://arxiv.org/pdf/2510.02296v1)

**Abstract**: Updating diffusion models in an incremental setting would be practical in
real-world applications yet computationally challenging. We present a novel
learning strategy of Concept Neuron Selection (CNS), a simple yet effective
approach to perform personalization in a continual learning scheme. CNS
uniquely identifies neurons in diffusion models that are closely related to the
target concepts. In order to mitigate catastrophic forgetting problems while
preserving zero-shot text-to-image generation ability, CNS finetunes concept
neurons in an incremental manner and jointly preserves knowledge learned of
previous concepts. Evaluation of real-world datasets demonstrates that CNS
achieves state-of-the-art performance with minimal parameter adjustments,
outperforming previous methods in both single and multi-concept personalization
works. CNS also achieves fusion-free operation, reducing memory storage and
processing time for continual personalization.


### Test-Time Anchoring for Discrete Diffusion Posterior Sampling
**Authors**: Litu Rout, Andreas Lugmayr, Yasamin Jafarian, Srivatsan Varadharajan, Constantine Caramanis, Sanjay Shakkottai, Ira Kemelmacher-Shlizerman

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.02291v1](http://arxiv.org/pdf/2510.02291v1)

**Abstract**: We study the problem of posterior sampling using pretrained discrete
diffusion foundation models, aiming to recover images from noisy measurements
without retraining task-specific models. While diffusion models have achieved
remarkable success in generative modeling, most advances rely on continuous
Gaussian diffusion. In contrast, discrete diffusion offers a unified framework
for jointly modeling categorical data such as text and images. Beyond
unification, discrete diffusion provides faster inference, finer control, and
principled training-free Bayesian inference, making it particularly well-suited
for posterior sampling. However, existing approaches to discrete diffusion
posterior sampling face severe challenges: derivative-free guidance yields
sparse signals, continuous relaxations limit applicability, and split Gibbs
samplers suffer from the curse of dimensionality. To overcome these
limitations, we introduce Anchored Posterior Sampling (APS) for masked
diffusion foundation models, built on two key innovations -- quantized
expectation for gradient-like guidance in discrete embedding space, and
anchored remasking for adaptive decoding. Our approach achieves
state-of-the-art performance among discrete diffusion samplers across linear
and nonlinear inverse problems on the standard benchmarks. We further
demonstrate the benefits of our approach in training-free stylization and
text-guided editing.


## Quantitative Finance
### Mean-field theory of the Santa Fe model revisited: a systematic derivation from an exact BBGKY hierarchy for the zero-intelligence limit-order book model
**Authors**: Taiki Wakatsuki, Kiyoshi Kanazawa

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-02

**PDF Url**: [2510.01814v1](http://arxiv.org/pdf/2510.01814v1)

**Abstract**: The Santa Fe model is an established econophysics model for describing
stochastic dynamics of the limit order book from the viewpoint of the
zero-intelligence approach. While its foundation was studied by combining a
dimensional analysis and a mean-field theory by E. Smith et al. in Quantitative
Finance 2003, their arguments are rather heuristic and lack solid mathematical
foundation; indeed, their mean-field equations were derived with heuristic
arguments and their solutions were not explicitly obtained. In this work, we
revisit the mean-field theory of the Santa Fe model from the viewpoint of
kinetic theory -- a traditional mathematical program in statistical physics. We
study the exact master equation for the Santa Fe model and systematically
derive the Bogoliubov-Born-Green-Kirkwood-Yvon (BBGKY) hierarchical equation.
By applying the mean-field approximation, we derive the mean-field equation for
the order-book density profile, parallel to the Boltzmann equation in
conventional statistical physics. Furthermore, we obtain explicit and closed
expression of the mean-field solutions. Our solutions have several
implications: (1)Our scaling formulas are available for both $\mu\to 0$ and
$\mu\to \infty$ asymptotics, where $\mu$ is the market-order submission
intensity. Particularly, the mean-field theory works very well for small $\mu$,
while its validity is partially limited for large $\mu$. (2)The ``method of
image'' solution, heuristically derived by Bouchaud-M\'ezard-Potters in
Quantitative Finance 2002, is obtained for large $\mu$, serving as a
mathematical foundation for their heuristic arguments. (3)Finally, we point out
an error in E. Smith et al. 2003 in the scaling law for the diffusion constant
due to a misspecification in their dimensional analysis.


