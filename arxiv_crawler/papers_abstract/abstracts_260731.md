# Abstracts of Papers

## World Model
### Learning to Trace Seiberg Dualities
**Authors**: Jonathan J. Heckman, Shani Meynet, Alessandro Mininno, Gary Shiu

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28628v1](https://arxiv.org/pdf/2607.28628v1)

**Abstract**: Dualities play an important role in establishing both microscopic and emergent phenomena in a wide range of physical systems. In practice, though, it can often be computationally challenging to establish when two systems are dual, even when all of the "rules of the game" are well-known. Said differently, when confronted with two systems, how can one efficiently establish that they are in fact dual? In this paper we use machine learning methods to address this question for Seiberg dualities of supersymmetric quiver gauge theories. Mathematically, this involves establishing mutations of quivers, which is in turn a variation on the theme of "learning to unknot". On the one hand, this leads us to a practical tool for establishing the computational complexity of different dualities. On the other hand, it also allows us to study how different network architectures learn how to trace Seiberg dualities. We find that for quivers with a modest number of quiver nodes (of order $10$), different network architectures consisting of transformers and multi-layer perceptrons tend to outperform deterministic algorithms. Supplementing the network by well-established pathfinder algorithms (essentially "Google Maps for quivers") leads to an additional improvement in the efficiency and accuracy of the search strategy. We anticipate that this class of questions can serve as a useful benchmark for frontier AI models applied to theoretical physics.


### ReToken: One Token to Improve Vision-Language Models for Visual Retrieval
**Authors**: Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28627v1](https://arxiv.org/pdf/2607.28627v1)

**Abstract**: Long visual context poses a challenge for vision-language models: performance degrades as the number of distractors grows, and processing all tokens at once is computationally infeasible under GPU memory constraints. We present ReToken, a single learnable embedding trained as an explicit retrieval target that selects a sparse set of query-relevant visual tokens from a pre-filled visual KV cache. Trained on only a small image-QA dataset, ReToken yields consistent gains across image and video benchmarks: on Visual Haystacks it improves Qwen3VL-8B by 13.4 points and InternVL3.5 by 12.4 points (>20% relative), and on LVBench it transfers zero-shot to long video for an 8.0-point gain with Qwen3VL-8B. Thanks to its lightweight design, both training and long-video inference fit on a single H100. Code is available at: https://github.com/avaxiao/ReToken


### ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine
**Authors**: Yukang Cao, Haozhe Xie, Beichen Wen, Runmao Yao, Yinghao Liu, Yue Huang, Zhichao Liao, Yunxiang Wang, Haiheng Liu, Xingshun Tian, Dawei Su, Long Zhuo, Dacheng Tao, Xiaogang Wang, Liang Pan, Ziwei Liu

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28625v1](https://arxiv.org/pdf/2607.28625v1)

**Abstract**: Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environments into spatially calibrated, temporally synchronized recording studios. ACE operates at two complementary scales: a table-scale configuration resolves hand-object manipulation, while a room-scale configuration captures whole-body motion, locomotion, and interactions across a furnished home. ACE records egocentric and multi-view exocentric video, full-body and articulated hand motion, object geometry and 6-DoF trajectories, audio, and tactile signals as a unified multisensory stream. Using ACE, we build ACE-Data-0, comprising 150 hours and 17M video frames across 200 task categories, performed by 50 participants in 2 environments, for a total of 75,000 interaction episodes. The dataset spans atomic manipulation, long-horizon chains of household activities, and human-scene interaction, while preserving natural behavioral variation through goal-level rather than step-by-step instructions. We further introduce a hierarchical benchmark that progresses from signals to scene components and then to interactions. Evaluations of state-of-the-art methods expose substantial gaps under contact, occlusion, egomotion, and long temporal horizons. ACE-Data-0 provides synchronized human demonstrations with aligned perceptual, kinematic, and contact supervision, offering a scalable foundation for imitation learning, world models, vision-language-action systems, and embodied AI.


### PhiZero: A World Model Built Around Physical Language
**Authors**: Shuyao Shang, Yuqi Wang, Ruopeng Gao, Xu Chen, Tieniu Tan, Lue Fan, Zhaoxiang Zhang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28624v1](https://arxiv.org/pdf/2607.28624v1)

**Abstract**: We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future videos directly in pixel space, leaving the underlying world dynamics implicit within high-dimensional visual predictors. Motivated by humans' ability to abstract predictive structure from visual experience and organize it in natural language for explicit reasoning, we learn physical language from in-the-wild videos through self-supervision and use it to explicitly reason about how the physical world evolves. Accordingly, PhiZero adopts a reason-then-render paradigm: it first infers future world evolution as a physical-language sequence and then renders the inferred transitions into videos. Extensive experiments across generation and understanding benchmarks validate the ability of PhiZero to model physically coherent world evolution. We further show its potential for realistic and interactive world modeling, fine-grained action-conditioned simulation, and zero-shot motion transfer.


### PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball
**Authors**: Lizhi Yang, Junheng Li, Aaron D. Ames

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28623v1](https://arxiv.org/pdf/2607.28623v1)

**Abstract**: We present PAC-MAN, a perception-aware CBF-RL framework that couples control-barrier safety with deployment-realistic onboard sensing for whole-body humanoid dodgeball. The deployed policy sees the ball only as segmentation-masked depth from a head-mounted camera, while training-time CBF guidance represents clearance to every body link, and an adversarial motion prior regularizes the resulting evasive reflexes. We evaluate on a controlled any-link contact benchmark with seeded throws in two regimes: single throws and a deployment loop in which the robot walks back to its station and recovers between throws. On this benchmark, the policy comes within a few points of a privileged state oracle: a fixed onboard camera alone is adequate for evasion. We find that usable barrier structure depends on perceptual observability: Joint-CBF gives the best performance with accurate ball states, degrades under fixed-camera observations when used only as training guidance, and recovers with a ball-tracking gimbal or privileged runtime filter. We therefore deploy a lightweight Link-CBF policy zero-shot on the Unitree G1 in the real world, where it tolerates imperfect perception, succeeds on 95% of throws, and uses semantic segmentation to dodge different balls.


### AISPA: User-Centric System Prompt Auditing for Large Language Model Applications
**Authors**: Xiangning Lin, Shenzhe Zhu, Shu Yang, Zhenyu Zhang, Haoqian Zhang, Yipeng Zhao, Chengxuan Qian, Tianwei Wang, Ziheng Zhang, Zhenlong Yuan, Dingcheng Wang, Juncheng Wu, Yuan Si, Jiaxin Liu, Baolong Bi, Robert Mahari, Tobin South, Dazza Greenwood, Zexue He, Rishi Bommasani, Sophia Kazinnik, Andreas Haupt, Samuele Marro, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28617v1](https://arxiv.org/pdf/2607.28617v1)

**Abstract**: System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to the public or regulators, creating a serious trust and accountability gap in the wide deployment of AI systems. In this paper, we introduce Artificial Intelligence System Prompt Assurance (AISPA), a user-centric framework for systematically auditing system prompts in AI systems. AISPA examines specific parts of a system prompt and evaluates them along eight dimensions that matter to users. We then use this framework to review 3,249 instructions from system prompts in 88 commercial AI products, classifying each instruction as either protective (of users) or problematic. Our audit surfaces four core findings. First, system prompt design varies substantially across products and developers, with some organizations averaging over 60 protective instructions per product while others average fewer than 5. Second, protective instructions are widely adopted but shallow in scope: 98.9% of products contain at least one, yet only 24% cover all eight dimensions of the AISPA taxonomy. Third, system prompts have grown steadily longer and more protective of users, suggesting that user protection is becoming a more visible concern in commercial prompt design. Fourth, despite this progress, problematic instructions remain pervasive: roughly 40% of products contain at least one instruction that works against user interests, and protective and problematic instructions frequently coexist within the same prompt. Our findings highlight the need for greater transparency, standardization, and independent oversight for system prompts in commercial AI products.


## Generation
### Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments
**Authors**: Haomin Qi, Xingliang Wang, Xuanqi Gao, Baihui Sang, Xin Zhang, Minghua Ma, Pengfei Gao, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28591v1](https://arxiv.org/pdf/2607.28591v1)

**Abstract**: Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. To expand this supply, we present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository. It aligns historical evidence with evolved code, reconstructs task states through Patch Reversal, Code Mapping, or Agent Reconstruction, and validates the lifecycle from a healthy base to a task state and a restored state. By deriving multiple tasks grounded in developer evidence from maintained environments, Change2Task provides executable data for coding agent training and evaluation while reducing repeated environment setup, storage, and task construction effort. We evaluate the system through five common and widely adopted coding agent task families: Bug Fix, Feature Addition, Test Generation, Application Programming Interface Migration, and Security Repair. Starting from 1,130 source changes eligible for construction, Change2Task achieves 79.6% verified task construction success across these task families. On a matched candidate set, it recovers 29.2% more verified tasks than a construction baseline based on pull requests. Historical and reconstructed cases achieve up to 98.0% matched outcome agreement under agent evaluation, while reuse of modern bases reduces measured expenditure across the complete pipeline by 10.8%.


### $β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation
**Authors**: Jiawei Xu, Minghui Liu, Juzheng Zhang, Tom Goldstein, Furong Huang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28582v1](https://arxiv.org/pdf/2607.28582v1)

**Abstract**: On-policy self-distillation (OPSD) is a promising approach to improve reasoning language models, but it remains brittle in practice: making it work reliably often requires substantial engineering effort. We identify a structural source of this difficulty: vanilla OPSD is precisely the $β=1$ member of a broader policy-optimization family, where $β$ weights the KL penalty anchoring the student to a reference policy. This equivalence turns $β$ from an implicit value fixed at one into a controllable regularization parameter, yielding a more general formulation that trades off proximity to a reference policy against privileged teacher guidance. We introduce $β$-OPSD and derive its optimal policy as a geometric interpolation between the reference policy and the privileged teacher. Directly optimizing this objective with reinforcement learning, however, would be costly and high-variance. Rather than optimize the RL objective directly, we turn its closed-form solution into a distillation target. Each value of $β$ selects a target along the reference-to-teacher path, which we implement efficiently by mixing their token-level logits. In this way, inexpensive distillation approximates the solution of expensive policy optimization. Return-to-go credit assignment further aligns token updates with the sequence-level objective while retaining the simplicity of OPSD. Experiments on mathematical reasoning benchmarks show that $β$-OPSD consistently outperforms vanilla OPSD, improving optimization stability and downstream reasoning performance. Our results provide a principled route from self-distillation to policy optimization and back without sacrificing the efficiency that makes OPSD practical.


### DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for Multimodal Retrieval-Augmented Generation
**Authors**: Jiacheng Tao, Qingyun Sun, Haonan Yuan, Ziwei Zhang, Jianxin Li

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28580v1](https://arxiv.org/pdf/2607.28580v1)

**Abstract**: While Multimodal Retrieval-Augmented Generation (MM-RAG) has shown promising results, it still struggles with complex multi-hop reasoning tasks. Existing methods primarily focus on independent instance-level matching, which often fails to capture explicit relationships across modalities and documents. Although Graph-enhanced methods introduce structural modeling, they face a fundamental challenge in multimodal scenarios: incorporating fine-grained visual features leads to rapid graph expansion and retrieval noise, whereas coarse-grained representations cause the discarding of critical local evidence. To address this dilemma, we propose DualG-MRAG, a Dual-tier framework that introduces a decoupled architecture comprising Macro-reasoning and Micro-matching Graphs for Multimodal RAG. Specifically, to suppress retrieval noise by isolating global structural reasoning from fine-grained evidence matching, we construct a Macro Graph for global topological routing and a Micro Graph for precise local verification. Subsequently, to enable dynamic relevance propagation across heterogeneous evidence sources, we formulate retrieval as a query-driven message passing process via a GNN Retriever. Furthermore, to provide the generative model with coherent structural guidance, we introduce a dynamic programming decoding mechanism that extracts explicit reasoning paths directly from the GNN's forward pass, replacing the standard input of isolated document chunks. Extensive experiments demonstrate that DualG-MRAG outperforms baselines in both evidence recall and complex QA accuracy.


### Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B
**Authors**: Iliya Mirzaei

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28576v1](https://arxiv.org/pdf/2607.28576v1)

**Abstract**: Methods that make a language model plan, criticise and rewrite its own answer, reflect on mistakes, pick the best of several attempts, or debate with copies of itself nearly all make it generate far more text than a single chain of thought. Because generating more text raises accuracy by itself, a gain over one chain of thought does not show the method's idea is what helped. Wang et al. (2024) reported that a simple baseline, sampling the same question repeatedly and keeping the most common answer, often wins once budgets are comparable, but gave point estimates with no confidence intervals or significance tests.
  We rerun that comparison as a designed experiment: seven methods, open models of 1.5B, 3B and 7B parameters, two mathematics benchmarks, 150 questions each. We count every generated token, including those spent on critiques, reflections, debate turns and checking, and compare each method against repeated sampling at its own measured cost. All 36 comparisons are paired by question, with bootstrap intervals and multiplicity correction.
  No method is reliably better than repeated sampling at equal cost anywhere. Ten are reliably worse, all of them methods where the model inspects its own output, and all 18 self-inspection comparisons are negative. The two kinds of self-inspection part company as models grow. Choosing stops hurting: taking Best-of-N's eight samples and just counting the most common answer beats letting the model pick by 8.0 and 11.3 points at 1.5B, but only 2.0 and 1.3 at 7B, no longer distinguishable from zero. Rewriting does not recover: Self-Refine and a forced Reflexion stay 3.6 to 10.1 points below baseline at 7B.
  Reflexion as published never triggered its own retry on the smallest model. It judged itself correct every time and silently became a single chain of thought. We release code, prompts, all generations, and our verification scripts.


### Algorithms for Structured Elections under Thiele Voting Rules
**Authors**: Alexandra Lassota, Krzysztof Sornat

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28575v1](https://arxiv.org/pdf/2607.28575v1)

**Abstract**: We study the computational complexity of winner determination problems in approval-based committee elections under Thiele voting rules. These form a class of rules parameterized by a fixed weight vector that specifies how a voter's satisfaction depends on the number of approved candidates elected. We first analyze the structure of optimal solutions based on the sets of voters who approve each candidate---that is, how voters' approval ballots induce dependencies between candidates---revealing constraints on a winning committee under any fixed Thiele voting rule. Using this, we design FPT algorithms for Proportional Approval Voting (PAV) and other Thiele rules on a natural restricted domain known as the Voter Interval (VI) domain---that is, after a suitable ordering of voters, each candidate is approved by a consecutive interval of voters. In particular, we show that every Thiele rule on VI is FPT with respect to a parameter for which the problem is NP-hard on general instances, even when the parameter takes constant values. Our results advance the understanding of the computational complexity of PAV on Voter Interval instances, which remains one of the central open questions in this area. We further resolve two open questions from the literature on PAV (and other Thiele voting rules) by providing a polynomial-time algorithm for instances where each candidate is approved by at most two voters, and an FPT algorithm parameterized by the total score of a winning committee.


### ORCA-bench: How Ready Are Language Model Agents for Oncall?
**Authors**: Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28545v1](https://arxiv.org/pdf/2607.28545v1)

**Abstract**: Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, and OpenSearch via Grafana) and full source-code access--with 1,079 RCA tasks that systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's $κ_w=0.90$). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard--a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access degrades every metric. Crucially, these are performances on a curated 50 GB / six-day testbed with tasks investigated in isolation on a system whose code and instrumentation are public. Since real production systems are order of magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability. We release the public set at https://hub.harborframework.com/datasets/orca-bench/ORCA-bench.


