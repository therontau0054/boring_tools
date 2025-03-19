# Abstracts of Papers

## Physics
### Scalable and fault-tolerant preparation of encoded k-uniform states
**Authors**: Shayan Majidy, Dominik Hangleiter, Michael J. Gullans

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14506v1](http://arxiv.org/pdf/2503.14506v1)

**Abstract**: $k$-uniform states are valuable resources in quantum information, enabling
tasks such as teleportation, error correction, and accelerated quantum
simulations. The practical realization of $k$-uniform states, at scale, faces
major obstacles: verifying $k$-uniformity is as difficult as measuring code
distances, and devising fault-tolerant preparation protocols further adds to
the complexity. To address these challenges, we present a scalable,
fault-tolerant method for preparing encoded $k$-uniform states, and we
illustrate our approach using surface and color codes. We first present a
technique to determine $k$-uniformity of stabilizer states directly from their
stabilizer tableau. We then identify a family of Clifford circuits that ensures
both fault tolerance and scalability in preparing these states. Building on the
encoded $k$-uniform states, we introduce a hybrid physical-logical strategy
that retains some of the error-protection benefits of logical qubits while
lowering the overhead for implementing arbitrary gates compared to fully
logical algorithms. We show that this hybrid approach can outperform fully
physical implementations for resource-state preparation, as demonstrated by
explicit constructions of $k$-uniform states.


### Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control
**Authors**: NVIDIA, :, Hassan Abu Alhaija, Jose Alvarez, Maciej Bala, Tiffany Cai, Tianshi Cao, Liz Cha, Joshua Chen, Mike Chen, Francesco Ferroni, Sanja Fidler, Dieter Fox, Yunhao Ge, Jinwei Gu, Ali Hassani, Michael Isaev, Pooya Jannaty, Shiyi Lan, Tobias Lasser, Huan Ling, Ming-Yu Liu, Xian Liu, Yifan Lu, Alice Luo, Qianli Ma, Hanzi Mao, Fabio Ramos, Xuanchi Ren, Tianchang Shen, Shitao Tang, Ting-Chun Wang, Jay Wu, Jiashu Xu, Stella Xu, Kevin Xie, Yuchong Ye, Xiaodong Yang, Xiaohui Zeng, Yu Zeng

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14492v1](http://arxiv.org/pdf/2503.14492v1)

**Abstract**: We introduce Cosmos-Transfer, a conditional world generation model that can
generate world simulations based on multiple spatial control inputs of various
modalities such as segmentation, depth, and edge. In the design, the spatial
conditional scheme is adaptive and customizable. It allows weighting different
conditional inputs differently at different spatial locations. This enables
highly controllable world generation and finds use in various world-to-world
transfer use cases, including Sim2Real. We conduct extensive evaluations to
analyze the proposed model and demonstrate its applications for Physical AI,
including robotics Sim2Real and autonomous vehicle data enrichment. We further
demonstrate an inference scaling strategy to achieve real-time world generation
with an NVIDIA GB200 NVL72 rack. To help accelerate research development in the
field, we open-source our models and code at
https://github.com/nvidia-cosmos/cosmos-transfer1.


### A Comprehensive Framework for Electroweak Phase Transitions: Thermal History and Dynamics from Bubble Nucleation to Percolation
**Authors**: Haibin Chen, Yun Jiang

**Published Date**: 2025-03-01

**Updated Date**: 2025-03-18

**PDF Url**: [2503.00421v2](http://arxiv.org/pdf/2503.00421v2)

**Abstract**: The electroweak phase transition (EWPT) is crucial for cosmology and particle
physics, with a profound impact on electroweak baryogenesis, symmetry breaking,
and gravitational wave (GW) signals. However, many studies overlook key aspects
of EWPT dynamics, leading to misidentified patterns and overestimated GW
signals. To address these gaps, we present a comprehensive framework for
analyzing EWPTs, focusing on the vacuum's thermal history and dynamics from
bubble nucleation to percolation. Using the $\mathbb{Z}_2$-odd real scalar
singlet model, we demonstrate the occurrence of spontaneous $\mathbb{Z}_2$
symmetry breaking in the high-temperature vacuum, leading to diverse EWPT
processes, including multi-step transitions and inverse symmetry breaking. We
identify four distinct EWPT patterns, each characterized by unique
symmetry-breaking mechanisms and associated with bubbles exhibiting distinct
field configurations, which can be analyzed using a formalism based on energy
density distributions developed here. A key finding is that bubble nucleation
fails in extremely strong phase transitions (PTs) with low nucleation rates, or
in ultra-fast PTs involving inverse $s$-bubbles that collapse instantly upon
formation, both of which lead to false vacuum trapping and the absence of
observable GW signals. In first-order PTs where nucleation succeeds, stronger
transitions occur later in the universe's evolution, while weaker transitions
proceed more rapidly. Multi-step transitions involving (inverse) $\mathbb{Z}_2$
symmetry breaking give rise to complex transition sequences and exotic bubble
dynamics, such as sequential nucleation or the coexistence of bubbles from
different vacua -- phenomena with significant implications for GW spectra, dark
matter, and baryogenesis. This work advances our understanding of EWPT dynamics
and lays the groundwork for future studies of EWPTs in BSM physics.


### EnQode: Fast Amplitude Embedding for Quantum Machine Learning Using Classical Data
**Authors**: Jason Han, Nicholas S. DiBrita, Younghyun Cho, Hengrui Luo, Tirthak Patel

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14473v1](http://arxiv.org/pdf/2503.14473v1)

**Abstract**: Amplitude embedding (AE) is essential in quantum machine learning (QML) for
encoding classical data onto quantum circuits. However, conventional AE methods
suffer from deep, variable-length circuits that introduce high output error due
to extensive gate usage and variable error rates across samples, resulting in
noise-driven inconsistencies that degrade model accuracy. We introduce EnQode,
a fast AE technique based on symbolic representation that addresses these
limitations by clustering dataset samples and solving for cluster mean states
through a low-depth, machine-specific ansatz. Optimized to reduce physical
gates and SWAP operations, EnQode ensures all samples face consistent, low
noise levels by standardizing circuit depth and composition. With over 90%
fidelity in data mapping, EnQode enables robust, high-performance QML on noisy
intermediate-scale quantum (NISQ) devices. Our open-source solution provides a
scalable and efficient alternative for integrating classical data with quantum
models.


### Demonstration of High-Fidelity Entangled Logical Qubits using Transmons
**Authors**: Arian Vezvaee, Vinay Tripathi, Mario Morford-Oberst, Friederike Butt, Victor Kasatkin, Daniel A. Lidar

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14472v1](http://arxiv.org/pdf/2503.14472v1)

**Abstract**: Quantum error correction (QEC) codes are necessary to fault-tolerantly
operate quantum computers. However, every such code is inherently limited by
its inability to detect logical errors. Here, we propose and implement a method
that leverages dynamical decoupling (DD) to drastically suppress logical
errors. The key to achieving this is to use the logical operators of the QEC
code as DD pulses, which we refer to as logical dynamical decoupling (LDD). The
resulting hybrid QEC-LDD strategy is in principle capable of handling arbitrary
weight errors. We test QEC-LDD using IBM transmon devices and the [[4,2,2]]
code, demonstrating performance that significantly exceeds the capabilities of
using either this code or DD in isolation. We present a method that allows for
the detection of logical errors affecting logically encoded Bell states, which,
in this case, arise primarily from crosstalk among physical qubits. Building on
this, we experimentally demonstrate high-fidelity entangled logical qubits.


### Rods in flows: the PDE theory of immersed elastic filaments
**Authors**: Dallas Albritton, Laurel Ohm

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14440v1](http://arxiv.org/pdf/2503.14440v1)

**Abstract**: We investigate a family of curve evolution equations approximating the motion
of a Kirchhoff rod immersed in a low Reynolds number fluid. The rod is modeled
as a framed curve whose energy consists of the bending energy of the curve and
the twisting energy of the frame. The equations we consider may be realized as
gradient flows of the rod energy under a certain anisotropic metric coming from
resistive force theory. Ultimately, our goal is to provide a comprehensive
treatment of the PDE theory of immersed rod dynamics. We begin by analyzing the
problem without the frame, in which case the evolution is globally well-posed
and solutions asymptotically converge to Euler elasticae. Next, in the planar
setting, we demonstrate the existence of large time-periodic solutions forced
by intrinsic curvature relevant to undulatory swimming. Finally, the majority
of the paper is devoted to the evolution of an immersed Kirchhoff rod in 3D,
which involves a strong coupling between the curve and frame. Under a
physically reasonable assumption on the curvature, solutions exist
globally-in-time and asymptotically converge to rod equilibria.


### Discovery of a Glueball-like particle X(2370) at BESIII
**Authors**: Yanping Huang

**Published Date**: 2025-03-17

**Updated Date**: 2025-03-18

**PDF Url**: [2503.13286v2](http://arxiv.org/pdf/2503.13286v2)

**Abstract**: Radiative decays of the $J/\psi$ particle are of gluon-rich environment,
providing an ideal place for hunting glueballs. The $X(2370)$ particle was
first discovered in $J/\psi\to \gamma \pi^+\pi^-\eta^{\prime}$ process in 2011
with the BESIII experiment at BEPCII Collider, and later it was confirmed in
$J/\psi\to\gamma K\bar{K}\eta^{\prime}$ decays. In 2024, with a sample of 10
billion $J/\psi$ events collected at the BESIII detector, the spin-parity of
the $X(2370)$ was determined to be $0^{-+}$ for the first time in the partial
wave analysis of $J/\psi\to \gamma K^{0}_{S}K^{0}_{S} \eta^{\prime}$ process.
Recently, new decay modes of $X(2370)\to K^{0}_{S}K^{0}_{S}\pi^0$,
$\pi^0\pi^0\eta$ and $a^0\pi^0$ were observed. The mass, spin-parity quantum
numbers, production and decay properties of the $X(2370)$ particle are
consistent with the features of the lightest pseudoscalar glueball.


### Functional classification of metabolic networks
**Authors**: Jorge Reyes, Jörn Dunkel

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14437v1](http://arxiv.org/pdf/2503.14437v1)

**Abstract**: Chemical reaction networks underpin biological and physical phenomena across
scales, from microbial interactions to planetary atmosphere dynamics. Bacterial
communities exhibit complex competitive interactions for resources, human
organs and tissues demonstrate specialized biochemical functions, and planetary
atmospheres are capable of displaying diverse organic and inorganic chemical
processes. Despite their complexities, comparing these networks methodically
remains a challenge due to the vast underlying degrees of freedom. In
biological systems, comparative genomics has been pivotal in tracing
evolutionary trajectories and classifying organisms via DNA sequences. However,
purely genomic classifications often fail to capture functional roles within
ecological systems. Metabolic changes driven by nutrient availability highlight
the need for classification schemes that integrate metabolic information. Here
we introduce and apply a computational framework for a classification scheme of
organisms that compares matrix representations of chemical reaction networks
using the Grassmann distance, corresponding to measuring distances between the
fundamental subspaces of stoichiometric matrices. Applying this framework to
human gut microbiome data confirms that metabolic distances are distinct from
phylogenetic distances, underscoring the limitations of genetic information in
metabolic classification. Importantly, our analysis of metabolic distances
reveals functional groups of organisms enriched or depleted in specific
metabolic processes and shows robustness to metabolically silent genetic
perturbations. The generalizability of metabolic Grassmann distances is
illustrated by application to chemical reaction networks in human tissue and
planetary atmospheres, highlighting its potential for advancing functional
comparisons across diverse chemical reaction systems.


### Magnetotransport of tomographic electrons in a channel
**Authors**: Nitay Ben-Shachar, Johannes Hofmann

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14431v1](http://arxiv.org/pdf/2503.14431v1)

**Abstract**: Hydrodynamics is a new paradigm of electron transport in high-mobility
devices, where frequent electron collisions give rise to a collective electron
flow profile. However, conventional descriptions of these flows, which are
based on the fluid equations for a classical gas extended to include impurity
scattering, do not account for the distinct collisional relaxation in
quantum-mechanical systems. In particular, by dint of Pauli blocking even modes
of the distribution function relax over significantly shorter length scales
than odd modes (dubbed the ``tomographic'' effect). We establish an analytical
description of tomographic electron flow in a channel, and find four new
distinguishing features: (i) Non-equilibrium effects from the boundaries
penetrate significantly deeper into the flow domain; (ii) an additional
velocity slip condition leads to a significant increase in the channel
conductance; (iii) bulk rarefaction corrections decrease the curvature of the
velocity profile in the channel center; and (iv) all these anomalous transport
effects are rapidly suppressed with magnetic fields. The latter effect leads to
a non-monotonic magneto-conductance, which can be used to measure both the
even- and odd-mode mean free paths. Our asymptotic results unveil the
underlying physics of tomographic flows and provide an alternative to numerical
solutions of the Fermi-liquid equations.


### Cosmos World Foundation Model Platform for Physical AI
**Authors**: NVIDIA, :, Niket Agarwal, Arslan Ali, Maciej Bala, Yogesh Balaji, Erik Barker, Tiffany Cai, Prithvijit Chattopadhyay, Yongxin Chen, Yin Cui, Yifan Ding, Daniel Dworakowski, Jiaojiao Fan, Michele Fenzi, Francesco Ferroni, Sanja Fidler, Dieter Fox, Songwei Ge, Yunhao Ge, Jinwei Gu, Siddharth Gururani, Ethan He, Jiahui Huang, Jacob Huffman, Pooya Jannaty, Jingyi Jin, Seung Wook Kim, Gergely Klár, Grace Lam, Shiyi Lan, Laura Leal-Taixe, Anqi Li, Zhaoshuo Li, Chen-Hsuan Lin, Tsung-Yi Lin, Huan Ling, Ming-Yu Liu, Xian Liu, Alice Luo, Qianli Ma, Hanzi Mao, Kaichun Mo, Arsalan Mousavian, Seungjun Nah, Sriharsha Niverty, David Page, Despoina Paschalidou, Zeeshan Patel, Lindsey Pavao, Morteza Ramezanali, Fitsum Reda, Xiaowei Ren, Vasanth Rao Naik Sabavat, Ed Schmerling, Stella Shi, Bartosz Stefaniak, Shitao Tang, Lyne Tchapmi, Przemek Tredak, Wei-Cheng Tseng, Jibin Varghese, Hao Wang, Haoxiang Wang, Heng Wang, Ting-Chun Wang, Fangyin Wei, Xinyue Wei, Jay Zhangjie Wu, Jiashu Xu, Wei Yang, Lin Yen-Chen, Xiaohui Zeng, Yu Zeng, Jing Zhang, Qinsheng Zhang, Yuxuan Zhang, Qingqing Zhao, Artur Zolkowski

**Published Date**: 2025-01-07

**Updated Date**: 2025-03-18

**PDF Url**: [2501.03575v2](http://arxiv.org/pdf/2501.03575v2)

**Abstract**: Physical AI needs to be trained digitally first. It needs a digital twin of
itself, the policy model, and a digital twin of the world, the world model. In
this paper, we present the Cosmos World Foundation Model Platform to help
developers build customized world models for their Physical AI setups. We
position a world foundation model as a general-purpose world model that can be
fine-tuned into customized world models for downstream applications. Our
platform covers a video curation pipeline, pre-trained world foundation models,
examples of post-training of pre-trained world foundation models, and video
tokenizers. To help Physical AI builders solve the most critical problems of
our society, we make Cosmos open-source and our models open-weight with
permissive licenses available via
https://github.com/nvidia-cosmos/cosmos-predict1.


## Diffusion
### MusicInfuser: Making Video Diffusion Listen and Dance
**Authors**: Susung Hong, Ira Kemelmacher-Shlizerman, Brian Curless, Steven M. Seitz

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14505v1](http://arxiv.org/pdf/2503.14505v1)

**Abstract**: We introduce MusicInfuser, an approach for generating high-quality dance
videos that are synchronized to a specified music track. Rather than attempting
to design and train a new multimodal audio-video model, we show how existing
video diffusion models can be adapted to align with musical inputs by
introducing lightweight music-video cross-attention and a low-rank adapter.
Unlike prior work requiring motion capture data, our approach fine-tunes only
on dance videos. MusicInfuser achieves high-quality music-driven video
generation while preserving the flexibility and generative capabilities of the
underlying models. We introduce an evaluation framework using Video-LLMs to
assess multiple dimensions of dance generation quality. The project page and
code are available at https://susunghong.github.io/MusicInfuser.


### The Power of Context: How Multimodality Improves Image Super-Resolution
**Authors**: Kangfu Mei, Hossein Talebi, Mojtaba Ardakani, Vishal M. Patel, Peyman Milanfar, Mauricio Delbracio

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14503v1](http://arxiv.org/pdf/2503.14503v1)

**Abstract**: Single-image super-resolution (SISR) remains challenging due to the inherent
difficulty of recovering fine-grained details and preserving perceptual quality
from low-resolution inputs. Existing methods often rely on limited image
priors, leading to suboptimal results. We propose a novel approach that
leverages the rich contextual information available in multiple modalities --
including depth, segmentation, edges, and text prompts -- to learn a powerful
generative prior for SISR within a diffusion model framework. We introduce a
flexible network architecture that effectively fuses multimodal information,
accommodating an arbitrary number of input modalities without requiring
significant modifications to the diffusion process. Crucially, we mitigate
hallucinations, often introduced by text prompts, by using spatial information
from other modalities to guide regional text-based conditioning. Each
modality's guidance strength can also be controlled independently, allowing
steering outputs toward different directions, such as increasing bokeh through
depth or adjusting object prominence via segmentation. Extensive experiments
demonstrate that our model surpasses state-of-the-art generative SISR methods,
achieving superior visual quality and fidelity. See project page at
https://mmsr.kfmei.com/.


### DiffMoE: Dynamic Token Selection for Scalable Diffusion Transformers
**Authors**: Minglei Shi, Ziyang Yuan, Haotian Yang, Xintao Wang, Mingwu Zheng, Xin Tao, Wenliang Zhao, Wenzhao Zheng, Jie Zhou, Jiwen Lu, Pengfei Wan, Di Zhang, Kun Gai

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14487v1](http://arxiv.org/pdf/2503.14487v1)

**Abstract**: Diffusion models have demonstrated remarkable success in various image
generation tasks, but their performance is often limited by the uniform
processing of inputs across varying conditions and noise levels. To address
this limitation, we propose a novel approach that leverages the inherent
heterogeneity of the diffusion process. Our method, DiffMoE, introduces a
batch-level global token pool that enables experts to access global token
distributions during training, promoting specialized expert behavior. To
unleash the full potential of the diffusion process, DiffMoE incorporates a
capacity predictor that dynamically allocates computational resources based on
noise levels and sample complexity. Through comprehensive evaluation, DiffMoE
achieves state-of-the-art performance among diffusion models on ImageNet
benchmark, substantially outperforming both dense architectures with 3x
activated parameters and existing MoE approaches while maintaining 1x activated
parameters. The effectiveness of our approach extends beyond class-conditional
generation to more challenging tasks such as text-to-image generation,
demonstrating its broad applicability across different diffusion model
applications. Project Page: https://shiml20.github.io/DiffMoE/


### Text-to-3D Generation using Jensen-Shannon Score Distillation
**Authors**: Khoi Do, Binh-Son Hua

**Published Date**: 2025-03-08

**Updated Date**: 2025-03-18

**PDF Url**: [2503.10660v2](http://arxiv.org/pdf/2503.10660v2)

**Abstract**: Score distillation sampling is an effective technique to generate 3D models
from text prompts, utilizing pre-trained large-scale text-to-image diffusion
models as guidance. However, the produced 3D assets tend to be over-saturating,
over-smoothing, with limited diversity. These issues are results from a reverse
Kullback-Leibler (KL) divergence objective, which makes the optimization
unstable and results in mode-seeking behavior. In this paper, we derive a
bounded score distillation objective based on Jensen-Shannon divergence (JSD),
which stabilizes the optimization process and produces high-quality 3D
generation. JSD can match well generated and target distribution, therefore
mitigating mode seeking. We provide a practical implementation of JSD by
utilizing the theory of generative adversarial networks to define an
approximate objective function for the generator, assuming the discriminator is
well trained. By assuming the discriminator following a log-odds classifier, we
propose a minority sampling algorithm to estimate the gradients of our proposed
objective, providing a practical implementation for JSD. We conduct both
theoretical and empirical studies to validate our method. Experimental results
on T3Bench demonstrate that our method can produce high-quality and diversified
3D assets.


### MagicComp: Training-free Dual-Phase Refinement for Compositional Video Generation
**Authors**: Hongyu Zhang, Yufan Deng, Shenghai Yuan, Peng Jin, Zesen Cheng, Yian Zhao, Chang Liu, Jie Chen

**Published Date**: 2025-03-18

**Updated Date**: 2025-03-18

**PDF Url**: [2503.14428v1](http://arxiv.org/pdf/2503.14428v1)

**Abstract**: Text-to-video (T2V) generation has made significant strides with diffusion
models. However, existing methods still struggle with accurately binding
attributes, determining spatial relationships, and capturing complex action
interactions between multiple subjects. To address these limitations, we
propose MagicComp, a training-free method that enhances compositional T2V
generation through dual-phase refinement. Specifically, (1) During the
Conditioning Stage: We introduce the Semantic Anchor Disambiguation to
reinforces subject-specific semantics and resolve inter-subject ambiguity by
progressively injecting the directional vectors of semantic anchors into
original text embedding; (2) During the Denoising Stage: We propose Dynamic
Layout Fusion Attention, which integrates grounding priors and model-adaptive
spatial perception to flexibly bind subjects to their spatiotemporal regions
through masked attention modulation. Furthermore, MagicComp is a model-agnostic
and versatile approach, which can be seamlessly integrated into existing T2V
architectures. Extensive experiments on T2V-CompBench and VBench demonstrate
that MagicComp outperforms state-of-the-art methods, highlighting its potential
for applications such as complex prompt-based and trajectory-controllable video
generation. Project page: https://hong-yu-zhang.github.io/MagicComp-Page/.


