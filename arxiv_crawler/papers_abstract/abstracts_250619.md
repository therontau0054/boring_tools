# Abstracts of Papers

## Physics
### Nabla-R2D3: Effective and Efficient 3D Diffusion Alignment with 2D Rewards
**Authors**: Qingming Liu, Zhen Liu, Dinghuai Zhang, Kui Jia

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15684v1](http://arxiv.org/pdf/2506.15684v1)

**Abstract**: Generating high-quality and photorealistic 3D assets remains a longstanding
challenge in 3D vision and computer graphics. Although state-of-the-art
generative models, such as diffusion models, have made significant progress in
3D generation, they often fall short of human-designed content due to limited
ability to follow instructions, align with human preferences, or produce
realistic textures, geometries, and physical attributes. In this paper, we
introduce Nabla-R2D3, a highly effective and sample-efficient reinforcement
learning alignment framework for 3D-native diffusion models using 2D rewards.
Built upon the recently proposed Nabla-GFlowNet method, which matches the score
function to reward gradients in a principled manner for reward finetuning, our
Nabla-R2D3 enables effective adaptation of 3D diffusion models using only 2D
reward signals. Extensive experiments show that, unlike vanilla finetuning
baselines which either struggle to converge or suffer from reward hacking,
Nabla-R2D3 consistently achieves higher rewards and reduced prior forgetting
within a few finetuning steps.


### Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos
**Authors**: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15680v1](http://arxiv.org/pdf/2506.15680v1)

**Abstract**: Modeling the dynamics of deformable objects is challenging due to their
diverse physical properties and the difficulty of estimating states from
limited visual information. We address these challenges with a neural dynamics
framework that combines object particles and spatial grids in a hybrid
representation. Our particle-grid model captures global shape and motion
information while predicting dense particle movements, enabling the modeling of
objects with varied shapes and materials. Particles represent object shapes,
while the spatial grid discretizes the 3D space to ensure spatial continuity
and enhance learning efficiency. Coupled with Gaussian Splattings for visual
rendering, our framework achieves a fully learning-based digital twin of
deformable objects and generates 3D action-conditioned videos. Through
experiments, we demonstrate that our model learns the dynamics of diverse
objects -- such as ropes, cloths, stuffed animals, and paper bags -- from
sparse-view RGB-D recordings of robot-object interactions, while also
generalizing at the category level to unseen instances. Our approach
outperforms state-of-the-art learning-based and physics-based simulators,
particularly in scenarios with limited camera views. Furthermore, we showcase
the utility of our learned models in model-based planning, enabling
goal-conditioned object manipulation across a range of tasks. The project page
is available at https://kywind.github.io/pgnd .


### Embodied Web Agents: Bridging Physical-Digital Realms for Integrated Agent Intelligence
**Authors**: Yining Hong, Rui Sun, Bingxuan Li, Xingcheng Yao, Maxine Wu, Alexander Chien, Da Yin, Ying Nian Wu, Zhecan James Wang, Kai-Wei Chang

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15677v1](http://arxiv.org/pdf/2506.15677v1)

**Abstract**: AI agents today are mostly siloed - they either retrieve and reason over vast
amount of digital information and knowledge obtained online; or interact with
the physical world through embodied perception, planning and action - but
rarely both. This separation limits their ability to solve tasks that require
integrated physical and digital intelligence, such as cooking from online
recipes, navigating with dynamic map data, or interpreting real-world landmarks
using web knowledge. We introduce Embodied Web Agents, a novel paradigm for AI
agents that fluidly bridge embodiment and web-scale reasoning. To
operationalize this concept, we first develop the Embodied Web Agents task
environments, a unified simulation platform that tightly integrates realistic
3D indoor and outdoor environments with functional web interfaces. Building
upon this platform, we construct and release the Embodied Web Agents Benchmark,
which encompasses a diverse suite of tasks including cooking, navigation,
shopping, tourism, and geolocation - all requiring coordinated reasoning across
physical and digital realms for systematic assessment of cross-domain
intelligence. Experimental results reveal significant performance gaps between
state-of-the-art AI systems and human capabilities, establishing both
challenges and opportunities at the intersection of embodied cognition and
web-scale knowledge access. All datasets, codes and websites are publicly
available at our project page https://embodied-web-agent.github.io/.


### Analog Quantum Phase Estimation with Single-Mode Readout
**Authors**: Wei-Chen Lin, Chiao-Hsuan Wang

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15668v1](http://arxiv.org/pdf/2506.15668v1)

**Abstract**: Eigenvalue estimation is a central problem for demonstrating quantum
advantage, yet its implementation on digital quantum computers remains limited
by circuit depth and operational overhead. We present an analog quantum phase
estimation (aQPE) protocol that extracts the eigenenergies of a target
Hamiltonian via continuous time evolution and single-mode cavity measurement.
By encoding eigenvalue information as conditional cavity phase-space rotations,
the scheme avoids deep quantum circuits and entangling gates, while enabling
readout through established cavity tomography techniques. We further illustrate
the feasibility of this approach by engineering a Hamiltonian that implements
aQPE of the XY model, whose ground-state energy problem is QMA-complete, within
a physical architecture compatible with existing circuit quantum
electrodynamics technology. Our results provide a resource-efficient and
scalable framework for implementing quantum phase estimation in near-term
quantum platforms.


### Exact solution for a class of quantum models of interacting bosons
**Authors**: Valery Shchesnovich

**Published Date**: 2024-11-21

**Updated Date**: 2025-06-18

**PDF Url**: [2411.14204v4](http://arxiv.org/pdf/2411.14204v4)

**Abstract**: Quantum models of interacting bosons have a wide range of applications,
including the propagation of optical modes in nonlinear media, such as the
$k$-photon down-conversion. Many of these models are related to nonlinear
deformations of finite group algebras and, in this sense, are exactly solvable.
While advanced group-theoretic methods were developed to study the eigenvalue
spectrum, in quantum optics, the primary focus is not on the spectrum of the
Hamiltonian but rather on the evolution of an initial state -- such as the
generation of optical signal modes by a strong pump mode propagating through a
nonlinear medium. I propose a simple and general method to solve the state
evolution problem, applicable to a broad class of quantum models of interacting
bosons. For the k-photon down-conversion model and its generalizations, the
solution to the state evolution problem is expressed as an infinite series
expansion in powers of the propagation time, with coefficients determined by a
recursion relation involving only a single polynomial function. This polynomial
function is unique to each nonlinear model. As an application, I compare the
exact solution of the parametric down-conversion process with the semiclassical
parametric approximation.


### Fokker-Planck Score Learning: Efficient Free-Energy Estimation under Periodic Boundary Conditions
**Authors**: Daniel Nagel, Tristan Bereau

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15653v1](http://arxiv.org/pdf/2506.15653v1)

**Abstract**: Accurate free-energy estimation is essential in molecular simulation, yet the
periodic boundary conditions (PBC) commonly used in computer simulations have
rarely been explicitly exploited. Equilibrium methods such as umbrella
sampling, metadynamics, and adaptive biasing force require extensive sampling,
while non-equilibrium pulling with Jarzynski's equality suffers from poor
convergence due to exponential averaging. Here, we introduce a
physics-informed, score-based diffusion framework: by mapping PBC simulations
onto a Brownian particle in a periodic potential, we derive the Fokker-Planck
steady-state score that directly encodes free-energy gradients. A neural
network is trained on non-equilibrium trajectories to learn this score,
providing a principled scheme to efficiently reconstruct the potential of mean
force (PMF). On benchmark periodic potentials and small-molecule membrane
permeation, our method is up to one order of magnitude more efficient than
umbrella sampling.


### Embedding physical symmetries into machine-learned reduced plasma physics models via data augmentation
**Authors**: Madox C. McGrae-Menge, Jacob R. Pierce, Frederico Fiuza, E. Paulo Alves

**Published Date**: 2025-06-16

**Updated Date**: 2025-06-18

**PDF Url**: [2506.14048v2](http://arxiv.org/pdf/2506.14048v2)

**Abstract**: Machine learning is offering powerful new tools for the development and
discovery of reduced models of nonlinear, multiscale plasma dynamics from the
data of first-principles kinetic simulations. However, ensuring the physical
consistency of such models requires embedding fundamental symmetries of plasma
dynamics. In this work, we explore a symmetry-embedding strategy based on data
augmentation, where symmetry-preserving transformations (e.g., Lorentz and
Galilean boosts) are applied to simulation data. Using both sparse regression
and neural networks, we show that models trained on symmetry-augmented data
more accurately infer the plasma fluid equations and pressure tensor closures
from fully kinetic particle-in-cell simulations of magnetic reconnection. We
show that this approach suppresses spurious inertial-frame-dependent
correlations between dynamical variables, improves data efficiency, and
significantly outperforms models trained without symmetry-augmented data, as
well as commonly used theoretical pressure closure models. Our results
establish symmetry-based data augmentation as a broadly applicable method for
incorporating physical structure into machine-learned reduced plasma models.


### Duplication-divergence growing graph models
**Authors**: Dario Borrelli

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15640v1](http://arxiv.org/pdf/2506.15640v1)

**Abstract**: In recent decades, it has been emphasized that the evolving structure of
networks may be shaped by interaction principles that yield sparse graphs with
a vertex degree distribution exhibiting an algebraic tail, and other structural
traits that are not featured in traditional random graphs. In this respect,
through a mean-field approach, this review tackles the statistical physics of
graph models based on the interaction principle of duplication-divergence.
Additional sophistications extending the duplication-divergence model are also
reviewed as well as generalizations of other known models. Possible research
gaps and related prior results are then discussed.


### Robust Physics-Informed Neural Network Approach for Estimating Heterogeneous Elastic Properties from Noisy Displacement Data
**Authors**: Tatthapong Srikitrungruang, Matthew Lemon, Sina Aghaee Dabaghan Fard, Jaesung Lee, Yuxiao Zhou

**Published Date**: 2025-06-16

**Updated Date**: 2025-06-18

**PDF Url**: [2506.14036v2](http://arxiv.org/pdf/2506.14036v2)

**Abstract**: Accurately estimating spatially heterogeneous elasticity parameters,
particularly Young's modulus and Poisson's ratio, from noisy displacement
measurements remains significantly challenging in inverse elasticity problems.
Existing inverse estimation techniques are often limited by instability,
pronounced sensitivity to measurement noise, and difficulty in recovering
absolute-scale Young's modulus. This work presents a novel Inverse Elasticity
Physics-Informed Neural Network (IE-PINN) specifically designed to robustly
reconstruct heterogeneous distributions of elasticity parameters from noisy
displacement data based on linear elasticity physics. IE-PINN integrates three
distinct neural network architectures dedicated to separately modeling
displacement fields, strain fields, and elasticity distributions, thereby
significantly enhancing stability and accuracy against measurement noise.
Additionally, a two-phase estimation strategy is introduced: the first phase
recovers relative spatial distributions of Young's modulus and Poisson's ratio,
and the second phase calibrates the absolute scale of Young's modulus using
imposed loading boundary conditions. Additional methodological innovations,
including positional encoding, sine activation functions, and a sequential
pretraining protocol, further enhance the model's performance and robustness.
Extensive numerical experiments demonstrate that IE-PINN effectively overcomes
critical limitations encountered by existing methods, delivering accurate
absolute-scale elasticity estimations even under severe noise conditions. This
advancement holds substantial potential for clinical imaging diagnostics and
mechanical characterization, where measurements typically encounter substantial
noise.


### A covariant description of the interactions of axion-like particles and hadrons
**Authors**: Reuven Balkin, Ta'el Coren, Yotam Soreq, Mike Williams

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15637v1](http://arxiv.org/pdf/2506.15637v1)

**Abstract**: We present a covariant framework for analyzing the interactions and decay
rates of axion-like particles (ALPs) that couple to both gluons and quarks. We
identify combinations of couplings that are invariant under quark-field
redefinitions, and use them to obtain physical expressions for the prominent
decay rates of such ALPs, which are compared with previous calculations for
scenarios where ALPs couple exclusively to quarks or to gluons. Our framework
can be used to obtain ALP decay rates for arbitrary ALP couplings to gluons and
quarks across a broad range of ALP masses.


## Diffusion
### One-Step Diffusion for Detail-Rich and Temporally Consistent Video Super-Resolution
**Authors**: Yujing Sun, Lingchen Sun, Shuaizheng Liu, Rongyuan Wu, Zhengqiang Zhang, Lei Zhang

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15591v1](http://arxiv.org/pdf/2506.15591v1)

**Abstract**: It is a challenging problem to reproduce rich spatial details while
maintaining temporal consistency in real-world video super-resolution
(Real-VSR), especially when we leverage pre-trained generative models such as
stable diffusion (SD) for realistic details synthesis. Existing SD-based
Real-VSR methods often compromise spatial details for temporal coherence,
resulting in suboptimal visual quality. We argue that the key lies in how to
effectively extract the degradation-robust temporal consistency priors from the
low-quality (LQ) input video and enhance the video details while maintaining
the extracted consistency priors. To achieve this, we propose a Dual LoRA
Learning (DLoRAL) paradigm to train an effective SD-based one-step diffusion
model, achieving realistic frame details and temporal consistency
simultaneously. Specifically, we introduce a Cross-Frame Retrieval (CFR) module
to aggregate complementary information across frames, and train a
Consistency-LoRA (C-LoRA) to learn robust temporal representations from
degraded inputs. After consistency learning, we fix the CFR and C-LoRA modules
and train a Detail-LoRA (D-LoRA) to enhance spatial details while aligning with
the temporal space defined by C-LoRA to keep temporal coherence. The two phases
alternate iteratively for optimization, collaboratively delivering consistent
and detail-rich outputs. During inference, the two LoRA branches are merged
into the SD model, allowing efficient and high-quality video restoration in a
single diffusion step. Experiments show that DLoRAL achieves strong performance
in both accuracy and speed. Code and models are available at
https://github.com/yjsunnn/DLoRAL.


### CLAIM: Clinically-Guided LGE Augmentation for Realistic and Diverse Myocardial Scar Synthesis and Segmentation
**Authors**: Farheen Ramzan, Yusuf Kiberu, Nikesh Jathanna, Shahnaz Jamil-Copley, Richard H. Clayton, Chen, Chen

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15549v1](http://arxiv.org/pdf/2506.15549v1)

**Abstract**: Deep learning-based myocardial scar segmentation from late gadolinium
enhancement (LGE) cardiac MRI has shown great potential for accurate and timely
diagnosis and treatment planning for structural cardiac diseases. However, the
limited availability and variability of LGE images with high-quality scar
labels restrict the development of robust segmentation models. To address this,
we introduce CLAIM: \textbf{C}linically-Guided \textbf{L}GE
\textbf{A}ugmentation for Real\textbf{i}stic and Diverse \textbf{M}yocardial
Scar Synthesis and Segmentation framework, a framework for anatomically
grounded scar generation and segmentation. At its core is the SMILE module
(Scar Mask generation guided by cLinical knowledgE), which conditions a
diffusion-based generator on the clinically adopted AHA 17-segment model to
synthesize images with anatomically consistent and spatially diverse scar
patterns. In addition, CLAIM employs a joint training strategy in which the
scar segmentation network is optimized alongside the generator, aiming to
enhance both the realism of synthesized scars and the accuracy of the scar
segmentation performance. Experimental results show that CLAIM produces
anatomically coherent scar patterns and achieves higher Dice similarity with
real scar distributions compared to baseline models. Our approach enables
controllable and realistic myocardial scar synthesis and has demonstrated
utility for downstream medical imaging task.


### Intrinsic and Extrinsic Organized Attention: Softmax Invariance and Network Sparsity
**Authors**: Oluwadamilola Fasina, Ruben V. C. Pohle, Pei-Chun Su, Ronald R. Coifman

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15541v1](http://arxiv.org/pdf/2506.15541v1)

**Abstract**: We examine the intrinsic (within the attention head) and extrinsic (amongst
the attention heads) structure of the self-attention mechanism in transformers.
Theoretical evidence for invariance of the self-attention mechanism to softmax
activation is obtained by appealing to paradifferential calculus, (and is
supported by computational examples), which relies on the intrinsic
organization of the attention heads. Furthermore, we use an existing
methodology for hierarchical organization of tensors to examine network
structure by constructing hierarchal partition trees with respect to the query,
key, and head axes of network 3-tensors. Such an organization is consequential
since it allows one to profitably execute common signal processing tasks on a
geometry where the organized network 3-tensors exhibit regularity. We exemplify
this qualitatively, by visualizing the hierarchical organization of the tree
comprised of attention heads and the diffusion map embeddings, and
quantitatively by investigating network sparsity with the expansion
coefficients of individual attention heads and the entire network with respect
to the bi and tri-haar bases (respectively) on the space of queries, keys, and
heads of the network. To showcase the utility of our theoretical and
methodological findings, we provide computational examples using vision and
language transformers. The ramifications of these findings are two-fold: (1) a
subsequent step in interpretability analysis is theoretically admitted, and can
be exploited empirically for downstream interpretability tasks (2) one can use
the network 3-tensor organization for empirical network applications such as
model pruning (by virtue of network sparsity) and network architecture
comparison.


### A Comprehensive Survey on Continual Learning in Generative Models
**Authors**: Haiyang Guo, Fanhu Zeng, Fei Zhu, Jiayi Wang, Xukai Wang, Jingang Zhou, Hongbo Zhao, Wenzhuo Liu, Shijie Ma, Da-Han Wang, Xu-Yao Zhang, Cheng-Lin Liu

**Published Date**: 2025-06-16

**Updated Date**: 2025-06-18

**PDF Url**: [2506.13045v2](http://arxiv.org/pdf/2506.13045v2)

**Abstract**: The rapid advancement of generative models has enabled modern AI systems to
comprehend and produce highly sophisticated content, even achieving human-level
performance in specific domains. However, these models remain fundamentally
constrained by catastrophic forgetting - a persistent challenge where adapting
to new tasks typically leads to significant degradation in performance on
previously learned tasks. To address this practical limitation, numerous
approaches have been proposed to enhance the adaptability and scalability of
generative models in real-world applications. In this work, we present a
comprehensive survey of continual learning methods for mainstream generative
models, including large language models, multimodal large language models,
vision language action models, and diffusion models. Drawing inspiration from
the memory mechanisms of the human brain, we systematically categorize these
approaches into three paradigms: architecture-based, regularization-based, and
replay-based methods, while elucidating their underlying methodologies and
motivations. We further analyze continual learning setups for different
generative models, including training objectives, benchmarks, and core
backbones, offering deeper insights into the field. The project page of this
paper is available at
https://github.com/Ghy0501/Awesome-Continual-Learning-in-Generative-Models.


### Diff-TONE: Timestep Optimization for iNstrument Editing in Text-to-Music Diffusion Models
**Authors**: Teysir Baoueb, Xiaoyu Bie, Xi Wang, Gaël Richard

**Published Date**: 2025-06-18

**Updated Date**: 2025-06-18

**PDF Url**: [2506.15530v1](http://arxiv.org/pdf/2506.15530v1)

**Abstract**: Breakthroughs in text-to-music generation models are transforming the
creative landscape, equipping musicians with innovative tools for composition
and experimentation like never before. However, controlling the generation
process to achieve a specific desired outcome remains a significant challenge.
Even a minor change in the text prompt, combined with the same random seed, can
drastically alter the generated piece. In this paper, we explore the
application of existing text-to-music diffusion models for instrument editing.
Specifically, for an existing audio track, we aim to leverage a pretrained
text-to-music diffusion model to edit the instrument while preserving the
underlying content. Based on the insight that the model first focuses on the
overall structure or content of the audio, then adds instrument information,
and finally refines the quality, we show that selecting a well-chosen
intermediate timestep, identified through an instrument classifier, yields a
balance between preserving the original piece's content and achieving the
desired timbre. Our method does not require additional training of the
text-to-music diffusion model, nor does it compromise the generation process's
speed.


