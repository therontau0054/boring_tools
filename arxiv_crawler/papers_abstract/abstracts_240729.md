# Abstracts of Papers

## Physics
### Hybrid summary statistics: neural weak lensing inference beyond the power spectrum
**Authors**: T. Lucas Makinen, Tom Charnock, Natalia Porqueres, Axel Lapel, Alan Heavens, Benjamin D. Wandelt

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18909v1](http://arxiv.org/pdf/2407.18909v1)

**Abstract**: In inference problems, we often have domain knowledge which allows us to
define summary statistics that capture most of the information content in a
dataset. In this paper, we present a hybrid approach, where such physics-based
summaries are augmented by a set of compressed neural summary statistics that
are optimised to extract the extra information that is not captured by the
predefined summaries. The resulting statistics are very powerful inputs to
simulation-based or implicit inference of model parameters. We apply this
generalisation of Information Maximising Neural Networks (IMNNs) to parameter
constraints from tomographic weak gravitational lensing convergence maps to
find summary statistics that are explicitly optimised to complement angular
power spectrum estimates. We study several dark matter simulation resolutions
in low- and high-noise regimes. We show that i) the information-update
formalism extracts at least $3\times$ and up to $8\times$ as much information
as the angular power spectrum in all noise regimes, ii) the network summaries
are highly complementary to existing 2-point summaries, and iii) our formalism
allows for networks with smaller, physically-informed architectures to match
much larger regression networks with far fewer simulations needed to obtain
asymptotically optimal inference.


### Lessons from Learning to Spin "Pens"
**Authors**: Jun Wang, Ying Yuan, Haichuan Che, Haozhi Qi, Yi Ma, Jitendra Malik, Xiaolong Wang

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18902v1](http://arxiv.org/pdf/2407.18902v1)

**Abstract**: In-hand manipulation of pen-like objects is an important skill in our daily
lives, as many tools such as hammers and screwdrivers are similarly shaped.
However, current learning-based methods struggle with this task due to a lack
of high-quality demonstrations and the significant gap between simulation and
the real world. In this work, we push the boundaries of learning-based in-hand
manipulation systems by demonstrating the capability to spin pen-like objects.
We first use reinforcement learning to train an oracle policy with privileged
information and generate a high-fidelity trajectory dataset in simulation. This
serves two purposes: 1) pre-training a sensorimotor policy in simulation; 2)
conducting open-loop trajectory replay in the real world. We then fine-tune the
sensorimotor policy using these real-world trajectories to adapt it to the real
world dynamics. With less than 50 trajectories, our policy learns to rotate
more than ten pen-like objects with different physical properties for multiple
revolutions. We present a comprehensive analysis of our design choices and
share the lessons learned during development.


### Physics-Guided Actor-Critic Reinforcement Learning for Swimming in Turbulence
**Authors**: Christopher Koh, Laurent Pagnier, Michael Chertkov

**Published Date**: 2024-06-05

**Updated Date**: 2024-07-26

