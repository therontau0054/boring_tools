# Abstracts of Papers

## Physics
### Hybrid Oscillator-Qubit Quantum Processors: Simulating Fermions, Bosons, and Gauge Fields
**Authors**: Eleanor Crane, Kevin C. Smith, Teague Tomesh, Alec Eickbusch, John M. Martyn, Stefan Kühn, Lena Funcke, Michael Austin DeMarco, Isaac L. Chuang, Nathan Wiebe, Alexander Schuckert, Steven M. Girvin

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03747v1](http://arxiv.org/pdf/2409.03747v1)

**Abstract**: We develop a hybrid oscillator-qubit processor framework for quantum
simulation of strongly correlated fermions and bosons that avoids the
boson-to-qubit mapping overhead encountered in qubit hardware. This framework
gives exact decompositions of particle interactions such as density-density
terms and gauge-invariant hopping, as well as approximate methods based on the
Baker-Campbell Hausdorff formulas including the magnetic field term for the
$U(1)$ quantum link model in $(2+1)$D. We use this framework to show how to
simulate dynamics using Trotterisation, perform ancilla-free partial error
detection using Gauss's law, measure non-local observables, estimate ground
state energies using a oscillator-qubit variational quantum eigensolver as well
as quantum signal processing, and we numerically study the influence of
hardware errors in circuit QED experiments. To show the advantages over
all-qubit hardware, we perform an end-to-end comparison of the gate complexity
for the gauge-invariant hopping term and find an improvement of the asymptotic
scaling with the boson number cutoff $S$ from $\mathcal{O}(\log(S)^2)$ to
$\mathcal{O}(1)$ in our framework as well as, for bosonic matter, a constant
factor improvement of better than $10^4$. We also find an improvement from
$\mathcal{O}(\log(S))$ to $\mathcal{O}(1)$ for the $U(1)$ magnetic field term.
While our work focusses on an implementation in superconducting hardware, our
framework can also be used in trapped ion, and neutral atom hardware. This work
establishes digital quantum simulation with hybrid oscillator-qubit hardware as
a viable and advantageous method for the study of qubit-boson models in
materials science, chemistry, and high-energy physics.


### Performance and tolerance study of the rectilinear cooling channel for a muon collider
**Authors**: Ruihu Zhu, Chris Rogers, Jiancheng Yang, He Zhao, Cheng Guo, Jiangdong Li

**Published Date**: 2024-09-04

**Updated Date**: 2024-09-05

**PDF Url**: [2409.02613v2](http://arxiv.org/pdf/2409.02613v2)

**Abstract**: The muon collider has the potential to be a powerful tool for the exploration
of frontiers in particle physics. In order to reach high luminosity, the 6D
emittance of the muon beam needs to be reduced by several orders of magnitude.
The cooling process for a muon collider involves two parts; initial
six-dimensional cooling and final transverse cooling. This paper focuses on the
former and proposes a conceptual design of the rectilinear cooling channel with
additional dipole magnets. In this paper, we first introduce a general method
for designing the rectilinear cooling channel. Subsequently, we apply this
method to develop two rectilinear cooling channels before and after a bunch
merging system. Furthermore, we investigate the impact on cooling performance
by employing $\pi$-mode RF cavities and considering the effect of errors in the
magnetic and RF fields.


### Hardware-Assisted Parameterized Circuit Execution
**Authors**: Abhi D. Rajagopala, Akel Hashim, Neelay Fruitwala, Gang Huang, Yilun Xu, Jordan Hines, Irfan Siddiqi, Katherine Klymko, Kasra Nowrouzi

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03725v1](http://arxiv.org/pdf/2409.03725v1)

**Abstract**: Standard compilers for quantum circuits decompose arbitrary single-qubit
gates into a sequence of physical X(pi/2) pulses and virtual-Z phase gates.
Consequently, many circuit classes implement different logic operations but
have an equivalent structure of physical pulses that only differ by changes in
virtual phases. When many structurally-equivalent circuits need to be measured,
generating sequences for each circuit is unnecessary and cumbersome, since
compiling and loading sequences onto classical control hardware is a primary
bottleneck in quantum circuit execution. In this work, we develop a
hardware-assisted protocol for executing parameterized circuits on our
FPGA-based control hardware, QubiC. This protocol relies on a hardware-software
co-design technique in which software identifies structural equivalency in
circuits and "peels" off the relevant parameterized angles to reduce the
overall waveform compilation time. The hardware architecture then performs
real-time "stitching" of the parameters in the circuit to measure circuits that
implement a different overall logical operation. This work demonstrates
significant speed ups in the total execution time for several different classes
of quantum circuits.


### Investigating Quantum Spin-Textures Using Universal MJ Hamiltonians
**Authors**: Manish Kumar Mohanta, Puru Jena

**Published Date**: 2024-08-26

**Updated Date**: 2024-09-05

**PDF Url**: [2408.14571v2](http://arxiv.org/pdf/2408.14571v2)

**Abstract**: This work introduces a pair of novel universal MJ spintronic models that
precisely mirror the complex spin textures observed in spintronic materials.
The spin-orbit coupled (SOC) Hamiltonians H_MJ1 and H_MJ2 reveal a range of
novel and intriguing spin phenomena by modulating spin-orbit interactions. The
Hamiltonian H_MJ1 reshapes the existing paradigm, providing a more robust and
versatile framework than the Hamiltonian H_RD, with the potential to catalyze
new advancements in the study of quantum materials. H_MJ1 encapsulates two
distinct spin textures: a unidirectional, momentum-independent persistent spin
texture (PST), and a bidirectional (partial) PST. In contrast Hamiltonian H_MJ2
portrays a spiral spin texture, drawing a conceptual link to the cosmological
process of expansion and contraction, mirrored within a two-dimensional quantum
framework. We also explore the fundamental aspects of earlier analytical models
that underpin the construction of the present MJ spintronic model. The physical
interpretations of these models are illustrated graphically, and the emerging
spin phenomena resulting from complex SOC are elucidated using a simple vector
model.


### Physics case for quarkonium studies at the Electron Ion Collider
**Authors**: Daniël Boer, Chris A. Flett, Carlo Flore, Daniel Kikoła, Jean-Philippe Lansberg, Maxim Nefedov, Charlotte Van Hulse, Shohini Bhattacharya, Jelle Bor, Mathias Butenschoen, Federico Ceccopieri, Longjie Chen, Vincent Cheung, Umberto D'Alesio, Miguel Echevarria, Yoshitaka Hatta, Charles E. Hyde, Raj Kishore, Leszek Kosarzewski, Cédric Lorcé, Wenliang Li, Xuan Li, Luca Maxia, Andreas Metz, Asmita Mukherjee, Carlos Muñoz Camacho, Francesco Murgia, Pawel Nadel-Turonski, Cristian Pisano, Jian-Wei Qiu, Sangem Rajesh, Matteo Rinaldi, Jennifer Rittenhouse West, Vladimir Saleev, Nathaly Santiesteban, Chalis Setyadi, Pieter Taels, Zhoudunmin Tu, Ivan Vitev, Ramona Vogt, Kazuhiro Watanabe, Xiaojun Yao, Yelyzaveta Yedelkina, Shinsuke Yoshida

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03691v1](http://arxiv.org/pdf/2409.03691v1)

**Abstract**: The physics case for quarkonium-production studies accessible at the US
Electron Ion Collider is described.


### Experimental evidence that a photon can spend a negative amount of time in an atom cloud
**Authors**: Daniela Angulo, Kyle Thompson, Vida-Michelle Nixon, Andy Jiao, Howard M. Wiseman, Aephraim M. Steinberg

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03680v1](http://arxiv.org/pdf/2409.03680v1)

**Abstract**: When a pulse of light traverses a material, it incurs a time delay referred
to as the group delay. Should the group delay experienced by photons be
attributed to the time they spend as atomic excitations? However reasonable
this connection may seem, it appears problematic when the frequency of the
light is close to the atomic resonance, as the group delay becomes negative in
this regime. To address this question, we use the cross-Kerr effect to probe
the degree of atomic excitation caused by a resonant transmitted photon, by
measuring the phase shift on a separate beam that is weak and off-resonant. Our
results, over a range of pulse durations and optical depths, are consistent
with the recent theoretical prediction that the mean atomic excitation time
caused by a transmitted photon (as measured via the time integral of the
observed phase shift) equals the group delay experienced by the light.
Specifically, we measure mean atomic excitation times ranging from $(-0.82\pm
0.31) \tau_0$ for the most narrowband pulse to $(0.54\pm 0.28) \tau_0$ for the
most broadband pulse, where $\tau_0$ is the non-post-selected excitation time,
given by the scattering (absorption) probability multiplied by the atomic
lifetime $\tau_{\rm sp}$. These results suggest that negative values taken by
times such as the group delay have more physical significance than has
generally been appreciated.


### A Natural Introduction to Fine-Tuning
**Authors**: Julian De Vuyst

**Published Date**: 2020-12-10

**Updated Date**: 2024-09-05

**PDF Url**: [2012.05617v2](http://arxiv.org/pdf/2012.05617v2)

**Abstract**: A well-known topic within the philosophy of physics is the problem of
fine-tuning: the fact that the universal constants seem to take non-arbitrary
values in order for live to thrive in our Universe. In this paper we will talk
about this problem in general, giving some examples from physics. We will
review some solutions like the design argument, logical probability,
cosmological natural selection, etc. Moreover, we will also discuss why it's
dangerous to uphold the Principle of Naturalness as a scientific principle.
After going through this paper, the reader should have a general idea what this
problem exactly entails whenever it is mentioned in other sources and we
recommend the reader to think critically about these concepts.


### Quantum complexity and localization in random quantum circuits
**Authors**: Himanshu Sahu, Aranya Bhattacharya, Pingal Pratyush Nath

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03656v1](http://arxiv.org/pdf/2409.03656v1)

**Abstract**: Quantum complexity has emerged as a central concept in diverse areas of
physics, ranging from quantum computing to the theory of black holes. We
perform a systematic study of complexity in random quantum circuits with and
without measurements. We observe that complexity grows linearly before
saturating to a constant value. For $N$ qubits without measurements, the
saturation value scales as $2^{N-1}$, and the saturation time scales as $2^N$.
This behaviour remains identical in the presence of random measurements with
different probabilities, indicating that this notion of complexity is
insensitive to the rate of measurement. We also study the behaviour of
complexity in two variants of the random unitary floquet circuit, where we
observe that complexity acts as a novel probe of Anderson localization and
many-body localization.


### Benchmarking the integration of hexagonal boron nitride crystals and thin films into graphene-based van der Waals heterostructures
**Authors**: Taoufiq Ouaj, Christophe Arnold, Jon Azpeitia, Sunaja Baltic, Julien Barjon, Jose Cascales, Huanyao Cun, David Esteban, Mar Garcia-Hernandez, Vincent Garnier, Subodh K. Gautam, Thomas Greber, Said Said Hassani, Adrian Hemmi, Ignacio Jimenéz, Catherine Journet, Paul Kögerler, Annick Loiseau, Camille Maestre, Marvin Metzelaars, Philipp Schmidt, Christoph Stampfer, Ingrid Stenger, Philippe Steyer, Takashi Taniguchi, Bérangère Toury, Kenji Watanabe, Bernd Beschoten

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03652v1](http://arxiv.org/pdf/2409.03652v1)

**Abstract**: We present a benchmarking protocol that combines the characterization of
boron nitride (BN) crystals and films with the evaluation of the electronic
properties of graphene on these substrates. Our study includes hBN crystals
grown under different conditions and scalable BN films deposited by either
chemical or physical vapor deposition (CVD or PVD). We explore the complete
process from boron nitride growth, over its optical characterization by
time-resolved cathodoluminescence (TRCL), to the optical and electronic
characterization of graphene by Raman spectroscopy after encapsulation and Hall
bar processing. Within our benchmarking protocol we achieve a homogeneous
electronic performance within each Hall bar device through a fast and
reproducible processing routine. We find that a free exciton lifetime of 1 ns
measured on as-grown hBN crystals by TRCL is sufficient to achieve high
graphene room temperature charge carrier mobilities of 80,000 cm$^2$/(Vs) at a
carrier density of |n| = 10$^{12}$ cm$^{-2}$, while respective exciton
lifetimes around 100 ps yield mobilities up to 30,000 cm$^2$/(Vs). For scalable
PVD-grown BN films, we measure carrier mobilities exceeding 10,000 cm$^2$/(Vs)
which correlates with a graphene Raman 2D peak linewidth of 22 cm$^{-1}$. Our
work highlights the importance of the Raman 2D linewidth of graphene as a
critical metric that effectively assesses the interface quality (i.e. surface
roughness) to the BN substrate, which directly affects the charge carrier
mobility of graphene. Graphene 2D linewidth analysis is suitable for all BN
substrates and is particularly advantageous when TRCL or BN Raman spectroscopy
cannot be applied to specific BN materials such as amorphous or thin films.
This underlines the superior role of spatially-resolved spectroscopy in the
evaluation of BN crystals and films for the use of high-mobility graphene
devices.


### QCD Masterclass Lectures on Jet Physics and Machine Learning
**Authors**: Andrew J. Larkoski

**Published Date**: 2024-07-06

**Updated Date**: 2024-09-05

**PDF Url**: [2407.04897v2](http://arxiv.org/pdf/2407.04897v2)

**Abstract**: These lectures were presented at the 2024 QCD Masterclass in
Saint-Jacut-de-la-Mer, France. They introduce and review fundamental theorems
and principles of machine learning within the context of collider particle
physics, focused on application to jet identification and discrimination.
Numerous examples of binary discrimination in jet physics are studied in
detail, including $H\to b\bar b$ identification in fixed-order perturbation
theory, generic one-versus two-prong discrimination with parametric power
counting techniques, and up versus down quark jet classification by assuming
the central limit theorem, isospin conservation, and a convergent moment
expansion of the single particle energy distribution. Quark versus gluon jet
discrimination is considered in multiple contexts, from using additive,
infrared and collinear safe observables, to using hadronic multiplicity, and to
including measurements of the jet charge. While many of the results presented
here are well known, some novel results are presented, the most prominent being
a parametrized expression for the likelihood ratio of quark versus gluon
discrimination for jets on which hadronic multiplicity and jet charge are
simultaneously measured. End-of-lecture exercises are also provided.


## Diffusion
### Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding
**Authors**: Yunze Man, Shuhong Zheng, Zhipeng Bao, Martial Hebert, Liang-Yan Gui, Yu-Xiong Wang

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03757v1](http://arxiv.org/pdf/2409.03757v1)

**Abstract**: Complex 3D scene understanding has gained increasing attention, with scene
encoding strategies playing a crucial role in this success. However, the
optimal scene encoding strategies for various scenarios remain unclear,
particularly compared to their image-based counterparts. To address this issue,
we present a comprehensive study that probes various visual encoding models for
3D scene understanding, identifying the strengths and limitations of each model
across different scenarios. Our evaluation spans seven vision foundation
encoders, including image-based, video-based, and 3D foundation models. We
evaluate these models in four tasks: Vision-Language Scene Reasoning, Visual
Grounding, Segmentation, and Registration, each focusing on different aspects
of scene understanding. Our evaluations yield key findings: DINOv2 demonstrates
superior performance, video models excel in object-level tasks, diffusion
models benefit geometric tasks, and language-pretrained models show unexpected
limitations in language-related tasks. These insights challenge some
conventional understandings, provide novel perspectives on leveraging visual
foundation models, and highlight the need for more flexible encoder selection
in future vision-language and scene-understanding tasks.


### Multimodal Laryngoscopic Video Analysis for Assisted Diagnosis of Vocal Cord Paralysis
**Authors**: Yucong Zhang, Xin Zou, Jinshan Yang, Wenjun Chen, Faya Liang, Ming Li

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03597v1](http://arxiv.org/pdf/2409.03597v1)

**Abstract**: This paper presents the Multimodal Analyzing System for Laryngoscope (MASL),
a system that combines audio and video data to automatically extract key
segments and metrics from laryngeal videostroboscopic videos for clinical
assessment. MASL integrates glottis detection with keyword spotting to analyze
patient vocalizations and refine video highlights for better inspection of
vocal cord movements. The system includes a strobing video extraction module
that identifies frames by analyzing hue, saturation, and value fluctuations.
MASL also provides effective metrics for vocal cord paralysis detection,
employing a two-stage glottis segmentation process using U-Net followed by
diffusion-based refinement to reduce false positives. Instead of glottal area
waveforms, MASL estimates anterior glottic angle waveforms (AGAW) from glottis
masks, evaluating both left and right vocal cords to detect unilateral vocal
cord paralysis (UVFP). By comparing AGAW variances, MASL distinguishes between
left and right paralysis. Ablation studies and experiments on public and
real-world datasets validate MASL's segmentation module and demonstrate its
ability to provide reliable metrics for UVFP diagnosis.


### DKDM: Data-Free Knowledge Distillation for Diffusion Models with Any Architecture
**Authors**: Qianlong Xiang, Miao Zhang, Yuzhang Shang, Jianlong Wu, Yan Yan, Liqiang Nie

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03550v1](http://arxiv.org/pdf/2409.03550v1)

**Abstract**: Diffusion models (DMs) have demonstrated exceptional generative capabilities
across various areas, while they are hindered by slow inference speeds and high
computational demands during deployment. The most common way to accelerate DMs
involves reducing the number of denoising steps during generation, achieved
through faster sampling solvers or knowledge distillation (KD). In contrast to
prior approaches, we propose a novel method that transfers the capability of
large pretrained DMs to faster architectures. Specifically, we employ KD in a
distinct manner to compress DMs by distilling their generative ability into
more rapid variants. Furthermore, considering that the source data is either
unaccessible or too enormous to store for current generative models, we
introduce a new paradigm for their distillation without source data, termed
Data-Free Knowledge Distillation for Diffusion Models (DKDM). Generally, our
established DKDM framework comprises two main components: 1) a DKDM objective
that uses synthetic denoising data produced by pretrained DMs to optimize
faster DMs without source data, and 2) a dynamic iterative distillation method
that flexibly organizes the synthesis of denoising data, preventing it from
slowing down the optimization process as the generation is slow. To our
knowledge, this is the first attempt at using KD to distill DMs into any
architecture in a data-free manner. Importantly, our DKDM is orthogonal to most
existing acceleration methods, such as denoising step reduction, quantization
and pruning. Experiments show that our DKDM is capable of deriving 2x faster
DMs with performance remaining on par with the baseline. Notably, our DKDM
enables pretrained DMs to function as "datasets" for training new DMs.


### KAN See In the Dark
**Authors**: Aoxiang Ning, Minglong Xue, Jinhong He, Chengyun Song

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03404v1](http://arxiv.org/pdf/2409.03404v1)

**Abstract**: Existing low-light image enhancement methods are difficult to fit the complex
nonlinear relationship between normal and low-light images due to uneven
illumination and noise effects. The recently proposed Kolmogorov-Arnold
networks (KANs) feature spline-based convolutional layers and learnable
activation functions, which can effectively capture nonlinear dependencies. In
this paper, we design a KAN-Block based on KANs and innovatively apply it to
low-light image enhancement. This method effectively alleviates the limitations
of current methods constrained by linear network structures and lack of
interpretability, further demonstrating the potential of KANs in low-level
vision tasks. Given the poor perception of current low-light image enhancement
methods and the stochastic nature of the inverse diffusion process, we further
introduce frequency-domain perception for visually oriented enhancement.
Extensive experiments demonstrate the competitive performance of our method on
benchmark datasets. The code will be available at:
https://github.com/AXNing/KSID}{https://github.com/AXNing/KSID.


### LinFusion: 1 GPU, 1 Minute, 16K Image
**Authors**: Songhua Liu, Weihao Yu, Zhenxiong Tan, Xinchao Wang

**Published Date**: 2024-09-03

**Updated Date**: 2024-09-05

**PDF Url**: [2409.02097v2](http://arxiv.org/pdf/2409.02097v2)

**Abstract**: Modern diffusion models, particularly those utilizing a Transformer-based
UNet for denoising, rely heavily on self-attention operations to manage complex
spatial relationships, thus achieving impressive generation performance.
However, this existing paradigm faces significant challenges in generating
high-resolution visual content due to its quadratic time and memory complexity
with respect to the number of spatial tokens. To address this limitation, we
aim at a novel linear attention mechanism as an alternative in this paper.
Specifically, we begin our exploration from recently introduced models with
linear complexity, e.g., Mamba2, RWKV6, Gated Linear Attention, etc, and
identify two key features-attention normalization and non-causal inference-that
enhance high-resolution visual generation performance. Building on these
insights, we introduce a generalized linear attention paradigm, which serves as
a low-rank approximation of a wide spectrum of popular linear token mixers. To
save the training cost and better leverage pre-trained models, we initialize
our models and distill the knowledge from pre-trained StableDiffusion (SD). We
find that the distilled model, termed LinFusion, achieves performance on par
with or superior to the original SD after only modest training, while
significantly reducing time and memory complexity. Extensive experiments on
SD-v1.5, SD-v2.1, and SD-XL demonstrate that LinFusion delivers satisfactory
zero-shot cross-resolution generation performance, generating high-resolution
images like 16K resolution. Moreover, it is highly compatible with pre-trained
SD components, such as ControlNet and IP-Adapter, requiring no adaptation
efforts. Codes are available at https://github.com/Huage001/LinFusion.


## Quantitative Finance
### Epistemic Limits of Empirical Finance: Causal Reductionism and Self-Reference
**Authors**: Daniel Polakow, Tim Gebbie, Emlyn Flint

**Published Date**: 2023-11-28

**Updated Date**: 2024-09-05

**PDF Url**: [2311.16570v5](http://arxiv.org/pdf/2311.16570v5)

**Abstract**: The clarion call for causal reduction in the study of capital markets is
intensifying. However, in self-referencing and open systems such as capital
markets, the idea of unidirectional causation (if applicable) may be limiting
at best, and unstable or fallacious at worst. In this work, we critically
assess the use of scientific deduction and causal inference within the study of
empirical finance and financial econometrics. We then demonstrate the idea of
competing causal chains using a toy model adapted from ecological predator/prey
relationships. From this, we develop the alternative view that the study of
empirical finance, and the risks contained therein, may be better appreciated
once we admit that our current arsenal of quantitative finance tools may be
limited to ex post causal inference under popular assumptions. Where these
assumptions are challenged, for example in a recognizable reflexive context,
the prescription of unidirectional causation proves deeply problematic.


### Pricing American Options using Machine Learning Algorithms
**Authors**: Prudence Djagba, Callixte Ndizihiwe

**Published Date**: 2024-09-05

**Updated Date**: 2024-09-05

**PDF Url**: [2409.03204v1](http://arxiv.org/pdf/2409.03204v1)

**Abstract**: This study investigates the application of machine learning algorithms,
particularly in the context of pricing American options using Monte Carlo
simulations. Traditional models, such as the Black-Scholes-Merton framework,
often fail to adequately address the complexities of American options, which
include the ability for early exercise and non-linear payoff structures. By
leveraging Monte Carlo methods in conjunction Least Square Method machine
learning was used. This research aims to improve the accuracy and efficiency of
option pricing. The study evaluates several machine learning models, including
neural networks and decision trees, highlighting their potential to outperform
traditional approaches. The results from applying machine learning algorithm in
LSM indicate that integrating machine learning with Monte Carlo simulations can
enhance pricing accuracy and provide more robust predictions, offering
significant insights into quantitative finance by merging classical financial
theories with modern computational techniques. The dataset was split into
features and the target variable representing bid prices, with an 80-20
train-validation split. LSTM and GRU models were constructed using TensorFlow's
Keras API, each with four hidden layers of 200 neurons and an output layer for
bid price prediction, optimized with the Adam optimizer and MSE loss function.
The GRU model outperformed the LSTM model across all evaluated metrics,
demonstrating lower mean absolute error, mean squared error, and root mean
squared error, along with greater stability and efficiency in training.


