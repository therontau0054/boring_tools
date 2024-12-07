# Abstracts of Papers

## Physics
### Block Lanczos for lattice QCD spectroscopy and matrix elements
**Authors**: Daniel C. Hackett, Michael L. Wagman

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04444v1](http://arxiv.org/pdf/2412.04444v1)

**Abstract**: Recent work introduced a new framework for analyzing correlation functions
with improved convergence and signal-to-noise properties, as well as rigorous
quantification of excited-state effects, based on the Lanczos algorithm and
spurious eigenvalue filtering with the Cullum-Willoughby test. Here, we extend
this framework to the analysis of correlation-function matrices built from
multiple interpolating operators in lattice quantum chromodynamics (QCD) by
constructing an oblique generalization of the block Lanczos algorithm, as well
as a new physically motivated reformulation of the Cullum-Willoughby test that
generalizes to block Lanczos straightforwardly. The resulting block Lanczos
method directly extends generalized eigenvalue problem (GEVP) methods, which
can be viewed as applying a single iteration of block Lanczos. Block Lanczos
provides qualitative and quantitative advantages over GEVP methods analogous to
the benefits of Lanczos over the standard effective mass, including faster
convergence to ground- and excited-state energies, explicitly computable
two-sided error bounds, straightforward extraction of matrix elements of
external currents, and asymptotically constant signal-to-noise. No fits or
statistical inference are required. Proof-of-principle calculations are
performed for noiseless mock-data examples as well as two-by-two proton
correlation-function matrices in lattice QCD.


### PDMD: Potential-free Data-driven Molecular Dynamics for Variable-sized Water Clusters
**Authors**: Hongyu Yan, Qi Dai, Yong Wei, Minghan Chen, Hanning Chen

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04442v1](http://arxiv.org/pdf/2412.04442v1)

**Abstract**: Conventional molecular dynamics (MD) simulation approaches, such as ab initio
MD and empirical force field MD, face significant trade-offs between physical
accuracy and computational efficiency. This work presents a novel
Potential-free Data-driven Molecular Dynamics (PDMD) framework for predicting
system energy and atomic forces of variable-sized water clusters. Specifically,
PDMD employs the smooth overlap of atomic positions descriptor to generate
high-dimensional, equivariant features before leveraging ChemGNN, a graph
neural network model that adaptively learns the atomic chemical environments
without requiring a priori knowledge. Through an iterative self-consistent
training approach, the converged PDMD achieves a mean absolute error of 7.1
meV/atom for energy and 59.8 meV/angstrom for forces, outperforming the
state-of-the-art DeepMD by ~80% in energy accuracy and ~200% in force
prediction. As a result, PDMD can reproduce the ab initio MD properties of
water clusters at a tiny fraction of its computational cost. These results
demonstrate that the proposed PDMD offers multiple-phase predictive power,
enabling ultra-fast, general-purpose MD simulations while retaining ab initio
accuracy.


### Masked Autoencoders are PDE Learners
**Authors**: Anthony Zhou, Amir Barati Farimani

**Published Date**: 2024-03-26

**Updated Date**: 2024-12-05

**PDF Url**: [2403.17728v3](http://arxiv.org/pdf/2403.17728v3)

**Abstract**: Neural solvers for partial differential equations (PDEs) have great potential
to generate fast and accurate physics solutions, yet their practicality is
currently limited by their generalizability. PDEs evolve over broad scales and
exhibit diverse behaviors; predicting these phenomena will require learning
representations across a wide variety of inputs which may encompass different
coefficients, boundary conditions, resolutions, or even equations. As a step
towards generalizable PDE modeling, we adapt masked pretraining for physics
problems. Through self-supervised learning across PDEs, masked autoencoders can
consolidate heterogeneous physics to learn rich latent representations. We show
that learned representations can generalize to a limited set of unseen
equations or parameters and are meaningful enough to regress PDE coefficients
or the classify PDE features. Furthermore, conditioning neural solvers on
learned latent representations can improve time-stepping and super-resolution
performance across a variety of coefficients, discretizations, or boundary
conditions, as well as on certain unseen PDEs. We hope that masked pretraining
can emerge as a unifying method across large, unlabeled, and heterogeneous
datasets to learn latent physics at scale.


### Black Hole Solutions in Non-Minimally Coupled Weyl Connection Gravity
**Authors**: M. Margarida Lima, Cláudio Gomes

**Published Date**: 2024-10-02

**Updated Date**: 2024-12-05

**PDF Url**: [2410.01856v2](http://arxiv.org/pdf/2410.01856v2)

**Abstract**: Schwarzschild and Reissner-Nordstr{\o}m black hole solutions are found in the
context of a non-minimal matter-curvature coupling with the Weyl connection,
both in vacuum and in the presence of a cosmological constant-like matter
content. This special case of non-metricity leads to black hole solutions with
non-vanishing scalar curvature. Moreover, vacuum Schwarzschild solutions differ
from the ones from a constant curvature scenario in $f(R)$ theories with the
appearance of a coefficient in the term linear in r and a corrected
"cosmological constant". Non-vacuum Shwarzschild solutions have formally the
same solutions as in the previous case with the exception being the physical
interpretation of a cosmological constant as the source of the matter
Lagrangian as not a simple reparametrization of the $f(R)$ description.
Reissner-Nordstr{\o}m solutions cannot be found in vacuum, but only in the
presence of matter fields, such that the solutions also differ from the
constant curvature scenario in $f(R)$ theories by the term linear in r and
corrected/dressed charge and cosmological constant.


### ACE2-SOM: Coupling to a slab ocean and learning the sensitivity of climate to changes in CO$_2$
**Authors**: Spencer K. Clark, Oliver Watt-Meyer, Anna Kwa, Jeremy McGibbon, Brian Henn, W. Andre Perkins, Elynn Wu, Christopher S. Bretherton, Lucas M. Harris

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04418v1](http://arxiv.org/pdf/2412.04418v1)

**Abstract**: While autoregressive machine-learning-based emulators have been trained to
produce stable and accurate rollouts in the climate of the present-day and
recent past, none so far have been trained to emulate the sensitivity of
climate to substantial changes in CO$_2$ or other greenhouse gases. As an
initial step we couple the Ai2 Climate Emulator version 2 to a slab ocean model
(hereafter ACE2-SOM) and train it on output from a collection of
equilibrium-climate physics-based reference simulations with varying levels of
CO$_2$. We test it in equilibrium and non-equilibrium climate scenarios with
CO$_2$ concentrations seen and unseen in training.
  ACE2-SOM performs well in equilibrium-climate inference with both in-sample
and out-of-sample CO$_2$ concentrations, accurately reproducing the emergent
time-mean spatial patterns of surface temperature and precipitation change with
CO$_2$ doubling, tripling, or quadrupling. In addition, the vertical profile of
atmospheric warming and change in extreme precipitation rates with increased
CO$_2$ closely agree with the reference model. Non-equilibrium-climate
inference is more challenging. With CO$_2$ increasing gradually at a rate of 2%
year$^{-1}$, ACE2-SOM can accurately emulate the global annual mean trends of
surface and lower-to-middle atmosphere fields but produces unphysical jumps in
stratospheric fields. With an abrupt quadrupling of CO$_2$, ML-controlled
fields transition unrealistically quickly to the 4xCO$_2$ regime. In doing so
they violate global energy conservation and exhibit unphysical sensitivities of
and surface and top of atmosphere radiative fluxes to instantaneous changes in
CO$_2$. Future emulator development needed to address these issues should
improve its generalizability to diverse climate change scenarios.


### Emergent unitary designs for encoded qubits from coherent errors and syndrome measurements
**Authors**: Zihan Cheng, Eric Huang, Vedika Khemani, Michael J. Gullans, Matteo Ippoliti

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04414v1](http://arxiv.org/pdf/2412.04414v1)

**Abstract**: Unitary $k$-designs are distributions of unitary gates that match the Haar
distribution up to its $k$-th statistical moment. They are a crucial resource
for randomized quantum protocols. However, their implementation on encoded
logical qubits is nontrivial due to the need for magic gates, which can require
a large resource overhead. In this work, we propose an efficient approach to
generate unitary designs for encoded qubits in surface codes by applying local
unitary rotations ("coherent errors") on the physical qubits followed by
syndrome measurement and error correction. We prove that under some conditions
on the coherent errors (notably including all single-qubit unitaries) and on
the error correcting code, this process induces a unitary transformation of the
logical subspace. We numerically show that the ensemble of logical unitaries
(indexed by the random syndrome outcomes) converges to a unitary design in the
thermodynamic limit, provided the density or strength of coherent errors is
above a finite threshold. This "unitary design" phase transition coincides with
the code's coherent error threshold under optimal decoding. Furthermore, we
propose a classical algorithm to simulate the protocol based on a "staircase"
implementation of the surface code encoder and decoder circuits. This enables a
mapping to a 1+1D monitored circuit, where we observe an entanglement phase
transition (and thus a classical complexity phase transition of the decoding
algorithm) coinciding with the aforementioned unitary design phase transition.
Our results provide a practical way to realize unitary designs on encoded
qubits, with applications including quantum state tomography and benchmarking
in error correcting codes.


### Providing Differential Privacy for Federated Learning Over Wireless: A Cross-layer Framework
**Authors**: Jiayu Mao, Tongxin Yin, Aylin Yener, Mingyan Liu

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04408v1](http://arxiv.org/pdf/2412.04408v1)

**Abstract**: Federated Learning (FL) is a distributed machine learning framework that
inherently allows edge devices to maintain their local training data, thus
providing some level of privacy. However, FL's model updates still pose a risk
of privacy leakage, which must be mitigated. Over-the-air FL (OTA-FL) is an
adapted FL design for wireless edge networks that leverages the natural
superposition property of the wireless medium. We propose a wireless physical
layer (PHY) design for OTA-FL which improves differential privacy (DP) through
a decentralized, dynamic power control that utilizes both inherent Gaussian
noise in the wireless channel and a cooperative jammer (CJ) for additional
artificial noise generation when higher privacy levels are required. Although
primarily implemented within the Upcycled-FL framework, where a
resource-efficient method with first-order approximations is used at every even
iteration to decrease the required information from clients, our power control
strategy is applicable to any FL framework, including FedAvg and FedProx as
shown in the paper. This adaptation showcases the flexibility and effectiveness
of our design across different learning algorithms while maintaining a strong
emphasis on privacy. Our design removes the need for client-side artificial
noise injection for DP, utilizing a cooperative jammer to enhance privacy
without affecting transmission efficiency for higher privacy demands. Privacy
analysis is provided using the Moments Accountant method. We perform a
convergence analysis for non-convex objectives to tackle heterogeneous data
distributions, highlighting the inherent trade-offs between privacy and
accuracy. Numerical results show that our approach with various FL algorithms
outperforms the state-of-the-art under the same DP conditions on the non-i.i.d.
FEMNIST dataset, and highlight the cooperative jammer's effectiveness in
ensuring strict privacy.


### Demonstration of quantum computation and error correction with a tesseract code
**Authors**: Ben W. Reichardt, David Aasen, Rui Chao, Alex Chernoguzov, Wim van Dam, John P. Gaebler, Dan Gresh, Dominic Lucchetti, Michael Mills, Steven A. Moses, Brian Neyenhuis, Adam Paetznick, Andres Paz, Peter E. Siegfried, Marcus P. da Silva, Krysta M. Svore, Zhenghan Wang, Matt Zanner

**Published Date**: 2024-09-06

**Updated Date**: 2024-12-05

**PDF Url**: [2409.04628v2](http://arxiv.org/pdf/2409.04628v2)

**Abstract**: A critical milestone for quantum computers is to demonstrate fault-tolerant
computation that outperforms computation on physical qubits. The tesseract
subsystem color code protects four logical qubits in 16 physical qubits, to
distance four. Using the tesseract code on Quantinuum's trapped-ion quantum
computers, we prepare high-fidelity encoded graph states on up to 12 logical
qubits, beneficially combining for the first time fault-tolerant error
correction and computation. We also protect encoded states through up to five
rounds of error correction. Using performant quantum software and hardware
together allows moderate-depth logical quantum circuits to have an order of
magnitude less error than the equivalent unencoded circuits.


### Enhanced Sampling of Protein Conformational Changes via True Reaction Coordinates from Energy Relaxation
**Authors**: Huiyu Li, Ao Ma

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04400v1](http://arxiv.org/pdf/2412.04400v1)

**Abstract**: The bottleneck in enhanced sampling lies in finding collective variables
(CVs) that can effectively accelerate protein conformational changes. True
reaction coordinates (tRCs) that can predict the committor are considered the
optimal CVs, but identifying them requires unbiased natural reactive
trajectories, which, paradoxically, depend on effective enhanced sampling.
Using the generalized work functional method, we found that tRCs control both
conformational changes and energy relaxation, enabling us to compute tRCs from
energy relaxation simulations. Applying bias to tRCs accelerated conformational
changes and ligand dissociation in HIV-1 protease and the PDZ2 domain by 10^5
to 10^15-fold. The resulting trajectories follow natural transition pathways,
enabling efficient generation of natural reactive trajectories. In contrast,
biased trajectories from empirical CVs often display non-physical features.
Furthermore, by computing tRCs from a single protein structure, our method
enables predictive sampling of conformational changes. These findings
significantly broaden the range of protein functional processes accessible to
molecular dynamics simulations.


### Studies of Cherenkov Photon Production in PbF$_2$ Crystals using Proton Beams at Fermilab
**Authors**: Thomas Anderson, Alberto Belloni, Grace Cummings, Sarah Eno, Nora Fischer, Liang Guan, Yuxiang Guo, Robert Hirosky, James Hirschauer, Yihui Lai, Daniel Levin, Hui-Chi Lin, Mekhala Paranjpe, Jianming Qian, Bing Zhou, Junjie Zhu, Ren-Yuan Zhu

**Published Date**: 2024-07-10

**Updated Date**: 2024-12-05

**PDF Url**: [2407.08033v2](http://arxiv.org/pdf/2407.08033v2)

**Abstract**: Future lepton colliders such as the FCC-ee, CEPC, ILC, or a muon collider
will collect large data samples that allow precision physics studies with
unprecedented accuracy, especially when the data is collected by innovative
state-of-the-art detectors. An electromagnetic calorimeter based on
scintillating crystals, designed to separately record Cherenkov and
scintillation light, can achieve precision measurements of electrons and
photons without sacrificing jet energy resolution, given adequate light
collection efficiency and separation. This paper presents initial measurements
from a program aimed at developing such a calorimeter system for future
colliders. We focus on using PbF2 crystals to enhance the understanding of
Cherenkov light collection, marking the first step in this endeavor.


## Diffusion
### PaintScene4D: Consistent 4D Scene Generation from Text Prompts
**Authors**: Vinayak Gupta, Yunze Man, Yu-Xiong Wang

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04471v1](http://arxiv.org/pdf/2412.04471v1)

**Abstract**: Recent advances in diffusion models have revolutionized 2D and 3D content
creation, yet generating photorealistic dynamic 4D scenes remains a significant
challenge. Existing dynamic 4D generation methods typically rely on distilling
knowledge from pre-trained 3D generative models, often fine-tuned on synthetic
object datasets. Consequently, the resulting scenes tend to be object-centric
and lack photorealism. While text-to-video models can generate more realistic
scenes with motion, they often struggle with spatial understanding and provide
limited control over camera viewpoints during rendering. To address these
limitations, we present PaintScene4D, a novel text-to-4D scene generation
framework that departs from conventional multi-view generative models in favor
of a streamlined architecture that harnesses video generative models trained on
diverse real-world datasets. Our method first generates a reference video using
a video generation model, and then employs a strategic camera array selection
for rendering. We apply a progressive warping and inpainting technique to
ensure both spatial and temporal consistency across multiple viewpoints.
Finally, we optimize multi-view images using a dynamic renderer, enabling
flexible camera control based on user preferences. Adopting a training-free
architecture, our PaintScene4D efficiently produces realistic 4D scenes that
can be viewed from arbitrary trajectories. The code will be made publicly
available. Our project page is at https://paintscene4d.github.io/


### Negative Token Merging: Image-based Adversarial Feature Guidance
**Authors**: Jaskirat Singh, Lindsey Li, Weijia Shi, Ranjay Krishna, Yejin Choi, Pang Wei Koh, Michael F. Cohen, Stephen Gould, Liang Zheng, Luke Zettlemoyer

**Published Date**: 2024-12-02

**Updated Date**: 2024-12-05

**PDF Url**: [2412.01339v2](http://arxiv.org/pdf/2412.01339v2)

**Abstract**: Text-based adversarial guidance using a negative prompt has emerged as a
widely adopted approach to steer diffusion models away from producing undesired
concepts. While useful, performing adversarial guidance using text alone can be
insufficient to capture complex visual concepts or avoid specific visual
elements like copyrighted characters. In this paper, for the first time we
explore an alternate modality in this direction by performing adversarial
guidance directly using visual features from a reference image or other images
in a batch. We introduce negative token merging (NegToMe), a simple but
effective training-free approach which performs adversarial guidance through
images by selectively pushing apart matching visual features between reference
and generated images during the reverse diffusion process. By simply adjusting
the used reference, NegToMe enables a diverse range of applications. Notably,
when using other images in same batch as reference, we find that NegToMe
significantly enhances output diversity (e.g., racial, gender, visual) by
guiding features of each image away from others. Similarly, when used w.r.t.
copyrighted reference images, NegToMe reduces visual similarity to copyrighted
content by 34.57%. NegToMe is simple to implement using just few-lines of code,
uses only marginally higher (<4%) inference time and is compatible with
different diffusion architectures, including those like Flux, which don't
natively support the use of a negative prompt. Code is available at
https://negtome.github.io


### Learning to Reconstruct Accelerated MRI Through K-space Cold Diffusion without Noise
**Authors**: Guoyao Shen, Mengyu Li, Chad W. Farris, Stephan Anderson, Xin Zhang

**Published Date**: 2023-11-16

**Updated Date**: 2024-12-05

**PDF Url**: [2311.10162v3](http://arxiv.org/pdf/2311.10162v3)

**Abstract**: Deep learning-based MRI reconstruction models have achieved superior
performance these days. Most recently, diffusion models have shown remarkable
performance in image generation, in-painting, super-resolution, image editing
and more. As a generalized diffusion model, cold diffusion further broadens the
scope and considers models built around arbitrary image transformations such as
blurring, down-sampling, etc. In this paper, we propose a k-space cold
diffusion model that performs image degradation and restoration in k-space
without the need for Gaussian noise. We provide comparisons with multiple deep
learning-based MRI reconstruction models and perform tests on a well-known
large open-source MRI dataset. Our results show that this novel way of
performing degradation can generate high-quality reconstruction images for
accelerated MRI.


### GeoPos: A Minimal Positional Encoding for Enhanced Fine-Grained Details in Image Synthesis Using Convolutional Neural Networks
**Authors**: Mehran Hosseini, Peyman Hosseini

**Published Date**: 2024-01-03

**Updated Date**: 2024-12-05

**PDF Url**: [2401.01951v2](http://arxiv.org/pdf/2401.01951v2)

**Abstract**: The enduring inability of image generative models to recreate intricate
geometric features, such as those present in human hands and fingers has been
an ongoing problem in image generation for nearly a decade. While strides have
been made by increasing model sizes and diversifying training datasets, this
issue remains prevalent across all models, from denoising diffusion models to
Generative Adversarial Networks (GAN), pointing to a fundamental shortcoming in
the underlying architectures. In this paper, we demonstrate how this problem
can be mitigated by augmenting convolution layers geometric capabilities
through providing them with a single input channel incorporating the relative
n-dimensional Cartesian coordinate system. We show this drastically improves
quality of images generated by Diffusion Models, GANs, and Variational
AutoEncoders (VAE).


### ActFusion: a Unified Diffusion Model for Action Segmentation and Anticipation
**Authors**: Dayoung Gong, Suha Kwak, Minsu Cho

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.04353v1](http://arxiv.org/pdf/2412.04353v1)

**Abstract**: Temporal action segmentation and long-term action anticipation are two
popular vision tasks for the temporal analysis of actions in videos. Despite
apparent relevance and potential complementarity, these two problems have been
investigated as separate and distinct tasks. In this work, we tackle these two
problems, action segmentation and action anticipation, jointly using a unified
diffusion model dubbed ActFusion. The key idea to unification is to train the
model to effectively handle both visible and invisible parts of the sequence in
an integrated manner; the visible part is for temporal segmentation, and the
invisible part is for future anticipation. To this end, we introduce a new
anticipative masking strategy during training in which a late part of the video
frames is masked as invisible, and learnable tokens replace these frames to
learn to predict the invisible future. Experimental results demonstrate the
bi-directional benefits between action segmentation and anticipation. ActFusion
achieves the state-of-the-art performance across the standard benchmarks of 50
Salads, Breakfast, and GTEA, outperforming task-specific models in both of the
two tasks with a single unified model through joint learning.


## Quantitative Finance
### A Unified Framework for Evaluating the Effectiveness and Enhancing the Transparency of Explainable AI Methods in Real-World Applications
**Authors**: Md. Ariful Islam, M. F. Mridha, Md Abrar Jahin, Nilanjan Dey

**Published Date**: 2024-12-05

**Updated Date**: 2024-12-05

**PDF Url**: [2412.03884v1](http://arxiv.org/pdf/2412.03884v1)

**Abstract**: The rapid advancement of deep learning has resulted in substantial
advancements in AI-driven applications; however, the "black box" characteristic
of these models frequently constrains their interpretability, transparency, and
reliability. Explainable artificial intelligence (XAI) seeks to elucidate AI
decision-making processes, guaranteeing that explanations faithfully represent
the model's rationale and correspond with human comprehension. Despite
comprehensive research in XAI, a significant gap persists in standardized
procedures for assessing the efficacy and transparency of XAI techniques across
many real-world applications. This study presents a unified XAI evaluation
framework incorporating extensive quantitative and qualitative criteria to
systematically evaluate the correctness, interpretability, robustness,
fairness, and completeness of explanations generated by AI models. The
framework prioritizes user-centric and domain-specific adaptations, hence
improving the usability and reliability of AI models in essential domains. To
address deficiencies in existing evaluation processes, we suggest defined
benchmarks and a systematic evaluation pipeline that includes data loading,
explanation development, and thorough method assessment. The suggested
framework's relevance and variety are evidenced by case studies in healthcare,
finance, agriculture, and autonomous systems. These provide a solid basis for
the equitable and dependable assessment of XAI methodologies. This paradigm
enhances XAI research by offering a systematic, flexible, and pragmatic method
to guarantee transparency and accountability in AI systems across many
real-world contexts.


