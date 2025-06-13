# Abstracts of Papers

## Physics
### Principled Approaches for Extending Neural Architectures to Function Spaces for Operator Learning
**Authors**: Julius Berner, Miguel Liu-Schiaffini, Jean Kossaifi, Valentin Duruisseaux, Boris Bonev, Kamyar Azizzadenesheli, Anima Anandkumar

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10973v1](http://arxiv.org/pdf/2506.10973v1)

**Abstract**: A wide range of scientific problems, such as those described by
continuous-time dynamical systems and partial differential equations (PDEs),
are naturally formulated on function spaces. While function spaces are
typically infinite-dimensional, deep learning has predominantly advanced
through applications in computer vision and natural language processing that
focus on mappings between finite-dimensional spaces. Such fundamental
disparities in the nature of the data have limited neural networks from
achieving a comparable level of success in scientific applications as seen in
other fields. Neural operators are a principled way to generalize neural
networks to mappings between function spaces, offering a pathway to replicate
deep learning's transformative impact on scientific problems. For instance,
neural operators can learn solution operators for entire classes of PDEs, e.g.,
physical systems with different boundary conditions, coefficient functions, and
geometries. A key factor in deep learning's success has been the careful
engineering of neural architectures through extensive empirical testing.
Translating these neural architectures into neural operators allows operator
learning to enjoy these same empirical optimizations. However, prior neural
operator architectures have often been introduced as standalone models, not
directly derived as extensions of existing neural network architectures. In
this paper, we identify and distill the key principles for constructing
practical implementations of mappings between infinite-dimensional function
spaces. Using these principles, we propose a recipe for converting several
popular neural architectures into neural operators with minimal modifications.
This paper aims to guide practitioners through this process and details the
steps to make neural operators work in practice. Our code can be found at
https://github.com/neuraloperator/NNs-to-NOs


### Large-scale quantization of trace I: Finite propagation operators
**Authors**: Matthias Ludewig, Guo Chuan Thiang

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10957v1](http://arxiv.org/pdf/2506.10957v1)

**Abstract**: Inspired by parallel developments in coarse geometry in mathematics and exact
macroscopic quantization in physics, we present a family of general trace
formulae which are universally quantized and depend only on large-scale
geometric features of the input data. They generalize, to arbitrary dimensions,
formulae found by Roe in his partitioned manifold index theorem, as well as the
Kubo and Kitaev formulae for 2D Hall conductance used in physics.


### Distillation of atomistic foundation models across architectures and chemical domains
**Authors**: John L. A. Gardner, Daniel F. Thomas du Toit, Chiheb Ben Mahmoud, Zoé Faure Beaulieu, Veronika Juraskova, Laura-Bianca Paşca, Louise A. M. Rosset, Fernanda Duarte, Fausto Martelli, Chris J. Pickard, Volker L. Deringer

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10956v1](http://arxiv.org/pdf/2506.10956v1)

**Abstract**: Machine-learned interatomic potentials have transformed computational
research in the physical sciences. Recent atomistic `foundation' models have
changed the field yet again: trained on many different chemical elements and
domains, these potentials are widely applicable, but comparably slow and
resource-intensive to run. Here we show how distillation via synthetic data can
be used to cheaply transfer knowledge from atomistic foundation models to a
range of different architectures, unlocking much smaller, more efficient
potentials. We demonstrate speed-ups of $> 10\times$ by distilling from one
graph-network architecture into another, and $> 100\times$ by leveraging the
atomic cluster expansion framework. We showcase applicability across chemical
and materials domains: from liquid water to hydrogen under extreme conditions;
from porous silica and a hybrid halide perovskite solar-cell material to
modelling organic reactions. Our work shows how distillation can support the
routine and computationally efficient use of current and future atomistic
foundation models in real-world scientific research.


### Orientation Reversal and the Chern-Simons Natural Boundary
**Authors**: Griffen Adams, Ovidiu Costin, Gerald V. Dunne, Sergei Gukov, Oğuz Öner

**Published Date**: 2025-05-20

**Updated Date**: 2025-06-12

**PDF Url**: [2505.14441v2](http://arxiv.org/pdf/2505.14441v2)

**Abstract**: We show that the fundamental property of preservation of relations,
underlying resurgent analysis, provides a new perspective on crossing a natural
boundary, an important general problem in theoretical and mathematical physics.
This reveals a deeper rigidity of resurgence in a quantum field theory. We
study the non-perturbative completion of complex Chern-Simons theory that
associates to a 3-manifold a collection of $q$-series invariants labeled by
Spin$^c$ structures, for which crossing the natural boundary corresponds to
orientation reversal of the 3-manifold. Our new resurgent perspective leads to
a practical numerical algorithm that generates $q$-series which are dual to
unary $q$-series composed of false theta functions. Until recently, these duals
were only known in a limited number of cases, essentially based on Ramanujan's
mock theta functions, and the common belief was that the more general duals
might not even exist. Resurgence analysis identifies as primary objects Mordell
integrals: transforms of resurgent functions. Their unique Borel summed
transseries decomposition on either side of the Stokes line is the unique
decomposition into real and imaginary parts. The latter are combinations of
unary $q$-series in terms of $q$ and its modular counterpart $\tilde{q}$, and
are resurgent by construction. The Mordell integral is analytic across the
natural boundary of the $q$ and $\tilde{q}$ series, and uniqueness of a similar
decomposition which preserves algebraic relations on the other side of the
boundary defines the unique boundary crossing of the $q$ series. This
continuation can be efficiently implemented numerically. This identifies known
unique mock modular identities, and extends well beyond. The resurgent approach
reveals new aspects, and is very different from other approaches based on
indefinite theta series, Appell-Lerch sums, and logarithmic vertex operator
algebras.


### Physics-informed Machine Learning Analysis for Nanoscale Grain Mapping by Synchrotron Laue Microdiffraction
**Authors**: Ka Hung Chan, Xinyue Huang, Nobumichi Tamura, Xian Chen

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10937v1](http://arxiv.org/pdf/2506.10937v1)

**Abstract**: Understanding the grain morphology, orientation distribution, and crystal
structure of nanocrystals is essential for optimizing the mechanical and
physical properties of functional materials. Synchrotron X-ray Laue
microdiffraction is a powerful technique for characterizing crystal structures
and orientation mapping using focused X-rays. However, when grain sizes are
smaller than the beam size, mixed peaks in the Laue pattern from neighboring
grains limit the resolution of grain morphology mapping. We propose a
physics-informed machine learning (PIML) approach that combines a CNN feature
extractor with a physics-informed filtering algorithm to overcome the spatial
resolution limits of X-rays, achieving nanoscale resolution for grain mapping.
Our PIML method successfully resolves the grain size, orientation distribution,
and morphology of Au nanocrystals through synchrotron microdiffraction scans,
showing good agreement with electron backscatter diffraction results. This
PIML-assisted synchrotron microdiffraction analysis can be generalized to other
diffraction-based probes, enabling the characterization of nanosized structures
with micron-sized probes.


### Investigating the Relationship Between Physical Activity and Tailored Behavior Change Messaging: Connecting Contextual Bandit with Large Language Models
**Authors**: Haochen Song, Dominik Hofer, Rania Islambouli, Laura Hawkins, Ananya Bhattacharjee, Meredith Franklin, Joseph Jay Williams

**Published Date**: 2025-06-08

**Updated Date**: 2025-06-12

**PDF Url**: [2506.07275v2](http://arxiv.org/pdf/2506.07275v2)

**Abstract**: Machine learning approaches, such as contextual multi-armed bandit (cMAB)
algorithms, offer a promising strategy to reduce sedentary behavior by
delivering personalized interventions to encourage physical activity. However,
cMAB algorithms typically require large participant samples to learn
effectively and may overlook key psychological factors that are not explicitly
encoded in the model. In this study, we propose a hybrid approach that combines
cMAB for selecting intervention types with large language models (LLMs) to
personalize message content. We evaluate four intervention types: behavioral
self-monitoring, gain-framed, loss-framed, and social comparison, each
delivered as a motivational message aimed at increasing motivation for physical
activity and daily step count. Message content is further personalized using
dynamic contextual factors including daily fluctuations in self-efficacy,
social influence, and regulatory focus. Over a seven-day trial, participants
receive daily messages assigned by one of four models: cMAB alone, LLM alone,
combined cMAB with LLM personalization (cMABxLLM), or equal randomization
(RCT). Outcomes include daily step count and message acceptance, assessed via
ecological momentary assessments (EMAs). We apply a causal inference framework
to evaluate the effects of each model. Our findings offer new insights into the
complementary roles of LLM-based personalization and cMAB adaptation in
promoting physical activity through personalized behavioral messaging.


### Data-Driven Prediction of Dynamic Interactions Between Robot Appendage and Granular Material
**Authors**: Guanjin Wang, Xiangxue Zhao, Shapour Azarm, Balakumar Balachandran

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10875v1](http://arxiv.org/pdf/2506.10875v1)

**Abstract**: An alternative data-driven modeling approach has been proposed and employed
to gain fundamental insights into robot motion interaction with granular
terrain at certain length scales. The approach is based on an integration of
dimension reduction (Sequentially Truncated Higher-Order Singular Value
Decomposition), surrogate modeling (Gaussian Process), and data assimilation
techniques (Reduced Order Particle Filter). This approach can be used online
and is based on offline data, obtained from the offline collection of
high-fidelity simulation data and a set of sparse experimental data. The
results have shown that orders of magnitude reduction in computational time can
be obtained from the proposed data-driven modeling approach compared with
physics-based high-fidelity simulations. With only simulation data as input,
the data-driven prediction technique can generate predictions that have
comparable accuracy as simulations. With both simulation data and sparse
physical experimental measurement as input, the data-driven approach with its
embedded data assimilation techniques has the potential in outperforming only
high-fidelity simulations for the long-horizon predictions. In addition, it is
demonstrated that the data-driven modeling approach can also reproduce the
scaling relationship recovered by physics-based simulations for maximum
resistive forces, which may indicate its general predictability beyond a
case-by-case basis. The results are expected to help robot navigation and
exploration in unknown and complex terrains during both online and offline
phases.


### Supernovae Time Profiles as a Probe of New Physics at Neutrino Telescopes
**Authors**: Jeff Lazar, Ying-Ying Li, Carlos A. Arguelles, Vedran Brdar

**Published Date**: 2024-03-14

**Updated Date**: 2025-06-12

**PDF Url**: [2403.09781v2](http://arxiv.org/pdf/2403.09781v2)

**Abstract**: Neutrino telescopes, including IceCube, can detect galactic supernova events
by observing the collective rise in photomultiplier count rates with a
sub-second time resolution. Leveraging precise timing, we demonstrate the
ability of neutrino telescopes to explore new weakly coupled states emitted
from supernovae and subsequently decaying to neutrinos. Our approach utilizes
publicly available packages, \texttt{ASTERIA} and \texttt{SNEWPY}, for
simulating detector responses and parametrizing neutrino fluxes originating
from Standard Model and new physics. We present results for two beyond the
Standard Model scenarios and introduce the tool developed for testing a diverse
range of new physics models.


### OmniFluids: Unified Physics Pre-trained Modeling of Fluid Dynamics
**Authors**: Rui Zhang, Qi Meng, Han Wan, Yang Liu, Zhi-Ming Ma, Hao Sun

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10862v1](http://arxiv.org/pdf/2506.10862v1)

**Abstract**: High-fidelity and efficient simulation of fluid dynamics drive progress in
various scientific and engineering applications. Traditional computational
fluid dynamics methods offer strong interpretability and guaranteed
convergence, but rely on fine spatial and temporal meshes, incurring
prohibitive computational costs. Physics-informed neural networks (PINNs) and
neural operators aim to accelerate PDE solvers using deep learning techniques.
However, PINNs require extensive retraining and careful tuning, and purely
data-driven operators demand large labeled datasets. Hybrid physics-aware
methods embed numerical discretizations into network architectures or loss
functions, but achieve marginal speed gains and become unstable when balancing
coarse priors against high-fidelity measurements. To this end, we introduce
OmniFluids, a unified physics pre-trained operator learning framework that
integrates physics-only pre-training, coarse-grid operator distillation, and
few-shot fine-tuning, which enables fast inference and accurate prediction
under limited or zero data supervision. For architectural design, the key
components of OmniFluids include a mixture of operators, a multi-frame decoder,
and factorized Fourier layers, which enable efficient and scalable modeling of
diverse physical tasks while maintaining seamless integration with
physics-based supervision. Across a broad range of two- and three-dimensional
benchmarks, OmniFluids significantly outperforms state-of-the-art AI-driven
methods in flow field reconstruction and turbulence statistics accuracy,
delivering 10-100x speedups compared to classical solvers, and accurately
recovers unknown physical parameters from sparse, noisy data. This work
establishes a new paradigm for efficient and generalizable surrogate modeling
in complex fluid systems under limited data availability.


### Photonic chiral bulk transports manipulated by boundary freedom in three-dimensional meta-crystals
**Authors**: Yingxin Qi, Hanyu Wang, Qinghua Guo, Zhihong Zhu, Biao Yang

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10861v1](http://arxiv.org/pdf/2506.10861v1)

**Abstract**: In topological physics, one of the most intriguing phenomena is the presence
of topological boundary states, accurately predicted by the well-established
bulk-edge correspondence. For example, in three-dimensional Weyl semimetals,
Fermi arcs emerge to connect projected Weyl points on the surface due to
inheriting the bulk-edge correspondence from the integer quantum Hall effect.
However, limited attention has been paid to exploring the reverse mechanism in
topological crystals. In this study, we propose that boundaries can serve as an
alternative degree of freedom to manipulate topological bulk transports. We
analytically and experimentally validate our concept using a finite-thickness
photonic meta-crystal that supports bulk nodal lines, with its zeroth modes
exhibiting opposite chiral bulk transports under different boundary conditions.
Notably, the mirror symmetry remains preserved across both configurations.
These findings are applicable to other topological systems, providing new
insights into systems with varied boundary conditions and offering the
potential for the design of more compact and spatially efficient topological
photonic devices.


## Diffusion
### Rethinking Losses for Diffusion Bridge Samplers
**Authors**: Sebastian Sanokowski, Lukas Gruber, Christoph Bartmann, Sepp Hochreiter, Sebastian Lehner

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10982v1](http://arxiv.org/pdf/2506.10982v1)

**Abstract**: Diffusion bridges are a promising class of deep-learning methods for sampling
from unnormalized distributions. Recent works show that the Log Variance (LV)
loss consistently outperforms the reverse Kullback-Leibler (rKL) loss when
using the reparametrization trick to compute rKL-gradients. While the on-policy
LV loss yields identical gradients to the rKL loss when combined with the
log-derivative trick for diffusion samplers with non-learnable forward
processes, this equivalence does not hold for diffusion bridges or when
diffusion coefficients are learned. Based on this insight we argue that for
diffusion bridges the LV loss does not represent an optimization objective that
can be motivated like the rKL loss via the data processing inequality. Our
analysis shows that employing the rKL loss with the log-derivative trick
(rKL-LD) does not only avoid these conceptual problems but also consistently
outperforms the LV loss. Experimental results with different types of diffusion
bridges on challenging benchmarks show that samplers trained with the rKL-LD
loss achieve better performance. From a practical perspective we find that
rKL-LD requires significantly less hyperparameter optimization and yields more
stable training behavior.


### Fine-Grained Perturbation Guidance via Attention Head Selection
**Authors**: Donghoon Ahn, Jiwon Kang, Sanghyun Lee, Minjae Kim, Jaewon Min, Wooseok Jang, Saungwu Lee, Sayak Paul, Susung Hong, Seungryong Kim

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10978v1](http://arxiv.org/pdf/2506.10978v1)

**Abstract**: Recent guidance methods in diffusion models steer reverse sampling by
perturbing the model to construct an implicit weak model and guide generation
away from it. Among these approaches, attention perturbation has demonstrated
strong empirical performance in unconditional scenarios where classifier-free
guidance is not applicable. However, existing attention perturbation methods
lack principled approaches for determining where perturbations should be
applied, particularly in Diffusion Transformer (DiT) architectures where
quality-relevant computations are distributed across layers. In this paper, we
investigate the granularity of attention perturbations, ranging from the layer
level down to individual attention heads, and discover that specific heads
govern distinct visual concepts such as structure, style, and texture quality.
Building on this insight, we propose "HeadHunter", a systematic framework for
iteratively selecting attention heads that align with user-centric objectives,
enabling fine-grained control over generation quality and visual attributes. In
addition, we introduce SoftPAG, which linearly interpolates each selected
head's attention map toward an identity matrix, providing a continuous knob to
tune perturbation strength and suppress artifacts. Our approach not only
mitigates the oversmoothing issues of existing layer-level perturbation but
also enables targeted manipulation of specific visual styles through
compositional head selection. We validate our method on modern large-scale
DiT-based text-to-image models including Stable Diffusion 3 and FLUX.1,
demonstrating superior performance in both general quality enhancement and
style-specific guidance. Our work provides the first head-level analysis of
attention perturbation in diffusion models, uncovering interpretable
specialization within attention layers and enabling practical design of
effective perturbation strategies.


### What Exactly Does Guidance Do in Masked Discrete Diffusion Models
**Authors**: He Ye, Rojas Kevin, Tao Molei

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10971v1](http://arxiv.org/pdf/2506.10971v1)

**Abstract**: We study masked discrete diffusion models with classifier-free guidance
(CFG). Assuming no score error nor discretization error, we derive an explicit
solution to the guided reverse dynamics, so that how guidance influences the
sampling behavior can be precisely characterized. When the full data
distribution is a mixture over classes and the goal is to sample from a
specific class, guidance amplifies class-specific regions while suppresses
regions shared with other classes. This effect depends on the guidance strength
$w$ and induces distinct covariance structures in the sampled distribution.
Notably, we observe quantitatively different behaviors in $1$D and $2$D. We
also show that for large $w$, the decay rate of the total variation
($\mathrm{TV}$) along the reverse dynamics is double-exponential in $w$ for
both $1$D and $2$D. These findings highlight the role of guidance, not just in
shaping the output distribution, but also in controlling the dynamics of the
sampling trajectory. Our theoretical analysis is supported by experiments that
illustrate the geometric effects of guidance and its impact on convergence.


### SpectralAR: Spectral Autoregressive Visual Generation
**Authors**: Yuanhui Huang, Weiliang Chen, Wenzhao Zheng, Yueqi Duan, Jie Zhou, Jiwen Lu

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10962v1](http://arxiv.org/pdf/2506.10962v1)

**Abstract**: Autoregressive visual generation has garnered increasing attention due to its
scalability and compatibility with other modalities compared with diffusion
models. Most existing methods construct visual sequences as spatial patches for
autoregressive generation. However, image patches are inherently parallel,
contradicting the causal nature of autoregressive modeling. To address this, we
propose a Spectral AutoRegressive (SpectralAR) visual generation framework,
which realizes causality for visual sequences from the spectral perspective.
Specifically, we first transform an image into ordered spectral tokens with
Nested Spectral Tokenization, representing lower to higher frequency
components. We then perform autoregressive generation in a coarse-to-fine
manner with the sequences of spectral tokens. By considering different levels
of detail in images, our SpectralAR achieves both sequence causality and token
efficiency without bells and whistles. We conduct extensive experiments on
ImageNet-1K for image reconstruction and autoregressive generation, and
SpectralAR achieves 3.02 gFID with only 64 tokens and 310M parameters. Project
page: https://huang-yh.github.io/spectralar/.


### ReGuidance: A Simple Diffusion Wrapper for Boosting Sample Quality on Hard Inverse Problems
**Authors**: Aayush Karan, Kulin Shah, Sitan Chen

**Published Date**: 2025-06-12

**Updated Date**: 2025-06-12

**PDF Url**: [2506.10955v1](http://arxiv.org/pdf/2506.10955v1)

**Abstract**: There has been a flurry of activity around using pretrained diffusion models
as informed data priors for solving inverse problems, and more generally around
steering these models using reward models. Training-free methods like diffusion
posterior sampling (DPS) and its many variants have offered flexible heuristic
algorithms for these tasks, but when the reward is not informative enough,
e.g., in hard inverse problems with low signal-to-noise ratio, these techniques
veer off the data manifold, failing to produce realistic outputs. In this work,
we devise a simple wrapper, ReGuidance, for boosting both the sample realism
and reward achieved by these methods. Given a candidate solution $\hat{x}$
produced by an algorithm of the user's choice, we propose inverting the
solution by running the unconditional probability flow ODE in reverse starting
from $\hat{x}$, and then using the resulting latent as an initialization for
DPS. We evaluate our wrapper on hard inverse problems like large box
in-painting and super-resolution with high upscaling. Whereas state-of-the-art
baselines visibly fail, we find that applying our wrapper on top of these
baselines significantly boosts sample quality and measurement consistency. We
complement these findings with theory proving that on certain multimodal data
distributions, ReGuidance simultaneously boosts the reward and brings the
candidate solution closer to the data manifold. To our knowledge, this
constitutes the first rigorous algorithmic guarantee for DPS.


