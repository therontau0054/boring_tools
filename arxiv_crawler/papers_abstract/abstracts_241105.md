# Abstracts of Papers

## Physics
### Data augmentation for the POD formulation of the parametric laminar incompressible Navier-Stokes equations
**Authors**: Alba Muixí, Sergio Zlotnik, Matteo Giacomini, Pedro Díez

**Published Date**: 2023-12-22

**Updated Date**: 2024-11-04

**PDF Url**: [2312.14756v2](http://arxiv.org/pdf/2312.14756v2)

**Abstract**: A posteriori reduced-order models (ROM), e.g. based on proper orthogonal
decomposition (POD), are essential to affordably tackle realistic parametric
problems. They rely on a trustful training set, that is a family of full-order
solutions (snapshots) representative of all possible outcomes of the parametric
problem. Having such a rich collection of snapshots is not, in many cases,
computationally viable. A strategy for data augmentation, designed for
parametric laminar incompressible flows, is proposed to enrich poorly populated
training sets. The goal is to include in the new, artificial snapshots emerging
features, not present in the original basis, that do enhance the quality of the
reduced basis (RB) constructed using POD dimensionality reduction. The
methodologies devised are based on exploiting basic physical principles, such
as mass and momentum conservation, to construct physically-relevant, artificial
snapshots at a fraction of the cost of additional full-order solutions.
Interestingly, the numerical results show that the ideas exploiting only mass
conservation (i.e., incompressibility) are not producing significant added
value with respect to the standard linear combinations of snapshots.
Conversely, accounting for the linearized momentum balance via the Oseen
equation does improve the quality of the resulting approximation and therefore
is an effective data augmentation strategy in the framework of viscous
incompressible laminar flows. Numerical experiments of parametric flow
problems, in two and three dimensions, at low and moderate values of the
Reynolds number are presented to showcase the superior performance of the
data-enriched POD-RB with respect to the standard ROM in terms of both accuracy
and efficiency.


### How Far is Video Generation from World Model: A Physical Law Perspective
**Authors**: Bingyi Kang, Yang Yue, Rui Lu, Zhijie Lin, Yang Zhao, Kaixin Wang, Gao Huang, Jiashi Feng

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02385v1](http://arxiv.org/pdf/2411.02385v1)

**Abstract**: OpenAI's Sora highlights the potential of video generation for developing
world models that adhere to fundamental physical laws. However, the ability of
video generation models to discover such laws purely from visual data without
human priors can be questioned. A world model learning the true law should give
predictions robust to nuances and correctly extrapolate on unseen scenarios. In
this work, we evaluate across three key scenarios: in-distribution,
out-of-distribution, and combinatorial generalization. We developed a 2D
simulation testbed for object movement and collisions to generate videos
deterministically governed by one or more classical mechanics laws. This
provides an unlimited supply of data for large-scale experimentation and
enables quantitative evaluation of whether the generated videos adhere to
physical laws. We trained diffusion-based video generation models to predict
object movements based on initial frames. Our scaling experiments show perfect
generalization within the distribution, measurable scaling behavior for
combinatorial generalization, but failure in out-of-distribution scenarios.
Further experiments reveal two key insights about the generalization mechanisms
of these models: (1) the models fail to abstract general physical rules and
instead exhibit "case-based" generalization behavior, i.e., mimicking the
closest training example; (2) when generalizing to new cases, models are
observed to prioritize different factors when referencing training data: color
> size > velocity > shape. Our study suggests that scaling alone is
insufficient for video generation models to uncover fundamental physical laws,
despite its role in Sora's broader success. See our project page at
https://phyworld.github.io


### LDPC stabilizer codes as gapped quantum phases: stability under graph-local perturbations
**Authors**: Wojciech De Roeck, Vedika Khemani, Yaodong Li, Nicholas O'Dea, Tibor Rakovszky

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02384v1](http://arxiv.org/pdf/2411.02384v1)

**Abstract**: We generalize the proof of stability of topological order, due to Bravyi,
Hastings and Michalakis, to stabilizer Hamiltonians corresponding to
low-density parity check (LDPC) codes without the restriction of geometric
locality in Euclidean space. We consider Hamiltonians $H_0$ defined by
$[[N,K,d]]$ LDPC codes which obey certain topological quantum order conditions:
(i) code distance $d \geq c \log(N)$, implying local indistinguishability of
ground states, and (ii) a mild condition on local and global compatibility of
ground states; these include good quantum LDPC codes, and the toric code on a
hyperbolic lattice, among others. We consider stability under weak
perturbations that are quasi-local on the interaction graph defined by $H_0$,
and which can be represented as sums of bounded-norm terms. As long as the
local perturbation strength is smaller than a finite constant, we show that the
perturbed Hamiltonian has well-defined spectral bands originating from the
$O(1)$ smallest eigenvalues of $H_0$. The band originating from the smallest
eigenvalue has $2^K$ states, is separated from the rest of the spectrum by a
finite energy gap, and has exponentially narrow bandwidth $\delta = C N
e^{-\Theta(d)}$, which is tighter than the best known bounds even in the
Euclidean case. We also obtain that the new ground state subspace is related to
the initial code subspace by a quasi-local unitary, allowing one to relate
their physical properties. Our proof uses an iterative procedure that performs
successive rotations to eliminate non-frustration-free terms in the
Hamiltonian. Our results extend to quantum Hamiltonians built from classical
LDPC codes, which give rise to stable symmetry-breaking phases. These results
show that LDPC codes very generally define stable gapped quantum phases, even
in the non-Euclidean setting, initiating a systematic study of such phases of
matter.


### Amplitudes and Renormalization Group Techniques: A Case Study
**Authors**: Diego Buccio, John F. Donoghue, Roberto Percacci

**Published Date**: 2023-06-30

**Updated Date**: 2024-11-04

**PDF Url**: [2307.00055v3](http://arxiv.org/pdf/2307.00055v3)

**Abstract**: We explore the properties of a simple renormalizable shift symmetric model
with a higher derivative kinetic energy and quartic derivative coupling, that
can serve as a toy model for higher derivative theories of gravity. The
scattering amplitude behaves as in a normal effective field theory below the
threshold for the production of ghosts, but has an unexpectedly soft behavior
above the threshold. The physical running of the parameters is extracted from
the 2-point and 4-point amplitudes. The results are compared to those obtained
by other methods and are found to agree only in limiting cases. We draw several
lessons that may apply also to gravity.


### Neural optical flow for planar and stereo PIV
**Authors**: Andrew I. Masker, Ke Zhou, Joseph P. Molnar, Samuel J. Grauer

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02373v1](http://arxiv.org/pdf/2411.02373v1)

**Abstract**: Neural optical flow (NOF) offers improved accuracy and robustness over
existing OF methods for particle image velocimetry (PIV). Unlike other OF
techniques, which rely on discrete displacement fields, NOF parameterizes the
physical velocity field using a continuous neural-implicit representation. This
formulation enables efficient data assimilation and ensures consistent
regularization across views for stereo PIV. The neural-implicit architecture
provides significant data compression and supports a space-time formulation,
facilitating the analysis of both steady and unsteady flows. NOF incorporates a
differentiable, nonlinear image-warping operator that relates particle motion
to intensity changes between frames. Discrepancies between the advected
intensity field and observed images form the data loss, while soft constraints,
such as Navier-Stokes residuals, enhance accuracy and enable direct pressure
inference from PIV images. Additionally, mass continuity can be imposed as a
hard constraint for both 2D and 3D flows. Implicit regularization is achieved
by tailoring the network's expressivity to match a target flow's spectral
characteristics. Results from synthetic planar and stereo PIV datasets, as well
as experimental planar data, demonstrate NOF's effectiveness compared to
state-of-the-art wavelet-based OF and CC methods. Additionally, we highlight
its potential broader applicability to techniques like background-oriented
schlieren, molecular tagging velocimetry, and other advanced measurement
systems.


### Physically Based Neural Bidirectional Reflectance Distribution Function
**Authors**: Chenliang Zhou, Alejandro Sztrajman, Gilles Rainer, Fangcheng Zhong, Fazilet Gokbudak, Zhilin Guo, Weihao Xia, Rafal Mantiuk, Cengiz Oztireli

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02347v1](http://arxiv.org/pdf/2411.02347v1)

**Abstract**: We introduce the physically based neural bidirectional reflectance
distribution function (PBNBRDF), a novel, continuous representation for
material appearance based on neural fields. Our model accurately reconstructs
real-world materials while uniquely enforcing physical properties for realistic
BRDFs, specifically Helmholtz reciprocity via reparametrization and energy
passivity via efficient analytical integration. We conduct a systematic
analysis demonstrating the benefits of adhering to these physical laws on the
visual quality of reconstructed materials. Additionally, we enhance the color
accuracy of neural BRDFs by introducing chromaticity enforcement supervising
the norms of RGB channels. Through both qualitative and quantitative
experiments on multiple databases of measured real-world BRDFs, we show that
adhering to these physical constraints enables neural fields to more faithfully
and stably represent the original data and achieve higher rendering quality.


### IR and UV limits of CDT and their relations to FRG
**Authors**: Jan Ambjorn, Jakub Gizbert-Studnicki, Andrzej Goerlich, Daniel Nemeth

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02330v1](http://arxiv.org/pdf/2411.02330v1)

**Abstract**: Causal Dynamical Triangulations (CDT) is a lattice theory of quantum gravity.
It is shown how to identify the IR and the UV limits of this lattice theory
with similar limits studied using the continuum, functional renormalization
group (FRG) approach. The main technical tool in this study will be the
so-called two-point function. It will allow us to identify a correlation length
not directly related to the propagation of physical degrees of freedom.


### Defining and Evaluating Physical Safety for Large Language Models
**Authors**: Yung-Chen Tang, Pin-Yu Chen, Tsung-Yi Ho

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02317v1](http://arxiv.org/pdf/2411.02317v1)

**Abstract**: Large Language Models (LLMs) are increasingly used to control robotic systems
such as drones, but their risks of causing physical threats and harm in
real-world applications remain unexplored. Our study addresses the critical gap
in evaluating LLM physical safety by developing a comprehensive benchmark for
drone control. We classify the physical safety risks of drones into four
categories: (1) human-targeted threats, (2) object-targeted threats, (3)
infrastructure attacks, and (4) regulatory violations. Our evaluation of
mainstream LLMs reveals an undesirable trade-off between utility and safety,
with models that excel in code generation often performing poorly in crucial
safety aspects. Furthermore, while incorporating advanced prompt engineering
techniques such as In-Context Learning and Chain-of-Thought can improve safety,
these methods still struggle to identify unintentional attacks. In addition,
larger models demonstrate better safety capabilities, particularly in refusing
dangerous commands. Our findings and benchmark can facilitate the design and
evaluation of physical safety for LLMs. The project page is available at
huggingface.co/spaces/TrustSafeAI/LLM-physical-safety.


### Enhanced non-macrorealism: Extreme violations of Leggett-Garg inequalities for a system evolving under superposition of unitaries
**Authors**: Arijit Chatterjee, H. S. Karthik, T. S. Mahesh, A. R. Usha Devi

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02301v1](http://arxiv.org/pdf/2411.02301v1)

**Abstract**: Quantum theory contravenes classical macrorealism by allowing a system to be
in a superposition of two or more physically distinct states, producing
physical consequences radically different from that of classical physics. We
show that a system, upon subjecting to transform under superposition of unitary
operators, exhibits enhanced non-macrorealistic feature - as quantified by
violation of the Leggett-Garg inequality (LGI) beyond the temporal Tsirelson
bound. Moreover, this superposition of unitaries also provides robustness
against decoherence by allowing the system to violate LGI and thereby retain
its non-macrorealistic behavior for a strikingly longer duration. Using an NMR
register, we experimentally demonstrate the superposition of unitaries with the
help of an ancillary qubit and verify these theoretical predictions.


### ControlSynth Neural ODEs: Modeling Dynamical Systems with Guaranteed Convergence
**Authors**: Wenjie Mei, Dongzhe Zheng, Shihua Li

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02292v1](http://arxiv.org/pdf/2411.02292v1)

**Abstract**: Neural ODEs (NODEs) are continuous-time neural networks (NNs) that can
process data without the limitation of time intervals. They have advantages in
learning and understanding the evolution of complex real dynamics. Many
previous works have focused on NODEs in concise forms, while numerous physical
systems taking straightforward forms, in fact, belong to their more complex
quasi-classes, thus appealing to a class of general NODEs with high scalability
and flexibility to model those systems. This, however, may result in intricate
nonlinear properties. In this paper, we introduce ControlSynth Neural ODEs
(CSODEs). We show that despite their highly nonlinear nature, convergence can
be guaranteed via tractable linear inequalities. In the composition of CSODEs,
we introduce an extra control term for learning the potential simultaneous
capture of dynamics at different scales, which could be particularly useful for
partial differential equation-formulated systems. Finally, we compare several
representative NNs with CSODEs on important physical dynamics under the
inductive biases of CSODEs, and illustrate that CSODEs have better learning and
predictive abilities in these settings.


## Diffusion
### From Imitation to Refinement -- Residual RL for Precise Assembly
**Authors**: Lars Ankile, Anthony Simeonov, Idan Shenfeld, Marcel Torne, Pulkit Agrawal

**Published Date**: 2024-07-23

**Updated Date**: 2024-11-04

**PDF Url**: [2407.16677v2](http://arxiv.org/pdf/2407.16677v2)

**Abstract**: Recent advances in behavior cloning (BC), like action-chunking and diffusion,
have led to impressive progress. Still, imitation alone remains insufficient
for tasks requiring reliable and precise movements, such as aligning and
inserting objects. Our key insight is that chunked BC policies function as
trajectory planners, enabling long-horizon tasks. Conversely, as they execute
action chunks open-loop, they lack the fine-grained reactivity necessary for
reliable execution. Further, we find that the performance of BC policies
saturates despite increasing data. Reinforcement learning (RL) is a natural way
to overcome this, but it is not straightforward to apply directly to
action-chunked models like diffusion policies. We present a simple yet
effective method, ResiP (Residual for Precise Manipulation), that sidesteps
these challenges by augmenting a frozen, chunked BC model with a fully
closed-loop residual policy trained with RL. The residual policy is trained via
on-policy RL, addressing distribution shifts and introducing reactivity without
altering the BC trajectory planner. Evaluation on high-precision manipulation
tasks demonstrates strong performance of ResiP over BC methods and direct RL
fine-tuning. Videos, code, and data are available at
\url{https://residual-assembly.github.io}.


### LayerDAG: A Layerwise Autoregressive Diffusion Model for Directed Acyclic Graph Generation
**Authors**: Mufei Li, Viraj Shitole, Eli Chien, Changhai Man, Zhaodong Wang, Srinivas Sridharan, Ying Zhang, Tushar Krishna, Pan Li

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02322v1](http://arxiv.org/pdf/2411.02322v1)

**Abstract**: Directed acyclic graphs (DAGs) serve as crucial data representations in
domains such as hardware synthesis and compiler/program optimization for
computing systems. DAG generative models facilitate the creation of synthetic
DAGs, which can be used for benchmarking computing systems while preserving
intellectual property. However, generating realistic DAGs is challenging due to
their inherent directional and logical dependencies. This paper introduces
LayerDAG, an autoregressive diffusion model, to address these challenges.
LayerDAG decouples the strong node dependencies into manageable units that can
be processed sequentially. By interpreting the partial order of nodes as a
sequence of bipartite graphs, LayerDAG leverages autoregressive generation to
model directional dependencies and employs diffusion models to capture logical
dependencies within each bipartite graph. Comparative analyses demonstrate that
LayerDAG outperforms existing DAG generative models in both expressiveness and
generalization, particularly for generating large-scale DAGs with up to 400
nodes-a critical scenario for system benchmarking. Extensive experiments on
both synthetic and real-world flow graphs from various computing platforms show
that LayerDAG generates valid DAGs with superior statistical properties and
benchmarking performance. The synthetic DAGs generated by LayerDAG enhance the
training of ML-based surrogate models, resulting in improved accuracy in
predicting performance metrics of real-world DAGs across diverse computing
platforms.


### Grouped Discrete Representation for Object-Centric Learning
**Authors**: Rongzhen Zhao, Vivienne Wang, Juho Kannala, Joni Pajarinen

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02299v1](http://arxiv.org/pdf/2411.02299v1)

**Abstract**: Object-Centric Learning (OCL) can discover objects in images or videos by
simply reconstructing the input. For better object discovery, representative
OCL methods reconstruct the input as its Variational Autoencoder (VAE)
intermediate representation, which suppresses pixel noises and promotes object
separability by discretizing continuous super-pixels with template features.
However, treating features as units overlooks their composing attributes, thus
impeding model generalization; indexing features with scalar numbers loses
attribute-level similarities and differences, thus hindering model convergence.
We propose \textit{Grouped Discrete Representation} (GDR) for OCL. We decompose
features into combinatorial attributes via organized channel grouping, and
compose these attributes into discrete representation via tuple indexes.
Experiments show that our GDR improves both Transformer- and Diffusion-based
OCL methods consistently on various datasets. Visualizations show that our GDR
captures better object separability.


### Hunyuan3D-1.0: A Unified Framework for Text-to-3D and Image-to-3D Generation
**Authors**: Xianghui Yang, Huiwen Shi, Bowen Zhang, Fan Yang, Jiacheng Wang, Hongxu Zhao, Xinhai Liu, Xinzhou Wang, Qingxiang Lin, Jiaao Yu, Lifu Wang, Zhuo Chen, Sicong Liu, Yuhong Liu, Yong Yang, Di Wang, Jie Jiang, Chunchao Guo

**Published Date**: 2024-11-04

**Updated Date**: 2024-11-04

**PDF Url**: [2411.02293v1](http://arxiv.org/pdf/2411.02293v1)

**Abstract**: While 3D generative models have greatly improved artists' workflows, the
existing diffusion models for 3D generation suffer from slow generation and
poor generalization. To address this issue, we propose a two-stage approach
named Hunyuan3D-1.0 including a lite version and a standard version, that both
support text- and image-conditioned generation. In the first stage, we employ a
multi-view diffusion model that efficiently generates multi-view RGB in
approximately 4 seconds. These multi-view images capture rich details of the 3D
asset from different viewpoints, relaxing the tasks from single-view to
multi-view reconstruction. In the second stage, we introduce a feed-forward
reconstruction model that rapidly and faithfully reconstructs the 3D asset
given the generated multi-view images in approximately 7 seconds. The
reconstruction network learns to handle noises and in-consistency introduced by
the multi-view diffusion and leverages the available information from the
condition image to efficiently recover the 3D structure. % Extensive
experimental results demonstrate the effectiveness of Hunyuan3D-1.0 in
generating high-quality 3D assets. Our framework involves the text-to-image
model ~\ie, Hunyuan-DiT, making it a unified framework to support both text-
and image-conditioned 3D generation. Our standard version has $10\times$ more
parameters than our lite and other existing model. Our Hunyuan3D-1.0 achieves
an impressive balance between speed and quality, significantly reducing
generation time while maintaining the quality and diversity of the produced
assets.


### DEFT: Efficient Fine-Tuning of Diffusion Models by Learning the Generalised $h$-transform
**Authors**: Alexander Denker, Francisco Vargas, Shreyas Padhy, Kieran Didi, Simon Mathis, Vincent Dutordoir, Riccardo Barbano, Emile Mathieu, Urszula Julia Komorowska, Pietro Lio

**Published Date**: 2024-06-03

**Updated Date**: 2024-11-04

**PDF Url**: [2406.01781v2](http://arxiv.org/pdf/2406.01781v2)

**Abstract**: Generative modelling paradigms based on denoising diffusion processes have
emerged as a leading candidate for conditional sampling in inverse problems. In
many real-world applications, we often have access to large, expensively
trained unconditional diffusion models, which we aim to exploit for improving
conditional sampling. Most recent approaches are motivated heuristically and
lack a unifying framework, obscuring connections between them. Further, they
often suffer from issues such as being very sensitive to hyperparameters, being
expensive to train or needing access to weights hidden behind a closed API. In
this work, we unify conditional training and sampling using the mathematically
well-understood Doob's h-transform. This new perspective allows us to unify
many existing methods under a common umbrella. Under this framework, we propose
DEFT (Doob's h-transform Efficient FineTuning), a new approach for conditional
generation that simply fine-tunes a very small network to quickly learn the
conditional $h$-transform, while keeping the larger unconditional network
unchanged. DEFT is much faster than existing baselines while achieving
state-of-the-art performance across a variety of linear and non-linear
benchmarks. On image reconstruction tasks, we achieve speedups of up to
1.6$\times$, while having the best perceptual quality on natural images and
reconstruction performance on medical images. Further, we also provide initial
experiments on protein motif scaffolding and outperform reconstruction guidance
methods.


