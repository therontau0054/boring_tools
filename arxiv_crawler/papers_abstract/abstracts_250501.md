# Abstracts of Papers

## Physics
### Can We Trust Embodied Agents? Exploring Backdoor Attacks against Embodied LLM-based Decision-Making Systems
**Authors**: Ruochen Jiao, Shaoyuan Xie, Justin Yue, Takami Sato, Lixu Wang, Yixuan Wang, Qi Alfred Chen, Qi Zhu

**Published Date**: 2024-05-27

**Updated Date**: 2025-04-30

**PDF Url**: [2405.20774v3](http://arxiv.org/pdf/2405.20774v3)

**Abstract**: Large Language Models (LLMs) have shown significant promise in real-world
decision-making tasks for embodied artificial intelligence, especially when
fine-tuned to leverage their inherent common sense and reasoning abilities
while being tailored to specific applications. However, this fine-tuning
process introduces considerable safety and security vulnerabilities, especially
in safety-critical cyber-physical systems. In this work, we propose the first
comprehensive framework for Backdoor Attacks against LLM-based Decision-making
systems (BALD) in embodied AI, systematically exploring the attack surfaces and
trigger mechanisms. Specifically, we propose three distinct attack mechanisms:
word injection, scenario manipulation, and knowledge injection, targeting
various components in the LLM-based decision-making pipeline. We perform
extensive experiments on representative LLMs (GPT-3.5, LLaMA2, PaLM2) in
autonomous driving and home robot tasks, demonstrating the effectiveness and
stealthiness of our backdoor triggers across various attack channels, with
cases like vehicles accelerating toward obstacles and robots placing knives on
beds. Our word and knowledge injection attacks achieve nearly 100% success rate
across multiple models and datasets while requiring only limited access to the
system. Our scenario manipulation attack yields success rates exceeding 65%,
reaching up to 90%, and does not require any runtime system intrusion. We also
assess the robustness of these attacks against defenses, revealing their
resilience. Our findings highlight critical security vulnerabilities in
embodied LLM systems and emphasize the urgent need for safeguarding these
systems to mitigate potential risks.


### Active Light Modulation to Counter Manipulation of Speech Visual Content
**Authors**: Hadleigh Schwartz, Xiaofeng Yan, Charles J. Carver, Xia Zhou

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21846v1](http://arxiv.org/pdf/2504.21846v1)

**Abstract**: High-profile speech videos are prime targets for falsification, owing to
their accessibility and influence. This work proposes Spotlight, a low-overhead
and unobtrusive system for protecting live speech videos from visual
falsification of speaker identity and lip and facial motion. Unlike predominant
falsification detection methods operating in the digital domain, Spotlight
creates dynamic physical signatures at the event site and embeds them into all
video recordings via imperceptible modulated light. These physical signatures
encode semantically-meaningful features unique to the speech event, including
the speaker's identity and facial motion, and are cryptographically-secured to
prevent spoofing. The signatures can be extracted from any video downstream and
validated against the portrayed speech content to check its integrity. Key
elements of Spotlight include (1) a framework for generating extremely compact
(i.e., 150-bit), pose-invariant speech video features, based on
locality-sensitive hashing; and (2) an optical modulation scheme that embeds
>200 bps into video while remaining imperceptible both in video and live.
Prototype experiments on extensive video datasets show Spotlight achieves AUCs
$\geq$ 0.99 and an overall true positive rate of 100% in detecting falsified
videos. Further, Spotlight is highly robust across recording conditions, video
post-processing techniques, and white-box adversarial attacks on its video
feature extraction methodologies.


### On the Efficacy of the Peeling Decoder for the Quantum Expander Code
**Authors**: Jefrin Sharmitha Prabhu, Abhinav Vaishya, Shobhit Bhatnagar, Aryaman Manish Kolhe, V. Lalitha, P. Vijay Kumar

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21845v1](http://arxiv.org/pdf/2504.21845v1)

**Abstract**: The problem of recovering from qubit erasures has recently gained attention
as erasures occur in many physical systems such as photonic systems, trapped
ions, superconducting qubits and circuit quantum electrodynamics. While several
linear-time decoders for error correction are known, their error-correcting
capability is limited to half the minimum distance of the code, whereas erasure
correction allows one to go beyond this limit. As in the classical case,
stopping sets pose a major challenge in designing efficient erasure decoders
for quantum LDPC codes. In this paper, we show through simulation, that an
attractive alternative here, is the use of quantum expander codes in
conjunction with the peeling decoder that has linear complexity. We also
discuss additional techniques including small-set-flip decoding, that can be
applied following the peeling operation, to improve decoding performance and
their associated complexity.


### Hamiltonian Learning at Heisenberg Limit for Hybrid Quantum Systems
**Authors**: Lixing Zhang, Ze-Xun Lin, Prineha Narang, Di Luo

**Published Date**: 2025-02-27

**Updated Date**: 2025-04-30

**PDF Url**: [2502.20373v3](http://arxiv.org/pdf/2502.20373v3)

**Abstract**: Hybrid quantum systems with different particle species are fundamental in
quantum materials and quantum information science. In this work, we establish a
rigorous theoretical framework proving that, given access to an unknown
spin-boson type Hamiltonian, our algorithm achieves Heisenberg-limited
estimation for all coupling parameters up to error $\epsilon$ with a total
evolution time ${O}(\epsilon^{-1})$ using only ${O}({\rm
polylog}(\epsilon^{-1}))$ measurements. It is also robust against small state
preparation and measurement errors. In addition, we provide an alternative
algorithm based on distributed quantum sensing, which significantly reduces the
evolution time per measurement. To validate our method, we demonstrate its
efficiency in hybrid Hamiltonian learning and spectrum learning, with broad
applications in AMO, condensed matter and high energy physics. Our results
provide a scalable and robust framework for precision Hamiltonian
characterization in hybrid quantum platforms.


### TRIMEG-GKX: an electromagnetic gyrokinetic particle code with a Piecewise Field-Aligned Finite Element Method for Micro- and Macro-Instability Studies in Tokamak Core Plasmas
**Authors**: Zhixin Lu, Guo Meng, Roman Hatzky, Philipp Lauber, Matthias Hoelzl

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21837v1](http://arxiv.org/pdf/2504.21837v1)

**Abstract**: The features of the TRIMEG-GKX code are described with emphasis on the
exploration using novel/different schemes compared to other gyrokinetic codes,
particularly the use of object-oriented programming, filter/buffer-free
treatment, and a high-order piecewise field-aligned finite element method. The
TRIMEG-GKX code solves the electromagnetic gyrokinetic equation using the
particle-in-cell scheme, taking into account multi-species effects and shear
Alfv\'en physics. The mixed-variable/pullback scheme has been implemented to
enable electromagnetic studies. This code is parallelized using particle
decomposition and domain cloning among computing nodes, replacing traditional
domain decomposition techniques. The applications to study the micro- and
macro-instabilities are demonstrated, including the energetic-particle-driven
Alfv\'en eigenmode, ion temperature gradient mode, and kinetic ballooning mode.
Good performance is achieved in both ad hoc and experimentally reconstructed
equilibria, such as those of the ASDEX Upgrade (AUG), Tokamak \`a configuration
variable (TCV), and the Joint European Torus (JET). Future studies of edge
physics using the high-order $C^1$ finite element method for triangular meshes
in the TRIMEG-C1 code will be built upon the same numerical methods.


### Non-standard quantum algebras and infinite-dimensional PT-symmetric systems
**Authors**: Ángel Ballesteros, Romina Ramírez, Marta Reboiro

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21833v1](http://arxiv.org/pdf/2504.21833v1)

**Abstract**: In this work, we introduce a PT-symmetric infinite-dimensional representation
of the Uz(sl(2,R)) Hopf algebra, and we analyse a multiparametric family of
Hamiltonians constructed from such representation of the generators of this
non-standard quantum algebra. It is shown that all these Hamiltonians can be
mapped to equivalent systems endowed with a position-dependent mass. From the
latter presentation, it is shown how appropriate point canonical
transformations can be further defined in order to transform them into
Hamiltonians with constant mass over suitable domains. By following this
approach, the bound-state spectrum and the corresponding eigenfunctions of the
initial PT-symmetric Hamiltonians can be determined. It is worth stressing that
a relevant feature of some of the new Uz(sl(2,R)) systems here presented is
found to be their connection with double-well and P\"oschl-Teller potentials.
In fact, as an application we present a particular Hamiltonian that can be
expressed as an effective double-well trigonometric potential, which is
commonly used to model several relevant systems in molecular physics.


### A Path to Quantum Simulations of Topological Phases: (2+1)D Wilson Fermions Coupled To U(1) Background Gauge Fields
**Authors**: Sriram Bharadwaj, Emil Rosanowski, Simran Singh, Alice di Tucci, Changnan Peng, Karl Jansen, Lena Funcke, Di Luo

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21828v1](http://arxiv.org/pdf/2504.21828v1)

**Abstract**: Quantum simulation offers a powerful approach to studying quantum field
theories, particularly (2+1)D quantum electrodynamics (QED$_3$), which hosts a
rich landscape of physical phenomena. A key challenge in lattice formulations
is the proper realization of topological phases and the Chern-Simons terms,
where fermion discretization plays a crucial role. In this work, we analyze
staggered and Wilson fermions coupled to $\text{U}(1)$ background gauge fields
in the Hamiltonian formulation and demonstrate that staggered fermions fail to
induce (2+1)D topological phases, while Wilson fermions admit a variety of
topological phases including Chern insulator and quantum spin Hall phases. We
additionally uncover a rich phase diagram for the two-flavor Wilson fermion
model in the presence of a chemical potential. Our findings resolve existing
ambiguities in Hamiltonian formulations and provide a theoretical foundation
for future quantum simulations of gauge theories with topological phases. We
further outline connections to experimental platforms, offering guidance for
implementations on near-term quantum computing architectures.


### Practical classical error correction for parity-encoded spin systems
**Authors**: Yoshihiro Nambu

**Published Date**: 2025-02-11

**Updated Date**: 2025-04-30

**PDF Url**: [2502.07170v4](http://arxiv.org/pdf/2502.07170v4)

**Abstract**: Quantum annealing (QA) has emerged as a promising candidate for fast solvers
for combinatorial optimization problems (COPs) and has attracted the interest
of many researchers. Since COP is logically encoded in the Ising interaction
among spins, its realization necessitates a spin system with all-to-all
connectivity, presenting technical challenges in the physical implementation of
large-scale QA devices. W. Lechner, P. Hauke, and P. Zoller proposed a
parity-encoding (PE) architecture consisting of an expanded spin system with
only local connectivity among them to circumvent this difficulty in developing
near-future QA devices. They suggested that this architecture not only
alleviates implementation challenges and enhances scalability but also
possesses intrinsic fault tolerance. This paper proposes a practical decoding
method tailored to correlated spin-flip errors in spin readout of PE
architecture. Our work is based on the close connection between PE architecture
and classical low-density parity-check (LDPC) codes. We show that the bit-flip
(BF) decoding algorithm can correct independent and identically distributed
errors in the readout of the SLHZ system with comparable performance to the
belief propagation (BP) decoding algorithm. Then, we show evidence that the
proposed BF decoding algorithm can efficiently correct correlated spinflip
errors by simulation. The result suggests that introducing post-readout BF
decoding reduces the computational cost of QA using the PE architecture and
improves the performance of global optimal solution search. Our results
emphasize the importance of the proper selection of decoding algorithms to
exploit the inherent fault tolerance potential of the PE architecture.


### Data-driven model validation for neutrino-nucleus cross section measurements
**Authors**: MicroBooNE collaboration, P. Abratenko, O. Alterkait, D. Andrade Aldana, L. Arellano, J. Asaadi, A. Ashkenazi, S. Balasubramanian, B. Baller, A. Barnard, G. Barr, D. Barrow, J. Barrow, V. Basque, J. Bateman, O. Benevides Rodrigues, S. Berkman, A. Bhanderi, A. Bhat, M. Bhattacharya, M. Bishai, A. Blake, B. Bogart, T. Bolton, M. B. Brunetti, L. Camilleri, Y. Cao, D. Caratelli, F. Cavanna, G. Cerati, A. Chappell, Y. Chen, J. M. Conrad, M. Convery, L. Cooper-Troendle, J. I. Crespo-Anadon, R. Cross, M. Del Tutto, S. R. Dennis, P. Detje, R. Diurba, Z. Djurcic, K. Duffy, S. Dytman, B. Eberly, P. Englezos, A. Ereditato, J. J. Evans, C. Fang, B. T. Fleming, W. Foreman, D. Franco, A. P. Furmanski, F. Gao, D. Garcia-Gamez, S. Gardiner, G. Ge, S. Gollapinni, E. Gramellini, P. Green, H. Greenlee, L. Gu, W. Gu, R. Guenette, P. Guzowski, L. Hagaman, M. D. Handley, O. Hen, C. Hilgenberg, G. A. Horton-Smith, Z. Imani, B. Irwin, M. S. Ismail, C. James, X. Ji, J. H. Jo, R. A. Johnson, Y. J. Jwa, D. Kalra, G. Karagiorgi, W. Ketchum, M. Kirby, T. Kobilarcik, N. Lane, J. -Y. Li, Y. Li, K. Lin, B. R. Littlejohn, L. Liu, W. C. Louis, X. Luo, T. Mahmud, C. Mariani, D. Marsden, J. Marshall, N. Martinez, D. A. Martinez Caicedo, S. Martynenko, A. Mastbaum, I. Mawby, N. McConkey, V. Meddage, L. Mellet, J. Mendez, J. Micallef, K. Miller, K. Mistry, T. Mohayai, A. Mogan, M. Mooney, A. F. Moor, C. D. Moore, L. Mora Lepin, M. M. Moudgalya, S. Mulleria Babu, D. Naples, A. Navrer-Agasson, N. Nayak, M. Nebot-Guinot, C. Nguyen, J. Nowak, N. Oza, O. Palamara, N. Pallat, V. Paolone, A. Papadopoulou, V. Papavassiliou, H. Parkinson, S. F. Pate, N. Patel, Z. Pavlovic, E. Piasetzky, K. Pletcher, I. Pophale, X. Qian, J. L. Raaf, V. Radeka, A. Rafique, M. Reggiani-Guzzo, L. Ren, L. Rochester, J. Rodriguez Rondon, M. Rosenberg, M. Ross-Lonergan, I. Safa, D. W. Schmitz, A. Schukraft, W. Seligman, M. H. Shaevitz, R. Sharankova, J. Shi, E. L. Snider, M. Soderberg, S. Soldner-Rembold, J. Spitz, M. Stancari, J. St. John, T. Strauss, A. M. Szelc, N. Taniuchi, K. Terao, C. Thorpe, D. Torbunov, D. Totani, M. Toups, A. Trettin, Y. -T. Tsai, J. Tyler, M. A. Uchida, T. Usher, B. Viren, J. Wang, M. Weber, H. Wei, A. J. White, S. Wolbers, T. Wongjirad, M. Wospakrik, K. Wresilo, W. Wu, E. Yandel, T. Yang, L. E. Yates, H. W. Yu, G. P. Zeller, J. Zennamo, C. Zhang

**Published Date**: 2024-11-05

**Updated Date**: 2025-04-30

**PDF Url**: [2411.03280v2](http://arxiv.org/pdf/2411.03280v2)

**Abstract**: Neutrino-nucleus cross section measurements are needed to improve interaction
modeling to meet the precision needs of neutrino experiments in efforts to
measure oscillation parameters and search for physics beyond the Standard
Model. We review the difficulties associated with modeling neutrino-nucleus
interactions that lead to a dependence on event generators in oscillation
analyses and cross section measurements alike. We then describe data-driven
model validation techniques intended to address this model dependence. The
method relies on utilizing various goodness-of-fit tests and the correlations
between different observables and channels to probe the model for defects in
the phase space relevant for the desired analysis. These techniques shed light
on relevant mis-modeling, allowing it to be detected before it begins to bias
the cross section results. We compare more commonly used model validation
methods which directly validate the model against alternative ones to these
data-driven techniques and show their efficacy with fake data studies. These
studies demonstrate that employing data-driven model validation in cross
section measurements represents a reliable strategy to produce robust results
that will stimulate the desired improvements to interaction modeling.


### Particle, kinetic and hydrodynamic models for sea ice floes. Part I: non-rotating floes
**Authors**: Quanling Deng, Seung-Yeal Ha

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21809v1](http://arxiv.org/pdf/2504.21809v1)

**Abstract**: We introduce a comprehensive modeling framework for the dynamics of sea ice
floes using particle, kinetic, and hydrodynamic approaches. Building upon the
foundational work of Ha and Tadmor on the Cucker-Smale model for flocking, we
derive a Vlasov-type kinetic formulation and a corresponding hydrodynamic
description. The particle model incorporates essential physical properties of
sea ice floes, including size, position, velocity, and interactions governed by
Newtonian mechanics. By extending these principles, the kinetic model captures
large-scale features through the phase-space distribution, and we also present
a hydrodynamic model using the velocity moments and a suitable closure
condition. In this paper, as an idea-introductory step, we assume that ice
floes are non-rotating and focus on the linear velocity dynamics. Our approach
highlights the role of contact forces, ocean drag effects, and conservation
laws in the multiscale description of sea ice dynamics, offering a pathway for
the improved understanding and prediction of sea ice behaviors in changing
climatic conditions.


## Diffusion
### BEVWorld: A Multimodal World Simulator for Autonomous Driving via Scene-Level BEV Latents
**Authors**: Yumeng Zhang, Shi Gong, Kaixin Xiong, Xiaoqing Ye, Xiaofan Li, Xiao Tan, Fan Wang, Jizhou Huang, Hua Wu, Haifeng Wang

**Published Date**: 2024-07-08

**Updated Date**: 2025-04-30

**PDF Url**: [2407.05679v3](http://arxiv.org/pdf/2407.05679v3)

**Abstract**: World models have attracted increasing attention in autonomous driving for
their ability to forecast potential future scenarios. In this paper, we propose
BEVWorld, a novel framework that transforms multimodal sensor inputs into a
unified and compact Bird's Eye View (BEV) latent space for holistic environment
modeling. The proposed world model consists of two main components: a
multi-modal tokenizer and a latent BEV sequence diffusion model. The
multi-modal tokenizer first encodes heterogeneous sensory data, and its decoder
reconstructs the latent BEV tokens into LiDAR and surround-view image
observations via ray-casting rendering in a self-supervised manner. This
enables joint modeling and bidirectional encoding-decoding of panoramic imagery
and point cloud data within a shared spatial representation. On top of this,
the latent BEV sequence diffusion model performs temporally consistent
forecasting of future scenes, conditioned on high-level action tokens, enabling
scene-level reasoning over time. Extensive experiments demonstrate the
effectiveness of BEVWorld on autonomous driving benchmarks, showcasing its
capability in realistic future scene generation and its benefits for downstream
tasks such as perception and motion prediction.


### GarmentDiffusion: 3D Garment Sewing Pattern Generation with Multimodal Diffusion Transformers
**Authors**: Xinyu Li, Qi Yao, Yuanda Wang

**Published Date**: 2025-04-30

**Updated Date**: 2025-04-30

**PDF Url**: [2504.21476v1](http://arxiv.org/pdf/2504.21476v1)

**Abstract**: Garment sewing patterns are fundamental design elements that bridge the gap
between design concepts and practical manufacturing. The generative modeling of
sewing patterns is crucial for creating diversified garments. However, existing
approaches are limited either by reliance on a single input modality or by
suboptimal generation efficiency. In this work, we present
\textbf{\textit{GarmentDiffusion}}, a new generative model capable of producing
centimeter-precise, vectorized 3D sewing patterns from multimodal inputs (text,
image, and incomplete sewing pattern). Our method efficiently encodes 3D sewing
pattern parameters into compact edge token representations, achieving a
sequence length that is $\textbf{10}\times$ shorter than that of the
autoregressive SewingGPT in DressCode. By employing a diffusion transformer, we
simultaneously denoise all edge tokens along the temporal axis, while
maintaining a constant number of denoising steps regardless of dataset-specific
edge and panel statistics. With all combination of designs of our model, the
sewing pattern generation speed is accelerated by $\textbf{100}\times$ compared
to SewingGPT. We achieve new state-of-the-art results on DressCodeData, as well
as on the largest sewing pattern dataset, namely GarmentCodeData. The project
website is available at https://shenfu-research.github.io/Garment-Diffusion/.


### Ditto: Motion-Space Diffusion for Controllable Realtime Talking Head Synthesis
**Authors**: Tianqi Li, Ruobing Zheng, Minghui Yang, Jingdong Chen, Ming Yang

**Published Date**: 2024-11-29

**Updated Date**: 2025-04-30

**PDF Url**: [2411.19509v3](http://arxiv.org/pdf/2411.19509v3)

**Abstract**: Recent advances in diffusion models have endowed talking head synthesis with
subtle expressions and vivid head movements, but have also led to slow
inference speed and insufficient control over generated results. To address
these issues, we propose Ditto, a diffusion-based talking head framework that
enables fine-grained controls and real-time inference. Specifically, we utilize
an off-the-shelf motion extractor and devise a diffusion transformer to
generate representations in a specific motion space. We optimize the model
architecture and training strategy to address the issues in generating motion
representations, including insufficient disentanglement between motion and
identity, and large internal discrepancies within the representation. Besides,
we employ diverse conditional signals while establishing a mapping between
motion representation and facial semantics, enabling control over the
generation process and correction of the results. Moreover, we jointly optimize
the holistic framework to enable streaming processing, real-time inference, and
low first-frame delay, offering functionalities crucial for interactive
applications such as AI assistants. Extensive experimental results demonstrate
that Ditto generates compelling talking head videos and exhibits superiority in
both controllability and real-time performance.


### Elucidating the Preconditioning in Consistency Distillation
**Authors**: Kaiwen Zheng, Guande He, Jianfei Chen, Fan Bao, Jun Zhu

**Published Date**: 2025-02-05

**Updated Date**: 2025-04-30

**PDF Url**: [2502.02922v3](http://arxiv.org/pdf/2502.02922v3)

**Abstract**: Consistency distillation is a prevalent way for accelerating diffusion models
adopted in consistency (trajectory) models, in which a student model is trained
to traverse backward on the probability flow (PF) ordinary differential
equation (ODE) trajectory determined by the teacher model. Preconditioning is a
vital technique for stabilizing consistency distillation, by linear combining
the input data and the network output with pre-defined coefficients as the
consistency function. It imposes the boundary condition of consistency
functions without restricting the form and expressiveness of the neural
network. However, previous preconditionings are hand-crafted and may be
suboptimal choices. In this work, we offer the first theoretical insights into
the preconditioning in consistency distillation, by elucidating its design
criteria and the connection to the teacher ODE trajectory. Based on these
analyses, we further propose a principled way dubbed \textit{Analytic-Precond}
to analytically optimize the preconditioning according to the consistency gap
(defined as the gap between the teacher denoiser and the optimal student
denoiser) on a generalized teacher ODE. We demonstrate that Analytic-Precond
can facilitate the learning of trajectory jumpers, enhance the alignment of the
student trajectory with the teacher's, and achieve $2\times$ to $3\times$
training acceleration of consistency trajectory models in multi-step generation
across various datasets.


### Diffusion Bridge Implicit Models
**Authors**: Kaiwen Zheng, Guande He, Jianfei Chen, Fan Bao, Jun Zhu

**Published Date**: 2024-05-24

**Updated Date**: 2025-04-30

**PDF Url**: [2405.15885v6](http://arxiv.org/pdf/2405.15885v6)

**Abstract**: Denoising diffusion bridge models (DDBMs) are a powerful variant of diffusion
models for interpolating between two arbitrary paired distributions given as
endpoints. Despite their promising performance in tasks like image translation,
DDBMs require a computationally intensive sampling process that involves the
simulation of a (stochastic) differential equation through hundreds of network
evaluations. In this work, we take the first step in fast sampling of DDBMs
without extra training, motivated by the well-established recipes in diffusion
models. We generalize DDBMs via a class of non-Markovian diffusion bridges
defined on the discretized timesteps concerning sampling, which share the same
marginal distributions and training objectives, give rise to generative
processes ranging from stochastic to deterministic, and result in diffusion
bridge implicit models (DBIMs). DBIMs are not only up to 25$\times$ faster than
the vanilla sampler of DDBMs but also induce a novel, simple, and insightful
form of ordinary differential equation (ODE) which inspires high-order
numerical solvers. Moreover, DBIMs maintain the generation diversity in a
distinguished way, by using a booting noise in the initial sampling step, which
enables faithful encoding, reconstruction, and semantic interpolation in image
translation tasks. Code is available at
https://github.com/thu-ml/DiffusionBridge.


## Quantitative Finance
### ClusterLOB: Enhancing Trading Strategies by Clustering Orders in Limit Order Books
**Authors**: Yichi Zhang, Mihai Cucuringu, Alexander Y. Shestopaloff, Stefan Zohren

**Published Date**: 2025-04-29

**Updated Date**: 2025-04-30

**PDF Url**: [2504.20349v2](http://arxiv.org/pdf/2504.20349v2)

**Abstract**: In the rapidly evolving world of financial markets, understanding the
dynamics of limit order book (LOB) is crucial for unraveling market
microstructure and participant behavior. We introduce ClusterLOB as a method to
cluster individual market events in a stream of market-by-order (MBO) data into
different groups. To do so, each market event is augmented with six
time-dependent features. By applying the K-means++ clustering algorithm to the
resulting order features, we are then able to assign each new order to one of
three distinct clusters, which we identify as directional, opportunistic, and
market-making participants, each capturing unique trading behaviors. Our
experimental results are performed on one year of MBO data containing
small-tick, medium-tick, and large-tick stocks from NASDAQ. To validate the
usefulness of our clustering, we compute order flow imbalances across each
cluster within 30-minute buckets during the trading day. We treat each
cluster's imbalance as a signal that provides insights into trading strategies
and participants' responses to varying market conditions. To assess the
effectiveness of these signals, we identify the trading strategy with the
highest Sharpe ratio in the training dataset, and demonstrate that its
performance in the test dataset is superior to benchmark trading strategies
that do not incorporate clustering. We also evaluate trading strategies based
on order flow imbalance decompositions across different market event types,
including add, cancel, and trade events, to assess their robustness in various
market conditions. This work establishes a robust framework for clustering
market participant behavior, which helps us to better understand market
microstructure, and inform the development of more effective predictive trading
signals with practical applications in algorithmic trading and quantitative
finance.


