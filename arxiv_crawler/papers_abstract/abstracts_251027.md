# Abstracts of Papers

## Physics
### Causal Climate Emulation with Bayesian Filtering
**Authors**: Sebastian Hickman, Ilija Trajkovic, Julia Kaltenborn, Francis Pelletier, Alex Archibald, Yaniv Gurwicz, Peer Nowack, David Rolnick, Julien Boussard

**Published Date**: 2025-06-11

**Updated Date**: 2025-10-24

**PDF Url**: [2506.09891v2](http://arxiv.org/pdf/2506.09891v2)

**Abstract**: Traditional models of climate change use complex systems of coupled equations
to simulate physical processes across the Earth system. These simulations are
highly computationally expensive, limiting our predictions of climate change
and analyses of its causes and effects. Machine learning has the potential to
quickly emulate data from climate models, but current approaches are not able
to incorporate physically-based causal relationships. Here, we develop an
interpretable climate model emulator based on causal representation learning.
We derive a novel approach including a Bayesian filter for stable long-term
autoregressive emulation. We demonstrate that our emulator learns accurate
climate dynamics, and we show the importance of each one of its components on a
realistic synthetic dataset and data from two widely deployed climate models.


### A Knowledge-Graph Translation Layer for Mission-Aware Multi-Agent Path Planning in Spatiotemporal Dynamics
**Authors**: Edward Holmberg, Elias Ioup, Mahdi Abdelguerfi

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21695v1](http://arxiv.org/pdf/2510.21695v1)

**Abstract**: The coordination of autonomous agents in dynamic environments is hampered by
the semantic gap between high-level mission objectives and low-level planner
inputs. To address this, we introduce a framework centered on a Knowledge Graph
(KG) that functions as an intelligent translation layer. The KG's two-plane
architecture compiles declarative facts into per-agent, mission-aware
``worldviews" and physics-aware traversal rules, decoupling mission semantics
from a domain-agnostic planner. This allows complex, coordinated paths to be
modified simply by changing facts in the KG. A case study involving Autonomous
Underwater Vehicles (AUVs) in the Gulf of Mexico visually demonstrates the
end-to-end process and quantitatively proves that different declarative
policies produce distinct, high-performing outcomes. This work establishes the
KG not merely as a data repository, but as a powerful, stateful orchestrator
for creating adaptive and explainable autonomous systems.


### On Uncertainty Calibration for Equivariant Functions
**Authors**: Edward Berman, Jacob Ginesin, Marco Pacini, Robin Walters

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21691v1](http://arxiv.org/pdf/2510.21691v1)

**Abstract**: Data-sparse settings such as robotic manipulation, molecular physics, and
galaxy morphology classification are some of the hardest domains for deep
learning. For these problems, equivariant networks can help improve modeling
across undersampled parts of the input space, and uncertainty estimation can
guard against overconfidence. However, until now, the relationships between
equivariance and model confidence, and more generally equivariance and model
calibration, has yet to be studied. Since traditional classification and
regression error terms show up in the definitions of calibration error, it is
natural to suspect that previous work can be used to help understand the
relationship between equivariance and calibration error. In this work, we
present a theory relating equivariance to uncertainty estimation. By proving
lower and upper bounds on uncertainty calibration errors (ECE and ENCE) under
various equivariance conditions, we elucidate the generalization limits of
equivariant models and illustrate how symmetry mismatch can result in
miscalibration in both classification and regression. We complement our
theoretical framework with numerical experiments that clarify the relationship
between equivariance and uncertainty using a variety of real and simulated
datasets, and we comment on trends with symmetry mismatch, group size, and
aleatoric and epistemic uncertainties.


### DynamicPAE: Generating Scene-Aware Physical Adversarial Examples in Real-Time
**Authors**: Jin Hu, Xianglong Liu, Jiakai Wang, Junkai Zhang, Xianqi Yang, Haotong Qin, Yuqing Ma, Ke Xu

**Published Date**: 2024-12-11

**Updated Date**: 2025-10-24

**PDF Url**: [2412.08053v3](http://arxiv.org/pdf/2412.08053v3)

**Abstract**: Physical adversarial examples (PAEs) are regarded as whistle-blowers of
real-world risks in deep-learning applications, thus worth further
investigation. However, current PAE generation studies show limited adaptive
attacking ability to diverse and varying scenes, revealing the urgent
requirement of dynamic PAEs that are generated in real time and conditioned on
the observation from the attacker. The key challenge in generating dynamic PAEs
is learning the sparse relation between PAEs and the observation of attackers
under the noisy feedback of attack training. To address the challenge, we
present DynamicPAE, the first generative framework that enables scene-aware
real-time physical attacks. Specifically, to address the noisy feedback problem
that obfuscates the exploration of scene-related PAEs, we introduce the
residual-guided adversarial pattern exploration technique. Residual-guided
training, which relaxes the attack training with a reconstruction task, is
proposed to enrich the feedback information, thereby achieving a more
comprehensive exploration of PAEs. To address the alignment problem between the
trained generator and the real-world scenario, we introduce the
distribution-matched attack scenario alignment, consisting of the
conditional-uncertainty-aligned data module and the skewness-aligned objective
re-weighting module. The former aligns the training environment with the
incomplete observation of the real-world attacker. The latter facilitates
consistent stealth control across different attack targets with the skewness
controller. Extensive digital and physical evaluations demonstrate the superior
attack performance of DynamicPAE, attaining a 2.07 $\times$ boost (58.8%
average AP drop under attack) on representative object detectors (e.g., DETR)
over state-of-the-art static PAE generating methods. Overall, our work opens
the door to end-to-end modeling of dynamic PAEs.


### Foundations of Carrollian Geometry
**Authors**: Luca Ciambelli, Puttarak Jai-akson

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21651v1](http://arxiv.org/pdf/2510.21651v1)

**Abstract**: Carrollian physics provides the natural framework for describing null
hypersurfaces. This review explores the geometry of Carrollian manifolds --
spaces endowed with a degenerate metric. We begin with an algebraic overview of
the Carroll group, its conformal extension, and its relation to the BMS group.
Then, in the core of the review, we follow the standard pseudo-Riemannian
narrative: metric $\to$ connection $\to$ curvature. We first introduce the
modern, general definition of a Carrollian structure, the analogue of the
metric on such manifolds, reviewing the historical developments, symmetries,
and link with the algebraic groups. The second part concerns connections. We
show the breakdown of the Levi-Civita theorem in the Carrollian setting and
construct the most general intrinsic Carrollian connection. A preferred
connection is then identified intrinsically and later shown to coincide with
the one induced by embedding a null hypersurface in an ambient spacetime. The
third part develops the associated curvature tensors. We include novel results
presented here for the first time.
  Two advanced topics highlight the broader scope of this framework. The first
treats null hypersurfaces via the rigging technique, deriving the induced
geometry from the ambient space. This provides a unified language for
spacelike, timelike, and null hypersurfaces, and shows that the induced rigged
connection exactly reproduces the intrinsic Carrollian one. From this, the
Gauss and Codazzi-Mainardi equations follow, and the Einstein equations emerge
as conservation laws for the null Brown-York stress tensor. The second topic
extends the Carrollian setup to generic, non-null hypersurfaces, enabling a
smooth null limit and completing the unified geometric description of
hypersurfaces of all causal characters.


### Search for dijet resonances with data scouting in proton-proton collisions at $\sqrt{s}$ = 13 TeV
**Authors**: CMS Collaboration

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21641v1](http://arxiv.org/pdf/2510.21641v1)

**Abstract**: A search is presented for narrow resonances, with a mass between 0.6 and 1.8
TeV, decaying to pairs of jets, in proton-proton collisions at $\sqrt{s}$ = 13
TeV. The search is performed using dijets that are reconstructed, selected, and
recorded in a compact form by the high-level trigger in a technique referred to
as "data scouting", from data collected in 2016$-$2018 corresponding to an
integrated luminosity of 177 fb$^{-1}$. The dijet mass spectra are well
described by a smooth parameterization, and no significant evidence for the
production of new particles is observed. Model-independent upper limits are
presented on the product of the cross section, branching fraction, and
acceptance for the individual cases of narrow quark-quark, quark-gluon, and
gluon-gluon resonances, and are compared to the predictions from a variety of
models of narrow dijet resonance production. The upper limit on the coupling of
a dark matter mediator to quarks is presented as a function of the mediator
mass. The sensitivity of this search goes beyond what is expected from
statistical scaling with the integrated luminosity alone, as a consequence of
the use of fewer parameters in the background function within a more robust
statistical procedure.


### Analytical determination of multi-time correlation functions in quantum chaotic systems
**Authors**: Yoana R. Chorbadzhiyska, Peter A. Ivanov, Charlie Nation

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21637v1](http://arxiv.org/pdf/2510.21637v1)

**Abstract**: The time-dependence of multi-point observable correlation functions are
essential quantities in analysis and simulation of quantum dynamics. Open
quantum systems approaches utilize two-point correlations to describe the
influence of an environment on a system of interest, and in studies of chaotic
quantum system, the out-of-time-ordered correlator (OTOC) is used to probe
chaoticity of dynamics. In this work we analytically derive the time dependence
of multi-point observable correlation functions in quantum systems from a
random matrix theoretic approach, with the highest order function of interest
being the OTOC. We find in each case that dynamical contributions are related
to a simple function, related to the Fourier transform of coarse-grained
wave-functions. We compare the predicted dynamics to exact numerical
experiments in a spin chain for various physical observables. We comment on
implications towards the emergence of Markovianity and quantum regression in
closed quantum systems, as well as relate our results to known bounds on
chaotic dynamics.


### RydIQule Version 2: Enhancing graph-based modeling of Rydberg atoms
**Authors**: Benjamin N. Miller, David H. Meyer, Carter A. Montag, Omar Nagib, Teemu Virtanen, Peter K. Elgee, Kevin C. Cox

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21628v1](http://arxiv.org/pdf/2510.21628v1)

**Abstract**: Rydberg atomic radio-frequency (rf) sensors are an emerging technology
platform that relies on vaporous atoms, interrogated with laser beams and
nearly ionized, to receive rf signals. Rydberg rf sensors have a number of
interesting fundamental distinctions from traditional receiver technologies,
such as those based on metallic antennas, since they are governed by the
quantum physics of atom-light interactions. As Rydberg sensors quickly advance
from laboratory experiments into fieldable devices, there is a need for a
general software modeling tool that fully encompasses the internal physics of
the sensor. The Rydberg Interactive Quantum Module (RydIQule) is a Python
package designed to fill this need. The initial public release of RydIQule in
late 2023 built the core functionality described above. Here we outline
RydIQule's version 2 release which expands on its capabilities to more
accurately model real-world atoms.


### DESI constraints on two-field quintessence with exponential potentials
**Authors**: George Alestas, Marienza Caldarola, Indira Ocampo, Savvas Nesseris, Shinji Tsujikawa

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21627v1](http://arxiv.org/pdf/2510.21627v1)

**Abstract**: We investigate a quintessence model involving two scalar fields with
double-exponential potentials. This configuration allows the system as a whole
to emulate the dynamics of a single field with a shallower potential, enabling
scalar fields that individually cannot drive cosmic acceleration to
collectively achieve and sustain it. We assess the viability of this model by
performing a fully Bayesian analysis and confronting its predictions with
observational data, including the Planck 2018 Cosmic Microwave Background (CMB)
shift parameters, the newly released Dark Energy Spectroscopic Instrument
(DESI) DR2 Baryon Acoustic Oscillation (BAO) measurements, and the Dark Energy
Survey Year 5 (DESY5) Type Ia supernova (SnIa) sample. Our analysis shows that
the two-field quintessence model yields a log Bayes factor relative to the flat
$\Lambda$CDM model of $\Delta \ln B \sim 4$, indicating moderate evidence
against the latter. We also find that the central values of the two slopes of
the exponential potentials are both close to 1, whereas the slope of an
effective single-field system is constrained to be less than order unity. This
property is theoretically desirable from the perspective of higher-dimensional
theories. Thus, the two-field quintessence model with exponential potentials
provides a physically motivated and compelling mechanism that is consistent
with both observational and theoretical requirements.


## Diffusion
### Visual Diffusion Models are Geometric Solvers
**Authors**: Nir Goren, Shai Yehezkel, Omer Dahary, Andrey Voynov, Or Patashnik, Daniel Cohen-Or

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21697v1](http://arxiv.org/pdf/2510.21697v1)

**Abstract**: In this paper we show that visual diffusion models can serve as effective
geometric solvers: they can directly reason about geometric problems by working
in pixel space. We first demonstrate this on the Inscribed Square Problem, a
long-standing problem in geometry that asks whether every Jordan curve contains
four points forming a square. We then extend the approach to two other
well-known hard geometric problems: the Steiner Tree Problem and the Simple
Polygon Problem.
  Our method treats each problem instance as an image and trains a standard
visual diffusion model that transforms Gaussian noise into an image
representing a valid approximate solution that closely matches the exact one.
The model learns to transform noisy geometric structures into correct
configurations, effectively recasting geometric reasoning as image generation.
  Unlike prior work that necessitates specialized architectures and
domain-specific adaptations when applying diffusion to parametric geometric
representations, we employ a standard visual diffusion model that operates on
the visual representation of the problem. This simplicity highlights a
surprising bridge between generative modeling and geometric problem solving.
Beyond the specific problems studied here, our results point toward a broader
paradigm: operating in image space provides a general and practical framework
for approximating notoriously hard problems, and opens the door to tackling a
far wider class of challenging geometric tasks.


### System-Embedded Diffusion Bridge Models
**Authors**: Bartlomiej Sobieski, Matthew Tivnan, Yuang Wang, Siyeop Yoon, Pengfei Jin, Dufan Wu, Quanzheng Li, Przemyslaw Biecek

**Published Date**: 2025-06-30

**Updated Date**: 2025-10-24

**PDF Url**: [2506.23726v2](http://arxiv.org/pdf/2506.23726v2)

**Abstract**: Solving inverse problems -- recovering signals from incomplete or noisy
measurements -- is fundamental in science and engineering. Score-based
generative models (SGMs) have recently emerged as a powerful framework for this
task. Two main paradigms have formed: unsupervised approaches that adapt
pretrained generative models to inverse problems, and supervised bridge methods
that train stochastic processes conditioned on paired clean and corrupted data.
While the former typically assume knowledge of the measurement model, the
latter have largely overlooked this structural information. We introduce System
embedded Diffusion Bridge Models (SDBs), a new class of supervised bridge
methods that explicitly embed the known linear measurement system into the
coefficients of a matrix-valued SDE. This principled integration yields
consistent improvements across diverse linear inverse problems and demonstrates
robust generalization under system misspecification between training and
deployment, offering a promising solution to real-world applications.


### Generalised Flow Maps for Few-Step Generative Modelling on Riemannian Manifolds
**Authors**: Oscar Davis, Michael S. Albergo, Nicholas M. Boffi, Michael M. Bronstein, Avishek Joey Bose

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21608v1](http://arxiv.org/pdf/2510.21608v1)

**Abstract**: Geometric data and purpose-built generative models on them have become
ubiquitous in high-impact deep learning application domains, ranging from
protein backbone generation and computational chemistry to geospatial data.
Current geometric generative models remain computationally expensive at
inference -- requiring many steps of complex numerical simulation -- as they
are derived from dynamical measure transport frameworks such as diffusion and
flow-matching on Riemannian manifolds. In this paper, we propose Generalised
Flow Maps (GFM), a new class of few-step generative models that generalises the
Flow Map framework in Euclidean spaces to arbitrary Riemannian manifolds. We
instantiate GFMs with three self-distillation-based training methods:
Generalised Lagrangian Flow Maps, Generalised Eulerian Flow Maps, and
Generalised Progressive Flow Maps. We theoretically show that GFMs, under
specific design decisions, unify and elevate existing Euclidean few-step
generative models, such as consistency models, shortcut models, and meanflows,
to the Riemannian setting. We benchmark GFMs against other geometric generative
models on a suite of geometric datasets, including geospatial data, RNA torsion
angles, and hyperbolic manifolds, and achieve state-of-the-art sample quality
for single- and few-step evaluations, and superior or competitive
log-likelihoods using the implicit probability flow.


### HollowFlow: Efficient Sample Likelihood Evaluation using Hollow Message Passing
**Authors**: Johann Flemming Gloy, Simon Olsson

**Published Date**: 2025-10-24

**Updated Date**: 2025-10-24

**PDF Url**: [2510.21542v1](http://arxiv.org/pdf/2510.21542v1)

**Abstract**: Flow and diffusion-based models have emerged as powerful tools for scientific
applications, particularly for sampling non-normalized probability
distributions, as exemplified by Boltzmann Generators (BGs). A critical
challenge in deploying these models is their reliance on sample likelihood
computations, which scale prohibitively with system size $n$, often rendering
them infeasible for large-scale problems. To address this, we introduce
$\textit{HollowFlow}$, a flow-based generative model leveraging a novel
non-backtracking graph neural network (NoBGNN). By enforcing a block-diagonal
Jacobian structure, HollowFlow likelihoods are evaluated with a constant number
of backward passes in $n$, yielding speed-ups of up to $\mathcal{O}(n^2)$: a
significant step towards scaling BGs to larger systems. Crucially, our
framework generalizes: $\textbf{any equivariant GNN or attention-based
architecture}$ can be adapted into a NoBGNN. We validate HollowFlow by training
BGs on two different systems of increasing size. For both systems, the sampling
and likelihood evaluation time decreases dramatically, following our
theoretical scaling laws. For the larger system we obtain a $10^2\times$
speed-up, clearly illustrating the potential of HollowFlow-based approaches for
high-dimensional scientific problems previously hindered by computational
bottlenecks.


