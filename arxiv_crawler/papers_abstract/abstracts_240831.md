# Abstracts of Papers

## Physics
### An algebraic characterisation of Kochen-Specker contextuality
**Authors**: Markus Frembs

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16764v1](http://arxiv.org/pdf/2408.16764v1)

**Abstract**: Contextuality is a key distinguishing feature between classical and quantum
physics. It expresses a fundamental obstruction to describing quantum theory
using classical concepts. In turn, understood as a resource for quantum
computation, it is expected to hold the key to quantum advantage. Yet, despite
its long recognised importance in quantum foundations and, more recently, in
quantum computation, the structural essence of contextuality has remained
somewhat elusive - different frameworks address different aspects of the
phenomenon, yet their precise relationship often remains unclear. This issue
already looms large at the level of the Bell-Kochen-Specker theorem: while
traditional proofs proceed by showing the nonexistence of valuations, the
notion of state-independent contextuality in the marginal approach allows to
prove contextuality from seemingly weaker assumptions. In the light of this,
and at the absence of a unified mathematical framework for Kochen-Specker
contextuality, the original algebraic approach has been widely abandoned, in
favour of the study of contextual correlations.
  Here, we reinstate the algebraic perspective on contextuality. Concretely, by
building on the novel concept of context connections, we reformulate the
algebraic relations between observables originally postulated by Kochen and
Specker, and we explicitly demonstrate their consistency with the notion of
state-independent contextuality. In the present paper, we focus on the new
conceptual ideas and discuss them in the concrete setting of spin-1
observables, specifically those in the example of [S. Yu and C.H. Oh, Phys.
Rev. Lett., 108, 030402 (2012)]; in a companion paper, we generalise these
ideas, obtain a complete characterisation of Kochen-Specker contextuality and
provide a detailed comparison with the related notions of contextuality in the
marginal and graph-theoretic approach.


### Conditional score-based diffusion models for solving inverse problems in mechanics
**Authors**: Agnimitra Dasgupta, Harisankar Ramaswamy, Javier Murgoitio-Esandi, Ken Foo, Runze Li, Qifa Zhou, Brendan Kennedy, Assad Oberai

**Published Date**: 2024-06-19

**Updated Date**: 2024-08-29

**PDF Url**: [2406.13154v3](http://arxiv.org/pdf/2406.13154v3)

**Abstract**: We propose a framework to perform Bayesian inference using conditional
score-based diffusion models to solve a class of inverse problems in mechanics
involving the inference of a specimen's spatially varying material properties
from noisy measurements of its mechanical response to loading. Conditional
score-based diffusion models are generative models that learn to approximate
the score function of a conditional distribution using samples from the joint
distribution. More specifically, the score functions corresponding to multiple
realizations of the measurement are approximated using a single neural network,
the so-called score network, which is subsequently used to sample the posterior
distribution using an appropriate Markov chain Monte Carlo scheme based on
Langevin dynamics. Training the score network only requires simulating the
forward model. Hence, the proposed approach can accommodate black-box forward
models and complex measurement noise. Moreover, once the score network has been
trained, it can be re-used to solve the inverse problem for different
realizations of the measurements. We demonstrate the efficacy of the proposed
approach on a suite of high-dimensional inverse problems in mechanics that
involve inferring heterogeneous material properties from noisy measurements.
Some examples we consider involve synthetic data, while others include data
collected from actual elastography experiments. Further, our applications
demonstrate that the proposed approach can handle different measurement
modalities, complex patterns in the inferred quantities, non-Gaussian and
non-additive noise models, and nonlinear black-box forward models. The results
show that the proposed framework can solve large-scale physics-based inverse
problems efficiently.


### Data-driven reduced order modeling of a two-layer quasi-geostrophic ocean model
**Authors**: Lander Besabe, Michele Girfoglio, Annalisa Quaini, Gianluigi Rozza

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16723v1](http://arxiv.org/pdf/2408.16723v1)

**Abstract**: The two-layer quasi-geostrophic equations (2QGE) is a simplified model that
describes the dynamics of a stratified, wind-driven ocean in terms of potential
vorticity and stream function. Its numerical simulation is plagued by a high
computational cost due to the size of the typical computational domain and the
need for high resolution to capture the full spectrum of turbulent scales. In
this paper, we present a data-driven reduced order model (ROM) for the 2QGE
that drastically reduces the computational time to predict ocean dynamics,
especially when there are variable physical parameters. The main building
blocks of our ROM are: i) proper orthogonal decomposition (POD) and ii) long
short-term memory (LSTM) recurrent neural networks. Snapshots data are
collected from a high-resolution simulation for part of the time interval of
interest and for given parameter values in the case of variable parameters. POD
is applied to each field variable to extract the dominant modes and a LSTM
model is trained on the modal coefficients associated with the snapshots for
each variable. Then, the trained LSTM models predict the modal coefficients for
the remaining part of the time interval of interest and for a new parameter
value. To illustrate the predictive performance of our POD-LSTM ROM and the
corresponding time savings, we consider an extension of the so-called
double-gyre wind forcing test. We show that the POD-LSTM ROM is accurate in
predicting both time-averaged fields and time-dependent quantities (modal
coefficients, enstrophy, and kinetic energy), even when retaining only 10-20\%
of the singular value energy of the system. The computational speed up for the
prediction is about up to 1E+07 compared to a finite volume based full order
method.


