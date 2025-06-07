# Abstracts of Papers

## Physics
### Direct Numerical Layout Generation for 3D Indoor Scene Synthesis via Spatial Reasoning
**Authors**: Xingjian Ran, Yixuan Li, Linning Xu, Mulin Yu, Bo Dai

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05341v1](http://arxiv.org/pdf/2506.05341v1)

**Abstract**: Realistic 3D indoor scene synthesis is vital for embodied AI and digital
content creation. It can be naturally divided into two subtasks: object
generation and layout generation. While recent generative models have
significantly advanced object-level quality and controllability, layout
generation remains challenging due to limited datasets. Existing methods either
overfit to these datasets or rely on predefined constraints to optimize
numerical layout that sacrifice flexibility. As a result, they fail to generate
scenes that are both open-vocabulary and aligned with fine-grained user
instructions. We introduce DirectLayout, a framework that directly generates
numerical 3D layouts from text descriptions using generalizable spatial
reasoning of large language models (LLMs). DirectLayout decomposes the
generation into three stages: producing a Bird's-Eye View (BEV) layout, lifting
it into 3D space, and refining object placements. To enable explicit spatial
reasoning and help the model grasp basic principles of object placement, we
employ Chain-of-Thought (CoT) Activation based on the 3D-Front dataset.
Additionally, we design CoT-Grounded Generative Layout Reward to enhance
generalization and spatial planning. During inference, DirectLayout addresses
asset-layout mismatches via Iterative Asset-Layout Alignment through in-context
learning. Extensive experiments demonstrate that DirectLayout achieves
impressive semantic consistency, generalization and physical plausibility.


### Seeing the Invisible: Machine learning-Based QPI Kernel Extraction via Latent Alignment
**Authors**: Yingshuai Ji, Haomin Zhuang, Matthew Toole, James McKenzie, Xiaolong Liu, Xiangliang Zhang

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05325v1](http://arxiv.org/pdf/2506.05325v1)

**Abstract**: Quasiparticle interference (QPI) imaging is a powerful tool for probing
electronic structures in quantum materials, but extracting the single-scatterer
QPI pattern (i.e., the kernel) from a multi-scatterer image remains a
fundamentally ill-posed inverse problem. In this work, we propose the first
AI-based framework for QPI kernel extraction. We introduce a two-step learning
strategy that decouples kernel representation learning from
observation-to-kernel inference. In the first step, we train a variational
autoencoder to learn a compact latent space of scattering kernels. In the
second step, we align the latent representation of QPI observations with those
of the pre-learned kernels using a dedicated encoder. This design enables the
model to infer kernels robustly even under complex, entangled scattering
conditions. We construct a diverse and physically realistic QPI dataset
comprising 100 unique kernels and evaluate our method against a direct one-step
baseline. Experimental results demonstrate that our approach achieves
significantly higher extraction accuracy, and improved generalization to unseen
kernels.


### On the Unruh effect and the thermofield double state
**Authors**: Gustavo Valdivia-Mera

**Published Date**: 2020-01-27

**Updated Date**: 2025-06-05

**PDF Url**: [2001.09869v6](http://arxiv.org/pdf/2001.09869v6)

**Abstract**: The purpose of this review is to provide a pedagogical development of the
Unruh effect and the thermofield double state. In Section 2, we construct
Rindler spacetime and analyze the perspective of an observer undergoing
constant acceleration in Minkowski spacetime, which motivates the establishment
of the relationship between the Fourier modes in both geometries using the
Bogoliubov-Valatin transformation. In Section 3, we explore the underlying
physics leading to the Unruh effect, its analogy with the thermal radiation
observed around a Schwarzschild black hole, and its manifestation through the
coupling of a particle detector to the scalar field. Finally, in Section 4, we
derive the thermofield double state by conducting a Euclidean analysis of the
field and geometry.


### Phase separation in a mixture of proliferating and motile active matter
**Authors**: Lukas Hupe, Joanna M. Materska, David Zwicker, Ramin Golestanian, Bartlomiej Waclaw, Philip Bittihn

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05288v1](http://arxiv.org/pdf/2506.05288v1)

**Abstract**: Proliferation and motility are ubiquitous drivers of activity in biological
systems. Here, we study a dense binary mixture of motile and proliferating
particles with exclusively repulsive interactions, where homeostasis in the
proliferating subpopulation is maintained by pressure-induced removal. Using
computer simulations, we show that phase separation emerges naturally in this
system at high density and weak enough self-propulsion. We show that
condensation is caused by interactions between motile particles induced by the
growing phase, and recapitulate this behavior in an effective model of only
motile particles with attractive interactions. Our results establish a new type
of phase transition and pave a way to reinterpret the physics of dense cellular
populations, such as bacterial colonies or tumors, as systems of mixed active
matter.


### Learning long range dependencies through time reversal symmetry breaking
**Authors**: Guillaume Pourcel, Maxence Ernoult

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05259v1](http://arxiv.org/pdf/2506.05259v1)

**Abstract**: Deep State Space Models (SSMs) reignite physics-grounded compute paradigms,
as RNNs could natively be embodied into dynamical systems. This calls for
dedicated learning algorithms obeying to core physical principles, with
efficient techniques to simulate these systems and guide their design. We
propose Recurrent Hamiltonian Echo Learning (RHEL), an algorithm which provably
computes loss gradients as finite differences of physical trajectories of
non-dissipative, Hamiltonian systems. In ML terms, RHEL only requires three
"forward passes" irrespective of model size, without explicit Jacobian
computation, nor incurring any variance in the gradient estimation. Motivated
by the physical realization of our algorithm, we first introduce RHEL in
continuous time and demonstrate its formal equivalence with the continuous
adjoint state method. To facilitate the simulation of Hamiltonian systems
trained by RHEL, we propose a discrete-time version of RHEL which is equivalent
to Backpropagation Through Time (BPTT) when applied to a class of recurrent
modules which we call Hamiltonian Recurrent Units (HRUs). This setting allows
us to demonstrate the scalability of RHEL by generalizing these results to
hierarchies of HRUs, which we call Hamiltonian SSMs (HSSMs). We apply RHEL to
train HSSMs with linear and nonlinear dynamics on a variety of time-series
tasks ranging from mid-range to long-range classification and regression with
sequence length reaching $\sim 50k$. We show that RHEL consistently matches the
performance of BPTT across all models and tasks. This work opens new doors for
the design of scalable, energy-efficient physical systems endowed with
self-learning capabilities for sequence modelling.


### Robust Moment Identification for Nonlinear PDEs via a Neural ODE Approach
**Authors**: Shaoxuan Chen, Su Yang, Panayotis G. Kevrekidis, Wei Zhu

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05245v1](http://arxiv.org/pdf/2506.05245v1)

**Abstract**: We propose a data-driven framework for learning reduced-order moment dynamics
from PDE-governed systems using Neural ODEs. In contrast to derivative-based
methods like SINDy, which necessitate densely sampled data and are sensitive to
noise, our approach based on Neural ODEs directly models moment trajectories,
enabling robust learning from sparse and potentially irregular time series.
Using as an application platform the nonlinear Schr\"{o}dinger equation, the
framework accurately recovers governing moment dynamics when closure is
available, even with limited and irregular observations. For systems without
analytical closure, we introduce a data-driven coordinate transformation
strategy based on Stiefel manifold optimization, enabling the discovery of
low-dimensional representations in which the moment dynamics become closed,
facilitating interpretable and reliable modeling. We also explore cases where a
closure model is not known, such as a Fisher-KPP reaction-diffusion system.
Here we demonstrate that Neural ODEs can still effectively approximate the
unclosed moment dynamics and achieve superior extrapolation accuracy compared
to physical-expert-derived ODE models. This advantage remains robust even under
sparse and irregular sampling, highlighting the method's robustness in
data-limited settings. Our results highlight the Neural ODE framework as a
powerful and flexible tool for learning interpretable, low-dimensional moment
dynamics in complex PDE-governed systems.


### How to Train Your Dragon: Quantum Neural Networks
**Authors**: Hao Zhang, Alex Kamenev

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05244v1](http://arxiv.org/pdf/2506.05244v1)

**Abstract**: Training of neural networks (NNs) has emerged as a major consumer of both
computational and energy resources. We demonstrate that quantum annealing
platforms, such as D-Wave, can enable fast and efficient training of classical
NNs, which are then deployable on conventional hardware. From a physics
perspective, NN training can be viewed as a dynamical phase transition: the
system evolves from an initial spin glass state to a highly ordered, trained
state. This process involves eliminating numerous undesired minima in its
energy landscape--akin to cutting off the ever-regenerating heads of a dragon.
The advantage of annealing devices is their ability to rapidly find multiple
deep states (dragon heads to be cut). We found that this quantum-assisted
training achieves superior performance scaling compared to classical
backpropagation methods, with a notably higher scaling exponent (1.01 vs.
0.78). It may be further increased up to a factor of 2 with a fully coherent
quantum platform using a variant of the Grover algorithm. Furthermore, we argue
that even a modestly sized annealer can be beneficial to train a deep NN by
being applied sequentially to a few layers at a time.


### Blink of an eye: a simple theory for feature localization in generative models
**Authors**: Marvin Li, Aayush Karan, Sitan Chen

**Published Date**: 2025-02-02

**Updated Date**: 2025-06-05

**PDF Url**: [2502.00921v2](http://arxiv.org/pdf/2502.00921v2)

**Abstract**: Large language models can exhibit unexpected behavior in the blink of an eye.
In a recent computer use demo, a language model switched from coding to
Googling pictures of Yellowstone, and these sudden shifts in behavior have also
been observed in reasoning patterns and jailbreaks. This phenomenon is not
unique to autoregressive models: in diffusion models, key features of the final
output are decided in narrow ``critical windows'' of the generation process. In
this work we develop a simple, unifying theory to explain this phenomenon using
the formalism of stochastic localization samplers. We show that it emerges
generically as the generation process localizes to a sub-population of the
distribution it models.
  While critical windows have been studied at length in diffusion models,
existing theory heavily relies on strong distributional assumptions and the
particulars of Gaussian diffusion. In contrast to existing work our theory (1)
applies to autoregressive and diffusion models; (2) makes no distributional
assumptions; (3) quantitatively improves previous bounds even when specialized
to diffusions; and (4) requires basic tools and no stochastic calculus or
statistical-physics-based machinery. We also identify an intriguing connection
to the all-or-nothing phenomenon from statistical inference. Finally, we
validate our predictions empirically for LLMs and find that critical windows
often coincide with failures in problem solving for various math and reasoning
benchmarks.


### Separation of variables for higher rank integrable models: review of recent progress
**Authors**: Fedor Levkovich-Maslyuk

**Published Date**: 2025-03-19

**Updated Date**: 2025-06-05

**PDF Url**: [2503.15398v2](http://arxiv.org/pdf/2503.15398v2)

**Abstract**: Separation of variables (SoV) is a powerful method expected to be applicable
for a wide range of quantum integrable systems, from models in condensed matter
physics to gauge and string theories. Yet its full implementation for many
higher rank examples, such as SU(N) spin chains with N>2, has remained elusive
for a long time. In this pedagogical review we discuss the major progress
achieved recently in understanding SoV for models of this type. In particular,
for rational SU(N) spin chains we describe different constructions of the SoV
basis, novel compact forms for spin chain eigenstates, the functional SoV
approach, and explicit computation of the SoV measure. We also discuss key
first applications of these results, namely the new compact determinant
representations for many observables such as scalar products and correlators.


### Black holes with electroweak hair -- the detailed derivation
**Authors**: Romain Gervalle, Mikhail S. Volkov

**Published Date**: 2025-04-12

**Updated Date**: 2025-06-05

**PDF Url**: [2504.09304v2](http://arxiv.org/pdf/2504.09304v2)

**Abstract**: We present a very detailed derivation of solutions describing hairy black
holes within the gravity-coupled Weinberg-Salam theory, which were previously
reported in
\href{https://doi.org/10.1103/PhysRevLett.133.171402}{Phys.Rev.Lett. 133 (2024)
171402}. These black holes support a strong magnetic field that polarizes the
electroweak vacuum and creates a condensate of massive fields carrying
superconducting currents along the black hole horizon. The currents, in turn,
generate a ``corona'' of magnetic vortex segments attached to the horizon at
both ends. The condensate and corona together constitute the black hole hair.
The extremal solutions approach, in the far field, the magnetic
Reissner-Nordstr\"om configuration, with a total mass that is {\it lower} than
the total charge, $M<|Q|$, due to the negative Zeeman energy of the condensate.
This makes the removal of the hair energetically unfavorable. The maximally
hairy black holes exhibit masses comparable to terrestrial values, with
approximately 11\% of their total mass stored in the hair. Given that these
solutions arise within a well-tested theoretical framework, they are likely to
have physical relevance.


## Diffusion
### Exploring Diffusion Transformer Designs via Grafting
**Authors**: Keshigeyan Chandrasegaran, Michael Poli, Daniel Y. Fu, Dongjun Kim, Lea M. Hadzic, Manling Li, Agrim Gupta, Stefano Massaroli, Azalia Mirhoseini, Juan Carlos Niebles, Stefano Ermon, Li Fei-Fei

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05340v1](http://arxiv.org/pdf/2506.05340v1)

**Abstract**: Designing model architectures requires decisions such as selecting operators
(e.g., attention, convolution) and configurations (e.g., depth, width).
However, evaluating the impact of these decisions on model quality requires
costly pretraining, limiting architectural investigation. Inspired by how new
software is built on existing code, we ask: can new architecture designs be
studied using pretrained models? To this end, we present grafting, a simple
approach for editing pretrained diffusion transformers (DiTs) to materialize
new architectures under small compute budgets. Informed by our analysis of
activation behavior and attention locality, we construct a testbed based on the
DiT-XL/2 design to study the impact of grafting on model quality. Using this
testbed, we develop a family of hybrid designs via grafting: replacing softmax
attention with gated convolution, local attention, and linear attention, and
replacing MLPs with variable expansion ratio and convolutional variants.
Notably, many hybrid designs achieve good quality (FID: 2.38-2.64 vs. 2.27 for
DiT-XL/2) using <2% pretraining compute. We then graft a text-to-image model
(PixArt-Sigma), achieving a 1.43x speedup with less than a 2% drop in GenEval
score. Finally, we present a case study that restructures DiT-XL/2 by
converting every pair of sequential transformer blocks into parallel blocks via
grafting. This reduces model depth by 2x and yields better quality (FID: 2.77)
than other models of comparable depth. Together, we show that new diffusion
model designs can be explored by grafting pretrained DiTs, with edits ranging
from operator replacement to architecture restructuring. Code and grafted
models: https://grafting.stanford.edu


### Learning normalized image densities via dual score matching
**Authors**: Florentin Guth, Zahra Kadkhodaie, Eero P Simoncelli

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05310v1](http://arxiv.org/pdf/2506.05310v1)

**Abstract**: Learning probability models from data is at the heart of many machine
learning endeavors, but is notoriously difficult due to the curse of
dimensionality. We introduce a new framework for learning \emph{normalized}
energy (log probability) models that is inspired from diffusion generative
models, which rely on networks optimized to estimate the score. We modify a
score network architecture to compute an energy while preserving its inductive
biases. The gradient of this energy network with respect to its input image is
the score of the learned density, which can be optimized using a denoising
objective. Importantly, the gradient with respect to the noise level provides
an additional score that can be optimized with a novel secondary objective,
ensuring consistent and normalized energies across noise levels. We train an
energy network with this \emph{dual} score matching objective on the ImageNet64
dataset, and obtain a cross-entropy (negative log likelihood) value comparable
to the state of the art. We further validate our approach by showing that our
energy model \emph{strongly generalizes}: estimated log probabilities are
nearly independent of the specific images in the training set. Finally, we
demonstrate that both image probability and dimensionality of local
neighborhoods vary significantly with image content, in contrast with
traditional assumptions such as concentration of measure or support on a
low-dimensional manifold.


### A Smooth Sea Never Made a Skilled $\texttt{SAILOR}$: Robust Imitation via Learning to Search
**Authors**: Arnav Kumar Jain, Vibhakar Mohta, Subin Kim, Atiksh Bhardwaj, Juntao Ren, Yunhai Feng, Sanjiban Choudhury, Gokul Swamy

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05294v1](http://arxiv.org/pdf/2506.05294v1)

**Abstract**: The fundamental limitation of the behavioral cloning (BC) approach to
imitation learning is that it only teaches an agent what the expert did at
states the expert visited. This means that when a BC agent makes a mistake
which takes them out of the support of the demonstrations, they often don't
know how to recover from it. In this sense, BC is akin to giving the agent the
fish -- giving them dense supervision across a narrow set of states -- rather
than teaching them to fish: to be able to reason independently about achieving
the expert's outcome even when faced with unseen situations at test-time. In
response, we explore learning to search (L2S) from expert demonstrations, i.e.
learning the components required to, at test time, plan to match expert
outcomes, even after making a mistake. These include (1) a world model and (2)
a reward model. We carefully ablate the set of algorithmic and design decisions
required to combine these and other components for stable and
sample/interaction-efficient learning of recovery behavior without additional
human corrections. Across a dozen visual manipulation tasks from three
benchmarks, our approach $\texttt{SAILOR}$ consistently out-performs
state-of-the-art Diffusion Policies trained via BC on the same data.
Furthermore, scaling up the amount of demonstrations used for BC by
5-10$\times$ still leaves a performance gap. We find that $\texttt{SAILOR}$ can
identify nuanced failures and is robust to reward hacking. Our code is
available at https://github.com/arnavkj1995/SAILOR .


### Stable Vision Concept Transformers for Medical Diagnosis
**Authors**: Lijie Hu, Songning Lai, Yuan Hua, Shu Yang, Jingfeng Zhang, Di Wang

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05286v1](http://arxiv.org/pdf/2506.05286v1)

**Abstract**: Transparency is a paramount concern in the medical field, prompting
researchers to delve into the realm of explainable AI (XAI). Among these XAI
methods, Concept Bottleneck Models (CBMs) aim to restrict the model's latent
space to human-understandable high-level concepts by generating a conceptual
layer for extracting conceptual features, which has drawn much attention
recently. However, existing methods rely solely on concept features to
determine the model's predictions, which overlook the intrinsic feature
embeddings within medical images. To address this utility gap between the
original models and concept-based models, we propose Vision Concept Transformer
(VCT). Furthermore, despite their benefits, CBMs have been found to negatively
impact model performance and fail to provide stable explanations when faced
with input perturbations, which limits their application in the medical field.
To address this faithfulness issue, this paper further proposes the Stable
Vision Concept Transformer (SVCT) based on VCT, which leverages the vision
transformer (ViT) as its backbone and incorporates a conceptual layer. SVCT
employs conceptual features to enhance decision-making capabilities by fusing
them with image features and ensures model faithfulness through the integration
of Denoised Diffusion Smoothing. Comprehensive experiments on four medical
datasets demonstrate that our VCT and SVCT maintain accuracy while remaining
interpretable compared to baselines. Furthermore, even when subjected to
perturbations, our SVCT model consistently provides faithful explanations, thus
meeting the needs of the medical field.


### How to Unlock Time Series Editing? Diffusion-Driven Approach with Multi-Grained Control
**Authors**: Hao Yu, Chu Xin Cheng, Runlong Yu, Yuyang Ye, Shiwei Tong, Zhaofeng Liu, Defu Lian

**Published Date**: 2025-06-05

**Updated Date**: 2025-06-05

**PDF Url**: [2506.05276v1](http://arxiv.org/pdf/2506.05276v1)

**Abstract**: Recent advances in time series generation have shown promise, yet controlling
properties in generated sequences remains challenging. Time Series Editing
(TSE) - making precise modifications while preserving temporal coherence -
consider both point-level constraints and segment-level controls that current
methods struggle to provide. We introduce the CocktailEdit framework to enable
simultaneous, flexible control across different types of constraints. This
framework combines two key mechanisms: a confidence-weighted anchor control for
point-wise constraints and a classifier-based control for managing statistical
properties such as sums and averages over segments. Our methods achieve precise
local control during the denoising inference stage while maintaining temporal
coherence and integrating seamlessly, with any conditionally trained
diffusion-based time series models. Extensive experiments across diverse
datasets and models demonstrate its effectiveness. Our work bridges the gap
between pure generative modeling and real-world time series editing needs,
offering a flexible solution for human-in-the-loop time series generation and
editing. The code and demo are provided for validation.


