# Abstracts of Papers

## Physics
### A domain decomposition-based autoregressive deep learning model for unsteady and nonlinear partial differential equations
**Authors**: Sheel Nidhan, Haoliang Jiang, Lalit Ghule, Clancy Umphrey, Rishikesh Ranade, Jay Pathak

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14461v1](http://arxiv.org/pdf/2408.14461v1)

**Abstract**: In this paper, we propose a domain-decomposition-based deep learning (DL)
framework, named transient-CoMLSim, for accurately modeling unsteady and
nonlinear partial differential equations (PDEs). The framework consists of two
key components: (a) a convolutional neural network (CNN)-based autoencoder
architecture and (b) an autoregressive model composed of fully connected
layers. Unlike existing state-of-the-art methods that operate on the entire
computational domain, our CNN-based autoencoder computes a lower-dimensional
basis for solution and condition fields represented on subdomains. Timestepping
is performed entirely in the latent space, generating embeddings of the
solution variables from the time history of embeddings of solution and
condition variables. This approach not only reduces computational complexity
but also enhances scalability, making it well-suited for large-scale
simulations. Furthermore, to improve the stability of our rollouts, we employ a
curriculum learning (CL) approach during the training of the autoregressive
model. The domain-decomposition strategy enables scaling to out-of-distribution
domain sizes while maintaining the accuracy of predictions -- a feature not
easily integrated into popular DL-based approaches for physics simulations. We
benchmark our model against two widely-used DL architectures, Fourier Neural
Operator (FNO) and U-Net, and demonstrate that our framework outperforms them
in terms of accuracy, extrapolation to unseen timesteps, and stability for a
wide range of use cases.


### Partitioning statistics of a correlated few-electron droplet
**Authors**: Jashwanth Shaju, Elina Pavlovska, Ralfs Suba, Junliang Wang, Seddik Ouacel, Thomas Vasselon, Matteo Aluffi, Lucas Mazzella, Clement Geffroy, Arne Ludwig, Andreas D. Wieck, Matias Urdampiletta, Christopher Bäuerle, Vyacheslavs Kashcheyevs, Hermann Sellier

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14458v1](http://arxiv.org/pdf/2408.14458v1)

**Abstract**: Emergence of universal collective behaviour from interactions in a
sufficiently large group of elementary constituents is a fundamental scientific
paradigm. In physics, correlations in fluctuating microscopic observables can
provide key information about collective states of matter such as deconfined
quark-gluon plasma in heavy-ion collisions or expanding quantum degenerate
gases. Two-particle correlations in mesoscopic colliders have provided
smoking-gun evidence on the nature of exotic electronic excitations such as
fractional charges, levitons and anyon statistics. Yet the gap between
two-particle collisions and the emergence of collectivity as the number of
interacting particles grows is hard to address at the microscopic level. Here,
we demonstrate all-body correlations in the partitioning of up to $N = 5$
electron droplets driven by a moving potential well through a Y-junction in a
semiconductor. We show that the measured multivariate cumulants (of order $k =
2$ to $N$) of the electron droplet are accurately described by $k$-spin
correlation functions of an effective Ising model below the N\'eel temperature
and can be interpreted as a Coulomb liquid in the thermodynamic limit. Finite
size scaling of high-order correlation functions provides otherwise
inaccessible fingerprints of emerging order. Our demonstration of emergence in
a simple correlated electron collider opens a new way to study engineered
states of matter.


### Detecting Quantum and Classical Phase Transitions via Unsupervised Machine Learning of the Fisher Information Metric
**Authors**: Victor Kasatkin, Evgeny Mozgunov, Nicholas Ezzell, Daniel Lidar

**Published Date**: 2024-08-06

**Updated Date**: 2024-08-26

**PDF Url**: [2408.03418v2](http://arxiv.org/pdf/2408.03418v2)

**Abstract**: The detection of quantum and classical phase transitions in the absence of an
order parameter is possible using the Fisher information metric (FIM), also
known as fidelity susceptibility. Here, we propose and investigate an
unsupervised machine learning (ML) task: estimating the FIM given limited
samples from a multivariate probability distribution of measurements made
throughout the phase diagram. We utilize an unsupervised ML method called
ClassiFIM (developed in a companion paper) to solve this task and demonstrate
its empirical effectiveness in detecting both quantum and classical phase
transitions using a variety of spin and fermionic models, for which we generate
several publicly available datasets with accompanying ground-truth FIM. We find
that ClassiFIM reliably detects both topological (e.g., XXZ chain) and
dynamical (e.g., metal-insulator transition in Hubbard model) quantum phase
transitions. We perform a detailed quantitative comparison with prior
unsupervised ML methods for detecting quantum phase transitions. We demonstrate
that ClassiFIM is competitive with these prior methods in terms of appropriate
accuracy metrics while requiring significantly less resource-intensive training
data compared to the original formulation of the prior methods. In particular,
ClassiFIM only requires classical (single-basis) measurements. As part of our
methodology development, we prove several theorems connecting the classical and
quantum fidelity susceptibilities through equalities or bounds. We also
significantly expand the existence conditions of the fidelity susceptibility,
e.g., by relaxing standard differentiability conditions. These results may be
of independent interest to the mathematical physics community.


### Quantizing a Non-locally Massive 2-form Model
**Authors**: Kumar Abhinav

**Published Date**: 2023-10-27

**Updated Date**: 2024-08-26

**PDF Url**: [2310.18272v2](http://arxiv.org/pdf/2310.18272v2)

**Abstract**: A non-local yet gauge-invariantly massive 2-form model is considered that
leads to local and unitary dynamics upon proper gauge-fixing. Since canonical
momenta cannot be defined owing to the non-locality, consistent quantization of
this system warrants particular care. We construct the Dirac brackets and
covariant commutators for this model, followed by its path integral
quantization, leading to consistent results. These treatments underline the
most efficient way to extract the physical modes and the subsequent spectrum
free from infrared ambiguity. Physically the massive 2-form represents a spin-1
excitation, with potential application to string theory and cosmology, that can
mediate a screened interaction when topologically coupled to fermions.


### Relaxation dynamics in the (double) sine-Gordon model -- an open-system viewpoint
**Authors**: D. Szász-Schagrin, D. X. Horváth, G. Takács

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14428v1](http://arxiv.org/pdf/2408.14428v1)

**Abstract**: We study the effects of integrability breaking on the relaxation dynamics of
the (double) sine-Gordon model. Compared to previous studies, we apply an
alternative viewpoint motivated by open-system physics by separating the phase
field into homogeneous and inhomogeneous parts, describing a quantum pendulum
(subsystem) and an interacting phononic bath (environment). To study the
relaxation dynamics in the model, we perform quantum quenches using the
mini-superspace-based truncated Hamiltonian approach developed recently and
simulate the real-time evolution of various entanglement measures and the
energy transfer between the subsystem and its environment. Our findings
demonstrate that in the presence of integrability-breaking perturbations, the
relaxation dynamics is substantially faster, signalled by the increase of
entanglement and energy transfer between the quantum pendulum and the phonon
bath.


### Spectrally Informed Learning of Fluid Flows
**Authors**: Benjamin D. Shaffer, Jeremy R. Vorenberg, M. Ani Hsieh

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14407v1](http://arxiv.org/pdf/2408.14407v1)

**Abstract**: Accurate and efficient fluid flow models are essential for applications
relating to many physical phenomena including geophysical, aerodynamic, and
biological systems. While these flows may exhibit rich and multiscale dynamics,
in many cases underlying low-rank structures exist which describe the bulk of
the motion. These structures tend to be spatially large and temporally slow,
and may contain most of the energy in a given flow. The extraction and
parsimonious representation of these low-rank dynamics from high-dimensional
data is a key challenge. Inspired by the success of physics-informed machine
learning methods, we propose a spectrally-informed approach to extract low-rank
models of fluid flows by leveraging known spectral properties in the learning
process. We incorporate this knowledge by imposing regularizations on the
learned dynamics, which bias the training process towards learning
low-frequency structures with corresponding higher power. We demonstrate the
effectiveness of this method to improve prediction and produce learned models
which better match the underlying spectral properties of prototypical fluid
flows.


### Linear-optical quantum computation with arbitrary error-correcting codes
**Authors**: Blayney W. Walshe, Ben Q. Baragiola, Hugo Ferretti, José Gefaell, Michael Vasmer, Ryohei Weil, Takaya Matsuura, Thomas Jaeken, Giacomo Pantaleoni, Zhihua Han, Timo Hillmann, Nicolas C. Menicucci, Ilan Tzitrin, Rafael N. Alexander

**Published Date**: 2024-08-07

**Updated Date**: 2024-08-26

**PDF Url**: [2408.04126v2](http://arxiv.org/pdf/2408.04126v2)

**Abstract**: High-rate quantum error correcting codes mitigate the imposing scale of
fault-tolerant quantum computers but require the efficient generation of
non-local many-body entanglement. We provide a linear-optical architecture with
these properties, compatible with arbitrary codes and Gottesman-Kitaev-Preskill
qubits on generic lattices, and featuring a natural way to leverage physical
noise bias. Simulations involving hyperbolic surface codes, promising quantum
low-density parity-check codes, reveal a threshold comparable to the 2D surface
code at about a ten-fold improvement in encoding rate.


### Extended Uncertainty Principle via Dirac Quantization
**Authors**: Mytraya Gattu, S. Shankaranarayanan

**Published Date**: 2022-04-04

**Updated Date**: 2024-08-26

**PDF Url**: [2204.01780v2](http://arxiv.org/pdf/2204.01780v2)

**Abstract**: Unifying quantum theory and gravity remains a fundamental challenge in
physics. While most existing literature focuses on the ultraviolet (UV)
modifications of quantum theory due to gravity, this work shows that generic
infrared (IR) modifications arise when we describe quantum theory in curved
spacetime. We explicitly demonstrate that the modifications to the
position-momentum algebra are proportional to curvature invariants (such as the
Ricci scalar and Kretschmann scalar). Our results, derived through a rigorous
application of Dirac's quantization procedure, demonstrate that infrared
effects in quantum systems can be axiomatically derived. We study particle
dynamics in an arbitrary curved spacetime by embedding them in a
higher-dimensional flat geometry. Our approach, which involves embedding
particle dynamics in a higher-dimensional flat geometry and utilizing Dirac's
quantization procedure, allows us to capture the dynamics of a particle in
4-dimensional curved spacetime through a modified position-momentum algebra.
When applied to various spacetimes, this method reveals that the corrections
due to the spacetime curvature are universal. We further compare our results
with those derived using extended uncertainty principles. Finally, we discuss
the implications of our work for black holes and entanglement.


### Dimension-eight Operator Basis for Universal Standard Model Effective Field Theory
**Authors**: Tyler Corbett, Jay Desai, O. J. P. Eboli, M. C. Gonzalez-Garcia

**Published Date**: 2024-04-04

**Updated Date**: 2024-08-26

**PDF Url**: [2404.03720v2](http://arxiv.org/pdf/2404.03720v2)

**Abstract**: We present the basis of dimension-eight operators associated with universal
theories. We first derive a complete list of independent dimension-eight
operators formed with the Standard Model bosonic fields characteristic of such
universal new physics scenarios. Without imposing C or P symmetries the basis
contains 175 operators -- that is, the assumption of Universality reduces the
number of independent SMEFT coefficients at dimension eight from 44807 to 175.
89 of the 175 universal operators are included in the general dimension-eight
operator basis in the literature. The 86 additional operators involve higher
derivatives of the Standard Model bosonic fields and can be rotated in favor of
operators involving fermions using the Standard Model equations of motion for
the bosonic fields. By doing so we obtain the allowed fermionic operators
generated in this class of models which we map into the corresponding 86
independent combinations of operators in the dimension-eight basis of Ref.
arXiv:2005.00059


### Nucleon Transversity from lattice QCD
**Authors**: Constantia Alexandrou

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14370v1](http://arxiv.org/pdf/2408.14370v1)

**Abstract**: We give a brief overview of recent progress in lattice QCD simulations that
is enabling precision studies of the three-dimensional structure of the
nucleon. We present results on nucleon charges and second Mellin moments of
parton distribution functions and generalized parton distributions,
highlighting results obtained at the continuum limit using only gauge ensembles
simulated with physical quark masses. The tensor charge and transversity
moments are determined with controlled systematics and used to extract nucleon
transverse density distributions. We also discuss progress towards the direct
evaluation of generalized parton distributions in lattice QCD and the impact
they are having on phenomenology.


## Diffusion
### Application of Neural Ordinary Differential Equations for ITER Burning Plasma Dynamics
**Authors**: Zefang Liu, Weston M. Stacey

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14404v1](http://arxiv.org/pdf/2408.14404v1)

**Abstract**: The dynamics of burning plasmas in tokamaks are crucial for advancing
controlled thermonuclear fusion. This study introduces the NeuralPlasmaODE, a
multi-region multi-timescale transport model to simulate the complex energy
transfer processes in ITER deuterium-tritium (D-T) plasmas. Our model captures
the interactions between energetic alpha particles, electrons, and ions, which
are vital for understanding phenomena such as thermal runaway instability. We
employ neural ordinary differential equations (Neural ODEs) for the numerical
derivation of diffusivity parameters, enabling precise modeling of energy
interactions between different plasma regions. By leveraging transfer learning,
we utilize model parameters derived from DIII-D experimental data, enhancing
the efficiency and accuracy of our simulations without training from scratch.
Applying this model to ITER's inductive and non-inductive operational
scenarios, our results demonstrate that radiation and transport processes
effectively remove excess heat from the core plasma, preventing thermal runaway
instability. This study underscores the potential of machine learning in
advancing our understanding and control of burning plasma dynamics in fusion
reactors.


### GR-MG: Leveraging Partially Annotated Data via Multi-Modal Goal Conditioned Policy
**Authors**: Peiyan Li, Hongtao Wu, Yan Huang, Chilam Cheang, Liang Wang, Tao Kong

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14368v1](http://arxiv.org/pdf/2408.14368v1)

**Abstract**: The robotics community has consistently aimed to achieve generalizable robot
manipulation with flexible natural language instructions. One of the primary
challenges is that obtaining robot data fully annotated with both actions and
texts is time-consuming and labor-intensive. However, partially annotated data,
such as human activity videos without action labels and robot play data without
language labels, is much easier to collect. Can we leverage these data to
enhance the generalization capability of robots? In this paper, we propose
GR-MG, a novel method which supports conditioning on both a language
instruction and a goal image. During training, GR-MG samples goal images from
trajectories and conditions on both the text and the goal image or solely on
the image when text is unavailable. During inference, where only the text is
provided, GR-MG generates the goal image via a diffusion-based image-editing
model and condition on both the text and the generated image. This approach
enables GR-MG to leverage large amounts of partially annotated data while still
using language to flexibly specify tasks. To generate accurate goal images, we
propose a novel progress-guided goal image generation model which injects task
progress information into the generation process, significantly improving the
fidelity and the performance. In simulation experiments, GR-MG improves the
average number of tasks completed in a row of 5 from 3.35 to 4.04. In
real-robot experiments, GR-MG is able to perform 47 different tasks and
improves the success rate from 62.5% to 75.0% and 42.4% to 57.6% in simple and
generalization settings, respectively. Code and checkpoints will be available
at the project page: https://gr-mg.github.io/.


### Foundation Models for Music: A Survey
**Authors**: Yinghao Ma, Anders Øland, Anton Ragni, Bleiz MacSen Del Sette, Charalampos Saitis, Chris Donahue, Chenghua Lin, Christos Plachouras, Emmanouil Benetos, Elio Quinton, Elona Shatri, Fabio Morreale, Ge Zhang, György Fazekas, Gus Xia, Huan Zhang, Ilaria Manco, Jiawen Huang, Julien Guinot, Liwei Lin, Luca Marinelli, Max W. Y. Lam, Megha Sharma, Qiuqiang Kong, Roger B. Dannenberg, Ruibin Yuan, Shangda Wu, Shih-Lun Wu, Shuqi Dai, Shun Lei, Shiyin Kang, Simon Dixon, Wenhu Chen, Wehhao Huang, Xingjian Du, Xingwei Qu, Xu Tan, Yizhi Li, Zeyue Tian, Zhiyong Wu, Zhizheng Wu, Ziyang Ma, Ziyu Wang

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14340v1](http://arxiv.org/pdf/2408.14340v1)

**Abstract**: In recent years, foundation models (FMs) such as large language models (LLMs)
and latent diffusion models (LDMs) have profoundly impacted diverse sectors,
including music. This comprehensive review examines state-of-the-art (SOTA)
pre-trained models and foundation models in music, spanning from representation
learning, generative learning and multimodal learning. We first contextualise
the significance of music in various industries and trace the evolution of AI
in music. By delineating the modalities targeted by foundation models, we
discover many of the music representations are underexplored in FM development.
Then, emphasis is placed on the lack of versatility of previous methods on
diverse music applications, along with the potential of FMs in music
understanding, generation and medical application. By comprehensively exploring
the details of the model pre-training paradigm, architectural choices,
tokenisation, finetuning methodologies and controllability, we emphasise the
important topics that should have been well explored, like instruction tuning
and in-context learning, scaling law and emergent ability, as well as
long-sequence modelling etc. A dedicated section presents insights into music
agents, accompanied by a thorough analysis of datasets and evaluations
essential for pre-training and downstream tasks. Finally, by underscoring the
vital importance of ethical considerations, we advocate that following research
on FM for music should focus more on such issues as interpretability,
transparency, human responsibility, and copyright issues. The paper offers
insights into future challenges and trends on FMs for music, aiming to shape
the trajectory of human-AI collaboration in the music realm.


### Streamline tractography of the fetal brain in utero with machine learning
**Authors**: Weide Liu, Camilo Calixto, Simon K. Warfield, Davood Karimi

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14326v1](http://arxiv.org/pdf/2408.14326v1)

**Abstract**: Diffusion-weighted magnetic resonance imaging (dMRI) is the only non-invasive
tool for studying white matter tracts and structural connectivity of the brain.
These assessments rely heavily on tractography techniques, which reconstruct
virtual streamlines representing white matter fibers. Much effort has been
devoted to improving tractography methodology for adult brains, while
tractography of the fetal brain has been largely neglected. Fetal tractography
faces unique difficulties due to low dMRI signal quality, immature and rapidly
developing brain structures, and paucity of reference data. This work presents
the first machine learning model for fetal tractography. The model input
consists of five sources of information: (1) Fiber orientation, inferred from a
diffusion tensor fit to the dMRI signal; (2) Directions of recent propagation
steps; (3) Global spatial information, encoded as distances to keypoints in the
brain cortex; (4) Tissue segmentation information; and (5) Prior information
about the expected local fiber orientations supplied with an atlas. In order to
mitigate the local tensor estimation error, a large spatial context around the
current point in the diffusion tensor image is encoded using convolutional and
attention neural network modules. Moreover, the diffusion tensor information at
a hypothetical next point is included in the model input. Filtering rules based
on anatomically constrained tractography are applied to prune implausible
streamlines. We trained the model on manually-refined whole-brain fetal
tractograms and validated the trained model on an independent set of 11 test
scans with gestational ages between 23 and 36 weeks. Results show that our
proposed method achieves superior performance across all evaluated tracts. The
new method can significantly advance the capabilities of dMRI for studying
normal and abnormal brain development in utero.


### Integrated Brain Connectivity Analysis with fMRI, DTI, and sMRI Powered by Interpretable Graph Neural Networks
**Authors**: Gang Qu, Ziyu Zhou, Vince D. Calhoun, Aiying Zhang, Yu-Ping Wang

**Published Date**: 2024-08-26

**Updated Date**: 2024-08-26

**PDF Url**: [2408.14254v1](http://arxiv.org/pdf/2408.14254v1)

**Abstract**: Multimodal neuroimaging modeling has becomes a widely used approach but
confronts considerable challenges due to heterogeneity, which encompasses
variability in data types, scales, and formats across modalities. This
variability necessitates the deployment of advanced computational methods to
integrate and interpret these diverse datasets within a cohesive analytical
framework. In our research, we amalgamate functional magnetic resonance
imaging, diffusion tensor imaging, and structural MRI into a cohesive
framework. This integration capitalizes on the unique strengths of each
modality and their inherent interconnections, aiming for a comprehensive
understanding of the brain's connectivity and anatomical characteristics.
Utilizing the Glasser atlas for parcellation, we integrate imaging derived
features from various modalities: functional connectivity from fMRI, structural
connectivity from DTI, and anatomical features from sMRI within consistent
regions. Our approach incorporates a masking strategy to differentially weight
neural connections, thereby facilitating a holistic amalgamation of multimodal
imaging data. This technique enhances interpretability at connectivity level,
transcending traditional analyses centered on singular regional attributes. The
model is applied to the Human Connectome Project's Development study to
elucidate the associations between multimodal imaging and cognitive functions
throughout youth. The analysis demonstrates improved predictive accuracy and
uncovers crucial anatomical features and essential neural connections,
deepening our understanding of brain structure and function.


