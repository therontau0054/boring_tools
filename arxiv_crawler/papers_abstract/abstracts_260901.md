# Abstracts of Papers

## World Model
### Context-Aware Interleaved Batching for WhisperX
**Authors**: Carlos Bain, Max Bain

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31170v1](https://arxiv.org/pdf/2608.31170v1)

**Abstract**: While WhisperX accelerates speech transcription via intra-audio batching, it isolates audio segments, losing the historical context needed for coherent punctuation and terminology transcription. Conversely, standard Whisper retains context sequentially but suffers from slow inference and hallucination loops. To achieve the best of both worlds, we propose Context-Aware Interleaved Batching. By using VAD-derived segment boundaries, our algorithm stabilizes Whisper's text conditioning, allowing us to safely maintain continuous historical context across batched audio segments. As demonstrated on long-form audio benchmarks, this approach reduces Word Error Rate (WER) and improves proper noun transcription, all while maintaining high-throughput inference speeds.


### SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies
**Authors**: Weiqi Wang, Zhi Li, Yudong Lei, David Martinez, Xiaofeng Gao, Yuxin Jiang, Chenfanfu Jiang, Yingnian Wu, Demetri Terzopoulos, Ran Gong

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31167v1](https://arxiv.org/pdf/2608.31167v1)

**Abstract**: Bridging model-based control and learned policies in long-horizon manipulation has harbored a silent disagreement: control executes specified objectives, learning amortizes that behavior into a reactive policy, yet existing protocols discard task semantics, leaving rewards hand-crafted and behavior drifting from what control verified.We introduce Semantically UNified (SUN) Programs, typed executables where geometric and contact relations are defined once and compiled into aligned Model Predictive Control (MPC) costs, satisfaction predicates, RL rewards, transition guards, and diagnostics. Our system, Kuafu, driven by large vision language systems, automatically synthesizes SUN Programs from language and scene semantics, screens feasibility via MPC, and retains semantics while training stage-conditioned policies. Across nine tasks, Kuafu achieves 82.03% macro-success, outperforming sparse-reward (35.67%) and Stage-BC (24.75%) baselines. At 8192-way scale, it generates 10.57x the successful trajectory time per hour of human teleoperation. With 500 trajectories per task, Kuafu data trains DP3 policies to 46.0% simulation success (vs. 22.4% for alternatives) and 34.7% on physical Franka and Kinova robots. These results establish that simulation-screened task semantics can effectively amortize control into robust policies, without demonstrations or manual dense rewards, unifying symbolic planning and data-driven execution.


### Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations
**Authors**: Shijun Zhang

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31157v1](https://arxiv.org/pdf/2608.31157v1)

**Abstract**: Many parameter-efficient methods generate the parameters of a large neural network from a low-dimensional latent representation. Given an architecture $Φ$ with $P_Φ$ parameter slots, we write $\boldsymbolθ_f=\mathcal{G}(\boldsymbolξ_f)$, where $\mathcal{G}\colon\mathbb{R}^M\to\mathbb{R}^{P_Φ}$ is a parameter generator and $\boldsymbolξ_f\in\mathbb{R}^M$ is a latent representation of the target function $f$. The architecture $Φ$ and the generator $\mathcal{G}$ are shared across the entire target class, while each target $f$ is represented by its own latent vector $\boldsymbolξ_f$, with $Φ_{\mathcal{G}(\boldsymbolξ_f)}$ approximating $f$. This framework encompasses hypernetworks, low-dimensional parameterizations, parameter-efficient adaptation, and model compression. Understanding the tradeoff between the latent dimension $M$ and the network budget $P$ is therefore fundamental to characterizing the expressive efficiency of these methods. We study this tradeoff for affine generators and fully connected ReLU architectures. More precisely, optimizing jointly over architectures $Φ$ satisfying $P_Φ\leq P$ and affine generators $\mathcal{G}:\mathbb{R}^M\to \mathbb{R}^{P_Φ}$, we prove that the optimal worst-case uniform approximation error over the unit ball of $α$-Hölder functions on $[0,1]^d$, where $0<α\leq1$, has the sharp order $ \bigl(P\min\{M,P\}\bigr)^{-α/d}. $ In particular, our result shows that even a fixed-dimensional latent space suffices to achieve vanishing approximation error as the network budget increases.


### Auditing Anonymous AI Models: A Four-Stage Protocol for Black-Box Identity Verification
**Authors**: Yisen Xi

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31142v1](https://arxiv.org/pdf/2608.31142v1)

**Abstract**: The 2025--2026 AI market has seen a wave of stealth releases: frontier models launched anonymously on developer platforms under codenames. For their users, identity determines data-handling terms, supply-chain risk, and capability expectations. No validated methodology exists for black-box identity verification of anonymous models: practitioner checklists lack accuracy evidence, and self-identification is untrustworthy by design. We propose a four-stage forensic audit protocol for API-served models. Stage 0 reconstructs launch-time configuration from archived platform snapshots (Internet Archive), exposing preview--production drift. Stage 1 fingerprints configuration (context, output ceiling, reasoning, modality) against the platform catalog. Stage 2 tests tokenizer identity with a cross-length differential that rejects short-prompt collisions. Stage 3 corroborates with behavioral probes. We test declaration consistency on 10 known-identity releases (7 exact, 2 precision-differences, 1 partial, 0 counter-directional), not end-to-end identification under anonymity. Identification is validated prospectively on a flagship case whose 2026-08-23 analysis pointed to the GLM-5.3 version line and whose official reveal confirmed those family and version-line inferences (deployment variant was not pre-asserted; Flash was consistent post-reveal), and on three Stage-0-only cases where the protocol produced a graded hypothesis or declined rather than guessed. A standard-library-only implementation is provided as supplementary material.


### OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques
**Authors**: Hamed Babaei Giglou, Sören Auer, Peio Popov, Mahsa Sanaei, Jennifer D'Souza

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31137v1](https://arxiv.org/pdf/2608.31137v1)

**Abstract**: Ontology alignment (OA) has evolved through several methodological paradigms, ranging from lexical and structural aligners to knowledge graph embedding (KGE) models and, more recently, Large Language Model (LLM)-based approaches. Although modern OA frameworks provide unified ecosystems for deploying these heterogeneous aligners, mechanisms for systematically reconciling their complementary and sometimes conflicting predictions remain relatively underexplored. We present OntoAligner-Ensemble, a modular and aligner-agnostic framework that combines candidate correspondences through a configurable two-stage process comprising voting-based fusion strategies followed by post-fusion selection policies. The framework supports any aligner implemented within OntoAligner that produces candidate correspondences, enabling diverse alignment paradigms to be integrated through a unified decision process. To demonstrate its effectiveness, we instantiate the framework using representative lightweight string-aligner, KGE-based, and Retrieval-Augmented Generation aligners powered by both open-weight and API-based LLMs. We evaluate individual aligners and ensemble configurations across eight benchmark tasks from five OAEI tracks spanning biomedical to beyond-equivalence. The results show that ensemble fusion consistently improves the balance between precision and recall and frequently outperforms standalone aligners across diverse domains. Furthermore, our analysis reveals that ensemble composition directly affects the precision-recall trade-off: heterogeneous cross-paradigm ensembles generally improve precision, whereas homogeneous LLM ensembles more often achieve higher overall F1-scores. These findings demonstrate that systematic ensemble learning offers a robust and reproducible strategy for OA while providing practical guidance for selecting ensemble compositions under different alignment scenarios.


### Implementing neural network mixed-effects models in Template Model Builder (TMB)
**Authors**: Nan Zheng, Hoi Yiu Cheung, Vibhu Sharma, James T. Thorson, Noel G. Cadigan

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31133v1](https://arxiv.org/pdf/2608.31133v1)

**Abstract**: Neural network mixed-effects models (NMMs) have gained traction by combining the strong representation and predictive power of artificial neural networks with the capacity of mixed-effects modeling to capture complex correlation structures. However, existing estimation approaches rely heavily on manual derivations of objective functions and gradients, which inherently forces simplifying approximations and severely constrains the complexity and accuracy of NMMs. In this work, we introduce a general framework for implementing NMMs using Template Model Builder (TMB). By leveraging automatic differentiation and Laplace approximation, TMB requires users to specify only the negative joint log-likelihood and any regularization terms. The framework automatically integrates out random effects and evaluates the marginal objective function alongside its exact gradients, eliminating the need for manual derivations or ad hoc approximations. We demonstrate the efficiency, flexibility, and statistical performance of TMB-based NMMs across two numerical examples, including an application to monotonic NMMs. Reproducible code is provided to facilitate broader adoption.


## Generation
### Constant Individual Regret in General Games
**Authors**: Mingyang Liu, Gabriele Farina, Asuman Ozdaglar

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31166v1](https://arxiv.org/pdf/2608.31166v1)

**Abstract**: Uncoupled no-regret dynamics provide a decentralized route to equilibrium, but prior guarantees for individual regret retain a polylogarithmic dependence on the horizon. We remove this dependence for every finite $N$-player normal-form game under full-information feedback. We introduce \emph{ECHO-OFTRL}: optimistic follow-the-regularized-leader (OFTRL) equipped with an EMA cascade for high-order optimism (ECHO), where EMA denotes exponential moving average. The algorithm is deterministic and fully uncoupled. If $m_{\max}$ denotes the largest action-set size, then, simultaneously for every horizon $T\geq1$, it guarantees that each of the $N$ players in the game incurs regret upper bounded by $O(\textrm{poly}(N, \log m_{\max}))$. Our algorithm leverages a new form of optimism inspired by modern filter design.


### When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning
**Authors**: Hamed Babaei Giglou, Sören Auer, Jennifer D'Souza

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31118v1](https://arxiv.org/pdf/2608.31118v1)

**Abstract**: The effect of Large Language Model (LLM) scale on ontology learning (OL) performance remains insufficiently characterized. We present a controlled evaluation of 13 models spanning dense and Mixture-of-Experts variants from the Qwen3.5 and Qwen3.6 lineages, together with proprietary GPT release variants, using the OntoLearner retrieval-augmented generation pipeline. All models are evaluated with the same embedding model, retrieval configuration, prompt templates, decoding settings, datasets, and metrics on term typing, taxonomy discovery, and non-taxonomic relationship extraction across four biomedical and materials science and engineering ontologies. Within the dense Qwen3.5 lineage, increasing parameter count primarily improves precision rather than recall, with the largest gains occurring between 9B and 27B parameters. However, the effect of scale is neither monotonic nor uniform across tasks and domains. Dense 27B models outperform substantially larger sparse models on term typing, whereas larger Mixture-of-Experts models achieve the strongest open-weight results on taxonomy discovery. Non-taxonomic relationship extraction remains difficult across model scales, particularly for the Materials Data Science ontology. Performance differences across matched Qwen variants and proprietary GPT releases further indicate that architecture and model lineage can outweigh nominal parameter count. These findings show that model size alone is an insufficient selection criterion for OL and provide empirical guidance for reproducible LLM-assisted ontology engineering.


### "Train classical, deploy quantum" requires rethinking generalization
**Authors**: Snehal Raj, Natansh Mathur, Alejandro Perdomo-Ortiz

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31117v1](https://arxiv.org/pdf/2608.31117v1)

**Abstract**: Generative models have become central across science and industry, from image and text synthesis to the design of molecules and materials. Quantum generative models are considered one of the most promising applications for quantum computers, since a quantum circuit naturally produces samples from the distribution it encodes, and for suitable circuits that distribution is believed to be hard for any classical computer to reproduce. A leading strategy trains these models on a classical computer and reserves the quantum device for generating samples at deployment. This is possible when the training loss can be evaluated on a classical computer. A prime example is the maximum mean discrepancy (MMD$^2$), a moment-matching loss that compares the model and the data through their Pauli-$Z$ correlations. Research so far has asked whether such models can be trained and whether their sampling is hard; whether minimizing such an objective yields a model that generalizes, rather than one that merely reproduces the training statistics, remains poorly understood. We benchmark a broad set of quantum and classical generative models by direct sampling and show that models trained with a moment-matching loss generally show worse generalization than the likelihood-trained models. We show this on two application-inspired datasets: first a cardinality-constrained dataset at up to $30$ qubits and second a dataset of genomic single-nucleotide variants, whose valid set is the observed data. These results indicate that a converged moment-matching loss is not a reliable measure of generalization, and that train-classical, deploy-quantum workflows will need approaches that target generalization directly, leaving open whether better training objectives suffice or whether the model architectures themselves must change.


### BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing
**Authors**: Adrians Skapars, Edoardo Manino

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31105v1](https://arxiv.org/pdf/2608.31105v1)

**Abstract**: Users of a deployed language model routinely encounter behaviours that testing almost never surfaces, since deployment puts the model through orders of magnitude more interactions than any evaluation can simulate. Automated auditors make testing cheap to scale and flexible enough to cover almost any specified behaviour, yet their lack of optimisation pressure makes them sample-inefficient. To address this shortcoming, we introduce BLOOM-WILT, a full auditing pipeline that elicits natural multi-turn instances of rare behaviours, without training cost or access beyond the target's next-token distribution. On the input side, WILT's auditor model revises its conversational strategy across rounds, learning from previous scored interactions. On the output side, WILT adaptively reweights the target's decoding using the model's own distribution conditioned on an elicitation prompt, so that behaviour-relevant generations are sampled ahead of others it finds equally probable when unprompted. We evaluate WILT across 4 target models and 8 behaviours, where it beats the baseline auditor in 30 of the 32 settings and overturns the previous model safety rankings. WILT raises average behaviour presence from 51% to 100% when eliciting self-harm encouragement from Qwen3.5-4B, beating every elicitation method we port into the same pipeline at matched compute, without pushing output probability below the baseline's.


### LLM Post-Training as Brownfield Maintenance: An Industrial Perspective on Dataware Engineering
**Authors**: Gopi Krishnan Rajbahadur, Amir M. Ebrahimi, Boyuan Chen, Ahmed E. Hassan

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31102v1](https://arxiv.org/pdf/2608.31102v1)

**Abstract**: Industrial post-training is a brownfield regime. Teams inherit a deployed checkpoint and must land targeted improvements under fixed compute and mixture budgets without regressing the rest. The maintained artifact is increasingly dataware: behavior governed by a curated post-training mixture, updated via bounded mixture patches rather than clean-slate retraining. From an industrial code-generation improvement effort, we offer a maintainer's perspective on why this work is hard in practice, distilling three recurring challenges, zero-sum mixture design, yield as the binding metric, and end-to-end integration under uncertainty, and arguing that progress depends less on one-off recipes than on an engineering discipline for programming dataware. In our case study, interventions that raised the conversion of teacher distillation into usable training data increased accepted supervision by 2.84 times while using the same solution teacher and four solution attempts per candidate problem. In our primary evaluation, the yield-engineered patch improved CodeForces pass@1 by +2.59 points (+3.11 pass@3) and held-out LiveCodeBench v6 pass@1 by +6.11 (+8.05 pass@3), all statistically significant across 16 stochastic evaluations of each benchmark from one fixed checkpoint per condition, with internal AIME and MATH regression suites within tolerance.


### Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data
**Authors**: Milad Rezaei Hajidehi, Qitong Wang, Stratos Idreos

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31082v1](https://arxiv.org/pdf/2608.31082v1)

**Abstract**: Valuable data remains embedded in unstructured sources: web pages, reports, contracts, filings, earnings calls, and PDFs. The big bet in enterprise AI is deploying LLM agents that reason over this data to answer complex questions for every knowledge worker. Agents can do this today, but at prohibitive cost. Each question repeatedly opens large documents to recover scattered evidence, consuming up to a million tokens. However, if the data were already structured, the same question would reduce to a cheap database lookup. For example, on FanOutQA benchmark, reasoning over an ideal pre-structured store is 28X cheaper, and the gap grows to orders of magnitude as questions fan out over more documents. Yet structuring everything in advance is not viable: documents hold vastly more possible structure than any workload will use, and the useful structure and documents are unknown until queries arrive. We propose agentic data cracking, a method that structures unstructured data adaptively and speculatively as a byproduct of reasoning itself. Structuring is adaptive because observed queries decide when it happens and what matters, and speculative because it goes beyond the current question. Whenever the agent opens a document to answer, a cracking sub-agent forks from the already-loaded context at marginal cost and extracts grounded structure likely to serve related future queries. Over time, an increasing share of queries is fully covered by structured data and answered without opening a document, keeping agentic accuracy at close to RAG cost. On FanOutQA, extended with merely one related question per test question, cracking cuts cost by 53% while preserving accuracy. Agentic data cracking is a first step toward next-generation data infrastructure for agentic reasoning over unstructured data: a shared substrate beneath the model where knowledge that reasoning already paid to uncover accumulates.


## VLA
### Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving
**Authors**: Tian Zhang, Zhuo Huang, Hongrui Ye, Yu Wu, Zengmao Wang, Kaixuan Zhou

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.30122v1](https://arxiv.org/pdf/2608.30122v1)

**Abstract**: Vision-language-action (VLA) driving methods increasingly combine multi-trajectory imitation learning with group-relative policy optimization (GRPO), making trajectory selection critical to final performance. However, some high-scoring trajectories that improve imitation can degrade subsequent GRPO by inducing advantage estimates misaligned with the current policy's feasible behavior distribution, driving updates away from safe and compliant behaviors. To address this, we propose a novel framework that aligns multi-trajectory supervision with policy optimization. To address the policy gradient bias induced by infeasible noisy trajectories outside the feasible region, augmented trajectories are constrained to a neighboring manifold of the ground-truth feasible region, and a Pareto-optimality criterion is adopted in place of the conventional aggregate score, retaining only non-dominated candidates and thereby filtering out conflicting samples at the source. To ensure that expanded trajectory supervision is effectively absorbed during policy optimization, we introduce two complementary mechanisms: feasibility-first advantage assignment and dynamic distillation. The former adapts Pareto credit to the feasibility composition of each rollout group and guides fully infeasible groups toward safe references. The latter updates teacher trajectories across refinement rounds to continually transfer useful supervision. Together, they progressively translate the benefits of expanded supervision into policy improvement. On NAVSIM v1 and v2, our method achieves 91.4 PDMS and 89.1 EPDMS, respectively, under single-trajectory inference, and recovers 440 of 658 initially failed scenes, 11.1\% higher than the original GRPO baseline.


### Training-Free Action Correction for VLA Model Failures via Language Feedback
**Authors**: Owen Kwon, Pablo Ortega-Kral, Arthur Bucker, Jean Oh

**Published Date**: 2026-08-30

**Updated Date**: 2026-08-30

**PDF Url**: [2608.29967v1](https://arxiv.org/pdf/2608.29967v1)

**Abstract**: Vision-Language-Action (VLA) models demonstrate strong semantic understanding yet exhibit systematic failures during deployment. The conditions under which these failures occur, and whether they can be corrected without retraining, remain poorly understood. In this paper, we take steps toward addressing this gap. We present CorrectVLA, a framework that translates task-level natural language corrections into additive action magnitude adjustments without modifying policy weights. A human provides a single task-level correction, applied uniformly across all rollouts without per-episode intervention. In simulation, CorrectVLA recovers execution misalignment failures across both in-distribution and OOD tasks. In real-robot experiments on a UFactory xArm7 under environment shift, CorrectVLA restores near-perfect success where the base policy almost entirely breaks down, generalizing across object locations and identities. Through a taxonomy of failure modes on LIBERO-90, we find that execution misalignment failures, where the policy reaches the correct target but miscalibrates action magnitudes, represent the correctable subset, while other failure modes where semantic comprehension itself breaks down are not amenable to this approach. The approach succeeds when policies possess strategic correctness and fails when fundamental comprehension is absent, establishing a practical operational boundary for inference-time correction.


### AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies
**Authors**: Hongbo Gao, Zeyu Ni, Xin Wen, Siyu Xu, Ruifeng Li

**Published Date**: 2026-08-30

**Updated Date**: 2026-08-30

**PDF Url**: [2608.29537v1](https://arxiv.org/pdf/2608.29537v1)

**Abstract**: Frozen vision-language-action (VLA) policies offer broad manipulation skills but execute open-loop action chunks without tracking task progress, so the agent cannot reliably decide whether to continue, retry, or terminate. External memory is a natural remedy, yet it can be harmful when attempted actions are treated as completed progress, turning local execution errors into persistent task-state errors. We propose Achievement-Grounded Memory (AGM), a lightweight closed-loop framework for frozen VLA policies that represents a task as a subgoal sequence with a progress pointer and advances this memory only after the current subgoal is verified by physical evidence. Proprioceptive interaction cues decide when to verify, while coherent point tracking and language-conditioned cross-view comparison, sourced from frozen foundation models through a single 2.43M-parameter verification head, decide what was achieved. AGM thereby converts open-loop execution into a closed loop of execution, verification, and progress, keeping the policy frozen without test-time large-model inference. On the RoboMME Counting benchmark, AGM reaches on PickXTimes and on BinFill, surpassing the strongest memory-augmented baseline by points on average, and the framework yields equally decisive gains on a physical robot. Reliable embodied memory thus depends more on disciplined state updates than on memory capacity.


### AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models
**Authors**: Sunghwan Han, Youngtae Han, Youngmin Yi

**Published Date**: 2026-08-29

**Updated Date**: 2026-08-29

**PDF Url**: [2608.29208v1](https://arxiv.org/pdf/2608.29208v1)

**Abstract**: Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning. However, the intensive computational overhead of VLAs constrains on-device deployment, hindering real-time responses to environmental changes. While various acceleration techniques have been proposed, they often rely on fine-tuning or access to training datasets, which are frequently unavailable due to privacy and proprietary concerns. Moreover, although flow-matching-based VLAs have emerged as efficient alternatives to standard diffusion models, current acceleration efforts largely target VLM inference costs, failing to address the iterative ODE solving process inherent in flow matching inference. To address these limitations, we propose AdaVLA, an online, training-free adaptive framework for fast yet accurate flow-matching-based Vision-Language-Action models. We introduce a novel metric derived from the flow matching trajectory curvature to quantify action generation confidence during inference. This metric enables the dynamic reduction of inference steps and the adaptive adjustment of MLP pruning ratios through an efficiently computed importance evaluation, requiring no access to training data. Experimental results on the LIBERO benchmark using a Jetson AGX Orin device demonstrate that our method achieves $1.87\times$ and $2.24\times$ speedups for $π_{0.5}$ and X-VLA, respectively, with negligible degradation in success rates. Furthermore, we validate the robustness of our approach on real-world robotic tasks using SmolVLA.


## Agent
### Reconciling Process Supervision with Outcome-Based Credit in Agentic Policy Optimization
**Authors**: Jingxiao Yang, Wangjie Gan, Yingxuan Zhuang, Wenqi Zhang, Jintao Chen, Xuhong Zhang

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31077v1](https://arxiv.org/pdf/2608.31077v1)

**Abstract**: Outcome-based reinforcement learning provides verified feedback for language-model agents, but assigns trajectory-level advantage uniformly to all decisions, yielding coarse credit over long-horizon interactions. On-policy self-distillation offers finer supervision by re-evaluating sampled behavior with privileged information (PI) available only during training. However, fine-grained supervision is not necessarily fine-grained credit: PI-induced likelihood changes describe how additional information alters policy preference, but do not directly determine how an executable action should inherit the verified task outcome. This creates a supervision-credit gap. Privileged signals may be irrelevant to the current interaction state, operate at a token granularity misaligned with executable decisions, and lack the outcome semantics required for reinforcement. We introduce TASPO, which converts privileged supervision into outcome-grounded action credit. TASPO constructs decision-applicable PI from verified successful experience, aggregates PI-induced likelihood shifts at the executable-action level, and converts relative action support into positive, bounded, mean-preserving weights on the original trajectory advantage. Thus, the verified outcome determines the update direction and average scale, while PI only redistributes credit across actions. Across three agentic benchmarks, TASPO improves over GRPO by 10.6\% and generalizes better to unseen tasks. Further analysis indicates that TASPO reduces supervision mismatch and that action-level assignment stabilizes the policy optimization process. These findings offer the community another interesting perspective.


### Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents
**Authors**: Xuehai Wang, Haowei Qin, Tongxin Liu, Junkai Li, Buqiang Xu, Jintian Zhang, Yijun Chen, Zirui Xue, Shumin Deng

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31076v1](https://arxiv.org/pdf/2608.31076v1)

**Abstract**: Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task. As a result, agents may miss important analyses, use inappropriate methods, or draw conclusions that are insufficiently supported by evidence. To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. AutoSciRub decomposes an underspecified instruction into atomic scientific goals, grounds them in relevant literature and task-visible data, and synthesizes specific, actionable, and verifiable criteria. The resulting rubric makes implicit experimental and evidential requirements explicit, providing guidance for experiments and analyses. During revision, rubric-guided verification identifies unmet criteria and enables targeted refinement of the research report and its supporting artifacts. On ResearchClawBench, AutoSciRub consistently improves all tested configurations, with an average gain of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using a fixed DeepSeek-V4-Flash backbone. On a randomly sampled 20-task subset of AstaBench E2E Discovery, AutoSciRub further achieves an average improvement of 16.8 points across three agent harnesses, while maintaining or increasing the number of successfully completed tasks. These results demonstrate that evaluation-first guidance provides an effective and generalizable control mechanism for autonomous scientific research (Code: https://github.com/zjunlp/AutoSciRub).


### Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence
**Authors**: Zhiqin Yang, Jingwen Fu, Yuhan Liu, Hengyu Liu, Yonggang Zhang, Kainan Cao, Zizhuo Zhang, Chenxin Li, Ruibin Yuan, Jiahao Pan, Jiankai Sun, Zhenyuan Zhang, Yibo Li, Yunlong Lin, Jing Xiong, Sida Lin, Bo Han, Wei Xue, Yike Guo

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31075v1](https://arxiv.org/pdf/2608.31075v1)

**Abstract**: Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to improve as human supervision gradually recedes from the learning loop. We examine two connected dimensions of this problem. The reward axis traces the development from per-instance human judgments to reusable verifiers and rewards that operate even without human feedback. The experience axis examines how learning can progress from human-curated tasks and environments toward self-generated curricula, constructed environments, and autonomous co-evolution. We connect these dimensions through a five-level ladder from L0 to L4 that identifies which parts of the learning process remain under continued human control. Our analysis further highlights the risks introduced by increasingly autonomous rewards and experience generation, including reward hacking, feedback drift, curriculum collapse, and environment errors. Consequently, we also provide the evaluation around three complementary objects: policy capability, feedback fidelity, and experience quality. This analysis provides a structured account of current approaches to scaling LRMs beyond human supervision and the open problems involved in developing self-sustaining learning systems toward superintelligence. Furthermore, we maintain a continuously updated \href{https://github.com/visitworld123/Awesome-Scaling-LRM-Beyond-Human-Supervision}{GitHub repository} to track the latest advances.


### Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents
**Authors**: Le Chen, Zishen Wan, Baixi Sun, Xiaolong Ma, Chih-Hsuan Yang, Feng Yan, Sheng Di, Franck Cappello, Rajeev Thakur

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31057v1](https://arxiv.org/pdf/2608.31057v1)

**Abstract**: Agent working memory is heterogeneous. Objects such as instructions, artifacts, tool outputs, and agent-generated state play different semantic roles and exhibit different size, retention, and representation profiles. Recent work has begun to explore memory-management mechanisms that account for such heterogeneity. This work focuses on semantic heterogeneity and studies how it should shape the management and evaluation of working memory in coding agents. Across 55 archived coding-agent trajectories, we find that semantically different working-memory objects exhibit distinct retention and compression behavior. This heterogeneity motivates semantically informed memory management. We study two semantically informed strategies: an object-aware compression policy and a retrieval-based policy. Their evaluation shows that calibration gains may not transfer to held-out tasks, and that equal token budgets do not imply equal delivered context or management cost. A real-system replay further exposes serving limits that nominal budgets alone do not capture. Together, these results show why semantic structure matters for agent working memory and why evaluating memory-management strategies requires more than a nominal token budget. We organize these lessons into four levels: stored state, delivered context, management work, and task or process outcome.


### MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents
**Authors**: Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31022v1](https://arxiv.org/pdf/2608.31022v1)

**Abstract**: AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.


### Language-Informed Flow Matching for Trend-Guided Structure-Based 3D Molecular Generation
**Authors**: Tianyu Gao, Zhikai Su, Jiashu Li, Wenjun Gao, Zichuan Ying, Zhe Zhao, Fei Zhang, Ye Wei

**Published Date**: 2026-08-31

**Updated Date**: 2026-08-31

**PDF Url**: [2608.31009v1](https://arxiv.org/pdf/2608.31009v1)

**Abstract**: Structure-based drug design (SBDD) requires ligands that satisfy both 3D target affinity and 1D chemical validity. Existing controllable generation methods often rely on task-specific fine-tuning or externally imposed sampling-time guidance, adding cost and potentially conflicting with evolving 3D geometric constraints. We propose LiFT, a language-informed cross-modal framework built on Flow Matching for trend-guided 3D molecular generation across both de novo design and scaffold hopping. LiFT uses a "Sense-Evolve-Assemble" agent to generate target-aware SMILES as intermediate chemical conditions, from which a pre-trained chemical foundation model extracts continuous semantic priors. These priors are integrated into geometric generation through a lightweight semantic projector with zero-initialized adaptive normalization for stable cross-modal conditioning. We further introduce a Self-Conditioned Decoupled Router (SCDR), which modulates the velocity field according to intermediate structural states during ODE integration. Experiments on Cross-Docked2020 show that LiFT achieves competitive distribution matching while improving medicinal chemistry metrics and maintaining competitive structural validity under task-steering settings without additional generator fine-tuning. Our results suggest that language-derived chemical priors provide effective trend-level guidance for 3D molecular generation. Code and released artifacts are available at https://github.com/kasurl/LiFT.


