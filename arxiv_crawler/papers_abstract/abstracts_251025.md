# Abstracts of Papers

## Physics
### VAMOS: A Hierarchical Vision-Language-Action Model for Capability-Modulated and Steerable Navigation
**Authors**: Mateo Guaman Castro, Sidharth Rajagopal, Daniel Gorbatov, Matt Schmittle, Rohan Baijal, Octi Zhang, Rosario Scalise, Sidharth Talia, Emma Romig, Celso de Melo, Byron Boots, Abhishek Gupta

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20818v1](http://arxiv.org/pdf/2510.20818v1)

**Abstract**: A fundamental challenge in robot navigation lies in learning policies that
generalize across diverse environments while conforming to the unique physical
constraints and capabilities of a specific embodiment (e.g., quadrupeds can
walk up stairs, but rovers cannot). We propose VAMOS, a hierarchical VLA that
decouples semantic planning from embodiment grounding: a generalist planner
learns from diverse, open-world data, while a specialist affordance model
learns the robot's physical constraints and capabilities in safe, low-cost
simulation. We enabled this separation by carefully designing an interface that
lets a high-level planner propose candidate paths directly in image space that
the affordance model then evaluates and re-ranks. Our real-world experiments
show that VAMOS achieves higher success rates in both indoor and complex
outdoor navigation than state-of-the-art model-based and end-to-end learning
methods. We also show that our hierarchical design enables cross-embodied
navigation across legged and wheeled robots and is easily steerable using
natural language. Real-world ablations confirm that the specialist model is key
to embodiment grounding, enabling a single high-level planner to be deployed
across physically distinct wheeled and legged robots. Finally, this model
significantly enhances single-robot reliability, achieving 3X higher success
rates by rejecting physically infeasible plans. Website:
https://vamos-vla.github.io/


### GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic Manipulation
**Authors**: Guangqi Jiang, Haoran Chang, Ri-Zhao Qiu, Yutong Liang, Mazeyu Ji, Jiyue Zhu, Zhao Dong, Xueyan Zou, Xiaolong Wang

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20813v1](http://arxiv.org/pdf/2510.20813v1)

**Abstract**: This paper presents GSWorld, a robust, photo-realistic simulator for robotics
manipulation that combines 3D Gaussian Splatting with physics engines. Our
framework advocates "closing the loop" of developing manipulation policies with
reproducible evaluation of policies learned from real-robot data and sim2real
policy training without using real robots. To enable photo-realistic rendering
of diverse scenes, we propose a new asset format, which we term GSDF (Gaussian
Scene Description File), that infuses Gaussian-on-Mesh representation with
robot URDF and other objects. With a streamlined reconstruction pipeline, we
curate a database of GSDF that contains 3 robot embodiments for single-arm and
bimanual manipulation, as well as more than 40 objects. Combining GSDF with
physics engines, we demonstrate several immediate interesting applications: (1)
learning zero-shot sim2real pixel-to-action manipulation policy with
photo-realistic rendering, (2) automated high-quality DAgger data collection
for adapting policies to deployment environments, (3) reproducible benchmarking
of real-robot manipulation policies in simulation, (4) simulation data
collection by virtual teleoperation, and (5) zero-shot sim2real visual
reinforcement learning. Website: https://3dgsworld.github.io/.


### Video Prediction of Dynamic Physical Simulations With Pixel-Space Spatiotemporal Transformers
**Authors**: Dean L Slack, G Thomas Hudson, Thomas Winterbottom, Noura Al Moubayed

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20807v1](http://arxiv.org/pdf/2510.20807v1)

**Abstract**: Inspired by the performance and scalability of autoregressive large language
models (LLMs), transformer-based models have seen recent success in the visual
domain. This study investigates a transformer adaptation for video prediction
with a simple end-to-end approach, comparing various spatiotemporal
self-attention layouts. Focusing on causal modeling of physical simulations
over time; a common shortcoming of existing video-generative approaches, we
attempt to isolate spatiotemporal reasoning via physical object tracking
metrics and unsupervised training on physical simulation datasets. We introduce
a simple yet effective pure transformer model for autoregressive video
prediction, utilizing continuous pixel-space representations for video
prediction. Without the need for complex training strategies or latent
feature-learning components, our approach significantly extends the time
horizon for physically accurate predictions by up to 50% when compared with
existing latent-space approaches, while maintaining comparable performance on
common video quality metrics. In addition, we conduct interpretability
experiments to identify network regions that encode information useful to
perform accurate estimations of PDE simulation parameters via probing models,
and find that this generalizes to the estimation of out-of-distribution
simulation parameters. This work serves as a platform for further
attention-based spatiotemporal modeling of videos via a simple, parameter
efficient, and interpretable approach.


### Analog Quantum Feature Selection with Neutral-Atom Quantum Processors
**Authors**: Jose J. Orquin-Marques, Carlos Flores-Garrigos, Alejandro Gomez Cadavid, Anton Simen, Enrique Solano, Narendra N. Hegade, Jose D. Martin-Guerrero, Yolanda Vives-Gilabert

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20798v1](http://arxiv.org/pdf/2510.20798v1)

**Abstract**: We present a quantum-native approach to quantum feature selection (QFS) based
on analog quantum simulation with neutral atom arrays, adaptable to a variety
of academic and industrial applications. In our method, feature
relevance-measured via mutual information with the target-is encoded as local
detuning amplitudes, while feature redundancy is embedded through
distance-dependent van der Waals interactions, constrained by the Rydberg
blockade radius. The system is evolved adiabatically toward low-energy
configurations, and the resulting measurement bitstrings are used to extract
physically consistent subsets of features. The protocol is evaluated through
simulations on three benchmark binary classification datasets: Adult Income,
Bank Marketing, and Telco Churn. Compared to classical methods such as mutual
information ranking and Boruta, combined with XGBoost and Random Forest
classifiers, our quantum-computing approach achieves competitive or superior
performance. In particular, for compact subsets of 2-5 features, analog QFS
improves mean AUC scores by 1.5-2.3% while reducing the number of features by
75-84%, offering interpretable, low-redundancy solutions. These results
demonstrate that programmable Rydberg arrays offer a viable platform for
intelligent feature selection with practical relevance in machine learning
pipelines, capable of transforming computational quantum advantage into
industrial quantum usefulness.


### Bayesian Inference of Primordial Magnetic Field Parameters from CMB with Spherical Graph Neural Networks
**Authors**: Juan Alejandro Pinto Castro, Héctor J. Hortúa, Jorge Enrique García-Farieta, Roger Anderson Hurtado

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20795v1](http://arxiv.org/pdf/2510.20795v1)

**Abstract**: Deep learning has emerged as a transformative methodology in modern
cosmology, providing powerful tools to extract meaningful physical information
from complex astronomical datasets. This paper implements a novel Bayesian
graph deep learning framework for estimating key cosmological parameters in a
primordial magnetic field (PMF) cosmology directly from simulated Cosmic
Microwave Background (CMB) maps. Our methodology utilizes DeepSphere, a
spherical convolutional neural network architecture specifically designed to
respect the spherical geometry of CMB data through HEALPix pixelization. To
advance beyond deterministic point estimates and enable robust uncertainty
quantification, we integrate Bayesian Neural Networks (BNNs) into the
framework, capturing aleatoric and epistemic uncertainties that reflect the
model confidence in its predictions. The proposed approach demonstrates
exceptional performance, achieving $R^{2}$ scores exceeding 0.89 for the
magnetic parameter estimation. We further obtain well-calibrated uncertainty
estimates through post-hoc training techniques including Variance Scaling and
GPNormal. This integrated DeepSphere-BNNs framework not only delivers accurate
parameter estimation from CMB maps with PMF contributions but also provides
reliable uncertainty quantification, providing the necessary tools for robust
cosmological inference in the era of precision cosmology.


### Trapping, manipulating and probing ultracold atoms: a quantum technologies tutorial
**Authors**: Louise Wolswijk, Luca Cavicchioli, Giuseppe Vinelli, Mauro Chiarotti, Ludovica Donati, Marcia Frometa Fernandez, Diego Hernández Rajkov, Christian Mancini, Paolo Vezio, Tianwei Zhou, Giulia Del Pace, Chiara Mazzinghi, Nicolò Antolini, Leonardo Salvi, Vladislav Gavryusev

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20790v1](http://arxiv.org/pdf/2510.20790v1)

**Abstract**: Engineered ultracold atomic systems are a valuable platform for fundamental
quantum mechanics studies and the development of quantum technologies. At near
zero absolute temperature, atoms exhibit macroscopic phase coherence and
collective quantum behavior, enabling their use in precision metrology, quantum
simulation, and even information processing. This review provides an
introductory overview of the key techniques used to trap, manipulate, and
detect ultracold atoms, while highlighting the main applications of each
method. We outline the principles of laser cooling, magnetic and optical
trapping, and the most widely used techniques, including optical lattices and
tweezers. Next, we discuss the manipulation methods of atomic internal and
external degrees of freedom, and we present atom interferometry techniques and
how to leverage and control interatomic interactions. Next, we review common
ensemble detection strategies, including absorption and fluorescence imaging,
state-selective readout, correlation and quantum non-demolition measurements
and conclude with high-resolution approaches. This review aims to provide
newcomers to the field with a broad understanding of the experimental toolkit
that underpins research in ultracold atom physics and its applications across
quantum science and technology.


### CSU-PCAST: A Dual-Branch Transformer Framework for medium-range ensemble Precipitation Forecasting
**Authors**: Tianyi Xiong, Haonan Chen

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20769v1](http://arxiv.org/pdf/2510.20769v1)

**Abstract**: Accurate medium-range precipitation forecasting is crucial for
hydrometeorological risk management and disaster mitigation, yet remains
challenging for current numerical weather prediction (NWP) systems. Traditional
ensemble systems such as the Global Ensemble Forecast System (GEFS) struggle to
maintain high skill, especially for moderate and heavy rainfall at extended
lead times. This study develops a deep learning-based ensemble framework for
multi-step precipitation prediction through joint modeling of a comprehensive
set of atmospheric variables. The model is trained on ERA5 reanalysis data at
0.25$^{\circ}$ spatial resolution, with precipitation labels from NASA's
Integrated Multi-satellite Retrievals for Global Precipitation Measurement
(GPM) constellation (IMERG), incorporating 57 input variables, including
upper-air and surface predictors. The architecture employs a patch-based Swin
Transformer backbone with periodic convolutions to handle longitudinal
continuity and integrates time and noise embeddings through conditional layer
normalization. A dual-branch decoder predicts total precipitation and other
variables, with targeted freezing of encoder-decoder pathways for specialized
training. Training minimizes a hybrid loss combining the Continuous Ranked
Probability Score (CRPS) and weighted log1p mean squared error (log1pMSE),
balancing probabilistic accuracy and magnitude fidelity. During inference, the
model ingests real-time Global Forecast System (GFS) initial conditions to
generate 15-day forecasts autoregressively. Evaluation against GEFS using IMERG
data demonstrates higher Critical Success Index (CSI) scores at precipitation
thresholds of 0.1 mm, 1 mm, 10 mm, and 20 mm, highlighting improved performance
for moderate to heavy rainfall.


### Dynamical entropy of charged black objects
**Authors**: Manus R. Visser, Zihan Yan

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20747v1](http://arxiv.org/pdf/2510.20747v1)

**Abstract**: We develop a general framework for electromagnetic potential-charge
contributions to the first law of black hole mechanics, applicable to dynamical
first-order perturbations of stationary black objects with possibly non-compact
bifurcate Killing horizons. Working in the covariant phase space formalism, we
derive both comparison and physical process versions of the first law. We
consider generic diffeomorphism-invariant theories of gravity in $D$ spacetime
dimensions, containing non-minimally coupled abelian $p$-form gauge fields. The
pullback of the gauge field to the horizon is allowed to diverge while its
field strength remains smooth, yielding gauge-invariant electric
potential-charge pairs in the first law. We further extend the construction to
include magnetic charges by developing a bundle-covariant, gauge-invariant
prescription that fixes the Jacobson-Kang-Myers ambiguity in the improved
Noether charge. Electric and magnetic charges are, respectively, associated
with non-trivial $(D - p - 1)$- and $(p + 1)$-cycles of the horizon
cross-section, whose homology classes determine the number of independent
potential-charge pairs through the Betti numbers $b_{D - p - 1}$ and $b_{p +
1}$. Further, the dynamical gravitational entropy entering the first law is
identified with the gauge-invariant part of the improved Noether charge, giving
a gauge-invariant extension of the recent proposal by Hollands, Wald and Zhang.
We illustrate our framework with dyonic AdS black holes, dipole black rings,
and charged black branes.


### CosmicWatch: The Desktop Muon Detector(v3X)
**Authors**: Spencer Axani, Masooma Sarfraz, Miles Garcia, Collin Owens, Katarzyna Frankiewicz, Janet M. Conrad

**Published Date**: 2025-08-16

**Updated Date**: 2025-10-23

**PDF Url**: [2508.12111v2](http://arxiv.org/pdf/2508.12111v2)

**Abstract**: The CosmicWatch Desktop Muon Detector (v3X) is a compact, low-cost, and
portable device designed for detecting ionizing radiation, including cosmic-ray
muons. Building on previous iterations, the v3X introduces significant hardware
and firmware improvements that enhance sensitivity, usability, and data
acquisition capabilities. The detector integrates a plastic scintillator and
silicon photomultiplier (SiPM), custom designed electronics for signal
processing, onboard data storage, OLED display, environmental sensors, and USB
connectivity. With a total component cost under \$100 and a build time suitable
for high school students, the v3X is ideal for education, outreach, and
introductory research applications in particle and astroparticle physics. This
paper details the design, performance, and potential use cases of the v3X,
supported by example measurements demonstrating its functionality.


### Mass-deformed Super Yang-Mills theory on $\mathbb T^4$: sum over twisted sectors, $\mathbfθ$-angle, and CP violation
**Authors**: Mohamed M. Anber, Erich Poppitz

**Published Date**: 2025-08-29

**Updated Date**: 2025-10-23

**PDF Url**: [2509.00157v2](http://arxiv.org/pdf/2509.00157v2)

**Abstract**: We study $SU(N)$ super Yang-Mills theory with a small gaugino mass $m$ and
vacuum angle $\theta$ on the four-torus $\mathbb{T}^4$ with 't Hooft twisted
boundary conditions. Introducing a detuning parameter $\Delta$, which measures
the deviation from an exactly self-dual $\mathbb{T}^4$, and working in the
limits $mLN \ll \Lambda LN \ll 1$ and $ \frac{(N-1) m^2 L^2}{4 \pi} \ll \Delta
\ll 1$, where $L$ is the torus size and $\Lambda$ the strong-coupling scale, we
compute the scalar and pseudo-scalar condensates to leading order in
$m^2L^2/\Delta$. The twists generate fractional-charge instantons, and we show
that summing over all such contributions is crucial for reproducing the correct
physical observables in the decompactified strong-coupling regime. From a
Hamiltonian perspective, the sum over twisted sectors, already at small torus
size, projects in the $m=0$ limit onto a definite superselection sector of the
$\mathbb{R}^4$ theory. In the massless limit, we recover the exact value of the
gaugino condensate $|\langle \lambda \lambda \rangle| = 16\pi^2 \Lambda^3$, and
demonstrate how a spurious $U(1)$ symmetry eliminates all $CP$-violating
effects. Our results are directly testable in lattice simulations, and our
method extends naturally to non-supersymmetric gauge theories.


## Diffusion
### One-Step Offline Distillation of Diffusion-based Models via Koopman Modeling
**Authors**: Nimrod Berman, Ilan Naiman, Moshe Eliasof, Hedi Zisling, Omri Azencot

**Published Date**: 2025-05-19

**Updated Date**: 2025-10-23

**PDF Url**: [2505.13358v3](http://arxiv.org/pdf/2505.13358v3)

**Abstract**: Diffusion-based generative models have demonstrated exceptional performance,
yet their iterative sampling procedures remain computationally expensive. A
prominent strategy to mitigate this cost is distillation, with offline
distillation offering particular advantages in terms of efficiency, modularity,
and flexibility. In this work, we identify two key observations that motivate a
principled distillation framework: (1) while diffusion models have been viewed
through the lens of dynamical systems theory, powerful and underexplored tools
can be further leveraged; and (2) diffusion models inherently impose
structured, semantically coherent trajectories in latent space. Building on
these observations, we introduce the Koopman Distillation Model (KDM), a novel
offline distillation approach grounded in Koopman theory - a classical
framework for representing nonlinear dynamics linearly in a transformed space.
KDM encodes noisy inputs into an embedded space where a learned linear operator
propagates them forward, followed by a decoder that reconstructs clean samples.
This enables single-step generation while preserving semantic fidelity. We
provide theoretical justification for our approach: (1) under mild assumptions,
the learned diffusion dynamics admit a finite-dimensional Koopman
representation; and (2) proximity in the Koopman latent space correlates with
semantic similarity in the generated outputs, allowing for effective trajectory
alignment. KDM achieves highly competitive performance across standard offline
distillation benchmarks.


### Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge
**Authors**: Nimrod Berman, Omkar Joglekar, Eitan Kosman, Dotan Di Castro, Omri Azencot

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20819v1](http://arxiv.org/pdf/2510.20819v1)

**Abstract**: Recent advances in generative modeling have positioned diffusion models as
state-of-the-art tools for sampling from complex data distributions. While
these models have shown remarkable success across single-modality domains such
as images and audio, extending their capabilities to Modality Translation (MT),
translating information across different sensory modalities, remains an open
challenge. Existing approaches often rely on restrictive assumptions, including
shared dimensionality, Gaussian source priors, and modality-specific
architectures, which limit their generality and theoretical grounding. In this
work, we propose the Latent Denoising Diffusion Bridge Model (LDDBM), a
general-purpose framework for modality translation based on a latent-variable
extension of Denoising Diffusion Bridge Models. By operating in a shared latent
space, our method learns a bridge between arbitrary modalities without
requiring aligned dimensions. We introduce a contrastive alignment loss to
enforce semantic consistency between paired samples and design a
domain-agnostic encoder-decoder architecture tailored for noise prediction in
latent space. Additionally, we propose a predictive loss to guide training
toward accurate cross-domain translation and explore several training
strategies to improve stability. Our approach supports arbitrary modality pairs
and performs strongly on diverse MT tasks, including multi-view to 3D shape
generation, image super-resolution, and multi-view scene synthesis.
Comprehensive experiments and ablations validate the effectiveness of our
framework, establishing a new strong baseline in general modality translation.
For more information, see our project page:
https://sites.google.com/view/lddbm/home.


### DragFlow: Unleashing DiT Priors with Region Based Supervision for Drag Editing
**Authors**: Zihan Zhou, Shilin Lu, Shuli Leng, Shaocong Zhang, Zhuming Lian, Xinlei Yu, Adams Wai-Kin Kong

**Published Date**: 2025-10-02

**Updated Date**: 2025-10-23

**PDF Url**: [2510.02253v2](http://arxiv.org/pdf/2510.02253v2)

**Abstract**: Drag-based image editing has long suffered from distortions in the target
region, largely because the priors of earlier base models, Stable Diffusion,
are insufficient to project optimized latents back onto the natural image
manifold. With the shift from UNet-based DDPMs to more scalable DiT with flow
matching (e.g., SD3.5, FLUX), generative priors have become significantly
stronger, enabling advances across diverse editing tasks. However, drag-based
editing has yet to benefit from these stronger priors. This work proposes the
first framework to effectively harness FLUX's rich prior for drag-based
editing, dubbed DragFlow, achieving substantial gains over baselines. We first
show that directly applying point-based drag editing to DiTs performs poorly:
unlike the highly compressed features of UNets, DiT features are insufficiently
structured to provide reliable guidance for point-wise motion supervision. To
overcome this limitation, DragFlow introduces a region-based editing paradigm,
where affine transformations enable richer and more consistent feature
supervision. Additionally, we integrate pretrained open-domain personalization
adapters (e.g., IP-Adapter) to enhance subject consistency, while preserving
background fidelity through gradient mask-based hard constraints. Multimodal
large language models (MLLMs) are further employed to resolve task ambiguities.
For evaluation, we curate a novel Region-based Dragging benchmark (ReD Bench)
featuring region-level dragging instructions. Extensive experiments on
DragBench-DR and ReD Bench show that DragFlow surpasses both point-based and
region-based baselines, setting a new state-of-the-art in drag-based image
editing. Code and datasets will be publicly available upon publication.


### BadGraph: A Backdoor Attack Against Latent Diffusion Model for Text-Guided Graph Generation
**Authors**: Liang Ye, Shengqin Chen, Jiazhu Dai

**Published Date**: 2025-10-23

**Updated Date**: 2025-10-23

**PDF Url**: [2510.20792v1](http://arxiv.org/pdf/2510.20792v1)

**Abstract**: The rapid progress of graph generation has raised new security concerns,
particularly regarding backdoor vulnerabilities. While prior work has explored
backdoor attacks in image diffusion and unconditional graph generation,
conditional, especially text-guided graph generation remains largely
unexamined. This paper proposes BadGraph, a backdoor attack method targeting
latent diffusion models for text-guided graph generation. BadGraph leverages
textual triggers to poison training data, covertly implanting backdoors that
induce attacker-specified subgraphs during inference when triggers appear,
while preserving normal performance on clean inputs. Extensive experiments on
four benchmark datasets (PubChem, ChEBI-20, PCDes, MoMu) demonstrate the
effectiveness and stealth of the attack: less than 10% poisoning rate can
achieves 50% attack success rate, while 24% suffices for over 80% success rate,
with negligible performance degradation on benign samples. Ablation studies
further reveal that the backdoor is implanted during VAE and diffusion training
rather than pretraining. These findings reveal the security vulnerabilities in
latent diffusion models of text-guided graph generation, highlight the serious
risks in models' applications such as drug discovery and underscore the need
for robust defenses against the backdoor attack in such diffusion models.


### Sampling from multi-modal distributions with polynomial query complexity in fixed dimension via reverse diffusion
**Authors**: Adrien Vacher, Omar Chehab, Anna Korba

**Published Date**: 2024-12-31

**Updated Date**: 2025-10-23

**PDF Url**: [2501.00565v3](http://arxiv.org/pdf/2501.00565v3)

**Abstract**: Even in low dimensions, sampling from multi-modal distributions is
challenging. We provide the first sampling algorithm for a broad class of
distributions -- including all Gaussian mixtures -- with a query complexity
that is polynomial in the parameters governing multi-modality, assuming fixed
dimension. Our sampling algorithm simulates a time-reversed diffusion process,
using a self-normalized Monte Carlo estimator of the intermediate score
functions. Unlike previous works, it avoids metastability, requires no prior
knowledge of the mode locations, and relaxes the well-known log-smoothness
assumption which excluded general Gaussian mixtures so far.


