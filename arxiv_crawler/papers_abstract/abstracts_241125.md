# Abstracts of Papers

## Physics
### Constructions and performance of hyperbolic and semi-hyperbolic Floquet codes
**Authors**: Oscar Higgott, Nikolas P. Breuckmann

**Published Date**: 2023-08-07

**Updated Date**: 2024-11-22

**PDF Url**: [2308.03750v2](http://arxiv.org/pdf/2308.03750v2)

**Abstract**: We construct families of Floquet codes derived from colour code tilings of
closed hyperbolic surfaces. These codes have weight-two check operators, a
finite encoding rate and can be decoded efficiently with minimum-weight perfect
matching. We also construct semi-hyperbolic Floquet codes, which have improved
distance scaling, and are obtained via a fine-graining procedure. Using a
circuit-based noise model that assumes direct two-qubit measurements, we show
that semi-hyperbolic Floquet codes can be $48\times$ more efficient than planar
honeycomb codes and therefore over $100\times$ more efficient than alternative
compilations of the surface code to two-qubit measurements, even at physical
error rates of $0.3\%$ to $1\%$. We further demonstrate that semi-hyperbolic
Floquet codes can have a teraquop footprint of only 32 physical qubits per
logical qubit at a noise strength of $0.1\%$. For standard circuit-level
depolarising noise at $p=0.1\%$, we find a $30\times$ improvement over planar
honeycomb codes and a $5.6\times$ improvement over surface codes. Finally, we
analyse small instances that are amenable to near-term experiments, including a
Floquet code derived from the Bolza surface that encodes four logical qubits
into 16 physical qubits.


### Learnable Activation Functions in Physics-Informed Neural Networks for Solving Partial Differential Equations
**Authors**: Afrah Fareaa, Mustafa Serdar Celebi

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15111v1](http://arxiv.org/pdf/2411.15111v1)

**Abstract**: We investigate the use of learnable activation functions in Physics-Informed
Neural Networks (PINNs) for solving Partial Differential Equations (PDEs).
Specifically, we compare the efficacy of traditional Multilayer Perceptrons
(MLPs) with fixed and learnable activations against Kolmogorov-Arnold Networks
(KANs), which employ learnable basis functions. Physics-informed neural
networks (PINNs) have emerged as an effective method for directly incorporating
physical laws into the learning process, offering a data-efficient solution for
both the forward and inverse problems associated with PDEs. However, challenges
such as effective training and spectral bias, where low-frequency components
are learned more effectively, often limit their applicability to problems
characterized by rapid oscillations or sharp transitions. By employing
different activation or basis functions on MLP and KAN, we assess their impact
on convergence behavior and spectral bias mitigation, and the accurate
approximation of PDEs. The findings offer insights into the design of neural
network architectures that balance training efficiency, convergence speed, and
test accuracy for PDE solvers. By evaluating the influence of activation or
basis function choices, this work provides guidelines for developing more
robust and accurate PINN models. The source code and pre-trained models used in
this study are made publicly available to facilitate reproducibility and future
exploration.


### Anomalous Dimensions via on-shell Methods: Operator Mixing and Leading Mass Effects
**Authors**: L. C. Bresciani, G. Levati, P. Mastrolia, P. Paradisi

**Published Date**: 2023-12-08

**Updated Date**: 2024-11-22

**PDF Url**: [2312.05206v2](http://arxiv.org/pdf/2312.05206v2)

**Abstract**: We elaborate on the application of on-shell and unitarity-based methods for
evaluating renormalization group coefficients, and generalize this framework to
account for the mixing of operators with different dimensions and leading mass
effects. We derive a master formula for anomalous dimensions stemming from the
general structure of operator mixings, up to two-loop order, and show how the
Higgs low-energy theorem can be exploited to include leading mass effects. A
few applications on the renormalization properties of popular effective field
theories showcase the strength of the proposed approach, which drastically
reduces the complexity of standard loop calculations. Our results provide a
powerful tool to interpret experimental measurements of low-energy observables,
such as flavor violating processes or electric and magnetic dipole moments, as
induced by new physics emerging above the electroweak scale.


### Investigation of pion-nucleon contributions to nucleon matrix elements
**Authors**: Constantia Alexandrou, Giannis Koutsou, Yan Li, Marcus Petschlies, Ferenc Pittler

**Published Date**: 2024-08-07

**Updated Date**: 2024-11-22

**PDF Url**: [2408.03893v2](http://arxiv.org/pdf/2408.03893v2)

**Abstract**: We investigate contributions of excited states to nucleon matrix elements
computed in lattice QCD by employing, in addition to the standard nucleon
interpolating operator, pion-nucleon ($\pi$-$N$) operators. We solve a
generalized eigenvalue problem (GEVP) to obtain an optimal interpolating
operator that minimizes overlap with the $\pi$-$N$ states. We derive a variant
of the standard application of the GEVP method, which allows for constructing
3-point correlation functions using the optimized interpolating operator
without requiring the computationally demanding combination that includes
$\pi$-$N$ operators in both sink and source. We extract nucleon matrix elements
using two twisted mass fermion ensembles, one ensemble generated using pion
mass of 346 MeV and one ensemble tuned to reproduce the physical value of the
pion mass. Especially, we determine the isoscalar and isovector scalar,
pseudoscalar, vector, axial, and tensor matrix elements. We include results
obtained using a range of kinematic setups, including momentum in the sink. Our
results using this variational approach are compared with previous results
obtained using the same ensembles and multi-state fits without GEVP
improvement. We find that for the physical mass point ensemble, the
improvement, in terms of suppression of excited states using this method, is
most significant for the case of the matrix elements of the isovector axial and
pseudoscalar currents.


### What You See is Not What You Get: Neural Partial Differential Equations and The Illusion of Learning
**Authors**: Arvind Mohan, Ashesh Chattopadhyay, Jonah Miller

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15101v1](http://arxiv.org/pdf/2411.15101v1)

**Abstract**: Differentiable Programming for scientific machine learning (SciML) has
recently seen considerable interest and success, as it directly embeds neural
networks inside PDEs, often called as NeuralPDEs, derived from first principle
physics. Therefore, there is a widespread assumption in the community that
NeuralPDEs are more trustworthy and generalizable than black box models.
However, like any SciML model, differentiable programming relies predominantly
on high-quality PDE simulations as "ground truth" for training. However,
mathematics dictates that these are only discrete numerical approximations of
the true physics. Therefore, we ask: Are NeuralPDEs and differentiable
programming models trained on PDE simulations as physically interpretable as we
think? In this work, we rigorously attempt to answer these questions, using
established ideas from numerical analysis, experiments, and analysis of model
Jacobians. Our study shows that NeuralPDEs learn the artifacts in the
simulation training data arising from the discretized Taylor Series truncation
error of the spatial derivatives. Additionally, NeuralPDE models are
systematically biased, and their generalization capability is likely enabled by
a fortuitous interplay of numerical dissipation and truncation error in the
training dataset and NeuralPDE, which seldom happens in practical applications.
This bias manifests aggressively even in relatively accessible 1-D equations,
raising concerns about the veracity of differentiable programming on complex,
high-dimensional, real-world PDEs, and in dataset integrity of foundation
models. Further, we observe that the initial condition constrains the
truncation error in initial-value problems in PDEs, thereby exerting
limitations to extrapolation. Finally, we demonstrate that an eigenanalysis of
model weights can indicate a priori if the model will be inaccurate for
out-of-distribution testing.


### Towards quantum simulation of lower-dimensional supersymmetric lattice models
**Authors**: Emanuele Mendicelli, David Schaich

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15083v1](http://arxiv.org/pdf/2411.15083v1)

**Abstract**: Supersymmetric models are grounded in the intriguing concept of a
hypothetical symmetry that relates bosonic and fermionic particles. This
symmetry has profound implications, offering valuable extensions to the
Standard Model of particle physics and fostering connections to theories of
quantum gravity. However, lattice studies exploring the non-perturbative
features of these models, such as spontaneous supersymmetry breaking and
real-time evolution encounter significant challenges, particularly due to the
infamous sign problem.
  The sign problem obstructs simulations on classical computers, especially
when dealing with high-dimensional lattice systems. While one potential
solution is to adopt the Hamiltonian formalism, this approach necessitates an
exponential increase in classical resources with the number of lattice sites
and degrees of freedom, rendering it impractical for large systems. In
contrast, quantum hardware offers a promising alternative, as it requires in
principle a polynomial amount of resources, making the study of these models
more accessible.
  In this context, we explore the encoding of lower-dimensional supersymmetric
quantum mechanics onto qubits. We also highlight our ongoing efforts to
implement and check the model supersymmetry breaking on an IBM gate-based
quantum simulator with and without shot noise, addressing the technical
challenges we face and the potential implications of our findings for advancing
our understanding of supersymmetry.


### Simulation of the Dissipative Dynamics of Strongly Interacting NV Centers with Tensor Networks
**Authors**: Jirawat Saiphet, Daniel Braun

**Published Date**: 2024-06-12

**Updated Date**: 2024-11-22

**PDF Url**: [2406.08108v2](http://arxiv.org/pdf/2406.08108v2)

**Abstract**: NV centers in diamond are a promising platform for highly sensitive quantum
sensors for magnetic fields and other physical quantities. The quest for high
sensitivity combined with high spatial resolution leads naturally to dense
ensembles of NV centers, and hence to strong, long-range interactions between
them. Hence, simulating strongly interacting NVs becomes essential. However,
obtaining the exact dynamics for a many-spin system is a challenging task due
to the exponential scaling of the Hilbert space dimension, a problem that is
exacerbated when the system is modelled as an open quantum system. In this
work, we employ the Matrix Product Density Operator (MPDO) method to represent
the many-body mixed state and to simulate the dynamics of an ensemble of NVs in
the presence of strong long-range couplings due to dipole-dipole forces. We
benchmark different time-evolution algorithms in terms of numerical accuracy
and stability against time evolution based on exact numerical diagonalization.
Subsequently, we simulate the dynamics in the strong interaction regime, and
study the impact of decoherence on the accuracy of the MPDO method. Lastly, we
investigate the dynamics of quantum Fisher information and discuss under what
circumstances a strong interaction can improve sensitivity for magnetic field
sensing.


### One-loop integrability with shifting masses
**Authors**: Matheus Fabri, Davide Polvara

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15080v1](http://arxiv.org/pdf/2411.15080v1)

**Abstract**: We investigate the perturbative integrability of two-dimensional massive
quantum field theories with polynomial-like interactions and show that any
theory of such class which is purely elastic at the tree level is also purely
elastic at one loop. To preserve the elasticity, the physical renormalized
masses of the theory must differ from the classical ones by quantum corrections
carried by one-loop bubble diagrams. After the masses are corrected in this
manner we show that one-loop inelastic processes vanish and integrability is
preserved under one-loop effects. Relying on this fact we show that the closed
expression for one-loop S-matrices in terms of tree S-matrices obtained in
arXiv:2402.12087 extends to models that do not preserve the mass ratios at one
loop. We test our results on the full class of nonsimply-laced affine Toda
theories and find exact match with the S-matrices bootstrapped in the past.


### Single color digital H&E staining with In-and-Out Net
**Authors**: Mengkun Chen, Yen-Tung Liu, Fadeel Sher Khan, Matthew C. Fox, Jason S. Reichenberg, Fabiana C. P. S. Lopes, Katherine R. Sebastian, Mia K. Markey, James W. Tunnell

**Published Date**: 2024-05-22

**Updated Date**: 2024-11-22

**PDF Url**: [2405.13278v2](http://arxiv.org/pdf/2405.13278v2)

**Abstract**: Virtual staining streamlines traditional staining procedures by digitally
generating stained images from unstained or differently stained images. While
conventional staining methods involve time-consuming chemical processes,
virtual staining offers an efficient and low infrastructure alternative.
Leveraging microscopy-based techniques, such as confocal microscopy,
researchers can expedite tissue analysis without the need for physical
sectioning. However, interpreting grayscale or pseudo-color microscopic images
remains a challenge for pathologists and surgeons accustomed to traditional
histologically stained images. To fill this gap, various studies explore
digitally simulating staining to mimic targeted histological stains. This paper
introduces a novel network, In-and-Out Net, specifically designed for virtual
staining tasks. Based on Generative Adversarial Networks (GAN), our model
efficiently transforms Reflectance Confocal Microscopy (RCM) images into
Hematoxylin and Eosin (H&E) stained images. We enhance nuclei contrast in RCM
images using aluminum chloride preprocessing for skin tissues. Training the
model with virtual H\&E labels featuring two fluorescence channels eliminates
the need for image registration and provides pixel-level ground truth. Our
contributions include proposing an optimal training strategy, conducting a
comparative analysis demonstrating state-of-the-art performance, validating the
model through an ablation study, and collecting perfectly matched input and
ground truth images without registration. In-and-Out Net showcases promising
results, offering a valuable tool for virtual staining tasks and advancing the
field of histological image analysis.


### Geometric phase and holonomy in the space of 2-by-2 symmetric operators
**Authors**: Jakub Rondomanski, José D. Cojal González, Jürgen P. Rabe, Carlos-Andres Palma, Konrad Polthier

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15038v1](http://arxiv.org/pdf/2411.15038v1)

**Abstract**: We present a non-trivial metric tensor field on the space of 2-by-2
real-valued, symmetric matrices whose Levi-Civita connection renders frames of
eigenvectors parallel. This results in fundamental reimagining of the space of
symmetric matrices as a curved manifold (rather than a flat vector space) and
reduces the computation of eigenvectors of one-parameter-families of matrices
to a single computation of eigenvectors at an initial point, while the rest are
obtained by the parallel transport ODE. Our work has important applications to
vibrations of physical systems whose topology is directly explained by the
non-trivial holonomy of the spaces of symmetric matrices.


## Diffusion
### VideoRepair: Improving Text-to-Video Generation via Misalignment Evaluation and Localized Refinement
**Authors**: Daeun Lee, Jaehong Yoon, Jaemin Cho, Mohit Bansal

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15115v1](http://arxiv.org/pdf/2411.15115v1)

**Abstract**: Recent text-to-video (T2V) diffusion models have demonstrated impressive
generation capabilities across various domains. However, these models often
generate videos that have misalignments with text prompts, especially when the
prompts describe complex scenes with multiple objects and attributes. To
address this, we introduce VideoRepair, a novel model-agnostic, training-free
video refinement framework that automatically identifies fine-grained
text-video misalignments and generates explicit spatial and textual feedback,
enabling a T2V diffusion model to perform targeted, localized refinements.
VideoRepair consists of four stages: In (1) video evaluation, we detect
misalignments by generating fine-grained evaluation questions and answering
those questions with MLLM. In (2) refinement planning, we identify accurately
generated objects and then create localized prompts to refine other areas in
the video. Next, in (3) region decomposition, we segment the correctly
generated area using a combined grounding module. We regenerate the video by
adjusting the misaligned regions while preserving the correct regions in (4)
localized refinement. On two popular video generation benchmarks (EvalCrafter
and T2V-CompBench), VideoRepair substantially outperforms recent baselines
across various text-video alignment metrics. We provide a comprehensive
analysis of VideoRepair components and qualitative examples.


### Efficient Pruning of Text-to-Image Models: Insights from Pruning Stable Diffusion
**Authors**: Samarth N Ramesh, Zhixue Zhao

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15113v1](http://arxiv.org/pdf/2411.15113v1)

**Abstract**: As text-to-image models grow increasingly powerful and complex, their
burgeoning size presents a significant obstacle to widespread adoption,
especially on resource-constrained devices. This paper presents a pioneering
study on post-training pruning of Stable Diffusion 2, addressing the critical
need for model compression in text-to-image domain. Our study tackles the
pruning techniques for the previously unexplored multi-modal generation models,
and particularly examines the pruning impact on the textual component and the
image generation component separately. We conduct a comprehensive comparison on
pruning the model or the single component of the model in various sparsities.
Our results yield previously undocumented findings. For example, contrary to
established trends in language model pruning, we discover that simple magnitude
pruning outperforms more advanced techniques in text-to-image context.
Furthermore, our results show that Stable Diffusion 2 can be pruned to 38.5%
sparsity with minimal quality loss, achieving a significant reduction in model
size. We propose an optimal pruning configuration that prunes the text encoder
to 47.5% and the diffusion generator to 35%. This configuration maintains image
generation quality while substantially reducing computational requirements. In
addition, our work uncovers intriguing questions about information encoding in
text-to-image models: we observe that pruning beyond certain thresholds leads
to sudden performance drops (unreadable images), suggesting that specific
weights encode critical semantics information. This finding opens new avenues
for future research in model compression, interoperability, and bias
identification in text-to-image models. By providing crucial insights into the
pruning behavior of text-to-image models, our study lays the groundwork for
developing more efficient and accessible AI-driven image generation systems


### AdaFlow: Imitation Learning with Variance-Adaptive Flow-Based Policies
**Authors**: Xixi Hu, Bo Liu, Xingchao Liu, Qiang Liu

**Published Date**: 2024-02-06

**Updated Date**: 2024-11-22

**PDF Url**: [2402.04292v2](http://arxiv.org/pdf/2402.04292v2)

**Abstract**: Diffusion-based imitation learning improves Behavioral Cloning (BC) on
multi-modal decision-making, but comes at the cost of significantly slower
inference due to the recursion in the diffusion process. It urges us to design
efficient policy generators while keeping the ability to generate diverse
actions. To address this challenge, we propose AdaFlow, an imitation learning
framework based on flow-based generative modeling. AdaFlow represents the
policy with state-conditioned ordinary differential equations (ODEs), which are
known as probability flows. We reveal an intriguing connection between the
conditional variance of their training loss and the discretization error of the
ODEs. With this insight, we propose a variance-adaptive ODE solver that can
adjust its step size in the inference stage, making AdaFlow an adaptive
decision-maker, offering rapid inference without sacrificing diversity.
Interestingly, it automatically reduces to a one-step generator when the action
distribution is uni-modal. Our comprehensive empirical evaluation shows that
AdaFlow achieves high performance with fast inference speed.


### OminiControl: Minimal and Universal Control for Diffusion Transformer
**Authors**: Zhenxiong Tan, Songhua Liu, Xingyi Yang, Qiaochu Xue, Xinchao Wang

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15098v1](http://arxiv.org/pdf/2411.15098v1)

**Abstract**: In this paper, we introduce OminiControl, a highly versatile and
parameter-efficient framework that integrates image conditions into pre-trained
Diffusion Transformer (DiT) models. At its core, OminiControl leverages a
parameter reuse mechanism, enabling the DiT to encode image conditions using
itself as a powerful backbone and process them with its flexible multi-modal
attention processors. Unlike existing methods, which rely heavily on additional
encoder modules with complex architectures, OminiControl (1) effectively and
efficiently incorporates injected image conditions with only ~0.1% additional
parameters, and (2) addresses a wide range of image conditioning tasks in a
unified manner, including subject-driven generation and spatially-aligned
conditions such as edges, depth, and more. Remarkably, these capabilities are
achieved by training on images generated by the DiT itself, which is
particularly beneficial for subject-driven generation. Extensive evaluations
demonstrate that OminiControl outperforms existing UNet-based and DiT-adapted
models in both subject-driven and spatially-aligned conditional generation.
Additionally, we release our training dataset, Subjects200K, a diverse
collection of over 200,000 identity-consistent images, along with an efficient
data synthesis pipeline to advance research in subject-consistent generation.


### Leapfrog Latent Consistency Model (LLCM) for Medical Images Generation
**Authors**: Lakshmikar R. Polamreddy, Kalyan Roy, Sheng-Han Yueh, Deepshikha Mahato, Shilpa Kuppili, Jialu Li, Youshan Zhang

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15084v1](http://arxiv.org/pdf/2411.15084v1)

**Abstract**: The scarcity of accessible medical image data poses a significant obstacle in
effectively training deep learning models for medical diagnosis, as hospitals
refrain from sharing their data due to privacy concerns. In response, we
gathered a diverse dataset named MedImgs, which comprises over 250,127 images
spanning 61 disease types and 159 classes of both humans and animals from
open-source repositories. We propose a Leapfrog Latent Consistency Model (LLCM)
that is distilled from a retrained diffusion model based on the collected
MedImgs dataset, which enables our model to generate real-time high-resolution
images. We formulate the reverse diffusion process as a probability flow
ordinary differential equation (PF-ODE) and solve it in latent space using the
Leapfrog algorithm. This formulation enables rapid sampling without
necessitating additional iterations. Our model demonstrates state-of-the-art
performance in generating medical images. Furthermore, our model can be
fine-tuned with any custom medical image datasets, facilitating the generation
of a vast array of images. Our experimental results outperform those of
existing models on unseen dog cardiac X-ray images. Source code is available at
https://github.com/lskdsjy/LeapfrogLCM.


## Quantitative Finance
### A New Way: Kronecker-Factored Approximate Curvature Deep Hedging and its Benefits
**Authors**: Tsogt-Ochir Enkhbayar

**Published Date**: 2024-11-22

**Updated Date**: 2024-11-22

**PDF Url**: [2411.15002v1](http://arxiv.org/pdf/2411.15002v1)

**Abstract**: This paper advances the computational efficiency of Deep Hedging frameworks
through the novel integration of Kronecker-Factored Approximate Curvature
(K-FAC) optimization. While recent literature has established Deep Hedging as a
data-driven alternative to traditional risk management strategies, the
computational burden of training neural networks with first-order methods
remains a significant impediment to practical implementation. The proposed
architecture couples Long Short-Term Memory (LSTM) networks with K-FAC
second-order optimization, specifically addressing the challenges of sequential
financial data and curvature estimation in recurrent networks. Empirical
validation using simulated paths from a calibrated Heston stochastic volatility
model demonstrates that the K-FAC implementation achieves marked improvements
in convergence dynamics and hedging efficacy. The methodology yields a 78.3%
reduction in transaction costs ($t = 56.88$, $p < 0.001$) and a 34.4% decrease
in profit and loss (P&L) variance compared to Adam optimization. Moreover, the
K-FAC-enhanced model exhibits superior risk-adjusted performance with a Sharpe
ratio of 0.0401, contrasting with $-0.0025$ for the baseline model. These
results provide compelling evidence that second-order optimization methods can
materially enhance the tractability of Deep Hedging implementations. The
findings contribute to the growing literature on computational methods in
quantitative finance while highlighting the potential for advanced optimization
techniques to bridge the gap between theoretical frameworks and practical
applications in financial markets.


