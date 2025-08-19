# Abstracts of Papers

## Physics
### Modeling wind farm noise emission and propagation: effects of flow layout
**Authors**: J. Colas, A. Emmanuelli, D. Dragna, R. J. A. M. Stevens

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13128v1](http://arxiv.org/pdf/2508.13128v1)

**Abstract**: This study demonstrates how wind farm flow physics influence noise generation
and downstream propagation through numerical simulations. The flow field is
modeled using large-eddy simulations (LES), and the time-averaged output serves
as input to acoustic models that predict wind turbine noise. In the first
turbine row, turbulence-induced noise (TIN) and trailing edge noise (TEN)
contribute equally, with TIN dominating at low frequencies and TEN at higher
frequencies. Downstream, TEN decreases due to lower wind speeds, while TIN
mostly persists due to increased turbulence dissipation. These effects are more
pronounced in aligned wind farms, where stronger wake interactions occur, than
in staggered layouts. However, staggered farms produce more noise overall
because turbines operate at higher wind speeds.Additionally, wind farm flow
significantly affects sound propagation downwind. The wake superposition
modifies sound focusing leading to different amplification area than for an
isolated turbine. For a staggered layout it particularly shows enhanced sound
focusing downwind due to the position of the turbine wakes. This leads to
higher sound levels and higher amplitude modulation downwind for the wind farm
compared to an aligned layout. These phenomena are not captured by models based
on isolated turbines. These findings underscore the importance of integrating
flow and acoustic models to more accurately assess the environmental impact of
wind farms.


### Probing Spin and Lifetime Correlations in Entangled Hyperon-AntiHyperon Pairs
**Authors**: Aihong Tang

**Published Date**: 2025-07-24

**Updated Date**: 2025-08-18

**PDF Url**: [2507.18507v2](http://arxiv.org/pdf/2507.18507v2)

**Abstract**: Quantum entanglement has now been demonstrated in several hadronic systems,
revealing that non-classical spin correlations survive even through the
strong-interaction hadronization process. To date, however, all studies have
focused exclusively on angular observables, leaving the possibility untouched
that quantum coherence might also influence the decay times of entangled
partners. In this work we propose data-driven tests of spin-lifetime and
lifetime-lifetime correlations for Lambda-antiLambda pairs produced in
high-energy collisions. By examining the opening-angle distribution in slices
of Delta t, constructing a pair-wise spin-lifetime correlator, and testing a
simple lifetime-lifetime covariance, we search for deviations from independent
exponential decay that align with known spin correlations. Observation of
nonzero lifetime correlations would compel a reassessment of how entanglement
manifests in decaying systems, revealing hitherto unexplored temporal
coherence.


### Rare event sampling for moving targets: extremes of temperature and daily precipitation in a general circulation model
**Authors**: Justin Finkel, Paul A. O'Gorman

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13120v1](http://arxiv.org/pdf/2508.13120v1)

**Abstract**: Extreme weather events epitomize high cost: to society through their physical
impacts, and to computer servers that are used to simulate them to provide
information to mitigate those impacts. It costs hundreds of years to sample a
few once-per-century events with straightforward model integration, but that
cost can be much reduced with rare event sampling, which nudges ensembles of
simulations to convert moderate events to severe ones, e.g., by steering a
cyclone directly through a region of interest. With proper statistical
accounting, rare event algorithms can provide quantitative climate risk
assessment at reduced cost. But this can only work if ensemble members diverge
fast enough. Sudden, transient events characteristic of Earth's midlatitude
storm track regions, such as heavy precipitation and heat extremes, pose a
particular challenge because they come and go faster than an ensemble can
explore the possibilities. Here we extend standard rare event algorithms to
handle this challenging case in an idealized atmospheric general circulation
model, achieving 5-10 times sped-up estimation of long return periods, such as
100-150 years from only 20 years of simulation for extremes of daily
precipitation and surface temperature. The algorithm, called TEAMS
(``trying-early adaptive multilevel splitting''), was developed previously in
Finkel and O'Gorman (2024) using a toy chaotic system, and relies on a key
parameter -- the advance split time -- which may be estimated based on simple
diagnostics of ensemble dispersion rates. The results are promising for
accelerated risk assessment across a wide range of physical hazards using more
realistic and complex models with acute computational constraints.


### Noise signatures of a charged Sachdev-Ye-Kitaev dot in mesoscopic transport
**Authors**: Andrei I. Pavlov, Mikhail N. Kiselev

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13098v1](http://arxiv.org/pdf/2508.13098v1)

**Abstract**: We investigate quantum noise in a mesoscopic quantum dot serving as a
realization of the charged Sachdev-Ye-Kitaev (SYK) model weakly coupled to a
fermionic lead via a tunnel contact. We find noise signatures under voltage and
temperature biases that can serve as clear markers of the SYK physics in
experiments with related setups. We develop a linear response theory that
treats all types of noise on the same footing and generalizes a concept of
transport coefficients for charge and heat currents, as well as relations
between them, to equilibrium noise power. Within this theory, we find
characteristic scaling of the noise coefficients with temperature in all
regimes that can be relevant for experimental realizations of the SYK dots,
find a set of universal constants, with their values being unique to the SYK
physics, that connect these coefficients, and characterize noise manifestations
of the Coulomb blockade. Beyond SYK systems, these results may serve as a
general framework for identification of non-Fermi-liquid signatures in
mesoscopic transport and provide additional observables for experiments on
thermoelectric phenomena.


### AutoChemSchematic AI: Agentic Physics-Aware Automation for Chemical Manufacturing Scale-Up
**Authors**: Sakhinana Sagar Srinivas, Shivam Gupta, Venkataramana Runkana

**Published Date**: 2025-05-30

**Updated Date**: 2025-08-18

**PDF Url**: [2505.24584v3](http://arxiv.org/pdf/2505.24584v3)

**Abstract**: Recent advances in generative AI have accelerated the discovery of novel
chemicals and materials. However, scaling these discoveries to industrial
production remains a major bottleneck due to the synthesis gap -- the need to
develop entirely new manufacturing processes. This challenge requires detailed
engineering blueprints: PFDs for equipment layouts and material/energy flows,
and PIDs for process plant operations. Current AI systems cannot yet reliably
generate these critical engineering schematics, creating a fundamental obstacle
to manufacturing scale-up of novel discoveries. We present a closed-loop,
physics-aware framework for automated generation of industrially viable PFDs
and PIDs. The framework integrates three key components: (1) domain-specialized
small language models (SLMs) trained for auto-generation of PFDs and PIDs, (2)
a hierarchical knowledge graph containing process flow and instrumentation
descriptions for 1,020+ chemicals for Graph Retrieval-Augmented Generation
(GRAG), and (3) an open-source chemical process simulator for modeling,
simulation, optimization, and analysis of novel chemical processes. The SLMs
are trained through a multi-stage pipeline on synthetic datasets, with process
simulator-in-the-loop validation ensuring feasibility. To enhance computational
efficiency, the framework implements structural pruning (width and depth)
guided by importance heuristics to reduce language model size while preserving
accuracy, followed by advanced inference optimizations including
FlashAttention, Lookahead Decoding, PagedAttention with KV-cache quantization,
and Test-Time Inference Scaling. Experimental results demonstrate that our
framework generates simulator-validated process descriptions with high
fidelity.


### Poisson-Nernst-Planck charging dynamics of an electric double layer capacitor: symmetric and asymmetric binary electrolytes
**Authors**: Ivan Palaia, Adelchi J. Asta, Megh Dutta, Patrick B. Warren, Benjamin Rotenberg, Emmanuel Trizac

**Published Date**: 2023-03-14

**Updated Date**: 2025-08-18

**PDF Url**: [2303.07859v3](http://arxiv.org/pdf/2303.07859v3)

**Abstract**: A parallel plate capacitor containing an electrolytic solution is the
simplest model of a supercapacitor, or electric double layer capacitor. Using
both analytical and numerical techniques, we solve the Poisson-Nernst-Planck
equations for such a system, describing the mean-field charging dynamics of the
capacitor, when a constant potential difference is abruptly applied to its
plates. Working at constant total number of ions, we focus on the physical
processes involved in the relaxation and, whenever possible, give its
functional shape and exact time constants. We first review and study the case
of a symmetric binary electrolyte, where we assume the two ionic species to
have the same charges and diffusivities. We then relax these assumptions and
present results for a generic strong (i.e. fully dissociated) binary
electrolyte. At low electrolyte concentration, the relaxation is simple to
understand, as the dynamics of positive and negative ions appear decoupled. At
higher electrolyte concentration, we distinguish several regimes. In the linear
regime (low voltages), relaxation is multi-exponential, it starts by the
build-up of the equilibrium charge profile and continues with neutral mass
diffusion, and the relevant time scales feature both the average and the
Nernst-Hartley diffusion coefficients. In the purely nonlinear regime
(intermediate voltages), the initial relaxation is slowed down exponentially
due to increased capacitance, while bulk effects become more and more evident.
In the fully nonlinear regime (high voltages), the dynamics of charge and mass
are completely entangled and, asymptotically, the relaxation is linear in time.
We finally discuss non-ideal behavior in real capacitors and provide conditions
for which mean-field is expected to hold.


### Effective permeability conditions for diffusive transport through impermeable membranes with gaps
**Authors**: Molly Brennan, Edwina F. Yeo, Philip Pearce, Mohit P. Dalwadi

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-18

**PDF Url**: [2508.10694v2](http://arxiv.org/pdf/2508.10694v2)

**Abstract**: Membranes regulate transport in a wide variety of industrial and biological
applications. The microscale geometry of the membrane can significantly affect
overall transport through the membrane, but the precise nature of this
multiscale coupling is not well characterised in general. Motivated by the
application of transport across a bacterial membrane, in this paper we use
formal multiscale analysis to derive explicit effective coupling conditions for
macroscale transport across a two-dimensional impermeable membrane with
periodically spaced gaps, and validate these with numerical simulations. We
derive analytic expressions for effective macroscale quantities associated with
the membrane, such as the permeability, in terms of the microscale geometry.
Our results generalise the classic constitutive membrane coupling conditions to
a wider range of membrane geometries and time-varying scenarios. Specifically,
we demonstrate that if the exterior concentration varies in time, for membranes
with long channels, the transport gains a memory property where the coupling
conditions depend on the system history. By applying our effective conditions
in the context of small molecule transport through gaps in bacterial membranes
called porins, we predict that bacterial membrane permeability is primarily
dominated by the thickness of the membrane. Furthermore, we predict how
alterations to membrane microstructure, for example via changes to porin
expression, might affect overall transport, including when external
concentrations vary in time. These results will apply to a broad range of
physical applications with similar membrane structures, from medical and
industrial filtration to carbon capture.


### Primary hairs may create echoes
**Authors**: R. A. Konoplya, A. Zhidenko

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13069v1](http://arxiv.org/pdf/2508.13069v1)

**Abstract**: In most scenarios studied so far, the appearance of echoes in the ringdown
signal requires modifications external to the black hole itself, such as the
presence of matter in the near-horizon region, quantum field clouds, or exotic
compact objects like wormholes that effectively introduce additional peaks in
the effective potential. In this work we show that echoes can naturally arise
in a different setting: black holes endowed with primary Proca-Gauss-Bonnet
hair. We demonstrate that the primary hair modifies the effective potential in
such a way that a second peak is formed, giving rise to late-time echoes
without invoking any external environment or exotic horizon-scale physics.
Using both the higher-order WKB method with Pad\'e resummation and time-domain
integration, we compute the quasinormal spectrum for scalar and Dirac test
fields and show the appearance of these echoes. Our results highlight a novel
mechanism by which primary hairs alone can leave observable imprints on the
ringdown signal of black holes in modified gravity.


### Regular BTZ black holes from an infinite tower of corrections
**Authors**: Pedro G. S. Fernandes

**Published Date**: 2025-04-11

**Updated Date**: 2025-08-18

**PDF Url**: [2504.08565v2](http://arxiv.org/pdf/2504.08565v2)

**Abstract**: We explore $2+1$-dimensional scalar-tensor theories derived from well-defined
dimensional regularizations of the Lovelock invariants. In the limit where an
infinite series of corrections is included, we obtain theories that admit fully
regular black hole solutions. We analyze the properties of these regular black
holes, investigate geodesics in these spacetimes, and examine the tidal forces,
finding they remain finite everywhere.


### Quantum Phase Estimation Beyond the Gaussian Limit
**Authors**: Kimin Park, Tanjung Krisnanda, Yvonne Gao, Radim Filip

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13046v1](http://arxiv.org/pdf/2508.13046v1)

**Abstract**: Quantum metrology aims to enhance measurement precision beyond the standard
quantum limit (SQL), the benchmark set by classical resources, enabling
advances in sensing, imaging, and fundamental physics. A critical milestone
beyond the SQL is surpassing the Gaussian bound -- the fundamental precision
limit achievable with any Gaussian state, such as optimally squeezed states.
Certain non-Gaussian states, specifically asymmetric superpositions of coherent
states (SCS) and superpositions of a vacuum and a Fock state (ON states), can
outperform this Gaussian bound within an intermediate energy range. In
particular, asymmetric SCS emerge as a highly practical resource for near-term
quantum sensing architectures operating beyond the Gaussian limit due to their
efficient preparation and processing via a constant-complexity protocol. Our
comprehensive analysis under realistic loss, noise, and detection schemes
quantifies the critical trade-off between achievable precision and the
operational range of the non-Gaussian advantage. This work sheds light on the
fundamental impact of non-Gaussianity and asymmetry on metrological tasks, and
offers insights on how to leverage such resources in realistic near-term
quantum enhanced sensors beyond the Gaussian limit.


## Diffusion
### MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models
**Authors**: Haoyu He, Katrin Renz, Yong Cao, Andreas Geiger

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13148v1](http://arxiv.org/pdf/2508.13148v1)

**Abstract**: Diffusion language models, as a promising alternative to traditional
autoregressive (AR) models, enable faster generation and richer conditioning on
bidirectional context. However, they suffer from a key discrepancy between
training and inference: during inference, MDLMs progressively reveal the
structure of the generated sequence by producing fewer and fewer masked tokens,
whereas this structure is ignored in training as tokens are masked at random.
Although this discrepancy between training and inference can lead to suboptimal
performance, it has been largely overlooked by previous works, leaving closing
this gap between the two stages an open problem. To address this, we frame the
problem of learning effective denoising trajectories as a sequential
decision-making problem and use the resulting framework to apply reinforcement
learning. We propose a novel Masked Diffusion Policy Optimization (MDPO) to
exploit the Markov property diffusion possesses and explicitly train the model
under the same progressive refining schedule used at inference. MDPO matches
the performance of the previous state-of-the-art (SOTA) method with 60x fewer
gradient updates, while achieving average improvements of 9.6% on MATH500 and
54.2% on Countdown over SOTA when trained within the same number of weight
updates. Additionally, we improve the remasking strategy of MDLMs as a plug-in
inference replacement to overcome the limitation that the model cannot refine
tokens flexibly. This simple yet effective training-free strategy, what we
refer to as RCR, consistently improves performance and yields additional gains
when combined with MDPO. Our findings establish great potential for
investigating the discrepancy between pre-training and inference of MDLMs.
Code: https://github.com/autonomousvision/mdpo. Project Page:
https://cli212.github.io/MDPO/.


### Denoising diffusion models for inverse design of inflatable structures with programmable deformations
**Authors**: Sara Karimi, Nikolaos N. Vlassis

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13097v1](http://arxiv.org/pdf/2508.13097v1)

**Abstract**: Programmable structures are systems whose undeformed geometries and material
property distributions are deliberately designed to achieve prescribed deformed
configurations under specific loading conditions. Inflatable structures are a
prominent example, using internal pressurization to realize large, nonlinear
deformations in applications ranging from soft robotics and deployable
aerospace systems to biomedical devices and adaptive architecture. We present a
generative design framework based on denoising diffusion probabilistic models
(DDPMs) for the inverse design of elastic structures undergoing large,
nonlinear deformations under pressure-driven actuation. The method formulates
the inverse design as a conditional generation task, using geometric
descriptors of target deformed states as inputs and outputting image-based
representations of the undeformed configuration. Representing these
configurations as simple images is achieved by establishing a pre- and
postprocessing pipeline that involves a fixed image processing, simulation
setup, and descriptor extraction methods. Numerical experiments with scalar and
higher-dimensional descriptors show that the framework can quickly produce
diverse undeformed configurations that achieve the desired deformations when
inflated, enabling parallel exploration of viable design candidates while
accommodating complex constraints.


### From Transthoracic to Transesophageal: Cross-Modality Generation using LoRA Diffusion
**Authors**: Emmanuel Oladokun, Yuxuan Ou, Anna Novikova, Daria Kulikova, Sarina Thomas, Jurica Šprem, Vicente Grau

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13077v1](http://arxiv.org/pdf/2508.13077v1)

**Abstract**: Deep diffusion models excel at realistic image synthesis but demand large
training sets-an obstacle in data-scarce domains like transesophageal
echocardiography (TEE). While synthetic augmentation has boosted performance in
transthoracic echo (TTE), TEE remains critically underrepresented, limiting the
reach of deep learning in this high-impact modality.
  We address this gap by adapting a TTE-trained, mask-conditioned diffusion
backbone to TEE with only a limited number of new cases and adapters as small
as $10^5$ parameters. Our pipeline combines Low-Rank Adaptation with MaskR$^2$,
a lightweight remapping layer that aligns novel mask formats with the
pretrained model's conditioning channels. This design lets users adapt models
to new datasets with a different set of anatomical structures to the base
model's original set.
  Through a targeted adaptation strategy, we find that adapting only MLP layers
suffices for high-fidelity TEE synthesis. Finally, mixing less than 200 real
TEE frames with our synthetic echoes improves the dice score on a multiclass
segmentation task, particularly boosting performance on underrepresented
right-heart structures. Our results demonstrate that (1) semantically
controlled TEE images can be generated with low overhead, (2) MaskR$^2$
effectively transforms unseen mask formats into compatible formats without
damaging downstream task performance, and (3) our method generates images that
are effective for improving performance on a downstream task of multiclass
segmentation.


### Reinforced Context Order Recovery for Adaptive Reasoning and Planning
**Authors**: Long Ma, Fangwei Zhong, Yizhou Wang

**Published Date**: 2025-08-18

**Updated Date**: 2025-08-18

**PDF Url**: [2508.13070v1](http://arxiv.org/pdf/2508.13070v1)

**Abstract**: Modern causal language models, followed by rapid developments in discrete
diffusion models, can now produce a wide variety of interesting and useful
content. However, these families of models are predominantly trained to output
tokens with a fixed (left-to-right) or random order, which may deviate from the
logical order in which tokens are generated originally. In this paper, we
observe that current causal and diffusion models encounter difficulties in
problems that require adaptive token generation orders to solve tractably,
which we characterize with the $\mathcal{V}$-information framework. Motivated
by this, we propose Reinforced Context Order Recovery (ReCOR), a
reinforcement-learning-based framework to extract adaptive, data-dependent
token generation orders from text data without annotations. Self-supervised by
token prediction statistics, ReCOR estimates the hardness of predicting every
unfilled token and adaptively selects the next token during both training and
inference. Experiments on challenging reasoning and planning datasets
demonstrate the superior performance of ReCOR compared with baselines,
sometimes outperforming oracle models supervised with the ground-truth order.


### Improving Text Style Transfer using Masked Diffusion Language Models with Inference-time Scaling
**Authors**: Tejomay Kishor Padole, Suyash P Awate, Pushpak Bhattacharyya

**Published Date**: 2025-08-14

**Updated Date**: 2025-08-18

**PDF Url**: [2508.10995v2](http://arxiv.org/pdf/2508.10995v2)

**Abstract**: Masked diffusion language models (MDMs) have recently gained traction as a
viable generative framework for natural language. This can be attributed to its
scalability and ease of training compared to other diffusion model paradigms
for discrete data, establishing itself as the state-of-the-art
non-autoregressive generator for discrete data. Diffusion models, in general,
have shown excellent ability to improve the generation quality by leveraging
inference-time scaling either by increasing the number of denoising steps or by
using external verifiers on top of the outputs of each step to guide the
generation. In this work, we propose a verifier-based inference-time scaling
method that aids in finding a better candidate generation during the denoising
process of the MDM. Our experiments demonstrate the application of MDMs for
standard text-style transfer tasks and establish MDMs as a better alternative
to autoregressive language models. Additionally, we show that a simple
soft-value-based verifier setup for MDMs using off-the-shelf pre-trained
embedding models leads to significant gains in generation quality even when
used on top of typical classifier-free guidance setups in the existing
literature.


