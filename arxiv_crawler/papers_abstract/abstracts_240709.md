# Abstracts of Papers

## Physics
### Polarized and unpolarized off-shell $H^\ast\to ZZ\rightarrow 4\ell$ decay above the $2m_Z$ threshold
**Authors**: A. I. Hernández-Juárez, R. Gaitán, G. Tavares-Velasco

**Published Date**: 2024-02-28

**Updated Date**: 2024-07-08

**PDF Url**: [2402.18497v2](http://arxiv.org/pdf/2402.18497v2)

**Abstract**: An analysis of the off-shell $H^\ast\rightarrow ZZ \rightarrow
\overline{\ell}_1\ell_1\overline{\ell}_2\ell_2$ decay width is presented for
both unpolarized and polarized $Z$ gauge bosons in the scenario with the most
general $H^*ZZ$ vertex function, which is given in terms of two $CP$-even
($\hat b_Z$ and $\hat c_Z$) and one $CP$-odd ($\tilde b_Z$) anomalous
couplings.
  The SM contributions to the $H^*ZZ$ coupling up to the one-loop level are
also included. Explicit analytic results for the unpolarized and polarized
$H^\ast\rightarrow ZZ \rightarrow
\overline{\ell}_1\ell_1\overline{\ell}_2\ell_2$ square amplitudes and the
four-body phase space are presented, out of which several observable quantities
can be obtained straightforwardly. As far as the numerical analysis is
concerned, a cross-check is performed via \texttt{MadGraph5\_aMC@NLO}, where
our model was implemented with the aid of FeynRules. We then consider the most
stringent bounds on anomalous complex $H^*ZZ$ couplings and analyze the effects
of the polarizations of the $Z$ gauge bosons through the polarized
$H^\ast\rightarrow ZZ \rightarrow
\overline{\ell}_1\ell_1\overline{\ell}_2\ell_2$ decay width as well as
left-right and forward-backward asymmetries, which are found to be sensitive to
new-physics effects. Particular focus is put on the effects of the absorptive
parts of the anomalous $H^*ZZ$ couplings, which have been largely overlooked up
to now in LHC analyses. It is found that the studied observable quantities,
particularly the left-right asymmetries, can be helpful to look for effects of
$CP$-violation in the $H^*ZZ$ coupling and set bounds on the absorptive parts.
For completeness, we also analyze the case of unpolarized $Z$ gauge bosons.


### Cellular-resolution X-ray microtomography of an entire mouse brain
**Authors**: Mattia Humbel, Christine Tanner, Marta Girona Alarcón, Georg Schulz, Timm Weitkamp, Mario Scheel, Vartan Kurtcuoglu, Bert Müller, Griffin Rodgers

**Published Date**: 2024-05-22

**Updated Date**: 2024-07-08

**PDF Url**: [2405.13971v2](http://arxiv.org/pdf/2405.13971v2)

**Abstract**: Purpose: Histology is the gold standard for sub-cellular visualization of the
mouse brain. It offers excellent in-plane resolution, but a comparably low
out-of-plane resolution due to physical sectioning. X-ray microtomography does
not require this trade-off. Tomographic imaging of the entire mouse brain with
isotropic cellular resolution produces datasets of multiple terabytes in size.
These data must be processed and made accessible to domain experts who may have
only limited image processing knowledge.
  Approach: Extended-field X-ray microtomography covering an entire mouse brain
was performed. The 4,495 projections from 8 $\times$ 8 offset acquisitions were
stitched to reconstruct a volume of 15,000$^3$ voxels. The microtomography
volume was non-rigidly registered to the Allen Mouse Brain Common Coordinate
Framework v3 based on a combination of image intensity and landmark pairs.
  Results: We present a 3.3 teravoxel dataset covering a full mouse brain with
0.65 $\mu$m voxel size. The data were blockwise transformed to a common
coordinate system, then stored in a public repository with a hierarchical
format for navigation and overlay with anatomical annotations in online viewers
such as Neuroglancer or siibra-explorer.
  Conclusions: This study demonstrates X-ray imaging and data processing for a
full mouse brain, augmenting current atlases by improving resolution in the
third dimension by an order of magnitude. The data are publicly available and
easily accessible for domain experts via browser-based viewers.


### A Hidden Convexity of Nonlinear Elasticity
**Authors**: Siddharth Singh, Janusz Ginster, Amit Acharya

**Published Date**: 2024-01-16

**Updated Date**: 2024-07-08

**PDF Url**: [2401.08538v2](http://arxiv.org/pdf/2401.08538v2)

**Abstract**: A technique for developing convex dual variational principles for the
governing PDE of nonlinear elastostatics and elastodynamics is presented. This
allows the definition of notions of a variational dual solution and a dual
solution corresponding to the PDEs of nonlinear elasticity, even when the
latter arise as formal Euler-Lagrange equations corresponding to
non-quasiconvex elastic energy functionals whose energy minimizers do not
exist. This is demonstrated rigorously in the case of elastostatics for the
Saint-Venant Kirchhoff material (in all dimensions), where the existence of
variational dual solutions is also proven. The existence of a variational dual
solution for the incompressible neo-Hookean material in 2-d is also shown.
Stressed and unstressed elastostatic and elastodynamic solutions in 1 space
dimension corresponding to a non-convex, double-well energy are computed using
the dual methodology. In particular, we show the stability of a dual
elastodynamic equilibrium solution for which there are regions of non-vanishing
length with negative elastic stiffness, i.e.~non-hyperbolic regions, for which
the corresponding primal problem is ill-posed and demonstrates an explosive
`Hadamard instability;' this appears to have implications for the modeling of
physically observed softening behavior in macroscopic mechanical response.


### Accelerating Phase Field Simulations Through a Hybrid Adaptive Fourier Neural Operator with U-Net Backbone
**Authors**: Christophe Bonneville, Nathan Bieberdorf, Arun Hegde, Mark Asta, Habib N. Najm, Laurent Capolungo, Cosmin Safta

**Published Date**: 2024-06-24

**Updated Date**: 2024-07-08

**PDF Url**: [2406.17119v2](http://arxiv.org/pdf/2406.17119v2)

**Abstract**: Prolonged contact between a corrosive liquid and metal alloys can cause
progressive dealloying. For such liquid-metal dealloying (LMD) process, phase
field models have been developed. However, the governing equations often
involve coupled non-linear partial differential equations (PDE), which are
challenging to solve numerically. In particular, stiffness in the PDEs requires
an extremely small time steps (e.g. $10^{-12}$ or smaller). This computational
bottleneck is especially problematic when running LMD simulation until a late
time horizon is required. This motivates the development of surrogate models
capable of leaping forward in time, by skipping several consecutive time steps
at-once. In this paper, we propose U-Shaped Adaptive Fourier Neural Operators
(U-AFNO), a machine learning (ML) model inspired by recent advances in neural
operator learning. U-AFNO employs U-Nets for extracting and reconstructing
local features within the physical fields, and passes the latent space through
a vision transformer (ViT) implemented in the Fourier space (AFNO). We use
U-AFNOs to learn the dynamics mapping the field at a current time step into a
later time step. We also identify global quantities of interest (QoI)
describing the corrosion process (e.g. the deformation of the liquid-metal
interface) and show that our proposed U-AFNO model is able to accurately
predict the field dynamics, in-spite of the chaotic nature of LMD. Our model
reproduces the key micro-structure statistics and QoIs with a level of accuracy
on-par with the high-fidelity numerical solver. We also investigate the
opportunity of using hybrid simulations, in which we alternate forward leap in
time using the U-AFNO with high-fidelity time stepping. We demonstrate that
while advantageous for some surrogate model design choices, our proposed U-AFNO
model in fully auto-regressive settings consistently outperforms hybrid
schemes.


### Prevalence of a growth mindset among introductory astronomy students
**Authors**: Moire K. M. Prescott, Laura Madson, Sandra M. Way, Kelly N. Sanderson

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06147v1](http://arxiv.org/pdf/2407.06147v1)

**Abstract**: While many previous studies have indicated that encouraging a growth mindset
can improve student learning outcomes, this conclusion's applicability to
college-level astronomy classrooms remains poorly understood owing to the
variation in students' overall and domain-specific learning attitudes. To
address this, we surveyed undergraduate students in an introductory astronomy
class about their attitudes towards learning astronomy over the course of five
semesters. Overall, students felt an affinity for astronomy, felt moderately
competent, perceived astronomy to be intermediate in terms of difficulty, and
agreed strongly with standard statements reflecting a "growth mindset," i.e.,
the belief that intelligence is malleable rather than fixed from birth. Their
responses were stable over the course of the semester and did not appear to
depend strongly on student demographics. The unexpected start of the COVID-19
pandemic and the associated shift to all-virtual learning correlated with a
drop in their affinity for astronomy, a small decrease in their perceived
competence, and an increase in the perceived difficulty of the topic. Their
overall learning mindset showed negligible change during this time, emphasizing
the stability of their belief in a growth mindset as compared to other measured
learning attitudes. However, more nuanced questions about their behaviors and
interpretations in the classroom, about how they felt "in the moment", and
about what factors were most important for their success in the class revealed
significantly lower alignment with a growth mindset. This suggests that while
introductory astronomy students may believe that they have a growth mindset,
this mindset is not necessarily reflected in their self-reported classroom
behaviors or measured responses to actual learning challenges.


### Constraining $|V_{cs}|$ and physics beyond the Standard Model from exclusive (semi)leptonic charm decays
**Authors**: Carolina Bolognani, Méril Reboud, Danny van Dyk, K. Keri Vos

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06145v1](http://arxiv.org/pdf/2407.06145v1)

**Abstract**: We study the available data on exclusive leptonic and semileptonic $c\to
s\ell^+\nu$ decays within the Standard Model and beyond. Our analysis accounts
for theory correlations between the relevant hadronic matrix elements through
application of dispersive bounds. We find that, within a global analysis, the
dispersive bounds are generally well respected and only mildly affect the
extraction of the Cabibbo-Kobayashi-Maskawa (CKM) matrix element $|V_{cs}|$.
Assuming Standard Model dynamics, we obtain $$
  |V_{cs}| = 0.957 \pm 0.003\,, $$ which is compatible with the HFLAV/PDG
reference value $|V_{cs}| = 0.975 \pm 0.006$ at the $2.7\,\sigma$ level. Our
findings lead to significant deficits in the second-row and second-column
unitarity relations of the CKM matrix. Allowing for beyond the SM contributions
in the Weak Effective Theory, we find very strong constraints on potential
(pseudo)scalar and tensor effects. However, the data still permits sizeable
CP-violating right-handed currents.


### Loewner traces driven by Levy processes
**Authors**: Eveliina Peltola, Anne Schreuder

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06144v1](http://arxiv.org/pdf/2407.06144v1)

**Abstract**: Loewner chains with Levy drivers have been proposed in the physics literature
as models related to random dendritic growth in off-critical systems (and even
for diffusion-limited aggregation), and in mathematics as candidates for
finding extremal multifractal spectra (towards Brennan's conjecture and related
problems in classical function theory). These processes are not scale-invariant
in general, but they do enjoy a natural domain Markov property thanks to the
stationary independent increments of Levy processes. The associated Loewner
hulls feature remarkably intricate topological properties and possibly
complicated multifractal phenomena, of which very little is known rigorously.
  We prove that a chordal Loewner chain driven by a Levy process $W$ satisfying
mild regularity conditions (including stable processes) is a.s. generated by a
cadlag curve. Specifically, if the diffusivity parameter of the driving process
$W$ is $\kappa \in [0,8)$, then the jump measure of $W$ is required to be
locally (upper) Ahlfors regular near the origin, while if $\kappa > 8$, no
constraints are imposed. In particular, we show that the associated Loewner
hulls are a.s. locally connected and path-connected. We also show that, the
complements of the hulls are a.s. Holder domains when $\kappa \neq 4$ (which is
not expected to hold when $\kappa=4$), without any regularity assumptions. The
proofs of these results mainly rely on careful derivative estimates for both
the forward and backward Loewner maps obtained using delicate but robust enough
supermartingale domination arguments. As one cannot control the jump
accumulation of general Levy processes, we must circumvent all reasoning that
would use continuity. To prove the local connectedness, we use an extension of
part of the Hahn-Mazurkiewicz theorem: hulls generated by cadlag curves are
locally connected even when jumps would occur at infinite intensity.


### Physics-informed machine learning approaches to reactor antineutrino detection
**Authors**: Sophia Farrell, Marc Bergevin, Adam Bernstein

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06139v1](http://arxiv.org/pdf/2407.06139v1)

**Abstract**: Nuclear reactors produce a high flux of MeV-scale antineutrinos that can be
observed through inverse beta-decay (IBD) interactions in particle detectors.
Reliable detection of reactor IBD signals depends on suppression of
backgrounds, both by physical shielding and vetoing and by pattern recognition
and rejection in acquired data. A particularly challenging background to
reactor antineutrino detection is from cosmogenically induced fast neutrons,
which can mimic the characteristics of an IBD signal. In this work, we explore
two methods of machine learning -- a tree-based classifier and a
graph-convolutional neural network -- to improve rejection of fast
neutron-induced background events in a water Cherenkov detector. The tree-based
classifier examines classification at the reconstructed feature level, while
the graphical network classifies events using only the raw signal data. Both
methods improve the sensitivity for a background-dominant search over
traditional cut-and-count methods, with the greatest improvement being from the
tree-based classification method. These performance enhancements are relevant
for reactor monitoring applications that make use of deep underground oil-based
or water-based kiloton-scale detectors with multichannel, PMT-based readouts,
and they are likely extensible to other similar physics analyses using this
class of detector.


### Depression Detection and Analysis using Large Language Models on Textual and Audio-Visual Modalities
**Authors**: Avinash Anand, Chayan Tank, Sarthak Pol, Vinayak Katoch, Shaina Mehta, Rajiv Ratn Shah

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06125v1](http://arxiv.org/pdf/2407.06125v1)

**Abstract**: Depression has proven to be a significant public health issue, profoundly
affecting the psychological well-being of individuals. If it remains
undiagnosed, depression can lead to severe health issues, which can manifest
physically and even lead to suicide. Generally, Diagnosing depression or any
other mental disorder involves conducting semi-structured interviews alongside
supplementary questionnaires, including variants of the Patient Health
Questionnaire (PHQ) by Clinicians and mental health professionals. This
approach places significant reliance on the experience and judgment of trained
physicians, making the diagnosis susceptible to personal biases. Given that the
underlying mechanisms causing depression are still being actively researched,
physicians often face challenges in diagnosing and treating the condition,
particularly in its early stages of clinical presentation. Recently,
significant strides have been made in Artificial neural computing to solve
problems involving text, image, and speech in various domains. Our analysis has
aimed to leverage these state-of-the-art (SOTA) models in our experiments to
achieve optimal outcomes leveraging multiple modalities. The experiments were
performed on the Extended Distress Analysis Interview Corpus Wizard of Oz
dataset (E-DAIC) corpus presented in the Audio/Visual Emotion Challenge (AVEC)
2019 Challenge. The proposed solutions demonstrate better results achieved by
Proprietary and Open-source Large Language Models (LLMs), which achieved a Root
Mean Square Error (RMSE) score of 3.98 on Textual Modality, beating the AVEC
2019 challenge baseline results and current SOTA regression analysis
architectures. Additionally, the proposed solution achieved an accuracy of
71.43% in the classification task. The paper also includes a novel audio-visual
multi-modal network that predicts PHQ-8 scores with an RMSE of 6.51.


### Leveraging data-driven weather models for improving numerical weather prediction skill through large-scale spectral nudging
**Authors**: Syed Zahid Husain, Leo Separovic, Jean-François Caron, Rabah Aider, Mark Buehner, Stéphane Chamberland, Ervig Lapalme, Ron McTaggart-Cowan, Christopher Subich, Paul Vaillancourt, Jing Yang, Ayrton Zadra

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06100v1](http://arxiv.org/pdf/2407.06100v1)

**Abstract**: Operational meteorological forecasting has long relied on physics-based
numerical weather prediction (NWP) models. Recently, this landscape has been
disrupted by the advent of data-driven artificial intelligence (AI)-based
weather models, which offer tremendous computational performance and
competitive forecasting skill. However, data-driven models for medium-range
forecasting generally suffer from major limitations, including low effective
resolution and a narrow range of predicted variables. This study illustrates
the relative strengths and weaknesses of these competing paradigms using the
GEM (Global Environmental Multiscale) and GraphCast models to represent
physics-based and AI-based approaches, respectively. By analyzing global
predictions from these two models against observations and analyses in both
physical and spectral spaces, this study demonstrates that GraphCast-predicted
large scales outperform GEM, particularly for longer lead times. Building on
this insight, a hybrid NWP-AI system is proposed, wherein GEM-predicted
large-scale state variables are spectrally nudged toward GraphCast predictions,
while allowing GEM to freely generate fine-scale details critical for weather
extremes. Results indicate that this hybrid approach is capable of leveraging
the strengths of GraphCast to enhance the prediction skill of the GEM model.
Importantly, trajectories of tropical cyclones are predicted with enhanced
accuracy without significant changes in intensity. Furthermore, this new hybrid
system ensures that meteorologists have access to a complete set of forecast
variables, including those relevant for high-impact weather events.


## Diffusion
### Potential Based Diffusion Motion Planning
**Authors**: Yunhao Luo, Chen Sun, Joshua B. Tenenbaum, Yilun Du

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06169v1](http://arxiv.org/pdf/2407.06169v1)

**Abstract**: Effective motion planning in high dimensional spaces is a long-standing open
problem in robotics. One class of traditional motion planning algorithms
corresponds to potential-based motion planning. An advantage of potential based
motion planning is composability -- different motion constraints can be easily
combined by adding corresponding potentials. However, constructing motion paths
from potentials requires solving a global optimization across configuration
space potential landscape, which is often prone to local minima. We propose a
new approach towards learning potential based motion planning, where we train a
neural network to capture and learn an easily optimizable potentials over
motion planning trajectories. We illustrate the effectiveness of such approach,
significantly outperforming both classical and recent learned motion planning
approaches and avoiding issues with local minima. We further illustrate its
inherent composability, enabling us to generalize to a multitude of different
motion constraints.


### ANOLE: An Open, Autoregressive, Native Large Multimodal Models for Interleaved Image-Text Generation
**Authors**: Ethan Chern, Jiadi Su, Yan Ma, Pengfei Liu

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06135v1](http://arxiv.org/pdf/2407.06135v1)

**Abstract**: Previous open-source large multimodal models (LMMs) have faced several
limitations: (1) they often lack native integration, requiring adapters to
align visual representations with pre-trained large language models (LLMs); (2)
many are restricted to single-modal generation; (3) while some support
multimodal generation, they rely on separate diffusion models for visual
modeling and generation. To mitigate these limitations, we present Anole, an
open, autoregressive, native large multimodal model for interleaved image-text
generation. We build Anole from Meta AI's Chameleon, adopting an innovative
fine-tuning strategy that is both data-efficient and parameter-efficient. Anole
demonstrates high-quality, coherent multimodal generation capabilities. We have
open-sourced our model, training framework, and instruction tuning data.


### Structured Generations: Using Hierarchical Clusters to guide Diffusion Models
**Authors**: Jorge da Silva Goncalves, Laura Manduchi, Moritz Vandenhirtz, Julia Vogt

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06124v1](http://arxiv.org/pdf/2407.06124v1)

**Abstract**: This paper introduces Diffuse-TreeVAE, a deep generative model that
integrates hierarchical clustering into the framework of Denoising Diffusion
Probabilistic Models (DDPMs). The proposed approach generates new images by
sampling from a root embedding of a learned latent tree VAE-based structure, it
then propagates through hierarchical paths, and utilizes a second-stage DDPM to
refine and generate distinct, high-quality images for each data cluster. The
result is a model that not only improves image clarity but also ensures that
the generated samples are representative of their respective clusters,
addressing the limitations of previous VAE-based methods and advancing the
state of clustering-based generative modeling.


### Layered Diffusion Model for One-Shot High Resolution Text-to-Image Synthesis
**Authors**: Emaad Khwaja, Abdullah Rashwan, Ting Chen, Oliver Wang, Suraj Kothawade, Yeqing Li

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.06079v1](http://arxiv.org/pdf/2407.06079v1)

**Abstract**: We present a one-shot text-to-image diffusion model that can generate
high-resolution images from natural language descriptions. Our model employs a
layered U-Net architecture that simultaneously synthesizes images at multiple
resolution scales. We show that this method outperforms the baseline of
synthesizing images only at the target resolution, while reducing the
computational cost per step. We demonstrate that higher resolution synthesis
can be achieved by layering convolutions at additional resolution scales, in
contrast to other methods which require additional models for super-resolution
synthesis.


### EndoUIC: Promptable Diffusion Transformer for Unified Illumination Correction in Capsule Endoscopy
**Authors**: Long Bai, Tong Chen, Qiaozhi Tan, Wan Jun Nah, Yanheng Li, Zhicheng He, Sishen Yuan, Zhen Chen, Jinlin Wu, Mobarakol Islam, Zhen Li, Hongbin Liu, Hongliang Ren

**Published Date**: 2024-06-19

**Updated Date**: 2024-07-08

**PDF Url**: [2406.13705v2](http://arxiv.org/pdf/2406.13705v2)

**Abstract**: Wireless Capsule Endoscopy (WCE) is highly valued for its non-invasive and
painless approach, though its effectiveness is compromised by uneven
illumination from hardware constraints and complex internal dynamics, leading
to overexposed or underexposed images. While researchers have discussed the
challenges of low-light enhancement in WCE, the issue of correcting for
different exposure levels remains underexplored. To tackle this, we introduce
EndoUIC, a WCE unified illumination correction solution using an end-to-end
promptable diffusion transformer (DiT) model. In our work, the illumination
prompt module shall navigate the model to adapt to different exposure levels
and perform targeted image enhancement, in which the Adaptive Prompt
Integration (API) and Global Prompt Scanner (GPS) modules shall further boost
the concurrent representation learning between the prompt parameters and
features. Besides, the U-shaped restoration DiT model shall capture the
long-range dependencies and contextual information for unified illumination
restoration. Moreover, we present a novel Capsule-endoscopy Exposure Correction
(CEC) dataset, including ground-truth and corrupted image pairs annotated by
expert photographers. Extensive experiments against a variety of
state-of-the-art (SOTA) methods on four datasets showcase the effectiveness of
our proposed method and components in WCE illumination restoration, and the
additional downstream experiments further demonstrate its utility for clinical
diagnosis and surgical assistance.


## Quantitative Finance
### Graph Anomaly Detection with Noisy Labels by Reinforcement Learning
**Authors**: Zhu Wang, Shuang Zhou, Junnan Dong, Chang Yang, Xiao Huang, Shengjie Zhao

**Published Date**: 2024-07-08

**Updated Date**: 2024-07-08

**PDF Url**: [2407.05934v1](http://arxiv.org/pdf/2407.05934v1)

**Abstract**: Graph anomaly detection (GAD) has been widely applied in many areas, e.g.,
fraud detection in finance and robot accounts in social networks. Existing
methods are dedicated to identifying the outlier nodes that deviate from normal
ones. While they heavily rely on high-quality annotation, which is hard to
obtain in real-world scenarios, this could lead to severely degraded
performance based on noisy labels. Thus, we are motivated to cut the edges of
suspicious nodes to alleviate the impact of noise. However, it remains
difficult to precisely identify the nodes with noisy labels. Moreover, it is
hard to quantitatively evaluate the regret of cutting the edges, which may have
either positive or negative influences. To this end, we propose a novel
framework REGAD, i.e., REinforced Graph Anomaly Detector. Specifically, we aim
to maximize the performance improvement (AUC) of a base detector by cutting
noisy edges approximated through the nodes with high-confidence labels. (i) We
design a tailored action and search space to train a policy network to
carefully prune edges step by step, where only a few suspicious edges are
prioritized in each step. (ii) We design a policy-in-the-loop mechanism to
iteratively optimize the policy based on the feedback from base detector. The
overall performance is evaluated by the cumulative rewards. Extensive
experiments are conducted on three datasets under different anomaly ratios. The
results indicate the superior performance of our proposed REGAD.


