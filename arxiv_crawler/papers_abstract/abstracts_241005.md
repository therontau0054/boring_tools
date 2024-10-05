# Abstracts of Papers

## Physics
### Transverse Energy-Energy Correlator for Vector Boson-Tagged Hadron Production in $pp$ and $pA$ collisions
**Authors**: Zhong-Bo Kang, Sookhyun Lee, Jani Penttala, Fanyi Zhao, Yiyu Zhou

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02747v1](http://arxiv.org/pdf/2410.02747v1)

**Abstract**: We investigate the transverse energy-energy correlator (TEEC) event-shape
observable for back-to-back $\gamma + h$ and $Z + h$ production in both $pp$
and $pA$ collisions. Our study incorporates nuclear modifications into the
transverse-momentum dependent (TMD) factorization framework, with resummation
up to next-to-leading logarithmic (NLL) accuracy, for TEEC as a function of the
variable $\tau = \left(1 + \cos{\phi} \right)/2$, where $\phi$ is the azimuthal
angle between the vector boson and the final hadron. We analyze the nuclear
modification factor $R_{pA}$ in $p\mathrm{Au}$ collisions at RHIC and
$p\mathrm{Pb}$ collisions at the LHC. Our results demonstrate that the TEEC
observable is a sensitive probe for nuclear modifications in TMD physics.
Specifically, the changes in the $\tau$-distribution shape provide insights
into transverse momentum broadening effects in large nuclei, while measurements
at different rapidities allow us to explore nuclear modifications in the
collinear component of the TMD parton distribution functions in nuclei.


### Grounding Large Language Models In Embodied Environment With Imperfect World Models
**Authors**: Haolan Liu, Jishen Zhao

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02742v1](http://arxiv.org/pdf/2410.02742v1)

**Abstract**: Despite a widespread success in various applications, large language models
(LLMs) often stumble when tackling basic physical reasoning or executing
robotics tasks, due to a lack of direct experience with the physical nuances of
the real world. To address these issues, we propose a Grounding Large language
model with Imperfect world MOdel (GLIMO), which utilizes proxy world models
such as simulators to collect and synthesize trining data. GLIMO incorporates
an LLM agent-based data generator to automatically create high-quality and
diverse instruction datasets. The generator includes an iterative self-refining
module for temporally consistent experience sampling, a diverse set of
question-answering instruction seeds, and a retrieval-augmented generation
module for reflecting on prior experiences. Comprehensive experiments show that
our approach improve the performance of strong open-source LLMs like LLaMA-3
with a performance boost of 2.04 $\times$, 1.54 $\times$, and 1.82 $\times$
across three different benchmarks, respectively. The performance is able to
compete with or surpass their larger counterparts such as GPT-4.


### Duality between string and computational order in symmetry-enriched topological phases
**Authors**: Paul Herringer, Vir B. Bulchandani, Younes Javanmard, David T. Stephen, Robert Raussendorf

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02716v1](http://arxiv.org/pdf/2410.02716v1)

**Abstract**: We present the first examples of topological phases of matter with uniform
power for measurement-based quantum computation. This is possible thanks to a
new framework for analyzing the computational properties of phases of matter
that is more general than previous constructions, which were limited to
short-range entangled phases in one dimension. We show that ground states of
the toric code in an anisotropic magnetic field yield a natural, albeit
non-computationally-universal, application of our framework. We then present a
new model with topological order whose ground states are universal resources
for MBQC. Both topological models are enriched by subsystem symmetries, and
these symmetries protect their computational power. Our framework greatly
expands the range of physical models that can be analyzed from the
computational perspective.


### VideoPhy: Evaluating Physical Commonsense for Video Generation
**Authors**: Hritik Bansal, Zongyu Lin, Tianyi Xie, Zeshun Zong, Michal Yarom, Yonatan Bitton, Chenfanfu Jiang, Yizhou Sun, Kai-Wei Chang, Aditya Grover

**Published Date**: 2024-06-05

**Updated Date**: 2024-10-03

**PDF Url**: [2406.03520v2](http://arxiv.org/pdf/2406.03520v2)

**Abstract**: Recent advances in internet-scale video data pretraining have led to the
development of text-to-video generative models that can create high-quality
videos across a broad range of visual concepts, synthesize realistic motions
and render complex objects. Hence, these generative models have the potential
to become general-purpose simulators of the physical world. However, it is
unclear how far we are from this goal with the existing text-to-video
generative models. To this end, we present VideoPhy, a benchmark designed to
assess whether the generated videos follow physical commonsense for real-world
activities (e.g. marbles will roll down when placed on a slanted surface).
Specifically, we curate diverse prompts that involve interactions between
various material types in the physical world (e.g., solid-solid, solid-fluid,
fluid-fluid). We then generate videos conditioned on these captions from
diverse state-of-the-art text-to-video generative models, including open models
(e.g., CogVideoX) and closed models (e.g., Lumiere, Dream Machine). Our human
evaluation reveals that the existing models severely lack the ability to
generate videos adhering to the given text prompts, while also lack physical
commonsense. Specifically, the best performing model, CogVideoX-5B, generates
videos that adhere to the caption and physical laws for 39.6% of the instances.
VideoPhy thus highlights that the video generative models are far from
accurately simulating the physical world. Finally, we propose an
auto-evaluator, VideoCon-Physics, to assess the performance reliably for the
newly released models.


### Lie Algebra Canonicalization: Equivariant Neural Operators under arbitrary Lie Groups
**Authors**: Zakhar Shumaylov, Peter Zaika, James Rowbottom, Ferdia Sherry, Melanie Weber, Carola-Bibiane Schönlieb

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02698v1](http://arxiv.org/pdf/2410.02698v1)

**Abstract**: The quest for robust and generalizable machine learning models has driven
recent interest in exploiting symmetries through equivariant neural networks.
In the context of PDE solvers, recent works have shown that Lie point
symmetries can be a useful inductive bias for Physics-Informed Neural Networks
(PINNs) through data and loss augmentation. Despite this, directly enforcing
equivariance within the model architecture for these problems remains elusive.
This is because many PDEs admit non-compact symmetry groups, oftentimes not
studied beyond their infinitesimal generators, making them incompatible with
most existing equivariant architectures. In this work, we propose Lie aLgebrA
Canonicalization (LieLAC), a novel approach that exploits only the action of
infinitesimal generators of the symmetry group, circumventing the need for
knowledge of the full group structure. To achieve this, we address existing
theoretical issues in the canonicalization literature, establishing connections
with frame averaging in the case of continuous non-compact groups. Operating
within the framework of canonicalization, LieLAC can easily be integrated with
unconstrained pre-trained models, transforming inputs to a canonical form
before feeding them into the existing model, effectively aligning the input for
model inference according to allowed symmetries. LieLAC utilizes standard Lie
group descent schemes, achieving equivariance in pre-trained models. Finally,
we showcase LieLAC's efficacy on tasks of invariant image classification and
Lie point symmetry equivariant neural PDE solvers using pre-trained models.


### Prospects of phase-adaptive cooling of levitated magnetic particles in a hollow-core photonic-crystal fibre
**Authors**: P. Kumar, F. G. Jimenez, S. Chakraborty, G. K. L. Wong, N. Y. Joly, C. Genes

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02697v1](http://arxiv.org/pdf/2410.02697v1)

**Abstract**: We analyze the feasibility of cooling of classical motion of a micro- to
nano-sized magnetic particle, levitated inside a hollow-core photonic crystal
fiber. The cooling action is implemented by means of controlling the phase of
one of the counter-propagating fiber guided waves. Direct imaging of the
particle's position, followed by the subsequent updating of the control laser's
phase leads to Stokes type of cooling force. We provide estimates of cooling
efficiency and final achievable temperature, taking into account thermal and
detection noise sources. Our results bring forward an important step towards
using trapped micro-magnets in sensing, testing the fundamental physics and
preparing the quantum states of magnetization.


### Supergeometric Quantum Effective Action
**Authors**: Viola Gattus, Apostolos Pilaftsis

**Published Date**: 2024-06-19

**Updated Date**: 2024-10-03

**PDF Url**: [2406.13594v2](http://arxiv.org/pdf/2406.13594v2)

**Abstract**: Supergeometric Quantum Field Theories (SG-QFTs) are theories that go beyond
the standard supersymmetric framework, since they allow for general
scalar-fermion field transformations on the configuration space of a
supermanifold, without requiring an equality between bosonic and fermionic
degrees of freedom. After revisiting previous considerations, we extend them by
calculating the one-loop effective action of minimal SG-QFTs that feature
non-zero fermionic curvature in two and four spacetime dimensions. By employing
an intuitive approach to the Schwinger-DeWitt heat-kernel technique and a novel
field-space generalised Clifford algebra, we derive the ultra-violet structure
of characteristic effective-field-theory (EFT) operators up to four spacetime
derivatives that emerge at the one-loop order and are of physical interest.
Upon minimising the impact of potential ambiguities due to the so-called
multiplicative anomalies, we find that the EFT interactions resulting from the
one-loop supergeometric effective action are manifestly diffeomorphically
invariant in configuration space. The extension of our approach to evaluating
higher-loops of the supergeometric quantum effective action is described. The
emerging landscape of theoretical and phenomenological directions for further
research of SG-QFTs is discussed.


### GUD: Generation with Unified Diffusion
**Authors**: Mathis Gerdes, Max Welling, Miranda C. N. Cheng

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02667v1](http://arxiv.org/pdf/2410.02667v1)

**Abstract**: Diffusion generative models transform noise into data by inverting a process
that progressively adds noise to data samples. Inspired by concepts from the
renormalization group in physics, which analyzes systems across different
scales, we revisit diffusion models by exploring three key design aspects: 1)
the choice of representation in which the diffusion process operates (e.g.
pixel-, PCA-, Fourier-, or wavelet-basis), 2) the prior distribution that data
is transformed into during diffusion (e.g. Gaussian with covariance $\Sigma$),
and 3) the scheduling of noise levels applied separately to different parts of
the data, captured by a component-wise noise schedule. Incorporating the
flexibility in these choices, we develop a unified framework for diffusion
generative models with greatly enhanced design freedom. In particular, we
introduce soft-conditioning models that smoothly interpolate between standard
diffusion models and autoregressive models (in any basis), conceptually
bridging these two approaches. Our framework opens up a wide design space which
may lead to more efficient training and data generation, and paves the way to
novel architectures integrating different generative approaches and generation
tasks.