**PDF Url**: [2406.10242v2](http://arxiv.org/pdf/2406.10242v2)

**Abstract**: Turbulent diffusion causes particles placed in proximity to separate. We
investigate the required swimming efforts to maintain a particle close to its
passively advected counterpart. We explore optimally balancing these efforts
with the intended goal by developing and comparing a novel Physics-Informed
Reinforcement Learning (PIRL) strategy with prescribed control (PC) and
standard physics-agnostic Reinforcement Learning strategies. Our PIRL scheme,
coined the Actor-Physicist, is an adaptation of the Actor-Critic algorithm in
which the Neural Network parameterized Critic is replaced with an analytically
derived physical heuristic function (the physicist). This strategy is then
compared with an analytically computed optimal PC policy derived from a
stochastic optimal control formulation and standard physics-agnostic
Actor-Critic type algorithms.


### The sPHENIX Micromegas Outer Tracker
**Authors**: S. Aune, B. Azmoun, A. Bonenfant, S. Boose, M. Bregant, D. Cacace, R. W. da Silva, R. Feder, A. Francisco, C. Goblin, A. Grabas, J. S. Haggerty, R. A. Hernandez, H. D. H. Herrera, J. Huang, J. Kelsey, I. Kotov, J. Kuczewski, I. Mandjavidze, T. A. Martins, J. Mead, J. Mills, A. Oskarsson, H. Pereira Da Costa, C. Pinkenburg, R. Pisani, T. Protzman, M. L. Purschke, E. Renner, R. Ruggiero, T. Sakaguchi, B. C. S. Sanches, B. Sayki, D. Silvermyr, W. Sondheim, M. Vandenbroucke, W. A. M. Van Noije, J. Vasquez, C. Vidal, A. Wils

**Published Date**: 2024-03-20

**Updated Date**: 2024-07-26

**PDF Url**: [2403.13789v3](http://arxiv.org/pdf/2403.13789v3)

**Abstract**: The sPHENIX Time Projection Chamber Outer Tracker (TPOT) is a Micromegas
based detector. It is a part of the sPHENIX experiment that aims to facilitate
the calibration of the Time Projection Chamber, in particular the correction of
the time-averaged and beam-induced distortions of the electron drift. This
paper describes the detector mission, setup, construction, installation,
commissioning and performance during the first year of sPHENIX data taking.


### Adaptive Parameter Selection in Nudging Based Data Assimilation
**Authors**: Aytekin Çıbık, Rui Fang, William Layton, Farjana Siddiqua

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18886v1](http://arxiv.org/pdf/2407.18886v1)

**Abstract**: Data assimilation combines (imperfect) knowledge of a flow's physical laws
with (noisy, time-lagged, and otherwise imperfect) observations to produce a
more accurate prediction of flow statistics. Assimilation by nudging (from
1964), while non-optimal, is easy to implement and its analysis is clear and
well-established. Nudging's uniform in time accuracy has even been established
under conditions on the nudging parameter $\chi$ and the density of
observational locations, $H$, Larios, Rebholz, and Zerfas
\cite{larios2019global}. One remaining issue is that nudging requires the user
to select a key parameter. The conditions required for this parameter, derived
through $\acute{a}$ priori (worst case) analysis are severe (Section
\ref{aprior-analysis} herein) and far beyond those found to be effective in
computational experience. One resolution, developed herein, is self-adaptive
parameter selection. This report develops, analyzes, tests, and compares two
methods of self-adaptation of nudging parameters. One combines analysis and
response to local flow behavior. The other is based only on response to flow
behavior. The comparison finds both are easily implemented and yield effective
values of the nudging parameter much smaller than those of $\acute{a}$ priori
analysis.


### Effective Modeling of Open Quantum Systems by Low-rank Discretization of Structured Environments
**Authors**: Hideaki Takahashi, Raffaele Borrelli

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18880v1](http://arxiv.org/pdf/2407.18880v1)

**Abstract**: The accurate description of the interaction of a quantum system with a its
environment is a challenging problem ubiquitous across all areas of physics,
and lies at the foundation of quantum mechanics theory. Here we pioneer a new
strategy to create discrete low-rank models of the system-environment
interaction, by exploiting the frequency and time domain information encoded in
the fluctuation-dissipation relation connecting the system-bath correlation
function and the spectral density. We demonstrate the effectiveness of our
methodology by combining it with tensor-network methodologies and simulating
the quantum dynamics of a complex excitonic systems in a highly structured
bosonic environment. The new modeling framework sets the basis for a leap in
the analysis of open quantum systems providing controlled accuracy at
significantly reduced computational costs, with benefits in all connected
research areas.


### Fast optical control of a coherent hole spin in a microcavity
**Authors**: Mark Hogg, Nadia Antoniadis, Malwina Marczak, Giang Nguyen, Timon Baltisberger, Alisa Javadi, Ruediger Schott, Sascha Valentin, Andreas Wieck, Arne Ludwig, Richard Warburton

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18876v1](http://arxiv.org/pdf/2407.18876v1)

**Abstract**: A spin-photon interface is one of the key components of a quantum network.
Physical platforms under investigation span the range of modern experimental
physics, from ultra-cold atoms and ions to a variety of solid-state systems.
Each system has its strengths and weaknesses, typically with a trade-off
between spin properties and photonic properties. Currently, the best
deterministic single-photon sources use a semiconductor quantum dot embedded in
an optical microcavity. However, coherent spin control has not yet been
integrated with a state-of-the-art single-photon source, and the magnetic noise
from host nuclear spins in the semiconductor environment has placed strong
limitations on the spin coherence. Here, we combine high-fidelity all-optical
spin control with a quantum dot in an open microcavity, currently the most
efficient single-photon source platform available. By imprinting a microwave
signal onto a red-detuned optical field, a Raman process, we demonstrate
coherent rotations of a hole spin around an arbitrary axis of the Bloch sphere,
achieving a maximum {\pi}-pulse fidelity of 98.6%. The cavity enhances the
Raman process, enabling ultra-fast Rabi frequencies above 1 GHz. We use our
flexible spin control to perform optical cooling of the nuclear spins in the
host material via the central hole spin, extending the hole-spin coherence time
T2* from 28 ns to 535 ns. Hahn echo preserves the spin coherence on a timescale
of 20 {\mu}s, and dynamical decoupling extends the coherence close to the
relaxation limit. Both the spin T2* and spin rotation time are much larger than
the Purcell-enhanced radiative recombination time, 50 ps, enabling many
spin-photon pairs to be created before the spin loses its coherence.


### Surpassing the Standard Quantum Limit using an Optical Spring
**Authors**: Torrey Cullen, Scott Aronson, Ron Pagano, Jonathan Cripe, Safura Sharifi, Michelle Lollie, Henry Cain, Paula Heu, David Follman, Garrett D Cole, Nancy Aggarwal, Thomas Corbitt

**Published Date**: 2022-10-21

**Updated Date**: 2024-07-26

**PDF Url**: [2210.12222v2](http://arxiv.org/pdf/2210.12222v2)

**Abstract**: Quantum mechanics places noise limits and sensitivity restrictions on
physical measurements. The balance between unwanted backaction and the
precision of optical measurements impose a standard quantum limit (SQL) on
interferometric systems. In order to realize a sensitivity below the SQL, it is
necessary to leverage a back-action evading measurement technique, or else
exploit cancellations of any excess noise contributions at the detector. %Many
proof of principle experiments have been performed, but only recently has an
experiment achieved sensitivity below the SQL. In this work, we extend that
initial demonstration and realize sub-SQL measurement sensitivity nearly two
times better than previous measurements, and with architecture applicable to
interferometric gravitational wave detectors. In fact, this technique is
directly applicable to Advanced LIGO, which could observe similar effects with
a detuned signal recycling cavity. By exploiting quantum correlations created
by an optical spring, we measure a total sensitivity below the SQL by
$\textbf{2.8}$ dB, corresponding to a reduction in the noise power by
$\textbf{72}\pm\textbf{5.1}$ \% below the quantum limit. Through the use of a
detuned optical spring, this noise reduction is tunable, allowing us to choose
the desired range of frequencies that fall below the SQL. This result
demonstrates access to sensitivities well below the SQL at frequencies ranges
applicable to LIGO, with the potential to extend the reach of gravitational
wave detectors further into the universe.


### Gravitational waves from a curvature-induced phase transition of a Higgs-portal dark matter sector
**Authors**: Andreas Mantziris, Orfeu Bertolami

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18845v1](http://arxiv.org/pdf/2407.18845v1)

**Abstract**: The study of interactions between dark matter and the Higgs field opens an
exciting connection between cosmology and particle physics, since such
scenarios can impact the features of dark matter as well as interfering with
the spontaneous breaking of the electroweak symmetry. Furthermore, such
Higgs-portal models of dark matter should be suitably harmonised with the
various epochs of the universe and the phenomenological constraints imposed by
collider experiments. At the same time, the prospect of a stochastic
gravitational wave background offers a promising new window into the primordial
universe, which can complement the insights gained from accelerators. In this
study, we examined whether gravitational waves can be generated from a
curvature-induced phase transition of a non-minimally coupled dark scalar field
with a portal coupling to the Higgs field. The main requirement is that the
phase transition is of first order, which can be achieved through the
introduction of a cubic term on the scalar potential and the sign change of the
curvature scalar. This mechanism was investigated in the context of a dynamical
spacetime during the transition from inflation to kination, while also
considering the possibility for inducing electroweak symmetry breaking in this
manner for a sufficiently low reheating temperature when the Higgs-portal
coupling is extremely weak. We considered a large range of inflationary scales
and both cases of positive and negative values for the non-minimal coupling,
while taking into account the bound imposed by Big Bang Nucleosythesis. The
resulting gravitational wave amplitudes are boosted by kination and thus
constrain the parameter space of the couplings significantly. Even though the
spectra lie at high frequencies for the standard high inflationary scales,
there are combinations of parameter space where they could be probed with
future experiments.


### Using stochastic resonance of two-level systems to increase qubit decoherence times
**Authors**: Yujun Choi, S. N. Coppersmith, Robert Joynt

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18829v1](http://arxiv.org/pdf/2407.18829v1)

**Abstract**: Two-level systems (TLS) are the major source of dephasing of spin qubits in
numerous quantum computing platforms. In spite of much effort, it has been
difficult to substantially mitigate the effects of this noise or, in many
cases, to fully understand its physical origin. We propose a method to make
progress on both of these issues. When an oscillating field is applied to a
TLS, stochastic resonance can occur and the noise spectrum is moved to higher
frequencies. This shift in the TLS noise spectrum will increase the dephasing
times of the qubits that they influence. Furthermore, the details of this
effect depend on the physical properties of the noise sources. Thus one can use
qubit spectroscopy to investigate their physical properties, specifically the
extent to which the TLS themselves possess quantum coherence. We find that it
should be possible to determine the dephasing rate and the energy level
separation of the TLS themselves in this way.


## Diffusion
### Unifying Visual and Semantic Feature Spaces with Diffusion Models for Enhanced Cross-Modal Alignment
**Authors**: Yuze Zheng, Zixuan Li, Xiangxian Li, Jinxing Liu, Yuqing Wang, Xiangxu Meng, Lei Meng

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18854v1](http://arxiv.org/pdf/2407.18854v1)

**Abstract**: Image classification models often demonstrate unstable performance in
real-world applications due to variations in image information, driven by
differing visual perspectives of subject objects and lighting discrepancies. To
mitigate these challenges, existing studies commonly incorporate additional
modal information matching the visual data to regularize the model's learning
process, enabling the extraction of high-quality visual features from complex
image regions. Specifically, in the realm of multimodal learning, cross-modal
alignment is recognized as an effective strategy, harmonizing different modal
information by learning a domain-consistent latent feature space for visual and
semantic features. However, this approach may face limitations due to the
heterogeneity between multimodal information, such as differences in feature
distribution and structure. To address this issue, we introduce a Multimodal
Alignment and Reconstruction Network (MARNet), designed to enhance the model's
resistance to visual noise. Importantly, MARNet includes a cross-modal
diffusion reconstruction module for smoothly and stably blending information
across different domains. Experiments conducted on two benchmark datasets,
Vireo-Food172 and Ingredient-101, demonstrate that MARNet effectively improves
the quality of image information extracted by the model. It is a plug-and-play
framework that can be rapidly integrated into various image classification
frameworks, boosting model performance.


### Weyl Calculus and Exactly Solvable Schrödinger Bridges with Quadratic State Cost
**Authors**: Alexis M. H. Teter, Wenqing Wang, Abhishek Halder

**Published Date**: 2024-07-21

**Updated Date**: 2024-07-26

**PDF Url**: [2407.15245v2](http://arxiv.org/pdf/2407.15245v2)

**Abstract**: Schr\"{o}dinger bridge--a stochastic dynamical generalization of optimal mass
transport--exhibits a learning-control duality. Viewed as a stochastic control
problem, the Schr\"{o}dinger bridge finds an optimal control policy that steers
a given joint state statistics to another while minimizing the total control
effort subject to controlled diffusion and deadline constraints. Viewed as a
stochastic learning problem, the Schr\"{o}dinger bridge finds the most-likely
distribution-valued trajectory connecting endpoint distributional observations,
i.e., solves the two point boundary-constrained maximum likelihood problem over
the manifold of probability distributions. Recent works have shown that solving
the Schr\"{o}dinger bridge problem with state cost requires finding the Markov
kernel associated with a reaction-diffusion PDE where the state cost appears as
a state-dependent reaction rate. We explain how ideas from Weyl calculus in
quantum mechanics, specifically the Weyl operator and the Weyl symbol, can help
determine such Markov kernels. We illustrate these ideas by explicitly finding
the Markov kernel for the case of quadratic state cost via Weyl calculus,
recovering our earlier results but avoiding tedious computation with Hermite
polynomials.


### Diffusion MRI with Machine Learning
**Authors**: Davood Karimi

**Published Date**: 2024-01-01

**Updated Date**: 2024-07-26

**PDF Url**: [2402.00019v2](http://arxiv.org/pdf/2402.00019v2)

**Abstract**: Diffusion-weighted magnetic resonance imaging (dMRI) offers unique
capabilities including noninvasive probing of brain's tissue microstructure and
structural connectivity. It is widely used for clinical assessment of brain
pathologies and for neuroscience research. Analyzing the dMRI data to extract
useful information for medical and scientific purposes can be challenging. The
dMRI measurements often suffer from strong noise and artifacts, there is
usually high inter-session and inter-scanner variability in the data, and
considerable inter-subject heterogeneity in brain structure. Moreover, the
relationship between measurements and the phenomena of interest can be highly
complex. Recent years have witnessed increasing use of machine learning methods
for dMRI analysis. This manuscript aims to assess these efforts, with a focus
on methods that have addressed data preprocessing and harmonization,
microstructure mapping, tractography, and white matter tract analysis. We study
the main findings, strengths, and weaknesses of the existing methods and
suggest topics for future research. We find that machine learning may be
exceptionally suited to tackle some of the difficult tasks in dMRI analysis.
However, for this to happen, several shortcomings of existing methods and
critical unresolved issues need to be addressed. These include deficient
evaluation practices, lack of rich training datasets and validation benchmarks,
as well as model generalizability, reliability, and explainability concerns.


### Log-Concave Coupling for Sampling Neural Net Posteriors
**Authors**: Curtis McDonald, Andrew R Barron

**Published Date**: 2024-07-26

**Updated Date**: 2024-07-26

**PDF Url**: [2407.18802v1](http://arxiv.org/pdf/2407.18802v1)

**Abstract**: In this work, we present a sampling algorithm for single hidden layer neural
networks. This algorithm is built upon a recursive series of Bayesian
posteriors using a method we call Greedy Bayes. Sampling of the Bayesian
posterior for neuron weight vectors $w$ of dimension $d$ is challenging because
of its multimodality. Our algorithm to tackle this problem is based on a
coupling of the posterior density for $w$ with an auxiliary random variable
$\xi$.
  The resulting reverse conditional $w|\xi$ of neuron weights given auxiliary
random variable is shown to be log concave. In the construction of the
posterior distributions we provide some freedom in the choice of the prior. In
particular, for Gaussian priors on $w$ with suitably small variance, the
resulting marginal density of the auxiliary variable $\xi$ is proven to be
strictly log concave for all dimensions $d$. For a uniform prior on the unit
$\ell_1$ ball, evidence is given that the density of $\xi$ is again strictly
log concave for sufficiently large $d$.
  The score of the marginal density of the auxiliary random variable $\xi$ is
determined by an expectation over $w|\xi$ and thus can be computed by various
rapidly mixing Markov Chain Monte Carlo methods. Moreover, the computation of
the score of $\xi$ permits methods of sampling $\xi$ by a stochastic diffusion
(Langevin dynamics) with drift function built from this score. With such
dynamics, information-theoretic methods pioneered by Bakry and Emery show that
accurate sampling of $\xi$ is obtained rapidly when its density is indeed
strictly log-concave. After which, one more draw from $w|\xi$, produces neuron
weights $w$ whose marginal distribution is from the desired posterior.


### Viewpoint Textual Inversion: Discovering Scene Representations and 3D View Control in 2D Diffusion Models
**Authors**: James Burgess, Kuan-Chieh Wang, Serena Yeung-Levy

**Published Date**: 2023-09-14

**Updated Date**: 2024-07-26

**PDF Url**: [2309.07986v2](http://arxiv.org/pdf/2309.07986v2)

**Abstract**: Text-to-image diffusion models generate impressive and realistic images, but
do they learn to represent the 3D world from only 2D supervision? We
demonstrate that yes, certain 3D scene representations are encoded in the text
embedding space of models like Stable Diffusion. Our approach, Viewpoint Neural
Textual Inversion (ViewNeTI), is to discover 3D view tokens; these tokens
control the 3D viewpoint - the rendering pose in a scene - of generated images.
Specifically, we train a small neural mapper to take continuous camera
viewpoint parameters and predict a view token (a word embedding). This token
conditions diffusion generation via cross-attention to produce images with the
desired camera viewpoint. Using ViewNeTI as an evaluation tool, we report two
findings: first, the text latent space has a continuous view-control manifold
for particular 3D scenes; second, we find evidence for a generalized
view-control manifold for all scenes. We conclude that since the view token
controls the 3D `rendering' viewpoint, there is likely a scene representation
embedded in frozen 2D diffusion models. Finally, we exploit the 3D scene
representations for 3D vision tasks, namely, view-controlled text-to-image
generation, and novel view synthesis from a single image, where our approach
sets state-of-the-art for LPIPS. Code available at
https://github.com/jmhb0/view_neti


