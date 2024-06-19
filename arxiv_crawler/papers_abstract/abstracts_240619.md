# Abstracts of Papers

## Latent Intuitive Physics: Learning to Transfer Hidden Physics from A 3D Video
**Authors**: Xiangming Zhu, Huayu Deng, Haochen Yuan, Yunbo Wang, Xiaokang Yang

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12769v1](http://arxiv.org/pdf/2406.12769v1)

**Abstract**: We introduce latent intuitive physics, a transfer learning framework for
physics simulation that can infer hidden properties of fluids from a single 3D
video and simulate the observed fluid in novel scenes. Our key insight is to
use latent features drawn from a learnable prior distribution conditioned on
the underlying particle states to capture the invisible and complex physical
properties. To achieve this, we train a parametrized prior learner given visual
observations to approximate the visual posterior of inverse graphics, and both
the particle states and the visual posterior are obtained from a learned neural
renderer. The converged prior learner is embedded in our probabilistic physics
engine, allowing us to perform novel simulations on unseen geometries,
boundaries, and dynamics without knowledge of the true physical parameters. We
validate our model in three ways: (i) novel scene simulation with the learned
visual-world physics, (ii) future prediction of the observed fluid dynamics,
and (iii) supervised particle simulation. Our model demonstrates strong
performance in all three tasks.


## Research on Dangerous Flight Weather Prediction based on Machine Learning
**Authors**: Haoxing Liu, Renjie Xie, Haoshen Qin, Yizhou Li

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12298v1](http://arxiv.org/pdf/2406.12298v1)

**Abstract**: With the continuous expansion of the scale of air transport, the demand for
aviation meteorological support also continues to grow. The impact of hazardous
weather on flight safety is critical. How to effectively use meteorological
data to improve the early warning capability of flight dangerous weather and
ensure the safe flight of aircraft is the primary task of aviation
meteorological services. In this work, support vector machine (SVM) models are
used to predict hazardous flight weather, especially for meteorological
conditions with high uncertainty such as storms and turbulence. SVM is a
supervised learning method that distinguishes between different classes of data
by finding optimal decision boundaries in a high-dimensional space. In order to
meet the needs of this study, we chose the radial basis function (RBF) as the
kernel function, which helps to deal with nonlinear problems and enables the
model to better capture complex meteorological data structures. During the
model training phase, we used historical meteorological observations from
multiple weather stations, including temperature, humidity, wind speed, wind
direction, and other meteorological indicators closely related to flight
safety. From this data, the SVM model learns how to distinguish between normal
and dangerous flight weather conditions.


## DustNet: skillful neural network predictions of Saharan dust
**Authors**: Trish E. Nowak, Andy T. Augousti, Benno I. Simmons, Stefan Siegert

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11754v1](http://arxiv.org/pdf/2406.11754v1)

**Abstract**: Suspended in the atmosphere are millions of tonnes of mineral dust which
interacts with weather and climate. Accurate representation of mineral dust in
weather models is vital, yet remains challenging. Large scale weather models
use high power supercomputers and take hours to complete the forecast. Such
computational burden allows them to only include monthly climatological means
of mineral dust as input states inhibiting their forecasting accuracy. Here, we
introduce DustNet a simple, accurate and super fast forecasting model for
24-hours ahead predictions of aerosol optical depth AOD. DustNet trains in less
than 8 minutes and creates predictions in 2 seconds on a desktop computer.
Created by DustNet predictions outperform the state-of-the-art physics-based
model on coarse 1 x 1 degree resolution at 95% of grid locations when compared
to ground truth satellite data. Our results show DustNet has a potential for
fast and accurate AOD forecasting which could transform our understanding of
dust impacts on weather patterns.


## Attention-Based Deep Reinforcement Learning for Qubit Allocation in Modular Quantum Architectures
**Authors**: Enrico Russo, Maurizio Palesi, Davide Patti, Giuseppe Ascia, Vincenzo Catania

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11452v1](http://arxiv.org/pdf/2406.11452v1)

**Abstract**: Modular, distributed and multi-core architectures are currently considered a
promising approach for scalability of quantum computing systems. The
integration of multiple Quantum Processing Units necessitates classical and
quantum-coherent communication, introducing challenges related to noise and
quantum decoherence in quantum state transfers between cores. Optimizing
communication becomes imperative, and the compilation and mapping of quantum
circuits onto physical qubits must minimize state transfers while adhering to
architectural constraints. The compilation process, inherently an NP-hard
problem, demands extensive search times even with a small number of qubits to
be solved to optimality. To address this challenge efficiently, we advocate for
the utilization of heuristic mappers that can rapidly generate solutions. In
this work, we propose a novel approach employing Deep Reinforcement Learning
(DRL) methods to learn these heuristics for a specific multi-core architecture.
Our DRL agent incorporates a Transformer encoder and Graph Neural Networks. It
encodes quantum circuits using self-attention mechanisms and produce outputs
through an attention-based pointer mechanism that directly signifies the
probability of matching logical qubits with physical cores. This enables the
selection of optimal cores for logical qubits efficiently. Experimental
evaluations show that the proposed method can outperform baseline approaches in
terms of reducing inter-core communications and minimizing online
time-to-solution. This research contributes to the advancement of scalable
quantum computing systems by introducing a novel learning-based heuristic
approach for efficient quantum circuit compilation and mapping.


## WeatherQA: Can Multimodal Language Models Reason about Severe Weather?
**Authors**: Chengqian Ma, Zhanxiang Hua, Alexandra Anderson-Frey, Vikram Iyer, Xin Liu, Lianhui Qin

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11217v1](http://arxiv.org/pdf/2406.11217v1)

**Abstract**: Severe convective weather events, such as hail, tornadoes, and thunderstorms,
often occur quickly yet cause significant damage, costing billions of dollars
every year. This highlights the importance of forecasting severe weather
threats hours in advance to better prepare meteorologists and residents in
at-risk areas. Can modern large foundation models perform such forecasting?
Existing weather benchmarks typically focus only on predicting time-series
changes in certain weather parameters (e.g., temperature, moisture) with
text-only features. In this work, we introduce WeatherQA, the first multimodal
dataset designed for machines to reason about complex combinations of weather
parameters (a.k.a., ingredients) and predict severe weather in real-world
scenarios. The dataset includes over 8,000 (multi-images, text) pairs for
diverse severe weather events. Each pair contains rich information crucial for
forecasting -- the images describe the ingredients capturing environmental
instability, surface observations, and radar reflectivity, and the text
contains forecast analyses written by human experts. With WeatherQA, we
evaluate state-of-the-art vision language models , including GPT4, Claude3,
Gemini-1.5, and a fine-tuned Llama3-based VLM, by designing two challenging
tasks: (1) multi-choice QA for predicting affected area and (2) classification
of the development potential of severe convection. These tasks require deep
understanding of domain knowledge (e.g., atmospheric dynamics) and complex
reasoning over multimodal data (e.g., interactions between weather parameters).
We show a substantial gap between the strongest VLM, GPT4o, and human
reasoning. Our comprehensive case study with meteorologists further reveals the
weaknesses of the models, suggesting that better training and data integration
are necessary to bridge this gap. WeatherQA link:
https://github.com/chengqianma/WeatherQA.


## Physics-Informed Deep Learning and Partial Transfer Learning for Bearing Fault Diagnosis in the Presence of Highly Missing Data
**Authors**: Mohammadreza Kavianpour, Parisa Kavianpour, Amin Ramezani

**Published Date**: 2024-06-16

**Updated Date**: 2024-06-16

**PDF Url**: [2406.11023v1](http://arxiv.org/pdf/2406.11023v1)

**Abstract**: One of the most significant obstacles in bearing fault diagnosis is a lack of
labeled data for various fault types. Also, sensor-acquired data frequently
lack labels and have a large amount of missing data. This paper tackles these
issues by presenting the PTPAI method, which uses a physics-informed deep
learning-based technique to generate synthetic labeled data. Labeled synthetic
data makes up the source domain, whereas unlabeled data with missing data is
present in the target domain. Consequently, imbalanced class problems and
partial-set fault diagnosis hurdles emerge. To address these challenges, the
RF-Mixup approach is used to handle imbalanced classes. As domain adaptation
strategies, the MK-MMSD and CDAN are employed to mitigate the disparity in
distribution between synthetic and actual data. Furthermore, the partial-set
challenge is tackled by applying weighting methods at the class and instance
levels. Experimental outcomes on the CWRU and JNU datasets indicate that the
proposed approach effectively addresses these problems.


## SPEAR: Receiver-to-Receiver Acoustic Neural Warping Field
**Authors**: Yuhang He, Shitong Xu, Jia-Xing Zhong, Sangyun Shin, Niki Trigoni, Andrew Markham

**Published Date**: 2024-06-16

**Updated Date**: 2024-06-16

**PDF Url**: [2406.11006v1](http://arxiv.org/pdf/2406.11006v1)

**Abstract**: We present SPEAR, a continuous receiver-to-receiver acoustic neural warping
field for spatial acoustic effects prediction in an acoustic 3D space with a
single stationary audio source. Unlike traditional source-to-receiver modelling
methods that require prior space acoustic properties knowledge to rigorously
model audio propagation from source to receiver, we propose to predict by
warping the spatial acoustic effects from one reference receiver position to
another target receiver position, so that the warped audio essentially
accommodates all spatial acoustic effects belonging to the target position.
SPEAR can be trained in a data much more readily accessible manner, in which we
simply ask two robots to independently record spatial audio at different
positions. We further theoretically prove the universal existence of the
warping field if and only if one audio source presents. Three physical
principles are incorporated to guide SPEAR network design, leading to the
learned warping field physically meaningful. We demonstrate SPEAR superiority
on both synthetic, photo-realistic and real-world dataset, showing the huge
potential of SPEAR to various down-stream robotic tasks.


## Diffusion Models Are Promising for Ab Initio Structure Solutions from Nanocrystalline Powder Diffraction Data
**Authors**: Gabe Guo, Tristan Saidi, Maxwell Terban, Simon JL Billinge, Hod Lipson

**Published Date**: 2024-06-16

**Updated Date**: 2024-06-16

**PDF Url**: [2406.10796v1](http://arxiv.org/pdf/2406.10796v1)

**Abstract**: A major challenge in materials science is the determination of the structure
of nanometer sized objects. Here we present a novel approach that uses a
generative machine learning model based on a Diffusion model that is trained on
45,229 known structures. The model factors both the measured diffraction
pattern as well as relevant statistical priors on the unit cell of atomic
cluster structures. Conditioned only on the chemical formula and the
information-scarce finite-size broadened powder diffraction pattern, we find
that our model, PXRDnet, can successfully solve simulated nanocrystals as small
as 10 angstroms across 200 materials of varying symmetry and complexity,
including structures from all seven crystal systems. We show that our model can
determine structural solutions with up to $81.5\%$ accuracy, as measured by
structural correlation. Furthermore, PXRDnet is capable of solving structures
from noisy diffraction patterns gathered in real-world experiments. We suggest
that data driven approaches, bootstrapped from theoretical simulation, will
ultimately provide a path towards determining the structure of previously
unsolved nano-materials.


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


## Sparsifying dimensionality reduction of PDE solution data with Bregman learning
**Authors**: Tjeerd Jan Heeringa, Christoph Brune, Mengwu Guo

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12672v1](http://arxiv.org/pdf/2406.12672v1)

**Abstract**: Classical model reduction techniques project the governing equations onto a
linear subspace of the original state space. More recent data-driven techniques
use neural networks to enable nonlinear projections. Whilst those often enable
stronger compression, they may have redundant parameters and lead to suboptimal
latent dimensionality. To overcome these, we propose a multistep algorithm that
induces sparsity in the encoder-decoder networks for effective reduction in the
number of parameters and additional compression of the latent space. This
algorithm starts with sparsely initialized a network and training it using
linearized Bregman iterations. These iterations have been very successful in
computer vision and compressed sensing tasks, but have not yet been used for
reduced-order modelling. After the training, we further compress the latent
space dimensionality by using a form of proper orthogonal decomposition. Last,
we use a bias propagation technique to change the induced sparsity into an
effective reduction of parameters. We apply this algorithm to three
representative PDE models: 1D diffusion, 1D advection, and 2D
reaction-diffusion. Compared to conventional training methods like Adam, the
proposed method achieves similar accuracy with 30% less parameters and a
significantly smaller latent space.


## Variational Distillation of Diffusion Policies into Mixture of Experts
**Authors**: Hongyi Zhou, Denis Blessing, Ge Li, Onur Celik, Xiaogang Jia, Gerhard Neumann, Rudolf Lioutikov

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12538v1](http://arxiv.org/pdf/2406.12538v1)

**Abstract**: This work introduces Variational Diffusion Distillation (VDD), a novel method
that distills denoising diffusion policies into Mixtures of Experts (MoE)
through variational inference. Diffusion Models are the current
state-of-the-art in generative modeling due to their exceptional ability to
accurately learn and represent complex, multi-modal distributions. This ability
allows Diffusion Models to replicate the inherent diversity in human behavior,
making them the preferred models in behavior learning such as Learning from
Human Demonstrations (LfD). However, diffusion models come with some drawbacks,
including the intractability of likelihoods and long inference times due to
their iterative sampling process. The inference times, in particular, pose a
significant challenge to real-time applications such as robot control. In
contrast, MoEs effectively address the aforementioned issues while retaining
the ability to represent complex distributions but are notoriously difficult to
train. VDD is the first method that distills pre-trained diffusion models into
MoE models, and hence, combines the expressiveness of Diffusion Models with the
benefits of Mixture Models. Specifically, VDD leverages a decompositional upper
bound of the variational objective that allows the training of each expert
separately, resulting in a robust optimization scheme for MoEs. VDD
demonstrates across nine complex behavior learning tasks, that it is able to:
i) accurately distill complex distributions learned by the diffusion model, ii)
outperform existing state-of-the-art distillation methods, and iii) surpass
conventional methods for training MoE.


## COT Flow: Learning Optimal-Transport Image Sampling and Editing by Contrastive Pairs
**Authors**: Xinrui Zu, Qian Tao

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.12140v1](http://arxiv.org/pdf/2406.12140v1)

**Abstract**: Diffusion models have demonstrated strong performance in sampling and editing
multi-modal data with high generation quality, yet they suffer from the
iterative generation process which is computationally expensive and slow. In
addition, most methods are constrained to generate data from Gaussian noise,
which limits their sampling and editing flexibility. To overcome both
disadvantages, we present Contrastive Optimal Transport Flow (COT Flow), a new
method that achieves fast and high-quality generation with improved zero-shot
editing flexibility compared to previous diffusion models. Benefiting from
optimal transport (OT), our method has no limitation on the prior distribution,
enabling unpaired image-to-image (I2I) translation and doubling the editable
space (at both the start and end of the trajectory) compared to other zero-shot
editing methods. In terms of quality, COT Flow can generate competitive results
in merely one step compared to previous state-of-the-art unpaired
image-to-image (I2I) translation methods. To highlight the advantages of COT
Flow through the introduction of OT, we introduce the COT Editor to perform
user-guided editing with excellent flexibility and quality. The code will be
released at https://github.com/zuxinrui/cot_flow.


## Adding Conditional Control to Diffusion Models with Reinforcement Learning
**Authors**: Yulai Zhao, Masatoshi Uehara, Gabriele Scalia, Tommaso Biancalani, Sergey Levine, Ehsan Hajiramezanali

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.12120v1](http://arxiv.org/pdf/2406.12120v1)

**Abstract**: Diffusion models are powerful generative models that allow for precise
control over the characteristics of the generated samples. While these
diffusion models trained on large datasets have achieved success, there is
often a need to introduce additional controls in downstream fine-tuning
processes, treating these powerful models as pre-trained diffusion models. This
work presents a novel method based on reinforcement learning (RL) to add
additional controls, leveraging an offline dataset comprising inputs and
corresponding labels. We formulate this task as an RL problem, with the
classifier learned from the offline dataset and the KL divergence against
pre-trained models serving as the reward functions. We introduce our method,
$\textbf{CTRL}$ ($\textbf{C}$onditioning pre-$\textbf{T}$rained diffusion
models with $\textbf{R}$einforcement $\textbf{L}$earning), which produces
soft-optimal policies that maximize the abovementioned reward functions. We
formally demonstrate that our method enables sampling from the conditional
distribution conditioned on additional controls during inference. Our RL-based
approach offers several advantages over existing methods. Compared to commonly
used classifier-free guidance, our approach improves sample efficiency, and can
greatly simplify offline dataset construction by exploiting conditional
independence between the inputs and additional controls. Furthermore, unlike
classifier guidance, we avoid the need to train classifiers from intermediate
states to additional controls.


## Decomposed evaluations of geographic disparities in text-to-image models
**Authors**: Abhishek Sureddy, Dishant Padalia, Nandhinee Periyakaruppa, Oindrila Saha, Adina Williams, Adriana Romero-Soriano, Megan Richards, Polina Kirichenko, Melissa Hall

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11988v1](http://arxiv.org/pdf/2406.11988v1)

**Abstract**: Recent work has identified substantial disparities in generated images of
different geographic regions, including stereotypical depictions of everyday
objects like houses and cars. However, existing measures for these disparities
have been limited to either human evaluations, which are time-consuming and
costly, or automatic metrics evaluating full images, which are unable to
attribute these disparities to specific parts of the generated images. In this
work, we introduce a new set of metrics, Decomposed Indicators of Disparities
in Image Generation (Decomposed-DIG), that allows us to separately measure
geographic disparities in the depiction of objects and backgrounds in generated
images. Using Decomposed-DIG, we audit a widely used latent diffusion model and
find that generated images depict objects with better realism than backgrounds
and that backgrounds in generated images tend to contain larger regional
disparities than objects. We use Decomposed-DIG to pinpoint specific examples
of disparities, such as stereotypical background generation in Africa,
struggling to generate modern vehicles in Africa, and unrealistically placing
some objects in outdoor settings. Informed by our metric, we use a new
prompting structure that enables a 52% worst-region improvement and a 20%
average improvement in generated background diversity.


## Crossfusor: A Cross-Attention Transformer Enhanced Conditional Diffusion Model for Car-Following Trajectory Prediction
**Authors**: Junwei You, Haotian Shi, Keshu Wu, Keke Long, Sicheng Fu, Sikai Chen, Bin Ran

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11941v1](http://arxiv.org/pdf/2406.11941v1)

**Abstract**: Vehicle trajectory prediction is crucial for advancing autonomous driving and
advanced driver assistance systems (ADAS), enhancing road safety and traffic
efficiency. While traditional methods have laid foundational work, modern deep
learning techniques, particularly transformer-based models and generative
approaches, have significantly improved prediction accuracy by capturing
complex and non-linear patterns in vehicle motion and traffic interactions.
However, these models often overlook the detailed car-following behaviors and
inter-vehicle interactions essential for real-world driving scenarios. This
study introduces a Cross-Attention Transformer Enhanced Conditional Diffusion
Model (Crossfusor) specifically designed for car-following trajectory
prediction. Crossfusor integrates detailed inter-vehicular interactions and
car-following dynamics into a robust diffusion framework, improving both the
accuracy and realism of predicted trajectories. The model leverages a novel
temporal feature encoding framework combining GRU, location-based attention
mechanisms, and Fourier embedding to capture historical vehicle dynamics. It
employs noise scaled by these encoded historical features in the forward
diffusion process, and uses a cross-attention transformer to model intricate
inter-vehicle dependencies in the reverse denoising process. Experimental
results on the NGSIM dataset demonstrate that Crossfusor outperforms
state-of-the-art models, particularly in long-term predictions, showcasing its
potential for enhancing the predictive capabilities of autonomous driving
systems.


## Tracking the perspectives of interacting language models
**Authors**: Hayden Helm, Brandon Duderstadt, Youngser Park, Carey E. Priebe

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11938v1](http://arxiv.org/pdf/2406.11938v1)

**Abstract**: Large language models (LLMs) are capable of producing high quality
information at unprecedented rates. As these models continue to entrench
themselves in society, the content they produce will become increasingly
pervasive in databases that are, in turn, incorporated into the pre-training
data, fine-tuning data, retrieval data, etc. of other language models. In this
paper we formalize the idea of a communication network of LLMs and introduce a
method for representing the perspective of individual models within a
collection of LLMs. Given these tools we systematically study information
diffusion in the communication network of LLMs in various simulated settings.


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


## Improving Quality Control of Whole Slide Images by Explicit Artifact Augmentation
**Authors**: Artur Jurgas, Marek Wodzinski, Marina D'Amato, Jeroen van der Laak, Manfredo Atzori, Henning Müller

**Published Date**: 2024-06-17

**Updated Date**: 2024-06-17

**PDF Url**: [2406.11538v1](http://arxiv.org/pdf/2406.11538v1)

**Abstract**: The problem of artifacts in whole slide image acquisition, prevalent in both
clinical workflows and research-oriented settings, necessitates human
intervention and re-scanning. Overcoming this challenge requires developing
quality control algorithms, that are hindered by the limited availability of
relevant annotated data in histopathology. The manual annotation of
ground-truth for artifact detection methods is expensive and time-consuming.
This work addresses the issue by proposing a method dedicated to augmenting
whole slide images with artifacts. The tool seamlessly generates and blends
artifacts from an external library to a given histopathology dataset. The
augmented datasets are then utilized to train artifact classification methods.
The evaluation shows their usefulness in classification of the artifacts, where
they show an improvement from 0.10 to 0.01 AUROC depending on the artifact
type. The framework, model, weights, and ground-truth annotations are freely
released to facilitate open science and reproducible research.


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