### CAX: Cellular Automata Accelerated in JAX
**Authors**: Maxence Faldor, Antoine Cully

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02651v1](http://arxiv.org/pdf/2410.02651v1)

**Abstract**: Cellular automata have become a cornerstone for investigating emergence and
self-organization across diverse scientific disciplines, spanning neuroscience,
artificial life, and theoretical physics. However, the absence of a
hardware-accelerated cellular automata library limits the exploration of new
research directions, hinders collaboration, and impedes reproducibility. In
this work, we introduce CAX (Cellular Automata Accelerated in JAX), a
high-performance and flexible open-source library designed to accelerate
cellular automata research. CAX offers cutting-edge performance and a modular
design through a user-friendly interface, and can support both discrete and
continuous cellular automata with any number of dimensions. We demonstrate
CAX's performance and flexibility through a wide range of benchmarks and
applications. From classic models like elementary cellular automata and
Conway's Game of Life to advanced applications such as growing neural cellular
automata and self-classifying MNIST digits, CAX speeds up simulations up to
2,000 times faster. Furthermore, we demonstrate CAX's potential to accelerate
research by presenting a collection of three novel cellular automata
experiments, each implemented in just a few lines of code thanks to the
library's modular architecture. Notably, we show that a simple one-dimensional
cellular automaton can outperform GPT-4 on the 1D-ARC challenge.


### Quantum many-body solver using artificial neural networks and its applications to strongly correlated electron systems
**Authors**: Yusuke Nomura, Masatoshi Imada

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02633v1](http://arxiv.org/pdf/2410.02633v1)

**Abstract**: With the evolution of numerical methods, we are now aiming at not only
qualitative understanding but also quantitative prediction and design of
quantum many-body phenomena. As a novel numerical approach, machine learning
techniques have been introduced in 2017 to analyze quantum many-body problems.
Since then, proposed various novel approaches have opened a new era, in which
challenging and fundamental problems in physics can be solved by machine
learning methods. Especially, quantitative and accurate estimates of
material-dependent physical properties of strongly correlated matter have now
become realized by combining first-principles calculations with highly accurate
quantum many-body solvers developed with the help of machine learning methods.
Thus developed quantitative description of electron correlations will
constitute a key element of materials science in the next generation.


## Diffusion
### Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models
**Authors**: Zhengfeng Lai, Vasileios Saveris, Chen Chen, Hong-You Chen, Haotian Zhang, Bowen Zhang, Juan Lao Tebar, Wenze Hu, Zhe Gan, Peter Grasch, Meng Cao, Yinfei Yang

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02740v1](http://arxiv.org/pdf/2410.02740v1)

**Abstract**: Recent advancements in multimodal models highlight the value of rewritten
captions for improving performance, yet key challenges remain. For example,
while synthetic captions often provide superior quality and image-text
alignment, it is not clear whether they can fully replace AltTexts: the role of
synthetic captions and their interaction with original web-crawled AltTexts in
pre-training is still not well understood. Moreover, different multimodal
foundation models may have unique preferences for specific caption formats, but
efforts to identify the optimal captions for each model remain limited. In this
work, we propose a novel, controllable, and scalable captioning pipeline
designed to generate diverse caption formats tailored to various multimodal
models. By examining Short Synthetic Captions (SSC) towards Dense Synthetic
Captions (DSC+) as case studies, we systematically explore their effects and
interactions with AltTexts across models such as CLIP, multimodal LLMs, and
diffusion models. Our findings reveal that a hybrid approach that keeps both
synthetic captions and AltTexts can outperform the use of synthetic captions
alone, improving both alignment and performance, with each model demonstrating
preferences for particular caption formats. This comprehensive analysis
provides valuable insights into optimizing captioning strategies, thereby
advancing the pre-training of multimodal foundation models.


### NETS: A Non-Equilibrium Transport Sampler
**Authors**: Michael S. Albergo, Eric Vanden-Eijnden

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02711v1](http://arxiv.org/pdf/2410.02711v1)

**Abstract**: We propose an algorithm, termed the Non-Equilibrium Transport Sampler (NETS),
to sample from unnormalized probability distributions. NETS can be viewed as a
variant of annealed importance sampling (AIS) based on Jarzynski's equality, in
which the stochastic differential equation used to perform the non-equilibrium
sampling is augmented with an additional learned drift term that lowers the
impact of the unbiasing weights used in AIS. We show that this drift is the
minimizer of a variety of objective functions, which can all be estimated in an
unbiased fashion without backpropagating through solutions of the stochastic
differential equations governing the sampling. We also prove that some these
objectives control the Kullback-Leibler divergence of the estimated
distribution from its target. NETS is shown to be unbiased and, in addition,
has a tunable diffusion coefficient which can be adjusted post-training to
maximize the effective sample size. We demonstrate the efficacy of the method
on standard benchmarks, high-dimensional Gaussian mixture distributions, and a
model from statistical lattice field theory, for which it surpasses the
performances of related work and existing baselines.


### SteerDiff: Steering towards Safe Text-to-Image Diffusion Models
**Authors**: Hongxiang Zhang, Yifeng He, Hao Chen

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02710v1](http://arxiv.org/pdf/2410.02710v1)

**Abstract**: Text-to-image (T2I) diffusion models have drawn attention for their ability
to generate high-quality images with precise text alignment. However, these
models can also be misused to produce inappropriate content. Existing safety
measures, which typically rely on text classifiers or ControlNet-like
approaches, are often insufficient. Traditional text classifiers rely on
large-scale labeled datasets and can be easily bypassed by rephrasing. As
diffusion models continue to scale, fine-tuning these safeguards becomes
increasingly challenging and lacks flexibility. Recent red-teaming attack
researches further underscore the need for a new paradigm to prevent the
generation of inappropriate content. In this paper, we introduce SteerDiff, a
lightweight adaptor module designed to act as an intermediary between user
input and the diffusion model, ensuring that generated images adhere to ethical
and safety standards with little to no impact on usability. SteerDiff
identifies and manipulates inappropriate concepts within the text embedding
space to guide the model away from harmful outputs. We conduct extensive
experiments across various concept unlearning tasks to evaluate the
effectiveness of our approach. Furthermore, we benchmark SteerDiff against
multiple red-teaming strategies to assess its robustness. Finally, we explore
the potential of SteerDiff for concept forgetting tasks, demonstrating its
versatility in text-conditioned image generation.


### Undesirable Memorization in Large Language Models: A Survey
**Authors**: Ali Satvaty, Suzan Verberne, Fatih Turkmen

**Published Date**: 2024-10-03

**Updated Date**: 2024-10-03

**PDF Url**: [2410.02650v1](http://arxiv.org/pdf/2410.02650v1)

**Abstract**: While recent research increasingly showcases the remarkable capabilities of
Large Language Models (LLMs), it's vital to confront their hidden pitfalls.
Among these challenges, the issue of memorization stands out, posing
significant ethical and legal risks. In this paper, we presents a
Systematization of Knowledge (SoK) on the topic of memorization in LLMs.
Memorization is the effect that a model tends to store and reproduce phrases or
passages from the training data and has been shown to be the fundamental issue
to various privacy and security attacks against LLMs.
  We begin by providing an overview of the literature on the memorization,
exploring it across five key dimensions: intentionality, degree,
retrievability, abstraction, and transparency. Next, we discuss the metrics and
methods used to measure memorization, followed by an analysis of the factors
that contribute to memorization phenomenon. We then examine how memorization
manifests itself in specific model architectures and explore strategies for
mitigating these effects. We conclude our overview by identifying potential
research topics for the near future: to develop methods for balancing
performance and privacy in LLMs, and the analysis of memorization in specific
contexts, including conversational agents, retrieval-augmented generation,
multilingual language models, and diffusion language models.


### NECOMIMI: Neural-Cognitive Multimodal EEG-informed Image Generation with Diffusion Models
**Authors**: Chi-Sheng Chen

**Published Date**: 2024-10-01

**Updated Date**: 2024-10-03

**PDF Url**: [2410.00712v2](http://arxiv.org/pdf/2410.00712v2)

**Abstract**: NECOMIMI (NEural-COgnitive MultImodal EEG-Informed Image Generation with
Diffusion Models) introduces a novel framework for generating images directly
from EEG signals using advanced diffusion models. Unlike previous works that
focused solely on EEG-image classification through contrastive learning,
NECOMIMI extends this task to image generation. The proposed NERV EEG encoder
demonstrates state-of-the-art (SoTA) performance across multiple zero-shot
classification tasks, including 2-way, 4-way, and 200-way, and achieves top
results in our newly proposed Category-based Assessment Table (CAT) Score,
which evaluates the quality of EEG-generated images based on semantic concepts.
A key discovery of this work is that the model tends to generate abstract or
generalized images, such as landscapes, rather than specific objects,
highlighting the inherent challenges of translating noisy and low-resolution
EEG data into detailed visual outputs. Additionally, we introduce the CAT Score
as a new metric tailored for EEG-to-image evaluation and establish a benchmark
on the ThingsEEG dataset. This study underscores the potential of EEG-to-image
generation while revealing the complexities and challenges that remain in
bridging neural activity with visual representation.


