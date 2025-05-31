# Abstracts of Papers

## Physics
### PhyX: Does Your Model Have the "Wits" for Physical Reasoning?
**Authors**: Hui Shen, Taiqiang Wu, Qi Han, Yunta Hsieh, Jizhou Wang, Yuyue Zhang, Yuxin Cheng, Zijian Hao, Yuansheng Ni, Xin Wang, Zhongwei Wan, Kai Zhang, Wendong Xu, Jing Xiong, Ping Luo, Wenhu Chen, Chaofan Tao, Zhuoqing Mao, Ngai Wong

**Published Date**: 2025-05-21

**Updated Date**: 2025-05-29

**PDF Url**: [2505.15929v2](http://arxiv.org/pdf/2505.15929v2)

**Abstract**: Existing benchmarks fail to capture a crucial aspect of intelligence:
physical reasoning, the integrated ability to combine domain knowledge,
symbolic reasoning, and understanding of real-world constraints. To address
this gap, we introduce PhyX: the first large-scale benchmark designed to assess
models capacity for physics-grounded reasoning in visual scenarios. PhyX
includes 3K meticulously curated multimodal questions spanning 6 reasoning
types across 25 sub-domains and 6 core physics domains: thermodynamics,
electromagnetism, mechanics, modern physics, optics, and wave\&acoustics. In
our comprehensive evaluation, even state-of-the-art models struggle
significantly with physical reasoning. GPT-4o, Claude3.7-Sonnet, and
GPT-o4-mini achieve only 32.5%, 42.2%, and 45.8% accuracy
respectively-performance gaps exceeding 29% compared to human experts. Our
analysis exposes critical limitations in current models: over-reliance on
memorized disciplinary knowledge, excessive dependence on mathematical
formulations, and surface-level visual pattern matching rather than genuine
physical understanding. We provide in-depth analysis through fine-grained
statistics, detailed case studies, and multiple evaluation paradigms to
thoroughly examine physical reasoning capabilities. To ensure reproducibility,
we implement a compatible evaluation protocol based on widely-used toolkits
such as VLMEvalKit, enabling one-click evaluation. More details are available
on our project page: https://phyx-bench.github.io/.


### Understanding and Mitigating Distribution Shifts For Machine Learning Force Fields
**Authors**: Tobias Kreiman, Aditi S. Krishnapriyan

**Published Date**: 2025-03-11

**Updated Date**: 2025-05-29

**PDF Url**: [2503.08674v2](http://arxiv.org/pdf/2503.08674v2)

**Abstract**: Machine Learning Force Fields (MLFFs) are a promising alternative to
expensive ab initio quantum mechanical molecular simulations. Given the
diversity of chemical spaces that are of interest and the cost of generating
new data, it is important to understand how MLFFs generalize beyond their
training distributions. In order to characterize and better understand
distribution shifts in MLFFs, we conduct diagnostic experiments on chemical
datasets, revealing common shifts that pose significant challenges, even for
large foundation models trained on extensive data. Based on these observations,
we hypothesize that current supervised training methods inadequately regularize
MLFFs, resulting in overfitting and learning poor representations of
out-of-distribution systems. We then propose two new methods as initial steps
for mitigating distribution shifts for MLFFs. Our methods focus on test-time
refinement strategies that incur minimal computational cost and do not use
expensive ab initio reference labels. The first strategy, based on spectral
graph theory, modifies the edges of test graphs to align with graph structures
seen during training. Our second strategy improves representations for
out-of-distribution systems at test-time by taking gradient steps using an
auxiliary objective, such as a cheap physical prior. Our test-time refinement
strategies significantly reduce errors on out-of-distribution systems,
suggesting that MLFFs are capable of and can move towards modeling diverse
chemical spaces, but are not being effectively trained to do so. Our
experiments establish clear benchmarks for evaluating the generalization
capabilities of the next generation of MLFFs. Our code is available at
https://tkreiman.github.io/projects/mlff_distribution_shifts/.


### Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better
**Authors**: Danny Driess, Jost Tobias Springenberg, Brian Ichter, Lili Yu, Adrian Li-Bell, Karl Pertsch, Allen Z. Ren, Homer Walke, Quan Vuong, Lucy Xiaoyang Shi, Sergey Levine

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23705v1](http://arxiv.org/pdf/2505.23705v1)

**Abstract**: Vision-language-action (VLA) models provide a powerful approach to training
control policies for physical systems, such as robots, by combining end-to-end
learning with transfer of semantic knowledge from web-scale vision-language
model (VLM) training. However, the constraints of real-time control are often
at odds with the design of VLMs: the most powerful VLMs have tens or hundreds
of billions of parameters, presenting an obstacle to real-time inference, and
operate on discrete tokens rather than the continuous-valued outputs that are
required for controlling robots. To address this challenge, recent VLA models
have used specialized modules for efficient continuous control, such as action
experts or continuous output heads, which typically require adding new
untrained parameters to the pretrained VLM backbone. While these modules
improve real-time and control capabilities, it remains an open question whether
they preserve or degrade the semantic knowledge contained in the pretrained
VLM, and what effect they have on the VLA training dynamics. In this paper, we
study this question in the context of VLAs that include a continuous diffusion
or flow matching action expert, showing that naively including such experts
significantly harms both training speed and knowledge transfer. We provide an
extensive analysis of various design choices, their impact on performance and
knowledge transfer, and propose a technique for insulating the VLM backbone
during VLA training that mitigates this issue. Videos are available at
https://pi.website/research/knowledge_insulation.


### (U)NFV: Supervised and Unsupervised Neural Finite Volume Methods for Solving Hyperbolic PDEs
**Authors**: Nathan Lichtlé, Alexi Canesse, Zhe Fu, Hossein Nick Zinat Matin, Maria Laura Delle Monache, Alexandre M. Bayen

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23702v1](http://arxiv.org/pdf/2505.23702v1)

**Abstract**: We introduce (U)NFV, a modular neural network architecture that generalizes
classical finite volume (FV) methods for solving hyperbolic conservation laws.
Hyperbolic partial differential equations (PDEs) are challenging to solve,
particularly conservation laws whose physically relevant solutions contain
shocks and discontinuities. FV methods are widely used for their mathematical
properties: convergence to entropy solutions, flow conservation, or total
variation diminishing, but often lack accuracy and flexibility in complex
settings. Neural Finite Volume addresses these limitations by learning update
rules over extended spatial and temporal stencils while preserving conservation
structure. It supports both supervised training on solution data (NFV) and
unsupervised training via weak-form residual loss (UNFV). Applied to
first-order conservation laws, (U)NFV achieves up to 10x lower error than
Godunov's method, outperforms ENO/WENO, and rivals discontinuous Galerkin
solvers with far less complexity. On traffic modeling problems, both from PDEs
and from experimental highway data, (U)NFV captures nonlinear wave dynamics
with significantly higher fidelity and scalability than traditional FV
approaches.


### Proposal for simplified template cross-sections extension using $\cal{CP}$ observables in $t\overline{t}H$
**Authors**: Carnelli Alberto

**Published Date**: 2025-01-08

**Updated Date**: 2025-05-29

**PDF Url**: [2501.04837v2](http://arxiv.org/pdf/2501.04837v2)

**Abstract**: The Large Hadron Collider (LHC) offers a unique opportunity to investigate
$\cal{CP}$ violation in the Yukawa coupling between the Higgs boson and the top
quark by studying Higgs production in association with top quarks; this is of
fundamental importance, seeing that the $\cal{CP}$ properties of the Higgs
boson are yet to measure with high precision. To address this, the focus of
this work has been an extension of the simplified template cross-section (STXS)
framework, devised to be sensitive to $\cal{CP}$ effects. Our study focused on
$\cal{CP}$-sensitive observables across multiple Higgs decay channels,
comparing their performances. The result indicates that the most efficient
extension of the current binning used in the STXS framework, which currently
uses the Higgs boson's transverse momentum $p_{T,H}$, requires adding one
further split using $\cal{CP}$-sensitive observables. Between these
observables, one of the best is the Collins-Soper angle $|\cos\theta^*|$, a
variable derived from momenta information of the top quarks. We have
investigated the improvement brought by our two-dimensional STXS setup and
compared it to the currently employed methodologies, finding an increase in
performances at an integrated luminosity of $300$ fb$^{-1}$. Moreover, our
results highlight that this advantage seems to be present also at $3000$
fb$^{-1}$.


### Measurements $\mathit{with}$ probabilities in the final state proposal
**Authors**: Ahmed Almheiri

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23664v1](http://arxiv.org/pdf/2505.23664v1)

**Abstract**: Bousso and Stanford (BS) argued that the black hole final state proposal
leads to acausal effects and ill-defined probabilities for the AMPS experiment.
We identify a loophole in their analysis using insights from entanglement wedge
reconstruction and replica wormholes. We trace the cause of the BS problems to
the misidentification of the physical interior where the second AMPS
measurement happens from among the multiple interiors introduced by the first
measurement.


### AMBER: Adaptive Mesh Generation by Iterative Mesh Resolution Prediction
**Authors**: Niklas Freymuth, Tobias Würth, Nicolas Schreiber, Balazs Gyenes, Andreas Boltres, Johannes Mitsch, Aleksandar Taranovic, Tai Hoang, Philipp Dahlinger, Philipp Becker, Luise Kärger, Gerhard Neumann

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23663v1](http://arxiv.org/pdf/2505.23663v1)

**Abstract**: The cost and accuracy of simulating complex physical systems using the Finite
Element Method (FEM) scales with the resolution of the underlying mesh.
Adaptive meshes improve computational efficiency by refining resolution in
critical regions, but typically require task-specific heuristics or cumbersome
manual design by a human expert. We propose Adaptive Meshing By Expert
Reconstruction (AMBER), a supervised learning approach to mesh adaptation.
Starting from a coarse mesh, AMBER iteratively predicts the sizing field, i.e.,
a function mapping from the geometry to the local element size of the target
mesh, and uses this prediction to produce a new intermediate mesh using an
out-of-the-box mesh generator. This process is enabled through a hierarchical
graph neural network, and relies on data augmentation by automatically
projecting expert labels onto AMBER-generated data during training. We evaluate
AMBER on 2D and 3D datasets, including classical physics problems, mechanical
components, and real-world industrial designs with human expert meshes. AMBER
generalizes to unseen geometries and consistently outperforms multiple recent
baselines, including ones using Graph and Convolutional Neural Networks, and
Reinforcement Learning-based approaches.


### Higher-order Tuning of Interface Physics in Multiphase Lattice Boltzmann
**Authors**: Matteo Lulli, Emily S. C. Ching

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23647v1](http://arxiv.org/pdf/2505.23647v1)

**Abstract**: Tuning the interface properties of multiphase models is of paramount
importance to the final goal of achieving a one-to-one matching with nucleation
and cavitation experiments. The surface tension, at the leading order, and the
Tolman length, at higher order, play a crucial role in the estimation of the
free-energy barrier determining the experimentally observed nucleation rates.
The lattice Boltzmann method allows for a computationally efficient modelling
approach of multiphase flows, however, tuning results are concerned with the
surface tension and neglect the Tolman length. We present a novel perspective
that leverages all the degrees of freedom hidden in the forcing stencil of the
Shan-Chen multiphase model. By means of the lattice pressure tensor we
determine and tune the coefficients of higher-order derivative terms related to
surface tension and Tolman length at constant interface width and density
ratio. We test the method by means of both hydrostatic and dynamic simulations
and demonstrate the dependence of homogeneous nucleation rates on the value of
the Tolman length. This work provides a new tool that can be integrated with
previously existing strategies thus marking a step forwards to a high-fidelity
modelling of phase-changing fluid dynamics.


### The Multiverse: a Philosophical Introduction
**Authors**: Jeremy Butterfield

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23639v1](http://arxiv.org/pdf/2505.23639v1)

**Abstract**: This book is a philosopher's introduction to the idea that our universe is
just one of many universes. I present and assess three versions of the idea:
one version from philosophy, and two from physics. In short, they are: all the
logically possible worlds; all the branches of the quantum state, in an
Everettian interpretation of quantum theory; and all the bubbles of
inflationary cosmology. For each proposal, I choose one main philosophical
question to discuss in depth. They are, respectively: what is a possible world;
what is chance; and what is explanation. But before treating these proposals
and their associated questions, I set the stage by reviewing physics and
philosophy from about 1600 to about 1900; and a final Chapter compares and
contrasts the proposals.


## Diffusion
### MAGREF: Masked Guidance for Any-Reference Video Generation
**Authors**: Yufan Deng, Xun Guo, Yuanyang Yin, Jacob Zhiyuan Fang, Yiding Yang, Yizhi Wang, Shenghai Yuan, Angtian Wang, Bo Liu, Haibin Huang, Chongyang Ma

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23742v1](http://arxiv.org/pdf/2505.23742v1)

**Abstract**: Video generation has made substantial strides with the emergence of deep
generative models, especially diffusion-based approaches. However, video
generation based on multiple reference subjects still faces significant
challenges in maintaining multi-subject consistency and ensuring high
generation quality. In this paper, we propose MAGREF, a unified framework for
any-reference video generation that introduces masked guidance to enable
coherent multi-subject video synthesis conditioned on diverse reference images
and a textual prompt. Specifically, we propose (1) a region-aware dynamic
masking mechanism that enables a single model to flexibly handle various
subject inference, including humans, objects, and backgrounds, without
architectural changes, and (2) a pixel-wise channel concatenation mechanism
that operates on the channel dimension to better preserve appearance features.
Our model delivers state-of-the-art video generation quality, generalizing from
single-subject training to complex multi-subject scenarios with coherent
synthesis and precise control over individual subjects, outperforming existing
open-source and commercial baselines. To facilitate evaluation, we also
introduce a comprehensive multi-subject video benchmark. Extensive experiments
demonstrate the effectiveness of our approach, paving the way for scalable,
controllable, and high-fidelity multi-subject video synthesis. Code and model
can be found at: https://github.com/MAGREF-Video/MAGREF


### DiffER: Categorical Diffusion for Chemical Retrosynthesis
**Authors**: Sean Current, Ziqi Chen, Daniel Adu-Ampratwum, Xia Ning, Srinivasan Parthasarathy

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23721v1](http://arxiv.org/pdf/2505.23721v1)

**Abstract**: Methods for automatic chemical retrosynthesis have found recent success
through the application of models traditionally built for natural language
processing, primarily through transformer neural networks. These models have
demonstrated significant ability to translate between the SMILES encodings of
chemical products and reactants, but are constrained as a result of their
autoregressive nature. We propose DiffER, an alternative template-free method
for retrosynthesis prediction in the form of categorical diffusion, which
allows the entire output SMILES sequence to be predicted in unison. We
construct an ensemble of diffusion models which achieves state-of-the-art
performance for top-1 accuracy and competitive performance for top-3, top-5,
and top-10 accuracy among template-free methods. We prove that DiffER is a
strong baseline for a new class of template-free model, capable of learning a
variety of synthetic techniques used in laboratory settings and outperforming a
variety of other template-free methods on top-k accuracy metrics. By
constructing an ensemble of categorical diffusion models with a novel length
prediction component with variance, our method is able to approximately sample
from the posterior distribution of reactants, producing results with strong
metrics of confidence and likelihood. Furthermore, our analyses demonstrate
that accurate prediction of the SMILES sequence length is key to further
boosting the performance of categorical diffusion models.


### Optimization-Free Diffusion Model -- A Perturbation Theory Approach
**Authors**: Yuehaw Khoo, Mathias Oster, Yifan Peng

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23652v1](http://arxiv.org/pdf/2505.23652v1)

**Abstract**: Diffusion models have emerged as a powerful framework in generative modeling,
typically relying on optimizing neural networks to estimate the score function
via forward SDE simulations. In this work, we propose an alternative method
that is both optimization-free and forward SDE-free. By expanding the score
function in a sparse set of eigenbasis of the backward Kolmogorov operator
associated with the diffusion process, we reformulate score estimation as the
solution to a linear system, avoiding iterative optimization and time-dependent
sample generation. We analyze the approximation error using perturbation theory
and demonstrate the effectiveness of our method on high-dimensional Boltzmann
distributions and real-world datasets.


### Inference-time Scaling of Diffusion Models through Classical Search
**Authors**: Xiangcheng Zhang, Haowei Lin, Haotian Ye, James Zou, Jianzhu Ma, Yitao Liang, Yilun Du

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23614v1](http://arxiv.org/pdf/2505.23614v1)

**Abstract**: Classical search algorithms have long underpinned modern artificial
intelligence. In this work, we tackle the challenge of inference-time control
in diffusion models -- adapting generated outputs to meet diverse test-time
objectives -- using principles from classical search. We propose a general
framework that orchestrates local and global search to efficiently navigate the
generative space. It employs a theoretically grounded local search via annealed
Langevin MCMC and performs compute-efficient global exploration using
breadth-first and depth-first tree search. We evaluate our approach on a range
of challenging domains, including planning, offline reinforcement learning, and
image generation. Across all tasks, we observe significant gains in both
performance and efficiency. These results show that classical search provides a
principled and practical foundation for inference-time scaling in diffusion
models. Project page at diffusion-inference-scaling.github.io.


### Muddit: Liberating Generation Beyond Text-to-Image with a Unified Discrete Diffusion Model
**Authors**: Qingyu Shi, Jinbin Bai, Zhuoran Zhao, Wenhao Chai, Kaidong Yu, Jianzong Wu, Shuangyong Song, Yunhai Tong, Xiangtai Li, Xuelong Li, Shuicheng Yan

**Published Date**: 2025-05-29

**Updated Date**: 2025-05-29

**PDF Url**: [2505.23606v1](http://arxiv.org/pdf/2505.23606v1)

**Abstract**: Unified generation models aim to handle diverse tasks across modalities --
such as text generation, image generation, and vision-language reasoning --
within a single architecture and decoding paradigm. Autoregressive unified
models suffer from slow inference due to sequential decoding, and
non-autoregressive unified models suffer from weak generalization due to
limited pretrained backbones. We introduce Muddit, a unified discrete diffusion
transformer that enables fast and parallel generation across both text and
image modalities. Unlike prior unified diffusion models trained from scratch,
Muddit integrates strong visual priors from a pretrained text-to-image backbone
with a lightweight text decoder, enabling flexible and high-quality multimodal
generation under a unified architecture. Empirical results show that Muddit
achieves competitive or superior performance compared to significantly larger
autoregressive models in both quality and efficiency. The work highlights the
potential of purely discrete diffusion, when equipped with strong visual
priors, as a scalable and effective backbone for unified generation.


