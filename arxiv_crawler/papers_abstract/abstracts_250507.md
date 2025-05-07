# Abstracts of Papers

## Physics
### Stay Positive: Neural Refinement of Sample Weights
**Authors**: Benjamin Nachman, Dennis Noll

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03724v1](http://arxiv.org/pdf/2505.03724v1)

**Abstract**: Monte Carlo simulations are an essential tool for data analysis in particle
physics. Simulated events are typically produced alongside weights that
redistribute the cross section across the phase space. Latent degrees of
freedom introduce a distribution of weights at a given point in the phase
space, which can include negative values. Several post-hoc reweighting methods
have been developed to eliminate the negative weights. All of these methods
share the common strategy of approximating the average weight as a function of
phase space. We introduce an alternative approach with a potentially simpler
learning task. Instead of reweighting to the average, we refine the initial
weights with a scaling transformation, utilizing a phase space-dependent
factor. Since this new refinement method does not need to model the full weight
distribution, it can be more accurate. High-dimensional and unbinned phase
space is processed using neural networks for the refinement. Using both
realistic and synthetic examples, we show that the new neural refinement method
is able to match or exceed the accuracy of similar weight transformations.


### Two-electron quantum walks probe entanglement and decoherence in an electron microscope
**Authors**: Offek Tziperman, David Nabben, Ron Ruimy, Jacob Holder, Ethan Nussinson, Yiqi Fang, Alexey Gorlach, Daniel Kazenwadel, Aviv Karnieli, Ido Kaminer, Peter Baum

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03707v1](http://arxiv.org/pdf/2505.03707v1)

**Abstract**: Classical physics is often a good approximation for quantum systems composed
of many interacting particles, although wavepacket dispersion and scattering
processes continuously induce delocalization and entanglement. According to
decoherence theory, an entangled ensemble can appear classical when only a
subset of all particles is observed. This emergence of macroscopic phenomena
from quantum interactions is, for example, relevant for phase transitions,
quantum thermalization, hydrodynamics, spin liquids, or time crystals. However,
entanglement and decoherence in free electrons have not yet been explored,
although the electron is a fundamental elementary particle with extraordinary
technological relevance. Here, we investigate the degree of coherence and
entanglement in a free-space electron gas in the beam of an ultrafast electron
microscope. Inspired by the strong interaction of free electrons with laser
light, we introduce a two-electron quantum walk that enables quantum state
tomography of entangled or partially entangled electron-electron pairs. We
apply this novel diagnostic to study the creation and loss of entanglement in
short pulses of hundreds of electrons. We observe high-contrast two-electron
interferences and signs of small electron-electron entanglement that we explain
by competition between entangling Coulomb interactions and decoherence effects
from unmeasured reservoir electrons. The ability to characterize entangled
free-electron quantum states will provide insight into the emergence of
classical phenomena from quantum principles in the realm of particles with mass
and charge, and will have practical applications in low-dose electron
microscopy, ghost imaging, or quantum electron microscopy.


### Multi-modal cascade feature transfer for polymer property prediction
**Authors**: Kiichi Obuchi, Yuta Yahagi, Kiyohiko Toyama, Shukichi Tanaka, Kota Matsui

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03704v1](http://arxiv.org/pdf/2505.03704v1)

**Abstract**: In this paper, we propose a novel transfer learning approach called
multi-modal cascade model with feature transfer for polymer property
prediction.Polymers are characterized by a composite of data in several
different formats, including molecular descriptors and additive information as
well as chemical structures. However, in conventional approaches, prediction
models were often constructed using each type of data separately. Our model
enables more accurate prediction of physical properties for polymers by
combining features extracted from the chemical structure by graph convolutional
neural networks (GCN) with features such as molecular descriptors and additive
information. The predictive performance of the proposed method is empirically
evaluated using several polymer datasets. We report that the proposed method
shows high predictive performance compared to the baseline conventional
approach using a single feature.


### Minimal Autocorrelation in Hybrid Monte Carlo simulations using Exact Fourier Acceleration
**Authors**: Johann Ostmeyer, Pavel Buividovich

**Published Date**: 2024-04-15

**Updated Date**: 2025-05-06

**PDF Url**: [2404.09723v3](http://arxiv.org/pdf/2404.09723v3)

**Abstract**: The hybrid Monte Carlo (HMC) algorithm is a ubiquitous method in
computational physics with applications ranging from condensed matter to
lattice QCD and beyond. However, HMC simulations often suffer from long
autocorrelation times, severely reducing their efficiency. In this work two of
the main sources of autocorrelations are identified and eliminated. The first
source is the sampling of the canonical momenta from a sub-optimal normal
distribution, the second is a badly chosen trajectory length. Analytic
solutions to both problems are presented and implemented in the exact Fourier
acceleration (EFA) method. It completely removes autocorrelations for
near-harmonic potentials and consistently yields (close-to-) optimal results
for numerical simulations of the Su-Schrieffer-Heeger and the Ising models as
well as in lattice gauge theory, in some cases reducing the autocorrelation by
multiple orders of magnitude. EFA is advantageous for and easily applicable to
any HMC simulation of an action that includes a quadratic part.


### PINN-MEP: Continuous Neural Representations for Minimum-Energy Path Discovery in Molecular Systems
**Authors**: Magnus Petersen, Roberto Covino

**Published Date**: 2025-04-23

**Updated Date**: 2025-05-06

**PDF Url**: [2504.16381v3](http://arxiv.org/pdf/2504.16381v3)

**Abstract**: Characterizing conformational transitions in physical systems remains a
fundamental challenge in the computational sciences. Traditional sampling
methods like molecular dynamics (MD) or MCMC often struggle with the
high-dimensional nature of molecular systems and the high energy barriers of
transitions between stable states. While these transitions are rare events in
simulation timescales, they often represent the most biologically significant
processes - for example, the conformational change of an ion channel protein
from its closed to open state, which controls cellular ion flow and is crucial
for neural signaling. Such transitions in real systems may take milliseconds to
seconds but could require months or years of continuous simulation to observe
even once. We present a method that reformulates transition path generation as
a continuous optimization problem solved through physics-informed neural
networks (PINNs) inspired by string methods for minimum-energy path (MEP)
generation. By representing transition paths as implicit neural functions and
leveraging automatic differentiation with differentiable molecular dynamics
force fields, our method enables the efficient discovery of physically
realistic transition pathways without requiring expensive path sampling. We
demonstrate our method's effectiveness on two proteins, including an explicitly
hydrated bovine pancreatic trypsin inhibitor (BPTI) system with over 8,300
atoms.


### Black holes, fast scrambling and the breakdown of the equivalence principle
**Authors**: Zhi-Wei Wang, Saurya Das, Samuel L. Braunstein

**Published Date**: 2022-06-04

**Updated Date**: 2025-05-06

**PDF Url**: [2206.02053v2](http://arxiv.org/pdf/2206.02053v2)

**Abstract**: Under reasonable assumptions, black holes have been argued to form firewalls,
burning up anything crossing their horizons. This argument finds that a
firewall would appear very late in a black hole's lifetime, when Hawking
radiation has caused the horizon to shrink to one-half its original area. For
stellar-mass black holes, this process surpasses the universe's current age and
so no such black hole would currently possess a firewall. However, black holes
have recently been conjectured to scramble their interior degrees-of-freedom,
with a scrambling time scale comparable to the time it takes light to travel a
Schwartzschild radius' distance. We prove that local observers will already
experience a firewall from the scrambling time onwards after the black hole's
formation. Here `local' means that the observer couples to fewer than one-half
the black hole's total interior `qubits.' Indeed, for observers to fail to be
local in this manner, it would mean that they couple to more `qubits' within
such black holes than exist in all the stars of the observable universe.
Therefore we find that if black holes are indeed fast scramblers, then every
astrophysical black hole in the universe will already have a fully developed
firewall for any local physical process.


### A Synergistic Framework of Nonlinear Acoustic Computing and Reinforcement Learning for Real-World Human-Robot Interaction
**Authors**: Xiaoliang Chen, Xin Yu, Le Chang, Yunhe Huang, Jiashuai He, Shibo Zhang, Jin Li, Likai Lin, Ziyu Zeng, Xianling Tu, Shuyu Zhang

**Published Date**: 2025-05-04

**Updated Date**: 2025-05-06

**PDF Url**: [2505.01998v2](http://arxiv.org/pdf/2505.01998v2)

**Abstract**: This paper introduces a novel framework integrating nonlinear acoustic
computing and reinforcement learning to enhance advanced human-robot
interaction under complex noise and reverberation. Leveraging physically
informed wave equations (e.g., Westervelt, KZK), the approach captures
higher-order phenomena such as harmonic generation and shock formation. By
embedding these models in a reinforcement learning-driven control loop, the
system adaptively optimizes key parameters (e.g., absorption, beamforming) to
mitigate multipath interference and non-stationary noise. Experimental
evaluations, covering far-field localization, weak signal detection, and
multilingual speech recognition, demonstrate that this hybrid strategy
surpasses traditional linear methods and purely data-driven baselines,
achieving superior noise suppression, minimal latency, and robust accuracy in
demanding real-world scenarios. The proposed system demonstrates broad
application prospects in AI hardware, robot, machine audition, artificial
audition, and brain-machine interfaces.


### A Centrality-independent Framework for Revealing Genuine Higher-Order Cumulants in Heavy-Ion Collisions
**Authors**: Zhaohui Wang, Xiaofeng Luo

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03666v1](http://arxiv.org/pdf/2505.03666v1)

**Abstract**: We propose a novel centrality definition-independent method for analyzing
higher-order proton cumulants, specifically addressing the challenge of volume
fluctuations that dominate in low-energy heavy-ion collisions. This method
reconstructs particle number distributions using the Edgeworth expansion, with
parameters optimized via a combination of differential evolution algorithm and
Bayesian inference. Its effectiveness is validated using UrQMD model
simulations and benchmarked against traditional approaches, including
centrality definitions based on particle multiplicity. Our results show that
the proposed framework yields cumulant patterns consistent with those obtained
using number of participant nucleon ($N_{\text{part}}$) based centrality
observables, while eliminating the conventional reliance on centrality
determination. This consistency confirms the method's ability to extract
genuine physical signals, thereby paving the way for probing the intrinsic
thermodynamic properties of the produced medium through event-by-event
fluctuations.


### Ultrafast Non-Hermitian Skin Effect
**Authors**: Barbara Schneider, Alexander Dikopoltsev, Markus Bestler, Philipp Täschler, Mattias Beck, David Burghoff, Oded Zilberberg, Jérome Faist

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03658v1](http://arxiv.org/pdf/2505.03658v1)

**Abstract**: Topological phases of matter commonly feature protected states at their
boundaries. Transferring this protection to time-metamaterials is extremely
challenging, as it requires the generation of an abrupt interface between two
topologically distinct bulks. Here, we realize and measure an ultrafast
topological non-Hermitian skin mode bound to an interface circulating within
the cavity of a fast-gain semiconductor laser. The nonlinear stationary state
generated in such devices features a jump in the instantaneous frequency. We
show that this discontinuity gives rise to a topological interface for the
field fluctuations in the system. Using direct intensity sampling, we
experimentally measure the skin modes and their positioning at the frequency
jump of the stationary state. Analysis of these isolated modes reveals an
ultrashort full-width at half-maximum of 583 $\pm$ 16 fs. Furthermore, we show
that we can tune the shape and relative timing shift of the skin modes via
external bias modulation. Finally, both numerical and experimental analysis of
the noise in the system reveal that field fluctuations are funneled into the
topological interface. Our findings reveal a new way to generate topologically
protected states of light in time, which paves the way for novel time-varying
physics as well as metrological applications.


### Rapid, Broadband, Optical Spectroscopy of Cold Radicals
**Authors**: Ashay N. Patel, Madison I. Howard, Timothy C. Steimle, Nicholas R. Hutzler

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03650v1](http://arxiv.org/pdf/2505.03650v1)

**Abstract**: Optical spectroscopy of molecular radicals is an important tool in physical
chemistry, and is a prerequisite for many experiments which use molecules for
quantum science and precision measurement. However, even the simplest molecules
have complex spectra which can be very time consuming to measure. Here we
present an approach which offers the ability to measure the optical spectra of
cryogenically-cooled molecular radicals with much greater efficiency. By
combining a supercontinuum laser with a cryogenic buffer gas molecular source
and a commercial optical spectrometer, we realize 15 nm of simultaneous
bandwidth with 0.56 pm $(\approx 0.5$ GHz) resolution and high sensitivity. As
a demonstration we measure and assign hundreds of lines and dozens of molecular
constants from 15 bands in the $B^2\Sigma^+-X^2\Sigma^+$ system of CaF,
including a low-abundance isotopologue, in a few hours. The setup is robust,
simple, and should enable spectroscopy of molecular radicals with much higher
throughput.


## Diffusion
### BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modelling
**Authors**: Hao Li, Yuhao Huang, Chang Xu, Viktor Schlegel, Renhe Jiang, Riza Batista-Navarro, Goran Nenadic, Jiang Bian

**Published Date**: 2025-03-04

**Updated Date**: 2025-05-06

**PDF Url**: [2503.02445v3](http://arxiv.org/pdf/2503.02445v3)

**Abstract**: Time-series Generation (TSG) is a prominent research area with broad
applications in simulations, data augmentation, and counterfactual analysis.
While existing methods have shown promise in unconditional single-domain TSG,
real-world applications demand for cross-domain approaches capable of
controlled generation tailored to domain-specific constraints and
instance-level requirements. In this paper, we argue that text can provide
semantic insights, domain information and instance-specific temporal patterns,
to guide and improve TSG. We introduce ``Text-Controlled TSG'', a task focused
on generating realistic time series by incorporating textual descriptions. To
address data scarcity in this setting, we propose a novel LLM-based Multi-Agent
framework that synthesizes diverse, realistic text-to-TS datasets. Furthermore,
we introduce BRIDGE, a hybrid text-controlled TSG framework that integrates
semantic prototypes with text description for supporting domain-level guidance.
This approach achieves state-of-the-art generation fidelity on 11 of 12
datasets, and improves controllability by 12.52% on MSE and 6.34% MAE compared
to no text input generation, highlighting its potential for generating tailored
time-series data.


### Real-Time Person Image Synthesis Using a Flow Matching Model
**Authors**: Jiwoo Jeong, Kirok Kim, Wooju Kim, Nam-Joon Kim

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03562v1](http://arxiv.org/pdf/2505.03562v1)

**Abstract**: Pose-Guided Person Image Synthesis (PGPIS) generates realistic person images
conditioned on a target pose and a source image. This task plays a key role in
various real-world applications, such as sign language video generation, AR/VR,
gaming, and live streaming. In these scenarios, real-time PGPIS is critical for
providing immediate visual feedback and maintaining user immersion.However,
achieving real-time performance remains a significant challenge due to the
complexity of synthesizing high-fidelity images from diverse and dynamic human
poses. Recent diffusion-based methods have shown impressive image quality in
PGPIS, but their slow sampling speeds hinder deployment in time-sensitive
applications. This latency is particularly problematic in tasks like generating
sign language videos during live broadcasts, where rapid image updates are
required. Therefore, developing a fast and reliable PGPIS model is a crucial
step toward enabling real-time interactive systems. To address this challenge,
we propose a generative model based on flow matching (FM). Our approach enables
faster, more stable, and more efficient training and sampling. Furthermore, the
proposed model supports conditional generation and can operate in latent space,
making it especially suitable for real-time PGPIS applications where both speed
and quality are critical. We evaluate our proposed method, Real-Time Person
Image Synthesis Using a Flow Matching Model (RPFM), on the widely used
DeepFashion dataset for PGPIS tasks. Our results show that RPFM achieves
near-real-time sampling speeds while maintaining performance comparable to the
state-of-the-art models. Our methodology trades off a slight, acceptable
decrease in generated-image accuracy for over a twofold increase in generation
speed, thereby ensuring real-time performance.


### Generating Synthetic Data via Augmentations for Improved Facial Resemblance in DreamBooth and InstantID
**Authors**: Koray Ulusan, Benjamin Kiefer

**Published Date**: 2025-05-06

**Updated Date**: 2025-05-06

**PDF Url**: [2505.03557v1](http://arxiv.org/pdf/2505.03557v1)

**Abstract**: The personalization of Stable Diffusion for generating professional portraits
from amateur photographs is a burgeoning area, with applications in various
downstream contexts. This paper investigates the impact of augmentations on
improving facial resemblance when using two prominent personalization
techniques: DreamBooth and InstantID. Through a series of experiments with
diverse subject datasets, we assessed the effectiveness of various augmentation
strategies on the generated headshots' fidelity to the original subject. We
introduce FaceDistance, a wrapper around FaceNet, to rank the generations based
on facial similarity, which aided in our assessment. Ultimately, this research
provides insights into the role of augmentations in enhancing facial
resemblance in SDXL-generated portraits, informing strategies for their
effective deployment in downstream applications.


### OSMamba: Omnidirectional Spectral Mamba with Dual-Domain Prior Generator for Exposure Correction
**Authors**: Gehui Li, Bin Chen, Chen Zhao, Lei Zhang, Jian Zhang

**Published Date**: 2024-11-22

**Updated Date**: 2025-05-06

**PDF Url**: [2411.15255v2](http://arxiv.org/pdf/2411.15255v2)

**Abstract**: Exposure correction is a fundamental problem in computer vision and image
processing. Recently, frequency domain-based methods have achieved impressive
improvement, yet they still struggle with complex real-world scenarios under
extreme exposure conditions. This is due to the local convolutional receptive
fields failing to model long-range dependencies in the spectrum, and the
non-generative learning paradigm being inadequate for retrieving lost details
from severely degraded regions. In this paper, we propose Omnidirectional
Spectral Mamba (OSMamba), a novel exposure correction network that incorporates
the advantages of state space models and generative diffusion models to address
these limitations. Specifically, OSMamba introduces an omnidirectional spectral
scanning mechanism that adapts Mamba to the frequency domain to capture
comprehensive long-range dependencies in both the amplitude and phase spectra
of deep image features, hence enhancing illumination correction and structure
recovery. Furthermore, we develop a dual-domain prior generator that learns
from well-exposed images to generate a degradation-free diffusion prior
containing correct information about severely under- and over-exposed regions
for better detail restoration. Extensive experiments on multiple-exposure and
mixed-exposure datasets demonstrate that the proposed OSMamba achieves
state-of-the-art performance both quantitatively and qualitatively.


### Taking a Big Step: Large Learning Rates in Denoising Score Matching Prevent Memorization
**Authors**: Yu-Han Wu, Pierre Marion, Gérard Biau, Claire Boyer

**Published Date**: 2025-02-05

**Updated Date**: 2025-05-06

**PDF Url**: [2502.03435v2](http://arxiv.org/pdf/2502.03435v2)

**Abstract**: Denoising score matching plays a pivotal role in the performance of
diffusion-based generative models. However, the empirical optimal score--the
exact solution to the denoising score matching--leads to memorization, where
generated samples replicate the training data. Yet, in practice, only a
moderate degree of memorization is observed, even without explicit
regularization. In this paper, we investigate this phenomenon by uncovering an
implicit regularization mechanism driven by large learning rates. Specifically,
we show that in the small-noise regime, the empirical optimal score exhibits
high irregularity. We then prove that, when trained by stochastic gradient
descent with a large enough learning rate, neural networks cannot stably
converge to a local minimum with arbitrarily small excess risk. Consequently,
the learned score cannot be arbitrarily close to the empirical optimal score,
thereby mitigating memorization. To make the analysis tractable, we consider
one-dimensional data and two-layer neural networks. Experiments validate the
crucial role of the learning rate in preventing memorization, even beyond the
one-dimensional setting.


