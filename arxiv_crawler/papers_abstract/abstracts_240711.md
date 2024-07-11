# Abstracts of Papers

## Physics
### Quantum Decoherence Effects: a complete treatment
**Authors**: Gabriela Barenboim, Alberto M. Gago

**Published Date**: 2024-02-05

**Updated Date**: 2024-07-10

**PDF Url**: [2402.03438v2](http://arxiv.org/pdf/2402.03438v2)

**Abstract**: Physical systems in real life are inextricably linked to their surroundings
and never completely separated from them. Truly closed systems do not exist.
The phenomenon of decoherence, which is brought about by the interaction with
the environment, removes the relative phase of quantum states in superposition
and makes them incoherent. In neutrino physics, decoherence, although
extensively studied has only been analyzed thus far, exclusively in terms of
its dissipative characteristics. While it is true that dissipation, or the
exponential suppression, eventually is the main observable effect, the exchange
of energy between the medium and the system, is an important factor that has
been overlooked up until now. In this work, we introduce this term and analyze
its consequences.


### AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation
**Authors**: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07889v1](http://arxiv.org/pdf/2407.07889v1)

**Abstract**: Predictive models are a crucial component of many robotic systems. Yet,
constructing accurate predictive models for a variety of deformable objects,
especially those with unknown physical properties, remains a significant
challenge. This paper introduces AdaptiGraph, a learning-based dynamics
modeling approach that enables robots to predict, adapt to, and control a wide
array of challenging deformable materials with unknown physical properties.
AdaptiGraph leverages the highly flexible graph-based neural dynamics (GBND)
framework, which represents material bits as particles and employs a graph
neural network (GNN) to predict particle motion. Its key innovation is a
unified physical property-conditioned GBND model capable of predicting the
motions of diverse materials with varying physical properties without
retraining. Upon encountering new materials during online deployment,
AdaptiGraph utilizes a physical property optimization process for a few-shot
adaptation of the model, enhancing its fit to the observed interaction data.
The adapted models can precisely simulate the dynamics and predict the motion
of various deformable materials, such as ropes, granular media, rigid boxes,
and cloth, while adapting to different physical properties, including
stiffness, granular size, and center of pressure. On prediction and
manipulation tasks involving a diverse set of real-world deformable objects,
our method exhibits superior prediction accuracy and task proficiency over
non-material-conditioned and non-adaptive models. The project page is available
at https://robopil.github.io/adaptigraph/ .


### Dynamical Measure Transport and Neural PDE Solvers for Sampling
**Authors**: Jingtong Sun, Julius Berner, Lorenz Richter, Marius Zeinhofer, Johannes Müller, Kamyar Azizzadenesheli, Anima Anandkumar

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07873v1](http://arxiv.org/pdf/2407.07873v1)

**Abstract**: The task of sampling from a probability density can be approached as
transporting a tractable density function to the target, known as dynamical
measure transport. In this work, we tackle it through a principled unified
framework using deterministic or stochastic evolutions described by partial
differential equations (PDEs). This framework incorporates prior
trajectory-based sampling methods, such as diffusion models or Schr\"odinger
bridges, without relying on the concept of time-reversals. Moreover, it allows
us to propose novel numerical methods for solving the transport task and thus
sampling from complicated targets without the need for the normalization
constant or data samples. We employ physics-informed neural networks (PINNs) to
approximate the respective PDE solutions, implying both conceptional and
computational advantages. In particular, PINNs allow for simulation- and
discretization-free optimization and can be trained very efficiently, leading
to significantly better mode coverage in the sampling task compared to
alternative methods. Moreover, they can readily be fine-tuned with Gauss-Newton
methods to achieve high accuracy in sampling.


### Synthetic Light-in-Flight
**Authors**: Patrick Cornwall, Manuel Ballester, Stefan Forschner, Muralidhar Madabhushi Balaji, Aggelos Katsaggelos, Florian Willomitzer

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07872v1](http://arxiv.org/pdf/2407.07872v1)

**Abstract**: Light-in-flight (LiF) measurements allow to resolve and visualize the path
that light travels through an arbitrary volumetric scene. Traditional LiF
methods involve expensive high-speed electronics or narrow-pulse light sources.
We present a novel computational LiF approach that only requires
continuous-wave (CW) lasers and off-the-shelf CMOS cameras to capture the full
LiF information about the scene. From multiple CW scene measurements at
different optical wavelengths, we create multiple "synthetic fields," each at a
"synthetic wave" which is the beat wave of two respective optical waves. Due to
their robustness to speckle, the synthetic fields can be computationally
combined into a "synthetic light pulse," which precisely sections the
volumetric scene. Moreover, the complex synthetic fields can be freely
manipulated in the computer after their acquisition, which allows for spatial
and temporal shaping of different sets of pulses from the same set of
measurements to maximize the decoded information output for each scene. In
addition, the relative speed at which the pulse travels through the scene can
be used to characterize physical scene properties such as depth or indices of
refraction.


### Equivalence of two component spinor mechanism and four component spinor mechanism in top quark pair production
**Authors**: Malvika Deo, Anuradha Misra, Sharada Subramaniam, Radhika Vinze

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07836v1](http://arxiv.org/pdf/2407.07836v1)

**Abstract**: In this article, we calculate the $S$-matrix elements for the process $e^{+}
e^{-}\rightarrow t \bar{t}$ mediated by SM photon, $Z$ boson and an additional
$Z^{'}$ boson indicating the contribution from new physics. We calculate the
amplitude square using two component spinor formalism and four component spinor
formalism and show the equivalence of the results using the two formalisms. We
also establish the relations between the couplings of $Z^{'}$ boson to fermions
in the two component spinor formalism and four component spinor formalism.


### TriQXNet: Forecasting Dst Index from Solar Wind Data Using an Interpretable Parallel Classical-Quantum Framework with Uncertainty Quantification
**Authors**: Md Abrar Jahin, M. F. Mridha, Zeyar Aung, Nilanjan Dey, R. Simon Sherratt

**Published Date**: 2024-07-09

**Updated Date**: 2024-07-10

**PDF Url**: [2407.06658v2](http://arxiv.org/pdf/2407.06658v2)

**Abstract**: Geomagnetic storms, caused by solar wind energy transfer to Earth's magnetic
field, can disrupt critical infrastructure like GPS, satellite communications,
and power grids. The disturbance storm-time (Dst) index measures storm
intensity. Despite advancements in empirical, physics-based, and
machine-learning models using real-time solar wind data, accurately forecasting
extreme geomagnetic events remains challenging due to noise and sensor
failures. This research introduces TriQXNet, a novel hybrid classical-quantum
neural network for Dst forecasting. Our model integrates classical and quantum
computing, conformal prediction, and explainable AI (XAI) within a hybrid
architecture. To ensure high-quality input data, we developed a comprehensive
preprocessing pipeline that included feature selection, normalization,
aggregation, and imputation. TriQXNet processes preprocessed solar wind data
from NASA's ACE and NOAA's DSCOVR satellites, predicting the Dst index for the
current hour and the next, providing vital advance notice to mitigate
geomagnetic storm impacts. TriQXNet outperforms 13 state-of-the-art hybrid
deep-learning models, achieving a root mean squared error of 9.27 nanoteslas
(nT). Rigorous evaluation through 10-fold cross-validated paired t-tests
confirmed its superior performance with 95% confidence. Conformal prediction
techniques provide quantifiable uncertainty, which is essential for operational
decisions, while XAI methods like ShapTime enhance interpretability.
Comparative analysis shows TriQXNet's superior forecasting accuracy, setting a
new level of expectations for geomagnetic storm prediction and highlighting the
potential of classical-quantum hybrid models in space weather forecasting.


### Inhibition of splitting of the chiral and deconfinement transition due to rotation in QCD: the phase diagram of linear sigma model coupled to Polyakov loop
**Authors**: Pracheta Singha, Victor E. Ambrus, Maxim N. Chernodub

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07828v1](http://arxiv.org/pdf/2407.07828v1)

**Abstract**: We discuss the effect of rigid rotation on critical temperatures of
deconfinement and chiral transitions in the linear sigma model coupled to
quarks and the Polyakov loop. We point out the essential role of the causality
condition, which requires that any point of the system should rotate slower
than the velocity of light. We show that imposing this physical requirement
leads to inhibition of the splitting between the chiral and confining
transitions, which becomes negligibly small ($\Delta T \sim 1$~MeV or less) for
experimentally relevant, slow angular velocities $\Omega \sim 10$~MeV of a
$(5-10)$~fm-sized systems. Moreover, the boundedness of the system has a much
bigger effect on temperature splitting than the rotation itself: the splitting
reaches 10~MeV in a small, one-fermi-sized non-rotating system. The temperature
splitting may, however, become enhanced in an academic limit of
ultra-relativistic regimes when the boundary of the system rotates at
near-to-light velocities.


### Using Activity to Compartmentalize Binary Mixtures
**Authors**: Nicholas J Lauersdorf, Ehssan Nazockdast, Daphne Klotsa

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07826v1](http://arxiv.org/pdf/2407.07826v1)

**Abstract**: We computationally study suspensions of slow and fast active Brownian
particles that have undergone motility induced phase separation and are at
steady state. Such mixtures, of varying non-zero activity, remain largely
unexplored even though they are relevant for a plethora of systems and
applications ranging from cellular biophysics to drone swarms. Our mixtures are
modulated by their activity ratios ($\mathrm{Pe}^\mathrm{R}$), which we find to
encode information by giving rise to three regimes, each of which display their
unique emergent behaviors. Specifically, we found non-monotonic behavior of
macroscopic properties, e.g. density and pressure, as a function of activity
ratio, microphase separation of fast and slow particle domains, increased
fluctuations on the interface and severe avalanche events compared to
monodisperse active systems. Our approach of simultaneously varying the two
activities of the particle species allowed us to discover these behaviors and
explain the microscopic physical mechanisms that drive them.


### A higher-order generalization of group theory
**Authors**: Balazs Szegedy

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07815v1](http://arxiv.org/pdf/2407.07815v1)

**Abstract**: The goal of this paper is to show that fundamental concepts in higher-order
Fourier analysis can be nauturally extended to the non-commutative setting. We
generalize Gowers norms to arbitrary compact non-commutative groups. On the
structural side, we show that nilspace theory (the algebraic part of
higher-order Fourier analysis) can be naturally extended to include all
non-commutative groups. To this end, we introduce generalized nilspaces called
"groupspaces" and demonstrate that they possess properties very similar to
nilspaces. We study $k$-th order generalizations of groups that are special
groupspaces called {\it k-step} groupspaces. One step groupspaces are groups.
We show that $k$-step groupspaces admit the structure of an iterated principal
bundle with structure groups $G_1,G_2,\dots,G_k$. A similar, but somewhat more
technical statement holds for general groupspaces, with possibly infinitely
many structure groups. Structure groups of groupspaces are in some sense
analogous to higher homotopy groups. In particular we use a version of the
Eckmann-Hilton argument from homotopy theory to show that $G_i$ is abelian for
$i\geq 2$. Groupspaces also show some similarities with $n$-groups from higher
category theory (also used in physics) but the exact relationship between these
concepts is a subject of future research.


### Exploring Subfield Interest Development in Undergraduate Physics Students through Social Cognitive Career Theory
**Authors**: Dina Zohrabi Alaee, Benjamin M. Zwickl

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07808v1](http://arxiv.org/pdf/2407.07808v1)

**Abstract**: This study aims to understand how undergraduate physics majors develop an
interest in specific subfields. We examine interest formation through the lens
of Social Cognitive Career Theory (SCCT) by exploring four key SCCT constructs:
learning experiences, self-efficacy, outcome expectations, and proximal
environmental influences. We conducted 27 interviews with physics majors across
various years of study between 2020 and 2022. Our first research question
analyzes SCCT constructs to provide detailed insights into the interest
formation of various subfields of physics. Examining these constructs, we
better understand the factors influencing students' preferences toward specific
subfields. Our findings indicate that positive class experiences and
experimental opportunities significantly impacted students' interest in
different subfields of physics. This understanding helped us explore
significant variations in interest formation between astrophysics and
biomedical physics in Research Question 2. By understanding how students decide
about their interests, we can provide valuable insights for physics departments
and career guidance professionals.


## Diffusion
### Generative Image as Action Models
**Authors**: Mohit Shridhar, Yat Long Lo, Stephen James

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07875v1](http://arxiv.org/pdf/2407.07875v1)

**Abstract**: Image-generation diffusion models have been fine-tuned to unlock new
capabilities such as image-editing and novel view synthesis. Can we similarly
unlock image-generation models for visuomotor control? We present GENIMA, a
behavior-cloning agent that fine-tunes Stable Diffusion to 'draw joint-actions'
as targets on RGB images. These images are fed into a controller that maps the
visual targets into a sequence of joint-positions. We study GENIMA on 25
RLBench and 9 real-world manipulation tasks. We find that, by lifting actions
into image-space, internet pre-trained diffusion models can generate policies
that outperform state-of-the-art visuomotor approaches, especially in
robustness to scene perturbations and generalizing to novel objects. Our method
is also competitive with 3D agents, despite lacking priors such as depth,
keypoints, or motion-planners.


### PhenDiff: Revealing Subtle Phenotypes with Diffusion Models in Real Images
**Authors**: Anis Bourou, Thomas Boyer, Kévin Daupin, Véronique Dubreuil, Aurélie De Thonel, Valérie Mezger, Auguste Genovesio

**Published Date**: 2023-12-13

**Updated Date**: 2024-07-10

**PDF Url**: [2312.08290v2](http://arxiv.org/pdf/2312.08290v2)

**Abstract**: For the past few years, deep generative models have increasingly been used in
biological research for a variety of tasks. Recently, they have proven to be
valuable for uncovering subtle cell phenotypic differences that are not
directly discernible to the human eye. However, current methods employed to
achieve this goal mainly rely on Generative Adversarial Networks (GANs). While
effective, GANs encompass issues such as training instability and mode
collapse, and they do not accurately map images back to the model's latent
space, which is necessary to synthesize, manipulate, and thus interpret outputs
based on real images. In this work, we introduce PhenDiff: a multi-class
conditional method leveraging Diffusion Models (DMs) designed to identify
shifts in cellular phenotypes by translating a real image from one condition to
another. We qualitatively and quantitatively validate this method on cases
where the phenotypic changes are visible or invisible, such as in low
concentrations of drug treatments. Overall, PhenDiff represents a valuable tool
for identifying cellular variations in real microscopy images. We anticipate
that it could facilitate the understanding of diseases and advance drug
discovery through the identification of novel biomarkers.


### Going beyond Compositions, DDPMs Can Produce Zero-Shot Interpolations
**Authors**: Justin Deschenaux, Igor Krawczuk, Grigorios Chrysos, Volkan Cevher

**Published Date**: 2024-05-29

**Updated Date**: 2024-07-10

**PDF Url**: [2405.19201v2](http://arxiv.org/pdf/2405.19201v2)

**Abstract**: Denoising Diffusion Probabilistic Models (DDPMs) exhibit remarkable
capabilities in image generation, with studies suggesting that they can
generalize by composing latent factors learned from the training data. In this
work, we go further and study DDPMs trained on strictly separate subsets of the
data distribution with large gaps on the support of the latent factors. We show
that such a model can effectively generate images in the unexplored,
intermediate regions of the distribution. For instance, when trained on clearly
smiling and non-smiling faces, we demonstrate a sampling procedure which can
generate slightly smiling faces without reference images (zero-shot
interpolation). We replicate these findings for other attributes as well as
other datasets. Our code is available at
https://github.com/jdeschena/ddpm-zero-shot-interpolation.


### Promises, Outlooks and Challenges of Diffusion Language Modeling
**Authors**: Justin Deschenaux, Caglar Gulcehre

**Published Date**: 2024-06-17

**Updated Date**: 2024-07-10

**PDF Url**: [2406.11473v2](http://arxiv.org/pdf/2406.11473v2)

**Abstract**: The modern autoregressive Large Language Models (LLMs) have achieved
outstanding performance on NLP benchmarks, and they are deployed in the real
world. However, they still suffer from limitations of the autoregressive
training paradigm. For example, autoregressive token generation is notably slow
and can be prone to \textit{exposure bias}. The diffusion-based language models
were proposed as an alternative to autoregressive generation to address some of
these limitations. We evaluate the recently proposed Score Entropy Discrete
Diffusion (SEDD) approach and show it is a promising alternative to
autoregressive generation but it has some short-comings too. We empirically
demonstrate the advantages and challenges of SEDD, and observe that SEDD
generally matches autoregressive models in perplexity and on benchmarks such as
HellaSwag, Arc or WinoGrande. Additionally, we show that in terms of inference
latency, SEDD can be up to 4.5$\times$ more efficient than GPT-2. While SEDD
allows conditioning on tokens at abitrary positions, SEDD appears slightly
weaker than GPT-2 for conditional generation given short prompts. Finally, we
reproduced the main results from the original SEDD paper.


### Feasibility Study on Active Learning of Smart Surrogates for Scientific Simulations
**Authors**: Pradeep Bajracharya, Javier Quetzalcóatl Toledo-Marín, Geoffrey Fox, Shantenu Jha, Linwei Wang

**Published Date**: 2024-07-10

**Updated Date**: 2024-07-10

**PDF Url**: [2407.07674v1](http://arxiv.org/pdf/2407.07674v1)

**Abstract**: High-performance scientific simulations, important for comprehension of
complex systems, encounter computational challenges especially when exploring
extensive parameter spaces. There has been an increasing interest in developing
deep neural networks (DNNs) as surrogate models capable of accelerating the
simulations. However, existing approaches for training these DNN surrogates
rely on extensive simulation data which are heuristically selected and
generated with expensive computation -- a challenge under-explored in the
literature. In this paper, we investigate the potential of incorporating active
learning into DNN surrogate training. This allows intelligent and objective
selection of training simulations, reducing the need to generate extensive
simulation data as well as the dependency of the performance of DNN surrogates
on pre-defined training simulations. In the problem context of constructing DNN
surrogates for diffusion equations with sources, we examine the efficacy of
diversity- and uncertainty-based strategies for selecting training simulations,
considering two different DNN architecture. The results set the groundwork for
developing the high-performance computing infrastructure for Smart Surrogates
that supports on-the-fly generation of simulation data steered by active
learning strategies to potentially improve the efficiency of scientific
simulations.


