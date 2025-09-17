# Abstracts of Papers

## Physics
### Conformal prediction for uncertainties in nucleon-nucleon scattering
**Authors**: Habib Yousefi Dezdarani, Ryan Curry, Alexandros Gezerlis

**Published Date**: 2025-07-10

**Updated Date**: 2025-09-16

**PDF Url**: [2507.08085v2](http://arxiv.org/pdf/2507.08085v2)

**Abstract**: Conformal prediction is a distribution-free and model-agnostic
uncertainty-quantification method that provides finite-sample prediction
intervals with guaranteed coverage. In this work, for the first time, we apply
conformal-prediction to generate uncertainty bands for physical observables in
nuclear physics, such as the total cross section and nucleon-nucleon phase
shifts. We demonstrate the method's flexibility by considering three scenarios:
(i) a pointwise model, where expansion coefficients in chiral effective field
theory are treated as random variables; (ii) a Gaussian-Process model for the
coefficients; and (iii) phase shifts at various energies and partial waves
calculated using local interactions from chiral effective field theory. In each
case, conformal-prediction intervals are constructed and validated empirically.
Our results show that conformal prediction provides reliable and adaptive
uncertainty bands even in the presence of non-Gaussian behavior, such as
skewness and heavy tails. These findings highlight conformal prediction as a
robust and practical framework for quantifying theoretical uncertainties.


### How Theory-Informed Priors Affect DESI Evidence for Evolving Dark Energy
**Authors**: Michael W. Toomey, Gabriele Montefalcone, Evan McDonough, Katherine Freese

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13318v1](http://arxiv.org/pdf/2509.13318v1)

**Abstract**: Recent measurements of baryon acoustic oscillations (BAO) from the Dark
Energy Spectroscopic Instrument (DESI) have been interpreted to suggest that
dark energy may be evolving. In this work, we examine how prior choices affect
such conclusions. Specifically, we study the biases introduced by the customary
use of uniform priors on the Chevallier-Polarski-Linder (CPL) parameters, $w_0$
and $w_a$, when assessing evidence for evolving dark energy. To do so, we
construct theory-informed priors on $(w_0, w_a)$ using a normalizing flow (NF),
trained on two representative quintessence models, which learns the
distribution of these parameters conditional on the underlying $\Lambda$CDM
parameters. In the combined $\textit{Planck}$ CMB + DESI BAO analysis we find
that the apparent tension with a cosmological constant in the CPL framework can
be reduced from $\sim 3.1\sigma$ to $\sim 1.3\sigma$ once theory-informed
priors are applied, rendering the result effectively consistent with
$\Lambda$CDM. For completeness, we also analyze combinations that include Type
Ia supernova data, showing similar shifts toward the $\Lambda$CDM limit. Taken
together, the observed sensitivity to prior choices in these analyses arises
because uniform priors - often mischaracterized as "uninformative" - can
actually bias inferences toward unphysical parameter regions. Consequently, our
results underscore the importance of adopting physically motivated priors to
ensure robust cosmological inferences, especially when evaluating new
hypotheses with only marginal statistical support. Lastly, our NF-based
framework achieves these results by post-processing existing MCMC chains,
requiring $\approx 1$ hour of additional CPU compute time on top of the base
analysis - a dramatic speedup over direct model sampling that highlights the
scalability of this approach for testing diverse theoretical models.


### Configurational Temperature as a Diagnostic for Complex Langevin Dynamics in the 3D XY Model
**Authors**: Anosh Joseph, Arpith Kumar

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13314v1](http://arxiv.org/pdf/2509.13314v1)

**Abstract**: We investigate the applicability of complex Langevin dynamics to the
three-dimensional XY model at finite chemical potential. To assess correctness,
we introduce a new diagnostic based on the configurational temperature (or
configurational coupling) estimator, recently proposed as a thermodynamic
consistency check. We compare this criterion with the established
Nagata-Nishimura-Shimasaki drift-decay test across a range of couplings and
chemical potentials. Our results show that complex Langevin dynamics yields
reliable results in the ordered phase (large $\beta$), but fails in the
disordered phase (small $\beta$), even when the sign problem is mild. The
configurational estimator provides a clear and physics-driven reliability test
that complements drift-based diagnostics. These findings establish the
estimator as a practical tool for identifying incorrect convergence, and
highlight its potential for broader applications in lattice field theories with
complex actions.


### Mixed Triplet-Singlet Order Parameter in Decoupled Superconducting 1H Monolayers of Transition-Metal Dichalcogenides
**Authors**: Avior Almoalem, Sajilesh Kunhiparambath, Roni Anna Gofman, Yuval Nitzav, Ilay Mangel, Nitzan Ragoler, Jun Fujii, Ivana Vobornik, Francois Bertran, Amit Kanigel, Jonathan Ruhman, Vidya Madhavan

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13303v1](http://arxiv.org/pdf/2509.13303v1)

**Abstract**: Understanding the emergence of unconventional superconductivity, where the
order parameter deviates from simple isotropic s-wave pairing, is a central
puzzle in condensed matter physics. Transition-metal dichalcogenides (TMDCs),
though generally regarded as conventional superconductors, display signatures
of this unusual behavior and thus provide a particularly intriguing platform to
explore how exotic states arise. Here we investigate the misfit compound
(SnS)$_{1.15}$(TaS$_2$), a heterostructure composed of alternating SnS and
1H-TaS$_2$ layers. Using transport, photoemission, and scanning tunneling
spectroscopy, we demonstrate that the SnS layers effectively decouple the
TaS$_2$ into electronically isolated 1H sheets. In this limit, the tunneling
density of states reveals a clear two-gap superconducting spectrum with T$_c
\sim$ 3.1 K. A theoretical model based on lack of inversion symmetry and
finite-range attraction reproduces the observed multi-gap structure as a mixed
singlet-triplet state. These results establish misfit compounds as a powerful
platform for studying unconventional superconductivity in isolated 1H layers
and for realizing multiple uncoupled superconductors within a single crystal.


### QDFlow: A Python package for physics simulations of quantum dot devices
**Authors**: Donovan L. Buterakos, Sandesh S. Kalantre, Joshua Ziegler, Jacob M Taylor, Justyna P. Zwolak

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13298v1](http://arxiv.org/pdf/2509.13298v1)

**Abstract**: Recent advances in machine learning (ML) have accelerated progress in
calibrating and operating quantum dot (QD) devices. However, most ML approaches
rely on access to large, high-quality labeled datasets for training,
benchmarking, and validation, with labels capturing key features in the data.
Obtaining such datasets experimentally is challenging due to limited data
availability and the labor-intensive nature of labeling. QDFlow is an
open-source physics simulator for multi-QD arrays that generates realistic
synthetic data with ground-truth labels. QDFlow combines a self-consistent
Thomas-Fermi solver, a dynamic capacitance model, and flexible noise modules to
produce charge stability diagrams and ray-based data closely resembling
experiments. With extensive tunable parameters and customizable noise models,
QDFlow supports the creation of large, diverse datasets for ML development,
benchmarking, and quantum device research.


### Higgs Phases and Boundary Criticality
**Authors**: Kristian Tyn Kai Chung, Rafael Flores-Calderón, Rafael C. Torres, Pedro Ribeiro, Sergej Moroz, Paul McClarty

**Published Date**: 2024-04-25

**Updated Date**: 2025-09-16

**PDF Url**: [2404.17001v2](http://arxiv.org/pdf/2404.17001v2)

**Abstract**: Motivated by recent work connecting Higgs phases to symmetry protected
topological (SPT) phases, we investigate the interplay of gauge redundancy and
global symmetry in lattice gauge theories with Higgs fields in the presence of
a boundary. The core conceptual point is that a global symmetry associated to a
Higgs field, which is pure-gauge in a closed system, acts physically at the
boundary under boundary conditions which allow electric flux to escape the
system. We demonstrate in both Abelian and non-Abelian models that this
symmetry is spontaneously broken in the Higgs regime, implying the presence of
gapless edge modes. Starting with the U(1) Abelian Higgs model in 4D, we
demonstrate a boundary phase transition in the 3D XY universality class
separating the bulk Higgs and confining regimes. Varying the boundary coupling
while preserving the symmetries shifts the location of the boundary phase
transition. We then consider non-Abelian gauge theories with fundamental and
group-valued Higgs matter, and identify the analogous non-Abelian global
symmetry acting on the boundary generated by the total color charge. For
SU($N$) gauge theory with fundamental Higgs matter we argue for a boundary
phase transition in the O($2N$) universality class, verified numerically for
$N=2,3$. For group-valued Higgs matter, the boundary theory is a principal
chiral model exhibiting chiral symmetry breaking. We further demonstrate this
mechanism in theories with higher-form Higgs fields. We show how the
higher-form matter symmetry acts at the boundary and can spontaneously break,
exhibiting a boundary confinement-deconfinement transition. We also study the
electric-magnetic dual theory, demonstrating a dual magnetic defect
condensation transition at the boundary. We discuss some implications and
extensions of these findings and what they may imply for the relation between
Higgs and SPT phases.


### Flavour and cosmological probes of Diracon models
**Authors**: Salvador Centelles Chuliá, Tim Herbermann, Antonio Herrero-Brocal, Avelino Vicente

**Published Date**: 2025-06-06

**Updated Date**: 2025-09-16

**PDF Url**: [2506.06449v2](http://arxiv.org/pdf/2506.06449v2)

**Abstract**: We present and analyze two minimal extensions of the Standard Model featuring
a spontaneously broken global, chiral, and anomaly-free $U(1)_D$ symmetry. This
breaking generates naturally small Dirac neutrino masses via a seesaw mechanism
and yields a physical massless Goldstone boson, the Diracon. Although both
models share the same particle content and scalar potential, their distinct
symmetry breaking pattern leads to remarkably different phenomenological and
cosmological signatures. In the first model, the Diracon couples weakly to
charged leptons but right-handed neutrinos can be efficiently produced in the
early Universe, resulting in stringent constraints from the effective number of
relativistic species, $\Delta N_{\text{eff}}$. Conversely, in the second one,
right-handed neutrino production is suppressed, and flavour-violating processes
such as $\mu \to e \mathcal{D}$ provide the most promising probes. These simple
but elegant models showcase the complementarity between cosmological
observations and low-energy flavour experiments in the search for physics
beyond the Standard Model.


### Emergent structures in open EFTs
**Authors**: Perseas Christodoulidis

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13284v1](http://arxiv.org/pdf/2509.13284v1)

**Abstract**: Open effective field theories (EFTs) provide a systematic framework for
describing systems coupled to an environment, where dissipation, noise, and
modified conservation laws naturally arise. Working within the
Schwinger-Keldysh formalism, we examine open extensions of well-studied
theories describing a spontaneous symmetry breaking phase in the higher-form
sense: the superfluid, Maxwell theory, and Einstein's gravity. We demonstrate
that to leading order breaking advanced symmetries while preserving the
physical ones leads to (i) deformed conservation laws that hold at the level of
expectation values for global symmetries and (ii) deformed noise constraints in
gauge or gravitational theories.


### HARMONIC: A Content-Centric Cognitive Robotic Architecture
**Authors**: Sanjay Oruganti, Sergei Nirenburg, Marjorie McShane, Jesse English, Michael K. Roberts, Christian Arndt, Carlos Gonzalez, Mingyo Seo, Luis Sentis

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13279v1](http://arxiv.org/pdf/2509.13279v1)

**Abstract**: This paper introduces HARMONIC, a cognitive-robotic architecture designed for
robots in human-robotic teams. HARMONIC supports semantic perception
interpretation, human-like decision-making, and intentional language
communication. It addresses the issues of safety and quality of results; aims
to solve problems of data scarcity, explainability, and safety; and promotes
transparency and trust. Two proof-of-concept HARMONIC-based robotic systems are
demonstrated, each implemented in both a high-fidelity simulation environment
and on physical robotic platforms.


### OGF: An Online Gradient Flow Method for Optimizing the Statistical Steady-State Time Averages of Unsteady Turbulent Flows
**Authors**: Tom Hickling, Jonathan F. MacArt, Justin Sirignano, Den Waidmann

**Published Date**: 2025-07-07

**Updated Date**: 2025-09-16

**PDF Url**: [2507.05149v2](http://arxiv.org/pdf/2507.05149v2)

**Abstract**: Turbulent flows are chaotic and unsteady, but their statistical distribution
converges to a statistical steady state. Engineering quantities of interest
typically take the form of time-average statistics such as $ \frac{1}{t}
\int_0^t f ( u(x,\tau; \theta) ) d\tau \overset{t \rightarrow
\infty}{\rightarrow} F(x; \theta)$, where $u(x,t; \theta)$ are solutions of the
Navier--Stokes equations with parameters $\theta$. Optimizing over $F(x;
\theta)$ has many engineering applications including geometric optimization,
flow control, and closure modeling. However, this remains an open challenge, as
existing computational approaches are incapable of scaling to physically
representative numbers of grid points. The fundamental obstacle is the
chaoticity of turbulent flows: gradients calculated with the adjoint method
diverge exponentially as $t \rightarrow \infty$.
  We develop a new online gradient-flow (OGF) method that is scalable to large
degree-of-freedom systems and enables optimizing for the steady-state
statistics of chaotic, unsteady, turbulence-resolving simulations. The method
forward-propagates an online estimate for the gradient of $F(x; \theta)$ while
simultaneously performing online updates of the parameters $\theta$. A key
feature is the fully online nature of the algorithm to facilitate faster
optimization progress and its combination with a finite-difference estimator to
avoid the divergence of gradients due to chaoticity. The proposed OGF method is
demonstrated for optimizations over three chaotic ordinary and partial
differential equations: the Lorenz-63 equation, the Kuramoto--Sivashinsky
equation, and Navier--Stokes solutions of compressible, forced, homogeneous
isotropic turbulence. In each case, the OGF method successfully reduces the
loss based on $F(x; \theta)$ by several orders of magnitude and accurately
recovers the optimal parameters.


## Diffusion
### Pitfalls of defacing whole-head MRI: re-identification risk with diffusion models and compromised research potential
**Authors**: Chenyu Gao, Kaiwen Xu, Michael E. Kim, Lianrui Zuo, Zhiyuan Li, Derek B. Archer, Timothy J. Hohman, Ann Zenobia Moore, Luigi Ferrucci, Lori L. Beason-Held, Susan M. Resnick, Christos Davatzikos, Jerry L. Prince, Bennett A. Landman

**Published Date**: 2025-01-31

**Updated Date**: 2025-09-16

**PDF Url**: [2501.18834v2](http://arxiv.org/pdf/2501.18834v2)

**Abstract**: Defacing is often applied to head magnetic resonance image (MRI) datasets
prior to public release to address privacy concerns. The alteration of facial
and nearby voxels has provoked discussions about the true capability of these
techniques to ensure privacy as well as their impact on downstream tasks. With
advancements in deep generative models, the extent to which defacing can
protect privacy is uncertain. Additionally, while the altered voxels are known
to contain valuable anatomical information, their potential to support research
beyond the anatomical regions directly affected by defacing remains uncertain.
To evaluate these considerations, we develop a refacing pipeline that recovers
faces in defaced head MRIs using cascaded diffusion probabilistic models
(DPMs). The DPMs are trained on images from 180 subjects and tested on images
from 484 unseen subjects, 469 of whom are from a different dataset. To assess
whether the altered voxels in defacing contain universally useful information,
we also predict computed tomography (CT)-derived skeletal muscle radiodensity
from facial voxels in both defaced and original MRIs. The results show that
DPMs can generate high-fidelity faces that resemble the original faces from
defaced images, with surface distances to the original faces significantly
smaller than those of a population average face (p < 0.05). This performance
also generalizes well to previously unseen datasets. For skeletal muscle
radiodensity predictions, using defaced images results in significantly weaker
Spearman's rank correlation coefficients compared to using original images (p <
10-4). For shin muscle, the correlation is statistically significant (p < 0.05)
when using original images but not statistically significant (p > 0.05) when
any defacing method is applied, suggesting that defacing might not only fail to
protect privacy but also eliminate valuable information.


### Discovering Mathematical Equations with Diffusion Language Model
**Authors**: Xiaoxu Han, Chengzhen Ning, Jinghui Zhong, Fubiao Yang, Yu Wang, Xin Mu

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13136v1](http://arxiv.org/pdf/2509.13136v1)

**Abstract**: Discovering valid and meaningful mathematical equations from observed data
plays a crucial role in scientific discovery. While this task, symbolic
regression, remains challenging due to the vast search space and the trade-off
between accuracy and complexity. In this paper, we introduce DiffuSR, a
pre-training framework for symbolic regression built upon a continuous-state
diffusion language model. DiffuSR employs a trainable embedding layer within
the diffusion process to map discrete mathematical symbols into a continuous
latent space, modeling equation distributions effectively. Through iterative
denoising, DiffuSR converts an initial noisy sequence into a symbolic equation,
guided by numerical data injected via a cross-attention mechanism. We also
design an effective inference strategy to enhance the accuracy of the
diffusion-based equation generator, which injects logit priors into genetic
programming. Experimental results on standard symbolic regression benchmarks
demonstrate that DiffuSR achieves competitive performance with state-of-the-art
autoregressive methods and generates more interpretable and diverse
mathematical expressions.


### Informed Correctors for Discrete Diffusion Models
**Authors**: Yixiu Zhao, Jiaxin Shi, Feng Chen, Shaul Druckmann, Lester Mackey, Scott Linderman

**Published Date**: 2024-07-30

**Updated Date**: 2025-09-16

**PDF Url**: [2407.21243v4](http://arxiv.org/pdf/2407.21243v4)

**Abstract**: Discrete diffusion has emerged as a powerful framework for generative
modeling in discrete domains, yet efficiently sampling from these models
remains challenging. Existing sampling strategies often struggle to balance
computation and sample quality when the number of sampling steps is reduced,
even when the model has learned the data distribution well. To address these
limitations, we propose a predictor-corrector sampling scheme where the
corrector is informed by the diffusion model to more reliably counter the
accumulating approximation errors. To further enhance the effectiveness of our
informed corrector, we introduce complementary architectural modifications
based on hollow transformers and a simple tailored training objective that
leverages more training signal. We use a synthetic example to illustrate the
failure modes of existing samplers and show how informed correctors alleviate
these problems. On the text8 and tokenized ImageNet 256x256 datasets, our
informed corrector consistently produces superior samples with fewer errors or
improved FID scores for discrete diffusion models. These results underscore the
potential of informed correctors for fast and high-fidelity generation using
discrete diffusion. Our code is available at
https://github.com/lindermanlab/informed-correctors.


### MIA-EPT: Membership Inference Attack via Error Prediction for Tabular Data
**Authors**: Eyal German, Daniel Samira, Yuval Elovici, Asaf Shabtai

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.13046v1](http://arxiv.org/pdf/2509.13046v1)

**Abstract**: Synthetic data generation plays an important role in enabling data sharing,
particularly in sensitive domains like healthcare and finance. Recent advances
in diffusion models have made it possible to generate realistic, high-quality
tabular data, but they may also memorize training records and leak sensitive
information. Membership inference attacks (MIAs) exploit this vulnerability by
determining whether a record was used in training. While MIAs have been studied
in images and text, their use against tabular diffusion models remains
underexplored despite the unique risks of structured attributes and limited
record diversity. In this paper, we introduce MIAEPT, Membership Inference
Attack via Error Prediction for Tabular Data, a novel black-box attack
specifically designed to target tabular diffusion models. MIA-EPT constructs
errorbased feature vectors by masking and reconstructing attributes of target
records, disclosing membership signals based on how well these attributes are
predicted. MIA-EPT operates without access to the internal components of the
generative model, relying only on its synthetic data output, and was shown to
generalize across multiple state-of-the-art diffusion models. We validate
MIA-EPT on three diffusion-based synthesizers, achieving AUC-ROC scores of up
to 0.599 and TPR@10% FPR values of 22.0% in our internal tests. Under the MIDST
2025 competition conditions, MIA-EPT achieved second place in the Black-box
Multi-Table track (TPR@10% FPR = 20.0%). These results demonstrate that our
method can uncover substantial membership leakage in synthetic tabular data,
challenging the assumption that synthetic data is inherently
privacy-preserving. Our code is publicly available at
https://github.com/eyalgerman/MIA-EPT.


### AC-Refiner: Efficient Arithmetic Circuit Optimization Using Conditional Diffusion Models
**Authors**: Chenhao Xue, Kezhi Li, Jiaxing Zhang, Yi Ren, Zhengyuan Shi, Chen Zhang, Yibo Lin, Lining Zhang, Qiang Xu, Guangyu Sun

**Published Date**: 2025-07-03

**Updated Date**: 2025-09-16

**PDF Url**: [2507.02598v2](http://arxiv.org/pdf/2507.02598v2)

**Abstract**: Arithmetic circuits, such as adders and multipliers, are fundamental
components of digital systems, directly impacting the performance, power
efficiency, and area footprint. However, optimizing these circuits remains
challenging due to the vast design space and complex physical constraints.
While recent deep learning-based approaches have shown promise, they struggle
to consistently explore high-potential design variants, limiting their
optimization efficiency. To address this challenge, we propose AC-Refiner, a
novel arithmetic circuit optimization framework leveraging conditional
diffusion models. Our key insight is to reframe arithmetic circuit synthesis as
a conditional image generation task. By carefully conditioning the denoising
diffusion process on target quality-of-results (QoRs), AC-Refiner consistently
produces high-quality circuit designs. Furthermore, the explored designs are
used to fine-tune the diffusion model, which focuses the exploration near the
Pareto frontier. Experimental results demonstrate that AC-Refiner generates
designs with superior Pareto optimality, outperforming state-of-the-art
baselines. The performance gain is further validated by integrating AC-Refiner
into practical applications.


## Quantitative Finance
### DeltaHedge: A Multi-Agent Framework for Portfolio Options Optimization
**Authors**: Feliks Bańka, Jarosław A. Chudziak

**Published Date**: 2025-09-16

**Updated Date**: 2025-09-16

**PDF Url**: [2509.12753v1](http://arxiv.org/pdf/2509.12753v1)

**Abstract**: In volatile financial markets, balancing risk and return remains a
significant challenge. Traditional approaches often focus solely on equity
allocation, overlooking the strategic advantages of options trading for dynamic
risk hedging. This work presents DeltaHedge, a multi-agent framework that
integrates options trading with AI-driven portfolio management. By combining
advanced reinforcement learning techniques with an ensembled options-based
hedging strategy, DeltaHedge enhances risk-adjusted returns and stabilizes
portfolio performance across varying market conditions. Experimental results
demonstrate that DeltaHedge outperforms traditional strategies and standalone
models, underscoring its potential to transform practical portfolio management
in complex financial environments. Building on these findings, this paper
contributes to the fields of quantitative finance and AI-driven portfolio
optimization by introducing a novel multi-agent system for integrating options
trading strategies, addressing a gap in the existing literature.


### SCOR: A Framework for Responsible AI Innovation in Digital Ecosystems
**Authors**: Mohammad Saleh Torkestani, Taha Mansouri

**Published Date**: 2025-09-12

**Updated Date**: 2025-09-12

**PDF Url**: [2509.10653v1](http://arxiv.org/pdf/2509.10653v1)

**Abstract**: AI-driven digital ecosystems span diverse stakeholders including technology
firms, regulators, accelerators and civil society, yet often lack cohesive
ethical governance. This paper proposes a four-pillar framework (SCOR) to embed
accountability, fairness, and inclusivity across such multi-actor networks.
Leveraging a design science approach, we develop a Shared Ethical Charter(S),
structured Co-Design and Stakeholder Engagement protocols(C), a system of
Continuous Oversight and Learning(O), and Adaptive Regulatory Alignment
strategies(R). Each component includes practical guidance, from lite modules
for resource-constrained start-ups to in-depth auditing systems for larger
consortia. Through illustrative vignettes in healthcare, finance, and smart
city contexts, we demonstrate how the framework can harmonize organizational
culture, leadership incentives, and cross-jurisdictional compliance. Our
mixed-method KPI design further ensures that quantitative targets are
complemented by qualitative assessments of user trust and cultural change. By
uniting ethical principles with scalable operational structures, this paper
offers a replicable pathway toward responsible AI innovation in complex digital
ecosystems.


### pySigLib -- Fast Signature-Based Computations on CPU and GPU
**Authors**: Daniil Shmelev, Cristopher Salvi

**Published Date**: 2025-09-12

**Updated Date**: 2025-09-12

**PDF Url**: [2509.10613v1](http://arxiv.org/pdf/2509.10613v1)

**Abstract**: Signature-based methods have recently gained significant traction in machine
learning for sequential data. In particular, signature kernels have emerged as
powerful discriminators and training losses for generative models on
time-series, notably in quantitative finance. However, existing implementations
do not scale to the dataset sizes and sequence lengths encountered in practice.
We present pySigLib, a high-performance Python library offering optimised
implementations of signatures and signature kernels on CPU and GPU, fully
compatible with PyTorch's automatic differentiation. Beyond an efficient
software stack for large-scale signature-based computation, we introduce a
novel differentiation scheme for signature kernels that delivers accurate
gradients at a fraction of the runtime of existing libraries.


