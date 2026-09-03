# Abstracts of Papers

## World Model
### SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models
**Authors**: Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02886v1](https://arxiv.org/pdf/2609.02886v1)

**Abstract**: We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive data mixing and model-specific implementations therefore produce inconsistent supervision and make results difficult to reproduce and compare. SolarWM addresses this coupling with a reconfigurable multi-source data engine and a backbone-native adaptation framework. The engine converts 1.43 million canonical clips from 10 datasets into a unified, frame-aligned contract covering visual observations, metric camera geometry, captions, quality metadata, selection decisions, and provenance, while decoupling source processing from mixture construction. Under shared camera-conditioning, training, and inference interfaces, we instantiate four 5B--33B models based on Wan2.2, LTX-2.5, and MiniMax-H3 while preserving their native representations and objectives. A unified three-stage recipe combines bidirectional adaptation, teacher-forced autoregressive initialization, and distribution matching distillation. The resulting causal models enable real-time interaction over rollouts ranging from minutes to hours after being trained on only 5s sequences. By releasing the resulting data, pipeline, recipes, weights, and framework, SolarWM provides a reproducible and extensible foundation for interactive world-model research.


### Discriminative World Models for Web Agents
**Authors**: Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02885v1](https://arxiv.org/pdf/2609.02885v1)

**Abstract**: Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PRM). These world models are typically trained via supervised next-state prediction to generate fixed representations like HTML or AXTree snapshots. However, this objective is misaligned with the downstream ranker, which relies on predicted states being discriminative across candidates to accurately score them. To address this, we introduce predicted-state matching, a training objective where the predicted representation must distinguish the true resulting state from those reached by alternative actions. We train these models using a branching web-agent dataset derived from WebArena Go-Browse trajectories, where every decision point contains multiple alternative actions and their resulting states. Experiments on our held-out predicted-state matching benchmark show that our approach outperforms world models trained with supervised next-state prediction. We further show that our approach improves PRM-style action ranking on WebPRMBench compared with action-only PRMs and PRMs augmented with supervised-next-state world models. Finally, on WebArena-Lite, using our world model for test-time action selection improves end-to-end task success. Our project page is available at: https://dhruvpendharkar.github.io/dwm/.


