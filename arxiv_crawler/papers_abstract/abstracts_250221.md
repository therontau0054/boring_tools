# Abstracts of Papers

## Physics
### A simple gravitational self-decoherence model
**Authors**: Gabriel H. S. Aguiar, George E. A. Matsas

**Published Date**: 2024-09-21

**Updated Date**: 2025-02-20

**PDF Url**: [2409.14155v3](http://arxiv.org/pdf/2409.14155v3)

**Abstract**: One of the most significant debates of our time is whether our macroscopic
world (i) naturally emerges from quantum mechanics or (ii) requires new
physics. We argue for the latter and propose a simple gravitational
self-decoherence mechanism. For this purpose, we postulate the existence of a
Heisenberg cut such that particles with masses $m$ much smaller and larger than
a critical mass $M_{\rm C}$ (of the order of the Planck mass $M_{\rm P}$) would
be necessarily treated according to quantum and classical rules, respectively.
Our effective model is designed to capture the new physics that free quantum
particles would experience as their masses approach $M_{\rm C}$. The purity
loss for free quantum particles is evaluated and shown to be highly inefficient
for quantum particles with $m \ll M_{\rm C}$ but very effective for those with
$m \sim M_{\rm C}$. The physical picture behind it is that coherence would
(easily) leak from heavy enough particles to (non-observable) spacetime quantum
degrees of freedom. Finally, we contextualize our proposal with
state-of-the-art experiments and show how it can be tested in a future
Stern-Gerlach-like experiment.


### Adaptive Syndrome Extraction
**Authors**: Noah Berthusen, Shi Jie Samuel Tan, Eric Huang, Daniel Gottesman

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14835v1](http://arxiv.org/pdf/2502.14835v1)

**Abstract**: Device error rates on current quantum computers have improved enough to where
demonstrations of error correction below break-even are now possible. Still,
the circuits required for quantum error correction introduce significant
overhead and sometimes inject more errors than they correct. In this work, we
introduce adaptive syndrome extraction as a scheme to improve code performance
and reduce the quantum error correction cycle time by measuring only the
stabilizer generators that are likely to provide useful syndrome information.
We provide a concrete example of the scheme through the [[4,2,2]] code
concatenated with a hypergraph product code and a syndrome extraction cycle
that uses quantum error detection to modify the syndrome extraction circuits in
real time. Compared to non-concatenated codes and non-adaptive syndrome
extraction, we find that the adaptive scheme achieves over an order of
magnitude lower logical error rates while requiring fewer CNOT gates and
physical qubits. Furthermore, we show how to achieve fault-tolerant universal
logical computation with [[4,2,2]]-concatenated hypergraph product codes.


### A data-driven approach for modeling large-amplitude flow-induced oscillations of elastically mounted pitching wings
**Authors**: Yuanhang Zhu, Kenneth Breuer

**Published Date**: 2023-12-13

**Updated Date**: 2025-02-20

**PDF Url**: [2312.08561v2](http://arxiv.org/pdf/2312.08561v2)

**Abstract**: We propose and validate a data-driven approach for modeling large-amplitude
flow-induced oscillations of elastically mounted pitching wings. We first train
a neural networks regression model for the nonlinear aerodynamic moment using
data obtained from experimental measurements during prescribed pitching
oscillations and at fixed angles of attack. We then embed this model into an
ordinary differential equation solver to solve the governing equation of the
passive aeroelastic system with desired structural parameters. The system
dynamics predicted by the proposed data-driven approach are characterized and
compared with those obtained from physical experiments. The predicted and
experimental pitching amplitude, frequency and aerodynamic moment responses are
found to be in excellent agreement. Both the inertia-dominated mode and the
hydrodynamic-dominated mode are successfully predicted. The transient growth
and saturation of the pitching oscillation amplitude and the aerodynamic moment
are also faithfully captured by the proposed approach. Additional test cases
demonstrate the broad applicability and good scalability potential of this
approach.


### Micro Blossom: Accelerated Minimum-Weight Perfect Matching Decoding for Quantum Error Correction
**Authors**: Yue Wu, Namitha Liyanage, Lin Zhong

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14787v1](http://arxiv.org/pdf/2502.14787v1)

**Abstract**: Minimum-Weight Perfect Matching (MWPM) decoding is important to quantum error
correction decoding because of its accuracy. However, many believe that it is
difficult, if possible at all, to achieve the microsecond latency requirement
posed by superconducting qubits. This work presents the first publicly known
MWPM decoder, called Micro Blossom, that achieves sub-microsecond decoding
latency. Micro Blossom employs a heterogeneous architecture that carefully
partitions a state-of-the-art MWPM decoder between software and a programmable
accelerator with parallel processing units, one of each vertex/edge of the
decoding graph. On a surface code with code distance $d$ and a circuit-level
noise model with physical error rate $p$, Micro Blossom's accelerator employs
$O(d^3)$ parallel processing units to reduce the worst-case latency from
$O(d^{12})$ to $O(d^9)$ and reduce the average latency from $O(p d^3+1)$ to
$O(p^2 d^2+1)$ when $p \ll 1$.
  We report a prototype implementation of Micro Blossom using FPGA. Measured at
$d=13$ and $p=0.1\%$, the prototype achieves an average decoding latency of
$0.8 \mu s$ at a moderate clock frequency of $62 MHz$. Micro Blossom is the
first publicly known hardware-accelerated exact MWPM decoder, and the decoding
latency of $0.8 \mu s$ is 8 times shorter than the best latency of MWPM decoder
implementations reported in the literature.


### Multivariate Bicycle Codes
**Authors**: Lukas Voss, Sim Jian Xian, Tobias Haug, Kishor Bharti

**Published Date**: 2024-06-27

**Updated Date**: 2025-02-20

**PDF Url**: [2406.19151v4](http://arxiv.org/pdf/2406.19151v4)

**Abstract**: Quantum error correction suppresses noise in quantum systems to allow for
high-precision computations. In this work, we introduce Multivariate Bicycle
(MB) Quantum Low-Density Parity-Check (QLDPC) codes, via an extension of the
framework developed by Bravyi et al. [Nature, 627, 778-782 (2024)] and
particularly focus on Trivariate Bicycle (TB) codes. Unlike the weight-6 codes
proposed in their study, we offer concrete examples of weight-5 TB-QLDPC codes
which promise to be more amenable to near-term experimental setups. We show
that TB-QLDPC codes up to weight-6 have a bi-planar structure and often posses
a two-dimensional toric layout. Under circuit level noise, we find
substantially better encoding rates than comparable surface codes while
offering similar error suppression capabilities. For example, we can encode $4$
logical qubits with distance $5$ into $60$ physical qubits using weight-5 check
measurements of circuit depth 7, while a surface code with these parameters
requires $200$ physical qubits. The high encoding rate and compact layout make
our codes highly suitable candidates for near-term hardware implementations,
paving the way for a realizable quantum error correction protocol.


### Fast Bayesian Inference for Neutrino Non-Standard Interactions at Dark Matter Direct Detection Experiments
**Authors**: Dorian W. P. Amaral, Shixiao Liang, Juehang Qin, Christopher Tunnell

**Published Date**: 2024-05-23

**Updated Date**: 2025-02-20

**PDF Url**: [2405.14932v2](http://arxiv.org/pdf/2405.14932v2)

**Abstract**: Multi-dimensional parameter spaces are commonly encountered in physics
theories that go beyond the Standard Model. However, they often possess
complicated posterior geometries that are expensive to traverse using
techniques traditional to astroparticle physics. Several recent innovations,
which are only beginning to make their way into this field, have made
navigating such complex posteriors possible. These include GPU acceleration,
automatic differentiation, and neural-network-guided reparameterization. We
apply these advancements to dark matter direct detection experiments in the
context of non-standard neutrino interactions and benchmark their performances
against traditional nested sampling techniques when conducting Bayesian
inference. Compared to nested sampling alone, we find that these techniques
increase performance for both nested sampling and Hamiltonian Monte Carlo,
accelerating inference by factors of $\sim 100$ and $\sim 60$, respectively. As
nested sampling also evaluates the Bayesian evidence, these advancements can be
exploited to improve model comparison performance while retaining compatibility
with existing implementations that are widely used in the natural sciences.
Using these techniques, we perform the first scan in the neutrino non-standard
interactions parameter space for direct detection experiments whereby all
parameters are allowed to vary simultaneously. We expect that these
advancements are broadly applicable to other areas of astroparticle physics
featuring multi-dimensional parameter spaces.


### Distributed network of smartphone sensors: a new tool for scientific field measurements
**Authors**: J. Zhang, N. Mokus, J. Casoli, A. Eddi, S. Perrard

**Published Date**: 2025-01-08

**Updated Date**: 2025-02-20

**PDF Url**: [2501.04886v2](http://arxiv.org/pdf/2501.04886v2)

**Abstract**: Smartphones are widespread objects that have been used as physics sensors for
the general public thanks to their availability, high connectivity and built-in
sensors. Here, we present the use of a fleet of smartphones to create a
distributed network of time-synchronized sensors. We first evaluate the sensors
quality in the laboratory and then describe the network configuration that
allows the remote control of an entire fleet. Finally, we present two test
cases that use the smartphone fleet for physical field measurements. By this
study, we show that this approach paves the way for large-scale field
scientific studies.


### Revisiting the displacement current: Two key examples showing when and why it can be neglected
**Authors**: Alvaro Suarez Arturo C. Marti, Martín Monteiro

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14737v1](http://arxiv.org/pdf/2502.14737v1)

**Abstract**: This work examines the often-overlooked role of the displacement current in
systems beyond capacitors, particularly in coaxial cables and resistors with
alternating currents. While its influence is negligible at low frequencies
compared to conduction currents, displacement current becomes crucial at higher
frequencies for precise field calculations. Introductory physics textbooks
commonly restrict the concept to capacitor charging, potentially leading to
misconceptions about its broader applications and the interdependence of
Maxwell's equations in dynamic scenarios. By analyzing two specific cases, we
clarify when displacement current can be disregarded, when simplified laws like
Biot-Savart are valid, and where coupled electromagnetic equations are
essential. This approach highlights the boundaries of common models and
promotes a deeper understanding of dynamic field interactions.


### Assessing Students' Understanding of Uncertainty in Undergraduate Physics Laboratory Courses at a Major Canadian University: Longitudinal Results and Misconceptions
**Authors**: Matheus A. S. Pessôa, Rebecca Brosseau, Benjamin J. Dringoli, Armin Yazdani, Jack Sankey, Thomas Brunner, April Colosimo, Janette Barrington, Kenneth Ragan, Marcy Slapcoff

**Published Date**: 2024-12-19

**Updated Date**: 2025-02-20

**PDF Url**: [2412.15382v2](http://arxiv.org/pdf/2412.15382v2)

**Abstract**: Over the last five years, McGill University's Office of Science Education
(OSE) has partnered with faculty members from the Department of Physics to form
an education working group with the aim of charting the progression of
students' conceptual understanding of uncertainties across their undergraduate
degree. The research conducted by this group seeks to provide further insight
into both the experimental skill set that students gain through undergraduate
laboratory courses and how the department could address noticeable gaps in
student understanding. In this paper, we evaluate the conceptual understanding
of uncertainty using the Concise Data Processing Assessment (CDPA) instrument.
First, we characterize the physics laboratory curriculum at McGill University
by evaluating the evolution of CDPA scores across consecutive laboratory
courses, and further propose the utilization of this tool for identifying gaps
in student understanding. Following the analysis of student responses (N=2023),
we specifically investigate data collected in second-year courses to better
diagnose what student errors can tell us about common misconceptions in
experimental physics. This more in-depth research focuses on data collected
from students at the beginning and the end of their first full year of
experimental laboratory courses, consisting of two consecutive laboratory
courses that build on each other. By the end of the second course, students
have engaged with all the material covered in the CDPA test. Interestingly,
there have been no changes in CDPA total scores throughout the COVID-19
pandemic. We notice a marked upward shift in student understanding; however,
the results indicate that a significant portion of students continue to
struggle with uncertainties, basic data analysis, and curve fitting.


### An Insight into Parameter Identifiability Issues in the Carreau-Yasuda Model: a Novel Rheological Formulation for Shear-thinning non-Newtonian Inelastic Fluids
**Authors**: Gianluca Santesarti, Michele Marino, Francesco Viola, Roberto Verzicco, Giuseppe Vairo

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14728v1](http://arxiv.org/pdf/2502.14728v1)

**Abstract**: The Carreau-Yasuda rheological model is widely employed in both research and
industrial applications to describe the shear-thinning behaviour of
non-Newtonian inelastic fluids. However, its calibration against experimental
data is often affected by intrinsic identifiability issues, which can lead to
misleading physical interpretations of model parameters and unreliable flow
predictions. In this paper, starting from the analysis of the identifiability
challenges associated with the Carreau-Yasuda model, a novel rheological
formulation for shear-thinning non-Newtonian inelastic fluids is proposed.
Analytical results and exemplary numerical case studies demonstrate that the
proposed formulation is based on physically meaningful model parameters, whose
identifiability is not compromised by the key limitations of the Carreau-Yasuda
model. Moreover, the new approach allows for effective parameter estimation
through a straightforward direct identification strategy, eliminating the need
for inverse calibration procedures based on optimization techniques.


## Diffusion
### Dynamic Concepts Personalization from Single Videos
**Authors**: Rameen Abdal, Or Patashnik, Ivan Skorokhodov, Willi Menapace, Aliaksandr Siarohin, Sergey Tulyakov, Daniel Cohen-Or, Kfir Aberman

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14844v1](http://arxiv.org/pdf/2502.14844v1)

**Abstract**: Personalizing generative text-to-image models has seen remarkable progress,
but extending this personalization to text-to-video models presents unique
challenges. Unlike static concepts, personalizing text-to-video models has the
potential to capture dynamic concepts, i.e., entities defined not only by their
appearance but also by their motion. In this paper, we introduce
Set-and-Sequence, a novel framework for personalizing Diffusion Transformers
(DiTs)-based generative video models with dynamic concepts. Our approach
imposes a spatio-temporal weight space within an architecture that does not
explicitly separate spatial and temporal features. This is achieved in two key
stages. First, we fine-tune Low-Rank Adaptation (LoRA) layers using an
unordered set of frames from the video to learn an identity LoRA basis that
represents the appearance, free from temporal interference. In the second
stage, with the identity LoRAs frozen, we augment their coefficients with
Motion Residuals and fine-tune them on the full video sequence, capturing
motion dynamics. Our Set-and-Sequence framework results in a spatio-temporal
weight space that effectively embeds dynamic concepts into the video model's
output domain, enabling unprecedented editability and compositionality while
setting a new benchmark for personalizing dynamic concepts.


### Improving the Diffusability of Autoencoders
**Authors**: Ivan Skorokhodov, Sharath Girish, Benran Hu, Willi Menapace, Yanyu Li, Rameen Abdal, Sergey Tulyakov, Aliaksandr Siarohin

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14831v1](http://arxiv.org/pdf/2502.14831v1)

**Abstract**: Latent diffusion models have emerged as the leading approach for generating
high-quality images and videos, utilizing compressed latent representations to
reduce the computational burden of the diffusion process. While recent
advancements have primarily focused on scaling diffusion backbones and
improving autoencoder reconstruction quality, the interaction between these
components has received comparatively less attention. In this work, we perform
a spectral analysis of modern autoencoders and identify inordinate
high-frequency components in their latent spaces, which are especially
pronounced in the autoencoders with a large bottleneck channel size. We
hypothesize that this high-frequency component interferes with the
coarse-to-fine nature of the diffusion synthesis process and hinders the
generation quality. To mitigate the issue, we propose scale equivariance: a
simple regularization strategy that aligns latent and RGB spaces across
frequencies by enforcing scale equivariance in the decoder. It requires minimal
code changes and only up to 20K autoencoder fine-tuning steps, yet
significantly improves generation quality, reducing FID by 19% for image
generation on ImageNet-1K 256x256 and FVD by at least 44% for video generation
on Kinetics-700 17x256x256.


### A Survey on Text-Driven 360-Degree Panorama Generation
**Authors**: Hai Wang, Xiaoyu Xiang, Weihao Xia, Jing-Hao Xue

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14799v1](http://arxiv.org/pdf/2502.14799v1)

**Abstract**: The advent of text-driven 360-degree panorama generation, enabling the
synthesis of 360-degree panoramic images directly from textual descriptions,
marks a transformative advancement in immersive visual content creation. This
innovation significantly simplifies the traditionally complex process of
producing such content. Recent progress in text-to-image diffusion models has
accelerated the rapid development in this emerging field. This survey presents
a comprehensive review of text-driven 360-degree panorama generation, offering
an in-depth analysis of state-of-the-art algorithms and their expanding
applications in 360-degree 3D scene generation. Furthermore, we critically
examine current limitations and propose promising directions for future
research. A curated project page with relevant resources and research papers is
available at https://littlewhitesea.github.io/Text-Driven-Pano-Gen/.


### Making Universal Policies Universal
**Authors**: Niklas Höpner, David Kuric, Herke van Hoof

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14777v1](http://arxiv.org/pdf/2502.14777v1)

**Abstract**: The development of a generalist agent capable of solving a wide range of
sequential decision-making tasks remains a significant challenge. We address
this problem in a cross-agent setup where agents share the same observation
space but differ in their action spaces. Our approach builds on the universal
policy framework, which decouples policy learning into two stages: a
diffusion-based planner that generates observation sequences and an inverse
dynamics model that assigns actions to these plans. We propose a method for
training the planner on a joint dataset composed of trajectories from all
agents. This method offers the benefit of positive transfer by pooling data
from different agents, while the primary challenge lies in adapting shared
plans to each agent's unique constraints. We evaluate our approach on the
BabyAI environment, covering tasks of varying complexity, and demonstrate
positive transfer across agents. Additionally, we examine the planner's
generalisation ability to unseen agents and compare our method to traditional
imitation learning approaches. By training on a pooled dataset from multiple
agents, our universal policy achieves an improvement of up to $42.20\%$ in task
completion accuracy compared to a policy trained on a dataset from a single
agent.


### ReQFlow: Rectified Quaternion Flow for Efficient and High-Quality Protein Backbone Generation
**Authors**: Angxiao Yue, Zichong Wang, Hongteng Xu

**Published Date**: 2025-02-20

**Updated Date**: 2025-02-20

**PDF Url**: [2502.14637v1](http://arxiv.org/pdf/2502.14637v1)

**Abstract**: Protein backbone generation plays a central role in de novo protein design
and is significant for many biological and medical applications. Although
diffusion and flow-based generative models provide potential solutions to this
challenging task, they often generate proteins with undesired designability and
suffer computational inefficiency. In this study, we propose a novel rectified
quaternion flow (ReQFlow) matching method for fast and high-quality protein
backbone generation. In particular, our method generates a local translation
and a 3D rotation from random noise for each residue in a protein chain, which
represents each 3D rotation as a unit quaternion and constructs its flow by
spherical linear interpolation (SLERP) in an exponential format. We train the
model by quaternion flow (QFlow) matching with guaranteed numerical stability
and rectify the QFlow model to accelerate its inference and improve the
designability of generated protein backbones, leading to the proposed ReQFlow
model. Experiments show that ReQFlow achieves state-of-the-art performance in
protein backbone generation while requiring much fewer sampling steps and
significantly less inference time (e.g., being 37x faster than RFDiffusion and
62x faster than Genie2 when generating a backbone of length 300), demonstrating
its effectiveness and efficiency. The code is available at
https://github.com/AngxiaoYue/ReQFlow.


