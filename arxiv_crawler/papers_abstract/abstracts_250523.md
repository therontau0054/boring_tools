# Abstracts of Papers

## Physics
### A Unified Framework for Simultaneous Parameter and Function Discovery in Differential Equations
**Authors**: Shalev Manor, Mohammad Kohandel

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16996v1](http://arxiv.org/pdf/2505.16996v1)

**Abstract**: Inverse problems involving differential equations often require identifying
unknown parameters or functions from data. Existing approaches, such as
Physics-Informed Neural Networks (PINNs), Universal Differential Equations
(UDEs) and Universal Physics-Informed Neural Networks (UPINNs), are effective
at isolating either parameters or functions but can face challenges when
applied simultaneously due to solution non-uniqueness. In this work, we
introduce a framework that addresses these limitations by establishing
conditions under which unique solutions can be guaranteed. To illustrate, we
apply it to examples from biological systems and ecological dynamics,
demonstrating accurate and interpretable results. Our approach significantly
enhances the potential of machine learning techniques in modeling complex
systems in science and engineering.


### PICT -- A Differentiable, GPU-Accelerated Multi-Block PISO Solver for Simulation-Coupled Learning Tasks in Fluid Dynamics
**Authors**: Aleksandra Franz, Hao Wei, Luca Guastoni, Nils Thuerey

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16992v1](http://arxiv.org/pdf/2505.16992v1)

**Abstract**: Despite decades of advancements, the simulation of fluids remains one of the
most challenging areas of in scientific computing. Supported by the necessity
of gradient information in deep learning, differentiable simulators have
emerged as an effective tool for optimization and learning in physics
simulations. In this work, we present our fluid simulator PICT, a
differentiable pressure-implicit solver coded in PyTorch with
Graphics-processing-unit (GPU) support. We first verify the accuracy of both
the forward simulation and our derived gradients in various established
benchmarks like lid-driven cavities and turbulent channel flows before we show
that the gradients provided by our solver can be used to learn complicated
turbulence models in 2D and 3D. We apply both supervised and unsupervised
training regimes using physical priors to match flow statistics. In particular,
we learn a stable sub-grid scale (SGS) model for a 3D turbulent channel flow
purely based on reference statistics. The low-resolution corrector trained with
our solver runs substantially faster than the highly resolved references, while
keeping or even surpassing their accuracy. Finally, we give additional insights
into the physical interpretation of different solver gradients, and motivate a
physically informed regularization technique. To ensure that the full potential
of PICT can be leveraged, it is published as open source:
https://github.com/tum-pbs/PICT.


### Attached Decelerating Turbulent Boundary Layers over Riblets
**Authors**: Benjamin S. Savino, Amirreza Rouhi, Wen Wu

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16962v1](http://arxiv.org/pdf/2505.16962v1)

**Abstract**: Turbulent boundary layers over riblets subjected to adverse pressure
gradients (APGs) are investigated by direct numerical simulation. Multiple APG
strengths and riblet sizes are examined, permitting evaluation of drag
modification by riblets, and associated physical mechanisms, in various regimes
established for zero-pressure-gradient (ZPG) riblet flows. The APG strengths
are selected such that the flow remains attached. It is found that during APGs,
riblets reduce drag beyond what has been achieved in ZPG flows. In extreme
cases, an upstream force (i.e., negative drag) is attained. The significant
drag reduction is found to be a product of Kelvin-Helmholtz roller vortices
forming near the riblet crest, which are augmented in size, strength, and
frequency during the APG. The preliminary results reported here indicate the
need to modify existing metrics to predict drag reduction and the onset of KH
rollers by riblets when the pressure gradient is non-negligible. Further
analysis will be documented in the final paper.


### Predicting the outcome of collisional neutrino flavor conversion
**Authors**: Julien Froustey

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16961v1](http://arxiv.org/pdf/2505.16961v1)

**Abstract**: Collisional flavor instabilities, driven by differing neutrino and
antineutrino reaction rates, are expected to occur in dense astrophysical
environments like supernovae and neutron star mergers, but have yet to be
incorporated in large-scale simulations. We derive, for the first time,
analytical expressions for the asymptotic state resulting from a homogeneous
and isotropic instability, and apply these predictions to two representative
conditions from a neutron star merger simulation. We emphasize the importance
of using a collision term that allows for both damping of flavor coherence and
relaxation back to thermal equilibrium, which leads to a "quantum" equilibrium
with nonzero coherence. These results can be implemented in a subgrid model of
collisional flavor transformation, an important step toward the inclusion of
flavor oscillation physics into global simulations.


### Higher order Jacobi method for solving a system of linear equations
**Authors**: Nithin Kumar Goona, Lama Tarsissi

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16906v1](http://arxiv.org/pdf/2505.16906v1)

**Abstract**: This work proposes a higher-order iterative framework for solving matrix
equations, inspired by the structure and functionality of neural networks. A
modification of the classical Jacobi method is introduced to compute
higher-order coefficient matrices through matrix-matrix multiplications. The
resulting method, termed the higher-order Jacobi method, structurally resembles
a shallow linear network and allows direct computation of the inverse of the
coefficient matrix. Building on this, an iterative scheme is developed that,
once the network parameters are determined for a known system, enables
efficient resolution of system variations without re-computing the
coefficients. This iterative process naturally assumes the form of a deep
recurrent neural network. The proposed approach moves beyond conventional
Physics-Informed Neural Networks (PINNs) by providing an explicit,
training-free definition of network parameters rooted in physical and
mathematical formulations. Computational analysis demonstrates improved order
of complexity, suggesting a promising direction for algorithmic efficiency in
solving linear systems. This methodology opens avenues for interpretable and
scalable solutions to physically motivated problems in computational science.


### Accurate crystal field Hamiltonians of single-ion magnets at mean-field cost
**Authors**: Linqing Peng, Shuanglong Liu, Xing Zhang, Xiao Chen, Chenghan Li, Hai-Ping Cheng, Garnet Kin-Lic Chan

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16905v1](http://arxiv.org/pdf/2505.16905v1)

**Abstract**: The effective crystal field Hamiltonian provides the key description of the
electronic properties of single-ion magnets, but obtaining its parameters from
ab initio computation is challenging. We introduce a simple approach to derive
the effective crystal field Hamiltonian through density functional calculations
of randomly rotated mean-field states within the low-energy manifold. In
benchmarks on five lanthanide-based complexes, we find that we compute with
mean-field cost an effective crystal field Hamiltonian that matches the
state-of-the-art from much more expensive multi-configurational quantum
chemistry methods. In addition, we are able to reproduce the experimental
low-energy spectrum and magnetic properties with an accuracy exceeding prior
attempts. Due to its low cost, our approach provides a crucial ingredient in
the computational design of single-ion magnets with tailored physical
properties and low-energy spectra.


### Structure-Aligned Protein Language Model
**Authors**: Can Chen, David Heurtel-Depeiges, Robert M. Vernon, Christopher James Langmead, Yoshua Bengio, Quentin Fournier

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16896v1](http://arxiv.org/pdf/2505.16896v1)

**Abstract**: Protein language models (pLMs) pre-trained on vast protein sequence databases
excel at various downstream tasks but lack the structural knowledge essential
for many biological applications. To address this, we integrate structural
insights from pre-trained protein graph neural networks (pGNNs) into pLMs
through a latent-level contrastive learning task. This task aligns residue
representations from pLMs with those from pGNNs across multiple proteins,
enriching pLMs with inter-protein structural knowledge. Additionally, we
incorporate a physical-level task that infuses intra-protein structural
knowledge by optimizing pLMs to predict structural tokens. The proposed
dual-task framework effectively incorporates both inter-protein and
intra-protein structural knowledge into pLMs. Given the variability in the
quality of protein structures in PDB, we further introduce a residue loss
selection module, which uses a small model trained on high-quality structures
to select reliable yet challenging residue losses for the pLM to learn.
Applying our structure alignment method to the state-of-the-art ESM2 and
AMPLIFY results in notable performance gains across a wide range of tasks,
including a 12.7% increase in ESM2 contact prediction. The data, code, and
resulting SaESM2 and SaAMPLIFY models will be released on Hugging Face.


### Quantum Compiler Design for Qubit Mapping and Routing: A Cross-Architectural Survey of Superconducting, Trapped-Ion, and Neutral Atom Systems
**Authors**: Chenghong Zhu, Xian Wu, Zhaohui Yang, Jingbo Wang, Anbang Wu, Shenggen Zheng, Xin Wang

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16891v1](http://arxiv.org/pdf/2505.16891v1)

**Abstract**: Quantum hardware development is progressing rapidly with substantial
advancements achieved across leading platforms, including superconducting
circuits, trapped-ion systems, and neutral atom arrays. As the pursuit of
practical quantum advantage continues, efficient quantum program compilation
becomes essential for transforming high-level representations of quantum
algorithms into physically executable circuits. A fundamental challenge in this
process is qubit mapping and gate scheduling, which play a critical role in
adapting compiled circuits to the architectural constraints and physical
limitations of specific quantum hardware. In this survey, we systematically
review and categorize research on the qubit mapping and routing problems across
the three mainstream quantum hardware platforms. We primarily explore the
development of hardware-aware compilers for superconducting platforms,
classifying existing methods into solver-based, heuristic-based, and machine
learning-based approaches, and analyze their optimization targets, including
gate count, circuit duration, fidelity, and scalability. Furthermore, we
examine the evolution of trapped-ion and neutral atom devices, analyzing the
distinct challenges posed by their hardware characteristics and highlighting
specialized compilers tailored to these unique physical constraints. Finally,
we summarize the key challenges and identify some promising opportunities for
future research in quantum compiler design across these hardware platforms.


### How high is `high'? Rethinking the roles of dimensionality in topological data analysis and manifold learning
**Authors**: Hannah Sansford, Nick Whiteley, Patrick Rubin-Delanchy

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16879v1](http://arxiv.org/pdf/2505.16879v1)

**Abstract**: We present a generalised Hanson-Wright inequality and use it to establish new
statistical insights into the geometry of data point-clouds. In the setting of
a general random function model of data, we clarify the roles played by three
notions of dimensionality: ambient intrinsic dimension $p_{\mathrm{int}}$,
which measures total variability across orthogonal feature directions;
correlation rank, which measures functional complexity across samples; and
latent intrinsic dimension, which is the dimension of manifold structure hidden
in data. Our analysis shows that in order for persistence diagrams to reveal
latent homology and for manifold structure to emerge it is sufficient that
$p_{\mathrm{int}}\gg \log n$, where $n$ is the sample size. Informed by these
theoretical perspectives, we revisit the ground-breaking neuroscience discovery
of toroidal structure in grid-cell activity made by Gardner et al. (Nature,
2022): our findings reveal, for the first time, evidence that this structure is
in fact isometric to physical space, meaning that grid cell activity conveys a
geometrically faithful representation of the real world.


### Magnetic vortex writing and local reversal seeding in artificial spin-vortex ice via all-optical and surface-probe control
**Authors**: Holly Holder, Jack C. Gartside, Alex Vanstone, Troy Dion, Xiaofei Xiao, Kilian D. Stenning, Tingjun Zheng, Daniel Bromley, Tobias Farchy, Rupert F. Oulton, Will R. Branford

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16874v1](http://arxiv.org/pdf/2505.16874v1)

**Abstract**: Artificial spin-vortex ice ('ASVI') is a reconfigurable nanomagnetic
metamaterial consisting of magnetic nanoislands tailored to support both Ising
macrospin and vortex textures. ASVI has recently shown functional applications
including reconfigurable magnonics and neuromorphic computing, where the
introduction of vortex textures broadens functionality beyond conventional
artificial spin ice which generally supports macrospin states. However, local
control of writing vortex states in ASVI remains an open challenge. Here we
demonstrate techniques for field-free magnetic vortex writing in ASVI. We
expand ASVI to support metastable macrospin, single-vortex and double-vortex
states. All-optical writing via focused laser illumination can locally write
double-vortex textures, and surface-probe writing using an MFM tip can locally
write single vortex states. We leverage this writing to tailor and explore the
reconfigurable energy landscape of ASVI, demonstrating programmable local
seeding of avalanche-like reversal events. The global field-free texture
selective writing techniques reported here expand the suite of nanomagnetic
control techniques, with a host of future applications including fundamental
studies of avalanche dynamics, physical memory, and direct writing of
nanomagnetic 'weights' in physical neuromorphic neural networks.


## Diffusion
### When Are Concepts Erased From Diffusion Models?
**Authors**: Kevin Lu, Nicky Kriplani, Rohit Gandikota, Minh Pham, David Bau, Chinmay Hegde, Niv Cohen

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.17013v1](http://arxiv.org/pdf/2505.17013v1)

**Abstract**: Concept erasure, the ability to selectively prevent a model from generating
specific concepts, has attracted growing interest, with various approaches
emerging to address the challenge. However, it remains unclear how thoroughly
these methods erase the target concept. We begin by proposing two conceptual
models for the erasure mechanism in diffusion models: (i) reducing the
likelihood of generating the target concept, and (ii) interfering with the
model's internal guidance mechanisms. To thoroughly assess whether a concept
has been truly erased from the model, we introduce a suite of independent
evaluations. Our evaluation framework includes adversarial attacks, novel
probing techniques, and analysis of the model's alternative generations in
place of the erased concept. Our results shed light on the tension between
minimizing side effects and maintaining robustness to adversarial prompts.
Broadly, our work underlines the importance of comprehensive evaluation for
erasure in diffusion models.


### Guided Diffusion Sampling on Function Spaces with Applications to PDEs
**Authors**: Jiachen Yao, Abbas Mammadov, Julius Berner, Gavin Kerrigan, Jong Chul Ye, Kamyar Azizzadenesheli, Anima Anandkumar

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.17004v1](http://arxiv.org/pdf/2505.17004v1)

**Abstract**: We propose a general framework for conditional sampling in PDE-based inverse
problems, targeting the recovery of whole solutions from extremely sparse or
noisy measurements. This is accomplished by a function-space diffusion model
and plug-and-play guidance for conditioning. Our method first trains an
unconditional discretization-agnostic denoising model using neural operator
architectures. At inference, we refine the samples to satisfy sparse
observation data via a gradient-based guidance mechanism. Through rigorous
mathematical analysis, we extend Tweedie's formula to infinite-dimensional
Hilbert spaces, providing the theoretical foundation for our posterior sampling
approach. Our method (FunDPS) accurately captures posterior distributions in
function spaces under minimal supervision and severe data scarcity. Across five
PDE tasks with only 3% observation, our method achieves an average 32% accuracy
improvement over state-of-the-art fixed-resolution diffusion baselines while
reducing sampling steps by 4x. Furthermore, multi-resolution fine-tuning
ensures strong cross-resolution generalizability. To the best of our knowledge,
this is the first diffusion-based framework to operate independently of
discretization, offering a practical and flexible solution for forward and
inverse problems in the context of PDEs. Code is available at
https://github.com/neuraloperator/FunDPS


### Bigger Isn't Always Memorizing: Early Stopping Overparameterized Diffusion Models
**Authors**: Alessandro Favero, Antonio Sclocchi, Matthieu Wyart

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16959v1](http://arxiv.org/pdf/2505.16959v1)

**Abstract**: Diffusion probabilistic models have become a cornerstone of modern generative
AI, yet the mechanisms underlying their generalization remain poorly
understood. In fact, if these models were perfectly minimizing their training
loss, they would just generate data belonging to their training set, i.e.,
memorize, as empirically found in the overparameterized regime. We revisit this
view by showing that, in highly overparameterized diffusion models,
generalization in natural data domains is progressively achieved during
training before the onset of memorization. Our results, ranging from image to
language diffusion models, systematically support the empirical law that
memorization time is proportional to the dataset size. Generalization vs.
memorization is then best understood as a competition between time scales. We
show that this phenomenology is recovered in diffusion models learning a simple
probabilistic context-free grammar with random rules, where generalization
corresponds to the hierarchical acquisition of deeper grammar rules as training
time grows, and the generalization cost of early stopping can be characterized.
We summarize these results in a phase diagram. Overall, our results support
that a principled early-stopping criterion - scaling with dataset size - can
effectively optimize generalization while avoiding memorization, with direct
implications for hyperparameter transfer and privacy-sensitive applications.


### LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning
**Authors**: Zebin You, Shen Nie, Xiaolu Zhang, Jun Hu, Jun Zhou, Zhiwu Lu, Ji-Rong Wen, Chongxuan Li

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16933v1](http://arxiv.org/pdf/2505.16933v1)

**Abstract**: In this work, we introduce LLaDA-V, a purely diffusion-based Multimodal Large
Language Model (MLLM) that integrates visual instruction tuning with masked
diffusion models, representing a departure from the autoregressive paradigms
dominant in current multimodal approaches. Built upon LLaDA, a representative
large language diffusion model, LLaDA-V incorporates a vision encoder and MLP
connector that projects visual features into the language embedding space,
enabling effective multimodal alignment. Our empirical investigation reveals
several intriguing results: First, LLaDA-V demonstrates promising multimodal
performance despite its language model being weaker on purely textual tasks
than counterparts like LLaMA3-8B and Qwen2-7B. When trained on the same
instruction data, LLaDA-V is highly competitive to LLaMA3-V across multimodal
tasks with better data scalability. It also narrows the performance gap to
Qwen2-VL, suggesting the effectiveness of its architecture for multimodal
tasks. Second, LLaDA-V achieves state-of-the-art performance in multimodal
understanding compared to existing hybrid autoregressive-diffusion and purely
diffusion-based MLLMs. Our findings suggest that large language diffusion
models show promise in multimodal contexts and warrant further investigation in
future research. Project page and codes:
https://ml-gsai.github.io/LLaDA-V-demo/.


### T2I-ConBench: Text-to-Image Benchmark for Continual Post-training
**Authors**: Zhehao Huang, Yuhang Liu, Yixin Lou, Zhengbao He, Mingzhen He, Wenxing Zhou, Tao Li, Kehan Li, Zeyi Huang, Xiaolin Huang

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16875v1](http://arxiv.org/pdf/2505.16875v1)

**Abstract**: Continual post-training adapts a single text-to-image diffusion model to
learn new tasks without incurring the cost of separate models, but naive
post-training causes forgetting of pretrained knowledge and undermines
zero-shot compositionality. We observe that the absence of a standardized
evaluation protocol hampers related research for continual post-training. To
address this, we introduce T2I-ConBench, a unified benchmark for continual
post-training of text-to-image models. T2I-ConBench focuses on two practical
scenarios, item customization and domain enhancement, and analyzes four
dimensions: (1) retention of generality, (2) target-task performance, (3)
catastrophic forgetting, and (4) cross-task generalization. It combines
automated metrics, human-preference modeling, and vision-language QA for
comprehensive assessment. We benchmark ten representative methods across three
realistic task sequences and find that no approach excels on all fronts. Even
joint "oracle" training does not succeed for every task, and cross-task
generalization remains unsolved. We release all datasets, code, and evaluation
tools to accelerate research in continual post-training for text-to-image
models.


## Quantitative Finance
### Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study
**Authors**: Yuke Zhang

**Published Date**: 2025-05-22

**Updated Date**: 2025-05-22

**PDF Url**: [2505.16136v1](http://arxiv.org/pdf/2505.16136v1)

**Abstract**: This study introduces an interpretable machine learning (ML) framework to
extract macroeconomic alpha from global news sentiment. We process the Global
Database of Events, Language, and Tone (GDELT) Project's worldwide news feed
using FinBERT -- a Bidirectional Encoder Representations from Transformers
(BERT) based model pretrained on finance-specific language -- to construct
daily sentiment indices incorporating mean tone, dispersion, and event impact.
These indices drive an XGBoost classifier, benchmarked against logistic
regression, to predict next-day returns for EUR/USD, USD/JPY, and 10-year U.S.
Treasury futures (ZN). Rigorous out-of-sample (OOS) backtesting (5-fold
expanding-window cross-validation, OOS period: c. 2017-April 2025) demonstrates
exceptional, cost-adjusted performance for the XGBoost strategy: Sharpe ratios
achieve 5.87 (EUR/USD), 4.65 (USD/JPY), and 4.65 (Treasuries), with respective
compound annual growth rates (CAGRs) exceeding 50% in Foreign Exchange (FX) and
22% in bonds. Shapley Additive Explanations (SHAP) affirm that sentiment
dispersion and article impact are key predictive features. Our findings
establish that integrating domain-specific Natural Language Processing (NLP)
with interpretable ML offers a potent and explainable source of macro alpha.


### Automate Strategy Finding with LLM in Quant Investment
**Authors**: Zhizhuo Kou, Holam Yu, Junyu Luo, Jingshu Peng, Xujia Li, Chengzhong Liu, Juntao Dai, Lei Chen, Sirui Han, Yike Guo

**Published Date**: 2024-09-10

**Updated Date**: 2025-05-21

**PDF Url**: [2409.06289v3](http://arxiv.org/pdf/2409.06289v3)

**Abstract**: We present a novel three-stage framework leveraging Large Language Models
(LLMs) within a risk-aware multi-agent system for automate strategy finding in
quantitative finance. Our approach addresses the brittleness of traditional
deep learning models in financial applications by: employing prompt-engineered
LLMs to generate executable alpha factor candidates across diverse financial
data, implementing multimodal agent-based evaluation that filters factors based
on market status, predictive quality while maintaining category balance, and
deploying dynamic weight optimization that adapts to market conditions.
Experimental results demonstrate the robust performance of the strategy in
Chinese & US market regimes compared to established benchmarks. Our work
extends LLMs capabilities to quantitative trading, providing a scalable
architecture for financial signal extraction and portfolio construction. The
overall framework significantly outperforms all benchmarks with 53.17%
cumulative return on SSE50 (Jan 2023 to Jan 2024), demonstrating superior
risk-adjusted performance and downside protection on the market.


### R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization
**Authors**: Yuante Li, Xu Yang, Xiao Yang, Minrui Xu, Xisen Wang, Weiqing Liu, Jiang Bian

**Published Date**: 2025-05-21

**Updated Date**: 2025-05-21

**PDF Url**: [2505.15155v1](http://arxiv.org/pdf/2505.15155v1)

**Abstract**: Financial markets pose fundamental challenges for asset return prediction due
to their high dimensionality, non-stationarity, and persistent volatility.
Despite advances in large language models and multi-agent systems, current
quantitative research pipelines suffer from limited automation, weak
interpretability, and fragmented coordination across key components such as
factor mining and model innovation. In this paper, we propose R&D-Agent for
Quantitative Finance, in short RD-Agent(Q), the first data-centric multi-agent
framework designed to automate the full-stack research and development of
quantitative strategies via coordinated factor-model co-optimization.
RD-Agent(Q) decomposes the quant process into two iterative stages: a Research
stage that dynamically sets goal-aligned prompts, formulates hypotheses based
on domain priors, and maps them to concrete tasks, and a Development stage that
employs a code-generation agent, Co-STEER, to implement task-specific code,
which is then executed in real-market backtests. The two stages are connected
through a feedback stage that thoroughly evaluates experimental outcomes and
informs subsequent iterations, with a multi-armed bandit scheduler for adaptive
direction selection. Empirically, RD-Agent(Q) achieves up to 2X higher
annualized returns than classical factor libraries using 70% fewer factors, and
outperforms state-of-the-art deep time-series models on real markets. Its joint
factor-model optimization delivers a strong balance between predictive accuracy
and strategy robustness. Our code is available at:
https://github.com/microsoft/RD-Agent.


