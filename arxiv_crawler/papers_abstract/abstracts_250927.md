# Abstracts of Papers

## Physics
### Hybrid Summary Statistics
**Authors**: T. Lucas Makinen, Ce Sui, Benjamin D. Wandelt, Natalia Porqueres, Alan Heavens

**Published Date**: 2024-10-10

**Updated Date**: 2025-09-25

**PDF Url**: [2410.07548v2](http://arxiv.org/pdf/2410.07548v2)

**Abstract**: We present a way to capture high-information posteriors from training sets
that are sparsely sampled over the parameter space for robust simulation-based
inference. In physical inference problems, we can often apply domain knowledge
to define traditional summary statistics to capture some of the information in
a dataset. We show that augmenting these statistics with neural network outputs
to maximise the mutual information improves information extraction compared to
neural summaries alone or their concatenation to existing summaries and makes
inference robust in settings with low training data. We introduce 1) two loss
formalisms to achieve this and 2) apply the technique to two different
cosmological datasets to extract non-Gaussian parameter information.


### Two-level overlapping additive Schwarz preconditioner for training scientific machine learning applications
**Authors**: Youngkyu Lee, Alena Kopaničáková, George Em Karniadakis

**Published Date**: 2024-06-16

**Updated Date**: 2025-09-25

**PDF Url**: [2406.10997v2](http://arxiv.org/pdf/2406.10997v2)

**Abstract**: We introduce a novel two-level overlapping additive Schwarz preconditioner
for accelerating the training of scientific machine learning applications. The
design of the proposed preconditioner is motivated by the nonlinear two-level
overlapping additive Schwarz preconditioner. The neural network parameters are
decomposed into groups (subdomains) with overlapping regions. In addition, the
network's feed-forward structure is indirectly imposed through a novel
subdomain-wise synchronization strategy and a coarse-level training step.
Through a series of numerical experiments, which consider physics-informed
neural networks and operator learning approaches, we demonstrate that the
proposed two-level preconditioner significantly speeds up the convergence of
the standard (LBFGS) optimizer while also yielding more accurate machine
learning models. Moreover, the devised preconditioner is designed to take
advantage of model-parallel computations, which can further reduce the training
time.


### Taxonomy-aware Dynamic Motion Generation on Hyperbolic Manifolds
**Authors**: Luis Augenstein, Noémie Jaquier, Tamim Asfour, Leonel Rozo

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21281v1](http://arxiv.org/pdf/2509.21281v1)

**Abstract**: Human-like motion generation for robots often draws inspiration from
biomechanical studies, which often categorize complex human motions into
hierarchical taxonomies. While these taxonomies provide rich structural
information about how movements relate to one another, this information is
frequently overlooked in motion generation models, leading to a disconnect
between the generated motions and their underlying hierarchical structure. This
paper introduces the \ac{gphdm}, a novel approach that learns latent
representations preserving both the hierarchical structure of motions and their
temporal dynamics to ensure physical consistency. Our model achieves this by
extending the dynamics prior of the Gaussian Process Dynamical Model (GPDM) to
the hyperbolic manifold and integrating it with taxonomy-aware inductive
biases. Building on this geometry- and taxonomy-aware frameworks, we propose
three novel mechanisms for generating motions that are both
taxonomically-structured and physically-consistent: two probabilistic recursive
approaches and a method based on pullback-metric geodesics. Experiments on
generating realistic motion sequences on the hand grasping taxonomy show that
the proposed GPHDM faithfully encodes the underlying taxonomy and temporal
dynamics, and generates novel physically-consistent trajectories.


### Does FLUX Already Know How to Perform Physically Plausible Image Composition?
**Authors**: Shilin Lu, Zhuming Lian, Zihan Zhou, Shaocong Zhang, Chen Zhao, Adams Wai-Kin Kong

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21278v1](http://arxiv.org/pdf/2509.21278v1)

**Abstract**: Image composition aims to seamlessly insert a user-specified object into a
new scene, but existing models struggle with complex lighting (e.g., accurate
shadows, water reflections) and diverse, high-resolution inputs. Modern
text-to-image diffusion models (e.g., SD3.5, FLUX) already encode essential
physical and resolution priors, yet lack a framework to unleash them without
resorting to latent inversion, which often locks object poses into contextually
inappropriate orientations, or brittle attention surgery. We propose SHINE, a
training-free framework for Seamless, High-fidelity Insertion with Neutralized
Errors. SHINE introduces manifold-steered anchor loss, leveraging pretrained
customization adapters (e.g., IP-Adapter) to guide latents for faithful subject
representation while preserving background integrity. Degradation-suppression
guidance and adaptive background blending are proposed to further eliminate
low-quality outputs and visible seams. To address the lack of rigorous
benchmarks, we introduce ComplexCompo, featuring diverse resolutions and
challenging conditions such as low lighting, strong illumination, intricate
shadows, and reflective surfaces. Experiments on ComplexCompo and
DreamEditBench show state-of-the-art performance on standard metrics (e.g.,
DINOv2) and human-aligned scores (e.g., DreamSim, ImageReward, VisionReward).
Code and benchmark will be publicly available upon publication.


### Revisiting Reactor Anti-Neutrino 5 MeV Bump with $^{13}$C Neutral-Current Interaction
**Authors**: Pouya Bakhti, Min-Gwa Park, Meshkat Rajaee, Chang Sub Shin, Seodong Shin

**Published Date**: 2024-05-14

**Updated Date**: 2025-09-25

**PDF Url**: [2405.08724v3](http://arxiv.org/pdf/2405.08724v3)

**Abstract**: For the first time, we comprehensively examine the potential of a
neutral-current interaction of reactor neutrino with $^{13}$C emitting a 3.685
MeV photon to identify the origin of the 5 MeV bump in reactor antineutrino
spectra observed through the inverse beta decay (IBD) process. This anomaly may
be due to new physics, reactor antineutrino flux inaccuracies, or IBD
systematics. The 3.685 MeV photon released during the de-excitation of
$^{13}$C$^\ast$ to its ground state is observable in liquid scintillator
detectors. Remarkably, we confirm the powerfulness of our proposal by
completely ruling out a new physics scenario explaining the bump from the
existing NEOS data. We also explore the potential of current and forthcoming
experiments, including solar neutrino studies at JUNO, pion and muon
decay-at-rest experiments at OscSNS, and isotope decay-at-rest studies at
Yemilab, to measure the cross-section precisely enough to distinguish the
expected bump and the theoretical flux models via our channel. Additionally, we
propose a novel method to track the time evolution of reactor isotopes by
analyzing the $^{13}$C signal, which yields critical insights into the
contributions of $^{235}$U and $^{239}$Pu to the bump, acting as a robust tool.


### Proper-Time Approach in Asymptotic Safety via Black Hole Quasinormal Modes and Grey-body Factors
**Authors**: Bekir Can Lütfüoğlu, Erdinç Ulaş Saka, Abubakir Shermatov, Javlon Rayimbaev, Inomjon Ibragimov, Sokhibjan Muminov

**Published Date**: 2025-09-19

**Updated Date**: 2025-09-25

**PDF Url**: [2509.15923v3](http://arxiv.org/pdf/2509.15923v3)

**Abstract**: We study the quasinormal mode spectrum and grey-body factors of black holes
in an effectively quantum-corrected spacetime, focusing on the influence of
near-horizon modifications on observable quantities. Employing scalar,
electromagnetic, and Dirac test fields, we analyze the perturbation equations
and extract the fundamental quasinormal frequencies using both the 6th-order
WKB method with Pad\'e resummation and time-domain integration. Our results
show that quantum corrections near the horizon significantly affect the real
and imaginary parts of the quasinormal modes, particularly for low multipole
numbers and in the near-extremal regime. We also verify the robustness of the
correspondence between quasinormal modes and grey-body factors by comparing WKB
results with those reconstructed from the dominant quasinormal modes. Across
all field types and parameter ranges considered, the WKB method proves accurate
within a few percent, confirming its reliability in probing the impact of
near-horizon physics. These findings support the use of quasinormal ringing and
Hawking radiation spectra as sensitive tools for testing quantum modifications
of black hole spacetimes.


### Limits on New Lorentz-violating Bosons
**Authors**: P. Carenza, J. Jaeckel, G. Lucente, T. K. Poddar, N. Sherrill, M. Spannowsky

**Published Date**: 2025-02-07

**Updated Date**: 2025-09-25

**PDF Url**: [2502.05263v2](http://arxiv.org/pdf/2502.05263v2)

**Abstract**: We obtain novel constraints on new scalar fields interacting with Standard
Model fermions through Lorentz-violating couplings, bridging searches for
scalar particles and Lorentz-symmetry tests. These constraints arise from
torsion-balance experiments, magnetometer searches, and an excessive energy
loss in Red Giant stars. Torsion-balance experiments impose stringent
constraints, benefitting from large macroscopic sources including the Sun and
Earth. Magnetometer-based searches, which detect pseudo-magnetic fields through
spin precession, offer additional limiting power to low-mass scalar fields.
Meanwhile, observations of Red Giant stars place strong limits on additional
energy loss mechanisms, extending these constraints to higher scalar mass
ranges and a wider range of Lorentz-violating couplings. Combining data from
laboratory experiments and astrophysical observations, this approach
strengthens constraints on Lorentz-violating interactions and paves the way for
future investigations into physics beyond the Standard Model.


### From Physics to Machine Learning and Back: Part II - Learning and Observational Bias in PHM
**Authors**: Olga Fink, Ismail Nejjar, Vinay Sharma, Keivan Faghih Niresi, Han Sun, Hao Dong, Chenghao Xu, Amaury Wei, Arthur Bizzi, Raffael Theiler, Yuan Tian, Leandro Von Krannichfeldt, Zhan Ma, Sergei Garmaev, Zepeng Zhang, Mengjie Zhao

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21207v1](http://arxiv.org/pdf/2509.21207v1)

**Abstract**: Prognostics and Health Management ensures the reliability, safety, and
efficiency of complex engineered systems by enabling fault detection,
anticipating equipment failures, and optimizing maintenance activities
throughout an asset lifecycle. However, real-world PHM presents persistent
challenges: sensor data is often noisy or incomplete, available labels are
limited, and degradation behaviors and system interdependencies can be highly
complex and nonlinear. Physics-informed machine learning has emerged as a
promising approach to address these limitations by embedding physical knowledge
into data-driven models. This review examines how incorporating learning and
observational biases through physics-informed modeling and data strategies can
guide models toward physically consistent and reliable predictions. Learning
biases embed physical constraints into model training through physics-informed
loss functions and governing equations, or by incorporating properties like
monotonicity. Observational biases influence data selection and synthesis to
ensure models capture realistic system behavior through virtual sensing for
estimating unmeasured states, physics-based simulation for data augmentation,
and multi-sensor fusion strategies. The review then examines how these
approaches enable the transition from passive prediction to active
decision-making through reinforcement learning, which allows agents to learn
maintenance policies that respect physical constraints while optimizing
operational objectives. This closes the loop between model-based predictions,
simulation, and actual system operation, empowering adaptive decision-making.
Finally, the review addresses the critical challenge of scaling PHM solutions
from individual assets to fleet-wide deployment. Fast adaptation methods
including meta-learning and few-shot learning are reviewed alongside domain
generalization techniques ...


### Differential-Integral Neural Operator for Long-Term Turbulence Forecasting
**Authors**: Hao Wu, Yuan Gao, Fan Xu, Fan Zhang, Qingsong Wen, Kun Wang, Xiaomeng Huang, Xian Wu

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21196v1](http://arxiv.org/pdf/2509.21196v1)

**Abstract**: Accurately forecasting the long-term evolution of turbulence represents a
grand challenge in scientific computing and is crucial for applications ranging
from climate modeling to aerospace engineering. Existing deep learning methods,
particularly neural operators, often fail in long-term autoregressive
predictions, suffering from catastrophic error accumulation and a loss of
physical fidelity. This failure stems from their inability to simultaneously
capture the distinct mathematical structures that govern turbulent dynamics:
local, dissipative effects and global, non-local interactions. In this paper,
we propose the
{\textbf{\underline{D}}}ifferential-{\textbf{\underline{I}}}ntegral
{\textbf{\underline{N}}}eural {\textbf{\underline{O}}}perator (\method{}), a
novel framework designed from a first-principles approach of operator
decomposition. \method{} explicitly models the turbulent evolution through
parallel branches that learn distinct physical operators: a local differential
operator, realized by a constrained convolutional network that provably
converges to a derivative, and a global integral operator, captured by a
Transformer architecture that learns a data-driven global kernel. This
physics-based decomposition endows \method{} with exceptional stability and
robustness. Through extensive experiments on the challenging 2D Kolmogorov flow
benchmark, we demonstrate that \method{} significantly outperforms
state-of-the-art models in long-term forecasting. It successfully suppresses
error accumulation over hundreds of timesteps, maintains high fidelity in both
the vorticity fields and energy spectra, and establishes a new benchmark for
physically consistent, long-range turbulence forecast.


## Diffusion
### IDEATOR: Jailbreaking and Benchmarking Large Vision-Language Models Using Themselves
**Authors**: Ruofan Wang, Juncheng Li, Yixu Wang, Bo Wang, Xiaosen Wang, Yan Teng, Yingchun Wang, Xingjun Ma, Yu-Gang Jiang

**Published Date**: 2024-10-29

**Updated Date**: 2025-09-25

**PDF Url**: [2411.00827v6](http://arxiv.org/pdf/2411.00827v6)

**Abstract**: As large Vision-Language Models (VLMs) gain prominence, ensuring their safe
deployment has become critical. Recent studies have explored VLM robustness
against jailbreak attacks-techniques that exploit model vulnerabilities to
elicit harmful outputs. However, the limited availability of diverse multimodal
data has constrained current approaches to rely heavily on adversarial or
manually crafted images derived from harmful text datasets, which often lack
effectiveness and diversity across different contexts. In this paper, we
propose IDEATOR, a novel jailbreak method that autonomously generates malicious
image-text pairs for black-box jailbreak attacks. IDEATOR is grounded in the
insight that VLMs themselves could serve as powerful red team models for
generating multimodal jailbreak prompts. Specifically, IDEATOR leverages a VLM
to create targeted jailbreak texts and pairs them with jailbreak images
generated by a state-of-the-art diffusion model. Extensive experiments
demonstrate IDEATOR's high effectiveness and transferability, achieving a 94%
attack success rate (ASR) in jailbreaking MiniGPT-4 with an average of only
5.34 queries, and high ASRs of 82%, 88%, and 75% when transferred to LLaVA,
InstructBLIP, and Chameleon, respectively. Building on IDEATOR's strong
transferability and automated process, we introduce the VLJailbreakBench, a
safety benchmark comprising 3,654 multimodal jailbreak samples. Our benchmark
results on 11 recently released VLMs reveal significant gaps in safety
alignment. For instance, our challenge set achieves ASRs of 46.31% on GPT-4o
and 19.65% on Claude-3.5-Sonnet, underscoring the urgent need for stronger
defenses. VLJailbreakBench is publicly available at
https://roywang021.github.io/VLJailbreakBench.


### Generalizing while preserving monotonicity in comparison-based preference learning models
**Authors**: Julien Fageot, Peva Blanchard, Gilles Bareilles, Lê-Nguyên Hoang

**Published Date**: 2025-06-10

**Updated Date**: 2025-09-25

**PDF Url**: [2506.08616v2](http://arxiv.org/pdf/2506.08616v2)

**Abstract**: If you tell a learning model that you prefer an alternative $a$ over another
alternative $b$, then you probably expect the model to be monotone, that is,
the valuation of $a$ increases, and that of $b$ decreases. Yet, perhaps
surprisingly, many widely deployed comparison-based preference learning models,
including large language models, fail to have this guarantee. Until now, the
only comparison-based preference learning algorithms that were proved to be
monotone are the Generalized Bradley-Terry models. Yet, these models are unable
to generalize to uncompared data. In this paper, we advance the understanding
of the set of models with generalization ability that are monotone. Namely, we
propose a new class of Linear Generalized Bradley-Terry models with Diffusion
Priors, and identify sufficient conditions on alternatives' embeddings that
guarantee monotonicity. Our experiments show that this monotonicity is far from
being a general guarantee, and that our new class of generalizing models
improves accuracy, especially when the dataset is limited.


### Pure Vision Language Action (VLA) Models: A Comprehensive Survey
**Authors**: Dapeng Zhang, Jing Sun, Chenghui Hu, Xiaoyan Wu, Zhenlong Yuan, Rui Zhou, Fei Shen, Qingguo Zhou

**Published Date**: 2025-09-23

**Updated Date**: 2025-09-25

**PDF Url**: [2509.19012v2](http://arxiv.org/pdf/2509.19012v2)

**Abstract**: The emergence of Vision Language Action (VLA) models marks a paradigm shift
from traditional policy-based control to generalized robotics, reframing Vision
Language Models (VLMs) from passive sequence generators into active agents for
manipulation and decision-making in complex, dynamic environments. This survey
delves into advanced VLA methods, aiming to provide a clear taxonomy and a
systematic, comprehensive review of existing research. It presents a
comprehensive analysis of VLA applications across different scenarios and
classifies VLA approaches into several paradigms: autoregression-based,
diffusion-based, reinforcement-based, hybrid, and specialized methods; while
examining their motivations, core strategies, and implementations in detail. In
addition, foundational datasets, benchmarks, and simulation platforms are
introduced. Building on the current VLA landscape, the review further proposes
perspectives on key challenges and future directions to advance research in VLA
models and generalizable robotics. By synthesizing insights from over three
hundred recent studies, this survey maps the contours of this rapidly evolving
field and highlights the opportunities and challenges that will shape the
development of scalable, general-purpose VLA methods.


### Why and When Deep is Better than Shallow: An Implementation-Agnostic State-Transition View of Depth Supremacy
**Authors**: Sho Sonoda, Yuka Hashimoto, Isao Ishikawa, Masahiro Ikeda

**Published Date**: 2025-05-21

**Updated Date**: 2025-09-25

**PDF Url**: [2505.15064v2](http://arxiv.org/pdf/2505.15064v2)

**Abstract**: Why and when is deep better than shallow? We answer this question in a
framework that is agnostic to network implementation. We formulate a deep model
as an abstract state-transition semigroup acting on a general metric space, and
separate the implementation (e.g., ReLU nets, transformers, and
chain-of-thought) from the abstract state transition. We prove a bias-variance
decomposition in which the variance depends only on the abstract depth-$k$
network and not on the implementation (Theorem 1). We further split the bounds
into output and hidden parts to tie the depth dependence of the variance to the
metric entropy of the state-transition semigroup (Theorem 2). We then
investigate implementation-free conditions under which the variance grow
polynomially or logarithmically with depth (Section 4). Combining these with
exponential or polynomial bias decay identifies four canonical bias-variance
trade-off regimes (EL/EP/PL/PP) and produces explicit optimal depths $k^\ast$.
Across regimes, $k^\ast>1$ typically holds, giving a rigorous form of depth
supremacy. The lowest generalization error bound is achieved under the EL
regime (exp-decay bias + log-growth variance), explaining why and when deep is
better, especially for iterative or hierarchical concept classes such as neural
ODEs, diffusion/score models, and chain-of-thought reasoning.


### A Unified Framework for Diffusion Model Unlearning with f-Divergence
**Authors**: Nicola Novello, Federico Fontana, Luigi Cinque, Deniz Gunduz, Andrea M. Tonello

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21167v1](http://arxiv.org/pdf/2509.21167v1)

**Abstract**: Machine unlearning aims to remove specific knowledge from a trained model.
While diffusion models (DMs) have shown remarkable generative capabilities,
existing unlearning methods for text-to-image (T2I) models often rely on
minimizing the mean squared error (MSE) between the output distribution of a
target and an anchor concept. We show that this MSE-based approach is a special
case of a unified $f$-divergence-based framework, in which any $f$-divergence
can be utilized. We analyze the benefits of using different $f$-divergences,
that mainly impact the convergence properties of the algorithm and the quality
of unlearning. The proposed unified framework offers a flexible paradigm that
allows to select the optimal divergence for a specific application, balancing
different trade-offs between aggressive unlearning and concept preservation.


## Quantitative Finance
### Multivariate Quadratic Hawkes Processes -- Part II: Non-Parametric Empirical Calibration
**Authors**: Cecilia Aubrun, Michael Benzaquen, Jean-Philippe Bouchaud

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21244v1](http://arxiv.org/pdf/2509.21244v1)

**Abstract**: This is the second part of our work on Multivariate Quadratic Hawkes
(MQHawkes) Processes, devoted to the calibration of the model defined and
studied analytically in Aubrun, C., Benzaquen, M., & Bouchaud, J. P.,
Quantitative Finance, 23(5), 741-758 (2023). We propose a non-parametric
calibration method based on the general method of moments applied to a
coarse-grained version of the MQHawkes model. This allows us to bypass
challenges inherent to tick by tick data. Our main methodological innovation is
a multi-step calibration procedure, first focusing on ''self'' feedback
kernels, and then progressively including cross-effects. Indeed, while
cross-effects are significant and interpretable, they are usually one order of
magnitude smaller than self-effects, and must therefore be disentangled from
noise with care. For numerical stability, we also restrict to pair interactions
and only calibrate bi-variate QHawkes, neglecting higher-order interactions.
Our main findings are: (a) While cross-Hawkes feedback effects have been
empirically studied previously, cross-Zumbach effects are clearly identified
here for the first time. The effect of recent trends of the E-Mini futures
contract onto the volatility of other futures contracts is especially strong;
(b) We have identified a new type of feedback that couples past realized
covariance between two assets and future volatility of these two assets, with
the pair E-Mini vs TBOND as a case in point; (c) A cross-leverage effect,
whereby the sign of the return of one asset impacts the volatility of another
asset, is also clearly identified. The cross-leverage effect between the E-Mini
and the residual volatility of single stocks is notable, and surprisingly
universal across the universe of stocks that we considered.


