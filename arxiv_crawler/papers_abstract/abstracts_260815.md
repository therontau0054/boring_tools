# Abstracts of Papers

## World Model
### AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design
**Authors**: Yaxin Luo, Haobin Jiang, Jialv Zou, Xu Huang, Wenhao Yan, Haodong Li, Zhengrong Yue, Jing Li, Xiaofu Chen, Xiaohan Zhao, Jiacheng Liu, Jiacheng Cui, Zhiqiang Shen, Xiaotong Li

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13560v1](https://arxiv.org/pdf/2608.13560v1)

**Abstract**: Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal harness system should align with human design priors and accumulate reusable experience through empirical exploration to drive recursive self-improvement, existing paradigms remain static and fall short of this capability. In this paper, we present AutoDesign, a framework that aligns with human design priors, where a meta-harness optimizer guides a code agent to recursively improve harness based on rollout feedback. To instantiate and evaluate this framework, we focus on the academic paper-to-poster generation task and introduce PosterBench, comprising a 100-paper Main Track spanning five disciplines and PosterBench-mini, a shared 10-paper subset for controlled evaluation. On the PosterBench Main Track, AutoDesign achieves the highest score of 78.32, surpassing the closed-source commercial system Claude Design by 7.45 points. Across seven controlled code-agent-model configurations, integrating the learned DesignHarness consistently improves performance, increasing the average PosterBench Score from 54.99 to 67.39 (+12.4%). In a fully autonomous long-horizon loop, it executes 253 tool calls and 11 editing turns within 40 minutes for under $3, reaching average conference-poster quality in human evaluation. A system-blind human study further demonstrates that AutoDesign achieves the highest human preference among evaluated systems.


### OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
**Authors**: Bobo Li, Hao Fei, Tianjie Ju, Mong-Li Lee, Wynne Hsu

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13558v1](https://arxiv.org/pdf/2608.13558v1)

**Abstract**: Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the agent. We introduce OmniScientist, an end-to-end, omni-modal AI scientist that conducts multidisciplinary research directly from heterogeneous raw evidence. A perception layer and 3 autonomous agents for ideation, experiment, and writeup operate within a deterministic pipeline, allowing observations to shape research questions, experimental decisions, and final claims throughout the research lifecycle. By running idea, rigour, and claim checks in code, the system enforces novelty screening, statistical validity, execution provenance, and numerical traceability. We evaluate OmniScientist on 36 real-data cases spanning 5 discipline families, 4 families of scientific evidence, and modalities including images, signals, audio, video, 3-D structures, trajectories, tables, formulae, and graphs. The system completes the full path from raw data to a compiled manuscript in all 36 cases and achieves a mean overall paper score of 6.3 with the reference reasoning backbone. In paired comparisons against a blind variant that receives only precomputed scalar features, direct perception improves all 7 evaluation dimensions and wins 85% of head-to-head judgments. These results show that lifecycle-wide perception is essential for evidence-grounded scientific discovery and provides a practical path toward broadly capable AI scientists.


### PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives
**Authors**: Kaixin Ding, Xi Chen, Minghong Cai, Zhiyuan Xu, Yiyang Wang, Yuxiang Lu, Junyi Li, Shuyang Chen, Yuan Gao, Xin Tao, Pengfei Wan, Hengshuang Zhao

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13552v1](https://arxiv.org/pdf/2608.13552v1)

**Abstract**: Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long sequences. However, fairly comparing these interactive models remains challenging. In practice, a human player typically evaluates a world model by pursuing long-horizon objectives through interaction. For example, a user may turn around 360 degrees to see whether the environment remains consistent, or walk into the water and inspect whether realistic water ripples are generated. The action sequence required to achieve the same objective may vary substantially between models, making fixed action-conditioned evaluation unsuitable for cross-model comparison. To address this, we employ multi-modal Agent Players to interact with world models toward specified long-horizon objectives. Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective. To evaluate performance thoroughly, we assess models along four core dimensions: geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution. In addition, we incorporate basic ability metrics for video quality and controllability. Experiments across nine state-of-the-art world models reveal that current models remain unreliable on long-horizon interactive objectives, particularly in maintaining spatial consistency and persistent state evolution. Code and data are available at https://github.com/kxding/PlayWorld.


### QuoteBench: How Matched Scores Can Hide Command-Path Failures
**Authors**: Shangao Li, Yao Zhang, Volker Tresp, Yuanyuan Yang

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13547v1](https://arxiv.org/pdf/2608.13547v1)

**Abstract**: LLM coding agents issue Bash commands through interfaces that may serialize, wrap, and reparse model output. Matched execution scores alone cannot distinguish command-generation errors from failures introduced after generation. QuoteBench measures this boundary with exact final-state validation on 56 one-shot tasks from 14 incident-derived families, crossing the generation contract with the execution transport around one deliberately unescaped added parser. Escaping at the interpolation point reproduces each replayed reply's raw-path outcome, so any recovery under a disclosed boundary must come from the model changing its generation. Across eight same-window configurations, replaying the same reply through the added parser lowers success by 55.4 to 73.2 percentage points; disclosure recovers 30.4 to 60.7 points for six configurations, and zero or slightly negative for the other two. Raw generation is nearly saturated at the frontier; boundary adaptation is what still separates models. GPT-5.6-sol's matched gap of -3.6 points hides -64.3 points of damage and +60.7 points of compensation. The deployment configuration reorders models: one reversal among 26 comparable pairs is unambiguous and four more sit on single-task margins. Evaluations of command-issuing agents should report the model configuration, generation contract, execution path, operating point, and final-state validator rather than treat a matched score as an intrinsic model property.


### Alaya-EVOKE: From Linear-Scaling Supervision to Endless World
**Authors**: Yuanyang Yin, Gongxuan Wang, Yifan Zhan, Chuanhao Li, Kaipeng Zhang, Feng Zhao

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13546v1](https://arxiv.org/pdf/2608.13546v1)

**Abstract**: Interactive world models must support persistent memory, responsive interaction, and long-horizon generation, yet these requirements place conflicting demands on the model. Maintaining history in the denoiser context or key-value cache incurs growing cost, forcing a trade-off between session length and retained memory, while low-latency interaction relies on few-step generation whose capabilities are bounded by its teacher. Evoke addresses both limitations by externalizing persistent world state and redesigning the teacher for long-horizon interactive generation. Scene geometry is maintained in an external, camera-indexed world state bank, from which only view-relevant information is retrieved, keeping the denoiser context bounded as the session grows. Rather than treating the teacher as a fixed generator, we design it for long-horizon supervision: its sparse attention combines chunk-wise grouping, retrieval of selected distant frames, and a linear-attention global state, yielding linear growth in memory and compute while enabling supervision over long horizons. Such supervision exposes content drift that stays locally plausible within short windows, while per-chunk conditioning enables prompt changes and event control throughout the sequence. A 30-second distribution-matching objective, applied under self-forced rollouts, transfers both capabilities to a three-step student that uses no classifier-free guidance, improving resistance to long-term drift while preserving responsive conditioning. With bounded context and recurrent external memory, Evoke supports open-ended, continuously evolving generation; on a single H200 at $384\times 640$, each $1.5\,\mathrm{s}$ chunk is generated in $2.11\,\mathrm{s}$. As a three-step world model, Evoke achieves state-of-the-art performance on WBench while remaining competitive on VBench-Long and VBench-2.0.


### LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure
**Authors**: Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13545v1](https://arxiv.org/pdf/2608.13545v1)

**Abstract**: Modern language models are trained on heterogeneous web-scale text corpora. Consequently, studying knowledge and skill acquisition is difficult, as prior exposure to related content is hard to characterize. To address this challenge, we introduce LITTLECURRICULUM, a curated 88B-token pretraining corpus tailored to U.S. elementary school material, explicitly excluding concepts, facts, and vocabulary taught above Grade 5. Training a 5B-parameter LLM from scratch on LITTLECURRICULUM yields LITTLELEARNER, a model with sufficient language competence for open-ended evaluation, yet with clear knowledge and capability boundaries mapped to interpretable curriculum guidelines. We release LITTLECURRICULUM and LITTLELEARNER as a developmentally restricted sandbox to study how models acquire, represent, and use data under a well-defined training scope. We illustrate the sandbox's utility in a first suite of experiments on injecting new knowledge through post-training and in-context learning. These methods let LITTLELEARNER better utilize existing knowledge, but do not raise out-of-scope capabilities. Our findings underscore the value of this controlled environment for future investigations.


## Generation
### Vero: Can AI Agents Build Formally Verified Software Repositories?
**Authors**: Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang, Soonho Kong, Jingxuan He, Dawn Song

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13522v1](https://arxiv.org/pdf/2608.13522v1)

**Abstract**: AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can make coherent implementation and proof choices across real multi-module codebases. To bridge this gap, we introduce Vero, the first benchmark to evaluate joint implementation and proof synthesis at the repository level. Vero contains 43 multi-module instances sourced from real-world repositories spanning Python, Dafny, Verus, and Coq, and covering diverse domains from cryptographic protocols to distributed systems. Each instance consists of a multi-module Lean 4 repository with predetermined API interfaces, manually curated formal specifications, and reference implementations, supporting both proof-only and code-and-proof evaluation modes. To improve benchmark reliability, Vero also includes an audit mechanism where agents are allowed to formally prove unsatisfiability of provided specification or incorrectness of reference code, which surfaces and corrects latent code and specification errors during curation. We evaluate frontier coding-agent configurations with Lean toolchain access. The strongest agent fully solves only 27 of 43 instances and closes no specifications on the hardest repositories. Vero provides a concrete testbed for measuring progress toward repository-scale verified software synthesis, where current agents still fall short. We release the benchmark, curation pipeline, and evaluation harness at https://github.com/sunblaze-ucb/vero.


### Bagging Robustly Learns VC Classes with Linear Sample Complexity
**Authors**: Omar Montasser

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13514v1](https://arxiv.org/pdf/2608.13514v1)

**Abstract**: We revisit the problem of learning predictors robust to adversarial examples at test-time. We prove that VC classes are adversarially robustly learnable with sample complexity linear in the VC dimension $d$, providing an exponential improvement over the previous upper bound of Montasser, Hanneke, and Srebro (2019). Remarkably, this result is achieved with a simple improper algorithm that combines the classic heuristic bagging (bootstrap aggregation) of Breiman (1996) with robust empirical risk minimization (RERM). Our algorithm computes RERMs on $O(d^\star)$ independent bootstrap samples and outputs their majority vote, where $d^\star$ denotes the dual VC dimension. We complement this result with a lower bound showing that this is unavoidable: in general, any learner in this oracle model requires $Ω(d^\star)$ calls to an RERM oracle, even when given arbitrarily many training examples.


### On the Structural Limits of Machine Learning Decision Systems: An Information-Theoretic, Interaction-Based, and Stochastic-Dynamical Perspective
**Authors**: Nestor R. Barraza, Gabriel Pena

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13510v1](https://arxiv.org/pdf/2608.13510v1)

**Abstract**: Machine learning procedures are commonly evaluated in terms of predictive accuracy and computational efficiency. However, their achievable performance is fundamentally constrained by structural properties of the underlying data-generating process, which are formalized in terms of informational bounds. In this work we examine intrinsic limits of data-driven decision systems from an information-theoretic and interaction-based perspective. We analyze minimal achievable error in classification through Fano-type bounds and precision limits in parametric estimation via the Cramér-Rao inequality, emphasizing that such limits depend on the underlying model rather than on algorithmic sophistication alone. We further discuss how implicit assumptions, such as independence, ergodicity, and distributional stability, affect the validity of inferential procedures. Building on interaction-based modeling principles, we review typical frameworks such as Markov Random Fields and potential based representations for encoding dependence mechanisms. We also describe decision systems, including LLM-integrated agent architectures, as feedback-driven stochastic processes where state-dependent dynamics may induce emergent macroscopic behavior. This perspective highlights the importance of having adequate models for the data as a prerequi- site for expanding predictive capability, and situates algorithmic learning within the informational limits imposed by the models.


### Equivariant learning of a transferable three-dimensional classical density functional
**Authors**: Bingqing Cheng

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13506v1](https://arxiv.org/pdf/2608.13506v1)

**Abstract**: Liquids exhibit collective behavior that depends sensitively on thermodynamic conditions, interfaces and confinement, yet predicting each new state commonly requires a separate atomistic simulation. Classical density functional theory offers a reusable variational description, but its central excess free-energy functional is generally unknown, and learned approximations have largely remained restricted to planar or lower-dimensional settings. Here we show that this functional can be learned directly from fully three-dimensional equilibrium density fields while preserving spatial symmetry and variational consistency, without free-energy or chemical-potential labels. A single learned functional transfers across temperatures, system sizes and statistical ensembles, and recovers structure factors, the equation of state, liquid--vapor coexistence and interfacial broadening, none of which are used as training targets. Applied to complex three-dimensional geometries, it predicts the non-monotonic force associated with formation and rupture of a solvent-depleted bridge between colloids and adsorption in an interconnected gyroid pore. These results demonstrate that equilibrium density data can be converted into a transferable thermodynamic generator connecting microscopic liquid structure to response, phase behavior and collective phenomena.


### Intern-S2-Preview: Scientific Agentic Foundation Model
**Authors**: Lei Bai, Jiaqi Cao, Chiyu Chen, Guanzhou Chen, Kai Chen, Guangran Cheng, Erfei Cui, Xuanlang Dai, Shengyuan Ding, Shangheng Du, Yanhui Duan, Yue Fan, Youqing Fang, Quan Gan, Yuanyuan Gao, Jiaye Ge, Lixin Gu, Yuzhe Gu, Qipeng Guo, Junjun He, Xin Hong, Ming Hu, Zhouqi Hua, Haian Huang, Junhao Huang, Zixian Huang, Minxi Jin, Lingkai Kong, Alexander Lam, Zehao Li, Zonglin Li, Tianhao Liang, Dahua Lin, Junyao Lin, Tianyang Lin, Zhouhan Lin, Jiangning Liu, Jin Liu, Kuikun Liu, Wenran Liu, Yifei Liu, Yuhong Liu, Yuhong Liu, Zhoumianze Liu, Ziyan Liu, Ziyu Liu, Haijun Lv, Han Lv, Chengqi Lyu, Le Ma, Ningsheng Ma, Zerun Ma, Haoyang Peng, Runyu Peng, Jifei Shan, Zixin Shang, Kou Shi, Xiang Shi, Qisheng Su, Xuerui Su, Hao Sun, Xiao Sun, Yanan Sun, Yu Sun, Huanze Tang, Yinghao Tang, Wenhui Tian, Zhongbo Tian, Bingli Wang, Haomin Wang, Jiarui Wang, Jingzhi Wang, Rui Wang, Xiquan Wang, Yi Wang, Zhecan Wang, Ziyi Wang, Zun Wang, Rubin Wei, Lianyi Wu, Wen Wu, Yue Wu, Yuhan Wu, Zhenyu Wu, Zijian Wu, Shuhao Xing, Jun Xu, Xingle Xu, Xuenan Xu, Xiangchao Yan, Ziang Yan, Bowen Yang, Danni Yang, Lin Yang, Zhiqi Yang, Qian Yao, Haochen Ye, Peng Ye, Jinhui Yin, Jiashuo Yu, Dingbo Yuan, Fei Yuan, Yuhang Zang, Bo Zhang, Chao Zhang, Chen Zhang, Hongjie Zhang, Junming Zhang, Wenlong Zhang, Wenwei Zhang, Yiming Zhang, Zhuo Zhang, Ziyang Zhang, Haiteng Zhao, Penghao Zhao, Yibo Zhao, Zhonghan Zhao, Zhihang Zhong, Bowen Zhou, Peiheng Zhou, Xin Zhou, Xinyu Zhou, Yunhua Zhou, Dongsheng Zhu, Yicheng Zou

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13505v1](https://arxiv.org/pdf/2608.13505v1)

**Abstract**: Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific documents, interleaved image-text data, and diverse scientific corpora. Starting from the pretrained checkpoint, we apply a unified post-training pipeline consisting of supervised fine-tuning, scalable multi-task reinforcement learning (RL), black- and white-box agentic RL, and on-policy distillation. This pipeline is supported by practical techniques that improve rollout and training stability and efficiency, including partial rollout with off-policy correction, adaptive length regularization, online speculative decoding, robust multi-task optimization, and trace-aware experience assembly for agentic tasks. At the architecture level, Intern-S2-Preview-397B extends time series modelling from efficient long-sequence understanding to numerical forecasting, while Memory Decoder is studied as a separate memory-augmented path for rapid scientific specialization without modifying the frozen 397B backbone. Evaluations across scientific, multimodal, agentic, and general-purpose benchmarks show that Intern-S2-Preview-397B achieves competitive or leading results in multiple settings. The time series modules improve scientific signal understanding and forecasting on SciTS, while the separate Intern-MemDec-4B extension improves the Biology-Instructions average score from 56.92 to 60.32 without modifying the frozen 397B backbone.


### Sparse Orthogonal Regression Technique: A Spectral Framework for Equation Discovery, Approximation, and Integration
**Authors**: Sabin Roman, Ljupco Todorovski, Saso Dzeroski

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13504v1](https://arxiv.org/pdf/2608.13504v1)

**Abstract**: We develop the Sparse Orthogonal Regression Technique (SORT), a sparse spectral framework for learning orthonormal-basis expansions from noisy and irregularly sampled data. SORT estimates expansion coefficients directly from observations using L1-regularized regression, avoiding explicit quadrature or analytic inner-product evaluation. The central application is data-driven discovery of ordinary differential equations: vector fields are represented in chosen orthogonal bases and learned as sparse coefficient expansions. This provides a complementary route to symbolic regression, grammar-based discovery, and SINDy-style sparse identification by first recovering a compact spectral representation, which can later guide searches for simpler analytic forms. Across the dynamical-system experiments, SORT matches or improves upon library-based sparse-regression baselines when the basis is well adapted to the problem, and shows more stable degradation under sparse sampling, noisy derivative estimates, and representation mismatch. Specific examples illustrate why this representation is useful: if a finite library misses the problem-specific nonlinearity, the resulting model can fail. SORT is not immune to mismatch, but it shifts the problem away from brittle selection among generic terms to basis design adapted to the problem domain. The experiments also show that dominant low-order coefficients persist as model order increases, supporting order-consistent model growth. Beyond equation discovery, the same learned expansion supports nonlinear approximation and estimation of complex, high-dimensional integrals by coefficient readout. Overall, SORT provides a reusable intermediate representation for system identification, approximation, and integration, while making basis design an explicit part of the scientific modeling problem.


## VLA
### UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models
**Authors**: Yukun Dai, Mingzhe Dai, Tianshi Wang, Fengling Li, Jingjing Li, Lei Zhu

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13453v1](https://arxiv.org/pdf/2608.13453v1)

**Abstract**: Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks. UniTexture backpropagates gradients from the policy's action outputs to surface texture parameters through a differentiable renderer. It jointly optimizes the shared texture over a distribution of tasks, instructions, states, and viewpoints using a targeted action-space objective, steering predicted actions toward attacker-defined targets without optimizing a separate texture for each task. We evaluate UniTexture on OpenVLA and $π_{0.5}$ across diverse manipulation tasks and multiple evaluation settings. UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization. Together, these findings reveal shared cross-task vulnerabilities in multitask VLAs that can be systematically exploited through a single adversarial surface texture.


### FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving
**Authors**: Zekai Li, Yihao Liang, Hongfei Zhang, Jian Chen, Yesheng Liang, Zhijian Liu

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.12932v1](https://arxiv.org/pdf/2608.12932v1)

**Abstract**: Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control. The core challenge is structural: VLA inference is not a single bottleneck but a cascade of four. Visual encoding wastes compute on overlapping video frames; language-model prefill recomputes context that could be carried over from the previous timestep; reasoning tokens are generated serially despite low entropy; and flow-matching denoising applies uniform compute to a non-uniform velocity field. Addressing any one stage in isolation leaves the others untouched. We propose FlashDrive, an algorithm-system co-design framework that targets all four stages simultaneously. Our key insight is that each bottleneck admits a distinct, lightweight algorithmic shortcut: temporal overlap enables streaming KV-cache reuse across frames; the low per-token entropy and strong intra-block correlations of driving-domain reasoning make a non-autoregressive diffusion drafter highly effective for speculative decoding; and the velocity field's structure---sharp at the endpoints, flat in the middle---permits adaptive step caching that concentrates compute where it matters. Layered on system-level CUDA Graph compilation and kernel fusion, these techniques compound. Applied to Alpamayo 1.5-10B with W4A8 quantization, FlashDrive reduces end-to-end latency from 717ms to 151ms (4.7x) while leaving accuracy essentially unchanged: minADE6@6.4s shifts by only 0.08m, minADE1 improves, and closed-loop collision and off-road rates improve in simulation. By raising a 10B-parameter reasoning VLA from 1.4~Hz to 6.6~Hz on a single GPU, FlashDrive moves end-to-end autonomous driving substantially closer to real-time deployment.


### BrainWAM: Action-Space Coordination of Semantic Priors and Predictive Dynamics for Autonomous Driving
**Authors**: Bing Zhan, Shuyao Shang, Jiahao Gu, Shuo Lu, Yuan Xu, Zhao Wang, Yida Wang, Xueyang Zhang, Kun Zhan, Lue Fan, Zhaoxiang Zhang

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.12854v1](https://arxiv.org/pdf/2608.12854v1)

**Abstract**: Autonomous driving requires planning under both semantic constraints and predictive dynamics. Existing end-to-end driving approaches, however, typically emphasize only one side of this requirement: Vision-Language-Action (VLA) models exploit VLM priors for semantic reasoning, while World Action Models (WAMs) provide future-aware prediction through generative world modeling. This naturally motivates a unified planner that can leverage both semantic priors and predictive dynamics. However, we find that a naive combination through joint token-level attention suffers from an attention-allocation mismatch, where semantic shortcuts dominate the shared attention space and suppress predictive dynamics. Inspired by neuroscience evidence that complex behavior arises from coordination among functionally specialized systems, we propose BrainWAM, a structured action-space coordination framework that converts semantic reasoning and predictive world modeling into two specialized action-oriented pathways, and aligns them at the level of compact action representations. We further introduce an asynchronous rectified-flow inference strategy with decoupled video and action denoising, which shortens inference latency while preserving planning-relevant predictive context. BrainWAM reaches state-of-the-art performance on both NAVSIM v1 (89.5 PDMS) and NAVSIM v2 (89.6 EPDMS), consistently outperforming VLA-only or WAM-only methods, highlighting BrainWAM as a practical and promising direction for autonomous driving systems.


### Scaling Automatic Research Agents via World Models
**Authors**: Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, Huiyuan Chen, Haiyang Zhang, Chenlei Guo, Jingrui He, Zhenyu Liao

**Published Date**: 2026-08-12

**Updated Date**: 2026-08-12

**PDF Url**: [2608.12564v1](https://arxiv.org/pdf/2608.12564v1)

**Abstract**: Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes. Behind these gains, post-training (especially RL) plays a central role. In this paper, we identify a fundamental tension when scaling RL for these agents: the two components of every AutoResearch trajectory (agent generation and environment execution) scale in very different manners, since all generation shares compute through batching, while each execution occupies its exclusive sandbox and real machine time. As a result, the environment execution dominates the training cost and becomes the bottleneck as trajectories grow. To resolve this tension, we propose World Model RL (WMRL), which replaces environment execution with a world model to remove this bottleneck. Additionally, the world model can be imperfect, as its rewards are corrupted by bias and noise. Therefore, we further equip WMRL with two mitigations, Online Debiasing and Inverse-Variance Denoising, which offset the bias and suppress the noise respectively. Theoretically, we prove that both mitigations of WMRL strictly improve the convergence guarantee. Empirically, WMRL accelerates training by 3-4x on various tasks at different agent scales, while exceeding the performance of standard RL baselines. Moreover, our post-trained 4B and 9B agents outperform much larger open-weight agents of 48B and 120B on held-out benchmarks. Beyond AutoResearch, WMRL also transfers to post-training embodied VLA policies, which demonstrates the generalizability of our method.


## Agent
### MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination
**Authors**: Saisha Shetty, Satvik Tripathi, Austin Lin, Colin Zhao, Theodore Kim, Don Enwerem, Jacinta Arnold, Shahriar Faghani, Tessa S Cook

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13476v1](https://arxiv.org/pdf/2608.13476v1)

**Abstract**: We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a plain-language description, eliminating manual prompt engineering. The framework supports both API-based and local CPU-compatible deployments and is entirely configurable via YAML, without code modifications. MARC is designed to be model-agnostic, interpretable, and accessible to clinical domain experts without programming expertise. The full framework is available at https://github.com/Penn-RAIL/MARC-v1.


### AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation to Sizing Using Large Language Models
**Authors**: Mohammed Ayman Habib, Rylan Hart, Morteza Fayazi

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13472v1](https://arxiv.org/pdf/2608.13472v1)

**Abstract**: Analog circuit design is a time-consuming, iterative process in a nonlinear and high-dimensional design space that relies heavily on expert intuition. Among recent developments, LLMs have introduced a promising approach by bringing natural language reasoning to circuit design tasks. The majority of conventional LLM-based approaches provide fragmented solutions that focus either only on sizing or topology generation. These methods require adding specific technical knowledge manually, which is inefficient and prone to hallucinations during circuit sizing. Moreover, the inherent trade-off in meeting different specs makes current approaches iterative and tedious. Another shortcoming is the inability to create innovative topologies, which may lead to sub-optimal designs due to reliance on conventional topologies. In this paper, we present AaLLM, an open-source end-to-end multi-agent LLM workflow that takes user specs as input and outputs the appropriate netlist, encompassing both topology generation and circuit sizing. AaLLM automates the creation of a relevant knowledge base from research papers and textbooks to combat tedious manual data collection. A RAG model is implemented to emulate circuit design expertise using this knowledge base. Moreover, AaLLM uses a novel tri-agent feedback system comprising a Designer that determines circuit component values, a Critic that scrutinizes these values, and an Evaluator that minimizes circuit sizing iterations by arbitrating between the other two agents. AaLLM-generated novel topologies achieve a figure of merit (FoM) comparable to that of known topologies, and up to 3x higher for certain circuits. Testing on several circuit topologies, our results show a 3x - 4.5x decrease in the number of SPICE calls at inference when compared to SOTA multi-agent LLM pipelines. The results also show a 40x decrease in wall-clock time compared to existing approaches.


### MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification
**Authors**: Daniel Perkins, John Squires, Janou Milligan, Chandra Raskoti, Linda Ungerboeck

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13463v1](https://arxiv.org/pdf/2608.13463v1)

**Abstract**: Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs. ARMDIL is an ensemble that uses a multimodal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. Our diverse ensemble employs convolutional neural networks (ResNets), self-supervised representation learners (SSL), and vision-language models (VLMs), each trained on a unified label space constructed from multiple image datasets with differing distributions and characteristics. Empirical evaluations illuminate the distinct capabilities and vulnerabilities of each architecture across disparate visual domains. Crucially, we show that ARMDIL effectively navigates these trade-offs, performing competitively with specialized training-based routers. Furthermore, it drastically improves adaptability by allowing new information to be integrated via simple prompt modifications, while enhancing interpretability through natural language reasoning traces. These advances in cross-dataset image classification pave the way for more reliable general-purpose vision systems such as AI assistants and autonomous robots.


### A Unifying Perspective on Causal World Models: From Observations to Representations to Structure
**Authors**: Avinash Kori, Fabrizio Russo

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13456v1](https://arxiv.org/pdf/2608.13456v1)

**Abstract**: World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entity interactions, and entity-to-environment interactions that determine and explain the dynamics of a system. We provide a formal definition of Causal WMs (CWMs) grounded in the tasks they are intended to support, connecting world modelling with existing work in causal representation learning, object-centric learning, causal discovery, structural causal models, and model-based decision-making. Finally, we relate CWMs to the literature on identifiability, clarifying when the components of a WM can be recovered from data and up to which equivalence. With this, we ground WMs in representations and structures that support causal reasoning and informed decision-making.


### RAIL: An Automatic Classifier of the Artificial Intelligence Readiness Level
**Authors**: Juan Irving Vasquez, Juan Terven, Laura-Ivoone Garay-Jimenez

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13428v1](https://arxiv.org/pdf/2608.13428v1)

**Abstract**: Assessing the maturity of artificial intelligence technologies is essential for investment decisions, project management, and policy monitoring, yet the available readiness frameworks are heterogeneous and difficult to apply automatically: the adaptation of Technology Readiness Levels to AI lacks AI-specific gating criteria, the Machine Learning Technology Readiness Levels presuppose access to internal process artifacts, and AI/data readiness dimension models employ scales that resist direct comparison. This paper makes two contributions. First, we unify these three frameworks into the Unified AI Readiness Level (AIRL), a nine-level ordinal scale built on an environmental evidence ladder and complemented by dimensional caps (covering specification, data existence, data quality, data legality, expert knowledge, and algorithmic maturity) together with a generality-anchoring rule and explicit assignment disciplines, so that a readiness level becomes decidable from a natural-language description of the work alone. Second, we propose RAIL (Readiness Assessment via Independent LLM-experts), a panel-of-experts classifier that operationalizes the scale: one evidence agent and six independent dimension agents, each a large language model with a narrowly scoped mandate, deliver verdicts that a deterministic minimum rule aggregates and a chief expert reviews under asymmetric authority, confirming or lowering the panel's recommendation but never raising it above the caps. The method was tested in the analysis of several research works showing consistency and avoiding overestimation from monolithic LLM classifiers.


### Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation of Think and Memory Processes
**Authors**: Aimilios Hadjiliasi, Louis Nisiotis

**Published Date**: 2026-08-13

**Updated Date**: 2026-08-13

**PDF Url**: [2608.13420v1](https://arxiv.org/pdf/2608.13420v1)

**Abstract**: Embodied intelligent virtual agents are expected to operate as persistent, adaptive, and context-aware entities within complex virtual and Metaverse worlds. However, implementing cognitively capable agents in such environments is conceptually and technologically challenging. Among a range of blueprints and development approaches, the Cognitive Embodied Agent Architecture (CEAA) has been developed as an implementation-oriented framework for architecting components of perception, memory, reasoning, planning, and embodied action. Considering the recent advances in edge computing and generative AI language models, this paper explores the use of Small Language Models (SLMs) to support edge-based operation of selected CEAA components, focusing on "Think" and "Memory" as processes central to cognitive orchestration and persistence of virtual agents in interactive virtual worlds. An edge-based virtual agent gateway system was developed and evaluated on an NVIDIA Jetson Orin NX using Qwen2.5 models of different sizes, exploring the system's capability to process service requests and handle memory-driven conversations. A series of simulation experiments evaluated routing accuracy, memory-read performance, and latency, demonstrating an SLM-driven prototype agent system that partially implements selected CEAA processes to support the development of embodied agents whose cognitive "brain" can operate efficiently and contextually for interactive experiences in immersive virtual worlds.


