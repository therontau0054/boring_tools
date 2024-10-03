# Abstracts of Papers

## Physics
### FabricDiffusion: High-Fidelity Texture Transfer for 3D Garments Generation from In-The-Wild Clothing Images
**Authors**: Cheng Zhang, Yuanhao Wang, Francisco Vicente Carrasco, Chenglei Wu, Jinlong Yang, Thabo Beeler, Fernando De la Torre

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01801v1](http://arxiv.org/pdf/2410.01801v1)

**Abstract**: We introduce FabricDiffusion, a method for transferring fabric textures from
a single clothing image to 3D garments of arbitrary shapes. Existing approaches
typically synthesize textures on the garment surface through 2D-to-3D texture
mapping or depth-aware inpainting via generative models. Unfortunately, these
methods often struggle to capture and preserve texture details, particularly
due to challenging occlusions, distortions, or poses in the input image.
Inspired by the observation that in the fashion industry, most garments are
constructed by stitching sewing patterns with flat, repeatable textures, we
cast the task of clothing texture transfer as extracting distortion-free,
tileable texture materials that are subsequently mapped onto the UV space of
the garment. Building upon this insight, we train a denoising diffusion model
with a large-scale synthetic dataset to rectify distortions in the input
texture image. This process yields a flat texture map that enables a tight
coupling with existing Physically-Based Rendering (PBR) material generation
pipelines, allowing for realistic relighting of the garment under various
lighting conditions. We show that FabricDiffusion can transfer various features
from a single clothing image including texture patterns, material properties,
and detailed prints and logos. Extensive experiments demonstrate that our model
significantly outperforms state-to-the-art methods on both synthetic data and
real-world, in-the-wild clothing images while generalizing to unseen textures
and garment shapes.


### Thermodynamic Bayesian Inference
**Authors**: Maxwell Aifer, Samuel Duffield, Kaelan Donatella, Denis Melanson, Phoebe Klett, Zach Belateche, Gavin Crooks, Antonio J. Martinez, Patrick J. Coles

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01793v1](http://arxiv.org/pdf/2410.01793v1)

**Abstract**: A fully Bayesian treatment of complicated predictive models (such as deep
neural networks) would enable rigorous uncertainty quantification and the
automation of higher-level tasks including model selection. However, the
intractability of sampling Bayesian posteriors over many parameters inhibits
the use of Bayesian methods where they are most needed. Thermodynamic computing
has emerged as a paradigm for accelerating operations used in machine learning,
such as matrix inversion, and is based on the mapping of Langevin equations to
the dynamics of noisy physical systems. Hence, it is natural to consider the
implementation of Langevin sampling algorithms on thermodynamic devices. In
this work we propose electronic analog devices that sample from Bayesian
posteriors by realizing Langevin dynamics physically. Circuit designs are given
for sampling the posterior of a Gaussian-Gaussian model and for Bayesian
logistic regression, and are validated by simulations. It is shown, under
reasonable assumptions, that the Bayesian posteriors for these models can be
sampled in time scaling with $\ln(d)$, where $d$ is dimension. For the
Gaussian-Gaussian model, the energy cost is shown to scale with $ d \ln(d)$.
These results highlight the potential for fast, energy-efficient Bayesian
inference using thermodynamic computing.


### Dynamical-generative downscaling of climate model ensembles
**Authors**: Ignacio Lopez-Gomez, Zhong Yi Wan, Leonardo Zepeda-Núñez, Tapio Schneider, John Anderson, Fei Sha

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01776v1](http://arxiv.org/pdf/2410.01776v1)

**Abstract**: Regional high-resolution climate projections are crucial for many
applications, such as agriculture, hydrology, and natural hazard risk
assessment. Dynamical downscaling, the state-of-the-art method to produce
localized future climate information, involves running a regional climate model
(RCM) driven by an Earth System Model (ESM), but it is too computationally
expensive to apply to large climate projection ensembles. We propose a novel
approach combining dynamical downscaling with generative artificial
intelligence to reduce the cost and improve the uncertainty estimates of
downscaled climate projections. In our framework, an RCM dynamically downscales
ESM output to an intermediate resolution, followed by a generative diffusion
model that further refines the resolution to the target scale. This approach
leverages the generalizability of physics-based models and the sampling
efficiency of diffusion models, enabling the downscaling of large multi-model
ensembles. We evaluate our method against dynamically-downscaled climate
projections from the CMIP6 ensemble. Our results demonstrate its ability to
provide more accurate uncertainty bounds on future regional climate than
alternatives such as dynamical downscaling of smaller ensembles, or traditional
empirical statistical downscaling methods. We also show that
dynamical-generative downscaling results in significantly lower errors than
bias correction and spatial disaggregation (BCSD), and captures more accurately
the spectra and multivariate correlations of meteorological fields. These
characteristics make the dynamical-generative framework a flexible, accurate,
and efficient way to downscale large ensembles of climate projections,
currently out of reach for pure dynamical downscaling.


### $^{229}\mathrm{ThF}_4$ thin films for solid-state nuclear clocks
**Authors**: Chuankun Zhang, Lars von der Wense, Jack F. Doyle, Jacob S. Higgins, Tian Ooi, Hans U. Friebel, Jun Ye, R. Elwell, J. E. S. Terhune, H. W. T. Morgan, A. N. Alexandrova, H. B. Tran Tan, Andrei Derevianko, Eric R. Hudson

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01753v1](http://arxiv.org/pdf/2410.01753v1)

**Abstract**: After nearly fifty years of searching, the vacuum ultraviolet $^{229}$Th
nuclear isomeric transition has recently been directly laser excited [1,2] and
measured with high spectroscopic precision [3]. Nuclear clocks based on this
transition are expected to be more robust [4,5] than and may outperform [6,7]
current optical atomic clocks. They also promise sensitive tests for new
physics beyond the standard model [5,8,9]. In light of these important advances
and applications, a dramatic increase in the need for $^{229}$Th spectroscopy
targets in a variety of platforms is anticipated. However, the growth and
handling of high-concentration $^{229}$Th-doped crystals [5] used in previous
measurements [1-3,10] are challenging due to the scarcity and radioactivity of
the $^{229}$Th material. Here, we demonstrate a potentially scalable solution
to these problems by demonstrating laser excitation of the nuclear transition
in $^{229}$ThF$_4$ thin films grown with a physical vapor deposition process,
consuming only micrograms of $^{229}$Th material. The $^{229}$ThF$_4$ thin
films are intrinsically compatible with photonics platforms and nanofabrication
tools for integration with laser sources and detectors, paving the way for an
integrated and field-deployable solid-state nuclear clock with radioactivity up
to three orders of magnitude smaller than typical \thor-doped crystals
[1-3,10]. The high nuclear emitter density in $^{229}$ThF$_4$ also potentially
enables quantum optics studies in a new regime. Finally, we describe the
operation and present the estimation of the performance of a nuclear clock
based on a defect-free ThF$_4$ crystal.


### TorchSISSO: A PyTorch-Based Implementation of the Sure Independence Screening and Sparsifying Operator for Efficient and Interpretable Model Discovery
**Authors**: Madhav Muthyala, Farshud Sorourifar, Joel A. Paulson

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01752v1](http://arxiv.org/pdf/2410.01752v1)

**Abstract**: Symbolic regression (SR) is a powerful machine learning approach that
searches for both the structure and parameters of algebraic models, offering
interpretable and compact representations of complex data. Unlike traditional
regression methods, SR explores progressively complex feature spaces, which can
uncover simple models that generalize well, even from small datasets. Among SR
algorithms, the Sure Independence Screening and Sparsifying Operator (SISSO)
has proven particularly effective in the natural sciences, helping to
rediscover fundamental physical laws as well as discover new interpretable
equations for materials property modeling. However, its widespread adoption has
been limited by performance inefficiencies and the challenges posed by its
FORTRAN-based implementation, especially in modern computing environments. In
this work, we introduce TorchSISSO, a native Python implementation built in the
PyTorch framework. TorchSISSO leverages GPU acceleration, easy integration, and
extensibility, offering a significant speed-up and improved accuracy over the
original. We demonstrate that TorchSISSO matches or exceeds the performance of
the original SISSO across a range of tasks, while dramatically reducing
computational time and improving accessibility for broader scientific
applications.


### Strategies for Pretraining Neural Operators
**Authors**: Anthony Zhou, Cooper Lorsung, AmirPouya Hemmasian, Amir Barati Farimani

**Published Date**: 2024-06-12

**Updated Date**: 2024-10-02

**PDF Url**: [2406.08473v2](http://arxiv.org/pdf/2406.08473v2)

**Abstract**: Pretraining for partial differential equation (PDE) modeling has recently
shown promise in scaling neural operators across datasets to improve
generalizability and performance. Despite these advances, our understanding of
how pretraining affects neural operators is still limited; studies generally
propose tailored architectures and datasets that make it challenging to compare
or examine different pretraining frameworks. To address this, we compare
various pretraining methods without optimizing architecture choices to
characterize pretraining dynamics on different models and datasets as well as
to understand its scaling and generalization behavior. We find that pretraining
is highly dependent on model and dataset choices, but in general transfer
learning or physics-based pretraining strategies work best. In addition,
pretraining performance can be further improved by using data augmentations.
Lastly, pretraining can be additionally beneficial when fine-tuning in scarce
data regimes or when generalizing to downstream data similar to the pretraining
distribution. Through providing insights into pretraining neural operators for
physics prediction, we hope to motivate future work in developing and
evaluating pretraining methods for PDEs.


### Observation of quantum entanglement in top-quark pairs using the ATLAS detector
**Authors**: ATLAS Collaboration

**Published Date**: 2023-11-13

**Updated Date**: 2024-10-02

**PDF Url**: [2311.07288v3](http://arxiv.org/pdf/2311.07288v3)

**Abstract**: Entanglement is a key feature of quantum mechanics, with applications in
fields such as metrology, cryptography, quantum information, and quantum
computation. It has been observed in a wide variety of systems and length
scales, ranging from the microscopic to the macroscopic. However, entanglement
remains largely unexplored at the highest accessible energy scales. Here we
report the highest-energy observation of entanglement, in top$-$antitop quark
events produced at the Large Hadron Collider, using a proton$-$proton collision
dataset with a center-of-mass energy of $\sqrt{s}=13$ TeV and an integrated
luminosity of 140 fb$^{-1}$ recorded with the ATLAS experiment. Spin
entanglement is detected from the measurement of a single observable $D$,
inferred from the angle between the charged leptons in their parent top- and
antitop-quark rest frames. The observable is measured in a narrow interval
around the top$-$antitop quark production threshold, where the entanglement
detection is expected to be significant. It is reported in a fiducial phase
space defined with stable particles to minimize the uncertainties that stem
from limitations of the Monte Carlo event generators and the parton shower
model in modeling top-quark pair production. The entanglement marker is
measured to be $D=-0.537 \pm 0.002~\text{(stat.)} \pm 0.019~\text{(syst.)}$ for
$340 < m_{t\bar{t}} < 380$ GeV. The observed result is more than five standard
deviations from a scenario without entanglement and constitutes the first
observation of entanglement in a pair of quarks and the highest-energy
observation of entanglement so far.


### Mind Scramble: Unveiling Large Language Model Psychology Via Typoglycemia
**Authors**: Miao Yu, Junyuan Mao, Guibin Zhang, Jingheng Ye, Junfeng Fang, Aoxiao Zhong, Yang Liu, Yuxuan Liang, Kun Wang, Qingsong Wen

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01677v1](http://arxiv.org/pdf/2410.01677v1)

**Abstract**: Research into the external behaviors and internal mechanisms of large
language models (LLMs) has shown promise in addressing complex tasks in the
physical world. Studies suggest that powerful LLMs, like GPT-4, are beginning
to exhibit human-like cognitive abilities, including planning, reasoning, and
reflection. In this paper, we introduce a research line and methodology called
LLM Psychology, leveraging human psychology experiments to investigate the
cognitive behaviors and mechanisms of LLMs. We migrate the Typoglycemia
phenomenon from psychology to explore the "mind" of LLMs. Unlike human brains,
which rely on context and word patterns to comprehend scrambled text, LLMs use
distinct encoding and decoding processes. Through Typoglycemia experiments at
the character, word, and sentence levels, we observe: (I) LLMs demonstrate
human-like behaviors on a macro scale, such as lower task accuracy and higher
token/time consumption; (II) LLMs exhibit varying robustness to scrambled
input, making Typoglycemia a benchmark for model evaluation without new
datasets; (III) Different task types have varying impacts, with complex logical
tasks (e.g., math) being more challenging in scrambled form; (IV) Each LLM has
a unique and consistent "cognitive pattern" across tasks, revealing general
mechanisms in its psychology process. We provide an in-depth analysis of hidden
layers to explain these phenomena, paving the way for future research in LLM
Psychology and deeper interpretability.


### Path integral treatment of coherence effects in charmonium production in nuclear ultra-peripheral collisions
**Authors**: J. Óbertová, J. Nemchik

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01668v1](http://arxiv.org/pdf/2410.01668v1)

**Abstract**: We present for the first time a revised study of charmonium production in
nuclear ultra-peripheral collisions (UPC) based on a rigorous Green function
formalism. This formalism allows for the proper incorporation of the effects of
color transparency, as well as the quantum coherence inherent in the higher
twist quark shadowing related to the $Q\bar Q$ Fock component of the photon.
The significance of this effect gradually decreases towards forward and/or
backward rapidities. In the LHC kinematic region we additionally incorporate
within the same formalism the leading twist gluon shadowing corrections related
to higher multi-gluon photon fluctuations. They represent a dominant source of
nuclear phenomena in the mid-rapidity region. Model predictions for the
rapidity distributions $d\sigma/dy$ are in good agreement with available UPC
data on coherent charmonium production at RHIC and the LHC. They can also be
verified by future measurements at the LHC, as well as at EIC.


### The Resonance Condition for Slow Wave Antennas: a Lagrangian Approach
**Authors**: Robert Nevels, Steven Scully, Francisco Espinal, Anatoly Svidzinsky

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01662v1](http://arxiv.org/pdf/2410.01662v1)

**Abstract**: A proof of the resonant property of linear periodically loaded antennas with
subwavelength elements is obtained by applying a Lagrangian formalism. A
Lagrangian is developed by modeling the antenna with lumped inductance and
capacitance elements on a single line, thereby physically similar to the
antenna and thus avoiding the inaccurate two parallel conductor transmission
line model. An equation for the antenna current driven by an incident
electromagnetic field is obtained via vector and scalar potentials. It is shown
that periodic loading provides a means to shorten the resonant length while the
antenna pattern remains unchanged. The Lagrangian model is validated through a
calculation showing the loaded resonant length is determined by a product of a
resonant half-wavelength dipole with the ratio of the free space velocity and
the longitudinal traveling wave velocity. A periodically loaded disk-on-rod
antenna example with simulations and measurements provides further validation
of the mathematics.


## Diffusion
### Bellman Diffusion: Generative Modeling as Learning a Linear Operator in the Distribution Space
**Authors**: Yangming Li, Chieh-Hsin Lai, Carola-Bibiane Schönlieb, Yuki Mitsufuji, Stefano Ermon

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01796v1](http://arxiv.org/pdf/2410.01796v1)

**Abstract**: Deep Generative Models (DGMs), including Energy-Based Models (EBMs) and
Score-based Generative Models (SGMs), have advanced high-fidelity data
generation and complex continuous distribution approximation. However, their
application in Markov Decision Processes (MDPs), particularly in distributional
Reinforcement Learning (RL), remains underexplored, with conventional
histogram-based methods dominating the field. This paper rigorously highlights
that this application gap is caused by the nonlinearity of modern DGMs, which
conflicts with the linearity required by the Bellman equation in MDPs. For
instance, EBMs involve nonlinear operations such as exponentiating energy
functions and normalizing constants. To address this, we introduce Bellman
Diffusion, a novel DGM framework that maintains linearity in MDPs through
gradient and scalar field modeling. With divergence-based training techniques
to optimize neural network proxies and a new type of stochastic differential
equation (SDE) for sampling, Bellman Diffusion is guaranteed to converge to the
target distribution. Our empirical results show that Bellman Diffusion achieves
accurate field estimations and is a capable image generator, converging 1.5x
faster than the traditional histogram-based baseline in distributional RL
tasks. This work enables the effective integration of DGMs into MDP
applications, unlocking new avenues for advanced decision-making frameworks.


### VitaGlyph: Vitalizing Artistic Typography with Flexible Dual-branch Diffusion Models
**Authors**: Kailai Feng, Yabo Zhang, Haodong Yu, Zhilong Ji, Jinfeng Bai, Hongzhi Zhang, Wangmeng Zuo

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01738v1](http://arxiv.org/pdf/2410.01738v1)

**Abstract**: Artistic typography is a technique to visualize the meaning of input
character in an imaginable and readable manner. With powerful text-to-image
diffusion models, existing methods directly design the overall geometry and
texture of input character, making it challenging to ensure both creativity and
legibility. In this paper, we introduce a dual-branch and training-free method,
namely VitaGlyph, enabling flexible artistic typography along with controllable
geometry change to maintain the readability. The key insight of VitaGlyph is to
treat input character as a scene composed of Subject and Surrounding, followed
by rendering them under varying degrees of geometry transformation. The subject
flexibly expresses the essential concept of input character, while the
surrounding enriches relevant background without altering the shape.
Specifically, we implement VitaGlyph through a three-phase framework: (i)
Knowledge Acquisition leverages large language models to design text
descriptions of subject and surrounding. (ii) Regional decomposition detects
the part that most matches the subject description and divides input glyph
image into subject and surrounding regions. (iii) Typography Stylization
firstly refines the structure of subject region via Semantic Typography, and
then separately renders the textures of Subject and Surrounding regions through
Controllable Compositional Generation. Experimental results demonstrate that
VitaGlyph not only achieves better artistry and readability, but also manages
to depict multiple customize concepts, facilitating more creative and pleasing
artistic typography generation. Our code will be made publicly at
https://github.com/Carlofkl/VitaGlyph.


### Latent Diffusion Models for Controllable RNA Sequence Generation
**Authors**: Kaixuan Huang, Yukang Yang, Kaidi Fu, Yanyi Chu, Le Cong, Mengdi Wang

**Published Date**: 2024-09-15

**Updated Date**: 2024-10-02

**PDF Url**: [2409.09828v2](http://arxiv.org/pdf/2409.09828v2)

**Abstract**: This work presents RNAdiffusion, a latent diffusion model for generating and
optimizing discrete RNA sequences of variable lengths. RNA is a key
intermediary between DNA and protein, exhibiting high sequence diversity and
complex three-dimensional structures to support a wide range of functions. We
utilize pretrained BERT-type models to encode raw RNA sequences into
token-level, biologically meaningful representations. A Query Transformer is
employed to compress such representations into a set of fixed-length latent
vectors, with an autoregressive decoder trained to reconstruct RNA sequences
from these latent variables. We then develop a continuous diffusion model
within this latent space. To enable optimization, we integrate the gradients of
reward models--surrogates for RNA functional properties--into the backward
diffusion process, thereby generating RNAs with high reward scores. Empirical
results confirm that RNAdiffusion generates non-coding RNAs that align with
natural distributions across various biological metrics. Further, we fine-tune
the diffusion model on mRNA 5' untranslated regions (5'-UTRs) and optimize
sequences for high translation efficiencies. Our guided diffusion model
effectively generates diverse 5'-UTRs with high Mean Ribosome Loading (MRL) and
Translation Efficiency (TE), outperforming baselines in balancing rewards and
structural stability trade-off. Our findings hold potential for advancing RNA
sequence-function research and therapeutic RNA design.


### Data Extrapolation for Text-to-image Generation on Small Datasets
**Authors**: Senmao Ye, Fei Liu

**Published Date**: 2024-10-02

**Updated Date**: 2024-10-02

**PDF Url**: [2410.01638v1](http://arxiv.org/pdf/2410.01638v1)

**Abstract**: Text-to-image generation requires large amount of training data to
synthesizing high-quality images. For augmenting training data, previous
methods rely on data interpolations like cropping, flipping, and mixing up,
which fail to introduce new information and yield only marginal improvements.
In this paper, we propose a new data augmentation method for text-to-image
generation using linear extrapolation. Specifically, we apply linear
extrapolation only on text feature, and new image data are retrieved from the
internet by search engines. For the reliability of new text-image pairs, we
design two outlier detectors to purify retrieved images. Based on
extrapolation, we construct training samples dozens of times larger than the
original dataset, resulting in a significant improvement in text-to-image
performance. Moreover, we propose a NULL-guidance to refine score estimation,
and apply recurrent affine transformation to fuse text information. Our model
achieves FID scores of 7.91, 9.52 and 5.00 on the CUB, Oxford and COCO
datasets. The code and data will be available on GitHub
(https://github.com/senmaoy/RAT-Diffusion).


