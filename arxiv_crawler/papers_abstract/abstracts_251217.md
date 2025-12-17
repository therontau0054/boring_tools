# Abstracts of Papers

## Physics
### Native and Compact Structured Latents for 3D Generation
**Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14692v1](https://arxiv.org/pdf/2512.14692v1)

**Abstract**: Recent advancements in 3D generative modeling have significantly improved the generation realism, yet the field is still hampered by existing representations, which struggle to capture assets with complex topologies and detailed appearance. This paper present an approach for learning a structured latent representation from native 3D data to address this challenge. At its core is a new sparse voxel structure called O-Voxel, an omni-voxel representation that encodes both geometry and appearance. O-Voxel can robustly model arbitrary topology, including open, non-manifold, and fully-enclosed surfaces, while capturing comprehensive surface attributes beyond texture color, such as physically-based rendering parameters. Based on O-Voxel, we design a Sparse Compression VAE which provides a high spatial compression rate and a compact latent space. We train large-scale flow-matching models comprising 4B parameters for 3D generation using diverse public 3D asset datasets. Despite their scale, inference remains highly efficient. Meanwhile, the geometry and material quality of our generated assets far exceed those of existing models. We believe our approach offers a significant advancement in 3D generative modeling.


### Drell-Yan at the Electron-Ion Collider
**Authors**: Henry T. Klest

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14690v1](https://arxiv.org/pdf/2512.14690v1)

**Abstract**: The photon is arguably the most universally important particle across all fields of physics. Despite its status as a fundamental particle, at high energies the photon can be seen as a hadronic source of partons. The partonic content of the photon is very poorly constrained compared to that of the proton, with photon PDF uncertainties typically one or two orders of magnitude larger than their proton counterparts, despite the fact that its source, the $γ\to q\bar{q}$ splitting, is perturbatively calculable. The high luminosity, excellent particle identification, and far-backward electron tagging capabilities of the Electron-Ion Collider make it an ideal environment for studying photon parton distribution functions. Similar to the $p+p$ or $π+p$ systems, photoproduction at the EIC can be thought of as two parton distributions colliding. One of the most powerful processes in such collisions is production of lepton pairs, i.e. $h+p\rightarrow l^+l^-+X$, known as the Drell--Yan process. This process has the ability to access for the first time the transverse-momentum-dependent parton distributions of the photon. The transversely polarized proton beam of the EIC additionally provides a possible means of accessing the transversity distribution of the proton without relying on fragmentation functions.


### A Physical Basis for Information
**Authors**: Wouter van der Wijngaart

**Published Date**: 2024-07-06

**Updated Date**: 2025-12-16

**PDF Url**: [2407.09567v6](https://arxiv.org/pdf/2407.09567v6)

**Abstract**: What is information, physically, and why does it so reliably emerge in living, cultural, and technological systems? Existing theories quantify uncertainty, cost, or compressibility, but do not identify which physical structures count as information or how informational entities arise from dynamics. Here we introduce a causal-physical framework that defines information as a heritable causal role played by persistent (metastable) structures in a dynamical system. We represent long-lived structures as almost-invariant sets and assemble them into causal structure sets that encode how such structures generate, transform, and maintain one another. Within this representation, informational entities are singled out by three generative motifs: replication, heritable variation, and translation under shared templates, which together define when a collection of structures constitutes an information family. We demonstrate the full pipeline by mapping a concrete cultural episode (fruit-salad recipe sharing and modification) into a causal structure set, and show how the motifs and information families can then be identified algorithmically. The framework yields computable quantities, including informational fitness and informational entropy, directly from causal structure, enabling informational variants to be detected, compared, and tracked across biological, cultural, engineered, and digital domains. Finally, motivated by analogies to random directed graphs and catalytic networks, we propose testable conditions under which hereditary informational motifs become statistically generic in sufficiently large causal-physical systems.


### WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields
**Authors**: Gabriele Accarino, Viviana Acquaviva, Sara Shamekh, Duncan Watson-Parris, David Lawrence

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14656v1](https://arxiv.org/pdf/2512.14656v1)

**Abstract**: We introduce WaveSim, a multi-scale similarity metric for the evaluation of spatial fields in weather and climate applications. WaveSim exploits wavelet transforms to decompose input fields into scale-specific wavelet coefficients. The metric is built by multiplying three orthogonal components derived from these coefficients: Magnitude, which quantifies similarities in the energy distribution of the coefficients, i.e., the intensity of the field; Displacement, which captures spatial shift by comparing the centers of mass of normalized energy distributions; and Structure, which assesses pattern organization independent of location and amplitude. Each component yields a scale-specific similarity score ranging from 0 (no similarity) to 1 (perfect similarity), which are then combined across scales to produce an overall similarity measure. We first evaluate WaveSim using synthetic test cases, applying controlled spatial and temporal perturbations to systematically assess its sensitivity and expected behavior. We then demonstrate its applicability to physically relevant case studies of key modes of climate variability in Earth System Models. Traditional point-wise metrics lack a mechanism for attributing errors to physical scales or modes of dissimilarity. By operating in the wavelet domain and decomposing the signal along independent axes, WaveSim bypasses these limitations and provides an interpretable and diagnostically rich framework for assessing similarity in complex fields. Additionally, the WaveSim framework allows users to place emphasis on a specific scale or component, and lends itself to user-specific model intercomparison, model evaluation, and calibration and training of forecasting systems. We provide a PyTorch-ready implementation of WaveSim, along with all evaluation scripts, at: https://github.com/gabrieleaccarino/wavesim.


### Axial Symmetric Navier Stokes Equations and the Beltrami /anti Beltrami spectrum in view of Physics Informed Neural Networks
**Authors**: Pietro Fré

**Published Date**: 2025-12-09

**Updated Date**: 2025-12-16

**PDF Url**: [2512.08846v2](https://arxiv.org/pdf/2512.08846v2)

**Abstract**: In this paper, I further continue an investigation on Beltrami Flows began in 2015 with A. Sorin and amply revised and developed in 2022 with M. Trigiante. Instead of a compact $3$-torus $T^3=\mathbb{R}^3/Λ$ where $Λ$ is a crystallographic lattice, as done in previous work, here I considered flows confined in a cylinder with identified opposite bases. In this topology I considered axial symmetric flows and found a complete basis of axial symmetric harmonic $1$-forms that, for each energy level, decomposes into six components: two Beltrami, two anti-Beltrami and two closed forms. These objects, that are written in terms of trigonometric and Bessel functions, constitute a function basis for an $L^2$ space of axial symmetric flows. I have presented a general scheme for the search of axial symmetric solutions of Navier Stokes equation by reducing the latter to an hierachy of quadratic relations on the development coefficients of the flow in the above described functional basis. It is proposed that the coefficients can be determined by means of a Physics Informed like Neural Network optimization recursive algorithm. Indeed the present paper provides the theoretical foundations for such a algorithmic construction that is planned for a future publication.


### Electrodrying in nanopores: from fundamentals to iontronic and memristive applications
**Authors**: Giovanni Di Muccio, Gonçalo Paulo, Lorenzo Iannetti, Adina Sauciuc, Giovanni Maglia, Alberto Giacomello

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14631v1](https://arxiv.org/pdf/2512.14631v1)

**Abstract**: Iontronics is a burgeoning paradigm that employs ions in solution as information carriers for sensing and computing, e.g., in neuromorphic devices. The fundamentally different working principle as compared to electronics requires novel approaches and concepts to control the impedance of nanoscale fluidic circuit elements, such as nanopores. For instance, previous research has focused on voltage-induced pore wetting as a means to trigger conduction in nanopores. The present study explores the opposite counter-intuitive mechanism: using voltage to dry hydrophobic nanopores and, therefore, to turn off conduction. This "electrodrying" concept affords exquisite, bidirectional control over the conductance of nanopores additionally showing hysteresis in the current-voltage curve that is the fingerprint of memristors. Using an analytical model and free-energy molecular dynamics simulations, we explain the physical mechanism underlying electrodrying and provide clear design criteria for solid-state and biological nanopores with bidirectional control over conductance. The electrical behaviour of electrodrying nanopores shows two unique features: i) the hysteresis loop is shifted from the origin, accounting for the fifth, previously unreported memristor type and ii) negative differential resistance is observed over a broad voltage range in which the non-conductive state is favoured by electrodrying. These properties are demonstrated in a short-term memory task and in an iontronic oscillator circuit to showcase their potential in neuromorphic applications and iontronic devices. Finally, we validate our predictions through experiments on engineered dipolar hydrophobic CytK nanopores, whose voltage-dependent conductance substantiates the electrodrying concept.


### Towards a worldsheet theory of entanglement entropy
**Authors**: Houwen Wu, Shuxuan Ying

**Published Date**: 2025-11-20

**Updated Date**: 2025-12-16

**PDF Url**: [2511.16586v2](https://arxiv.org/pdf/2511.16586v2)

**Abstract**: We propose a new action for entanglement entropy in the framework of the AdS$_{3}$/CFT$_{2}$ correspondence. This action is constructed directly from the entanglement entropy of the CFT$_{2}$, and we show that the Einstein equations of AdS$_{3}$ gravity can be derived from it. In the near-coincidence limit, using Riemann normal coordinates, the action reduces to a string worldsheet action in a curved background that naturally includes the symmetric spacetime metric, an antisymmetric Kalb-Ramond field, and a dilaton. The Kalb-Ramond field gives rise to a string charge density, from which we demonstrate that bit threads can be exactly reproduced. This correspondence provides a clear physical interpretation of bit threads. Exploiting this correspondence, we establish explicit relations between the emergent string worldsheet and the Ryu-Takayanagi (RT) surface, providing new insights into entanglement entropy. In particular, entanglement entropy can be computed from open string charge, while Bekenstein-Hawking entropy arises from closed string charge through open-closed string duality. These results suggest a unified picture in which the Susskind-Uglum conjecture, open-closed string duality, and the ER=EPR proposal emerge as equivalent manifestations of the same underlying principle. Finally, we propose a quantization of the RT surface, pointing to a possible connection with loop quantum gravity that refines Wall's conjecture.


### Geometric calculations on probability manifolds from reciprocal relations in Master equations
**Authors**: Wuchen Li

**Published Date**: 2025-04-27

**Updated Date**: 2025-12-16

**PDF Url**: [2504.19368v3](https://arxiv.org/pdf/2504.19368v3)

**Abstract**: Onsager reciprocal relations model physical irreversible processes from complex systems. Recently, it has been shown that Onsager principles for master equations on finite states introduce a class of Riemannian metrics in a probability simplex, named probability manifolds. We call these manifolds finite-state generalized Wasserstein-$2$ spaces. In this paper, we study geometric calculations on probability manifolds, in which we derive the Levi-Civita connection, gradient, Hessian, and parallel transport, and compute the Riemannian and sectional curvatures. We present two examples of geometric quantities in probability manifolds. These include Levi-Civita connections from the chemical monomolecular triangle reaction and sectional, Ricci, and scalar curvatures in Wasserstein space on a three-point lattice.


### Self-adaptive physics-informed neural network for forward and inverse problems in heterogeneous porous flow
**Authors**: Md. Abdul Aziz, Thilo Strauss, Muhammad Mohebujjaman, Taufiquar Khan

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14610v1](https://arxiv.org/pdf/2512.14610v1)

**Abstract**: We develop a self-adaptive physics-informed neural network (PINN) framework that reliably solves forward Darcy flow and performs accurate permeability inversion in heterogeneous porous media. In the forward setting, the PINN predicts velocity and pressure for discontinuous, piecewise-constant permeability; in the inverse setting, it identifies spatially varying permeability directly from indirect flow observations. Both models use a region-aware permeability parameterization with binary spatial masks, which preserves sharp permeability jumps and avoids the smoothing artifacts common in standard PINNs. To stabilize training, we introduce self-learned loss weights that automatically balance PDE residuals, boundary constraints, and data mismatch, eliminating manual tuning and improving robustness, particularly for inverse problems. An interleaved AdamW-L-BFGS optimization strategy further accelerates and stabilizes convergence. Numerical results demonstrate accurate forward surrogates and reliable inverse permeability recovery, establishing the method as an effective mesh-free solver and data-driven inversion tool for porous-media systems governed by partial differential equations.


### Generalization performance of narrow one-hidden layer networks in the teacher-student setting
**Authors**: Jean Barbier, Federica Gerace, Alessandro Ingrosso, Clarissa Lauditi, Enrico M. Malatesta, Gibbs Nwemadji, Rodrigo Pérez Ortiz

**Published Date**: 2025-07-01

**Updated Date**: 2025-12-16

**PDF Url**: [2507.00629v3](https://arxiv.org/pdf/2507.00629v3)

**Abstract**: Understanding the generalization abilities of neural networks for simple input-output distributions is crucial to account for their learning performance on real datasets. The classical teacher-student setting, where a network is trained from data obtained thanks to a label-generating teacher model, serves as a perfect theoretical test bed. In this context, a complete theoretical account of the performance of fully connected one-hidden layer networks in the presence of generic activation functions is lacking. In this work, we develop such a general theory for narrow networks, i.e. with a large number of hidden units, yet much smaller than the input dimension. Using methods from statistical physics, we provide closed-form expressions for the typical performance of both finite temperature (Bayesian) and empirical risk minimization estimators, in terms of a small number of summary statistics. In doing so, we highlight the presence of a transition where hidden neurons specialize when the number of samples is sufficiently large and proportional to the number of parameters of the network. Our theory accurately predicts the generalization error of neural networks trained on regression or classification tasks with either noisy full-batch gradient descent (Langevin dynamics) or full-batch gradient descent.


## Diffusion
### Understanding Sampler Stochasticity in Training Diffusion Models for RLHF
**Authors**: Jiayuan Sheng, Hanyang Zhao, Haoxian Chen, David D. Yao, Wenpin Tang

**Published Date**: 2025-10-12

**Updated Date**: 2025-12-16

**PDF Url**: [2510.10767v2](https://arxiv.org/pdf/2510.10767v2)

**Abstract**: Reinforcement Learning from Human Feedback (RLHF) is increasingly used to fine-tune diffusion models, but a key challenge arises from the mismatch between stochastic samplers used during training and deterministic samplers used during inference. In practice, models are fine-tuned using stochastic SDE samplers to encourage exploration, while inference typically relies on deterministic ODE samplers for efficiency and stability. This discrepancy induces a reward gap, raising concerns about whether high-quality outputs can be expected during inference. In this paper, we theoretically characterize this reward gap and provide non-vacuous bounds for general diffusion models, along with sharper convergence rates for Variance Exploding (VE) and Variance Preserving (VP) Gaussian models. Methodologically, we adopt the generalized denoising diffusion implicit models (gDDIM) framework to support arbitrarily high levels of stochasticity, preserving data marginals throughout. Empirically, our findings through large-scale experiments on text-to-image models using denoising diffusion policy optimization (DDPO) and mixed group relative policy optimization (MixGRPO) validate that reward gaps consistently narrow over training, and ODE sampling quality improves when models are updated using higher-stochasticity SDE training.


### Dual Language Models: Balancing Training Efficiency and Overfitting Resilience
**Authors**: David Samuel, Lucas Georges Gabriel Charpentier

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14549v1](https://arxiv.org/pdf/2512.14549v1)

**Abstract**: This paper combines autoregressive and masked-diffusion training objectives without any architectural modifications, resulting in flexible language models that outperform single-objective models. Autoregressive modeling has been a popular approach, partly because of its training efficiency; however, that comes at the cost of sensitivity to overfitting. On the other hand, masked-diffusion models are less efficient to train while being more resilient to overfitting. In this work, we demonstrate that dual-objective training achieves the best of both worlds. To derive the optimal ratio between both objectives, we train and evaluate 50 language models under varying levels of data repetition. We show that it is optimal to combine both objectives under all evaluated settings and that the optimal ratio is similar whether targeting autoregressive or masked-diffusion downstream performance.


### Massive Editing for Large Language Models Based on Dynamic Weight Generation
**Authors**: Wentao Wan, Qiqing Lao, Zhiwei Xie, Hefeng Wu, Runnan Lin, Liang Lin, Keze Wang

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14395v1](https://arxiv.org/pdf/2512.14395v1)

**Abstract**: Knowledge Editing (KE) is a field that studies how to modify some knowledge in Large Language Models (LLMs) at a low cost (compared to pre-training). Currently, performing large-scale edits on LLMs while ensuring the Reliability, Generality, and Locality metrics of the edits remain a challenge. This paper proposes a Massive editing approach for LLMs based on dynamic weight Generation (MeG). Our MeG involves attaching a dynamic weight neuron to specific layers of the LLMs and using a diffusion model to conditionally generate the weights of this neuron based on the input query required for the knowledge. This allows the use of adding a single dynamic weight neuron to achieve the goal of large-scale knowledge editing. Experiments show that our MeG can significantly improve the performance of large-scale KE in terms of Reliability, Generality, and Locality metrics compared to existing knowledge editing methods, particularly with a high percentage point increase in the absolute value index for the Locality metric, demonstrating the advantages of our proposed method.


### High Volume Rate 3D Ultrasound Reconstruction with Diffusion Models
**Authors**: Tristan S. W. Stevens, Oisín Nolan, Oudom Somphone, Jean-Luc Robert, Ruud J. G. van Sloun

**Published Date**: 2025-05-28

**Updated Date**: 2025-12-16

**PDF Url**: [2505.22090v2](https://arxiv.org/pdf/2505.22090v2)

**Abstract**: Three-dimensional ultrasound enables real-time volumetric visualization of anatomical structures. Unlike traditional 2D ultrasound, 3D imaging reduces reliance on precise probe orientation, potentially making ultrasound more accessible to clinicians with varying levels of experience and improving automated measurements and post-exam analysis. However, achieving both high volume rates and high image quality remains a significant challenge. While 3D diverging waves can provide high volume rates, they suffer from limited tissue harmonic generation and increased multipath effects, which degrade image quality. One compromise is to retain focus in elevation while leveraging unfocused diverging waves in the lateral direction to reduce the number of transmissions per elevation plane. Reaching the volume rates achieved by full 3D diverging waves, however, requires dramatically undersampling the number of elevation planes. Subsequently, to render the full volume, simple interpolation techniques are applied. This paper introduces a novel approach to 3D ultrasound reconstruction from a reduced set of elevation planes by employing diffusion models (DMs) to achieve increased spatial and temporal resolution. We compare both traditional and supervised deep learning-based interpolation methods on a 3D cardiac ultrasound dataset. Our results show that DM-based reconstruction consistently outperforms the baselines in image quality and downstream task performance. Additionally, we accelerate inference by leveraging the temporal consistency inherent to ultrasound sequences. Finally, we explore the robustness of the proposed method by exploiting the probabilistic nature of diffusion posterior sampling to quantify reconstruction uncertainty and demonstrate improved recall on out-of-distribution data with synthetic anomalies under strong subsampling.


### Towards Transferable Defense Against Malicious Image Edits
**Authors**: Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen

**Published Date**: 2025-12-16

**Updated Date**: 2025-12-16

**PDF Url**: [2512.14341v1](https://arxiv.org/pdf/2512.14341v1)

**Abstract**: Recent approaches employing imperceptible perturbations in input images have demonstrated promising potential to counter malicious manipulations in diffusion-based image editing systems. However, existing methods suffer from limited transferability in cross-model evaluations. To address this, we propose Transferable Defense Against Malicious Image Edits (TDAE), a novel bimodal framework that enhances image immunity against malicious edits through coordinated image-text optimization. Specifically, at the visual defense level, we introduce FlatGrad Defense Mechanism (FDM), which incorporates gradient regularization into the adversarial objective. By explicitly steering the perturbations toward flat minima, FDM amplifies immune robustness against unseen editing models. For textual enhancement protection, we propose an adversarial optimization paradigm named Dynamic Prompt Defense (DPD), which periodically refines text embeddings to align the editing outcomes of immunized images with those of the original images, then updates the images under optimized embeddings. Through iterative adversarial updates to diverse embeddings, DPD enforces the generation of immunized images that seek a broader set of immunity-enhancing features, thereby achieving cross-model transferability. Extensive experimental results demonstrate that our TDAE achieves state-of-the-art performance in mitigating malicious edits under both intra- and cross-model evaluations.


## Quantitative Finance
### A stochastic volatility approximation for a tick-by-tick price model with mean-field interaction
**Authors**: Paolo Dai Pra, Paolo Pigato

**Published Date**: 2025-04-04

**Updated Date**: 2025-12-16

**PDF Url**: [2504.03445v2](https://arxiv.org/pdf/2504.03445v2)

**Abstract**: We consider a tick-by-tick model of price formation, in which buy and sell orders are modeled as self-exciting point processes (Hawkes process), similar to the one in [Hoffmann, Bacry, Delattre, Muzy, Modelling microstructure noise with mutually exciting point processes, Quantitative Finance, 2013] and [El Euch, Fukasawa, Rosenbaum, The microstructural foundations of leverage effect and rough volatility, Finance and Stochastics, 2018]. We adopt an agent based approach by studying the aggregation of a large number of these point processes, mutually interacting in a mean-field sense.
  The financial interpretation is that of an asset on which several labeled agents place buy and sell orders following these point processes, influencing the price. The mean-field interaction introduces positive correlations between order volumes coming from different agents that reflect features of real markets such as herd behavior and contagion. When the large scale limit of the aggregated asset price is computed, if parameters are set to a critical value, a singular phenomenon occurs: the aggregated model converges to a stochastic volatility model with leverage effect and faster-than-linear mean reversion of the volatility process.
  The faster-than-linear mean reversion of the volatility process is supported by econometric evidence, and we have linked it in [Dai Pra, Pigato, Multi-scaling of moments in stochastic volatility models, Stochastic Processes and their Applications, 2015] to the observed multifractal behavior of assets prices and market indices. This seems connected to the Statistical Physics perspective that expects anomalous scaling properties to arise in the critical regime.


### Interpretable Hypothesis-Driven Trading:A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals
**Authors**: Gagan Deep, Akash Deep, William Lamptey

**Published Date**: 2025-12-15

**Updated Date**: 2025-12-15

**PDF Url**: [2512.12924v1](https://arxiv.org/pdf/2512.12924v1)

**Abstract**: We develop a rigorous walk-forward validation framework for algorithmic trading designed to mitigate overfitting and lookahead bias. Our methodology combines interpretable hypothesis-driven signal generation with reinforcement learning and strict out-of-sample testing. The framework enforces strict information set discipline, employs rolling window validation across 34 independent test periods, maintains complete interpretability through natural language hypothesis explanations, and incorporates realistic transaction costs and position constraints. Validating five market microstructure patterns across 100 US equities from 2015 to 2024, the system yields modest annualized returns (0.55%, Sharpe ratio 0.33) with exceptional downside protection (maximum drawdown -2.76%) and market-neutral characteristics (beta = 0.058). Performance exhibits strong regime dependence, generating positive returns during high-volatility periods (0.60% quarterly, 2020-2024) while underperforming in stable markets (-0.16%, 2015-2019). We report statistically insignificant aggregate results (p-value 0.34) to demonstrate a reproducible, honest validation protocol that prioritizes interpretability and extends naturally to advanced hypothesis generators, including large language models. The key empirical finding reveals that daily OHLCV-based microstructure signals require elevated information arrival and trading activity to function effectively. The framework provides complete mathematical specifications and open-source implementation, establishing a template for rigorous trading system evaluation that addresses the reproducibility crisis in quantitative finance research. For researchers, practitioners, and regulators, this work demonstrates that interpretable algorithmic trading strategies can be rigorously validated without sacrificing transparency or regulatory compliance.


