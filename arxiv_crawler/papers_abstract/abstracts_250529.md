# Abstracts of Papers

## Physics
### SimProcess: High Fidelity Simulation of Noisy ICS Physical Processes
**Authors**: Denis Donadel, Gabriele Crestanello, Giulio Morandini, Daniele Antonioli, Mauro Conti, Massimo Merro

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22638v1](http://arxiv.org/pdf/2505.22638v1)

**Abstract**: Industrial Control Systems (ICS) manage critical infrastructures like power
grids and water treatment plants. Cyberattacks on ICSs can disrupt operations,
causing severe economic, environmental, and safety issues. For example,
undetected pollution in a water plant can put the lives of thousands at stake.
ICS researchers have increasingly turned to honeypots -- decoy systems designed
to attract attackers, study their behaviors, and eventually improve defensive
mechanisms. However, existing ICS honeypots struggle to replicate the ICS
physical process, making them susceptible to detection. Accurately simulating
the noise in ICS physical processes is challenging because different factors
produce it, including sensor imperfections and external interferences.
  In this paper, we propose SimProcess, a novel framework to rank the fidelity
of ICS simulations by evaluating how closely they resemble real-world and noisy
physical processes. It measures the simulation distance from a target system by
estimating the noise distribution with machine learning models like Random
Forest. Unlike existing solutions that require detailed mathematical models or
are limited to simple systems, SimProcess operates with only a timeseries of
measurements from the real system, making it applicable to a broader range of
complex dynamic systems. We demonstrate the framework's effectiveness through a
case study using real-world power grid data from the EPIC testbed. We compare
the performance of various simulation methods, including static and generative
noise techniques. Our model correctly classifies real samples with a recall of
up to 1.0. It also identifies Gaussian and Gaussian Mixture as the best
distribution to simulate our power systems, together with a generative solution
provided by an autoencoder, thereby helping developers to improve honeypot
fidelity. Additionally, we make our code publicly available.


### The Sky as a Killing Horizon
**Authors**: Níckolas de Aguiar Alves, Andre G. S. Landulfo

**Published Date**: 2025-04-16

**Updated Date**: 2025-05-28

**PDF Url**: [2504.12514v2](http://arxiv.org/pdf/2504.12514v2)

**Abstract**: Symmetries are ubiquitous in modern physics. They not only allow for a more
simplified description of physical systems but also, from a more fundamental
perspective, can be seen as determining a theory itself. In the present paper,
we propose a new definition of asymptotic symmetries that unifies and
generalizes the usual notions of symmetry considered in asymptotically flat
spacetimes and expanding universes with cosmological horizons. This is done by
considering BMS-like symmetries for "asymptotic (conformal) Killing horizons",
or A(C)KHs, here defined as null hypersurfaces that are tangent to a vector
field satisfying the (conformal) Killing equation in a limiting sense. The
construction is theory-agnostic and extremely general, for it makes no use of
the Einstein equations and can be applied to a wide range of scenarios with
different dimensions or hypersurface cross sections. While we reproduce the
results by Dappiaggi, Moretti, and Pinamonti in the case of asymptotic Killing
horizons, the conformal generalization does not yield only the BMS group, but a
larger group. The enlargement is due to the presence of "superdilations". We
speculate on many implications and possible continuations of this work,
including the exploration of gravitational memory effects beyond general
relativity, understanding antipodal matching conditions at spatial infinity in
terms of bifurcate horizons, and the absence of superrotations in de Sitter
spacetime and Killing horizons.


### An effective model for describing coherent population trapping resonances, which correctly takes into account the off-resonant frequency components in periodically modulated laser field
**Authors**: V. I. Yudin, M. Yu. Basalaev, A. V. Taichenachev, O. N. Prudnikov

**Published Date**: 2025-05-03

**Updated Date**: 2025-05-28

**PDF Url**: [2505.01924v2](http://arxiv.org/pdf/2505.01924v2)

**Abstract**: We have developed an effective mathematical model to calculate the coherent
population trapping (CPT) resonance in periodically modulated light, when the
modulation frequency $f$ varies near the fractional part of hyperfine splitting
in the ground state $\Delta_{\rm hfs}/N$ (where $N=1,2,...$). In such
polychromatic field, only two frequency components that are most resonant with
atomic optical transitions are taken into account accurately, while all other
off-resonant components are taken into account using the second-order
perturbation theory in the field. Within the presented concept, equation for
atomic density matrix is obtained, in which the contribution of all
off-resonant components is reduced to the appearance of two new operators
(non-diagonal, in general case): the shift operator and relaxation operators.
In the case of three-level $\Lambda$-system, the adequacy of presented
effective model was verified by numerical calculations of various dependencies,
in which we did not find visual differences from the exact calculations. In
addition to a significant mathematical simplification, our model provides a
clear physical picture of various features of CPT spectroscopy in a
periodically modulated laser field, including effects that have not been
discussed in the scientific literature before. In particular, we show that the
widespread viewpoint that the CPT resonance shift is determined by usual ac
Stark shifts of the lower levels is, in general, fundamentally incorrect, since
the contribution to the light shift due to beats at the frequency $\Delta_{\rm
hfs}$ between different off-resonant frequency components can be comparable (or
even dominate) with the standard ac Stark shift. Therefore, even if we have
detailed information on the modulated field spectrum (e.g. using a spectrum
analyzer), this is, in general, absolutely insufficient to determine the light
shift of CPT resonance.


### Arnold Diffusion in the Full Three-Body Problem
**Authors**: Maciej J. Capinski, Marian Gidea

**Published Date**: 2025-04-12

**Updated Date**: 2025-05-28

**PDF Url**: [2504.09273v3](http://arxiv.org/pdf/2504.09273v3)

**Abstract**: The full three-body problem, on the motion of three celestial bodies under
their mutual gravitational attraction, is one of the oldest unsolved problems
in classical mechanics. The main difficulty comes from the presence of unstable
and chaotic motions, which make long-term prediction impossible. In this paper,
we show that the full three-body problem exhibits a strong form of instability
known as Arnold diffusion. We consider the planar full three-body problem,
formulated as a perturbation of both the Kepler problem and the planar circular
restricted three-body problem. We show that the system exhibits Arnold
diffusion, in the sense that there is a transfer of energy -- of an amount
independent of the perturbation parameter -- between the Kepler problem and the
restricted three-body problem. Our argument is based on the topological method
of correctly aligned windows, which is implemented into a computer assisted
proof. We demonstrate that the approach can be applied to physically relevant
masses of the bodies, choosing a Neptune-Triton-asteroid system as an example.
In this case, we obtain explicit estimates for the range of the perturbation
parameter and for the diffusion time.


### On the performance of machine-learning assisted Monte Carlo in sampling from simple statistical physics models
**Authors**: Luca Maria Del Bono, Federico Ricci-Tersenghi, Francesco Zamponi

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22598v1](http://arxiv.org/pdf/2505.22598v1)

**Abstract**: Recent years have seen a rise in the application of machine learning
techniques to aid the simulation of hard-to-sample systems that cannot be
studied using traditional methods. Despite the introduction of many different
architectures and procedures, a wide theoretical understanding is still
lacking, with the risk of suboptimal implementations. As a first step to
address this gap, we provide here a complete analytic study of the widely-used
Sequential Tempering procedure applied to a shallow MADE architecture for the
Curie-Weiss model. The contribution of this work is twofold: firstly, we give a
description of the optimal weights and of the training under Gradient Descent
optimization. Secondly, we compare what happens in Sequential Tempering with
and without the addition of local Metropolis Monte Carlo steps. We are thus
able to give theoretical predictions on the best procedure to apply in this
case. This work establishes a clear theoretical basis for the integration of
machine learning techniques into Monte Carlo sampling and optimization.


### Universal Visuo-Tactile Video Understanding for Embodied Interaction
**Authors**: Yifan Xie, Mingyang Li, Shoujie Li, Xingting Li, Guangyu Chen, Fei Ma, Fei Richard Yu, Wenbo Ding

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22566v1](http://arxiv.org/pdf/2505.22566v1)

**Abstract**: Tactile perception is essential for embodied agents to understand physical
attributes of objects that cannot be determined through visual inspection
alone. While existing approaches have made progress in visual and language
modalities for physical understanding, they fail to effectively incorporate
tactile information that provides crucial haptic feedback for real-world
interaction. In this paper, we present VTV-LLM, the first multi-modal large
language model for universal Visuo-Tactile Video (VTV) understanding that
bridges the gap between tactile perception and natural language. To address the
challenges of cross-sensor and cross-modal integration, we contribute VTV150K,
a comprehensive dataset comprising 150,000 video frames from 100 diverse
objects captured across three different tactile sensors (GelSight Mini, DIGIT,
and Tac3D), annotated with four fundamental tactile attributes (hardness,
protrusion, elasticity, and friction). We develop a novel three-stage training
paradigm that includes VTV enhancement for robust visuo-tactile representation,
VTV-text alignment for cross-modal correspondence, and text prompt finetuning
for natural language generation. Our framework enables sophisticated tactile
reasoning capabilities including feature assessment, comparative analysis,
scenario-based decision making and so on. Experimental evaluations demonstrate
that VTV-LLM achieves superior performance in tactile video understanding
tasks, establishing a foundation for more intuitive human-machine interaction
in tactile domains.


### Geometric Hyena Networks for Large-scale Equivariant Learning
**Authors**: Artem Moskalev, Mangal Prakash, Junjie Xu, Tianyu Cui, Rui Liao, Tommaso Mansi

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22560v1](http://arxiv.org/pdf/2505.22560v1)

**Abstract**: Processing global geometric context while preserving equivariance is crucial
when modeling biological, chemical, and physical systems. Yet, this is
challenging due to the computational demands of equivariance and global context
at scale. Standard methods such as equivariant self-attention suffer from
quadratic complexity, while local methods such as distance-based message
passing sacrifice global information. Inspired by the recent success of
state-space and long-convolutional models, we introduce Geometric Hyena, the
first equivariant long-convolutional model for geometric systems. Geometric
Hyena captures global geometric context at sub-quadratic complexity while
maintaining equivariance to rotations and translations. Evaluated on all-atom
property prediction of large RNA molecules and full protein molecular dynamics,
Geometric Hyena outperforms existing equivariant models while requiring
significantly less memory and compute that equivariant self-attention. Notably,
our model processes the geometric context of 30k tokens 20x faster than the
equivariant transformer and allows 72x longer context within the same budget.


### RiverMamba: A State Space Model for Global River Discharge and Flood Forecasting
**Authors**: Mohamad Hakam Shams Eddin, Yikui Zahng, Stefan Kollet, Juergen Gall

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22535v1](http://arxiv.org/pdf/2505.22535v1)

**Abstract**: Recent deep learning approaches for river discharge forecasting have improved
the accuracy and efficiency in flood forecasting, enabling more reliable early
warning systems for risk management. Nevertheless, existing deep learning
approaches in hydrology remain largely confined to local-scale applications and
do not leverage the inherent spatial connections of bodies of water. Thus,
there is a strong need for new deep learning methodologies that are capable of
modeling spatio-temporal relations to improve river discharge and flood
forecasting for scientific and operational applications. To address this, we
present RiverMamba, a novel deep learning model that is pretrained with
long-term reanalysis data and that can forecast global river discharge and
floods on a $0.05^\circ$ grid up to 7 days lead time, which is of high
relevance in early warning. To achieve this, RiverMamba leverages efficient
Mamba blocks that enable the model to capture global-scale channel network
routing and enhance its forecast capability for longer lead times. The forecast
blocks integrate ECMWF HRES meteorological forecasts, while accounting for
their inaccuracies through spatio-temporal modeling. Our analysis demonstrates
that RiverMamba delivers reliable predictions of river discharge, including
extreme floods across return periods and lead times, surpassing both
operational AI- and physics-based models.


### Unveiling the jet angular broadening with photon-tagged jets in high-energy nuclear collisions
**Authors**: Sa Wang, Yao Li, Jin-Wen Kang, Ben-Wei Zhang

**Published Date**: 2024-08-20

**Updated Date**: 2025-05-28

**PDF Url**: [2408.10924v2](http://arxiv.org/pdf/2408.10924v2)

**Abstract**: The medium modification of jet substructure in hot and dense nuclear matter
has garnered significant interest from the heavy-ion physics community in
recent years. Measurements of inclusive jets show an angular narrowing in
nucleus-nucleus collisions, while recent CMS results for photon-tagged jets
($\gamma$+jets) suggest evidence of broadening. In this study, we conduct a
theoretical analysis of the angular structure of inclusive jets and
$\gamma$+jets using a transport approach that accounts for jet energy loss and
the medium response in the quark-gluon plasma. We examine the girth
modification of $\gamma$+jets in $0-30\%$ PbPb collisions at $\sqrt{s_{NN}} =
5.02$ TeV, achieving satisfactory agreement with recent CMS measurements. We
explore the relationship between selection bias and jet kinematics by varying
the threshold for $x_{j\gamma} = p_T^{\rm jet}/p_T^{\gamma}$. Notably, we
quantitatively demonstrate that $\gamma$+jets significantly reduce selection
bias and can effectively select jets that have been sufficiently quenched in
PbPb collisions, which is crucial for capture the jet angular broadening.
Additionally, we estimate the contributions of medium-induced gluon radiation
and the medium response to the broadening of the jet angular substructure.
Lastly, we analyze the modification patterns of jet $R_g$ and $\Delta R_{\rm
axis}$ in PbPb collisions, which indicate slight broadening for $\gamma$+jets
and noticeable narrowing for inclusive jets compared to pp collisions.


### Geometric GNNs for Charged Particle Tracking at GlueX
**Authors**: Ahmed Hossam Mohammed, Kishansingh Rajput, Simon Taylor, Denis Furletov, Sergey Furletov, Malachi Schram

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22504v1](http://arxiv.org/pdf/2505.22504v1)

**Abstract**: Nuclear physics experiments are aimed at uncovering the fundamental building
blocks of matter. The experiments involve high-energy collisions that produce
complex events with many particle trajectories. Tracking charged particles
resulting from collisions in the presence of a strong magnetic field is
critical to enable the reconstruction of particle trajectories and precise
determination of interactions. It is traditionally achieved through
combinatorial approaches that scale worse than linearly as the number of hits
grows. Since particle hit data naturally form a 3-dimensional point cloud and
can be structured as graphs, Graph Neural Networks (GNNs) emerge as an
intuitive and effective choice for this task. In this study, we evaluate the
GNN model for track finding on the data from the GlueX experiment at Jefferson
Lab. We use simulation data to train the model and test on both simulation and
real GlueX measurements. We demonstrate that GNN-based track finding
outperforms the currently used traditional method at GlueX in terms of
segment-based efficiency at a fixed purity while providing faster inferences.
We show that the GNN model can achieve significant speedup by processing
multiple events in batches, which exploits the parallel computation capability
of Graphical Processing Units (GPUs). Finally, we compare the GNN
implementation on GPU and FPGA and describe the trade-off.


## Diffusion
### Principled Out-of-Distribution Generalization via Simplicity
**Authors**: Jiawei Ge, Amanda Wang, Shange Tang, Chi Jin

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22622v1](http://arxiv.org/pdf/2505.22622v1)

**Abstract**: Modern foundation models exhibit remarkable out-of-distribution (OOD)
generalization, solving tasks far beyond the support of their training data.
However, the theoretical principles underpinning this phenomenon remain
elusive. This paper investigates this problem by examining the compositional
generalization abilities of diffusion models in image generation. Our analysis
reveals that while neural network architectures are expressive enough to
represent a wide range of models -- including many with undesirable behavior on
OOD inputs -- the true, generalizable model that aligns with human expectations
typically corresponds to the simplest among those consistent with the training
data.
  Motivated by this observation, we develop a theoretical framework for OOD
generalization via simplicity, quantified using a predefined simplicity metric.
We analyze two key regimes: (1) the constant-gap setting, where the true model
is strictly simpler than all spurious alternatives by a fixed gap, and (2) the
vanishing-gap setting, where the fixed gap is replaced by a smoothness
condition ensuring that models close in simplicity to the true model yield
similar predictions. For both regimes, we study the regularized maximum
likelihood estimator and establish the first sharp sample complexity guarantees
for learning the true, generalizable, simple model.


### Test-Time Alignment of Discrete Diffusion Models with Sequential Monte Carlo
**Authors**: Chinmay Pani, Zijing Ou, Yingzhen Li

**Published Date**: 2025-05-28

**Updated Date**: 2025-05-28

**PDF Url**: [2505.22524v1](http://arxiv.org/pdf/2505.22524v1)

**Abstract**: Discrete diffusion models have become highly effective across various
domains. However, real-world applications often require the generative process
to adhere to certain constraints but without task-specific fine-tuning. To this
end, we propose a training-free method based on Sequential Monte Carlo (SMC) to
sample from the reward-aligned target distribution at the test time. Our
approach leverages twisted SMC with an approximate locally optimal proposal,
obtained via a first-order Taylor expansion of the reward function. To address
the challenge of ill-defined gradients in discrete spaces, we incorporate a
Gumbel-Softmax relaxation, enabling efficient gradient-based approximation
within the discrete generative framework. Empirical results on both synthetic
datasets and image modelling validate the effectiveness of our approach.


### Outsourced diffusion sampling: Efficient posterior inference in latent spaces of generative models
**Authors**: Siddarth Venkatraman, Mohsin Hasan, Minsu Kim, Luca Scimeca, Marcin Sendera, Yoshua Bengio, Glen Berseth, Nikolay Malkin

**Published Date**: 2025-02-10

**Updated Date**: 2025-05-28

**PDF Url**: [2502.06999v2](http://arxiv.org/pdf/2502.06999v2)

**Abstract**: Any well-behaved generative model over a variable $\mathbf{x}$ can be
expressed as a deterministic transformation of an exogenous ('outsourced')
Gaussian noise variable $\mathbf{z}$: $\mathbf{x}=f_\theta(\mathbf{z})$. In
such a model (\eg, a VAE, GAN, or continuous-time flow-based model), sampling
of the target variable $\mathbf{x} \sim p_\theta(\mathbf{x})$ is
straightforward, but sampling from a posterior distribution of the form
$p(\mathbf{x}\mid\mathbf{y}) \propto
p_\theta(\mathbf{x})r(\mathbf{x},\mathbf{y})$, where $r$ is a constraint
function depending on an auxiliary variable $\mathbf{y}$, is generally
intractable. We propose to amortize the cost of sampling from such posterior
distributions with diffusion models that sample a distribution in the noise
space ($\mathbf{z}$). These diffusion samplers are trained by reinforcement
learning algorithms to enforce that the transformed samples
$f_\theta(\mathbf{z})$ are distributed according to the posterior in the data
space ($\mathbf{x}$). For many models and constraints, the posterior in noise
space is smoother than in data space, making it more suitable for amortized
inference. Our method enables conditional sampling under unconditional GAN,
(H)VAE, and flow-based priors, comparing favorably with other inference
methods. We demonstrate the proposed outsourced diffusion sampling in several
experiments with large pretrained prior models: conditional image generation,
reinforcement learning with human feedback, and protein structure generation.


### Inference-Time Scaling for Flow Models via Stochastic Generation and Rollover Budget Forcing
**Authors**: Jaihoon Kim, Taehoon Yoon, Jisung Hwang, Minhyuk Sung

**Published Date**: 2025-03-25

**Updated Date**: 2025-05-28

**PDF Url**: [2503.19385v4](http://arxiv.org/pdf/2503.19385v4)

**Abstract**: We propose an inference-time scaling approach for pretrained flow models.
Recently, inference-time scaling has gained significant attention in LLMs and
diffusion models, improving sample quality or better aligning outputs with user
preferences by leveraging additional computation. For diffusion models,
particle sampling has allowed more efficient scaling due to the stochasticity
at intermediate denoising steps. On the contrary, while flow models have gained
popularity as an alternative to diffusion models--offering faster generation
and high-quality outputs in state-of-the-art image and video generative
models--efficient inference-time scaling methods used for diffusion models
cannot be directly applied due to their deterministic generative process. To
enable efficient inference-time scaling for flow models, we propose three key
ideas: 1) SDE-based generation, enabling particle sampling in flow models, 2)
Interpolant conversion, broadening the search space and enhancing sample
diversity, and 3) Rollover Budget Forcing (RBF), an adaptive allocation of
computational resources across timesteps to maximize budget utilization. Our
experiments show that SDE-based generation, particularly variance-preserving
(VP) interpolant-based generation, improves the performance of particle
sampling methods for inference-time scaling in flow models. Additionally, we
demonstrate that RBF with VP-SDE achieves the best performance, outperforming
all previous inference-time scaling approaches.


