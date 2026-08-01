# Abstracts of Papers

## World Model
### KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models
**Authors**: Sparsh Roy, Samuel Girmachew, Nishita Chavan

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28608v1](https://arxiv.org/pdf/2607.28608v1)

**Abstract**: Clinical risk models routinely achieve strong aggregate performance while producing materially different error rates across patient subgroups. Audit pipelines have been proposed to catch this, but their components are rarely stress-tested, so it is unclear which parts of an audit can be trusted and under what conditions. We present KAISEN, a five-phase audit pipeline covering subgroup stratification, disparity measurement, mechanism diagnostics, post-hoc mitigation, and drift monitoring, evaluated to the point of failure on a synthetic benchmark of 16 disease tasks, 15 social-determinant axes from Healthy People 2030, and three prespecified intersections. Four findings follow. (i) Significance tracks each axis's gap against its own minimum detectable effect: rank correlation between significance count and raw equalized-odds difference (EOD) across the 15 axes is rho = 0.56, rising to rho = 0.78 once EOD is standardized by that floor. (ii) Per-group threshold optimization reduces EOD in 48 of 48 held-out runs (paired delta = -0.285, 95% CI [-0.313, -0.252]), while group-wise Platt scaling -- the better calibrator -- behaves as a coin flip on EOD (19 of 48 runs improved, 95% CI [0.26, 0.55]) with mean effect near zero, so what an audit should report is the variance, not the average. (iii) The mechanism diagnostic classifies 144 of 144 controlled cases correctly but recovers none of 48 model-driven cases under proxy misspecification, with no signal that it failed. (iv) CUSUM failures and false alarms track cohort realization far more than disease: at the reference threshold, all 27 false alarms and 7 of 8 missed shifts come from different seeds (chi-squared p = 0.002), so a threshold tuned on one cohort fails to transfer. All results are synthetic with known ground truth and do not establish clinical validity. Code, artifacts, and scripts reproducing every number are released.


### Laboratory demonstration of low order wavefront control using light reflected off the vortex coronagraph
**Authors**: Clarissa R. Do Ó, Kane Sjoberg, Luke Lamitina, Susan Redmond, Dimitri Mawet, Jorge Llop-Sayson, Siria Alicata

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28603v1](https://arxiv.org/pdf/2607.28603v1)

**Abstract**: The Astro2020 Decadal Survey identified exoplanet imaging as a high priority for the Habitable Worlds Observatory (HWO), which must image and characterize exo-Earths at contrasts of $1\times10^{-10}$. The vector vortex coronagraph (VVC) is a leading architecture for this task owing to its small inner working angle and high throughput. Using light reflected from the VVC for wavefront sensing and control provides a potential path to improving robustness to residual wavefront errors and minimizing contrast degradation. Here we present the first laboratory demonstration of a low order wavefront sensing and control (LOWFS) tip-tilt loop operating on light reflected from a VVC, carried out on the High Contrast and Spectroscopy Testbed (HCST) at Caltech's Exoplanet Technology Laboratory. The demonstration is enabled by HCST's upgrade to CATKit2, a service-oriented framework in which we implement phase retrieval, electric field conjugation (EFC), and the LOWFS loop as concurrent routines. Our phase retrieval reduces the science camera wavefront error from 71.6 to 7.9 nm RMS, a $>$9$\times$ improvement. Over a 12 hour open loop run, we find that PSF drift is strongly correlated with bench temperature ($r>0.88$). Closing the tip-tilt loop suppresses drift below 1 Hz by more than two orders of magnitude and holds pointing to $<0.005~λ/D$. Run concurrently with EFC, the closed loop maintains a dark hole contrast of $\sim$5$\times10^{-8}$ over one hour, whereas in open loop a drift of $\sim$0.2--0.4 $λ/D$ degrades contrast by more than an order of magnitude. These results establish reflected light sensing off a VVC as a viable foundation for future wavefront control architectures in high contrast coronagraphy.


### Using Theory of Mind to Arbitrate between Social and Non-social Learning
**Authors**: Lance Ying, Ryan Truong, Joshua B. Tenenbaum, Samuel J. Gershman

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28601v1](https://arxiv.org/pdf/2607.28601v1)

**Abstract**: Social learning is a powerful mechanism through which agents learn about the world from others. However, humans sometimes choose direct experience over social learning, which can carry time and cognitive resource costs. How do people balance social and non-social learning? We propose a Rational Mentalizing model of the decision to engage in social learning. This model estimates the utility of social learning by reasoning about another agent's goal and the informativeness of their future actions. It then weighs the utility of social learning against the utility of non-social learning. Using a novel game where players choose between observing other agents or exploring the environment, we show that the Rational Mentalizing model can quantitatively capture human trade-offs between these strategies. These findings suggest that selective social learning is guided by 'Theory of Mind' in the service of utility maximization.


### ROAD: Reciprocal-Objective Alignment of Discriminative Semantics for 3D Shape Generation
**Authors**: Xiao Luo, Mingyang Du, Xin Zhou, Tianrui Feng, Xiwu Chen, Xiaofan Li, Jiangning Zhang, Dingkang Liang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28581v1](https://arxiv.org/pdf/2607.28581v1)

**Abstract**: High-fidelity 3D generation predominantly relies on scaling model capacity and data, which incurs prohibitive computational costs. This paradigm typically requires learning geometry from scratch and overlooks the rich semantic and structural priors already encapsulated in discriminative 3D foundation models. We contend that leveraging the profound understanding of the 3D world possessed by these discriminative models can significantly reduce generative cost. To this end, we propose ROAD, a framework that reduces the training cost of 3D generation by transferring these rich discriminative priors into diffusion transformers. To address the inherent semantic-structural heterogeneity between generative and discriminative latents, we introduce a reciprocal-objective alignment strategy. This method synergizes Holistic Semantic Condensing to enforce global semantic coherence and Structural Optimal Alignment, which is formulated as a bipartite matching problem to rigorously align microscopic geometric details between disparate latent spaces. The 3D foundation model is only used for training-time supervision of alignment and is not used at inference, incurring no additional inference cost. Compared with the industrial baseline Step1X-3D, the proposed ROAD achieves highly competitive generation performance with only 1.5% of the training data and significantly reduces training costs, effectively reducing the computational overhead of high-fidelity 3D generation. Code is available at https://github.com/H-EmbodVis/ROAD.


### Benchmarking Quantum Simulations of the Lipkin-Meshkov-Glick Model Using Large Tensor Networks
**Authors**: Maggie Bao, Rushil Dandamudi, Jerimiah Wright, Joan Étude Arrow, Henry Zou, Vardaan Sahgal, Brian J. McDermott

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28570v1](https://arxiv.org/pdf/2607.28570v1)

**Abstract**: As quantum computing matures, it is critical to benchmark its real-world problem solving performance against competitive classical methods, such as tensor networks. In this work, we leverage the Density Matrix Renormalization Group (DMRG) algorithm to compute ground state energies of the Lipkin Meshkov Glick (LMG) model as a comparative benchmark against popular noisy intermediate-scale (NISQ) algorithms like the Variational Quantum Eigensolver (VQE) and Sample-Based Quantum Diagonalization (SQD) method. By running DMRG on the NERSC Perlmutter supercomputer, we provide one of the largest LMG ground state energy datasets in literature, containing accurate ground state energies for systems up to 1400 particles. We compare these results with VQE and SQD implementations on an IBM Eagle quantum computer for comparison. VQE achieved results within 1 percent error for 6 particles, while exceeding that threshold for all other values while SQD extended that range to 17 particles, suggesting that in a noisy intermediate scale quantum era, subspace-based approaches may strike the best balance between accuracy, circuit depth, and noise resilience.


### X-NavDP: Generalizing Navigation Diffusion Policy to Novel Behavior and Embodiments with Group Q-score Reweighted Matching
**Authors**: Tianyu Yang, Yiming Zeng, Wenzhe Cai, Yuqiang Yang, Jiaqi Peng, Hui Cheng, Jiangmiao Pang, Tai Wang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28560v1](https://arxiv.org/pdf/2607.28560v1)

**Abstract**: Pretraining navigation diffusion policies rely on large-scale expert demonstrations. These data are typically generated by a fully-informed oracle planner suited to a single nominal robot. This limits the policy's generalization to diverse embodiments and challenging scenarios (e.g., escaping dead ends or detouring long obstacles) that demand diverse local reactive behaviors with only onboard local observations. Post-training the policy with reinforcement learning (RL) offers a principled remedy. However, previous RL for diffusion approaches lead to only marginal improvements. This is because the intractable likelihood of diffusion policies renders policy gradients unstable in addition to inefficient policy exploration. To address these challenges, we propose a data-efficient diffusion RL post-training framework - GQRM (Group Q-score Reweighted Matching). Our framework introduces two complementary designs: (i) a self-bootstrapped exploration strategy with behavior perturbation that preserves the pretrained policy prior, and (ii) a group Q-score normalization mechanism that computes per-trajectory values on each state for efficient reweighted score matching. By conducting distributed online RL training across heterogeneous embodiments, the resulting fine-tuned policy, X-NavDP, achieves state-of-the-art cross-embodiment visual navigation performance, improving the overall success rate from 61.20% to 84.28% in simulation and 10% to 65% in real-world hard cases. The code and model are publicly available at https://yty-sky.github.io/x-navdp-project-page.


## Generation
### ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature Programs
**Authors**: Ruman Wang, Hangting Ye

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28538v1](https://arxiv.org/pdf/2607.28538v1)

**Abstract**: Classifying pathological scars from clinical photographs requires distinguishing keloids from hypertrophic scars despite limited expert-labeled data and substantial acquisition variation across hospitals. End-to-end image models remain data-dependent, whereas sending photographs to a hosted vision-language model (VLM) may conflict with local data-governance requirements and yields decisions that are difficult to reproduce and audit. We introduce ScaFE (Scar Feature Engineering), which transfers clinical knowledge from a large language model (LLM) into deterministic, executable feature programs instead of asking the model to diagnose images. A web-enabled LLM retrieves clinical evidence and synthesizes programs that measure visually assessable scar attributes. Candidate programs execute in a restricted local environment, and only aggregate validation statistics and feature-level SHAP summaries are returned for iterative repair and refinement; raw images and patient-level outputs remain local. A lightweight Random Forest then operates on the resulting structured representation. On 600 photographs from three hospitals under leave-one-site-out evaluation, ScaFE achieves 81.0% site-macro balanced accuracy, exceeding the strongest baseline, BiomedCLIP, by 10.0 percentage points. With only 10% of the development data, ScaFE retains 72.0% balanced accuracy and an 11.8-point lead. Iterative refinement also raises the executable-program rate from 66.7% to 95.0%, with verified evidence for 91.7% of the final features. These results show that LLM knowledge can support data-efficient, cross-site medical image classification through local and auditable feature programs rather than direct VLM decisions.


### Graph Neural Network Force Fields for Spin Dynamics in Metallic Magnets
**Authors**: Ali Rayat, Yunhao Fan, Gia-Wei Chern

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28537v1](https://arxiv.org/pdf/2607.28537v1)

**Abstract**: Metallic magnets exhibit complex spin dynamics governed by electronically generated interactions. Predictive simulations of such dynamics typically require repeated solutions of an underlying electronic problem throughout the time evolution, creating a major computational bottleneck. Here we introduce a graph neural network (GNN) magnetic force-field framework that learns the effective magnetic energy functional governing itinerant spin dynamics directly from electronic calculations. Conceptually analogous to machine-learned interatomic potentials, the proposed framework enables efficient evaluation of spin torques while capturing the nonlinear and spatially extended interactions generated by itinerant electrons. We benchmark the method on representative metallic magnetic systems exhibiting collinear, noncollinear, and noncoplanar magnetic order. The learned force fields accurately reproduce electronically generated spin torques and yield nonequilibrium spin dynamics in excellent agreement with direct electronic simulations. Our results establish graph neural networks as a powerful framework for machine-learned magnetic force fields, providing a pathway toward predictive large-scale simulations of nonequilibrium magnetism across multiple length and time scales.


### What to Remove, What to Preserve: Dual-Ambiguity Rectification for All-in-One Image Restoration
**Authors**: Cencen Liu, Wen Yin, Dongyang Zhang, Dongmin Li, Shan Zhao, Bing Su, Tao He, Jielei Wang, Guoming Lu

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28526v1](https://arxiv.org/pdf/2607.28526v1)

**Abstract**: All-in-one image restoration aims to handle diverse degradations within a unified framework. Existing methods commonly encode heterogeneous degradation conditions in a shared latent space, where degradation-related cues and scene content can remain entangled. We characterize the resulting challenge as dual ambiguity: semantic ambiguity in channel-wise modulation and spatial ambiguity in restoration responses, which can lead to content corruption and residual artifacts. To mitigate this issue, we propose DAR-Net, a Dual-Ambiguity Rectification Network for all-in-one image restoration. DAR-Net first introduces a Degradation Archetype Representation (DAR) module to construct a structured degradation state through simplex-constrained archetype mixture modeling. Based on this state, a Semantic Ambiguity Rectification (SeAR) module generates degradation-aware prompts to improve channel-wise conditioning in the decoder. A Spatial Ambiguity Rectification (SpAR) module further regularizes degradation-aware and complementary features toward orthogonal response subspaces, reducing spatial interference between removal and preservation cues. Extensive experiments on standard all-in-one restoration benchmarks show that DAR-Net achieves the best overall performance under both three-degradation and five-degradation settings, improving the average PSNR over the strongest competitor by 0.14 dB and 0.34 dB, respectively; it additionally shows superior performance on CDD-11 and WeatherBench.


### TCA-SIR: Learning Target-Conditioned Abstractions for Scientific Inspiration Retrieval
**Authors**: Yuto Suzuki, Farnoush Banaei-Kashani

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28498v1](https://arxiv.org/pdf/2607.28498v1)

**Abstract**: Scientific hypothesis generation for AI for Science typically involves Scientific Inspiration Retrieval (SIR) followed by hypothesis composition. Existing SIR methods rank papers by topical similarity and do not explicitly represent how a candidate inspiration transfers to a target problem. This is especially limiting for remote inspirations, whose value often lies in reusable problem-solving principles rather than topical overlap. Motivated by how humans abstract transferable aspects of a source and remap them to a new target, we reformulate SIR as target-conditioned abstraction (TCA). The retrieval object is a transferable abstract principle extracted from a candidate specifically for the target. We present TCA-SIR, which learns to generate target-conditioned abstractions and uses their representations to predict transferability. On ResearchBench, TCA-SIR outperforms prior SIR methods and direct LLM retrieval, improving HitRate@top4% over MOOSE-Chem by more than 10 percentage points. Learned abstractions also recover target-relevant mechanisms more clearly than an untrained TCA prompt, yielding both stronger retrieval and an interpretable rationale for scientific inspiration.


### A Fuzzy Rule-based Neuro-Symbolic Approach for Pipe Severity Prediction in Sewer Networks
**Authors**: Ngoc Thai Le, Thanh Ma, Umberto Straccia

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28481v1](https://arxiv.org/pdf/2607.28481v1)

**Abstract**: Standard automated sewer pipe severity assessment relies on direct image classification, creating a "black box" where the link between visual defects and final severity scores remains implicit. This study introduces a modular, fuzzy rule-based neuro-symbolic framework that bridges this gap by decoupling neural perception from symbolic reasoning. The perception module utilizes a Swin Transformer to predict 14 multilabel inspection CODE degrees directly from images. For reasoning, a DT, specifically Weka's J48, algorithm is trained on ground-truth CODEs and severity labels, and its paths are converted into 19 fixed IF--THEN rules. Inference operates via fuzzy logic: t-norm activations from CODE conditions are weighted by rule confidence and combined with corresponding s-norms to produce interpretable class evidence. We assessed Product, Łukasiewicz, and Hamacher operator pairs using a dataset of 3,244 images spanning five highly imbalanced severity classes. Ground-truth labels were robustly generated via consensus from five independent large language models analyzing original inspector notes. Our results show an improvement of accuracy, balanced accuracy, Macro F1 and MCC by 17.9%, 12.2%, 23.0%, and 17.3%, respectively, over image-only based classification.
  Overall, the framework combines competitive class-balanced performance with traceable reasoning from predicted CODE degrees to rule supports and severity evidence.


### Towards Autonomous Aircraft Surveillance from Nanosatellites through On-Board Inference and Generative Data Augmentation
**Authors**: Antonio Delgado-Rosa, David Muñoz-Valero, Enrique Adrian Villarrubia-Martin, Juan Moreno-Garcia

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28470v1](https://arxiv.org/pdf/2607.28470v1)

**Abstract**: Airborne surveillance from low Earth orbit is hindered by two interconnected bottlenecks: nanosatellites have a limited downlink budget, yet the conventional approach still transmits terabytes of raw imagery to the ground for processing, and open satellite datasets for aircraft are scarce and severely class-imbalanced. These limitations either delay timely decision-making or prevent standard detectors from learning robust representations of rare aircraft classes. In this paper, a workflow that combines on-board inference with generative data augmentation is proposed to address both limitations jointly. Inference is executed on a 6U CubeSat equipped with a low-power edge tensor accelerator, while a diffusion model fine-tuned through low-rank adaptation generates synthetic minority-class imagery. This synthetic output is automatically annotated, pseudo-labelled, by an intermediate detector and merged with classically augmented samples. The results show that the balanced dataset increases global mean average precision from 77.9% to 82.2%, with the minority class rising from F1=0.683 to F1=0.811, and that the quantised detector fits the on-chip memory and projects 25-30 frames per second on orbit. This approach contrasts with the conventional bent-pipe architecture, in which the satellite acts as a passive data collector. Therefore, the computational tests support the proposed workflow as a decision-support tool for real-time, autonomous airborne surveillance from nanosatellites.


## Agent
### Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent Exploitation
**Authors**: Boning Li, Longbo Huang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28520v1](https://arxiv.org/pdf/2607.28520v1)

**Abstract**: An agent playing a Nash-equilibrium strategy in a two-player zero-sum imperfect-information game secures the game value but forfeits the additional value offered by a flawed opponent. Diffuse deviations pose a particular challenge: binary release rules may gather too little evidence to act, while a full best response to an incomplete opponent model can be highly exploitable. We introduce \emph{budget-constrained confidence-scheduled restricted responses} (CS-RNR), the first opponent-exploitation method whose safety guarantee is a certificate the agent computes on the strategy it actually deploys, so that every exploit it commits to is one it has audited itself. The method tracks pooled action frequencies with anytime-valid confidence sequences and treats a frequency as exploitable only once its interval separates from an equilibrium reference. The confirmed deviations define a conservative opponent model, which a restricted-response solve turns into candidate counter-strategies over a grid of pin levels. Before deployment, each complete candidate is evaluated by a full-tree best response. The resulting certificate is compared with a user-specified budget and committed atomically with the strategy. Because this check is performed on the played strategy, model quality determines the exploitation achieved while the certificate controls reference-relative expected loss. In Leduc hold'em, CS-RNR obtains $6.2\times$ the steady-state gain of a money-verified binary gate while keeping every deployed strategy within budget. A trajectory mixture using the same estimator reaches $13.6\times$ the budget. Across Leduc, Liar's Dice, and 5-rank Leduc, all $36{,}000$ audited hands satisfy the reported certificate tolerance.


### The Role of Causality in Algorithmic Recourse
**Authors**: Srikanth Avasarala, Varun Gupta, Shahin Jabbari, Saber Salehkaleybar, Juba Ziani

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28497v1](https://arxiv.org/pdf/2607.28497v1)

**Abstract**: Algorithmic recourse aims to provide individuals with actionable changes to improve their predicted outcomes in high-stakes classification settings, such as loan and mortgage applications. However, most existing approaches focus only on flipping a model's prediction, without accounting for whether the recommended changes lead to genuine improvement in an individual's true qualifications or merely enable strategic gaming of the classifier. Consequently, deployed recourse policies can induce behavioral responses that degrade predictive accuracy and become ineffective after model retraining.
  In this work, we formalize this failure mode through a causal performative framework for recourse. We model how recourse actions propagate through a structural causal model, capturing interactions among features as well as their effect on the true label. These causal responses induce a non-convex optimization problem, even under standard convex losses. We characterize conditions under which performatively stable solutions exist and can be efficiently computed via simple iterative dynamics. Our analysis reveals that recourse policies that ignore causal structure can induce large, misaligned behavioral responses, whereas causal recourse leads to stable equilibria that reduce incentives for gaming. Experiments on both semi-synthetic and real credit datasets demonstrate that our approach consistently outperforms standard empirical risk minimization while reducing the need for repeated model retraining to accommodate distribution shifts caused by strategic agent behavior.


### A foundation model of numerical intelligence with cross-disciplinary generalization
**Authors**: Chenghan Wu, Zongmin Yu, Liu Yang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28432v1](https://arxiv.org/pdf/2607.28432v1)

**Abstract**: Intelligence is commonly understood as the ability to acquire and apply knowledge, adapt to unfamiliar situations and solve new problems. Large language models exhibit this capacity by inferring task-relevant knowledge from textual context and applying it to new tasks. Yet intelligence need not be confined to language. For scientific and social systems, we need models that acquire and apply knowledge from numerical context-an ability we call numerical intelligence. Here we introduce UNified In-Context Operator Networks (UNICON), a foundation model that exhibits numerical intelligence across disciplines. Using graph-based examples from a system as context, UNICON infers the predictive relation shared across them and applies it to queries from the same system. Across scientific and social systems, including those from disciplines absent from training, the same model approaches specialist performance without retraining. Combining UNICON with language-model agents yields further gains, enabling it to surpass state-of-the-art specialists in a discipline unseen in training. We further show that training-corpus diversity improves generalization to unseen disciplines. Together, these results establish UNICON as a foundation model of numerical intelligence and position it as a building block for a broader ecosystem of artificial intelligence.


### On-Policy and Off-Policy Learning for Large Action Spaces
**Authors**: Imad Aouali

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28408v1](https://arxiv.org/pdf/2607.28408v1)

**Abstract**: This thesis studies policy learning in interactive systems where an agent observes a context, selects an action from a very large set, and receives partial feedback. The main framework is contextual bandits, with two paradigms: on-policy learning, where the agent interacts sequentially with the environment and minimizes regret, and off-policy learning, where it learns from logged data collected by a logging policy. In large action spaces, both settings face major challenges: inefficient exploration, sparse data coverage, high-variance importance weights, extrapolation bias, and difficult optimization landscapes. The first part develops structured Bayesian methods for on-policy learning. We introduce meTS, a mixed-effect extension of Thompson sampling, and dTS, which leverages diffusion-inspired priors to model dependencies between actions. These methods share information across actions and yield regret guarantees depending on an effective number of actions. The second part addresses off-policy learning. We propose sDM, a structured direct method based on latent variables, show that optimization error can dominate estimation error in large action spaces, and introduce concave, efficiently optimizable policy-weighted log-likelihood objectives. Finally, we develop differentiable pessimistic methods based on exponential smoothing and PAC-Bayesian bounds to control the bias-variance trade-off of regularized importance-sampling estimators.


### Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees
**Authors**: Zihan Dong, Rui Qian, Qishi Zhan, Dongshen Peng, Kaixin Li, Yu Li

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28399v1](https://arxiv.org/pdf/2607.28399v1)

**Abstract**: Computer-use agents often fail on transient GUI events because they produce the correct action only after the relevant window has already closed. We identify the main cause as expensive autoregressive decoding on the decision-time critical path. We propose Adaptive Anticipatory Policy Trees (AAPT), which eliminates this delay without modifying the underlying model. During idle screen periods, the same frozen multimodal model constructs a bounded conditional policy tree with observable guards, pre-authorized actions, and branch-specific deadlines. The tree is sized to cover the model's own decoding latency. When an event occurs, a lightweight observer matches change-gated frames to a prepared branch and immediately executes the corresponding action without generating new text. In paired trials with pre-registered endpoints and exact McNemar tests, AAPT improves the success rate from 0.50 to 0.79 within a contested decision window ($p=1.8\times10^{-3}$), while producing no incorrect actions. Both open-loop and predict-and-replan baselines achieve zero success because they still decode during execution. A preparation-time sweep shows that the gain emerges where the latency-based tree-sizing rule predicts, and ablations reveal three key requirements: fast observer decoding, valid tree planning, and accurate branch routing. A pre-registered oracle probe rejects our initial hypothesis and instead points to branch routing as the causal bottleneck. We further reproduce the effect on an independent general-purpose multimodal model over 126 paired trials ($p=4.9\times10^{-13}$). On an external benchmark, AAPT matches the overall performance of a reactive baseline, although the two methods exhibit complementary strengths. Together, these results suggest that AAPT performs best when candidate actions can be enumerated in advance, whereas reactive execution remains stronger when they cannot.


### Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs
**Authors**: Ankur Naskar, Vaneet Aggarwal

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28390v1](https://arxiv.org/pdf/2607.28390v1)

**Abstract**: Constrained Markov Decision Processes (CMDPs) provide a natural framework for reinforcement learning in safety-critical applications, where agents maximize long-term reward while satisfying long-term constraints. Although primal-dual actor-critic methods with linear critics are well understood, extending order-optimal convergence guarantees to neural critics in average-reward CMDPs has remained open. The main challenge is a fundamental bias-cost trade-off in neural critic estimation: under Neural Tangent Kernel (NTK) analysis, reducing critic bias substantially increases critic optimization cost, preventing order-optimal convergence in the primal-dual framework. We resolve this bottleneck by introducing a hierarchical Multilevel Monte Carlo (MLMC) neural critic that performs debiasing simultaneously across trajectory sampling and critic optimization. The resulting estimator attains the bias of a long critic optimization run with only logarithmic expected sample cost. Building on this estimator, we develop a primal-dual Natural Actor-Critic algorithm that achieves both an optimality gap and a constraint violation of order $\tilde{O}(T^{-1/2})$. This establishes the first order-optimal convergence guarantees for infinite-horizon average-reward CMDPs with general policy parameterization and neural critics, while eliminating the need to know the underlying mixing time. Our results are novel even in the unconstrained setting.


