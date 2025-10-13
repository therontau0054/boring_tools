# Abstracts of Papers

## Physics
### Simplified Quantum Weight Reduction with Optimal Bounds
**Authors**: Min-Hsiu Hsieh, Xingjian Li, Ting-Chun Lin

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09601v1](http://arxiv.org/pdf/2510.09601v1)

**Abstract**: Quantum weight reduction is the task of transforming a quantum code with
large check weight into one with small check weight. Low-weight codes are
essential for implementing quantum error correction on physical hardware, since
high-weight measurements cannot be executed reliably. Weight reduction also
serves as a critical theoretical tool, which may be relevant to the quantum PCP
conjecture.
  We introduce a new procedure for quantum weight reduction that combines
geometric insights with coning techniques, which simplifies Hastings' previous
approach while achieving better parameters. Given an arbitrary $[[n,k,d]]$
quantum code with weight $w$, our method produces a code with parameters $[[O(n
w^2 \log w), k, \Omega(d w)]]$ with check weight $5$ and qubit weight $6$.
  When applied to random dense CSS codes, our procedure yields explicit quantum
codes that surpass the square-root distance barrier, achieving parameters $[[n,
\tilde O(n^{1/3}), \tilde \Omega(n^{2/3})]]$. Furthermore, these codes admit a
three-dimensional embedding that saturates the Bravyi-Poulin-Terhal (BPT)
bound.
  As a further application, our weight reduction technique improves
fault-tolerant logical operator measurements by reducing the number of ancilla
qubits.


### Optimal Binning for Small-Angle Neutron Scattering Data Using the Freedman-Diaconis Rule
**Authors**: Jessie E. An, Chi-Huan Tung, Changwoo Do, Wei-Ren Chen

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09581v1](http://arxiv.org/pdf/2510.09581v1)

**Abstract**: Small-Angle Neutron Scattering (SANS) data analysis often relies on
fixed-width binning schemes that overlook variations in signal strength and
structural complexity. We introduce a statistically grounded approach based on
the Freedman-Diaconis (FD) rule, which minimizes the mean integrated squared
error between the histogram estimate and the true intensity distribution. By
deriving the competing scaling relations for counting noise ($\propto h^{-1}$)
and binning distortion ($\propto h^{2}$), we establish an optimal bin width
that balances statistical precision and structural resolution. Application to
synthetic data from the Debye scattering function of a Gaussian polymer chain
demonstrates that the FD criterion quantitatively determines the most efficient
binning, faithfully reproducing the curvature of $I(Q)$ while minimizing random
error. The optimal width follows the expected scaling $h_{\mathrm{opt}} \propto
N_{\mathrm{total}}^{-1/3}$, delineating the transition between noise- and
resolution-limited regimes. This framework provides a unified, physics-informed
basis for adaptive, statistically efficient binning in neutron scattering
experiments.


### Differential Analysis of Pseudo Haptic Feedback: Novel Comparative Study of Visual and Auditory Cue Integration for Psychophysical Evaluation
**Authors**: Nishant Gautam, Somya Sharma, Peter Corcoran, Kaspar Althoefer

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09570v1](http://arxiv.org/pdf/2510.09570v1)

**Abstract**: Pseudo-haptics exploit carefully crafted visual or auditory cues to trick the
brain into "feeling" forces that are never physically applied, offering a
low-cost alternative to traditional haptic hardware. Here, we present a
comparative psychophysical study that quantifies how visual and auditory
stimuli combine to evoke pseudo-haptic pressure sensations on a commodity
tablet. Using a Unity-based Rollball game, participants (n = 4) guided a
virtual ball across three textured terrains while their finger forces were
captured in real time with a Robotous RFT40 force-torque sensor. Each terrain
was paired with a distinct rolling-sound profile spanning 440 Hz - 4.7 kHz, 440
Hz - 13.1 kHz, or 440 Hz - 8.9 kHz; crevice collisions triggered additional
"knocking" bursts to heighten realism. Average tactile forces increased
systematically with cue intensity: 0.40 N, 0.79 N and 0.88 N for visual-only
trials and 0.41 N, 0.81 N and 0.90 N for audio-only trials on Terrains 1-3,
respectively. Higher audio frequencies and denser visual textures both elicited
stronger muscle activation, and their combination further reduced the force
needed to perceive surface changes, confirming multisensory integration. These
results demonstrate that consumer-grade isometric devices can reliably induce
and measure graded pseudo-haptic feedback without specialized actuators,
opening a path toward affordable rehabilitation tools, training simulators and
assistive interfaces.


### Unveiling dynamical quantum error correcting codes via non-invertible symmetries
**Authors**: Rajath Radhakrishnan, Adar Sharon, Nathanan Tantivasadakarn

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09565v1](http://arxiv.org/pdf/2510.09565v1)

**Abstract**: Dynamical stabilizer codes (DSCs) have recently emerged as a powerful
generalization of static stabilizer codes for quantum error correction,
replacing a fixed stabilizer group with a sequence of non-commuting
measurements. This dynamical structure unlocks new possibilities for fault
tolerance but also introduces new challenges, as errors must now be tracked
across both space and time. In this work, we provide a physical and topological
understanding of DSCs by establishing a correspondence between qudit Pauli
measurements and non-invertible symmetries in 4+1-dimensional 2-form gauge
theories. Sequences of measurements in a DSC are mapped to a fusion of the
operators implementing these non-invertible symmetries. We show that the error
detectors of a DSC correspond to endable surface operators in the gauge theory,
whose endpoints define line operators, and that detectable errors are precisely
those surface operators that braid non-trivially with these lines. Finally, we
demonstrate how this framework naturally recovers the spacetime stabilizer code
associated with a DSC.


### Robo-Instruct: Simulator-Augmented Instruction Alignment For Finetuning Code LLMs
**Authors**: Zichao Hu, Junyi Jessy Li, Arjun Guha, Joydeep Biswas

**Published Date**: 2024-05-30

**Updated Date**: 2025-10-10

**PDF Url**: [2405.20179v5](http://arxiv.org/pdf/2405.20179v5)

**Abstract**: Code LLMs have shown promising results with converting tasks in natural
language to programs that can be executed by service robots. We are interested
in finetuning small, specialized LLMs for this purpose, but collecting datasets
of task-program pairs specific to each robot is time-consuming and expensive.
While approaches such as SELF-INSTRUCT and EVOL-INSTRUCT are capable of
generating novel tasks given a few examples, they are unable to provide the
corresponding programs that correctly abide by physical-world and
robot-constraints using the provided programming interface. Using a simulator
is a natural potential solution to checking for such constraints, but building
simulation environments that can handle arbitrary tasks and their necessary
objects and locations, is challenging. To address these challenges, we
introduce ROBO-INSTRUCT, which synthesizes task-specific simulation
environments on the fly during program execution, by opportunistically
inferring entity properties and enforcing corresponding constraints based on
how the entities are used in the task program. Additionally, ROBO-INSTRUCT
integrates an LLM-aided post-processing procedure to refine instructions for
better alignment with robot programs. We demonstrate the effectiveness of
ROBO-INSTRUCT across multiple LLMs, showing that our fine-tuned models
outperform all baseline methods and even match or surpass the performance of
several larger and proprietary models.


### Generalized Modulated Symmetries in $\mathbb{Z}_2$ Topological Ordered Phases
**Authors**: Gustavo M. Yoshitome, Heitor Casasola, Rodrigo Corso, Pedro R. S. Gomes

**Published Date**: 2025-06-12

**Updated Date**: 2025-10-10

**PDF Url**: [2506.10819v2](http://arxiv.org/pdf/2506.10819v2)

**Abstract**: We study $\mathbb{Z}_2$ topological ordered phases in 2+1 dimensions
characterized by generalized modulated symmetries. Such phases have explicit
realizations in terms of fixed-point Hamiltonians involving commuting
projectors with support $h=3,5,7,\ldots$ in the horizontal direction, which
dictates the modulation of the generalized symmetries. These symmetries are
sensitive to the lattice sizes. For certain sizes, they are spontaneously
broken and the ground state is degenerated, while for the remaining ones, the
symmetries are explicitly broken and the ground state is unique. The ground
state dependence on the lattice sizes is a manifestation of the
ultraviolet/infrared (UV/IR) mixing. The structure of the modulated symmetries
implies that the anyons can move only in rigid steps of size $h$, leading to
the notion of position-dependent anyons. The phases exhibit rich boundary
physics with a variety of gapped phases, including trivial, partial and total
symmetry-breaking, and SPT phases. Effective field theory descriptions are
discussed, making transparent the relation between the generalized modulated
symmetries and the restrictions on anyon mobility, incorporating the boundary
physics in a natural way, and showing how the short-distance details can be
incorporated into the continuum by means of twisted boundary conditions.


### A relationship between nonunitary mixed parity superconductivity and magnetism with spin-orbit coupling
**Authors**: Takehito Yokoyama

**Published Date**: 2025-05-15

**Updated Date**: 2025-10-10

**PDF Url**: [2505.10336v2](http://arxiv.org/pdf/2505.10336v2)

**Abstract**: We show that Hamiltonian for nonunitary mixed parity superconductivity can be
recast into that for magnetism with spin-orbit coupling by the Schrieffer-Wolff
transformation, indicating that nonunitary mixed parity superconductivity and
magnetism with spin-orbit coupling can share the same physics. As
demonstrations, we discuss the Dzyaloshinskii-Moriya type interactions,
magnetoelectric effect, supercurrent-induced spin current, and altermagnetism
in nonunitary mixed parity superconductors. All these effects originate purely
from superconductivity, without any magnetism and spin-orbit coupling.


### Lie symmetry analysis of the two-Higgs-doublet model field equations
**Authors**: M. Aa. Solberg

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09542v1](http://arxiv.org/pdf/2510.09542v1)

**Abstract**: We apply Lie symmetry analysis of partial differential equations (PDEs) to
the Euler-Lagrange equations of the two-Higgs-doublet model (2HDM), to
determine its scalar Lie point symmetries. A Lie point symmetry is a
structure-preserving transformation of the spacetime variables and the fields
of the model, which is also continuous and connected to the identity.
Symmetries of PDEs may in general be divided into strict variational
symmetries, divergence symmetries and non-variational symmetries, where the
first two are collectively referred to as variational symmetries. Variational
symmetries are usually preserved under quantization, and variational Lie
symmetries yield conservation laws. We demonstrate that there are no scalar Lie
point divergence symmetries or non-variational Lie point symmetries in the
2HDM, and re-derive its well-known strict variational Lie point symmetries,
thus confirming the consistency of our implementation of Lie's method.
Moreover, we prove three general results which may simplify Lie symmetry
calculations for a wide class of particle physics models. Lie symmetry analysis
of PDEs is a broadly applicable method for determining Lie symmetries. As
demonstrated here by example, it can be applied to models with many variables,
parameters and reparametrization freedom, while any missing discrete symmetries
may be identified through the automorphism groups of the resulting Lie symmetry
algebras.


### A Digital Twin for Diesel Engines: Operator-infused Physics-Informed Neural Networks with Transfer Learning for Engine Health Monitoring
**Authors**: Kamaljyoti Nath, Varun Kumar, Daniel J. Smith, George Em Karniadakis

**Published Date**: 2024-12-16

**Updated Date**: 2025-10-10

**PDF Url**: [2412.11967v2](http://arxiv.org/pdf/2412.11967v2)

**Abstract**: Improving diesel engine efficiency, reducing emissions, and enabling robust
health monitoring have been critical research topics in engine modelling. While
recent advancements in the use of neural networks for system monitoring have
shown promising results, such methods often focus on component-level analysis,
lack generalizability, and physical interpretability. In this study, we propose
a novel hybrid framework that combines physics-informed neural networks (PINNs)
with deep operator networks (DeepONet) to enable accurate and computationally
efficient parameter identification in mean-value diesel engine models. Our
method leverages physics-based system knowledge in combination with data-driven
training of neural networks to enhance model applicability. Incorporating
offline-trained DeepONets to predict actuator dynamics significantly lowers the
online computation cost when compared to the existing PINN framework. To
address the re-training burden typical of PINNs under varying input conditions,
we propose two transfer learning (TL) strategies: (i) a multi-stage TL scheme
offering better runtime efficiency than full online training of the PINN model
and (ii) a few-shot TL scheme that freezes a shared multi-head network body and
computes physics-based derivatives required for model training outside the
training loop. The second strategy offers a computationally inexpensive and
physics-based approach for predicting engine dynamics and parameter
identification, offering computational efficiency over the existing PINN
framework. Compared to existing health monitoring methods, our framework
combines the interpretability of physics-based models with the flexibility of
deep learning, offering substantial gains in generalization, accuracy, and
deployment efficiency for diesel engine diagnostics.


### Hartman effect, time-delays, and the non-spatial nature of quantum particles
**Authors**: Massimiliano Sassoli de Bianchi

**Published Date**: 2023-03-11

**Updated Date**: 2025-10-10

**PDF Url**: [2303.08031v3](http://arxiv.org/pdf/2303.08031v3)

**Abstract**: The phenomenon of quantum tunneling remains a fascinating and enigmatic one,
defying classical notions of particle behavior. This paper presents a novel
theoretical investigation of the tunneling phenomenon, from the viewpoint of
Hartman effect, showing that the classical concept of spatiality is transcended
during tunneling, since one cannot describe the process as a crossing of the
potential barrier. This means that quantum tunneling strongly indicates that
quantum non-locality should be understood as an aspect of quantum
non-spatiality. It is also emphasized that according to the Conceptuality
Interpretation of quantum mechanics, a non-spatial state should be understood
as an abstract state of a conceptual-like entity, which only when it reaches
its maximum degree of concreteness, during the wave-function collapse, can
enter the spatiotemporal layer of our physical reality.


## Diffusion
### On the Interpolation Effect of Score Smoothing in Diffusion Models
**Authors**: Zhengdao Chen

**Published Date**: 2025-02-26

**Updated Date**: 2025-10-10

**PDF Url**: [2502.19499v2](http://arxiv.org/pdf/2502.19499v2)

**Abstract**: Score-based diffusion models have achieved remarkable progress in various
domains with the ability to generate new data samples that do not exist in the
training set. In this work, we study the hypothesis that such creativity arises
from an interpolation effect caused by a smoothing of the empirical score
function. Focusing on settings where the training set lies uniformly in a
one-dimensional subspace, we show theoretically how regularized two-layer ReLU
neural networks tend to learn approximately a smoothed version of the empirical
score function, and further probe the interplay between score smoothing and the
denoising dynamics with analytical solutions and numerical experiments. In
particular, we demonstrate how a smoothed score function can lead to the
generation of samples that interpolate the training data along their subspace
while avoiding full memorization. Moreover, we present experimental evidence
that learning score functions with neural networks indeed induces a score
smoothing effect, including in simple nonlinear settings and without explicit
regularization.


### SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models
**Authors**: Chengyu Wang, Paria Rashidinejad, DiJia Su, Song Jiang, Sid Wang, Siyan Zhao, Cai Zhou, Shannon Zejiang Shen, Feiyu Chen, Tommi Jaakkola, Yuandong Tian, Bo Liu

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09541v1](http://arxiv.org/pdf/2510.09541v1)

**Abstract**: Diffusion large language models (dLLMs) are emerging as an efficient
alternative to autoregressive models due to their ability to decode multiple
tokens in parallel. However, aligning dLLMs with human preferences or
task-specific rewards via reinforcement learning (RL) is challenging because
their intractable log-likelihood precludes the direct application of standard
policy gradient methods. While prior work uses surrogates like the evidence
lower bound (ELBO), these one-sided approximations can introduce significant
policy gradient bias. To address this, we propose the Sandwiched Policy
Gradient (SPG) that leverages both an upper and a lower bound of the true
log-likelihood. Experiments show that SPG significantly outperforms baselines
based on ELBO or one-step estimation. Specifically, SPG improves the accuracy
over state-of-the-art RL methods for dLLMs by 3.6% in GSM8K, 2.6% in MATH500,
18.4% in Countdown and 27.0% in Sudoku.


### Conditional Flow Matching for Bayesian Posterior Inference
**Authors**: So Won Jeong, Percy S. Zhai, Veronika Ročová

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09534v1](http://arxiv.org/pdf/2510.09534v1)

**Abstract**: We propose a generative multivariate posterior sampler via flow matching. It
offers a simple training objective, and does not require access to likelihood
evaluation. The method learns a dynamic, block-triangular velocity field in the
joint space of data and parameters, which results in a deterministic transport
map from a source distribution to the desired posterior. The inverse map, named
vector rank, is accessible by reversibly integrating the velocity over time. It
is advantageous to leverage the dynamic design: proper constraints on the
velocity yield a monotone map, which leads to a conditional Brenier map,
enabling a fast and simultaneous generation of Bayesian credible sets whose
contours correspond to level sets of Monge-Kantorovich data depth. Our approach
is computationally lighter compared to GAN-based and diffusion-based
counterparts, and is capable of capturing complex posterior structures.
Finally, frequentist theoretical guarantee on the consistency of the recovered
posterior distribution, and of the corresponding Bayesian credible sets, is
provided.


### Editable Noise Map Inversion: Encoding Target-image into Noise For High-Fidelity Image Manipulation
**Authors**: Mingyu Kang, Yong Suk Choi

**Published Date**: 2025-09-30

**Updated Date**: 2025-10-10

**PDF Url**: [2509.25776v2](http://arxiv.org/pdf/2509.25776v2)

**Abstract**: Text-to-image diffusion models have achieved remarkable success in generating
high-quality and diverse images. Building on these advancements, diffusion
models have also demonstrated exceptional performance in text-guided image
editing. A key strategy for effective image editing involves inverting the
source image into editable noise maps associated with the target image.
However, previous inversion methods face challenges in adhering closely to the
target text prompt. The limitation arises because inverted noise maps, while
enabling faithful reconstruction of the source image, restrict the flexibility
needed for desired edits. To overcome this issue, we propose Editable Noise Map
Inversion (ENM Inversion), a novel inversion technique that searches for
optimal noise maps to ensure both content preservation and editability. We
analyze the properties of noise maps for enhanced editability. Based on this
analysis, our method introduces an editable noise refinement that aligns with
the desired edits by minimizing the difference between the reconstructed and
edited noise maps. Extensive experiments demonstrate that ENM Inversion
outperforms existing approaches across a wide range of image editing tasks in
both preservation and edit fidelity with target prompts. Our approach can also
be easily applied to video editing, enabling temporal consistency and content
manipulation across frames.


### CRPS-LAM: Regional ensemble weather forecasting from matching marginals
**Authors**: Erik Larsson, Joel Oskarsson, Tomas Landelius, Fredrik Lindsten

**Published Date**: 2025-10-10

**Updated Date**: 2025-10-10

**PDF Url**: [2510.09484v1](http://arxiv.org/pdf/2510.09484v1)

**Abstract**: Machine learning for weather prediction increasingly relies on ensemble
methods to provide probabilistic forecasts. Diffusion-based models have shown
strong performance in Limited-Area Modeling (LAM) but remain computationally
expensive at sampling time. Building on the success of global weather
forecasting models trained based on Continuous Ranked Probability Score (CRPS),
we introduce CRPS-LAM, a probabilistic LAM forecasting model trained with a
CRPS-based objective. By sampling and injecting a single latent noise vector
into the model, CRPS-LAM generates ensemble members in a single forward pass,
achieving sampling speeds up to 39 times faster than a diffusion-based model.
We evaluate the model on the MEPS regional dataset, where CRPS-LAM matches the
low errors of diffusion models. By retaining also fine-scale forecast details,
the method stands out as an effective approach for probabilistic regional
weather forecasting


