# Abstracts of Papers

## Physics
### Exact overlaps for "all" integrable matrix product states of rational spin chains
**Authors**: Tamas Gombor

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23282v1](http://arxiv.org/pdf/2410.23282v1)

**Abstract**: The overlaps between integrable matrix product states (MPS) and Bethe states
are important in both the non-equilibrium statistical physics and the AdS/CFT
duality. We present the general MPS overlap formula. The result is a product of
a ratio of Gaudin determinants and a prefactor. The Gaudin determinants depend
on the spin chain but not on the MPS. The MPS dependent prefactor is given for
all integrable MPS of the $\mathfrak{gl}_{N}$, $\mathfrak{o}_{N}$ and
$\mathfrak{sp}_{N}$ symmetric spin chains with arbitrary representations.


### Slow Relaxation in a Glassy Quantum Circuit
**Authors**: Richard D. Barney, Yunxiang Liao, Victor Galitski

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23281v1](http://arxiv.org/pdf/2410.23281v1)

**Abstract**: Quantum circuits have become a powerful tool in the study of many-body
quantum physics, providing insights into both fast-thermalizing chaotic and
non-thermalizing integrable many-body dynamics. In this work, we explore a
distinct intermediate class - glassy quantum systems - where thermalization
occurs, but over very long timescales. We introduce and analyze a Floquet
random quantum circuit that can be tuned between glassy and fully ergodic
behavior through a single adjustable parameter. This circuit can be understood
as the unitary analog of the block Rosenzweig-Porter model, which is defined by
a Hamiltonian. Using an effective field theory for random quantum circuits, we
analyze the correlations between quasienergy eigenstates and thereby determine
the time evolution of the disorder-averaged density matrix. In the intermediate
regime the circuit displays a two-step thermalization process: an initial
relaxation within weakly coupled sectors followed by a later, global
thermalization. We also show that the ramp of the spectral form factor is
enhanced by a factor of the number of sectors in the glassy regime, and at
early times in the intermediate regime. These results indicate that quantum
circuits provide an ideal platform for the exploration of nontrivial
thermalization dynamics in many-body quantum systems, offering deeper insights
into quantum thermalization.


### A little less conversation, a little more action, please: Investigating the physical common-sense of LLMs in a 3D embodied environment
**Authors**: Matteo G. Mecattaf, Ben Slater, Marko Tešić, Jonathan Prunty, Konstantinos Voudouris, Lucy G. Cheke

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23242v1](http://arxiv.org/pdf/2410.23242v1)

**Abstract**: As general-purpose tools, Large Language Models (LLMs) must often reason
about everyday physical environments. In a question-and-answer capacity,
understanding the interactions of physical objects may be necessary to give
appropriate responses. Moreover, LLMs are increasingly used as reasoning
engines in agentic systems, designing and controlling their action sequences.
The vast majority of research has tackled this issue using static benchmarks,
comprised of text or image-based questions about the physical world. However,
these benchmarks do not capture the complexity and nuance of real-life physical
processes. Here we advocate for a second, relatively unexplored, approach:
'embodying' the LLMs by granting them control of an agent within a 3D
environment. We present the first embodied and cognitively meaningful
evaluation of physical common-sense reasoning in LLMs. Our framework allows
direct comparison of LLMs with other embodied agents, such as those based on
Deep Reinforcement Learning, and human and non-human animals. We employ the
Animal-AI (AAI) environment, a simulated 3D virtual laboratory, to study
physical common-sense reasoning in LLMs. For this, we use the AAI Testbed, a
suite of experiments that replicate laboratory studies with non-human animals,
to study physical reasoning capabilities including distance estimation,
tracking out-of-sight objects, and tool use. We demonstrate that
state-of-the-art multi-modal models with no finetuning can complete this style
of task, allowing meaningful comparison to the entrants of the 2019 Animal-AI
Olympics competition and to human children. Our results show that LLMs are
currently outperformed by human children on these tasks. We argue that this
approach allows the study of physical reasoning using ecologically valid
experiments drawn directly from cognitive science, improving the predictability
and reliability of LLMs.


### Super-resolution in disordered media using neural networks
**Authors**: Alexander Christie, Matan Leibovich, Miguel Moscoso, Alexei Novikov, George Papanicolaou, Chrysoula Tsogka

**Published Date**: 2024-10-28

**Updated Date**: 2024-10-30

**PDF Url**: [2410.21556v2](http://arxiv.org/pdf/2410.21556v2)

**Abstract**: We propose a methodology that exploits large and diverse data sets to
accurately estimate the ambient medium's Green's functions in strongly
scattering media. Given these estimates, obtained with and without the use of
neural networks, excellent imaging results are achieved, with a resolution that
is better than that of a homogeneous medium. This phenomenon, also known as
super-resolution, occurs because the ambient scattering medium effectively
enhances the physical imaging aperture.


### HGPflow: Extending Hypergraph Particle Flow to Collider Event Reconstruction
**Authors**: Nilotpal Kakati, Etienne Dreyer, Anna Ivina, Francesco Armando Di Bello, Lukas Heinrich, Marumi Kado, Eilam Gross

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23236v1](http://arxiv.org/pdf/2410.23236v1)

**Abstract**: In high energy physics, the ability to reconstruct particles based on their
detector signatures is essential for downstream data analyses. A particle
reconstruction algorithm based on learning hypergraphs (HGPflow) has previously
been explored in the context of single jets. In this paper, we expand the scope
to full proton-proton and electron-positron collision events and study
reconstruction quality using metrics at the particle, jet, and event levels.
Rather than operating on the entire event in a single pass, we train HGPflow on
smaller partitions to avoid potentially learning long-range correlations
related to the physics process. We demonstrate that this approach is feasible
and that on most metrics, HGPflow outperforms both traditional particle flow
algorithms and a machine learning-based benchmark model.


### Kinetix: Investigating the Training of General Agents through Open-Ended Physics-Based Control Tasks
**Authors**: Michael Matthews, Michael Beukman, Chris Lu, Jakob Foerster

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23208v1](http://arxiv.org/pdf/2410.23208v1)

**Abstract**: While large models trained with self-supervised learning on offline datasets
have shown remarkable capabilities in text and image domains, achieving the
same generalisation for agents that act in sequential decision problems remains
an open challenge. In this work, we take a step towards this goal by
procedurally generating tens of millions of 2D physics-based tasks and using
these to train a general reinforcement learning (RL) agent for physical
control. To this end, we introduce Kinetix: an open-ended space of
physics-based RL environments that can represent tasks ranging from robotic
locomotion and grasping to video games and classic RL environments, all within
a unified framework. Kinetix makes use of our novel hardware-accelerated
physics engine Jax2D that allows us to cheaply simulate billions of environment
steps during training. Our trained agent exhibits strong physical reasoning
capabilities, being able to zero-shot solve unseen human-designed environments.
Furthermore, fine-tuning this general agent on tasks of interest shows
significantly stronger performance than training an RL agent *tabula rasa*.
This includes solving some environments that standard RL training completely
fails at. We believe this demonstrates the feasibility of large scale,
mixed-quality pre-training for online RL and we hope that Kinetix will serve as
a useful framework to investigate this further.


### Classically studied coherent structures only paint a partial picture of wall-bounded turbulence
**Authors**: Andrés Cremades, Sergio Hoyas, Ricardo Vinuesa

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23189v1](http://arxiv.org/pdf/2410.23189v1)

**Abstract**: For the last 140 years, the mechanisms of transport and dissipation of energy
in a turbulent flow have not been completely understood due to the complexity
of this phenomenon. The dissipation of energy due to turbulence is
significative, and understanding turbulence physics is crucial for fighting the
present climate emergency. Previous research has focused on analyzing the
so-called coherent structures of the flow (Q events, streaks, and vortices),
which are regions of high turbulence transport, high/low streamwise
fluctuation, and rotation, respectively. However, the connection between these
classically studied structures and the flow development is still uncertain. To
fill this gap, here we show a data-driven methodology for objectively
identifying high-importance regions in a turbulent flow. A deep-learning model
is trained to predict a future state of a turbulent channel flow and the
gradient-SHAP explainability algorithm is used to calculate the importance of
each grid point for such a prediction. Finally, high-importance regions are
computed using the SHAP data, analyzing and comparing their characteristics
with those of the other coherent structures. The SHAP analysis provides an
objective way to identify the regions of highest importance in the turbulent
flow, which exhibit different levels of agreement with the classically studied
structures.


### Double BFV quantisation of 3d Gravity
**Authors**: Giovanni Canepa, Michele Schiavina

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23184v1](http://arxiv.org/pdf/2410.23184v1)

**Abstract**: We extend the cohomological setting developed by Batalin, Fradkin and
Vilkovisky to the case of a nested coisotropic embedding $C\hookrightarrow
C_\circ \hookrightarrow F$ inside a symplectic manifold $F$.
  To this, we naturally assign the coisotropic reductions $\pi\colon C\to
\underline{C}$, as well as $\pi_\circ\colon C_\circ\to\underline{C_\circ}$ and
the residual reduction $\pi_{\mathrm{res}}\colon C_{\mathrm{res}}\to
\underline{C_{\mathrm{res}}}$, where
$C_{\mathrm{res}}=\pi_\circ(C)\hookrightarrow \underline{C_\circ}$ is the
residual coisotropic embedding such that $\underline{C_{\mathrm{res}}}\simeq
\underline{C}$.
  We show that there is a relation between the BFV resolutions of
$\underline{C_\circ}$ and $\underline{C}$, in terms of a graded coisotropic
embedding, which can further be resolved via BFV.
  We call this construction \emph{double BFV resolution}, and we use it to
prove that "resolution commutes with reduction". We then deduce a quantisation
of $\underline{C}\simeq\underline{C_{\mathrm{res}}}$, from a quantisation of
the double BFV Hamiltonian dg manifold following the quantum BFV prescription
(when it exists). As an application, we provide a well defined candidate space
of (physical) quantum states of three-dimensional Einstein--Hilbert theory,
which is thought of as a partial reduction of the Palatini--Cartan model for
gravity.


### A Low-Cost, Low-Power Media Converter Solution for Next-Generation Detector Readout Systems
**Authors**: Alberto Perro, Mitja Vodnik, Paolo Durante

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23173v1](http://arxiv.org/pdf/2410.23173v1)

**Abstract**: High Energy Physics (HEP) data acquisition systems are often built from
high-end FPGAs. As such systems scale in the HL-LHC era, severe
under-utilization of FPGA transceivers can occur because front-end links
prioritize radiation hardness and power consumption over raw data bandwidth.
This work evaluates recently introduced low-power, low-cost FPGA devices as an
alternative building block for future readout architectures. This study
presents the implementation of a readout back-End on FPGA where the front-end
protocol is based on the Low-Power GigaBit Transceiver (lpGBT) and the readout
protocol is based on 10 Gigabit Ethernet, using the LHCb Run 4 RICH detector as
a practical case study.


### When can classical neural networks represent quantum states?
**Authors**: Tai-Hsuan Yang, Mehdi Soleimanifar, Thiago Bergamaschi, John Preskill

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23152v1](http://arxiv.org/pdf/2410.23152v1)

**Abstract**: A naive classical representation of an n-qubit state requires specifying
exponentially many amplitudes in the computational basis. Past works have
demonstrated that classical neural networks can succinctly express these
amplitudes for many physically relevant states, leading to computationally
powerful representations known as neural quantum states. What underpins the
efficacy of such representations? We show that conditional correlations present
in the measurement distribution of quantum states control the performance of
their neural representations. Such conditional correlations are basis
dependent, arise due to measurement-induced entanglement, and reveal features
not accessible through conventional few-body correlations often examined in
studies of phases of matter. By combining theoretical and numerical analysis,
we demonstrate how the state's entanglement and sign structure, along with the
choice of measurement basis, give rise to distinct patterns of short- or
long-range conditional correlations. Our findings provide a rigorous framework
for exploring the expressive power of neural quantum states.


## Diffusion
### Provable acceleration for diffusion models under minimal assumptions
**Authors**: Gen Li, Changxiao Cai

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23285v1](http://arxiv.org/pdf/2410.23285v1)

**Abstract**: While score-based diffusion models have achieved exceptional sampling
quality, their sampling speeds are often limited by the high computational
burden of score function evaluations. Despite the recent remarkable empirical
advances in speeding up the score-based samplers, theoretical understanding of
acceleration techniques remains largely limited. To bridge this gap, we propose
a novel training-free acceleration scheme for stochastic samplers. Under
minimal assumptions -- namely, $L^2$-accurate score estimates and a finite
second-moment condition on the target distribution -- our accelerated sampler
provably achieves $\varepsilon$-accuracy in total variation within
$\widetilde{O}(d^{5/4}/\sqrt{\varepsilon})$ iterations, thereby significantly
improving upon the $\widetilde{O}(d/\varepsilon)$ iteration complexity of
standard score-based samplers. Notably, our convergence theory does not rely on
restrictive assumptions on the target distribution or higher-order score
estimation guarantees.


### SlowFast-VGen: Slow-Fast Learning for Action-Driven Long Video Generation
**Authors**: Yining Hong, Beide Liu, Maxine Wu, Yuanhao Zhai, Kai-Wei Chang, Lingjie Li, Kevin Lin, Chung-Ching Lin, Jianfeng Wang, Zhengyuan Yang, Yingnian Wu, Lijuan Wang

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23277v1](http://arxiv.org/pdf/2410.23277v1)

**Abstract**: Human beings are endowed with a complementary learning system, which bridges
the slow learning of general world dynamics with fast storage of episodic
memory from a new experience. Previous video generation models, however,
primarily focus on slow learning by pre-training on vast amounts of data,
overlooking the fast learning phase crucial for episodic memory storage. This
oversight leads to inconsistencies across temporally distant frames when
generating longer videos, as these frames fall beyond the model's context
window. To this end, we introduce SlowFast-VGen, a novel dual-speed learning
system for action-driven long video generation. Our approach incorporates a
masked conditional video diffusion model for the slow learning of world
dynamics, alongside an inference-time fast learning strategy based on a
temporal LoRA module. Specifically, the fast learning process updates its
temporal LoRA parameters based on local inputs and outputs, thereby efficiently
storing episodic memory in its parameters. We further propose a slow-fast
learning loop algorithm that seamlessly integrates the inner fast learning loop
into the outer slow learning loop, enabling the recall of prior multi-episode
experiences for context-aware skill learning. To facilitate the slow learning
of an approximate world model, we collect a large-scale dataset of 200k videos
with language action annotations, covering a wide range of scenarios. Extensive
experiments show that SlowFast-VGen outperforms baselines across various
metrics for action-driven video generation, achieving an FVD score of 514
compared to 782, and maintaining consistency in longer videos, with an average
of 0.37 scene cuts versus 0.89. The slow-fast learning loop algorithm
significantly enhances performances on long-horizon planning tasks as well.
Project Website: https://slowfast-vgen.github.io


### Multi-student Diffusion Distillation for Better One-step Generators
**Authors**: Yanke Song, Jonathan Lorraine, Weili Nie, Karsten Kreis, James Lucas

**Published Date**: 2024-10-30

**Updated Date**: 2024-10-30

**PDF Url**: [2410.23274v1](http://arxiv.org/pdf/2410.23274v1)

**Abstract**: Diffusion models achieve high-quality sample generation at the cost of a
lengthy multistep inference procedure. To overcome this, diffusion distillation
techniques produce student generators capable of matching or surpassing the
teacher in a single step. However, the student model's inference speed is
limited by the size of the teacher architecture, preventing real-time
generation for computationally heavy applications. In this work, we introduce
Multi-Student Distillation (MSD), a framework to distill a conditional teacher
diffusion model into multiple single-step generators. Each student generator is
responsible for a subset of the conditioning data, thereby obtaining higher
generation quality for the same capacity. MSD trains multiple distilled
students, allowing smaller sizes and, therefore, faster inference. Also, MSD
offers a lightweight quality boost over single-student distillation with the
same architecture. We demonstrate MSD is effective by training multiple
same-sized or smaller students on single-step distillation using distribution
matching and adversarial distillation techniques. With smaller students, MSD
gets competitive results with faster inference for single-step generation.
Using 4 same-sized students, MSD sets a new state-of-the-art for one-step image
generation: FID 1.20 on ImageNet-64x64 and 8.20 on zero-shot COCO2014.


### Optimal deep learning of holomorphic operators between Banach spaces
**Authors**: Ben Adcock, Nick Dexter, Sebastian Moraga

**Published Date**: 2024-06-20

**Updated Date**: 2024-10-30

**PDF Url**: [2406.13928v2](http://arxiv.org/pdf/2406.13928v2)

**Abstract**: Operator learning problems arise in many key areas of scientific computing
where Partial Differential Equations (PDEs) are used to model physical systems.
In such scenarios, the operators map between Banach or Hilbert spaces. In this
work, we tackle the problem of learning operators between Banach spaces, in
contrast to the vast majority of past works considering only Hilbert spaces. We
focus on learning holomorphic operators - an important class of problems with
many applications. We combine arbitrary approximate encoders and decoders with
standard feedforward Deep Neural Network (DNN) architectures - specifically,
those with constant width exceeding the depth - under standard $\ell^2$-loss
minimization. We first identify a family of DNNs such that the resulting Deep
Learning (DL) procedure achieves optimal generalization bounds for such
operators. For standard fully-connected architectures, we then show that there
are uncountably many minimizers of the training problem that yield equivalent
optimal performance. The DNN architectures we consider are `problem agnostic',
with width and depth only depending on the amount of training data $m$ and not
on regularity assumptions of the target operator. Next, we show that DL is
optimal for this problem: no recovery procedure can surpass these
generalization bounds up to log terms. Finally, we present numerical results
demonstrating the practical performance on challenging problems including the
parametric diffusion, Navier-Stokes-Brinkman and Boussinesq PDEs.


### MemControl: Mitigating Memorization in Diffusion Models via Automated Parameter Selection
**Authors**: Raman Dutt, Ondrej Bohdal, Pedro Sanchez, Sotirios A. Tsaftaris, Timothy Hospedales

**Published Date**: 2024-05-29

**Updated Date**: 2024-10-30

**PDF Url**: [2405.19458v2](http://arxiv.org/pdf/2405.19458v2)

**Abstract**: Diffusion models excel in generating images that closely resemble their
training data but are also susceptible to data memorization, raising privacy,
ethical, and legal concerns, particularly in sensitive domains such as medical
imaging. We hypothesize that this memorization stems from the
overparameterization of deep models and propose that regularizing model
capacity during fine-tuning can mitigate this issue. Firstly, we empirically
show that regulating the model capacity via Parameter-efficient fine-tuning
(PEFT) mitigates memorization to some extent, however, it further requires the
identification of the exact parameter subsets to be fine-tuned for high-quality
generation. To identify these subsets, we introduce a bi-level optimization
framework, MemControl, that automates parameter selection using memorization
and generation quality metrics as rewards during fine-tuning. The parameter
subsets discovered through MemControl achieve a superior tradeoff between
generation quality and memorization. For the task of medical image generation,
our approach outperforms existing state-of-the-art memorization mitigation
strategies by fine-tuning as few as 0.019% of model parameters. Moreover, we
demonstrate that the discovered parameter subsets are transferable to
non-medical domains. Our framework is scalable to large datasets, agnostic to
reward functions, and can be integrated with existing approaches for further
memorization mitigation. To the best of our knowledge, this is the first study
to empirically evaluate memorization in medical images and propose a targeted
yet universal mitigation strategy. The code is available at
https://github.com/Raman1121/Diffusion_Memorization_HPO


## Quantitative Finance
### FinTeamExperts: Role Specialized MOEs For Financial Analysis
**Authors**: Yue Yu, Prayag Tiwari

**Published Date**: 2024-10-28

**Updated Date**: 2024-10-28

**PDF Url**: [2410.21338v1](http://arxiv.org/pdf/2410.21338v1)

**Abstract**: Large Language Models (LLMs), such as ChatGPT, Phi3 and Llama-3, are leading
a significant leap in AI, as they can generalize knowledge from their training
to new tasks without fine-tuning. However, their application in the financial
domain remains relatively limited. The financial field is inherently complex,
requiring a deep understanding across various perspectives, from macro, micro
economic trend to quantitative analysis. Motivated by this complexity, a
mixture of expert LLMs tailored to specific financial domains could offer a
more comprehensive understanding for intricate financial tasks. In this paper,
we present the FinTeamExperts, a role-specialized LLM framework structured as a
Mixture of Experts (MOEs) for financial analysis. The framework simulates a
collaborative team setting by training each model to specialize in distinct
roles: Macro Analysts, Micro analysts, and Quantitative Analysts. This
role-specific specialization enhances the model's ability to integrate their
domain-specific expertise. We achieve this by training three 8-billion
parameter models on different corpus, each dedicated to excelling in specific
finance-related roles. We then instruct-tune FinTeamExperts on downstream tasks
to align with practical financial tasks. The experimental results show that
FinTeamExperts outperform all models of the same size and larger on three out
of four datasets. On the fourth dataset, which presents a more complex task,
FinTeamExperts still surpass all models of the same size. This highlights the
success of our role-based specialization approach and the continued training
approach for FinTeamExperts.


