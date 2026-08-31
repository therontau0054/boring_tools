# Abstracts of Papers

## World Model
### QGPINNs: A Physics-Informed Neural Network Framework for Nonlocal Differential Equations on Quantum Graphs
**Authors**: Vaibhav Mehandiratta, Saket Ramchandra

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28589v1](https://arxiv.org/pdf/2608.28589v1)

**Abstract**: We propose QGPINNs, a physics-informed neural network framework developed in PyTorch for the numerical solution of nonlocal differential equations on quantum graphs. The framework is designed as a general computational implementation in which the solution on each edge of the graph is approximated by a neural network, while a unified graph-based loss function enforces the governing equations together with initial, boundary, and vertex transmission conditions. In particular, the formulation incorporates standard continuity and Kirchhoff-Neumann vertex conditions and Dirichlet boundary conditions into the learning process to couple the local edge-wise neural approximations into a global solution on the graph. The framework is developed for two representative classes of nonlinear models: multi-order fractional elliptic problems and time-fractional evolution equations on quantum graphs. To improve accuracy and training stability, QGPINNs integrates several graph-adapted learning strategies, including soft and hard constraint enforcement, dynamic loss balancing, Fourier feature embeddings, and a learnable singularity-capturing feature for weakly singular solutions arising in the considered problems. The framework also extends naturally to inverse problems, including the identification of the orders of fractional operators and physical parameters from noisy observational data. We validate the accuracy, computational efficiency, and physical consistency of the proposed framework through numerical experiments on benchmark graph structures and real-world networks, including the IEEE 14-bus system and an open-channel agricultural drainage network.


### Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning
**Authors**: Nan Wang, Mohit Yadav, Jonathan Wulff, Aidan Rosenbaum, Kezhou Chen, Yuvan Sharma, Xu Dong, Yiwei Tao

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28578v1](https://arxiv.org/pdf/2608.28578v1)

**Abstract**: Tendon-driven hands are anthropomorphic, and moving the actuators off the joints is what makes a hand of this capability affordable to build. Two effects produce that saving. Routing force through a cable removes the requirement that a motor fit inside the joint it drives, so smaller and cheaper motors suffice, and one motor can drive several joints through a single cable, so fewer motors are needed. They are also harder to learn on than a direct-drive hand. The underactuated transmission that produces the saving is itself difficult to represent in a simulator, and the joints one cable drives are not independently commandable. We present Aero Hand Open, a tendon-driven anthropomorphic hand that is released simulation-ready. Three things ship with it. A simulation model reproduces the cable transmission itself. An identified actuation map connects that model to the motor commands in both directions, including the three-way coupling of the thumb. A reinforcement learning package trains policies for the hand. Together they let a policy be trained entirely in simulation and run on the hand with no fine-tuning and no state estimation. We release the mechanical design, the simulation model, the identified mapping, the training environment and the deployment stack.


### Learning a Size-Weight Frontier for Synthetic-Augmented Inference
**Authors**: Chengpiao Huang, Kaizheng Wang

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28576v1](https://arxiv.org/pdf/2608.28576v1)

**Abstract**: Synthetic data can improve statistical inference when real data are scarce, but naively treating synthetic samples as real data can introduce bias and lead to unreliable inference. We develop a general framework for synthetic-augmented inference across a population of related tasks. It characterizes synthetic augmentation by the number of synthetic observations and their weight. Central to our framework is a size-weight frontier that specifies, for each weight, the largest synthetic sample size for which all smaller sizes attain the target task-marginal coverage. We estimate this frontier from historical tasks, and establish a finite-sample coverage guarantee simultaneously for all size-weight configurations on or below the estimated frontier. In experiments using large language model responses to augment opinion survey data, our procedure achieves target coverage and substantially narrows confidence intervals.


### ChainSplat: A Physics-Inspired Screw-Theoretic Model for Learning Deformable Linear Object Dynamics from Multi-View RGB Videos
**Authors**: Seungyeon Kim, Noémie Jaquier

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28570v1](https://arxiv.org/pdf/2608.28570v1)

**Abstract**: Identifying the underlying dynamics and 3D geometry of deformable linear objects (DLOs), such as cables, ropes, and hoses, is essential for accurate robotic manipulation, but remains challenging due to their high-dimensional configuration spaces and diverse behaviors arising from varying material properties. Existing methods often rely on multi-stage pipelines and auxiliary depth inputs, which are prone to errors under dynamic interactions, while their high-dimensional state representations make model-based control computationally expensive. In this paper, we introduce ChainSplat, a physics-inspired framework that jointly learns the 3D geometry, appearance, kinematics, and dynamics of DLOs solely from multi-view RGB videos. ChainSplat represents a DLO as an open-chain structure of rigid links connected by revolute joints, yielding an analytic, screw-theoretic model with a compact state representation parameterized by joint configurations. By integrating this formulation with Gaussian splatting, ChainSplat jointly recovers DLO dynamics, kinematics-aware 3D geometry, and appearance, while enabling high-fidelity RGB rendering from arbitrary states. Through real-world experiments, we demonstrate that ChainSplat achieves state-of-the-art performance in dynamics predictions, 3D geometry reconstruction, and RGB rendering across dynamic interactions. ChainSplat further enables real-time state and force estimation, as well as accurate model-based trajectory optimization, highlighting its practical utility for real-world robotic manipulation of DLOs. Accompanying source code and video are available at: https://chainsplat.github.io.


### Blog: Survey of Optimizers
**Authors**: Ruoran Xu

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28557v1](https://arxiv.org/pdf/2608.28557v1)

**Abstract**: Neural-network optimization in 2025-2026 is no longer well described as a succession of new Adam variants. The design space has expanded from coordinates to matrices and layers, from fixed training horizons to policies over time, and from mathematical update rules to state representations that must survive sharding and low-precision computation. This survey organizes recent optimizers and training optimization methods along four largely independent axes: temporal estimation, update geometry, horizon management, and representation and systems. It connects the spectral normalization of Muon, the historical matrix statistics of Shampoo and SOAP, adaptive and hybrid matrix methods, memory-efficient optimizers, schedule-free training, small-batch corrections, and quantized optimizer states. The central empirical conclusion is deliberately non-triumphal: matrix-aware methods represent a genuine advance, but there is no context-independent replacement for AdamW. Rankings change with model scale, data-to-parameter ratio, batch size, schedule, parameter partition, tuning budget, and whether the target metric is tokens, FLOPs, wall-clock time, or memory. The practical consequence is a compositional view of optimizer design and a stricter protocol for evaluating optimizer claims.


### Logos: An Agent Harness on a Cross-Process Bus
**Authors**: Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28553v1](https://arxiv.org/pdf/2608.28553v1)

**Abstract**: Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.


## Generation
### On two proofs of $d^2$ mixing of weighted Dikin walks
**Authors**: Yuansi Chen, Yunbum Kook

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28566v1](https://arxiv.org/pdf/2608.28566v1)

**Abstract**: We study the mixing time of weighted Dikin walks for sampling from exponential distributions on polytopes and truncated positive-semidefinite (PSD) cones. Our first result gives a general total-variation mixing bound under strong self-concordance, $\barν$-symmetry, and mixed-trace regularity on the local metric. The key idea is to control the Metropolis--Hastings acceptance probability on a high-probability region rather than at every point. Applying this framework to the Lee--Sidford, Lewis-weight, and John metrics yields an $\widetilde O(d^2)$ mixing bound for sampling from polytopes, while applying it to a hybrid barrier yields an $\widetilde O(d^4)$ mixing bound for sampling from truncated PSD cones. Our second result establishes stronger $χ^2$-divergence guarantees and pointwise acceptance control using a new fourth-order bootstrap condition. For a suitably scaled Lee--Sidford metric, this yields an $\widetilde O(d^2)$ mixing bound in $χ^2$-divergence, improving on the previous $\widetilde O(d^{9/4})$ bound.


### Learning between the peaks: sharp asymptotics for kernel ridge regression under power-law anisotropy
**Authors**: Lorenzo Rizzi, Arie Wortsman Zurich, Bruno Loureiro

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28564v1](https://arxiv.org/pdf/2608.28564v1)

**Abstract**: We study kernel ridge regression under anisotropic Gaussian data, where the input covariance decays as a power law with exponent $α\geq 0$ for polynomial inner-product kernels. We derive asymptotically sharp expressions for the kernel spectrum and the generalization error in the polynomial high-dimensional regime $n=Θ(d^κ)$, revealing how anisotropy reshapes the learning curves. For weak anisotropy ($0<α<1$), the problem remains effectively high-dimensional and retains some features of the isotropic case, while departing from it in others: the variance still peaks at integer sample complexities $κ\in\mathbb{N}$, but these peaks are progressively damped as $α$ grows; meanwhile, for targets strongly aligned with the data's principal directions, the bias drops at fractional sample complexities, decoupling the bias transitions from the interpolation peaks. For strong anisotropy ($α> 1$), the effective dimension of the problem is constant, and the variance stops depending on sample size altogether, plateauing under ridgeless interpolation or vanishing at an explicit rate under fixed ridge penalty. The bias undergoes a sharp transition governed by the target's decay rate: below a threshold, learning is abrupt rather than gradual; above it, the bias decays as a power law that recovers the classical source and capacity rates. We finally specialize these results to single-index targets, showing how the alignment of the index with the data's principal directions determines the effect of anisotropy on learning. Together, our results clarify how the input geometry shapes the kernel features and fundamentally impacts its generalization properties.


### Video Generative Models as Geometry Learner
**Authors**: Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28549v1](https://arxiv.org/pdf/2608.28549v1)

**Abstract**: Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image <-> geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.


### DARTS: Decoder-Aware Representation Tuning via Surgery for Model Merging
**Authors**: Aaryan Ajay Sharma, Sai Nishanth Padala, Seganrasan Subramanian

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28547v1](https://arxiv.org/pdf/2608.28547v1)

**Abstract**: Model merging combines multiple task-specific fine-tuned LLMs into a single multi-task model without additional training. However, merged models are known to suffer from representation bias: systematic drift between the merged model's hidden states and those of each individual source model. Prior work (Yang et al., 2024a) study and mitigate this bias for encoder-based vision models using a lightweight correction module trained with L1 loss. However, such bias is not studied for decoder models due to their autoregressive nature. We analyze the problem of representation bias in decoder models, and show two challenges absent in encoders: (1) the causal attention mask causes bias to accumulate across token positions, requiring position-dependent correction; and (2) not all token positions are equally important, i.e., high-entropy (decision-critical) positions matter far more than low-entropy ones. To address these challenges, we propose Decoder-Aware Representation Tuning via Surgery (DARTS). DARTS employs a novel entropy-weighted L1 loss to upweight correction at high-entropy positions where errors most affect generation quality, and a per-position additive bias that captures position-dependent error without overparameterization. We perform extensive evaluation on three domains: code generation (HumanEval), mathematical reasoning (GSM8K), and instruction following (AlpacaEval) on Llama-2-7B models, and show DARTS achieves significant improvement over the standard surgery approach while adding negligible parameters ($0.1\%$ of total parameters).


### InstructMesh: Selective Refinement of Generative 3D Models for Fabrication
**Authors**: Faraz Faruqi, Ahmed Katary, Demircan Tas, Theresa Hradilak, Ning Zhang, Jiaji Li, Fabian Manhardt, Martin Nisser, Vrushank Phadnis, Ruofei Du, Federico Tombari, Megan Hofmann, Stefanie Mueller

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28534v1](https://arxiv.org/pdf/2608.28534v1)

**Abstract**: Recent advances in generative AI allow users to create 3D models from text or images. However, these models prioritize visual plausibility over geometric accuracy, often generating results with flaws that compromise their intended use post-fabrication. We present InstructMesh, an interactive post-generation refinement tool that enables selective repair of generative 3D models through region selection and targeted operations, such as opening or sealing voids, or adjusting local thickness. Users can invoke edit operations via natural language prompts or slider controls. By operating directly on the intermediate latent representation, InstructMesh allows users to apply robust geometric corrections without requiring expert modeling skills. To inform our design, we first analyze common fabrication-related failure modes in outputs from state-of-the-art generative tools. We then conduct two user studies, demonstrating that novices can identify and perform fabrication-relevant repairs on generative outputs using InstructMesh, and revealing user preference for hybrid interfaces that combine slider controls with natural language input.


### When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI
**Authors**: Sihan Jia, Oliver Lemon

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28518v1](https://arxiv.org/pdf/2608.28518v1)

**Abstract**: We investigate whether automatic speech recognition (ASR) errors in user input can lead to unsafe outputs from Embodied AI (EAI) models. We find that ASR errors can lead to harmful instructions being accepted and executed by EAI models, thereby reducing safety. We simulate ASR errors and combine them with existing safety benchmarks (SafeAgentBench and POEX) to evaluate how different errors affect embodied AI safety. We find that some of them preserve semantic structure but increase harmful ambiguity, while others weaken the model refusal behaviour and allow unsafe plans to be generated and executed. We show that in some cases automatic correction of ASR errors can reduce the risk, but this is not always effective. Overall, we show that ASR errors lead to significant safety risks for embodied AI.


## VLA
### PHR-VLA: Planning Horizon Reasoning for Vision-Language-Action Models
**Authors**: Davood Soleymanzadeh, Kaidi Zhang, Zhiyuan Zhang, Bihao Zhang, Xiao Liang, Yu She, Minghui Zheng

**Published Date**: 2026-08-27

**Updated Date**: 2026-08-27

**PDF Url**: [2608.27609v1](https://arxiv.org/pdf/2608.27609v1)

**Abstract**: Vision-language-action models (VLAs) have shown strong promise for general-purpose robotic manipulation by mapping language instructions and vision observations directly to actions. However, most VLAs primarily condition action prediction on current observations and lack an explicit mechanism for reasoning over future task dynamics, which is particularly important for fine-grained, contact-rich manipulation. We present PHR-VLA, a framework that enables planning-horizon reasoning in VLAs through privileged latent representations of future dynamics. PHR-VLA introduces a lightweight auxiliary future head that, during training, aligns the VLA's internal representations with latent dynamics extracted from future observations. Evaluation results demonstrate that local, contact-centric, patch-level latent dynamics supervision from the wrist camera improves success rate on LIBERO from 84.1% to 88.4% and on real-world disassembly tasks from 63.3% to 82.5%. Patch-level supervision from a third-person camera also improves performance on Meta-World from 56.70% to 57.8%. These results demonstrate that privileged latent dynamics alignment provides an effective training signal for improving anticipatory reasoning in VLA policies. Project website: \href{https://davoodsz.github.io/PHR-VLA.github.io/}{https://davoodsz.github.io/PHR-VLA.github.io/}


## Agent
### On the Maintenance and Co-evolution of Agent Plugins: An Empirical Study of Claude Code Plugin Marketplaces
**Authors**: Ahmed Hereiz, Yingzhe Lyu, Hao Li, Bram Adams, Ahmed E. Hassan

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28497v1](https://arxiv.org/pdf/2608.28497v1)

**Abstract**: AI coding agents, software tools that automate development tasks through reasoning and tool use, are increasingly extended through plugin marketplaces, yet the structure, maintenance, and co-evolution dynamics of these emerging repositories remain empirically unexplored. Unlike traditional software packages that deliver functionality through source code, agent plugins deliver functionality through a combination of natural-language instruction files, scripts, and configuration files, raising the question of whether these plugins are maintained artifacts that co-evolve across components, or one-off artifacts that developers write once and do not need to revisit. To study the maintenance and co-evolution of agent plugins, we conduct an empirical study of 1,926 repositories hosting Claude Code plugin marketplaces, analyzing 8,351 plugins and 77,773 commits across 2,018 marketplaces. We find that the marketplace is expanding rapidly, plugin-touching commit activity growing 8.8x over six months after the October 2025 launch, and plugins targeting Software Engineering tasks accounting for 61.3% of all plugins. Plugin development is predominantly feature-driven, with feature commits occurring at more than twice the rate of conventional open-source software (OSS) (39.6% vs. 17.2%). Claude co-authors 34.9% of all commits, and four commit types (docs, perf, style, and refactor) carry substantially different meanings in plugin repositories than in traditional software. Most component types evolve independently, but within skills directories, natural-language instruction files and implementation scripts co-evolve at above-chance rates, with 78% of co-changes being functionally coupled, representing a new class of maintenance dependency not observed in traditional software engineering.


### LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment
**Authors**: Jingjing Nie, Jiawei Guo, Krishna Meda, Haipeng Cai

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28490v1](https://arxiv.org/pdf/2608.28490v1)

**Abstract**: Software and systems security workflows are typically procedural: analysts inspect heterogeneous artifacts, form hypotheses, invoke tools, interpret outputs, and revise plans. Large language model (LLM)-based agents, which can plan, use tools, retain state, and revise actions across multi-step workflows, are being rapidly adopted to automate this work. Given the consequences of delegating security decisions to autonomous systems, understanding how such agents are built, used, and assessed is crucial. Yet to this date, there remains a lack of systematic understanding of what has been done and how far we are in this field: the term "agent" is applied inconsistently, applications differ sharply in risk, and assessment protocols are often incomparable. To gain a comprehensive and coherent view of this area hence inform relevant future research, this paper provides a systematic literature review of the (1) technical approaches, including agent architecture, perception, memory, reasoning and planning, action space, orchestration, and self-improvement, (2) applications, with respect to the security tasks served, and (3) assessment, including the datasets, outcome and trajectory metrics, safety measures, and baselines considered, over the peer-reviewed literature spanning the emergence of this area (2023--2026). Our synthesis reveals a field that has built agents able to act but not yet agents whose authority is bounded or whose behavior is auditable. In addition to knowledge systematization, we also extend our insights into the limitations of and challenges faced by current approach, application, and assessment designs, which shed light on potentially promising future research directions.


### COVER: Identifiable Evaluation of Coalition Routing
**Authors**: Raghul Sugumar, Amrit Gopinath

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28475v1](https://arxiv.org/pdf/2608.28475v1)

**Abstract**: When a multi-agent system changes its team, it also changes the messages and final answer it produces, so an end-to-end accuracy gap does not by itself identify a routing effect. We introduce method, an evaluation contract that fixes a public information boundary, downstream stack G, and finite legal team family before outcomes are generated. Complete coverage identifies exact finite-benchmark oracle regret conditional on that stack. For any finite collection of frozen policies, executing the union of their distinct selected teams is the minimal assumption-free support for every pairwise policy contrast, though not for absolute oracle regret. Two controlled tables with source-ID-disjoint splits test the instrument. On MuSiQue-12, a pre-specified privileged positive control improves regret from 0.532 to 0.402; a later public-interface control reaches 0.424 versus 0.554 but is retrospective. On HotpotQA-4, a pre-specified public direct scorer improves regret from 0.313 to 0.110. In fixed-stack Llama execution, verified route regret improves by 0.190, while the raw-answer gain is 0.010 with an interval crossing zero. A five-family ToolSandbox variant-shift validation exhaustively evaluates 16 declared teams on 14 untouched task variants (224/224 valid rows): the declared-family oracle reaches 0.768 safe-evidence completion, while the prospectively frozen router gets 0.637 (regret 0.131), failing the predeclared 0.10 criterion. A later retrospective comparator reaches 0.655, matching all-workers with 4.57 versus 5.00 workers on average. Thus COVER exposes selection headroom without manufacturing a routing win. A crossed-stack diagnostic shows absolute scores depend on G but finds no detectable router-by-finalizer interaction. COVER is an auditable measurement methodology, not a claim of stack-invariant or universal agent-routing superiority.


### Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents
**Authors**: Nan Li

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28458v1](https://arxiv.org/pdf/2608.28458v1)

**Abstract**: Interactive dialogue games test a capability that static benchmarks largely leave implicit: a model must carry state across turns, interpret feedback, and choose valid actions under changing constraints. We study this setting in the LM Playschool Challenge with a 2B open-weight model, and find that many failures are not only broad knowledge failures but also local decision failures: repeated guesses, malformed actions, and violations of feedback that the model has just seen. These diagnostics motivate a training recipe organized around three steps: acquire broad game participation through supervised fine-tuning, repair mechanically verifiable failures within one targeted dialogue-game family using turn-local preference pairs, and preserve general capabilities beyond these dialogue games. In the official final evaluation, our submission improves public clemscore from 10.67 to 38.92 and closed in-domain score from 13.41 to 41.17, while approximately preserving aggregate static performance (44.14 vs. 44.24 for the baseline). Out-of-domain clemscore remains low at 7.88, with the largest gains concentrated in unseen variants of the targeted family. Our results suggest that broad SFT brings most of the model's capability improvement; turn-local supervision can be effective when failure detection is precise, with observed transfer concentrated primarily within-family.


### Fidelity Is Not Enough: Dispatch-Level Instrumentation for Agentic Datasheet Extraction
**Authors**: Qing Ye, Meng-Hsuan Lin

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28439v1](https://arxiv.org/pdf/2608.28439v1)

**Abstract**: One model passed our fidelity check without ever opening the datasheet. We found it while qualifying models for an internal extraction service: a structured-output constraint had silently disabled tool use, and the model answered anyway, with fabricated source text. Only the per-tool trace exposed it. Fidelity -- whether an extracted value matches the source -- is the standard measure for agentic document extraction, and it scores that run a success. We therefore log every tool call in an agentic benchmark of 25 hand-curated claims over three components, with 12 more on a fourth, 37 in all. From that dispatch record we build two instruments: a rule-based failure-attribution classifier, and a silent-failure detector whose two rules check only which tools were called, never the extracted value. The detector raises no flag on 207 clean fidelity-passing extractions across three model families, and recovers all 50 planted faults that withhold exactly the tools its rules check. The two results are not symmetric: the first bounds the false-positive rate, the second is recall by construction, and detection power against runs that call their tools and still answer wrongly is unmeasured. A second, independent oracle, a causal chamber that tests whether the datasheet's claims hold under physical measurement, is intentionally partial: it confirms only what the apparatus can exercise, a verifiable envelope of 2 of those 37 claims, and we give a taxonomy of why the rest are not physically gradable. Under a controlled perturbation, fidelity passes throughout while the chamber verdict flips exactly at the measurement uncertainty. Across three deployed model stacks (one destabilised by its serving stack, not by any capability gap) the tool layer buys portability and observability rather than accuracy, and earns its premium only once a document outgrows the context window.


### Prove2Me: An Open Collaborative Platform for Scaling Math Formalization
**Authors**: Shuze Chen, Kunal Marwaha, Xiaoyang Lu, Henry Yuen, Tianyi Peng

**Published Date**: 2026-08-28

**Updated Date**: 2026-08-28

**PDF Url**: [2608.28433v1](https://arxiv.org/pdf/2608.28433v1)

**Abstract**: Proof assistants such as Lean 4 promise the paradigm of formally verified mathematics, but large-scale formalization projects have faced major barriers to entry, including the need for expertise in formal verification (as well as the underlying mathematics) and the significant time required for writing formal proofs. AI coding agents have dramatically reduced these barriers; human users can now use natural language to prompt agents to write complex proofs in Lean. This opens up the intriguing possibility of internet-scale mathematical collaboration involving both humans and AI agents, where correctness is machine-checked.
  To realize this possibility, we introduce Prove2Me (https://prove2.me), an open collaborative platform for formalizing mathematics. Users launch formalization "missions", to which AI agents contribute formal proofs toward completion. We designed mechanisms and a specialized harness in Prove2Me that enable large-scale collaboration so that agents can build on one another's work and freely reuse existing results. In doing so, Prove2Me aims to turn math formalization into a scalable, crowd-sourced effort open to anyone with an agent.


