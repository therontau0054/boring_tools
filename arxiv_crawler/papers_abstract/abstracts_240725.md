# Abstracts of Papers

## Physics
### Quantum error-correcting codes with a covariant encoding
**Authors**: Aurélie Denys, Anthony Leverrier

**Published Date**: 2023-06-20

**Updated Date**: 2024-07-24

**PDF Url**: [2306.11621v4](http://arxiv.org/pdf/2306.11621v4)

**Abstract**: Given some group $G$ of logical gates, for instance the Clifford group, what
are the quantum encodings for which these logical gates can be implemented by
simple physical operations, described by some physical representation of $G$?
We study this question by constructing a general form of such encoding maps.
For instance, we recover that the $[[5,1,3]]$ and Steane codes admit
transversal implementations of the binary tetrahedral and binary octahedral
groups, respectively. For bosonic encodings, we show how to obtain the GKP and
cat qudit encodings by considering the appropriate groups, and essentially the
simplest physical implementations. We further illustrate this approach by
introducing a 2-mode bosonic code defined from a constellation of 48 coherent
states, for which all single-qubit Clifford gates correspond to passive
Gaussian unitaries.


### Investigating Resource-efficient Neutron/Gamma Classification ML Models Targeting eFPGAs
**Authors**: Jyothisraj Johnson, Billy Boxer, Tarun Prakash, Carl Grace, Peter Sorensen, Mani Tripathi

**Published Date**: 2024-04-19

**Updated Date**: 2024-07-24

**PDF Url**: [2404.14436v2](http://arxiv.org/pdf/2404.14436v2)

**Abstract**: There has been considerable interest and resulting progress in implementing
machine learning (ML) models in hardware over the last several years from the
particle and nuclear physics communities. A big driver has been the release of
the Python package, hls4ml, which has enabled porting models specified and
trained using Python ML libraries to register transfer level (RTL) code. So
far, the primary end targets have been commercial FPGAs or synthesized custom
blocks on ASICs. However, recent developments in open-source embedded FPGA
(eFPGA) frameworks now provide an alternate, more flexible pathway for
implementing ML models in hardware. These customized eFPGA fabrics can be
integrated as part of an overall chip design. In general, the decision between
a fully custom, eFPGA, or commercial FPGA ML implementation will depend on the
details of the end-use application. In this work, we explored the parameter
space for eFPGA implementations of fully-connected neural network (fcNN) and
boosted decision tree (BDT) models using the task of neutron/gamma
classification with a specific focus on resource efficiency. We used data
collected using an AmBe sealed source incident on Stilbene, which was optically
coupled to an OnSemi J-series SiPM to generate training and test data for this
study. We investigated relevant input features and the effects of
bit-resolution and sampling rate as well as trade-offs in hyperparameters for
both ML architectures while tracking total resource usage. The performance
metric used to track model performance was the calculated neutron efficiency at
a gamma leakage of 10$^{-3}$. The results of the study will be used to aid the
specification of an eFPGA fabric, which will be integrated as part of a test
chip.


### Search for heavy Majorana neutrinos in $e^{\pm} e^{\pm}$ and $e^{\pm} μ^{\pm}$ final states via WW scattering in $pp$ collisions at $\sqrt{s}=13$ TeV with the ATLAS detector
**Authors**: ATLAS Collaboration

**Published Date**: 2024-03-22

**Updated Date**: 2024-07-24

**PDF Url**: [2403.15016v2](http://arxiv.org/pdf/2403.15016v2)

**Abstract**: A search for heavy Majorana neutrinos in scattering of same-sign $W$ boson
pairs in proton-proton collisions at $\sqrt{s}= 13$ TeV at the LHC is reported.
The dataset used corresponds to an integrated luminosity of 140 fb$^{-1}$,
collected with the ATLAS detector during 2015-2018. The search is performed in
final states including a same-sign $ee$ or $e\mu$ pair and at least two jets
with large invariant mass and a large rapidity difference. No significant
excess of events with respect to the Standard Model background predictions is
observed. The results are interpreted in a benchmark scenario of the
Phenomenological Type-I Seesaw model. New constraints are set on the values of
the $\vert V_{e N} \vert^{2}$ and $\vert V_{e N} V^{*}_{\mu N} \vert$
parameters for heavy Majorana neutrino masses between 50 GeV and 20 TeV, where
$V_{\ell N}$ is the matrix element describing the mixing of the heavy Majorana
neutrino mass eigenstate with the Standard Model neutrino of flavour $\ell = e,
\mu$. The sensitivity to the Weinberg operator is investigated and constraints
on the effective $ee$ and $e\mu$ Majorana neutrino masses are reported. The
statistical combination of the $ee$ and $e\mu$ channels with the previously
published $\mu\mu$ channel is performed.


### Gender disparities in the dissemination and acquisition of scientific knowledge
**Authors**: Chiara Zappalà, Luca Gallo, Jan Bachmann, Federico Battiston, Fariba Karimi

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17441v1](http://arxiv.org/pdf/2407.17441v1)

**Abstract**: Recent research has challenged the widespread belief that gender inequities
in academia would disappear simply by increasing the number of women. More
complex causes might be at play, embodied in the networked structure of
scientific collaborations. Here, we aim to understand the structural inequality
between male and female scholars in the dissemination of scientific knowledge.
We use a large-scale dataset of academic publications from the American
Physical Society (APS) to build a time-varying network of collaborations from
1970 to 2020. We model knowledge dissemination as a contagion process in which
scientists become informed based on the propagation of knowledge through their
collaborators. We quantify the fairness of the system in terms of how women
acquire and diffuse knowledge compared to men. Our results indicate that
knowledge acquisition and diffusion are slower for women than expected. We find
that the main determinant of women's disadvantage is the gap in the cumulative
number of collaborators, highlighting how time creates structural disadvantages
that contribute to marginalize women in physics. Our work sheds light on how
the dynamics of scientific collaborations shape gender disparities in knowledge
dissemination and calls for a deeper understanding on how to intervene to
improve fairness and diversity in the scientific community.


### Numerical evaluation of orientation averages and its application to molecular physics
**Authors**: Alexander Blech, Raoul M. M. Ebeling, Marec Heger, Christiane P. Koch, Daniel M. Reich

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17434v1](http://arxiv.org/pdf/2407.17434v1)

**Abstract**: In molecular physics, it is often necessary to average over the orientation
of molecules when calculating observables, in particular when modelling
experiments in the liquid or gas phase. Evaluated in terms of Euler angles,
this is closely related to integration over two- or three-dimensional unit
spheres, a common problem discussed in numerical analysis. The computational
cost of the integration depends significantly on the quadrature method, making
the selection of an appropriate method crucial for the feasibility of
simulations. After reviewing several classes of spherical quadrature methods in
terms of their efficiency and error distribution, we derive guidelines for
choosing the best quadrature method for orientation averages and illustrate
these with three examples from chiral molecule physics. While Gauss quadratures
allow for achieving numerically exact integration for a wide range of
applications, other methods offer advantages in specific circumstances. Our
guidelines can also by applied to higher-dimensional spherical domains and
other geometries. We also present a Python package providing a flexible
interface to a variety of quadrature methods.


### Physical limits on galvanotaxis depends on cell morphology and orientation
**Authors**: Ifunanya Nwogbaga, Brian A. Camley

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17420v1](http://arxiv.org/pdf/2407.17420v1)

**Abstract**: Galvanotaxis is believed to be driven by the redistribution of transmembrane
proteins and other molecules, referred to as "sensors", through electrophoresis
and electroosmosis. Here, we update our previous model of the limits of
galvanotaxis due to stochasticity of sensor movements to account for cell shape
and orientation. Computing the Fisher information, we find that cells in
principle possess more information about the electric field direction when
their long axis is parallel to the field, but that for weak fields
maximum-likelihood estimators of the field direction may actually have lower
variability when the cell's long axis is perpendicular to the field. In an
alternate possibility, we find that if cells instead estimate the field
direction by taking the average of all the sensor locations as its directional
cue ("vector sum"), this introduces a bias towards the short axis, an effect
not present for isotropic cells. We also explore the possibility that cell
elongation arises downstream of sensor redistribution. We argue that if sensors
migrate to the cell's rear, the cell will expand perpendicular the field - as
is more commonly observed - but if sensors migrate to the front, the cell will
elongate parallel to the field.


### Generalized Uncertainty Principle theories and their classical interpretation
**Authors**: Matteo Bruno, Sebastiano Segreto, Giovanni Montani

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17408v1](http://arxiv.org/pdf/2407.17408v1)

**Abstract**: In this work, we show that it is possible to define a classical system
associated with a Generalized Uncertainty Principle (GUP) theory via the
implementation of a consistent symplectic structure. This provides a solid
framework for the classical Hamiltonian formulation of such theories and the
study of the dynamics of physical systems in the corresponding deformed phase
space. By further characterizing the functions that govern non-commutativity in
the configuration space using the algebra of angular momentum, we determine a
general form for the rotation generator in these theories and crucially, we
show that, under these conditions, unlike what has been previously found in the
literature at the quantum level, this requirement does not lead to the
superselection of GUP models at the classical level. Finally, we demonstrate
that a properly defined GUP theory can be correctly interpreted classically if
and only if the corresponding quantum commutators satisfy the Jacobi
identities.


### SMEFT Matching to $Z^\prime$ Models at Dimension-8
**Authors**: Sally Dawson, Matthew Forslund, Marvin Schnubel

**Published Date**: 2024-04-01

**Updated Date**: 2024-07-24

**PDF Url**: [2404.01375v3](http://arxiv.org/pdf/2404.01375v3)

**Abstract**: Heavy neutral gauge bosons arise in many motivated models of Beyond the
Standard Model Physics. Experimental searches require that such gauge bosons
are above the TeV scale in most models which means that the tools of effective
field theories, in particular the Standard Model Effective Field Theory
(SMEFT), are useful. We match the SMEFT to models with heavy $Z^\prime$ bosons,
including effects of dimension-8 operators, and consider the restrictions on
model parameters from electroweak precision measurements and from Drell Yan
invariant mass distributions and forward-backward asymmetry, $A_\text{FB}$,
measurements at the LHC. The results demonstrate the model dependence of the
resulting limits on SMEFT coefficients and the relatively small impact of
including dimension-8 matching. In all cases, the limits from invariant mass
distributions are stronger than from $A_\text{FB}$ measurements in the
$Z^\prime$ models we consider.


### Cosmic ray susceptibility of the Terahertz Intensity Mapper detector arrays
**Authors**: Lun-Jun Liu, Reinier M. J. Janssen, Bruce Bumble, Elijah Kane, Logan M. Foote, Charles M. Bradford, Steven Hailey-Dunsheath, Shubh Agrawal, James E. Aguirre, Hrushi Athreya, Justin S. Bracks, Brockton S. Brendal, Anthony J. Corso, Jeffrey P. Filippini, Jianyang Fu, Christopher E. Groppi, Dylan Joralmon, Ryan P. Keenan, Mikolaj Kowalik, Ian N. Lowe, Alex Manduca, Daniel P. Marrone, Philip D. Mauskopf, Evan C. Mayer, Rong Nie, Vesal Razavimaleki, Talia Saeid, Isaac Trumper, Joaquin D. Vieira

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17381v1](http://arxiv.org/pdf/2407.17381v1)

**Abstract**: We report on the effects of cosmic ray interactions with the Kinetic
Inductance Detector (KID) based focal plane array for the Terahertz Intensity
Mapper (TIM). TIM is a NASA-funded balloon-borne experiment designed to probe
the peak of the star formation in the Universe. It employs two spectroscopic
bands, each equipped with a focal plane of four $\sim\,$900-pixel, KID-based
array chips. Measurements of an 864-pixel TIM array shows 791 resonators in a
0.5$\,$GHz bandwidth. We discuss challenges with resonator calibration caused
by this high multiplexing density. We robustly identify the physical positions
of 788 (99.6$\,$%) detectors using a custom LED-based identification scheme.
Using this information we show that cosmic ray events occur at a rate of
2.1$\,\mathrm{events/min/cm^2}$ in our array. 66$\,$% of the events affect a
single pixel, and another 33$\,$% affect $<\,$5 KIDs per event spread over a
0.66$\,\mathrm{cm^2}$ region (2 pixel pitches in radius). We observe a total
cosmic ray dead fraction of 0.0011$\,$%, and predict that the maximum possible
in-flight dead fraction is $\sim\,$0.165$\,$%, which demonstrates our design
will be robust against these high-energy events.


### Design of The Kinetic Inductance Detector Based Focal Plane Assembly for The Terahertz Intensity Mapper
**Authors**: L. -J. Liu, R. M. J. Janssen, C. M. Bradford, S. Hailey-Dunsheath, J. Fu, J. P. Filippini, J. E. Aguirre, J. S. Bracks, A. J. Corso, C. Groppi, J. Hoh, R. P. Keenan, I. N. Lowe, D. P. Marrone, P. Mauskopf, R. Nie, J. Redford, I. Trumper, J. D. Vieira

**Published Date**: 2022-11-17

**Updated Date**: 2024-07-24

**PDF Url**: [2211.09351v2](http://arxiv.org/pdf/2211.09351v2)

**Abstract**: We report on the kinetic inductance detector (KID) array focal plane assembly
design for the Terahertz Intensity Mapper (TIM). Each of the 2 arrays consists
of 4 wafer-sized dies (quadrants), and the overall assembly must satisfy
thermal and mechanical requirements, while maintaining high optical efficiency
and a suitable electromagnetic environment for the KIDs. In particular, our
design manages to strictly maintain a 50 $\mathrm{\mu m}$ air gap between the
array and the horn block. We have prototyped and are now testing a sub-scale
assembly which houses a single quadrant for characterization before integration
into the full array. The initial test result shows a $>$95% yield, indicating a
good performance of our TIM detector packaging design.


## Diffusion
### Sublinear Regret for An Actor-Critic Algorithm in Continuous-Time Linear-Quadratic Reinforcement Learning
**Authors**: Yilie Huang, Yanwei Jia, Xun Yu Zhou

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17226v1](http://arxiv.org/pdf/2407.17226v1)

**Abstract**: We study reinforcement learning (RL) for a class of continuous-time
linear-quadratic (LQ) control problems for diffusions where volatility of the
state processes depends on both state and control variables. We apply a
model-free approach that relies neither on knowledge of model parameters nor on
their estimations, and devise an actor-critic algorithm to learn the optimal
policy parameter directly. Our main contributions include the introduction of a
novel exploration schedule and a regret analysis of the proposed algorithm. We
provide the convergence rate of the policy parameter to the optimal one, and
prove that the algorithm achieves a regret bound of $O(N^{\frac{3}{4}})$ up to
a logarithmic factor. We conduct a simulation study to validate the theoretical
results and demonstrate the effectiveness and reliability of the proposed
algorithm. We also perform numerical comparisons between our method and those
of the recent model-based stochastic LQ RL studies adapted to the state- and
control-dependent volatility setting, demonstrating a better performance of the
former in terms of regret bounds.


### Audio Prompt Adapter: Unleashing Music Editing Abilities for Text-to-Music with Lightweight Finetuning
**Authors**: Fang-Duo Tsai, Shih-Lun Wu, Haven Kim, Bo-Yu Chen, Hao-Chung Cheng, Yi-Hsuan Yang

**Published Date**: 2024-07-23

**Updated Date**: 2024-07-24

**PDF Url**: [2407.16564v2](http://arxiv.org/pdf/2407.16564v2)

**Abstract**: Text-to-music models allow users to generate nearly realistic musical audio
with textual commands. However, editing music audios remains challenging due to
the conflicting desiderata of performing fine-grained alterations on the audio
while maintaining a simple user interface. To address this challenge, we
propose Audio Prompt Adapter (or AP-Adapter), a lightweight addition to
pretrained text-to-music models. We utilize AudioMAE to extract features from
the input audio, and construct attention-based adapters to feedthese features
into the internal layers of AudioLDM2, a diffusion-based text-to-music model.
With 22M trainable parameters, AP-Adapter empowers users to harness both global
(e.g., genre and timbre) and local (e.g., melody) aspects of music, using the
original audio and a short text as inputs. Through objective and subjective
studies, we evaluate AP-Adapter on three tasks: timbre transfer, genre
transfer, and accompaniment generation. Additionally, we demonstrate its
effectiveness on out-of-domain audios containing unseen instruments during
training.


### Visual Stereotypes of Autism Spectrum in DALL-E, Stable Diffusion, SDXL, and Midjourney
**Authors**: Maciej Wodziński, Marcin Rządeczka, Anastazja Szuła, Marta Sokół, Marcin Moskalewicz

**Published Date**: 2024-07-23

**Updated Date**: 2024-07-24

**PDF Url**: [2407.16292v2](http://arxiv.org/pdf/2407.16292v2)

**Abstract**: Avoiding systemic discrimination requires investigating AI models' potential
to propagate stereotypes resulting from the inherent biases of training
datasets. Our study investigated how text-to-image models unintentionally
perpetuate non-rational beliefs regarding autism. The research protocol
involved generating images based on 53 prompts aimed at visualizing concrete
objects and abstract concepts related to autism across four models: DALL-E,
Stable Diffusion, SDXL, and Midjourney (N=249). Expert assessment of results
was performed via a framework of 10 deductive codes representing common
stereotypes contested by the community regarding their presence and spatial
intensity, quantified on ordinal scales and subject to statistical analysis of
inter-rater reliability and size effects. The models frequently utilised
controversial themes and symbols which were unevenly distributed, however, with
striking homogeneity in terms of skin colour, gender, and age, with autistic
individuals portrayed as engaged in solitary activities, interacting with
objects rather than people, and displaying stereotypical emotional expressions
such as pale, anger, or sad. Secondly we observed representational
insensitivity regarding autism images despite directional prompting aimed at
falsifying the above results. Additionally, DALL-E explicitly denied
perpetuating stereotypes. We interpret this as ANNs mirroring the human
cognitive architecture regarding the discrepancy between background and
reflective knowledge, as justified by our previous research on autism-related
stereotypes in humans.


### Sparse Inducing Points in Deep Gaussian Processes: Enhancing Modeling with Denoising Diffusion Variational Inference
**Authors**: Jian Xu, Delu Zeng, John Paisley

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.17033v1](http://arxiv.org/pdf/2407.17033v1)

**Abstract**: Deep Gaussian processes (DGPs) provide a robust paradigm for Bayesian deep
learning. In DGPs, a set of sparse integration locations called inducing points
are selected to approximate the posterior distribution of the model. This is
done to reduce computational complexity and improve model efficiency. However,
inferring the posterior distribution of inducing points is not straightforward.
Traditional variational inference approaches to posterior approximation often
lead to significant bias. To address this issue, we propose an alternative
method called Denoising Diffusion Variational Inference (DDVI) that uses a
denoising diffusion stochastic differential equation (SDE) to generate
posterior samples of inducing variables. We rely on score matching methods for
denoising diffusion model to approximate score functions with a neural network.
Furthermore, by combining classical mathematical theory of SDEs with the
minimization of KL divergence between the approximate and true processes, we
propose a novel explicit variational lower bound for the marginal likelihood
function of DGP. Through experiments on various datasets and comparisons with
baseline methods, we empirically demonstrate the effectiveness of DDVI for
posterior inference of inducing points for DGP models.


### Diffree: Text-Guided Shape Free Object Inpainting with Diffusion Model
**Authors**: Lirui Zhao, Tianshuo Yang, Wenqi Shao, Yuxin Zhang, Yu Qiao, Ping Luo, Kaipeng Zhang, Rongrong Ji

**Published Date**: 2024-07-24

**Updated Date**: 2024-07-24

**PDF Url**: [2407.16982v1](http://arxiv.org/pdf/2407.16982v1)

**Abstract**: This paper addresses an important problem of object addition for images with
only text guidance. It is challenging because the new object must be integrated
seamlessly into the image with consistent visual context, such as lighting,
texture, and spatial location. While existing text-guided image inpainting
methods can add objects, they either fail to preserve the background
consistency or involve cumbersome human intervention in specifying bounding
boxes or user-scribbled masks. To tackle this challenge, we introduce Diffree,
a Text-to-Image (T2I) model that facilitates text-guided object addition with
only text control. To this end, we curate OABench, an exquisite synthetic
dataset by removing objects with advanced image inpainting techniques. OABench
comprises 74K real-world tuples of an original image, an inpainted image with
the object removed, an object mask, and object descriptions. Trained on OABench
using the Stable Diffusion model with an additional mask prediction module,
Diffree uniquely predicts the position of the new object and achieves object
addition with guidance from only text. Extensive experiments demonstrate that
Diffree excels in adding new objects with a high success rate while maintaining
background consistency, spatial appropriateness, and object relevance and
quality.


