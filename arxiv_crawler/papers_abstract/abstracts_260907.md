# Abstracts of Papers

## World Model
### WorldSculpt: Generating Compositional Worlds from Grounded Videos
**Authors**: Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05416v1](https://arxiv.org/pdf/2609.05416v1)

**Abstract**: We study the problem of generating a compositional 3D representation of a cluttered scene containing hundreds of objects. The goal is to represent the scene as a collection of individual object meshes placed in a shared world frame, as required by downstream applications such as gaming, AR/VR, simulation, and robotics. This task is challenging in densely cluttered scenes, where objects heavily occlude one another and each view reveals only a fraction of their geometry. Geometry-based approaches typically reconstruct the scene as a single representation and leave incomplete geometry in occluded regions, while existing compositional methods with generative priors are largely limited to relatively simple scenes. We show that complex scenes with hundreds of objects can instead be generated compositionally by adapting a strong single-object 3D generative prior to multi-view observations. We instantiate this paradigm with Pixal3D, extending it with a multi-view conditioning pathway that grounds object generation in multiple posed observations. Although the model is finetuned entirely on single objects in canonical space, it generalizes to large scenes with severe occlusion without any scene-level training, demonstrating the feasibility and scalability of this paradigm. We further introduce UE-MeshyScene, a photorealistic benchmark of densely cluttered scenes with hundreds of objects, per-object annotations, and ground-truth meshes. Across single-object, controlled multi-object, and UE-MeshyScene evaluations, our method consistently outperforms prior approaches, with larger gains as scene complexity and occlusion increase. Finally, we demonstrate broader applicability by converting generated 3DGS worlds, such as Marble and HY-World 2.0, into compositional mesh scenes.


### UniMate: One Unified Model to Animate Diverse Skeletons
**Authors**: Linzhan Mou, Jiahui Lei, Zhiyang Dou, Chenyue Cai, Chaoyue Song, Adam Finkelstein, Szymon Rusinkiewicz

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05415v1](https://arxiv.org/pdf/2609.05415v1)

**Abstract**: Recent advances in automatic rigging now deliver animation-ready 3D assets at scale, yet generating the motion to drive them remains a bottleneck. Existing learned animators are topology-constrained: they rely on category-specific templates or require per-skeleton fine-tuning and reference motions at inference. We present UniMate, a unified foundation model that synthesizes articulated motion for arbitrary skeletons from a rigged 3D asset and a text prompt, with no test-time optimization or per-skeleton retraining. UniMate introduces a topology-aware diffusion transformer, which integrates skeletal topology into attention via three mechanisms: (1) a graph-aware attention bias from pairwise joint relations and geodesic distances; (2) a spectral rotary position embedding generalizing RoPE to arbitrary kinematic trees via the graph Laplacian; and (3) a global topological conditioner attention-pooled from the rest-pose skeleton. We also curate UniML3D, 13,006 motion sequences spanning bipedal, quadrupedal, avian, marine, insectoid, serpentine, and articulated rigid objects with unified canonicalization and text pairing. Trained on this dataset, UniMate outperforms state-of-the-art baselines in quality, generalization, and efficiency, and supports zero-shot cross-topology transfer, in-betweening, expansion, and text-guided editing. Our project page is available at https://linzhanmou.com/unimate/.


### Two extremely irradiated volatile-rich sub-Neptunes with companions in the TOI-426 and TOI-1839 systems: Insights into arrival and survival near the lower edge of the Neptunian desert
**Authors**: A. Castro-González, O. Barragán, D. J. Armstrong, A. Aguichine, V. Bourrier, D. Ehrenreich, E. X. Tao, J. Lillo-Box, M. R. Standing, S. G. Sousa, E. Delgado-Mena, A. Moya, V. Adibekyan, M. Lendl, C. Hellier, S. B. Howell, E. Furlan, C. Ziegler, A. C. M. Correia, K. Cui, P. Figueira, J. M. Jenkins, M. A. Fetzner Keniger, B. Merín, A. Osborn, L. Parc, F. Pepe, P. J. Wheatley, J. N. Winn

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05413v1](https://arxiv.org/pdf/2609.05413v1)

**Abstract**: Using TESS photometry and 147 HARPS radial velocities, we confirm two extremely irradiated, volatile-rich sub-Neptunes near the lower edge of the Neptunian desert: TOI-426 b and TOI-1839 b, orbiting the solar-type stars HD 34390 and TYC 304-865-1. We modelled stellar activity with shared-timescale and multidimensional Gaussian processes. The planets have orbital periods of approximately 1.32 and 1.42 days, radii of $2.19\pm0.09$ and $2.27\pm0.10$ Earth radii, and masses of $6.7\pm1.8$ and $7.10\pm0.78$ Earth masses, respectively. They receive approximately 1700 and 1050 times Earth's irradiation, yet their densities require substantial volatile content. We also detect a transiting sub-Neptune, TOI-1839 c, at approximately 4.02 days and a giant companion, TOI-426 c, with a period of $235.8^{+9.2}_{-8.5}$ days and a minimum mass of $444^{+18}_{-17}$ Earth masses, assuming a circular orbit. Interior-structure and atmospheric-escape models yield mass-loss timescales of 1-100 Myr for hydrogen/helium envelopes, compared with 100-1000 Gyr for water-dominated envelopes, favouring a steam-world interpretation for all three transiting planets. A population analysis reveals a striking excess of detected outer giant companions to low-mass sub-Neptunes near the desert edge, where high-eccentricity tidal migration is expected to circularize surviving planets: 36% (9/25) within the tidal survival band versus 6% (9/148) outside it (Fisher exact test $p=1.4\times10^{-4}$). This excess is robust to changes in sample selection and companion definitions. The survival of these volatile-rich planets challenges a boundary set solely by evaporation of primordial hydrogen/helium envelopes, while the companion excess supports an important role for high-eccentricity tidal migration in shaping the lower desert edge.


### WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
**Authors**: Ji Soo Lee, Xilun Chen, Pierce Chuang, Ashish Shenoy, Jason Wei, Dohwan Ko, Hyunwoo J. Kim, Benoit Corda

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05405v1](https://arxiv.org/pdf/2609.05405v1)

**Abstract**: Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whether AI systems can reason over a real user's longitudinal wearable record. We introduce WearableQA, a benchmark comprising 4,084 10-option multiple-choice questions constructed from the wearable time series, blood biomarkers, and demographics of 200 real users, each with up to 500 days of daily measurements. WearableQA preserves authentic wearable distributions that include device noise and inter-individual variability. To evaluate distinct reasoning capabilities, we introduce 16 question types organized along two complementary axes: data versus health reasoning, which distinguishes computation over longitudinal measurements from physiological interpretation; and single- versus cross-signal reasoning, which separates reasoning about individual signals from the integration of multiple signals. To construct reliable questions at scale, we adopt a dual-grounding framework that combines literature-grounded physiological findings with statistically validated population-grounded physiological patterns. This enables the capture of meaningful relationships observed in real-world wearable data. Evaluation of 14 proprietary and open-source LLMs demonstrates that WearableQA effectively differentiates model capabilities, with performance ranging from 19.6% to 72.9% against a 10% chance baseline. Moreover, WearableQA remains far from solved: most models achieve accuracies below 60%. Overall, WearableQA provides a realistic and diagnostic benchmark for evaluating LLM reasoning over real-world wearable data.


### Diffusion TV: Experiencing Diffusion Models through Tangible, Embodied Interaction
**Authors**: Sihwa Park

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05404v1](https://arxiv.org/pdf/2609.05404v1)

**Abstract**: Diffusion TV is an interactive AI art installation that offers a tangible and embodied experience of diffusion models through a modified CRT TV. By physically manipulating the TV's antenna, audiences control the clarity of AI-generated images and sounds, metaphorically enacting the denoising process that underlies diffusion-based generation. Using the tuning knob, participants switch between three channels featuring AI-generated animals from the Past (extinct species), Present (endangered species), and Future (speculative creatures), situating the interaction within a temporal and ecological narrative. Through continuous audiovisual feedback and physical interaction, Diffusion TV foregrounds the generative process over final outputs, allowing audiences to explore intermediate states as experiential material. Rather than providing explicit technical explanation, the work presents an alternative, embodied mode of explainable AI that invites exploratory engagement with and reflection on generative technologies.


### RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous Retail Environments
**Authors**: Quoc H. Nguyen, Ali Lafzi, Abhijeet Phatak, Siddharth Pratap Singh, Rohit Upadhyay, Yogananda Domlur Seetharama, Chittaranjan Tripathy

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05403v1](https://arxiv.org/pdf/2609.05403v1)

**Abstract**: Retail search systems serve diverse geographic regions with distinct query patterns, vocabularies, and product preferences, creating significant data heterogeneity that challenges both privacy-preserving training and model personalization. Federated learning offers a natural solution for privacy, but standard FL methods produce global models that sacrifice regional performance, while existing personalized FL approaches operate at the parameter level and catastrophically collapse on modern transformers (below 10\% accuracy on T5) due to tied embeddings and LayerNorm interactions. We introduce RegionFed, an \textit{architecture-robust} federated learning framework that sidesteps this failure by operating entirely at the gradient level. RegionFed uses the $\ell_2$ conflict between regional and global gradients as a unified signal that (i) diagnoses heterogeneity, (ii) routes each region to the cheapest sufficient personalization strategy, and (iii) adaptively controls personalization strength. Because it treats models as differentiable black boxes, RegionFed deploys on T5-Small, T5-3B, RoBERTa, and CNN with zero code changes, providing large gains on transformers (where parameter-level methods collapse) and consistent improvements on CNNs. Across three public datasets (Amazon ESCI, Amazon Reviews, LEAF-FEMNIST) and four architectures, RegionFed-Meta achieves 92.27\%, closing the gap to the privacy-violating centralized upper bound (Centralized + Regional Weighting: 92.04\%, $Δ$=0.23pp, within 1$σ$) while providing $(ε{\approx}0.60)$-differential privacy and $\mathcal{O}(1/\sqrt{T})$ convergence.


## Generation
### A Deep Generative Model for Synthesizing Labeled Wireless Signals
**Authors**: Yuxiao Li, Keke Hu, Santiago Mazuelas, Yuan Shen

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05396v1](https://arxiv.org/pdf/2609.05396v1)

**Abstract**: Wireless signals with position-related labels are pivotal for both performance evaluation and model training in the realm of wireless sensing. However, acquiring real-world datasets is often challenged by significant measurement and labeling costs. Traditional methods for synthesizing labeled wireless signals typically rely on environmental models, leading to extensive hyper-parameter tuning and inadequate realism for comprehensive model training purposes. To address these limitations, we introduce a novel deep learning (DL)-based method, namely Inter-Instance Generative Adversarial Networks (IIns-GAN), to generate realistic labeled wireless signals. The generated signals are particularly adaptive to different environment scenarios and well-suited for various model training tasks, including distance estimation and environment identification. We have conducted extensive experiments on public Ultra-Wideband (UWB) datasets to evaluate the realism and utility of the generated signals. The results demonstrate that the signals generated by IIns-GAN mirror the physical characteristics of real-world measurements, and significantly contribute to the improvement of model training in diverse wireless sensing tasks.


### Reflection-aware Generative Novel View Synthesis
**Authors**: GeonU Kim, Shin Dong-Yeon, Tae-Hyun Oh

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05382v1](https://arxiv.org/pdf/2609.05382v1)

**Abstract**: We propose Ref-GeNVS, a training-free, reflection-aware method for generative novel view synthesis (NVS) in mirror scenes. Existing multi-view diffusion models often fail to recognize the mirror in the scene and cannot exploit reflected content for scene generation. To fix this issue without additional training, our key idea is to treat a mirror image as two complementary views. From input images, we estimate the mirror plane and reflect camera poses to form virtual views. Based on this virtual view setup, we propose a two-stage generation method consisting of Mirror-gated attention and Reflection injection, which enables reflection-consistent NVS by explicitly leveraging reflection relationships in a multi-view diffusion model. Ref-GeNVS inherits the strong generalizability of the multi-view diffusion backbone, while it does not require finetuning. On synthetic and real scenes including mirrors, Ref-GeNVS outperforms recent generative NVS methods by generating reflection-consistent and contextually coherent novel views, revealing scene structure visible only through mirrors. Project page: https://kim-geonu.github.io/Ref-GeNVS/


### Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models
**Authors**: Matthias Busch, Marius Tacke, Sviatlana V. Lamaka, Mikhail L. Zheludkevich, Christian J. Cyron, Roland C. Aydin, Christian Feiler

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05381v1](https://arxiv.org/pdf/2609.05381v1)

**Abstract**: Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, while on the remaining datasets it appears only in isolated cells. We run our experiments at two reasoning levels and find that reasoning changes retrieval. The same experiments, on the same molecules and with the same prompt, are flagged $89\%$ more often at the higher reasoning level than at the lowest one. Finally, we test a way to interrupt retrieval in our most contaminated cases, and find that the strongest models in some cases still recognise a combination of transformed SMILES strings and original labels. Furthermore, suppressing retrieval moves the prediction errors of the different models closer together in relative terms, while their differing use of verbatim retrieval spreads them apart. This indicates that the general predictive capability of an LLM is not determined solely by the amount of memorised values. This work provides an overview of the amount and depth of verbatim retrieval in molecular regression benchmarks using LLMs.


### CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents
**Authors**: Haoting Shi, Wenhao Wang, Weicheng Fang, Yaozhong Liang, Tian Jin, Pengxiang Zhao, Guangyi Liu, Siheng Chen, Yanfeng Wang

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05374v1](https://arxiv.org/pdf/2609.05374v1)

**Abstract**: Computer-use agents have advanced on benchmarks like OSWorld and AndroidWorld, but still act mostly through the GUI, often producing inefficient trajectories. Real-world computer work is hybrid, combining visual-state inspection with precise, high-throughput command-line operations, so capable agents must coordinate both modalities over shared application state. Yet scalable hybrid environments remain scarce because supporting both GUI and CLI over real applications typically requires substantial manual engineering for each application. Existing agents also struggle to use the two interfaces complementarily: CLI-native agents lack visual perception for tasks involving interface state or layout, while GUI-native agents are inefficient for operations better executed through commands. We introduce CUA-Universe, a scalable environment-to-data pipeline that turns real desktop software into hybrid GUI+CLI environments. App-Forge adapts applications into reproducible VMs and command-line surfaces it discovers, wraps, or generates, scaling to 16 applications; Task-Weave synthesizes diverse hybrid tasks of controllable difficulty from reusable operations over seed files; and Path-Steer steers rollouts along efficient hybrid paths and harvests verified trajectories for post-training. Training on this data shifts behavior from inefficient GUI interaction and brittle CLI scripting toward effective GUI+CLI orchestration. Our 9B model improves both success and efficiency on CUA-Verse (Score +39.3 pts; -37% steps, -60% tokens), OSWorld (SR +16.8 pts; -57% steps, -44% tokens), and OSWorld-MCP (Score +7.84 pts; -27% steps, -30% tokens). CUA-Universe provides a scalable path toward more capable and efficient computer-use agents.


### Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool
**Authors**: Samuel Kushnir, Kimia Noorbakhsh, Kavya Sreedhar, Liqun Cheng, Ming Liu, Parthasarathy Ranganathan, Mohammad Alizadeh, Fred Kjolstad, Suvinay Subramanian

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05364v1](https://arxiv.org/pdf/2609.05364v1)

**Abstract**: Machine-learning performance modeling is a uniquely hostile terrain for long-lived software: the assumptions baked into today's abstractions are invalidated by tomorrow's models and systems, forcing perpetual refactoring of performance-modeling frameworks. Meanwhile, AI coding agents have become fast and capable enough that regenerating an entire library is cheaper than paying down the tech debt of incrementally patching it. We describe SMART, a rigorous symbolic performance-modeling library for ML systems whose main branch contains almost no code: the repository is a DAG of self-contained natural-language design docs, coding sub-agents regenerate the implementation from only the docs on new version updates, and every human change is a natural-language edit to a doc--self-documenting by construction. Two ingredients make regeneration reliable: (i) a design-doc style built around step-by-step worked examples that act as in-context demonstrations for the generating agents, and (ii) a minimal, recursively defined operator IR with symbolic (SymPy) cost expressions, a fast analytical roll-up mode for large sweeps, and a slow modulo-scheduling mode for fine-grained schedule studies. Regenerated implementations reproduce hand-audited reference models--including DeepSeek-V3 serving on a TPU pod slice--to round-off precision, suggesting that design docs--not code--can be the durable artifact for ML-systems co-design tools.


### Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation
**Authors**: Siliang Liu, Mohammad Ghasemi, Sapan Patel, Amin Banitalebi-Dehkordi

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05363v1](https://arxiv.org/pdf/2609.05363v1)

**Abstract**: Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits. Large language models (LLMs) can reason about such distinctions, but applying them directly to hundreds of millions of product pairs is operationally impractical. We introduce a two-level framework that distills LLM reasoning into an efficient non-generative student and adapts its decision boundary to product-type-specific trade-up criteria. At Level 1, a retrieval-augmented few-shot LLM teacher generates structured relation labels and natural-language rationales. These rationales supervise a compact embedding-pair classifier through alignment and contrastive objectives; at inference, the student uses only two precomputed 768-dimensional product embeddings, with no LLM calls or text generation. On a fixed human-annotated benchmark of 8,352 pairs, a 15.5M-parameter four-class reasoning-distilled student achieves AUC 0.924 (95% CI [0.918, 0.929]), compared with 0.912 for the four-class label-only student. At Level 2, product-type test-time training (PT-TTT) uses few-shot demonstrations to optimize lightweight category-specific adapters over the frozen student. PT-TTT improves AUC from 0.924 to 0.941 and average precision from 0.920 to 0.940. On a 100K-pair proxy catalog, the distilled student on a single eight-GPU machine is approximately 5,000x faster and 10,000x lower in estimated cost than direct LLM inference.


## VLA
### RoboSPA: Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks?
**Authors**: Zhenxuan Fan, Bo Zhang, Yutong Lin, Yuqian Yuan, Juekai Lin, Liang Liang, Zhuoyi Huang, Wenqiao Zhang, Juncheng Li, Siliang Tang, Jun Xiao, Yueting Zhuang

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05324v1](https://arxiv.org/pdf/2609.05324v1)

**Abstract**: Vision-Language-Action (VLA) models have shown promising progress in language-conditioned robotic manipulation. However, existing datasets and benchmarks mainly evaluate task completion under predefined settings, offering limited insight into model reasoning under increasing spatial and procedural complexity. We introduce \textbf{RoboSPA} (\textbf{Robo}t \textbf{S}patial-\textbf{P}rocedural \textbf{A}ssessment), a large-scale robotic manipulation dataset and benchmark for diagnosing embodied reasoning in VLA models. \texttt{RoboSPA} focuses on two core dimensions, Fine-Grained Spatial Reasoning and Long-Horizon Procedural Planning, covering 10 task categories and 56 base tasks. Each task is instantiated across five difficulty levels, yielding 280 variants with increasing spatial ambiguity and procedural complexity. We collect 527K trajectories across multiple embodiments and diverse scenes. Beyond binary success rate, \texttt{RoboSPA} introduces diagnostic metrics for more detailed evaluation. Experiments on representative VLA models show that current systems still struggle with complex spatial relations, precise low-level execution, and memory-intensive planning. These results establish \texttt{RoboSPA} as a challenging diagnostic benchmark for developing more capable, reliable, and generalizable embodied agents. Our data and code are available at https://github.com/fanzhenxuan/RoboSPA.


### VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models
**Authors**: Chenyu Su, Zhaolong Shen, Yuan Qian, Chen Qian, Rui Zhang, Feng Yan, Weixing Chen, Fei Zhang, Jiamin Wang, Shuang Cong, Weiwei Shang

**Published Date**: 2026-09-03

**Updated Date**: 2026-09-03

**PDF Url**: [2609.04355v1](https://arxiv.org/pdf/2609.04355v1)

**Abstract**: Pretrained vision-language-action (VLA) models enable broad manipulation but remain unreliable in tasks demanding precision and repeatability. Applying real-world online reinforcement learning (RL) to VLA post-training enables autonomous trial-and-error improvement beyond demonstrations alone, but exposes two bottlenecks: 1) unreliable value signals can induce policy drift; 2) large-VLA overhead constrains throughput and sample efficiency. To address these challenges, we present VLA-Precision, an efficient real-world online RL framework featuring the Asymmetric Co-Bootstrapping (ACoB) algorithm and the ACoB-Stream architecture. Specifically, ACoB establishes asymmetric co-bootstrapping across timescales: early intervention-guided behavioral learning rapidly improves policy performance while enhancing online experience quality. As autonomous experience accumulates, global return propagation and local preference ranking progressively calibrate value estimates, yielding relative action advantages for reference-regularized policy improvement while suppressing drift. To enable ACoB on large VLAs, we develop ACoB-Stream, a closed-loop experience--policy architecture that establishes invariant-state decoupling and on-demand streaming as design principles, delivering up to 10.9$\times$ improvements in throughput and computational efficiency. Extensive evaluations on nine high-precision chemistry tasks across four categories and four robot embodiments show that VLA-Precision achieves 98.3\% mean success rate in 45.8 min/task, with 27.6 s episodes running at 1.2$\times$ and 1.8$\times$ the speeds of VLA and RL baselines. Resources are available at https://vla-precision.github.io.


