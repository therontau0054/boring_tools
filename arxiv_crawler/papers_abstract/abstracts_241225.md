# Abstracts of Papers

## Physics
### Crosscap Quenches and Entanglement Evolution
**Authors**: Zixia Wei, Yasushi Yoneta

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18610v1](http://arxiv.org/pdf/2412.18610v1)

**Abstract**: Understanding the mechanisms by which complex correlations emerge through the
dynamics of quantum many-body systems remains a fundamental challenge in modern
physics. To address this, quench dynamics starting from nonequilibrium states
have been extensively studied, leading to significant progress. In this paper,
we propose a novel quench protocol, termed the ``crosscap quench'', to
investigate how highly structured thermal pure states relax into typical ones.
We begin by analyzing conformal field theories (CFTs) and derive universal
features in the time evolution of entanglement entropy. Furthermore, leveraging
the AdS/CFT correspondence, we study holographic CFTs, providing an
analytically tractable example in chaotic CFTs. Finally, we validate these
findings through numerical simulations in both nonintegrable and integrable
quantum spin systems.


### A Paragraph is All It Takes: Rich Robot Behaviors from Interacting, Trusted LLMs
**Authors**: OpenMind, Shaohong Zhong, Adam Zhou, Boyuan Chen, Homin Luo, Jan Liphardt

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18588v1](http://arxiv.org/pdf/2412.18588v1)

**Abstract**: Large Language Models (LLMs) are compact representations of all public
knowledge of our physical environment and animal and human behaviors. The
application of LLMs to robotics may offer a path to highly capable robots that
perform well across most human tasks with limited or even zero tuning. Aside
from increasingly sophisticated reasoning and task planning, networks of
(suitably designed) LLMs offer ease of upgrading capabilities and allow humans
to directly observe the robot's thinking. Here we explore the advantages,
limitations, and particularities of using LLMs to control physical robots. The
basic system consists of four LLMs communicating via a human language data bus
implemented via web sockets and ROS2 message passing. Surprisingly, rich robot
behaviors and good performance across different tasks could be achieved despite
the robot's data fusion cycle running at only 1Hz and the central data bus
running at the extremely limited rates of the human brain, of around 40 bits/s.
The use of natural language for inter-LLM communication allowed the robot's
reasoning and decision making to be directly observed by humans and made it
trivial to bias the system's behavior with sets of rules written in plain
English. These rules were immutably written into Ethereum, a global, public,
and censorship resistant Turing-complete computer. We suggest that by using
natural language as the data bus among interacting AIs, and immutable public
ledgers to store behavior constraints, it is possible to build robots that
combine unexpectedly rich performance, upgradability, and durable alignment
with humans.


### ReducedLUT: Table Decomposition with "Don't Care" Conditions
**Authors**: Oliver Cassidy, Marta Andronic, Samuel Coward, George A. Constantinides

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18579v1](http://arxiv.org/pdf/2412.18579v1)

**Abstract**: Lookup tables (LUTs) are frequently used to efficiently store arrays of
precomputed values for complex mathematical computations. When used in the
context of neural networks, these functions exhibit a lack of recognizable
patterns which presents an unusual challenge for conventional logic synthesis
techniques. Several approaches are known to break down a single large lookup
table into multiple smaller ones that can be recombined. Traditional methods,
such as plain tabulation, piecewise linear approximation, and multipartite
table methods, often yield inefficient hardware solutions when applied to
LUT-based NNs.
  This paper introduces ReducedLUT, a novel method to reduce the footprint of
the LUTs by injecting don't cares into the compression process. This additional
freedom introduces more self-similarities which can be exploited using known
decomposition techniques. We then demonstrate a particular application to
machine learning; by replacing unobserved patterns within the training data of
neural network models with don't cares, we enable greater compression with
minimal model accuracy degradation. In practice, we achieve up to $1.63\times$
reduction in Physical LUT utilization, with a test accuracy drop of no more
than $0.01$ accuracy points.


### Randomized Benchmarking with Synthetic Quantum Circuits
**Authors**: Yale Fan, Riley Murray, Thaddeus D. Ladd, Kevin Young, Robin Blume-Kohout

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18578v1](http://arxiv.org/pdf/2412.18578v1)

**Abstract**: Randomized benchmarking (RB) comprises a set of mature and widely used
techniques for assessing the quality of operations on a quantum
information-processing system. Modern RB protocols for multiqubit systems
extract physically relevant error rates by exploiting the structure of the
group representation generated by the set of benchmarked operations. However,
existing techniques become prohibitively inefficient for representations that
are highly reducible yet decompose into irreducible subspaces of high
dimension. These situations prevail when benchmarking high-dimensional systems
such as qudits or bosonic modes, where experimental control is limited to
implementing a small subset of all possible unitary operations. In this work,
we introduce a broad framework for enhancing the sample efficiency of RB that
is sufficiently powerful to extend the practical reach of RB beyond the
multiqubit setting. Our strategy, which applies to any benchmarking group, uses
"synthetic" quantum circuits with classical post-processing of both input and
output data to leverage the full structure of reducible superoperator
representations. To demonstrate the efficacy of our approach, we develop a
detailed theory of RB for systems with rotational symmetry. Such systems carry
a natural action of the group $\text{SU}(2)$, and they form the basis for
several novel quantum error-correcting codes. We show that, for experimentally
accessible high-spin systems, synthetic RB protocols can reduce the complexity
of measuring rotationally invariant error rates by more than two orders of
magnitude relative to standard approaches such as character RB.


### Scalable Quantum-Inspired Optimization through Dynamic Qubit Compression
**Authors**: Co Tran, Quoc-Bao Tran, Hy Truong Son, Thang N Dinh

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18571v1](http://arxiv.org/pdf/2412.18571v1)

**Abstract**: Hard combinatorial optimization problems, often mapped to Ising models,
promise potential solutions with quantum advantage but are constrained by
limited qubit counts in near-term devices. We present an innovative
quantum-inspired framework that dynamically compresses large Ising models to
fit available quantum hardware of different sizes. Thus, we aim to bridge the
gap between large-scale optimization and current hardware capabilities. Our
method leverages a physics-inspired GNN architecture to capture complex
interactions in Ising models and accurately predict alignments among
neighboring spins (aka qubits) at ground states. By progressively merging such
aligned spins, we can reduce the model size while preserving the underlying
optimization structure. It also provides a natural trade-off between the
solution quality and size reduction, meeting different hardware constraints of
quantum computing devices. Extensive numerical studies on Ising instances of
diverse topologies show that our method can reduce instance size at multiple
levels with virtually no losses in solution quality on the latest D-wave
quantum annealers.


### Efficient Aircraft Design Optimization Using Multi-Fidelity Models and Multi-fidelity Physics Informed Neural Networks
**Authors**: Apurba Sarker

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18564v1](http://arxiv.org/pdf/2412.18564v1)

**Abstract**: Aircraft design optimization traditionally relies on computationally
expensive simulation techniques such as Finite Element Method (FEM) and Finite
Volume Method (FVM), which, while accurate, can significantly slow down the
design iteration process. The challenge lies in reducing the computational
complexity while maintaining high accuracy for quick evaluations of multiple
design alternatives. This research explores advanced methods, including
surrogate models, reduced-order models (ROM), and multi-fidelity machine
learning techniques, to achieve more efficient aircraft design evaluations.
Specifically, the study investigates the application of Multi-fidelity
Physics-Informed Neural Networks (MPINN) and autoencoders for manifold
alignment, alongside the potential of Generative Adversarial Networks (GANs)
for refining design geometries. Through a proof-of-concept task, the research
demonstrates the ability to predict high-fidelity results from low-fidelity
simulations, offering a path toward faster and more cost effective aircraft
design iterations.


### Spread Complexity of High Energy Neutrino Propagation over Astrophysical Distances
**Authors**: Khushboo Dixit, S. Shajidul Haque, Soebur Razzaque

**Published Date**: 2024-06-11

**Updated Date**: 2024-12-24

**PDF Url**: [2406.07491v2](http://arxiv.org/pdf/2406.07491v2)

**Abstract**: Spread complexity measures the minimized spread of quantum states over all
choices of basis. It generalizes Krylov operator complexity to quantum states
under continuous Hamiltonian evolution. In this paper, we study spread
complexity in the context of high-energy astrophysical neutrinos and propose a
new flavor ratio based on complexity. Our findings indicate that our proposal
might favor an initial ratio of fluxes as $\phi_{\nu_e}^0: \phi_{\nu_\mu}^0:
\phi_{\nu_\tau}^0 = 1:0:0$ over a more generally expected ratio of $1:2:0$,
when the IceCube neutrino observatory achieves its projected sensitivity to
discriminate between flavors. Additionally, complexity-based definitions of
flavor ratios exhibit a slight but nonzero sensitivity to the neutrino mass
ordering, which traditional flavor ratios cannot capture.


### Fano physics behind the N-resonance in graphene
**Authors**: R. O. Kuzian, D. V. Efremov, E. E. Krasovskii

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18561v1](http://arxiv.org/pdf/2412.18561v1)

**Abstract**: Bound states and scattering resonances in the unoccupied continuum of a
two-dimensional crystal predicted in [Phys.Rev. B 87, 041405(R) (2013)] are
considered within an exactly solvable model. A close connection of the observed
resonances with those arising in the Fano theory is revealed. The resonance
occurs when the lateral scattering couples the layer-perpendicular incident
electron wave to a strictly bound state. The coupling strength determines the
location of the pole in the scattering amplitude in the complex energy plane,
which is analytically shown to lead to a characteristic Fano-lineshape of the
energy dependence of the electron transmissivity through the crystal. The
implications for the timing of the resonance scattering are discussed. The
analytical results are illustrated by ab initio calculations for a graphene
monolayer.


### Born-Oppenheimer Renormalization group for High Energy Scattering: the Modified BFKL, or where did it all go?
**Authors**: Haowu Duan, Alex Kovner, Michael Lublinsky

**Published Date**: 2024-12-13

**Updated Date**: 2024-12-24

**PDF Url**: [2412.10560v2](http://arxiv.org/pdf/2412.10560v2)

**Abstract**: We continue exploring the Born-Oppenheimer renormalization group generating
evolution in frequency of physical observables. In this paper we study the
evolution of the total cross section for dilute-dilute scattering retaining
only eikonal emissions. We derive and analyze the analog of the BFKL equation
in this framework. The frequency evolution has a very strong effect on the
solutions of the BO-BFKL equation, slowing down the evolution of the scattering
amplitude in a spectacular fashion: the intercept of the Pomeron is decreased
by about a factor of three relative to the canonical LO BFKL result. The
anomalous dimension is also modified significantly - from the BFKL value of one
it goes down to the negative value of $\approx-0.2$. Introducing saturation
boundary as a proxy for the full saturation dynamics, we find that the
dependence of the saturation momentum on rapidity $\eta$ becomes quite weak
with $Q^2_s\sim e^{a\bar\alpha_s\eta}$ with $a\approx 0.784$ as opposed to the
BFKL value $a=4.88$. Our results underscore the necessity to take into account
the DGLAP effects in the high energy evolution. This is left for future work.


### Post-pandemic social contacts in Italy: implications for social distancing measures on in-person school and work attendance
**Authors**: Lorenzo Lucchini, Valentina Marziano, Filippo Trentini, Chiara Chiavenna, Elena D'Agnese, Vittoria Offeddu, Mattia Manica, Piero Poletti, Duilio Balsamo, Giorgio Guzzetta, Marco Aielli, Alessia Melegaro, Stefano Merler

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18549v1](http://arxiv.org/pdf/2412.18549v1)

**Abstract**: The collection of updated data on social contact patterns following the
COVID-19 pandemic disruptions is crucial for future epidemiological assessments
and evaluating non-pharmaceutical interventions (NPIs) based on physical
distancing. We conducted two waves of an online survey in March 2022 and March
2023 in Italy, gathering data from a representative population sample on direct
(verbal/physical interactions) and indirect (prolonged co-location in indoor
spaces) contacts. Using a generalized linear mixed model, we examined
determinants of individuals' total social contacts and evaluated the potential
impact of work-from-home and distance learning on the transmissibility of
respiratory pathogens. In-person attendance at work or school emerged as a
primary driver of social contacts. Adults attending in person reported a mean
of 1.69 (95% CI: 1.56-1.84) times the contacts of those staying home; among
children and adolescents, this ratio increased to 2.38 (95% CI: 1.98-2.87). We
estimated that suspending all non-essential work alone would marginally reduce
transmissibility. However, combining distance learning for all education levels
with work-from-home policies could decrease transmissibility by up to 23.7%
(95% CI: 18.2%-29.0%). Extending these measures to early childcare services
would yield only minimal additional benefits. These results provide useful data
for modelling the transmission of respiratory pathogens in Italy after the end
of the COVID-19 emergency. They also provide insights into the potential
epidemiological effectiveness of social distancing interventions targeting work
and school attendance, supporting considerations on the balance between the
expected benefits and their heavy societal costs.


## Diffusion
### DiTCtrl: Exploring Attention Control in Multi-Modal Diffusion Transformer for Tuning-Free Multi-Prompt Longer Video Generation
**Authors**: Minghong Cai, Xiaodong Cun, Xiaoyu Li, Wenze Liu, Zhaoyang Zhang, Yong Zhang, Ying Shan, Xiangyu Yue

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18597v1](http://arxiv.org/pdf/2412.18597v1)

**Abstract**: Sora-like video generation models have achieved remarkable progress with a
Multi-Modal Diffusion Transformer MM-DiT architecture. However, the current
video generation models predominantly focus on single-prompt, struggling to
generate coherent scenes with multiple sequential prompts that better reflect
real-world dynamic scenarios. While some pioneering works have explored
multi-prompt video generation, they face significant challenges including
strict training data requirements, weak prompt following, and unnatural
transitions. To address these problems, we propose DiTCtrl, a training-free
multi-prompt video generation method under MM-DiT architectures for the first
time. Our key idea is to take the multi-prompt video generation task as
temporal video editing with smooth transitions. To achieve this goal, we first
analyze MM-DiT's attention mechanism, finding that the 3D full attention
behaves similarly to that of the cross/self-attention blocks in the UNet-like
diffusion models, enabling mask-guided precise semantic control across
different prompts with attention sharing for multi-prompt video generation.
Based on our careful design, the video generated by DiTCtrl achieves smooth
transitions and consistent object motion given multiple sequential prompts
without additional training. Besides, we also present MPVBench, a new benchmark
specially designed for multi-prompt video generation to evaluate the
performance of multi-prompt generation. Extensive experiments demonstrate that
our method achieves state-of-the-art performance without additional training.


### Resolution-Robust 3D MRI Reconstruction with 2D Diffusion Priors: Diverse-Resolution Training Outperforms Interpolation
**Authors**: Anselm Krainovic, Stefan Ruschke, Reinhard Heckel

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18584v1](http://arxiv.org/pdf/2412.18584v1)

**Abstract**: Deep learning-based 3D imaging, in particular magnetic resonance imaging
(MRI), is challenging because of limited availability of 3D training data.
Therefore, 2D diffusion models trained on 2D slices are starting to be
leveraged for 3D MRI reconstruction. However, as we show in this paper,
existing methods pertain to a fixed voxel size, and performance degrades when
the voxel size is varied, as it is often the case in clinical practice. In this
paper, we propose and study several approaches for resolution-robust 3D MRI
reconstruction with 2D diffusion priors. As a result of this investigation, we
obtain a simple resolution-robust variational 3D reconstruction approach based
on diffusion-guided regularization of randomly sampled 2D slices. This method
provides competitive reconstruction quality compared to posterior sampling
baselines. Towards resolving the sensitivity to resolution-shifts, we
investigate state-of-the-art model-based approaches including Gaussian
splatting, neural representations, and infinite-dimensional diffusion models,
as well as a simple data-centric approach of training the diffusion model on
several resolutions. Our experiments demonstrate that the model-based
approaches fail to close the performance gap in 3D MRI. In contrast, the
data-centric approach of training the diffusion model on various resolutions
effectively provides a resolution-robust method without compromising accuracy.


### CognitionCapturer: Decoding Visual Stimuli From Human EEG Signal With Multimodal Information
**Authors**: Kaifan Zhang, Lihuo He, Xin Jiang, Wen Lu, Di Wang, Xinbo Gao

**Published Date**: 2024-12-13

**Updated Date**: 2024-12-24

**PDF Url**: [2412.10489v2](http://arxiv.org/pdf/2412.10489v2)

**Abstract**: Electroencephalogram (EEG) signals have attracted significant attention from
researchers due to their non-invasive nature and high temporal sensitivity in
decoding visual stimuli. However, most recent studies have focused solely on
the relationship between EEG and image data pairs, neglecting the valuable
``beyond-image-modality" information embedded in EEG signals. This results in
the loss of critical multimodal information in EEG. To address this limitation,
we propose CognitionCapturer, a unified framework that fully leverages
multimodal data to represent EEG signals. Specifically, CognitionCapturer
trains Modality Expert Encoders for each modality to extract cross-modal
information from the EEG modality. Then, it introduces a diffusion prior to map
the EEG embedding space to the CLIP embedding space, followed by using a
pretrained generative model, the proposed framework can reconstruct visual
stimuli with high semantic and structural fidelity. Notably, the framework does
not require any fine-tuning of the generative models and can be extended to
incorporate more modalities. Through extensive experiments, we demonstrate that
CognitionCapturer outperforms state-of-the-art methods both qualitatively and
quantitatively. Code: https://github.com/XiaoZhangYES/CognitionCapturer.


### Discovery of 2D Materials via Symmetry-Constrained Diffusion Model
**Authors**: Shihang Xu, Shibing Chu, Rami Mrad, Zhejun Zhang, Zhelin Li, Runxian Jiao, Yuanping Chen

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18414v1](http://arxiv.org/pdf/2412.18414v1)

**Abstract**: Generative model for 2D materials has shown significant promise in
accelerating the material discovery process. The stability and performance of
these materials are strongly influenced by their underlying symmetry. However,
existing generative models for 2D materials often neglect symmetry constraints,
which limits both the diversity and quality of the generated structures. Here,
we introduce a symmetry-constrained diffusion model (SCDM) that integrates
space group symmetry into the generative process. By incorporating Wyckoff
positions, the model ensures adherence to symmetry principles, leading to the
generation of 2,000 candidate structures. DFT calculations were conducted to
evaluate the convex hull energies of these structures after structural
relaxation. From the generated samples, 843 materials that met the energy
stability criteria (Ehull < 0.6 eV/atom) were identified. Among these, six
candidates were selected for further stability analysis, including phonon band
structure evaluations and electronic properties investigations, all of which
exhibited phonon spectrum stability. To benchmark the performance of SCDM, a
symmetry-unconstrained diffusion model was also evaluated via crystal structure
prediction model. The results highlight that incorporating symmetry constraints
enhances the effectiveness of generated 2D materials, making a contribution to
the discovery of 2D materials through generative modeling.


### RDPM: Solve Diffusion Probabilistic Models via Recurrent Token Prediction
**Authors**: Wu Xiaoping, Hu Jie, Wei Xiaoming

**Published Date**: 2024-12-24

**Updated Date**: 2024-12-24

**PDF Url**: [2412.18390v1](http://arxiv.org/pdf/2412.18390v1)

**Abstract**: Diffusion Probabilistic Models (DPMs) have emerged as the de facto approach
for high-fidelity image synthesis, operating diffusion processes on continuous
VAE latent, which significantly differ from the text generation methods
employed by Large Language Models (LLMs). In this paper, we introduce a novel
generative framework, the Recurrent Diffusion Probabilistic Model (RDPM), which
enhances the diffusion process through a recurrent token prediction mechanism,
thereby pioneering the field of Discrete Diffusion. By progressively
introducing Gaussian noise into the latent representations of images and
encoding them into vector-quantized tokens in a recurrent manner, RDPM
facilitates a unique diffusion process on discrete-value domains. This process
iteratively predicts the token codes for subsequent timesteps, transforming the
initial standard Gaussian noise into the source data distribution, aligning
with GPT-style models in terms of the loss function. RDPM demonstrates superior
performance while benefiting from the speed advantage of requiring only a few
inference steps. This model not only leverages the diffusion process to ensure
high-quality generation but also converts continuous signals into a series of
high-fidelity discrete tokens, thereby maintaining a unified optimization
strategy with other discrete tokens, such as text. We anticipate that this work
will contribute to the development of a unified model for multimodal
generation, specifically by integrating continuous signal domains such as
images, videos, and audio with text. We will release the code and model weights
to the open-source community.


