# Abstracts of Papers

## Physics
### Quantum simulation of bubble nucleation across a quantum phase transition
**Authors**: De Luo, Federica Maria Surace, Arinjoy De, Alessio Lerose, Elizabeth R. Bennewitz, Brayden Ware, Alexander Schuckert, Zohreh Davoudi, Alexey V. Gorshkov, Or Katz, Christopher Monroe

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09607v1](http://arxiv.org/pdf/2505.09607v1)

**Abstract**: The liquid-vapor transition is a classic example of a discontinuous
(first-order) phase transition. Such transitions underlie many phenomena in
cosmology, nuclear and particle physics, and condensed-matter physics. They
give rise to long-lived metastable states, whose decay can be driven by either
thermal or quantum fluctuations. Yet, direct experimental observations of how
these states collapse into a stable phase remain elusive in the quantum regime.
Here, we use a trapped-ion quantum simulator to observe the real-time dynamics
of ``bubble nucleation'' induced by quantum fluctuations. Bubbles are localized
domains of the stable phase which spontaneously form, or nucleate, and expand
as the system is driven across a discontinuous quantum phase transition.
Implementing a mixed-field Ising spin model with tunable and time-dependent
interactions, we track the microscopic evolution of the metastable state as the
Hamiltonian parameters are varied in time with various speeds, bringing the
system out of equilibrium. Site-resolved measurements reveal the emergence and
evolution of finite-size quantum bubbles, providing direct insight into the
mechanism by which the metastable phase decays. We also identify nonequilibrium
scaling behavior near the transition, consistent with a generalized
Kibble-Zurek mechanism. Our results demonstrate the power of quantum simulators
to probe out-of-equilibrium many-body physics, including quantum bubble
nucleation, a key feature of discontinuous quantum phase transitions, with
application to studies of matter formation in the early universe.


### Comparative Analysis of GFN Methods in Geometry Optimization of Small Organic Semiconductor Molecules: A DFT Benchmarking Study
**Authors**: Steve Cabrel Teguia Kouam, Jean-Pierre Tchapet Njafa, Raoult Dabou Teukam, Patrick Mvoto Kongo, Jean-Pierre Nguenang, Serge Guy Nana Engo

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09606v1](http://arxiv.org/pdf/2505.09606v1)

**Abstract**: This study benchmarks the geometric, frequency, non-covalent (GFN)
semi-empirical methods, GFN1-xTB, GFN2-xTB, GFN0-xTB, and GFN-FF, against
density functional theory (DFT) for the geometry optimization of small organic
semiconductor molecules. Two datasets are evaluated: a QM9-derived subset of
small organic molecules and the Harvard Clean Energy Project (CEP) database of
extended $\pi$-systems relevant to organic photovoltaics. Structural agreement
is quantified using heavy-atom RMSD, equilibrium rotational constants, bond
lengths, angles, and HOMO-LUMO energy gaps. Computational efficiency is
assessed via CPU time and scaling behavior. GFN1-xTB and GFN2-xTB demonstrate
the highest structural fidelity, while GFN-FF offers an optimal balance between
accuracy and speed, particularly for larger systems. The results indicate that
GFN-based methods are suitable for high-throughput molecular screening of small
organic semiconductors, the choice of the method depending on the accuracy-cost
trade-offs. The findings support the deployment of GFN approaches in
computational pipelines for the discovery of organic electronics and materials,
providing information on their strengths and limitations relative to
established DFT methods.


### Exponential improvement in quantum simulations of bosons
**Authors**: Masanori Hanada, Shunji Matsuura, Emanuele Mendicelli, Enrico Rinaldi

**Published Date**: 2025-05-05

**Updated Date**: 2025-05-14

**PDF Url**: [2505.02553v2](http://arxiv.org/pdf/2505.02553v2)

**Abstract**: Hamiltonian quantum simulation of bosons on digital quantum computers
requires truncating the Hilbert space to finite dimensions. The method of
truncation and the choice of basis states can significantly impact the
complexity of the quantum circuit required to simulate the system. For example,
a truncation in the Fock basis where each boson is encoded with a register of
$Q$ qubits, can result in an exponentially large number of Pauli strings
required to decompose the truncated Hamiltonian. This, in turn, can lead to an
exponential increase in $Q$ in the complexity of the quantum circuit. For
lattice quantum field theories such as Yang-Mills theory and QCD, several
Hamiltonian formulations and corresponding truncations have been put forward in
recent years. There is no exponential increase in $Q$ when resorting to the
orbifold lattice Hamiltonian, while we do not know how to remove the
exponential complexity in $Q$ in the commonly used Kogut-Susskind Hamiltonian.
Specifically, when using the orbifold lattice Hamiltonian, the continuum limit,
or, in other words, the removal of the ultraviolet energy cutoff, is obtained
with circuits whose resources scale like $Q$, while they scale like
$\mathcal{O}(\exp(Q))$ for the Kogut-Susskind Hamiltonian: this can be seen as
an exponential speed up in approaching the physical continuum limit for the
orbifold lattice Hamiltonian formulation. We show that the universal framework,
advocated by three of the authors (M.~H., S.~M., and E.~R.) and collaborators
provides a natural avenue to solve the exponential scaling of circuit
complexity with $Q$, and it is the reason why using the orbifold lattice
Hamiltonian is advantageous. We also point out that Hamiltonian formulations
based on a gauge-invariant Hilbert space require an exponential increase in the
resource requirement with respect to using an extended Hilbert space.


### High-Performance Computational Magnetohydrodynamics with Python
**Authors**: Chris Bard, John Dorelli

**Published Date**: 2025-03-26

**Updated Date**: 2025-05-14

**PDF Url**: [2503.20899v2](http://arxiv.org/pdf/2503.20899v2)

**Abstract**: We present the AGATE simulation code, a Python-based framework developed
primarily for solving the magnetohydrodynamics (MHD) equations while
maintaining adaptability to other equation sets. The code employs a modular,
object-oriented architecture that separates interface specifications from
numerical implementations, allowing users to customize numerical methods and
physics models. Built on a Godunov-type finite-volume scheme, AGATE currently
supports the ideal, Hall, and Chew-Goldberger-Low (CGL) MHD equations, with
multiple acceleration options ranging from Numpy to GPU-enabled computation via
NVIDIA CUDA. Performance testing demonstrates that our GPU implementations
achieve 40-60x speedups over CPU versions. Comprehensive validation through
established benchmarks confirms accurate reproduction of both linear and
nonlinear phenomena across different MHD regimes. This combination of
modularity, performance, and extensibility makes AGATE suitable for multiple
applications: from rapid prototyping to production simulations, and from
numerical algorithm development to physics education.


### Experimental demonstration of an analogy between optical non-coherence and irreversibility of heat transport
**Authors**: Aleksandr Meilakhs, Claudio Pastorino, Miguel Larotonda

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09522v1](http://arxiv.org/pdf/2505.09522v1)

**Abstract**: We probe experimentally a connection between coherence in the context of
optical physics and the irreversibility present in heat transfer through an
interface separating two media. The robustness of the experiment on the one
hand, and the theoretical description taken from the statistical-mechanics
treatment of the heat transfer problem, on the other hand, allows for the study
of the arrow of time's problem within the clean and precise framework of
experimental optical physics. The central aspect of the experiment is a light
beam incident and split at an interface to produce a second common interaction
point again at the interface. The experiment was carried out with two light
sources that only differ in their coherence length. In the case of the highly
coherent light source, we were able to combine the previously split parts of
the light back into a single beam. This is indicative of the reversibility of
the process of coherent light transmission through the interface. The light
source with low coherence length, on the contrary, does not allow for such a
recombination, thus producing an irreversible process. We explain how the
latter case is analogous to the process of interfacial heat transport, thus
establishing an important connection between optical non-coherence and
irreversibility of transport phenomena. Our finding paves the way for the study
of fundamental processes in heat transfer and the surge of irreversibility in
the realm of optical physics.


### The impact of the TMD shape function on matching the transverse momentum spectrum in $J/ψ$ production at the EIC
**Authors**: Luca Maxia, Daniël Boer, Jelle Bor

**Published Date**: 2025-04-28

**Updated Date**: 2025-05-14

**PDF Url**: [2504.19617v2](http://arxiv.org/pdf/2504.19617v2)

**Abstract**: The impact of the inclusion of TMD shape functions on the transverse momentum
spectrum in $J/\psi$ production at the EIC is investigated by considering the
matching of the TMD factorization description at low transverse momentum with
the collinear factorization description at high transverse momentum by means of
the inverse-error weighting method. Despite large uncertainties from scale
variations and the $J/\psi$ long-distance matrix elements, predictions for the
differential cross section and its $\cos(2\phi_\psi)$ modulation are obtained.
We find that physical constraints are satisfied in case a process-dependent
term is included for color octet production, but not in all cases when it is
excluded. These numerical results support the analytic calculations in
\cite{Boer:2023zit}. Future experimental data can thus test the validity of TMD
factorization in $J/\psi$ production and explore the presence of nontrivial
process-dependent effects in the soft-gluon resummation. This will be crucial
in the extraction of gluon unpolarized and linearly polarized TMD distributions
of the proton. In addition, we suggest how the sign of the latter can be
determined by investigating the presence of a node in the $\cos(2\phi_\psi)$
modulation as a function of transverse momentum.


### Platforms for the realization and characterization of Tomonaga-Luttinger liquids
**Authors**: Isabelle Bouchoule, Roberta Citro, Tim Duty, Thierry Giamarchi, Randall G. Hulet, Martin Klanjsek, Edmond Orignac, Bent Weber

**Published Date**: 2025-01-21

**Updated Date**: 2025-05-14

**PDF Url**: [2501.12097v2](http://arxiv.org/pdf/2501.12097v2)

**Abstract**: The concept of a Tomonaga-Luttinger liquid (TLL) has been established as a
fundamental theory for the understanding of one-dimensional quantum systems.
Originally formulated as a replacement for Landau's Fermi-liquid theory, which
accurately predicts the behaviour of most 3D metals but fails dramatically in
1D, the TLL description applies to a even broader class of 1D systems,including
bosons and anyons. After a certain number of theoretical breakthroughs, its
descriptive power has now been confirmed experimentally in different
experimental platforms. They extend from organic conductors, carbon nanotubes,
quantum wires, topological edge states of quantum spin Hall insulators to cold
atoms, Josephson junctions, Bose liquids confined within 1D nanocapillaries and
spin chains. In the ground state of such systems, quantum fluctuations become
correlated on all length scales, but, counter-intuitively, no long-range order
exists. In this respect, this review will illustrate the validity of conformal
field theory for describing real-world systems, establishing the boundaries for
its application and, on the other side will discuss the spectacular
demonstration of how the quantum-critical TLL state governs the properties of
many-body systems in one dimension.


### Physical Representations of Corner Symmetries
**Authors**: Ludovic Varrin

**Published Date**: 2024-09-16

**Updated Date**: 2025-05-14

**PDF Url**: [2409.10624v3](http://arxiv.org/pdf/2409.10624v3)

**Abstract**: We give the full representation theory of the gravitational extended corner
symmetry group in two-dimensions. This includes projective representations,
which correspond to representations of the quantum corner symmetry group. We
find that they are described by one-dimensional conformal fields with an
additional index in the Fock space of the harmonic oscillator. We begin with a
review of Mackey's theory of induced representations and then proceed to its
application to the corner symmetries. The field representations, induced from
the irreducible representations of the special linear group are worked out
first. The little group method is then applied to the extended corner symmetry
group to obtain the irreducible unitary representations. Finally, we focus on
projective representations and their application to the description of local
subsystems.


### Equivalence Theorems and Double-Copy Structure in Scattering Amplitudes of Massive Kaluza-Klein States with Matter Interactions
**Authors**: Kezhu Guo, Yanfeng Hang

**Published Date**: 2025-04-07

**Updated Date**: 2025-05-14

**PDF Url**: [2504.05199v2](http://arxiv.org/pdf/2504.05199v2)

**Abstract**: We investigate the scattering amplitudes of massive Kaluza-Klein (KK) states
in compactified five-dimensional warped gauge and gravity theories. Focusing on
tree-level $2\to2$ processes, we analyze the leading-order amplitudes involving
bulk KK matter fields and KK gauge/gravitational Goldstone bosons. By imposing
the gauge theory equivalence theorem (GAET) and the gravitational equivalence
theorem (GRET) within warped KK theories, we systematically reconstruct the
leading-order amplitudes for physical KK gauge bosons and gravitons, thereby
circumventing the intricate energy cancellations inherent in physical
amplitudes. Within this framework, the correspondence between GAET and GRET
arises as a direct manifestation of the leading-order double-copy relation in
the high-energy expansion. This connection provides a foundation for extending
the BCJ double-copy construction to four-point amplitudes involving bulk KK
matter fields, and further generalizes to arbitrary $N$-point cases, enabling a
systematic derivation of the corresponding gravitational amplitudes with
consistent incorporation of KK matter fields at leading order.


### Surface excitation of Rydberg dressed quantum droplet of Bose-Einstein Condensates
**Authors**: Avra Banerjee, Dwipesh Majumder

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09474v1](http://arxiv.org/pdf/2505.09474v1)

**Abstract**: We have considered a quantum droplet of two components of Bose-Einstein
condensate (BEC) inside the electron of a Rydberg atom to study the surface
mode of collective excitation using the Bogoliubov theory of excitation. We
have calculated the surface excitation spectrum for various Rydberg
electron-atom interaction strengths. From the energy spectrum, we calculated
the surface tension of the droplet as a function of Rydberg electron-atom
interaction strength. Our study shows that the electron-atom interaction
enhances the surface energy; hence, the droplet will be more stable inside the
electron of a Rydberg atom.


## Diffusion
### BLIP3-o: A Family of Fully Open Unified Multimodal Models-Architecture, Training and Dataset
**Authors**: Jiuhai Chen, Zhiyang Xu, Xichen Pan, Yushi Hu, Can Qin, Tom Goldstein, Lifu Huang, Tianyi Zhou, Saining Xie, Silvio Savarese, Le Xue, Caiming Xiong, Ran Xu

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09568v1](http://arxiv.org/pdf/2505.09568v1)

**Abstract**: Unifying image understanding and generation has gained growing attention in
recent research on multimodal models. Although design choices for image
understanding have been extensively studied, the optimal model architecture and
training recipe for a unified framework with image generation remain
underexplored. Motivated by the strong potential of autoregressive and
diffusion models for high-quality generation and scalability, we conduct a
comprehensive study of their use in unified multimodal settings, with emphasis
on image representations, modeling objectives, and training strategies.
Grounded in these investigations, we introduce a novel approach that employs a
diffusion transformer to generate semantically rich CLIP image features, in
contrast to conventional VAE-based representations. This design yields both
higher training efficiency and improved generative quality. Furthermore, we
demonstrate that a sequential pretraining strategy for unified models-first
training on image understanding and subsequently on image generation-offers
practical advantages by preserving image understanding capability while
developing strong image generation ability. Finally, we carefully curate a
high-quality instruction-tuning dataset BLIP3o-60k for image generation by
prompting GPT-4o with a diverse set of captions covering various scenes,
objects, human gestures, and more. Building on our innovative model design,
training recipe, and datasets, we develop BLIP3-o, a suite of state-of-the-art
unified multimodal models. BLIP3-o achieves superior performance across most of
the popular benchmarks spanning both image understanding and generation tasks.
To facilitate future research, we fully open-source our models, including code,
model weights, training scripts, and pretraining and instruction tuning
datasets.


### Learning Long-Context Diffusion Policies via Past-Token Prediction
**Authors**: Marcel Torne, Andy Tang, Yuejiang Liu, Chelsea Finn

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09561v1](http://arxiv.org/pdf/2505.09561v1)

**Abstract**: Reasoning over long sequences of observations and actions is essential for
many robotic tasks. Yet, learning effective long-context policies from
demonstrations remains challenging. As context length increases, training
becomes increasingly expensive due to rising memory demands, and policy
performance often degrades as a result of spurious correlations. Recent methods
typically sidestep these issues by truncating context length, discarding
historical information that may be critical for subsequent decisions. In this
paper, we propose an alternative approach that explicitly regularizes the
retention of past information. We first revisit the copycat problem in
imitation learning and identify an opposite challenge in recent diffusion
policies: rather than over-relying on prior actions, they often fail to capture
essential dependencies between past and future actions. To address this, we
introduce Past-Token Prediction (PTP), an auxiliary task in which the policy
learns to predict past action tokens alongside future ones. This regularization
significantly improves temporal modeling in the policy head, with minimal
reliance on visual representations. Building on this observation, we further
introduce a multistage training strategy: pre-train the visual encoder with
short contexts, and fine-tune the policy head using cached long-context
embeddings. This strategy preserves the benefits of PTP while greatly reducing
memory and computational overhead. Finally, we extend PTP into a
self-verification mechanism at test time, enabling the policy to score and
select candidates consistent with past actions during inference. Experiments
across four real-world and six simulated tasks demonstrate that our proposed
method improves the performance of long-context diffusion policies by 3x and
accelerates policy training by more than 10x.


### Detecting Multimedia Generated by Large AI Models: A Survey
**Authors**: Li Lin, Neeraj Gupta, Yue Zhang, Hainan Ren, Chun-Hao Liu, Feng Ding, Xin Wang, Xin Li, Luisa Verdoliva, Shu Hu

**Published Date**: 2024-01-22

**Updated Date**: 2025-05-14

**PDF Url**: [2402.00045v5](http://arxiv.org/pdf/2402.00045v5)

**Abstract**: The rapid advancement of Large AI Models (LAIMs), particularly diffusion
models and large language models, has marked a new era where AI-generated
multimedia is increasingly integrated into various aspects of daily life.
Although beneficial in numerous fields, this content presents significant
risks, including potential misuse, societal disruptions, and ethical concerns.
Consequently, detecting multimedia generated by LAIMs has become crucial, with
a marked rise in related research. Despite this, there remains a notable gap in
systematic surveys that focus specifically on detecting LAIM-generated
multimedia. Addressing this, we provide the first survey to comprehensively
cover existing research on detecting multimedia (such as text, images, videos,
audio, and multimodal content) created by LAIMs. Specifically, we introduce a
novel taxonomy for detection methods, categorized by media modality, and
aligned with two perspectives: pure detection (aiming to enhance detection
performance) and beyond detection (adding attributes like generalizability,
robustness, and interpretability to detectors). Additionally, we have presented
a brief overview of generation mechanisms, public datasets, online detection
tools, and evaluation metrics to provide a valuable resource for researchers
and practitioners in this field. Most importantly, we offer a focused analysis
from a social media perspective to highlight their broader societal impact.
Furthermore, we identify current challenges in detection and propose directions
for future research that address unexplored, ongoing, and emerging issues in
detecting multimedia generated by LAIMs. Our aim for this survey is to fill an
academic gap and contribute to global AI security efforts, helping to ensure
the integrity of information in the digital realm. The project link is
https://github.com/Purdue-M2/Detect-LAIM-generated-Multimedia-Survey.


### Fragment-Masked Diffusion for Molecular Optimization
**Authors**: Kun Li, Xiantao Cai, Jia Wu, Shirui Pan, Huiting Xu, Bo Du, Wenbin Hu

**Published Date**: 2024-08-17

**Updated Date**: 2025-05-14

**PDF Url**: [2408.09106v3](http://arxiv.org/pdf/2408.09106v3)

**Abstract**: Molecular optimization is a crucial aspect of drug discovery, aimed at
refining molecular structures to enhance drug efficacy and minimize side
effects, ultimately accelerating the overall drug development process. Many
molecular optimization methods have been proposed, significantly advancing drug
discovery. These methods primarily on understanding the specific drug target
structures or their hypothesized roles in combating diseases. However,
challenges such as a limited number of available targets and a difficulty
capturing clear structures hinder innovative drug development. In contrast,
phenotypic drug discovery (PDD) does not depend on clear target structures and
can identify hits with novel and unbiased polypharmacology signatures. As a
result, PDD-based molecular optimization can reduce potential safety risks
while optimizing phenotypic activity, thereby increasing the likelihood of
clinical success. Therefore, we propose a fragment-masked molecular
optimization method based on PDD (FMOP). FMOP employs a regression-free
diffusion model to conditionally optimize the molecular masked regions,
effectively generating new molecules with similar scaffolds. On the large-scale
drug response dataset GDSCv2, we optimize the potential molecules across all
985 cell lines. The overall experiments demonstrate that the in-silico
optimization success rate reaches 95.4\%, with an average efficacy increase of
7.5\%. Additionally, we conduct extensive ablation and visualization
experiments, confirming that FMOP is an effective and robust molecular
optimization method. The code is available at:
https://anonymous.4open.science/r/FMOP-98C2.


### Train a Multi-Task Diffusion Policy on RLBench-18 in One Day with One GPU
**Authors**: Yutong Hu, Pinhao Song, Kehan Wen, Renaud Detry

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09430v1](http://arxiv.org/pdf/2505.09430v1)

**Abstract**: We present a method for training multi-task vision-language robotic diffusion
policies that reduces training time and memory usage by an order of magnitude.
This improvement arises from a previously underexplored distinction between
action diffusion and the image diffusion techniques that inspired it: image
generation targets are high-dimensional, while robot actions lie in a much
lower-dimensional space. Meanwhile, the vision-language conditions for action
generation remain high-dimensional. Our approach, Mini-Diffuser, exploits this
asymmetry by introducing Level-2 minibatching, which pairs multiple noised
action samples with each vision-language condition, instead of the conventional
one-to-one sampling strategy. To support this batching scheme, we introduce
architectural adaptations to the diffusion transformer that prevent information
leakage across samples while maintaining full conditioning access. In RLBench
simulations, Mini-Diffuser achieves 95\% of the performance of state-of-the-art
multi-task diffusion policies, while using only 5\% of the training time and
7\% of the memory. Real-world experiments further validate that Mini-Diffuser
preserves the key strengths of diffusion-based policies, including the ability
to model multimodal action distributions and produce behavior conditioned on
diverse perceptual inputs. Code available at
github.com/utomm/mini-diffuse-actor.


## Quantitative Finance
### Fast Learning in Quantitative Finance with Extreme Learning Machine
**Authors**: Liexin Cheng, Xue Cheng, Shuaiqiang Liu

**Published Date**: 2025-05-14

**Updated Date**: 2025-05-14

**PDF Url**: [2505.09551v1](http://arxiv.org/pdf/2505.09551v1)

**Abstract**: This paper demonstrates that a broad class of problems in quantitative
finance, including those previously addressed using deep neural networks, can
be efficiently solved using single-layer neural networks without iterative
gradient-based training, namely extreme learning machine (ELM). ELM utilizes a
single-layer network with randomly initialized hidden nodes and analytically
computed output weights obtained via convex optimization, enabling rapid
training and inference. Both supervised and unsupervised learning tasks are
explored.
  In supervised learning, ELM is employed to learn parametric option pricing
functions, predict intraday stock returns, and complete implied volatility
surfaces. Compared with deep neural networks, Gaussian process regression, and
logistic regression, ELM achieves higher computational speed, comparable
accuracy, and superior generalization.
  In unsupervised learning, ELM numerically solves Black-Scholes-type PDEs, and
outperforms Physics-Informed Neural Networks in training speed without losing
precision. The approximation and generalization abilities of ELM are briefly
discussed.
  The findings establish ELM as a practical and efficient tool for various
tasks in quantitative finance.


