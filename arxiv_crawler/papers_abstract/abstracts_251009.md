# Abstracts of Papers

## Physics
### GyroSwin: 5D Surrogates for Gyrokinetic Plasma Turbulence Simulations
**Authors**: Fabian Paischer, Gianluca Galletti, William Hornsby, Paul Setinek, Lorenzo Zanisi, Naomi Carey, Stanislas Pamela, Johannes Brandstetter

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07314v1](http://arxiv.org/pdf/2510.07314v1)

**Abstract**: Nuclear fusion plays a pivotal role in the quest for reliable and sustainable
energy production. A major roadblock to viable fusion power is understanding
plasma turbulence, which significantly impairs plasma confinement, and is vital
for next-generation reactor design. Plasma turbulence is governed by the
nonlinear gyrokinetic equation, which evolves a 5D distribution function over
time. Due to its high computational cost, reduced-order models are often
employed in practice to approximate turbulent transport of energy. However,
they omit nonlinear effects unique to the full 5D dynamics. To tackle this, we
introduce GyroSwin, the first scalable 5D neural surrogate that can model 5D
nonlinear gyrokinetic simulations, thereby capturing the physical phenomena
neglected by reduced models, while providing accurate estimates of turbulent
heat transport.GyroSwin (i) extends hierarchical Vision Transformers to 5D,
(ii) introduces cross-attention and integration modules for latent
3D$\leftrightarrow$5D interactions between electrostatic potential fields and
the distribution function, and (iii) performs channelwise mode separation
inspired by nonlinear physics. We demonstrate that GyroSwin outperforms widely
used reduced numerics on heat flux prediction, captures the turbulent energy
cascade, and reduces the cost of fully resolved nonlinear gyrokinetics by three
orders of magnitude while remaining physically verifiable. GyroSwin shows
promising scaling laws, tested up to one billion parameters, paving the way for
scalable neural surrogates for gyrokinetic simulations of plasma turbulence.


### Is it Gaussian? Testing bosonic quantum states
**Authors**: Filippo Girardi, Freek Witteveen, Francesco Anna Mele, Lennart Bittel, Salvatore F. E. Oliviero, David Gross, Michael Walter

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07305v1](http://arxiv.org/pdf/2510.07305v1)

**Abstract**: Gaussian states are widely regarded as one of the most relevant classes of
continuous-variable (CV) quantum states, as they naturally arise in physical
systems and play a key role in quantum technologies. This motivates a
fundamental question: given copies of an unknown CV state, how can we
efficiently test whether it is Gaussian? We address this problem from the
perspective of representation theory and quantum learning theory,
characterizing the sample complexity of Gaussianity testing as a function of
the number of modes. For pure states, we prove that just a constant number of
copies is sufficient to decide whether the state is exactly Gaussian. We then
extend this to the tolerant setting, showing that a polynomial number of copies
suffices to distinguish states that are close to Gaussian from those that are
far. In contrast, we establish that testing Gaussianity of general mixed states
necessarily requires exponentially many copies, thereby identifying a
fundamental limitation in testing CV systems. Our approach relies on
rotation-invariant symmetries of Gaussian states together with the recently
introduced toolbox of CV trace-distance bounds.


### Effects of Wall Roughness on Coupled Flow and Heat Transport in Fractured Media
**Authors**: Alessandro Lenci, Yves Méheust, Maria Klepikova, Vittorio Di Federico, Daniel M. Tartakovsky

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07294v1](http://arxiv.org/pdf/2510.07294v1)

**Abstract**: Heat transfer in fractured media is governed by the interplay between
advective transport along rough-walled fractures and conductive transport, both
within the fractures and in the surrounding low-permeability matrix. Flow
localization induced by aperture heterogeneity, combined with matrix
conduction, gives rise to anomalous thermal behavior. To capture these effects,
we develop a stochastic modeling framework that couples a time-domain random
walk (TDRW) representation of advective and conductive transport in the
fractures with a semi-analytical model of conductive heat exchange with the
matrix. Matrix trapping times follow a L\'evy-Smirnov distribution derived from
first-passage theory, capturing the heavy-tailed dynamics typical of fractured
systems. Heat flux at the fracture-matrix interface is computed via a nonlocal
convolution integral based on Duhamel's principle, accounting for thermal
memory effects. The model is validated against analytical benchmarks and
finite-element simulations. Monte Carlo simulations over stochastic aperture
fields quantify the influence of fracture closure, correlation length, and
P\'eclet number. Results reveal a transition from superdiffusive to
subdiffusive regimes, driven by the competition between advective transport
along preferential paths, dispersion induced by aperture variability, and
matrix-driven heat conduction. In the long-time regime, heat exchange exhibits
a characteristic $t^{-1/2}$ decay. At early times, limited thermal penetration
into the matrix leads to weaker interfacial fluxes, underscoring the role of
matrix thermal inertia. The proposed framework enables physically consistent
and computationally efficient simulations of thermal transport in complex
fractured systems, with implications for geothermal energy, subsurface thermal
storage, and engineered heat exchange in low-permeability environments.


### Quantum Replica Exchange
**Authors**: Zherui Chen, Joao Basso, Zhiyan Ding, Lin Lin

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07291v1](http://arxiv.org/pdf/2510.07291v1)

**Abstract**: The presence of energy barriers in the state space of a physical system can
lead to exponentially slow convergence for sampling algorithms like Markov
chain Monte Carlo (MCMC). In the classical setting, replica exchange (or
parallel tempering) is a powerful heuristic to accelerate mixing in these
scenarios. In the quantum realm, preparing Gibbs states of Hamiltonians faces a
similar challenge, where bottlenecks can dramatically increase the mixing time
of quantum dynamical semigroups. In this work, we introduce a quantum analogue
of the replica exchange method. We define a Lindbladian on a joint system of
two replicas and prove that it can accelerate mixing for a class of
Hamiltonians with local energy barriers. Our main result provides a rigorous
lower bound on the spectral gap of the combined system's Lindbladian, which
leads to an exponential improvement in spectral gap with respect to the barrier
height. We showcase the applicability of our method with several examples,
including the defected 1D Ising model at arbitrary constant temperature, and
defected non-commuting local Hamiltonians at high temperature. Our work
provides a rigorous acceleration mechanism for quantum Gibbs preparation.


### Muonium HFS Uncertainty Revisited
**Authors**: Michael I. Eides

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07281v1](http://arxiv.org/pdf/2510.07281v1)

**Abstract**: Uncertainty of the quantum electrodynamics theoretical prediction for the
hyperfine splitting in the ground state of muonium is considered. It is
compared with the respective discussion in the two most recent CODATA
adjustments of the fundamental physical constants.


### Dual Natural Gradient Descent for Scalable Training of Physics-Informed Neural Networks
**Authors**: Anas Jnini, Flavio Vella

**Published Date**: 2025-05-27

**Updated Date**: 2025-10-08

**PDF Url**: [2505.21404v2](http://arxiv.org/pdf/2505.21404v2)

**Abstract**: Natural-gradient methods markedly accelerate the training of Physics-Informed
Neural Networks (PINNs), yet their Gauss--Newton update must be solved in the
parameter space, incurring a prohibitive $O(n^3)$ time complexity, where $n$ is
the number of network trainable weights. We show that exactly the same step can
instead be formulated in a generally smaller residual space of size $m =
\sum_{\gamma} N_{\gamma} d_{\gamma}$, where each residual class $\gamma$ (e.g.
PDE interior, boundary, initial data) contributes $N_{\gamma}$ collocation
points of output dimension $d_{\gamma}$.
  Building on this insight, we introduce \textit{Dual Natural Gradient Descent}
(D-NGD). D-NGD computes the Gauss--Newton step in residual space, augments it
with a geodesic-acceleration correction at negligible extra cost, and provides
both a dense direct solver for modest $m$ and a Nystrom-preconditioned
conjugate-gradient solver for larger $m$.
  Experimentally, D-NGD scales second-order PINN optimization to networks with
up to 12.8 million parameters, delivers one- to three-order-of-magnitude lower
final error $L^2$ than first-order methods (Adam, SGD) and quasi-Newton
methods, and -- crucially -- enables natural-gradient training of PINNs at this
scale on a single GPU.


### On quantum to classical comparison for Davies generators
**Authors**: Joao Basso, Shirshendu Ganguly, Alistair Sinclair, Nikhil Srivastava, Zachary Stier, Thuy-Duong Vuong

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07267v1](http://arxiv.org/pdf/2510.07267v1)

**Abstract**: Despite extensive study, our understanding of quantum Markov chains remains
far less complete than that of their classical counterparts. [Temme'13]
observed that the Davies Lindbladian, a well-studied model of quantum Markov
dynamics, contains an embedded classical Markov generator, raising the natural
question of how the convergence properties of the quantum and classical
dynamics are related. While [Temme'13] showed that the spectral gap of the
Davies Lindbladian can be much smaller than that of the embedded classical
generator for certain highly structured Hamiltonians, we show that if the
spectrum of the Hamiltonian does not contain long arithmetic progressions, then
the two spectral gaps must be comparable. As a consequence, we prove that for a
large class of Hamiltonians, including those obtained by perturbing a fixed
Hamiltonian with a generic external field, the quantum spectral gap remains
within a constant factor of the classical spectral gap. Our result aligns with
physical intuition and enables the application of classical Markov chain
techniques to the quantum setting.
  The proof is based on showing that any ``off-diagonal'' eigenvector of the
Davies generator can be used to construct an observable which commutes with the
Hamiltonian and has a Lindbladian Rayleigh quotient which can be upper bounded
in terms of that of the original eigenvector's Lindbladian Rayleigh quotient.
Thus, a spectral gap for such observables implies a spectral gap for the full
Davies generator.


### Statistical Estimates for 2D stochastic Navier-Stokes Equations
**Authors**: Anuj Kumar, Ali Pakzad

**Published Date**: 2025-01-30

**Updated Date**: 2025-10-08

**PDF Url**: [2501.18213v2](http://arxiv.org/pdf/2501.18213v2)

**Abstract**: The statistical features of homogeneous, isotropic, two-dimensional
stochastic turbulence are discussed. We derive some rigorous bounds for the
mean value of the bulk energy dissipation rate $\mathbb{E} [\varepsilon ]$ and
enstrophy dissipation rates $\mathbb{E} [\chi] $ for 2D flows sustained by a
variety of stochastic driving forces. We show that $$\mathbb{E} [ \varepsilon ]
\rightarrow 0 \hspace{0.5cm}\mbox{and} \hspace{0.5cm} \mathbb{E} [ \chi ]
\lesssim \mathcal{O}(1)$$ in the inviscid limit, consistent with the
dual-cascade in 2D turbulence.


### Structure-Preserving MHD-Driftkinetic Discretization for Wave-Particle Interactions
**Authors**: Byung Kyu Na, Stefan Possanner, Xin Wang

**Published Date**: 2025-10-05

**Updated Date**: 2025-10-08

**PDF Url**: [2510.04385v2](http://arxiv.org/pdf/2510.04385v2)

**Abstract**: We present a structure-preserving discretization of the hybrid
magnetohydrodynamics (MHD)-driftkinetic system for simulations of low-frequency
wave-particle interactions. The model equations are derived from a variational
principle, assuring energetically consistent couplings between MHD fluids and
driftkinetic particles. The spatial discretization is based on a
finite-element-exterior-calculus (FEEC) framework for the MHD and a
particle-in-cell (PIC) method for the driftkinetic. A key feature of the scheme
is the inclusion of the non-quadratic particle magnetic moment energy term in
the Hamiltonian, which is introduced by the guiding-center approximation. The
resulting discrete Hamiltonian structure naturally organizes the dynamics into
skew-symmetric subsystems, enabling balanced energy exchange. To handle the
non-quadratic energy term, we develop energy-preserving time integrators based
on discrete gradient methods. The algorithm is implemented in the open-source
Python package $\texttt{STRUPHY}$. Numerical experiments confirm the
energy-conserving property of the scheme and demonstrate the capability to
simulate energetic particles (EP) induced excitation of toroidal Alfv\'en
eigenmodes (TAE) without artificial dissipation or mode filtering. This
capability highlights the potential of structure-preserving schemes for
high-fidelity simulations of hybrid systems.


### Diffusion Codes: Self-Correction from Small(er)-Set Expansion with Tunable Non-locality
**Authors**: Adithya Sriram, Vedika Khemani, Benedikt Placke

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07179v1](http://arxiv.org/pdf/2510.07179v1)

**Abstract**: Optimal constructions of classical LDPC codes can be obtained by choosing the
Tanner graph uniformly at random among biregular graphs. We introduce a class
of codes that we call ``diffusion codes'', defined by placing each edge
connecting bits and checks on some graph, and acting on that graph with a
random SWAP network. By tuning the depth of the SWAP network, we can tune a
tradeoff between the amount of randomness -- and hence the optimality of code
parameters -- and locality with respect to the underlying graph. For diffusion
codes defined on the cycle graph, if the SWAP network has depth $\sim Tn$ with
$T> n^{2\beta}$ for arbitrary $\beta>0$, then we prove that almost surely the
Tanner graph is a lossless ``smaller set'' vertex expander for small sets up
size $\delta \sim \sqrt T \sim n^{\beta}$, with bounded bit and check degree.
At the same time, the geometric size of the largest stabilizer is bounded by
$\sqrt T$ in graph distance. We argue, based on physical intuition, that this
result should hold more generally on arbitrary graphs. By taking hypergraph
products of these classical codes we obtain quantum LDPC codes defined on the
torus with smaller-set boundary and co-boundary expansion and the same
expansion/locality tradeoffs as for the classical codes. These codes are
self-correcting and admit single-shot decoding, while having the geometric size
of the stabilizer growing as an arbitrarily small power law. Our proof
technique establishes mixing of a random SWAP network on small subsystems at
times scaling with only the subsystem size, which may be of independent
interest.


## Diffusion
### Bit-Level Discrete Diffusion with Markov Probabilistic Models: An Improved Framework with Sharp Convergence Bounds under Minimal Assumptions
**Authors**: Le-Tuyet-Nhi Pham, Dario Shariatian, Antonio Ocello, Giovanni Conforti, Alain Durmus

**Published Date**: 2025-02-11

**Updated Date**: 2025-10-08

**PDF Url**: [2502.07939v2](http://arxiv.org/pdf/2502.07939v2)

**Abstract**: This paper introduces Discrete Markov Probabilistic Models (DMPMs), a novel
discrete diffusion algorithm for discrete data generation. The algorithm
operates in discrete bit space, where the noising process is a continuous-time
Markov chain that flips labels uniformly at random. The time-reversal process,
like the forward noise process, is a jump process with its intensity governed
by a discrete analogue of the classical score function. Crucially, this
intensity is proven to be the conditional expectation of a function of the
forward process, underlining theoretical alignment with score-based generative
models. We establish convergence bounds for the algorithm under minimal
assumptions, ensuring robustness and efficiency, which we demonstrate through
experiments on low-dimensional Bernoulli-distributed datasets and
high-dimensional binary MNIST data. The results highlight competitive
performance in generating discrete structures compared to the state-of-the-art.
This work bridges theoretical foundations and practical applications, advancing
the development of effective and theoretically grounded discrete generative
modeling.


### Generative AI for Cel-Animation: A Survey
**Authors**: Yolo Yunlong Tang, Junjia Guo, Pinxin Liu, Zhiyuan Wang, Hang Hua, Jia-Xing Zhong, Yunzhong Xiao, Chao Huang, Luchuan Song, Susan Liang, Yizhi Song, Liu He, Jing Bi, Mingqian Feng, Xinyang Li, Zeliang Zhang, Chenliang Xu

**Published Date**: 2025-01-08

**Updated Date**: 2025-10-08

**PDF Url**: [2501.06250v4](http://arxiv.org/pdf/2501.06250v4)

**Abstract**: Traditional Celluloid (Cel) Animation production pipeline encompasses
multiple essential steps, including storyboarding, layout design, keyframe
animation, inbetweening, and colorization, which demand substantial manual
effort, technical expertise, and significant time investment. These challenges
have historically impeded the efficiency and scalability of Cel-Animation
production. The rise of generative artificial intelligence (GenAI),
encompassing large language models, multimodal models, and diffusion models,
offers innovative solutions by automating tasks such as inbetween frame
generation, colorization, and storyboard creation. This survey explores how
GenAI integration is revolutionizing traditional animation workflows by
lowering technical barriers, broadening accessibility for a wider range of
creators through tools like AniDoc, ToonCrafter, and AniSora, and enabling
artists to focus more on creative expression and artistic innovation. Despite
its potential, challenges like visual consistency, stylistic coherence, and
ethical considerations persist. Additionally, this paper explores future
directions and advancements in AI-assisted animation. For further exploration
and resources, please visit our GitHub repository:
https://github.com/yunlong10/Awesome-AI4Animation


### A Digital Twin Framework for Metamorphic Testing of Autonomous Driving Systems Using Generative Model
**Authors**: Tony Zhang, Burak Kantarci, Umair Siddique

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07133v1](http://arxiv.org/pdf/2510.07133v1)

**Abstract**: Ensuring the safety of self-driving cars remains a major challenge due to the
complexity and unpredictability of real-world driving environments. Traditional
testing methods face significant limitations, such as the oracle problem, which
makes it difficult to determine whether a system's behavior is correct, and the
inability to cover the full range of scenarios an autonomous vehicle may
encounter. In this paper, we introduce a digital twin-driven metamorphic
testing framework that addresses these challenges by creating a virtual replica
of the self-driving system and its operating environment. By combining digital
twin technology with AI-based image generative models such as Stable Diffusion,
our approach enables the systematic generation of realistic and diverse driving
scenes. This includes variations in weather, road topology, and environmental
features, all while maintaining the core semantics of the original scenario.
The digital twin provides a synchronized simulation environment where changes
can be tested in a controlled and repeatable manner. Within this environment,
we define three metamorphic relations inspired by real-world traffic rules and
vehicle behavior. We validate our framework in the Udacity self-driving
simulator and demonstrate that it significantly enhances test coverage and
effectiveness. Our method achieves the highest true positive rate (0.719), F1
score (0.689), and precision (0.662) compared to baseline approaches. This
paper highlights the value of integrating digital twins with AI-powered
scenario generation to create a scalable, automated, and high-fidelity testing
solution for autonomous vehicle safety.


### Graph Conditioned Diffusion for Controllable Histopathology Image Generation
**Authors**: Sarah Cechnicka, Matthew Baugh, Weitong Zhang, Mischa Dombrowski, Zhe Li, Johannes C. Paetzold, Candice Roufosse, Bernhard Kainz

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07129v1](http://arxiv.org/pdf/2510.07129v1)

**Abstract**: Recent advances in Diffusion Probabilistic Models (DPMs) have set new
standards in high-quality image synthesis. Yet, controlled generation remains
challenging, particularly in sensitive areas such as medical imaging. Medical
images feature inherent structure such as consistent spatial arrangement, shape
or texture, all of which are critical for diagnosis. However, existing DPMs
operate in noisy latent spaces that lack semantic structure and strong priors,
making it difficult to ensure meaningful control over generated content. To
address this, we propose graph-based object-level representations for
Graph-Conditioned-Diffusion. Our approach generates graph nodes corresponding
to each major structure in the image, encapsulating their individual features
and relationships. These graph representations are processed by a transformer
module and integrated into a diffusion model via the text-conditioning
mechanism, enabling fine-grained control over generation. We evaluate this
approach using a real-world histopathology use case, demonstrating that our
generated data can reliably substitute for annotated patient data in downstream
segmentation tasks. The code is available here.


### Diffusion-Augmented Reinforcement Learning for Robust Portfolio Optimization under Stress Scenarios
**Authors**: Himanshu Choudhary, Arishi Orra, Manoj Thakur

**Published Date**: 2025-10-08

**Updated Date**: 2025-10-08

**PDF Url**: [2510.07099v1](http://arxiv.org/pdf/2510.07099v1)

**Abstract**: In the ever-changing and intricate landscape of financial markets, portfolio
optimisation remains a formidable challenge for investors and asset managers.
Conventional methods often struggle to capture the complex dynamics of market
behaviour and align with diverse investor preferences. To address this, we
propose an innovative framework, termed Diffusion-Augmented Reinforcement
Learning (DARL), which synergistically integrates Denoising Diffusion
Probabilistic Models (DDPMs) with Deep Reinforcement Learning (DRL) for
portfolio management. By leveraging DDPMs to generate synthetic market crash
scenarios conditioned on varying stress intensities, our approach significantly
enhances the robustness of training data. Empirical evaluations demonstrate
that DARL outperforms traditional baselines, delivering superior risk-adjusted
returns and resilience against unforeseen crises, such as the 2025 Tariff
Crisis. This work offers a robust and practical methodology to bolster stress
resilience in DRL-driven financial applications.


