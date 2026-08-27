# Abstracts of Papers

## World Model
### VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning
**Authors**: Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji, Tongxi Zhou, Chenyang Gu, Jing Zuo, Hongcan Xiao, Yimeng Geng, Wanqi Yin, Wei Chen, Oscar Qian, Zhengan Yan, Ziqi Huang, Haiwen Diao, Liang Pan, Bo Li, Xiangyu Fan, Dezhi Luo, Fengyuan Yu, Zehong Zhao, Qingying Gao, Tinghui Zhu, Yilan Zhang, Jingqi Tong, Pinyuan Feng, Zhengze Jiang, Letian Wang, Ziyu Guo, Renrui Zhang, Jieneng Chen, Sonia Joseph, Constantin Venhoff, Saman Motamed, Mengyue Yang, Chandra Sripada, Alan Yuille, Philip Torr, Lvmin Zhang, Vikash Kumar, Daniel Khashabi, Nikolaus Kriegeskorte, Raphaël Millière, Vincent C. Müller, Anyi Rao, Quan Wang, Ziwei Liu, Dahua Lin, Lei Yang, Hokin Deng, Zhongang Cai

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26105v1](https://arxiv.org/pdf/2608.26105v1)

**Abstract**: Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-class substrates for problem solving beyond language. Yet progress remains bottlenecked by the lack of scalable training tasks, reliable feedback, and controlled comparisons across generative substrates. In this work, we introduce VBVR-Pro, a closed-loop testbed that makes native visual reasoning through generation trainable, verifiable, optimizable, and experimentally controllable. 1) Task scaling. VBVR-Pro turns visual reasoning into a controlled task space of 300 procedurally generated tasks. Models trained on VBVR-Pro show strong transfer beyond the proposed suite across seven external visual reasoning benchmarks such as RISE-Video, MME-CoF-Pro, and BabyVision. 2) Verifiable rewards. VBVR-Pro provides verifiable reward scorers for task-grounded evaluation. Through a systematic study of leading MLLMs as judges, we identify recurring failure modes of the prevalent VLM-as-a-judge paradigm. In contrast, the proposed scorers are grounded in deterministic, task-specific rules, achieve fine-grained alignment with human judgments. Importantly, they serve as reliable reward signals for large-scale multi-task reinforcement learning and demonstrate stronger post-RL performance across visual reasoning tasks. 3) Mechanism study. VBVR-Pro enables controlled modality studies across more than 30 image, video, and interleaved generators. Our analysis shows that video generation remains strongest for tasks requiring persistent spatiotemporal state tracking, while interleaved generation provides a compute-efficient alternative. Critically, ablations and probing suggest the presence of vision-native trajectories that are crucial to visual reasoning. We release all data, models, scorers, and code.


### Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization
**Authors**: Jiaming Zhou, Qihang Zhang, Gangwei Xu, Cunxin Fan, Yujie Zhao, Ruilin Wang, Yiming Luo, Shuai Yang, Xing Zhu, Yujun Shen, Junwei Liang, Yinghao Xu

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26103v1](https://arxiv.org/pdf/2608.26103v1)

**Abstract**: Zero-shot cross-task generalization, where a policy must execute manipulation tasks never seen during training, remains a central challenge in robot learning. In large language models, a novel task can be performed simply by specifying it in the context, without any parameter update. This form of in-context learning (ICL) turns generalization into a problem of task specification. To achieve cross-task generalization, we bring this paradigm to robotic manipulation, and argue that the natural task specification for manipulation is a human video: unlike language, it provides rich visual cues about the intended task evolution. We present Zero-WAM, a causal video-action model that executes unseen tasks by following in-context human video guidance. To address the scarcity of task-rich paired human-robot data, we propose an automatic pipeline that converts task-sampled robot trajectories into semantically matched human videos, yielding HumanGen, a dataset of 74.2K human-robot ICL pairs across 8.6K tasks. For model training, we further introduce an in-context future chunk prediction (IFP) objective that suppresses shortcuts learned from seen tasks and forces the policy to draw task information from the video prompt. On seven unseen tasks in RoboTwin 2.0 simulation, Zero-WAM achieves a 47.0% average success rate, an absolute improvement of 29.5 percentage points over the strongest video-action baseline. In real-world evaluations, it follows human video guidance to generalize to unseen task configurations involving multi-object scenes, long-horizon manipulation, and fine-grained insertion.


### MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching
**Authors**: Hao Yin, Paritosh Parmar, Lijun Gu, Lin Xu, Tianxiao Guo, Xiujin Liu, Tianyou Zheng, Yang Zhang, Weiwei Fu

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26094v1](https://arxiv.org/pdf/2608.26094v1)

**Abstract**: Existing action quality assessment (AQA) datasets and methods rely primarily on visual inputs such as RGB and pose, overlooking physiological dynamics such as muscle mechanics and often modeling actions as monolithic patterns. These limitations hinder fine-grained, biomechanically grounded feedback. We introduce MyoMechanix, a multimodal ecosystem for weight-loaded actions that aligns motion with muscle activity. Expert-annotated, it contains 7,500+ samples of 20 actions from 38 subjects, with synchronized multiview RGB video, 3D pose, sEMG, and additional physiological signals, forming the largest multimodal AQA benchmark to date. We further construct the Fitness Knowledge Graph (FKG), which organizes expert annotations into structured relationships among actions, phases, key steps, errors, and corrective feedback, enabling compositional scoring and interpretable assessment. Building on these representations, we develop CUBIST (Compositional Ontological Reasoning Engine), which performs decomposition-analysis-recomposition for fine-grained error attribution and feedback generation. We also establish MyoMechanix-AQA, MyoMechanix-VideoQA, and a novel MyoMechanix-Video2EMG task. Experiments show that multimodal sensing and structured representations improve performance, interpretability, and error attribution, with CUBIST achieving state-of-the-art results; VideoQA enhances language-grounded action understanding; and Video2EMG suggests video-based alternatives to costly EMG sensing. MyoMechanix advances skilled activity understanding toward biomechanically grounded, multimodal, and compositional reasoning for Physical AI applications in fitness, rehabilitation, healthcare, and machine learning. Project page: https://haoyin116.github.io/MyoMechanix/


### Finding and using interpretable latents in a neutrino foundation model with sparse autoencoders
**Authors**: Raphaël Bonnet-Guerrini, Johann Ioannou-Nikolaides, Inar Timiryasov, Vincenzo Piuri

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26090v1](https://arxiv.org/pdf/2608.26090v1)

**Abstract**: We present a first application of sparse-autoencoder-based mechanistic interpretability to particle physics. Studying a neutrino foundation model pretrained on IceCube data and fine-tuned for direction reconstruction, we identify a validated atlas of physical concepts in the model representation, using a strict validation protocol consisting of held-out tests, matched nuisance controls, and replication across independent dictionary trainings. Causal interventions show that the direction head barely draws on this atlas. Motivated by this underused information, we train an uncertainty head on the same event-level representation to predict the model's angular reconstruction error. Unlike the direction head, it depends causally on quality and brightness features from the atlas. At $20\%$ selection efficiency, this interpretable estimator improves the median angular resolution from $20.2^\circ$ to $3.2^\circ$. These results suggest that mechanistic interpretability can reveal learned latent physics encoded within a model's internal representation and help design downstream tasks that exploit it.


### Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent Data Selection and Foundation Model Embeddings
**Authors**: Evelyn Ma, Rama Kumar Pasumarthi, Kishwar Shafin, Mandar Sharma, Mimi Sun, Hamed Sadeghi, Dav M. Ebengo, Mbulayi Onesime, Rouslan Solomakhin, John Wamburu, William Ogallo, Aisha Walcott-Bryant, Sanxing Chen, Arbaaz Muslim, Yael Mayer, Ronald Ho, Roy Lee, Ruth Alcantara, Abdoulaye Diack, Monica Bharel, Lambert Rosique, Jeremy Amez-Droz, Christopher Haire, James Manyika, Yossi Matias, Niv Efron, Gautam Prasad, Shravya Shetty

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26088v1](https://arxiv.org/pdf/2608.26088v1)

**Abstract**: Addressing critical global challenges, from food security and disaster risk to disease outbreaks and socio-economic vulnerability, demands high-fidelity geospatial modeling. However, building predictive planetary models remains bottlenecked by a fragmented data ecosystem, requiring manual data retrieval, multimodal data curation and fusion along with iterative model selection. We present the Planetary Prediction Engine (PPE), an autonomous AI system that executes this end-to-end workflow directly from natural-language queries. PPE synthesizes multimodal datasets on the fly, retrieving spatiotemporally relevant covariates across open-web and Earth observation platforms (Data Commons, Google Earth Engine) and fusing them with geospatial foundation model embeddings (PDFM, AlphaEarth). Simultaneously, it searches over task-tailored model architecture families with automated overfitting guards. Across diverse tasks, geographies, and scientific domains, PPE consistently outperforms state-of-the-art or manually tuned expert baselines. For US spatial regression, PPE improves mean $R^2$ across 21 CDC health indicators (76.8% vs. 60.0%), FEMA national risk indices (64.9% vs. 60.0%), and the Social Vulnerability Index (66.2% vs. 58.6%). For spatial downscaling in data-scarce settings, PPE integrates localized proxies to double baseline accuracy in Nigerian food security indicators ($R^2$ of 66.1% vs. 31.5%). For epidemiological nowcasting of the 2026 DRC Bundibugyo Ebola outbreak, PPE achieves a Recall@10 of 83.3% (identifying 15 of 18 newly invaded health zones across five weekly forecasts), a +10.3 percentage-point improvement over the public state-of-the-art modeling (~73%). By combining autonomous multimodal planetary data discovery with targeted model optimization, PPE lowers the technical barrier to planetary-scale analytics, enabling rapid, customized, expert-level deployment.


### TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development
**Authors**: Jiarui Yan, Weiwei Sun, Sijie Li, Wenhan Li, Yiming Yang

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26086v1](https://arxiv.org/pdf/2608.26086v1)

**Abstract**: Large language models write correct code for isolated problems but remain far weaker at autonomous machine-learning development, where an agent must revise data pipelines, models, and validation over hours of feedback, and on most competitions still finishes below strong human competitors. Outcome-based benchmarks record this gap but not its cause, because they grade the final submission and discard the development process behind it. We introduce TraceML, which pairs human and agent work on the same competitions under one version-level schema: 4,465 human Kaggle trajectories across 134 competitions, seven of which are also worked by two agent scaffolds, giving 430 paired human and 207 agent trajectories. Every code version carries its score, its timestamp, and labels for the action taken, its intent, the edit size, and the score effect. Read this way, the gap becomes concrete. Experts alternate data work, validation, model changes, and ensembling, and return to approaches they had set aside. Each agent scaffold instead collapses into a narrow loop: Codex spends its steps re-weighting ensembles and tuning submissions, MLEvolve mutates its model in place, and neither pivots at the human rate nor reopens abandoned work. A short planning prompt distilled from human practice moves the behaviors it names toward the human profile and lifts scores, but the effort profile stays agent-shaped: instruction closes only the part of the gap that reduces to instructions. We release the corpus, the schema, the labelers, and the extraction pipeline at https://huggingface.co/datasets/jerryyan/TraceML.


## Generation
### $R^3$: Training Robots to Reason in Natural Language via Reinforcement Learning
**Authors**: Lehong Wu, Yuxiao Qu, Zheyuan Hu, Ivan Zhang, Limin Wei, Zackory Erickson, Aviral Kumar

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26053v1](https://arxiv.org/pdf/2608.26053v1)

**Abstract**: Reasoning in language allows foundation models to spend more test-time compute on hard problems, such as those requiring decomposition, constraint tracking, and prediction of future consequences. Whether this mechanism can improve robotic manipulation remains unclear, where long-horizon tasks require tracking partial progress, reasoning about object relations, recovering from mistakes, and steering noisy low-level policies. In this paper, we study whether VLMs can be trained to reason directly in natural language to guide low-level manipulation policies. We introduce $R^3$, a simple post-training recipe that turns off-the-shelf VLMs into robotic reasoners: it first mid-trains a VLM on expert-generated reasoning traces to initialize the desired reasoning style, then improves the reasoner with single-step rubric-based RL from offline action data. Unlike prior robotic reasoning methods that mostly use structured traces as auxiliary supervision, $R^3$ trains free-form language reasoning to produce test-time guidance for action. We instantiate $R^3$ on Language Table and simulated bimanual grocery packing, two controlled testbeds for studying robotic reasoning and long-horizon manipulation. $R^3$ improves exploration and generalization across unseen tasks and significantly outperforms instruction-only imitation learning baselines on both benchmarks. Our analyses suggest that free-form language reasoning can function as a test-time compute mechanism for steering low-level policies. Our project page is available at https://robotic-reasoner.github.io/.


### AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs
**Authors**: Sheng Liang, Yongyue Zhang, Nathanael Brian, Hang Lv, Hao Wang, Chen Zhang, Yong Liu

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26004v1](https://arxiv.org/pdf/2608.26004v1)

**Abstract**: Agentic LLM pipelines face escalating inference costs as context accumulates across retrieval, tool use, and multi-turn interactions. To control latency, deployments routinely compress inputs, but this degrades task accuracy. Speculative decoding (SD) accelerates generation losslessly, yet it assumes the drafter and verifier share an identical context, preventing SD from resolving the accuracy-overhead trade-off. We propose AsymSpec, an asymmetric speculative decoding framework that breaks this symmetry: a lightweight drafter reads the full input while the large verifier operates on the compressed view. The drafter steers the verifier via a contrastive $δ$-fusion of logits, modulated by a divergence-aware acceptance gate that preserves verification stability and high draft acceptance rates. Evaluated across four agentic capabilities and two end-to-end agent benchmarks, AsymSpec reaches $\approx 90\%$ of full-context accuracy on average, delivering $1.3$--$1.7\times$ throughput speedups at $0.2$--$0.3\times$ the compute cost on isolated text capabilities. These results show that asymmetric context access yields substantial gains precisely when compression discards critical reasoning signals.


### ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs
**Authors**: Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25992v1](https://arxiv.org/pdf/2608.25992v1)

**Abstract**: Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operating costs due to repeated LLM invocations and long-horizon context accumulation. Existing cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows, in which the right LLM at each step depends on evolving task progress, remaining task difficulty, and cost-efficiency requirements. We present ProgRouter, an online progress-guided routing framework that adaptively selects LLM agents across workflow steps to preserve task-solving quality while adhering to time and cost budgets. ProgRouter introduces a multi-view task progress scorer that combines coarse workflow outcome regimes with fine-grained signals on subtask completion, progress trends, and workflow state quality. Then, a dual-path task progress predictor and an adaptive meta-gating mechanism estimate the progress gain for each candidate routed LLM. ProgRouter makes online step-wise routing decisions that balance progress gain, task time budgets, and long-term operating cost efficiency. Experiments on HumanEval Plus, MBPP, MATH-500, and ASQA, spanning agentic code generation, mathematical reasoning, and retrieval-augmented long-form question answering, demonstrate that ProgRouter reduces the operating cost relative to key baselines while maintaining strong task-solving performance.


### Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs
**Authors**: Zongyu Wu, Yilong Wang, Xiaochen Wang, Minhua Lin, Zhichao Xu, Fenglong Ma, Xiang Zhang, Suhang Wang

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25986v1](https://arxiv.org/pdf/2608.25986v1)

**Abstract**: Retrieval-augmented generation (RAG) is widely used to mitigate hallucination issues in large language models (LLMs) and multimodal large language models (MLLMs). In particular, knowledge graph (KG)-based RAG leverages structured knowledge to provide (M)LLMs with high-quality external information. Building on these works, recent studies have explored multimodal knowledge graphs (MMKGs) as knowledge bases for GraphRAG. This enables Graph RAG to integrate knowledge across multiple modalities, thereby further enhancing its performance. However, existing MMKG-based RAG methods generally follow a common pipeline in which different modalities are largely processed independently before being fusion. As a result, textual context is only used to a limited extent during visual information extraction and subsequent multimodal knowledge fusion. This brings a semantic gap between images and text which limits the multimodal GraphRAG performance. To address this issue, we propose a novel framework for constructing a Context-Enhanced MMKG (CEMMKG) to better support multimodal GraphRAG. The proposed CEMMKG enriches each image with complementary textual context at both local and global scopes. Local context goes beyond the surrounding text by incorporating sentences that are semantically related to the image, while global context provides a summary of the entire passage. We further introduce a multi-granularity design for the local context, allowing it to capture semantically relevant information at different levels of detail. Extensive experiments on the selected vision-centric dataset validate that CEMMKG is effective in leveraging contextual information to improve MMKG-based RAG performance. Moreover, its effectiveness across different MMKG-based RAG methods demonstrates its broad applicability.


### SciMIF: Understanding Multimodal Instruction Following in Scientific Domains
**Authors**: Ye Shen, Yuting Zheng, Dun Pei, Zijian Chen, Wenlong Zhang, Qi Jia, Guangtao Zhai

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25973v1](https://arxiv.org/pdf/2608.25973v1)

**Abstract**: Understanding instruction-following capabilities in scientific domains is essential for effectively leveraging Multimodal Large Language Models (MLLMs) to advance the development of scientific fields. In this work, we introduce SciMIF, a novel benchmark designed to evaluate the capability of MLLMs in following complex scientific instructions. Specifically, based on an extensive analysis of 22 distinct tasks across 5 representative scientific disciplines, we propose a comprehensive taxonomy comprising 10 constraint groups that captures both general functional requirements and discipline-specific characteristics. Guided by this taxonomy, we develop a high-fidelity instruction injection pipeline to systematically augment existing scientific datasets. We conduct comprehensive experiments on multiple state-of-the-art closed-source and open-source MLLMs. Our findings reveal significant performance disparities across different scientific disciplines, with chemistry posing greater challenges for current MLLMs. Furthermore, we observe that increasing the model scale does not yield corresponding improvements in constraint adherence, and current models still struggle severely with fine-grained constraints and instructions requiring the deep application of disciplinary knowledge. SciMIF fills the current void in evaluating multimodal instruction adherence within scientific domains, laying a crucial foundation for future enhancements of MLLMs in rigorous scientific applications. Data and code will be released at https://github.com/shenye7436/SciMIF .


### Quantitative Analysis of $ω$-Regular Robust MDPs
**Authors**: Ali Asadi, Krishnendu Chatterjee, Ehsan Kafshdar Goharshady, Mehrdad Karrabi, Alipasha Montaseri, Ali Shafiee

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25968v1](https://arxiv.org/pdf/2608.25968v1)

**Abstract**: Robust Markov Decision Processes (RMDPs) generalize classical MDPs by allowing uncertainty in transition probabilities and optimizing against their worst-case realization. We consider $(s,a)$-rectangular RMDPs with \emph{linearly defined} uncertainty sets and study parity objectives, which are a canonical representation of $ω$-regular objectives. An uncertainty set is linearly defined if it is described by linear inequalities over the transition distribution together with auxiliary variables, which capture the standard $L_1$ and $L_\infty$ balls as well as general polytopic uncertainty sets.
  The quantitative value is the supremum, over all agent policies, of the satisfaction probability guaranteed against the adversarial environment. Previous work studied the qualitative analysis, namely the almost-sure (resp. positive) problem that asks whether a single agent policy guarantees satisfaction with probability one (resp. positive probability) against every environment policy. In this work, we solve the exact quantitative problem.
  Our contributions are threefold. First, we show that both the agent and the environment admit pure memoryless optimal policies. Second, we give a polynomial-time algorithm for quantitative parity on linearly defined robust Markov chains and use it as a subroutine in a policy-iteration algorithm for RMDPs. The algorithm combines quantitative one-step improvements with qualitative almost-sure improvements. Finally, we report experiments comparing our approach with the explicit reduction to stochastic games.


## VLA
### LM-X: Explainable Action Modeling with Progress, Event, and Uncertainty Prediction for Generalist Robot Manipulation
**Authors**: Jin Lou, Jingxuan Zhu, Andong Chen, Xupeng Wang, Yuan Xu, Yuexuan Li, Xingdong Zhu, Zhijie Zhu, Yingwei Ji, Wenpeng Nie, Jingyi Li, Liangliang Chen, Jinyan Liu, Zhiqi Song, Jidong Zhang, Hongming Li, Yuchen Zhu

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25757v1](https://arxiv.org/pdf/2608.25757v1)

**Abstract**: Generalist vision--language--action (VLA) policies learn long-horizon behavior mainly through short-horizon action prediction and reveal little beyond sampled commands. This creates two coupled bottlenecks: a single action target must implicitly absorb task progress, intermediate intent, and local reliability, while these control states remain hidden during execution. Inspired by functional principles of biological sensorimotor control, we introduce LM-X , which organizes prediction across task, event, and motor scales without claiming anatomical correspondence. Three explicitly supervised signals are emitted online and directly condition action generation: return-to-go (RTG) measures visible task progress, event-to-go (ETG) identifies the next semantic transition, and heteroscedastic action flow estimates local reliability through propagated variance. Explanation is therefore intrinsic to control rather than generated post hoc. Before a costly 20-day pretraining run on 64 NVIDIA B200 GPUs, a controlled five-task pretraining gate verifies the design: the complete model improves success by 16.0 points over the action-only backbone and by 10.8 points over the strongest single-head variant. We then train LM-X on more than 20,000 hours of real-robot trajectories, including over 1,000 hours of failed policy rollouts. LM-X achieves 74.1\% across 50 randomized-hard RoboTwin2.0 tasks versus 55.4\% for GR00T N1.7, and 68.6\% versus 50.7\% across seven real-robot tasks. RTG tracks semantic progress and visible regression, while variance rises during hesitation and oscillatory control. These results show that explicit multi-timescale predictive state can strengthen control while exposing interpretable internal estimates.


### PonderPounce: A Pretrained MLLM as an Episode Context Engine for Robot Control
**Authors**: Suhwan Choi, Jaeyoon Jung, Sungkyung Kim, Yunsung Lee, Youngjae Yu

**Published Date**: 2026-08-25

**Updated Date**: 2026-08-25

**PDF Url**: [2608.24115v1](https://arxiv.org/pdf/2608.24115v1)

**Abstract**: Multimodal large language models (MLLMs) can integrate long visual histories, reason under partial observability, and infer behavior from a few examples. Yet vision-language-action (VLA) models generally inherit pretrained representations without using this contextual capacity as episode memory. Memory-dependent policies address this gap through purpose-built history mechanisms. PonderPounce instead reuses an MLLM's native causal context as robot memory. Ponder, a System2 MLLM, accumulates episode observations, demonstrations, and prior cognition in its native causal context and can generate subgoal text and demonstration reasoning for internal use. Pounce, a System1 VLA, receives the current observation, instruction, and proprioception directly; through the Ponder--Pounce interface, it asynchronously receives only the newest continuous cognition token and its age. Both are jointly trained end to end without a purpose-built memory module or separate bridge pretraining. Optimized serving achieves p50 latencies of 78ms for cognition refresh and 25ms for action-model invocation, supporting 20Hz action playback. On RoboMME with base-scale training data, PonderPounce reaches 60.83% with 9B and 50.04% with 0.8B under the same Pounce architecture and interface, versus 44.51% for FrameSamp+Modul and 17.93% for the current-observation π_{0.5}. With 9x data, it reaches 75.54% versus 57.88% for FrameSamp+Modul. On RoboCasa-DC, the same interface learns from action supervision alone and reaches 12.5% versus 11.6% for the strongest published demonstration-conditioned baseline, falling to 8.6% when cognition is replaced by a learned null state.


### Hierarchical Skill Retrieval for Data-Efficient Adaptation of Vision-Language-Action Models
**Authors**: Haoran Hao, Shahram Najam Syed, Jeff Schneider, Jeffrey Ichnowski

**Published Date**: 2026-08-25

**Updated Date**: 2026-08-25

**PDF Url**: [2608.24042v1](https://arxiv.org/pdf/2608.24042v1)

**Abstract**: While Vision-Language-Action (VLA) models pretrained on large-scale robot datasets provide a strong foundation for robot manipulation, their performance can degrade when adapted to new tasks with limited task-specific demonstrations. Retrieval offers a practical way to reuse existing demonstrations for data-efficient adaptation, but existing methods often rely on visual similarity, state-action representations, or task-level language matching. These approaches may overlook the hierarchical structure of long-horizon manipulation tasks, where complete task matches are rare but reusable skills are often abundant. To address this challenge, we propose Hierarchical Skill Retrieval (HSR), a retrieval framework for data-efficient VLA adaptation. Specifically, HSR first decomposes a target task into candidate skill sequences. It evaluates each plan based on both semantic plausibility and skill reliability estimated from the prior dataset. The selected decomposition is then used for hybrid retrieval. This combines subtask-level language retrieval with behavior-feature reranking to identify demonstrations that are both semantically relevant and compatible with the target task. Finally, we adapt the policy through a two-stage pretraining and finetuning pipeline, which separates general skill acquisition from task-specific adaptation. Experiments on the LIBERO benchmark and several real-world robot manipulation tasks show that HSR improves the average success rate by 10.3% and 21.3% over the strongest baseline, respectively. These results demonstrate the effectiveness of structured skill-level retrieval for data-efficient VLA adaptation. Videos and code are available at https://hoar012.github.io/HSR-Project.


### Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency
**Authors**: Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt, Bernd Kast, Philine Meister, Pranav Atreya, Qiyang Li, Finn Ferchau, Cesar Colmenero, Yash Shahapurkar, Gokul Narayanan, Melih Erdogan, Kai Wurm, Georg von Wichert, Oier Mees, Eugen Solowjow, Andrew Wagenmaker, Sergey Levine

**Published Date**: 2026-08-24

**Updated Date**: 2026-08-26

**PDF Url**: [2608.23831v2](https://arxiv.org/pdf/2608.23831v2)

**Abstract**: While reinforcement learning (RL) allows generalist robot policies to continually improve during deployment, the large model size of modern generalist policies, such as VLAs, poses a fundamental obstacle to effective RL improvement. In particular, their severe inference latency---which can lead to pauses or jerky movements---can alter the effective environment dynamics and, if not correctly accounted for, break the Markov assumption that RL relies on, causing standard RL algorithms to fail completely. In this work, we introduce a latency-aware framework, Asynchronous RL with Intermediate Information (ARLI), that enables RL-based improvement of generalist policies under inference delays. Our framework builds on asynchronous inference approaches, which interleave action generation with execution to hide latency, and addresses its incompatibility with RL by providing a low-latency RL policy design that maximizes reactivity within the inference window through two contributions: state augmentations that restore near-Markovian structure by incorporating committed actions and a mid-inference observation. We evaluate our approach across simulated and real-world manipulation tasks, and find that it enables effective finetuning under inference delays where standard RL fails entirely, even matching or exceeding the performance of standard RL in idealized no-latency settings.


### ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation
**Authors**: Siyuan Ma, Yutian Zhang, Boshi Zhang, Qinglian Wu, Jiaqi Zhai, Dong Wei, Xiaojin Huang

**Published Date**: 2026-08-21

**Updated Date**: 2026-08-24

**PDF Url**: [2608.20735v2](https://arxiv.org/pdf/2608.20735v2)

**Abstract**: Manipulating moving objects requires a policy to anticipate contact events, yet vision-language-action (VLA) policies are commonly fine-tuned from the current observation alone. World action models (WAMs) learn predictive dynamics, but running a video-scale teacher or explicitly imagining future frames at deployment is costly. We introduce ForeTime-VLA, a dense pi0.5 policy that distills a future-aware, action-equivalent representation from a frozen Fast-WAM-derived teacher while remaining causal at inference. Offline, current and future video latents are compressed into a whitened 64-D target. Online, an eight-frame history encoder predicts this target together with manipulation phase and normalized time-to-transition. Four future tokens and one phase token condition the VLM prefix, while the predicted future and transition horizon condition the action expert. Training retains the original flow-matching action target and adds cosine, relational geometry, phase, time-to-transition, and action-equivalence objectives. On a deduplicated conveyor-belt dataset, we compare 40k-step checkpoints on 768 matched windows per split. Test MAE decreases from 0.134119 to 0.130593 (2.63%; paired-bootstrap 95% CI: 0.82-4.48% improvement), and test L2 decreases by 3.02%, at a 2.46-2.93% latency cost. In quantitative real-robot evaluation, ForeTime-VLA achieves 81.1% stationary and 58.9% slow-moving grasp success, exceeding the next-best reference by 12.2 and 22.2 percentage points, respectively. Across three belt speeds, it completes 44/90 grasps versus 23/90 for pi0.5, including 11/30 versus 2/30 at fast speed. The agreement between offline orientation gains and reduced real-robot contact-pose failures supports causal future-token distillation as an effective way to improve dynamic manipulation without deploying the world-model teacher.


### Geo-VLA: Geometry-Aware Vision-Language-Action Planning via Internalization of Map Semantics
**Authors**: Ran Chen, Jiaxing Ren, Zhikun Zhang, Yunhao Hou, Junbao Zhuo, Bochao Zou

**Published Date**: 2026-08-18

**Updated Date**: 2026-08-18

**PDF Url**: [2608.21440v1](https://arxiv.org/pdf/2608.21440v1)

**Abstract**: Vision-language-action (VLA) models have advanced end-to-end autonomous driving by leveraging foundation models for semantic reasoning and long-tail generalization. However, their planning performance remains limited in complex driving environments because image-only representations inadequately capture planning-relevant road geometry and topology. In this paper, we propose Geo-VLA, a plug-and-play framework that enhances VLA models by learning geometry-aware visual representations. During training, Geo-VLA internalizes geometric map semantics to strengthen road-structure representations, while requiring no HD maps or additional lane information during inference. To support this approach, we introduce Geo-QA, a geometry-focused question-answering dataset that injects road geometry into vision-language representations through contrastive learning and instruction tuning. Experiments on NAVSIM v1 demonstrate that Geo-VLA consistently improves VLA planners with distinct action-generation architectures, achieving 92.1 PDMS and establishing a new state-of-the-art among single-camera VLA planners.


## Agent
### Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role
**Authors**: Ahmad Khan, Akram Bin Sediq, Sara Azadegi Naeini, Raviraj S. Adve

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26093v1](https://arxiv.org/pdf/2608.26093v1)

**Abstract**: Designing machine learning algorithms for wireless resource management is labour-intensive: the architecture, the loss function and the training recipe are all specified by hand. We demonstrate that this design layer can be surrendered to an autonomous agent in its entirety. We adopt the autoresearch protocol, in which an AI coding agent edits a training script, runs a fixed-budget experiment, and retains or discards the change according to a single immutable metric. We grant the agent authority over the architecture family, the input representation, the output parameterization, the loss function and the task-sampling law, and set it a target chosen for its difficulty: sum-least-percentile-rate power control across a multicell network. The formulation targets cell-edge throughput and is non-convex, non-smooth and strongly NP-hard away from its max-min vertex. Safeguards render the results trustworthy: a hash-pinned evaluator, an enforced inference contract and a pre-registered falsifier per experiment. In eighty-one unattended experiments over twenty-six hours, the agent reached $99.5\%$ of a converged minorization-maximization reference in one fixed-cost inference pass, at roughly $600\times$ lower inference cost, closing $94\%$ of the gap from its first working architecture, with one parameter set serving every network size and percentile target. It recovered provable structure rather than tuned constants: the output parameterization it discovered reproduces the exact max-min-optimal allocation at the minimum percentile, for every value of the trained weights.


### SwarmWorld: Stigmergic technological evolution in societies of language-model agents
**Authors**: Subhadeep Pal, Fiona Y. Wang, Markus J. Buehler

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26081v1](https://arxiv.org/pdf/2608.26081v1)

**Abstract**: Collective intelligence can emerge when individuals coordinate through a shared environment, allowing local actions to accumulate into durable social organization. Language-model agents offer a new substrate for this process, yet most multi-agent systems rely on direct conversation, predefined roles, or centralized workflows. It remains unclear whether decentralized agents can build functional technologies and outperform independent search. Here, initially homogeneous LLM agents in SwarmWorld self-organize without assigned roles or recipes into evolving technological societies. Agents explore a spatial environment, process resources, test materials, construct persistent artifacts, and write executable controllers evaluated by a deterministic simulator under unseen disturbances after the agents are removed. SwarmWorld splits cognition from consequence: agents propose architectures and controllers within fixed action and material schemas, while the simulated world determines function. Shared societies develop broader, more resilient technological portfolios than a strong best-of-N isolated-search baseline, although isolated search remains competitive for the strongest artifact. Agents differentiate into exploration, construction, maintenance, and coordination behaviors, transitioning as the world matures. Technologies accumulate through collaborative construction, executable inheritance, and persistent agent-artifact networks, with most reuse beginning through physical observation rather than communication. Explicit cultural mechanisms amplify collaboration and organization, but functional benefits depend on outcome and timescale. Physical stigmergy alone supports capable societies, while interaction drives persistent technological ecologies rather than universally superior individual inventions.


### Trace Integrity for LLM Data Agents: A Vision for Auditable Structured Reasoning in Real-World Systems
**Authors**: Srimonti Dutta, Akshata Kishore Moharir

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.26036v1](https://arxiv.org/pdf/2608.26036v1)

**Abstract**: Answer accuracy is an insufficient reliability signal for LLM data agents. In structured-data tasks, a benchmark-correct answer can be produced by an invalid trace. This paper introduces Trace Integrity, a deployment reliability criterion for evaluating whether the computation recorded behind an answer is explicit, executable, schema-valid, operator-faithful, replayable, answer-consistent, and auditable. We identify the Structure Gap as the deployment failure mode that makes Trace Integrity necessary: natural-language reasoning and free-form rationales do not reliably specify the operator-level programs required by real-world systems. We operationalize Trace Integrity with execution contracts, structured artifacts that bind user intent to schema elements, operator plans, assumptions, executable queries, verification status, and final-answer linkage. We also introduce CAIT (Correct Answer / Invalid Trace) Rate, which measures how often answer-only evaluation counts computationally unsupported outputs as successes. In an empirical demonstration on BIRD Mini-Dev, Direct SQL, Operation Summary + SQL, and Contract-First SQL achieve answer accuracies of 20%, 22%, and 24%, while their Trace Integrity Pass Rates are 39%, 43%, and 40% and their CAIT Rates remain high at 55%, 59.1%, and 45.8%, showing that answer accuracy, trace validity, and silent-failure risk are distinct evaluation signals. Real-world LLM data agents should, therefore, be evaluated not only by whether their outputs match a reference answer, but by whether those outputs are backed by auditable computation.


### Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
**Authors**: Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25937v1](https://arxiv.org/pdf/2608.25937v1)

**Abstract**: Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.


### TAU-Agent: An Agentic Retrieval-Augmented Framework for Traffic Anomaly Understanding
**Authors**: Yuqiang Lin, Yan Shi, Sam Lockyer, Harish Tayyar Madabushi, Adrian Evans, Wenbin Li, Yinhai Wang, Nic Zhang

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25935v1](https://arxiv.org/pdf/2608.25935v1)

**Abstract**: Traffic Anomaly Understanding (TAU) requires models and systems to detect, reason about, and explain anomalous events in transportation videos. To address this challenge, we propose TAU-Agent, an agentic retrieval-augmented framework for traffic anomaly understanding. Given a task query, a central retrieval agent orchestrates two visual perception tools, namely a Video Captioning Tool and an Open-Vocabulary Tracking Tool, to retrieve and select query-relevant evidence, including captions, temporal intervals, and object trajectories. The selected evidence, together with sampled video frames and the input query, is provided to a supervised fine-tuned vision-language model for final reasoning and answer generation. We evaluate TAU-Agent on both the in-domain and the out-of-domain benchmarks from the AI City Challenge 2026. TAU-Agent achieves scores of 0.6779 on Track 3, 0.3998 on Track 7, and 67.9275 on Track 8, ranking second, twelfth, and fifth, respectively. Code is available at: https://github.com/siri-rouser/TAU-Agent.


### Code World Model: Coding Agent as World Brain
**Authors**: Yiwen Chen, Guosheng Lin, Chi Zhang

**Published Date**: 2026-08-26

**Updated Date**: 2026-08-26

**PDF Url**: [2608.25927v1](https://arxiv.org/pdf/2608.25927v1)

**Abstract**: World models aim to simulate how complex environments evolve under actions and events, yet existing video-based world models primarily learn dynamics from visual observations, which reveal outcomes rather than the underlying knowledge, rules, and mechanisms governing world evolution. This makes it difficult to maintain persistent consequences and support coherent, open-ended evolution. We introduce Code World Model, a framework that separates world evolution from visual realization by combining the reasoning and coding capabilities of language models with the generative priors of video models. A coding agent serves as the world brain, reasoning about events and their consequences and generating executable code to maintain persistent world state and perform rule-consistent evolution. To connect executable state with visual generation, we introduce a proxy representation that encodes frame-wise spatiotemporal constraints and is compiled into a proxy video, which conditions a video model to render high-fidelity visual observations. We further develop data pipelines for constructing aligned proxy-observation pairs from gameplay and real-world videos. After fine-tuning on paired gameplay data, MiniMax-H3 follows proxy-based spatiotemporal specifications from simple interactive worlds built by the coding agent while preserving rich visual details and dynamics. These results demonstrate the potential of combining code for persistent world evolution with video models for flexible visual realization, providing a new path toward open-ended world models.


