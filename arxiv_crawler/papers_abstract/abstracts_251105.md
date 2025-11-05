# Abstracts of Papers

## Physics
### Tensors, entanglement, separability, and their complexity
**Authors**: Shmuel Friedland

**Published Date**: 2025-09-25

**Updated Date**: 2025-11-04

**PDF Url**: [2509.21639v2](http://arxiv.org/pdf/2509.21639v2)

**Abstract**: One of the most challenging problems in quantum physics is to quantify the
entanglement of $d$-partite states and their separability. We show here that
these problems are best addressed using tensors. The geometric measure of
entanglement of a pure state is one of most natural ways to quantify the
entanglement, which is simply related to the spectral norm of a tensor state.
On the other hand, the logarithm of the nuclear norm of the state and density
tensors can be considered as its ``energy''. We first show that the most
geometric measure entangled $d$-partite state has the minimum spectral norm and
maximum nuclear norm. Second, we introduce the notion of Hermitian and density
tensors, and the subspace of bi-symmetric Hermitian tensors, which correspond
to Bosons. We show that separable density tensors, and strongly separable
bi-symmetric density tensors are characterized by the value (equal to one) of
their corresponding nuclear norms. In general, these characterizations are
NP-hard to verify. Third, we show that the above quantities are computed in
polynomial time when we restrict our attentions to Bosons: symmetric
$d$-qubits, or more generally to symmetric $d$-qunits in $C^n$, and the
corresponding bi-symmetric Hermtian density tensors, for a fixed value of $n$.


### Neurosymbolic Deep Learning Semantics
**Authors**: Artur d'Avila Garcez, Simon Odense

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02825v1](http://arxiv.org/pdf/2511.02825v1)

**Abstract**: Artificial Intelligence (AI) is a powerful new language of science as
evidenced by recent Nobel Prizes in chemistry and physics that recognized
contributions to AI applied to those areas. Yet, this new language lacks
semantics, which makes AI's scientific discoveries unsatisfactory at best. With
the purpose of uncovering new facts but also improving our understanding of the
world, AI-based science requires formalization through a framework capable of
translating insight into comprehensible scientific knowledge. In this paper, we
argue that logic offers an adequate framework. In particular, we use logic in a
neurosymbolic framework to offer a much needed semantics for deep learning, the
neural network-based technology of current AI. Deep learning and neurosymbolic
AI lack a general set of conditions to ensure that desirable properties are
satisfied. Instead, there is a plethora of encoding and knowledge extraction
approaches designed for particular cases. To rectify this, we introduced a
framework for semantic encoding, making explicit the mapping between neural
networks and logic, and characterizing the common ingredients of the various
existing approaches. In this paper, we describe succinctly and exemplify how
logical semantics and neural networks are linked through this framework, we
review some of the most prominent approaches and techniques developed for
neural encoding and knowledge extraction, provide a formal definition of our
framework, and discuss some of the difficulties of identifying a semantic
encoding in practice in light of analogous problems in the philosophy of mind.


### Hybrid Quantum-Classical Recurrent Neural Networks
**Authors**: Wenduan Xu

**Published Date**: 2025-10-29

**Updated Date**: 2025-11-04

**PDF Url**: [2510.25557v2](http://arxiv.org/pdf/2510.25557v2)

**Abstract**: We present a hybrid quantum-classical recurrent neural network (QRNN)
architecture in which the recurrent core is realized as a parametrized quantum
circuit (PQC) controlled by a classical feedforward network. The hidden state
is the quantum state of an $n$-qubit PQC in an exponentially large Hilbert
space $\mathbb{C}^{2^n}$, which serves as a coherent recurrent quantum memory.
The PQC is unitary by construction, making the hidden-state evolution
norm-preserving without external constraints. At each timestep, mid-circuit
Pauli expectation-value readouts are combined with the input embedding and
processed by the feedforward network, which provides explicit classical
nonlinearity. The outputs parametrize the PQC, which updates the hidden state
via unitary dynamics. The QRNN is compact and physically consistent, and it
unifies (i) unitary recurrence as a high-capacity memory, (ii) partial
observation via mid-circuit readouts, and (iii) nonlinear classical control for
input-conditioned parametrization. We evaluate the model in simulation with up
to 14 qubits on sentiment analysis, MNIST, permuted MNIST, copying memory, and
language modeling. For sequence-to-sequence learning, we further devise a soft
attention mechanism over the mid-circuit readouts and show its effectiveness
for machine translation. To our knowledge, this is the first model (RNN or
otherwise) grounded in quantum operations to achieve competitive performance
against strong classical baselines across a broad class of sequence-learning
tasks.


### Majorana string simulation of nonequilibrium dynamics in two-dimensional lattice fermion systems
**Authors**: Matteo D'Anna, Jannes Nys, Juan Carrasquilla

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02809v1](http://arxiv.org/pdf/2511.02809v1)

**Abstract**: The study of real-time dynamics of fermions remains one of the last frontiers
beyond the reach of classical simulations and is key to our understanding of
quantum behavior in chemistry and materials, with implications for quantum
technology. Here we introduce a Heisenberg-picture algorithm that propagates
observables expressed in a Majorana-string basis using a truncation scheme that
preserves Trotter accuracy and aims at maintaining computational efficiency.
The framework is exact for quadratic Hamiltonians--remaining restricted to a
fixed low-weight sector determined by the physical observable--admits
variational initial states, and can be extended to interacting regimes via
systematically controlled truncations. We benchmark our approach on one- and
two-dimensional Fermi-Hubbard quenches, comparing against tensor network
methods (MPS and fPEPS) and recent experimental data. The method achieves high
accuracy on timescales comparable to state-of-the-art variational techniques
and experiments, demonstrating that controlled Majorana-string truncation is a
practical tool for simulating two-dimensional fermionic dynamics.


### Topologically Quantized Soliton-Like Pumping using Synthetic Nonlinearity
**Authors**: Ankitkumar Maisuriya, Siddhi Mali, Sunil Mittal

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02806v1](http://arxiv.org/pdf/2511.02806v1)

**Abstract**: The interplay between nonlinear and topological physics has led to intriguing
emergent phenomena, such as quantized and fractionally quantized Thouless
pumping of solitons dictated by the topological invariants of the underlying
band structure. Unlike linear Thouless pumping, which requires excitation of a
Wannier function of a uniformly filled band, quantized soliton pumping is
observed even with localized excitations that do not represent Wannier
functions. Here, we show that similar soliton-like quantized pumping can be
observed in Aubry-Andre-Harper (AAH) model by introducing a synthetic
nonlinearity in the form of a cutoff on the coupling strengths between lattice
sites. More importantly, we reveal that the localized excitations driving
quantized soliton pumping are precisely the Wannier functions of the uniformly
filled bands of the effectively nonlinear lattice, thus restoring consistency
with linear Thouless pumping. We extend this approach to multi-band systems and
show that the nonlinearity introduces a degeneracy between bands, subsequently
leading to the observation of fractionally quantized pumping. Our approach of
introducing a synthetic nonlinearity is general and could be extended to reveal
soliton dynamics in other nonlinear topological systems.


### Code in Motion: Integrating Computational Thinking with Kinematics Exploration
**Authors**: Mateo Dutra, Álvaro Suárez, Arturo C. Marti

**Published Date**: 2025-03-05

**Updated Date**: 2025-11-04

**PDF Url**: [2503.03850v2](http://arxiv.org/pdf/2503.03850v2)

**Abstract**: Although physics has become increasingly computational, with computing even
being considered the third pillar of physics, it is still not well integrated
into physics education. Research suggests that integrating Computational
Thinking (CT) into physics enhances conceptual understanding and strengthens
students' ability to model and analyze phenomena. Building on this, we designed
a didactic sequence for K9 students to foster specific CT practices while
reinforcing fundamental kinematics concepts. The activity revealed students'
ability to apply CT skills and is well suited for use in introductory
kinematics courses.


### Visualization of High Dynamic Range Solar Imagery and the Radial Histogram Equalizing Filter
**Authors**: Chris Gilly, Steven Cranmer

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02798v1](http://arxiv.org/pdf/2511.02798v1)

**Abstract**: Standard visualizations of Extreme Ultraviolet (EUV) solar imagery often fail
to convey the full complexity of the Sun's corona, especially in faint off-limb
regions. This can leave the misleading impression of the Sun as a bright ball
in a dark void, rather than revealing it as the dynamic, structured source of
the solar wind and space weather. A variety of enhancement algorithms have been
developed to address this challenge, each with its own strengths and tradeoffs.
We introduce the Radial Histogram Equalizing Filter (RHEF), a novel hybrid
technique that optimizes contrast in high dynamic range solar images. By
combining the spatial awareness of radial graded filters with the perceptual
benefits of histogram equalization, RHEF reveals faint coronal structures and
works out of the box -- without requiring careful parameter tuning or prior
dataset characterization. RHEF operates independently on each frame, and it
enhances on-disk and off-limb features uniformly across the field of view. For
additional control, we also present the Upsilon redistribution function -- a
symmetrized cousin of gamma correction -- as an optional post-processing step
that provides intuitive programmatic tonal compression. We benchmark RHEF
against established methods and offer guidance on filter selection across
various applications, with examples from multiple solar instruments provided in
an appendix. Implemented and available in both Python sunkit_image and IDL,
RHEF enables immediate improvements in solar coronal visualization.


### Enhancing Kinematics Understanding through a Video Game Based on Real-Time Motion Graphs
**Authors**: Mateo Dutra, Marcos Abreu, Martín Monteiro, Silvia Sguilla, Cecilia Stari, Álvaro Suárez, Arturo Martí

**Published Date**: 2025-08-26

**Updated Date**: 2025-11-04

**PDF Url**: [2508.19119v3](http://arxiv.org/pdf/2508.19119v3)

**Abstract**: Interpreting kinematic graphs remains a significant challenge in physics
education. The MissionMotion Project addresses this issue by providing a
gamified physical-computational environment combining low-cost sensors,
physical activity, computational thinking, and real-time visualization of
motion graphs. This paper presents the design, development, and implementation
of the project, with a particular focus on the pilot phase conducted with high
school students in Uruguay. During this phase, we primarily used the MEEGA+
questionnaire to evaluate the gaming experience, usability, and motivation of
the participants. Our analysis of the results shows high levels of
satisfaction, perceived learning, and engagement, supporting the proposal's
viability. Finally, we plan to conduct a large-scale conceptual evaluation to
analyze how the proposal impacts understanding of kinematic graphs using
standardized assessment tools.


### When alcoved polytopes add
**Authors**: Nick Early, Lukas Kühne, Leonid Monin

**Published Date**: 2025-01-28

**Updated Date**: 2025-11-04

**PDF Url**: [2501.17249v2](http://arxiv.org/pdf/2501.17249v2)

**Abstract**: Alcoved polytopes are characterized by the property that all facet normal
directions are parallel to the roots $e_i-e_j$. Unlike other prominent families
of polytopes, like generalized permutahedra, alcoved polytopes are not closed
under Minkowski sums. We nonetheless show that the Minkowski sum of a
collection of alcoved polytopes is alcoved if and only if each pairwise sum is
alcoved. This implies that the type fan of alcoved polytopes is determined by
its two-dimensional cones. Moreover, we provide a complete characterization of
when the Minkowski sum of alcoved simplices is again alcoved via a graphical
criterion on pairs of ordered set partitions. Our characterization reduces to
checking conditions on restricted partitions of length at most six. In
particular, we show how the Minkowski sum decompositions of the two most
well-known families of alcoved polytopes, the associahedron and the
cyclohedron, fit in our framework. Additionally, inspired by the physical
construction of one-loop scattering amplitudes, we present a new infinite
family of alcoved polytopes, called $\widehat{D}_n$ polytopes. We conclude by
drawing a connection to matroidal blade arrangements and the Dressian.


### An introduction to Markovian open quantum systems
**Authors**: Shovan Dutta

**Published Date**: 2025-10-30

**Updated Date**: 2025-11-04

**PDF Url**: [2510.26530v2](http://arxiv.org/pdf/2510.26530v2)

**Abstract**: This is a concise, pedagogical introduction to the dynamic field of open
quantum systems governed by Markovian master equations. We focus on the
mathematical and physical origins of the widely used Lindblad equation, its
unraveling in terms of stochastic pure-state trajectories and the corresponding
continuous measurement protocols, the structure of steady states with emphasis
on the role of symmetry and conservation laws, and a sampling of the novel
physical phenomena that arise from nonunitary dynamics (dissipation and
measurements). This is far from a comprehensive summary of the field. Rather,
the objective is to provide a conceptual foundation and physically illuminating
examples that are useful to graduate students and researchers entering this
subject. There are exercise problems and references for further reading
throughout the notes.


## Diffusion
### Measuring AI Diffusion: A Population-Normalized Metric for Tracking Global AI Usage
**Authors**: Amit Misra, Jane Wang, Scott McCullers, Kevin White, Juan Lavista Ferres

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02781v1](http://arxiv.org/pdf/2511.02781v1)

**Abstract**: Measuring global AI diffusion remains challenging due to a lack of
population-normalized, cross-country usage data. We introduce AI User Share, a
novel indicator that estimates the share of each country's working-age
population actively using AI tools. Built from anonymized Microsoft telemetry
and adjusted for device access and mobile scaling, this metric spans 147
economies and provides consistent, real-time insight into global AI diffusion.
We find wide variation in adoption, with a strong correlation between AI User
Share and GDP. High uptake is concentrated in developed economies, though usage
among internet-connected populations in lower-income countries reveals
substantial latent demand. We also detect sharp increases in usage following
major product launches, such as DeepSeek in early 2025. While the metric's
reliance solely on Microsoft telemetry introduces potential biases related to
this user base, it offers an important new lens into how AI is spreading
globally. AI User Share enables timely benchmarking that can inform data-driven
AI policy.


### AI Diffusion in Low Resource Language Countries
**Authors**: Amit Misra, Syed Waqas Zamir, Wassim Hamidouche, Inbal Becker-Reshef, Juan Lavista Ferres

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02752v1](http://arxiv.org/pdf/2511.02752v1)

**Abstract**: Artificial intelligence (AI) is diffusing globally at unprecedented speed,
but adoption remains uneven. Frontier Large Language Models (LLMs) are known to
perform poorly on low-resource languages due to data scarcity. We hypothesize
that this performance deficit reduces the utility of AI, thereby slowing
adoption in Low-Resource Language Countries (LRLCs). To test this, we use a
weighted regression model to isolate the language effect from socioeconomic and
demographic factors, finding that LRLCs have a share of AI users that is
approximately 20% lower relative to their baseline. These results indicate that
linguistic accessibility is a significant, independent barrier to equitable AI
diffusion.


### TAUE: Training-free Noise Transplant and Cultivation Diffusion Model
**Authors**: Daichi Nagai, Ryugo Morita, Shunsuke Kitada, Hitoshi Iyatomi

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02580v1](http://arxiv.org/pdf/2511.02580v1)

**Abstract**: Despite the remarkable success of text-to-image diffusion models, their
output of a single, flattened image remains a critical bottleneck for
professional applications requiring layer-wise control. Existing solutions
either rely on fine-tuning with large, inaccessible datasets or are
training-free yet limited to generating isolated foreground elements, failing
to produce a complete and coherent scene. To address this, we introduce the
Training-free Noise Transplantation and Cultivation Diffusion Model (TAUE), a
novel framework for zero-shot, layer-wise image generation. Our core technique,
Noise Transplantation and Cultivation (NTC), extracts intermediate latent
representations from both foreground and composite generation processes,
transplanting them into the initial noise for subsequent layers. This ensures
semantic and structural coherence across foreground, background, and composite
layers, enabling consistent, multi-layered outputs without requiring
fine-tuning or auxiliary datasets. Extensive experiments show that our
training-free method achieves performance comparable to fine-tuned methods,
enhancing layer-wise consistency while maintaining high image quality and
fidelity. TAUE not only eliminates costly training and dataset requirements but
also unlocks novel downstream applications, such as complex compositional
editing, paving the way for more accessible and controllable generative
workflows.


## Quantitative Finance
### The ORCA Benchmark: Evaluating Real-World Calculation Accuracy in Large Language Models
**Authors**: Claudia Herambourg, Dawid Siuda, Anna Szczepanek, Julia Kopczyńska, Joao R. L. Santos, Wojciech Sas, Joanna Śmietańska-Nowak

**Published Date**: 2025-11-04

**Updated Date**: 2025-11-04

**PDF Url**: [2511.02589v1](http://arxiv.org/pdf/2511.02589v1)

**Abstract**: We present ORCA (Omni Research on Calculation in AI) Benchmark -- a novel
benchmark that evaluates large language models (LLMs) on multi-domain,
real-life quantitative reasoning using verified outputs from Omni's calculator
engine. In 500 natural-language tasks across domains such as finance, physics,
health, and statistics, the five state-of-the-art systems (ChatGPT-5,
Gemini~2.5~Flash, Claude~Sonnet~4.5, Grok~4, and DeepSeek~V3.2) achieved only
$45\text{--}63\,\%$ accuracy, with errors mainly related to rounding ($35\,\%$)
and calculation mistakes ($33\,\%$). Results in specific domains indicate
strengths in mathematics and engineering, but weaknesses in physics and natural
sciences. Correlation analysis ($r \approx 0.40\text{--}0.65$) shows that the
models often fail together but differ in the types of errors they make,
highlighting their partial complementarity rather than redundancy. Unlike
standard math datasets, ORCA evaluates step-by-step reasoning, numerical
precision, and domain generalization across real problems from finance,
physics, health, and statistics.


