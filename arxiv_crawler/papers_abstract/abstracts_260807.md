# Abstracts of Papers

## World Model
### Learning When to Trust via Selective Context Preference Optimization
**Authors**: Xian Sun, Wei Chow, Yingshuo Wang, Junhao Liu, Wei Gao, Qing Wu, Lingdong Kong

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06377v1](https://arxiv.org/pdf/2608.06377v1)

**Abstract**: Language models increasingly condition their answers on external signals, and a single misleading one can turn a correct answer wrong. The obvious remedy, training models to resist such signals, hides a failure mode: a model that ignores all context looks robust yet is useless when the context is worth trusting. We recast the problem as selective trust and introduce MIST, a human-annotated benchmark that renders each reasoning item under four matched conditions (clean, misleading, correct-context, and irrelevant-context), together with SC2W, a paired metric counting how often a misleading signal flips a clean-correct answer to wrong. Across a comprehensive benchmark study, we observe that such a susceptibility is universal. We then propose SCOPE, which mines clean-correct/misleading-wrong failures and optimizes a standard Direct Preference Optimization (DPO) objective over matched preference pairs balanced equally across all four conditions, rather than over misleading items alone. Our approach substantially reduces SC2W on popular open-sourced models while preserving accuracy when the added context is clean, correct, or irrelevant. With this work, we argue that models should be judged on selective trust, not on resistance alone.


### $ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation
**Authors**: Zhe Li, Zhenzhe Zhang, Yangyang Wei, Wenjie Zhang, Xichen Yuan, Peiyuan Zhi, Gen Li, Xinying Guo, Fengjie Gao, Jianfei Yang, Shanghang Zhang

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06375v1](https://arxiv.org/pdf/2608.06375v1)

**Abstract**: Humanoid household tasks often require concurrent loco-manipulation, where the robot must move, adjust posture, maintain balance, and manipulate objects as a single coordinated behavior. Yet existing humanoid policies typically decompose locomotion and manipulation, while recent world-action models remain either arm-centric or video-centered. We present $ω$-0, a latent predictive whole-body world-action model for real-world humanoid concurrent loco-manipulation. Given a language instruction, current visual observation, and robot proprioceptive state, $ω$-0 directly predicts controller-compatible whole-body action latents for real-robot execution. Rather than reconstructing future videos, $ω$-0 learns compact future observation embeddings as a lightweight predictive objective, coupling latent visual foresight with diffusion-based whole-body action generation. The model supports egocentric RGB, exocentric RGB, and exocentric depth inputs, and leverages controller-based simulation replay to ground human/public visual-motion priors into robot-executable action latents. We further collect $ω$-HOME, a 40+ hour real-world household humanoid dataset with synchronized multi-view observations, whole-body SMPL motions, robot states, and action latents. Real-world experiments on 11 household tasks demonstrate that a single $ω$-0 model can produce smooth manipulate-while-moving behaviors and consistently outperform representative imitation learning, VLA, humanoid, and WAM baselines.


### DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation
**Authors**: Junfeng Li, Junjie He, Zhide Zhong, Yangyang Zheng, Pingyue Sheng, Jiayu Dong, Ruixin Li, Haodong Yan, Jiaguan Zhu, Tianran Zhang, Runze Yu, Wen Chen, Liuqing Yang, Yuxiang Gao, Haoang Li

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06374v1](https://arxiv.org/pdf/2608.06374v1)

**Abstract**: Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations. First, they underuse dynamics priors shared across diverse visual and interaction data, limiting cross-embodiment transfer. Second, they require extensive manual preprocessing to convert embodiment-specific actions into a common format. To overcome these limitations, we propose DyPES-VLA, a cross-embodiment VLA that learns shared Dynamics Priors and Embodiment-Specific control. First, we learn shared dynamics priors by training the vision-language model (VLM) with a future-prediction objective on cross-embodiment data, driving the shared query representation to capture object motion, contact, and interaction-induced scene changes. Second, an embodiment-specific Mixture-of-Experts (MoE) action head translates these shared dynamics priors into executable controls directly in each embodiment's native action space, without manually pre-aligning heterogeneous actions into a common format. This head shares attention layers to capture common temporal action structures, while its embodiment-specific feed-forward experts resolve the unique kinematic constraints and control semantics of distinct embodiments. As a generalist policy, our \ourmethod achieves state-of-the-art performance across simulation and real-world evaluations, reaching 98.0% success on LIBERO, 59.25% on RoboCasa-GR1, and 89.02% on RoboTwin~2.0.


### The Bitter Lesson of Tool Calling
**Authors**: Ishan Patel, Sahil Sen, Elias Lumer, Vamse Kumar Subbiah

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06370v1](https://arxiv.org/pdf/2608.06370v1)

**Abstract**: Tool use transforms LLMs into agents that act beyond their training data, and for code-capable models, programmatic tool calling extends this further by replacing rigid JSON calls with scripts that chain and parallelize naturally. However, a systematic evaluation of tools as code on an established benchmark across current and prior model generations under real-world task conditions has not been conducted. In this work, we empirically compare programmatic tool calling (PTC) to native JSON tool calling across 14 language models on BFCL v4. In the programmatic tool calling paradigm, tools are exposed as typed Python stubs that the model invokes through code, with execution and results handled in a single agent turn. Programmatic tool calling matches or exceeds native JSON tool calling in 11 of 14 models on BFCL v4, with the GPT-5.6 family achieving a 10.6% improvement over the JSON tool calling baseline. Further, it matches or outperforms baseline in 13 of 14 models under parallel fan-out, and holds stable under context rot conditions where baseline degrades 2.3% on average. Our results demonstrate that programmatic tool calling is a viable and robust alternative to JSON tool calling, with performance tracking model capability across release generations.


### Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering
**Authors**: Soorya Ram Shimgekar, Michelle Hu, Dorisa Shehi, Daniel Kang, Roy Ka-Wei Lee, Koustuv Saha, Christian Poellabauer, Christopher Lee, Sajeev Singh, Piyum Zonooz, Navin Kumar, Zeeshan Ahmed, Priyadarshini Kachroo

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06366v1](https://arxiv.org/pdf/2608.06366v1)

**Abstract**: Electronic health record (EHR) feature engineering is a major bottleneck in clinical research and AI, accounting for 39-45% of data scientists' workload. This is especially pronounced in heart failure, which affects an estimated 6.7 million U.S. adults and requires integrating fragmented EHR data with disease-specific, guideline-based clinical reasoning. Existing rule-based and large language model (LLM)-based approaches offer only partial automation with limited maintainability and evidence traceability. We developed the Nimblemind Multi-Agent System (nMAS), an evidence-linked, rubric-grounded pipeline for automated heart-failure feature engineering, and evaluated it on 500 dummy patient records from nine EHR source tables. nMAS generated 132 structured and 70 rubric-scored aggregated features, verified for structural integrity, rubric compliance, and provenance, and audited by a restricted LLM. Adding the aggregated features improved held-out AUROC from 0.895 to 0.963 for HFrEF and 0.870 to 0.910 for HFpEF phenotyping, and an independent LLM-based rubric assessment of evidence support and methodological soundness scored the features at 81.5% of maximum points. These results demonstrate the feasibility of automated, auditable feature engineering for complex cardiovascular EHR data, though evaluation was limited to a single-institution cohort and external validation is needed.


### AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games
**Authors**: Boning Li, Yu Chen, Longbo Huang

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06362v1](https://arxiv.org/pdf/2608.06362v1)

**Abstract**: Deciding which of two agents is stronger means playing games until skill outweighs luck, and every game costs money, model inference, or expert time. Since the number of games needed is unknown, fixed-budget evaluations either keep paying after the result is settled or stop before the agents can be told apart, while naive optional stopping with an ordinary confidence interval invalidates the stated level. We make such an evaluation stop as soon as its evidence suffices, with the guarantee intact. The Action-Informed Value Assessment Tool (AIVAT) reduces variance in imperfect-information games through conditional mean-zero corrections, by a median $54\times$ across 15 LLM agent configurations spanning 71,439 paired Heads-Up No-Limit Hold'em (HUNL) hands, but does not say when to stop. We combine AIVAT with continuously monitored Confidence Sequences (CSs) into anytime-valid AIVAT (AV-AIVAT), whose online value model learns only from past games so that no game scores its own correction. At the nominal 95\% level and a target precision of $\pm1$ Big Blind, raw outcomes need a median $74\times$ as many hands as AIVAT-corrected outcomes to stop under the Asymptotic CS (AsympCS). Exact finite-sample certification uses the Empirical-Bernstein CS (EB-CS), which needs an independently justified bound on corrected payoffs. We establish such a bound structurally for Leduc hold'em and characterize a width floor set by the CS's bet cap and that bound, which governs how much of a variance gain becomes earlier stopping; the descriptive HUNL EB-CS runs show a median $1.37\times$ stopping-time ratio. AV-AIVAT turns variance reduction into efficient, auditable early stopping while separating asymptotic screening from exact certification, so an evaluation can stop the moment its evidence suffices and hand a third party everything needed to recheck the verdict at that very stopping time.


## Generation
### Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data
**Authors**: Donna Hooshmand, Shubham Shahi, Cameron Barrie, Abhratanu Dutta, Marko Sterbentz, Harper Pack, Kristian J. Hammond

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06331v1](https://arxiv.org/pdf/2608.06331v1)

**Abstract**: From natural-language query interfaces to automated report generation, data analysis tools need a description of the data: the real-world entities it contains, which columns function as measures or identifiers, and how tables connect into units of analysis. Today, this semantic layer is usually written by hand. This is a knowledge-acquisition bottleneck that limits the scalability of analytic systems, keeps non-technical users dependent on experts, and is itself error-prone. We present TYTAN, a system for automatically constructing an analytic semantic schema from a relational database and, when available, a short user-provided description. TYTAN combines symbolic analysis of the database with LLM-based semantic inference for entity proposal, role assignment, and naming. When the evidence leaves a decision ambiguous, TYTAN asks the user a targeted natural-language question. We evaluate TYTAN on eight databases spanning real-world and benchmark domains along the three axes that define a schema's functional utility: (i) coverage, are all important entities and features captured?; (ii) retrieval correctness, do the schema's instructions actually reach the data; and (iii) characterization accuracy, are semantic types correct? Across the seven reference domains, TYTAN reaches every entity, attribute, and aggregable feature of the expert-corrected reference schemas (100% coverage). Additionally, 100% of its retrieval instructions execute correctly (1,678 of 1,678 self-generated claims), and semantic roles agree with the reference on 92-100% of matched attributes. Checking the underlying data showed the small disagreement is in the reference, not in TYTAN. On a held-out blind test (a live, ten-table database with no declared keys), TYTAN recovers the full entity structure with verified keys and satisfies 100% of the satisfiable expectations of five independent blind annotators.


### Benchmarking the Benchmarks: Evaluating Benchmarks for Conversational Agents
**Authors**: Noam Koren, Roy Bar-Haim, Abigail Goldsteen

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06329v1](https://arxiv.org/pdf/2608.06329v1)

**Abstract**: Task-oriented conversational agents are evaluated using curated or automatically generated benchmarks, yet benchmark quality is rarely assessed. Poor benchmarks may contain inconsistent tasks, simplistic scenarios, or limited policy coverage, leading to unreliable evaluations. We introduce a reference-free framework that uses LLM judges to assess benchmark consistency, complexity, and policy coverage, while providing actionable diagnostics of weaknesses. We validate the framework by demonstrating agreement with independent human annotations and by evaluating benchmarks generated by LLMs of varying capabilities, as well as benchmarks subjected to controlled quality-degrading perturbations. Across domains and judge models, the proposed metrics consistently distinguish between benchmark quality levels. We further demonstrate the framework's applicability to manually curated benchmarks. Our framework offers a practical approach for evaluating synthetic and manually curated conversational-agent benchmarks.


### RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction
**Authors**: Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06310v1](https://arxiv.org/pdf/2608.06310v1)

**Abstract**: Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation arises from a mismatch between the comparative nature of generative reward modeling and the scalar scoring paradigm adopted by existing RL algorithms. To bridge this gap, we propose a Ranking-based Reward Construction (RRC) approach, which enables generative reward models to provide more effective RL learning signals by deriving rewards from relative preference rankings. RRC introduces two complementary strategies: self-competitive ranking, which exploits comparisons among sampled responses, and anchor-guided ranking, which enables scalable ranking-based reward construction with a small set of reference responses. Experiments across open-ended chat and reasoning benchmarks demonstrate that RRC substantially improves RL training with generative reward models, achieving consistent gains over existing reward construction approaches. Our code can be found at https://github.com/wangclnlp/RRC.


### Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations
**Authors**: Sagar Tamang, Ayush Vyas, Tabarakul Hazarika

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06305v1](https://arxiv.org/pdf/2608.06305v1)

**Abstract**: Retrieval-augmented generation over long documents is dominated by one design: chunk the text, embed the chunks, and surface the top-k nearest neighbours of the query. We argue that for an important class of documents -- financial statements, audit reports, regulatory returns -- this design is structurally unsound, and we make the argument measurable. On a 780-page government financial report, 86.8% of content lines are table rows, thousands of near-identical figures compete in one embedding space, and a figure inherits its unit from a header a median of 13 lines above it -- so a chunk boundary routinely separates a number from whether it is in lakh or crore, an error of two orders of magnitude. A table-aware chunker built as a steelman fixes the unit problem but leaves 27-30% of numeric chunks with no fiscal-year header at every chunk size we tried. We propose READ (Reliable Embedding-free Agentic Document-search), in which an agent reads the raw document through three deterministic operations -- normalized lexical search, structural navigation, and bounded span reads -- exposed over the Model Context Protocol, so a trajectory is a replayable audit trail, not an opaque similarity score. On 51 verified questions READ answers 58.8% against dense retrieval's 15.7% (p_Holm = 2 x 10^-5) -- or 35.3% tuned, which READ still leads by 23.5 points (p_Holm = 0.017). An agent given the same loop but a top-k tool reaches only 27.5%, locating the gain in the interface rather than in iteration. We also report what the evidence does not support: BM25 is statistically indistinguishable from READ, so our result separates embedding-based from embedding-free retrieval, not agentic from lexical search.


### On-Policy Self-Distillation without Any Supervision
**Authors**: Yijiang Li, Bingyang Wang, Yijun Liang, Yunjie Tian, Di Fu, Nuno Vasconcelos

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06296v1](https://arxiv.org/pdf/2608.06296v1)

**Abstract**: On-policy (Self-)Distillation (OPD / OPSD) has shown strong potential for post-training large language models (LLMs). However, existing methods still rely heavily on external supervision, including ground-truth signals, environmental feedback, or guidance from larger models, and therefore fall short of genuine "self"-distillation. In this study, we show that on-policy self-distillation can be achieved using only a model's own generations via internal consistency. We propose Unsupervised On-Policy Self-Distillation (U-OPSD). U-OPSD first samples multiple rollouts and constructs a pseudo-solution by majority vote under a self-consistency threshold. It then conditions a teacher distribution on the shortest pseudo-solution and distills it into prefixes of the model's longest incorrect completion, allowing the model to correct itself precisely where it is confidently wrong. Across diverse benchmarks, base models, and training settings, U-OPSD consistently improves over the base models and matches or surpasses supervised methods with ground truth (GT), such as OPSD and GRPO. On AIME24, AIME25, HMMT25, MATH500, and AMC23, U-OPSD improves over the base model by 8.5% and 10.7% on Qwen3 non-thinking mode at the 4B and 8B scales, respectively, and outperforms OPSD by an average of 3.2% and 2.3%. In thinking mode, U-OPSD remains on par with OPSD, outperforming it by 0.9% at 4B and matching it at 8B, while surpassing GRPO by 0.7% and 1.1%, respectively.


### Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints
**Authors**: Omid Bazgir, Md Nasir, Jacob Hoffman, Yang Yang, Manu Agrawal, Anusua Trivedi, Vinay Rao Dandin, Chris Gibbons, Christine Swisher

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06265v1](https://arxiv.org/pdf/2608.06265v1)

**Abstract**: Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice.
  We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility floor. We instantiate this idea on a care-gap benchmark derived from Synthea-generated patients exercised through demonstration electronic health record workflows and then processed by the same downstream pipeline as operational data. Realism is measured through missingness structure, simplicity, structural plausibility, and population alignment.
  The baseline benchmark is extremely thin: sampled-pair missingness is 79.44%, only 12.75% of rows are actionable, 38.94% of patients have zero actionable measures, and top-three token concentration reaches 100.0%. Two deterministic revisions improve these panels while remaining above the current utility floor, whereas a naive densification control preserves unrealistic templating. We further show that internal benchmark realism and source fidelity to an aggregate operational reference are related but distinct objectives. These results suggest that synthetic benchmark quality should be optimized explicitly, with utility treated as one constraint rather than as sufficient evidence of realism.


## VLA
### SkillMemo: Expert-guided Skill Memory Framework for Compositional Embodied Manipulation
**Authors**: Changyuan Wang, Chubin Zhang, Zhenyu Wu, Runhao Li, Angyuan Ma, Ke Chao, Yinan Liang, Xiuwei Xu, Ziwei Wang, Yansong Tang, Jiwen Lu

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.05970v1](https://arxiv.org/pdf/2608.05970v1)

**Abstract**: Embodied visuomotor models, including Diffusion Policy (DP) and Vision-Language-Action (VLA) models, have demonstrated promising performance on robotic manipulation benchmarks. However, their potential remains fundamentally constrained by the scarcity of large-scale embodied trajectory datasets, leading to insufficient compositional generalization in out-of-distribution (OOD) scenarios with limited capability to capture reusable skill structures. To address this limitation, we propose Skill-Based Memory (SkillMemo) framework that implicitly decomposes long-horizon demonstrations into latent atomic skills and integrates skill-level features into a dynamic episodic memory bank for solving compositional tasks. Specifically, we first introduce an expert-guided trajectory segmentation module built upon a Mixture-of-Experts (MoE) architecture, which implicitly partitions trajectories into distinct skill primitives represented by learned gating coefficients. We further design a skill-level episodic memory architecture that stores compact skill representations as retrievable key-value pairs. During inference, the memory bank retrieves the most relevant skill primitives which are subsequently fused with the model's current gating distribution, providing a robust contextual prior to refine action predictions. Extensive experiments on the simulation benchmark and real-world manipulation tasks demonstrate that SkillMemo consistently enhances both DP and VLA backbones, achieving state-of-the-art performance and outperforming $π_{0.5}$, while exhibiting strong compositional generalization to unseen task configurations.


### Explicit Language Memory for Long-Horizon Planning in Vision-Language-Action Models
**Authors**: Houze Xu, Jizhong Li, Ziyi Ye

**Published Date**: 2026-08-05

**Updated Date**: 2026-08-05

**PDF Url**: [2608.04765v1](https://arxiv.org/pdf/2608.04765v1)

**Abstract**: Vision-language-action (VLA) models provide a unified paradigm for connecting visual perception, language understanding, and robotic control. However, existing VLA models still face major challenges in long-horizon tasks: sparse expert demonstrations constrain cross-task compositional generalization; the non-Markovian nature of long-horizon tasks makes it difficult for policies conditioned only on current observations to maintain temporal consistency; limited closed-loop error correction allows execution errors to accumulate; and end-to-end action fine-tuning may weaken the high-level semantic representations of vision-language model (VLM) backbones. To address these issues, we propose a hierarchical long-horizon VLA architecture with an explicit language-memory module. The central idea is to convert discrete temporal observations into a coherent textual memory sequence with temporal logic. The system is decoupled into a high-level VLM and a low-level VLA: the high-level VLM performs semantic reasoning through a visual question answering training paradigm, while the low-level VLA executes precise continuous control conditioned on subtask instructions and visual observations. The high-level VLM recursively updates both language memory and subtask instructions using the previous memory as a contextual anchor, enabling persistent temporal tracking and dynamic correction during long-horizon execution. We evaluate the proposed method in multiple simulation environments and conduct sim-to-real experiments on a real robotic platform. The results demonstrate that explicit language memory improves the success rate and robustness of VLA models on complex long-horizon tasks while providing an interpretable semantic account of the decision process.


### Suppression Sticks, Locality Is Fragile: A Closed-Loop Target-and-Control Audit of Task-Vector Negation in VLA Policies
**Authors**: Shaoguang Wang, Weiyu Guo, Rushi Dai, Yiren Zhao, Yandong Guo, Hui Xiong

**Published Date**: 2026-08-05

**Updated Date**: 2026-08-05

**PDF Url**: [2608.04692v1](https://arxiv.org/pdf/2608.04692v1)

**Abstract**: Task-vector arithmetic offers a closed-form way to modify a model, yet its behavioral locality remains unclear in closed-loop robot control. We present a target-and-control audit of per-skill task-vector subtraction from multitask vision-language-action (VLA) policies. Across all ten LIBERO-Goal skills, subtraction produces three qualitatively different regimes: target-control separation for five skills, resistance for three, and global collapse for two. On held-out initial states, the five suppressible targets remain at 0% success; however, mean baseline-normalized control retention is only 52%, and each target-suppressing edit materially harms at least one nominally unrelated control. Additional Goal panels show separation across tested policies with continuous-regression, discrete-token, and flow-matching action heads, whereas we observe no clean separation on Spatial and control collapse on the tested Object and Long-horizon panels. Mean task-vector cosine does not account for this variation. A matched-norm control identifies a local sign asymmetry around one Goal anchor, while multi-vector outcomes vary with anchor and scale. Retain-aware gradient baselines provide data-dependent comparators but require removal-time data and optimization; subtraction is data- and gradient-free only at edit time, assuming precomputed expert deltas. Finally, a single-skill relearning probe is consistent with behavioral masking, not certified unlearning. These results characterize task-vector subtraction as a fast but brittle intervention and underscore the need for closed-loop target-and-control evaluation when assessing locality in embodied model editing.


### GUARD: Grounding Uncertainty and Ablation-Based Risk Detection for Diffusion-Based VLAs
**Authors**: Suhas Hegde, Jitendra Yasaswi Bharadwaj Katta

**Published Date**: 2026-08-05

**Updated Date**: 2026-08-05

**PDF Url**: [2608.04510v1](https://arxiv.org/pdf/2608.04510v1)

**Abstract**: Diffusion-based vision-language-action (VLA) policies can generate plausible actions even when their predictions are weakly grounded in the visual and language evidence defining the task. We introduce GUARD, a test-time failure detection method that measures this grounding without modifying the pretrained policy. GUARD estimates the influence of token-indexed entries in the final vision-language model key-value (KV) cache, constructs counterfactual caches by ablating salient KV entries, and compares their denoising responses with the original conditioning. Based on the comparison, we derive GUARD diagnostic stream including sensitivity, attention entropy, modality bias, and grounding efficiency, which are calibrated online and processed by a lightweight temporal classifier. We evaluate GUARD under task-held-out splits across five policy-benchmark settings, using Pi0, SmolVLA, and Alpamayo-1.5 on LIBERO, SimplerEnv, MetaWorld, and PhysicalAI-AV. GUARD achieves the best ROC-AUC on four of five unseen-task settings and ranks second on the remaining setting, improving the average unseen-task ROC-AUC by 5.73 percentage points over the strongest competing runtime monitor while remaining within 0.19 points of the best seen-task average. These results show that directly probing action-head dependence on multimodal evidence provides a transferable failure signal across policies, tasks, embodiments, and domains.


### Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference
**Authors**: Zheng Liu, Zeyu Guo, Zihan Liu, Anbang Wu, Han Zhao, Fangxin Liu, Zhezhi He, Yinhe Han, Jingwen Leng, Minyi Guo, Yiming Gan, Yu Feng

**Published Date**: 2026-08-05

**Updated Date**: 2026-08-05

**PDF Url**: [2608.04428v1](https://arxiv.org/pdf/2608.04428v1)

**Abstract**: Vision-language-action (VLA) models have emerged as a key component in embodied AI. Among existing approaches, diffusion-based VLA models achieve superior motion quality and generalization. However, diffusion-based VLA models are compute-intensive and must run at high control frequency, e.g., 50-200 Hz. Thus, it imposes strict latency and energy constraints on edge devices.
  In this work, we present Deltoris, an algorithm-hardware co-design framework for efficient diffusion-based VLA inference. First, we exploit the temporal similarity of consecutive inputs and propose a \textit{temporal-aware bit-sparsity} algorithm that computes only the differences between consecutive inputs, eliminating redundant bit-level operations. To further address the extra off-chip traffic introduced by our algorithm, we propose a \textit{speculative inference} technique, which amortizes data loading across multiple control steps. Lastly, to support these techniques, we co-design a dedicated accelerator with customized 1D systolic bit-serial PE arrays that eliminate PE workload imbalance. Our evaluation shows that Deltoris achieves up to 34.2$\times$ speedup over mobile GPUs and 6.1$\times$ over prior accelerators, while maintaining comparable accuracy.


### SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation
**Authors**: Nie Lin, Takehiko Ohkawa, Sijin Chen, Ruoshi Wen, Zhuohang Li, Liqun Huang, Zhengming Zhu, Yiming Bao, Yunfei Li, Minjie Cai, Xiao Ma, Wei Xu, Yoichi Sato

**Published Date**: 2026-08-04

**Updated Date**: 2026-08-04

**PDF Url**: [2608.04196v1](https://arxiv.org/pdf/2608.04196v1)

**Abstract**: Recent years have witnessed an explosive trend of scaling ego-centric human videos for robot manipulation, yet it remains unclear which data actually benefits dexterous manipulation. We present SiMDex, a similarity-based data mining framework that casts human data selection for VLA post-training in dexterous manipulation as a recommendation problem. For each robot demonstration, SiMDex employs a three-layer recall-ranking-re-ranking pipeline to extract task-relevant subsets from a pool of ~32M egocentric human samples, operating in a morphology-agnostic action space that requires no changes to VLA architecture or training. Against a strong baseline trained with an equal amount of randomly sampled human data, SiMDex uses only ~1.49M mined samples (<5% of the pool) yet improves the overall success rate from 47.7% to 61.1%, showing that selective curation outperforms indiscriminate data mixing.


## Agent
### Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents
**Authors**: Praphul Chandra, Sujit Gujar, Ganesh Ghalme

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06353v1](https://arxiv.org/pdf/2608.06353v1)

**Abstract**: We give a formal mechanism design model for the continuous participatory governance of a deployed AI agent. The mechanism is built on the principle that governance should control an AI agent through resource allocation so as to make authorization self enforcing via compute budgets. The mechanism seeks to establish the Safe AI paradigm that compute is an effective governance lever. We situate our work as a compliance or commons overlay on a deployer. One governance period is an extensive form game in which verified human stakeholders arrive sequentially and contribute, on a provision or a rejection market, in a governance currency that is deliberately distinct from the agents compute. A funding aggregator turns raw contributions into breadth weighted effective supports - a two threshold gate with hysteresis converts net support into a binary authorization that, through a coupling map bounded by an exogenously certified safety ceiling, releases a metered compute budget - realized in hardware as a signed compute license so that the decision is self-enforcing. We characterize the class of agents the mechanism can govern and isolate manipulation of the governing electorate by the governed agent as the central open problem. We also introduce several challenges addressing manipulation of governing electorate by the governed agents.


### CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks
**Authors**: Fanzhe Meng, Guoxin Chen, Jiale Zhao, Shuang Sun, Zhiyu Lin, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, Kai Jia

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06352v1](https://arxiv.org/pdf/2608.06352v1)

**Abstract**: Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting. In this paper, we present CalibForge, an autonomous terminal-task synthesis system that uses verified solver behavior to revise candidate tasks through adversarial solver calibration. Multi-solver calibration targets disagreement within a heterogeneous solver pool, whereas contrastive solver calibration targets a designated strong-pass/weak-fail relation; both operationalize a solver-relative learnable zone anchored in demonstrated solvability. Using CalibForge, we construct 5,431 calibrated terminal tasks. Our ablations show that both strategies yield more effective supervision than authoring and validation alone or ordinary single-solver feedback. Models trained on the full collection achieve 32.58% and 47.57% on Terminal-Bench 2.0. The largest improvements over the corresponding base model reach 24.71 percentage points on Terminal-Bench 2.0, 27.68 points on SWE-bench Pro, and 30.04 points on Doc2Repo. Together, these results support solver-relative learnability as a practical target for constructing effective and transferable agent training data.


### TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories
**Authors**: Yunjia Qi, Zehua Yin, Xintong Shi, Hao Peng, Songyuanyi Lu, Yixian Liu, Richeng Xuan, Yuhong Liu, Zhichao Hu, Xiaozhi Wang, Lei Hou, Bin Xu, Juanzi Li

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06346v1](https://arxiv.org/pdf/2608.06346v1)

**Abstract**: LLM-based agentic systems have shown remarkable capabilities in complex domains, while suffering from cascading errors and difficulty in debugging. Critical error detection aims to locate the earliest error step in a failed trajectory that is responsible for the final failure. However, progress faces two main challenges. First, long trajectories make it difficult to identify individual errors, since the evidence for judging a step may be scattered across distant instructions, observations, and prior context. Second, failed trajectories often contain multiple local errors with different downstream effects, only some of which remain responsible for the final failure. In this work, we propose TrajDebug, an error-lifecycle tracing framework that addresses long-trajectory error discovery with multi-granularity history compression and evidence-based error identification, and supports critical attribution by tracing each error's resolution status and terminal impact. We further construct TrajErrBench, a benchmark of 486 manually annotated failed trajectories from Tau2Bench and SWE-Bench Pro, covering realistic tool-use and coding scenarios. Experiments across diverse agent benchmarks show that TrajDebug achieves the best overall performance over existing baselines, and application studies further demonstrate that its diagnoses provide actionable feedback for improving downstream agent success. We will release the codes and data to facilitate further research.


### HarnessOpt-Bench: Evaluating LLMs at Harness Optimization
**Authors**: Varun Ursekar, Apaar Shanker, Yash Maurya, Shehab Yasser, Vijay S. Kalmath, Veronica Chatrath, Yuan Xue

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06301v1](https://arxiv.org/pdf/2608.06301v1)

**Abstract**: As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measuring how well frontier LLMs perform at this task. We introduce HarnessOpt-Bench, a benchmark for end-to-end harness optimization under expensive and stochastic evaluation. An optimizer, an LLM paired with a coding harness, receives a target agent's seed harness, graded evaluation feedback, and a fixed target-evaluation budget. It edits the harness and nominates a final candidate, which is scored by its normalized gain over the seed on a held-out test partition that remains inaccessible throughout search. A trusted execution environment enforces the evaluation boundary, meters target-agent resource use, and preserves candidate versions for audit. We evaluate 5 frontier LLMs as optimizers both under a shared coding harness and under their native harnesses across 4 downstream tasks, over 111 scored runs. Experiment results show that optimizer models separate more than the coding harnesses they act through, native harnesses are not consistently superior, and gains vary substantially across tasks and seed regimes. These results establish harness optimization as a measurable and discriminative capability with large space for improvement.


### QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac Arrest Mortality Prediction
**Authors**: Mutasim Fuad Sarker, Adiba Rahman Namira, Wafa Binte Alam, Md Adnan Arefeen, Mahzabeen Emu, Sumaiya Tabassum Nimi

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06294v1](https://arxiv.org/pdf/2608.06294v1)

**Abstract**: Cardiac arrest remains one of the most lethal conditions encountered in intensive care units. Despite the growing availability of electronic health record data, existing mortality prediction studies in this population largely depend on static summaries derived from early admission. Such approaches ignore the temporal progression of physiological deterioration and recovery that unfolds throughout a patient's ICU stay. To address this limitation, we introduce QuanTiMedAI, a quantum-agentic framework developed for cardiac arrest mortality prediction using agentic AI guided quantum enhancement time series model. The proposed system combines an agentic large language model (LLM) for clinically informed feature discovery with a compact quantum recurrent network for temporality aware mortality prediction. Our findings demonstrate that agentic LLM-guided feature selection consistently outperforms conventional feature selection approaches, and the proposed quantum architecture achieves competitive predictive performance through nonlinear feature enhancement while keeping the number of parameters very low. Through extensive experimentation on a MIMIC-IV cohort of cardiac arrest patients, QuanTiMedAI's quantum-enhanced architecture attains an AUROC of 0.852 using only 605 parameters, an improvement of approximately 2.9\% over a current state-of-the-art baseline for this task. A structured ablation study systematically validates the contribution of each architectural design choice. These results show that quantum-enhanced sequential modeling can exceed classical recurrent networks while using substantially fewer parameters.


### From Passive Mirrors to Active Agents: Holonic Digital Twins for Physical AI over Networks
**Authors**: Christo Kurisummoottil Thomas, Omar Hashash, Walid Saad

**Published Date**: 2026-08-06

**Updated Date**: 2026-08-06

**PDF Url**: [2608.06227v1](https://arxiv.org/pdf/2608.06227v1)

**Abstract**: Despite advances in artificial intelligence (AI) across multiple sectors, today's AI tools, including deep learning and generative AI, still fail when embedded into physical systems, such as robots and vehicles operating under real-world physical laws. This stems from their inability to maintain reliable world models for long-horizon planning under uncertainty and generalize to unseen scenarios. In this context, wireless networks, through pervasive sensing and communication, can orchestrate physical intelligence. However, current architectures optimize throughput, latency, and reliability and cannot support real-time physical AI coordination, requiring agents to maintain shared spatiotemporal context. To address these challenges, a network of holonic digital twins (HDT-Nets) framework is proposed to deliver real-time physical AI inference through holonic agents that actively reason about their environment rather than passively mirror physical assets. Each HDT is realized as a hierarchical structure spanning the physical agent and network edge, reasoning autonomously at the local level while cooperating with neighboring HDTs to form collectively intelligent units. In HDT-Net, causal Markov blankets spanning sensing, communication, and control determine which agents must coordinate and enable counterfactual reasoning over multi-domain interventions. Active inference within these boundaries unifies perception, action, and learning by minimizing expected free energy while deciding which beliefs to transmit based on their cognitive value to the receiver. Category theory ensures that transmitted beliefs preserve semantic structure across heterogeneous agents with incompatible representations. Finally, integrated information theory quantifies when collective intelligence exceeds independent operation and how network intelligence evolves through coordinated learning and information exchange.