### Correlators of long strings on AdS$_3\times$S$^3\times$T$^4$
**Authors**: Zhe-fei Yu, Cheng Peng

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16712v1](http://arxiv.org/pdf/2408.16712v1)

**Abstract**: In this work, we calculate correlators of long strings on
AdS$_3\times$S$^3\times$T$^4$ with pure NS-NS flux. We first construct physical
vertex operators that correspond to long strings. Due to the GSO projection,
they depend on the parity of the spectral flow parameter $w$. For a given $w$,
we construct the physical operators that have the lowest space-time weights in
both the NS and R sector. Then, we calculate three point correlators for each
possible type of parities of spectral flows. We find that the recursion
relations of correlators in the bosonic SL$(2,\mathbb{R})$ WZW model can be
understood from the equivalence of these superstring correlators with different
picture choices. Furthermore, after carefully mapping the vertex operators to
appropriate operators in the dual CFT, we find that once the fermionic
contributions together with the picture changing effects are correctly taken
into account, some mathematical identities of covering maps lead to the
matching of the correlators of the two sides. We check this explicitly at the
leading order in the conformal perturbation computation and conjecture that
this remains correct to all orders.


### Kinematic Varieties for Massless Particles
**Authors**: Smita Rajan, Svala Sverrisdóttir, Bernd Sturmfels

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16711v1](http://arxiv.org/pdf/2408.16711v1)

**Abstract**: We study algebraic varieties that encode the kinematic data for $n$ massless
particles in $d$-dimensional spacetime subject to momentum conservation. Their
coordinates are spinor brackets, which we derive from the Clifford algebra
associated to the Lorentz group. This was proposed for $d=5$ in the recent
physics literature. Our kinematic varieties are given by polynomial constraints
on tensors with both symmetric and skew symmetric slices.


### SympGNNs: Symplectic Graph Neural Networks for identifiying high-dimensional Hamiltonian systems and node classification
**Authors**: Alan John Varghese, Zhen Zhang, George Em Karniadakis

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16698v1](http://arxiv.org/pdf/2408.16698v1)

**Abstract**: Existing neural network models to learn Hamiltonian systems, such as
SympNets, although accurate in low-dimensions, struggle to learn the correct
dynamics for high-dimensional many-body systems. Herein, we introduce
Symplectic Graph Neural Networks (SympGNNs) that can effectively handle system
identification in high-dimensional Hamiltonian systems, as well as node
classification. SympGNNs combines symplectic maps with permutation
equivariance, a property of graph neural networks. Specifically, we propose two
variants of SympGNNs: i) G-SympGNN and ii) LA-SympGNN, arising from different
parameterizations of the kinetic and potential energy. We demonstrate the
capabilities of SympGNN on two physical examples: a 40-particle coupled
Harmonic oscillator, and a 2000-particle molecular dynamics simulation in a
two-dimensional Lennard-Jones potential. Furthermore, we demonstrate the
performance of SympGNN in the node classification task, achieving accuracy
comparable to the state-of-the-art. We also empirically show that SympGNN can
overcome the oversmoothing and heterophily problems, two key challenges in the
field of graph neural networks.


