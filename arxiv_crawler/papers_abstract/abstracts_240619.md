# Abstracts of Papers

## Physics
### Neural Approximate Mirror Maps for Constrained Diffusion Models
**Authors**: Berthy T. Feng, Ricardo Baptista, Katherine L. Bouman

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12816v1](http://arxiv.org/pdf/2406.12816v1)

**Abstract**: Diffusion models excel at creating visually-convincing images, but they often
struggle to meet subtle constraints inherent in the training data. Such
constraints could be physics-based (e.g., satisfying a PDE), geometric (e.g.,
respecting symmetry), or semantic (e.g., including a particular number of
objects). When the training data all satisfy a certain constraint, enforcing
this constraint on a diffusion model not only improves its
distribution-matching accuracy but also makes it more reliable for generating
valid synthetic data and solving constrained inverse problems. However,
existing methods for constrained diffusion models are inflexible with different
types of constraints. Recent work proposed to learn mirror diffusion models
(MDMs) in an unconstrained space defined by a mirror map and to impose the
constraint with an inverse mirror map, but analytical mirror maps are
challenging to derive for complex constraints. We propose neural approximate
mirror maps (NAMMs) for general constraints. Our approach only requires a
differentiable distance function from the constraint set. We learn an
approximate mirror map that pushes data into an unconstrained space and a
corresponding approximate inverse that maps data back to the constraint set. A
generative model, such as an MDM, can then be trained in the learned mirror
space and its samples restored to the constraint set by the inverse map. We
validate our approach on a variety of constraints, showing that compared to an
unconstrained diffusion model, a NAMM-based MDM substantially improves
constraint satisfaction. We also demonstrate how existing diffusion-based
inverse-problem solvers can be easily applied in the learned mirror space to
solve constrained inverse problems.


### The $g$-function and Defect Changing Operators from Wavefunction Overlap on a Fuzzy Sphere
**Authors**: Zheng Zhou, Davide Gaiotto, Yin-Chen He, Yijian Zou

**Published Date**: 2023-12-29

**Updated Date**: 2024-06-18

**PDF Url**: [2401.00039v3](http://arxiv.org/pdf/2401.00039v3)

**Abstract**: Defects are common in physical systems with boundaries, impurities or
extensive measurements. The interaction between bulk and defect can lead to
rich physical phenomena. Defects in gapless phases of matter with conformal
symmetry usually flow to a defect conformal field theory (dCFT). Understanding
the universal properties of dCFTs is a challenging task. In this paper, we
propose a computational strategy applicable to a line defect in arbitrary
dimensions. Our main assumption is that the defect has a UV description in
terms of a local modification of the Hamiltonian so that we can compute the
overlap between low-energy eigenstates of a system with or without the defect
insertion. We argue that these overlaps contain a wealth of conformal data,
including the $g$-function, which is an RG monotonic quantity that
distinguishes different dCFTs, the scaling dimensions of defect creation
operators $\Delta^{+0}_\alpha$ and changing operators $\Delta^{+-}_\alpha$ that
live on the intersection of different types of line defects, and various OPE
coefficients. We apply this method to the fuzzy sphere regularization of 3D
CFTs and study the magnetic line defect of the 3D Ising CFT. Using exact
diagonalization and DMRG, we report the non-perturbative results
$g=0.602(2),\Delta^{+0}_0=0.108(5)$ and $\Delta^{+-}_0=0.84(5)$ for the first
time. We also obtain other OPE coefficients and scaling dimensions. Our results
have significant physical implications. For example, they constrain the
possible occurrence of spontaneous symmetry breaking at line defects of the 3D
Ising CFT. Our method can be potentially applied to various other dCFTs, such
as plane defects and Wilson lines in gauge theories.


### Engineering the Kitaev spin liquid in a quantum dot system
**Authors**: Tessa Cookmeyer, Sankar Das Sarma

**Published Date**: 2023-10-27

**Updated Date**: 2024-06-18

**PDF Url**: [2310.18393v3](http://arxiv.org/pdf/2310.18393v3)

**Abstract**: The Kitaev model on a honeycomb lattice may provide a robust topological
quantum memory platform, but finding a material that realizes the unique spin
liquid phase remains a considerable challenge. We demonstrate that an effective
Kitaev Hamiltonian can arise from a half-filled Fermi-Hubbard Hamiltonian where
each site can experience a magnetic field in a different direction. As such, we
provide a method for realizing the Kitaev spin liquid on a single hexagonal
plaquette made up of twelve quantum dots. Despite the small system size, there
are clear signatures of the Kitaev spin-liquid ground state, and there is a
range of parameters where these signatures are predicted, allowing a potential
platform where Kitaev spin-liquid physics can be explored experimentally in
quantum dot plaquettes.


### Latent Intuitive Physics: Learning to Transfer Hidden Physics from A 3D Video
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


### A hybrid reduced-order model for segregated fluid-structure interaction solvers in an ALE approach at high Reynolds number
**Authors**: Valentin Nkana Ngan, Giovanni Stabile, Andrea Mola, Gianluigi Rozza

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12701v1](http://arxiv.org/pdf/2406.12701v1)

**Abstract**: This study introduces a first step for constructing a hybrid reduced-order
models (ROMs) for segregated fluid-structure interaction in an Arbitrary
Lagrangian-Eulerian (ALE) approach at a high Reynolds number using the Finite
Volume Method (FVM). The ROM is driven by proper orthogonal decomposition (POD)
with hybrid techniques that combines the classical Galerkin projection and two
data-driven methods (radial basis networks , and neural networks/ long short
term memory). Results demonstrate the ROM ability to accurately capture the
physics of fluid-structure interaction phenomena. This approach is validated
through a case study focusing on flow-induced vibration (FIV) of a pitch-plunge
airfoil at a high Reynolds number 10000000.


### Exponential Error Reduction for Glueball Calculations Using a Two-Level Algorithm in Pure Gauge Theory
**Authors**: Lorenzo Barca, Francesco Knechtli, Sofie Martins, Michael Peardon, Stefan Schaefer, Juan Andrés Urrea-Niño

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12656v1](http://arxiv.org/pdf/2406.12656v1)

**Abstract**: This study explores the application of a two-level algorithm to enhance the
signal-to-noise ratio of glueball calculations in four-dimensional
$\mathrm{SU(3)}$ pure gauge theory. Our findings demonstrate that the
statistical errors exhibit an exponential reduction, enabling reliable
extraction of effective masses at distances where current standard methods
would demand exponentially more samples. However, at shorter distances,
standard methods prove more efficient due to a saturation of the variance
reduction using the multi-level method. We discuss the physical distance at
which the multi-level sampling is expected to outperform the standard
algorithm, supported by numerical evidence across different lattice spacings
and glueball channels. Additionally, we construct a variational basis
comprising 35 Wilson loops up to length 12 and 5 smearing sizes each,
presenting results for the first state in the spectrum for the scalar,
pseudoscalar, and tensor channels.


### Noncompletely Positive Quantum Maps Enable Efficient Local Energy Extraction in Batteries
**Authors**: Aparajita Bhattacharyya, Kornikar Sen, Ujjwal Sen

**Published Date**: 2023-07-31

**Updated Date**: 2024-06-18

**PDF Url**: [2307.16746v4](http://arxiv.org/pdf/2307.16746v4)

**Abstract**: Energy extraction from quantum batteries by means of completely positive
trace-preserving (CPTP) maps leads to the concept of CPTP-local passive states,
which identify bipartite states from which no energy can be squeezed out by
applying any CPTP map to a particular subsystem. We prove, for arbitrary
dimension, that if a state is CPTP-local passive with respect to a Hamiltonian,
then an arbitrary number of copies of the same state - including an
asymptotically large one - is also CPTP-local passive. We show further that
energy can be extracted efficiently from CPTP-local passive states employing
NCPTP but still physically realizable maps on the same part of the shared
battery on which operation of CPTP maps were useless. Moreover, we provide the
maximum extractable energy using local-CPTP operations, and then, we present an
explicit class of states and corresponding Hamiltonians, for which the maximum
can be outperformed using physical local NCPTP maps. We provide a necessary and
sufficient condition and a separate necessary condition for an arbitrary
bipartite state to be unable to supply any energy using non-completely positive
trace-preserving (NCPTP) operations on one party with respect to an arbitrary
but fixed Hamiltonian. We build an analogy between the relative status of CPTP
and NCPTP operations for energy extraction in quantum batteries, and the
association of distillable entanglement with entanglement cost for asymptotic
local manipulations of entanglement. The surpassing of the maximum energy
extractable by NCPTP maps for CPTP-passive as well as for CPTP non-passive
battery states can act as detectors of non-CPTPness of quantum maps.


### Photoproduction of J/$ψ$ and dileptons in Pb-Pb collisions with nuclear overlap
**Authors**: Nicolas Bizé

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12630v1](http://arxiv.org/pdf/2406.12630v1)

**Abstract**: Photon-photon reactions and the production of J/$\psi$ meson through
photonuclear reactions have been extensively studied in ultra-peripheral
heavy-ion collisions, in which the impact parameter is larger than twice the
nuclear radius. In recent years, coherently photoproduced J/$\psi$ and dilepton
production via photon-photon interactions have also been observed in
nucleus-nucleus (A-A) collisions with nuclear overlap. The former can help to
constrain the nuclear gluon distributions at low Bjorken-$x$ and high energy,
while the latter could be used to further map the electromagnetic fields
produced in heavy-ion collisions. In addition, these measurements can shed
light on the theory behind photon-induced reactions in A-A collisions with
nuclear overlap, including possible interactions of the measured probes with
the formed and fast expanding quark-gluon plasma. Since the produced quarkonium
is expected to keep the polarization of the incoming photon due to $s$-channel
helicity conservation, the photoproduction origin of the J/$\psi$ yield excess
at very low transverse momentum, $p_{\rm T}$, can be confirmed by the
measurement of the J/$\psi$ polarization. The ALICE detector can perform
quarkonium production measurements at both mid ($|y|<0.9$) and forward
($2.5<y<4$) rapidities down to $p_{\rm T} = 0$. In the following, the new ALICE
measurements of the J/$\psi$ $y$-differential cross section and the first
polarization results of coherently photoproduced J/$\psi$ via the dimuon decay
channel at forward rapidity in Pb-Pb collisions at $\sqrt{s_{NN}}=$ 5.02 TeV
are reported. Additionally, the measurement of an excess with respect to
expectations from hadronic production in the dielectron yield, at low mass and
$p_{\rm T}$, at midrapidity in Pb-Pb collisions at $\sqrt{s_{NN}}=$ 5.02~TeV,
is presented. The results are compared with available theoretical models.


### Nonresonant central exclusive production of charged-hadron pairs in proton-proton collisions at $\sqrt{s}$ = 13 TeV
**Authors**: CMS, TOTEM Collaborations

**Published Date**: 2024-01-25

**Updated Date**: 2024-06-18

**PDF Url**: [2401.14494v2](http://arxiv.org/pdf/2401.14494v2)

**Abstract**: The central exclusive production of charged-hadron pairs in pp collisions at
a centre-of-mass energy of 13 TeV is examined, based on data collected in a
special high-$\beta^*$ run of the LHC. The nonresonant continuum processes are
studied with the invariant mass of the centrally produced two-pion system in
the resonance-free region, $m_{\pi^+\pi^-}$ $\lt$ 0.7 GeV or $m_{\pi^+\pi^-}$
$\gt$ 1.8 GeV. Differential cross sections as functions of the azimuthal angle
between the surviving protons, squared exchanged four-momenta, and
$m_{\pi^+\pi^-}$ are measured in a wide region of scattered proton transverse
momenta, between 0.2 and 0.8 GeV, and for pion rapidities $\lvert y\rvert$
$\lt$ 2. A rich structure of interactions related to double-pomeron exchange is
observed. A parabolic minimum in the distribution of the two-proton azimuthal
angle is observed for the first time. It can be interpreted as an effect of
additional pomeron exchanges between the protons from the interference between
the bare and the rescattered amplitudes. After model tuning, various physical
quantities are determined that are related to the pomeron cross section,
proton-pomeron and meson-pomeron form factors, pomeron trajectory and
intercept, and coefficients of diffractive eigenstates of the proton.


### Second gadolinium loading to Super-Kamiokande
**Authors**: K. Abe, C. Bronner, Y. Hayato, K. Hiraide, K. Hosokawa, K. Ieki, M. Ikeda, J. Kameda, Y. Kanemura, R. Kaneshima, Y. Kashiwagi, Y. Kataoka, S. Miki, S. Mine, M. Miura, S. Moriyama, Y. Nakano, M. Nakahata, S. Nakayama, Y. Noguchi, K. Sato, H. Sekiya, H. Shiba, K. Shimizu, M. Shiozawa, Y. Sonoda, Y. Suzuki, A. Takeda, Y. Takemoto, H. Tanaka, T. Yano, S. Han, T. Kajita, K. Okumura, T. Tashiro, T. Tomiya, X. Wang, S. Yoshida, P. Fernandez, L. Labarga, N. Ospina, B. Zaldivar, B. W. Pointon, E. Kearns, J. L. Raaf, L. Wan, T. Wester, J. Bian, N. J. Griskevich, M. B. Smy, H. W. Sobel, V. Takhistov, A. Yankelevich, J. Hill, M. C. Jang, S. H. Lee, D. H. Moon, R. G. Park, B. Bodur, K. Scholberg, C. W. Walter, A. Beauchene, O. Drapier, A. Giampaolo, Th. A. Mueller, A. D. Santos, P. Paganini, B. Quilain, R. Rogly, T. Nakamura, J. S. Jang, L. N. Machado, J. G. Learned, K. Choi, N. Iovine, S. Cao, L. H. V. Anthony, D. Martin, N. W. Prouse, M. Scott, Y. Uchida, V. Berardi, N. F. Calabria, M. G. Catanesi, E. Radicioni, A. Langella, G. De Rosa, G. Collazuol, F. Iacob, M. Mattiazzi, L. Ludovici, M. Gonin, L. Perisse, G. Pronost, C. Fujisawa, Y. Maekawa, Y. Nishimura, R. Okazaki, R. Akutsu, M. Friend, T. Hasegawa, T. Ishida, T. Kobayashi, M. Jakkapu, T. Matsubara, T. Nakadaira, K. Nakamura, Y. Oyama, K. Sakashita, T. Sekiguchi, T. Tsukamoto, N. Bhuiyan, G. T. Burton, F. Di Lodovico, J. Gao, A. Goldsack, T. Katori, J. Migenda, R. M. Ramsden, Z. Xie, S. Zsoldos, A. T. Suzuki, Y. Takagi, Y. Takeuchi, H. Zhong, J. Feng, L. Feng, J. R. Hu, Z. Hu, M. Kawaue, T. Kikawa, M. Mori, T. Nakaya, R. A. Wendell, K. Yasutome, S. J. Jenkins, N. McCauley, P. Mehta, A. Tarant, M. J. Wilking, Y. Fukuda, Y. Itow, H. Menjo, K. Ninomiya, Y. Yoshioka, J. Lagoda, M. Mandal, P. Mijakowski, Y. S. Prabhu, J. Zalipska, M. Jia, J. Jiang, W. Shi, C. Yanagisawa, M. Harada, Y. Hino, H. Ishino, Y. Koshio, F. Nakanishi, S. Sakai, T. Tada, T. Tano, T. Ishizuka, G. Barr, D. Barrow, L. Cook, S. Samani, D. Wark, A. Holin, F. Nova, S. Jung, B. S. Yang, J. Y. Yang, J. Yoo, J. E. P. Fannon, L. Kneale, M. Malek, J. M. McElwee, M. D. Thiesse, L. F. Thompson, S. T. Wilson, H. Okazawa, S. M. Lakshmi, S. B. Kim, E. Kwon, J. W. Seo, I. Yu, A. K. Ichikawa, K. Nakamura, S. Tairafune, K. Nishijima, A. Eguchi, K. Nakagiri, Y. Nakajima, S. Shima, N. Taniuchi, E. Watanabe, M. Yokoyama, P. de Perio, S. Fujita, C. Jesus-Valls, K. Martens, K. M. Tsui, M. R. Vagins, J. Xia, S. Izumiyama, M. Kuze, R. Matsumoto, K. Terada, M. Ishitsuka, H. Ito, Y. Ommura, N. Shigeta, M. Shinoki, K. Yamauchi, T. Yoshida, R. Gaur, V. Gousy-Leblanc, M. Hartz, A. Konaka, X. Li, S. Chen, B. D. Xu, B. Zhang, M. Posiadala-Zezula, S. B. Boyd, R. Edwards, D. Hadley, M. Nicholson, M. O'Flaherty, B. Richards, A. Ali, B. Jamieson, S. Amanai, Ll. Marti, A. Minamino, S. Suzuki, P. R. Scovell, E. Meehan, I. Bandac, C. Pena-Garay, J. Perez, O. Gileva, E. K. Lee, D. S. Leonard, Y. Sakakieda, A. Sakaguchi, K. Sueki, Y. Takaku, S. Yamasaki

**Published Date**: 2024-03-12

**Updated Date**: 2024-06-18

**PDF Url**: [2403.07796v3](http://arxiv.org/pdf/2403.07796v3)

**Abstract**: The first loading of gadolinium (Gd) into Super-Kamiokande in 2020 was
successful, and the neutron capture efficiency on Gd reached 50\%. To further
increase the Gd neutron capture efficiency to 75\%, 26.1 tons of $\rm Gd_2(\rm
SO_4)_3\cdot \rm 8H_2O$ was additionally loaded into Super-Kamiokande (SK) from
May 31 to July 4, 2022. As the amount of loaded $\rm Gd_2(\rm SO_4)_3\cdot \rm
8H_2O$ was doubled compared to the first loading, the capacity of the powder
dissolving system was doubled. We also developed new batches of gadolinium
sulfate with even further reduced radioactive impurities. In addition, a more
efficient screening method was devised and implemented to evaluate these new
batches of $\rm Gd_2(\rm SO_4)_3\cdot \rm 8H_2O$. Following the second loading,
the Gd concentration in SK was measured to be $333.5\pm2.5$ ppm via an Atomic
Absorption Spectrometer (AAS). From the mean neutron capture time constant of
neutrons from an Am/Be calibration source, the Gd concentration was
independently measured to be 332.7 $\pm$ 6.8(sys.) $\pm$ 1.1(stat.) ppm,
consistent with the AAS result. Furthermore, during the loading the Gd
concentration was monitored continually using the capture time constant of each
spallation neutron produced by cosmic-ray muons,and the final neutron capture
efficiency was shown to become 1.5 times higher than that of the first loaded
phase, as expected.


## Diffusion
### Evaluating the design space of diffusion-based generative models
**Authors**: Yuqing Wang, Ye He, Molei Tao

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12839v1](http://arxiv.org/pdf/2406.12839v1)

**Abstract**: Most existing theoretical investigations of the accuracy of diffusion models,
albeit significant, assume the score function has been approximated to a
certain accuracy, and then use this a priori bound to control the error of
generation. This article instead provides a first quantitative understanding of
the whole generation process, i.e., both training and sampling. More precisely,
it conducts a non-asymptotic convergence analysis of denoising score matching
under gradient descent. In addition, a refined sampling error analysis for
variance exploding models is also provided. The combination of these two
results yields a full error analysis, which elucidates (again, but this time
theoretically) how to design the training and sampling processes for effective
generation. For instance, our theory implies a preference toward noise
distribution and loss weighting that qualitatively agree with the ones used in
[Karras et al. 2022]. It also provides some perspectives on why the time and
variance schedule used in [Karras et al. 2022] could be better tuned than the
pioneering version in [Song et al. 2020].


### Influence Maximization via Graph Neural Bandits
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


### Extracting Training Data from Unconditional Diffusion Models
**Authors**: Yunhao Chen, Xingjun Ma, Difan Zou, Yu-Gang Jiang

**Published Date**: 2024-06-18

**Updated Date**: 2024-06-18

**PDF Url**: [2406.12752v1](http://arxiv.org/pdf/2406.12752v1)

**Abstract**: As diffusion probabilistic models (DPMs) are being employed as mainstream
models for generative artificial intelligence (AI), the study of their
memorization of the raw training data has attracted growing attention. Existing
works in this direction aim to establish an understanding of whether or to what
extent DPMs learn by memorization. Such an understanding is crucial for
identifying potential risks of data leakage and copyright infringement in
diffusion models and, more importantly, for more controllable generation and
trustworthy application of Artificial Intelligence Generated Content (AIGC).
While previous works have made important observations of when DPMs are prone to
memorization, these findings are mostly empirical, and the developed data
extraction methods only work for conditional diffusion models. In this work, we
aim to establish a theoretical understanding of memorization in DPMs with 1) a
memorization metric for theoretical analysis, 2) an analysis of conditional
memorization with informative and random labels, and 3) two better evaluation
metrics for measuring memorization. Based on the theoretical analysis, we
further propose a novel data extraction method called \textbf{Surrogate
condItional Data Extraction (SIDE)} that leverages a classifier trained on
generated data as a surrogate condition to extract training data directly from
unconditional diffusion models. Our empirical results demonstrate that SIDE can
extract training data from diffusion models where previous methods fail, and it
is on average over 50\% more effective across different scales of the CelebA
dataset.


### To smooth a cloud or to pin it down: Guarantees and Insights on Score Matching in Denoising Diffusion Models
**Authors**: Francisco Vargas, Teodora Reu, Anna Kerekes

**Published Date**: 2023-05-16

**Updated Date**: 2024-06-18

**PDF Url**: [2305.09605v2](http://arxiv.org/pdf/2305.09605v2)

**Abstract**: Denoising diffusion models are a class of generative models which have
recently achieved state-of-the-art results across many domains. Gradual noise
is added to the data using a diffusion process, which transforms the data
distribution into a Gaussian. Samples from the generative model are then
obtained by simulating an approximation of the time reversal of this diffusion
initialized by Gaussian samples. Recent research has explored adapting
diffusion models for sampling and inference tasks. In this paper, we leverage
known connections to stochastic control akin to the F\"ollmer drift to extend
established neural network approximation results for the F\"ollmer drift to
denoising diffusion models and samplers.


### Sparsifying dimensionality reduction of PDE solution data with Bregman learning
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


## Quantitative Finance
### Self-Specialization: Uncovering Latent Expertise within Large Language Models
**Authors**: Junmo Kang, Hongyin Luo, Yada Zhu, Jacob Hansen, James Glass, David Cox, Alan Ritter, Rogerio Feris, Leonid Karlinsky

**Published Date**: 2023-09-29

**Updated Date**: 2024-06-05

**PDF Url**: [2310.00160v2](http://arxiv.org/pdf/2310.00160v2)

**Abstract**: Recent works have demonstrated the effectiveness of self-alignment in which a
large language model is aligned to follow general instructions using
instructional data generated from the model itself starting from a handful of
human-written seeds. Instead of general alignment, in this work, we focus on
self-alignment for expert domain specialization (e.g., biomedicine, finance).
As a preliminary, we quantitively show the marginal effect that generic
instruction-following training has on downstream expert domains' performance.
To remedy this, we propose self-specialization - allowing for effective model
specialization while achieving cross-task generalization by leveraging only a
few labeled seeds. Self-specialization offers a data- and parameter-efficient
way of "carving out" an expert model out of a generalist pre-trained LLM.
Exploring a variety of popular open large models as a base for specialization,
our experimental results in both biomedical and financial domains show that our
self-specialized models outperform their base models by a large margin, and
even larger models that are generally instruction-tuned or that have been
adapted to the target domain by other means.


### Limit Order Book Dynamics and Order Size Modelling Using Compound Hawkes Process
**Authors**: Konark Jain, Nick Firoozye, Jonathan Kochems, Philip Treleaven

**Published Date**: 2023-12-14

**Updated Date**: 2024-05-07

**PDF Url**: [2312.08927v4](http://arxiv.org/pdf/2312.08927v4)

**Abstract**: Hawkes Process has been used to model Limit Order Book (LOB) dynamics in
several ways in the literature however the focus has been limited to capturing
the inter-event times while the order size is usually assumed to be constant.
We propose a novel methodology of using Compound Hawkes Process for the LOB
where each event has an order size sampled from a calibrated distribution. The
process is formulated in a novel way such that the spread of the process always
remains positive. Further, we condition the model parameters on time of day to
support empirical observations. We make use of an enhanced non-parametric
method to calibrate the Hawkes kernels and allow for inhibitory
cross-excitation kernels. We showcase the results and quality of fits for an
equity stock's LOB in the NASDAQ exchange and compare them against several
baselines. Finally, we conduct a market impact study of the simulator and show
the empirical observation of a concave market impact function is indeed
replicated.


### Fourier Neural Network Approximation of Transition Densities in Finance
**Authors**: Rong Du, Duy-Minh Dang

**Published Date**: 2023-09-07

**Updated Date**: 2024-05-05

**PDF Url**: [2309.03966v2](http://arxiv.org/pdf/2309.03966v2)

**Abstract**: This paper introduces FourNet, a novel single-layer feed-forward neural
network (FFNN) method designed to approximate transition densities for which
closed-form expressions of their Fourier transforms, i.e. characteristic
functions, are available. A unique feature of FourNet lies in its use of a
Gaussian activation function, enabling exact Fourier and inverse Fourier
transformations and drawing analogies with the Gaussian mixture model. We
mathematically establish FourNet's capacity to approximate transition densities
in the $L_2$-sense arbitrarily well with finite number of neurons. The
parameters of FourNet are learned by minimizing a loss function derived from
the known characteristic function and the Fourier transform of the FFNN,
complemented by a strategic sampling approach to enhance training. We derive
practical bounds for the $L_2$ estimation error and the potential pointwise
loss of nonnegativity in FourNet, highlighting its robustness and applicability
in practical settings. FourNet's accuracy and versatility are demonstrated
through a wide range of dynamics common in quantitative finance, including
L\'{e}vy processes and the Heston stochastic volatility models-including those
augmented with the self-exciting Queue-Hawkes jump process.


### Fairness of ChatGPT
**Authors**: Yunqi Li, Lanjing Zhang, Yongfeng Zhang

**Published Date**: 2023-05-22

**Updated Date**: 2024-05-05

**PDF Url**: [2305.18569v2](http://arxiv.org/pdf/2305.18569v2)

**Abstract**: Understanding and addressing unfairness in LLMs are crucial for responsible
AI deployment. However, there is a limited number of quantitative analyses and
in-depth studies regarding fairness evaluations in LLMs, especially when
applying LLMs to high-stakes fields. This work aims to fill this gap by
providing a systematic evaluation of the effectiveness and fairness of LLMs
using ChatGPT as a study case. We focus on assessing ChatGPT's performance in
high-takes fields including education, criminology, finance and healthcare. To
conduct a thorough evaluation, we consider both group fairness and individual
fairness metrics. We also observe the disparities in ChatGPT's outputs under a
set of biased or unbiased prompts. This work contributes to a deeper
understanding of LLMs' fairness performance, facilitates bias mitigation and
fosters the development of responsible AI systems.


### Modelling Opaque Bilateral Market Dynamics in Financial Trading: Insights from a Multi-Agent Simulation Study
**Authors**: Alicia Vidler, Toby Walsh

**Published Date**: 2024-05-05

**Updated Date**: 2024-05-05

**PDF Url**: [2405.02849v1](http://arxiv.org/pdf/2405.02849v1)

**Abstract**: Exploring complex adaptive financial trading environments through multi-agent
based simulation methods presents an innovative approach within the realm of
quantitative finance. Despite the dominance of multi-agent reinforcement
learning approaches in financial markets with observable data, there exists a
set of systematically significant financial markets that pose challenges due to
their partial or obscured data availability. We, therefore, devise a
multi-agent simulation approach employing small-scale meta-heuristic methods.
This approach aims to represent the opaque bilateral market for Australian
government bond trading, capturing the bilateral nature of bank-to-bank
trading, also referred to as "over-the-counter" (OTC) trading, and commonly
occurring between "market makers". The uniqueness of the bilateral market,
characterized by negotiated transactions and a limited number of agents, yields
valuable insights for agent-based modelling and quantitative finance. The
inherent rigidity of this market structure, which is at odds with the global
proliferation of multilateral platforms and the decentralization of finance,
underscores the unique insights offered by our agent-based model. We explore
the implications of market rigidity on market structure and consider the
element of stability, in market design. This extends the ongoing discourse on
complex financial trading environments, providing an enhanced understanding of
their dynamics and implications.


