# Abstracts of Papers

## Physics
### Spatiotemporal optical vortex (STOV) polariton
**Authors**: M. S. Le, S. W. Hancock, N. Tripathi, H. M. Milchberg

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17413v1](http://arxiv.org/pdf/2502.17413v1)

**Abstract**: We confirm the existence of the spatiotemporal optical vortex (STOV)
polariton and the value of its tOAM, verifying our theory of transverse orbital
angular momentum in a simple dispersive medium [S. W. Hancock et al., Phys.
Rev. Lett. 127, 193901 (2021)]. We also develop a physical picture of the
polariton as a structure driven by torques induced by the ponderomotive force
of the light in the presence of material dispersion. This is a new type of
spatiotemporal torque unanticipated in our recent work [S. W. Hancock et al.,
Phys. Rev. X 14, 011031 (2024)]. These results are accomplished by high
resolution particle-in-cell (PIC) simulations of STOV pulse reflection from and
transmission through a fully ionized hydrogen plasma slab. The linear theory
matches the PIC simulations up to near-critical plasma densities and
near-relativistic field strengths. For higher intensities, optical tOAM becomes
invested in collective modes of the plasma.


### Multi-scale physics of cryogenic liquid helium-4: Inverse coarse-graining properties of smoothed particle hydrodynamics
**Authors**: Satori Tsuzuki

**Published Date**: 2025-01-24

**Updated Date**: 2025-02-24

**PDF Url**: [2501.14244v2](http://arxiv.org/pdf/2501.14244v2)

**Abstract**: Our recent numerical studies on cryogenic liquid helium-4 strongly indicate
the features of multiscale physics that can be identified using the Landau's
two-fluid model. This study presents the possibility that two-fluid models
based on classical and quantum hydrodynamics have a relationship between the
scale transformation using filtering in large eddy simulations (LES) and the
inverse scale transformation using smoothed particle hydrodynamics (SPH). We
show that the spin angular momentum conservation term, which we previously
introduced into the two-fluid model as a quantum mechanical correction,
formally corresponds to the subgrid-scale (SGS) model, which can be derived
from the scale transformation of the two-fluid model from quantum to classical
hydrodynamics. Our theoretical analysis shows that solving the two-fluid model
based on classical hydrodynamics using SPH can reproduce the microscopic
fluctuations even at the macroscopic scale because the truncation errors owing
to the smoothing kernel approximation can substitute the microscopic
fluctuations. In particular, the fluctuations can be amplified according to the
size of the kernel radius at the macroscopic scale. Our further theoretical
analysis shows that the Condiff viscosity model can serve as an SGS model and
incorporate the quantum vortex interactions into the two-fluid model. Our
results and discussion provide new insights into the microscopic composition of
the cryogenic liquid helium-4 within a multiscale framework. First, a normal
fluid can be a mixture of inviscid and viscous fluid particles. Second, a flow
identified as a normal fluid on the microscopic scale because of the presence
of molecular viscosity is still classified as an inviscid fluid on the
hydrodynamic scale because its viscosity is insufficient to produce eddy
viscosity.


### Robust Confinement State Classification with Uncertainty Quantification through Ensembled Data-Driven Methods
**Authors**: Yoeri Poels, Cristina Venturini, Alessandro Pau, Olivier Sauter, Vlado Menkovski, the TCV team, the WPTE team

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17397v1](http://arxiv.org/pdf/2502.17397v1)

**Abstract**: Maximizing fusion performance in tokamaks relies on high energy confinement,
often achieved through distinct operating regimes. The automated labeling of
these confinement states is crucial to enable large-scale analyses or for
real-time control applications. While this task becomes difficult to automate
near state transitions or in marginal scenarios, much success has been achieved
with data-driven models. However, these methods generally provide predictions
as point estimates, and cannot adequately deal with missing and/or broken input
signals. To enable wide-range applicability, we develop methods for confinement
state classification with uncertainty quantification and model robustness. We
focus on off-line analysis for TCV discharges, distinguishing L-mode, H-mode,
and an in-between dithering phase (D). We propose ensembling data-driven
methods on two axes: model formulations and feature sets. The former considers
a dynamic formulation based on a recurrent Fourier Neural Operator-architecture
and a static formulation based on gradient-boosted decision trees. These models
are trained using multiple feature groupings categorized by diagnostic system
or physical quantity. A dataset of 302 TCV discharges is fully labeled, and
will be publicly released. We evaluate our method quantitatively using Cohen's
kappa coefficient for predictive performance and the Expected Calibration Error
for the uncertainty calibration. Furthermore, we discuss performance using a
variety of common and alternative scenarios, the performance of individual
components, out-of-distribution performance, cases of broken or missing
signals, and evaluate conditionally-averaged behavior around different state
transitions. Overall, the proposed method can distinguish L, D and H-mode with
high performance, can cope with missing or broken signals, and provides
meaningful uncertainty estimates.


### Data efficiency and long-term prediction capabilities for neural operator surrogate models of edge plasma simulations
**Authors**: N. Carey, L. Zanisi, S. Pamela, V. Gopakumar, J. Omotani, J. Buchanan, J. Brandstetter, F. Paischer, G. Galletti, P. Setinek

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17386v1](http://arxiv.org/pdf/2502.17386v1)

**Abstract**: Modelling of plasma dynamics is fundamental to ensure appropriate diverter
and core performance, and is desirable for both interpreting the current
generation of experiments and informing the next generation devices like ITER
\cite{Loarte2007Chapter4P,Eich2013ScalingOT}. Yet the computational expense of
many plasma simulations makes them unsuitable for real-time applications or
iterative design workflows. Neural operator surrogate models of JOREK
\cite{Hoelzl_2021} and STORM \cite{Walkden2016-ys} are evaluated, investigating
their capability to replicate plasma dynamics accurately whilst reducing
computational cost. It is found that the accuracy of the surrogate models will
degrade for long term predictions, and that physics considerations are
important in assessing the performance of the surrogates. Surrogates trained on
one dataset can be effectively fine tuned with only a few simulations from a
target domain. This is particularly effective where the source domain is a low
fidelity physics model and the target domain is a high fidelity model, with an
order of magnitude improvement in performance for a small dataset and a short
rollout.


### Travel Time Reliability in Stochastic Kinematic Flow Models
**Authors**: Alexander Hammerl, Ravi Seshadri, Thomas Kjær Rasmussen, Otto Anker Nielsen

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17359v1](http://arxiv.org/pdf/2502.17359v1)

**Abstract**: This paper analyzes the time-dependent relationship between the mean and
variance of travel time on a single corridor under rush hour like congestion
patterns. To model this phenomenon, we apply the LWR ((Lighthill & Whitham,
1955), (Richards, 1956)) theory on a homogenous freeway with a discontinuous
bottleneck at its downstream end, assuming a uni-modal demand profile with a
stochastic peak. We establish conditions for typical counterclockwise
hysteresis loops under these assumptions. It is demonstrated that shapes of the
fundamental diagram which always produce a counterclockwise loop can be
interpreted as an indication of aggressive driving behavior, while deviations
may occur under defensive driving. This classification enables a detailed
explanation of the qualitative physical mechanisms behind this pattern, as well
as an analysis of the causes for quantitatively limited deviations. Some of the
mathematical properties of the LWR model identified in our analysis have not
yet been addressed in the literature and we critically examine the extent to
which these reflect actual traffic flow behavior. Our considerations are
supported by numerical experiments. The obtained results aim to improve the
fundamental understanding of the physical causes of this hysteresis pattern and
to facilitate its better estimation in traffic planning and control.


### An Explainable AI Model for Binary LJ Fluids
**Authors**: Israrul H Hashmi, Rahul Karmakar, Marripelli Maniteja, Kumar Ayush, Tarak K. Patra

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17357v1](http://arxiv.org/pdf/2502.17357v1)

**Abstract**: Lennard-Jones (LJ) fluids serve as an important theoretical framework for
understanding molecular interactions. Binary LJ fluids, where two distinct
species of particles interact based on the LJ potential, exhibit rich phase
behavior and provide valuable insights of complex fluid mixtures. Here we
report the construction and utility of an artificial intelligence (AI) model
for binary LJ fluids, focusing on their effectiveness in predicting radial
distribution functions (RDFs) across a range of conditions. The RDFs of a
binary mixture with varying compositions and temperatures are collected from
molecular dynamics (MD) simulations to establish and validate the AI model. In
this AI pipeline, RDFs are discretized in order to reduce the output dimension
of the model. This, in turn, improves the efficacy, and reduce the complexity
of an AI RDF model. The model is shown to predict RDFs for many unknown
mixtures very accurately, especially outside the training temperature range.
Our analysis suggests that the particle size ratio has a higher order impact on
the microstructure of a binary mixture. We also highlight the areas where the
fidelity of the AI model is low when encountering new regimes with different
underlying physics.


### Hierarchical poromechanical approach to investigate the impact of mechanical loading on human skin micro-circulation
**Authors**: Thomas Lavigne, Stéphane Urcun, Bérengère Fromy, Audrey Josset-Lamaugarny, Alexandre Lagache, Camilo A. Suarez-Afanador, Stéphane P. A. Bordas, Pierre-Yves Rohan, Giuseppe Sciumè

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17354v1](http://arxiv.org/pdf/2502.17354v1)

**Abstract**: Research on human skin anatomy reveals its complex multi-scale, multi-phase
nature, with up to 70% of its composition being bounded and free water. Fluid
movement plays a key role in the skin's mechanical and biological responses,
influencing its time-dependent behavior and nutrient transport.
  Poroelastic modeling is a promising approach for studying skin dynamics
across scales by integrating multi-physics processes. This paper introduces a
hierarchical two-compartment model capturing fluid distribution in the
interstitium and micro-circulation. A theoretical framework is developed with a
biphasic interstitium -- distinguishing interstitial fluid and non-structural
cells -- and analyzed through a one-dimensional consolidation test of a column.
This biphasic approach allows separate modeling of cell and fluid motion,
considering their differing characteristic times. An appendix discusses
extending the model to include biological exchanges like oxygen transport.
Preliminary results indicate that cell viscosity introduces a second
characteristic time, and at high viscosity and short time scales, cells behave
similarly to solids.
  A simplified model was used to replicate an experimental campaign on short
time scales. Local pressure (up to 31 kPa) was applied to dorsal finger skin
using a laser Doppler probe PF801 (Perimed Sweden), following a setup described
in Fromy Brain Res (1998). The model qualitatively captured ischemia and
post-occlusive reactive hyperemia, aligning with experimental data.
  All numerical simulations used the open-source software FEniCSx v0.9.0. To
ensure transparency and reproducibility, anonymized experimental data and
finite element codes are publicly available on GitHub.


### Optimized circuits for windowed modular arithmetic with applications to quantum attacks against RSA
**Authors**: Alessandro Luongo, Varun Narasimhachar, Adithya Sireesh

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17325v1](http://arxiv.org/pdf/2502.17325v1)

**Abstract**: Windowed arithmetic [Gidney, 2019] is a technique for reducing the cost of
quantum arithmetic circuits with space--time tradeoffs using memory queries to
precomputed tables. It can reduce the asymptotic cost of modular exponentiation
from $O\left(n^3\right)$ to $O\left(n^3/\log^2 n\right)$ operations, resulting
in the current state-of-the-art compilations of quantum attacks against modern
cryptography. In this work we introduce four optimizations to windowed modular
exponentiation. We (1) show how the cost of unlookups can be reduced by $66\%$
asymptotically in the number of bits, (2) illustrate how certain addresses can
be bypassed, reducing both circuit depth and the overall lookup cost, (3)
demonstrate that multiple lookup--addition operations can be merged into a
single, larger lookup at the start of the modular exponentiation circuit, and
(4) reduce the depth of the unary conversion for unlookups. On a logical level,
this leads to a $3\%$ improvement in Toffoli count and Toffoli depth for
modular exponentiation circuits relevant to cryptographic applications. This
translates to some improvements on [Gidney and Eker\r{a}, 2021]'s factoring
algorithm: for a given number of physical qubits, our improvements show a
reduction in the expected runtime from $2\%$ to $6\%$ for factoring
$\mathsf{RSA}$-$2048$ integers.


### Engineering of Anyons on M5-Probes via Flux Quantization
**Authors**: Hisham Sati, Urs Schreiber

**Published Date**: 2025-01-29

**Updated Date**: 2025-02-24

**PDF Url**: [2501.17927v2](http://arxiv.org/pdf/2501.17927v2)

**Abstract**: These extended lecture notes survey a novel derivation of anyonic topological
order (as seen in fractional quantum Hall systems) on single magnetized
M5-branes probing Seifert orbi-singularities ("geometric engineering" of
anyons), which we motivate from fundamental open problems in the field of
quantum computing.
  The rigorous construction is non-Lagrangian and non-perturbative, based on
previously neglected global completion of the M5-brane's tensor field by
flux-quantization consistent with its non-linear self-duality and its twisting
by the bulk C-field. This exists only in little-studied non-abelian generalized
cohomology theories, notably in a twisted equivariant (and "twistorial") form
of unstable Cohomotopy ("Hypothesis H").
  As a result, topological quantum observables form Pontrjagin homology
algebras of mapping spaces from the orbi-fixed worldvolume into a classifying
2-sphere. Remarkably, results from algebraic topology imply from this the
quantum observables and modular functor of abelian Chern-Simons theory, as well
as braid group actions on defect anyons of the kind envisioned as hardware for
topologically protected quantum gates.


### Hyperfine and Zeeman Optical Pumping and Transverse Laser Cooling of a Thermal Atomic Beam of Dysprosium Using a Single 421 nm Laser
**Authors**: Rohan Chakravarthy, Jonathan Agil, Arijit Sharma, Jung Bog Kim, Dmitry Budker

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17310v1](http://arxiv.org/pdf/2502.17310v1)

**Abstract**: We demonstrate the effect of Zeeman and hyperfine optical pumping and
transverse laser cooling of a dysprosium (Dy) atomic beam on the $4f^{10}6s^2(J
= 8) \rightarrow 4f^{10}6s6p(J = 9)$ transition at 421.291 nm. For $^{163}$Dy,
an electro-optic modulator is used to generate five frequency sidebands
required to pump the atoms to the $F = 10.5$ ground state hyperfine level and
the light polarization is chosen to pump the atoms to the $m_F = 10.5$ Zeeman
sublevel. The atoms are simultaneously laser-cooled using a standing wave
orthogonal to the atomic beam. The resulting polarized and cooled atomic beam
will be used in fundamental physics experiments taking advantage of the
accidental degeneracy of excited states in Dy including the ongoing measurement
of parity violation in this system.


## Diffusion
### S4S: Solving for a Diffusion Model Solver
**Authors**: Eric Frankel, Sitan Chen, Jerry Li, Pang Wei Koh, Lillian J. Ratliff, Sewoong Oh

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17423v1](http://arxiv.org/pdf/2502.17423v1)

**Abstract**: Diffusion models (DMs) create samples from a data distribution by starting
from random noise and iteratively solving a reverse-time ordinary differential
equation (ODE). Because each step in the iterative solution requires an
expensive neural function evaluation (NFE), there has been significant interest
in approximately solving these diffusion ODEs with only a few NFEs without
modifying the underlying model. However, in the few NFE regime, we observe that
tracking the true ODE evolution is fundamentally impossible using traditional
ODE solvers. In this work, we propose a new method that learns a good solver
for the DM, which we call Solving for the Solver (S4S). S4S directly optimizes
a solver to obtain good generation quality by learning to match the output of a
strong teacher solver. We evaluate S4S on six different pre-trained DMs,
including pixel-space and latent-space DMs for both conditional and
unconditional sampling. In all settings, S4S uniformly improves the sample
quality relative to traditional ODE solvers. Moreover, our method is
lightweight, data-free, and can be plugged in black-box on top of any
discretization schedule or architecture to improve performance. Building on top
of this, we also propose S4S-Alt, which optimizes both the solver and the
discretization schedule. By exploiting the full design space of DM solvers,
with 5 NFEs, we achieve an FID of 3.73 on CIFAR10 and 13.26 on MS-COCO,
representing a $1.5\times$ improvement over previous training-free ODE methods.


### Score Change of Variables
**Authors**: Stephen Robbins

**Published Date**: 2024-12-10

**Updated Date**: 2025-02-24

**PDF Url**: [2412.07904v3](http://arxiv.org/pdf/2412.07904v3)

**Abstract**: We derive a general change of variables formula for score functions, showing
that for a smooth, invertible transformation $\mathbf{y} = \phi(\mathbf{x})$,
the transformed score function $\nabla_{\mathbf{y}} \log q(\mathbf{y})$ can be
expressed directly in terms of $\nabla_{\mathbf{x}} \log p(\mathbf{x})$. Using
this result, we develop two applications: First, we establish a reverse-time
It\^o lemma for score-based diffusion models, allowing the use of
$\nabla_{\mathbf{x}} \log p_t(\mathbf{x})$ to reverse an SDE in the transformed
space without directly learning $\nabla_{\mathbf{y}} \log q_t(\mathbf{y})$.
This approach enables training diffusion models in one space but sampling in
another, effectively decoupling the forward and reverse processes. Second, we
introduce generalized sliced score matching, extending traditional sliced score
matching from linear projections to arbitrary smooth transformations. This
provides greater flexibility in high-dimensional density estimation. We
demonstrate these theoretical advances through applications to diffusion on the
probability simplex and empirically compare our generalized score matching
approach against traditional sliced score matching methods.


### FetDTIAlign: A Deep Learning Framework for Affine and Deformable Registration of Fetal Brain dMRI
**Authors**: Bo Li, Qi Zeng, Simon K. Warfield, Davood Karimi

**Published Date**: 2025-02-03

**Updated Date**: 2025-02-24

**PDF Url**: [2502.01057v3](http://arxiv.org/pdf/2502.01057v3)

**Abstract**: Diffusion MRI (dMRI) provides unique insights into fetal brain microstructure
in utero. Longitudinal and cross-sectional fetal dMRI studies can reveal
crucial neurodevelopmental changes but require precise spatial alignment across
scans and subjects. This is challenging due to low data quality, rapid brain
development, and limited anatomical landmarks. Existing registration methods,
designed for high-quality adult data, struggle with these complexities. To
address this, we introduce FetDTIAlign, a deep learning approach for fetal
brain dMRI registration, enabling accurate affine and deformable alignment.
FetDTIAlign features a dual-encoder architecture and iterative feature-based
inference, reducing the impact of noise and low resolution. It optimizes
network configurations and domain-specific features at each registration stage,
enhancing both robustness and accuracy. We validated FetDTIAlign on data from
23 to 36 weeks gestation, covering 60 white matter tracts. It consistently
outperformed two classical optimization-based methods and a deep learning
pipeline, achieving superior anatomical correspondence. Further validation on
external data from the Developing Human Connectome Project confirmed its
generalizability across acquisition protocols. Our results demonstrate the
feasibility of deep learning for fetal brain dMRI registration, providing a
more accurate and reliable alternative to classical techniques. By enabling
precise cross-subject and tract-specific analyses, FetDTIAlign supports new
discoveries in early brain development.


### HybridLinker: Topology-Guided Posterior Sampling for Enhanced Diversity and Validity in 3D Molecular Linker Generation
**Authors**: Minyeong Hwang, Ziseok Lee, Gwangsoo Kim, Kyungsu Kim, Eunho Yang

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17349v1](http://arxiv.org/pdf/2502.17349v1)

**Abstract**: Linker generation is critical in drug discovery applications such as lead
optimization and PROTAC design, where molecular fragments are assembled into
diverse drug candidates. Existing methods fall into PC-Free and PC-Aware
categories based on their use of 3D point clouds (PC). PC-Free models
prioritize diversity but suffer from lower validity due to overlooking PC
constraints, while PC-Aware models ensure higher validity but restrict
diversity by enforcing strict PC constraints. To overcome these trade-offs
without additional training, we propose HybridLinker, a framework that enhances
PC-Aware inference by providing diverse bonding topologies from a pretrained
PC-Free model as guidance. At its core, we propose LinkerDPS, the first
diffusion posterior sampling (DPS) method operating across PC-Free and PC-Aware
spaces, bridging molecular topology with 3D point clouds via an energy-inspired
function. By transferring the diverse sampling distribution of PC-Free models
into the PC-Aware distribution, HybridLinker significantly and consistently
surpasses baselines, improving both validity and diversity in foundational
molecular design and applied property optimization tasks, establishing a new
DPS framework in the molecular and graph domains beyond imaging.


### AnyTop: Character Animation Diffusion with Any Topology
**Authors**: Inbar Gat, Sigal Raab, Guy Tevet, Yuval Reshef, Amit H. Bermano, Daniel Cohen-Or

**Published Date**: 2025-02-24

**Updated Date**: 2025-02-24

**PDF Url**: [2502.17327v1](http://arxiv.org/pdf/2502.17327v1)

**Abstract**: Generating motion for arbitrary skeletons is a longstanding challenge in
computer graphics, remaining largely unexplored due to the scarcity of diverse
datasets and the irregular nature of the data. In this work, we introduce
AnyTop, a diffusion model that generates motions for diverse characters with
distinct motion dynamics, using only their skeletal structure as input. Our
work features a transformer-based denoising network, tailored for arbitrary
skeleton learning, integrating topology information into the traditional
attention mechanism. Additionally, by incorporating textual joint descriptions
into the latent feature representation, AnyTop learns semantic correspondences
between joints across diverse skeletons. Our evaluation demonstrates that
AnyTop generalizes well, even with as few as three training examples per
topology, and can produce motions for unseen skeletons as well. Furthermore,
our model's latent space is highly informative, enabling downstream tasks such
as joint correspondence, temporal segmentation and motion editing. Our webpage,
https://anytop2025.github.io/Anytop-page, includes links to videos and code.


## Quantitative Finance
### Rebalancing the Scales: A Systematic Mapping Study of Generative Adversarial Networks (GANs) in Addressing Data Imbalance
**Authors**: Pankaj Yadav, Gulshan Sihag, Vivek Vijay

**Published Date**: 2025-02-23

**Updated Date**: 2025-02-23

**PDF Url**: [2502.16535v1](http://arxiv.org/pdf/2502.16535v1)

**Abstract**: Machine learning algorithms are used in diverse domains, many of which face
significant challenges due to data imbalance. Studies have explored various
approaches to address the issue, like data preprocessing, cost-sensitive
learning, and ensemble methods. Generative Adversarial Networks (GANs) showed
immense potential as a data preprocessing technique that generates good quality
synthetic data. This study employs a systematic mapping methodology to analyze
3041 papers on GAN-based sampling techniques for imbalanced data sourced from
four digital libraries. A filtering process identified 100 key studies spanning
domains such as healthcare, finance, and cybersecurity. Through comprehensive
quantitative analysis, this research introduces three categorization mappings
as application domains, GAN techniques, and GAN variants used to handle the
imbalanced nature of the data. GAN-based over-sampling emerges as an effective
preprocessing method. Advanced architectures and tailored frameworks helped
GANs to improve further in the case of data imbalance. GAN variants like
vanilla GAN, CTGAN, and CGAN show great adaptability in structured imbalanced
data cases. Interest in GANs for imbalanced data has grown tremendously,
touching a peak in recent years, with journals and conferences playing crucial
roles in transmitting foundational theories and practical applications. While
with these advances, none of the reviewed studies explicitly explore hybridized
GAN frameworks with diffusion models or reinforcement learning techniques. This
gap leads to a future research idea develop innovative approaches for
effectively handling data imbalance.


