# Abstracts of Papers

## Physics
### LiteReality: Graphics-Ready 3D Scene Reconstruction from RGB-D Scans
**Authors**: Zhening Huang, Xiaoyang Wu, Fangcheng Zhong, Hengshuang Zhao, Matthias Nießner, Joan Lasenby

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02861v1](http://arxiv.org/pdf/2507.02861v1)

**Abstract**: We propose LiteReality, a novel pipeline that converts RGB-D scans of indoor
environments into compact, realistic, and interactive 3D virtual replicas.
LiteReality not only reconstructs scenes that visually resemble reality but
also supports key features essential for graphics pipelines -- such as object
individuality, articulation, high-quality physically based rendering materials,
and physically based interaction. At its core, LiteReality first performs scene
understanding and parses the results into a coherent 3D layout and objects with
the help of a structured scene graph. It then reconstructs the scene by
retrieving the most visually similar 3D artist-crafted models from a curated
asset database. Next, the Material Painting module enhances realism by
recovering high-quality, spatially varying materials. Finally, the
reconstructed scene is integrated into a simulation engine with basic physical
properties to enable interactive behavior. The resulting scenes are compact,
editable, and fully compatible with standard graphics pipelines, making them
suitable for applications in AR/VR, gaming, robotics, and digital twins. In
addition, LiteReality introduces a training-free object retrieval module that
achieves state-of-the-art similarity performance on the Scan2CAD benchmark,
along with a robust material painting module capable of transferring
appearances from images of any style to 3D assets -- even under severe
misalignment, occlusion, and poor lighting. We demonstrate the effectiveness of
LiteReality on both real-life scans and public datasets. Project page:
https://litereality.github.io; Video:
https://www.youtube.com/watch?v=ecK9m3LXg2c


### Nine circles of elastic brittle fracture: A series of challenge problems to assess fracture models
**Authors**: Farhad Kamarei, Bo Zheng, John E. Dolbow, Oscar Lopez-Pamies

**Published Date**: 2025-06-30

**Updated Date**: 2025-07-03

**PDF Url**: [2507.00266v2](http://arxiv.org/pdf/2507.00266v2)

**Abstract**: Since the turn of the millennium, capitalizing on modern advances in
mathematics and computation, a slew of computational models have been proposed
in the literature with the objective of describing the nucleation and
propagation of fracture in materials subjected to mechanical, thermal, and/or
other types of loads. By and large, each new proposal focuses on a particular
aspect of the problem, while ignoring others that have been well-established.
This approach has resulted in a plethora of models that are, at best,
descriptors of fracture only under a restricted set of conditions, while they
may predict grossly incorrect and even non-physical behaviors in general. In an
attempt to address this predicament, this paper introduces a vetting process in
the form of nine challenge problems that any computational model of fracture
must convincingly handle if it is to potentially describe fracture nucleation
and propagation in general. The focus is on the most basic of settings, that of
isotropic elastic brittle materials subjected to quasi-static mechanical loads.
The challenge problems have been carefully selected so that: $i$) they can be
carried out experimentally with standard testing equipment; $ii$) they can be
unambiguously analyzed with a sharp description of fracture; and, most
critically, $iii$) in aggregate they span the entire range of well settled
experimental knowledge on fracture nucleation and propagation that has been
amassed for over a century. For demonstration purposes, after their
introduction, each challenge problem is solved with two phase-field models of
fracture.


