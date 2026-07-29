# Abstracts of Papers

## World Model
### INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models
**Authors**: Junhan Sun, Hao Zhao, Guofeng Zhang

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26056v1](https://arxiv.org/pdf/2607.26056v1)

**Abstract**: Forward latent world models predict how actions change a scene, but recover actions for a desired change only through expensive test-time search. We introduce INTACT (INtent-To-ACTion), an end-to-end JEPA that turns action-labeled, reward-free trajectories into a deployable intent-to-action interface. Each transition supplies physical intent $z_{t+1}-z_t$, while a future goal supplies deployment intent $\operatorname{sg}(z_g)-z_t$. The architecture is isomorphic between the local and goal motion-intent backbone-input graphs through an identical four-slot grammar and shared parameters, and between supported local and goal motion-intent families through action-law semantics induced by the same predictor rather than pointwise latent equality. INTACT also provides intact transfer from RGB evidence to action-effective latent intent coordinates and from intent families to their corresponding action-law families. Asymmetric endpoint gradients ground physical successors and fix future goals as anchors, joining representation learning and control without pointwise latent matching or globally linear dynamics. The resulting coordinates support a robust distributional action law: its conditional mean serves directly as a search-free policy, while sampling remains available for diversity or optional verification. On the four official LeWM tasks, one-epoch, zero-search models reach 85.78\%, 100.00\%, 97.67\%, and 97.89\% success. Optional local CEM centered on the Direct plan reaches 96.86\% macro success using 384 instead of 9,000 candidate sequences, reducing sampling by $23.44\times$ while improving pure CEM by 16.00 points. One shared four-task encoder reaches 89.39\% E5 Direct macro and improves every task over jointly trained LeWM, while predicted--expert action-family kNN tracks Direct success at $r=0.954$. Direct inference takes 2.9--5.5 ms.


### $π\mathbf{R}^2$: Reactive Real-time Flow Policies
**Authors**: Sungjae Park, Shubham Tulsiani

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26055v1](https://arxiv.org/pdf/2607.26055v1)

**Abstract**: Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones. Such chunks run open-loop, so the policy cannot react to sensory input arriving mid-execution, sacrificing \emph{reactivity}. Replanning more often would restore it, but the perception-to-action pipeline (a large backbone plus multiple denoising steps) is too slow: this \emph{latency} forbids frequent replanning and leaves committed actions stale, making such policies ill-suited for dynamic, closed-loop control. We present $π\mathbf{R}^2$, which makes these policies reactive and real-time while retaining large backbones, expressive multi-modal policies, and multi-action prediction. Built on the per-position noise schedule of diffusion forcing, $π\mathbf{R}^2$ contributes two ideas. First, it splits conditioning into a fast channel (proprioception, fresh every tick) and an asynchronously updated slow channel (vision-language features), so the policy reacts to proprioception within a chunk while tolerating stale vision. Second, a latency-adaptive flow schedule treats in-flight actions as inpainting conditioning and emits actions in one denoising step per call, letting one trained model adapt to varying hardware latency. Requiring minimal modification to existing architectures, $π\mathbf{R}^2$ can be finetuned from a pretrained policy: applied to GR00T-N1.7 on a real xArm6+XHand platform, it replans closed-loop roughly $4\times$ faster than the base policy (~$25$Hz on an A5000 GPU), acting on a fresh observation every $40$ms. Across simulation and real-world manipulation tasks, $π\mathbf{R}^2$ improves the success rate by up to $23\%$ in simulation and $30\%$ in the real world over the strongest baseline. Project page: https://pi-r2-flow.github.io/


### Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA
**Authors**: Tom Saliencro, Rohan Desai, Priya Nair, Maya Lindqvist, Daniel Whitmore

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26052v1](https://arxiv.org/pdf/2607.26052v1)

**Abstract**: Mixture-of-Experts (MoE) variants of Low-Rank Adaptation (LoRA) route every token to a fixed number of experts $k$. Tokens differ in how uncertain the model is about them, so a single k over-spends on easy tokens and under-serves hard ones. We observe that the router's output distribution is already a per-token uncertainty signal: peaked mass indicates confidence, while a flat distribution indicates ambiguity. We introduce CARE (Confidence-Adaptive Routing of Experts), which admits experts in a nucleus fashion. Experts are activated in decreasing router weight until their cumulative mass reaches a threshold, with a small extension when the admitted experts disagree. A budget thermostat calibrates the threshold so that the average number of active experts matches any target. CARE is a drop-in, single-forward-pass rule with no extra parameters. Across eight commonsense benchmarks on LLaMA-3.1-8B and Qwen2.5-7B, as well as math, code, and knowledge tasks, CARE improves over fixed top-k MoE-LoRA at matched compute and matches the fixed-k=4 baseline while activating fewer experts. The same confidence and disagreement signals also improve out-of-distribution detection over MSP, entropy, and multi-pass proxies. We support the design with nucleus fidelity, budget optimality, and an epistemic reading of disagreement, and we release code.


### S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information
**Authors**: Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26047v1](https://arxiv.org/pdf/2607.26047v1)

**Abstract**: Acoustic information provides rich cues about object location, material properties, and changes caused by contact or motion. This paper introduces a new set of acoustic-aware manipulation tasks for imitation learning, in which robots must use auditory cues to determine manipulation targets. These tasks require sound source localization and identification for active exploration in robotic manipulation. Also, we propose a multimodal imitation learning framework, Spatial-Spectral Audio Action (S2A2), that integrates visual features with acoustic spatial and acoustic signal information for the acoustic-aware manipulation tasks. We implemented S2A2 models that integrates policies such as ACT, Diffusion Policy, VQ-BeT, and $π_0$, into our framework. Simulation experiments showed that the proposed method is the most effective for tasks requiring both position and timbre. Furthermore, real-robot experiments confirm the applicability of the proposed tasks and framework to real-world manipulation.


### VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening
**Authors**: Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti, Abdur R. Shahid

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26042v1](https://arxiv.org/pdf/2607.26042v1)

**Abstract**: We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph manages the stateful screening workflow, including input validation, image transmission, model invocation, safety checks, conditional routing, failure handling, and structured logging. This design moves beyond static image classification by enabling the system to collect visual evidence, invoke external models, apply deterministic safety rules, and generate diagnostic-support alerts. Results show that image-only VLM prediction remains limited, whereas symptom-guided and multimodal inputs improve zero-shot classification performance. Thus, VetClaw transforms a static prediction model into a coordinated, safety-aware system that can use tools, manage workflows, handle failures, and escalate uncertain cases.


### Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?
**Authors**: Abhishek Pillai, Samir Kumar Nayak, Yuan Chen

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26041v1](https://arxiv.org/pdf/2607.26041v1)

**Abstract**: Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. Neither isolates whether a model can reconstruct the causal, task-relevant transition produced by an action- crucial for rejecting stale observations, verifying progress, and recovering from failure. This is difficult because inference, remote input, app rendering, and screenshot capture are asynchronous: the next observation may be delayed, occluded, transient, or unrelated, then misread as progress and carried into subsequent planning. We introduce Desktop-Delta Bench (DDB), an offline step-level benchmark with 2,013 human-verified instances from novel, multi-app Linux trajectories across ~15 applications and 50 task domains. DDB trajectories targets 3 failure dimensions- state verification, source tracking, and context-aware control- through 2 complementary tasks: 463 3-frame temporal-ordering instances, including 105 with a cross-trajectory decoy, and 1,550 before-after pairs labeled from 5 actions + its payload. We evaluate 8 closed and open-source model families across 32 ordering and 16 single-action settings, observing consistent gaps. Ordering remains unsaturated: best non-decoy and decoy exact-match rates are 65.1% and 65.7%. Task context improves decoy identification by 6.9 percentage points but reduces non-decoy exact match by 2.2 points; error analysis reveals systematic copying of the presented A-B-C order. Single-action results show that inferring the action family is harder than locating it: click F1 is 0.96 vs, 0.76 for drag, while recognized drags are generally localized well. DDB, thus, complements end-to-end benchmarks by filling the missing diagnostic layer between GUI grounding and final task success, enabling targeted improvements to desktop CUA verification, reliability, and recovery.


## Generation
### Pass the Baton: Trajectory-Relayed On-Policy Distillation
**Authors**: Haolei Xu, Xiaowen Xu, Haiwen Hong, Zixuan Ni, Hongxing Li, Yiwen Qiu, Weiming Lu, Yongliang Shen

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26057v1](https://arxiv.org/pdf/2607.26057v1)

**Abstract**: On-policy distillation (OPD) grounds token-level supervision in the student's own trajectory, yet suffers from prefix failure: once the student commits to a wrong reasoning direction, all subsequent generation builds on this deviation, producing misdirected continuations that elicit unreliable supervision and waste compute. We identify a teacher-student continuation asymmetry on failed prefixes, where the teacher tends to redirect while the student continues along the original direction, and convert it into a label-free handoff trigger in Relay On-Policy Distillation (Relay-OPD). During training, Relay-OPD constructs relay trajectories by letting the teacher briefly take over at detected trigger points to produce a teacher leg, after which the student resumes and is optimized on the resulting trajectory. A limited relay budget concentrates intervention on critical early positions while limiting departure from the student policy. With a Qwen3-4B-Instruct-2507 teacher and Qwen3-0.6B/1.7B-Non-Thinking students on eight mathematical reasoning benchmarks, Relay-OPD achieves the best or second-best results on every benchmark, outperforming standard OPD by +5.73% and the strongest baseline FastOPD by +1.49% on average for 1.7B, with consistent gains at 0.6B. Training trajectory length is reduced by over 50%.


### CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer
**Authors**: Ankang Yang, Jitao Zhao, Di Jin, Yuxiao Huang, Dongxiao He

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26023v1](https://arxiv.org/pdf/2607.26023v1)

**Abstract**: Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored. Existing GNN-based graph foundation models typically require downstream adaptation, whereas LLM-based graph methods mainly address unimodal graphs or tasks within a single domain. This setting presents two key challenges. First, models must generalize knowledge from individual modalities while capturing transferable cross-modal relations. Second, without target-domain fine-tuning, node representations remain entangled with domain-specific structures and modality-specific characteristics, obscuring shared concepts in unseen domains. To address these challenges, we propose CHARM, a multimodal graph foundation model with hierarchical context modeling for zero-shot transfer. CHARM replaces isolated raw nodes with hierarchical graph contexts that capture multimodal semantics and cross-modal relations. These contexts map domain-specific node patterns to shared high-level concepts, reducing reliance on target-domain supervision or adaptation. A modality-aware graph context encoder integrates multimodal information with graph structure and converts the resulting representations into graph tokens for a large language model . Experiments show consistent improvements on zero-shot multimodal graph tasks.


### MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar
**Authors**: Solomon Micheal Serunjogi, Rachmad Vidya Wicaksana Putra, Ayat Taha, Muhammad Shafique, Mahmoud Rasras

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26016v1](https://arxiv.org/pdf/2607.26016v1)

**Abstract**: Recently, photonic transformer accelerators (PTAs) have successfully achieved significant speedup and energy efficiency improvements over electronic accelerators for expediting Transformer inference. However, state-of-the-art rely on expensive multi-wavelength light generation and large dot-product units due to active phase-shifter components, thus making their approach inefficient and impractical. To address this, we propose MDTransformer, a novel hardware-software co-design of PTA based on mode-division optical dataflow and operations. Specifically, MDTransformer performs complex matrix operations using spatial-mode interference, that leverages the inverse-designed multi-mode couplers, crossings, and Mach-Zehnder IQ modulators into a compact mode-division photonic tensor core (MPTC), capable of executing matrix multiplications in the optical domain. Its each guided mode (i.e., TE0-TE3) acts as an independent computational lane, enabling four-fold parallelism-per-waveguide without spectral filtering or free-spectral-range limitations. Moreover, its coherent detection and IQ modulation jointly encode amplitude and phase, realizing complex-valued arithmetic for full-range operations in transformers. MDTransformer offers analog multiplication with sub-4-bit effective precision and inter-modal crosstalk below -30 dB. Its inverse-designed approach also offers scalable and full compatibility with single-laser continuous-wave operation at 1550 nm. Experimental results show that MDTransformer achieves 40.4% area reduction, 63.6% power saving, 40.6% energy saving, and comparable latency over the state-of-the-art PTA across different workloads (i.e., DeiT-Tiny/Small/Base and BERT-Base/Large). These results show that MDTransformer offers a practical solution for high-performance and energy-efficient transformer-based systems.


### Parallel Decoding Distillation for Fast Image and Video Generation
**Authors**: Neta Shaul, Chao Liu, Arash Vahdat, Julius Berner

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26004v1](https://arxiv.org/pdf/2607.26004v1)

**Abstract**: Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. Albeit achieving high-quality video generation, these training losses are notoriously hard to optimize and suffer from mode collapse, leading to loss of video diversity and lack of motion. In this paper, we introduce Parallel Decoding Distillation (PDD), a simplified and scalable trajectory-based distillation method for fast inference of diffusion and flow matching models. Our architecture and training procedure are compatible with any pre-trained model and support sampling with a varying number of function evaluations (NFE). PDD accelerates generation by predicting multiple denoising steps per network evaluation. Conceptually, it learns a representation of the mean velocity without regressing its derivative using JVPs or finite-difference approximations. Our method achieves SOTA performance with 4-8 NFE on LTX-2.3 Text-to-Video/Audio, Wan 14B Text-to-Video, and Qwen-Image Text-to-Image. Moreover, PDD presents a significant improvement in generated video diversity.


### Sharpness-Aware Minimization and Muon: Robustness under the Spectral Norm
**Authors**: Wenzhi Zhong, Edward Milsom, Michael Murray

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26001v1](https://arxiv.org/pdf/2607.26001v1)

**Abstract**: Sharpness-Aware Minimization (SAM) aims to improve generalization by encouraging insensitivity to small, worst-case parameter perturbations. However, the notion of a "small" perturbation is inherently geometry-dependent: while existing SAM variants have explored a wide range of choices, a clear perspective on which geometries are most effective in practice remains elusive. Recent work on matrix-aware optimization, particularly the Muon optimizer, suggests that respecting the matrix structure of hidden-layer weights can lead to strong empirical performance. Motivated by this, we study matrix-aware geometry in both stages of SAM: we introduce a layerwise spectral inner perturbation for matrix-valued hidden-layer parameters and combine it with either AdamW/SGDW or Muon in the outer update. Across ImageNet-1K experiments on ViT-Small/16 and ResNet-50, we find that the combination of a spectral inner step with a Muon outer step performs consistently strongly, achieving the best validation accuracy on both models among the evaluated methods.


### Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?
**Authors**: Farooq Shaikh

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25995v1](https://arxiv.org/pdf/2607.25995v1)

**Abstract**: Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads. Recent work suggests that large language models (LLMs) can automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings without human authoring. Such systems, however, prompt the model with each finding in isolation from the live service call graph, assuming general hardening knowledge suffices. This assumption breaks down whenever a patch must preserve a runtime service dependency invisible to the model: an otherwise compliant fix then carries a destructive functional blast radius, crashing downstream callers or silently severing call edges across the cluster. Whether live cluster context improves patch correctness has not been measured under controlled conditions across multiple dependency classes. We introduce KuTIE (Kubernetes Topology Intelligence Engine), which builds a live cluster context from Istio call edges, Trivy KSPM findings, and the service-account bindings a workload reads, and conditions LLM patch generation on it. It is evaluated on VulnCare, a purpose-built 36-deployment, four-namespace healthcare cluster with 31 injectable findings across seven dependency classes, each labelled by topology dependence against cluster ground truth. Across 248 trials, topology context raises topology-dependent patch correctness from 11.1% to 78.0% ($Δ= 0.669$), a gap that holds for every model and for six of seven classes, from credential and network-policy ($Δ= 0.95$) to role-based access control ($Δ= 0.31$); a topology-independent control exhibits no such effect ($Δ= 0.0$), isolating the result from generic prompt enrichment. Supplying the live service-call graph and the service-account bindings it exposes thus improves remediation of topology-dependent findings well beyond scanner-only context.


## VLA
### SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models
**Authors**: Zonghe Liu, Shanyuan Jie, Xiaoquan Sun, Chen Cao, Zetian Xu, Zongsheng Liu, Jiayu Chen

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25912v1](https://arxiv.org/pdf/2607.25912v1)

**Abstract**: Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion, pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment framework built upon $π_0$, using SAM3D as a frozen 3D teacher to provide target-object 3D priors during training. Specifically, we localize task-relevant objects with object recognition models, generate corresponding object masks, and use SAM3D to extract dense object-level 3D representations, which are aligned with intermediate visual features of $π_0$. This enables the policy to internalize target-object 3D information while preserving the original RGB-language-to-action inference pipeline without requiring depth, point clouds, masks, SAM3D, or additional 3D modules at test time. Simulation experiments show consistent improvements, achieving 99.1\% on LIBERO and an average length of 4.11 on CALVIN. Real-world experiments further demonstrate that our method is particularly effective in long-horizon manipulation scenarios where the robot must focus on different target objects across multiple subtasks.


### CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model
**Authors**: Minhyeok Lee, Chiyoung Kim, Chanhoe Gu, Seongrok Kim, Sanghyuk Roy Choi, Donghwan Hwang, Donghun Ryu, Seokhyun Kim

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25487v1](https://arxiv.org/pdf/2607.25487v1)

**Abstract**: Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets. We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. Three components target different axes of the problem: dual-view temporal input of 16 history frames per step with textual camera and time markers; hierarchical chain-of-thought (CoT) distillation from a 35B teacher into an episode-level Plan and a chunk-level Think span over task phase, gripper state and next subaction; and paraphrase augmentation expanding 40 base commands into 800 variants. On LIBERO-Plus, spanning 10,030 perturbed tasks across seven perturbation dimensions, CoTinyVLA reaches 90.8% on Spatial, 87.3% on Object, 86.6% on Goal and 80.7% on Long, leading the strongest 7B baseline on all four suites by 4.7, 2.8, 15.9 and 3.0 points, with every margin interval excluding zero. The gains concentrate on the hardest axes of the benchmark: across the eleven published baselines none exceeds 53.2% on Robot Initial States in any suite, whereas CoTinyVLA reaches 73.6% on Goal against 39.9% for the strongest baseline. Ablations show the three components to be separable by perturbation axis, and at a matched image budget how frames are divided between the two cameras and across time accounts for 8.6 points on its own. Closed-loop inference peaks at 2.25 GiB of allocated GPU memory, and paired interventions show the episode Plan to be load-bearing: replacing it with an empty or contradictory span costs 40 to 45 points of success. Structured supervision thus lets a 0.9B backbone exceed all of them. Code: https://github.com/BrainJellyPie/CoTinyVLA


### A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference
**Authors**: Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li, Xiaoyao Liang, Haibing Guan

**Published Date**: 2026-07-27

**Updated Date**: 2026-07-27

**PDF Url**: [2607.24148v1](https://arxiv.org/pdf/2607.24148v1)

**Abstract**: Vision-Language-Action (VLA) models have demonstrated strong potential for embodied AI, yet their high inference latency on GPUs limits real-time deployment. Existing accelerators, such as Dadu-Corki, improve efficiency but treat VLA models as full-precision workloads, leaving substantial redundancy in both memory and computation underexploited.
  In this paper, we propose VQVLA, an algorithm-hardware co-design framework that accelerates VLA inference by exploiting weight similarity and execution dynamics. We first introduce MotionVQ, a motion-aware vector quantization scheme that dynamically adjusts quantization precision based on the robot's execution state, reducing memory access while preserving task success rate. We then propose a merged-centroid vectorized GEMM paradigm that operates on the codebook-index representation, eliminating redundant multiplications through spatial aggregation and temporal reuse of centroids. To realize these optimizations, we design an accelerator that efficiently supports dynamic precision selection and centroid-reuse computation. Experimental results show that VQVLA achieves 6.5x, 2.8x, 1.9x, 3.3x, and 4.3x speedup over the A100 GPU, Dadu-Corki, LUT-DLA, CodeGEMM, and ShiftAddLLM, respectively, with negligible accuracy degradation.


### MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents
**Authors**: Belal S. Alsinglawi, Weizheng Wang, Junyi Wu, Yi Jiang, Lianhai Lin, Merouane Debbah, Izzat Alsmadi

**Published Date**: 2026-07-26

**Updated Date**: 2026-07-26

**PDF Url**: [2607.23870v1](https://arxiv.org/pdf/2607.23870v1)

**Abstract**: Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. We introduce MulRobBench, an offline, protocol-conditioned benchmark for Vision-Language-Action (VLA) UAV agents in smart-city environments. MulRobBench integrates real UAV multimodal observations, protocol-level security policies, and action-level cyber-physical safety into a unified evaluation framework. The benchmark contains 3,024 samples spanning 17 task taxonomy nodes and 12 scoring dimensions across four stages: operational context understanding, multimodal evidence arbitration, degradation-aware reasoning, and risk-aware action planning. Evaluation combines semantic scoring with structural diagnostics, including policy compliance, format compliance, unsafe actions, parsing failures, and dimension-level validity. Across 17 multimodal models, the best semantic protocol-decision score reaches only 0.5141, while the best strict mean scoring-dimension accuracy is 0.1599. A controlled 20-anchor modality-ablation study changes 4-15 action selections per model, confirming that both visual and textual inputs influence decisions. Analysis identifies modality-trust selection, constraint extraction, glare, missing data, and operator shorthand as the primary causes of decision instability. MulRobBench provides a reproducible benchmark for trustworthy multimodal UAV decision making under realistic operational constraints.


### A Few Words Go a Long Way: Language Guided Robot Policy Synthesis
**Authors**: Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray, Nick Walker, Maya Cakmak

**Published Date**: 2026-07-26

**Updated Date**: 2026-07-26

**PDF Url**: [2607.23784v1](https://arxiv.org/pdf/2607.23784v1)

**Abstract**: While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages the reasoning capabilities of LLM coding agents to synthesize modular robot programs that utilize a suite of perception and control tools. Unlike end-to-end models where distribution shift leads to unpredictable, cascading failures, our modular architecture allows users to isolate failures and localize feedback at the level of abstraction required. We introduce an iterative process where a human supervisor provides natural language corrections to steer the policy. These corrections are grounded in the policy code by program execution traces and distilled into a persistent skill library, a form of long-term in-context learning which enables the agent to accumulate a repertoire of reusable, interpretable behaviors. In a benchmark evaluation on a Franka Panda robot, ARCHITECT outperforms state-of-the-art VLA models and program synthesis baselines on complex, long-horizon tasks, including articulated object manipulation and cloth folding. Our results demonstrate that the synthesized skill library enables the system to transfer to novel tasks with decreasing human intervention, providing a steerable and data-efficient alternative to black-box robot learning. Website: https://robo-architect.github.io/


### Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline
**Authors**: Qing Yang, Xun Wang, Ziguan Wang, Zhenjiang Li, Hongqiang Wang, Dongdong Weng

**Published Date**: 2026-07-25

**Updated Date**: 2026-07-25

**PDF Url**: [2607.22997v1](https://arxiv.org/pdf/2607.22997v1)

**Abstract**: Physical AI -- the integration of large vision-language-action (VLA) models with embodied agents that act in the real world -- has emerged as the next major frontier for AI, echoed by industry leaders such as Jensen Huang (``the next big thing is Physical AI, AI with a body,'' GTC Paris, June 2025) and Dr. Lisa Su (`we're entering the world of Physical AI ... this is where AI enters the real world,' CES 2026). This paper presents an end-to-end, fully AMD-accelerated technology stack for embodied manipulation, spanning data-center training silicon, Radeon PRO simulation/rendering GPUs, and Ryzen AI edge compute, unified by the open ROCm software stack. We demonstrate that training and deploying VLA-based manipulation policies does not require a CUDA-locked ecosystem. Four progressive demonstrations are presented: (1) a Sim-to-Real manipulation pipeline trained with SmolVLA and deployed on a physical Franka arm; (2) a semantic, language-grounded object-selection task (`one-of-three'); (3) a Real2Sim synthetic-data generation pipeline that fuses 3D Gaussian Splatting (3DGS) reconstructions of real scenes with the Genesis physics engine; and (4) large-scale reinforcement learning for quadruped and humanoid locomotion benchmarked across multiple hardware platforms. All pipelines run natively on ROCm + PyTorch on RDNA4 (Radeon AI PRO R9700) and RDNA3.5 (Radeon PRO W7900) hardware and are reproducible on the free Radeon Cloud Platform.


## Agent
### Pictura: Perspective-View Self-Play at Scale for Driving
**Authors**: Yuan Yin, Elias Ramzi, Marc Lafon, Valentin Charraut, Victor Bares, Yihong Xu, Éloi Zablocki, Alexandre Boulch, Thibault Buhet, Andrei Bursuc, Matthieu Cord

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.26005v1](https://arxiv.org/pdf/2607.26005v1)

**Abstract**: Self-play in simulation produces robust driving policies at scale. Demonstrations of such behavior have been made using privileged vectorized observations such as exact poses and velocities, even for occluded agents. This assumes that perception is solved and introduces a representation gap with the partial observation of a deployed agent driving from the perspective view of egocentric cameras. A common fix, distilling the privileged policy into a camera-input student, leaves the student imitating decisions its own view cannot justify. Instead, we establish perspective-view self-play as a practical training regime. We introduce Pictura, a GPU-accelerated multi-agent driving simulator that renders each agent's egocentric view at every step, mitigating the representation gap at its source. Pictura sustains up to 500K agent-steps/s (2M images/s) on a single H100. Using Pictura, we train Alberti by self-play with plain PPO. It is the first large-scale driving self-play policy trained directly from perspective images, without privileged observations. Training spans 50B agent steps for ~35M km of driving. It approaches the driving performance of its privileged vectorized counterpart, and transfers zero-shot to Waymo Open Motion Dataset layouts re-rendered in Pictura, where it outperforms privileged vectorized agents. Project page: https://valeoai.github.io/Pictura/


### MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents
**Authors**: Shuyue Wei, Chang Liu, Zimu Zhou, Yongxin Tong, Lizhen Cui

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25992v1](https://arxiv.org/pdf/2607.25992v1)

**Abstract**: Recently, memory management has become a key infrastructure for LLM-based agents, as it directly affects long-horizon reasoning, personalized responses, and knowledge reuse. However, existing LLM memory systems typically adopt a coarse-grained (utility-agnostic) manner that treats heterogeneous user-LLM interaction records uniformly, leading to redundant and low-impact records persisting in the memory repository. To address this challenge, we present MemLens, a value-aware memory management system that takes memory records as first-class data objects. MemLens provides an end-to-end interactive analytics dashboard that exposes the complete memory lifecycle, including Shapley-style memory evaluation, value-aware storage, and memory-assisted response. Through a study-copilot application, the system enables users to inspect memory values, visualize hierarchical memory structures, and compare various memory management strategies in terms of response quality, retrieval latency, and token consumption. Therefore, our MemLens can serve as an efficient, interpretable, and personalized long-term memory management system for LLM-based agents.


### Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA
**Authors**: Carlos Celemin, Benedict Wilkins, Adrián Barahona-Ríos, Saman Zadtootaghaj, Nabajeet Barman

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25921v1](https://arxiv.org/pdf/2607.25921v1)

**Abstract**: In this work, we study the use of Vision-Language Models (VLMs) for anomaly detection in an agent-driven game Quality Assurance (QA) pipeline focusing on geometry clipping. In this evaluation, a custom exploration agent navigates a game level to collect visual observations, while the automatic annotation pipeline provides frame-level clipping labels. This setup allows us to evaluate recent VLMs on a controlled anomaly detection task without manual annotation. We benchmark six recent VLMs (Gemini, GPT, Qwen, Gemma, Llama, and Ministral) under a zero-shot prompting setting and analyse their sensitivity to four prompt variants.
  Our results show that while the VLMs can capture visual cues associated with geometry clipping, they all produce substantial false positives on visually ambiguous frames such as near-contact geometry and partial occlusions. Gemini-3.1-Flash achieves the best overall accuracy and is the most robust to prompt variation, while open-source models exhibit large precision--recall swings depending on the prompt design. These findings suggest that current VLMs are best suited as high-recall candidate filters within multi-stage QA pipelines rather than as standalone bug detectors.


### Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks
**Authors**: Ravi Kant Sharma, Ashutosh Uttam, Ajay Kumar

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25914v1](https://arxiv.org/pdf/2607.25914v1)

**Abstract**: Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management. The model comprises: a formally defined trust state machine with provable graduated enforcement, damped cascade propagation with bounded convergence, cross-vendor trust notifications via existing Management Services (MnS) interfaces, and retroactive impact assessment through NRM dependency graph traversal. Simulation-based evaluation across multi-vendor topologies shows that standardized cross-vendor notifications reduce blast radius from hours-scale undetected propagation to near-real-time containment bounded by MnS notification delivery, with cascade convergence guaranteed in bounded iterations and sub-linear notification scaling across vendor domains. The framework operates within existing 3GPP management infrastructure, leverages existing protocols, and provides a standardization pathway for trustworthy multi-vendor autonomous network management.


### Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification
**Authors**: Chenrui Shi, Yuwei Wu, Yang Liu, Ruining Feng, Zirui Shang, Zhi Gao, Lifeng Fan, Che Sun

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25904v1](https://arxiv.org/pdf/2607.25904v1)

**Abstract**: Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction. Automated GUI task evaluation has received increasing attention because the evaluation results can serve as reward signals for both test-time scaling and post-training. However, reliable GUI task evaluation remains challenging because the judgments often require access to environment states, such as system configurations, file data, and application settings, beyond the screenshots of execution trajectories. In this paper, we propose an interactive reward agent (IRA) based on a propose-then-verify framework to acquire and verify evidence from the post-execution environment. Given a task instruction and a GUI environment after the GUI agent execution, IRA first proposes the task completion conditions and then verifies them by invoking system tools, application tools, and GUI tools. This design combines evidence from both visible interfaces and the environment state in an interactive process. We further introduce GUI-RewardBench, a benchmark of 321 GUI task trajectories spanning 10 Ubuntu desktop application categories. Experiments show that IRA achieves 86.9% accuracy on GUI-RewardBench, outperforming existing evaluator baselines. We further apply IRA to reinforcement learning of GUI agents, achieving a 34.0% OSWorld success rate, which demonstrates that IRA can provide effective reward signals for training GUI agents.


### Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation
**Authors**: Stefan Krsteski, Charlotte Meyer, Guillaume Allegre, Tony O'Halloran, Alexandre Sallinen

**Published Date**: 2026-07-28

**Updated Date**: 2026-07-28

**PDF Url**: [2607.25891v1](https://arxiv.org/pdf/2607.25891v1)

**Abstract**: Evaluating AI agents in interactive environments is hindered by fragmented tasks, scaffolds, verifiers, and scoring rules. Existing efforts focus on narrow settings, remain limited in scale, or require costly reruns, leaving much of the empirical record incomparable. We introduce Messier, a unified corpus of 957,253 records that span 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers. Messier consolidates public benchmark scores and supplements them with five-agent runs across six underrepresented professional and scientific domains, including a recent legal benchmark. Each record is standardized by model, scaffold, environment, task, verifier, and aggregation rule, with SOC/NAICS classifications for occupational and industry analysis. Using this corpus, we show frontier progress is uneven across benchmark types, with "function calling" saturated, "programming" improving the fastest, and "enterprise workflows" remaining the most challenging. Furthermore, counterfactual rescoring shows that strict all-pass aggregation in multi-verifier tasks can obscure progress and artificially alter agent rankings. From these standardized records, we derive capability scales that align with Epoch's Evaluation Capability Index rankings at Spearman \r{ho} = 0.81 and can be specialized by domain, occupation, action space, or verifier type. Messier provides a foundational, reusable infrastructure for agent capability scaling, benchmark auditing, and fine-grained analysis of evaluation failures.


