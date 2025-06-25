# Abstracts of Papers

## Physics
### Radial Attention: $O(n\log n)$ Sparse Attention with Energy Decay for Long Video Generation
**Authors**: Xingyang Li, Muyang Li, Tianle Cai, Haocheng Xi, Shuo Yang, Yujun Lin, Lvmin Zhang, Songlin Yang, Jinbo Hu, Kelly Peng, Maneesh Agrawala, Ion Stoica, Kurt Keutzer, Song Han

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19852v1](http://arxiv.org/pdf/2506.19852v1)

**Abstract**: Recent advances in diffusion models have enabled high-quality video
generation, but the additional temporal dimension significantly increases
computational costs, making training and inference on long videos prohibitively
expensive. In this paper, we identify a phenomenon we term Spatiotemporal
Energy Decay in video diffusion models: post-softmax attention scores diminish
as spatial and temporal distance between tokens increase, akin to the physical
decay of signal or waves over space and time in nature. Motivated by this, we
propose Radial Attention, a scalable sparse attention mechanism with $O(n \log
n)$ complexity that translates energy decay into exponentially decaying compute
density, which is significantly more efficient than standard $O(n^2)$ dense
attention and more expressive than linear attention. Specifically, Radial
Attention employs a simple, static attention mask where each token attends to
spatially nearby tokens, with the attention window size shrinking with temporal
distance. Moreover, it allows pre-trained video diffusion models to extend
their generation length with efficient LoRA-based fine-tuning. Extensive
experiments show that Radial Attention maintains video quality across
Wan2.1-14B, HunyuanVideo, and Mochi 1, achieving up to a 1.9$\times$ speedup
over the original dense attention. With minimal tuning, it enables video
generation up to 4$\times$ longer while reducing training costs by up to
4.4$\times$ compared to direct fine-tuning and accelerating inference by up to
3.7$\times$ compared to dense attention inference.


### Marginally stable Schwarzschild-black-hole-non-minimally-coupled-Proca-field bound-state configurations
**Authors**: Shahar Hod

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19849v1](http://arxiv.org/pdf/2506.19849v1)

**Abstract**: It has recently been revealed that, in curved black-hole spacetimes,
non-minimally coupled massive Proca fields may be characterized by the
existence of poles in their linearized perturbation equations and may therefore
develop exponentially growing instabilities. Interestingly, recent numerical
computations [H. W. Chiang, S. Garcia-Saenz, and A. Sang, arXiv:2504.04779]
have provided compelling evidence that the onset of monopole instabilities in
the composed black-hole-field system is controlled by the dimensionless
physical parameter $\mu r_-$, where $\mu$ is the proper mass of the
non-minimally coupled Proca field and $r_-\equiv (-2\alpha)^{1/3}r_{\text{H}}$
is the radial location of the pole [here $\alpha$ is the non-minimal coupling
parameter of the Einstein-Proca theory and $r_{\text{H}}$ is the radius of the
black-hole horizon]. In the present paper we use {\it analytical} techniques in
order to explore the physical properties of critical (marginally-stable)
composed Schwarzschild-black-hole-nonminimally-coupled-monopole-Proca-field
configurations. In particular, we derive a remarkably compact analytical
formula for the discrete spectrum $\{\mu(r_{\text{H}},r_-;n)
\}^{n=\infty}_{n=1}$ of Proca field masses which characterize the critical
black-hole-monopole-Proca-field configurations in the dimensionless regime
${{r_- -r_{\text{H}}}\over{r_{\text{H}}}}\ll1$ of near-horizon poles. The
physical significance of the analytically derived resonance spectrum stems from
the fact that the critical field mass
$\mu_{\text{c}}\equiv\mu(r_{\text{H}},r_-;n=1)$ marks the onset of
instabilities in the
Schwarzschild-black-hole-nonminimally-coupled-monopole-Proca-field system. In
particular, composed black-hole-linearized-Proca-field configurations in the
small-mass regime $\mu\leq\mu_{\text{c}}$ of the Proca field are stable.


### ManiGaussian++: General Robotic Bimanual Manipulation with Hierarchical Gaussian World Model
**Authors**: Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding, Guoqiang Hu, Yansong Tang, Ziwei Wang

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19842v1](http://arxiv.org/pdf/2506.19842v1)

**Abstract**: Multi-task robotic bimanual manipulation is becoming increasingly popular as
it enables sophisticated tasks that require diverse dual-arm collaboration
patterns. Compared to unimanual manipulation, bimanual tasks pose challenges to
understanding the multi-body spatiotemporal dynamics. An existing method
ManiGaussian pioneers encoding the spatiotemporal dynamics into the visual
representation via Gaussian world model for single-arm settings, which ignores
the interaction of multiple embodiments for dual-arm systems with significant
performance drop. In this paper, we propose ManiGaussian++, an extension of
ManiGaussian framework that improves multi-task bimanual manipulation by
digesting multi-body scene dynamics through a hierarchical Gaussian world
model. To be specific, we first generate task-oriented Gaussian Splatting from
intermediate visual features, which aims to differentiate acting and
stabilizing arms for multi-body spatiotemporal dynamics modeling. We then build
a hierarchical Gaussian world model with the leader-follower architecture,
where the multi-body spatiotemporal dynamics is mined for intermediate visual
representation via future scene prediction. The leader predicts Gaussian
Splatting deformation caused by motions of the stabilizing arm, through which
the follower generates the physical consequences resulted from the movement of
the acting arm. As a result, our method significantly outperforms the current
state-of-the-art bimanual manipulation techniques by an improvement of 20.2% in
10 simulated tasks, and achieves 60% success rate on average in 9 challenging
real-world tasks. Our code is available at
https://github.com/April-Yz/ManiGaussian_Bimanual.


### Inferring Higher-Order Couplings with Neural Networks
**Authors**: Aurélien Decelle, Alfonso de Jesús Navas Gómez, Beatriz Seoane

**Published Date**: 2025-01-10

**Updated Date**: 2025-06-24

**PDF Url**: [2501.06108v3](http://arxiv.org/pdf/2501.06108v3)

**Abstract**: Maximum entropy methods, rooted in the inverse Ising/Potts problem from
statistical physics, are widely used to model pairwise interactions in complex
systems across disciplines such as bioinformatics and neuroscience. While
successful, these approaches often fail to capture higher-order interactions
that are critical for understanding collective behavior. In contrast, modern
machine learning methods can model such interactions, but their
interpretability often comes at a prohibitive computational cost. Restricted
Boltzmann Machines (RBMs) provide a computationally efficient alternative by
encoding statistical correlations through hidden units in a bipartite
architecture. In this work, we introduce a method that maps RBMs onto
generalized Potts models, enabling the systematic extraction of interactions up
to arbitrary order. Leveraging large-$N$ approximations -- made tractable by
the RBM's structure -- we extract effective many-body couplings with minimal
computational effort. We further propose a robust framework for recovering
higher-order interactions in more complex generative models, and introduce a
simple gauge-fixing scheme for the effective Potts representation. Validation
on synthetic data demonstrates accurate recovery of two- and three-body
interactions. Applied to protein sequence data, our method reconstructs contact
maps with high fidelity and outperforms state-of-the-art inverse Potts models.
These results establish RBMs as a powerful and efficient tool for modeling
higher-order structure in high-dimensional categorical data.


### Resonances of recurrence time of monitored quantum walks
**Authors**: Ruoyu Yin, Qingyuan Wang, Sabine Tornow, Eli Barkai

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19832v1](http://arxiv.org/pdf/2506.19832v1)

**Abstract**: The recurrence time is the time a process first returns to its initial state.
Using quantum walks on a graph, the recurrence time is defined through
stroboscopic monitoring of the arrival of the particle to a node of the system.
When the time interval between repeated measurements is tuned in such a way
that eigenvalues of the unitary become degenerate, the mean recurrence time
exhibits resonances. These resonances imply faster mean recurrence times, which
were recorded on quantum computers. The resonance broadening is captured by a
restart uncertainty relation [R. Yin, Q. Wang, S. Tornow, E. Barkai, Proc.
Natl. Acad. Sci. U.S.A. 122, e2402912121 (2025)]. To ensure a comprehensive
analysis, we extend our investigation to include the impact of system size on
the widened resonances, showing how the connectivity and energy spectrum
structure of a system influence the restart uncertainty relation. Breaking the
symmetry of the system, for example time-reversal symmetry breaking with a
magnetic flux applied to a ring, removes the degeneracy of {the eigenvalues of
the unitary}, hence modifying {the mean recurrence time and the widening of the
transitions}, and this effect is studied in detail. The width of resonances
studied here is related to the finite time resolution of relevant experiments
on quantum computers, and to the restart paradigm.19


### Curating art exhibitions using machine learning
**Authors**: Eurico Covas

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19813v1](http://arxiv.org/pdf/2506.19813v1)

**Abstract**: Art curatorship has always been mostly the subjective work of human experts,
who, with extensive knowledge of many and diverse artworks, select a few of
those to present in communal spaces, spaces that evolved into what we now call
art galleries. There are no hard and fast set of rules on how to select these
artworks, given a theme which either is presented to the art curator or
constructed by her/him. Here we present a series of artificial models -- a
total of four related models -- based on machine learning techniques (a subset
of artificial intelligence) that attempt to learn from existing exhibitions
which have been curated by human experts, in order to be able to do similar
curatorship work. We focus exclusively on the last 25 years of past exhibitions
at the Metropolitan Museum of Art in New York, due to the quality of the data
available and the physical and time limitations of our research. Our four
artificial intelligence models achieve a reasonable ability at imitating these
various curators responsible for all those exhibitions, with various degrees of
precision and curatorial coherence. In particular, we can conclude two key
insights: first, that there is sufficient information in these exhibitions to
construct an artificial intelligence model that replicates past exhibitions
with an accuracy well above random choices; second, that using feature
engineering and carefully designing the architecture of modest size models can
make them as good as those using the so-called large language models such as
GPT in a brute force approach. We also believe, based on small attempts to use
the models in out-of-sample experiments, that given more much more data, it
should be possible for these kinds of artificial intelligence agents to be
closer and closer to the aesthetic and curatorial judgment of human art
curators.


### First-Passage Approach to Optimizing Perturbations for Improved Training of Machine Learning Models
**Authors**: Sagi Meir, Tommer D. Keidar, Shlomi Reuveni, Barak Hirshberg

**Published Date**: 2025-02-06

**Updated Date**: 2025-06-24

**PDF Url**: [2502.04121v3](http://arxiv.org/pdf/2502.04121v3)

**Abstract**: Machine learning models have become indispensable tools in applications
across the physical sciences. Their training is often time-consuming, vastly
exceeding the inference timescales. Several protocols have been developed to
perturb the learning process and improve the training, such as shrink and
perturb, warm restarts, and stochastic resetting. For classifiers, these
perturbations have been shown to result in enhanced speedups or improved
generalization. However, the design of such perturbations is usually done ad
hoc by intuition and trial and error. To rationally optimize training
protocols, we frame them as first-passage processes and consider their response
to perturbations. We show that if the unperturbed learning process reaches a
quasi-steady state, the response at a single perturbation frequency can predict
the behavior at a wide range of frequencies. We employ this approach to a
CIFAR-10 classifier using the ResNet-18 model and identify a useful
perturbation and frequency among several possibilities. We demonstrate the
transferability of the approach to other datasets, architectures, optimizers
and even tasks (regression instead of classification). Our work allows
optimization of perturbations for improving the training of machine learning
models using a first-passage approach.


### Convolution-weighting method for the physics-informed neural network: A Primal-Dual Optimization Perspective
**Authors**: Chenhao Si, Ming Yan

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19805v1](http://arxiv.org/pdf/2506.19805v1)

**Abstract**: Physics-informed neural networks (PINNs) are extensively employed to solve
partial differential equations (PDEs) by ensuring that the outputs and
gradients of deep learning models adhere to the governing equations. However,
constrained by computational limitations, PINNs are typically optimized using a
finite set of points, which poses significant challenges in guaranteeing their
convergence and accuracy. In this study, we proposed a new weighting scheme
that will adaptively change the weights to the loss functions from isolated
points to their continuous neighborhood regions. The empirical results show
that our weighting scheme can reduce the relative $L^2$ errors to a lower
value.


### Chimera baryons and mesons on the lattice: a spectral density analysis
**Authors**: Ed Bennett, Luigi Del Debbio, Niccolò Forzano, Ryan Hill, Deog Ki Hong, Ho Hsiao, Jong-Wan Lee, C. -J. David Lin, Biagio Lucini, Alessandro Lupo, Maurizio Piai, Davide Vadacchino, Fabian Zierler

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19804v1](http://arxiv.org/pdf/2506.19804v1)

**Abstract**: We develop and test a spectral-density analysis method, based on the
introduction of smeared energy kernels, to extract physical information from
two-point correlation functions computed numerically in lattice field theory.
We apply it to a $Sp(4)$ gauge theory and fermion matter fields transforming in
distinct representations, with $N_{\rm f}=2$ Dirac fermions in the fundamental
and $N_{\rm as}=3$ in the 2-index antisymmetric representation. The
corresponding continuum theory provides the minimal candidate model for a
composite Higgs boson with partial top compositeness. We consider a broad class
of composite operators, that source flavored mesons and (chimera) baryons, for
several finite choices of lattice bare parameters. For the chimera baryons,
which include candidate top-quark partners, we provide the first measurements,
obtained with dynamical fermions, of the ground state and the lowest excited
state masses, in all channels of spin, isospin, and parity. We also measure
matrix elements and overlap factors, that are important to realize viable
models of partial top compositeness, by implementing an innovative way of
extracting this information from the spectral densities. For the mesons, among
which the pseudoscalars can be reinterpreted to provide an extension of the
Higgs sector of the Standard Model of particle physics, our measurements of the
renormalized matrix elements and decay constants are new results. We complement
them with an update of existing measurements of the meson masses, obtained with
higher statistics and improved analysis. The analysis software is made publicly
available, and can be used in other lattice studies, including application to
quantum chromodynamics (QCD).


### Noncontextual Pauli Hamiltonians
**Authors**: Alexis Ralli, Tim Weaving, Peter J. Love

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19778v1](http://arxiv.org/pdf/2506.19778v1)

**Abstract**: Contextuality is a key feature of quantum mechanics, and identification of
noncontextual subtheories of quantum mechanics is of both fundamental and
practical importance. Recently, noncontextual Pauli Hamiltonians have been
defined in the setting of variational quantum algorithms. In this work we
rigorously establish a number of properties of noncontextual Pauli
Hamiltonians. We prove that these Hamiltonians can be composed of more Pauli
operators than diagonal Hamiltonians. This establishes that noncontextual
Hamiltonians are able to describe a greater number of physical interactions. We
then show that the eigenspaces admit an efficient classical description. We
analyse the eigenspace of these Hamiltonians and prove that for every
eigenvalue there exists an associated eigenvector whose stabilizer rank scales
linearly with the number of qubits. We prove that further structure in these
Hamiltonians allow us to derive where degeneracies in the eigenspectrum can
arise. We thus open the field to a new class of efficiently simulatable states.


## Diffusion
### Improving Progressive Generation with Decomposable Flow Matching
**Authors**: Moayed Haji-Ali, Willi Menapace, Ivan Skorokhodov, Arpit Sahni, Sergey Tulyakov, Vicente Ordonez, Aliaksandr Siarohin

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19839v1](http://arxiv.org/pdf/2506.19839v1)

**Abstract**: Generating high-dimensional visual modalities is a computationally intensive
task. A common solution is progressive generation, where the outputs are
synthesized in a coarse-to-fine spectral autoregressive manner. While diffusion
models benefit from the coarse-to-fine nature of denoising, explicit
multi-stage architectures are rarely adopted. These architectures have
increased the complexity of the overall approach, introducing the need for a
custom diffusion formulation, decomposition-dependent stage transitions,
add-hoc samplers, or a model cascade. Our contribution, Decomposable Flow
Matching (DFM), is a simple and effective framework for the progressive
generation of visual media. DFM applies Flow Matching independently at each
level of a user-defined multi-scale representation (such as Laplacian pyramid).
As shown by our experiments, our approach improves visual quality for both
images and videos, featuring superior results compared to prior multistage
frameworks. On Imagenet-1k 512px, DFM achieves 35.2% improvements in FDD scores
over the base architecture and 26.4% over the best-performing baseline, under
the same training compute. When applied to finetuning of large models, such as
FLUX, DFM shows faster convergence speed to the training distribution.
Crucially, all these advantages are achieved with a single model, architectural
simplicity, and minimal modifications to existing training pipelines.


### Machine Learning with Privacy for Protected Attributes
**Authors**: Saeed Mahloujifar, Chuan Guo, G. Edward Suh, Kamalika Chaudhuri

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19836v1](http://arxiv.org/pdf/2506.19836v1)

**Abstract**: Differential privacy (DP) has become the standard for private data analysis.
Certain machine learning applications only require privacy protection for
specific protected attributes. Using naive variants of differential privacy in
such use cases can result in unnecessary degradation of utility. In this work,
we refine the definition of DP to create a more general and flexible framework
that we call feature differential privacy (FDP). Our definition is
simulation-based and allows for both addition/removal and replacement variants
of privacy, and can handle arbitrary and adaptive separation of protected and
non-protected features. We prove the properties of FDP, such as adaptive
composition, and demonstrate its implications for limiting attribute inference
attacks. We also propose a modification of the standard DP-SGD algorithm that
satisfies FDP while leveraging desirable properties such as amplification via
sub-sampling. We apply our framework to various machine learning tasks and show
that it can significantly improve the utility of DP-trained models when public
features are available. For example, we train diffusion models on the AFHQ
dataset of animal faces and observe a drastic improvement in FID compared to
DP, from 286.7 to 101.9 at $\epsilon=8$, assuming that the blurred version of a
training image is available as a public feature. Overall, our work provides a
new approach to private data analysis that can help reduce the utility cost of
DP while still providing strong privacy guarantees.


### ProxelGen: Generating Proteins as 3D Densities
**Authors**: Felix Faltings, Hannes Stark, Regina Barzilay, Tommi Jaakkola

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19820v1](http://arxiv.org/pdf/2506.19820v1)

**Abstract**: We develop ProxelGen, a protein structure generative model that operates on
3D densities as opposed to the prevailing 3D point cloud representations.
Representing proteins as voxelized densities, or proxels, enables new tasks and
conditioning capabilities. We generate proteins encoded as proxels via a 3D
CNN-based VAE in conjunction with a diffusion model operating on its latent
space. Compared to state-of-the-art models, ProxelGen's samples achieve higher
novelty, better FID scores, and the same level of designability as the training
set. ProxelGen's advantages are demonstrated in a standard motif scaffolding
benchmark, and we show how 3D density-based generation allows for more flexible
shape conditioning.


### Alleviating User-Sensitive bias with Fair Generative Sequential Recommendation Model
**Authors**: Yang Liu, Feng Wu, Xuefang Zhu

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19777v1](http://arxiv.org/pdf/2506.19777v1)

**Abstract**: Recommendation fairness has recently attracted much attention. In the real
world, recommendation systems are driven by user behavior, and since users with
the same sensitive feature (e.g., gender and age) tend to have the same
patterns, recommendation models can easily capture the strong correlation
preference of sensitive features and thus cause recommendation unfairness.
Diffusion model (DM) as a new generative model paradigm has achieved great
success in recommendation systems. DM's ability to model uncertainty and
represent diversity, and its modeling mechanism has a high degree of
adaptability with the real-world recommendation process with bias. Therefore,
we use DM to effectively model the fairness of recommendation and enhance the
diversity. This paper proposes a FairGENerative sequential Recommendation model
based on DM, FairGENRec. In the training phase, we inject random noise into the
original distribution under the guidance of the sensitive feature recognition
model, and a sequential denoise model is designed for the reverse
reconstruction of items. Simultaneously, recommendation fairness modeling is
completed by injecting multi-interests representational information that
eliminates the bias of sensitive user features into the generated results. In
the inference phase, the model obtains the noise in the form of noise addition
by using the history interactions which is followed by reverse iteration to
reconstruct the target item representation. Finally, our extensive experiments
on three datasets demonstrate the dual enhancement effect of FairGENRec on
accuracy and fairness, while the statistical analysis of the cases visualizes
the degree of improvement on the fairness of the recommendation.


### Kling-Foley: Multimodal Diffusion Transformer for High-Quality Video-to-Audio Generation
**Authors**: Jun Wang, Xijuan Zeng, Chunyu Qiang, Ruilong Chen, Shiyao Wang, Le Wang, Wangjing Zhou, Pengfei Cai, Jiahui Zhao, Nan Li, Zihan Li, Yuzhe Liang, Xiaopeng Wang, Haorui Zheng, Ming Wen, Kang Yin, Yiran Wang, Nan Li, Feng Deng, Liang Dong, Chen Zhang, Di Zhang, Kun Gai

**Published Date**: 2025-06-24

**Updated Date**: 2025-06-24

**PDF Url**: [2506.19774v1](http://arxiv.org/pdf/2506.19774v1)

**Abstract**: We propose Kling-Foley, a large-scale multimodal Video-to-Audio generation
model that synthesizes high-quality audio synchronized with video content. In
Kling-Foley, we introduce multimodal diffusion transformers to model the
interactions between video, audio, and text modalities, and combine it with a
visual semantic representation module and an audio-visual synchronization
module to enhance alignment capabilities. Specifically, these modules align
video conditions with latent audio elements at the frame level, thereby
improving semantic alignment and audio-visual synchronization. Together with
text conditions, this integrated approach enables precise generation of
video-matching sound effects. In addition, we propose a universal latent audio
codec that can achieve high-quality modeling in various scenarios such as sound
effects, speech, singing, and music. We employ a stereo rendering method that
imbues synthesized audio with a spatial presence. At the same time, in order to
make up for the incomplete types and annotations of the open-source benchmark,
we also open-source an industrial-level benchmark Kling-Audio-Eval. Our
experiments show that Kling-Foley trained with the flow matching objective
achieves new audio-visual SOTA performance among public models in terms of
distribution matching, semantic alignment, temporal alignment and audio
quality.


