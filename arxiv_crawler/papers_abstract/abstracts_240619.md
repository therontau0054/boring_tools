# Abstracts of Papers

## Neural Approximate Mirror Maps for Constrained Diffusion Models
**Authors**: Berthy T. Feng, Ricardo Baptista, Katherine L. Bouman

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12816v1](http://arxiv.org/pdf/2406.12816v1)

**Abstract**: Diffusion models excel at creating visually-convincing images, but they often
struggle to meet subtle constraints inherent in the training data. Such
constraints could be physics-based (e.g., satisfying a PDE), geometric (e.g.,
respecting symmetry), or semantic (e.g., including a particular number of
objects). When the training data all satisfy a certain constraint, enforcing
this constraint on a diffusion model not only improves its
distribution-matching accuracy but also makes it more reliable for generating
valid synthetic data and solving constrained inverse problems. However,
existing methods for constrained diffusion models are inflexible with different
types of constraints. Recent work proposed to learn mirror diffusion models
(MDMs) in an unconstrained space defined by a mirror map and to impose the
constraint with an inverse mirror map, but analytical mirror maps are
challenging to derive for complex constraints. We propose neural approximate
mirror maps (NAMMs) for general constraints. Our approach only requires a
differentiable distance function from the constraint set. We learn an
approximate mirror map that pushes data into an unconstrained space and a
corresponding approximate inverse that maps data back to the constraint set. A
generative model, such as an MDM, can then be trained in the learned mirror
space and its samples restored to the constraint set by the inverse map. We
validate our approach on a variety of constraints, showing that compared to an
unconstrained diffusion model, a NAMM-based MDM substantially improves
constraint satisfaction. We also demonstrate how existing diffusion-based
inverse-problem solvers can be easily applied in the learned mirror space to
solve constrained inverse problems.


## Predicting the energetic proton flux with a machine learning regression algorithm
**Authors**: Mirko Stumpo, Monica Laurenza, Simone Benella, Maria Federica Marcucci

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12730v1](http://arxiv.org/pdf/2406.12730v1)

**Abstract**: The need of real-time of monitoring and alerting systems for Space Weather
hazards has grown significantly in the last two decades. One of the most
important challenge for space mission operations and planning is the prediction
of solar proton events (SPEs). In this context, artificial intelligence and
machine learning techniques have opened a new frontier, providing a new
paradigm for statistical forecasting algorithms. The great majority of these
models aim to predict the occurrence of a SPE, i.e., they are based on the
classification approach. In this work we present a simple and efficient machine
learning regression algorithm which is able to forecast the energetic proton
flux up to 1 hour ahead by exploiting features derived from the electron flux
only. This approach could be helpful to improve monitoring systems of the
radiation risk in both deep space and near-Earth environments. The model is
very relevant for mission operations and planning, especially when flare
characteristics and source location are not available in real time, as at Mars
distance.


## Reinforcement-Learning based routing for packet-optical networks with hybrid telemetry
**Authors**: A. L. García Navarro, Nataliia Koneva, Alfonso Sánchez-Macián, José Alberto Hernández, Óscar González de Dios, J. M. Rivas-Moscoso

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12602v1](http://arxiv.org/pdf/2406.12602v1)

**Abstract**: This article provides a methodology and open-source implementation of
Reinforcement Learning algorithms for finding optimal routes in a
packet-optical network scenario. The algorithm uses measurements provided by
the physical layer (pre-FEC bit error rate and propagation delay) and the link
layer (link load) to configure a set of latency-based rewards and penalties
based on such measurements. Then, the algorithm executes Q-learning based on
this set of rewards for finding the optimal routing strategies. It is further
shown that the algorithm dynamically adapts to changing network conditions by
re-calculating optimal policies upon either link load changes or link
degradation as measured by pre-FEC BER.


## TroL: Traversal of Layers for Large Language and Vision Models
**Authors**: Byung-Kwan Lee, Sangyun Chung, Chae Won Kim, Beomchan Park, Yong Man Ro

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12246v1](http://arxiv.org/pdf/2406.12246v1)

**Abstract**: Large language and vision models (LLVMs) have been driven by the
generalization power of large language models (LLMs) and the advent of visual
instruction tuning. Along with scaling them up directly, these models enable
LLVMs to showcase powerful vision language (VL) performances by covering
diverse tasks via natural language instructions. However, existing open-source
LLVMs that perform comparably to closed-source LLVMs such as GPT-4V are often
considered too large (e.g., 26B, 34B, and 110B parameters), having a larger
number of layers. These large models demand costly, high-end resources for both
training and inference. To address this issue, we present a new efficient LLVM
family with 1.8B, 3.8B, and 7B LLM model sizes, Traversal of Layers (TroL),
which enables the reuse of layers in a token-wise manner. This layer traversing
technique simulates the effect of looking back and retracing the answering
stream while increasing the number of forward propagation layers without
physically adding more layers. We demonstrate that TroL employs a simple layer
traversing approach yet efficiently outperforms the open-source LLVMs with
larger model sizes and rivals the performances of the closed-source LLVMs with
substantial sizes.


## Quantum Compiling with Reinforcement Learning on a Superconducting Processor
**Authors**: Z. T. Wang, Qiuhao Chen, Yuxuan Du, Z. H. Yang, Xiaoxia Cai, Kaixuan Huang, Jingning Zhang, Kai Xu, Jun Du, Yinan Li, Yuling Jiao, Xingyao Wu, Wu Liu, Xiliang Lu, Huikai Xu, Yirong Jin, Ruixia Wang, Haifeng Yu, S. P. Zhao

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12195v1](http://arxiv.org/pdf/2406.12195v1)

**Abstract**: To effectively implement quantum algorithms on noisy intermediate-scale
quantum (NISQ) processors is a central task in modern quantum technology. NISQ
processors feature tens to a few hundreds of noisy qubits with limited
coherence times and gate operations with errors, so NISQ algorithms naturally
require employing circuits of short lengths via quantum compilation. Here, we
develop a reinforcement learning (RL)-based quantum compiler for a
superconducting processor and demonstrate its capability of discovering novel
and hardware-amenable circuits with short lengths. We show that for the
three-qubit quantum Fourier transformation, a compiled circuit using only seven
CZ gates with unity circuit fidelity can be achieved. The compiler is also able
to find optimal circuits under device topological constraints, with lengths
considerably shorter than those by the conventional method. Our study
exemplifies the codesign of the software with hardware for efficient quantum
compilation, offering valuable insights for the advancement of RL-based
compilers.


## Thermodynamic Transferability in Coarse-Grained Force Fields using Graph Neural Networks
**Authors**: Emily Shinkle, Aleksandra Pachalieva, Riti Bahl, Sakib Matin, Brendan Gifford, Galen T. Craven, Nicholas Lubbers

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.12112v1](http://arxiv.org/pdf/2406.12112v1)

**Abstract**: Coarse-graining is a molecular modeling technique in which an atomistic
system is represented in a simplified fashion that retains the most significant
system features that contribute to a target output, while removing the degrees
of freedom that are less relevant. This reduction in model complexity allows
coarse-grained molecular simulations to reach increased spatial and temporal
scales compared to corresponding all-atom models. A core challenge in
coarse-graining is to construct a force field that represents the interactions
in the new representation in a way that preserves the atomistic-level
properties. Many approaches to building coarse-grained force fields have
limited transferability between different thermodynamic conditions as a result
of averaging over internal fluctuations at a specific thermodynamic state
point. Here, we use a graph-convolutional neural network architecture, the
Hierarchically Interacting Particle Neural Network with Tensor Sensitivity
(HIP-NN-TS), to develop a highly automated training pipeline for coarse grained
force fields which allows for studying the transferability of coarse-grained
models based on the force-matching approach. We show that this approach not
only yields highly accurate force fields, but also that these force fields are
more transferable through a variety of thermodynamic conditions. These results
illustrate the potential of machine learning techniques such as graph neural
networks to improve the construction of transferable coarse-grained force
fields.


## QC-Forest: a Classical-Quantum Algorithm to Provably Speedup Retraining of Random Forest
**Authors**: Romina Yalovetzky, Niran Kumar, Changhao Li, Marco Pistoia

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.12008v1](http://arxiv.org/pdf/2406.12008v1)

**Abstract**: Random Forest (RF) is a popular tree-ensemble method for supervised learning,
prized for its ease of use and flexibility. Online RF models require to account
for new training data to maintain model accuracy. This is particularly
important in applications were data is periodically and sequentially generated
over time in data streams, such as auto-driving systems, and credit card
payments. In this setting, performing periodic model retraining with the old
and new data accumulated is beneficial as it fully captures possible drifts in
the data distribution over time. However, this is unpractical with
state-of-the-art classical algorithms for RF as they scale linearly with the
accumulated number of samples. We propose QC-Forest, a classical-quantum
algorithm designed to time-efficiently retrain RF models in the streaming
setting for multi-class classification and regression, achieving a runtime
poly-logarithmic in the total number of accumulated samples. QC-Forest
leverages Des-q, a quantum algorithm for single tree construction and
retraining proposed by Kumar et al. by expanding to multi-class classification,
as the original proposal was limited to binary classes, and introducing an
exact classical method to replace an underlying quantum subroutine incurring a
finite error, while maintaining the same poly-logarithmic dependence. Finally,
we showcase that QC-Forest achieves competitive accuracy in comparison to
state-of-the-art RF methods on widely used benchmark datasets with up to 80,000
samples, while significantly speeding up the model retrain.


## Modeling, Inference, and Prediction in Mobility-Based Compartmental Models for Epidemiology
**Authors**: Ning Jiang, Weiqi Chu, Yao Li

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.12002v1](http://arxiv.org/pdf/2406.12002v1)

**Abstract**: Classical compartmental models in epidemiology often struggle to accurately
capture real-world dynamics due to their inability to address the inherent
heterogeneity of populations. In this paper, we introduce a novel approach that
incorporates heterogeneity through a mobility variable, transforming the
traditional ODE system into a system of integro-differential equations that
describe the dynamics of population densities across different compartments.
Our results show that, for the same basic reproduction number, our
mobility-based model predicts a smaller final pandemic size compared to classic
compartmental models, whose population densities are represented as Dirac delta
functions in our density-based framework. This addresses the overestimation
issue common in many classical models. Additionally, we demonstrate that the
time series of the infected population is sufficient to uniquely identify the
mobility distribution. We reconstruct this distribution using a
machine-learning-based framework, providing both theoretical and algorithmic
support to effectively constrain the mobility-based model with real-world data.


## Evaluating the design space of diffusion-based generative models
**Authors**: Yuqing Wang, Ye He, Molei Tao

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12839v1](http://arxiv.org/pdf/2406.12839v1)

**Abstract**: Most existing theoretical investigations of the accuracy of diffusion models,
albeit significant, assume the score function has been approximated to a
certain accuracy, and then use this a priori bound to control the error of
generation. This article instead provides a first quantitative understanding of
the whole generation process, i.e., both training and sampling. More precisely,
it conducts a non-asymptotic convergence analysis of denoising score matching
under gradient descent. In addition, a refined sampling error analysis for
variance exploding models is also provided. The combination of these two
results yields a full error analysis, which elucidates (again, but this time
theoretically) how to design the training and sampling processes for effective
generation. For instance, our theory implies a preference toward noise
distribution and loss weighting that qualitatively agree with the ones used in
[Karras et al. 2022]. It also provides some perspectives on why the time and
variance schedule used in [Karras et al. 2022] could be better tuned than the
pioneering version in [Song et al. 2020].


## Influence Maximization via Graph Neural Bandits
**Authors**: Yuting Feng, Vincent Y. F. Tan, Bogdan Cautis

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12835v1](http://arxiv.org/pdf/2406.12835v1)

**Abstract**: We consider a ubiquitous scenario in the study of Influence Maximization
(IM), in which there is limited knowledge about the topology of the diffusion
network. We set the IM problem in a multi-round diffusion campaign, aiming to
maximize the number of distinct users that are influenced. Leveraging the
capability of bandit algorithms to effectively balance the objectives of
exploration and exploitation, as well as the expressivity of neural networks,
our study explores the application of neural bandit algorithms to the IM
problem. We propose the framework IM-GNB (Influence Maximization with Graph
Neural Bandits), where we provide an estimate of the users' probabilities of
being influenced by influencers (also known as diffusion seeds). This initial
estimate forms the basis for constructing both an exploitation graph and an
exploration one. Subsequently, IM-GNB handles the exploration-exploitation
tradeoff, by selecting seed nodes in real-time using Graph Convolutional
Networks (GCN), in which the pre-estimated graphs are employed to refine the
influencers' estimated rewards in each contextual setting. Through extensive
experiments on two large real-world datasets, we demonstrate the effectiveness
of IM-GNB compared with other baseline methods, significantly improving the
spread outcome of such diffusion campaigns, when the underlying network is
unknown.


## Extracting Training Data from Unconditional Diffusion Models
**Authors**: Yunhao Chen, Xingjun Ma, Difan Zou, Yu-Gang Jiang

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12752v1](http://arxiv.org/pdf/2406.12752v1)

**Abstract**: As diffusion probabilistic models (DPMs) are being employed as mainstream
models for generative artificial intelligence (AI), the study of their
memorization of the raw training data has attracted growing attention. Existing
works in this direction aim to establish an understanding of whether or to what
extent DPMs learn by memorization. Such an understanding is crucial for
identifying potential risks of data leakage and copyright infringement in
diffusion models and, more importantly, for more controllable generation and
trustworthy application of Artificial Intelligence Generated Content (AIGC).
While previous works have made important observations of when DPMs are prone to
memorization, these findings are mostly empirical, and the developed data
extraction methods only work for conditional diffusion models. In this work, we
aim to establish a theoretical understanding of memorization in DPMs with 1) a
memorization metric for theoretical analysis, 2) an analysis of conditional
memorization with informative and random labels, and 3) two better evaluation
metrics for measuring memorization. Based on the theoretical analysis, we
further propose a novel data extraction method called \textbf{Surrogate
condItional Data Extraction (SIDE)} that leverages a classifier trained on
generated data as a surrogate condition to extract training data directly from
unconditional diffusion models. Our empirical results demonstrate that SIDE can
extract training data from diffusion models where previous methods fail, and it
is on average over 50\% more effective across different scales of the CelebA
dataset.


