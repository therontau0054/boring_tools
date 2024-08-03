# Abstracts of Papers

## Physics
### To reset, or not to reset -- that is the question
**Authors**: György P. Gehér, Marcin Jastrzebski, Earl T. Campbell, Ophelia Crawford

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00758v1](http://arxiv.org/pdf/2408.00758v1)

**Abstract**: Whether to reset qubits, or not, during quantum error correction experiments
is a question of both foundational and practical importance for quantum
computing. Text-book quantum error correction demands that qubits are reset
after measurement. However, fast qubit reset has proven challenging to execute
at high fidelity. Consequently, many cutting-edge quantum error correction
experiments are opting for the no-reset approach, where physical reset is not
performed. It has recently been postulated that no-reset is functionally
equivalent to reset procedures, as well as being faster and easier. For memory
experiments, we confirm numerically that resetting provides no benefit. On the
other hand, we identify a remarkable difference during logical operations. We
find that unconditionally resetting qubits can reduce the duration of
fault-tolerant logical operation by up to a factor of two as the number of
measurement errors that can be tolerated is doubled. We support this with
numerical simulations. However, our simulations also reveal that the no-reset
performance is superior if the reset duration or infidelity exceeds a given
threshold. Lastly, we introduce two novel syndrome extraction circuits that can
reduce the time overhead of no-reset approaches. Our findings provide guidance
on how experimentalists should design future experiments.


### Thermal Conductivity Predictions with Foundation Atomistic Models
**Authors**: Balázs Póta, Paramvir Ahlawat, Gábor Csányi, Michele Simoncelli

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00755v1](http://arxiv.org/pdf/2408.00755v1)

**Abstract**: Recent advances in machine learning have led to foundation models for
atomistic materials chemistry, potentially enabling quantum-accurate
descriptions of interatomic forces at reduced computational cost. These models
are benchmarked by predicting materials' properties over large databases;
however, these computationally intensive tests have been limited to basic
quantities related to harmonic phonons, leaving uncertainty about the
reliability for complex, technologically and experimentally relevant anharmonic
heat-conduction properties. Here we present an automated framework that relies
on foundation models to compute microscopic vibrational properties, and employs
them within the Wigner formulation of heat transport to predict the macroscopic
thermal conductivity in solids with arbitrary composition and structure. We
apply this framework with the foundation models M3GNet, CHGNet, MACE-MP-0, and
SevenNET to 103 diverse compounds, comparing predictions against
first-principles references and introducing a benchmark metric based on
conductivity. This framework paves the way for physics-aware, accurate
predictions of vibrational and thermal properties, and for uncovering materials
that violate semiclassical Boltzmann transport and feature exceptional
heat-shielding or thermoelectric performance.


### The Inevitable Quark Three-Body Force and its Implications for Exotic States
**Authors**: Sungsik Noh, Aaron Park, Hyeongock Yun, Sungtae Cho, Su Houng Lee

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00715v1](http://arxiv.org/pdf/2408.00715v1)

**Abstract**: Three-body nuclear forces are essential for explaining the properties of
light nuclei with a nucleon number greater than three. Building on insights
from nuclear physics, we extract the form of quark three-body interactions and
demonstrate that these terms are crucial for extending the quark model fit of
the meson spectrum to include baryons using the same parameter set. We then
discuss the implications of our findings for exotic configurations involving
more than three quarks, such as the $T_{cc}$ and $\chi_{c1}(3872)$. We find
that the quark three-body interactions provide additional repulsion on the
order of 10 MeV for the compact configurations of both the $T_{cc}$ and
$\chi_{c1}(3872)$. This result, combined with previous calculations, strongly
suggests that these tetraquark states are molecular rather than compact states.


### Attosecond Probing of Coherent Vibrational Dynamics in CBr$_4$
**Authors**: Jen-Hao Ou, Diptarka Hait, Patrick Rupprecht, John E. Beetar, Todd J. Martínez, Stephen R. Leone

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00696v1](http://arxiv.org/pdf/2408.00696v1)

**Abstract**: A coherent vibrational wavepacket is launched and manipulated in the
symmetric stretch (a$_1$) mode of CBr$_4$, by impulsive stimulated Raman
scattering from non-resonant 400 nm laser pump pulses with various peak
intensities on the order of tens of 10$^{12}$ W/cm$^2$. Extreme ultraviolet
(XUV) attosecond transient absorption spectroscopy (ATAS) records the
wavepacket dynamics as temporal oscillations in XUV absorption energy at the
bromine M$_{4,5}$ 3d$_{3/2,5/2}$ edges around 70 eV. The results are augmented
by nuclear time-dependent Schr\"odinger equation simulations. Slopes of the
(Br-3d$_{3/2,5/2}$)$^{-1}$10a$_1^*$ core-excited state potential energy surface
(PES) along the a$_1$ mode are calculated to be -9.4 eV/{\AA} from restricted
open-shell Kohn-Sham calculations. Using analytical relations derived for the
small-displacement limit with the calculated slopes of the core-excited state
PES, a deeper insight into the vibrational dynamics is obtained by retrieving
the experimental excursion amplitude of the vibrational wavepacket and the
amount of population transferred to the vibrational first-excited state, as a
function of pump-pulse peak intensity. Experimentally, the results show that
XUV ATAS is capable of easily resolving oscillations in the XUV absorption
energy on the order of few to tens of meV and tens of femtosecond time
precision, limited only by the averaging times in the experimental scans. This
corresponds to oscillations of C-Br bond length on the order of 10$^{-4}$ to
10$^{-3}$ {\AA}. The results and the analytic relationships offer a clear
physical picture, on multiple levels of understanding, for how the pump-pulse
intensity controls the vibrational dynamics launched by non-resonant ISRS in
the small-displacement limit.


### Accelerating Full Waveform Inversion By Transfer Learning
**Authors**: Divya Shyam Singh, Leon Herrmann, Qing Sun, Tim Bürchner, Felix Dietrich, Stefan Kollmannsberger

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00695v1](http://arxiv.org/pdf/2408.00695v1)

**Abstract**: Full waveform inversion (FWI) is a powerful tool for reconstructing material
fields based on sparsely measured data obtained by wave propagation. For
specific problems, discretizing the material field with a neural network (NN)
improves the robustness and reconstruction quality of the corresponding
optimization problem. We call this method NN-based FWI. Starting from an
initial guess, the weights of the NN are iteratively updated to fit the
simulated wave signals to the sparsely measured data set. For gradient-based
optimization, a suitable choice of the initial guess, i.e., a suitable NN
weight initialization, is crucial for fast and robust convergence.
  In this paper, we introduce a novel transfer learning approach to further
improve NN-based FWI. This approach leverages supervised pretraining to provide
a better NN weight initialization, leading to faster convergence of the
subsequent optimization problem. Moreover, the inversions yield physically more
meaningful local minima. The network is pretrained to predict the unknown
material field using the gradient information from the first iteration of
conventional FWI. In our computational experiments on two-dimensional domains,
the training data set consists of reference simulations with arbitrarily
positioned elliptical voids of different shapes and orientations. We compare
the performance of the proposed transfer learning NN-based FWI with three other
methods: conventional FWI, NN-based FWI without pretraining and conventional
FWI with an initial guess predicted from the pretrained NN. Our results show
that transfer learning NN-based FWI outperforms the other methods in terms of
convergence speed and reconstruction quality.


### Subspace-projected multireference covariant density functional theory
**Authors**: X. Zhang, C. C. Wang, C. R. Ding, J. M. Yao

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00691v1](http://arxiv.org/pdf/2408.00691v1)

**Abstract**: Multireference density functional theory (MR-DFT) has been a pivotal method
for studying nuclear spectroscopy and neutrinoless double-beta
($0\nu\beta\beta$) decay. However, quantifying their theoretical uncertainties
has been a significant challenge due to the computational demands. This study
introduces a subspace-projected covariant density functional theory (SP-CDFT),
which efficiently emulates MR-CDFT calculations for nuclear low-lying states.
This approach leverages the eigenvector continuation method combined with the
quantum-number projected generator coordinate method, based on a relativistic
energy density functional (EDF). We apply SP-CDFT to investigate the
correlations among the physical quantities of nuclear matter, nuclear low-lying
spectroscopy, and the nuclear matrix elements (NMEs) of $0\nu\beta\beta$ decay
in the two heaviest candidate nuclei. Our findings reveal generally strong
correlations between the NMEs of $0\nu\beta\beta$ decay and the excitation
energy of the $2_1^+$ state, as well as the $E2$ transition strength, although
these correlations vary significantly among nuclei. The Bayesian analysis,
which integrates the properties of nuclear matter and low-lying states, yields
mean values and statistical uncertainties for the NMEs 4.33(5) for $^{136}$Xe
and 5.51(14) for $^{150}$Nd. This work also paves the way for refining nuclear
EDF parameters using spectroscopic data.


### Application of Transformers for Nonlinear Channel Compensation in Optical Systems
**Authors**: Behnam Behinaein Hamgini, Hossein Najafi, Ali Bakhshali, Zhuhong Zhang

**Published Date**: 2023-04-25

**Updated Date**: 2024-08-01

**PDF Url**: [2304.13119v3](http://arxiv.org/pdf/2304.13119v3)

**Abstract**: In this paper, we introduce a new nonlinear optical channel equalizer based
on Transformers. By leveraging parallel computation and attending directly to
the memory across a sequence of symbols, we show that Transformers can be used
effectively for nonlinear compensation (NLC) in coherent long-haul transmission
systems. For this application, we present an implementation of the encoder part
of the Transformer and analyze its performance over a wide range of different
hyper-parameters. It is shown that by proper embeddings and processing blocks
of symbols at each iteration and also carefully selecting subsets of the
encoder's output to be processed together, an efficient nonlinear equalization
can be achieved for different complexity constraints. To reduce the
computational complexity of the attention mechanism, we further propose the use
of a physic-informed mask inspired by nonlinear perturbation theory. We also
compare the Transformer-NLC with digital back-propagation (DBP) under different
transmission scenarios in order to demonstrate the flexibility and
generalizability of the proposed data-driven solution.


### Actor-Critic Physics-informed Neural Lyapunov Control
**Authors**: Jiarui Wang, Mahyar Fazlyab

**Published Date**: 2024-03-13

**Updated Date**: 2024-08-01

**PDF Url**: [2403.08448v2](http://arxiv.org/pdf/2403.08448v2)

**Abstract**: Designing control policies for stabilization tasks with provable guarantees
is a long-standing problem in nonlinear control. A crucial performance metric
is the size of the resulting region of attraction, which essentially serves as
a robustness "margin" of the closed-loop system against uncertainties. In this
paper, we propose a new method to train a stabilizing neural network controller
along with its corresponding Lyapunov certificate, aiming to maximize the
resulting region of attraction while respecting the actuation constraints.
Crucial to our approach is the use of Zubov's Partial Differential Equation
(PDE), which precisely characterizes the true region of attraction of a given
control policy. Our framework follows an actor-critic pattern where we
alternate between improving the control policy (actor) and learning a Zubov
function (critic). Finally, we compute the largest certifiable region of
attraction by invoking an SMT solver after the training procedure. Our
numerical experiments on several design problems show consistent and
significant improvements in the size of the resulting region of attraction.


### Graph neural network-based surrogate modelling for real-time hydraulic prediction of urban drainage networks
**Authors**: Zhiyu Zhang, Chenkaixiang Lu, Wenchong Tian, Zhenliang Liao, Zhiguo Yuan

**Published Date**: 2024-04-16

**Updated Date**: 2024-08-01

**PDF Url**: [2404.10324v2](http://arxiv.org/pdf/2404.10324v2)

**Abstract**: Physics-based models are computationally time-consuming and infeasible for
real-time scenarios of urban drainage networks, and a surrogate model is needed
to accelerate the online predictive modelling. Fully-connected neural networks
(NNs) are potential surrogate models, but may suffer from low interpretability
and efficiency in fitting complex targets. Owing to the state-of-the-art
modelling power of graph neural networks (GNNs) and their match with urban
drainage networks in the graph structure, this work proposes a GNN-based
surrogate of the flow routing model for the hydraulic prediction problem of
drainage networks, which regards recent hydraulic states as initial conditions,
and future runoff and control policy as boundary conditions. To incorporate
hydraulic constraints and physical relationships into drainage modelling,
physics-guided mechanisms are designed on top of the surrogate model to
restrict the prediction variables with flow balance and flooding occurrence
constraints. According to case results in a stormwater network, the GNN-based
model is more cost-effective with better hydraulic prediction accuracy than the
NN-based model after equal training epochs, and the designed mechanisms further
limit prediction errors with interpretable domain knowledge. As the model
structure adheres to the flow routing mechanisms and hydraulic constraints in
urban drainage networks, it provides an interpretable and effective solution
for data-driven surrogate modelling. Simultaneously, the surrogate model
accelerates the predictive modelling of urban drainage networks for real-time
use compared with the physics-based model.


### Distributed quantum architecture search
**Authors**: Haozhen Situ, Zhimin He, Shenggen Zheng, Lvzhou Li

**Published Date**: 2024-03-10

**Updated Date**: 2024-08-01

**PDF Url**: [2403.06214v2](http://arxiv.org/pdf/2403.06214v2)

**Abstract**: Variational quantum algorithms, inspired by neural networks, have become a
novel approach in quantum computing. However, designing efficient parameterized
quantum circuits remains a challenge. Quantum architecture search tackles this
by adjusting circuit structures along with gate parameters to automatically
discover high-performance circuit structures. In this study, we propose an
end-to-end distributed quantum architecture search framework, where we aim to
automatically design distributed quantum circuit structures for interconnected
quantum processing units with specific qubit connectivity. We devise a circuit
generation algorithm which incorporates TeleGate and TeleData methods to enable
nonlocal gate implementation across quantum processing units. While taking into
account qubit connectivity, we also incorporate qubit assignment from logical
to physical qubits within our quantum architecture search framework. A
two-stage progressive training-free strategy is employed to evaluate extensive
circuit structures without circuit training costs. Through numerical
experiments on three VQE tasks, the efficacy and efficiency of our scheme is
demonstrated. Our research into discovering efficient structures for
distributed quantum circuits is crucial for near-term quantum computing where a
single quantum processing unit has a limited number of qubits. Distributed
quantum circuits allow for breaking down complex computations into manageable
parts that can be processed across multiple quantum processing units.


## Diffusion
### Smoothed Energy Guidance: Guiding Diffusion Models with Reduced Energy Curvature of Attention
**Authors**: Susung Hong

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00760v1](http://arxiv.org/pdf/2408.00760v1)

**Abstract**: Conditional diffusion models have shown remarkable success in visual content
generation, producing high-quality samples across various domains, largely due
to classifier-free guidance (CFG). Recent attempts to extend guidance to
unconditional models have relied on heuristic techniques, resulting in
suboptimal generation quality and unintended effects. In this work, we propose
Smoothed Energy Guidance (SEG), a novel training- and condition-free approach
that leverages the energy-based perspective of the self-attention mechanism to
enhance image generation. By defining the energy of self-attention, we
introduce a method to reduce the curvature of the energy landscape of attention
and use the output as the unconditional prediction. Practically, we control the
curvature of the energy landscape by adjusting the Gaussian kernel parameter
while keeping the guidance scale parameter fixed. Additionally, we present a
query blurring method that is equivalent to blurring the entire attention
weights without incurring quadratic complexity in the number of tokens. In our
experiments, SEG achieves a Pareto improvement in both quality and the
reduction of side effects. The code is available at
\url{https://github.com/SusungHong/SEG-SDXL}.


### TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models
**Authors**: Gilad Deutch, Rinon Gal, Daniel Garibi, Or Patashnik, Daniel Cohen-Or

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00735v1](http://arxiv.org/pdf/2408.00735v1)

**Abstract**: Diffusion models have opened the path to a wide range of text-based image
editing frameworks. However, these typically build on the multi-step nature of
the diffusion backwards process, and adapting them to distilled, fast-sampling
methods has proven surprisingly challenging. Here, we focus on a popular line
of text-based editing frameworks - the ``edit-friendly'' DDPM-noise inversion
approach. We analyze its application to fast sampling methods and categorize
its failures into two classes: the appearance of visual artifacts, and
insufficient editing strength. We trace the artifacts to mismatched noise
statistics between inverted noises and the expected noise schedule, and suggest
a shifted noise schedule which corrects for this offset. To increase editing
strength, we propose a pseudo-guidance approach that efficiently increases the
magnitude of edits without introducing new artifacts. All in all, our method
enables text-based image editing with as few as three diffusion steps, while
providing novel insights into the mechanisms behind popular text-based editing
approaches.


### Alpha-VI DeepONet: A prior-robust variational Bayesian approach for enhancing DeepONets with uncertainty quantification
**Authors**: Soban Nasir Lone, Subhayan De, Rajdip Nayek

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00681v1](http://arxiv.org/pdf/2408.00681v1)

**Abstract**: We introduce a novel deep operator network (DeepONet) framework that
incorporates generalised variational inference (GVI) using R\'enyi's
$\alpha$-divergence to learn complex operators while quantifying uncertainty.
By incorporating Bayesian neural networks as the building blocks for the branch
and trunk networks, our framework endows DeepONet with uncertainty
quantification. The use of R\'enyi's $\alpha$-divergence, instead of the
Kullback-Leibler divergence (KLD), commonly used in standard variational
inference, mitigates issues related to prior misspecification that are
prevalent in Variational Bayesian DeepONets. This approach offers enhanced
flexibility and robustness. We demonstrate that modifying the variational
objective function yields superior results in terms of minimising the mean
squared error and improving the negative log-likelihood on the test set. Our
framework's efficacy is validated across various mechanical systems, where it
outperforms both deterministic and standard KLD-based VI DeepONets in
predictive accuracy and uncertainty quantification. The hyperparameter
$\alpha$, which controls the degree of robustness, can be tuned to optimise
performance for specific problems. We apply this approach to a range of
mechanics problems, including gravity pendulum, advection-diffusion, and
diffusion-reaction systems. Our findings underscore the potential of
$\alpha$-VI DeepONet to advance the field of data-driven operator learning and
its applications in engineering and scientific domains.


### Illustrating Classic Brazilian Books using a Text-To-Image Diffusion Model
**Authors**: Felipe Mahlow, André Felipe Zanella, William Alberto Cruz Castañeda, Regilene Aparecida Sarzi-Ribeiro

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00544v1](http://arxiv.org/pdf/2408.00544v1)

**Abstract**: In recent years, Generative Artificial Intelligence (GenAI) has undergone a
profound transformation in addressing intricate tasks involving diverse
modalities such as textual, auditory, visual, and pictorial generation. Within
this spectrum, text-to-image (TTI) models have emerged as a formidable approach
to generating varied and aesthetically appealing compositions, spanning
applications from artistic creation to realistic facial synthesis, and
demonstrating significant advancements in computer vision, image processing,
and multimodal tasks. The advent of Latent Diffusion Models (LDMs) signifies a
paradigm shift in the domain of AI capabilities. This article delves into the
feasibility of employing the Stable Diffusion LDM to illustrate literary works.
For this exploration, seven classic Brazilian books have been selected as case
studies. The objective is to ascertain the practicality of this endeavor and to
evaluate the potential of Stable Diffusion in producing illustrations that
augment and enrich the reader's experience. We will outline the beneficial
aspects, such as the capacity to generate distinctive and contextually
pertinent images, as well as the drawbacks, including any shortcomings in
faithfully capturing the essence of intricate literary depictions. Through this
study, we aim to provide a comprehensive assessment of the viability and
efficacy of utilizing AI-generated illustrations in literary contexts,
elucidating both the prospects and challenges encountered in this pioneering
application of technology.


### A new approach for encoding code and assisting code understanding
**Authors**: Mengdan Fan, Wei Zhang, Haiyan Zhao, Zhi Jin

**Published Date**: 2024-08-01

**Updated Date**: 2024-08-01

**PDF Url**: [2408.00521v1](http://arxiv.org/pdf/2408.00521v1)

**Abstract**: Some companies(e.g., Microsoft Research and Google DeepMind) have discovered
some of the limitations of GPTs autoregressive paradigm next-word prediction,
manifested in the model lack of planning, working memory, backtracking, and
reasoning skills. GPTs rely on a local and greedy process of generating the
next word, without a global understanding of the task or the output.We have
confirmed the above limitations through specialized empirical studies of code
comprehension. Although GPT4 is good at producing fluent and coherent text, it
cannot handle complex logic and generate new code that haven not been seen, and
it relies too much on the formatting of the prompt to generate the correct
code.We propose a new paradigm for code understanding that goes beyond the
next-word prediction paradigm, inspired by the successful application of
diffusion techniques to image generation(Dalle2, Sora) and protein structure
generation(AlphaFold3), which have no autoregressive constraints.Instead of
encoding the code in a form that mimics natural language, we encode the code as
a heterogeneous image paradigm with a memory of global information that mimics
both images and protein structures.We then refer to Sora's CLIP upstream
text-to-image encoder model to design a text-to-code encoder model that can be
applied to various downstream code understanding tasks.The model learns the
global understanding of code under the new paradigm heterogeneous image,
connects the encoding space of text and code, and encodes the input of text
into the vector of code most similar to it.Using self-supervised comparative
learning on 456,360 text-code pairs, the model achieved a zero-shot prediction
of new data. This work is the basis for future work on code generation using
diffusion techniques under a new paradigm to avoid autoregressive limitations.


