# Abstracts of Papers

## Physics
### Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization
**Authors**: Lujie Yang, H. J. Terry Suh, Tong Zhao, Bernhard Paus Graesdal, Tarik Kelestemur, Jiuguang Wang, Tao Pang, Russ Tedrake

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20382v1](http://arxiv.org/pdf/2502.20382v1)

**Abstract**: We present a low-cost data generation pipeline that integrates physics-based
simulation, human demonstrations, and model-based planning to efficiently
generate large-scale, high-quality datasets for contact-rich robotic
manipulation tasks. Starting with a small number of embodiment-flexible human
demonstrations collected in a virtual reality simulation environment, the
pipeline refines these demonstrations using optimization-based kinematic
retargeting and trajectory optimization to adapt them across various robot
embodiments and physical parameters. This process yields a diverse, physically
consistent dataset that enables cross-embodiment data transfer, and offers the
potential to reuse legacy datasets collected under different hardware
configurations or physical parameters. We validate the pipeline's effectiveness
by training diffusion policies from the generated datasets for challenging
contact-rich manipulation tasks across multiple robot embodiments, including a
floating Allegro hand and bimanual robot arms. The trained policies are
deployed zero-shot on hardware for bimanual iiwa arms, achieving high success
rates with minimal human input. Project website:
https://lujieyang.github.io/physicsgen/.


### Benchmarking Quantum Red TEA on CPUs, GPUs, and TPUs
**Authors**: Daniel Jaschke, Marco Ballarin, Nora Reinić, Luka Pavešić, Simone Montangero

**Published Date**: 2024-09-05

**Updated Date**: 2025-02-27

**PDF Url**: [2409.03818v2](http://arxiv.org/pdf/2409.03818v2)

**Abstract**: We benchmark simulations of many-body quantum systems on heterogeneous
hardware platforms using CPUs, GPUs, and TPUs. We compare different linear
algebra backends, e.g., NumPy versus the PyTorch, JAX, or TensorFlow libraries,
as well as a mixed-precision-inspired approach and optimizations for the target
hardware. Quantum Red TEA out of the Quantum TEA library specifically addresses
handling tensors with different libraries or hardware, where the tensors are
the building blocks of tensor network algorithms. The benchmark problem is a
variational search of a ground state in an interacting model. This is a
ubiquitous problem in quantum many-body physics, which we solve using tensor
network methods. This approximate state-of-the-art method compresses quantum
correlations which is key to overcoming the exponential growth of the Hilbert
space as a function of the number of particles. We present a way to obtain
speedups of a factor of 34 when tuning parameters on the CPU, and an additional
factor of 2.76 on top of the best CPU setup when migrating to GPUs.


### T1-PILOT: Optimized Trajectories for T1 Mapping Acceleration
**Authors**: Tamir Shor, Moti Freiman, Chaim Baskin, Alex Bronstein

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20333v1](http://arxiv.org/pdf/2502.20333v1)

**Abstract**: Cardiac T1 mapping provides critical quantitative insights into myocardial
tissue composition, enabling the assessment of pathologies such as fibrosis,
inflammation, and edema. However, the inherently dynamic nature of the heart
imposes strict limits on acquisition times, making high-resolution T1 mapping a
persistent challenge. Compressed sensing (CS) approaches have reduced scan
durations by undersampling k-space and reconstructing images from partial data,
and recent studies show that jointly optimizing the undersampling patterns with
the reconstruction network can substantially improve performance. Still, most
current T1 mapping pipelines rely on static, hand-crafted masks that do not
exploit the full acceleration and accuracy potential. In this work, we
introduce T1-PILOT: an end-to-end method that explicitly incorporates the T1
signal relaxation model into the sampling-reconstruction framework to guide the
learning of non-Cartesian trajectories, crossframe alignment, and T1 decay
estimation. Through extensive experiments on the CMRxRecon dataset, T1-PILOT
significantly outperforms several baseline strategies (including learned
single-mask and fixed radial or golden-angle sampling schemes), achieving
higher T1 map fidelity at greater acceleration factors. In particular, we
observe consistent gains in PSNR and VIF relative to existing methods, along
with marked improvements in delineating finer myocardial structures. Our
results highlight that optimizing sampling trajectories in tandem with the
physical relaxation model leads to both enhanced quantitative accuracy and
reduced acquisition times. Code for reproducing all results will be made
publicly available upon publication.


### Next to Soft Threshold Resummation for $VH$ Production
**Authors**: Arunima Bhattacharya, Chinmoy Dey, M. C. Kumar, Vaibhav Pandey

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20331v1](http://arxiv.org/pdf/2502.20331v1)

**Abstract**: We study the threshold effects for the associated production of a Higgs boson
with a massive vector boson $(V=Z,W)$ in the $q\bar{q} \rightarrow V^\star
\rightarrow VH$ process at the LHC. By leveraging the universality of threshold
logarithms and employing soft-virtual (SV) and next-to-soft virtual (NSV)
resummation techniques, we compute threshold corrections to
next-to-next-to-leading logarithmic accuracy. After matching the resummed
predictions to the Next-to-Next-to-Leading order (NNLO) fixed order results, we
present the invariant mass distribution to NNLO$+\overline{\text{NNLL}}$
accuracy in QCD for the current LHC energies and the total production cross
sections. The $VH$ production channel is crucial for studying the couplings of
the Higgs boson to the vector bosons $(W,Z)$ and understanding the mechanism of
electroweak symmetry breaking. Precision measurements of this process help test
the validity of the standard model (SM) and can reveal potential deviations
indicating new physics.


### Andreev non-Hermitian Hamiltonian for open Josephson junctions from Green's functions
**Authors**: Roberto Capecelatro, Marco Marciani, Gabriele Campagnano, Procolo Lucignano

**Published Date**: 2024-12-02

**Updated Date**: 2025-02-27

**PDF Url**: [2412.01702v2](http://arxiv.org/pdf/2412.01702v2)

**Abstract**: We investigate the transport properties of open Josephson junctions (JJs)
through a minimal effective non-Hermitian (NH) approach derived from the
equilibrium Green's function (GF) formalism. Specifically, we consider a JJ
with a quantum dot barrier coupled to a normal metal reservoir. The coupling
introduces an imaginary self-energy term in the JJ Hamiltonian which can be
naturally accounted for in the NH formalism. While most approaches to similar
problems work with the full junction Hamiltonian we propose a scheme for
deriving an effective NH Hamiltonian for the Andreev levels only, that we
compute from the singular part of the barrier GF. To establish the range of
applicability of this NH model we benchmark our results for both the dot
density of states and the supercurrent against exact GF predictions in
different transport regimes. We find that, as a rule of thumb, the Andreev NH
description is accurate when the spectral overlap between the Andreev bound
states (ABS) and the near-gap continuum states is negligible, i.e. when the ABS
energies lie sufficiently far from the superconducting gap relative to their
line-width. This method not only highlights the effective physics of the JJ but
also offers a scalable framework for studying large-size devices.


### The complete trans-series for conserved charges in integrable field theories
**Authors**: Zoltán Bajnok, János Balog, István Vona

**Published Date**: 2025-01-27

**Updated Date**: 2025-02-27

**PDF Url**: [2501.16435v2](http://arxiv.org/pdf/2501.16435v2)

**Abstract**: We analyze the vacuum expectation values of conserved charges in two
dimensional integrable theories. We study the situations when the ground-state
can be described by a single integral equation with a finite support: the
thermodynamic limit of the Bethe ansatz equation. We solve this integral
equation by expanding around the infinite support limit and write the
expectation values in terms of an explicitly calculable trans-series, which
includes both perturbative and all non-perturbative corrections. These
different types of corrections are interrelated via resurgence relations, which
we all reveal. We provide explicit formulas for a wide class of bosonic and
fermionic models including the $O(N)$ (super) symmetric nonlinear sigma and
Gross-Neveu, the $SU(N)$ invariant principal chiral and chiral Gross-Neveu
models along with the Lieb-Liniger and Gaudin-Yang models and the case of the
disk capacitor. With numerical analyses we demonstrate that the laterally Borel
resummed trans-series is convergent and reproduces the physical result.


### Long-range interactions in double heavy tetraquarks $\bar Q \bar Q qq$
**Authors**: Muhammad Naeem Anwar

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20329v1](http://arxiv.org/pdf/2502.20329v1)

**Abstract**: At the large distances compared to the chiral symmetry breaking scale, a
four-quark system $\bar Q \bar Q qq$ (with $Q$ as heavy and $q$ as light
quarks) can be treated as two asymptotic mesons interacting via strong residual
forces. The static heavy quark assumption enables using the Born-Oppenheimer
approximation, where one can compute the potential between two heavy antiquarks
in the presence of two light quarks of finite mass -- a prescription utilized
in several lattice QCD studies. To analyse the long-range strong force in a
$\bar Q \bar Q qq$ system, we study the interaction between two bottom mesons
in the heavy quark limit using chiral effective field theory and dispersion
theory with unphysical pion mass. We present methods to obtain
two-pion-exchange potential between two static heavy mesons at non-physical
pion mass and compare our preliminary results with the corresponding lattice
QCD potentials.


### 2064 global population crisis scenario predicted by the most general dynamic model
**Authors**: Alessio Zaccone, Kostya Trachenko

**Published Date**: 2025-02-26

**Updated Date**: 2025-02-27

**PDF Url**: [2502.19063v2](http://arxiv.org/pdf/2502.19063v2)

**Abstract**: There is currently no consensus on how the global population will evolve in
the next decades and in the next century. The reason for this uncertainty is
the absence of reliable population dynamic models. In this paper, we remedy to
this situation by reporting on a population dynamic model, a single nonlinear
differential equation adapted from the physics of disordered systems, which is
able to mathematically describe all the various regimes encountered in the
global population recorded as a function of time, over the past 12000 years
until now. Regimes of simple exponential growth (Malthus), logistic (Verhulst)
plateaus as well as stretched-exponential and compressed-exponential growth
regimes are all reliably described by this mathematical equation in its various
limits. Besides showing that this is, indeed, the most general population
dynamic model, we use it to explore its solutions projected into the future. In
particular, two different scenarios are predicted. In one of them, which
assumes that the future evolution would continue along a similar pattern as the
past decades (hence without any major global ecological crisis affecting the
resource exploitation), a von Foerster-type doomsday scenario with a sudden
rise of the global population to unsustainable levels could appear as early as
2078. In the opposite scenario, if a global ecological crisis were to set in
today, affecting the ability to exploit resources, given the current estimates
of the Earth's carrying capacity, the global population is forecasted to reduce
by half by 2064. Furthermore, the proposed dynamic model provides with a new
aggregated parameter (K, in the model) that can be monitored and controlled so
as to avoid the doomsday scenarios.


### Impilict Runge-Kutta based sparse identification of governing equations in biologically motivated systems
**Authors**: Mehrdad Anvari, Hamidreza Marasi, Hossein Kheiri

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20319v1](http://arxiv.org/pdf/2502.20319v1)

**Abstract**: Identifying governing equations in physical and biological systems from
datasets remains a long-standing challenge across various scientific
disciplines, providing mechanistic insights into complex system evolution.
Common methods like sparse identification of nonlinear dynamics (SINDy) often
rely on precise derivative estimations, making them vulnerable to data scarcity
and noise. This study presents a novel data-driven framework by integrating
high order implicit Runge-Kutta methods (IRKs) with the sparse identification,
termed IRK-SINDy. The framework exhibits remarkable robustness to data scarcity
and noise by leveraging the lower stepsize constraint of IRKs. Two methods for
incorporating IRKs into sparse regression are introduced: one employs iterative
schemes for numerically solving nonlinear algebraic system of equations, while
the other utilizes deep neural networks to predict stage values of IRKs. The
performance of IRK-SINDy is demonstrated through numerical experiments on
benchmark problems with varied dynamical behaviors, including linear and
nonlinear oscillators, the Lorenz system, and biologically relevant models like
predator-prey dynamics, logistic growth, and the FitzHugh-Nagumo model. Results
indicate that IRK-SINDy outperforms conventional SINDy and the RK4-SINDy
framework, particularly under conditions of extreme data scarcity and noise,
yielding interpretable and generalizable models.


### Non-relativistic limit of Dirac Hamiltonians with Aharonov-Bohm fields
**Authors**: Matteo Gallone, Alessandro Michelangeli, Diego Noja

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20318v1](http://arxiv.org/pdf/2502.20318v1)

**Abstract**: We characterise the families of self-adjoint Dirac and Schr\"{o}dinger
operators with Aharonov-Bohm magnetic field, and we exploit the
non-relativistic limit of infinite light speed to connect the former to the
latter. The limit consists of the customary removal of the rest energy and of a
suitable scaling, with the light speed, of the short-scale boundary condition
of self-adjointness. This ensures that the scattering length of the
Aharonov-Bohm interaction is preserved along the limit. Noteworthy is the fact
that the whole family of Dirac-AB operators is mapped, in the non-relativistic
limit, into the physically relevant sub-family of $s$-wave,
angular-momentum-commuting, Schr\"{o}\-dinger-AB Hamiltonians with relativistic
Dirac approximants.


## Diffusion
### Tight Inversion: Image-Conditioned Inversion for Real Image Editing
**Authors**: Edo Kadosh, Nir Goren, Or Patashnik, Daniel Garibi, Daniel Cohen-Or

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20376v1](http://arxiv.org/pdf/2502.20376v1)

**Abstract**: Text-to-image diffusion models offer powerful image editing capabilities. To
edit real images, many methods rely on the inversion of the image into Gaussian
noise. A common approach to invert an image is to gradually add noise to the
image, where the noise is determined by reversing the sampling equation. This
process has an inherent tradeoff between reconstruction and editability,
limiting the editing of challenging images such as highly-detailed ones.
Recognizing the reliance of text-to-image models inversion on a text condition,
this work explores the importance of the condition choice. We show that a
condition that precisely aligns with the input image significantly improves the
inversion quality. Based on our findings, we introduce Tight Inversion, an
inversion method that utilizes the most possible precise condition -- the input
image itself. This tight condition narrows the distribution of the model's
output and enhances both reconstruction and editability. We demonstrate the
effectiveness of our approach when combined with existing inversion methods
through extensive experiments, evaluating the reconstruction accuracy as well
as the integration with various editing methods.


### Constrained Generative Modeling with Manually Bridged Diffusion Models
**Authors**: Saeid Naderiparizi, Xiaoxuan Liang, Berend Zwartsenberg, Frank Wood

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20371v1](http://arxiv.org/pdf/2502.20371v1)

**Abstract**: In this paper we describe a novel framework for diffusion-based generative
modeling on constrained spaces. In particular, we introduce manual bridges, a
framework that expands the kinds of constraints that can be practically used to
form so-called diffusion bridges. We develop a mechanism for combining multiple
such constraints so that the resulting multiply-constrained model remains a
manual bridge that respects all constraints. We also develop a mechanism for
training a diffusion model that respects such multiple constraints while also
adapting it to match a data distribution. We develop and extend theory
demonstrating the mathematical validity of our mechanisms. Additionally, we
demonstrate our mechanism in constrained generative modeling tasks,
highlighting a particular high-value application in modeling trajectory
initializations for path planning and control in autonomous vehicles.


### Explainable, Multi-modal Wound Infection Classification from Images Augmented with Generated Captions
**Authors**: Palawat Busaranuvong, Emmanuel Agu, Reza Saadati Fard, Deepak Kumar, Shefalika Gautam, Bengisu Tulu, Diane Strong

**Published Date**: 2025-02-27

**Updated Date**: 2025-02-27

**PDF Url**: [2502.20277v1](http://arxiv.org/pdf/2502.20277v1)

**Abstract**: Infections in Diabetic Foot Ulcers (DFUs) can cause severe complications,
including tissue death and limb amputation, highlighting the need for accurate,
timely diagnosis. Previous machine learning methods have focused on identifying
infections by analyzing wound images alone, without utilizing additional
metadata such as medical notes. In this study, we aim to improve infection
detection by introducing Synthetic Caption Augmented Retrieval for Wound
Infection Detection (SCARWID), a novel deep learning framework that leverages
synthetic textual descriptions to augment DFU images. SCARWID consists of two
components: (1) Wound-BLIP, a Vision-Language Model (VLM) fine-tuned on
GPT-4o-generated descriptions to synthesize consistent captions from images;
and (2) an Image-Text Fusion module that uses cross-attention to extract
cross-modal embeddings from an image and its corresponding Wound-BLIP caption.
Infection status is determined by retrieving the top-k similar items from a
labeled support set. To enhance the diversity of training data, we utilized a
latent diffusion model to generate additional wound images. As a result,
SCARWID outperformed state-of-the-art models, achieving average sensitivity,
specificity, and accuracy of 0.85, 0.78, and 0.81, respectively, for wound
infection classification. Displaying the generated captions alongside the wound
images and infection detection results enhances interpretability and trust,
enabling nurses to align SCARWID outputs with their medical knowledge. This is
particularly valuable when wound notes are unavailable or when assisting novice
nurses who may find it difficult to identify visual attributes of wound
infection.


