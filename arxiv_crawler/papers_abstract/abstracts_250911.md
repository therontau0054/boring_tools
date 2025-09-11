# Abstracts of Papers

## Physics
### Thermoelectric processes of quantum normal-superconductor interfaces
**Authors**: L. Arrachea, A. Braggio, P. Burset, E. J. H. Lee, A. Levy Yeyati, R. Sánchez

**Published Date**: 2025-05-12

**Updated Date**: 2025-09-10

**PDF Url**: [2505.07426v2](http://arxiv.org/pdf/2505.07426v2)

**Abstract**: Superconducting interfaces have recently been demonstrated to contain a rich
variety of effects that give rise to sizable thermoelectric responses and
unexpected thermal properties, despite traditionally being considered poor
thermoelectrics due to their intrinsic electron-hole symmetry. We review
different mechanisms driving this response in hybrid normal-superconducting
junctions, depending on the dimensionality of the mesoscopic interface. In
addition to discussing heat to power conversion, cooling and heat transport,
special emphasis is put on physical properties of hybrid devices that can be
revealed by the thermoelectric effect.


### A Pathway to Practical Quantum Advantage in Solving Navier-Stokes Equations
**Authors**: Xi-Ning Zhuang, Zhao-Yun Chen, Ming-Yang Tan, Jiaxuan Zhang, Chuang-Chao Ye, Tian-Hao Wei, Teng-Yang Ma, Cheng Xue, Huan-Yu Liu, Qing-Song Li, Tai-Ping Sun, Xiao-Fan Xu, Yun-Jie Wang, Yu-Chun Wu, Guo-Ping Guo

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08807v1](http://arxiv.org/pdf/2509.08807v1)

**Abstract**: The advent of fault-tolerant quantum computing (FTQC) promises to tackle
classically intractable problems. A key milestone is solving the Navier-Stokes
equations (NSE), which has remained formidable for quantum algorithms due to
their high input-output overhead and nonlinearity. Here, we establish a
full-stack framework that charts a practical pathway to a quantum advantage for
large-scale NSE simulation. Our approach integrates a spectral-based
input/output algorithm, an explicit and synthesized quantum circuit, and a
refined error-correction protocol. The algorithm achieves an end-to-end
exponential speedup in asymptotic complexity, meeting the lower bound for
general quantum linear system solvers. Through symmetry-based circuit synthesis
and optimized error correction, we reduce the required logical and physical
resources by two orders of magnitude. Our concrete resource analysis
demonstrates that solving NSE on a $2^{80}$-grid is feasible with 8.71 million
physical qubits (at an error rate of $5 \times 10^{-4}$) in 42.6 days --
outperforming a state-of-the-art supercomputer, which would require over a
century. This work bridges the gap between theoretical quantum speedup and the
practical deployment of high-performance scientific computing.


### Using machine learning to downscale coarse-resolution environmental variables for understanding the spatial frequency of convective storms
**Authors**: Hungjui Yu, Lander Ver Hoef, Kristen L. Rasmussen, Imme Ebert-Uphoff

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08802v1](http://arxiv.org/pdf/2509.08802v1)

**Abstract**: Global climate models (GCMs), typically run at ~100-km resolution, capture
large-scale environmental conditions but cannot resolve convection and cloud
processes at kilometer scales. Convection-permitting models offer
higher-resolution simulations that explicitly simulate convection but are
computationally expensive and impractical for large ensemble runs. This study
explores machine learning (ML) as a bridge between these approaches. We train
simple, pixel-based neural networks to predict convective storm frequency from
environmental variables produced by a regional convection-permitting model. The
ML models achieve promising results, with structural similarity index measure
(SSIM) values exceeding 0.8, capturing the diurnal cycle and orographic
convection without explicit temporal or spatial coordinates as input. Model
performance declines when fewer input features are used or specific regions are
excluded, underscoring the role of diverse physical mechanisms in convective
activity. These findings highlight ML potential as a computationally efficient
tool for representing convection and as a means of scientific discovery,
offering insights into convective processes. Unlike convolutional neural
networks, which depend on spatial structure and grid size, the pixel-based
model treats each grid point independently, enabling value-to-value prediction
without spatial context. This design enhances adaptability to resolution
changes and supports generalization to unseen environmental regimes, making it
particularly suited for linking environmental conditions to convective features
and for application across diverse model grids or climate scenarios.


### Whose Name Comes Up? Auditing LLM-Based Scholar Recommendations
**Authors**: Daniele Barolo, Chiara Valentin, Fariba Karimi, Luis Galárraga, Gonzalo G. Méndez, Lisette Espín-Noboa

**Published Date**: 2025-05-29

**Updated Date**: 2025-09-10

**PDF Url**: [2506.00074v2](http://arxiv.org/pdf/2506.00074v2)

**Abstract**: This paper evaluates the performance of six open-weight LLMs (llama3-8b,
llama3.1-8b, gemma2-9b, mixtral-8x7b, llama3-70b, llama3.1-70b) in recommending
experts in physics across five tasks: top-k experts by field, influential
scientists by discipline, epoch, seniority, and scholar counterparts. The
evaluation examines consistency, factuality, and biases related to gender,
ethnicity, academic popularity, and scholar similarity. Using ground-truth data
from the American Physical Society and OpenAlex, we establish scholarly
benchmarks by comparing model outputs to real-world academic records. Our
analysis reveals inconsistencies and biases across all models. mixtral-8x7b
produces the most stable outputs, while llama3.1-70b shows the highest
variability. Many models exhibit duplication, and some, particularly gemma2-9b
and llama3.1-8b, struggle with formatting errors. LLMs generally recommend real
scientists, but accuracy drops in field-, epoch-, and seniority-specific
queries, consistently favoring senior scholars. Representation biases persist,
replicating gender imbalances (reflecting male predominance),
under-representing Asian scientists, and over-representing White scholars.
Despite some diversity in institutional and collaboration networks, models
favor highly cited and productive scholars, reinforcing the rich-getricher
effect while offering limited geographical representation. These findings
highlight the need to improve LLMs for more reliable and equitable scholarly
recommendations.


### Design-GenNO: A Physics-Informed Generative Model with Neural Operators for Inverse Microstructure Design
**Authors**: Yaohua Zang, Phaedon-Stelios Koutsourelakis

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08749v1](http://arxiv.org/pdf/2509.08749v1)

**Abstract**: Inverse microstructure design plays a central role in materials discovery,
yet remains challenging due to the complexity of structure-property linkages
and the scarcity of labeled training data. We propose Design-GenNO, a
physics-informed generative neural operator framework that unifies generative
modeling with operator learning to address these challenges. In Design-GenNO,
microstructures are encoded into a low-dimensional, well-structured latent
space, which serves as the generator for both reconstructing microstructures
and predicting solution fields of governing PDEs. MultiONet-based decoders
enable functional mappings from latent variables to both microstructures and
full PDE solution fields, allowing a multitude of design objectives to be
addressed without retraining. A normalizing flow prior regularizes the latent
space, facilitating efficient sampling and robust gradient-based optimization.
A distinctive feature of the framework is its physics-informed training
strategy: by embedding PDE residuals directly into the learning objective,
Design-GenNO significantly reduces reliance on labeled datasets and can even
operate in a self-supervised setting. We validate the method on a suite of
inverse design tasks in two-phase materials, including effective property
matching, recovery of microstructures from sparse field measurements, and
maximization of conductivity ratios. Across all tasks, Design-GenNO achieves
high accuracy, generates diverse and physically meaningful designs, and
consistently outperforms the state-of-the-art method. Moreover, it demonstrates
strong extrapolation by producing microstructures with effective properties
beyond the training distribution. These results establish Design-GenNO as a
robust and general framework for physics-informed inverse design, offering a
promising pathway toward accelerated materials discovery.


### DEQuify your force field: More efficient simulations using deep equilibrium models
**Authors**: Andreas Burger, Luca Thiede, Alán Aspuru-Guzik, Nandita Vijaykumar

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08734v1](http://arxiv.org/pdf/2509.08734v1)

**Abstract**: Machine learning force fields show great promise in enabling more accurate
molecular dynamics simulations compared to manually derived ones. Much of the
progress in recent years was driven by exploiting prior knowledge about
physical systems, in particular symmetries under rotation, translation, and
reflections. In this paper, we argue that there is another important piece of
prior information that, thus fa,r hasn't been explored: Simulating a molecular
system is necessarily continuous, and successive states are therefore extremely
similar. Our contribution is to show that we can exploit this information by
recasting a state-of-the-art equivariant base model as a deep equilibrium
model. This allows us to recycle intermediate neural network features from
previous time steps, enabling us to improve both accuracy and speed by
$10\%-20\%$ on the MD17, MD22, and OC20 200k datasets, compared to the non-DEQ
base model. The training is also much more memory efficient, allowing us to
train more expressive models on larger systems.


### RINO: Renormalization Group Invariance with No Labels
**Authors**: Zichun Hao, Raghav Kansal, Abhijith Gandrakota, Chang Sun, Ngadiuba Jennifer, Javier Duarte, Maria Spiropulu

**Published Date**: 2025-09-09

**Updated Date**: 2025-09-10

**PDF Url**: [2509.07486v2](http://arxiv.org/pdf/2509.07486v2)

**Abstract**: A common challenge with supervised machine learning (ML) in high energy
physics (HEP) is the reliance on simulations for labeled data, which can often
mismodel the underlying collision or detector response. To help mitigate this
problem of domain shift, we propose RINO (Renormalization Group Invariance with
No Labels), a self-supervised learning approach that can instead pretrain
models directly on collision data, learning embeddings invariant to
renormalization group flow scales. In this work, we pretrain a
transformer-based model on jets originating from quantum chromodynamic (QCD)
interactions from the JetClass dataset, emulating real QCD-dominated
experimental data, and then finetune on the JetNet dataset -- emulating
simulations -- for the task of identifying jets originating from top quark
decays. RINO demonstrates improved generalization from the JetNet training data
to JetClass data compared to supervised training on JetNet from scratch,
demonstrating the potential for RINO pretraining on real collision data
followed by fine-tuning on small, high-quality MC datasets, to improve the
robustness of ML models in HEP.


### Feynman paradox induced by vacuum and thermal fluctuations
**Authors**: Svend-Age Biehs, Ivan Latella

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08711v1](http://arxiv.org/pdf/2509.08711v1)

**Abstract**: A charged particle initially at rest in an external magnetic field starts to
rotate when the magnetic field is switched off. This is a variant of the
Feynman disc paradox, where the conservation of angular momentum is seemingly
violated. The paradox is understood by realizing that angular momentum is
initially stored in the electromagnetic field and is transferred to the
particle when the magnetic field is removed. In a classical description, no
rotation occurs if the particle is uncharged, as the initial angular momentum
is zero in this case. We show that electromagnetic fluctuations in thermal
equilibrium can induce a quantum analog of the Feynman paradox, where a
nonreciprocal particle without charge starts to rotate when the source of
nonreciprocity is removed. This paradox is due to persistent energy fluxes
arising in nonreciprocal systems at equilibrium, leading to angular momentum
stored in the electromagnetic field. We demonstrate that the contribution of
vacuum fluctuations to persistent energy fluxes dominate over thermal
fluctuations at finite temperature, so vacuum fluctuations dominate the
equilibrium angular momentum as well. Observation of the induced motion would
thus provide a means of detecting persistent energy fluxes and offer further
evidence for the physical reality of vacuum fluctuations.


### Quantifying model prediction sensitivity to model-form uncertainty
**Authors**: Teresa Portone, Rebekah D. White, Joseph L. Hart

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08708v1](http://arxiv.org/pdf/2509.08708v1)

**Abstract**: Model-form uncertainty (MFU) in assumptions made during physics-based model
development is widely considered a significant source of uncertainty; however,
there are limited approaches that can quantify MFU in predictions extrapolating
beyond available data. As a result, it is challenging to know how important MFU
is in practice, especially relative to other sources of uncertainty in a model,
making it difficult to prioritize resources and efforts to drive down error in
model predictions. To address these challenges, we present a novel method to
quantify the importance of uncertainties associated with model assumptions. We
combine parameterized modifications to assumptions (called MFU representations)
with grouped variance-based sensitivity analysis to measure the importance of
assumptions. We demonstrate how, in contrast to existing methods addressing
MFU, our approach can be applied without access to calibration data. However,
if calibration data is available, we demonstrate how it can be used to inform
the MFU representation, and how variance-based sensitivity analysis can be
meaningfully applied even in the presence of dependence between parameters (a
common byproduct of calibration).


### Solar System Constraints on Light Propagation from Higher Derivative Corrections to General Relativity and Implications for Fundamental Physics
**Authors**: Mark P. Hertzberg, Rachel Nathan, Suzanna E. Semaan

**Published Date**: 2025-03-25

**Updated Date**: 2025-09-10

**PDF Url**: [2503.19236v3](http://arxiv.org/pdf/2503.19236v3)

**Abstract**: While the two derivative action of gravitation is specified uniquely, higher
derivative operators are also allowed with coefficients that are not specified
uniquely by effective field theory. We focus on a four derivative operator in
which the Riemann tensor couples directly to the electromagnetic field
$a\,R_{\mu\nu\alpha\beta}F^{\mu\nu}F^{\alpha\beta}$. We compute the
corresponding corrections to the Shapiro time delay in the solar system and
compare this to data from the Cassini probe. We place an observational upper
bound on the coefficient $a$ at 95\% confidence $|a|<26\,(1000\,\mbox{km})^2$.
By way of motivation, we also compare this to a weak gravity conjecture (WGC)
prediction of a bound on the coefficients $a,\,b$ of four derivative operators
involving the graviton and the photon; this includes the above term
$a\,R_{\mu\nu\alpha\beta}F^{\mu\nu}F^{\alpha\beta}$ as well as $b\,F^4$. We
show that by using the observed value of the $b$ coefficient from measurements
of light by light scattering, which arises in the Standard Model from
integrating out the electron, the WGC predicted bound for $a$ is $a\lesssim
7.8\,(1000\,\mbox{km})^2$. This is consistent with the above observational
bound, but is intriguingly close and can be further probed in other
observations.


## Diffusion
### Reangle-A-Video: 4D Video Generation as Video-to-Video Translation
**Authors**: Hyeonho Jeong, Suhyeon Lee, Jong Chul Ye

**Published Date**: 2025-03-12

**Updated Date**: 2025-09-10

**PDF Url**: [2503.09151v3](http://arxiv.org/pdf/2503.09151v3)

**Abstract**: We introduce Reangle-A-Video, a unified framework for generating synchronized
multi-view videos from a single input video. Unlike mainstream approaches that
train multi-view video diffusion models on large-scale 4D datasets, our method
reframes the multi-view video generation task as video-to-videos translation,
leveraging publicly available image and video diffusion priors. In essence,
Reangle-A-Video operates in two stages. (1) Multi-View Motion Learning: An
image-to-video diffusion transformer is synchronously fine-tuned in a
self-supervised manner to distill view-invariant motion from a set of warped
videos. (2) Multi-View Consistent Image-to-Images Translation: The first frame
of the input video is warped and inpainted into various camera perspectives
under an inference-time cross-view consistency guidance using DUSt3R,
generating multi-view consistent starting images. Extensive experiments on
static view transport and dynamic camera control show that Reangle-A-Video
surpasses existing methods, establishing a new solution for multi-view video
generation. We will publicly release our code and data. Project page:
https://hyeonho99.github.io/reangle-a-video/


### Learning Turbulent Flows with Generative Models: Super-resolution, Forecasting, and Sparse Flow Reconstruction
**Authors**: Vivek Oommen, Siavash Khodakarami, Aniruddha Bora, Zhicheng Wang, George Em Karniadakis

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08752v1](http://arxiv.org/pdf/2509.08752v1)

**Abstract**: Neural operators are promising surrogates for dynamical systems but when
trained with standard L2 losses they tend to oversmooth fine-scale turbulent
structures. Here, we show that combining operator learning with generative
modeling overcomes this limitation. We consider three practical turbulent-flow
challenges where conventional neural operators fail: spatio-temporal
super-resolution, forecasting, and sparse flow reconstruction. For Schlieren
jet super-resolution, an adversarially trained neural operator (adv-NO) reduces
the energy-spectrum error by 15x while preserving sharp gradients at neural
operator-like inference cost. For 3D homogeneous isotropic turbulence, adv-NO
trained on only 160 timesteps from a single trajectory forecasts accurately for
five eddy-turnover times and offers 114x wall-clock speed-up at inference than
the baseline diffusion-based forecasters, enabling near-real-time rollouts. For
reconstructing cylinder wake flows from highly sparse Particle Tracking
Velocimetry-like inputs, a conditional generative model infers full 3D velocity
and pressure fields with correct phase alignment and statistics. These advances
enable accurate reconstruction and forecasting at low compute cost, bringing
near-real-time analysis and control within reach in experimental and
computational fluid mechanics. See our project page:
https://vivekoommen.github.io/Gen4Turb/


### Data-driven generative simulation of SDEs using diffusion models
**Authors**: Xuefeng Gao, Jiale Zha, Xun Yu Zhou

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08731v1](http://arxiv.org/pdf/2509.08731v1)

**Abstract**: This paper introduces a new approach to generating sample paths of unknown
stochastic differential equations (SDEs) using diffusion models, a class of
generative AI models commonly employed in image and video applications. Unlike
the traditional Monte Carlo methods for simulating SDEs, which require explicit
specifications of the drift and diffusion coefficients, our method takes a
model-free, data-driven approach. Given a finite set of sample paths from an
SDE, we utilize conditional diffusion models to generate new, synthetic paths
of the same SDE. To demonstrate the effectiveness of our approach, we conduct a
simulation experiment to compare our method with alternative benchmark ones
including neural SDEs. Furthermore, in an empirical study we leverage these
synthetically generated sample paths to enhance the performance of
reinforcement learning algorithms for continuous-time mean-variance portfolio
selection, hinting promising applications of diffusion models in financial
analysis and decision-making.


### BranchGRPO: Stable and Efficient GRPO with Structured Branching in Diffusion Models
**Authors**: Yuming Li, Yikai Wang, Yuying Zhu, Zhongyu Zhao, Ming Lu, Qi She, Shanghang Zhang

**Published Date**: 2025-09-07

**Updated Date**: 2025-09-10

**PDF Url**: [2509.06040v3](http://arxiv.org/pdf/2509.06040v3)

**Abstract**: Recent advancements in aligning image and video generative models via GRPO
have achieved remarkable gains in enhancing human preference alignment.
However, these methods still face high computational costs from on-policy
rollouts and excessive SDE sampling steps, as well as training instability due
to sparse rewards. In this paper, we propose BranchGRPO, a novel method that
introduces a branch sampling policy updating the SDE sampling process. By
sharing computation across common prefixes and pruning low-reward paths and
redundant depths, BranchGRPO substantially lowers the per-update compute cost
while maintaining or improving exploration diversity. This work makes three
main contributions: (1) a branch sampling scheme that reduces rollout and
training cost; (2) a tree-based advantage estimator incorporating dense
process-level rewards; and (3) pruning strategies exploiting path and depth
redundancy to accelerate convergence and boost performance. Experiments on
image and video preference alignment show that BranchGRPO improves alignment
scores by 16% over strong baselines, while cutting training time by 50%.


### Prompt-Driven Image Analysis with Multimodal Generative AI: Detection, Segmentation, Inpainting, and Interpretation
**Authors**: Kaleem Ahmad

**Published Date**: 2025-09-10

**Updated Date**: 2025-09-10

**PDF Url**: [2509.08489v1](http://arxiv.org/pdf/2509.08489v1)

**Abstract**: Prompt-driven image analysis converts a single natural-language instruction
into multiple steps: locate, segment, edit, and describe. We present a
practical case study of a unified pipeline that combines open-vocabulary
detection, promptable segmentation, text-conditioned inpainting, and
vision-language description into a single workflow. The system works end to end
from a single prompt, retains intermediate artifacts for transparent debugging
(such as detections, masks, overlays, edited images, and before and after
composites), and provides the same functionality through an interactive UI and
a scriptable CLI for consistent, repeatable runs. We highlight integration
choices that reduce brittleness, including threshold adjustments, mask
inspection with light morphology, and resource-aware defaults. In a small,
single-word prompt segment, detection and segmentation produced usable masks in
over 90% of cases with an accuracy above 85% based on our criteria. On a
high-end GPU, inpainting makes up 60 to 75% of total runtime under typical
guidance and sampling settings, which highlights the need for careful tuning.
The study offers implementation-guided advice on thresholds, mask tightness,
and diffusion parameters, and details version pinning, artifact logging, and
seed control to support replay. Our contribution is a transparent, reliable
pattern for assembling modern vision and multimodal models behind a single
prompt, with clear guardrails and operational practices that improve
reliability in object replacement, scene augmentation, and removal.


