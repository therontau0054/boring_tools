# Abstracts of Papers

## Physics
### Quantum algorithm for the gradient of a logarithm-determinant
**Authors**: Thomas E. Baker, Jaimie Greasley

**Published Date**: 2025-01-16

**Updated Date**: 2025-04-16

**PDF Url**: [2501.09413v2](http://arxiv.org/pdf/2501.09413v2)

**Abstract**: The logarithm-determinant is a common quantity in many areas of physics and
computer science. Derivatives of the logarithm-determinant compute physically
relevant quantities in statistical physics models, quantum field theories, as
well as the inverses of matrices. A multi-variable version of the quantum
gradient algorithm is developed here to evaluate the derivative of the
logarithm-determinant. From this, the inverse of a sparse-rank input operator
may be determined efficiently. Measuring an expectation value of the quantum
state--instead of all $N^2$ elements of the input operator--can be accomplished
in $O(k\sigma)$ time in the idealized case for $k$ relevant eigenvectors of the
input matrix. A factor $\sigma=\frac1{\varepsilon^3}$ or
$-\frac1{\varepsilon^2}\log_2\varepsilon$ depends on the version of the quantum
Fourier transform used for a precision $\varepsilon$. Practical implementation
of the required operator will likely need $\log_2N$ overhead, giving an overall
complexity of $O(k\sigma\log_2 N)$. The method applies widely and converges
super-linearly in $k$ when the condition number is high. The best classical
method we are aware of scales as $N$.
  Given the same resource assumptions as other algorithms, such that an equal
superposition of eigenvectors is available efficiently, the algorithm is
evaluated in the practical case as $O(\sigma\log_2 N)$. The output is given in
$O(1)$ queries of oracle, which is given explicitly here and only relies on
time-evolution operators that can be implemented with arbitrarily small error.
The algorithm is envisioned for fully error-corrected quantum computers but may
be implementable on near-term machines. We discuss how this algorithm can be
used for kernel-based quantum machine-learning.


### QSHS: An Axion Dark Matter Resonant Search Apparatus
**Authors**: A. Alsulami, I. Bailey, G. Carosi, G. Chapman, B. Chakraborty, E. J. Daw, N. Duc, S. Durham, J. Esmenda, J. Gallop, T. Gamble, T. Godfrey, G. Gregori, J. Halliday, L. Hao, E. Hardy, E. A. Laird, P. Leek, J. March-Russell, P. J. Meeson, C. F. Mostyn, Yu. A. Pashkin, S. O. Peatain, M. Perry, M. Piscitelli, M. Reig, E. J. Romans, S. Sarkar, P. J. Smith, A. Sokolov, N. Song, A. Sundararajan, B. -K Tan, S. M. West, S. Withington

**Published Date**: 2025-04-16

**Updated Date**: 2025-04-16

**PDF Url**: [2504.12257v1](http://arxiv.org/pdf/2504.12257v1)

**Abstract**: We describe a resonant cavity search apparatus for axion dark matter
constructed by the Quantum Sensors for the Hidden Sector (QSHS) collaboration.
The apparatus is configured to search for QCD axion dark matter, though also
has the capability to detect axion-like particles (ALPs), dark photons, and
some other forms of wave-like dark matter. Initially, a tuneable cylindrical
oxygen-free copper cavity is read out using a low noise microwave amplifier
feeding a heterodyne receiver. The cavity is housed in a dilution refrigerator
and threaded by a solenoidal magnetic field, nominally 8T. The apparatus also
houses a magnetic field shield for housing superconducting electronics, and
several other fixed-frequency resonators for use in testing and commissioning
various prototype quantum electronic devices sensitive at a range of axion
masses in the range $\rm 2.0$ to $\rm 40\,eV/c^2$. We present performance data
for the resonator, dilution refrigerator, and magnet, and plans for the first
science run.


### MFC 5.0: An exascale many-physics flow solver
**Authors**: Benjamin Wilfong, Henry A. Le Berre, Anand Radhakrishnan, Ansh Gupta, Diego Vaca-Revelo, Dimitrios Adam, Haocheng Yu, Hyeoksu Lee, Jose Rodolfo Chreim, Mirelys Carcana Barbosa, Yanjun Zhang, Esteban Cisneros-Garibay, Aswin Gnanaskandan, Mauro Rodriguez Jr., Reuben D. Budiardja, Stephen Abbott, Tim Colonius, Spencer H. Bryngelson

**Published Date**: 2025-03-11

**Updated Date**: 2025-04-16

**PDF Url**: [2503.07953v3](http://arxiv.org/pdf/2503.07953v3)

**Abstract**: Many problems of interest in engineering, medicine, and the fundamental
sciences rely on high-fidelity flow simulation, making performant computational
fluid dynamics solvers a mainstay of the open-source software community. A
previous work (Bryngelson et al., Comp. Phys. Comm. (2021)) published MFC 3.0
with numerous physical features, numerics, and scalability. MFC 5.0 is a marked
update to MFC 3.0, including a broad set of well-established and novel physical
models and numerical methods, and the introduction of XPU acceleration. We
exhibit state-of-the-art performance and ideal scaling on the first two
exascale supercomputers, OLCF Frontier and LLNL El Capitan. Combined with MFC's
single-accelerator performance, MFC achieves exascale computation in practice.
New physical features include the immersed boundary method, N-fluid phase
change, Euler--Euler and Euler--Lagrange sub-grid bubble models,
fluid-structure interaction, hypo- and hyper-elastic materials, chemically
reacting flow, two-material surface tension, magnetohydrodynamics (MHD), and
more. Numerical techniques now represent the current state-of-the-art,
including general relaxation characteristic boundary conditions, WENO variants,
Strang splitting for stiff sub-grid flow features, and low Mach number
treatments. Weak scaling to tens of thousands of GPUs on OLCF Summit and
Frontier and LLNL El Capitan sees efficiencies within 5% of ideal to their full
system sizes. Strong scaling results for a 16-times increase in device count
show parallel efficiencies over 90% on OLCF Frontier. MFC's software stack has
improved, including continuous integration, ensuring code resilience and
correctness through over 300 regression tests; metaprogramming, reducing code
length and maintaining performance portability; and code generation for
computing chemical reactions.


### Exceptional deficiency of non-Hermitian systems: high-dimensional coalescence and dynamics
**Authors**: Zhen Li, Xulong Wang, Rundong Cai, Kenji Shimomura, Zhesen Yang, Masatoshi Sato, Guancong Ma

**Published Date**: 2025-04-16

**Updated Date**: 2025-04-16

**PDF Url**: [2504.12238v1](http://arxiv.org/pdf/2504.12238v1)

**Abstract**: Exceptional points (EPs) are non-Hermitian singularities associated with the
coalescence of individual eigenvectors accompanied by the degeneracy of their
complex energies. Here, we report the discovery of a generalization to the
concept of EP called exceptional deficiency (ED), which features the complete
coalescence of two eigenspaces with identical but arbitrarily large dimensions
and the coincidence of entire spectral continua. The characteristics of the ED
are studied using one-way coupled Hermitian and non-Hermitian lattices. The ED
can induce an anomalous absence and presence of non-Hermitian skin effect
(NHSE) that transcends the topological bulk-edge correspondence of NHSE,
resulting in unexpected synergistic skin-propagative dynamics. The conditions
of the ED are also explored for unprecedented control of localization and
propagation in non-Hermitian systems. These effects are experimentally observed
using active mechanical lattices. The discovery of ED opens multiple new
frontiers in non-Hermitian physics and can potentially resolve long-standing
challenges in related applications.


### Multimodal Lego: Model Merging and Fine-Tuning Across Topologies and Modalities in Biomedicine
**Authors**: Konstantin Hemker, Nikola Simidjievski, Mateja Jamnik

**Published Date**: 2024-05-30

**Updated Date**: 2025-04-16

**PDF Url**: [2405.19950v2](http://arxiv.org/pdf/2405.19950v2)

**Abstract**: Learning holistic computational representations in physical, chemical or
biological systems requires the ability to process information from different
distributions and modalities within the same model. Thus, the demand for
multimodal machine learning models has sharply risen for modalities that go
beyond vision and language, such as sequences, graphs, time series, or tabular
data. While there are many available multimodal fusion and alignment
approaches, most of them require end-to-end training, scale quadratically with
the number of modalities, cannot handle cases of high modality imbalance in the
training set, or are highly topology-specific, making them too restrictive for
many biomedical learning tasks. This paper presents Multimodal Lego (MM-Lego),
a general-purpose fusion framework to turn any set of encoders into a
competitive multimodal model with no or minimal fine-tuning. We achieve this by
introducing a wrapper for any unimodal encoder that enforces shape consistency
between modality representations. It harmonises these representations by
learning features in the frequency domain to enable model merging with little
signal interference. We show that MM-Lego 1) can be used as a model merging
method which achieves competitive performance with end-to-end fusion models
without any fine-tuning, 2) can operate on any unimodal encoder, and 3) is a
model fusion method that, with minimal fine-tuning, surpasses all benchmarks in
five out of seven datasets.


### Using skateboarding to develop a culturally relevant tutorial on static equilibrium
**Authors**: Gian Viray, Isaac Cheney, Tong Wan

**Published Date**: 2024-06-25

**Updated Date**: 2025-04-16

**PDF Url**: [2406.17625v3](http://arxiv.org/pdf/2406.17625v3)

**Abstract**: Culturally relevant pedagogy (CRP), initially developed by Ladson-Billings,
is an instructional framework for supporting diverse learners by drawing on
their cultural backgrounds and experiences. In line with the CRP framework, we
developed a tutorial on static equilibrium using skateboarding, a popular
activity on university campuses, as a culturally relevant context. To help
students refine their conceptions about static equilibrium documented in the
physics education research (PER) literature, we used the
elicit-confront-resolve (ECR) strategy to develop the tutorial. In this paper,
we provide a detailed account of how we operationalized the ECR strategy in
designing the sequences of questions in the tutorial. Additionally, we present
anecdotal evidence to show that this research-based culturally relevant
tutorial appears to effectively engage students and motivate their interest in
learning physics.


### Non-Hermitian Numerical Renormalization Group: Solution of the non-Hermitian Kondo model
**Authors**: Phillip C. Burke, Andrew K. Mitchell

**Published Date**: 2025-04-09

**Updated Date**: 2025-04-16

**PDF Url**: [2504.07019v2](http://arxiv.org/pdf/2504.07019v2)

**Abstract**: Non-Hermitian (NH) Hamiltonians describe open quantum systems, nonequilibrium
dynamics, and dissipative processes. Although a rich range of single-particle
NH physics has been uncovered, many-body phenomena in strongly correlated NH
systems have been far less well studied. The Kondo effect, an important
paradigm for strong correlation physics, has recently been considered in the NH
setting. Here we develop a NH generalization of the numerical renormalization
group (NRG) and use it to solve the NH Kondo model. Our non-perturbative
solution applies beyond weak coupling, and we uncover a nontrivial phase
diagram. The method is showcased by application to the NH pseudogap Kondo
model, which we show supports a completely novel phase with a genuine NH stable
fixed point and complex eigenspectrum. Our NH-NRG code, which can be used in
regimes and for models inaccessible to, e.g., perturbative scaling and Bethe
ansatz, is provided open source.


### Care for the Mind Amid Chronic Diseases: An Interpretable AI Approach Using IoT
**Authors**: Jiaheng Xie, Xiaohang Zhao, Xiang Liu, Xiao Fang

**Published Date**: 2022-11-08

**Updated Date**: 2025-04-16

**PDF Url**: [2211.04509v2](http://arxiv.org/pdf/2211.04509v2)

**Abstract**: Health sensing for chronic disease management creates immense benefits for
social welfare. Existing health sensing studies primarily focus on the
prediction of physical chronic diseases. Depression, a widespread complication
of chronic diseases, is however understudied. We draw on the medical literature
to support depression detection using motion sensor data. To connect humans in
this decision-making, safeguard trust, and ensure algorithm transparency, we
develop an interpretable deep learning model: Temporal Prototype Network
(TempPNet). TempPNet is built upon the emergent prototype learning models. To
accommodate the temporal characteristic of sensor data and the progressive
property of depression, TempPNet differs from existing prototype learning
models in its capability of capturing temporal progressions of prototypes.
Extensive empirical analyses using real-world motion sensor data show that
TempPNet outperforms state-of-the-art benchmarks in depression detection.
Moreover, TempPNet interprets its decision by visualizing the temporal
progression of depression and its corresponding symptoms detected from sensor
data. We further employ a user study and a medical expert panel to demonstrate
its superiority over the benchmarks in interpretability. This study offers an
algorithmic solution for impactful social good -- collaborative care of chronic
diseases and depression in health sensing. Methodologically, it contributes to
extant literature with a novel interpretable deep learning model for depression
detection from sensor data. Patients, doctors, and caregivers can deploy our
model on mobile devices to monitor patients' depression risks in real-time. Our
model's interpretability also allows human experts to participate in the
decision-making by reviewing the interpretation and making informed
interventions.


### Correlations as a resource in molecular switches
**Authors**: Daniel Siciliano, Rudi B. P. Pietsch, Giovanni Spaventa, Susana F. Huelga, Martin B. Plenio

**Published Date**: 2025-04-16

**Updated Date**: 2025-04-16

**PDF Url**: [2504.12202v1](http://arxiv.org/pdf/2504.12202v1)

**Abstract**: Photoisomerization, a photochemical process underlying many biological
mechanisms, has been modeled recently within the quantum resource theory of
thermodynamics. This approach has emerged as a promising tool for studying
fundamental limitations to nanoscale processes independently of the microscopic
details governing their dynamics. On the other hand, correlations between
physical systems have been shown to play a crucial role in quantum
thermodynamics by lowering the work cost of certain operations. Here, we
explore quantitatively how correlations between multiple photoswitches can
enhance the efficiency of photoisomerization beyond that attainable for single
molecules. Furthermore, our analysis provides insights into the interplay
between quantum and classical correlations in these transformations.


### Evidential Deep Learning for Interatomic Potentials
**Authors**: Han Xu, Taoyong Cui, Chenyu Tang, Jinzhe Ma, Dongzhan Zhou, Yuqiang Li, Xiang Gao, Xingao Gong, Wanli Ouyang, Shufei Zhang, Mao Su

**Published Date**: 2024-07-19

**Updated Date**: 2025-04-16

**PDF Url**: [2407.13994v2](http://arxiv.org/pdf/2407.13994v2)

**Abstract**: Machine learning interatomic potentials (MLIPs) have been widely used to
facilitate large-scale molecular simulations with accuracy comparable to ab
initio methods. In practice, MLIP-based molecular simulations often encounter
the issue of collapse due to reduced prediction accuracy for
out-of-distribution (OOD) data. Addressing this issue requires enriching the
training dataset through active learning, where uncertainty serves as a
critical indicator for identifying and collecting OOD data. However, existing
uncertainty quantification (UQ) methods tend to involve either expensive
computations or compromise prediction accuracy. In this work, we introduce
evidential deep learning for interatomic potentials (eIP) with a
physics-inspired design. Our experiments indicate that eIP provides reliable UQ
results without significant computational overhead or decreased prediction
accuracy, consistently outperforming other UQ methods across a variety of
datasets. Furthermore, we demonstrate the applications of eIP in exploring
diverse atomic configurations, using examples including water and universal
potentials. These results highlight the potential of eIP as a robust and
efficient alternative for UQ in molecular simulations.


## Diffusion
### How Do I Do That? Synthesizing 3D Hand Motion and Contacts for Everyday Interactions
**Authors**: Aditya Prakash, Benjamin Lundell, Dmitry Andreychuk, David Forsyth, Saurabh Gupta, Harpreet Sawhney

**Published Date**: 2025-04-16

**Updated Date**: 2025-04-16

**PDF Url**: [2504.12284v1](http://arxiv.org/pdf/2504.12284v1)

**Abstract**: We tackle the novel problem of predicting 3D hand motion and contact maps (or
Interaction Trajectories) given a single RGB view, action text, and a 3D
contact point on the object as input. Our approach consists of (1) Interaction
Codebook: a VQVAE model to learn a latent codebook of hand poses and contact
points, effectively tokenizing interaction trajectories, (2) Interaction
Predictor: a transformer-decoder module to predict the interaction trajectory
from test time inputs by using an indexer module to retrieve a latent
affordance from the learned codebook. To train our model, we develop a data
engine that extracts 3D hand poses and contact trajectories from the diverse
HoloAssist dataset. We evaluate our model on a benchmark that is 2.5-10X larger
than existing works, in terms of diversity of objects and interactions
observed, and test for generalization of the model across object categories,
action categories, tasks, and scenes. Experimental results show the
effectiveness of our approach over transformer & diffusion baselines across all
settings.


### d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning
**Authors**: Siyan Zhao, Devaansh Gupta, Qinqing Zheng, Aditya Grover

**Published Date**: 2025-04-16

**Updated Date**: 2025-04-16

**PDF Url**: [2504.12216v1](http://arxiv.org/pdf/2504.12216v1)

**Abstract**: Recent large language models (LLMs) have demonstrated strong reasoning
capabilities that benefits from online reinforcement learning (RL). These
capabilities have primarily been demonstrated within the left-to-right
autoregressive (AR) generation paradigm. In contrast, non-autoregressive
paradigms based on diffusion generate text in a coarse-to-fine manner. Although
recent diffusion-based large language models (dLLMs) have achieved competitive
language modeling performance compared to their AR counterparts, it remains
unclear if dLLMs can also leverage recent advances in LLM reasoning. To this
end, we propose d1, a framework to adapt pre-trained masked dLLMs into
reasoning models via a combination of supervised finetuning (SFT) and RL.
Specifically, we develop and extend techniques to improve reasoning in
pretrained dLLMs: (a) we utilize a masked SFT technique to distill knowledge
and instill self-improvement behavior directly from existing datasets, and (b)
we introduce a novel critic-free, policy-gradient based RL algorithm called
diffu-GRPO. Through empirical studies, we investigate the performance of
different post-training recipes on multiple mathematical and logical reasoning
benchmarks. We find that d1 yields the best performance and significantly
improves performance of a state-of-the-art dLLM.


### Score as Action: Fine-Tuning Diffusion Generative Models by Continuous-time Reinforcement Learning
**Authors**: Hanyang Zhao, Haoxian Chen, Ji Zhang, David D. Yao, Wenpin Tang

**Published Date**: 2025-02-03

**Updated Date**: 2025-04-16

**PDF Url**: [2502.01819v2](http://arxiv.org/pdf/2502.01819v2)

**Abstract**: Reinforcement learning from human feedback (RLHF), which aligns a diffusion
model with input prompt, has become a crucial step in building reliable
generative AI models. Most works in this area use a discrete-time formulation,
which is prone to induced errors, and often not applicable to models with
higher-order/black-box solvers. The objective of this study is to develop a
disciplined approach to fine-tune diffusion models using continuous-time RL,
formulated as a stochastic control problem with a reward function that aligns
the end result (terminal state) with input prompt. The key idea is to treat
score matching as controls or actions, and thereby making connections to policy
optimization and regularization in continuous-time RL. To carry out this idea,
we lay out a new policy optimization framework for continuous-time RL, and
illustrate its potential in enhancing the value networks design space via
leveraging the structural property of diffusion models. We validate the
advantages of our method by experiments in downstream tasks of fine-tuning
large-scale Text2Image models of Stable Diffusion v1.5.


### Fine-Tuning Diffusion Generative Models via Rich Preference Optimization
**Authors**: Hanyang Zhao, Haoxian Chen, Yucheng Guo, Genta Indra Winata, Tingting Ou, Ziyu Huang, David D. Yao, Wenpin Tang

**Published Date**: 2025-03-13

**Updated Date**: 2025-04-16

**PDF Url**: [2503.11720v3](http://arxiv.org/pdf/2503.11720v3)

**Abstract**: We introduce Rich Preference Optimization (RPO), a novel pipeline that
leverages rich feedback signals to improve the curation of preference pairs for
fine-tuning text-to-image diffusion models. Traditional methods, like
Diffusion-DPO, often rely solely on reward model labeling, which can be opaque,
offer limited insights into the rationale behind preferences, and are prone to
issues such as reward hacking or overfitting. In contrast, our approach begins
with generating detailed critiques of synthesized images to extract reliable
and actionable image editing instructions. By implementing these instructions,
we create refined images, resulting in synthetic, informative preference pairs
that serve as enhanced tuning datasets. We demonstrate the effectiveness of our
pipeline and the resulting datasets in fine-tuning state-of-the-art diffusion
models.


### AttentionDrop: A Novel Regularization Method for Transformer Models
**Authors**: Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Abdul Akbar Khan, Shahid Munir Shah

**Published Date**: 2025-04-16

**Updated Date**: 2025-04-16

**PDF Url**: [2504.12088v1](http://arxiv.org/pdf/2504.12088v1)

**Abstract**: Transformer-based architectures achieve state-of-the-art performance across a
wide range of tasks in natural language processing, computer vision, and
speech. However, their immense capacity often leads to overfitting, especially
when training data is limited or noisy. We propose AttentionDrop, a unified
family of stochastic regularization techniques that operate directly on the
self-attention distributions. We introduces three variants: 1. Hard Attention
Masking: randomly zeroes out top-k attention logits per query to encourage
diverse context utilization. 2. Blurred Attention Smoothing: applies a dynamic
Gaussian convolution over attention logits to diffuse overly peaked
distributions. 3. Consistency-Regularized AttentionDrop: enforces output
stability under multiple independent AttentionDrop perturbations via a KL-based
consistency loss.


