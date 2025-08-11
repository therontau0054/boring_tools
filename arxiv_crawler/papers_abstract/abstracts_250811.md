# Abstracts of Papers

## Physics
### WGAST: Weakly-Supervised Generative Network for Daily 10 m Land Surface Temperature Estimation via Spatio-Temporal Fusion
**Authors**: Sofiane Bouaziz, Adel Hafiane, Raphael Canals, Rachid Nedjai

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06485v1](http://arxiv.org/pdf/2508.06485v1)

**Abstract**: Urbanization, climate change, and agricultural stress are increasing the
demand for precise and timely environmental monitoring. Land Surface
Temperature (LST) is a key variable in this context and is retrieved from
remote sensing satellites. However, these systems face a trade-off between
spatial and temporal resolution. While spatio-temporal fusion methods offer
promising solutions, few have addressed the estimation of daily LST at 10 m
resolution. In this study, we present WGAST, a Weakly-Supervised Generative
Network for Daily 10 m LST Estimation via Spatio-Temporal Fusion of Terra
MODIS, Landsat 8, and Sentinel-2. WGAST is the first end-to-end deep learning
framework designed for this task. It adopts a conditional generative
adversarial architecture, with a generator composed of four stages: feature
extraction, fusion, LST reconstruction, and noise suppression. The first stage
employs a set of encoders to extract multi-level latent representations from
the inputs, which are then fused in the second stage using cosine similarity,
normalization, and temporal attention mechanisms. The third stage decodes the
fused features into high-resolution LST, followed by a Gaussian filter to
suppress high-frequency noise. Training follows a weakly supervised strategy
based on physical averaging principles and reinforced by a PatchGAN
discriminator. Experiments demonstrate that WGAST outperforms existing methods
in both quantitative and qualitative evaluations. Compared to the
best-performing baseline, on average, WGAST reduces RMSE by 17.18% and improves
SSIM by 11.00%. Furthermore, WGAST is robust to cloud-induced LST and
effectively captures fine-scale thermal patterns, as validated against 33
ground-based sensors. The code is available at
https://github.com/Sofianebouaziz1/WGAST.git.


### Intuition emerges in Maximum Caliber models at criticality
**Authors**: Lluís Arola-Fernández

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06477v1](http://arxiv.org/pdf/2508.06477v1)

**Abstract**: Whether large predictive models merely parrot their training data or produce
genuine insight lacks a physical explanation. This work reports a primitive
form of intuition that emerges as a metastable phase of learning that
critically balances next-token prediction against future path-entropy. The
intuition mechanism is discovered via mind-tuning, the minimal principle that
imposes Maximum Caliber in predictive models with a control temperature-like
parameter $\lambda$. Training on random walks in deterministic mazes reveals a
rich phase diagram: imitation (low $\lambda$), rule-breaking hallucination
(high $\lambda$), and a fragile in-between window exhibiting strong
protocol-dependence (hysteresis) and multistability, where models spontaneously
discover novel goal-directed strategies. These results are captured by an
effective low-dimensional theory and frame intuition as an emergent property at
the critical balance between memorizing what is and wondering what could be.


### Characterization and automated optimization of laser-driven proton beams from converging liquid sheet jet targets
**Authors**: G. D. Glenn, F. Treffert, H. Ahmed, S. Astbury, M. Borghesi, N. Bourgeois, C. B. Curry, S. J. D. Dann, S. DiIorio, N. P. Dover, T. Dzelzainis, O. Ettlinger, M. Gauthier, L. Giuffrida, R. J. Gray, J. S. Green, G. S. Hicks, C. Hyland, V. Istokskaia, M. King, B. Loughran, D. Margarone, O. McCusker, P. McKenna, Z. Najmudin, C. Parisuaña, P. Parsons, C. Spindloe, M. J. V. Streeter, D. R. Symes, A. G. R. Thomas, N. Xu, S. H. Glenzer, C. A. J. Palmer

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06462v1](http://arxiv.org/pdf/2508.06462v1)

**Abstract**: Compact, stable, and versatile laser-driven ion sources hold great promise
for applications ranging from medicine to materials science and fundamental
physics. While single-shot sources have demonstrated favorable beam properties,
including the peak fluxes necessary for several applications, high repetition
rate operation will be necessary to generate and sustain the high average flux
needed for many of the most exciting applications of laser-driven ion sources.
Further, to navigate through the high-dimensional space of laser and target
parameters towards experimental optima, it is essential to develop ion
acceleration platforms compatible with machine learning learning techniques and
capable of autonomous real-time optimization. Here we present a multi-Hz ion
acceleration platform employing a liquid sheet jet target. We characterize the
laser-plasma interaction and the laser-driven proton beam across a variety of
key parameters governing the interaction using an extensive suite of online
diagnostics. We also demonstrate real-time, closed-loop optimization of the ion
beam maximum energy by tuning the laser wavefront using a Bayesian optimization
scheme. This approach increased the maximum proton energy by 11% compared to a
manually-optimized wavefront by enhancing the energy concentration within the
laser focal spot, demonstrating the potential for closed-loop optimization
schemes to tune future ion accelerators for robust high repetition rate
operation.


### Entanglement-Based Artificial Topology: Neighboring Remote Network Nodes
**Authors**: SiYi Chen, Jessica Illiano, Angela Sara Cacciapuoti, Marcello Caleffi

**Published Date**: 2024-04-24

**Updated Date**: 2025-08-08

**PDF Url**: [2404.16204v4](http://arxiv.org/pdf/2404.16204v4)

**Abstract**: Entanglement is unanimously recognized as the key communication resource of
the Quantum Internet. Yet, the possibility of implementing novel network
functionalities by exploiting the marvels of entanglement has been poorly
investigated so far, by mainly restricting the attention to bipartite
entanglement. Conversely, in this paper, we aim at exploiting multipartite
entanglement as inter-network resource. Specifically, we consider the
interconnection of different Quantum Local Area Networks (QLANs), and we show
that multipartite entanglement allows to dynamically generate an inter-QLAN
artificial topology, by means of local operations only, that overcomes the
limitations of the physical QLAN topologies. To this aim, we first design the
multipartite entangled state to be distributed within each QLAN. Then, we show
how such a state can be engineered to: i) interconnect nodes belonging to
different QLANs, and ii) dynamically adapt to different inter-QLAN traffic
patterns. Our contribution aims at providing the network engineering community
with a hands-on guideline towards the concept of artificial topology and
artificial neighborhood.