### Bayesian frequency estimation at the fundamental quantum limit
**Authors**: James W. Gardner, Tuvia Gefen, Ethan Payne, Su Direkci, Sander M. Vermeulen, Simon A. Haine, Joseph J. Hope, Lee McCuller, Yanbei Chen

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02811v1](http://arxiv.org/pdf/2507.02811v1)

**Abstract**: Searching for a weak signal at an unknown frequency is a canonical task in
experiments probing fundamental physics such as gravitational-wave
observatories and ultra-light dark matter haloscopes. These state-of-the-art
sensors are limited by quantum noise arising from the fundamental uncertainty
about the state of the device. Classically, frequency estimation suffers from a
threshold effect in the signal-to-noise ratio such that weak signals are
extremely hard to localise in frequency. We show that this phenomenon persists
at the fundamental quantum limit but that the classical approach, a quadrature
measurement, can nevertheless be beaten by a coherent protocol of projecting
onto the "quantum whitened" possible quantum states. Quantum whitening is a
covariant measurement, and we examine it analytically in the wide-prior limit
and numerically for finite-width priors. Beyond accelerating searches for
unknown frequencies, quantum whitening may be used generally to sense the
parameter of a unitary encoding given no prior information about the parameter.


### PAD: Phase-Amplitude Decoupling Fusion for Multi-Modal Land Cover Classification
**Authors**: Huiling Zheng, Xian Zhong, Bin Liu, Yi Xiao, Bihan Wen, Xiaofeng Li

**Published Date**: 2025-04-27

**Updated Date**: 2025-07-03

**PDF Url**: [2504.19136v2](http://arxiv.org/pdf/2504.19136v2)

**Abstract**: The fusion of Synthetic Aperture Radar (SAR) and RGB imagery for land cover
classification remains challenging due to modality heterogeneity and
underutilized spectral complementarity. Existing methods often fail to decouple
shared structural features from modality-complementary radiometric attributes,
causing feature conflicts and information loss. To address this, we propose
Phase-Amplitude Decoupling (PAD), a frequency-aware framework that separates
phase (modality-shared) and amplitude (modality-complementary) components in
the Fourier domain, thus reinforcing shared structures while preserving
complementary characteristics to improve fusion quality. Unlike prior
approaches that overlook the distinct physical properties encoded in frequency
spectra, PAD is the first to introduce explicit amplitude-phase decoupling for
multi-modal fusion. Specifically, PAD comprises two key components: 1) Phase
Spectrum Correction (PSC), which aligns cross-modal phase features via
convolution-guided scaling to enhance geometric consistency; and 2) Amplitude
Spectrum Fusion (ASF), which dynamically integrates high-frequency and
low-frequency patterns using frequency-adaptive multilayer perceptrons,
leveraging SAR's morphological sensitivity and RGB's spectral richness.
Extensive experiments on WHU-OPT-SAR and DDHR-SK datasets demonstrate
state-of-the-art performance. Our work establishes a new paradigm for
physics-aware multi-modal fusion in remote sensing. The code will be available
at https://github.com/RanFeng2/PAD.


### LLM-Powered Prediction of Hyperglycemia and Discovery of Behavioral Treatment Pathways from Wearables and Diet
**Authors**: Abdullah Mamun, Asiful Arefeen, Susan B. Racette, Dorothy D. Sears, Corrie M. Whisner, Matthew P. Buman, Hassan Ghasemzadeh

**Published Date**: 2025-03-05

**Updated Date**: 2025-07-03

