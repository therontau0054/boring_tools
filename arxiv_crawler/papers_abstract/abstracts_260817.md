# Abstracts of Papers

## World Model
### CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Image Editing
**Authors**: Qinye Zhou, Jun Zheng, Yongchao Du, Yuan Wang, Zhengrui Chen, Zuan Gao, Taihang Hu, Chao Lin, Yefeng Shen, Xingjian Wang, Zhao Wang, Zhengtao Wu, Xiaoli Xu, Zhengze Xu, Hao Yan, Denghui Yang, Yuhang Yu, Huayu Zhang, Mingzhou Zhang, Mengting Chen

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14546v1](https://arxiv.org/pdf/2608.14546v1)

**Abstract**: With the rapid advancement of image editing models and their widespread application across various domains, there is an increasingly urgent need to deploy these model capabilities directly into real-world scenarios. However, existing benchmarks remain confined to simple single-image tasks, suffering from limited coverage dimensions and an inability to effectively differentiate performance among diverse models. Consequently, they fail to reliably evaluate model performance in complex multi-image editing, highly demanding reasoning instructions, and practical deployment settings. To address these limitations, we propose CPI-Bench, a Comprehensive, Practical andIntelligent benchmark for real-world image editing. CPI-Bench comprises three core subsets: CPI-General-Bench, which comprehensively covers diverse editing tasks and pioneers the inclusion of multi-image editing evaluation; CPI-Practical-Bench, which focuses on high-frequency real-user application scenarios; and CPI-Intelligent-Bench, which is dedicated to evaluating capabilities in highly demanding reasoning-based editing. Evaluation results of mainstream image editing models based on CPI-Bench demonstrate that CPI-Bench enhances performance differentiation among models. It provides a comprehensive and reliable quantification of gaps in general editing capabilities, practical deployment efficacy, and advanced reasoning-based editing, offering invaluable guidance for the future optimization of image editing models. Crucially, our ranking analysis reveals that CPI-Bench achieves the highest alignment with the Arena Image Edit Leaderboard, indicating it faithfully captures the preferences and perceptual judgments of human evaluators, serving as a robust proxy for real-world user experience.


### MagnifiQ: Patch-aware Text Guided Progressive Upscaling for High-Resolution Image Restoration
**Authors**: Mahesh Reddy, Yashesh Savani, Antoine Mercier, Hong Cai, Fatih Porikli, Guillaume Berger

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14543v1](https://arxiv.org/pdf/2608.14543v1)

**Abstract**: High-resolution image restoration from degraded inputs is challenging because it must preserve global structural consistency while recovering fine-grained local details, especially at 4K resolution where direct diffusion-based restoration is computationally expensive and prone to repeated or inconsistent textures. In this work, we introduce MagnifiQ, an image restoration framework that progressively upscales and restores images across resolutions, e.g., from 1024x1024 to 4096x4096. Our approach leverages a pre-trained text-to-image diffusion model such as SDXL and adapts it for more scalable high-resolution inference by replacing its original self-attention layers with convolutional operations whose computational cost grows linearly with image resolution. We further propose a progressive upscaling strategy that iteratively restores images over multiple resolution stages, refining each intermediate output rather than directly hallucinating the final 4K image, thereby improving global coherence and reducing high-resolution artifacts. To enhance local details while controlling content drift, MagnifiQ uses patch-specific text prompts that provide spatially localized semantic guidance during restoration. Extensive experiments on synthetic and real-world degraded images show that MagnifiQ outperforms prior diffusion-based restoration methods in perceptual quality and human preference, producing sharper textures and more coherent 4K results while offering practical speed--quality trade-offs through its scalable backbone and progressive design.


### Decoding the Past: An Uncertainty-Aware Deep Learning Framework for Sex Attribution in Prehistoric Hand Stencils
**Authors**: Karel Becerra, Boris Mederos, Dean Snow, Ramón A. Mollineda

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14539v1](https://arxiv.org/pdf/2608.14539v1)

**Abstract**: Determining the biological sex of the individuals who created Upper Paleolithic hand stencils remains a challenging problem due to the absence of ground truth, population differences between contemporary and prehistoric groups, and the uncertainty introduced by image degradation. Traditional morphometric methods suffer from high structural overlap across sexes, poor cross-population generalizability, and subjective feature engineering. This study presents an uncertainty-aware deep learning framework for sex attribution in prehistoric hand stencils that explicitly models, propagates, and aggregates uncertainty throughout the analytical pipeline. The methodology combines dual image processing, dual contour extraction, structured silhouette augmentation, model architectural diversity, and ensemble-based decision aggregation. The pipeline generates twelve plausible silhouette realizations per stencil to capture boundary uncertainties, which are processed by two ensembles of ten deep neural networks each (EfficientNet-B3 and MobileViT-S) trained on 14,036 contemporary hand samples. Furthermore, a triangulated validation scheme integrates ensemble predictions with unsupervised 2D latent-space manifold mapping (UMAP + k-NN) and explainable AI spatial attributions (LayerCAM) to ensure anatomical consistency. On contemporary data, ensemble models achieve strong classification performance, with accuracies exceeding 88% in older age groups. When applied to prehistoric stencils, the framework produces both sex predictions and confidence measures of internal agreement, enabling the distinction between morphologically stable and ambiguous cases. Convergence across ensemble predictions, latent-space structure, and interpretability analyses shows that uncertainty can become a measurable component of archaeological inference, enabling robust and reproducible decoding of ancient rock art.


### Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking
**Authors**: Ruizhe Wang, Meng Xu, N. Asokan

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14533v1](https://arxiv.org/pdf/2608.14533v1)

**Abstract**: Vulnerability detection via static analysis traditionally relies on security experts encoding insecure coding patterns into algorithmic rules. However, this approach often focuses on syntactic patterns and overlooks deeper semantic information in the code, such as the meanings of variable and function names. As software systems grow more complex, modeling vulnerabilities using only syntactic rules becomes increasingly challenging.
  In this paper, we propose a semantics-aware approach to detecting software vulnerabilities. We present SETYPE, a semantics-aware type system that can be derived directly from source code based solely on the meanings of symbols and expressions in natural language. In the SETYPE type system, both type inference and checking are performed by Large Language Models (LLMs), and a failed type check indicates a potential vulnerability.
  We prototype PYSETYPE to demonstrate the feasibility of SETYPE for detecting vulnerabilities in Python web applications. Our evaluation on real-world applications achieves 87% detection precision and 88% detection accuracy. Using PYSETYPE, we identified 15 potential zero-day vulnerabilities, nine of which were confirmed by developers.


### Marionette: Predicting World States, Rendering Geometry, Painting Appearance
**Authors**: Zian Meng, Zhen Li, Chuanhao Li, Qiang Li, Kaipeng Zhang

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14530v1](https://arxiv.org/pdf/2608.14530v1)

**Abstract**: Interactive game world models typically autoregress visual observations directly in pixel or latent space, forcing structured properties such as pose, geometry, and occlusion to be implicitly maintained by the same generative sequence. Over long horizons, errors in these latent world properties accumulate, making consistency and controllability fragile. We explicitly model the evolving world state, delegate exact geometric computation to a fixed, zero-parameter renderer, and leave the neural model to synthesize appearance. We instantiate this idea as Marionette, a world model for interactive games with articulated characters. First, a two-stage autoregressive dynamics model predicts an explicit and interpretable 276-dimensional 3D world state comprising multi-entity articulated skeletons, metric root trajectories, and rotations. Second, a zero-parameter graphics bridge converts the predicted state into pose-control videos, computing world-space geometry and occlusion in closed form. Third, a control-conditioned video-diffusion observation model synthesizes photorealistic RGB observations from the resulting structured controls. Our experiments establish two properties of Marionette. First, the predicted world state is directly controllable. Forcing a mismatched action stream changes root-aligned joint error by 31% across 48 held-out segments. Second, long-horizon behaviour is determined in the state, and can be repaired there. Left free, the two generated characters drift to 21.2 m apart (recorded sessions stay near 5 m) and a third of frames show ground penetration. Two rules imposed on the explicit state, a terrain collider and a separation cap, cut penetration by 66% and keep the pair engaged, with no change to the observation model. Routing appearance through the predicted state costs no fidelity we can detect, at an FVD of 831 against 799 for recorded pose.


### Handover of In-Context Learning State Across Session Boundaries
**Authors**: Masahiro Kato, Taka Kato

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14528v1](https://arxiv.org/pdf/2608.14528v1)

**Abstract**: This study investigates the methodological and theoretical properties of session handover in applications that use large language models. A task may continue in a new session when the context reaches the model's input limit, when the application restarts, or when another agent is asked to finish the task. The application must then decide which information from the earlier session to pass on. We formulate handover as the transfer of a task-relative in-context learning (ICL) state and distinguish exact recovery of earlier material from preservation of the target distribution. Under an exogeneity condition, predictive equivalence characterizes the coarsest deterministic sufficient handover and gives a fixed-length bit requirement. The analysis isolates the effects of the memory constraint, the writer, and the continuation procedure, and quantifies the cost of writing before the realized downstream query is known. We propose a three-part record that stores decisions and constraints exactly, uses task-justified statistics for repeated evidence, and retains original observations whose effect is not preserved by those statistics. Gaussian linear regression gives an exact finite-dimensional handover and finite-bit perturbation bounds, while nonparametric regression gives upper and lower bounds that relate memory to squared prediction error. These results provide a theory and method for deciding what a handover must retain and how its memory requirement depends on the continuation task.


## Generation
### Participatory Moral AI Is Not Neutral: The Invisible Hand of Developers
**Authors**: Taenyun Kim, Edyta Bogucka, Daniele Quercia

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14522v1](https://arxiv.org/pdf/2608.14522v1)

**Abstract**: As AI systems make more morally loaded decisions across society, one response has been moral preference elicitation. In this approach, researchers poll participants on hypothetical dilemmas and use the aggregated votes to train a policy that an AI model then applies at scale. Before any vote is cast, developers make three key choices in the moral AI elicitation pipeline: feature scoping, voter sampling, and question framing. In other words, they decide which features go to a vote, which voters to include, and how to present the question. These choices are often opaque, undocumented, and treated as technical details rather than normative ones. We examine each of these choices within a common empirical study and show that each can shape the preferences produced by moral AI elicitation. Across two phases (N = 809) in three deployment contexts (i.e., AI kidney allocation, AI agents simulating absent workers, and generative AI depictions of the deceased), we examine the three main stages of the moral AI elicitation pipeline. First, morally relevant features shift across contexts. This suggests that feature schemas should not be assumed to transfer across deployment domains. Second, preferences differ by political ideology for roughly one-third of features, with some differences reversing direction. The ideological composition of the voter pool can therefore affect the resulting aggregated preference profile. Third, the wording of the elicitation question can narrow or widen ideological gaps by up to a full scale point. The framing conditions also change how moral foundations are associated with participants' judgments. Taken together, these findings suggest that voting-based alignment cannot deliver fair or transparent AI by aggregation alone; at minimum, each stage of the moral AI elicitation pipeline should be audited and disclosed.


### Learning-to-Transition for Large-scale and High-Order MIMO Detection
**Authors**: Yubo Zhang, Yiyao Liu, Xiaodong Wang

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14511v1](https://arxiv.org/pdf/2608.14511v1)

**Abstract**: High-order multiple-input multiple-output (MIMO) detection requires efficient search over a large discrete symbol space while producing reliable soft information for channel decoding. This paper develops a learning-to-transition (L2T) framework that formulates MIMO detection as a stochastic sequence of complete-vector transitions. At each transition, a channel-coupled Transformer updates both the instance embedding and the sampling policy, while a blockwise autoregressive factorization captures inter-stream dependence with moderate sequential complexity. For hard-output detection, a transition network is applied recursively and trained through a residual-to-BER curriculum, which first learns the MIMO search geometry from the exact residual metric and then aligns the policy with transmitted-bit accuracy. For soft-output reception, the well-trained hard policy is cloned at the parameter level into every layer of an untied soft-input soft-output iterative detection and decoding (IDD) receiver. This tied-to-untied transfer preserves the learned zero-prior search dynamics while enabling layer- and round-specific specialization under decoder feedback. Within each IDD round, decoder priors tilt candidate generation according to Bayes' rule, and likelihood-weighted terminal hypotheses produce posterior and extrinsic log-likelihood ratios for LDPC decoding. A multi-stage training strategy further stabilizes the hard-to-soft transfer by progressively exposing the receiver to synthetic and in-loop decoder-generated priors.


### Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training
**Authors**: Hanfeng Lu, Tianyu Feng, Suyi Li, Yuheng Zhao, Wei Gao, Shaopan Xiong, Ju Huang, Siran Yang, Jiamang Wang, Lin Qu, Wei Wang

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14498v1](https://arxiv.org/pdf/2608.14498v1)

**Abstract**: Vision-language models (VLMs) enable embodied agents to reason and act from visual observations and language instructions. Reinforcement learning (RL) post-training enhances these capabilities using task feedback, but current on-policy RL runtimes execute rollout, reference scoring, and actor training in strict serial phases. While effective for text-only RL, this phase-granular execution is wasteful for VLMs, where processing dense video inputs and prompt prefixes occupies a large fraction of each phase. Because prefix processing is independent of the generated response, it can be run alongside rollout decoding, which leaves GPU compute capacity underutilized, without breaking synchronous on-policy semantics.
  We present Rollplex, a runtime that decomposes the reference and training phase and moves the prefix computation into the rollout decode window. Realizing this schedule requires more than concurrent kernel launches: naive colocation of Qwen2.5-VL-32\,B requires roughly 165\,GiB per GPU, while rollout and training prefer different tensor-parallel (TP) degrees and weight layouts. Rollplex addresses these constraints with two mechanisms. Phase-aware memory management controls HBM residency according to producer--consumer lifetimes. Parallelism-aware weight sharing uses the same physical storage for layout-compatible tensors across distinct TP degrees and reconstructs only incompatible tensors, avoiding a complete second actor copy. On 32 H800 GPUs, Rollplex achieves $1.23\times$--$1.30\times$ speedup over serial colocation and $1.57\times$--$2.24\times$ over disaggregation under the same GPU budget, while preserving the synchronous RL update.


### Generating Benchmark Health Data Using a Tabular Diffusion Transformer
**Authors**: Hao Yan, Lisa Pilgram, Dan Liu, Linglong Kong, Fida Dankar, Khaled El Emam

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14496v1](https://arxiv.org/pdf/2608.14496v1)

**Abstract**: Cross-Tabular Data Generation (CTDG) seeks to learn a generative model from multiple heterogeneous tables and produce new synthetic tabular datasets. However, existing synthetic tabular data generation methods are largely restricted to single-input-table scenarios and struggle to effectively handle multiple heterogeneous tables with diverse feature sets. To address this limitation, we propose a two-stage framework for cross-tabular data generation. In the first stage, each heterogeneous raw table is transformed into a standardized statistical table with the same set of columns across all tables. Each statistical table captures the marginal distributions of the original columns and the pairwise correlations among them. In the second stage, a diffusion transformer model is trained to capture structural patterns across these homogeneous statistical tables and to generate synthetic statistical tables. Synthetic raw tables are subsequently reconstructed from the generated statistical tables via multivariate Gaussian sampling followed by an inverse probability integral transform. This two-stage CTDG framework enables the learning of a unified generative model from multiple heterogeneous tables and supports the generation of an unlimited number of realistic synthetic heterogeneous tables. Experimental results demonstrate high fidelity in the learned statistical representations and a favorable fidelity-diversity trade-off in the generated synthetic data, validating the effectiveness of the proposed approach.


### LP-NAS: Linear Programming-based Neural Architecture Search
**Authors**: Abhishek Shukla, Ankur Sinha, Faiz Hamid

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14472v1](https://arxiv.org/pdf/2608.14472v1)

**Abstract**: Neural Architecture Search (NAS) aims to automate neural network architecture design, reducing reliance on human expertise. Among the various NAS methods, differentiable NAS has gained prominence due to its efficiency and accuracy compared to conventional NAS approaches. Since differentiable NAS relaxes the architecture search space into a continuous domain, it is possible to apply principles from continuous optimization to NAS. In this paper, we propose Linear Programming-based NAS (LP-NAS), a mathematical programming-based framework for differentiable NAS that is applicable to a wide range of continuous search spaces. LP-NAS formulates a linear program (LP) using the validation-loss gradient and the training-loss Hessian to compute an architecture update direction that improves generalization while preserving the optimality of the model parameters. By following this LP-derived descent direction, LP-NAS efficiently navigates the architecture search space, leading to faster and more effective architecture optimization. We introduce two computationally efficient variants of LP-NAS, namely S-LP-NAS and R-LP-NAS. Applying LP-NAS to the Differentiable Architecture Search (DARTS) search space results in two algorithmic variants, S-LP-DARTS and R-LP-DARTS. Both variants achieve faster convergence and significantly higher validation performance during the early search iterations than the standard DARTS algorithm. Extensive experiments on CIFAR-10 and CIFAR-100 show that LP-DARTS outperforms standard DARTS in both the architecture search and evaluation phases. Additionally, we compare our approach with several DARTS variants (P-DARTS, PC-DARTS, and STO-DARTS) on the CIFAR-10 dataset and demonstrate its effectiveness. Furthermore, we validate the transferability of the discovered architectures through experiments on the ImageNet dataset.


### Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports
**Authors**: Beatrice Alessandra Motetti, Emilien Guandalino, Daniele Jahier Pagliari, Alessio Burrello, Lorenz K. Müller, Konstantin Berestizshevsky, Lukas Cavigelli

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14446v1](https://arxiv.org/pdf/2608.14446v1)

**Abstract**: In the current artificial intelligence-driven innovation era, the pace of knowledge growth is accelerating, and is hard to keep up with. While generative models are increasingly used to synthesize content, they often lack in information grounding. To address these peculiarities of our time, we propose Wyvern, a multi-agent framework for the automated generation of grounded, multimodal technical reports. Wyvern allows for the generation of multimodal outputs, integrating images, tables, and text with supporting references in a unified report. Additionally, a particular focus is placed on the grounding of the content, with the implementation of a claims auto-revision stage. We conduct a human evaluation study to assess the quality of our proposed framework. The results show that the figures' informativeness is perceived as superior to that of a recent baseline in 87% of cases. Furthermore, Wyvern's reports are rated as more useful than those produced by three alternative methods in 63% to 100% of instances. We also carry out automatic evaluations showing that Wyvern gains up to 2.3$\times$ in citation recall and 1.6$\times$ in citation precision with respect to the baselines.


## VLA
### Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation
**Authors**: Yuxuan Chen, Wanruo Zhang, Xiao Li

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14379v1](https://arxiv.org/pdf/2608.14379v1)

**Abstract**: Vision-Language-Action (VLA) models have recently achieved promising performance in robotic manipulation. However, existing benchmarks mainly evaluate generalization on static manipulation tasks and largely overlook dynamic interaction scenarios. To address this gap, we present ReflexBench, a benchmark for reaction-critical manipulation. ReflexBench contains six dynamic tasks and introduces an evaluation framework that decouples simulator stepping from robot control while supporting configurable latency under synchronous and asynchronous inference. Building upon ReflexBench, we propose ReflexVLA, an efficient VLA model designed for reaction-critical manipulation without large-scale robot-data pretraining. ReflexVLA enhances temporal reasoning through latent future prediction and multi-frame temporal fusion within the vision backbone, while reducing deployment latency through batched visual encoding and CUDA Graph replay. Experiments show that ReflexVLA consistently improves dynamic manipulation performance while maintaining competitive accuracy on standard static manipulation benchmarks, and real-world experiments further demonstrate its effectiveness under practical deployment conditions. Project website: https://reflexvla.github.io


### Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use
**Authors**: Yi Ding, Yanzhao Yu, Xili Dai, Xianbiao Qi, Peiwen Sun, Xueqian Wang, Xiangyu Yue, Jianan Wang

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14047v1](https://arxiv.org/pdf/2608.14047v1)

**Abstract**: This paper integrates end-to-end Visual-Language-Action (VLA) models with agentic tool-use to propose Agentic Robot with Tool-use (ART). ART is a tool-injection framework that tunes any VLA model to leverage off-the-shelf tool modules for low-level vision, high-level affordance, and embodiment enhancement. Compared to vanilla VLA models with a whole continuous action solution space, ART reduces the complexity of the action solution space through tool-use, which not only improves generalizability across different tasks but also reduces data dependency. To demonstrate the advantages (high generalizability and low data dependency) of this framework, we first built a dataset of 30K tool-use trajectories and action demonstrations, which is much smaller than those used by baseline methods. We then designed a training regimen for long-trajectory tool-use reasoning in challenging environments. Experiments show that ART achieves a 20% higher success rate than mainstream baselines on simulation and real-world tasks, such as pick-and-place in the dark at novel viewpoints. Empirical results highlight the benefits of an agent-based approach: modular tool utilization enables more efficient training, lightweight deployment, and scalable integration of new tools. This design fosters robustness, adaptability, and extensibility, paving the way for the practical deployment of VLA systems in complex real-world scenarios.


## Agent
### Twin: Playing an Unknown Game with a Test-Time Digital Twin
**Authors**: Alexy Skoutnev, Kirill Acharya, Gaston Longhitano, Madeleine Udell, Kevin Ellis, Iddo Drori

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14490v1](https://arxiv.org/pdf/2608.14490v1)

**Abstract**: We present a Test-time World-model Inference (Twin) system, in which a frontier coding agent writes an executable world model for completing continual learning tasks, such as ARC-AGI-3 games. Traditional approaches hand-engineer such models, one custom design per task. Each game hides its rules and goal, and our system constructs them from simulation and interaction alone. Its inductive prior over grid games is strong enough to recover the true transitions of the game and the goal on nearly all levels. Replay validation happens in a twin world model. The harness enforces that an action is not made until the program reproduces every previous observed game transition. Each mismatch between a world model prediction and the actual action result becomes a counterexample that is used to repair the world model. Twin clears 179 out of 183 levels (97.8%), and does so more efficiently than humans in 158 out of 179 levels (88.3%). The system infers the goal before any reward on 156 of the levels it clears (87.2%), and in the remaining levels automatically discovers the goal by search. The benchmark scores completion and action efficiency, between 0 and 100, against humans playing each game for the first time. Played directly, the base model scores only 7.8%; an off-the-shelf harness increases it to 61.1%, whereas our twin world model increases the same base model to 93.3%, clearing 23 out of 25 games. Building a usable world model is simpler than anticipated, whereas the harder problem is inferring the right goal.


### Expected Free Energy-based Informative Path Planning for Robotic Mars Exploration
**Authors**: Ajith Anil Meera, Pablo Lanillos, Wouter Kouw

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14466v1](https://arxiv.org/pdf/2608.14466v1)

**Abstract**: An autonomous robot efficiently exploring an unknown environment, such as looking for water sources on Mars, faces two simultaneous demands: building an accurate information map while quickly finding the regions of greatest value, and paying for every meter of travel and the cost of every measurement it takes. Classical information-seeking and reward-seeking criteria address only one of these objectives at a time. Here, we propose Expected Free Energy (EFE), the principled action-selection objective from active inference, as a unifying criterion for budgeted robotic informative path planning. Maintaining a Gaussian-process belief over the information field, our agent plans continuous trajectories that minimize expected free energy under hard path-length constraints. The results from multiple realizations show that EFE-based planning yields accurate posterior maps and locates the highest-value regions simultaneously, outperforming information-theoretic baselines under the same settings. In robotic exploration, these unified, easy-to-tune principled information-gathering strategies facilitate autonomous deployment while enforcing efficiency and resource constraints.


### SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning
**Authors**: Panjing He, Mingyue Cheng, Yucong Luo, Li Li, Xiaohan Zhang

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14452v1](https://arxiv.org/pdf/2608.14452v1)

**Abstract**: Spreadsheets are widely used to organize, analyze, and manipulate semi-structured data, yet automated spreadsheet reasoning remains challenging for large language models (LLMs). Real-world workbooks often contain implicit cross-table associations, fine-grained column dependencies, and complex spatial layouts. Existing methods typically flatten these multidimensional structures into sequential strings, losing important intra-sheet boundaries and inter-sheet semantics. Consequently, LLMs cannot exploit the global spatial context that human experts naturally use when inspecting spreadsheets. We propose SheetCompass, a graph-guided and memory-driven agentic framework for spreadsheet reasoning and automation. SheetCompass explicitly models structural relationships within and across worksheets while maintaining task-relevant information in memory, enabling agents to reason more effectively over complex workbooks.


### PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments
**Authors**: Yuhao Zhan, Bingxiang He, Zecong Tang, Chaojun Xiao

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14441v1](https://arxiv.org/pdf/2608.14441v1)

**Abstract**: Self-evolving agents improve future behavior from interaction experience, yet existing evaluations typically optimize under fixed execution conditions and do not test recovery after those conditions change. To address this gap, we introduce PACE-Bench (Physics Adaptation via Code Evolution), a simulator-grounded benchmark of 144 source-to-target adaptation pairs across six physics domains. Each pair links a source environment to a mutated target environment with the same goal and interface. A code-driven design that succeeds in the source fails in the target, where agents must iteratively adapt it into a working target design using diagnostic sandbox feedback within a limited attempt budget. We compare ten self-evolving methods from four paradigms. The benchmark remains far from saturated: Reflexion + Qwen3-14B succeeds on only 35.9\% of full-benchmark pairs, while GPT-5.5 solves 66.7\% of the Statics subset under the full budget. Together, these results show that simulator-grounded reflection is more reliable than unverified self-revision, while memory anchors agents to early designs and broad tree search explores without converging. Even revealing exact physical changes does not raise the performance ceiling, pointing to mechanism redesign rather than parameter inference as the central bottleneck. Data and code are available at https://github.com/thunlp/PACE-Bench.


### The Past and Future of AI Scientists
**Authors**: Ross D. King

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14407v1](https://arxiv.org/pdf/2608.14407v1)

**Abstract**: We present a survey of the past and future of AI Scientists: machines capable of automating science. AI Scientists can originate hypotheses, deduce their consequences, design and execute experiments, interpret their results, and revise their beliefs. Such systems are integrated scientific agents, connected to the literature, formal knowledge, mathematical models, simulations, data-analysis systems and physical laboratories.
  Adam was the first machine to make novel scientific discoveries through cycles of hypothesis formation and physical experimentation. Eve established the architecture of the modern self-driving laboratory. Foundation models, autonomous agents and laboratory robotics now make it possible to build systems far more general than either Adam or Eve.
  The central problem is no longer whether individual components of science can be automated. They can. The problem is integration. AI Scientists must combine neural learning with logic, probability, mathematics, causal reasoning, simulation, experimental design, robotics and formal scientific records.
  AI Scientists have the potential to transform science: to make science faster, cheaper, more systematic and more reproducible. AI Scientists could investigate systems too complicated for unaided human science, and enable thousands of AI scientists to work together on single problems.
  The Nobel Turing Challenge sets the goal of developing by 2050 AI systems capable of automating Nobel-quality discoveries. Progress is ahead of schedule. When we succeed it will create a new form of science and transform the world.


### AgentRewind: Recoverable Execution for Long-Horizon LLM Agents
**Authors**: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang

**Published Date**: 2026-08-14

**Updated Date**: 2026-08-14

**PDF Url**: [2608.14380v1](https://arxiv.org/pdf/2608.14380v1)

**Abstract**: Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, a runtime recovery framework that records aligned checkpoints of the agent context and controlled environment, allowing agents to return to an earlier state and resume execution with information from previous attempts. We also construct MettleBench, a benchmark for evaluating task completion and partial progress on long-horizon engineering assignments containing a series of related requirements. Experiments across tasks, multiple models, execution strategies, and agent harnesses show that AgentRewind improves task success rate and average checklist progress over the compared baselines.


