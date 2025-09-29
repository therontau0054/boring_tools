# Abstracts of Papers

## Physics
### Toward a Physics of Deep Learning and Brains
**Authors**: Arsham Ghavasieh, Meritxell Vila-Minana, Akanksha Khurd, John Beggs, Gerardo Ortiz, Santo Fortunato

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22649v1](http://arxiv.org/pdf/2509.22649v1)

**Abstract**: Deep neural networks and brains both learn and share superficial
similarities: processing nodes are likened to neurons and adjustable weights
are likened to modifiable synapses. But can a unified theoretical framework be
found to underlie them both? Here we show that the equations used to describe
neuronal avalanches in living brains can also be applied to cascades of
activity in deep neural networks. These equations are derived from
non-equilibrium statistical physics and show that deep neural networks learn
best when poised between absorbing and active phases. Because these networks
are strongly driven by inputs, however, they do not operate at a true critical
point but within a quasi-critical regime -- one that still approximately
satisfies crackling noise scaling relations. By training networks with
different initializations, we show that maximal susceptibility is a more
reliable predictor of learning than proximity to the critical point itself.
This provides a blueprint for engineering improved network performance.
Finally, using finite-size scaling we identify distinct universality classes,
including Barkhausen noise and directed percolation. This theoretical framework
demonstrates that universal features are shared by both biological and
artificial neural networks.


### Overview of the ESCAPE Dark Matter Test Science Project for Astronomers
**Authors**: James Pearson, Hugh Dickinson, Sukanya Sinha, Stephen Serjeant

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22609v1](http://arxiv.org/pdf/2509.22609v1)

**Abstract**: The search for dark matter has been ongoing for decades within both
astrophysics and particle physics. Both fields have employed different
approaches and conceived a variety of methods for constraining the properties
of dark matter, but have done so in relative isolation of one another. From an
astronomer's perspective, it can be challenging to interpret the results of
dark matter particle physics experiments and how these results apply to
astrophysical scales. Over the past few years, the ESCAPE Dark Matter Test
Science Project has been developing tools to aid the particle physics community
in constraining dark matter properties; however, ESCAPE itself also aims to
foster collaborations between research disciplines. This is especially
important in the search for dark matter, as while particle physics is concerned
with detecting the particles themselves, all of the evidence for its existence
lies solely within astrophysics and cosmology. Here, we present a short review
of the progress made by the Dark Matter Test Science Project and their
applications to existing experiments, with a view towards how this project can
foster complementary with astrophysical observations.


### Probing Fractional Quantum Hall states in weakly interacting Fermi gases
**Authors**: Viktor Bekassy, Mikael Fogelström, Johannes Hofmann

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22606v1](http://arxiv.org/pdf/2509.22606v1)

**Abstract**: Quantum gases are used to simulate the physics of the lowest Landau level
(LLL) with neutral atoms, which in the simplest setup is achieved by rotating
the gas at the confining harmonic trap frequency, a requirement that is
difficult to achieve in practice. We point out that for weakly interacting
Fermi gases, this rapid-rotation limit is not needed to access the LLL: As a
direct consequence of first-order perturbation theory, many-body wave functions
of states in the LLL remain unchanged at any rotation, and only their energies
shift. This implies that even in the absence of rotations or for moderate
rotations frequencies, LLL states are present as excited states at finite
angular momentum. For fermions with contact interactions, these states are
exact eigenstates of a paradigmatic model of Fractional Quantum Hall (FQH)
states described by a single Haldane pseudopotential ($V_1$ for spin-polarized
and $V_0$ for spinful systems), which realizes exact Laughlin and Haldane wave
functions. We suggest that recently developed excitation and imaging techniques
for rotating few-fermion systems allow for a detailed experimental
investigation of FQH wave functions and to study the crossover to large
particle number. We illustrate this for $N = 6$ spin-balanced fermions


### Relativistic Quantum Simulation under Periodic and Dirichlet Boundary Conditions: A First-Quantised Framework for Near-Term Devices
**Authors**: Jaewoo Joo, Timothy P. Spiller, Kyunghyun Baek, Jeongho Bang

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22579v1](http://arxiv.org/pdf/2509.22579v1)

**Abstract**: We present a new recipe for relativistic quantum simulation using the first
quantisation approach, under periodic (PBC) and Dirichlet (DBC) boundary
conditions. The wavefunction is discretised across a finite grid represented by
system qubits, and the squared momentum operator is expressed using the
finite-difference method based on quantum translation operations. The
relativistic kinetic energy is approximated through a perturbative expansion of
the total kinetic Hamiltonian, incorporating higher-order momentum terms. The
approach would allow variational optimisation of appropriate ansatz states to
estimate both non-relativistic and relativistic ground-state energies on a
quantum computer. This work offers a practical route to simulating relativistic
effects on near-term quantum devices, supporting future developments in quantum
physics and chemistry.


### A $ν$ look at the Sun: Probing the conditions of the solar core using $^8$B neutrinos
**Authors**: Melanie A. Zaidel, John F. Beacom

**Published Date**: 2025-04-14

**Updated Date**: 2025-09-26

**PDF Url**: [2504.10583v2](http://arxiv.org/pdf/2504.10583v2)

**Abstract**: In the coming age of precision neutrino physics, neutrinos from the Sun
become robust probes of the conditions of the solar core. Here, we focus on
$^8$B neutrinos, for which there are already high precision measurements by the
Sudbury Neutrino Observatory and Super-Kamiokande. Using only basic physical
principles and straightforward statistical tools, we estimate projected
constraints on the temperature and density of the $^8$B neutrino production
zone compared to a reference solar model. We outline how to better understand
the astrophysics of the solar interior using forthcoming neutrino data and
solar models. Finally, we note that detailed forward modeling will be needed to
develop the full potential of this approach.


### Two failure modes of deep transformers and how to avoid them: a unified theory of signal propagation at initialisation
**Authors**: Alessio Giorlandino, Sebastian Goldt

**Published Date**: 2025-05-30

**Updated Date**: 2025-09-26

**PDF Url**: [2505.24333v2](http://arxiv.org/pdf/2505.24333v2)

**Abstract**: Finding the right initialisation for neural networks is crucial to ensure
smooth training and good performance. In transformers, the wrong initialisation
can lead to one of two failure modes of self-attention layers: rank collapse,
where all tokens collapse into similar representations, and entropy collapse,
where highly concentrated attention scores lead to training instability. While
previous work has studied different scaling regimes for transformers, an
asymptotically exact, down-to-the constant prescription for how to initialise
transformers has so far been lacking. Here, we provide an analytical theory of
signal propagation through deep transformers with self-attention, layer
normalisation, skip connections and MLP. Our theory yields a simple algorithm
to compute trainability diagrams that identify the correct choice of
initialisation hyper-parameters for a given architecture. We overcome the key
challenge, an exact treatment of the self-attention layer, by establishing a
formal parallel with the Random Energy Model from statistical physics. We also
analyse gradients in the backward path and determine the regime where gradients
vanish at initialisation. We demonstrate the versatility of our framework
through three case studies. Our theoretical framework gives a unified
perspective on the two failure modes of self-attention and gives quantitative
predictions on the scale of both weights and residual connections that
guarantee smooth training.


### Naturalistic intuitionism for physics
**Authors**: Bruno Bentzen, Flavio Del Santo, Nicolas Gisin

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22528v1](http://arxiv.org/pdf/2509.22528v1)

**Abstract**: Recently, a novel intuitionistic reconstruction of the foundations of physics
has been primarily developed by Nicolas Gisin and Flavio Del Santo drawing on
naturalism. Our goal in this paper is to examine and develop the philosophical
background of their naturalistic intuitionism for physics in contrast with
Brouwer's defense of his intuitionistic mathematics. To be exact, we propose a
systematic rearticulation of Brouwer's so-called two acts of intuitionism to
serve as the self-contained philosophical framework justifying naturalistic
intuitionism in physics. This revision is accompanied by an investigation of
the distinctive naturalistic treatment of some central intuitionistic topics,
including logic, language, time, ontology, meaning, and truth.


### Dirac Oscillator for Spin-1/2 Particles in a Spinning Cosmic String Spacetime with Spacelike Disclination and Dislocation
**Authors**: Abdelmalek Boumali

**Published Date**: 2025-09-19

**Updated Date**: 2025-09-26

**PDF Url**: [2509.18197v2](http://arxiv.org/pdf/2509.18197v2)

**Abstract**: We study the Dirac oscillator for spin-1/2 particles in a spacetime
containing a spinning cosmic string endowed with both curvature (disclination)
and torsion (screw dislocation). The background geometry includes off-diagonal
and is analyzed through a local tetrad formalism. Working in cylindrical
coordinates, we derive the covariant Dirac equation and solve it exactly via a
second-order differential equation for the lower spinor component. Three
distinct physical configurations are examined: (i) balanced torsion where
temporal and spatial contributions are equal, (ii) purely temporal torsion
(spinning string), and (iii) purely spatial torsion (screw dislocation). In all
cases, we obtain exact energy spectra expressed in terms of effective angular
quantum numbers that depend on the oscillator frequency, the angular deficit
parameter \alpha , the torsional parameters J_{t} and J_{z}, and the
longitudinal momentum k. The resulting energy levels generalize the
flat-spacetime Moshinsky oscillator spectrum by incorporating energy- and
momentum-dependent shifts due to the background geometry. We show that
curvature and torsion lift degeneracies and induce nontrivial modifications to
the angular structure of the solutions. The flat-space spectrum is recovered as
a special limit when both curvature and torsion vanish. This work provides a
fully solvable model that illustrates how spacetime defects affect relativistic
quantum systems, offering insights relevant to both high-energy physics and
condensed-matter analogs.


### Cryogenic In-Memory Computing with Phase-Change Memory
**Authors**: Davide G. F. Lombardo, Siddharth Gautam, Alberto Ferraris, Manuel Le Gallo, Abu Sebastian, Ghazi Sarwat Syed

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22511v1](http://arxiv.org/pdf/2509.22511v1)

**Abstract**: In-memory computing (IMC) is an emerging non-von Neumann paradigm that
leverages the intrinsic physics of memory devices to perform computations
directly within the memory array. Among the various candidates, phase-change
memory (PCM) has emerged as a leading non-volatile technology, showing
significant promise for IMC, particularly in deep learning acceleration.
PCM-based IMC is also poised to play a pivotal role in cryogenic applications,
including quantum computing and deep space electronics. In this work, we
present a comprehensive characterization of PCM devices across temperatures
down to 5 K, covering the range most relevant to these domains. We
systematically investigate key physical mechanisms such as phase transitions
and threshold switching that govern device programming at low temperatures. In
addition, we study attributes including electrical transport, structural
relaxation, and read noise, which critically affect readout behavior and, in
turn, the precision achievable in computational tasks.


### Model Training, Data Assimilation, and Forecast Experiments with a Hybrid Atmospheric Model that Incorporates Machine Learning
**Authors**: Dylan Elliott, Troy Arcomano, Istvan Szunyogh, Brian R. Hunt

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22465v1](http://arxiv.org/pdf/2509.22465v1)

**Abstract**: The hybrid model combines the physics-based primitive-equations model SPEEDY
with a machine learning-based (ML-based) model component, while ERA5 reanalyses
provide the presumed true states of the atmosphere. Six-hourly simulated noisy
observations are generated for a 30-year ML training period and a one-year
testing period. These observations are assimilated with a Local Ensemble
Transform Kalman Filter (LETKF), and a 10-day deterministic forecast is also
started from each ensemble mean analysis of the testing period. In the first
experiment, the physics-based model provides the background ensemble members
and the 10-day deterministic forecasts. In the other three experiments, the
hybrid model plays the same role as the physics-based model in the first
experiment, but it is trained on a different data set in each experiment. These
training data sets are analyses obtained by using the physics-based model
(second experiment), the hybrid model of the previous experiment (third
experiment), and for comparison, ERA5 reanalyses (fourth experiment). The
results of the experiments show that hybridizing the model can substantially
improve the accuracy of the analyses and forecasts. When the model is trained
on ERA5 reanalyses, the biases of the analyses are negligible and the magnitude
of the flow-dependent part of the analysis errors is greatly reduced. While the
gains in analysis accuracy are distinctly more modest in the other two hybrid
model experiments, the gains in forecast accuracy tend to be larger in those
experiments after 1-3 forecast days. However, these extra gains of forecast
accuracy are achieved, in part, by a modest gradual reduction of the spatial
variability of the forecasts.


## Diffusion
### Scale-Wise VAR is Secretly Discrete Diffusion
**Authors**: Amandeep Kumar, Nithin Gopalakrishnan Nair, Vishal M. Patel

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22636v1](http://arxiv.org/pdf/2509.22636v1)

**Abstract**: Autoregressive (AR) transformers have emerged as a powerful paradigm for
visual generation, largely due to their scalability, computational efficiency
and unified architecture with language and vision. Among them, next scale
prediction Visual Autoregressive Generation (VAR) has recently demonstrated
remarkable performance, even surpassing diffusion-based models. In this work,
we revisit VAR and uncover a theoretical insight: when equipped with a
Markovian attention mask, VAR is mathematically equivalent to a discrete
diffusion. We term this reinterpretation as Scalable Visual Refinement with
Discrete Diffusion (SRDD), establishing a principled bridge between AR
transformers and diffusion models. Leveraging this new perspective, we show how
one can directly import the advantages of diffusion such as iterative
refinement and reduce architectural inefficiencies into VAR, yielding faster
convergence, lower inference cost, and improved zero-shot reconstruction.
Across multiple datasets, we show that the diffusion based perspective of VAR
leads to consistent gains in efficiency and generation.


### Training-Free Synthetic Data Generation with Dual IP-Adapter Guidance
**Authors**: Luc Boudier, Loris Manganelli, Eleftherios Tsonis, Nicolas Dufour, Vicky Kalogeiton

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22635v1](http://arxiv.org/pdf/2509.22635v1)

**Abstract**: Few-shot image classification remains challenging due to the limited
availability of labeled examples. Recent approaches have explored generating
synthetic training data using text-to-image diffusion models, but often require
extensive model fine-tuning or external information sources. We present a novel
training-free approach, called DIPSY, that leverages IP-Adapter for
image-to-image translation to generate highly discriminative synthetic images
using only the available few-shot examples. DIPSY introduces three key
innovations: (1) an extended classifier-free guidance scheme that enables
independent control over positive and negative image conditioning; (2) a class
similarity-based sampling strategy that identifies effective contrastive
examples; and (3) a simple yet effective pipeline that requires no model
fine-tuning or external captioning and filtering. Experiments across ten
benchmark datasets demonstrate that our approach achieves state-of-the-art or
comparable performance, while eliminating the need for generative model
adaptation or reliance on external tools for caption generation and image
filtering. Our results highlight the effectiveness of leveraging dual image
prompting with positive-negative guidance for generating class-discriminative
features, particularly for fine-grained classification tasks.


### TAMMs: Temporal-Aware Multimodal Model for Satellite Image Change Understanding and Forecasting
**Authors**: Zhongbin Guo, Yuhao Wang, Ping Jian, Chengzhi Li, Xinyue Chen, Zhen Yang, Ertai E

**Published Date**: 2025-06-23

**Updated Date**: 2025-09-26

**PDF Url**: [2506.18862v2](http://arxiv.org/pdf/2506.18862v2)

**Abstract**: Temporal Change Description (TCD) and Future Satellite Image Forecasting
(FSIF) are critical, yet historically disjointed tasks in Satellite Image Time
Series (SITS) analysis. Both are fundamentally limited by the common challenge
of modeling long-range temporal dynamics. To explore how to improve the
performance of methods on both tasks simultaneously by enhancing long-range
temporal understanding capabilities, we introduce TAMMs, the first unified
framework designed to jointly perform TCD and FSIF within a single
MLLM-diffusion architecture. TAMMs introduces two key innovations: Temporal
Adaptation Modules (TAM) enhance frozen MLLM's ability to comprehend long-range
dynamics, and Semantic-Fused Control Injection (SFCI) mechanism translates this
change understanding into fine-grained generative control. This synergistic
design makes the understanding from the TCD task to directly inform and improve
the consistency of the FSIF task. Extensive experiments demonstrate TAMMs
significantly outperforms state-of-the-art specialist baselines on both tasks.


### JointDiff: Bridging Continuous and Discrete in Multi-Agent Trajectory Generation
**Authors**: Guillem Capellera, Luis Ferraz, Antonio Rubio, Alexandre Alahi, Antonio Agudo

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22522v1](http://arxiv.org/pdf/2509.22522v1)

**Abstract**: Generative models often treat continuous data and discrete events as separate
processes, creating a gap in modeling complex systems where they interact
synchronously. To bridge this gap, we introduce JointDiff, a novel diffusion
framework designed to unify these two processes by simultaneously generating
continuous spatio-temporal data and synchronous discrete events. We demonstrate
its efficacy in the sports domain by simultaneously modeling multi-agent
trajectories and key possession events. This joint modeling is validated with
non-controllable generation and two novel controllable generation scenarios:
weak-possessor-guidance, which offers flexible semantic control over game
dynamics through a simple list of intended ball possessors, and text-guidance,
which enables fine-grained, language-driven generation. To enable the
conditioning with these guidance signals, we introduce CrossGuid, an effective
conditioning operation for multi-agent domains. We also share a new unified
sports benchmark enhanced with textual descriptions for soccer and football
datasets. JointDiff achieves state-of-the-art performance, demonstrating that
joint modeling is crucial for building realistic and controllable generative
models for interactive systems.


### Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)
**Authors**: Nikita Kornilov, David Li, Tikhon Mavrin, Aleksei Leonov, Nikita Gushchin, Evgeny Burnaev, Iaroslav Koshelev, Alexander Korotin

**Published Date**: 2025-09-26

**Updated Date**: 2025-09-26

**PDF Url**: [2509.22459v1](http://arxiv.org/pdf/2509.22459v1)

**Abstract**: While achieving exceptional generative quality, modern diffusion, flow, and
other matching models suffer from slow inference, as they require many steps of
iterative generation. Recent distillation methods address this by training
efficient one-step generators under the guidance of a pre-trained teacher
model. However, these methods are often constrained to only one specific
framework, e.g., only to diffusion or only to flow models. Furthermore, these
methods are naturally data-free, and to benefit from the usage of real data, it
is required to use an additional complex adversarial training with an extra
discriminator model. In this paper, we present RealUID, a universal
distillation framework for all matching models that seamlessly incorporates
real data into the distillation procedure without GANs. Our RealUID approach
offers a simple theoretical foundation that covers previous distillation
methods for Flow Matching and Diffusion models, and is also extended to their
modifications, such as Bridge Matching and Stochastic Interpolants.


## Quantitative Finance
### QuantMind: A Context-Engineering Based Knowledge Framework for Quantitative Finance
**Authors**: Haoxue Wang, Keli Wen, Yuante Li, Qiancheng Qu, Xiangxu Mu, Xinjie Shen, Jiaqi Gao, Chenyang Chang, Chuhan Xie, San Yu Cheung, Zhuoyuan Hu, Xinyu Wang, Sirui Bi, Bi'an Du

**Published Date**: 2025-09-25

**Updated Date**: 2025-09-25

**PDF Url**: [2509.21507v1](http://arxiv.org/pdf/2509.21507v1)

**Abstract**: Quantitative research increasingly relies on unstructured financial content
such as filings, earnings calls, and research notes, yet existing LLM and RAG
pipelines struggle with point-in-time correctness, evidence attribution, and
integration into research workflows. To tackle this, We present QuantMind, an
intelligent knowledge extraction and retrieval framework tailored to
quantitative finance. QuantMind adopts a two-stage architecture: (i) a
knowledge extraction stage that transforms heterogeneous documents into
structured knowledge through multi-modal parsing of text, tables, and formulas,
adaptive summarization for scalability, and domain-specific tagging for
fine-grained indexing; and (ii) an intelligent retrieval stage that integrates
semantic search with flexible strategies, multi-hop reasoning across sources,
and knowledge-aware generation for auditable outputs. A controlled user study
demonstrates that QuantMind improves both factual accuracy and user experience
compared to unaided reading and generic AI assistance, underscoring the value
of structured, domain-specific context engineering for finance.


