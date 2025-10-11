# Abstracts of Papers

## Physics
### The Complexity of Thermalization in Finite Quantum Systems
**Authors**: Dhruv Devulapalli, T. C. Mooney, James D. Watson

**Published Date**: 2025-07-01

**Updated Date**: 2025-10-09

**PDF Url**: [2507.00405v2](http://arxiv.org/pdf/2507.00405v2)

**Abstract**: Thermalization is the process through which a physical system evolves toward
a state of thermal equilibrium. Determining whether or not a physical system
will thermalize from an initial state has been a key question in condensed
matter physics. Closely related questions are determining whether observables
in these systems relax to stationary values, and what those values are. Using
tools from computational complexity theory, we demonstrate that given a
Hamiltonian on a finite-sized system, determining whether or not it thermalizes
or relaxes to a given stationary value is computationally intractable, even for
a quantum computer. In particular, we show that the problem of determining
whether an observable of a finite-sized quantum system relaxes to a given value
is PSPACE-complete, and so no efficient algorithm for determining the value is
expected to exist. Further, we show the existence of Hamiltonians for which the
problem of determining whether the system thermalizes to the Gibbs expectation
value is PSPACE-complete. We also show that the related problem of determining
whether the system thermalizes to the microcanonical expectation value is
contained in PSPACE and is PSPACE-hard under quantum polynomial time
reductions. In light of recent results demonstrating undecidability of
thermalization in the thermodynamic limit, our work shows that the
intractability of the problem is due to inherent difficulties in many-body
physics rather than particularities of infinite systems.


### Energy, Bosons and Computational Complexity
**Authors**: Ulysse Chabaud, Sevag Gharibian, Saeed Mehraban, Arsalan Motamedi, Hamid Reza Naeij, Dorian Rudolph, Dhruva Sambrani

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08545v1](http://arxiv.org/pdf/2510.08545v1)

**Abstract**: We investigate the role of energy, i.e. average photon number, as a resource
in the computational complexity of bosonic systems. We show three sets of
results: (1. Energy growth rates) There exist bosonic gate sets which increase
energy incredibly rapidly, obtaining e.g. infinite energy in finite/constant
time. We prove these high energies can make computing properties of bosonic
computations, such as deciding whether a given computation will attain infinite
energy, extremely difficult, formally undecidable. (2. Lower bounds on
computational power) More energy ``='' more computational power. For example,
certain gate sets allow poly-time bosonic computations to simulate PTOWER, the
set of deterministic computations whose runtime scales as a tower of
exponentials with polynomial height. Even just exponential energy and $O(1)$
modes suffice to simulate NP, which, importantly, is a setup similar to that of
the recent bosonic factoring algorithm of [Brenner, Caha, Coiteux-Roy and
Koenig (2024)]. For simpler gate sets, we show an energy hierarchy theorem. (3.
Upper bounds on computational power) Bosonic computations with polynomial
energy can be simulated in BQP, ``physical'' bosonic computations with
arbitrary finite energy are decidable, and the gate set consisting of Gaussian
gates and the cubic phase gate can be simulated in PP, with exponential bound
on energy, improving upon the previous PSPACE upper bound. Finally, combining
upper and lower bounds yields no-go theorems for a continuous-variable
Solovay--Kitaev theorem for gate sets such as the Gaussian and cubic phase
gates.


### A Dobrushin condition for quantum Markov chains: Rapid mixing and conditional mutual information at high temperature
**Authors**: Ainesh Bakshi, Allen Liu, Ankur Moitra, Ewin Tang

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08542v1](http://arxiv.org/pdf/2510.08542v1)

**Abstract**: A central challenge in quantum physics is to understand the structural
properties of many-body systems, both in equilibrium and out of equilibrium.
For classical systems, we have a unified perspective which connects structural
properties of systems at thermal equilibrium to the Markov chain dynamics that
mix to them. We lack such a perspective for quantum systems: there is no
framework to translate the quantitative convergence of the Markovian evolution
into strong structural consequences.
  We develop a general framework that brings the breadth and flexibility of the
classical theory to quantum Gibbs states at high temperature. At its core is a
natural quantum analog of a Dobrushin condition; whenever this condition holds,
a concise path-coupling argument proves rapid mixing for the corresponding
Markovian evolution. The same machinery bridges dynamic and structural
properties: rapid mixing yields exponential decay of conditional mutual
information (CMI) without restrictions on the size of the probed subsystems,
resolving a central question in the theory of open quantum systems. Our key
technical insight is an optimal transport viewpoint which couples quantum
dynamics to a linear differential equation, enabling precise control over how
local deviations from equilibrium propagate to distant sites.


### On anomalous dissipation induced by transport noise
**Authors**: Antonio Agresti

**Published Date**: 2024-05-06

**Updated Date**: 2025-10-09

**PDF Url**: [2405.03525v3](http://arxiv.org/pdf/2405.03525v3)

**Abstract**: In this paper, we show that suitable transport noises produce anomalous
dissipation of both enstrophy of solutions to 2D Navier-Stokes equations and of
energy of solutions to diffusion equations in all dimensions. The key
ingredients are Meyers' type estimates for SPDEs with transport noise, which
are combined with recent scaling limits for such SPDEs. The former enables us
to establish, for the first time, uniform-in-time convergence in a space of
positive smoothness for such scaling limits. Compared to previous work, one of
the main novelties is that anomalous dissipation might take place even in the
presence of a transport noise of arbitrarily small intensity. Physical
interpretations of our results are also discussed.


### How hard is it to verify a classical shadow?
**Authors**: Georgios Karaiskos, Dorian Rudolph, Johannes Jakob Meyer, Jens Eisert, Sevag Gharibian

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08515v1](http://arxiv.org/pdf/2510.08515v1)

**Abstract**: Classical shadows are succinct classical representations of quantum states
which allow one to encode a set of properties P of a quantum state rho, while
only requiring measurements on logarithmically many copies of rho in the size
of P. In this work, we initiate the study of verification of classical shadows,
denoted classical shadow validity (CSV), from the perspective of computational
complexity, which asks: Given a classical shadow S, how hard is it to verify
that S predicts the measurement statistics of a quantum state? We show that
even for the elegantly simple classical shadow protocol of [Huang, Kueng,
Preskill, Nature Physics 2020] utilizing local Clifford measurements, CSV is
QMA-complete. This hardness continues to hold for the high-dimensional
extension of said protocol due to [Mao, Yi, and Zhu, PRL 2025]. Among other
results, we also show that CSV for exponentially many observables is complete
for a quantum generalization of the second level of the polynomial hierarchy,
yielding the first natural complete problem for such a class.


### The quantum communication power of indefinite causal order
**Authors**: Xuanqiang Zhao, Benchi Zhao, Giulio Chiribella

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08507v1](http://arxiv.org/pdf/2510.08507v1)

**Abstract**: Quantum theory is in principle compatible with scenarios where physical
processes take place in an indefinite causal order, a possibility that was
shown to yield advantages in several information processing tasks. However,
advantages in communication, the most basic form of information processing,
have so far remained controversial and hard to prove. Here we develop a
framework that can be used to rigorously assess the role of causal order in a
scenario where communication links are built by assembling multiple quantum
devices. In this setting, we establish a clear-cut advantage of indefinite
order in the one-shot transmission of classical messages. On the other hand, we
also show that the advantage is not generic to all communication tasks.
Notably, we find that indefinite order does not offer any advantage over shared
entanglement in the asymptotic scenario where a large number of uses of the
same communication device is employed. Overall, our results unveil non-trivial
relations between communication, causal order, entanglement, and no-signaling
resources in quantum mechanics.


### Constraining the new contributions to electron $g-2$ in a radiative neutrino mass model
**Authors**: Bayu Dirgantara, J. Julio

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08504v1](http://arxiv.org/pdf/2510.08504v1)

**Abstract**: We examine electron and muon anomalous magnetic dipole moments within a
radiative neutrino mass model featuring TeV-scale scalar leptoquarks
$S(3,1,-1/3)$ and $R(3,2,1/6)$. We utilize textures with decoupling electron
and muon sectors, so that both electron and muon anomalous magnetic dipole
moments could receive internal chiral enhancements from different heavy up-type
quarks while in the same time evading the stringent $\mu\to e\gamma$
constraint. A successful fit to neutrino oscillation data requires the
simultaneous presence of one- and two-loop neutrino mass contributions. This
severely constrains the parameter space of the model, which results in a
negligible new physics correction to the muon $g-2$. The electron $g-2$
discrepancy implied by the rubidium experiment, on the other hand, can be
resolved within $2\sigma$ uncertainty provided that neutrino mass ordering is
inverted. Lepton-flavor-violating tau decay rates, such as $\tau\to e\gamma$
and $\tau\to 3e$, are predicted to be within the sensitivities of
next-generation experiments.


### Quantum Probe Tomography
**Authors**: Sitan Chen, Jordan Cotler, Hsin-Yuan Huang

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08499v1](http://arxiv.org/pdf/2510.08499v1)

**Abstract**: Characterizing quantum many-body systems is a fundamental problem across
physics, chemistry, and materials science. While significant progress has been
made, many existing Hamiltonian learning protocols demand digital quantum
control over the entire system, creating a disconnect from many real-world
settings that provide access only through small, local probes. Motivated by
this, we introduce and formalize the problem of quantum probe tomography, where
one seeks to learn the parameters of a many-body Hamiltonian using a single
local probe access to a small subsystem of a many-body thermal state undergoing
time evolution. We address the identifiability problem of determining which
Hamiltonians can be distinguished from probe data through a new combination of
tools from algebraic geometry and smoothed analysis. Using this approach, we
prove that generic Hamiltonians in various physically natural families are
identifiable up to simple, unavoidable structural symmetries. Building on these
insights, we design the first efficient end-to-end algorithm for probe
tomography that learns Hamiltonian parameters to accuracy $\varepsilon$, with
query complexity scaling polynomially in $1/\varepsilon$ and classical
post-processing time scaling polylogarithmically in $1/\varepsilon$. In
particular, we demonstrate that translation- and rotation-invariant
nearest-neighbor Hamiltonians on square lattices in one, two, and three
dimensions can be efficiently reconstructed from single-site probes of the
Gibbs state, up to inversion symmetry about the probed site. Our results
demonstrate that robust Hamiltonian learning remains achievable even under
severely constrained experimental access.


### Average-case quantum complexity from glassiness
**Authors**: Alexander Zlokapa, Bobak T. Kiani, Eric R. Anschuetz

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08497v1](http://arxiv.org/pdf/2510.08497v1)

**Abstract**: Glassiness -- a phenomenon in physics characterized by a rough free-energy
landscape -- implies hardness for stable classical algorithms. For example, it
can obstruct constant-time Langevin dynamics and message-passing in random
$k$-SAT and max-cut instances. We provide an analogous framework for
average-case quantum complexity showing that a natural family of quantum
algorithms (e.g., Lindbladian evolution) fails for natural Hamiltonian
ensembles (e.g., random 3-local Hamiltonians). Specifically, we prove that the
standard notion of quantum glassiness based on replica symmetry breaking
obstructs stable quantum algorithms for Gibbs sampling, which we define by a
Lipschitz temperature dependence in quantum Wasserstein complexity. Our proof
relies on showing that such algorithms fail to capture a structural phase
transition in the Gibbs state, where glassiness causes the Gibbs state to
decompose into clusters extensively separated in quantum Wasserstein distance.
This yields average-case lower bounds for constant-time local Lindbladian
evolution and shallow variational circuits. Unlike mixing time lower bounds,
our results hold even when dynamics are initialized from the maximally mixed
state. We apply these lower bounds to non-commuting, non-stoquastic
Hamiltonians by showing a glass transition via the replica trick. We find that
the ensemble of all 3-local Pauli strings with independent Gaussian
coefficients is average-case hard, while providing analytical evidence that the
general $p$-local Pauli ensemble is non-glassy for sufficiently large constant
$p$, in contrast to its classical (Ising $p$-spin, always glassy) and fermionic
(SYK, never glassy) counterparts.


## Diffusion
### Who Said Neural Networks Aren't Linear?
**Authors**: Nimrod Berman, Assaf Hallak, Assaf Shocher

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08570v1](http://arxiv.org/pdf/2510.08570v1)

**Abstract**: Neural networks are famously nonlinear. However, linearity is defined
relative to a pair of vector spaces, $f$$:$$X$$\to$$Y$. Is it possible to
identify a pair of non-standard vector spaces for which a conventionally
nonlinear function is, in fact, linear? This paper introduces a method that
makes such vector spaces explicit by construction. We find that if we sandwich
a linear operator $A$ between two invertible neural networks, $f(x)=g_y^{-1}(A
g_x(x))$, then the corresponding vector spaces $X$ and $Y$ are induced by newly
defined addition and scaling actions derived from $g_x$ and $g_y$. We term this
kind of architecture a Linearizer. This framework makes the entire arsenal of
linear algebra, including SVD, pseudo-inverse, orthogonal projection and more,
applicable to nonlinear mappings. Furthermore, we show that the composition of
two Linearizers that share a neural network is also a Linearizer. We leverage
this property and demonstrate that training diffusion models using our
architecture makes the hundreds of sampling steps collapse into a single step.
We further utilize our framework to enforce idempotency (i.e. $f(f(x))=f(x)$)
on networks leading to a globally projective generative model and to
demonstrate modular style transfer.


### Improving Reasoning for Diffusion Language Models via Group Diffusion Policy Optimization
**Authors**: Kevin Rojas, Jiahe Lin, Kashif Rasul, Anderson Schneider, Yuriy Nevmyvaka, Molei Tao, Wei Deng

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08554v1](http://arxiv.org/pdf/2510.08554v1)

**Abstract**: Diffusion language models (DLMs) enable parallel, order-agnostic generation
with iterative refinement, offering a flexible alternative to autoregressive
large language models (LLMs). However, adapting reinforcement learning (RL)
fine-tuning to DLMs remains an open challenge because of the intractable
likelihood. Pioneering work such as diffu-GRPO estimated token-level
likelihoods via one-step unmasking. While computationally efficient, this
approach is severely biased. A more principled foundation lies in
sequence-level likelihoods, where the evidence lower bound (ELBO) serves as a
surrogate. Yet, despite this clean mathematical connection, ELBO-based methods
have seen limited adoption due to the prohibitive cost of likelihood
evaluation. In this work, we revisit ELBO estimation and disentangle its
sources of variance. This decomposition motivates reducing variance through
fast, deterministic integral approximations along a few pivotal dimensions.
Building on this insight, we introduce \textbf{Group Diffusion Policy
Optimization (GDPO)}, a new RL algorithm tailored for DLMs. GDPO leverages
simple yet effective Semi-deterministic Monte Carlo schemes to mitigate the
variance explosion of ELBO estimators under vanilla double Monte Carlo
sampling, yielding a provably lower-variance estimator under tight evaluation
budgets. Empirically, GDPO achieves consistent gains over pretrained
checkpoints and outperforms diffu-GRPO, one of the state-of-the-art baselines,
on the majority of math, reasoning, and coding benchmarks.


### Permutation-Invariant Spectral Learning via Dyson Diffusion
**Authors**: Tassilo Schwarz, Cai Dieball, Constantin Kogler, Kevin Lam, Renaud Lambiotte, Arnaud Doucet, Aljaž Godec, George Deligiannidis

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08535v1](http://arxiv.org/pdf/2510.08535v1)

**Abstract**: Diffusion models are central to generative modeling and have been adapted to
graphs by diffusing adjacency matrix representations. The challenge of having
up to $n!$ such representations for graphs with $n$ nodes is only partially
mitigated by using permutation-equivariant learning architectures. Despite
their computational efficiency, existing graph diffusion models struggle to
distinguish certain graph families, unless graph data are augmented with ad hoc
features. This shortcoming stems from enforcing the inductive bias within the
learning architecture. In this work, we leverage random matrix theory to
analytically extract the spectral properties of the diffusion process, allowing
us to push the inductive bias from the architecture into the dynamics. Building
on this, we introduce the Dyson Diffusion Model, which employs Dyson's Brownian
Motion to capture the spectral dynamics of an Ornstein-Uhlenbeck process on the
adjacency matrix while retaining all non-spectral information. We demonstrate
that the Dyson Diffusion Model learns graph spectra accurately and outperforms
existing graph diffusion models.


### Wavefunction Flows: Efficient Quantum Simulation of Continuous Flow Models
**Authors**: David Layden, Ryan Sweke, Vojtěch Havlíček, Anirban Chowdhury, Kirill Neklyudov

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08462v1](http://arxiv.org/pdf/2510.08462v1)

**Abstract**: Flow models are a cornerstone of modern machine learning. They are generative
models that progressively transform probability distributions according to
learned dynamics. Specifically, they learn a continuous-time Markov process
that efficiently maps samples from a simple source distribution into samples
from a complex target distribution. We show that these models are naturally
related to the Schr\"odinger equation, for an unusual Hamiltonian on continuous
variables. Moreover, we prove that the dynamics generated by this Hamiltonian
can be efficiently simulated on a quantum computer. Together, these results
give a quantum algorithm for preparing coherent encodings (a.k.a., qsamples)
for a vast family of probability distributions--namely, those expressible by
flow models--by reducing the task to an existing classical learning problem,
plus Hamiltonian simulation. For statistical problems defined by flow models,
such as mean estimation and property testing, this enables the use of quantum
algorithms tailored to qsamples, which may offer advantages over classical
algorithms based only on samples from a flow model. More broadly, these results
reveal a close connection between state-of-the-art machine learning models,
such as flow matching and diffusion models, and one of the main expected
capabilities of quantum computers: simulating quantum dynamics.


### SummDiff: Generative Modeling of Video Summarization with Diffusion
**Authors**: Kwanseok Kim, Jaehoon Hahm, Sumin Kim, Jinhwan Sul, Byunghak Kim, Joonseok Lee

**Published Date**: 2025-10-09

**Updated Date**: 2025-10-09

**PDF Url**: [2510.08458v1](http://arxiv.org/pdf/2510.08458v1)

**Abstract**: Video summarization is a task of shortening a video by choosing a subset of
frames while preserving its essential moments. Despite the innate subjectivity
of the task, previous works have deterministically regressed to an averaged
frame score over multiple raters, ignoring the inherent subjectivity of what
constitutes a good summary. We propose a novel problem formulation by framing
video summarization as a conditional generation task, allowing a model to learn
the distribution of good summaries and to generate multiple plausible summaries
that better reflect varying human perspectives. Adopting diffusion models for
the first time in video summarization, our proposed method, SummDiff,
dynamically adapts to visual contexts and generates multiple candidate
summaries conditioned on the input video. Extensive experiments demonstrate
that SummDiff not only achieves the state-of-the-art performance on various
benchmarks but also produces summaries that closely align with individual
annotator preferences. Moreover, we provide a deeper insight with novel metrics
from an analysis of the knapsack, which is an important last step of generating
summaries but has been overlooked in evaluation.


