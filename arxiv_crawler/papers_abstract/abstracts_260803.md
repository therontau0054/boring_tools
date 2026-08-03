# Abstracts of Papers

## World Model
### Scaling Properties of Text Conditioning in Visual Generation
**Authors**: Zilong Chen, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29679v1](https://arxiv.org/pdf/2607.29679v1)

**Abstract**: We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measures: a white-box likelihood metric (GPG) and a black-box attribute metric (ED). Across controlled training runs, the converged diffusion loss decreases approximately linearly with GPG and follows a power law with ED. Guided by these scaling properties, we improve \emph{diffusability} by constructing structured prompts with semantic and geometric annotations derived from images, and improve \emph{promptability} by training a prompter through supervised fine-tuning, cold-start, and verifier-gated on-policy distillation. The resulting system outperforms all evaluated open-weight models on nearly every compositional, reasoning, and world-knowledge benchmark, while matching or surpassing the strongest closed-weight models on most evaluations.


### GQ-FSL: Green Quantized Federated Split Learning
**Authors**: Idan Roth, Lutz Lampe

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29659v1](https://arxiv.org/pdf/2607.29659v1)

**Abstract**: Deploying state-of-the-art deep neural networks (DNNs) at the wireless edge is severely bottlenecked by the strict energy and resource constraints of mobile devices. While federated split learning (FSL) mitigates on-device computation by offloading workloads to an edge server, this may introduce systemic overheads, while the continuous exchange of cut-layer data, and submodels still incurs significant energy consumption (EC). To address this, we propose a green quantized FSL (GQ-FSL) framework that incorporates stochastic quantization for both local collaborative training and wireless transmissions. Notably, GQ-FSL supports asymmetric precision levels for the client- and server-side submodels, effectively decoupling device energy constraints from global convergence degradation. To quantify these tradeoffs, we develop parameterized energy models for the split architecture and derive a theoretical convergence bound under statistically heterogeneous data. Building on that, we formulate a joint optimization problem to configure the DNN split point and precision levels, minimizing the total system EC while satisfying a strict target accuracy constraint. Ultimately, we demonstrate that GQ-FSL enables large-scale DNN deployment on resource-constrained devices, achieving superior energy efficiency compared to quantized federated learning and full-precision FSL.


### Non-reciprocal torques guide self-assembly of active particles into clusters with controllable function
**Authors**: Till Welker, Yukino Fujiya, Holger Stark

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29651v1](https://arxiv.org/pdf/2607.29651v1)

**Abstract**: Self-assembly of constituents determines structure formation in the microscopic world. Attractive forces can assemble active particles into colloidal machines, but they do not fix the particles' orientations, which limits control over the machine's function. We demonstrate that non-reciprocal turn-towards torques not only assemble active particles into clusters, without requiring attractive forces, but also link particle orientations to the cluster configuration. Symmetry then dictates whether the cluster is static, rotates, or translates. In small systems, the particle number uniquely determines the stable configuration and function. In larger systems, there are multiple stable configurations with distinct functions, and tuning the torque strength allows us to bias towards the desired function, such as a run-and-tumble motion. Because the interactions driving assembly can be switched on and off, the clusters self-assemble when needed. For such a "just-in-time" self-assembly to be practical, fast assembly is necessary. We show that stochastic resetting, implemented by briefly turning off propulsion and torque, significantly speeds up self-assembly by avoiding slow pathways. Together, our findings demonstrate that non-reciprocal torques can rapidly assemble active particles into colloidal micromachines with controllable function.


### Bootstrapping Self-Supervised Learning of Binary Classification Using Error Bounds: A Case Study on a Robotic Insertion Task
**Authors**: Zebin Duan, Norbert Krüger, Juan Heredia, Thorbjørn Mosekjær Iversen, Frederik Hagelskjær

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29640v1](https://arxiv.org/pdf/2607.29640v1)

**Abstract**: Flexible manufacturing requires rapid deployment of solutions and minimal setup time to remain competitive. An essential attribute is the ability to control error levels, as failures can range from minor performance degradation to severe equipment damage. However, conventional deployment often involves extensive setup, data collection, model training or parameter tuning, and system testing, resulting in significant delays that hinder commercial feasibility. We propose a data engine which gathers data and improves its performance while executing the task. The data engine consists of two classifiers, a fast model prediction and expensive verification. First, a model prediction is performed and based on the confidence level of the prediction, the expensive verification can be used. By adjusting the confidence level, users can control the level of tolerable error.
  Our method is implemented on a real-world robotic insertion task, which uses force data for the model prediction. The system applies UMAP dimensionality reduction and uses Wilson-Score to compute the confidence bounds of the prediction. Results demonstrate the ability to learn and reduce the need for expensive verifications over time, while staying within the set error-rate. The results highlight the potential of confidence bounds in self-improving models to enhance reliability in robotic classification task.


### FlexComposer: Unified Video Compositing from Images to Dynamic Footage with Flexible Trajectory Control
**Authors**: Songchun Zhang, Sitong Guo, Xianghao Kong, Pengwei Liu, Yuwei Guo, Lvmin Zhang, Anyi Rao

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29627v1](https://arxiv.org/pdf/2607.29627v1)

**Abstract**: Generative video compositing, which involves inserting external assets seamlessly into existing video sequences, is essential for content creation and visual effects. However, existing approaches suffer from a control-fidelity trade-off: they either hallucinate motion from static images, failing to preserve the dynamics of pre-animated assets, or lack fine-grained spatial control for precise asset placement along user-defined trajectories. We propose FlexComposer, a unified framework that standardizes video compositing as a trajectory-guided conditional generation task, enabling the seamless integration of both static images and dynamic footage. Our approach introduces three key designs: (1) a Unified Canonical Foreground Representation that decouples an object's intrinsic motion from its global displacement, standardizing heterogeneous inputs into a stabilized, centered latent space; (2) a Spatial-Aware Latent Injection strategy that exploits the translation equivariance of VAE latent spaces to transport canonical features onto target trajectories via a parameter-free mechanism; and (3) a Hybrid Dataset and Synthetic-to-Real Curriculum that synergizes procedural simulation, real-world cinematic footage, and generative data to implicitly learn physically plausible illumination and shadow harmonization. This unified design handles diverse inputs from product photos to dynamic subjects achieving high-fidelity motion control and environmental integration without the need for explicit 3D reconstruction or auxiliary learnable adapters. Extensive experiments demonstrate that FlexComposer outperforms state-of-the-art methods in visual quality, temporal consistency, and trajectory adherence.


### The Theoretical Foundation of Socratic Tests: Dynamic, Multimodal, Conversational Examinations
**Authors**: Ilya Mikhelson

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29624v1](https://arxiv.org/pdf/2607.29624v1)

**Abstract**: Traditional static assessments rely on a subtractive, deficit-based grading model that often penalizes ambition and obscures diagnostic feedback. Conversely, traditional face-to-face oral examinations introduce severe construct-irrelevant variance by exacerbating performative anxiety and the sociological power imbalances inherent to academic hierarchies. This paper presents the theoretical foundation for the "Socratic Test," an automated, computer-mediated conversational assessment. By integrating Dynamic Assessment principles, multimodal workspaces, Bloom's Taxonomy for real-time proctoring, and the SOLO Taxonomy for structural evaluation, the Socratic Test actively maps a student's cognitive boundaries. This paper formalizes the use of graduated scaffolding to quantify the Zone of Proximal Development (ZPD) and details a non-compensatory, additive grading architecture that prioritizes mastery over penalty and human-AI alignment to ensure unprecedented measurement reliability.


## Generation
### Sign compression for Muon: SignMuon, MuonSign, and the Limits of Error Feedback
**Authors**: Maria Smirnova, Alexey Kravatskiy

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29674v1](https://arxiv.org/pdf/2607.29674v1)

**Abstract**: SignMuon compresses the Muon update to one bit per parameter by taking its elementwise sign, providing the most direct way to run a matrix-aware optimizer under an extremely low communication budget. It outperforms SignSGD in practice, yet it can ascend even on a linear function. Signing the gradient before the Linear Minimization Oracle (LMO), rather than after, does not repair this: we construct a small explicit instance on which sign-before (MuonUSign) and sign-on-both-sides (MuonSign) ascend as well, so no placement of the sign around the oracle descends in general. Error feedback, the standard remedy for a biased compressor, does not rescue SignMuon: when applied to Muon's output, error feedback can fail for every smoothness constant, step size, and momentum. Applied to the gradient, error feedback does work, and EF21-MuonUSign and EF21-MuonSign attain the standard $\mathcal{O}(T^{-1/2})$ rate for the squared gradient norm on smooth nonconvex problems, the latter at one bit in each direction. Experiments then reverse the ordering: across centralized CIFAR-10, federated CIFAR-10, and the nanoGPT speedrun, the strongest compressed method is consistently sign-after-the-LMO, precisely the placement we prove divergent, with the provably convergent variants trailing it. Compressing after the LMO, a heuristic, matters more at these scales than the guarantee does.


### Freeze, Then Select: Structured Field Adapters and Stability-Validated Weak Selection for PDE Discovery from Sparse Observations
**Authors**: Juncheng Zhong, Chenghuang Shen, Jianfeng Liu, Zhengdong Xiao, Longjiu Luo, Qianrong Wang, Wenjun Xu, Wenlian Lu

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29665v1](https://arxiv.org/pdf/2607.29665v1)

**Abstract**: PDE discovery from sparse observations requires reconstructing a continuous field and selecting the correct differential terms. Our analysis of optimization paths in coupled neural PDE discovery reveals three behaviors: the exact support can persist to the end of training, appear only transiently, or fail to emerge. To decouple equation selection from neural optimization, we develop a freeze-then-select method combining a structured field adapter with Stability-Validated Weak Selection (SVWS). Trained from observations without a PDE residual, the adapter factorizes the field into learned spatial features and temporal coefficients represented by cubic splines. After freezing the field, SVWS identifies recurrent terms across independent weak-form systems, refits candidate supports, and selects the final equation on held-out weak-form systems. Beyond fixed libraries, we apply the same principle to expressions generated by genetic programming and recover the power-law form of an unknown nonlinear diffusion function from sparse, noisy observations. Across all six sparse MDBench regimes, our method attains the highest exact support recovery rate, with its clearest gains over classical and neural baselines on challenging Kuramoto-Sivashinsky dynamics.


### AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers
**Authors**: Tianyu Huai, Tingshuo Fan, Xinchi Chen, Yining Zheng, Yuxin Wang, Shuang Chen, Jie Zhou, Xuanjing Huang

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29626v1](https://arxiv.org/pdf/2607.29626v1)

**Abstract**: As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter decisions. To address this gap, we introduce AgentHPOBench, a sequential benchmark comprising 30 executable machine learning tasks across seven research categories. Each task begins with a validated baseline run, after which an agent performs several sequential interventions. At each step, the agent observes the accumulated configurations, metrics, and logs before proposing the next valid configuration. We evaluate 12 widely used agents and conventional HPO baselines under a unified protocol. The results show that current agents exhibit measurable experimental optimization ability across domains, but still face clear limitations in sustained iterative refinement, complex log diagnosis, and consistent progress toward reported reference performance.


### When Does On-Policy Interaction Help? Representational Tradeoffs in Value-Based Imitation Learning
**Authors**: Luca Viano, Antoine Moulin, Audrey Huang, Volkan Cevher, Philip Amortila, Dylan J. Foster

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29617v1](https://arxiv.org/pdf/2607.29617v1)

**Abstract**: Imitation learning (IL)---training an agent to replicate expert behavior from demonstrations---underpins applications from robotics to language model training. Standard approaches such as Behavior Cloning (BC) are known to suffer from compounding errors and performance plateaus, particularly when the learner cannot perfectly represent the expert's policy (as is typical, e.g., in distillation). Two interventions are widely understood empirically to improve performance: querying the expert interactively along the learner's own trajectories, and using value function estimation en route to generating a policy rather than directly fitting the expert's full action distribution.
  We investigate the nature of these improvements and their potentially surprising interplay. Our main finding is that expert interaction relaxes the representational demands on the learner: one only needs a model capable of realizing the expert's value function, bypassing the (often stricter) requirement of realizing the expert's policy itself. Concretely, we introduce OVI, an interactive on-policy IL algorithm that is statistically efficient whenever the learner can represent the expert's value function and computationally efficient given access to a linear maximization oracle. We complement this with a negative result showing that interaction is necessary. Namely, without stronger assumptions beyond expert-value realizability alone, any offline IL algorithm must scale with the complexity of the expert policy class. Our findings bear out empirically. OVI outperforms offline policy-based (BC), interactive policy-based (DAgger), and offline value-based IL methods, with the largest gains when the learner network is substantially less expressive than the expert's.


### QASP: Query-Adaptive Robust Vector Search Policy
**Authors**: Hakan Ferhatosmanoglu, Kushal Kumar, Tal Wagner, Andy Warfield

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29606v1](https://arxiv.org/pdf/2607.29606v1)

**Abstract**: A fundamental challenge of vector search is achieving consistently high recall while minimizing computational costs. Fixed search parameters cause significant performance variance across queries, and conventional evaluation on average recall masks these per-query disparities. We introduce QASP (Query-Adaptive robust vector Search Policy), which predicts the complete recall progression curve per query via a single upfront supervised regression, from which a search policy is derived for any recall target; this avoids iterative model invocations during search or separate predictors per target. By predicting normalized recall values with scale-invariant features and pre-search inference, QASP generalizes across recall targets, index configurations, and datasets. Its fine-grained progress predictions further enable a lightweight reactive complement that adjusts search depth based on predicted-versus-observed deviations without additional inference. We prove that QASP requires a finite training sample independent of dataset size and dimensionality, that its loss exceeds the irreducible lower bound of any fixed policy by a vanishing margin, and that its data access savings over fixed probing grow exponentially in intrinsic dimensionality. Experimentally, QASP achieves significantly lower recall variance and deviation from target, higher query satisfaction rate, and scales to large data and hierarchical indices without retraining, achieving 99% recall with 80% less data access.


### DungeonBench: A Benchmark for Rules-Rich Tactical Reasoning in Dungeons & Dragons Combat
**Authors**: Ismayil Ismayilov, Atakan Kara, Kaan Oktay

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29577v1](https://arxiv.org/pdf/2607.29577v1)

**Abstract**: Games and simulators make valuable benchmarks by turning decisions into measurable outcomes, but many current suites under-test rules-rich tactical reasoning: the ability to choose well when geometry, timing, resources, objectives, and rule interactions all matter at once. We introduce DungeonBench, a benchmark for tactical reasoning in Dungeons & Dragons combat, built to cover the vast majority of combat-relevant 2014 System Reference Document content whose effects can be resolved by the simulator while retaining mechanics that simplified combat simulators often abstract away. At each step, DungeonBench exposes a complete tactical observation, a pending decision, and an indexed list of executable options spanning movement, attacks, spells, reactions, objectives, preparation, and scarce resources. The task is to value legal choices whose consequences depend on action economy, creature traits, battlefield geometry, timing windows, and future encounters. DungeonBench has two tracks: Encounter, which evaluates local tactical play in single fights, and Day, which links encounters through persistent hit points, spell slots, consumables, preparation, and short-rest timing, forcing policies to trade off immediate tactical advantage against future survivability. The same engine-generated decision stream supports heuristic controllers, language-model policies, learned option rankers, and masked-action reinforcement-learning agents. We evaluate frontier language-model policies on this shared decision stream. Results show that full tactical observations do not saturate the benchmark: frontier policies often win direct encounters, but linked encounter days expose failures in resource budgeting, rest timing, and rule-aware tactical discipline.


## VLA
### CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning
**Authors**: Yuxin Chen, Hari Srikanth, Nathan Jew, Menglin Wu, Pengcheng Wang, Junli Ren, Masayoshi Tomizuka, Peng Xu, Jinyu Xie, Thomas Tian

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29172v1](https://arxiv.org/pdf/2607.29172v1)

**Abstract**: While robot foundation models are growing increasingly capable, the strongest models are typically trained on proprietary data and remain closed-source, limiting downstream users' ability to adapt them to new tasks, embodiments, and deployment settings. Following the LLM community, an emerging access paradigm for closed-weight robot foundation models is the managed supervised fine-tuning (SFT) API, where users submit training data and receive a tuned policy without access to model weights, gradients, or training internals. While such APIs let downstream users leverage powerful proprietary foundation models, they restrict policy improvement to pure imitation, ruling out reinforcement learning and other closed-loop methods that rely on internal training signals. This limitation is particularly acute for agile, contact-rich humanoid manipulation, where the gap between policy outputs and deployed behavior is large due to novel states, action tracking dynamics, latency, and controller-specific failure modes. We study how effective this managed-API regime is for humanoid adaptation, and how closed-loop improvement can be realized within it to push policies toward task mastery. We conduct one of the first empirical studies of managed-API adaptation on a real humanoid, instantiated on Gemini Robotics On-Device (GROD). We find that direct SFT through the API substantially outperforms a leading open-weight VLA trained on the same demonstrations, yet still falls short of deployment-level mastery on agile, contact-rich tasks. To close this gap, we introduce CLIFT: Closed-Loop Iterative Fine-Tuning, which turns deployment-time reward feedback into API-compatible supervised data and enables closed-loop policy improvement without accessing weights, gradients, likelihoods, or losses-pushing GROD to near-perfect success after two flywheel cycles, all without "opening the model box."


### ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency
**Authors**: Wenda Yu, Tianshi Wang, Fengling Li, Xin Li, Jingjing Li, Lei Zhu

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29169v1](https://arxiv.org/pdf/2607.29169v1)

**Abstract**: Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying the underlying VLA policy. ActFovea uses robot kinematics, proprioceptive states, and recent actions to construct action-conditioned foveated regions that retain contact-relevant areas and predicted motion corridors while suppressing task-irrelevant visual content. It detects runtime risks by evaluating whether visual motion and observation freshness remain consistent with geometric, proprioceptive, and action transitions. For recoverable disturbances, ActFovea constructs disturbance-specific candidate observations and accepts a recovery only after verifying the resulting action chunk. When stale or replayed observations make reliable recovery impossible, it invokes a bounded safe-failure procedure. In closed-loop evaluations of $π_0$ across multiple LIBERO suites, ActFovea increases success under localized visual overlays from 49.3\% to 90.3\%, closing 93.7\% of the gap to clean performance. It further improves success under action drift and visual delay by 7.0 and 9.8 percentage points, respectively, while preserving clean-task performance. Under frozen-observation replay, ActFovea triggers timely safe failure in all trials, with no unprotected failures. These results demonstrate that spatiotemporal visual-action consistency provides an effective basis for runtime safeguarding of VLA policies.


## Agent
### ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction
**Authors**: Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li, Simon Suo

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29677v1](https://arxiv.org/pdf/2607.29677v1)

**Abstract**: Enterprise workflows increasingly rely on agents for \emph{schema-guided extraction}: given a document and a user-defined schema, the agent faithfully follows the schema to produce the correct output with source evidence as grounding metadata. We present ExtractBench, a benchmark for schema-guided extraction and, to our knowledge, the first to score value accuracy, record completeness at scale, grounding, and measured cost together. The evaluation system contains 4,869 pages across 370 enterprise documents, 8 business domains, and 67 document types, with clear tags differentiating their challenge scenarios. The scalable schema and ground-truth curation pipeline combines independent-system agreement for real documents, known values for synthetic lists, and human verification for forms. We report order-insensitive value F1 for value accuracy, plus two grounding metrics for source traceability: word- and page-level F1. Commercial VLMs perform well on short documents but often truncate record lists on long ones, while coding agents retain higher accuracy at much higher cost. LlamaExtract Agentic Plus ranks first on all three metrics, with accuracy comparable to coding agents at a fraction of the cost. Dataset and evaluation code are available on \href{https://huggingface.co/datasets/llamaindex/ExtractBench}{HuggingFace} and \href{https://github.com/run-llama/ExtractBench}{GitHub}.


### LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from Preference Feedback
**Authors**: Manith Adikari, Bei Peng, Samuele Vinanzi, Angelo Cangelosi

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29559v1](https://arxiv.org/pdf/2607.29559v1)

**Abstract**: Reinforcement Learning (RL) systems are typically trained using a single, well-specified scalar reward function. However, real-world decision-making tasks often involve multiple, competing objectives, such as performance versus efficiency, where ground-truth reward functions are difficult to specify or inaccessible. While Multi-Objective RL (MORL) addresses such trade-offs by modeling rewards as vectors, existing approaches typically assume access to a well-specified reward function for each objective, inheriting the same challenges faced by single-objective RL. Meanwhile, Preference-based RL (PbRL) has shown great potential in solving complex tasks without access to a pre-defined reward function through reward learning from human feedback, yet has largely been studied in single-objective settings. In this work, we bridge this gap with LEMUR: Learning to Align with Multi-Objective Reinforcement Learning with Preference feedback, a novel framework where an agent interactively learns from the preferences of multiple humans to learn optimal multi-objective policies. Our approach jointly learns policies and multiple objective-specific reward models from human feedback, enabling agents to effectively balance competing objectives during learning. We evaluate LEMUR on a variety of benchmark multi-objective tasks, and empirical results demonstrate its superior performance over baseline methods. Our method presents a promising direction for solving multi-objective decision-making tasks without pre-defined reward functions.


### AMTFV: Agentic Mathematical Tool-Flow Verification for LLM Self-Correction
**Authors**: Rui Zou, Yutao Zhu, Mengqi Wei, Ji-Rong Wen

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29549v1](https://arxiv.org/pdf/2607.29549v1)

**Abstract**: Large language models have demonstrated strong mathematical problem-solving capabilities, yet reliably verifying their candidate answers remains challenging. Existing representative methods mainly revise outputs through natural-language reflection or assist verification by directly generating verification programs; the former may not reliably support exact computation, whereas the latter prematurely couples mathematical modeling with low-level implementation. We propose AMTFV (Agentic Mathematical Tool-Flow Verification). By introducing Mathematical Tool Flow (MTF) as an interrupt--execute--resume interface, AMTFV decouples verification modeling from concrete execution and supports exact computation through a mathematical toolbox. Specifically, the verification agent first constructs a verification workflow, encodes the mathematical objects and computational intent requiring reliable execution in an MTF request, and sends it to the mathematical toolbox agent. The latter parses the request, generates executable calls, and dispatches them to the backend for exact computation. Tool outputs then support candidate-answer adjudication, answer revision, and verification-workflow revision. We evaluate AMTFV on five challenging mathematical reasoning datasets with seven model configurations from DeepSeek, GPT, and Gemini. Experimental results show that AMTFV outperforms the representative baselines evaluated in this study overall; under an individual model configuration, it improves average accuracy over the strongest baseline by up to 8.3 percentage points, with larger gains on samples of medium and high verification complexity.


### From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale
**Authors**: Chandra Maddila, Mashrur Rashik, Euna Mehnaz Khan, Smriti Jha, James Saindon, Nachi Nagappan, Peter C. Rigby

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29516v1](https://arxiv.org/pdf/2607.29516v1)

**Abstract**: AI coding agents are generating code at volumes that exceed the capacity of traditional peer review. At the same time, existing AI code review tools over-index on low-value suggestions such as style and best practices while under-indexing on the concerns human reviewers prioritize most: correctness, security, and performance. We present ARCTIC, an AI-powered Code Critique system that reframes code review around three capabilities: intent prediction, which infers why a change was made from conversation logs and metadata; drift detection, which measures divergence between the developer's intent and the agent's output via backtranslation; and code spotlight, which ranks the regions of a diff most warranting human scrutiny. We ground these capabilities in a six-theme taxonomy derived from 18,000 code reviews. Offline evaluation shows that intent prediction achieves 0.86 F1, drift detection reaches near-perfect ordinal agreement with human annotators (QWK = 0.907), and spotlight outperforms the baseline AI reviewer by 2.4x on quality estimation at 5x fewer tokens. In the experimental rollout, the drift scores reduces code misalignment by an additional 5.76 points (p = 0.026), intent prediction receives 90.2% approval, and zero defects have been attributed to self-reviewed diffs since launch.


### Transcript-Managed Transformers: Monotone Multi-Agent Collapse and Universality with Two Pop-Enabled Transcripts
**Authors**: Sergey Salishev

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29496v1](https://arxiv.org/pdf/2607.29496v1)

**Abstract**: We study transcript management for fixed, finite-precision causal Transformers. A transcript is partitioned into channels of bounded blocks. Each transition consults a fixed visible suffix and may append one block, leaving the model, weights, and token protocol unchanged. The operation $P_c:=\PopContext(c)$ deletes the newest block on channel $c$ and exposes its predecessor.
  We model the layer by the Transcript-Managed Transducer $\TMTn{k}$: one finite controller, $k$ channels, and per-round actions from stay, push, and pop under a caller-driven status map. Fixed visible windows encode as finite symbols. The pop-free Restricted Transcript-Managed Transducer $\RTMTn{k}$ is the standard append-only layer and, for every fixed $k$, realizes exactly the deterministic finite-state transductions. The same holds for every fixed finite agent population under a monotone protocol that appends, routes, and copies visible blocks.
  Admitting $\{P_c\}_{c=1}^k$ restores pop. Newest-first, a pop-enabled channel is a stack; compiling to the Hopcroft--Ullman presentation transfers the classical hierarchy: $\DCFL$ for $k=1$ and $\RE$ for every $k\ge2$. Orchestrated one-channel agents match one controller with $k$ channels, so two pop-enabled transcripts---in one agent or two---suffice for universality. Simulation costs and invariance to fixed block size and visible radius are stated. The bounds fix precision, alphabets, blocks, visibility, controller state, and population; growing exact context, hidden-block access, writable stores, and unbounded \textbf{Spawn} add further state.


### Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember
**Authors**: Zenghuang Fu, Zhaoyang Li, Qiuyuan Ai, Haoyu Wu, Minghui Wu, Chenxu Zhao, Ante Wang, Guannan He, Changwei Wang

**Published Date**: 2026-07-31

**Updated Date**: 2026-07-31

**PDF Url**: [2607.29468v1](https://arxiv.org/pdf/2607.29468v1)

**Abstract**: Self-play agents can generate training problems without questions from target benchmarks, but their curricula lack persistent state: failures affect gradients yet do not explicitly shape future practice. External skill memories preserve procedural experience but are typically learned from fixed task distributions. We introduce \textbf{SESA} (Self-Evolving Skill-Augmented Agent), which makes procedural memory an evolving state of tool-augmented search self-play. A challenger poses problems, while a separately parameterized solver alone retrieves skills. Informative failures are distilled into reusable skills and written back to memory. The updated memory changes solver behavior and success, which changes the challenger's reward and the distribution of future problems; the resulting frontier produces new failures that rewrite memory. This bidirectional loop makes task generation and skill memory co-evolve. Because retrieved skills shape on-policy training trajectories, their benefits can enter the model parameters as well as remain in the external bank, enabling memory-free deployment and optional inference-time retrieval. Across seven open-domain and multi-hop question-answering benchmarks, SESA improves average accuracy over SSP by 1.2--3.2 points across multiple backbones and surpasses the skill-augmented SkillRL baseline by 0.9 points under a unified evaluation protocol. On Qwen3 models, SESA-Off retains 1.8--2.2 points of improvement over SSP, while the final skill bank adds a further 0.5--1.0 points. These results show that evolving skill memory is not merely an inference-time plug-in: it changes policy learning and the future training distribution while retaining value as optional external memory. Our code is available at https://github.com/Zenghuang-Fu/SESA-Self-Evolving-Search-Agents.


