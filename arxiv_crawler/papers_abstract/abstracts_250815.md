# Abstracts of Papers

## Physics
### QB Ground State Energy Estimation Benchmark
**Authors**: Nicole Bellonzi, Joshua T. Cantin, Mohammad Reza Jangrouei, Alexander Kunitsa, Jason Necaise, Nam Nguyen, John Penuel, Maxwell D. Radin, Jhonathan Romero Fontalvo, Rashmi Sundareswara, Linjun Wang, Thomas Watts, Yanbing Zhou, Michael C. Garrett, Adam Holmes, Artur F. Izmaylov, Matthew Otten

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10873v1](http://arxiv.org/pdf/2508.10873v1)

**Abstract**: Ground State Energy Estimation (GSEE) is a central problem in quantum
chemistry and condensed matter physics, demanding efficient algorithms to solve
complex electronic structure calculations. This work introduces a structured
benchmarking framework for evaluating the performance of both classical and
quantum solvers on diverse GSEE problem instances. We assess three prominent
methods -- Semistochastic Heat-Bath Configuration Interaction (SHCI), Density
Matrix Renormalization Group (DMRG), and Double-Factorized Quantum Phase
Estimation (DF QPE) -- ighlighting their respective strengths and limitations.
Our results show that fully optimized SHCI achieves near-universal solvability
on the benchmark set, DMRG excels for low-entanglement systems, and DF QPE is
currently constrained by hardware and algorithmic limitations. However, we
observe that many benchmark Hamiltonians are drawn from datasets tailored to
SHCI and related approaches, introducing a bias that favors classical solvers.
To mitigate this, we propose expanding the benchmark suite to include more
challenging, strongly correlated systems to enable a more balanced and
forward-looking evaluation of solver capabilities. As quantum hardware and
algorithms improve, this benchmarking framework will serve as a vital tool for
tracking progress and identifying domains where quantum methods may surpass
classical techniques. The QB-GSEE benchmark repository is openly available at
https://github.com/isi-usc-edu/qb-gsee-benchmark [1]. By maintaining a scalable
and open resource, we aim to accelerate innovation in computational quantum
chemistry and quantum computing.


### TLE-Based A2C Agent for Terrestrial Coverage Orbital Path Planning
**Authors**: Anantha Narayanan, Battu Bhanu Teja, Pruthwik Mishra

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10872v1](http://arxiv.org/pdf/2508.10872v1)

**Abstract**: The increasing congestion of Low Earth Orbit (LEO) poses persistent
challenges to the efficient deployment and safe operation of Earth observation
satellites. Mission planners must now account not only for mission-specific
requirements but also for the increasing collision risk with active satellites
and space debris. This work presents a reinforcement learning framework using
the Advantage Actor-Critic (A2C) algorithm to optimize satellite orbital
parameters for precise terrestrial coverage within predefined surface radii. By
formulating the problem as a Markov Decision Process (MDP) within a custom
OpenAI Gymnasium environment, our method simulates orbital dynamics using
classical Keplerian elements. The agent progressively learns to adjust five of
the orbital parameters - semi-major axis, eccentricity, inclination, right
ascension of ascending node, and the argument of perigee-to achieve targeted
terrestrial coverage. Comparative evaluation against Proximal Policy
Optimization (PPO) demonstrates A2C's superior performance, achieving 5.8x
higher cumulative rewards (10.0 vs 9.263025) while converging in 31.5x fewer
timesteps (2,000 vs 63,000). The A2C agent consistently meets mission
objectives across diverse target coordinates while maintaining computational
efficiency suitable for real-time mission planning applications. Key
contributions include: (1) a TLE-based orbital simulation environment
incorporating physics constraints, (2) validation of actor-critic methods'
superiority over trust region approaches in continuous orbital control, and (3)
demonstration of rapid convergence enabling adaptive satellite deployment. This
approach establishes reinforcement learning as a computationally efficient
alternative for scalable and intelligent LEO mission planning.


### Phased-Array Laser Power Beaming from Cislunar Space to the Lunar Surface
**Authors**: Slava G. Turyshev

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10855v1](http://arxiv.org/pdf/2508.10855v1)

**Abstract**: This paper presents a rigorous analytical framework for quantitatively
evaluating space-based laser power beaming from lunar-orbiting spacecraft to
surface receivers, addressing the critical need for continuous, high-density
energy to sustain lunar exploration and habitation. The framework integrates
physics-based models of spacecraft photovoltaic generation, precise orbital
geometries, time-dependent link availability and slant-range variations,
coherent beam propagation (including transmitter aperture diameter, beam
quality factor, path losses, and pointing jitter), and photonic-to-electrical
conversion at the lunar surface. Particular emphasis is placed on phased-array
transmitter systems, whose large effective apertures significantly reduce beam
divergence relative to single-aperture designs, resulting in
orders-of-magnitude increases in delivered surface power under equivalent
orbital and power conditions. Parametric sensitivity analyses and illustrative
numerical simulations demonstrate how phased-array architectures improve power
density and end-to-end efficiency at operational lunar distances. The study
also examines advanced orbital configurations (e.g., Near-Rectilinear Halo
Orbits, Earth-Moon Lagrange points), real-time adaptive beam steering and
wavefront control, optimized receiver geometries, and thermal/dust mitigation
strategies. The results establish a clear pathway toward scalable, efficient
laser power beaming infrastructures capable of overcoming lunar-specific
challenges - including prolonged darkness and permanently shadowed regions -
and enabling sustained robotic and crewed surface operations.


### Assessing Teleportation of Logical Qubits in a Distributed Quantum Architecture under Error Correction
**Authors**: John Stack, Ming Wang, Frank Mueller

**Published Date**: 2025-04-08

**Updated Date**: 2025-08-14

**PDF Url**: [2504.05611v2](http://arxiv.org/pdf/2504.05611v2)

**Abstract**: Quantum computing is facing challenges in terms of scaling to thousands of
qubits and implementing quantum error correction (QEC). Scaling efforts focus
on connecting multiple smaller quantum devices (nodes) in a distributed manner.
Non-local CNOTs and teleportation of quantum states become important operations
as they enable computation between different nodes in a distributed
architecture. For physical qubits, today's high quantum network noise rates
prevent the execution of distributed operations with useful accuracy. By
employing QEC, we show that non-local operations and teleportation of logical
qubits between nodes are feasible under Surface Code and qLDPC encodings with
very low logical error rates (LER), even with network noise in near-term
regimes. We use circuit-level simulations to assess physical and network noise
regimes ranging from $10^{-1}$ to $10^{-6}$. This is a wider range than
typically studied in circuit level simulations, understanding the behavior of
QEC codes in these regimes is necessary for achieving accurate computation. Our
simulations give evidence that transversal distributed operations may carry
significantly lower LER than lattice surgery. Importantly, we also find that
the LER of our distributed operations decreases exponentially as QEC code
distance increases, proving the feasibility of executing large algorithms on
distributed quantum computers. Our results indicate that non-local CNOTs can be
carried out with a logical error rate of $10^{-12}$ for a physical error rate
of $10^{-3}$ and ebit noise of $10^{-2}$. Teleportations realized with the same
logical error rate under a physical error rate of $3 \times 10^{-4}$ and ebit
noise of $3 \times 10^{-3}$.


### Certified algorithms for equilibrium states of local quantum Hamiltonians
**Authors**: Hamza Fawzi, Omar Fawzi, Samuel O. Scalet

**Published Date**: 2023-11-30

**Updated Date**: 2025-08-14

**PDF Url**: [2311.18706v3](http://arxiv.org/pdf/2311.18706v3)

**Abstract**: Predicting observables in equilibrium states is a central yet notoriously
hard question in quantum many-body systems. In the physically relevant
thermodynamic limit, certain mathematical formulations of this task have even
been shown to result in undecidable problems. Using a finite-size scaling of
algorithms devised for finite systems often fails due to the lack of certified
convergence bounds for this limit. In this work, we design certified algorithms
for computing expectation values of observables in the equilibrium states of
local quantum Hamiltonians, both at zero and positive temperature. Importantly,
our algorithms output rigorous lower and upper bounds on these values. This
allows us to show that expectation values of local observables can be
approximated in finite time, contrasting related undecidability results. When
the Hamiltonian is commuting on a 2-dimensional lattice, we prove fast
convergence of the hierarchy at high temperature and as a result for a desired
precision $\varepsilon$, local observables can be approximated by a convex
optimization program of quasi-polynomial size in $1/\varepsilon$.


### Gauging the variational optimization of projected entangled-pair states
**Authors**: Wei Tang, Laurens Vanderstraeten, Jutho Haegeman

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10822v1](http://arxiv.org/pdf/2508.10822v1)

**Abstract**: Projected entangled-pair states (PEPS) constitute a powerful variational
ansatz for capturing ground state physics of two-dimensional quantum systems.
However, accurately computing and minimizing the energy expectation value
remains challenging, in part because the impact of the gauge degrees of freedom
that are present in the tensor network representation is poorly understood. We
analyze the role of gauge transformations for the case of a U(1)-symmetric PEPS
with point group symmetry, thereby reducing the gauge degrees of freedom to a
single class. We show how gradient-based optimization strategies exploit the
gauge freedom, causing the tensor network contraction to become increasingly
inaccurate and to produce artificially low variational energies. Furthermore,
we develop a gauge-fixed optimization strategy that largely suppresses this
effect, resulting in a more robust optimization. Our study underscores the need
for gauge-aware optimization strategies to guarantee reliability of variational
PEPS in general settings.


### Quantitative Comparison of Fine-Tuning Techniques for Pretrained Latent Diffusion Models in the Generation of Unseen SAR Images
**Authors**: Solène Debuysère, Nicolas Trouvé, Nathan Letheule, Olivier Lévêque, Elise Colin

**Published Date**: 2025-06-16

**Updated Date**: 2025-08-14

**PDF Url**: [2506.13307v2](http://arxiv.org/pdf/2506.13307v2)

**Abstract**: We present a framework for adapting a large pretrained latent diffusion model
to high-resolution Synthetic Aperture Radar (SAR) image generation. The
approach enables controllable synthesis and the creation of rare or
out-of-distribution scenes beyond the training set. Rather than training a
task-specific small model from scratch, we adapt an open-source text-to-image
foundation model to the SAR modality, using its semantic prior to align prompts
with SAR imaging physics (side-looking geometry, slant-range projection, and
coherent speckle with heavy-tailed statistics). Using a 100k-image SAR dataset,
we compare full fine-tuning and parameter-efficient Low-Rank Adaptation (LoRA)
across the UNet diffusion backbone, the Variational Autoencoder (VAE), and the
text encoders. Evaluation combines (i) statistical distances to real SAR
amplitude distributions, (ii) textural similarity via Gray-Level Co-occurrence
Matrix (GLCM) descriptors, and (iii) semantic alignment using a SAR-specialized
CLIP model. Our results show that a hybrid strategy-full UNet tuning with LoRA
on the text encoders and a learned token embedding-best preserves SAR geometry
and texture while maintaining prompt fidelity. The framework supports
text-based control and multimodal conditioning (e.g., segmentation maps,
TerraSAR-X, or optical guidance), opening new paths for large-scale SAR scene
data augmentation and unseen scenario simulation in Earth observation.


### Reinforcement-Learning-Designed Field-Free Sub-Nanosecond Spin-Orbit-Torque Switching
**Authors**: Yuta Igarashi, Junji Fujimoto

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10792v1](http://arxiv.org/pdf/2508.10792v1)

**Abstract**: We demonstrate deterministic, field-free magnetization reversal of a
single-domain nanomagnet within 300 ps under a current density of $3 \times
10^{10}~\mathrm{A/m^2}$ by coupling reinforcement learning (RL) to the
Landau-Lifshitz-Gilbert equation with the spin-orbit torques (SOTs). The RL
agent autonomously discovers a current waveform that minimizes the
magnetization trajectory path and exploits a precessional shortcut enabled by
the field-like SOT and hard-axis anisotropy. From the learned pulse, we extract
a clear physical picture of the dynamics and develop a model-based analytical
framework that establishes a lower bound on the switching time. The control
strategy remains robust across a wide range of damping constants and is
stabilized against thermal fluctuations at higher current densities. We also
discuss feasible experimental implementations for the precessional switching.


### IBEX: Information-Bottleneck-EXplored Coarse-to-Fine Molecular Generation under Limited Data
**Authors**: Dong Xu, Zhangfan Yang, Jenna Xinyi Yao, Shuangbao Song, Zexuan Zhu, Junkai Ji

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10775v1](http://arxiv.org/pdf/2508.10775v1)

**Abstract**: Three-dimensional generative models increasingly drive structure-based drug
discovery, yet it remains constrained by the scarce publicly available
protein-ligand complexes. Under such data scarcity, almost all existing
pipelines struggle to learn transferable geometric priors and consequently
overfit to training-set biases. As such, we present IBEX, an
Information-Bottleneck-EXplored coarse-to-fine pipeline to tackle the chronic
shortage of protein-ligand complex data in structure-based drug design.
Specifically, we use PAC-Bayesian information-bottleneck theory to quantify the
information density of each sample. This analysis reveals how different masking
strategies affect generalization and indicates that, compared with conventional
de novo generation, the constrained Scaffold Hopping task endows the model with
greater effective capacity and improved transfer performance. IBEX retains the
original TargetDiff architecture and hyperparameters for training to generate
molecules compatible with the binding pocket; it then applies an L-BFGS
optimization step to finely refine each conformation by optimizing five
physics-based terms and adjusting six translational and rotational degrees of
freedom in under one second. With only these modifications, IBEX raises the
zero-shot docking success rate on CBGBench CrossDocked2020-based from 53% to
64%, improves the mean Vina score from $-7.41 kcal mol^{-1}$ to $-8.07 kcal
mol^{-1}$, and achieves the best median Vina energy in 57 of 100 pockets versus
3 for the original TargetDiff. IBEX also increases the QED by 25%, achieves
state-of-the-art validity and diversity, and markedly reduces extrapolation
error.


### Natively Trainable Sparse Attention for Hierarchical Point Cloud Datasets
**Authors**: Nicolas Lapautre, Maria Marchenko, Carlos Miguel Patiño, Xin Zhou

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10758v1](http://arxiv.org/pdf/2508.10758v1)

**Abstract**: Unlocking the potential of transformers on datasets of large physical systems
depends on overcoming the quadratic scaling of the attention mechanism. This
work explores combining the Erwin architecture with the Native Sparse Attention
(NSA) mechanism to improve the efficiency and receptive field of transformer
models for large-scale physical systems, addressing the challenge of quadratic
attention complexity. We adapt the NSA mechanism for non-sequential data,
implement the Erwin NSA model, and evaluate it on three datasets from the
physical sciences -- cosmology simulations, molecular dynamics, and air
pressure modeling -- achieving performance that matches or exceeds that of the
original Erwin model. Additionally, we reproduce the experimental results from
the Erwin paper to validate their implementation.


## Diffusion
### A Survey on Diffusion Language Models
**Authors**: Tianyi Li, Mingda Chen, Bowei Guo, Zhiqiang Shen

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10875v1](http://arxiv.org/pdf/2508.10875v1)

**Abstract**: Diffusion Language Models (DLMs) are rapidly emerging as a powerful and
promising alternative to the dominant autoregressive (AR) paradigm. By
generating tokens in parallel through an iterative denoising process, DLMs
possess inherent advantages in reducing inference latency and capturing
bidirectional context, thereby enabling fine-grained control over the
generation process. While achieving a several-fold speed-up, recent
advancements have allowed DLMs to show performance comparable to their
autoregressive counterparts, making them a compelling choice for various
natural language processing tasks. In this survey, we provide a holistic
overview of the current DLM landscape. We trace its evolution and relationship
with other paradigms, such as autoregressive and masked language models, and
cover both foundational principles and state-of-the-art models. Our work offers
an up-to-date, comprehensive taxonomy and an in-depth analysis of current
techniques, from pre-training strategies to advanced post-training methods.
Another contribution of this survey is a thorough review of DLM inference
strategies and optimizations, including improvements in decoding parallelism,
caching mechanisms, and generation quality. We also highlight the latest
approaches to multimodal extensions of DLMs and delineate their applications
across various practical scenarios. Furthermore, our discussion addresses the
limitations and challenges of DLMs, including efficiency, long-sequence
handling, and infrastructure requirements, while outlining future research
directions to sustain progress in this rapidly evolving field. Project GitHub
is available at https://github.com/VILA-Lab/Awesome-DLMs.


### Ultra-High-Definition Reference-Based Landmark Image Super-Resolution with Generative Diffusion Prior
**Authors**: Zhenning Shi, Zizheng Yan, Yuhang Yu, Clara Xue, Jingyu Zhuang, Qi Zhang, Jinwei Chen, Tao Li, Qingnan Fan

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10779v1](http://arxiv.org/pdf/2508.10779v1)

**Abstract**: Reference-based Image Super-Resolution (RefSR) aims to restore a
low-resolution (LR) image by utilizing the semantic and texture information
from an additional reference high-resolution (reference HR) image. Existing
diffusion-based RefSR methods are typically built upon ControlNet, which
struggles to effectively align the information between the LR image and the
reference HR image. Moreover, current RefSR datasets suffer from limited
resolution and poor image quality, resulting in the reference images lacking
sufficient fine-grained details to support high-quality restoration. To
overcome the limitations above, we propose TriFlowSR, a novel framework that
explicitly achieves pattern matching between the LR image and the reference HR
image. Meanwhile, we introduce Landmark-4K, the first RefSR dataset for
Ultra-High-Definition (UHD) landmark scenarios. Considering the UHD scenarios
with real-world degradation, in TriFlowSR, we design a Reference Matching
Strategy to effectively match the LR image with the reference HR image.
Experimental results show that our approach can better utilize the semantic and
texture information of the reference HR image compared to previous methods. To
the best of our knowledge, we propose the first diffusion-based RefSR pipeline
for ultra-high definition landmark scenarios under real-world degradation. Our
code and model will be available at https://github.com/nkicsl/TriFlowSR.


### Video-BLADE: Block-Sparse Attention Meets Step Distillation for Efficient Video Generation
**Authors**: Youping Gu, Xiaolong Li, Yuhao Hu, Bohan Zhuang

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10774v1](http://arxiv.org/pdf/2508.10774v1)

**Abstract**: Diffusion transformers currently lead the field in high-quality video
generation, but their slow iterative denoising process and prohibitive
quadratic attention costs for long sequences create significant inference
bottlenecks. While both step distillation and sparse attention mechanisms have
shown promise as independent acceleration strategies, effectively combining
these approaches presents critical challenges -- training-free integration
yields suboptimal results, while separately training sparse attention after
step distillation requires prohibitively expensive high-quality video data. To
overcome these limitations, we propose BLADE, an innovative data-free joint
training framework that introduces: (1) an Adaptive Block-Sparse Attention
(ASA) mechanism for dynamically generating content-aware sparsity masks to
focus computation on salient spatiotemporal features, and (2) a sparsity-aware
step distillation paradigm built upon Trajectory Distribution Matching (TDM)
that directly incorporates sparsity into the distillation process rather than
treating it as a separate compression step, with fast convergence. We validate
BLADE on text-to-video models like CogVideoX-5B and Wan2.1-1.3B. Our framework
demonstrates remarkable efficiency gains across different scales. On
Wan2.1-1.3B, BLADE achieves a 14.10x end-to-end inference acceleration over a
50-step baseline. Moreover, on models such as CogVideoX-5B with short video
sequence lengths, our framework delivers a robust 8.89x speedup. Crucially, the
acceleration is accompanied by a consistent quality improvement. On the
VBench-2.0 benchmark, BLADE boosts the score of CogVideoX-5B to 0.569 (from
0.534) and Wan2.1-1.3B to 0.570 (from 0.563), results that are further
corroborated by superior ratings in human evaluations. Our code and model
weights are publicly available at: http://ziplab.co/BLADE-Homepage/.


### AEGIS: Authenticity Evaluation Benchmark for AI-Generated Video Sequences
**Authors**: Jieyu Li, Xin Zhang, Joey Tianyi Zhou

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10771v1](http://arxiv.org/pdf/2508.10771v1)

**Abstract**: Recent advances in AI-generated content have fueled the rise of highly
realistic synthetic videos, posing severe risks to societal trust and digital
integrity. Existing benchmarks for video authenticity detection typically
suffer from limited realism, insufficient scale, and inadequate complexity,
failing to effectively evaluate modern vision-language models against
sophisticated forgeries. To address this critical gap, we introduce AEGIS, a
novel large-scale benchmark explicitly targeting the detection of
hyper-realistic and semantically nuanced AI-generated videos. AEGIS comprises
over 10,000 rigorously curated real and synthetic videos generated by diverse,
state-of-the-art generative models, including Stable Video Diffusion,
CogVideoX-5B, KLing, and Sora, encompassing open-source and proprietary
architectures. In particular, AEGIS features specially constructed challenging
subsets enhanced with robustness evaluation. Furthermore, we provide multimodal
annotations spanning Semantic-Authenticity Descriptions, Motion Features, and
Low-level Visual Features, facilitating authenticity detection and supporting
downstream tasks such as multimodal fusion and forgery localization. Extensive
experiments using advanced vision-language models demonstrate limited detection
capabilities on the most challenging subsets of AEGIS, highlighting the
dataset's unique complexity and realism beyond the current generalization
capabilities of existing models. In essence, AEGIS establishes an indispensable
evaluation benchmark, fundamentally advancing research toward developing
genuinely robust, reliable, broadly generalizable video authenticity detection
methodologies capable of addressing real-world forgery threats. Our dataset is
available on https://huggingface.co/datasets/Clarifiedfish/AEGIS.


### MDNS: Masked Diffusion Neural Sampler via Stochastic Optimal Control
**Authors**: Yuchen Zhu, Wei Guo, Jaemoo Choi, Guan-Horng Liu, Yongxin Chen, Molei Tao

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-14

**PDF Url**: [2508.10684v1](http://arxiv.org/pdf/2508.10684v1)

**Abstract**: We study the problem of learning a neural sampler to generate samples from
discrete state spaces where the target probability mass function
$\pi\propto\mathrm{e}^{-U}$ is known up to a normalizing constant, which is an
important task in fields such as statistical physics, machine learning,
combinatorial optimization, etc. To better address this challenging task when
the state space has a large cardinality and the distribution is multi-modal, we
propose $\textbf{M}$asked $\textbf{D}$iffusion $\textbf{N}$eural
$\textbf{S}$ampler ($\textbf{MDNS}$), a novel framework for training discrete
neural samplers by aligning two path measures through a family of learning
objectives, theoretically grounded in the stochastic optimal control of the
continuous-time Markov chains. We validate the efficiency and scalability of
MDNS through extensive experiments on various distributions with distinct
statistical properties, where MDNS learns to accurately sample from the target
distributions despite the extremely high problem dimensions and outperforms
other learning-based baselines by a large margin. A comprehensive study of
ablations and extensions is also provided to demonstrate the efficacy and
potential of the proposed framework.


## Quantitative Finance
### Marketron Through the Looking Glass: From Equity Dynamics to Option Pricing in Incomplete Markets
**Authors**: Igor Halperin, Andrey Itkin

**Published Date**: 2025-08-13

**Updated Date**: 2025-08-13

**PDF Url**: [2508.09863v1](http://arxiv.org/pdf/2508.09863v1)

**Abstract**: The Marketron model, introduced by [Halperin, Itkin, 2025], describes price
formation in inelastic markets as the nonlinear diffusion of a quasiparticle
(the marketron) in a multidimensional space comprising the log-price $x$, a
memory variable $y$ encoding past money flows, and unobservable return
predictors $z$. While the original work calibrated the model to S\&P 500 time
series data, this paper extends the framework to option markets - a
fundamentally distinct challenge due to market incompleteness stemming from
non-tradable state variables. We develop a utility-based pricing approach that
constructs a risk-adjusted measure via the dual solution of an optimal
investment problem. The resulting Hamilton-Jacobi-Bellman (HJB) equation,
though computationally formidable, is solved using a novel methodology enabling
efficient calibration even on standard laptop hardware. Having done that, we
look at the additional question to answer: whether the Marketron model,
calibrated to market option prices, can simultaneously reproduce the
statistical properties of the underlying asset's log-returns. We discuss our
results in view of the long-standing challenge in quantitative finance of
developing an unified framework capable of jointly capturing equity returns,
option smile dynamics, and potentially volatility index behavior.