## Learning Diffusion at Lightspeed
**Authors**: Antonio Terpin, Nicolas Lanzetti, Florian Dörfler

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12616v1](http://arxiv.org/pdf/2406.12616v1)

**Abstract**: Diffusion regulates a phenomenal number of natural processes and the dynamics
of many successful generative models. Existing models to learn the diffusion
terms from observational data rely on complex bilevel optimization problems and
properly model only the drift of the system. We propose a new simple model,
JKOnet*, which bypasses altogether the complexity of existing architectures
while presenting significantly enhanced representational capacity: JKOnet*
recovers the potential, interaction, and internal energy components of the
underlying diffusion process. JKOnet* minimizes a simple quadratic loss, runs
at lightspeed, and drastically outperforms other baselines in practice.
Additionally, JKOnet* provides a closed-form optimal solution for linearly
parametrized functionals. Our methodology is based on the interpretation of
diffusion processes as energy-minimizing trajectories in the probability space
via the so-called JKO scheme, which we study via its first-order optimality
conditions, in light of few-weeks-old advancements in optimization in the
probability space.


## The Limits of Pure Exploration in POMDPs: When the Observation Entropy is Enough
**Authors**: Riccardo Zamboni, Duilio Cirino, Marcello Restelli, Mirco Mutti

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12795v1](http://arxiv.org/pdf/2406.12795v1)

**Abstract**: The problem of pure exploration in Markov decision processes has been cast as
maximizing the entropy over the state distribution induced by the agent's
policy, an objective that has been extensively studied. However, little
attention has been dedicated to state entropy maximization under partial
observability, despite the latter being ubiquitous in applications, e.g.,
finance and robotics, in which the agent only receives noisy observations of
the true state governing the system's dynamics. How can we address state
entropy maximization in those domains? In this paper, we study the simple
approach of maximizing the entropy over observations in place of true latent
states. First, we provide lower and upper bounds to the approximation of the
true state entropy that only depends on some properties of the observation
function. Then, we show how knowledge of the latter can be exploited to compute
a principled regularization of the observation entropy to improve performance.
With this work, we provide both a flexible approach to bring advances in state
entropy maximization to the POMDP setting and a theoretical characterization of
its intrinsic limits.


## Bridging Design Gaps: A Parametric Data Completion Approach With Graph Guided Diffusion Models
**Authors**: Rui Zhou, Chenyang Yuan, Frank Permenter, Yanxia Zhang, Nikos Arechiga, Matt Klenk, Faez Ahmed

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11934v1](http://arxiv.org/pdf/2406.11934v1)

**Abstract**: This study introduces a generative imputation model leveraging graph
attention networks and tabular diffusion models for completing missing
parametric data in engineering designs. This model functions as an AI design
co-pilot, providing multiple design options for incomplete designs, which we
demonstrate using the bicycle design CAD dataset. Through comparative
evaluations, we demonstrate that our model significantly outperforms existing
classical methods, such as MissForest, hotDeck, PPCA, and tabular generative
method TabCSDI in both the accuracy and diversity of imputation options.
Generative modeling also enables a broader exploration of design possibilities,
thereby enhancing design decision-making by allowing engineers to explore a
variety of design completions. The graph model combines GNNs with the
structural information contained in assembly graphs, enabling the model to
understand and predict the complex interdependencies between different design
parameters. The graph model helps accurately capture and impute complex
parametric interdependencies from an assembly graph, which is key for design
problems. By learning from an existing dataset of designs, the imputation
capability allows the model to act as an intelligent assistant that
autocompletes CAD designs based on user-defined partial parametric design,
effectively bridging the gap between ideation and realization. The proposed
work provides a pathway to not only facilitate informed design decisions but
also promote creative exploration in design.


## Score-fPINN: Fractional Score-Based Physics-Informed Neural Networks for High-Dimensional Fokker-Planck-Levy Equations
**Authors**: Zheyuan Hu, Zhongqiang Zhang, George Em Karniadakis, Kenji Kawaguchi

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11676v1](http://arxiv.org/pdf/2406.11676v1)

**Abstract**: We introduce an innovative approach for solving high-dimensional
Fokker-Planck-L\'evy (FPL) equations in modeling non-Brownian processes across
disciplines such as physics, finance, and ecology. We utilize a fractional
score function and Physical-informed neural networks (PINN) to lift the curse
of dimensionality (CoD) and alleviate numerical overflow from exponentially
decaying solutions with dimensions. The introduction of a fractional score
function allows us to transform the FPL equation into a second-order partial
differential equation without fractional Laplacian and thus can be readily
solved with standard physics-informed neural networks (PINNs). We propose two
methods to obtain a fractional score function: fractional score matching (FSM)
and score-fPINN for fitting the fractional score function. While FSM is more
cost-effective, it relies on known conditional distributions. On the other
hand, score-fPINN is independent of specific stochastic differential equations
(SDEs) but requires evaluating the PINN model's derivatives, which may be more
costly. We conduct our experiments on various SDEs and demonstrate numerical
stability and effectiveness of our method in dealing with high-dimensional
problems, marking a significant advancement in addressing the CoD in FPL
equations.


## Constrained Reinforcement Learning with Average Reward Objective: Model-Based and Model-Free Algorithms
**Authors**: Vaneet Aggarwal, Washim Uddin Mondal, Qinbo Bai

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11481v1](http://arxiv.org/pdf/2406.11481v1)

**Abstract**: Reinforcement Learning (RL) serves as a versatile framework for sequential
decision-making, finding applications across diverse domains such as robotics,
autonomous driving, recommendation systems, supply chain optimization, biology,
mechanics, and finance. The primary objective in these applications is to
maximize the average reward. Real-world scenarios often necessitate adherence
to specific constraints during the learning process.
  This monograph focuses on the exploration of various model-based and
model-free approaches for Constrained RL within the context of average reward
Markov Decision Processes (MDPs). The investigation commences with an
examination of model-based strategies, delving into two foundational methods -
optimism in the face of uncertainty and posterior sampling. Subsequently, the
discussion transitions to parametrized model-free approaches, where the
primal-dual policy gradient-based algorithm is explored as a solution for
constrained MDPs. The monograph provides regret guarantees and analyzes
constraint violation for each of the discussed setups.
  For the above exploration, we assume the underlying MDP to be ergodic.
Further, this monograph extends its discussion to encompass results tailored
for weakly communicating MDPs, thereby broadening the scope of its findings and
their relevance to a wider range of practical scenarios.


## Trading Devil: Robust backdoor attack via Stochastic investment models and Bayesian approach
**Authors**: Orson Mengara

**Published Date**: 2024-06-15

**Updated Date**: 2024-06-15

**PDF Url**: [2406.10719v1](http://arxiv.org/pdf/2406.10719v1)

**Abstract**: With the growing use of voice-activated systems and speech recognition
technologies, the danger of backdoor attacks on audio data has grown
significantly. This research looks at a specific type of attack, known as a
Stochastic investment-based backdoor attack (MarketBack), in which adversaries
strategically manipulate the stylistic properties of audio to fool speech
recognition systems. The security and integrity of machine learning models are
seriously threatened by backdoor attacks, in order to maintain the reliability
of audio applications and systems, the identification of such attacks becomes
crucial in the context of audio data. Experimental results demonstrated that
MarketBack is feasible to achieve an average attack success rate close to 100%
in seven victim models when poisoning less than 1% of the training data.