### Graph Machine: Towards Better Pretraining via Edges
**Authors**: Lintai Hou

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02881v1](https://arxiv.org/pdf/2609.02881v1)

**Abstract**: We introduce the Graph Machine (GM), an architecture that maintains an $O(n)$-sized state and accesses it through sparse, dynamic routing. Unlike methods with fixed-size states or sparse but static routing, GM preserves $O(n)$ complexity in its sparse layers without restricting the potentially accessible state size to $O(1)$. Instead, GM uses edges - pointer-like objects updated differentiably by a referral mechanism resembling pointer chasing. We replace 75% of the dense Transformer layers in Qwen3-0.6B with GM sparse layers and pretrain from scratch on 15.7B tokens. With only 2 of 4,096 tokens retrieved per KV head in each sparse layer, loss degrades only slightly; with 4, the best model marginally improves loss.


### GRADSOLVE: fast exact gradients for ODE ensembles on GPUs
**Authors**: Alessio Spurio Mancini

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02876v1](https://arxiv.org/pdf/2609.02876v1)

**Abstract**: Ordinary differential equations (ODEs) underlie models in science and engineering, and many applications need derivatives of their solutions with respect to parameters. Ensembles of independent trajectories suit graphics processing units (GPUs), but current GPU software forces a trade-off: the fastest ensemble solvers cannot be differentiated in reverse mode at the speed they solve, and the solvers built for differentiation solve more slowly. No single tool has yet offered a reverse-mode gradient at the speed of a fused-kernel solve.
  We present GRADSOLVE, an open-source JAX library for solving and reverse-mode differentiating low-dimensional ODE ensembles on NVIDIA GPUs. It records the steps an adaptive solver accepts and differentiates a fixed-step replay of them; the returned gradient is the exact discrete adjoint of those steps, the same derivative Diffrax returns by default, obtained more cheaply from a fixed-length chain than from an adaptive loop. It targets ensembles differentiated many times against one recorded mesh, keeps Diffrax as a fallback, and supports explicit and Rosenbrock integrators.
  Used as a solver, GRADSOLVE's forward-only kernel ran 2.8x faster than DiffEqGPU.jl; used for gradients, once a record exists, it computed them 5.6-14.1x faster than Diffrax's checkpointed adjoint at matched forward-state accuracy across three GPU generations, the advantage narrowing on large ensembles and, on stiff systems, down to parity at tight accuracy. GRADSOLVE is released at https://github.com/ECLIPSE-AI4Science/gradsolve.


### Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation
**Authors**: Yutong Liu, Nan Huang, Xu Cao, James M. Rehg

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02864v1](https://arxiv.org/pdf/2609.02864v1)

**Abstract**: Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introduce RIG-BENCH, a novel comprehensive benchmark that systematically evaluates Reasoning-driven Image Generation (RIG) across four cognitively demanding domains: Concept-based, Transformation-based, Pattern & Structure, and Scenario-based. Featuring 2000 curated samples, RIG-BENCH serves as a rigorous stress test for RIG. Our extensive evaluations of state-of-the-art UGMs and image/video generation models reveal a significant reasoning-generation gap, wherein models frequently produce locally plausible but globally illogical outputs. RIG-BENCH provides a vital diagnostic framework to guide the development of next-generation, logically grounded UGMs and world simulators.


### Towards Trustworthy Autonomous Robots: An Explainable AI-Based Decision Framework
**Authors**: Cagri Temel

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02861v1](https://arxiv.org/pdf/2609.02861v1)

**Abstract**: Autonomous robots powered by deep learning face a fundamental auditability challenge: when incidents occur, investigators cannot reconstruct why the system made specific decisions. This paper presents TRACE (Transparent Reasoning Architecture for Credible Execution), a decision framework that ensures every autonomous action can be traced back to sensor evidence through documented causal chains. The framework organizes decision-making into four auditable layers: Semantic Perception for evidence-grounded entity recognition, Belief Reasoning for probabilistic state estimation with causal graphs, Action Synthesis for constraint-aware planning with counterfactual documentation, and Execution Verification for compliance monitoring. TRACE is model-agnostic yet designed to integrate learning-based perception modules (CNNs, transformers) while preserving decision-level auditability. We evaluate the framework using three objective metrics: Evidence Traceability (sensor-to-decision linkage), Decision Reconstructability (post-hoc analysis capability), and Temporal Continuity (audit trail completeness). Experimental evaluation on warehouse robot navigation demonstrates that TRACE achieves 98.6% evidence traceability, 99.0% temporal continuity, and 98.1% decision reconstructability across 500 simulated decision cycles. Post-hoc methods like LIME provide feature attributions but lack the artifact structure needed for decision-level reconstruction. The framework addresses EU AI Act requirements for high-risk system transparency and contributes to Explainable AI for safety-critical autonomous systems.


## Generation
### The Implications of Linguistic Illegibility for LLM Security
**Authors**: James Mickens

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02852v1](https://arxiv.org/pdf/2609.02852v1)

**Abstract**: LLMs are trained to generate natural language. However, various strands of evidence indicate that an LLM's externalized linguistic outputs and mechanistically-extracted linguistic features can be an unreliable lens for understanding internal model computation. We introduce the term ``linguistic illegibility'' to broadly refer to scenarios in which an LLM's externalized or mechanistically-probed language artifacts fail to represent how the model actually thinks. We argue that the specter of linguistic illegibility is unavoidable for LLMs whose internal computations are not directly expressed via language, but rather math over activation spaces (with lossy translations between activation spaces and natural language happening at the bookends). If linguistic illegibility is always possible, then security mechanisms that rely on a model's linguistic self-reporting (e.g., chain-of-thought monitoring, constitutional self-critique, activation probing for linguistically-defined feature vectors) can never be completely sound; the model sandbox will always need isolation techniques whose guarantees do not depend on reading a model's linguistic state at all. We argue that observing a model's outputs using taint tracking is a promising approach for an effective sandbox: regardless of how a model linguistically self-reports, a taint tracking policy can define, a priori, various pieces of system state that should never be influenced by model-produced data. We also discuss several additional sandboxing mechanisms (e.g., robust virtualization, third-party auditing of sandboxing configurations) which collectively provide a critical floor beneath linguistic monitoring, and would have mitigated recent sandbox exploits by frontier models.


### Post-Training Language Models for Gold-Medal Performance in Coding Competitions
**Authors**: Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02849v1](https://arxiv.org/pdf/2609.02849v1)

**Abstract**: Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, we train Nemotron-3-Nano-CC (30B-A3B) with SFT and RL and Nemotron-3-Ultra-CC (550B-A55B) with SFT alone. We further introduce GenCorrect, a feedback-driven test-time compute strategy that iteratively generates, evaluates, and refines diverse solutions. On IOI 2025, Nano-CC improves from 130 points to 291 after post-training and to 468 with GenCorrect, exceeding the gold threshold of 438.3 while Ultra-CC reaches 502. Guided by these results, we develop a competition-specific Ultra-CC system and evaluate it prospectively during IOI 2026. Under the same time, internet-access, and submission constraints as human contestants, it scores 535.4 out of 600, exceeding both the gold threshold of 361.12 and the top human score of 498.27. To our knowledge, this is the first AI system to outscore the highest-scoring human contestant on an IOI problem set.


### Learning Spectral-Like Mesh-Free Discretisations
**Authors**: Lucas Gerken Starepravo, Henry Broadley, Steven Lind, Jack R. C. King

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02833v1](https://arxiv.org/pdf/2609.02833v1)

**Abstract**: Meshfree methods such as smoothed particle hydrodynamics (SPH) with kernel corrections, radial basis function-generated finite differences (RBF-FD), and the local anisotropic basis function method (LABFM) construct discrete differential operators by imposing polynomial consistency on a local stencil. For stencils containing more nodes than there are consistency constraints, the resulting linear system is underdetermined, and the remaining degrees of freedom are fixed implicitly by the choice of kernel, basis preconditioning, or a minimum-norm condition. Polynomial consistency constrains the operator only in the low-wavenumber limit, and no part of the construction selects for accuracy at the wavenumbers where fine-scale content resides. We introduce Spectral-like Neural Discretisation (SpeND), in which the choice of those degrees of freedom is cast as a learning problem: stencil weights are parametrised by a neural network conditioned on the local node geometry, trained to approximate the modal response of a spectral operator over the resolvable band. A hard-constrained projection layer maps the network output onto the affine subspace of consistent weights, so that polynomial consistency holds exactly by construction rather than as a penalty. Training is self-supervised and physics-agnostic, requiring no reference solutions; the objective minimises dispersion and dissipation error over a prescribed band-limited function space. Modal analysis on disordered two-dimensional node distributions shows that the learned fourth-order operator follows the exact response over a substantially wider band than either explicit LABFM at equal stencil size or fourth-order finite differences on a structured grid, whilst recovering the expected fourth-order convergence rate under refinement.


### Cliff: Learning Process Rewards from the First Mistake
**Authors**: Peixuan Han, Runhui Wang, Ketan Ramaneti, Jie Hao, Gerald Friedland, Chris Kong

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02817v1](https://arxiv.org/pdf/2609.02817v1)

**Abstract**: Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for large language model (LLM) post-training, but its reliance on coarse outcome rewards leads to limited guidance on intermediate reasoning processes. Existing approaches such as process reward modeling and on-policy distillation introduce additional constraints, such as reliance on a specialized reward model or assuming identical reasoning patterns between teacher and student. Nevertheless, we observe that once a reasoning process first goes wrong, evaluating the subsequent reasoning provides limited additional information, as it is already conditioned on an invalid prefix. Therefore, we propose Cliff, a reward shaping strategy that utilizes an off-the-shelf LLM as a teacher to identify the first mistake in each rollout. As a result, the rollout is naturally decomposed into two parts: a correct prefix and an incorrect suffix. Cliff then converts this signal into token-level advantages, assigning positive advantages for the correct prefix and negative feedback afterward. Experiments across 12 different scenarios demonstrate that Cliff consistently improves reasoning performance, outperforming on-policy distillation by 15% and standard GRPO by 7%, even with teachers of modest capability. Furthermore, we analyse the role of ``ground truth'' in Cliff and investigate its training dynamics. These results establish Cliff as a simple, general and effective approach for improving RLVR with richer, fine-grained supervision.


### Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis
**Authors**: Hao Zhou, Mandar Kulkarni, Hao Chen, Yan Xin,  Charlie,  Zhang

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02805v1](https://arxiv.org/pdf/2609.02805v1)

**Abstract**: Root cause analysis (RCA) is a critical task in telecom network operations, but diagnosing performance degradations in modern 5G and emerging 6G networks remains challenging due to complex cross-layer dependencies. While large language models (LLMs) offer promising capabilities for reasoning and knowledge integration, directly applying vanilla LLMs to telecom RCA often leads to hallucination, unstable reasoning, and poor alignment with structured network evidence. This work first reviews the evolution of telecom RCA from rule-based and machine learning (ML) approaches to emerging LLM-enabled techniques, and provides an overview of recent paradigms, including structured reasoning, retrieval-augmented knowledge grounding, agentic orchestration, and verifiable reasoning. Building upon these insights, we propose a structured reasoning framework for LLM-enabled telecom RCA that aligns diagnostic reasoning with telecom-specific evidence and domain knowledge. The proposed approach first organizes heterogeneous network telemetry into canonical contexts, and then enforces decision-path reasoning during diagnosis, and finally generates evidence-grounded explanations for reliable fault identification. Experimental results on two 5G RCA datasets, TeleLogs and TelecomTS, demonstrate that the proposed framework consistently improves diagnostic accuracy and decision consistency compared with baseline techniques. These cross-dataset results highlight the importance of structured reasoning design for practical LLM-based RCA systems in next-generation telecom networks.


### Dutch Books for Language Models
**Authors**: Isaiah Andrews, Suproteem Sarkar

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02797v1](https://arxiv.org/pdf/2609.02797v1)

**Abstract**: People increasingly use language models to support life decisions. Many such decisions involve a probabilistic forecast: How likely is a major life event, a natural disaster, or an economic outcome? Users of language models may implicitly trust that these forecasts fall out of a coherent world model. In this paper, we evaluate the coherence of language model probabilistic forecasts through a procedure that builds on a theorem due to de Finetti. We elicit forecasts from language models across events generated from stock returns data. We then use linear programs to compute the largest Dutch-book profit - the profit an arbitrageur could guarantee by betting against model-generated probabilities - which we use as a measure of incoherence. Our procedure does not require outcome labels, so we can evaluate coherence even in settings where outcomes are not observed or have not yet resolved. We find substantial evidence of incoherence in language model forecasts. Such incoherence increases when there are richer logical relationships between events, and irrelevant contextual details can increase incoherence by an order of magnitude. We conclude by discussing how alternative training strategies may improve probabilistic coherence.


## VLA
### EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents
**Authors**: Wei Wang, Wenqiao Zhang, Yutong Lin, Yuqian Yuan, Tianwei Lin, Jinhao Mao, Zhenxuan Fan, Mingjian Gao, Yang Dai, Wentong Li, Zheqi Lv, Zheng Dong, Yingjie Niu, Jiaqi Zhu, Jun Xiao, Chao Li, Yueting Zhuang

**Published Date**: 2026-09-01

**Updated Date**: 2026-09-01

**PDF Url**: [2609.01281v1](https://arxiv.org/pdf/2609.01281v1)

**Abstract**: Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, but long-horizon tasks require more than action prediction. An agent must coordinate perception, planning, execution, progress verification, and recovery as the physical state evolves. An action prediction or a model-generated skill decision does not, by itself, guarantee that the proposed operation is valid in the current state or that its outcome will be verified. We propose EmbodiedSkills, a unified framework that treats each skill decision as an execution proposal: the runtime checks its prerequisites before execution and verifies the outcome afterward. A shared executable-skill interface connects high-level skill selection, bounded low-level VLA execution, and post-action verification within a single agent loop. Because this interface remains fixed, low-level VLA policies can be replaced or adapted without changing the agent loop. The interface also records planning, execution, verification, and recovery events as structured trajectories, which provide supervision for individual components and can support optional online adaptation when interactive feedback is available. We instantiate EmbodiedSkills with Qwen3-VL and OpenPI/pi0.5 on RoboTwin 2.0 and LIBERO. Task-adapted low-level VLA policies achieve an average success rate of 86.20% across 50 RoboTwin 2.0 tasks and 97.40% across the four LIBERO suites. These results establish the execution performance of the task-adapted low-level VLA policies used in EmbodiedSkills. On four memory-dependent RMBench tasks, the same task-adapted execution approach achieves 12.5% average success. The framework provides a trainable and inspectable agent layer for turning these policies into closed-loop embodied systems.


### REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs
**Authors**: Riyaaz Shaik, Chandru Venkataraman

**Published Date**: 2026-09-01

**Updated Date**: 2026-09-01

**PDF Url**: [2609.01215v1](https://arxiv.org/pdf/2609.01215v1)

**Abstract**: Most vision-language-action (VLA) models -- OpenVLA, $π_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's dynamics. We introduce REFACTOR-VLA, a wake/sleep system for learning reusable skills. Its sleep phase clusters motor-program fragments under a Behavioral-Equivalence Kernel (BEK) computed from rollouts of a learned latent world model $M_φ$; its wake phase emits typed lambda terms over a Hindley--Milner-inspired vocabulary, consumed by a library-conditioned rectified-flow action decoder. Abstractions are admitted only if they pass Minimum Description Length and return-preservation gates. On LIBERO we report two findings. First, enlarging the world model from 188M to 430M parameters worsened performance on 4 of 4 suites, so capacity alone does not help. Second, the training objective matters far more: adding an auxiliary supervised contrastive (InfoNCE) loss during world-model warmup substantially improves sleep-phase clustering, giving Normalized Mutual Information at $n=3$ seeds of $0.462 \pm 0.021$ (object), $0.867 \pm 0.025$ (spatial), $0.915 \pm 0.013$ (goal) and $0.754 \pm 0.010$ (LIBERO-10), and beating the strongest published baseline on all 4 suites by a mean $Δ= +0.184$. Across providers ($n=12$) the 95% bootstrap confidence interval for mean pairwise NMI is $[0.683, 0.729]$ (mean $0.705$). The sleep phase also yields the first real-LIBERO task-language library: the decoder uses 2 of 3 admitted abstractions and rewrites all 256 sampled demonstrations.


## Agent
### SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment
**Authors**: Qinghua Mao, Wanying Qu, Dadi Guo, Leitao Yuan, Qingyu Liu, Yu Li, Guanxu Chen, Yanwei Fu, Xi Lin, Xia Hu, Dongrui Liu

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02786v1](https://arxiv.org/pdf/2609.02786v1)

**Abstract**: The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses and multi-step execution trajectories. Existing safety alignment mechanisms often rely on either external harness updates or policy optimization, yet applying either paradigm in isolation fails to bridge runtime control with intrinsic safety. We propose SafeEvolve, an experience-driven self-evolving framework for agent safety alignment. SafeEvolve leverages safety experience from completed on-policy trajectories to drive a continual loop of harness-policy co-evolution. On the harness side, SafeEvolve converts trajectory-level safety evidence into bounded, component-level updates across safety prompt and hierarchical skills, yielding auditable and reversible harness artifacts. On the policy side, SafeEvolve follows a two-stage SFT-RL paradigm, where harness-use SFT bootstraps the policy to actively leverage evolved harness artifacts, and harness-augmented RL further shapes autonomous safety behaviors during multi-step exploration via verifier-decomposed rewards. Through harness-policy co-evolution, SafeEvolve converts safety experience into an evolved runtime harness and improved policy behavior. Experiments on agentic safety benchmarks show that SafeEvolve achieves a stronger safety-utility tradeoff than existing baselines. For Qwen3.5-4B, SafeEvolve achieves a $3\times$ ASR reduction on AgentDojo while improving benign utility from 59.79% to 61.86%.


### Measurement-Driven Sub-Network Selection for On-Premise Retrieval-Augmented Factory Agents
**Authors**: Vasileios Rizeakos, Georgios Paisios, Alexandros Machairas, Michael Birbas, Athanasios Bachoumis

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02760v1](https://arxiv.org/pdf/2609.02760v1)

**Abstract**: On-premise assistants can give factory workers conversational access to machine documentation, but models capable of the task rarely fit shop-floor hardware. We show that after structural compression and retrieval-grounded adaptation, model size is no longer a reliable predictor of adapted answer quality: general capability falls almost linearly with parameter count, while judged retrieval-augmented answer quality does not. We therefore treat deployment as a post-adaptation selection problem, committing one sub-network per device on judged answer quality and measured on-device throughput under a configurable general-capability floor and memory budget; rules that optimize size, speed, or quality alone each give up capability or throughput. A weight-shared supernetwork trained with sandwich-style in-place distillation keeps this selection inexpensive. In a manufacturing-manual case study, extraction costs 13.7 percent of the unpruned model's judged quality and retrieval-grounded distillation returns it to within 4.6 percent, recovering two thirds of the loss, and the same assistant runs across three heterogeneous edge tiers at 1.3 to 5 watts standby.


### Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems
**Authors**: Yihang Chen, Yuxiang Chen, Yuxuan Huang, Meng Fang, Weilin Luo, Jun Wang

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02750v1](https://arxiv.org/pdf/2609.02750v1)

**Abstract**: Multi-agent LLM systems commonly use an orchestrator to decompose a task for a team of workers and then improve through textual reflection. Despite strong empirical results, these systems lack a unified account of coordination, memory improvement, and the role of external verification. We model orchestrator-worker interaction as a bilevel coordination game: under bounded coupling, the workers' local-update game is an approximate potential game whose equilibrium slack is controlled by decomposition quality. We then analyse reflection as stochastic movement over semantic memory states. For free-form reflection, we derive a finite-time upper bound, prove worst-case tightness, and give a positive lower bound under a falsifiable persistent-harm condition. We further prove an information-theoretic impossibility result: no gate that observes only the generated transcript can improve uniformly over text-indistinguishable environments, whereas an environment-grounded gate can. Motivated by this separation, we introduce Stochastic Reflective Memory Ascent (SRMA), which accepts a candidate memory only after a grounded evaluation risk strictly decreases. Under calibration and non-degenerate corrective mass, SRMA converges exactly, geometrically or polynomially; matching constructions show that both rate regimes are order-tight. We also provide confidence gating for stochastic evaluation and re-anchoring guarantees for piecewise-stationary environments. Experiments instantiate these objects with environment-grounded metrics and test the predicted coordination and drift laws. On 500 SWE-bench instances, the complete Kimi-based system resolves 72.2% versus a 70.8% public mini-SWE-agent reference. Code: https://github.com/YihangChen9/Bilevel-Coordinated-Reflection


### Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills
**Authors**: Jianlyu Chen, Yuyang Hu, Hongjin Qian, Jiawei Liu, Wenqing Wei, Xiaolong Chen, Defu Lian, Zhicheng Dou, Chaozhuo Li, Qiwei Ye, Zheng Liu

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02749v1](https://arxiv.org/pdf/2609.02749v1)

**Abstract**: Autonomous agents are beginning to carry out machine-learning (ML) research end to end. These agents combine a model backbone with a harness for planning, execution, memory, and verification, but this architecture still leaves domain-specific know-how outside the agent. We call this missing layer operational knowledge, the know-how that separates knowing a method from making it work. That knowledge is not absent from the field. It appears in repositories and papers, but in forms written for human readers and too large to load during a task. Once distilled into compact, verified skills, this knowledge can be reused across tasks rather than rediscovered during each run.
  We present DisCo, a skill-powered research agent that creates skills and uses them during research. Its distillation runs in two complementary forms: task-agnostic, condensing the field's widely used repositories into reusable skills, and task-oriented, producing the skills a concrete task calls for. The former, applied across the open ecosystem, yields the AREX-Skill Library, with 5,000+ verified skills distilled from 1,000 widely used ML repositories and organized into 20 areas and 178 capability families. With the GPT-5.5 backbone, research harness, and downstream execution budget held fixed, the skill-equipped research agent scores 134.3% higher on MLE-bench, 34.4% higher on PaperBench, 9.2% higher on FrontierCS, and 14.0% higher on PassNet than the same agent without skills. These gains come from adding distilled operating context under that fixed setup.


### Loom: Weaving Diagnostic Strands into Free-Text Consensus via Embedding-Space Reweighting
**Authors**: Ron Begleiter, Katya Egert Berg, Gilad Saban, Gil Shabat

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02649v1](https://arxiv.org/pdf/2609.02649v1)

**Abstract**: Aggregating noisy, conflicting textual hypotheses into a reliable consensus is a fundamental challenge when deploying NLP systems in real-world industrial settings. While monolithic Large Language Model (LLM) agents offer unbounded expressivity for tasks like Root Cause Analysis (RCA), they suffer from context limits, compounding hallucinations, and prohibitive inference latency. Traditional weak supervision offers statistical rigor but is mathematically restricted to discrete classes. We present Loom, a generative consensus framework deployed for real-world RCA that bridges these paradigms. Loom aggregates open-form hypotheses emitted by modular heuristics (diagnostic templates dynamically populated with episode-specific entities, times, and metrics) by projecting them into a continuous embedding space, and resolves conflicting signals with an iterative centroid-based reweighting algorithm. The resulting consensus weights ground a single lightweight LLM synthesis step. Evaluated on the OpenRCA benchmark, Loom occupies the accuracy--efficiency Pareto frontier: it matches a state-of-the-art autonomous agent on Bank and Market-2 and trails on Market-1 and Telecom, while using a single LLM call per incident on all four datasets ($\sim$26$\times$ faster; $\sim$33$\times$ with an 8B-parameter synthesizer). We discuss our deployment experience, highlighting lessons learned regarding the trade-offs between agentic depth and inference latency, negative results in redundancy detection, and how deterministic consensus fosters trust among Subject Matter Experts~(SMEs).


### Collective creativity in hybrid societies
**Authors**: Mason Youngblood, Katie Mudd, Manuel Anglada-Tort, Cameron Jones, Elena Miu, Diana Omigie, Margaret Schedel

**Published Date**: 2026-09-02

**Updated Date**: 2026-09-02

**PDF Url**: [2609.02620v1](https://arxiv.org/pdf/2609.02620v1)

**Abstract**: Generative AI is changing how cultural artifacts are created and circulated, and with it our understanding of creativity itself. Researchers disagree about whether these tools enrich or impoverish culture, and we argue that much of that disagreement comes from conflating two distinct components of creativity: novelty, a property of single artifacts, and diversity, a property of populations. We argue further that creativity in the context of generative AI is best understood as a property of hybrid collectives, or populations of interacting people and algorithms, rather than of individuals. AI-assisted ideation reliably raises the novelty of individual output while narrowing diversity in the aggregate, but this is not an inevitable consequence of putting machines in the loop. Because humans and models search in complementary ways, mixed groups can outperform and out-diversify groups of either kind alone, and machine-discovered solutions can enter human culture and persist there. What decides the outcome is composition: which agents are present, in what proportion, and how they are connected. The question is no longer whether AI helps or harms creativity, but which mixtures let individual gains accumulate without eroding collective diversity.


