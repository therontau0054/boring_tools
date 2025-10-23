# Abstracts of Papers

## Physics
### Passive quantum error correction of photon loss at breakeven
**Authors**: Shruti Shirol, Sean van Geldern, Hanzhe Xi, Chen Wang

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19794v1](http://arxiv.org/pdf/2510.19794v1)

**Abstract**: Physical qubits in a quantum computer are often represented by superposition
states of single particles or excitations. Decay of the excitation itself is a
fundamental error channel that is difficult to overcome via external drive or
control techniques. Quantum error correcting codes, which encode information in
superpositions involving multiple excitations, provide a path to preserve
information beyond the capacity of individual excitations, but typically
require exquisite active operations on the system. Here, we demonstrate a
steady-state driven dissipative quantum system, composed of a superconducting
cavity and a transmon ancilla, that preserves a logical qubit beyond the
photon-lifetime limit by about 5% using a binomial encoding. This realization
of continuous quantum error correction at the breakeven point highlights the
quantitative competitiveness of passive correction strategies while
circumventing some demanding hardware requirements of its active counterparts.


### First Observation of Dispersive Shock Waves in an Electron Beam
**Authors**: H. McCright, I. G. Abel, I. Haber, P. G. O'Shea, B. L. Beaudoin

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19786v1](http://arxiv.org/pdf/2510.19786v1)

**Abstract**: Dispersive shock waves (DSWs) are expanding nonlinear wave trains that arise
when dispersion regularizes a steepening front, a phenomenon observed in
fluids, plasmas, optics, and superfluids. Here we report the first experimental
observation of DSWs in an intense electron beam, using the University of
Maryland Electron Ring (UMER). A localized induction-cell perturbation produced
a negative density pulse that evolved into a leading soliton-like peak followed
by an expanding train of oscillations. The leading peak satisfied soliton
scaling laws for width^2 vs inverse amplitude and velocity vs amplitude, while
the total wave-train width increased linearly with time, consistent with
Korteweg--de Vries (KdV) predictions. Successive peaks showed decreasing
amplitude and velocity toward the trailing edge, in agreement with dispersive
shock ordering. These results demonstrate that intense charged particle beams
provide a new laboratory platform for studying dispersive hydrodynamics,
extending nonlinear wave physics into the high-intensity beam regime.


### Diffusion-Based Hierarchical Graph Neural Networks for Simulating Nonlinear Solid Mechanics
**Authors**: Tobias Würth, Niklas Freymuth, Gerhard Neumann, Luise Kärger

**Published Date**: 2025-06-06

**Updated Date**: 2025-10-22

**PDF Url**: [2506.06045v2](http://arxiv.org/pdf/2506.06045v2)

**Abstract**: Graph-based learned simulators have emerged as a promising approach for
simulating physical systems on unstructured meshes, offering speed and
generalization across diverse geometries. However, they often struggle with
capturing global phenomena, such as bending or long-range correlations usually
occurring in solid mechanics, and suffer from error accumulation over long
rollouts due to their reliance on local message passing and direct next-step
prediction. We address these limitations by introducing the Rolling
Diffusion-Batched Inference Network (ROBIN), a novel learned simulator that
integrates two key innovations: (i) Rolling Diffusion-Batched Inference (ROBI),
a parallelized inference scheme that amortizes the cost of diffusion-based
refinement across physical time steps by overlapping denoising steps across a
temporal window. (ii) A Hierarchical Graph Neural Network built on algebraic
multigrid coarsening, enabling multiscale message passing across different mesh
resolutions. This architecture, implemented via Algebraic-hierarchical Message
Passing Networks, captures both fine-scale local dynamics and global structural
effects critical for phenomena like beam bending or multi-body contact. We
validate ROBIN on challenging 2D and 3D solid mechanics benchmarks involving
geometric, material, and contact nonlinearities. ROBIN achieves
state-of-the-art accuracy on all tasks, substantially outperforming existing
next-step learned simulators while reducing inference time by up to an order of
magnitude compared to standard diffusion simulators.


### Training-Free Constrained Generation With Stable Diffusion Models
**Authors**: Stefano Zampini, Jacob K. Christopher, Luca Oneto, Davide Anguita, Ferdinando Fioretto

**Published Date**: 2025-02-08

**Updated Date**: 2025-10-22

**PDF Url**: [2502.05625v4](http://arxiv.org/pdf/2502.05625v4)

**Abstract**: Stable diffusion models represent the state-of-the-art in data synthesis
across diverse domains and hold transformative potential for applications in
science and engineering, e.g., by facilitating the discovery of novel solutions
and simulating systems that are computationally intractable to model
explicitly. While there is increasing effort to incorporate physics-based
constraints into generative models, existing techniques are either limited in
their applicability to latent diffusion frameworks or lack the capability to
strictly enforce domain-specific constraints. To address this limitation this
paper proposes a novel integration of stable diffusion models with constrained
optimization frameworks, enabling the generation of outputs satisfying
stringent physical and functional requirements. The effectiveness of this
approach is demonstrated through material design experiments requiring
adherence to precise morphometric properties, challenging inverse design tasks
involving the generation of materials inducing specific stress-strain
responses, and copyright-constrained content generation tasks. All code has
been released at
https://github.com/RAISELab-atUVA/Constrained-Stable-Diffusion.


### Committors without Descriptors
**Authors**: Peilin Kang, Jintu Zhang, Enrico Trizio, TingJun Hou, Michele Parrinello

**Published Date**: 2025-10-20

**Updated Date**: 2025-10-22

**PDF Url**: [2510.18018v2](http://arxiv.org/pdf/2510.18018v2)

**Abstract**: The study of rare events is one of the major challenges in atomistic
simulations, and several enhanced sampling methods towards its solution have
been proposed. Recently, it has been suggested that the use of the committor,
which provides a precise formal description of rare events, could be of use in
this context. We have recently followed up on this suggestion and proposed a
committor-based method that promotes frequent transitions between the
metastable states of the system and allows extensive sampling of the process
transition state ensemble. One of the strengths of our approach is being
self-consistent and semi-automatic, exploiting a variational criterion to
iteratively optimize a neural-network-based parametrization of the committor,
which uses a set of physical descriptors as input. Here, we further automate
this procedure by combining our previous method with the expressive power of
graph neural networks, which can directly process atomic coordinates rather
than descriptors. Besides applications on benchmark systems, we highlight the
advantages of a graph-based approach in describing the role of solvent
molecules in systems, such as ion pair dissociation or ligand binding.


### Coupling of neutrino beam-driven MHD waves and resonant instabilities in rotating magnetoplasmas with neutrino two-flavor oscillations
**Authors**: Jyoti Turi, Amar P. Misra

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19729v1](http://arxiv.org/pdf/2510.19729v1)

**Abstract**: We present an analysis of neutrino-driven magnetohydrodynamic (MHD) waves and
instabilities in a rotating magnetoplasma with weak neutrino interactions. We
show, for the first time, that neutrino-driven shear Alfv{\'e}n and oblique
magnetosonic waves can be coupled by the Coriolis force, forming new wave modes
affected by this force, as well as neutrino beam and two neutrino flavor
oscillations. Our work extends previous theories by demonstrating that shear
Alfv{\'e}n waves are influenced by neutrino effects and by identifying
instabilities resulting from resonant interactions with both a streaming
neutrino beam and flavor oscillations. We find that the Coriolis force, as well
as plasma density and magnetic field strength, have a significant impact on the
profiles of the instability growth rates. Our findings may shed new light on
the physical mechanisms underlying core-collapse supernovae.


### Classical theories of gravity produce entanglement
**Authors**: Joseph Aziz, Richard Howl

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19714v1](http://arxiv.org/pdf/2510.19714v1)

**Abstract**: The unification of gravity and quantum mechanics remains one of the most
profound open questions in science. With recent advances in quantum technology,
an experimental idea first proposed by Richard Feynman is now regarded as a
promising route to testing this unification for the first time. The experiment
involves placing a massive object in a quantum superposition of two locations
and letting it gravitationally interact with another mass. If the two objects
subsequently become entangled, this is considered unambiguous evidence that
gravity obeys the laws of quantum mechanics. This conclusion derives from
theorems that treat a classical gravitational interaction as a local
interaction capable of only transmitting classical, not quantum, information.
Here, we extend the description of the gravitational interaction used in these
theorems to the full framework of quantum field theory, finding that theories
with classical gravity can then transmit quantum information, and thus generate
entanglement through physical, local processes. The effect scales differently
to that predicted by theories of quantum gravity, providing information on the
parameters and form of the experiment required to robustly evidence the quantum
nature of gravity.


### Modification of ion-temperature-gradient turbulence by impurities in stellarator plasmas
**Authors**: Ivan Calvo, Felix I. Parra, Hanne Thienpondt, Jose Manuel Garcia-Regaña

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19690v1](http://arxiv.org/pdf/2510.19690v1)

**Abstract**: Recent nonlinear gyrokinetic simulations have shown that impurities can
strongly modify the turbulent heat flux in stellarator plasmas. Here, the
ion-temperature-gradient (ITG) dispersion relation in a plasma containing
impurities is analytically solved in certain limits and an expression for the
modification of the ITG growth rate by impurities is derived. The analytical
expression is the sum of three terms corresponding to three different physical
causes (impurity density gradient, impurity temperature gradient and dilution)
of the change in the growth rate. The scalings predicted analytically for the
modification of the growth rate are shown to be reproduced by linear
gyrokinetic simulations. The conditions for reduction or increase of the ITG
growth by impurities are also correctly predicted by the analytical solution to
the dispersion relation. Finally, a remarkable correlation is found between the
analytical expression for the modification of the growth rate and the
modification of the turbulent heat flux obtained from nonlinear gyrokinetic
simulations.


### Collisional Excitation in Space: Recent Advances and Future Challenges in the JWST Era
**Authors**: Francesca Tonolo

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19686v1](http://arxiv.org/pdf/2510.19686v1)

**Abstract**: This perspective offers a viewpoint on how the challenges of molecular
scattering investigations of astrophysical interest have evolved in recent
years. Computational progress has steadily expanded collisional databases and
provided essential tools for modeling non-LTE astronomical regions. However,
the observational leap enabled by the JWST and new observational facilities has
revealed critical gaps in these databases. In this framework, two major
frontiers emerge: the characterization of collisional processes involving heavy
projectiles, and the treatment of ro-vibrational excitation. The significant
computational effort of these investigations emphasizes the need to test and
develop robust theoretical methods and approximations, capable of extending the
census of collisional coefficients required for reliable astrophysical
modeling. Recent developments in these directions are outlined, with particular
attention to their application and their potential to broaden the coverage of
molecular systems and physical environments.


### AeroDiT: Diffusion Transformers for Reynolds-Averaged Navier-Stokes Simulations of Airfoil Flows
**Authors**: Chunyang Wang, Biyue Pan, Zhibo Dai, Yudi Cai, Yuhao Ma, Hao Zheng, Dixia Fan, Hui Xiang

**Published Date**: 2024-12-23

**Updated Date**: 2025-10-22

**PDF Url**: [2412.17394v4](http://arxiv.org/pdf/2412.17394v4)

**Abstract**: Real-time and accurate prediction of aerodynamic flow fields around airfoils
is crucial for flow control and aerodynamic optimization. However, achieving
this remains challenging due to the high computational costs and the non-linear
nature of flow physics. Traditional Computational Fluid Dynamics (CFD) methods
face limitations in balancing computational efficiency and accuracy, hindering
their application in real-time scenarios. To address these challenges, this
study presents AeroDiT, a novel surrogate model that integrates scalable
diffusion models with transformer architectures to address these challenges.
Trained on Reynolds-Averaged Navier-Stokes (RANS) simulation data for high
Reynolds-number airfoil flows, AeroDiT accurately captures complex flow
patterns while enabling real-time predictions. The model demonstrates
impressive performance, with mean relative $L_2$ errors of 0.1, 0.025, and
0.050 for pressure $p$ and velocity components $u_x, u_y$, confirming its
reliability. To further enhance physical consistency, we incorporate explicit
physics-informed losses based on RANS residuals, including mass and momentum
conservation constraints. The transformer-based structure allows for real-time
predictions within seconds, enabling efficient aerodynamic simulations. This
work underscores the potential of generative machine learning techniques to
advance computational fluid dynamics, offering potential solutions to
challenges in simulating high-fidelity aerodynamic flows.


## Diffusion
### Graph Representation Learning with Diffusion Generative Models
**Authors**: Daniel Wesego

**Published Date**: 2025-01-22

**Updated Date**: 2025-10-22

**PDF Url**: [2501.13133v2](http://arxiv.org/pdf/2501.13133v2)

**Abstract**: Diffusion models have established themselves as state-of-the-art generative
models across various data modalities, including images and videos, due to
their ability to accurately approximate complex data distributions. Unlike
traditional generative approaches such as VAEs and GANs, diffusion models
employ a progressive denoising process that transforms noise into meaningful
data over multiple iterative steps. This gradual approach enhances their
expressiveness and generation quality. Not only that, diffusion models have
also been shown to extract meaningful representations from data while learning
to generate samples. Despite their success, the application of diffusion models
to graph-structured data remains relatively unexplored, primarily due to the
discrete nature of graphs, which necessitates discrete diffusion processes
distinct from the continuous methods used in other domains. In this work, we
leverage the representational capabilities of diffusion models to learn
meaningful embeddings for graph data. By training a discrete diffusion model
within an autoencoder framework, we enable both effective autoencoding and
representation learning tailored to the unique characteristics of
graph-structured data. We extract the representation from the combination of
the encoder's output and the decoder's first time step hidden embedding. Our
approach demonstrates the potential of discrete diffusion models to be used for
graph representation learning. The code can be found at
https://github.com/DanielMitiku/Graph-Representation-Learning-with-Diffusion-Generative-Models


### Are Modern Speech Enhancement Systems Vulnerable to Adversarial Attacks?
**Authors**: Rostislav Makarov, Lea Schönherr, Timo Gerkmann

**Published Date**: 2025-09-25

**Updated Date**: 2025-10-22

**PDF Url**: [2509.21087v2](http://arxiv.org/pdf/2509.21087v2)

**Abstract**: Machine learning approaches for speech enhancement are becoming increasingly
expressive, enabling ever more powerful modifications of input signals. In this
paper, we demonstrate that this expressiveness introduces a vulnerability:
advanced speech enhancement models can be susceptible to adversarial attacks.
Specifically, we show that adversarial noise, carefully crafted and
psychoacoustically masked by the original input, can be injected such that the
enhanced speech output conveys an entirely different semantic meaning. We
experimentally verify that contemporary predictive speech enhancement models
can indeed be manipulated in this way. Furthermore, we highlight that diffusion
models with stochastic samplers exhibit inherent robustness to such adversarial
attacks by design.


### A Survey on Cache Methods in Diffusion Models: Toward Efficient Multi-Modal Generation
**Authors**: Jiacheng Liu, Xinyu Wang, Yuqi Lin, Zhikai Wang, Peiru Wang, Peiliang Cai, Qinming Zhou, Zhengan Yan, Zexuan Yan, Zhengyi Shi, Chang Zou, Yue Ma, Linfeng Zhang

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19755v1](http://arxiv.org/pdf/2510.19755v1)

**Abstract**: Diffusion Models have become a cornerstone of modern generative AI for their
exceptional generation quality and controllability. However, their inherent
\textit{multi-step iterations} and \textit{complex backbone networks} lead to
prohibitive computational overhead and generation latency, forming a major
bottleneck for real-time applications. Although existing acceleration
techniques have made progress, they still face challenges such as limited
applicability, high training costs, or quality degradation.
  Against this backdrop, \textbf{Diffusion Caching} offers a promising
training-free, architecture-agnostic, and efficient inference paradigm. Its
core mechanism identifies and reuses intrinsic computational redundancies in
the diffusion process. By enabling feature-level cross-step reuse and
inter-layer scheduling, it reduces computation without modifying model
parameters. This paper systematically reviews the theoretical foundations and
evolution of Diffusion Caching and proposes a unified framework for its
classification and analysis.
  Through comparative analysis of representative methods, we show that
Diffusion Caching evolves from \textit{static reuse} to \textit{dynamic
prediction}. This trend enhances caching flexibility across diverse tasks and
enables integration with other acceleration techniques such as sampling
optimization and model distillation, paving the way for a unified, efficient
inference framework for future multimodal and interactive applications. We
argue that this paradigm will become a key enabler of real-time and efficient
generative AI, injecting new vitality into both theory and practice of
\textit{Efficient Generative Intelligence}.


### Beyond Masked and Unmasked: Discrete Diffusion Models via Partial Masking
**Authors**: Chen-Hao Chao, Wei-Fang Sun, Hanwen Liang, Chun-Yi Lee, Rahul G. Krishnan

**Published Date**: 2025-05-24

**Updated Date**: 2025-10-22

**PDF Url**: [2505.18495v2](http://arxiv.org/pdf/2505.18495v2)

**Abstract**: Masked diffusion models (MDM) are powerful generative models for discrete
data that generate samples by progressively unmasking tokens in a sequence.
Each token can take one of two states: masked or unmasked. We observe that
token sequences often remain unchanged between consecutive sampling steps;
consequently, the model repeatedly processes identical inputs, leading to
redundant computation. To address this inefficiency, we propose the Partial
masking scheme (Prime), which augments MDM by allowing tokens to take
intermediate states interpolated between the masked and unmasked states. This
design enables the model to make predictions based on partially observed token
information, and facilitates a fine-grained denoising process. We derive a
variational training objective and introduce a simple architectural design to
accommodate intermediate-state inputs. Our method demonstrates superior
performance across a diverse set of generative modeling tasks. On text data, it
achieves a perplexity of 15.36 on OpenWebText, outperforming previous MDM
(21.52), autoregressive models (17.54), and their hybrid variants (17.58),
without relying on an autoregressive formulation. On image data, it attains
competitive FID scores of 3.26 on CIFAR-10 and 6.98 on ImageNet-32, comparable
to leading continuous generative models.


## Quantitative Finance
### Quantum Machine Learning methods for Fourier-based distribution estimation with application in option pricing
**Authors**: Fernando Alonso, Álvaro Leitao, Carlos Vázquez

**Published Date**: 2025-10-22

**Updated Date**: 2025-10-22

**PDF Url**: [2510.19494v1](http://arxiv.org/pdf/2510.19494v1)

**Abstract**: The ongoing progress in quantum technologies has fueled a sustained
exploration of their potential applications across various domains. One
particularly promising field is quantitative finance, where a central challenge
is the pricing of financial derivatives-traditionally addressed through Monte
Carlo integration techniques. In this work, we introduce two hybrid
classical-quantum methods to address the option pricing problem. These
approaches rely on reconstructing Fourier series representations of statistical
distributions from the outputs of Quantum Machine Learning (QML) models based
on Parametrized Quantum Circuits (PQCs). We analyze the impact of data size and
PQC dimensionality on performance. Quantum Accelerated Monte Carlo (QAMC) is
employed as a benchmark to quantitatively assess the proposed models in terms
of computational cost and accuracy in the extraction of Fourier coefficients.
Through the numerical experiments, we show that the proposed methods achieve
remarkable accuracy, becoming a competitive quantum alternative for derivatives
valuation.