## VLA
### RoboBRIDGE: A Modular Framework for Bridging Policies to Robust Real-World Robotic Agents
**Authors**: Sihyung Yoon, Minjong Yoo, Sanghyun Ahn, Seojeong Choi, Honguk Woo

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.27881v1](https://arxiv.org/pdf/2607.27881v1)

**Abstract**: Vision-Language-Action (VLA) models have attracted growing interest as a scalable approach to robotic manipulation. While these models are effective action predictors, deploying them as robotic agents exposes critical gaps: no mechanism for failure recovery, inconsistent execution over long horizons, and limited robustness to shifts in observations, tasks, or embodiments. Existing solutions address these limitations individually through model retraining or environment-specific modules, yet what is needed is a general framework that systematically transforms a pretrained VLA into a robotic agent. We present RoboBRIDGE, a modular framework that provides an orchestration layer over five coordinated modules, namely Monitor, Perceptor, Planner, Controller, and Robot Interface, to compose robust robotic agents from off-the-shelf components, including pretrained VLAs. The Monitor pairs rapid failure detection with hierarchical recovery to correct errors before they cascade. When the environment diverges from the current plan, the Planner triggers replanning while the Perceptor updates scene understanding asynchronously, avoiding execution stalls. Within the Controller, primitive skill fine-tuning factors manipulation into domain-invariant primitives with dedicated LoRA adapters, reducing sensitivity to domain shifts when a VLA is used. Across LIBERO, RoboCasa, and real-world case studies spanning multiple robot platforms and VLA backbones, RoboBRIDGE consistently outperforms both standalone policies and prior augmented VLA deployments. These results suggest that reliable robotic agency does not arise from scaling action predictors alone, but from structured orchestration around them.


### RedFlow: Redirect Failure into Action-Level Corrections for Flow-matching VLA Policy
**Authors**: Zhengyang Yan, Junhao Li, Fangqi Zhu, Zijun Wang, Quanxin Shou, Yikun Miao, Xiaoyi Pang, Zicong Hong, Song Guo

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.27782v1](https://arxiv.org/pdf/2607.27782v1)

**Abstract**: Flow-matching Vision-Language-Action (VLA) policies have shown strong potential for robotic manipulation but often suffer from compounding errors caused by distribution shifts during deployment. While offline reinforcement learning (RL) provides a practical way to improve deployed policies using rollout data, existing methods either ignore failure data or exploit it only at the trajectory level, resulting in low learning efficiency and persistent errors. We propose **RedFlow**, a fine-grained offline RL framework that redirects failure experiences into action-level corrective supervision for flow-matching VLA policies. RedFlow consists of two key components: (1) a **Context-Aware Corrective Matching** mechanism that identifies failure-inducing actions and retrieves successful alternatives from similar contexts as corrective targets, and (2) an **Adaptive Redirection Objective** that jointly reinforces successful actions, suppresses undesirable ones, and redirects recoverable failures toward corrective targets. By converting both successful and failed experiences into dense supervision, RedFlow enables robust recovery learning from mixed-quality data. Experiments on the LIBERO benchmark and three real-world manipulation tasks show that RedFlow consistently outperforms state-of-the-art offline RL baselines, improving the real-world success rate from 56.7% to 74.7%. It also matches strong on-policy methods (PPO, GRPO, and DDPO) while requiring roughly an order of magnitude fewer training samples.


### World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models
**Authors**: Xiangcheng Zhang, Yilun Du

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.27599v1](https://arxiv.org/pdf/2607.27599v1)

**Abstract**: Building generalizable agents for diverse applications remains a fundamental challenge. While imitation learning-based policies succeed in specific training environments, they often fail to generalize to novel scenes and tasks. In this work, we propose World Action Planner, a robot planning system that leverages the reasoning capabilities of Vision-Language Models (VLMs) and the physical grounding of a multi-task pose-image conditioned world model. Our system enables an agent to propose initial action plans and iteratively refine them via optimization and search, reasoning over imagined world model rollouts. We demonstrate that our approach achieves superior performance across compositional tasks, new layouts, and zero-shot generalization scenarios, significantly outperforming state-of-the-art end-to-end policy models such as VLAs and WAMs. Project website at worldactionplanner.github.io


### Cross-Embodiment Transfer via Behavior-Aligned Representations
**Authors**: Ajay Sridhar, Jensen Gao, Jonathan Yang, Jean Mercat, Suneel Belkhale, Dorsa Sadigh

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.27549v1](https://arxiv.org/pdf/2607.27549v1)

**Abstract**: Recent progress in large-scale imitation learning for robot manipulation has been driven by leveraging datasets across a wide range of robot embodiments. However, achieving significant cross-embodiment transfer is often still challenging. In this work, we study the role of using behavior-aligned representations (e.g., object bounding boxes, language motions, end-effector traces of robot motion) in vision-language-action (VLA) models to promote cross-embodiment transfer. We hypothesize that by possessing invariances across embodiments while being predictive of robot actions, these representations can help unify large-scale cross-embodiment data to enhance transfer. To assess our hypothesis, we develop a simulation-based benchmark designed to assess transfer with diverse cross-embodiment data to new embodiments. Using this benchmark, we compare different representations and ways of incorporating them. We identify that end-effector traces can be particularly beneficial for transfer, representations are generally more useful with larger prior datasets, and can be used to benefit from action-free data. We also demonstrate that they can enhance sim-to-real cross-embodiment transfer, improving task completion progress of real robot policies pre-trained on simulation data by 28%. We provide videos of our evaluations at our website: https://ajaysridhar.com/barx/.


### DLAM: Distributional Latent Actions with Temporal Constraints
**Authors**: Zuojin Tang, Feifan Luo, Haoyun Liu, Botai Yuan, Dekang Qi, Ronghan Chen, Yandan Yang, Tong Lin, Xinyuan Chang, Mu Xu, Bin Liu, De Ma, Zhiheng Ma

**Published Date**: 2026-07-29

**Updated Date**: 2026-07-29

**PDF Url**: [2607.27138v1](https://arxiv.org/pdf/2607.27138v1)

**Abstract**: Vision-language-action (VLA) models remain constrained by scarce action-labeled robot data, whereas action-free videos offer abundant observations of physical change. Latent action models can extract such priors, but reconstruction-trained codes may predict future observations without the structure required for joint generation with robot actions. Existing structured methods add temporal constraints but retain deterministic transition points, so residual errors in locally inferred transitions may propagate and compound under recursive composition. We introduce DLAM, a distributional latent-action model that represents each transition as a diagonal Gaussian. Reconstruction conditioned on the reference frame grounds the mean in observed visual change, while normalized composition and reversal over equal-gap triplets constrain both the mean and dimension-wise variance. Variance composition uses a lightweight shared-correlation coefficient to account for dependence between adjacent transitions that share an intermediate frame, whereas reversal negates the mean and preserves the variance. For downstream policy learning, we freeze the encoder and train a flow-matching policy to jointly generate mean transition sequences and robot actions. On held-out transitions, DLAM learns more temporally consistent latent dynamics than existing latent-action baselines and achieves stronger direct and cumulative reconstruction on held-out videos. Under the same controlled $π_0$ transfer protocol, it also improves policy performance on MetaWorld MT50, LIBERO, and real-world manipulation tasks. Controlled ablations show that normalized mean constraints account for most of the reconstruction gain, while learned variance and correlation-aware composition provide complementary improvements in downstream control.


## Agent
### AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis
**Authors**: Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28618v1](https://arxiv.org/pdf/2607.28618v1)

**Abstract**: Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying claim: each paper is converted into atomic, typed claims, each grounded by a source DOI and a verbatim quote or an explicit evidence locator. Over this shared claim store, AskChem exposes complementary structures for search and synthesis: a stabilized faceted taxonomy for hierarchical retrieval and browsing, an evidence graph linking claims through relations, and an exploratory living taxonomy that situates indexed papers under scientific principles. AskChem currently indexes 2.4M claims from 147K papers and provides a web interface, as well as REST, SDK, and MCP access for AI agents. On AskChem-Bench, grounding a GPT-5.5 reader in AskChem yields 100% resolvable DOIs, compared with 88.3% without retrieval, and the highest citation density among five tested systems. AskChem is live at https://askchem.org.


### OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models
**Authors**: Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li, Kaiming Jin, Xinfeng Yuan, Zhoumianze Liu, Jingyang Gong, Zhangyue Yin, Jiahui Gao, Zhiyong Wu, Tianbao Xie, Jianbing Zhang, Ben Kao, Lingpeng Kong

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28609v1](https://arxiv.org/pdf/2607.28609v1)

**Abstract**: Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.


### PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks
**Authors**: Manyi Wang, Junjielong Xu, Pinjia He

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28587v1](https://arxiv.org/pdf/2607.28587v1)

**Abstract**: SWE-bench-like benchmarks are widely used for evaluating LLM's issue resolution capability. They typically follow a common construction pipeline: each PR (Pull Request) is paired with its linked issue by extracting issue references from the PR description; the issue description is used as the problem statement, and the PR patch serves as the test oracle. However, due to the inherent complexity of developing and maintaining large repositories, such PR-Issue pairings are often misaligned in practice. In this work, we systematically study SWE-bench Verified instances, finding that 13.6% exhibit misalignment across five patterns in eleven fine-grained scenarios. To enable reliable and scalable construction of those benchmarks in the future, we propose PAIChecker, a multi-agent system for checking PR-Issue misalignment in SWE-bench-like benchmarks. Specifically, PAIChecker adopts a three-phase design that combines specific pattern identification, cross-agent label synthesis, and code-level validation, thereby enabling more accurate, generalizable, and progressively verified detection. Experiments on SWE-Gym and SWE-bench Multilingual show that PAIchecker achieves the best performance across all four LLM backbones, reaching up to 92.12% and 91.67% binary accuracy, respectively.


### Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs
**Authors**: Woongkyu Lee, Jungwook Choi

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28573v1](https://arxiv.org/pdf/2607.28573v1)

**Abstract**: Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging. While recent studies show that inference-time scaling can improve frontier computer-use agents through additional computation during execution, its effectiveness for resource-constrained local models remains poorly understood. We present a systematic empirical study of inference-time scaling in local CUAs across contextual, temporal, structural, and parallel dimensions. We evaluate Qwen3-VL-8B/30B-A3B, UI-TARS-1.5-7B, and OpenCUA-7B on the OSWorld benchmark. Our results show that additional computation often yields diminishing returns while changing failure modes. Contextual scaling provides historical grounding that improves trajectory stability and task accuracy, but its gains saturate as token cost increases and failures shift from repetitive or stalled trajectories toward premature false successes. Temporal scaling similarly reduces max-step stalls, yet does not substantially improve task success, indicating that longer horizons often extend erroneous trajectories rather than correct them. We further find that structural decomposition can introduce planning and formatting overhead in local two-stage agents, while parallel scaling partially mitigates these failures at a substantial computational cost. Overall, our findings suggest that efficient local CUAs require selective compute allocation, failure-aware control mechanisms, and agentic frameworks designed around the capabilities and limitations of local models.


### MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems
**Authors**: Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28527v1](https://arxiv.org/pdf/2607.28527v1)

**Abstract**: Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.


### Selective Credibility-Limited Belief Update
**Authors**: Theofanis Aravanis, Costas D. Koutras

**Published Date**: 2026-07-30

**Updated Date**: 2026-07-30

**PDF Url**: [2607.28523v1](https://arxiv.org/pdf/2607.28523v1)

**Abstract**: Belief update concerns changes in an agent's beliefs induced by changes in the underlying world. Standard Katsuno-Mendelzon update assumes that an epistemic input can be incorporated from every initially possible world, whereas credibility-limited belief update restricts, for each source world, the successor worlds regarded as credible or reachable. Nevertheless, existing credibility-limited approaches treat the epistemic input as an indivisible whole, and therefore cannot represent cases in which only part of a compound epistemic input can be realized. We introduce selective credibility-limited belief update, in which the epistemic input is transformed, relative to each source world, into a weaker proxy before the credibility-limited transition is performed. We provide semantic and axiomatic characterizations of the resulting class of update operators. We then identify two well-behaved sub-classes; namely, consistency-preserving update operators, which require every transformed epistemic input to be credible from its source world whenever the original epistemic input is consistent, and maximal consistency-preserving update operators, which additionally require the selected proxy to be maximally informative among the credible consequences of the original epistemic input. Finally, we establish the generality of the proposed framework by showing that credibility-limited belief update is recovered as a special case, while Katsuno--Mendelzon belief update emerges when credibility restrictions are removed and the transformation functions are taken to be identities. These results demonstrate that the framework provides a unified and strictly more expressive account of belief update, encompassing established approaches while supporting source-dependent selective acceptance.