### Learning interactions between Rydberg atoms
**Authors**: Olivier Simard, Anna Dawid, Joseph Tindall, Michel Ferrero, Anirvan M. Sengupta, Antoine Georges

**Published Date**: 2024-12-16

**Updated Date**: 2025-08-08

**PDF Url**: [2412.12019v2](http://arxiv.org/pdf/2412.12019v2)

**Abstract**: Quantum simulators have the potential to solve quantum many-body problems
that are beyond the reach of classical computers, especially when they feature
long-range entanglement. To fulfill their prospects, quantum simulators must be
fully controllable, allowing for precise tuning of the microscopic physical
parameters that define their implementation. We consider Rydberg-atom arrays, a
promising platform for quantum simulations. Experimental control of such arrays
is limited by the imprecision on the optical tweezers positions when assembling
the array, hence introducing uncertainties in the simulated Hamiltonian. In
this work, we introduce a scalable approach to Hamiltonian learning using graph
neural networks (GNNs). We employ the Density Matrix Renormalization Group
(DMRG) to generate ground-state snapshots of the transverse field Ising model
realized by the array, for many realizations of the Hamiltonian parameters.
Correlation functions reconstructed from these snapshots serve as input data to
carry out the training. We demonstrate that our GNN model has a remarkable
capacity to extrapolate beyond its training domain, both regarding the size and
the shape of the system, yielding an accurate determination of the Hamiltonian
parameters with a minimal set of measurements. We prove a theorem establishing
a bijective correspondence between the correlation functions and the
interaction parameters in the Hamiltonian, which provides a theoretical
foundation to our learning algorithm. Our work could open the road to feedback
control of the positions of the optical tweezers, hence providing a decisive
improvement of analog quantum simulators.


### Nonreciprocal and Geometric Frustration in Dissipative Quantum Spins
**Authors**: Guitao Lyu, Myung-Joong Hwang

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06444v1](http://arxiv.org/pdf/2508.06444v1)

**Abstract**: Nonreciprocal interactions often create conflicting dynamical objectives that
cannot be simultaneously satisfied, leading to nonreciprocal frustration. On
the other hand, geometric frustration arises when conflicting static objectives
in energy minimization cannot be satisfied. In this work, we show that
nonreciprocal interaction among three collective quantum spins, mediated by a
damped cavity, induces not only nonreciprocal frustration, intrinsic to
nonreciprocity, but also geometric frustration with a remarkable robustness
against disorder. It therefore ensures that the accidental degeneracy for
steady states remains intact even when the system is perturbed away from a
fine-tuned point of enhanced symmetry, in sharp contrast to the equilibrium
case. Leveraging this finding, we identify a nonreciprocal phase transition
driven by both geometric and nonreciprocal frustration. It gives rise to a
time-dependent state, which shows a chiral dynamics along a geometry shaped by
the geometric frustration and dynamically restores the broken discrete
symmetries. Moreover, it constitutes a time-crystalline order, with multiple
harmonics set by an emergent time scale that exhibits critical slowing down.
Our predictions have important physical implications for a three-component
spinor BEC-cavity system, which manifest as a geometric frustration in the
structural phase transition and chiral dynamics of the frustrated
self-organized BECs. We demonstrate the feasibility of experimental observation
despite the presence of disorder in the spin-cavity coupling strengths.


### Perturbative unitarity bounds from momentum-space entanglement
**Authors**: Carlos Duaso Pueyo, Harry Goodhew, Ciaran McCulloch, Enrico Pajer

**Published Date**: 2024-10-31

**Updated Date**: 2025-08-08

**PDF Url**: [2410.23709v2](http://arxiv.org/pdf/2410.23709v2)

**Abstract**: Physical theories have a limited regime of validity and hence must be
accompanied by a breakdown diagnostic to establish when they cease to be valid
as parameters are varied. For perturbative theories, estimates of the first
neglected order offer valuable guidance, but one is often interested in sharp
bounds beyond which perturbation theory necessarily fails. In particle physics,
it is common to employ the bounds on partial waves imposed by unitarity as such
a diagnostic. Unfortunately, these bounds don't extend to curved spacetime,
where scattering experiments are challenging to define. Here, we propose to use
the growth of entanglement in momentum space as a breakdown diagnostic for
perturbation theory in general field theories. This diagnostic can be readily
used in cosmological spacetimes and does not require any flat spacetime limit.
More in detail, we consider the so-called purity of the reduced density
operator constructed by tracing out all but one of the Fourier modes in an
effective theory and we present a diagrammatic technique to compute it
perturbatively. Constraints on the regime of validity of perturbation theory
are then derived when the perturbative purity violates its unitarity bounds.
  In flat spacetime, we compare these purity bounds to those from partial
waves. We find general qualitative agreement but with remarkable differences:
purity bounds can be sometimes weaker, but other times they exist when no
partial wave bounds exist. We then derive purity bounds for scalar field
theories in de Sitter spacetime for a variety of interactions that appear in
inflationary models. Importantly, our bounds make no reference to time
evolution and in de Sitter they depend exclusively on scale-invariant ratios of
the physical kinematics.


### Optoelectronic Physical Unclonable Functions and Reservoir-Inspired Computation with Low Symmetry Integrated Photonics
**Authors**: Farhan Bin Tarik, Yingjie Lao, Mustafa Hammood, Jonathan Barnes, Madeline Mahanloo, Lukas Chrostowski, Taufiquar Khan, Judson D. Ryckman

**Published Date**: 2025-07-09

**Updated Date**: 2025-08-08

**PDF Url**: [2507.06473v2](http://arxiv.org/pdf/2507.06473v2)

**Abstract**: Structural symmetry in photonics has long been exploited to engineer devices
with predictable, analytically describable behaviors. Yet this predictability
often limits their expressivity, constraining complex interactions essential
for advanced functionalities in computing, sensing, and security. Here we
demonstrate how low symmetry integrated photonic circuits can unlock enhanced
mode diversity and rich spectral complexity, enabling highly non-linear
transformations of input signals into outputs. Our devices, physically
unclonable moir\'e quasicrystal interferometers integrated on a silicon
photonics platform, exhibit aperiodic and reconfigurable spectral responses and
are characterized by analyticity breaking and erasable mutual information.
Using dynamic thermo-optic control to drive their complex spectral dynamics, we
demonstrate that these devices function as reconfigurable physical unclonable
functions (rPUFs). We also highlight their ability to perform high-dimensional
input--output transformations, emulating reservoir-inspired information
processing in a compact photonic platform. This work bridges the gap between
engineered and natural complexity in photonic systems, revealing new
opportunities for scalable, energy-efficient, and information-dense
opto-electronics with applications in secure communications, hardware security,
advanced sensing, and optical information processing. Our results establish
low-symmetry integrated photonics as a powerful resource for complex signal
manipulation in photonic systems.


### Single photon emission from lithographically-positioned engineered nanodiamonds for cryogenic applications
**Authors**: Vivekanand Tiwari, Zhaojin Liu, Hao-Cheng Weng, Krishna C Balram, John G Rarity, Soumen Mandal, Oliver A Williams, Gavin W Morley, Joe A Smith

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06424v1](http://arxiv.org/pdf/2508.06424v1)

**Abstract**: Nitrogen-vacancy centres in nanodiamonds (NDs) provide a promising resource
for quantum photonic systems. However, developing a technology beyond
proof-of-principle physics requires optimally engineering its component parts.
In this work, we present a hybrid materials platform by photolithographically
positioning ball-milled isotopically-enriched NDs on broadband metal
reflectors. The structure enhances the photonic collection efficiency, enabling
cryogenic characterisation despite the limited numerical aperture imposed by
our cryostat. Our device, with SiO$_2$ above a silver reflector, allows us to
perform spectroscopic characterisation at 16 K and measure autocorrelation
functions confirming single-photon emission (g$^2$(0)<0.5). Through comparative
studies of similar hybrid device configurations, we can move towards optimally
engineered techniques for building and analysing quantum emitters in
wafer-scale photonic environments.


### Quantum Annealing for the Set Splitting Problem
**Authors**: Sean Borneman

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06410v1](http://arxiv.org/pdf/2508.06410v1)

**Abstract**: I present a novel use of quantum annealing to solve the Set Splitting Problem
using (QUBO) problem formulation. The contribution of the work is in
formulating penalty functions that ensure the ground state of the QUBO
Hamiltonian corresponds to valid solutions that split the input subsets. This
approach scales linearly in terms of the number of logical qubits relative to
problem size. Empirical tests of the proposed solution show convergence to
globally optimal solutions, with high accuracy rates over repeated trials.
Hardware limitations of current quantum annealers lead to an exponential rise
in required physical qubits, versus the theoretical linear increase, although
this can improve with future developments. Further work is needed to enhance
formulation robustness, reduce qubit requirements for embedded problems, and to
conduct more extensive bench-marking. Quantum solutions to the Set-Splitting
problem lead to reduced time complexity versus classical solutions, and may
accelerate research in biology, cybersecurity, and other domains.


## Diffusion
### LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation
**Authors**: Yuhang Huang, JIazhao Zhang, Shilong Zou, XInwang Liu, Ruizhen Hu, Kai Xu

**Published Date**: 2025-05-13

**Updated Date**: 2025-08-08

**PDF Url**: [2505.11528v2](http://arxiv.org/pdf/2505.11528v2)

**Abstract**: Predictive manipulation has recently gained considerable attention in the
Embodied AI community due to its potential to improve robot policy performance
by leveraging predicted states. However, generating accurate future visual
states of robot-object interactions from world models remains a well-known
challenge, particularly in achieving high-quality pixel-level representations.
To this end, we propose LaDi-WM, a world model that predicts the latent space
of future states using diffusion modeling. Specifically, LaDi-WM leverages the
well-established latent space aligned with pre-trained Visual Foundation Models
(VFMs), which comprises both geometric features (DINO-based) and semantic
features (CLIP-based). We find that predicting the evolution of the latent
space is easier to learn and more generalizable than directly predicting
pixel-level images. Building on LaDi-WM, we design a diffusion policy that
iteratively refines output actions by incorporating forecasted states, thereby
generating more consistent and accurate results. Extensive experiments on both
synthetic and real-world benchmarks demonstrate that LaDi-WM significantly
enhances policy performance by 27.9\% on the LIBERO-LONG benchmark and 20\% on
the real-world scenario. Furthermore, our world model and policies achieve
impressive generalizability in real-world experiments.


### Conditional Diffusion Models are Medical Image Classifiers that Provide Explainability and Uncertainty for Free
**Authors**: Gian Mario Favero, Parham Saremi, Emily Kaczmarek, Brennan Nichyporuk, Tal Arbel

**Published Date**: 2025-02-06

**Updated Date**: 2025-08-08

**PDF Url**: [2502.03687v2](http://arxiv.org/pdf/2502.03687v2)

**Abstract**: Discriminative classifiers have become a foundational tool in deep learning
for medical imaging, excelling at learning separable features of complex data
distributions. However, these models often need careful design, augmentation,
and training techniques to ensure safe and reliable deployment. Recently,
diffusion models have become synonymous with generative modeling in 2D. These
models showcase robustness across a range of tasks including natural image
classification, where classification is performed by comparing reconstruction
errors across images generated for each possible conditioning input. This work
presents the first exploration of the potential of class conditional diffusion
models for 2D medical image classification. First, we develop a novel majority
voting scheme shown to improve the performance of medical diffusion
classifiers. Next, extensive experiments on the CheXpert and ISIC Melanoma skin
cancer datasets demonstrate that foundation and trained-from-scratch diffusion
models achieve competitive performance against SOTA discriminative classifiers
without the need for explicit supervision. In addition, we show that diffusion
classifiers are intrinsically explainable, and can be used to quantify the
uncertainty of their predictions, increasing their trustworthiness and
reliability in safety-critical, clinical contexts. Further information is
available on our project page:
https://faverogian.github.io/med-diffusion-classifier.github.io/.


### ActivityDiff: A diffusion model with Positive and Negative Activity Guidance for De Novo Drug Design
**Authors**: Renyi Zhou, Huimin Zhu, Jing Tang, Min Li

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06364v1](http://arxiv.org/pdf/2508.06364v1)

**Abstract**: Achieving precise control over a molecule's biological activity-encompassing
targeted activation/inhibition, cooperative multi-target modulation, and
off-target toxicity mitigation-remains a critical challenge in de novo drug
design. However, existing generative methods primarily focus on producing
molecules with a single desired activity, lacking integrated mechanisms for the
simultaneous management of multiple intended and unintended molecular
interactions. Here, we propose ActivityDiff, a generative approach based on the
classifier-guidance technique of diffusion models. It leverages separately
trained drug-target classifiers for both positive and negative guidance,
enabling the model to enhance desired activities while minimizing harmful
off-target effects. Experimental results show that ActivityDiff effectively
handles essential drug design tasks, including single-/dual-target generation,
fragment-constrained dual-target design, selective generation to enhance target
specificity, and reduction of off-target effects. These results demonstrate the
effectiveness of classifier-guided diffusion in balancing efficacy and safety
in molecular design. Overall, our work introduces a novel paradigm for
achieving integrated control over molecular activity, and provides ActivityDiff
as a versatile and extensible framework.


### OM2P: Offline Multi-Agent Mean-Flow Policy
**Authors**: Zhuoran Li, Xun Wang, Hai Zhong, Longbo Huang

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06269v1](http://arxiv.org/pdf/2508.06269v1)

**Abstract**: Generative models, especially diffusion and flow-based models, have been
promising in offline multi-agent reinforcement learning. However, integrating
powerful generative models into this framework poses unique challenges. In
particular, diffusion and flow-based policies suffer from low sampling
efficiency due to their iterative generation processes, making them impractical
in time-sensitive or resource-constrained settings. To tackle these
difficulties, we propose OM2P (Offline Multi-Agent Mean-Flow Policy), a novel
offline MARL algorithm to achieve efficient one-step action sampling. To
address the misalignment between generative objectives and reward maximization,
we introduce a reward-aware optimization scheme that integrates a
carefully-designed mean-flow matching loss with Q-function supervision.
Additionally, we design a generalized timestep distribution and a
derivative-free estimation strategy to reduce memory overhead and improve
training stability. Empirical evaluations on Multi-Agent Particle and MuJoCo
benchmarks demonstrate that OM2P achieves superior performance, with up to a
3.8x reduction in GPU memory usage and up to a 10.8x speed-up in training time.
Our approach represents the first to successfully integrate mean-flow model
into offline MARL, paving the way for practical and scalable generative
policies in cooperative multi-agent settings.


### Synthetic Data-Driven Multi-Architecture Framework for Automated Polyp Segmentation Through Integrated Detection and Mask Generation
**Authors**: Ojonugwa Oluwafemi Ejiga Peter, Akingbola Oluwapemiisin, Amalahu Chetachi, Adeniran Opeyemi, Fahmi Khalifa, Md Mahmudur Rahman

**Published Date**: 2025-08-08

**Updated Date**: 2025-08-08

**PDF Url**: [2508.06170v1](http://arxiv.org/pdf/2508.06170v1)

**Abstract**: Colonoscopy is a vital tool for the early diagnosis of colorectal cancer,
which is one of the main causes of cancer-related mortality globally; hence, it
is deemed an essential technique for the prevention and early detection of
colorectal cancer. The research introduces a unique multidirectional
architectural framework to automate polyp detection within colonoscopy images
while helping resolve limited healthcare dataset sizes and annotation
complexities. The research implements a comprehensive system that delivers
synthetic data generation through Stable Diffusion enhancements together with
detection and segmentation algorithms. This detection approach combines Faster
R-CNN for initial object localization while the Segment Anything Model (SAM)
refines the segmentation masks. The faster R-CNN detection algorithm achieved a
recall of 93.08% combined with a precision of 88.97% and an F1 score of
90.98%.SAM is then used to generate the image mask. The research evaluated five
state-of-the-art segmentation models that included U-Net, PSPNet, FPN, LinkNet,
and MANet using ResNet34 as a base model. The results demonstrate the superior
performance of FPN with the highest scores of PSNR (7.205893) and SSIM
(0.492381), while UNet excels in recall (84.85%) and LinkNet shows balanced
performance in IoU (64.20%) and Dice score (77.53%).


