# Abstracts of Papers

## Physics
### Physics-Informed Latent Neural Operator for Real-time Predictions of time-dependent parametric PDEs
**Authors**: Sharmila Karumuri, Lori Graham-Brady, Somdatta Goswami

**Published Date**: 2025-01-14

**Updated Date**: 2025-10-28

**PDF Url**: [2501.08428v3](http://arxiv.org/pdf/2501.08428v3)

**Abstract**: Deep operator network (DeepONet) has shown significant promise as surrogate
models for systems governed by partial differential equations (PDEs), enabling
accurate mappings between infinite-dimensional function spaces. However, when
applied to systems with high-dimensional input-output mappings arising from
large numbers of spatial and temporal collocation points, these models often
require heavily overparameterized networks, leading to long training times.
Latent DeepONet addresses some of these challenges by introducing a two-step
approach: first learning a reduced latent space using a separate model,
followed by operator learning within this latent space. While efficient, this
method is inherently data-driven and lacks mechanisms for incorporating
physical laws, limiting its robustness and generalizability in data-scarce
settings. In this work, we propose PI-Latent-NO, a physics-informed latent
neural operator framework that integrates governing physics directly into the
learning process. Our architecture features two coupled DeepONets trained
end-to-end: a Latent-DeepONet that learns a low-dimensional representation of
the solution, and a Reconstruction-DeepONet that maps this latent
representation back to the physical space. By embedding PDE constraints into
the training via automatic differentiation, our method eliminates the need for
labeled training data and ensures physics-consistent predictions. The proposed
framework is both memory and compute-efficient, exhibiting near-constant
scaling with problem size and demonstrating significant speedups over
traditional physics-informed operator models. We validate our approach on a
range of parametric PDEs, showcasing its accuracy, scalability, and suitability
for real-time prediction in complex physical systems.


### DeltaPhi: Physical States Residual Learning for Neural Operators in Data-Limited PDE Solving
**Authors**: Xihang Yue, Yi Yang, Linchao Zhu

**Published Date**: 2024-06-14

**Updated Date**: 2025-10-28

**PDF Url**: [2406.09795v2](http://arxiv.org/pdf/2406.09795v2)

**Abstract**: The limited availability of high-quality training data poses a major obstacle
in data-driven PDE solving, where expensive data collection and resolution
constraints severely impact the ability of neural operator networks to learn
and generalize the underlying physical system. To address this challenge, we
propose DeltaPhi, a novel learning framework that transforms the PDE solving
task from learning direct input-output mappings to learning the residuals
between similar physical states, a fundamentally different approach to neural
operator learning. This reformulation provides implicit data augmentation by
exploiting the inherent stability of physical systems where closer initial
states lead to closer evolution trajectories. DeltaPhi is architecture-agnostic
and can be seamlessly integrated with existing neural operators to enhance
their performance. Extensive experiments demonstrate consistent and significant
improvements across diverse physical systems including regular and irregular
domains, different neural architectures, multiple training data amount, and
cross-resolution scenarios, confirming its effectiveness as a general
enhancement for neural operators in data-limited PDE solving.


### ComboBench: Can LLMs Manipulate Physical Devices to Play Virtual Reality Games?
**Authors**: Shuqing Li, Jiayi Yan, Chenyu Niu, Jen-tse Huang, Yun Peng, Wenxuan Wang, Yepang Liu, Michael R. Lyu

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24706v1](http://arxiv.org/pdf/2510.24706v1)

**Abstract**: Virtual Reality (VR) games require players to translate high-level semantic
actions into precise device manipulations using controllers and head-mounted
displays (HMDs). While humans intuitively perform this translation based on
common sense and embodied understanding, whether Large Language Models (LLMs)
can effectively replicate this ability remains underexplored. This paper
introduces a benchmark, ComboBench, evaluating LLMs' capability to translate
semantic actions into VR device manipulation sequences across 262 scenarios
from four popular VR games: Half-Life: Alyx, Into the Radius, Moss: Book II,
and Vivecraft. We evaluate seven LLMs, including GPT-3.5, GPT-4, GPT-4o,
Gemini-1.5-Pro, LLaMA-3-8B, Mixtral-8x7B, and GLM-4-Flash, compared against
annotated ground truth and human performance. Our results reveal that while
top-performing models like Gemini-1.5-Pro demonstrate strong task decomposition
capabilities, they still struggle with procedural reasoning and spatial
understanding compared to humans. Performance varies significantly across
games, suggesting sensitivity to interaction complexity. Few-shot examples
substantially improve performance, indicating potential for targeted
enhancement of LLMs' VR manipulation capabilities. We release all materials at
https://sites.google.com/view/combobench.


### Fast algorithms enabling optimization and deep learning for photoacoustic tomography in a circular detection geometry
**Authors**: Andreas Hauptmann, Leonid Kunyansky, Jenni Poimala

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24687v1](http://arxiv.org/pdf/2510.24687v1)

**Abstract**: The inverse source problem arising in photoacoustic tomography and in several
other coupled-physics modalities is frequently solved by iterative algorithms.
Such algorithms are based on the minimization of a certain cost functional. In
addition, novel deep learning techniques are currently being investigated to
further improve such optimization approaches. All such methods require multiple
applications of the operator defining the forward problem, and of its adjoint.
In this paper, we present new asymptotically fast algorithms for numerical
evaluation of the forward and adjoint operators, applicable in the circular
acquisition geometry. For an $(n \times n)$ image, our algorithms compute these
operators in $\mathcal{O}(n^2 \log n)$ floating point operations. We
demonstrate the performance of our algorithms in numerical simulations, where
they are used as an integral part of several iterative image reconstruction
techniques: classic variational methods, such as non-negative least squares and
total variation regularized least squares, as well as deep learning methods,
such as learned primal dual. A Python implementation of our algorithms and
computational examples is available to the general public.


### Learning constitutive models and rheology from partial flow measurements
**Authors**: Alp M. Sunol, James V. Roggeveen, Mohammed G. Alhashim, Henry S. Bae, Michael P. Brenner

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24673v1](http://arxiv.org/pdf/2510.24673v1)

**Abstract**: Constitutive laws are at the core of fluid mechanics, relating the fluid
stress to its deformation rate. Unlike Newtonian fluids, most industrial and
biological fluids are non-Newtonian, exhibiting a nonlinear relation.
Accurately characterizing this nonlinearity is essential for predicting flow
behavior in real-world engineering and translational applications. Yet current
methods fall short by relying on bulk rheometer data and simple fits that fail
to capture behaviors relevant in complex geometries and flow conditions.
Data-driven approaches can capture more complex behaviors, but lack
interpretability or consistency. To close this gap, we leverage automatic
differentiation to build an end-to-end framework for robust rheological
learning. We develop a differentiable non-Newtonian fluid solver with a tensor
basis neural network closure that learns stress directly from arbitrary flow
measurements, such as velocimetry data. In parallel, we implement
differentiable versions of major constitutive relations, enabling Bayesian
model parametrization and selection from rheometer data. Our framework predicts
flows in unseen geometries and ensures physical consistency and
interpretability by matching neural network responses to known constitutive
laws. Ultimately, this work lays the groundwork for advanced digital rheometry
capable of comprehensively characterizing non-Newtonian and viscoelastic fluids
under realistic in-situ or in-line operating conditions.


### Pearl: A Foundation Model for Placing Every Atom in the Right Location
**Authors**: Genesis Research Team, Alejandro Dobles, Nina Jovic, Kenneth Leidal, Pranav Murugan, David C. Williams, Drausin Wulsin, Nate Gruver, Christina X. Ji, Korrawat Pruegsanusak, Gianluca Scarpellini, Ansh Sharma, Wojciech Swiderski, Andrea Bootsma, Richard Strong Bowen, Charlotte Chen, Jamin Chen, Marc André Dämgen, Roy Tal Dew, Benjamin DiFrancesco, J. D. Fishman, Alla Ivanova, Zach Kagin, David Li-Bland, Zuli Liu, Igor Morozov, Jeffrey Ouyang-Zhang, Frank C. Pickard IV, Kushal S. Shah, Ben Shor, Gabriel Monteiro da Silva, Maxx Tessmer, Carl Tilbury, Cyr Vetcher, Daniel Zeng, Maruan Al-Shedivat, Aleksandra Faust, Evan N. Feinberg, Michael V. LeVine, Matteus Pan

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24670v1](http://arxiv.org/pdf/2510.24670v1)

**Abstract**: Accurately predicting the three-dimensional structures of protein-ligand
complexes remains a fundamental challenge in computational drug discovery that
limits the pace and success of therapeutic design. Deep learning methods have
recently shown strong potential as structural prediction tools, achieving
promising accuracy across diverse biomolecular systems. However, their
performance and utility are constrained by scarce experimental data,
inefficient architectures, physically invalid poses, and the limited ability to
exploit auxiliary information available at inference. To address these issues,
we introduce Pearl (Placing Every Atom in the Right Location), a foundation
model for protein-ligand cofolding at scale. Pearl addresses these challenges
with three key innovations: (1) training recipes that include large-scale
synthetic data to overcome data scarcity; (2) architectures that incorporate an
SO(3)-equivariant diffusion module to inherently respect 3D rotational
symmetries, improving generalization and sample efficiency, and (3)
controllable inference, including a generalized multi-chain templating system
supporting both protein and non-polymeric components as well as dual
unconditional/conditional modes. Pearl establishes a new state-of-the-art
performance in protein-ligand cofolding. On the key metric of generating
accurate (RMSD < 2 \r{A}) and physically valid poses, Pearl surpasses AlphaFold
3 and other open source baselines on the public Runs N' Poses and PoseBusters
benchmarks, delivering 14.5% and 14.2% improvements, respectively, over the
next best model. In the pocket-conditional cofolding regime, Pearl delivers
$3.6\times$ improvement on a proprietary set of challenging, real-world drug
targets at the more rigorous RMSD < 1 \r{A} threshold. Finally, we demonstrate
that model performance correlates directly with synthetic dataset size used in
training.


### Study of the Semileptonic Decay $Λ\to p\,\ell\,\barν_{\ell}$ in QCD
**Authors**: M. Ahmadi, Z. Rajabi Najjar, K. Azizi

**Published Date**: 2025-09-27

**Updated Date**: 2025-10-28

**PDF Url**: [2509.23421v2](http://arxiv.org/pdf/2509.23421v2)

**Abstract**: We conduct a comprehensive study of the semileptonic decay process \(\Lambda
\to p\,\ell\,\bar{\nu}_{\ell}\), focusing on the determination of all six
vector and axial-vector form factors that govern the low-energy hadronic matrix
elements of the underlying theory. These invariant form factors constitute the
essential inputs for describing the decay, and their dependence on the momentum
transfer \(q^{2}\) is analyzed across the entire physical kinematic region. To
parameterize the \(q^{2}\)-dependence, we adopt both the \(z\)-expansion
formalism and a polynomial fitting approach. Utilizing these parameterizations,
we compute the exclusive decay widths for both the electron and muon channels
and subsequently extract the corresponding branching ratios. Furthermore, we
evaluate the ratio of decay widths between the muon and electron channels,
defined as $R^{\mu e} \equiv \frac{\Gamma(\Lambda \to
p\,\mu\,\bar{\nu}_{\mu})}{\Gamma(\Lambda \to p\,e\,\bar{\nu}_{e})}$, obtaining
\(R^{\mu e} = 0.196^{+0.009}_{-0.012}\) from the polynomial fit and \(R^{\mu e}
= 0.174^{+0.002}_{-0.005}\) from the \(z\)-expansion. While both ratios are
compatible with previously reported values in the literature, the result from
the \(z\)-expansion exhibits particularly strong agreement with the averages
reported by the Particle Data Group (PDG).


### Radiation enhanced diffusion in cartilages as a physical mechanism underlying radiation treatments of osteoarthritis and related disorders
**Authors**: Diana Shvydka, Victor Karpov

**Published Date**: 2025-10-27

**Updated Date**: 2025-10-28

**PDF Url**: [2510.22903v2](http://arxiv.org/pdf/2510.22903v2)

**Abstract**: Degradation of joint cartilages can result in osteoarthritis (OA) affecting
about 10\% of the US population and responsible for significant hospitalization
costs. While observations show that low dose radiation treatments (LDRT) bring
improvements for a majority of OA patients, the underlying mechanism is not
sufficiently understood. Here, we show how the radiation enhanced diffusion
(RED) can boost the molecular transport in cartilages promoting cartilage
self-healing rendering a mechanism for the observed positive LDRT effects on
OA. Along with quantitative estimates for RED, we predict a related phenomenon
of the electric charge build up that allows LDRT schedules promoting desirable
types of molecular transports dominated by either positive or negative
molecular species. Our analyses call upon further experimental verifications
and clinical trials with curative rather than palliative intent. In addition to
OA applications, our developed approaches can be useful for sports medicine
dealing with damage or degeneration of the articular cartilages.


### Statistical physics of deep learning: Optimal learning of a multi-layer perceptron near interpolation
**Authors**: Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore, Rudy Skerk

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24616v1](http://arxiv.org/pdf/2510.24616v1)

**Abstract**: For three decades statistical physics has been providing a framework to
analyse neural networks. A long-standing question remained on its capacity to
tackle deep learning models capturing rich feature learning effects, thus going
beyond the narrow networks or kernel methods analysed until now. We positively
answer through the study of the supervised learning of a multi-layer
perceptron. Importantly, (i) its width scales as the input dimension, making it
more prone to feature learning than ultra wide networks, and more expressive
than narrow ones or with fixed embedding layers; and (ii) we focus on the
challenging interpolation regime where the number of trainable parameters and
data are comparable, which forces the model to adapt to the task. We consider
the matched teacher-student setting. It provides the fundamental limits of
learning random deep neural network targets and helps in identifying the
sufficient statistics describing what is learnt by an optimally trained network
as the data budget increases. A rich phenomenology emerges with various
learning transitions. With enough data optimal performance is attained through
model's "specialisation" towards the target, but it can be hard to reach for
training algorithms which get attracted by sub-optimal solutions predicted by
the theory. Specialisation occurs inhomogeneously across layers, propagating
from shallow towards deep ones, but also across neurons in each layer.
Furthermore, deeper targets are harder to learn. Despite its simplicity, the
Bayesian-optimal setting provides insights on how the depth, non-linearity and
finite (proportional) width influence neural networks in the feature learning
regime that are potentially relevant way beyond it.


### Efficient magic state cultivation with lattice surgery
**Authors**: Yutaka Hirano, Riki Toshio, Tomohiro Itogawa, Keisuke Fujii

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24615v1](http://arxiv.org/pdf/2510.24615v1)

**Abstract**: Magic state distillation plays a crucial role in fault-tolerant quantum
computation and represents a major bottleneck. In contrast to traditional
logical-level distillation, physical-level distillation offers significant
overhead reduction by enabling direct implementation with physical gates. Magic
state cultivation is a state-of-the-art physical-level distillation protocol
that is compatible with the square-grid connectivity and yields high-fidelity
magic states. However, it relies on the complex grafted code, which incurs
substantial spacetime overhead and complicates practical implementation. In
this work, we propose an efficient cultivation-based protocol compatible with
the square-grid connectivity. We reduce the spatial overhead by avoiding the
grafted code and further reduce the average spacetime overhead by utilizing
code expansion and enabling early rejection. Numerical simulations show that,
with a color code distance of 3 and a physical error probability of $10^{-3}$,
our protocol achieves a logical error probability for the resulting magic state
comparable to that of magic state cultivation ($\approx 3 \times 10^{-6}$),
while requiring about half the spacetime overhead. Our work provides an
efficient and simple distillation protocol suitable for megaquop use cases and
early fault-tolerant devices.


## Diffusion
### Generative View Stitching
**Authors**: Chonghyuk Song, Michal Stary, Boyuan Chen, George Kopanas, Vincent Sitzmann

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24718v1](http://arxiv.org/pdf/2510.24718v1)

**Abstract**: Autoregressive video diffusion models are capable of long rollouts that are
stable and consistent with history, but they are unable to guide the current
generation with conditioning from the future. In camera-guided video generation
with a predefined camera trajectory, this limitation leads to collisions with
the generated scene, after which autoregression quickly collapses. To address
this, we propose Generative View Stitching (GVS), which samples the entire
sequence in parallel such that the generated scene is faithful to every part of
the predefined camera trajectory. Our main contribution is a sampling algorithm
that extends prior work on diffusion stitching for robot planning to video
generation. While such stitching methods usually require a specially trained
model, GVS is compatible with any off-the-shelf video model trained with
Diffusion Forcing, a prevalent sequence diffusion framework that we show
already provides the affordances necessary for stitching. We then introduce
Omni Guidance, a technique that enhances the temporal consistency in stitching
by conditioning on both the past and future, and that enables our proposed
loop-closing mechanism for delivering long-range coherence. Overall, GVS
achieves camera-guided video generation that is stable, collision-free,
frame-to-frame consistent, and closes loops for a variety of predefined camera
paths, including Oscar Reutersv\"ard's Impossible Staircase. Results are best
viewed as videos at https://andrewsonga.github.io/gvs.


### Causal Ordering for Structure Learning From Time Series
**Authors**: Pedro P. Sanchez, Damian Machlanski, Steven McDonagh, Sotirios A. Tsaftaris

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24639v1](http://arxiv.org/pdf/2510.24639v1)

**Abstract**: Predicting causal structure from time series data is crucial for
understanding complex phenomena in physiology, brain connectivity, climate
dynamics, and socio-economic behaviour. Causal discovery in time series is
hindered by the combinatorial complexity of identifying true causal
relationships, especially as the number of variables and time points grow. A
common approach to simplify the task is the so-called ordering-based methods.
Traditional ordering methods inherently limit the representational capacity of
the resulting model. In this work, we fix this issue by leveraging multiple
valid causal orderings, instead of a single one as standard practice. We
propose DOTS (Diffusion Ordered Temporal Structure), using diffusion-based
causal discovery for temporal data. By integrating multiple orderings, DOTS
effectively recovers the transitive closure of the underlying directed acyclic
graph, mitigating spurious artifacts inherent in single-ordering approaches. We
formalise the problem under standard assumptions such as stationarity and the
additive noise model, and leverage score matching with diffusion processes to
enable efficient Hessian estimation. Extensive experiments validate the
approach. Empirical evaluations on synthetic and real-world datasets
demonstrate that DOTS outperforms state-of-the-art baselines, offering a
scalable and robust approach to temporal causal discovery. On synthetic
benchmarks ($d{=}\!3-\!6$ variables, $T{=}200\!-\!5{,}000$ samples), DOTS
improves mean window-graph $F1$ from $0.63$ (best baseline) to $0.81$. On the
CausalTime real-world benchmark ($d{=}20\!-\!36$), while baselines remain the
best on individual datasets, DOTS attains the highest average summary-graph
$F1$ while halving runtime relative to graph-optimisation methods. These
results establish DOTS as a scalable and accurate solution for temporal causal
discovery.


### Diffusion Models for Wireless Transceivers: From Pilot-Efficient Channel Estimation to AI-Native 6G Receivers
**Authors**: Yuzhi Yang, Sen Yan, Weijie Zhou, Brahim Mefgouda, Ridong Li, Zhaoyang Zhang, Mérouane Debbah

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24495v1](http://arxiv.org/pdf/2510.24495v1)

**Abstract**: With the development of artificial intelligence (AI) techniques, implementing
AI-based techniques to improve wireless transceivers becomes an emerging
research topic. Within this context, AI-based channel characterization and
estimation become the focus since these methods have not been solved by
traditional methods very well and have become the bottleneck of transceiver
efficiency in large-scale orthogonal frequency division multiplexing (OFDM)
systems. Specifically, by formulating channel estimation as a generative AI
problem, generative AI methods such as diffusion models (DMs) can efficiently
deal with rough initial estimations and have great potential to cooperate with
traditional signal processing methods. This paper focuses on the transceiver
design of OFDM systems based on DMs, provides an illustration of the potential
of DMs in wireless transceivers, and points out the related research directions
brought by DMs. We also provide a proof-of-concept case study of further
adapting DMs for better wireless receiver performance.


### Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies
**Authors**: Zhixuan Liang, Yizhuo Li, Tianshuo Yang, Chengyue Wu, Sitong Mao, Tian Nian, Liuao Pei, Shunbo Zhou, Xiaokang Yang, Jiangmiao Pang, Yao Mu, Ping Luo

**Published Date**: 2025-08-27

**Updated Date**: 2025-10-28

**PDF Url**: [2508.20072v2](http://arxiv.org/pdf/2508.20072v2)

**Abstract**: Vision-Language-Action (VLA) models adapt large vision-language backbones to
map images and instructions into robot actions. However, prevailing VLAs either
generate actions auto-regressively in a fixed left-to-right order or attach
separate MLP or diffusion heads outside the backbone, leading to fragmented
information pathways and specialized training requirements that hinder a
unified, scalable architecture. We present Discrete Diffusion VLA, a
unified-transformer policy that models discretized action chunks with discrete
diffusion. The design retains diffusion's progressive refinement paradigm while
remaining natively compatible with the discrete token interface of VLMs. Our
method achieves an adaptive decoding order that resolves easy action elements
before harder ones and uses secondary re-masking to revisit uncertain
predictions across refinement rounds, which improves consistency and enables
robust error correction. This unified decoder preserves pre-trained
vision-language priors, supports parallel decoding, breaks the autoregressive
bottleneck, and reduces the number of function evaluations. Discrete Diffusion
VLA achieves 96.3% avg. success rates on LIBERO, 71.2% visual matching on
SimplerEnv-Fractal and 54.2% overall on SimplerEnv-Bridge, improving over
autoregressive, MLP decoder and continuous diffusion baselines. These findings
indicate that discrete-diffusion VLA supports precise action modeling and
consistent training, laying groundwork for scaling VLA to larger models and
datasets. Our project page is https://github.com/Liang-ZX/DiscreteDiffusionVLA


### Rethinking Visual Intelligence: Insights from Video Pretraining
**Authors**: Pablo Acuaviva, Aram Davtyan, Mariam Hassan, Sebastian Stapf, Ahmad Rahimi, Alexandre Alahi, Paolo Favaro

**Published Date**: 2025-10-28

**Updated Date**: 2025-10-28

**PDF Url**: [2510.24448v1](http://arxiv.org/pdf/2510.24448v1)

**Abstract**: Large language models (LLMs) have demonstrated that large-scale pretraining
enables systems to adapt rapidly to new problems with little supervision in the
language domain. This success, however, has not translated as effectively to
the visual domain, where models, including LLMs, continue to struggle with
compositional understanding, sample efficiency, and general-purpose
problem-solving. We investigate Video Diffusion Models (VDMs) as a promising
direction for bridging this gap. Pretraining on spatiotemporal data endows
these models with strong inductive biases for structure and dynamics, which we
hypothesize can support broad task adaptability. To test this, we design a
controlled evaluation in which both a pretrained LLM and a pretrained VDM are
equipped with lightweight adapters and presented with tasks in their natural
modalities. Across benchmarks including ARC-AGI, ConceptARC, visual games,
route planning, and cellular automata, VDMs demonstrate higher data efficiency
than their language counterparts. Taken together, our results indicate that
video pretraining offers inductive biases that support progress toward visual
foundation models.


## Quantitative Finance
### Stochastic PDEs and Quantitative Finance: The Black-Scholes-Merton Model of Options Pricing and Riskless Trading
**Authors**: Brandon Kaplowitz, Siddharth G. Reddy

**Published Date**: 2012-12-09

**Updated Date**: 2025-10-26

**PDF Url**: [1212.1919v3](http://arxiv.org/pdf/1212.1919v3)

**Abstract**: Differential equations can be used to construct predictive models of a
diverse set of real-world phenomena like heat transfer, predator-prey
interactions, and missile tracking. In our work, we explore one particular
application of stochastic differential equations, the Black-Scholes-Merton
model, which can be used to predict the prices of financial derivatives and
maintain a riskless, hedged position in the stock market. This paper is
intended to provide the reader with a history, derivation, and implementation
of the canonical model as well as an improved trading strategy that better
handles arbitrage opportunities in high-volatility markets. Our attempted
improvements may be broken into two components: an implementation of 24-hour,
worldwide trading designed to create a continuous trading scenario and the use
of the Student's t-distribution (with two degrees of freedom) in evaluating the
Black-Scholes equations.