## Agent
### Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe
**Authors**: Dain Kim, Eungi Cho, Kyumin Kim, Shinyeong Noh, Kyuseong Lim

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05395v1](https://arxiv.org/pdf/2609.05395v1)

**Abstract**: Data-sovereignty regulations increasingly require public institutions to deploy open-source, on-premise LLM agents that chain multiple tool-calls across live government APIs. However, open-source models consistently underperform in this multi-step setting, and no existing benchmark measures the gap. We introduce the Korean Open Public API Benchmark (KOPA-Bench), comprising 145 real-world tasks. To close this gap, we present EDGE, an Execution-grounded Dynamic Graph for tool-calling data synthEsis driven by live execution. EDGE builds a graph of how each tool's output can feed another's input, keeps only the links that succeed when actually called against the live APIs, and traverses these verified links to synthesize executable multi-step trajectories. Fine-tuned via GRPO on the resulting dataset, our 9B model nearly matches the untuned 27B model from the same family, improving substantially not only on KOPA-Bench but also on the BFCL benchmark.


### Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence
**Authors**: Urja Pawar, Rajitha Ramanayake, Nabeel Kemal, Ashwin Kandath, Owen O'Neill, Guillaume Bourgeon, Houssem Chatbri

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05385v1](https://arxiv.org/pdf/2609.05385v1)

**Abstract**: LLM decision components that can operate within agent workflows often produce action-relevant recommendations or judgements together with explanations. Operators may use the named factors to monitor a system, diagnose errors, or decide when to escalate an output. Such use assumes that the explanations agree with the component's observable decision behaviour. We test two interpretations of the named factors: necessity, meaning that changing a factor would change the output, and sufficiency, meaning that retaining it while removing other changeable information would preserve the output. We evaluate these interpretations in two synthetic use cases: recommending advisors to clients and judging prompts for harmfulness or risk. Models return an output and the top three factors that most influenced it. Controlled black-box interventions estimate a necessity score for each factor by measuring how often changing it changes the output, and a sufficiency score by measuring how often retaining it preserves the output. Across eight models from the Claude, GPT, and Gemini families, the mean Spearman correlations between the cited ranking and the necessity and sufficiency scores are 0.349 and 0.354 for advisor recommendation, and 0.431 and 0.580 for prompt monitoring. Furthermore, an uncited factor scores above the lowest-scoring cited factor in 57.6% of advisor responses under necessity and 58.1% under sufficiency; the corresponding prompt-monitoring rates are 25.8% and 8.9%. The cited top three contain useful information but do not reliably identify the three factors with the strongest measured influence under necessity or sufficiency. The framework provides a black-box reliability check for explanations used in agent oversight while remaining scoped to individual LLM decisions.


### Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability
**Authors**: Ankit Goyal, Jaideep Ray

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05339v1](https://arxiv.org/pdf/2609.05339v1)

**Abstract**: Model upgrades are routine; memory migrations are not. An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair may fail without the original evidence. We compare memory as the same history is preserved verbatim for long-context reading (LC-RAW), divided into chunks for retrieval-augmented generation (RAG), compressed by a model into natural-language notes (NOTES), or normalized into a fixed-schema knowledge graph (KG-fixed). The study uses 48 synthetic histories with randomized answer codes, exact scoring, and two open-weight models with sub 10 billion parameters.
  Our measurements show that fixed-schema structures transfer reliably, with KG-fixed accuracy changing by only $+0.0004 \pm 0.0020$ following a writer swap. Conversely, compressed NOTES exhibit high model coupling, with accuracy shifting asymmetrically by $+9.91$ or $-13.28$ percentage points depending on the specific migration direction. In RAG systems, partial embedding migrations using a 50/50 mixed index capture only a 4.96-point accuracy improvement, forfeiting the majority of the 11.90-point gain achieved through full re-embedding. Diagnostic decomposition attributes 80% ($0.467 \pm 0.014$) of the NOTES accuracy deficit to information lost during initial construction, whereas retrieval failures drive 81% ($0.364 \pm 0.012$) of the RAG deficit. Finally, store-only repair of NOTES fails to reach a 90% performance recovery target in all 48 test cases, whereas retaining the raw source history enables successful recovery in 34 of 48 cases for one tested direction. These findings highlight the necessity of direction-specific migration testing, strict embedding space isolation, and the retention of source histories for memory repair.


### The History Is the Detector: Executing CVE Patch History, End-to-End
**Authors**: Qiushi Wu, Kevin Eykholt, Youngja Park, Xiaokui Shu, Dhilung Kirat, Douglas Lee Schales, Ian Molloy

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05335v1](https://arxiv.org/pdf/2609.05335v1)

**Abstract**: Public vulnerability databases collect rich information about known software flaws, including their weakness types, affected components, and related patches. Fixing commits provide the exact code changes that removed these flaws. While these records capture why the original code was unsafe, they are documented mainly for human inspection rather than automated reuse. Consequently, the same unsafe conditions may still exist elsewhere in code without a known advisory, leaving much of this detection knowledge unused.
  We present BUGSTONE-E2E, a framework that transforms vulnerability history into executable detection rules and validates their findings. First, BUGSTONE-E2E mines reusable rules from verified fixing commits, capturing scan anchors, fix semantics, and CVE provenance and organizing them by CWE and language. Second, detection follows a funnel-shaped pipeline: early stages process a large pool of candidates using lightweight analysis, while later stages apply increasingly capable and expensive models to a shrinking set of targets. Specifically, BUGSTONE-E2E first enumerates call sites matching rule anchors using Tree-sitter, then removes benign sites using lightweight heuristics without LLM calls. Next, LLM-based agents inspect the remaining candidates guided by the rule. Following this inspection, the system re-triages surviving candidates and builds runtime verifications, then generates scope-checked patches validated via two-sided differential tests. Using 19,325 high-severity CVEs from 2022 to 2026, BUGSTONE-E2E identifies 2,710 fixing commits and constructs 1,033 detection rules across 56 CWE families, packaged into 172 skills. When applied across 14 programs, it produced runtime evidence for 644 findings. These results demonstrate that CVE history can be turned into an executable workflow, transforming past vulnerabilities into reproducible detection and repair.


### Optimal Rates for Agentic Networked Information Aggregation
**Authors**: MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi, Mahdi JafariRaviz, Shayan Taherijam

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05318v1](https://arxiv.org/pdf/2609.05318v1)

**Abstract**: Building on the pioneering paper of Kearns, Roth, and Ryu (SODA'26), we study information aggregation in a networked learning model. The model captures a central pattern in agentic AI: each agent sees only part of the data and passes on only its own conclusion. Their model considers a linear regression problem with the mean squared error (MSE) loss. Agents sit in a DAG and each sees only a subset of the features and its parents' predictions, fits a linear predictor, and passes only its prediction forward. The benchmark is the full-feature learner that sees all raw features. A path of depth $D$ is $M$-covered if every block of $M$ consecutive agents collectively sees all raw features. Kearns, Roth, and Ryu proved that the excess mean squared error of the last agent on such a path is $O(M/\sqrt D)$, and gave a cyclic instance with excess error $Ω(M/D)$ for $D<M^2$.
  We close this gap: the correct rate is constant up to depth $M^2$, and $Θ(M^2/D)$ beyond it. We first give a sharper analysis of the cyclic instance and improve its lower bound to $Ω(\sqrt{M/D})$ for $D<M^2$. We then construct, for every depth $D\ge M^2$, an $M$-covered path of depth $D$ with excess error $Ω(M^2/D)$. The same instance gives the constant lower bound for all $D < M^2$. We also show that for any fixed distribution the excess error contracts geometrically along the path, ruling out any single instance that witnesses any polynomial lower bound at every depth.
  Finally, we prove the same optimal rate for logistic classification in the logit-passing model of Bateni et al., which considers the binary cross-entropy (BCE) loss. The same improved upper bound of $O(M^2/D)$ holds, and we transfer all the regression lower bounds by showing that on those examples the logistic path follows the least-squares path up to rescaling.


### Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness
**Authors**: Alexander Neubauer, Tianzhen Hong, Han Li, Mengbo Yu, Amin Darbandi, Yannick Fürst, Martin Kriegel

**Published Date**: 2026-09-04

**Updated Date**: 2026-09-04

**PDF Url**: [2609.05314v1](https://arxiv.org/pdf/2609.05314v1)

**Abstract**: Building automation systems generate rich sensor data yet remain insight-poor because heterogeneous point naming, missing metadata, and fragmented documentation obstruct their operational use. This systematic review analyses and codes 66 peer-reviewed studies on large language models (LLMs) for HVAC operations published between 2023 and March 2026. Each study is classified across five application families and three LLM method families and assessed for evidence realism, deployment readiness, and the responsibility boundary between the LLM and physical HVAC decisions. The corpus is concentrated in building energy modelling (BEM, 32 of 66 papers), while load forecasting remains too sparse for subfield-level conclusions. Only four studies reach pilot-level evidence, and none reports sustained operational deployment. No study was classified as ready-now for industry adoption; three were near-term and 63 research-only. Nevertheless, several bounded, human-in-the-loop uses merit near-term trials, including point-name normalisation, document-grounded operator support, BEM workflow assistance, and advisory interfaces around physics-based controllers. Conventional machine learning (ML), model predictive control (MPC), reinforcement learning (RL) and ontology-based tools remain more adopted for high-frequency control, short-horizon numerical forecasting, and well-posed ontology mapping, while autonomous agentic operation and unvalidated occupant proxies remain research-stage. Current evidence therefore supports LLMs primarily as semantic and workflow layers rather than autonomous HVAC controllers. Future work should prioritise field-validated benchmarks, orchestration evaluation under operational constraints, and LLM-MPC/RL architectures with bounded latency and verifiable safety properties.


