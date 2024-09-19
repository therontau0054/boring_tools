# Abstracts of Papers

## Physics
### Quantum computational advantage with constant-temperature Gibbs sampling
**Authors**: Thiago Bergamaschi, Chi-Fang Chen, Yunchao Liu

**Published Date**: 2024-04-23

**Updated Date**: 2024-09-18

**PDF Url**: [2404.14639v2](http://arxiv.org/pdf/2404.14639v2)

**Abstract**: A quantum system coupled to a bath at some fixed, finite temperature
converges to its Gibbs state. This thermalization process defines a natural,
physically-motivated model of quantum computation. However, whether quantum
computational advantage can be achieved within this realistic physical setup
has remained open, due to the challenge of finding systems that thermalize
quickly, but are classically intractable. Here we consider sampling from the
measurement outcome distribution of quantum Gibbs states at constant
temperatures, and prove that this task demonstrates quantum computational
advantage. We design a family of commuting local Hamiltonians (parent
Hamiltonians of shallow quantum circuits) and prove that they rapidly converge
to their Gibbs states under the standard physical model of thermalization (as a
continuous-time quantum Markov chain). On the other hand, we show that no
polynomial time classical algorithm can sample from the measurement outcome
distribution by reducing to the classical hardness of sampling from noiseless
shallow quantum circuits. The key step in the reduction is constructing a
fault-tolerance scheme for shallow IQP circuits against input noise.


### AHKASH: a new Hybrid particle-in-cell code for simulations of astrophysical collisionless plasma
**Authors**: Radhika Achikanath Chirakkara, Christoph Federrath, Amit Seta

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12151v1](http://arxiv.org/pdf/2409.12151v1)

**Abstract**: We introduce $\texttt{A}$strophysical $\texttt{H}$ybrid-$\texttt{K}$inetic
simulations with the $\texttt{flASH}$ code ($\texttt{AHKASH}$) -- a new Hybrid
particle-in-cell (PIC) code developed within the framework of the multi-physics
code $\texttt{FLASH}$. The new code uses a second-order accurate Boris
integrator and a predictor-predictor-corrector algorithm for advancing the
Hybrid-kinetic equations, using the constraint transport method to ensure that
magnetic fields are divergence-free. The code supports various interpolation
schemes between the particles and grid cells, with post-interpolation smoothing
to reduce finite particle noise. We further implement a $\delta f$ method to
study instabilities in weakly collisional plasmas. The new code is tested on
standard physical problems such as the motion of charged particles in uniform
and spatially varying magnetic fields, the propagation of Alfv\'en and whistler
waves, and Landau damping of ion acoustic waves. We test different
interpolation kernels and demonstrate the necessity of performing
post-interpolation smoothing. We couple the $\texttt{TurbGen}$ turbulence
driving module to the new Hybrid PIC code, allowing us to test the code on the
highly complex physical problem of the turbulent dynamo. To investigate
steady-state turbulence with a fixed sonic Mach number, it is important to
maintain isothermal plasma conditions. Therefore, we introduce a novel cooling
method for Hybrid PIC codes and provide tests and calibrations of this method
to keep the plasma isothermal. We describe and test the `hybrid precision'
method, which significantly reduces (by a factor $\sim1.5$) the computational
cost, without compromising the accuracy of the numerical solutions. Finally, we
test the parallel scalability of the new code, showing excellent scaling up to
10,000~cores.


### Model-free quantification of completeness, uncertainties, and outliers in atomistic machine learning using information theory
**Authors**: Daniel Schwalbe-Koda, Sebastien Hamel, Babak Sadigh, Fei Zhou, Vincenzo Lordi

**Published Date**: 2024-04-18

**Updated Date**: 2024-09-18

**PDF Url**: [2404.12367v2](http://arxiv.org/pdf/2404.12367v2)

**Abstract**: An accurate description of information is relevant for a range of problems in
atomistic machine learning (ML), such as crafting training sets, performing
uncertainty quantification (UQ), or extracting physical insights from large
datasets. However, atomistic ML often relies on unsupervised learning or model
predictions to analyze information contents from simulation or training data.
Here, we introduce a theoretical framework that provides a rigorous, model-free
tool to quantify information contents in atomistic simulations. We demonstrate
that the information entropy of a distribution of atom-centered environments
explains known heuristics in ML potential developments, from training set sizes
to dataset optimality. Using this tool, we propose a model-free UQ method that
reliably predicts epistemic uncertainty and detects out-of-distribution
samples, including rare events in systems such as nucleation. This method
provides a general tool for data-driven atomistic modeling and combines efforts
in ML, simulations, and physical explainability.


### IMRL: Integrating Visual, Physical, Temporal, and Geometric Representations for Enhanced Food Acquisition
**Authors**: Rui Liu, Zahiruddin Mahammad, Amisha Bhaskar, Pratap Tokekar

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12092v1](http://arxiv.org/pdf/2409.12092v1)

**Abstract**: Robotic assistive feeding holds significant promise for improving the quality
of life for individuals with eating disabilities. However, acquiring diverse
food items under varying conditions and generalizing to unseen food presents
unique challenges. Existing methods that rely on surface-level geometric
information (e.g., bounding box and pose) derived from visual cues (e.g.,
color, shape, and texture) often lacks adaptability and robustness, especially
when foods share similar physical properties but differ in visual appearance.
We employ imitation learning (IL) to learn a policy for food acquisition.
Existing methods employ IL or Reinforcement Learning (RL) to learn a policy
based on off-the-shelf image encoders such as ResNet-50. However, such
representations are not robust and struggle to generalize across diverse
acquisition scenarios. To address these limitations, we propose a novel
approach, IMRL (Integrated Multi-Dimensional Representation Learning), which
integrates visual, physical, temporal, and geometric representations to enhance
the robustness and generalizability of IL for food acquisition. Our approach
captures food types and physical properties (e.g., solid, semi-solid, granular,
liquid, and mixture), models temporal dynamics of acquisition actions, and
introduces geometric information to determine optimal scooping points and
assess bowl fullness. IMRL enables IL to adaptively adjust scooping strategies
based on context, improving the robot's capability to handle diverse food
acquisition scenarios. Experiments on a real robot demonstrate our approach's
robustness and adaptability across various foods and bowl configurations,
including zero-shot generalization to unseen settings. Our approach achieves
improvement up to $35\%$ in success rate compared with the best-performing
baseline.


### Uncovering liquid-substrate fluctuation effects on crystal growth and disordered hyperuniformity of two-dimensional materials
**Authors**: S. K. Mkhonta, Zhi-Feng Huang, K. R. Elder

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12090v1](http://arxiv.org/pdf/2409.12090v1)

**Abstract**: We investigate the growth of two-dimensional (2D) crystals on fluctuating
surfaces using a phase field crystal model that is relevant on atomic length
and diffusive time scales. Motivated by recent experiments which achieved
unprecedented fast growth of large-size high-quality 2D crystals on liquid
substrates, we uncover novel effects of liquid surfaces on microstructural
ordering. We find that substrate fluctuations generate short-ranged noise that
speeds up crystallization and grain growth of the overlayer, surpassing that of
free-standing system. Coupling to the liquid substrate fluctuations can also
modulate local randomness, leading to intriguing disordered structures with
hidden spatial order, i.e., disordered hyperuniformity. These results reveal
the physical mechanisms underlying the fast growth of 2D crystals on liquid
surfaces and demonstrate a novel strategy for synthesizing disordered
hyperuniform thin film structures.


### Unveiling the Secrets of New Physics Through Top Quark Tagging
**Authors**: Rameswar Sahu, Saiyad Ashanujjaman, Kirtiman Ghosh

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12085v1](http://arxiv.org/pdf/2409.12085v1)

**Abstract**: The ubiquity of top-rich final states in the context of beyond the Standard
Model (BSM) searches has led to their status as extensively studied signatures
at the LHC. Over the past decade, numerous endeavours have been undertaken in
the literature to develop methods for efficiently distinguishing boosted top
quark jets from QCD jets. Although cut-based strategies for boosted top
tagging, which rely on substructure information from fat jets resulting from
the hadronic decay of boosted top quarks, were introduced in the literature as
early as 2008, recent years have witnessed a surge in the utilization of
machine learning-based approaches for the classification of top-jets from QCD
jets. The review focuses on the present status of boosted top tagging and its
application for BSM searchers.


### The $η_c$-meson leading-twist distribution amplitude
**Authors**: Benoît Blossier, Mariane Mangin-Brinet, José Manuel Morgado Chávez, Teseo San José

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12084v1](http://arxiv.org/pdf/2409.12084v1)

**Abstract**: In this project, we employ the short-distance factorization to compute the
distribution amplitude of the $\eta_c$-meson from Lattice QCD at leading twist.
We employ a set of CLS $N_f=2$ ensembles at three lattice spacings and various
quark masses to extrapolate the pseudo distribution to the physical point in
the isospin limit. We solve the inverse problem modeling the distribution
amplitude, and we match our results to the light-cone in the
$\overline{\text{MS}}$-scheme. We include a complete error budget, and we
compare to two alternative approaches: non-relativistic QCD and Dyson-Schwinger
equations, finding good agreement with the latter but not with the former.


### First constraint on the dissipative tidal deformability of neutron stars
**Authors**: Justin L. Ripley, Abhishek Hegade K. R., Rohit S. Chandramouli, and Nicolas Yunes

**Published Date**: 2023-12-18

**Updated Date**: 2024-09-18

**PDF Url**: [2312.11659v3](http://arxiv.org/pdf/2312.11659v3)

**Abstract**: The gravitational waves (GWs) emitted by neutron star binaries probe the
physics of matter at supra nuclear densities. During the late inspiral, tidal
deformations raised on each star by the gravitational field of its companion
depend crucially on the star's internal properties. The misalignment of a
star's tidal bulge with its companion's gravitational field encodes the
strength of internal dissipative processes, which imprint onto the phase of the
gravitational waves emitted. We here analyze GW data from the GW170817 (binary
neutron star) event detected by LIGO and Virgo and find the first constraint on
the dissipative tidal deformability of a neutron star. From this constraint,
\emph{assuming} a temperature profile for each star in the binary, we obtain an
order of magnitude bound on the averaged bulk ($\zeta$) and shear ($\eta$)
viscosity of each star during the inspiral.: $\zeta \lesssim 10^{31}
\mathrm{g}\;\mathrm{cm}^{-1}\mathrm{s}^{-1}$ and $\eta \lesssim 10^{28}
\mathrm{g}\;\mathrm{cm}^{-1}\mathrm{s}^{-1} $. We forecast that these bounds
could be improved by two orders of magnitude with third-generation detectors,
like Cosmic Explorer, using inspiral data. These constraints already inform
nuclear physics models and motivate further theoretical work to better
understand the interplay between viscosity and temperature in the late inspiral
of neutron stars.


### Optimal light cone for macroscopic particle transport in long-range systems: A quantum speed limit approach
**Authors**: Tan Van Vu, Tomotaka Kuwahara, Keiji Saito

**Published Date**: 2023-07-03

**Updated Date**: 2024-09-18

**PDF Url**: [2307.01059v2](http://arxiv.org/pdf/2307.01059v2)

**Abstract**: Understanding the ultimate rate at which information propagates is a pivotal
issue in nonequilibrium physics. Nevertheless, the task of elucidating the
propagation speed inherent in quantum bosonic systems presents challenges due
to the unbounded nature of their interactions. In this study, we tackle the
problem of macroscopic particle transport in a long-range generalization of the
lattice Bose-Hubbard model through the lens of the quantum speed limit. By
developing a unified approach based on optimal transport theory, we rigorously
prove that the minimum time required for macroscopic particle transport is
always bounded by the distance between the source and target regions, while
retaining its significance even in the thermodynamic limit. Furthermore, we
derive an upper bound for the probability of observing a specific number of
bosons inside the target region, thereby providing additional insights into the
dynamics of particle transport. Our results hold true for arbitrary initial
states under both long-range hopping and long-range interactions, thus
resolving an open problem of particle transport in generic bosonic systems.


### Doppler-free selective reflection spectroscopy of electric-quadrupole transitions
**Authors**: Eng Aik Chan, Syed Abdullah Aljunid, Athanasios Laliotis, David Wilkowski, Martial Ducloy

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12017v1](http://arxiv.org/pdf/2409.12017v1)

**Abstract**: Electric-dipole-forbidden transitions play an important role as in quantum
sensing, quantum information, and fundamental test in physics. As such, the
development of novel and sensitive spectroscopic methods is of major interest.
Here, we present a Doppler-free selective reflection experiment on the 6S1/2
--> 5D5/2 electric-quadrupole transition of cesium vapor at the vicinity of a
sapphire window. This is achieved by a precision experiment overcoming
limitations due to the small signal amplitude of forbidden transitions. Narrow
sub-Doppler lines allow for a collisional broadening measurement on the
electric-quadrupole line. The interaction of cesium atoms with the sapphire
surface of the cell is evidenced, but, due to its weak contribution, a
quantitative analysis remains challenging. Nevertheless, our experiment paves
the way for further studies of the Casimir-Polder interaction between exotic
excited-state atoms and dielectric surfaces.


## Diffusion
### Vista3D: Unravel the 3D Darkside of a Single Image
**Authors**: Qiuhong Shen, Xingyi Yang, Michael Bi Mi, Xinchao Wang

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12193v1](http://arxiv.org/pdf/2409.12193v1)

**Abstract**: We embark on the age-old quest: unveiling the hidden dimensions of objects
from mere glimpses of their visible parts. To address this, we present Vista3D,
a framework that realizes swift and consistent 3D generation within a mere 5
minutes. At the heart of Vista3D lies a two-phase approach: the coarse phase
and the fine phase. In the coarse phase, we rapidly generate initial geometry
with Gaussian Splatting from a single image. In the fine phase, we extract a
Signed Distance Function (SDF) directly from learned Gaussian Splatting,
optimizing it with a differentiable isosurface representation. Furthermore, it
elevates the quality of generation by using a disentangled representation with
two independent implicit functions to capture both visible and obscured aspects
of objects. Additionally, it harmonizes gradients from 2D diffusion prior with
3D-aware diffusion priors by angular diffusion prior composition. Through
extensive evaluation, we demonstrate that Vista3D effectively sustains a
balance between the consistency and diversity of the generated 3D objects.
Demos and code will be available at https://github.com/florinshen/Vista3D.


### DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control
**Authors**: Zichen Jeff Cui, Hengkai Pan, Aadhithya Iyer, Siddhant Haldar, Lerrel Pinto

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12192v1](http://arxiv.org/pdf/2409.12192v1)

**Abstract**: Imitation learning has proven to be a powerful tool for training complex
visuomotor policies. However, current methods often require hundreds to
thousands of expert demonstrations to handle high-dimensional visual
observations. A key reason for this poor data efficiency is that visual
representations are predominantly either pretrained on out-of-domain data or
trained directly through a behavior cloning objective. In this work, we present
DynaMo, a new in-domain, self-supervised method for learning visual
representations. Given a set of expert demonstrations, we jointly learn a
latent inverse dynamics model and a forward dynamics model over a sequence of
image embeddings, predicting the next frame in latent space, without
augmentations, contrastive sampling, or access to ground truth actions.
Importantly, DynaMo does not require any out-of-domain data such as Internet
datasets or cross-embodied datasets. On a suite of six simulated and real
environments, we show that representations learned with DynaMo significantly
improve downstream imitation learning performance over prior self-supervised
learning objectives, and pretrained representations. Gains from using DynaMo
hold across policy classes such as Behavior Transformer, Diffusion Policy, MLP,
and nearest neighbors. Finally, we ablate over key components of DynaMo and
measure its impact on downstream policy performance. Robot videos are best
viewed at https://dynamo-ssl.github.io


### Massively Multi-Person 3D Human Motion Forecasting with Scene Context
**Authors**: Felix B Mueller, Julian Tanke, Juergen Gall

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12189v1](http://arxiv.org/pdf/2409.12189v1)

**Abstract**: Forecasting long-term 3D human motion is challenging: the stochasticity of
human behavior makes it hard to generate realistic human motion from the input
sequence alone. Information on the scene environment and the motion of nearby
people can greatly aid the generation process. We propose a scene-aware social
transformer model (SAST) to forecast long-term (10s) human motion motion.
Unlike previous models, our approach can model interactions between both widely
varying numbers of people and objects in a scene. We combine a temporal
convolutional encoder-decoder architecture with a Transformer-based bottleneck
that allows us to efficiently combine motion and scene information. We model
the conditional motion distribution using denoising diffusion models. We
benchmark our approach on the Humans in Kitchens dataset, which contains 1 to
16 persons and 29 to 50 objects that are visible simultaneously. Our model
outperforms other approaches in terms of realism and diversity on different
metrics and in a user study. Code is available at
https://github.com/felixbmuller/SAST.


### Denoising diffusion models for high-resolution microscopy image restoration
**Authors**: Pamela Osuna-Vargas, Maren H. Wehrheim, Lucas Zinz, Johanna Rahm, Ashwin Balakrishnan, Alexandra Kaminer, Mike Heilemann, Matthias Kaschube

**Published Date**: 2024-09-18

**Updated Date**: 2024-09-18

**PDF Url**: [2409.12078v1](http://arxiv.org/pdf/2409.12078v1)

**Abstract**: Advances in microscopy imaging enable researchers to visualize structures at
the nanoscale level thereby unraveling intricate details of biological
organization. However, challenges such as image noise, photobleaching of
fluorophores, and low tolerability of biological samples to high light doses
remain, restricting temporal resolutions and experiment durations. Reduced
laser doses enable longer measurements at the cost of lower resolution and
increased noise, which hinders accurate downstream analyses. Here we train a
denoising diffusion probabilistic model (DDPM) to predict high-resolution
images by conditioning the model on low-resolution information. Additionally,
the probabilistic aspect of the DDPM allows for repeated generation of images
that tend to further increase the signal-to-noise ratio. We show that our model
achieves a performance that is better or similar to the previously
best-performing methods, across four highly diverse datasets. Importantly,
while any of the previous methods show competitive performance for some, but
not all datasets, our method consistently achieves high performance across all
four data sets, suggesting high generalizability.


### Neural Graph Generator: Feature-Conditioned Graph Generation using Latent Diffusion Models
**Authors**: Iakovos Evdaimon, Giannis Nikolentzos, Christos Xypolopoulos, Ahmed Kammoun, Michail Chatzianastasis, Hadi Abdine, Michalis Vazirgiannis

**Published Date**: 2024-03-03

**Updated Date**: 2024-09-18

**PDF Url**: [2403.01535v3](http://arxiv.org/pdf/2403.01535v3)

**Abstract**: Graph generation has emerged as a crucial task in machine learning, with
significant challenges in generating graphs that accurately reflect specific
properties. Existing methods often fall short in efficiently addressing this
need as they struggle with the high-dimensional complexity and varied nature of
graph properties. In this paper, we introduce the Neural Graph Generator (NGG),
a novel approach which utilizes conditioned latent diffusion models for graph
generation. NGG demonstrates a remarkable capacity to model complex graph
patterns, offering control over the graph generation process. NGG employs a
variational graph autoencoder for graph compression and a diffusion process in
the latent vector space, guided by vectors summarizing graph statistics. We
demonstrate NGG's versatility across various graph generation tasks, showing
its capability to capture desired graph properties and generalize to unseen
graphs. We also compare our generator to the graph generation capabilities of
different LLMs. This work signifies a shift in graph generation methodologies,
offering a more practical and efficient solution for generating diverse graphs
with specific characteristics.


