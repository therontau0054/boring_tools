# Abstracts of Papers

## Physics
### Solving Differential Equations using Physics-Informed Deep Equilibrium Models
**Authors**: Bruno Machado Pacheco, Eduardo Camponogara

**Published Date**: 2024-06-05

**Updated Date**: 2024-06-28

**PDF Url**: [2406.03472v2](http://arxiv.org/pdf/2406.03472v2)

**Abstract**: This paper introduces Physics-Informed Deep Equilibrium Models (PIDEQs) for
solving initial value problems (IVPs) of ordinary differential equations
(ODEs). Leveraging recent advancements in deep equilibrium models (DEQs) and
physics-informed neural networks (PINNs), PIDEQs combine the implicit output
representation of DEQs with physics-informed training techniques. We validate
PIDEQs using the Van der Pol oscillator as a benchmark problem, demonstrating
their efficiency and effectiveness in solving IVPs. Our analysis includes key
hyperparameter considerations for optimizing PIDEQ performance. By bridging
deep learning and physics-based modeling, this work advances computational
techniques for solving IVPs, with implications for scientific computing and
engineering applications.


### Tau Tridents at Accelerator Neutrino Facilities
**Authors**: Innes Bigaran, P. S. Bhupal Dev, Diego Lopez Gutierrez, Pedro A. N. Machado

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.20067v1](http://arxiv.org/pdf/2406.20067v1)

**Abstract**: We present the first detailed study of Standard Model (SM) neutrino tridents
involving tau leptons at the near detectors of accelerator neutrino facilities.
These processes were previously thought to be negligible, even at future
facilities like DUNE, based on approximations that underestimated the tau
trident cross sections. Our full $2\to 4$ calculation, including both coherent
and incoherent scatterings, reveals that the DUNE near detector will actually
get a non-negligible number of tau tridents, which is an important background
to new physics searches. We identify promising kinematic features that may
allow distinction of tau tridents from the usual neutrino charged-current
background at DUNE, and thus could establish the observation of tau tridents
for the first time. We also comment on the detection prospects at other
accelerator and collider neutrino experiments.


### Neural Differentiable Modeling with Diffusion-Based Super-resolution for Two-Dimensional Spatiotemporal Turbulence
**Authors**: Xiantao Fan, Deepak Akhare, Jian-Xun Wang

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.20047v1](http://arxiv.org/pdf/2406.20047v1)

**Abstract**: Simulating spatiotemporal turbulence with high fidelity remains a cornerstone
challenge in computational fluid dynamics (CFD) due to its intricate multiscale
nature and prohibitive computational demands. Traditional approaches typically
employ closure models, which attempt to represent small-scale features in an
unresolved manner. However, these methods often sacrifice accuracy and lose
high-frequency/wavenumber information, especially in scenarios involving
complex flow physics. In this paper, we introduce an innovative neural
differentiable modeling framework designed to enhance the predictability and
efficiency of spatiotemporal turbulence simulations. Our approach features
differentiable hybrid modeling techniques that seamlessly integrate deep neural
networks with numerical PDE solvers within a differentiable programming
framework, synergizing deep learning with physics-based CFD modeling.
Specifically, a hybrid differentiable neural solver is constructed on a coarser
grid to capture large-scale turbulent phenomena, followed by the application of
a Bayesian conditional diffusion model that generates small-scale turbulence
conditioned on large-scale flow predictions. Two innovative hybrid architecture
designs are studied, and their performance is evaluated through comparative
analysis against conventional large eddy simulation techniques with
physics-based subgrid-scale closures and purely data-driven neural solvers. The
findings underscore the potential of the neural differentiable modeling
framework to significantly enhance the accuracy and computational efficiency of
turbulence simulations. This study not only demonstrates the efficacy of
merging deep learning with physics-based numerical solvers but also sets a new
precedent for advanced CFD modeling techniques, highlighting the transformative
impact of differentiable programming in scientific computing.


### Electrostatics-based particle sampling and approximate inference
**Authors**: Yongchao Huang

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.20044v1](http://arxiv.org/pdf/2406.20044v1)

**Abstract**: A new particle-based sampling and approximate inference method, based on
electrostatics and Newton mechanics principles, is introduced with theoretical
ground, algorithm design and experimental validation. This method simulates an
interacting particle system (IPS) where particles, i.e. the freely-moving
negative charges and spatially-fixed positive charges with magnitudes
proportional to the target distribution, interact with each other via
attraction and repulsion induced by the resulting electric fields described by
Poisson's equation. The IPS evolves towards a steady-state where the
distribution of negative charges conforms to the target distribution. This
physics-inspired method offers deterministic, gradient-free sampling and
inference, achieving comparable performance as other particle-based and MCMC
methods in benchmark tasks of inferring complex densities, Bayesian logistic
regression and dynamical system identification. A discrete-time, discrete-space
algorithmic design, readily extendable to continuous time and space, is
provided for usage in more general inference problems occurring in
probabilistic machine learning scenarios such as Bayesian inference, generative
modelling, and beyond.


### On Bjorken sum rule with analytic coupling
**Authors**: I. R. Gabdrakhmanov, N. A Gramotkov, A. V. Kotikov, O. V. Teryaev, D. A. Volkova, I. A. Zemlyakov

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.20000v1](http://arxiv.org/pdf/2406.20000v1)

**Abstract**: We present the results of [1], where good agreement was obtained between
calculations within the framework of analytic QCD and experimental data on
polarized Bjorken sum rule. The photoproduction limit was also considered and a
new representation of the perturbative contribution to the polarized Bjorken
sum rule was obtained.


### Quantum error cancellation in photonic systems -- undoing photon losses
**Authors**: Adam Taylor, Gabriele Bressanini, Hyukjoon Kwon, M. S. Kim

**Published Date**: 2024-03-08

**Updated Date**: 2024-06-28

**PDF Url**: [2403.05252v2](http://arxiv.org/pdf/2403.05252v2)

**Abstract**: Real photonic devices are subject to photon losses that can decohere quantum
information encoded in the system. In the absence of full fault tolerance,
quantum error mitigation techniques have been introduced to help manage errors
in noisy quantum devices. In this work, we introduce an error mitigation
protocol inspired by probabilistic error cancellation (a popular error
mitigation technique in discrete variable systems) for continuous variable
systems. We show that our quantum error cancellation protocol can undo photon
losses in expectation value estimation tasks. To do this, we analytically
derive the (non-physical) inverse photon loss channel and decompose it into a
sum over physically realisable channels with potentially negative coefficients.
The bias of our ideal expectation value estimator can be made arbitrarily small
at the cost of increasing the sampling overhead. The protocol requires a
noiseless amplification followed by a series of photon-subtractions. While
these operations can be implemented probabilistically, for certain classes of
initial state one can avoid the burden of carrying out the amplification and
photon-subtractions by leveraging Monte-Carlo methods to give an unbiased
estimate of the ideal expectation value. We validate our proposed mitigation
protocol by simulating the scheme on squeezed vacuum states, cat states and
entangled coherent states.


### Scalable Bayesian uncertainty quantification with data-driven priors for radio interferometric imaging
**Authors**: Tobías I. Liaudat, Matthijs Mars, Matthew A. Price, Marcelo Pereyra, Marta M. Betcke, Jason D. McEwen

**Published Date**: 2023-11-30

**Updated Date**: 2024-06-28

**PDF Url**: [2312.00125v2](http://arxiv.org/pdf/2312.00125v2)

**Abstract**: Next-generation radio interferometers like the Square Kilometer Array have
the potential to unlock scientific discoveries thanks to their unprecedented
angular resolution and sensitivity. One key to unlocking their potential
resides in handling the deluge and complexity of incoming data. This challenge
requires building radio interferometric imaging methods that can cope with the
massive data sizes and provide high-quality image reconstructions with
uncertainty quantification (UQ). This work proposes a method coined QuantifAI
to address UQ in radio-interferometric imaging with data-driven (learned)
priors for high-dimensional settings. Our model, rooted in the Bayesian
framework, uses a physically motivated model for the likelihood. The model
exploits a data-driven convex prior, which can encode complex information
learned implicitly from simulations and guarantee the log-concavity of the
posterior. We leverage probability concentration phenomena of high-dimensional
log-concave posteriors that let us obtain information about the posterior,
avoiding MCMC sampling techniques. We rely on convex optimisation methods to
compute the MAP estimation, which is known to be faster and better scale with
dimension than MCMC sampling strategies. Our method allows us to compute local
credible intervals, i.e., Bayesian error bars, and perform hypothesis testing
of structure on the reconstructed image. In addition, we propose a novel
blazing-fast method to compute pixel-wise uncertainties at different scales. We
demonstrate our method by reconstructing radio-interferometric images in a
simulated setting and carrying out fast and scalable UQ, which we validate with
MCMC sampling. Our method shows an improved image quality and more meaningful
uncertainties than the benchmark method based on a sparsity-promoting prior.
QuantifAI's source code: https://github.com/astro-informatics/QuantifAI.


### Tracer dynamics in the active random average process
**Authors**: Saikat Santra, Prashant Singh, Anupam Kundu

**Published Date**: 2023-07-19

**Updated Date**: 2024-06-28

**PDF Url**: [2307.09908v3](http://arxiv.org/pdf/2307.09908v3)

**Abstract**: We investigate the dynamics of tracer particles in the random average process
(RAP), a single-file system in one dimension. In addition to the position,
every particle possesses an internal spin variable $\sigma (t)$ that can
alternate between two values, $\pm 1$, at a constant rate $\gamma$. Physically,
the value of $\sigma (t)$ dictates the direction of motion of the corresponding
particle and for finite $\gamma$, every particle performs a non-Markovian
active dynamics. Herein, we study the effect of this non-Markovianity in the
fluctuations and correlations of the positions of tracer particles. We
analytically show that the variance of the position of a tagged particle grows
sub-diffusively as $\sim \zeta_{\text{q}} \sqrt{t}$ at large times for the
quenched uniform initial condition. While this sub-diffusive growth is
identical to that of the Markovian/non-persistent RAP, the coefficient
$\zeta_{\text{q}} $ is rather different and bears the signature of the
persistent motion of active particles through higher point correlations (unlike
in the Markovian case). Similarly, for the annealed (steady state) initial
condition, we find that the variance scales as $\sim \zeta_{\text{a}} \sqrt{t}$
at large times with coefficient $\zeta_{\text{a}} $ once again different from
the non-persistent case. Although $\zeta_{\text{q}}$ and $\zeta_{\text{a}} $
both individually depart from their Markov counterparts, their ratio
$\zeta_{\text{a}} / \zeta_{\text{q}}$ is still equal to $\sqrt{2}$, a condition
observed for other diffusive single-file systems. This condition turns out to
be true even in the strongly active regimes as corroborated by extensive
simulations and calculations. Finally, we study the correlation between the
positions of two tagged particles in both quenched uniform and annealed initial
conditions. We verify all our analytic results by extensive numerical
simulations.


### Text2Robot: Evolutionary Robot Design from Text Descriptions
**Authors**: Ryan P. Ringel, Zachary S. Charlick, Jiaxun Liu, Boxi Xia, Boyuan Chen

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.19963v1](http://arxiv.org/pdf/2406.19963v1)

**Abstract**: Robot design has traditionally been costly and labor-intensive. Despite
advancements in automated processes, it remains challenging to navigate a vast
design space while producing physically manufacturable robots. We introduce
Text2Robot, a framework that converts user text specifications and performance
preferences into physical quadrupedal robots. Within minutes, Text2Robot can
use text-to-3D models to provide strong initializations of diverse
morphologies. Within a day, our geometric processing algorithms and
body-control co-optimization produce a walking robot by explicitly considering
real-world electronics and manufacturability. Text2Robot enables rapid
prototyping and opens new opportunities for robot design with generative
models.


### Gauge invariant quantum backreaction in U(1) axion inflation
**Authors**: Davide Campanella Galanti, Pietro Conzinu, Giovanni Marozzi, Simony Santos da Costa

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.19960v1](http://arxiv.org/pdf/2406.19960v1)

**Abstract**: We evaluate the quantum backreaction due to a gauge field coupled to a pseudo
scalar field driving a slow-roll inflationary stage, the so-called axion
inflation. The backreaction is evaluated for the first time using a gauge
invariant approach, going to second order in perturbation theory and taking in
consideration inflaton fluctuations as well as scalar perturbations of the
metric. Within our gauge invariant, but observer-dependent approach, we
naturally consider as physical observer the one comoving with the inflaton
field. Considering the effective expansion rate consequent to the gauge fields
bacreaction, we observe that the backreaction effect becomes significant quite
rapidly, moving the system out of the perturbative regime and into what is
often referred to the strong backreaction regime. This behavior also applies to
the parameter which dictates the production of the gauge fields. The space-time
dynamic is initially mainly influenced by the helicity contribution, with a
significant response to the energy density which occurs much later with respect
to the number of e-folds. As a final result, we see that the evaluated
backreaction prolongs the inflationary period much more compared to the
scenarios previously studied neglecting scalar metric perturbations.


## Diffusion
### On the Trade-off between Flatness and Optimization in Distributed Learning
**Authors**: Ying Cao, Zhaoxian Wu, Kun Yuan, Ali H. Sayed

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.20006v1](http://arxiv.org/pdf/2406.20006v1)

**Abstract**: This paper proposes a theoretical framework to evaluate and compare the
performance of gradient-descent algorithms for distributed learning in relation
to their behavior around local minima in nonconvex environments. Previous works
have noticed that convergence toward flat local minima tend to enhance the
generalization ability of learning algorithms. This work discovers two
interesting results. First, it shows that decentralized learning strategies are
able to escape faster away from local minimizers and favor convergence toward
flatter minima relative to the centralized solution in the large-batch training
regime. Second, and importantly, the ultimate classification accuracy is not
solely dependent on the flatness of the local minimizer but also on how well a
learning algorithm can approach that minimum. In other words, the
classification accuracy is a function of both flatness and optimization
performance. The paper examines the interplay between the two measures of
flatness and optimization error closely. One important conclusion is that
decentralized strategies of the diffusion type deliver enhanced classification
accuracy because it strikes a more favorable balance between flatness and
optimization performance.


### Kandinsky 3.0 Technical Report
**Authors**: Vladimir Arkhipkin, Andrei Filatov, Viacheslav Vasilev, Anastasia Maltseva, Said Azizov, Igor Pavlov, Julia Agafonova, Andrey Kuznetsov, Denis Dimitrov

**Published Date**: 2023-12-06

**Updated Date**: 2024-06-28

**PDF Url**: [2312.03511v3](http://arxiv.org/pdf/2312.03511v3)

**Abstract**: We present Kandinsky 3.0, a large-scale text-to-image generation model based
on latent diffusion, continuing the series of text-to-image Kandinsky models
and reflecting our progress to achieve higher quality and realism of image
generation. In this report we describe the architecture of the model, the data
collection procedure, the training technique, and the production system for
user interaction. We focus on the key components that, as we have identified as
a result of a large number of experiments, had the most significant impact on
improving the quality of our model compared to the others. We also describe
extensions and applications of our model, including super resolution,
inpainting, image editing, image-to-video generation, and a distilled version
of Kandinsky 3.0 - Kandinsky 3.1, which does inference in 4 steps of the
reverse process and 20 times faster without visual quality decrease. By
side-by-side human preferences comparison, Kandinsky becomes better in text
understanding and works better on specific domains. The code is available at
https://github.com/ai-forever/Kandinsky-3


### Deceptive Diffusion: Generating Synthetic Adversarial Examples
**Authors**: Lucas Beerens, Catherine F. Higham, Desmond J. Higham

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.19807v1](http://arxiv.org/pdf/2406.19807v1)

**Abstract**: We introduce the concept of deceptive diffusion -- training a generative AI
model to produce adversarial images. Whereas a traditional adversarial attack
algorithm aims to perturb an existing image to induce a misclassificaton, the
deceptive diffusion model can create an arbitrary number of new, misclassified
images that are not directly associated with training or test images. Deceptive
diffusion offers the possibility of strengthening defence algorithms by
providing adversarial training data at scale, including types of
misclassification that are otherwise difficult to find. In our experiments, we
also investigate the effect of training on a partially attacked data set. This
highlights a new type of vulnerability for generative diffusion models: if an
attacker is able to stealthily poison a portion of the training data, then the
resulting diffusion model will generate a similar proportion of misleading
outputs.


### DISCO: Efficient Diffusion Solver for Large-Scale Combinatorial Optimization Problems
**Authors**: Kexiong Yu, Hang Zhao, Yuhang Huang, Renjiao Yi, Kai Xu, Chenyang Zhu

**Published Date**: 2024-06-28

**Updated Date**: 2024-06-28

**PDF Url**: [2406.19705v1](http://arxiv.org/pdf/2406.19705v1)

**Abstract**: Combinatorial Optimization (CO) problems are fundamentally crucial in
numerous practical applications across diverse industries, characterized by
entailing enormous solution space and demanding time-sensitive response.
Despite significant advancements made by recent neural solvers, their limited
expressiveness does not conform well to the multi-modal nature of CO
landscapes. While some research has pivoted towards diffusion models, they
require simulating a Markov chain with many steps to produce a sample, which is
time-consuming and does not meet the efficiency requirement of real
applications, especially at scale. We propose DISCO, an efficient DIffusion
Solver for Combinatorial Optimization problems that excels in both solution
quality and inference speed. DISCO's efficacy is two-pronged: Firstly, it
achieves rapid denoising of solutions through an analytically solvable form,
allowing for direct sampling from the solution space with very few reverse-time
steps, thereby drastically reducing inference time. Secondly, DISCO enhances
solution quality by restricting the sampling space to a more constrained,
meaningful domain guided by solution residues, while still preserving the
inherent multi-modality of the output probabilistic distributions. DISCO
achieves state-of-the-art results on very large Traveling Salesman Problems
with 10000 nodes and challenging Maximal Independent Set benchmarks, with its
per-instance denoising time up to 44.8 times faster. Through further combining
a divide-and-conquer strategy, DISCO can be generalized to solve
arbitrary-scale problem instances off the shelf, even outperforming models
trained specifically on corresponding scales.


### Behavior Generation with Latent Actions
**Authors**: Seungjae Lee, Yibin Wang, Haritheja Etukuru, H. Jin Kim, Nur Muhammad Mahi Shafiullah, Lerrel Pinto

**Published Date**: 2024-03-05

**Updated Date**: 2024-06-28

**PDF Url**: [2403.03181v2](http://arxiv.org/pdf/2403.03181v2)

**Abstract**: Generative modeling of complex behaviors from labeled datasets has been a
longstanding problem in decision making. Unlike language or image generation,
decision making requires modeling actions - continuous-valued vectors that are
multimodal in their distribution, potentially drawn from uncurated sources,
where generation errors can compound in sequential prediction. A recent class
of models called Behavior Transformers (BeT) addresses this by discretizing
actions using k-means clustering to capture different modes. However, k-means
struggles to scale for high-dimensional action spaces or long sequences, and
lacks gradient information, and thus BeT suffers in modeling long-range
actions. In this work, we present Vector-Quantized Behavior Transformer
(VQ-BeT), a versatile model for behavior generation that handles multimodal
action prediction, conditional generation, and partial observations. VQ-BeT
augments BeT by tokenizing continuous actions with a hierarchical vector
quantization module. Across seven environments including simulated
manipulation, autonomous driving, and robotics, VQ-BeT improves on
state-of-the-art models such as BeT and Diffusion Policies. Importantly, we
demonstrate VQ-BeT's improved ability to capture behavior modes while
accelerating inference speed 5x over Diffusion Policies. Videos and code can be
found https://sjlee.cc/vq-bet


## Quantitative Finance
### A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist
**Authors**: Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao, Yilei Zhao, Xinyu Cai, Longtao Zheng, Xinrun Wang, Bo An

**Published Date**: 2024-02-28

**Updated Date**: 2024-06-28

**PDF Url**: [2402.18485v3](http://arxiv.org/pdf/2402.18485v3)

**Abstract**: Financial trading is a crucial component of the markets, informed by a
multimodal information landscape encompassing news, prices, and Kline charts,
and encompasses diverse tasks such as quantitative trading and high-frequency
trading with various assets. While advanced AI techniques like deep learning
and reinforcement learning are extensively utilized in finance, their
application in financial trading tasks often faces challenges due to inadequate
handling of multimodal data and limited generalizability across various tasks.
To address these challenges, we present FinAgent, a multimodal foundational
agent with tool augmentation for financial trading. FinAgent's market
intelligence module processes a diverse range of data-numerical, textual, and
visual-to accurately analyze the financial market. Its unique dual-level
reflection module not only enables rapid adaptation to market dynamics but also
incorporates a diversified memory retrieval system, enhancing the agent's
ability to learn from historical data and improve decision-making processes.
The agent's emphasis on reasoning for actions fosters trust in its financial
decisions. Moreover, FinAgent integrates established trading strategies and
expert insights, ensuring that its trading approaches are both data-driven and
rooted in sound financial principles. With comprehensive experiments on 6
financial datasets, including stocks and Crypto, FinAgent significantly
outperforms 9 state-of-the-art baselines in terms of 6 financial metrics with
over 36% average improvement on profit. Specifically, a 92.27% return (a 84.39%
relative improvement) is achieved on one dataset. Notably, FinAgent is the
first advanced multimodal foundation agent designed for financial trading
tasks.