**PDF Url**: [2503.03935v2](http://arxiv.org/pdf/2503.03935v2)

**Abstract**: Postprandial hyperglycemia, marked by the blood glucose level exceeding the
normal range after consuming a meal, is a critical indicator of progression
toward type 2 diabetes in people with prediabetes and in healthy individuals. A
key metric for understanding blood glucose dynamics after eating is the
postprandial area under the curve (AUC). Predicting postprandial AUC in advance
based on a person's lifestyle factors, such as diet and physical activity
level, and explaining the factors that affect postprandial blood glucose could
allow an individual to adjust their lifestyle accordingly to maintain normal
glucose levels. In this study, we developed an explainable machine learning
solution, GlucoLens, that takes sensor-driven inputs and uses advanced data
processing, large language models, and trainable machine learning models to
predict postprandial AUC and hyperglycemia from diet, physical activity, and
recent glucose patterns. We used data obtained from wearables in a five-week
clinical trial of 10 adults who worked full-time to develop and evaluate the
proposed computational model that integrates wearable sensing, multimodal data,
and machine learning. Our machine learning model takes multimodal data from
wearable activity and glucose monitoring sensors, along with food and work
logs, and provides an interpretable prediction of the postprandial glucose
pattern. Our GlucoLens system achieves a normalized root mean squared error
(NRMSE) of 0.123 in its best configuration. On average, the proposed technology
provides a 16% better performance level compared to the comparison models.
Additionally, our technique predicts hyperglycemia with an accuracy of 73.3%
and an F1 score of 0.716 and recommends different treatment options to help
avoid hyperglycemia through diverse counterfactual explanations. Code
available: https://github.com/ab9mamun/GlucoLens.


### Grounding Intelligence in Movement
**Authors**: Melanie Segado, Felipe Parodi, Jordan K. Matelsky, Michael L. Platt, Eva B. Dyer, Konrad P. Kording

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02771v1](http://arxiv.org/pdf/2507.02771v1)

**Abstract**: Recent advances in machine learning have dramatically improved our ability to
model language, vision, and other high-dimensional data, yet they continue to
struggle with one of the most fundamental aspects of biological systems:
movement. Across neuroscience, medicine, robotics, and ethology, movement is
essential for interpreting behavior, predicting intent, and enabling
interaction. Despite its core significance in our intelligence, movement is
often treated as an afterthought rather than as a rich and structured modality
in its own right. This reflects a deeper fragmentation in how movement data is
collected and modeled, often constrained by task-specific goals and
domain-specific assumptions. But movement is not domain-bound. It reflects
shared physical constraints, conserved morphological structures, and purposeful
dynamics that cut across species and settings. We argue that movement should be
treated as a primary modeling target for AI. It is inherently structured and
grounded in embodiment and physics. This structure, often allowing for compact,
lower-dimensional representations (e.g., pose), makes it more interpretable and
computationally tractable to model than raw, high-dimensional sensory inputs.
Developing models that can learn from and generalize across diverse movement
data will not only advance core capabilities in generative modeling and
control, but also create a shared foundation for understanding behavior across
biological and artificial systems. Movement is not just an outcome, it is a
window into how intelligent systems engage with the world.


### Defining and classifying models of groups: The social ontology of higher-order networks
**Authors**: Jonathan St-Onge, Randall Harp, Giulio Burgio, Timothy M. Waring, Juniper Lovato, Laurent Hébert-Dufresne

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02758v1](http://arxiv.org/pdf/2507.02758v1)

**Abstract**: In complex systems research, the study of higher-order interactions has
exploded in recent years. Researchers have formalized various types of group
interactions, such as public goods games, biological contagion, and information
broadcasting, showing how higher-order networks can capture group effects more
directly than pairwise models. However, equating hyperedges-edges involving
more than two agents-with groups can be misleading, as it obscures the
polysemous nature of ``group interactions''. For instance, many models of
higher-order interactions focus on the internal state of the hyperedge,
specifying dynamical rules at the group level. These models often neglect how
interactions with external groups can influence behaviors and dynamics within
the group. Yet, anthropologists and philosophers remind us that external norms,
factors, and forces governing intergroup behavior are essential to defining
within-group dynamics. In this paper, we synthesize concepts from social
ontology relevant to the emerging physics of higher-order networks. We propose
a typology for classifying models of group interactions based on two
perspectives. The first focuses on individuals within groups engaging in
collective action, where shared agency serves as the binding force. The second
adopts a group-first approach, emphasizing institutional facts that extend
beyond the specific individuals involved. Building on these perspectives, we
introduce four dimensions to classify models of group interactions:
persistence, coupling, reducibility, and alignment. For the physics of
higher-order networks, we provide a hierarchy of nested mathematical models to
explore the complex properties of social groups. We highlight social
interactions not yet explored in the literature on higher-order networks and
propose future research avenues to foster collaboration between social ontology
and the physics of complex systems.


### Bounded information as a foundation for quantum theory
**Authors**: Paolo Ferro

**Published Date**: 2025-06-23

**Updated Date**: 2025-07-03

**PDF Url**: [2506.18549v2](http://arxiv.org/pdf/2506.18549v2)

**Abstract**: The purpose of this paper is to formalize the concept that best synthesizes
our intuitive understanding of quantum mechanics -- that the information
carried by a system is limited -- and, from this principle, to construct the
foundations of quantum theory. In our discussion, we also introduce a second
important hypothesis: if a measurement closely approximates an ideal one in
terms of experimental precision, the information it provides about a physical
system is independent of the measurement method and, specifically, of the
system's physical quantities being measured. This principle can be expressed in
terms of metric properties of a manifold whose points represent the state of
the system. These and other reasonable hypotheses provide the foundation for a
framework of quantum reconstruction.
  The theory presented in this paper is based on a description of physical
systems in terms of their statistical properties, specifically statistical
parameters, and focuses on the study of estimators for these parameters. To
achieve the goal of quantum reconstruction, a divide-and-conquer approach is
employed, wherein the space of two discrete conjugate Hamiltonian variables is
partitioned into a binary tree of nested sets. This approach naturally leads to
the reconstruction of the linear and probabilistic structure of quantum
mechanics.


### Generation of Intense Deep-Ultraviolet Pulses at 200 nm
**Authors**: X. Xie, S. Soultanis, G. Knopp, A. L. Cavalieri, S. L. Johnson

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02756v1](http://arxiv.org/pdf/2507.02756v1)

**Abstract**: We report the generation of intense deep ultraviolet pulses at 200 nm with a
duration of 48 fs and pulse energy of 130 uJ, achieved via cascaded sum
frequency generation using 800 nm femtosecond pulses in barium borate crystals.
Efficient frequency up-conversion is realized by optimizing phase-matching
conditions and implementing dispersion control, while maintaining the
ultrashort pulse characteristics. The generated deep ultraviolet pulses are
characterized using two-photon absorption frequency-resolved optical gating,
providing detailed insight into their temporal profile and phase. This approach
addresses key challenges in ultrashort deep ultraviolet pulse generation,
delivering a high-energy, ultrashort source suitable for ultrafast
spectroscopy, nonlinear optics, and strong-field physics. These results
represent a significant advancement in the generation of high-energy,
ultrashort deep ultraviolet pulses, opening new possibilities for time-resolved
investigations in ultrafast molecular dynamics, as well as emerging
applications in semiconductor science, quantum materials, and photochemistry.


### Linear Attention with Global Context: A Multipole Attention Mechanism for Vision and Physics
**Authors**: Alex Colagrande, Paul Caillon, Eva Feillet, Alexandre Allauzen

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02748v1](http://arxiv.org/pdf/2507.02748v1)

**Abstract**: Transformers have become the de facto standard for a wide range of tasks,
from image classification to physics simulations. Despite their impressive
performance, the quadratic complexity of standard Transformers in both memory
and time with respect to the input length makes them impractical for processing
high-resolution inputs. Therefore, several variants have been proposed, the
most successful relying on patchification, downsampling, or coarsening
techniques, often at the cost of losing the finest-scale details. In this work,
we take a different approach. Inspired by state-of-the-art techniques in
$n$-body numerical simulations, we cast attention as an interaction problem
between grid points. We introduce the Multipole Attention Neural Operator
(MANO), which computes attention in a distance-based multiscale fashion. MANO
maintains, in each attention head, a global receptive field and achieves linear
time and memory complexity with respect to the number of grid points. Empirical
results on image classification and Darcy flows demonstrate that MANO rivals
state-of-the-art models such as ViT and Swin Transformer, while reducing
runtime and peak memory usage by orders of magnitude. We open source our code
for reproducibility at https://github.com/AlexColagrande/MANO.


## Diffusion
### USAD: An Unsupervised Data Augmentation Spatio-Temporal Attention Diffusion Network
**Authors**: Ying Yu, Hang Xiao, Siyao Li, Jiarui Li, Haotian Tang, Hanyu Liu, Chao Li

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02827v1](http://arxiv.org/pdf/2507.02827v1)

**Abstract**: The primary objective of human activity recognition (HAR) is to infer ongoing
human actions from sensor data, a task that finds broad applications in health
monitoring, safety protection, and sports analysis. Despite proliferating
research, HAR still faces key challenges, including the scarcity of labeled
samples for rare activities, insufficient extraction of high-level features,
and suboptimal model performance on lightweight devices. To address these
issues, this paper proposes a comprehensive optimization approach centered on
multi-attention interaction mechanisms. First, an unsupervised,
statistics-guided diffusion model is employed to perform data augmentation,
thereby alleviating the problems of labeled data scarcity and severe class
imbalance. Second, a multi-branch spatio-temporal interaction network is
designed, which captures multi-scale features of sequential data through
parallel residual branches with 3*3, 5*5, and 7*7 convolutional kernels.
Simultaneously, temporal attention mechanisms are incorporated to identify
critical time points, while spatial attention enhances inter-sensor
interactions. A cross-branch feature fusion unit is further introduced to
improve the overall feature representation capability. Finally, an adaptive
multi-loss function fusion strategy is integrated, allowing for dynamic
adjustment of loss weights and overall model optimization. Experimental results
on three public datasets, WISDM, PAMAP2, and OPPORTUNITY, demonstrate that the
proposed unsupervised data augmentation spatio-temporal attention diffusion
network (USAD) achieves accuracies of 98.84%, 93.81%, and 80.92% respectively,
significantly outperforming existing approaches. Furthermore, practical
deployment on embedded devices verifies the efficiency and feasibility of the
proposed method.


### FairHuman: Boosting Hand and Face Quality in Human Image Generation with Minimum Potential Delay Fairness in Diffusion Models
**Authors**: Yuxuan Wang, Tianwei Cao, Huayu Zhang, Zhongjiang He, Kongming Liang, Zhanyu Ma

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02714v1](http://arxiv.org/pdf/2507.02714v1)

**Abstract**: Image generation has achieved remarkable progress with the development of
large-scale text-to-image models, especially diffusion-based models. However,
generating human images with plausible details, such as faces or hands, remains
challenging due to insufficient supervision of local regions during training.
To address this issue, we propose FairHuman, a multi-objective fine-tuning
approach designed to enhance both global and local generation quality fairly.
Specifically, we first construct three learning objectives: a global objective
derived from the default diffusion objective function and two local objectives
for hands and faces based on pre-annotated positional priors. Subsequently, we
derive the optimal parameter updating strategy under the guidance of the
Minimum Potential Delay (MPD) criterion, thereby attaining fairness-ware
optimization for this multi-objective problem. Based on this, our proposed
method can achieve significant improvements in generating challenging local
details while maintaining overall quality. Extensive experiments showcase the
effectiveness of our method in improving the performance of human image
generation under different scenarios.


### APT: Adaptive Personalized Training for Diffusion Models with Limited Data
**Authors**: JungWoo Chae, Jiyoon Kim, JaeWoong Choi, Kyungyul Kim, Sangheum Hwang

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02687v1](http://arxiv.org/pdf/2507.02687v1)

**Abstract**: Personalizing diffusion models using limited data presents significant
challenges, including overfitting, loss of prior knowledge, and degradation of
text alignment. Overfitting leads to shifts in the noise prediction
distribution, disrupting the denoising trajectory and causing the model to lose
semantic coherence. In this paper, we propose Adaptive Personalized Training
(APT), a novel framework that mitigates overfitting by employing adaptive
training strategies and regularizing the model's internal representations
during fine-tuning. APT consists of three key components: (1) Adaptive Training
Adjustment, which introduces an overfitting indicator to detect the degree of
overfitting at each time step bin and applies adaptive data augmentation and
adaptive loss weighting based on this indicator; (2)Representation
Stabilization, which regularizes the mean and variance of intermediate feature
maps to prevent excessive shifts in noise prediction; and (3) Attention
Alignment for Prior Knowledge Preservation, which aligns the cross-attention
maps of the fine-tuned model with those of the pretrained model to maintain
prior knowledge and semantic coherence. Through extensive experiments, we
demonstrate that APT effectively mitigates overfitting, preserves prior
knowledge, and outperforms existing methods in generating high-quality, diverse
images with limited reference data.


### Learning few-step posterior samplers by unfolding and distillation of diffusion models
**Authors**: Charlesquin Kemajou Mbakam, Jonathan Spence, Marcelo Pereyra

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02686v1](http://arxiv.org/pdf/2507.02686v1)

**Abstract**: Diffusion models (DMs) have emerged as powerful image priors in Bayesian
computational imaging. Two primary strategies have been proposed for leveraging
DMs in this context: Plug-and-Play methods, which are zero-shot and highly
flexible but rely on approximations; and specialized conditional DMs, which
achieve higher accuracy and faster inference for specific tasks through
supervised training. In this work, we introduce a novel framework that
integrates deep unfolding and model distillation to transform a DM image prior
into a few-step conditional model for posterior sampling. A central innovation
of our approach is the unfolding of a Markov chain Monte Carlo (MCMC) algorithm
- specifically, the recently proposed LATINO Langevin sampler (Spagnoletti et
al., 2025) - representing the first known instance of deep unfolding applied to
a Monte Carlo sampling scheme. We demonstrate our proposed unfolded and
distilled samplers through extensive experiments and comparisons with the state
of the art, where they achieve excellent accuracy and computational efficiency,
while retaining the flexibility to adapt to variations in the forward model at
inference time.


### Guided Generation for Developable Antibodies
**Authors**: Siqi Zhao, Joshua Moller, Porfi Quintero-Cadena, Lood van Niekerk

**Published Date**: 2025-07-03

**Updated Date**: 2025-07-03

**PDF Url**: [2507.02670v1](http://arxiv.org/pdf/2507.02670v1)

**Abstract**: Therapeutic antibodies require not only high-affinity target engagement, but
also favorable manufacturability, stability, and safety profiles for clinical
effectiveness. These properties are collectively called `developability'. To
enable a computational framework for optimizing antibody sequences for
favorable developability, we introduce a guided discrete diffusion model
trained on natural paired heavy- and light-chain sequences from the Observed
Antibody Space (OAS) and quantitative developability measurements for 246
clinical-stage antibodies. To steer generation toward biophysically viable
candidates, we integrate a Soft Value-based Decoding in Diffusion (SVDD) Module
that biases sampling without compromising naturalness. In unconstrained
sampling, our model reproduces global features of both the natural repertoire
and approved therapeutics, and under SVDD guidance we achieve significant
enrichment in predicted developability scores over unguided baselines. When
combined with high-throughput developability assays, this framework enables an
iterative, ML-driven pipeline for designing antibodies that satisfy binding and
biophysical criteria in tandem.


