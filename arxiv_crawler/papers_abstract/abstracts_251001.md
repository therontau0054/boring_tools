# Abstracts of Papers

## Physics
### AccidentBench: Benchmarking Multimodal Understanding and Reasoning in Vehicle Accidents and Beyond
**Authors**: Shangding Gu, Xiaohan Wang, Donghao Ying, Haoyu Zhao, Runing Yang, Ming Jin, Boyi Li, Marco Pavone, Serena Yeung-Levy, Jun Wang, Dawn Song, Costas Spanos

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26636v1](http://arxiv.org/pdf/2509.26636v1)

**Abstract**: Rapid advances in multimodal models demand benchmarks that rigorously
evaluate understanding and reasoning in safety-critical, dynamic real-world
settings. We present AccidentBench, a large-scale benchmark that combines
vehicle accident scenarios with Beyond domains, safety-critical settings in air
and water that emphasize spatial and temporal reasoning (e.g., navigation,
orientation, multi-vehicle motion). The benchmark contains approximately 2000
videos and over 19000 human-annotated question--answer pairs spanning multiple
video lengths (short/medium/long) and difficulty levels (easy/medium/hard).
Tasks systematically probe core capabilities: temporal, spatial, and intent
understanding and reasoning. By unifying accident-centric traffic scenes with
broader safety-critical scenarios in air and water, AccidentBench offers a
comprehensive, physically grounded testbed for evaluating models under
real-world variability. Evaluations of state-of-the-art models (e.g.,
Gemini-2.5 Pro and GPT-5) show that even the strongest models achieve only
about 18% accuracy on the hardest tasks and longest videos, revealing
substantial gaps in real-world temporal, spatial, and intent reasoning.
AccidentBench is designed to expose these critical gaps and drive the
development of multimodal models that are safer, more robust, and better
aligned with real-world safety-critical challenges. The code and dataset are
available at: https://github.com/SafeRL-Lab/AccidentBench


### OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
**Authors**: Lujie Yang, Xiaoyu Huang, Zhen Wu, Angjoo Kanazawa, Pieter Abbeel, Carmelo Sferrazza, C. Karen Liu, Rocky Duan, Guanya Shi

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26633v1](http://arxiv.org/pdf/2509.26633v1)

**Abstract**: A dominant paradigm for teaching humanoid robots complex skills is to
retarget human motions as kinematic references to train reinforcement learning
(RL) policies. However, existing retargeting pipelines often struggle with the
significant embodiment gap between humans and robots, producing physically
implausible artifacts like foot-skating and penetration. More importantly,
common retargeting methods neglect the rich human-object and human-environment
interactions essential for expressive locomotion and loco-manipulation. To
address this, we introduce OmniRetarget, an interaction-preserving data
generation engine based on an interaction mesh that explicitly models and
preserves the crucial spatial and contact relationships between an agent, the
terrain, and manipulated objects. By minimizing the Laplacian deformation
between the human and robot meshes while enforcing kinematic constraints,
OmniRetarget generates kinematically feasible trajectories. Moreover,
preserving task-relevant interactions enables efficient data augmentation, from
a single demonstration to different robot embodiments, terrains, and object
configurations. We comprehensively evaluate OmniRetarget by retargeting motions
from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour
trajectories that achieve better kinematic constraint satisfaction and contact
preservation than widely used baselines. Such high-quality data enables
proprioceptive RL policies to successfully execute long-horizon (up to 30
seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained
with only 5 reward terms and simple domain randomization shared by all tasks,
without any learning curriculum.


### Quantum Optics and Quantum Electrodynamics of Strong Field Processes
**Authors**: Marcelo F. Ciappina, Misha Yu. Ivanov, Maciej Lewenstein, Javier Rivera-Dean, Philipp Stammer, Paraskevas Tzallas

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26602v1](http://arxiv.org/pdf/2509.26602v1)

**Abstract**: In its beginnings, the physics of intense laser-matter interactions was the
physics of multiphoton processes. The theory was reduced then to high-order
perturbation theory, while treating matter and light in a quantum manner. With
the advent of chirped pulse amplification developed by D. Strickland and G.
Mourou, which enabled generation of ultra-intense, ultra-short, coherent laser
pulses, the need for a quantum electrodynamics description of electromagnetic
(EM) fields practically ceased to exist and lost relevance. Contemporary
attoscience (AS), and more generally ultrafast laser physics, awarded the Nobel
Prize in 2023 to P. Agostini, F. Krausz, and A. L'Huillier, commonly uses the
classical description of EM fields while keeping a fully quantum description of
matter. The progress and successes of AS in the last 40 years have been
spectacular, with an enormous amount of fascinating investigations in basic
research and technology. Yet a central question remains: can ultrafast laser
physics continue to advance without reintroducing quantum electrodynamics and
quantum optics into its description of light-matter interactions? This article
discusses future perspectives at the intersection of strong-field physics and
quantum optics.


### ODE-GS: Latent ODEs for Dynamic Scene Extrapolation with 3D Gaussian Splatting
**Authors**: Daniel Wang, Patrick Rim, Tian Tian, Dong Lao, Alex Wong, Ganesh Sundaramoorthi

**Published Date**: 2025-06-05

**Updated Date**: 2025-09-30

**PDF Url**: [2506.05480v3](http://arxiv.org/pdf/2506.05480v3)

**Abstract**: We introduce ODE-GS, a novel approach that integrates 3D Gaussian Splatting
with latent neural ordinary differential equations (ODEs) to enable future
extrapolation of dynamic 3D scenes. Unlike existing dynamic scene
reconstruction methods, which rely on time-conditioned deformation networks and
are limited to interpolation within a fixed time window, ODE-GS eliminates
timestamp dependency by modeling Gaussian parameter trajectories as
continuous-time latent dynamics. Our approach first learns an interpolation
model to generate accurate Gaussian trajectories within the observed window,
then trains a Transformer encoder to aggregate past trajectories into a latent
state evolved via a neural ODE. Finally, numerical integration produces smooth,
physically plausible future Gaussian trajectories, enabling rendering at
arbitrary future timestamps. On the D-NeRF, NVFi, and HyperNeRF benchmarks,
ODE-GS achieves state-of-the-art extrapolation performance, improving metrics
by 19.8% compared to leading baselines, demonstrating its ability to accurately
represent and predict 3D scene dynamics.


### Probing the Critical Point (CritPt) of AI Reasoning: a Frontier Physics Research Benchmark
**Authors**: Minhui Zhu, Minyang Tian, Xiaocheng Yang, Tianci Zhou, Penghao Zhu, Eli Chertkov, Shengyan Liu, Yufeng Du, Lifan Yuan, Ziming Ji, Indranil Das, Junyi Cao, Yufeng Du, Jinchen He, Yifan Su, Jiabin Yu, Yikun Jiang, Yujie Zhang, Chang Liu, Ze-Min Huang, Weizhen Jia, Xinan Chen, Peixue Wu, Yunkai Wang, Juntai Zhou, Yong Zhao, Farshid Jafarpour, Jessie Shelton, Aaron Young, John Bartolotta, Wenchao Xu, Yue Sun, Anjun Chu, Victor Colussi, Chris Akers, Nathan Brooks, Wenbo Fu, Christopher Wilson, Jinchao Zhao, Marvin Qi, Anqi Mu, Yubo Yang, Allen Zang, Yang Lyu, Peizhi Mai, Xuefei Guo, Luyu Gao, Ze Yang, Chi Xue, Dmytro Bandak, Yaïr Hein, Yonatan Kahn, Kevin Zhou, John Drew Wilson Jarrod T. Reilly, Di Luo, Daniel Inafuku, Hao Tong, Liang Yang, Ruixing Zhang, Xueying Wang, Ofir Press, Nicolas Chia, Eliu Huerta, Hao Peng

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26574v1](http://arxiv.org/pdf/2509.26574v1)

**Abstract**: While large language models (LLMs) with reasoning capabilities are
progressing rapidly on high-school math competitions and coding, can they
reason effectively through complex, open-ended challenges found in frontier
physics research? And crucially, what kinds of reasoning tasks do physicists
want LLMs to assist with? To address these questions, we present the CritPt
(Complex Research using Integrated Thinking - Physics Test, pronounced
"critical point"), the first benchmark designed to test LLMs on unpublished,
research-level reasoning tasks that broadly covers modern physics research
areas, including condensed matter, quantum physics, atomic, molecular & optical
physics, astrophysics, high energy physics, mathematical physics, statistical
physics, nuclear physics, nonlinear dynamics, fluid dynamics and biophysics.
CritPt consists of 71 composite research challenges designed to simulate
full-scale research projects at the entry level, which are also decomposed to
190 simpler checkpoint tasks for more fine-grained insights. All problems are
newly created by 50+ active physics researchers based on their own research.
Every problem is hand-curated to admit a guess-resistant and machine-verifiable
answer and is evaluated by an automated grading pipeline heavily customized for
advanced physics-specific output formats. We find that while current
state-of-the-art LLMs show early promise on isolated checkpoints, they remain
far from being able to reliably solve full research-scale challenges: the best
average accuracy among base models is only 4.0% , achieved by GPT-5 (high),
moderately rising to around 10% when equipped with coding tools. Through the
realistic yet standardized evaluation offered by CritPt, we highlight a large
disconnect between current model capabilities and realistic physics research
demands, offering a foundation to guide the development of scientifically
grounded AI tools.


### Elias' Encoding from Lagrangians and Renormalization
**Authors**: Alexander Kolpakov, Aidan Rocke

**Published Date**: 2025-06-30

**Updated Date**: 2025-09-30

**PDF Url**: [2506.23447v4](http://arxiv.org/pdf/2506.23447v4)

**Abstract**: In the present paper we give a derivation of Elias' Omega code from physics
principles by combining a constrained variational formulation of prefix coding
with a renormalization flow on codeword distributions.
  Starting from a Lagrangian that minimizes average codelength under the
Kraft-McMillan constraint, we show that the implied distribution is a fixed
point of a coarse-graining map, yielding the canonical iterated log-sum length,
asymptotically up to an additive constant.
  This establishes completeness and asymptotic optimality, and connects
universal integer coding with coarse-grained entropy, uncertainty-type bounds,
and entropy relations familiar from statistical physics.


### The REDTOP experiment: a $η/η^{\prime}$ factory to explore dark matter and physics beyond the Standard Model
**Authors**: Marcin Zielinski, Corrado Gatto

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26552v1](http://arxiv.org/pdf/2509.26552v1)

**Abstract**: The REDTOP experiment is a proposed super-$\eta$/$\eta'$ factory aimed at
exploring physics beyond the Standard Model in the MeV-GeV range and rare
$\eta$/$\eta'$ meson decays. With projected production rates exceeding
$10^{13}$ $\eta$/year and $10^{12}$ $\eta'$/year, REDTOP will enable studies of
symmetry violations and all four portals to the Dark Sector. Preliminary
studies show sensitivity, which could open a broad possibility for exploring
new physics and contribute to a deeper understanding of fundamental
interactions within the Standard Model. Such high statistics experiments and
the required sensitivity can only be achieved with a high intensity proton or
pion beam, available at several accelerator facilities worldwide. This article
discusses the physics potential of the REDTOP experiment, the detector design,
and the future beam requirements.


### Interdisciplinary Digital Twin Engine InterTwin for calorimeter simulation
**Authors**: Corentin Allaire, Vera Maiboroda, David Rousseau

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26527v1](http://arxiv.org/pdf/2509.26527v1)

**Abstract**: Calorimeter shower simulations are computationally expensive, and generative
models offer an efficient alternative. However, achieving a balance between
accuracy and speed remains a challenge, with distribution tail modeling being a
key limitation. Invertible generative network CaloINN provides a trade-off
between simulation quality and efficiency. The ongoing study targets
introducing a set of post-processing modifications of analysis-level
observables aimed at improving the accuracy of distribution tails. As part of
interTwin project initiative developing an open-source Digital Twin Engine, we
implemented the CaloINN within the interTwin AI framework.


### Electromagnetically driven, environmentally adaptive, and functionally switchable hydrodynamic devices
**Authors**: Chen-Long Wu, Bin Wang, Hao Wang, Neng-Zhi Yao, Liujun Xu, Xuesheng Wang, Jiping Huang

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26491v1](http://arxiv.org/pdf/2509.26491v1)

**Abstract**: Metamaterials provide exceptional control over physical phenomena, enabling
many disruptive technologies. However, researches in hydrodynamic meta-devices
have mainly used intrusive methods to manipulate material structures, limited
by material properties and specific environmental conditions. Each design
serves a single function, reducing versatility. This study introduces a
meta-hydrodynamics theory using applied force fields to avoid physical contact
with the fluid and eliminate the need for inhomogeneous and anisotropic
metamaterials, allowing continuous switching between cloaking, shielding, and
Venturi amplification. The force field operates independently of the fluid's
physical properties, making it adaptable to various fluids and environmental
conditions. We derive volumetric force distributions for hydrodynamic devices
based on fluid properties and forces equivalence, using the integral median
theorem to homogenize these forces for practical applications. The
effectiveness of the proposed hydrodynamic devices is validated through
numerical simulations and quantitative analyses. By utilizing the
electromagnetic forces produced by the interaction between a conducting fluid
and an electromagnetic field, we experimentally verified the validity of our
theoretical simulations. Our research offers different insights into
hydrodynamic meta-devices design, enhancing practical applications and opening
avenues for innovative flow manipulation.


### Nondestructive characterization of laser-cooled atoms using machine learning
**Authors**: G. De Sousa, M. Doris, D. D'Amato, B. Egleston, J. P. Zwolak, I. B. Spielman

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26479v1](http://arxiv.org/pdf/2509.26479v1)

**Abstract**: We develop machine learning techniques for estimating physical properties of
laser-cooled potassium-39 atoms in a magneto-optical trap using only the
scattered light -- i.e., fluorescence -- that is intrinsic to the cooling
process. In-situ snap-shot images of fluorescing atomic ensembles directly
reveal the spatial structure of these millimeter-scale objects but contain no
obvious information regarding internal properties such as the temperature. We
first assembled and labeled a balanced dataset sampling $8\times10^3$ different
experimental parameters that includes examples with: large and dense atomic
ensembles, a complete absence of atoms, and everything in between. We describe
a range of models trained to predict atom number and temperature solely from
fluorescence images. These run the gamut from a poorly performing linear
regression model based only on integrated fluorescence to deep neural networks
that give number and temperature with fractional uncertainties of $0.1$ and
$0.2$ respectively.


## Diffusion
### Stitch: Training-Free Position Control in Multimodal Diffusion Transformers
**Authors**: Jessica Bader, Mateusz Pach, Maria A. Bravo, Serge Belongie, Zeynep Akata

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26644v1](http://arxiv.org/pdf/2509.26644v1)

**Abstract**: Text-to-Image (T2I) generation models have advanced rapidly in recent years,
but accurately capturing spatial relationships like "above" or "to the right
of" poses a persistent challenge. Earlier methods improved spatial relationship
following with external position control. However, as architectures evolved to
enhance image quality, these techniques became incompatible with modern models.
We propose Stitch, a training-free method for incorporating external position
control into Multi-Modal Diffusion Transformers (MMDiT) via
automatically-generated bounding boxes. Stitch produces images that are both
spatially accurate and visually appealing by generating individual objects
within designated bounding boxes and seamlessly stitching them together. We
find that targeted attention heads capture the information necessary to isolate
and cut out individual objects mid-generation, without needing to fully
complete the image. We evaluate Stitch on PosEval, our benchmark for
position-based T2I generation. Featuring five new tasks that extend the concept
of Position beyond the basic GenEval task, PosEval demonstrates that even top
models still have significant room for improvement in position-based
generation. Tested on Qwen-Image, FLUX, and SD3.5, Stitch consistently enhances
base models, even improving FLUX by 218% on GenEval's Position task and by 206%
on PosEval. Stitch achieves state-of-the-art results with Qwen-Image on
PosEval, improving over previous models by 54%, all accomplished while
integrating position control into leading models training-free. Code is
available at https://github.com/ExplainableML/Stitch.


### Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training
**Authors**: Junlin Han, Shengbang Tong, David Fan, Yufan Ren, Koustuv Sinha, Philip Torr, Filippos Kokkinos

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26625v1](http://arxiv.org/pdf/2509.26625v1)

**Abstract**: Large Language Models (LLMs), despite being trained on text alone,
surprisingly develop rich visual priors. These priors allow latent visual
capabilities to be unlocked for vision tasks with a relatively small amount of
multimodal data, and in some cases, to perform visual tasks without ever having
seen an image. Through systematic analysis, we reveal that visual priors-the
implicit, emergent knowledge about the visual world acquired during language
pre-training-are composed of separable perception and reasoning priors with
unique scaling trends and origins. We show that an LLM's latent visual
reasoning ability is predominantly developed by pre-training on
reasoning-centric data (e.g., code, math, academia) and scales progressively.
This reasoning prior acquired from language pre-training is transferable and
universally applicable to visual reasoning. In contrast, a perception prior
emerges more diffusely from broad corpora, and perception ability is more
sensitive to the vision encoder and visual instruction tuning data. In
parallel, text describing the visual world proves crucial, though its
performance impact saturates rapidly. Leveraging these insights, we propose a
data-centric recipe for pre-training vision-aware LLMs and verify it in 1T
token scale pre-training. Our findings are grounded in over 100 controlled
experiments consuming 500,000 GPU-hours, spanning the full MLLM construction
pipeline-from LLM pre-training to visual alignment and supervised multimodal
fine-tuning-across five model scales, a wide range of data categories and
mixtures, and multiple adaptation setups. Along with our main findings, we
propose and investigate several hypotheses, and introduce the Multi-Level
Existence Bench (MLE-Bench). Together, this work provides a new way of
deliberately cultivating visual priors from language pre-training, paving the
way for the next generation of multimodal LLMs.


### HilbertA: Hilbert Attention for Image Generation with Diffusion Models
**Authors**: Shaoyi Zheng, Wenbo Lu, Yuxuan Xia, Haomin Liu, Shengjie Wang

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26538v1](http://arxiv.org/pdf/2509.26538v1)

**Abstract**: Designing sparse attention for diffusion transformers requires reconciling
two-dimensional spatial locality with GPU efficiency, a trade-off that current
methods struggle to achieve. Existing approaches enforce two-dimensional
spatial locality but often incur uncoalesced memory access. We present
HilbertA, a 2D-aware and GPU-efficient sparse attention mechanism. HilbertA
reorders image tokens along Hilbert curves to achieve a contiguous memory
layout while preserving spatial neighborhoods, and employs a sliding schedule
across layers to enable long-range information propagation without repeated or
uncoalesced memory access. To further enhance cross-tile communication and
positional awareness, HilbertA introduces a small central shared region.
Implemented in Triton, HilbertA delivers comparable image quality with
significant acceleration over prior methods on Flux.1-dev, demonstrating the
feasibility of hardware-aligned two-dimensional sparse attention for
high-resolution image generation. HilbertA delivers attention speedups of
$2.3\times$ when generating $1024\times 1024$ images, and up to $4.17\times$ at
$2048\times 2048$, while achieving image quality comparable to or surpassing
baselines.


### CE-SDWV: Effective and Efficient Concept Erasure for Text-to-Image Diffusion Models via a Semantic-Driven Word Vocabulary
**Authors**: Jiahang Tu, Qian Feng, Jiahua Dong, Hanbin Zhao, Chao Zhang, Nicu Sebe, Hui Qian

**Published Date**: 2025-01-26

**Updated Date**: 2025-09-30

**PDF Url**: [2501.15562v2](http://arxiv.org/pdf/2501.15562v2)

**Abstract**: Large-scale text-to-image (T2I) diffusion models have achieved remarkable
generative performance about various concepts. With the limitation of privacy
and safety in practice, the generative capability concerning NSFW (Not Safe For
Work) concepts is undesirable, e.g., producing sexually explicit photos, and
licensed images. The concept erasure task for T2I diffusion models has
attracted considerable attention and requires an effective and efficient
method. To achieve this goal, we propose a CE-SDWV framework, which removes the
target concepts (e.g., NSFW concepts) of T2I diffusion models in the text
semantic space by only adjusting the text condition tokens and does not need to
re-train the original T2I diffusion model's weights. Specifically, our
framework first builds a target concept-related word vocabulary to enhance the
representation of the target concepts within the text semantic space, and then
utilizes an adaptive semantic component suppression strategy to ablate the
target concept-related semantic information in the text condition tokens. To
further adapt the above text condition tokens to the original image semantic
space, we propose an end-to-end gradient-orthogonal token optimization
strategy. Extensive experiments on I2P and UnlearnCanvas benchmarks demonstrate
the effectiveness and efficiency of our method. Code is available at
https://github.com/TtuHamg/CE-SDWV.


### Contrastive Diffusion Guidance for Spatial Inverse Problems
**Authors**: Sattwik Basu, Chaitanya Amballa, Zhongweiyang Xu, Jorge Vančo Sampedro, Srihari Nelakuditi, Romit Roy Choudhury

**Published Date**: 2025-09-30

**Updated Date**: 2025-09-30

**PDF Url**: [2509.26489v1](http://arxiv.org/pdf/2509.26489v1)

**Abstract**: We consider the inverse problem of reconstructing the spatial layout of a
place, a home floorplan for example, from a user`s movements inside that
layout. Direct inversion is ill-posed since many floorplans can explain the
same movement trajectories. We adopt a diffusion-based posterior sampler to
generate layouts consistent with the measurements. While active research is in
progress on generative inverse solvers, we find that the forward operator in
our problem poses new challenges. The path-planning process inside a floorplan
is a non-invertible, non-differentiable function, and causes instability while
optimizing using the likelihood score. We break-away from existing approaches
and reformulate the likelihood score in a smoother embedding space. The
embedding space is trained with a contrastive loss which brings compatible
floorplans and trajectories close to each other, while pushing mismatched pairs
far apart. We show that a surrogate form of the likelihood score in this
embedding space is a valid approximation of the true likelihood score, making
it possible to steer the denoising process towards the posterior. Across
extensive experiments, our model CoGuide produces more consistent floorplans
from trajectories, and is more robust than differentiable-planner baselines and
guided-diffusion methods.


## Quantitative Finance
### AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration
**Authors**: Binqi Chen, Hongjun Ding, Ning Shen, Jinsheng Huang, Taian Guo, Luchen Liu, Ming Zhang

**Published Date**: 2025-09-29

**Updated Date**: 2025-09-30

**PDF Url**: [2509.25055v2](http://arxiv.org/pdf/2509.25055v2)

**Abstract**: The automated mining of predictive signals, or alphas, is a central challenge
in quantitative finance. While Reinforcement Learning (RL) has emerged as a
promising paradigm for generating formulaic alphas, existing frameworks are
fundamentally hampered by a triad of interconnected issues. First, they suffer
from reward sparsity, where meaningful feedback is only available upon the
completion of a full formula, leading to inefficient and unstable exploration.
Second, they rely on semantically inadequate sequential representations of
mathematical expressions, failing to capture the structure that determine an
alpha's behavior. Third, the standard RL objective of maximizing expected
returns inherently drives policies towards a single optimal mode, directly
contradicting the practical need for a diverse portfolio of non-correlated
alphas. To overcome these challenges, we introduce AlphaSAGE (Structure-Aware
Alpha Mining via Generative Flow Networks for Robust Exploration), a novel
framework is built upon three cornerstone innovations: (1) a structure-aware
encoder based on Relational Graph Convolutional Network (RGCN); (2) a new
framework with Generative Flow Networks (GFlowNets); and (3) a dense,
multi-faceted reward structure. Empirical results demonstrate that AlphaSAGE
outperforms existing baselines in mining a more diverse, novel, and highly
predictive portfolio of alphas, thereby proposing a new paradigm for automated
alpha mining. Our code is available at https://github.com/BerkinChen/AlphaSAGE.


### Rethinking Portfolio Risk: Forecasting Volatility Through Cointegrated Asset Dynamics
**Authors**: Gabriele Casto

**Published Date**: 2025-09-28

**Updated Date**: 2025-09-28

**PDF Url**: [2509.23533v1](http://arxiv.org/pdf/2509.23533v1)

**Abstract**: We introduce the Historical and Dynamic Volatility Ratios (HVR/DVR) and show
that equity and index volatilities are cointegrated at intraday and daily
horizons. This allows us to construct a VECM to forecast portfolio volatility
by exploiting volatility cointegration. On S&P 500 data, HVR is generally
stationary and cointegration with the index is frequent; the VECM
implementation yields substantially lower mean absolute percentage error (MAPE)
than covariance-based forecasts at short- to medium-term horizons across
portfolio sizes. The approach is interpretable and readily implementable,
factorizing covariance into market volatility, relative-volatility ratios, and
correlations.


