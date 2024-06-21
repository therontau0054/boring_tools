# Abstracts of Papers

## Physics
### Local symmetries in partially ordered sets
**Authors**: Christoph Minz

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14533v1](http://arxiv.org/pdf/2406.14533v1)

**Abstract**: Partially ordered sets (posets) have a universal appearance as an abstract
structure in many areas of mathematics. Though, even their explicit enumeration
remains unknown in general, and only the counts of all partial orders on sets
of up to 16 unlabelled elements have been calculated to date, see sequence
A000112 in the OEIS.
  In this work, we study automorphisms of posets in order to formulate a
classification by local symmetries. These symmetries give rise to a division
operation on the set of all posets and lead us to the construction of symmetry
classes that are easier to characterise and enumerate. Additionally to the
enumeration of symmetry classes, I derive polynomial expressions that count
certain subsets of posets with a large number of layers (a large height). As an
application in physics, I investigate local symmetries (or rather their lack
of) in causal sets, which are discrete spacetime models used as a candidate
framework for quantum gravity.


### Ambiguity Clustering: an accurate and efficient decoder for qLDPC codes
**Authors**: Stasiu Wolanski, Ben Barber

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14527v1](http://arxiv.org/pdf/2406.14527v1)

**Abstract**: Error correction allows a quantum computer to preserve a state long beyond
the decoherence time of its physical qubits by encoding logical qubits in a
larger number of physical qubits. The leading proposal for a scheme of quantum
error correction is based on the surface code, but several recently proposed
quantum low-density parity check (qLDPC) codes allow more logical information
to be encoded in significantly fewer physical qubits. Key to any scheme of
quantum error correction is the decoder, an algorithm that estimates the error
state of the qubits from the results of syndrome measurements performed on
them. The surface code has a variety of fast and accurate decoders, but the
state-of-the-art decoder for general qLDPC codes, BP-OSD, has a high
computational complexity. Here we introduce Ambiguity Clustering (AC), an
algorithm which seeks to divide the measurement data into clusters which are
decoded independently. We benchmark AC on the recently proposed bivariate
bicycle codes and find that, at physically realistic error rates, AC is between
one and three orders of magnitude faster than BP-OSD with no reduction in
logical fidelity. Our CPU implementation of AC is already fast enough to decode
the 144-qubit Gross code in real time for neutral atom and trapped ion systems.


### Scaling up global kinetic models of pulsar magnetospheres using a hybrid force-free-PIC numerical approach
**Authors**: Adrien Soudais, Benoît Cerutti, Ioannis Contopoulos

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14512v1](http://arxiv.org/pdf/2406.14512v1)

**Abstract**: The particle-in-cell approach has proven effective at modeling neutron star
and black hole magnetospheres from first principles, but global simulations are
plagued with an unrealistically small separation between the scales where
microphysics operates and the system-size scales due to limited numerical
resources. A legitimate concern is whether the scale separation currently
achieved is large enough, such that results can be safely extrapolated to
realistic scales. In this work, our aim is to explore the effect of scaling
physical parameters up, and to check whether salient features uncovered by pure
kinetic models at smaller scales are still valid, with a special emphasis on
particle acceleration and high-energy radiation emitted beyond the light
cylinder. To reach this objective, we develop a new hybrid numerical scheme
coupling the ideal force-free and the particle-in-cell methods, to optimize the
numerical cost of global models. We propose a domain decomposition of the
magnetosphere based on the magnetic field topology using the flux function. The
force-free model is enforced along open field lines while the particle-in-cell
model is restricted to the reconnecting field line region. As a proof of
concept, this new hybrid model is applied to simulate a weak millisecond pulsar
magnetosphere with realistic scales using high-resolution axisymmetric
simulations. Magnetospheric features reported by previous kinetic models are
recovered, and strong synchrotron radiation above 100MeV consistent with the
Fermi-LAT gamma-ray pulsar population is successfully reproduced. This work
further consolidates the shining reconnecting current sheet scenario as the
origin of the gamma-ray emission in pulsars, as well as firmly establishes
pulsar magnetospheres as at least TeV particle accelerators.


### rKAN: Rational Kolmogorov-Arnold Networks
**Authors**: Alireza Afzal Aghaei

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14495v1](http://arxiv.org/pdf/2406.14495v1)

**Abstract**: The development of Kolmogorov-Arnold networks (KANs) marks a significant
shift from traditional multi-layer perceptrons in deep learning. Initially,
KANs employed B-spline curves as their primary basis function, but their
inherent complexity posed implementation challenges. Consequently, researchers
have explored alternative basis functions such as Wavelets, Polynomials, and
Fractional functions. In this research, we explore the use of rational
functions as a novel basis function for KANs. We propose two different
approaches based on Pade approximation and rational Jacobi functions as
trainable basis functions, establishing the rational KAN (rKAN). We then
evaluate rKAN's performance in various deep learning and physics-informed tasks
to demonstrate its practicality and effectiveness in function approximation.


### Valid Error Bars for Neural Weather Models using Conformal Prediction
**Authors**: Vignesh Gopakumar, Joel Oskarrson, Ander Gray, Lorenzo Zanisi, Stanislas Pamela, Daniel Giles, Matt Kusner, Marc Deisenroth

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14483v1](http://arxiv.org/pdf/2406.14483v1)

**Abstract**: Neural weather models have shown immense potential as inexpensive and
accurate alternatives to physics-based models. However, most models trained to
perform weather forecasting do not quantify the uncertainty associated with
their forecasts. This limits the trust in the model and the usefulness of the
forecasts. In this work we construct and formalise a conformal prediction
framework as a post-processing method for estimating this uncertainty. The
method is model-agnostic and gives calibrated error bounds for all variables,
lead times and spatial locations. No modifications are required to the model
and the computational cost is negligible compared to model training. We
demonstrate the usefulness of the conformal prediction framework on a limited
area neural weather model for the Nordic region. We further explore the
advantages of the framework for deterministic and probabilistic models.


### High-threshold, low-overhead and single-shot decodable fault-tolerant quantum memory
**Authors**: Thomas R. Scruby, Timo Hillmann, Joschka Roffe

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14445v1](http://arxiv.org/pdf/2406.14445v1)

**Abstract**: We present a new family of quantum low-density parity-check codes, which we
call radial codes, obtained from the lifted product of a specific subset of
classical quasi-cyclic codes. The codes are defined using a pair of integers
$(r,s)$ and have parameters $[\![2r^2s,2(r-1)^2,\leq2s]\!]$, with numerical
studies suggesting average-case distance linear in $s$. In simulations of
circuit-level noise, we observe comparable error suppression to surface codes
of similar distance while using approximately five times fewer physical qubits.
This is true even when radial codes are decoded using a single-shot approach,
which can allow for faster logical clock speeds and reduced decoding
complexity. We describe an intuitive visual representation, canonical basis of
logical operators and optimal-length stabiliser measurement circuits for these
codes, and argue that their error correction capabilities, tunable parameters
and small size make them promising candidates for implementation on near-term
quantum devices.


### Physics-aware Machine Learning Revolutionizes Scientific Paradigm for Machine Learning and Process-based Hydrology
**Authors**: Qingsong Xu, Yilei Shi, Jonathan Bamber, Ye Tuo, Ralf Ludwig, Xiao Xiang Zhu

**Published Date**: 2023-10-08

**Updated Date**: 2024-06-20

**PDF Url**: [2310.05227v4](http://arxiv.org/pdf/2310.05227v4)

**Abstract**: Accurate hydrological understanding and water cycle prediction are crucial
for addressing scientific and societal challenges associated with the
management of water resources, particularly under the dynamic influence of
anthropogenic climate change. Existing reviews predominantly concentrate on the
development of machine learning (ML) in this field, yet there is a clear
distinction between hydrology and ML as separate paradigms. Here, we introduce
physics-aware ML as a transformative approach to overcome the perceived barrier
and revolutionize both fields. Specifically, we present a comprehensive review
of the physics-aware ML methods, building a structured community (PaML) of
existing methodologies that integrate prior physical knowledge or physics-based
modeling into ML. We systematically analyze these PaML methodologies with
respect to four aspects: physical data-guided ML, physics-informed ML,
physics-embedded ML, and physics-aware hybrid learning. PaML facilitates
ML-aided hypotheses, accelerating insights from big data and fostering
scientific discoveries. We first conduct a systematic review of hydrology in
PaML, including rainfall-runoff hydrological processes and hydrodynamic
processes, and highlight the most promising and challenging directions for
different objectives and PaML methods. Finally, a new PaML-based hydrology
platform, termed HydroPML, is released as a foundation for hydrological
applications. HydroPML enhances the explainability and causality of ML and lays
the groundwork for the digital water cycle's realization. The HydroPML platform
is publicly available at https://hydropml.github.io/.


### Transferable Boltzmann Generators
**Authors**: Leon Klein, Frank Noé

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14426v1](http://arxiv.org/pdf/2406.14426v1)

**Abstract**: The generation of equilibrium samples of molecular systems has been a
long-standing problem in statistical physics. Boltzmann Generators are a
generative machine learning method that addresses this issue by learning a
transformation via a normalizing flow from a simple prior distribution to the
target Boltzmann distribution of interest. Recently, flow matching has been
employed to train Boltzmann Generators for small molecular systems in Cartesian
coordinates. We extend this work and propose a first framework for Boltzmann
Generators that are transferable across chemical space, such that they predict
zero-shot Boltzmann distributions for test molecules without being retrained
for these systems. These transferable Boltzmann Generators allow approximate
sampling from the target distribution of unseen systems, as well as efficient
reweighting to the target Boltzmann distribution. The transferability of the
proposed framework is evaluated on dipeptides, where we show that it
generalizes efficiently to unseen systems. Furthermore, we demonstrate that our
proposed architecture enhances the efficiency of Boltzmann Generators trained
on single molecular systems.


### Electrical switching of Ising-superconducting nonreciprocity for quantum neuronal transistor
**Authors**: Junlin Xiong, Jiao Xie, Bin Cheng, Yudi Dai, Xinyu Cui, Lizheng Wang, Zenglin Liu, Ji Zhou, Naizhou Wang, Xianghan Xu, Xianhui Chen, Sang-Wook Cheong, Shi-Jun Liang, Feng Miao

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14417v1](http://arxiv.org/pdf/2406.14417v1)

**Abstract**: Nonreciprocal quantum transport effect is mainly governed by the symmetry
breaking of the material systems and is gaining extensive attention in
condensed matter physics. Realizing electrical switching of the polarity of the
nonreciprocal transport without external magnetic field is essential to the
development of nonreciprocal quantum devices. However, electrical switching of
superconducting nonreciprocity remains yet to be achieved. Here, we report the
observation of field-free electrical switching of nonreciprocal Ising
superconductivity in Fe3GeTe2/NbSe2 van der Waals (vdW) heterostructure. By
taking advantage of this electrically switchable superconducting
nonreciprocity, we demonstrate a proof-of-concept nonreciprocal quantum
neuronal transistor, which allows for implementing the XOR logic gate and
faithfully emulating biological functionality of a cortical neuron in the
brain. Our work provides a promising pathway to realize field-free and
electrically switchable nonreciprocity of quantum transport and demonstrate its
potential in exploring neuromorphic quantum devices with both functionality and
performance beyond the traditional devices.


### Silicon Nitride C-Band Grating Coupler with Reduced Waveguide Back-Reflection Using Adaptively Corrected Elliptical Grates
**Authors**: Ibrahim Ghannam, Florian Merget, Jeremy Witzens

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14413v1](http://arxiv.org/pdf/2406.14413v1)

**Abstract**: We present experimental results for a fully etched C-band grating coupler
with reduced back reflection fabricated in an 800 nm silicon nitride platform.
Back-reflections are reduced by symmetrically interrupting the first few grates
around the center axis of the propagating light. The span of the etched grates
is gradually increased until they cover the full width. By interrupting the
grates, light is reflected back obliquely, which leads to the excitation of
higher-order modes that are scattered out of the structure. While this approach
has been previously shown in silicon, it comes with a significant penalty in
coupling efficiency of around 2.4 dB of extra loss in the layer stack
investigated here. In this work, we present the design and measurement results
of a grating coupler in which waveguide-to-waveguide back-reflections are
suppressed by ~10 dB with this technique, while at the same time mitigating
excess insertion losses by reshaping the grates as ellipses of varying
eccentricity. This helps to compensate the phase front error induced by the
interruption of the grates. This correction does not affect the level by which
the back-reflection is suppressed, but reduces the insertion loss penalty from
2.4 dB to 1 dB.


## Diffusion
### Consistency Models Made Easy
**Authors**: Zhengyang Geng, Ashwini Pokle, William Luo, Justin Lin, J. Zico Kolter

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14548v1](http://arxiv.org/pdf/2406.14548v1)

**Abstract**: Consistency models (CMs) are an emerging class of generative models that
offer faster sampling than traditional diffusion models. CMs enforce that all
points along a sampling trajectory are mapped to the same initial point. But
this target leads to resource-intensive training: for example, as of 2024,
training a SoTA CM on CIFAR-10 takes one week on 8 GPUs. In this work, we
propose an alternative scheme for training CMs, vastly improving the efficiency
of building such models. Specifically, by expressing CM trajectories via a
particular differential equation, we argue that diffusion models can be viewed
as a special case of CMs with a specific discretization. We can thus fine-tune
a consistency model starting from a pre-trained diffusion model and
progressively approximate the full consistency condition to stronger degrees
over the training process. Our resulting method, which we term Easy Consistency
Tuning (ECT), achieves vastly improved training times while indeed improving
upon the quality of previous methods: for example, ECT achieves a 2-step FID of
2.73 on CIFAR10 within 1 hour on a single A100 GPU, matching Consistency
Distillation trained of hundreds of GPU hours. Owing to this computational
efficiency, we investigate the scaling law of CMs under ECT, showing that they
seem to obey classic power law scaling, hinting at their ability to improve
efficiency and performance at larger scales. Code
(https://github.com/locuslab/ect) is available.


### V-LASIK: Consistent Glasses-Removal from Videos Using Synthetic Data
**Authors**: Rotem Shalev-Arkushin, Aharon Azulay, Tavi Halperin, Eitan Richardson, Amit H. Bermano, Ohad Fried

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14510v1](http://arxiv.org/pdf/2406.14510v1)

**Abstract**: Diffusion-based generative models have recently shown remarkable image and
video editing capabilities. However, local video editing, particularly removal
of small attributes like glasses, remains a challenge. Existing methods either
alter the videos excessively, generate unrealistic artifacts, or fail to
perform the requested edit consistently throughout the video. In this work, we
focus on consistent and identity-preserving removal of glasses in videos, using
it as a case study for consistent local attribute removal in videos. Due to the
lack of paired data, we adopt a weakly supervised approach and generate
synthetic imperfect data, using an adjusted pretrained diffusion model. We show
that despite data imperfection, by learning from our generated data and
leveraging the prior of pretrained diffusion models, our model is able to
perform the desired edit consistently while preserving the original video
content. Furthermore, we exemplify the generalization ability of our method to
other local video editing tasks by applying it successfully to facial
sticker-removal. Our approach demonstrates significant improvement over
existing methods, showcasing the potential of leveraging synthetic data and
strong video priors for local video editing tasks.


### SafeSora: Towards Safety Alignment of Text2Video Generation via a Human Preference Dataset
**Authors**: Josef Dai, Tianle Chen, Xuyao Wang, Ziran Yang, Taiye Chen, Jiaming Ji, Yaodong Yang

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14477v1](http://arxiv.org/pdf/2406.14477v1)

**Abstract**: To mitigate the risk of harmful outputs from large vision models (LVMs), we
introduce the SafeSora dataset to promote research on aligning text-to-video
generation with human values. This dataset encompasses human preferences in
text-to-video generation tasks along two primary dimensions: helpfulness and
harmlessness. To capture in-depth human preferences and facilitate structured
reasoning by crowdworkers, we subdivide helpfulness into 4 sub-dimensions and
harmlessness into 12 sub-categories, serving as the basis for pilot
annotations. The SafeSora dataset includes 14,711 unique prompts, 57,333 unique
videos generated by 4 distinct LVMs, and 51,691 pairs of preference annotations
labeled by humans. We further demonstrate the utility of the SafeSora dataset
through several applications, including training the text-video moderation
model and aligning LVMs with human preference by fine-tuning a prompt
augmentation module or the diffusion model. These applications highlight its
potential as the foundation for text-to-video alignment research, such as human
preference modeling and the development and validation of alignment algorithms.


### CollaFuse: Collaborative Diffusion Models
**Authors**: Simeon Allmendinger, Domenique Zipperling, Lukas Struppek, Niklas Kühl

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14429v1](http://arxiv.org/pdf/2406.14429v1)

**Abstract**: In the landscape of generative artificial intelligence, diffusion-based
models have emerged as a promising method for generating synthetic images.
However, the application of diffusion models poses numerous challenges,
particularly concerning data availability, computational requirements, and
privacy. Traditional approaches to address these shortcomings, like federated
learning, often impose significant computational burdens on individual clients,
especially those with constrained resources. In response to these challenges,
we introduce a novel approach for distributed collaborative diffusion models
inspired by split learning. Our approach facilitates collaborative training of
diffusion models while alleviating client computational burdens during image
synthesis. This reduced computational burden is achieved by retaining data and
computationally inexpensive processes locally at each client while outsourcing
the computationally expensive processes to shared, more efficient server
resources. Through experiments on the common CelebA dataset, our approach
demonstrates enhanced privacy by reducing the necessity for sharing raw data.
These capabilities hold significant potential across various application areas,
including the design of edge computing solutions. Thus, our work advances
distributed machine learning by contributing to the evolution of collaborative
diffusion models.


### Active Diffusion Subsampling
**Authors**: Oisin Nolan, Tristan S. W. Stevens, Wessel L. van Nierop, Ruud J. G. van Sloun

**Published Date**: 2024-06-20

**Updated Date**: 2024-06-20

**PDF Url**: [2406.14388v1](http://arxiv.org/pdf/2406.14388v1)

**Abstract**: Subsampling is commonly used to mitigate costs associated with data
acquisition, such as time or energy requirements, motivating the development of
algorithms for estimating the fully-sampled signal of interest $x$ from
partially observed measurements $y$. In maximum-entropy sampling, one selects
measurement locations that are expected to have the highest entropy, so as to
minimize uncertainty about $x$. This approach relies on an accurate model of
the posterior distribution over future measurements, given the measurements
observed so far. Recently, diffusion models have been shown to produce
high-quality posterior samples of high-dimensional signals using guided
diffusion. In this work, we propose Active Diffusion Subsampling (ADS), a
method for performing active subsampling using guided diffusion in which the
model tracks a distribution of beliefs over the true state of $x$ throughout
the reverse diffusion process, progressively decreasing its uncertainty by
choosing to acquire measurements with maximum expected entropy, and ultimately
generating the posterior distribution $p(x | y)$. ADS can be applied using
pre-trained diffusion models for any subsampling rate, and does not require
task-specific retraining - just the specification of a measurement model.
Furthermore, the maximum entropy sampling policy employed by ADS is
interpretable, enhancing transparency relative to existing methods using
black-box policies. Experimentally, we show that ADS outperforms fixed sampling
strategies, and study an application of ADS in Magnetic Resonance Imaging
acceleration using the fastMRI dataset, finding that ADS performs competitively
with supervised methods. Code available at
https://active-diffusion-subsampling.github.io/.


## Quantitative Finance