### Ultrathin natural biotite crystals as a dielectric layer for van der Waals heterostructure applications
**Authors**: Raphaela de Oliveira, Ana Beatriz Yoshida, Cesar Rabahi, Raul O. Freitas, Christiano J. S. de Matos, Yara Galvão Gobato, Ingrid D. Barcelos, Alisson R. Cadore

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16697v1](http://arxiv.org/pdf/2408.16697v1)

**Abstract**: Biotite, an iron-rich mineral belonging to the trioctahedral mica group, is a
naturally abundant layered material (LM) exhibiting attractive electronic
properties for application in nanodevices. Biotite stands out as a
non-degradable LM under ambient conditions, featuring high-quality basal
cleavage, a significant advantage for van der Waals heterostructure (vdWH)
applications. In this work, we present the micro-mechanical exfoliation of
biotite down to monolayers (1Ls), yielding ultrathin flakes with large areas
and atomically flat surfaces. To identify and characterize the mineral, we
conducted a multi-elemental analysis of biotite using energy-dispersive
spectroscopy mapping. Additionally, synchrotron infrared nano-spectroscopy was
employed to probe its vibrational signature in few-layer form, with sensitivity
to the layer number. We have also observed good morphological and structural
stability in time (up to 12 months) and no important changes in their physical
properties after thermal annealing processes in ultrathin biotite flakes.
Conductive atomic force microscopy evaluated its electrical capacity, revealing
an electrical breakdown strength of approximately 1 V/nm. Finally, we explore
the use of biotite as a substrate and encapsulating LM in vdWH applications. We
have performed optical and magneto-optical measurements at low temperatures. We
find that ultrathin biotite flakes work as a good substrate for 1L-MoSe2,
comparable to hexagonal boron nitride flakes, but it induces a small change of
the 1L-MoSe2 g-factor values, most likely due to natural impurities on its
crystal structure. Furthermore, our results show that biotite flakes are useful
systems to protect sensitive LMs such as black phosphorus from degradation for
up to 60 days in ambient air. Our study introduces biotite as a promising,
cost-effective LM for the advancement of future ultrathin nanotechnologies.


### On Nucleon "Radii"
**Authors**: Vladimir A. Petrov

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16679v1](http://arxiv.org/pdf/2408.16679v1)

**Abstract**: We show that various nucleon "radii" that appear in the literature,
e.g."charge", "gravitational", "mass" or "mechanical, do not have a direct
geometric meaning and do not give an idea of the physical size of the nucleon.
In the framework of the Gribov parton scheme we show that at high enough energy
the gluon cloud of the nucleon shows up and begins to define the interaction
region of nucleon-nucleon scattering.


### Intersection Numbers from Companion Tensor Algebra
**Authors**: Giacomo Brunello, Vsevolod Chestnov, Pierpaolo Mastrolia

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16668v1](http://arxiv.org/pdf/2408.16668v1)

**Abstract**: Twisted period integrals are ubiquitous in theoretical physics and
mathematics, where they inhabit a finite-dimensional vector space governed by
an inner product known as the intersection number. In this work, we uncover the
associated tensor structures of intersection numbers and integrate them with
the fibration method to develop a novel and efficient evaluation scheme.
Companion matrices allow us to cast the computation of the intersection numbers
in terms of a matrix operator calculus within the ambient tensor space. Our
algorithm has been successfully applied to the decomposition of two-loop
five-point massless functions, representing a significant advancement for the
direct projection of Feynman integrals to master integrals via intersection
numbers.


### In-situ scanning gate imaging of individual two-level material defects in live superconducting quantum circuits
**Authors**: M. Hegedüs, R. Banerjee, A. Hutcheson, T. Barker, S. Mahashabde, A. V. Danilov, S. E. Kubatkin, V. Antonov, S. E. de Graaf

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16660v1](http://arxiv.org/pdf/2408.16660v1)

**Abstract**: The low temperature physics of structurally amorphous materials is governed
by two-level system defects (TLS), the exact origin and nature of which remain
elusive despite decades of study. Recent advances towards realising stable
high-coherence platforms for quantum computing has increased the importance of
studying TLS in solid-state quantum circuits, as they are a persistent source
of decoherence and instability. Here we perform scanning gate microscopy on a
live superconducting quantum circuit at millikelvin temperatures to locate
individual TLS. Our method directly reveals the microscopic nature of TLS and
is also capable of deducing the three dimensional orientation of individual TLS
electric dipole moments. Such insights, when combined with structural
information of the underlying materials, can help unravel the detailed
microscopic nature and chemical origin of TLS, directing strategies for their
eventual mitigation.


## Diffusion
### ReconX: Reconstruct Any Scene from Sparse Views with Video Diffusion Model
**Authors**: Fangfu Liu, Wenqiang Sun, Hanyang Wang, Yikai Wang, Haowen Sun, Junliang Ye, Jun Zhang, Yueqi Duan

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16767v1](http://arxiv.org/pdf/2408.16767v1)

**Abstract**: Advancements in 3D scene reconstruction have transformed 2D images from the
real world into 3D models, producing realistic 3D results from hundreds of
input photos. Despite great success in dense-view reconstruction scenarios,
rendering a detailed scene from insufficient captured views is still an
ill-posed optimization problem, often resulting in artifacts and distortions in
unseen areas. In this paper, we propose ReconX, a novel 3D scene reconstruction
paradigm that reframes the ambiguous reconstruction challenge as a temporal
generation task. The key insight is to unleash the strong generative prior of
large pre-trained video diffusion models for sparse-view reconstruction.
However, 3D view consistency struggles to be accurately preserved in directly
generated video frames from pre-trained models. To address this, given limited
input views, the proposed ReconX first constructs a global point cloud and
encodes it into a contextual space as the 3D structure condition. Guided by the
condition, the video diffusion model then synthesizes video frames that are
both detail-preserved and exhibit a high degree of 3D consistency, ensuring the
coherence of the scene from various perspectives. Finally, we recover the 3D
scene from the generated video through a confidence-aware 3D Gaussian Splatting
optimization scheme. Extensive experiments on various real-world datasets show
the superiority of our ReconX over state-of-the-art methods in terms of quality
and generalizability.


### A Score-Based Density Formula, with Applications in Diffusion Generative Models
**Authors**: Gen Li, Yuling Yan

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16765v1](http://arxiv.org/pdf/2408.16765v1)

**Abstract**: Score-based generative models (SGMs) have revolutionized the field of
generative modeling, achieving unprecedented success in generating realistic
and diverse content. Despite empirical advances, the theoretical basis for why
optimizing the evidence lower bound (ELBO) on the log-likelihood is effective
for training diffusion generative models, such as DDPMs, remains largely
unexplored. In this paper, we address this question by establishing a density
formula for a continuous-time diffusion process, which can be viewed as the
continuous-time limit of the forward process in an SGM. This formula reveals
the connection between the target density and the score function associated
with each step of the forward process. Building on this, we demonstrate that
the minimizer of the optimization objective for training DDPMs nearly coincides
with that of the true objective, providing a theoretical foundation for
optimizing DDPMs using the ELBO. Furthermore, we offer new insights into the
role of score-matching regularization in training GANs, the use of ELBO in
diffusion classifiers, and the recently proposed diffusion loss.


### UV-free Texture Generation with Denoising and Geodesic Heat Diffusions
**Authors**: Simone Foti, Stefanos Zafeiriou, Tolga Birdal

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16762v1](http://arxiv.org/pdf/2408.16762v1)

**Abstract**: Seams, distortions, wasted UV space, vertex-duplication, and varying
resolution over the surface are the most prominent issues of the standard
UV-based texturing of meshes. These issues are particularly acute when
automatic UV-unwrapping techniques are used. For this reason, instead of
generating textures in automatically generated UV-planes like most
state-of-the-art methods, we propose to represent textures as coloured
point-clouds whose colours are generated by a denoising diffusion probabilistic
model constrained to operate on the surface of 3D objects. Our sampling and
resolution agnostic generative model heavily relies on heat diffusion over the
surface of the meshes for spatial communication between points. To enable
processing of arbitrarily sampled point-cloud textures and ensure long-distance
texture consistency we introduce a fast re-sampling of the mesh spectral
properties used during the heat diffusion and introduce a novel
heat-diffusion-based self-attention mechanism. Our code and pre-trained models
are available at github.com/simofoti/UV3-TeD.


### DriveGenVLM: Real-world Video Generation for Vision Language Model based Autonomous Driving
**Authors**: Yongjie Fu, Anmol Jain, Xuan Di, Xu Chen, Zhaobin Mo

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16647v1](http://arxiv.org/pdf/2408.16647v1)

**Abstract**: The advancement of autonomous driving technologies necessitates increasingly
sophisticated methods for understanding and predicting real-world scenarios.
Vision language models (VLMs) are emerging as revolutionary tools with
significant potential to influence autonomous driving. In this paper, we
propose the DriveGenVLM framework to generate driving videos and use VLMs to
understand them. To achieve this, we employ a video generation framework
grounded in denoising diffusion probabilistic models (DDPM) aimed at predicting
real-world video sequences. We then explore the adequacy of our generated
videos for use in VLMs by employing a pre-trained model known as Efficient
In-context Learning on Egocentric Videos (EILEV). The diffusion model is
trained with the Waymo open dataset and evaluated using the Fr\'echet Video
Distance (FVD) score to ensure the quality and realism of the generated videos.
Corresponding narrations are provided by EILEV for these generated videos,
which may be beneficial in the autonomous driving domain. These narrations can
enhance traffic scene understanding, aid in navigation, and improve planning
capabilities. The integration of video generation with VLMs in the DriveGenVLM
framework represents a significant step forward in leveraging advanced AI
models to address complex challenges in autonomous driving.


### RLCP: A Reinforcement Learning-based Copyright Protection Method for Text-to-Image Diffusion Model
**Authors**: Zhuan Shi, Jing Yan, Xiaoli Tang, Lingjuan Lyu, Boi Faltings

**Published Date**: 2024-08-29

**Updated Date**: 2024-08-29

**PDF Url**: [2408.16634v1](http://arxiv.org/pdf/2408.16634v1)

**Abstract**: The increasing sophistication of text-to-image generative models has led to
complex challenges in defining and enforcing copyright infringement criteria
and protection. Existing methods, such as watermarking and dataset
deduplication, fail to provide comprehensive solutions due to the lack of
standardized metrics and the inherent complexity of addressing copyright
infringement in diffusion models. To deal with these challenges, we propose a
Reinforcement Learning-based Copyright Protection(RLCP) method for
Text-to-Image Diffusion Model, which minimizes the generation of
copyright-infringing content while maintaining the quality of the
model-generated dataset. Our approach begins with the introduction of a novel
copyright metric grounded in copyright law and court precedents on
infringement. We then utilize the Denoising Diffusion Policy Optimization
(DDPO) framework to guide the model through a multi-step decision-making
process, optimizing it using a reward function that incorporates our proposed
copyright metric. Additionally, we employ KL divergence as a regularization
term to mitigate some failure modes and stabilize RL fine-tuning. Experiments
conducted on 3 mixed datasets of copyright and non-copyright images demonstrate
that our approach significantly reduces copyright infringement risk while
maintaining image quality.


