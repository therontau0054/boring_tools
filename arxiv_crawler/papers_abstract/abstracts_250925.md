# Abstracts of Papers

## Physics
### Directly Probing Neutrino Interactions through CMB Phase Shift Measurements
**Authors**: Gabriele Montefalcone, Subhajit Ghosh, Kimberly K. Boddy, Daven Wei Ren Ho, Yuhsin Tsai

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20363v1](http://arxiv.org/pdf/2509.20363v1)

**Abstract**: Perturbations in the cosmic neutrino background produce a characteristic
phase shift in the acoustic oscillations imprinted in the anisotropies of the
cosmic microwave background (CMB), providing a unique observational probe of
neutrino physics. In this work, we explore how this phase shift signature is
altered in the presence of neutrino interactions with temperature-dependent
scattering rates, motivated by physical constructions for neutrino
self-interactions and neutrino-dark matter couplings. A key finding is that the
phase shift in these realistic models -- characterized by gradual rather than
instantaneous decoupling -- maintains the same functional form as the
free-streaming template, with only the asymptotic amplitude decreasing for
stronger interactions that delay decoupling. This simple parametrization
enables us to directly constrain neutrino interactions through phase shift
measurements in the temperature and polarization power spectra from CMB
observations. Analyzing the latest data from \textit{Planck}, the Atacama
Cosmology Telescope, and the South Pole Telescope, we derive strong constraints
on the neutrino decoupling redshift. Our global analysis indicates that
neutrinos have been freely streaming since deep within the radiation-dominated
epoch. We also explore flavor-dependent scenarios in which only one neutrino
species interacts. Overall, our work establishes a signature-driven framework
that exploits the clean phase shift signal in the acoustic oscillations of the
CMB as a precise and robust probe of non-standard neutrino interactions in the
early universe.


### Superfluid-Mott transition in a frustrated triangular optical lattice
**Authors**: Mehedi Hasan, Luca Donini, Sompob Shanokprasith, Daniel Braund, Tobias Marozsak, Moritz Epping, Daniel Reed, Max Melchner, Tiffany Harte, Ulrich Schneider

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20352v1](http://arxiv.org/pdf/2509.20352v1)

**Abstract**: Geometric frustration can significantly increase the complexity and richness
of many-body physics and, for instance, suppress antiferromagnetic order in
quantum magnets. Here, we employ ultracold bosonic $^{39}$K atoms in a
triangular optical lattice to study geometric frustration by stabilizing the
gas at the frustrated upper band edge using negative absolute temperatures. We
find that geometric frustration suppresses the critical interaction strength
for the (chiral-)superfluid to Mott insulator ($\chi$-SF-MI) quantum phase
transition by a factor of 2.7(3) and furthermore changes the critical dynamics
of the transition. Although the emergence of coherence during fast ramps from
MI to the ($\chi$-)SF regime is continuous in both cases, for ramps longer than
a few tunnelling times, significant differences emerge. In the \frs case, no
long-range order emerges on the studied timescales, highlighting a
significantly reduced rate or even saturation of the emerging coherence. This
work opens the door to quantum simulations of frustrated systems that are often
intractable by classical simulations.


### Exploring Graph-Transformer Out-of-Distribution Generalization Abilities
**Authors**: Itay Niv, Neta Rabin

**Published Date**: 2025-06-25

**Updated Date**: 2025-09-24

**PDF Url**: [2506.20575v2](http://arxiv.org/pdf/2506.20575v2)

**Abstract**: Deep learning on graphs has shown remarkable success across numerous
applications, including social networks, bio-physics, traffic networks, and
recommendation systems. Regardless of their successes, current methods
frequently depend on the assumption that training and testing data share the
same distribution, a condition rarely met in real-world scenarios. While
graph-transformer (GT) backbones have recently outperformed traditional
message-passing neural networks (MPNNs) in multiple in-distribution (ID)
benchmarks, their effectiveness under distribution shifts remains largely
unexplored. In this work, we address the challenge of out-of-distribution (OOD)
generalization for graph neural networks, with a special focus on the impact of
backbone architecture. We systematically evaluate GT and hybrid backbones in
OOD settings and compare them to MPNNs. To do so, we adapt several leading
domain generalization (DG) algorithms to work with GTs and assess their
performance on a benchmark designed to test a variety of distribution shifts.
Our results reveal that GT and hybrid GT-MPNN backbones demonstrate stronger
generalization ability compared to MPNNs, even without specialized DG
algorithms (on four out of six benchmarks). Additionally, we propose a novel
post-training analysis approach that compares the clustering structure of the
entire ID and OOD test datasets, specifically examining domain alignment and
class separation. Highlighting its model-agnostic design, the method yielded
valuable insights into both GT and MPNN backbones and appears well suited for
broader DG applications beyond graph learning, offering a deeper perspective on
generalization abilities that goes beyond standard accuracy metrics. Together,
our findings highlight the promise of graph-transformers for robust, real-world
graph learning and set a new direction for future research in OOD
generalization.


### Generalizable neural-network parameterization of mesoscale eddies in idealized and global ocean models
**Authors**: Pavel Perezhogin, Alistair Adcroft, Laure Zanna

**Published Date**: 2025-05-13

**Updated Date**: 2025-09-24

**PDF Url**: [2505.08900v6](http://arxiv.org/pdf/2505.08900v6)

**Abstract**: Data-driven methods have become popular to parameterize the effects of
mesoscale eddies in ocean models. However, they perform poorly in
generalization tasks and may require retuning if the grid resolution or ocean
configuration changes. We address the generalization problem by enforcing
physics constraints on a neural network parameterization of mesoscale eddy
fluxes. We found that the local scaling of input and output features helps to
generalize to unseen grid resolutions and depths offline in the global ocean.
The scaling is based on dimensional analysis and incorporates grid spacing as a
length scale. We formulate our findings as a general algorithm that can be used
to enforce data-driven parameterizations with dimensional scaling. The new
parameterization improves the representation of kinetic and potential energy in
online simulations with idealized and global ocean models. Comparison to
baseline parameterizations and impact on global ocean biases are discussed.


### Process-Informed Forecasting of Complex Thermal Dynamics in Pharmaceutical Manufacturing
**Authors**: Ramona Rubini, Siavash Khodakarami, Aniruddha Bora, George Em Karniadakis, Michele Dassisti

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20349v1](http://arxiv.org/pdf/2509.20349v1)

**Abstract**: Accurate time-series forecasting for complex physical systems is the backbone
of modern industrial monitoring and control. While deep learning models excel
at capturing complex dynamics, currently, their deployment is limited due to
physical inconsistency and robustness, hence constraining their reliability in
regulated environments. We introduce process-informed forecasting (PIF) models
for temperature in pharmaceutical lyophilization. We investigate a wide range
of models, from classical ones such as Autoregressive Integrated Moving Average
Model (ARIMA) and Exponential Smoothing Model (ETS), to modern deep learning
architectures, including Kolmogorov-Arnold Networks (KANs). We compare three
different loss function formulations that integrate a process-informed
trajectory prior: a fixed-weight loss, a dynamic uncertainty-based loss, and a
Residual-Based Attention (RBA) mechanism. We evaluate all models not only for
accuracy and physical consistency but also for robustness to sensor noise.
Furthermore, we test the practical generalizability of the best model in a
transfer learning scenario on a new process. Our results show that PIF models
outperform their data-driven counterparts in terms of accuracy, physical
plausibility and noise resilience. This work provides a roadmap for developing
reliable and generalizable forecasting solutions for critical applications in
the pharmaceutical manufacturing landscape.


### Quantum speed limits based on Jensen-Shannon and Jeffreys divergences for general physical processes
**Authors**: Jucelino Ferreira de Sousa, Diego Paiva Pires

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20347v1](http://arxiv.org/pdf/2509.20347v1)

**Abstract**: We discuss quantum speed limits (QSLs) for finite-dimensional quantum systems
undergoing a general physical process. These QSLs were obtained using two
families of entropic measures, namely the square root of the Jensen-Shannon
divergence, which in turn defines a faithful distance of quantum states, and
the square root of the quantum Jeffreys divergence. The results apply to both
closed and open quantum systems, and are evaluated in terms of the Schatten
speed of the evolved state, as well as cost functions that depend on the
smallest and largest eigenvalues of both initial and instantaneous states of
the quantum system. To illustrate our findings, we focus on the unitary and
nonunitary dynamics of mixed single-qubit states. In the first case, we obtain
speed limits $\textit{\`{a} la}$ Mandelstam-Tamm that are inversely
proportional to the variance of the Hamiltonian driving the evolution. In the
second case, we set the nonunitary dynamics to be described by the noisy
operations: depolarizing channel, phase damping channel, and generalized
amplitude damping channel. We provide analytical results for the two entropic
measures, present numerical simulations to support our results on the speed
limits, comment on the tightness of the bounds, and provide a comparison with
previous QSLs. Our results may find applications in the study of quantum
thermodynamics, entropic uncertainty relations, and also complexity of
many-body systems.


### Video models are zero-shot learners and reasoners
**Authors**: Thaddäus Wiedemer, Yuxuan Li, Paul Vicol, Shixiang Shane Gu, Nick Matarese, Kevin Swersky, Been Kim, Priyank Jaini, Robert Geirhos

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20328v1](http://arxiv.org/pdf/2509.20328v1)

**Abstract**: The remarkable zero-shot capabilities of Large Language Models (LLMs) have
propelled natural language processing from task-specific models to unified,
generalist foundation models. This transformation emerged from simple
primitives: large, generative models trained on web-scale data. Curiously, the
same primitives apply to today's generative video models. Could video models be
on a trajectory towards general-purpose vision understanding, much like LLMs
developed general-purpose language understanding? We demonstrate that Veo 3 can
solve a broad variety of tasks it wasn't explicitly trained for: segmenting
objects, detecting edges, editing images, understanding physical properties,
recognizing object affordances, simulating tool use, and more. These abilities
to perceive, model, and manipulate the visual world enable early forms of
visual reasoning like maze and symmetry solving. Veo's emergent zero-shot
capabilities indicate that video models are on a path to becoming unified,
generalist vision foundation models.


### Deep learning for exoplanet detection and characterization by direct imaging at high contrast
**Authors**: Théo Bodrito, Olivier Flasseur, Julien Mairal, Jean Ponce, Maud Langlois, Anne-Marie Lagrange

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20310v1](http://arxiv.org/pdf/2509.20310v1)

**Abstract**: Exoplanet imaging is a major challenge in astrophysics due to the need for
high angular resolution and high contrast. We present a multi-scale statistical
model for the nuisance component corrupting multivariate image series at high
contrast. Integrated into a learnable architecture, it leverages the physics of
the problem and enables the fusion of multiple observations of the same star in
a way that is optimal in terms of detection signal-to-noise ratio. Applied to
data from the VLT/SPHERE instrument, the method significantly improves the
detection sensitivity and the accuracy of astrometric and photometric
estimation.


### Efficient Microcanonical Histogram Analysis and Application to Peptide Aggregation
**Authors**: Michael Bachmann

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20305v1](http://arxiv.org/pdf/2509.20305v1)

**Abstract**: A novel approach designed to directly estimate microcanonical quantities from
energy histograms is proposed, which enables the immediate systematic
identification and classification of phase transitions in physical systems of
any size by means of the recently introduced generalized microcanonical
inflection-point analysis method. The application to the aggregation problem of
GNNQQNY heptapeptides, for which the entire transition sequence is revealed,
shows the power of this promising method.


## Diffusion
### AnchDrive: Bootstrapping Diffusion Policies with Hybrid Trajectory Anchors for End-to-End Driving
**Authors**: Jinhao Chai, Anqing Jiang, Hao Jiang, Shiyi Mu, Zichong Gu, Shugong Xu

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20253v1](http://arxiv.org/pdf/2509.20253v1)

**Abstract**: End-to-end multi-modal planning has become a transformative paradigm in
autonomous driving, effectively addressing behavioral multi-modality and the
generalization challenge in long-tail scenarios. We propose AnchDrive, a
framework for end-to-end driving that effectively bootstraps a diffusion policy
to mitigate the high computational cost of traditional generative models.
Rather than denoising from pure noise, AnchDrive initializes its planner with a
rich set of hybrid trajectory anchors. These anchors are derived from two
complementary sources: a static vocabulary of general driving priors and a set
of dynamic, context-aware trajectories. The dynamic trajectories are decoded in
real-time by a Transformer that processes dense and sparse perceptual features.
The diffusion model then learns to refine these anchors by predicting a
distribution of trajectory offsets, enabling fine-grained refinement. This
anchor-based bootstrapping design allows for efficient generation of diverse,
high-quality trajectories. Experiments on the NAVSIM benchmark confirm that
AnchDrive sets a new state-of-the-art and shows strong gen?eralizability


### Latent Wavelet Diffusion For Ultra-High-Resolution Image Synthesis
**Authors**: Luigi Sigillo, Shengfeng He, Danilo Comminiello

**Published Date**: 2025-05-31

**Updated Date**: 2025-09-24

**PDF Url**: [2506.00433v3](http://arxiv.org/pdf/2506.00433v3)

**Abstract**: High-resolution image synthesis remains a core challenge in generative
modeling, particularly in balancing computational efficiency with the
preservation of fine-grained visual detail. We present Latent Wavelet Diffusion
(LWD), a lightweight training framework that significantly improves detail and
texture fidelity in ultra-high-resolution (2K-4K) image synthesis. LWD
introduces a novel, frequency-aware masking strategy derived from wavelet
energy maps, which dynamically focuses the training process on detail-rich
regions of the latent space. This is complemented by a scale-consistent VAE
objective to ensure high spectral fidelity. The primary advantage of our
approach is its efficiency: LWD requires no architectural modifications and
adds zero additional cost during inference, making it a practical solution for
scaling existing models. Across multiple strong baselines, LWD consistently
improves perceptual quality and FID scores, demonstrating the power of
signal-driven supervision as a principled and efficient path toward
high-resolution generative modeling.


### Diffusion Curriculum: Synthetic-to-Real Generative Curriculum Learning via Image-Guided Diffusion
**Authors**: Yijun Liang, Shweta Bhardwaj, Tianyi Zhou

**Published Date**: 2024-10-17

**Updated Date**: 2025-09-24

**PDF Url**: [2410.13674v3](http://arxiv.org/pdf/2410.13674v3)

**Abstract**: Low-quality or scarce data has posed significant challenges for training deep
neural networks in practice. While classical data augmentation cannot
contribute very different new data, diffusion models opens up a new door to
build self-evolving AI by generating high-quality and diverse synthetic data
through text-guided prompts. However, text-only guidance cannot control
synthetic images' proximity to the original images, resulting in
out-of-distribution data detrimental to the model performance. To overcome the
limitation, we study image guidance to achieve a spectrum of interpolations
between synthetic and real images. With stronger image guidance, the generated
images are similar to the training data but hard to learn. While with weaker
image guidance, the synthetic images will be easier for model but contribute to
a larger distribution gap with the original data. The generated full spectrum
of data enables us to build a novel "Diffusion Curriculum (DisCL)". DisCL
adjusts the image guidance level of image synthesis for each training stage: It
identifies and focuses on hard samples for the model and assesses the most
effective guidance level of synthetic images to improve hard data learning. We
apply DisCL to two challenging tasks: long-tail (LT) classification and
learning from low-quality data. It focuses on lower-guidance images of
high-quality to learn prototypical features as a warm-up of learning
higher-guidance images that might be weak on diversity or quality. Extensive
experiments showcase a gain of 2.7% and 2.1% in OOD and ID macro-accuracy when
applying DisCL to iWildCam dataset. On ImageNet-LT, DisCL improves the base
model's tail-class accuracy from 4.4% to 23.64% and leads to a 4.02%
improvement in all-class accuracy.


### Learning hidden cascades via classification
**Authors**: Derrick Gilchrist Edward Manoharan, Anubha Goel, Alexandros Iosifidis, Henri Hansen, Juho Kanniainen

**Published Date**: 2025-05-16

**Updated Date**: 2025-09-24

**PDF Url**: [2505.11228v3](http://arxiv.org/pdf/2505.11228v3)

**Abstract**: The spreading dynamics in social networks are often studied under the
assumption that individuals' statuses, whether informed or infected, are fully
observable. However, in many real-world situations, such statuses remain
unobservable, which is crucial for determining an individual's potential to
further spread the infection. While final statuses are hidden, intermediate
indicators such as symptoms of infection are observable and provide useful
representations of the underlying diffusion process. We propose a partial
observability-aware Machine Learning framework to learn the characteristics of
the spreading model. We term the method Distribution Classification, which
utilizes the power of classifiers to infer the underlying transmission
dynamics. Through extensive benchmarking against Approximate Bayesian
Computation and GNN-based baselines, our framework consistently outperforms
these state-of-the-art methods, delivering accurate parameter estimates across
diverse diffusion settings while scaling efficiently to large networks. We
validate the method on synthetic networks and extend the study to a real-world
insider trading network, demonstrating its effectiveness in analyzing spreading
phenomena where direct observation of individual statuses is not possible.


### KSDiff: Keyframe-Augmented Speech-Aware Dual-Path Diffusion for Facial Animation
**Authors**: Tianle Lyu, Junchuan Zhao, Ye Wang

**Published Date**: 2025-09-24

**Updated Date**: 2025-09-24

**PDF Url**: [2509.20128v1](http://arxiv.org/pdf/2509.20128v1)

**Abstract**: Audio-driven facial animation has made significant progress in multimedia
applications, with diffusion models showing strong potential for talking-face
synthesis. However, most existing works treat speech features as a monolithic
representation and fail to capture their fine-grained roles in driving
different facial motions, while also overlooking the importance of modeling
keyframes with intense dynamics. To address these limitations, we propose
KSDiff, a Keyframe-Augmented Speech-Aware Dual-Path Diffusion framework.
Specifically, the raw audio and transcript are processed by a Dual-Path Speech
Encoder (DPSE) to disentangle expression-related and head-pose-related
features, while an autoregressive Keyframe Establishment Learning (KEL) module
predicts the most salient motion frames. These components are integrated into a
Dual-path Motion generator to synthesize coherent and realistic facial motions.
Extensive experiments on HDTF and VoxCeleb demonstrate that KSDiff achieves
state-of-the-art performance, with improvements in both lip synchronization
accuracy and head-pose naturalness. Our results highlight the effectiveness of
combining speech disentanglement with keyframe-aware diffusion for talking-head
generation.


