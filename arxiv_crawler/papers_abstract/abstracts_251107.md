# Abstracts of Papers

## Physics
### X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations
**Authors**: Maximus A. Pace, Prithwish Dan, Chuanruo Ning, Atiksh Bhardwaj, Audrey Du, Edward W. Duan, Wei-Chiu Ma, Kushal Kedia

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04671v1](http://arxiv.org/pdf/2511.04671v1)

**Abstract**: Human videos can be recorded quickly and at scale, making them an appealing
source of training data for robot learning. However, humans and robots differ
fundamentally in embodiment, resulting in mismatched action execution. Direct
kinematic retargeting of human hand motion can therefore produce actions that
are physically infeasible for robots. Despite these low-level differences,
human demonstrations provide valuable motion cues about how to manipulate and
interact with objects. Our key idea is to exploit the forward diffusion
process: as noise is added to actions, low-level execution differences fade
while high-level task guidance is preserved. We present X-Diffusion, a
principled framework for training diffusion policies that maximally leverages
human data without learning dynamically infeasible motions. X-Diffusion first
trains a classifier to predict whether a noisy action is executed by a human or
robot. Then, a human action is incorporated into policy training only after
adding sufficient noise such that the classifier cannot discern its embodiment.
Actions consistent with robot execution supervise fine-grained denoising at low
noise levels, while mismatched human actions provide only coarse guidance at
higher noise levels. Our experiments show that naive co-training under
execution mismatches degrades policy performance, while X-Diffusion
consistently improves it. Across five manipulation tasks, X-Diffusion achieves
a 16% higher average success rate than the best baseline. The project website
is available at https://portal-cornell.github.io/X-Diffusion/.


### Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions
**Authors**: Kaifeng Zhang, Shuo Sha, Hanxiao Jiang, Matthew Loper, Hyunjong Song, Guangyan Cai, Zhuo Xu, Xiaochen Hu, Changxi Zheng, Yunzhu Li

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04665v1](http://arxiv.org/pdf/2511.04665v1)

**Abstract**: Robotic manipulation policies are advancing rapidly, but their direct
evaluation in the real world remains costly, time-consuming, and difficult to
reproduce, particularly for tasks involving deformable objects. Simulation
provides a scalable and systematic alternative, yet existing simulators often
fail to capture the coupled visual and physical complexity of soft-body
interactions. We present a real-to-sim policy evaluation framework that
constructs soft-body digital twins from real-world videos and renders robots,
objects, and environments with photorealistic fidelity using 3D Gaussian
Splatting. We validate our approach on representative deformable manipulation
tasks, including plush toy packing, rope routing, and T-block pushing,
demonstrating that simulated rollouts correlate strongly with real-world
execution performance and reveal key behavioral patterns of learned policies.
Our results suggest that combining physics-informed reconstruction with
high-quality rendering enables reproducible, scalable, and accurate evaluation
of robotic manipulation policies. Website: https://real2sim-eval.github.io/


### Nowcast3D: Reliable precipitation nowcasting via gray-box learning
**Authors**: Huaguan Chen, Wei Han, Haofei Sun, Ning Lin, Xingtao Song, Yunfan Yang, Jie Tian, Yang Liu, Ji-Rong Wen, Xiaoye Zhang, Xueshun Shen, Hao Sun

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04659v1](http://arxiv.org/pdf/2511.04659v1)

**Abstract**: Extreme precipitation nowcasting demands high spatiotemporal fidelity and
extended lead times, yet existing approaches remain limited. Numerical Weather
Prediction (NWP) and its deep-learning emulations are too slow and coarse for
rapidly evolving convection, while extrapolation and purely data-driven models
suffer from error accumulation and excessive smoothing. Hybrid 2D radar-based
methods discard crucial vertical information, preventing accurate
reconstruction of height-dependent dynamics. We introduce a gray-box, fully
three-dimensional nowcasting framework that directly processes volumetric radar
reflectivity and couples physically constrained neural operators with
datadriven learning. The model learns vertically varying 3D advection fields
under a conservative advection operator, parameterizes spatially varying
diffusion, and introduces a Brownian-motion--inspired stochastic term to
represent unresolved motions. A residual branch captures small-scale convective
initiation and microphysical variability, while a diffusion-based stochastic
module estimates uncertainty. The framework achieves more accurate forecasts up
to three-hour lead time across precipitation regimes and ranked first in 57\%
of cases in a blind evaluation by 160 meteorologists. By restoring full 3D
dynamics with physical consistency, it offers a scalable and robust pathway for
skillful and reliable nowcasting of extreme precipitation.


### Automated Discovery of Non-local Photonic Gates
**Authors**: Sören Arlt, Mario Krenn, Xuemei Gu

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04648v1](http://arxiv.org/pdf/2511.04648v1)

**Abstract**: Interactions between quantum systems enable quantum gates, the building
blocks of quantum information processing. In photonics, direct photon-photon
interactions are too weak to be practically useful, so effective interactions
are engineered with linear optics and measurement. A central challenge is to
realize such interactions non-locally, i.e., between photons that remain
spatially separated. We present experimental proposals for several essential
non-local multiphoton quantum gates that act on spatially separated photons, in
both qubit and high-dimensional qudit systems. All solutions were discovered by
the AI-driven discovery system called PyTheus. Rather than using pre-shared
entanglement or Bell state measurements, our gates use as a resource quantum
indistinguishability by path identity - a technique that exploits coherent
superpositions of the photon pair origins. While analyzing these solutions, we
uncovered a new mechanism that mimics much of the properties of quantum
teleportation, without shared entanglement or Bell state measurements.
Technically, our results establish path indistinguishability as a practical
resource for distributed quantum information processing; conceptually, they
demonstrate how automated discovery systems can contribute new ideas and
techniques in physics.


### The phase-field model of fracture incorporating Mohr-Coulomb, Mogi-Coulomb, and Hoek-Brown strength surfaces
**Authors**: S Chockalingam, Adrian Buganza Tepole, Aditya Kumar

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04627v1](http://arxiv.org/pdf/2511.04627v1)

**Abstract**: Classical phase-field theories of brittle fracture capture
toughness-controlled crack propagation but do not account for the material's
strength surface, which governs fracture nucleation in the absence of cracks.
The phase-field formulation of Kumar et al. (2020) proposed a blueprint for
incorporating the strength surface while preserving toughness-controlled
propagation by introducing a nucleation driving force and presented results for
the Drucker--Prager surface. Following this blueprint, Chockalingam (2025)
recently derived a general driving-force expression that incorporates arbitrary
strength surfaces. The present work implements this driving force within a
finite-element framework and incorporates representative strength surfaces that
span diverse mathematical and physical characteristics -- the Mohr--Coulomb, 3D
Hoek--Brown, and Mogi--Coulomb surfaces. Through simulations of canonical
fracture problems, the formulation is comprehensively validated across fracture
regimes, capturing (i) nucleation under uniform stress, (ii) crack growth from
large pre-existing flaws, and (iii) fracture governed jointly by strength and
toughness. While the strength surfaces examined here already encompass a broad
range of brittle materials, the results demonstrate the generality and
robustness of the proposed driving-force construction for materials governed by
arbitrary strength surfaces.


### Implications of recent $\left(g-2\right)_μ$ measurements for MeV-GeV dark sector searches
**Authors**: Aleksandr Pustyntsev, Marc Vanderhaeghen

**Published Date**: 2025-06-21

**Updated Date**: 2025-11-06

**PDF Url**: [2506.17750v2](http://arxiv.org/pdf/2506.17750v2)

**Abstract**: Recent theoretical and experimental studies of the muon magnetic moment
indicate the absence of the previously reported discrepancy, providing a vital
opportunity to constrain potential BSM physics. In this work, we explore the
MeV-GeV mass range, where existing exclusion limits remain relatively loose. We
analyze both scalar and pseudoscalar as well as vector and axial vector
mediators. We demonstrate that the new bounds are not only comparable to - but
in several cases, significantly more stringent than - the constraints obtained
from previous collider experiments, even when near-future projections are
considered.


### Effective matter sectors from modified entropies
**Authors**: Ankit Anand, Sahil Devdutt, Kimet Jusufi, Emmanuel N. Saridakis

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04613v1](http://arxiv.org/pdf/2511.04613v1)

**Abstract**: We present a general formalism linking modified entropy functions directly to
a modified spacetime metric and, subsequently, to an effective matter sector of
entropic origin. In particular, within the framework of general relativity,
starting from the first law of black-hole thermodynamics we establish an
explicit correspondence between the entropy derivative and the metric function,
which naturally leads to an emergent stress-energy tensor representing an
anisotropic effective fluid. This backreaction effect of horizon entropy may
resolve possible inconsistencies recently identified in black hole physics with
modified entropies. As specific examples, we apply this procedure to a wide
class of modified entropies, such as Barrow, Tsallis-Cirto, Renyi, Kaniadakis,
logarithmic, power-law, loop-quantum-gravity, and exponential modifications,
and we derive the associated effective matter sectors, analyzing their physical
properties and energy conditions.


### Qubit Mapping and Routing tailored to Advanced Quantum ISAs: Not as Costly as You Think
**Authors**: Zhaohui Yang, Kai Zhang, Xinyang Tian, Xiangyu Ren, Yingjian Liu, Yunfeng Li, Jianxin Chen, Dawei Ding, Yuanx Xie

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04608v1](http://arxiv.org/pdf/2511.04608v1)

**Abstract**: Qubit mapping/routing is a critical stage in compilation for both near-term
and fault-tolerant quantum computers, yet existing scalable methods typically
impose several times the routing overhead in terms of circuit depth or
duration. This inefficiency stems from a fundamental disconnect: compilers rely
on an abstract routing model (e.g., three-$ \mathrm{CX} $-unrolled SWAP
insertion) that completely ignores the idiosyncrasies of native gates supported
by physical devices.
  Recent hardware breakthroughs have enabled high-precision implementations of
diverse instruction set architectures (ISAs) beyond standard
$\mathrm{CX}$-based gates. Advanced ISAs involving gates such as
$\mathrm{\sqrt{iSWAP}}$ and $\mathrm{ZZ}(\theta)$ gates offer superior circuit
synthesis capabilities and can be realized with higher fidelities. However,
systematic compiler optimization strategies tailored to these advanced ISAs are
lacking.
  To address this, we propose Canopus, a unified qubit mapping/routing
framework applicable to diverse quantum ISAs. Built upon the canonical
representation of two-qubit gates, Canopus centers on qubit routing to perform
deep co-optimization in an ISA-aware approach. Canopus leverages the two-qubit
canonical representation and the monodromy polytope to model the synthesis cost
for more intelligent $ \mathrm{SWAP} $ insertion during the routing stage. We
also formalize the commutation relations between two-qubit gates through the
canonical form, providing a generalized approach to commutativity-based
optimizations. Experiments show that Canopus consistently reduces routing
overhead by 15\%-35\% compared to state-of-the-art methods across different
ISAs and topologies. Our work also presents a coherent method for
co-exploration of program patterns, quantum ISAs, and hardware topologies.


### Controlling Hong-Ou-Mandel antibunching via parity governed spectral shaping of biphoton states
**Authors**: Mikhail Guselnikov, Alexei D. Kiselev, Andrei Gaidash, George Miroshnichenko, Anton Kozubov

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04604v1](http://arxiv.org/pdf/2511.04604v1)

**Abstract**: We investigate into experimentally detectable effects such as the
Hong-Ou-Mandel (HOM) bunching and antibunching. These regimes can be
characterized using the symmetry degree parameter $D_S$ that enters the
two-photon coincidence probability $P_{2c}=(1-D_S)/2$. In the case of HOM
bunching (antibunching), $D_S$ is positive (negative). Though the symmetry
degree can generally be expressed in terms of the difference between the
contributions coming from the symmetric and antisymmetric parts of the biphoton
joint spectral amplitude (JSA), $\psi(\omega_1,\omega_2)$, for a certain
physically realizable class of the JSA, where $\psi(\omega_1,\omega_2)$ is
proportional to the product of amplitudes
$\varphi_1(\omega_1)\varphi_2(\omega_2)$ multiplied by a Gaussian shaped
entangling factor, we find the sign of $D_S$ is primarily governed by the
parity properties of the spectral function,
$\varphi_{12}(\omega)=\varphi_1(\omega)\varphi_2^*(\omega)$. It is the even
(odd) part of $\varphi_{12}=\varphi_{12}^{(+)}+\varphi_{12}^{(-)}$ that meets
the parity condition
$\varphi_{12}^{(+)}(\omega-\Omega)=\varphi_{12}^{(+)}(\Omega-\omega)$
($\varphi_{12}^{(-)}(\omega-\Omega)=- \varphi_{12}^{(-)}(\Omega-\omega)$) to
yield the positive (negative) contribution, $D_S^{(+)}$ ($-D_S^{(-)}$), to the
symmetry degree parameter: $D_S=D_S^{(+)}-D_S^{(-)}$. We have shown that
switching between the bunching and antibunching regimes can be realized using
the experimentally accessible family of modulated biphoton states produced
using the spectral phase modulation fine-tuned via the sub-nanometer scale
variation of the path length. For this class of modulated states, the Schmidt
number has been computed as a function of the modulation parameter. This
dependence reveals the structure of narrow resonance peaks strongly correlated
with the corresponding narrow dips of the symmetry degree where the HOM
antibunching occurs.


### Cosmogenic Neutron Production in Water at SNO+
**Authors**: SNO+ Collaboration, :, M. Abreu, A. Allega, M. R. Anderson, S. Andringa, S. Arora, D. M. Asner, D. J. Auty, A. Bacon, T. Baltazar, F. Barão, N. Barros, R. Bayes, C. Baylis, E. W. Beier, A. Bialek, S. D. Biller, E. Caden, M. Chen, S. Cheng, B. Cleveland, D. Cookman, J. Corning, S. DeGraw, R. Dehghani, J. Deloye, M. M. Depatie, C. Dima, J. Dittmer, K. H. Dixon, M. S. Esmaeilian, E. Falk, N. Fatemighomi, R. Ford, S. Gadamsetty, A. Gaur, D. Gooding, C. Grant, J. Grove, S. Hall, A. L. Hallin, D. Hallman, M. R. Hebert, W. J. Heintzelman, R. L. Helmer, C. Hewitt, B. Hreljac, P. Huang, R. Hunt-Stokes, A. S. Inácio, C. J. Jillings, S. Kaluzienski, T. Kaptanoglu, J. Kladnik, J. R. Klein, L. L. Kormos, B. Krar, C. Kraus, C. B. Krauss, T. Kroupová, C. Lake, L. Lebanowski, C. Lefebvre, B. Liggins, V. Lozza, M. Luo, S. Maguire, A. Maio, S. Manecki, J. Maneira, R. D. Martin, N. McCauley, A. B. McDonald, G. Milton, D. Morris, M. Mubasher, S. Naugle, L. J. Nolan, H. M. O'Keeffe, G. D. Orebi Gann, S. Ouyang, J. Page, S. Pal, K. Paleshi, W. Parker, L. J. Pickard, R. C. Pitelka, B. Quenallata, P. Ravi, A. Reichold, S. Riccetto, J. Rose, R. Rosero, J. Shen, J. Simms, P. Skensved, M. Smiley, M. I. Stringer, R. Tafirout, B. Tam, J. Tseng, E. Vázquez-Jáuregui, J. G. C. Veinot, C. J. Virtue, F. Wang, M. Ward, J. D. Wilson, J. R. Wilson, A. Wright, S. Yang, Z. Ye, M. Yeh, S. Yu, Y. Zhang, K. Zuber

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04600v1](http://arxiv.org/pdf/2511.04600v1)

**Abstract**: Accurate measurement of the cosmogenic muon-induced neutron yield is crucial
for constraining a significant background in a wide range of low-energy physics
searches. Although previous underground experiments have measured this yield
across various cosmogenic muon energies, SNO+ is uniquely positioned due to its
exposure to one of the highest average cosmogenic muon energies at
364\,\textup{GeV}. Using ultra-pure water, we have determined a neutron yield
of
Y_{n}=(3.38^{+0.23}_{-0.30})\times10^{-4}\,\textup{cm}^{2}\textup{g}^{-1}\mu^{-1}
at SNO+. Comparison with simulations demonstrates clear agreement with the
\textsc{FLUKA} neutron production model, highlighting discrepancies with the
widely used \textsc{GEANT4} model. Furthermore, this measurement reveals a
lower cosmogenic neutron yield than that observed by the SNO experiment, which
used heavy water under identical muon flux conditions. This result provides new
evidence that nuclear structure and target material composition significantly
influence neutron production by cosmogenic muons, offering fresh insight with
important implications for the design and background modelling of future
underground experiments.


## Diffusion
### Optimal Inference Schedules for Masked Diffusion Models
**Authors**: Sitan Chen, Kevin Cong, Jerry Li

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04647v1](http://arxiv.org/pdf/2511.04647v1)

**Abstract**: A major bottleneck of standard auto-regressive large language models is that
their inference process is inherently sequential, resulting in very long and
costly inference times. To circumvent this, practitioners proposed a class of
language models called diffusion language models, of which the masked diffusion
model (MDM) is the most successful. The MDM is able to sample tokens
out-of-order and, ostensibly, many tokens at once and in parallel. However,
there is very limited rigorous understanding of how much parallel sampling
these models can perform without noticeable degradation in their sampling
performance. Prior work of Li and Cai obtained some preliminary bounds, but
these are not tight for many natural classes of distributions. In this work, we
give a new, exact characterization of the expected divergence between the true
distribution and the sampled distribution, for any distribution and any
unmasking schedule for the sampler, showing an elegant connection to the theory
of univariate function approximation.
  By leveraging this connection, we then attain a number of novel lower and
upper bounds for this problem. While the connection to function approximation
in principle gives the optimal unmasking schedule for any distribution, we show
that it is in general impossible to compete with it without strong a priori
knowledge of the distribution, even in seemingly benign settings. However, we
also demonstrate new upper bounds and new sampling schedules in terms of
well-studied information-theoretic properties of the base distribution, namely,
its total correlation and dual total correlation, which show that in some
natural settings, one can sample in $O(log n)$ steps without any visible loss
in performance, where $n$ is the total sequence length.


### Efficient probabilistic surrogate modeling techniques for partially-observed large-scale dynamical systems
**Authors**: Hans Harder, Abhijeet Vishwasrao, Luca Guastoni, Ricardo Vinuesa, Sebastian Peitz

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04641v1](http://arxiv.org/pdf/2511.04641v1)

**Abstract**: This paper is concerned with probabilistic techniques for forecasting
dynamical systems described by partial differential equations (such as, for
example, the Navier-Stokes equations). In particular, it is investigating and
comparing various extensions to the flow matching paradigm that reduce the
number of sampling steps. In this regard, it compares direct distillation,
progressive distillation, adversarial diffusion distillation, Wasserstein GANs
and rectified flows. Moreover, experiments are conducted on a set of
challenging systems. In particular, we also address the challenge of directly
predicting 2D slices of large-scale 3D simulations, paving the way for
efficient inflow generation for solvers.


### Unified Generative Latent Representation for Functional Brain Graphs
**Authors**: Subati Abulikemu, Tiago Azevedo, Michail Mamalakis, John Suckling

**Published Date**: 2025-11-06

**Updated Date**: 2025-11-06

**PDF Url**: [2511.04539v1](http://arxiv.org/pdf/2511.04539v1)

**Abstract**: Functional brain graphs are often characterized with separate graph-theoretic
or spectral descriptors, overlooking how these properties covary and partially
overlap across brains and conditions. We anticipate that dense, weighted
functional connectivity graphs occupy a low-dimensional latent geometry along
which both topological and spectral structures display graded variations. Here,
we estimated this unified graph representation and enabled generation of dense
functional brain graphs through a graph transformer autoencoder with latent
diffusion, with spectral geometry providing an inductive bias to guide
learning. This geometry-aware latent representation, although unsupervised,
meaningfully separated working-memory states and decoded visual stimuli, with
performance further enhanced by incorporating neural dynamics. From the
diffusion modeled distribution, we were able to sample biologically plausible
and structurally grounded synthetic dense graphs.


### Diffusion & Adversarial Schrödinger Bridges via Iterative Proportional Markovian Fitting
**Authors**: Sergei Kholkin, Grigoriy Ksenofontov, David Li, Nikita Kornilov, Nikita Gushchin, Alexandra Suvorikova, Alexey Kroshnin, Evgeny Burnaev, Alexander Korotin

**Published Date**: 2024-10-03

**Updated Date**: 2025-11-06

**PDF Url**: [2410.02601v4](http://arxiv.org/pdf/2410.02601v4)

**Abstract**: The Iterative Markovian Fitting (IMF) procedure, which iteratively projects
onto the space of Markov processes and the reciprocal class, successfully
solves the Schr\"odinger Bridge (SB) problem. However, an efficient practical
implementation requires a heuristic modification -- alternating between fitting
forward and backward time diffusion at each iteration. This modification is
crucial for stabilizing training and achieving reliable results in applications
such as unpaired domain translation. Our work reveals a close connection
between the modified version of IMF and the Iterative Proportional Fitting
(IPF) procedure -- a foundational method for the SB problem, also known as
Sinkhorn's algorithm. Specifically, we demonstrate that the heuristic
modification of the IMF effectively integrates both IMF and IPF procedures. We
refer to this combined approach as the Iterative Proportional Markovian Fitting
(IPMF) procedure. Through theoretical and empirical analysis, we establish the
convergence of the IPMF procedure under various settings, contributing to
developing a unified framework for solving SB problems. Moreover, from a
practical standpoint, the IPMF procedure enables a flexible trade-off between
image similarity and generation quality, offering a new mechanism for tailoring
models to specific tasks.


