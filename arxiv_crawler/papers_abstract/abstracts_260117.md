# Abstracts of Papers

## Physics
### Emergence and transition of incompressible phases in decorated Landau levels
**Authors**: Bo Peng, Yuzhu Wang, Bo Yang

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10717v1](https://arxiv.org/pdf/2601.10717v1)

**Abstract**: We show a single Landau level (LL) dressed with periodic electrostatic potentials can realize a plethora of interacting topological phases where the Hall conductivity generally does not equal to the LL filling factor. Their physics can be captured by a minimal model of a delta potential lattice within a single LL, realizing exact zero energy Chern bands (denoted as decorated Landau levels or dLL) gapped from dispersive bands with rich geometric properties. With $p/q$ magnetic fluxes per unit cell, there are $q$ dispersive bands and $p-q$ zero energy bands forming the dLL. When the one-body potential strength dominates the electron-electron interaction, band mixing is suppressed and the dispersion bands consist of ``localized states" with vanishing total Chern number. Nevertheless these dispersive bands can have highly nontrivial Berry curvature distribution, and even non-zero Chern numbers when $q>1$. Interestingly even in the limit of large short range interaction, band mixing between dLL and dispersion bands can be strongly suppressed at low filling factor, leading to robust topological phases within the dLL stabilized by the one-body potential. The dLL and the associated dispersive bands can serve as minimal theoretical models for correlated physics in lattice or moire systems; they are also highly tunable experimental platforms for realizing rich phase diagrams of exotic 2D quantum fluids.


### DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids
**Authors**: Navami Kairanda, Shanthika Naik, Marc Habermann, Avinash Sharma, Christian Theobalt, Vladislav Golyanik

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10715v1](https://arxiv.org/pdf/2601.10715v1)

**Abstract**: We present a novel differentiable grid-based representation for efficiently solving differential equations (DEs). Widely used architectures for neural solvers, such as sinusoidal neural networks, are coordinate-based MLPs that are both computationally intensive and slow to train. Although grid-based alternatives for implicit representations (e.g., Instant-NGP and K-Planes) train faster by exploiting signal structure, their reliance on linear interpolation restricts their ability to compute higher-order derivatives, rendering them unsuitable for solving DEs. Our approach overcomes these limitations by combining the efficiency of feature grids with radial basis function interpolation, which is infinitely differentiable. To effectively capture high-frequency solutions and enable stable and faster computation of global gradients, we introduce a multi-resolution decomposition with co-located grids. Our proposed representation, DInf-Grid, is trained implicitly using the differential equations as loss functions, enabling accurate modelling of physical fields. We validate DInf-Grid on a variety of tasks, including the Poisson equation for image reconstruction, the Helmholtz equation for wave fields, and the Kirchhoff-Love boundary value problem for cloth simulation. Our results demonstrate a 5-20x speed-up over coordinate-based MLP-based methods, solving differential equations in seconds or minutes while maintaining comparable accuracy and compactness.


### See Less, Drive Better: Generalizable End-to-End Autonomous Driving via Foundation Models Stochastic Patch Selection
**Authors**: Amir Mallak, Erfan Aasi, Shiva Sreeram, Tsun-Hsuan Wang, Daniela Rus, Alaa Maalouf

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10707v1](https://arxiv.org/pdf/2601.10707v1)

**Abstract**: Recent advances in end-to-end autonomous driving show that policies trained on patch-aligned features extracted from foundation models generalize better to Out-of-Distribution (OOD). We hypothesize that due to the self-attention mechanism, each patch feature implicitly embeds/contains information from all other patches, represented in a different way and intensity, making these descriptors highly redundant. We quantify redundancy in such (BLIP2) features via PCA and cross-patch similarity: $90$% of variance is captured by $17/64$ principal components, and strong inter-token correlations are pervasive. Training on such overlapping information leads the policy to overfit spurious correlations, hurting OOD robustness. We present Stochastic-Patch-Selection (SPS), a simple yet effective approach for learning policies that are more robust, generalizable, and efficient. For every frame, SPS randomly masks a fraction of patch descriptors, not feeding them to the policy model, while preserving the spatial layout of the remaining patches. Thus, the policy is provided with different stochastic but complete views of the (same) scene: every random subset of patches acts like a different, yet still sensible, coherent projection of the world. The policy thus bases its decisions on features that are invariant to which specific tokens survive. Extensive experiments confirm that across all OOD scenarios, our method outperforms the state of the art (SOTA), achieving a $6.2$% average improvement and up to $20.4$% in closed-loop simulations, while being $2.4\times$ faster. We conduct ablations over masking rates and patch-feature reorganization, training and evaluating 9 systems, with 8 of them surpassing prior SOTA. Finally, we show that the same learned policy transfers to a physical, real-world car without any tuning.


### The Effective Theory of Muon-to-Electron Conversion
**Authors**: W. C. Haxton, Evan Rule

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10704v1](https://arxiv.org/pdf/2601.10704v1)

**Abstract**: We summarize recent work to develop an effective theory of muon-to-electron conversion, based on a complete set of low-energy effective operators that are developed from a systematic expansion in velocities and momenta. The expansion effectively factors rates into sums of particle physics and nuclear physics terms, where the former are expressed as bilinears in the LECs (the low-energy constants of the effective theory) and the latter are the associated nuclear responses. One can view the nuclear responses as ``dials" that can be adjusted -- for example, by selection of targets with specific properties -- in order to isolate the former. We show that an important dial, in the case of Mu2e and COMET, will be inelastic transitions to certain low-energy nuclear states that are resolvable in 27Al. If these transitions are exploited, the experiments have the potential not only to discover charged lepton flavor violation (CLFV), but to determine the operators responsible for the CLFV. We also discuss how such low-energy results can be ``ported" to higher energies through a tower of matched EFTs, so they can be combined with other experimental limits to further constrain CLFV


### Data-driven stochastic reduced-order modeling of parametrized dynamical systems
**Authors**: Andrew F. Ilersich, Kevin Course, Prasanth B. Nair

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10690v1](https://arxiv.org/pdf/2601.10690v1)

**Abstract**: Modeling complex dynamical systems under varying conditions is computationally intensive, often rendering high-fidelity simulations intractable. Although reduced-order models (ROMs) offer a promising solution, current methods often struggle with stochastic dynamics and fail to quantify prediction uncertainty, limiting their utility in robust decision-making contexts. To address these challenges, we introduce a data-driven framework for learning continuous-time stochastic ROMs that generalize across parameter spaces and forcing conditions. Our approach, based on amortized stochastic variational inference, leverages a reparametrization trick for Markov Gaussian processes to eliminate the need for computationally expensive forward solvers during training. This enables us to jointly learn a probabilistic autoencoder and stochastic differential equations governing the latent dynamics, at a computational cost that is independent of the dataset size and system stiffness. Additionally, our approach offers the flexibility of incorporating physics-informed priors if available. Numerical studies are presented for three challenging test problems, where we demonstrate excellent generalization to unseen parameter combinations and forcings, and significant efficiency gains compared to existing approaches.


### Efficiency, Curvature, and Complexity of Quantum Evolutions for Qubits in Nonstationary Magnetic Fields
**Authors**: Carlo Cafaro, James Schneeloch

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10672v1](https://arxiv.org/pdf/2601.10672v1)

**Abstract**: In optimal quantum-mechanical evolutions, motion can take place along paths of minimal length within an optimal time frame. Alternatively, optimal evolutions may occur along established paths without any waste of energy resources and achieving 100% speed efficiency. Unfortunately, realistic physical scenarios often lead to less-than-ideal evolutions that demonstrate suboptimal efficiency, nonzero curvature, and a high level of complexity. In this paper, we provide an exact analytical expression for the curvature of a quantum evolution pertaining to a two-level quantum system subjected to various time-dependent magnetic fields. Specifically, we examine the dynamics produced by a two-parameter nonstationary Hermitian Hamiltonian with unit speed efficiency. To enhance our understanding of the physical implications of the curvature coefficient, we analyze the curvature behavior in relation to geodesic efficiency, speed efficiency, and the complexity of the quantum evolution (as described by the ratio of the difference between accessible and accessed Bloch-sphere volumes for the evolution from initial to final state to the accessible volume for the given quantum evolution). Our findings indicate that, generally, efficient quantum evolutions exhibit lower complexity compared to inefficient ones. However, we also note that complexity transcends mere length. In fact, longer paths that are sufficiently curved can demonstrate a complexity that is less than that of shorter paths with a lower curvature coefficient.


### JT de Sitter Gravity as a Model of Coleman-de Luccia Tunneling
**Authors**: Sidan A, Tom Banks

**Published Date**: 2025-06-10

**Updated Date**: 2026-01-15

**PDF Url**: [2506.09283v3](https://arxiv.org/pdf/2506.09283v3)

**Abstract**: We interpret the Euclidean solution of JT de Sitter gravity as the Coleman-de Luccia instanton for the decay of the low-entropy horizon of its static patch solution into either a Big Crunch or an infinite-entropy Lorentzian de Sitter cosmology. As in previous work by one of the authors, the Big Crunch is interpreted as bounding the entropy of the static state. The principle of detailed balance then guarantees it will transition back to a higher entropy causal diamond in the expanding cosmology. We then construct a family of explicit quantum mechanical models and appropriate metastable states, with transition probabilities well approximated by the semi-classical calculations in JT de Sitter gravity.


### Massless-Massive Amplitude Correspondence II: Constructive Massive Amplitudes in Standard Model
**Authors**: Yu-Han Ni, Chao Wu, Jiang-Hao Yu

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10622v1](https://arxiv.org/pdf/2601.10622v1)

**Abstract**: In the minimal helicity-chirality formalism, we systematically construct higher-point massive amplitudes from the fundamental building blocks: the contact three-point and four-point massive amplitudes. The inclusion of four-point contact amplitudes is essential to maintain gauge invariance in the spontaneously broken Standard Model. We construct all the standard model massive contact amplitudes and identify the physical light-cone gauge nature of massive amplitudes. Then only using the contact minimal helicity-chirality amplitudes at the leading order, we show both bootstrap techniques and on-shell recursion relations can be utilized to compute higher-point massive amplitudes. This provides a systematic framework for constructing various higher-point electroweak amplitudes, analogous to established on-shell methods for massless theories. Finally by deforming the gauge-invariant $n$-point amplitudes, we extend the massless-massive correspondence from three-and-four point contact amplitudes to general $n$-point factorized amplitudes.


### Localization with non-Hermitian off-diagonal disorder
**Authors**: Aitijhya Saha, Debraj Rakshit

**Published Date**: 2023-10-20

**Updated Date**: 2026-01-15

**PDF Url**: [2310.13744v5](https://arxiv.org/pdf/2310.13744v5)

**Abstract**: In this work, we discuss a non-Hermitian system described via a one-dimensional single-particle tight-binding model, where the non-Hermiticity is governed by random nearest-neighbour tunnellings, such that the left-to-right and right-to-left hopping strengths are unequal. A physical situation of completely real eigenspectrum arises owing to the Hamiltonian's tridiagonal matrix structure under a simple sign conservation of the product of the conjugate nearest-neighbour tunnelling terms. The off-diagonal disorder leads the non-Hermitian system to a delocalization-localization crossover in finite systems. The emergent nature of the crossover is recognized through a finite-size spectral analysis. The system enters into a localized phase for infinitesimal disorder strength in the thermodynamic limit. We perform a careful scaling analysis of localization length, inverse participation ratio (IPR), and energy splitting and report the corresponding scaling exponents. Noticeably, in contrast to the diagonal disorder, the density of states (DOS) has a singularity at E=0 in the presence of the off-diagonal disorder and the corresponding wavefunction remains delocalized for any given disorder strength.


### Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs
**Authors**: Zhiyuan Hu, Yucheng Wang, Yufei He, Jiaying Wu, Yilun Zhao, See-Kiong Ng, Cynthia Breazeal, Anh Tuan Luu, Hae Won Park, Bryan Hooi

**Published Date**: 2026-01-13

**Updated Date**: 2026-01-15

**PDF Url**: [2601.08763v2](https://arxiv.org/pdf/2601.08763v2)

**Abstract**: Reinforcement learning (RL) has become a central paradigm for post-training large language models (LLMs), particularly for complex reasoning tasks, yet it often suffers from exploration collapse: policies prematurely concentrate on a small set of dominant reasoning patterns, improving pass@1 while limiting rollout-level diversity and gains in pass@k. We argue that this failure stems from regularizing local token behavior rather than diversity over sets of solutions. To address this, we propose Uniqueness-Aware Reinforcement Learning, a rollout-level objective that explicitly rewards correct solutions that exhibit rare high-level strategies. Our method uses an LLM-based judge to cluster rollouts for the same problem according to their high-level solution strategies, ignoring superficial variations, and reweights policy advantages inversely with cluster size. As a result, correct but novel strategies receive higher rewards than redundant ones. Across mathematics, physics, and medical reasoning benchmarks, our approach consistently improves pass@$k$ across large sampling budgets and increases the area under the pass@$k$ curve (AUC@$K$) without sacrificing pass@1, while sustaining exploration and uncovering more diverse solution strategies at scale.


## Diffusion
### High-accuracy and dimension-free sampling with diffusions
**Authors**: Khashayar Gatmiry, Sitan Chen, Adil Salim

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10708v1](https://arxiv.org/pdf/2601.10708v1)

**Abstract**: Diffusion models have shown remarkable empirical success in sampling from rich multi-modal distributions. Their inference relies on numerically solving a certain differential equation. This differential equation cannot be solved in closed form, and its resolution via discretization typically requires many small iterations to produce \emph{high-quality} samples.
  More precisely, prior works have shown that the iteration complexity of discretization methods for diffusion models scales polynomially in the ambient dimension and the inverse accuracy $1/\varepsilon$. In this work, we propose a new solver for diffusion models relying on a subtle interplay between low-degree approximation and the collocation method (Lee, Song, Vempala 2018), and we prove that its iteration complexity scales \emph{polylogarithmically} in $1/\varepsilon$, yielding the first ``high-accuracy'' guarantee for a diffusion-based sampler that only uses (approximate) access to the scores of the data distribution. In addition, our bound does not depend explicitly on the ambient dimension; more precisely, the dimension affects the complexity of our solver through the \emph{effective radius} of the support of the target distribution only.


### Data-Driven Dynamic Factor Modeling via Manifold Learning
**Authors**: Graeme Baker, Agostino Capponi, J. Antonio Sidaoui

**Published Date**: 2025-06-24

**Updated Date**: 2026-01-15

**PDF Url**: [2506.19945v2](https://arxiv.org/pdf/2506.19945v2)

**Abstract**: We introduce a data-driven dynamic factor framework for modeling the joint evolution of high-dimensional covariates and responses without parametric assumptions. Standard factor models applied to covariates alone often lose explanatory power for responses. Our approach uses anisotropic diffusion maps, a manifold learning technique, to learn low-dimensional embeddings that preserve both the intrinsic geometry of the covariates and the predictive relationship with responses. For time series arising from Langevin diffusions in Euclidean space, we show that the associated graph Laplacian converges to the generator of the underlying diffusion. We further establish a bound on the approximation error between the diffusion map coordinates and linear diffusion processes, and we show that ergodic averages in the embedding space converge under standard spectral assumptions. These results justify using Kalman filtering in diffusion-map coordinates for predicting joint covariate-response evolution. We apply this methodology to equity-portfolio stress testing using macroeconomic and financial variables from Federal Reserve supervisory scenarios, achieving mean absolute error improvements of up to 55% over classical scenario analysis and 39% over principal component analysis benchmarks.


### Discrete Feynman-Kac Correctors
**Authors**: Mohsin Hasan, Viktor Ohanesian, Artem Gazizov, Yoshua Bengio, Alán Aspuru-Guzik, Roberto Bondesan, Marta Skreta, Kirill Neklyudov

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10403v1](https://arxiv.org/pdf/2601.10403v1)

**Abstract**: Discrete diffusion models have recently emerged as a promising alternative to the autoregressive approach for generating discrete sequences. Sample generation via gradual denoising or demasking processes allows them to capture hierarchical non-sequential interdependencies in the data. These custom processes, however, do not assume a flexible control over the distribution of generated samples. We propose Discrete Feynman-Kac Correctors, a framework that allows for controlling the generated distribution of discrete masked diffusion models at inference time. We derive Sequential Monte Carlo (SMC) algorithms that, given a trained discrete diffusion model, control the temperature of the sampled distribution (i.e. perform annealing), sample from the product of marginals of several diffusion processes (e.g. differently conditioned processes), and sample from the product of the marginal with an external reward function, producing likely samples from the target distribution that also have high reward. Notably, our framework does not require any training of additional models or fine-tuning of the original model. We illustrate the utility of our framework in several applications including: efficient sampling from the annealed Boltzmann distribution of the Ising model, improving the performance of language models for code generation and amortized learning, as well as reward-tilted protein sequence generation.


### Discrete Solution Operator Learning for Geometry-Dependent PDEs
**Authors**: Jinshuai Bai, Haolin Li, Zahra Sharif Khodaei, M. H. Aliabadi, YuanTong Gu, Xi-Qiao Feng

**Published Date**: 2026-01-14

**Updated Date**: 2026-01-15

**PDF Url**: [2601.09143v2](https://arxiv.org/pdf/2601.09143v2)

**Abstract**: Neural operator learning accelerates PDE solution by approximating operators as mappings between continuous function spaces. Yet in many engineering settings, varying geometry induces discrete structural changes, including topological changes, abrupt changes in boundary conditions or boundary types, and changes in the computational domain, which break the smooth-variation premise. Here we introduce Discrete Solution Operator Learning (DiSOL), a complementary paradigm that learns discrete solution procedures rather than continuous function-space operators. DiSOL factorizes the solver into learnable stages that mirror classical discretizations: local contribution encoding, multiscale assembly, and implicit solution reconstruction on an embedded grid, thereby preserving procedure-level consistency while adapting to geometry-dependent discrete structures. Across geometry-dependent Poisson, advection-diffusion, linear elasticity, as well as spatiotemporal heat conduction problems, DiSOL produces stable and accurate predictions under both in-distribution and strongly out-of-distribution geometries, including discontinuous boundaries and topological changes. These results highlight the need for procedural operator representations in geometry-dominated problems and position discrete solution operator learning as a distinct, complementary direction in scientific machine learning.


### Towards Efficient Low-rate Image Compression with Frequency-aware Diffusion Prior Refinement
**Authors**: Yichong Xia, Yimin Zhou, Jinpeng Wang, Bin Chen

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10373v1](https://arxiv.org/pdf/2601.10373v1)

**Abstract**: Recent advancements in diffusion-based generative priors have enabled visually plausible image compression at extremely low bit rates. However, existing approaches suffer from slow sampling processes and suboptimal bit allocation due to fragmented training paradigms. In this work, we propose Accelerate \textbf{Diff}usion-based Image Compression via \textbf{C}onsistency Prior \textbf{R}efinement (DiffCR), a novel compression framework for efficient and high-fidelity image reconstruction. At the heart of DiffCR is a Frequency-aware Skip Estimation (FaSE) module that refines the $ε$-prediction prior from a pre-trained latent diffusion model and aligns it with compressed latents at different timesteps via Frequency Decoupling Attention (FDA). Furthermore, a lightweight consistency estimator enables fast \textbf{two-step decoding} by preserving the semantic trajectory of diffusion sampling. Without updating the backbone diffusion model, DiffCR achieves substantial bitrate savings (27.2\% BD-rate (LPIPS) and 65.1\% BD-rate (PSNR)) and over $10\times$ speed-up compared to SOTA diffusion-based compression baselines.


## Quantitative Finance
### ProbFM: Probabilistic Time Series Foundation Model with Uncertainty Decomposition
**Authors**: Arundeep Chinta, Lucas Vinh Tran, Jay Katukuri

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10591v1](https://arxiv.org/pdf/2601.10591v1)

**Abstract**: Time Series Foundation Models (TSFMs) have emerged as a promising approach for zero-shot financial forecasting, demonstrating strong transferability and data efficiency gains. However, their adoption in financial applications is hindered by fundamental limitations in uncertainty quantification: current approaches either rely on restrictive distributional assumptions, conflate different sources of uncertainty, or lack principled calibration mechanisms. While recent TSFMs employ sophisticated techniques such as mixture models, Student's t-distributions, or conformal prediction, they fail to address the core challenge of providing theoretically-grounded uncertainty decomposition. For the very first time, we present a novel transformer-based probabilistic framework, ProbFM (probabilistic foundation model), that leverages Deep Evidential Regression (DER) to provide principled uncertainty quantification with explicit epistemic-aleatoric decomposition. Unlike existing approaches that pre-specify distributional forms or require sampling-based inference, ProbFM learns optimal uncertainty representations through higher-order evidence learning while maintaining single-pass computational efficiency. To rigorously evaluate the core DER uncertainty quantification approach independent of architectural complexity, we conduct an extensive controlled comparison study using a consistent LSTM architecture across five probabilistic methods: DER, Gaussian NLL, Student's-t NLL, Quantile Loss, and Conformal Prediction. Evaluation on cryptocurrency return forecasting demonstrates that DER maintains competitive forecasting accuracy while providing explicit epistemic-aleatoric uncertainty decomposition. This work establishes both an extensible framework for principled uncertainty quantification in foundation models and empirical evidence for DER's effectiveness in financial applications.


### History Is Not Enough: An Adaptive Dataflow System for Financial Time-Series Synthesis
**Authors**: Haochong Xia, Yao Long Teng, Regan Tan, Molei Qin, Xinrun Wang, Bo An

**Published Date**: 2026-01-15

**Updated Date**: 2026-01-15

**PDF Url**: [2601.10143v1](https://arxiv.org/pdf/2601.10143v1)

**Abstract**: In quantitative finance, the gap between training and real-world performance-driven by concept drift and distributional non-stationarity-remains a critical obstacle for building reliable data-driven systems. Models trained on static historical data often overfit, resulting in poor generalization in dynamic markets. The mantra "History Is Not Enough" underscores the need for adaptive data generation that learns to evolve with the market rather than relying solely on past observations. We present a drift-aware dataflow system that integrates machine learning-based adaptive control into the data curation process. The system couples a parameterized data manipulation module comprising single-stock transformations, multi-stock mix-ups, and curation operations, with an adaptive planner-scheduler that employs gradient-based bi-level optimization to control the system. This design unifies data augmentation, curriculum learning, and data workflow management under a single differentiable framework, enabling provenance-aware replay and continuous data quality monitoring. Extensive experiments on forecasting and reinforcement learning trading tasks demonstrate that our framework enhances model robustness and improves risk-adjusted returns. The system provides a generalizable approach to adaptive data management and learning-guided workflow automation for financial data.


