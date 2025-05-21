# Abstracts of Papers

## Physics
### Abacus: A Cost-Based Optimizer for Semantic Operator Systems
**Authors**: Matthew Russo, Sivaprasad Sudhir, Gerardo Vitagliano, Chunwei Liu, Tim Kraska, Samuel Madden, Michael Cafarella

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14661v1](http://arxiv.org/pdf/2505.14661v1)

**Abstract**: LLMs enable an exciting new class of data processing applications over large
collections of unstructured documents. Several new programming frameworks have
enabled developers to build these applications by composing them out of
semantic operators: a declarative set of AI-powered data transformations with
natural language specifications. These include LLM-powered maps, filters,
joins, etc. used for document processing tasks such as information extraction,
summarization, and more. While systems of semantic operators have achieved
strong performance on benchmarks, they can be difficult to optimize. An
optimizer for this setting must determine how to physically implement each
semantic operator in a way that optimizes the system globally. Existing
optimizers are limited in the number of optimizations they can apply, and most
(if not all) cannot optimize system quality, cost, or latency subject to
constraint(s) on the other dimensions. In this paper we present Abacus, an
extensible, cost-based optimizer which searches for the best implementation of
a semantic operator system given a (possibly constrained) optimization
objective. Abacus estimates operator performance by leveraging a minimal set of
validation examples and, if available, prior beliefs about operator
performance. We evaluate Abacus on document processing workloads in the
biomedical and legal domains (BioDEX; CUAD) and multi-modal question answering
(MMQA). We demonstrate that systems optimized by Abacus achieve 18.7%-39.2%
better quality and up to 23.6x lower cost and 4.2x lower latency than the next
best system.


### Engineering the Kondo impurity problem with alkaline-earth atom arrays
**Authors**: Adriano Amaricci, Andrea Richaud, Massimo Capone, Nelson Darkwah Oppong, Francesco Scazza

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14630v1](http://arxiv.org/pdf/2505.14630v1)

**Abstract**: We propose quantum simulation experiments of the Kondo impurity problem using
cold alkaline-earth(-like) atoms (AEAs) in a combination of optical lattice and
optical tweezer potentials. Within an ab initio model for atomic interactions
in the optical potentials, we analyze hallmark signatures of the Kondo effect
in a variety of observables accessible in cold-atom quantum simulators. We
identify additional terms not part of the textbook Kondo problem, mostly
ignored in previous works and giving rise to a direct competition between spin
and charge correlations--strongly suppressing Kondo physics. Crucially, we show
that the Kondo effect can be restored by locally adjusting the chemical
potential on the impurity site. We identify realistic parameter regimes and
preparation protocols suited to current experiments with AEA arrays. Our work
paves the way for novel quantum simulations of the Kondo problem and offers new
insights into Kondo physics in unconventional regimes.


### LaMET's Asymptotic Extrapolation vs. Inverse Problem
**Authors**: Jiunn-Wei Chen, Xiang Gao, Jinchen He, Jun Hua, Xiangdong Ji, Andreas Schäfer, Yushan Su, Wei Wang, Yi-Bo Yang, Jian-Hui Zhang, Qi-An Zhang, Rui Zhang, Yong Zhao

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14619v1](http://arxiv.org/pdf/2505.14619v1)

**Abstract**: Large-Momentum Effective Theory (LaMET) is a physics-guided systematic
expansion to calculate light-cone parton distributions, including collinear
(PDFs) and transverse-momentum-dependent ones, at any fixed momentum fraction
$x$ within a range of $[x_{\rm min}, x_{\rm max}]$. It theoretically solves the
ill-posed inverse problem that afflicts other theoretical approaches to
collinear PDFs, such as short-distance factorizations. Recently,
arXiv:2504.17706~\cite{Dutrieux:2025jed} raised practical concerns about
whether current or even future lattice data will have sufficient precision in
the sub-asymptotic correlation region to support an error-controlled
extrapolation -- and if not, whether it becomes an inverse problem where the
relevant uncertainties cannot be properly quantified. While we agree that not
all current lattice data have the desired precision to qualify for an
asymptotic extrapolation, some calculations do, and more are expected in the
future. We comment on the analysis and results in Ref.~\cite{Dutrieux:2025jed}
and argue that a physics-based systematic extrapolation still provides the most
reliable error estimates, even when the data quality is not ideal. In contrast,
re-framing the long-distance asymptotic extrapolation as a data-driven-only
inverse problem with {\it ad hoc} mathematical conditioning could lead to
unnecessarily conservative errors.


### Electrostatics from Laplacian Eigenbasis for Neural Network Interatomic Potentials
**Authors**: Maksim Zhdanov, Vladislav Kurenkov

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14606v1](http://arxiv.org/pdf/2505.14606v1)

**Abstract**: Recent advances in neural network interatomic potentials have emerged as a
promising research direction. However, popular deep learning models often lack
auxiliary constraints grounded in physical laws, which could accelerate
training and improve fidelity through physics-based regularization. In this
work, we introduce $\Phi$-Module, a universal plugin module that enforces
Poisson's equation within the message-passing framework to learn electrostatic
interactions in a self-supervised manner. Specifically, each atom-wise
representation is encouraged to satisfy a discretized Poisson's equation,
making it possible to acquire a potential $\boldsymbol{\phi}$ and a
corresponding charge density $\boldsymbol{\rho}$ linked to the learnable
Laplacian eigenbasis coefficients of a given molecular graph. We then derive an
electrostatic energy term, crucial for improved total energy predictions. This
approach integrates seamlessly into any existing neural potential with
insignificant computational overhead. Experiments on the OE62 and MD22
benchmarks confirm that models combined with $\Phi$-Module achieve robust
improvements over baseline counterparts. For OE62 error reduction ranges from
4.5\% to 17.8\%, and for MD22, baseline equipped with $\Phi$-Module achieves
best results on 5 out of 14 cases. Our results underscore how embedding a
first-principles constraint in neural interatomic potentials can significantly
improve performance while remaining hyperparameter-friendly, memory-efficient
and lightweight in training. Code will be available at
\href{https://github.com/dunnolab/phi-module}{dunnolab/phi-module}.


### A Physical Interpretation of Imaginary Time Delay
**Authors**: Isabella L. Giovannelli, Steven M. Anlage

**Published Date**: 2024-12-17

**Updated Date**: 2025-05-20

**PDF Url**: [2412.13139v2](http://arxiv.org/pdf/2412.13139v2)

**Abstract**: The scattering matrix $S$ linearly relates the vector of incoming waves to
outgoing wave excitations, and contains an enormous amount of information about
the scattering system and its connections to the scattering channels. Time
delay is one way to extract information from $S$, and the transmission time
delay $\tau_T$ is a complex (even for Hermitian systems with unitary scattering
matrices) measure of how long a wave excitation lingers before being
transmitted. The real part of $\tau_T$ is a well-studied quantity, but the
imaginary part of $\tau_T$ has not been systematically examined experimentally,
and theoretical predictions for its behavior have not been tested. Here we
experimentally test the predictions of Asano, et al. [Nat. Comm. 7, 13488
(2016)] for the imaginary part of transmission time delay in a non-unitary
scattering system. We utilize Gaussian time-domain pulses scattering from a
2-port microwave graph supporting a series of well-isolated absorptive modes to
show that the carrier frequency of the pulses is changed in the scattering
process by an amount in agreement with the imaginary part of the independently
determined complex transmission time delay, $\text{Im}[\tau_T]$, from
frequency-domain measurements of the sub-unitary $S$ matrix. Our results also
generalize and extend those of Asano, et al., establishing a means to predict
pulse propagation properties of non-Hermitian systems over a broad range of
conditions.


### Physics-informed Reduced Order Modeling of Time-dependent PDEs via Differentiable Solvers
**Authors**: Nima Hosseini Dashtbayaz, Hesam Salehipour, Adrian Butscher, Nigel Morris

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14595v1](http://arxiv.org/pdf/2505.14595v1)

**Abstract**: Reduced-order modeling (ROM) of time-dependent and parameterized differential
equations aims to accelerate the simulation of complex high-dimensional systems
by learning a compact latent manifold representation that captures the
characteristics of the solution fields and their time-dependent dynamics.
Although high-fidelity numerical solvers generate the training datasets, they
have thus far been excluded from the training process, causing the learned
latent dynamics to drift away from the discretized governing physics. This
mismatch often limits generalization and forecasting capabilities. In this
work, we propose Physics-informed ROM ($\Phi$-ROM) by incorporating
differentiable PDE solvers into the training procedure. Specifically, the
latent space dynamics and its dependence on PDE parameters are shaped directly
by the governing physics encoded in the solver, ensuring a strong
correspondence between the full and reduced systems. Our model outperforms
state-of-the-art data-driven ROMs and other physics-informed strategies by
accurately generalizing to new dynamics arising from unseen parameters,
enabling long-term forecasting beyond the training horizon, maintaining
continuity in both time and space, and reducing the data cost. Furthermore,
$\Phi$-ROM learns to recover and forecast the solution fields even when trained
or evaluated with sparse and irregular observations of the fields, providing a
flexible framework for field reconstruction and data assimilation. We
demonstrate the framework's robustness across different PDE solvers and
highlight its broad applicability by providing an open-source JAX
implementation readily extensible to other PDE systems and differentiable
solvers.


### Entanglement-assisted multiparameter estimation with a solid-state quantum sensor
**Authors**: Takuya Isogawa, Guoqing Wang, Boning Li, Zhiyao Hu, Shunsuke Nishimura, Ayumi Kanamoto, Haidong Yuan, Paola Cappellaro

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14578v1](http://arxiv.org/pdf/2505.14578v1)

**Abstract**: Quantum multiparameter estimation promises to extend quantum advantage to the
simultaneous high-precision measurements of multiple physical quantities.
However, realizing this capability in practical quantum sensors under realistic
conditions remains challenging due to intrinsic system imperfections. Here, we
experimentally demonstrate multiparameter estimation using a nitrogen-vacancy
(NV) center in diamond, a widely adopted solid-state quantum sensor. Leveraging
electronic-nuclear spin entanglement and optimized Bell state measurement at
room temperature, we simultaneously estimate the amplitude, detuning, and phase
of a microwave drive from a single measurement sequence. Despite practical
constraints, our results achieve linear sensitivity scaling for all parameters
with respect to interrogation time. This work bridges the gap between
foundational quantum estimation theory and real-world quantum sensing, opening
pathways toward enhanced multiparameter quantum sensors suitable for diverse
scientific and technological applications.


### Physics-Guided Learning of Meteorological Dynamics for Weather Downscaling and Forecasting
**Authors**: Yingtao Luo, Shikai Fang, Binqing Wu, Qingsong Wen, Liang Sun

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14555v1](http://arxiv.org/pdf/2505.14555v1)

**Abstract**: Weather forecasting is essential but remains computationally intensive and
physically incomplete in traditional numerical weather prediction (NWP)
methods. Deep learning (DL) models offer efficiency and accuracy but often
ignore physical laws, limiting interpretability and generalization. We propose
PhyDL-NWP, a physics-guided deep learning framework that integrates physical
equations with latent force parameterization into data-driven models. It
predicts weather variables from arbitrary spatiotemporal coordinates, computes
physical terms via automatic differentiation, and uses a physics-informed loss
to align predictions with governing dynamics. PhyDL-NWP enables resolution-free
downscaling by modeling weather as a continuous function and fine-tunes
pre-trained models with minimal overhead, achieving up to 170x faster inference
with only 55K parameters. Experiments show that PhyDL-NWP improves both
forecasting performance and physical consistency.


### A Renormalizable Model of Quantized Gravitational and Matter Fields
**Authors**: D. G. C. McKeon, F. T. Brandt, J. Frenkel, S. Martins-Filho

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14554v1](http://arxiv.org/pdf/2505.14554v1)

**Abstract**: A Lagrange multiplier field can be used to restrict radiative corrections to
the Einstein-Hilbert action to one-loop order. This result is employed to show
that it is possible to couple a scalar field to the metric (graviton) field in
such a way that the model is both renormalizable and unitary. The usual
Einstein equations of motion for the gravitational field are recovered,
perturbatively, in the classical limit. By evaluating the generating functional
of proper Green's functions in closed form, one obtains a novel analytic
contribution to the effective action.


### Distributed quantum computing with black-box subroutines
**Authors**: X. Xu, Y. -D. Liu, S. Shi, Y. -J. Wang, D. -S. Wang

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14519v1](http://arxiv.org/pdf/2505.14519v1)

**Abstract**: In this work, we propose a general protocol for distributed quantum computing
that accommodates arbitrary unknown subroutines. It can be applied to scale up
quantum computing through multi-chip interconnection, as well as to tasks such
as estimating unknown parameters or processes for circuit depth reduction and
constructing secure quantum cryptographic protocols. Our protocol builds upon a
few techniques we develop, such as the oblivious quantum teleportation and
control, which can circumvent quantum no-go theorems on the manipulation of
unknown objects. Furthermore, we demonstrate that this protocol can be
physically implemented using currently available quantum computing platforms.
These results suggest that our framework could provide a foundation for
developing more advanced quantum algorithms and protocols in the future.


## Diffusion
### Training-Free Watermarking for Autoregressive Image Generation
**Authors**: Yu Tong, Zihao Pan, Shuai Yang, Kaiyang Zhou

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14673v1](http://arxiv.org/pdf/2505.14673v1)

**Abstract**: Invisible image watermarking can protect image ownership and prevent
malicious misuse of visual generative models. However, existing generative
watermarking methods are mainly designed for diffusion models while
watermarking for autoregressive image generation models remains largely
underexplored. We propose IndexMark, a training-free watermarking framework for
autoregressive image generation models. IndexMark is inspired by the redundancy
property of the codebook: replacing autoregressively generated indices with
similar indices produces negligible visual differences. The core component in
IndexMark is a simple yet effective match-then-replace method, which carefully
selects watermark tokens from the codebook based on token similarity, and
promotes the use of watermark tokens through token replacement, thereby
embedding the watermark without affecting the image quality. Watermark
verification is achieved by calculating the proportion of watermark tokens in
generated images, with precision further improved by an Index Encoder.
Furthermore, we introduce an auxiliary validation scheme to enhance robustness
against cropping attacks. Experiments demonstrate that IndexMark achieves
state-of-the-art performance in terms of image quality and verification
accuracy, and exhibits robustness against various perturbations, including
cropping, noises, Gaussian blur, random erasing, color jittering, and JPEG
compression.


### Diffusion-Based Failure Sampling for Evaluating Safety-Critical Autonomous Systems
**Authors**: Harrison Delecki, Marc R. Schlichting, Mansur Arief, Anthony Corso, Marcell Vazquez-Chanlatte, Mykel J. Kochenderfer

**Published Date**: 2024-06-20

**Updated Date**: 2025-05-20

**PDF Url**: [2406.14761v2](http://arxiv.org/pdf/2406.14761v2)

**Abstract**: Validating safety-critical autonomous systems in high-dimensional domains
such as robotics presents a significant challenge. Existing black-box
approaches based on Markov chain Monte Carlo may require an enormous number of
samples, while methods based on importance sampling often rely on simple
parametric families that may struggle to represent the distribution over
failures. We propose to sample the distribution over failures using a
conditional denoising diffusion model, which has shown success in complex
high-dimensional problems such as robotic task planning. We iteratively train a
diffusion model to produce state trajectories closer to failure. We demonstrate
the effectiveness of our approach on high-dimensional robotic validation tasks,
improving sample efficiency and mode coverage compared to existing black-box
techniques.


### Latent Flow Transformer
**Authors**: Yen-Chen Wu, Feng-Ting Liao, Meng-Hsi Chen, Pei-Chen Ho, Farhang Nabiei, Da-shan Shiu

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14513v1](http://arxiv.org/pdf/2505.14513v1)

**Abstract**: Transformers, the standard implementation for large language models (LLMs),
typically consist of tens to hundreds of discrete layers. While more layers can
lead to better performance, this approach has been challenged as far from
efficient, especially given the superiority of continuous layers demonstrated
by diffusion and flow-based models for image generation. We propose the Latent
Flow Transformer (LFT), which replaces a block of layers with a single learned
transport operator trained via flow matching, offering significant compression
while maintaining compatibility with the original architecture. Additionally,
we address the limitations of existing flow-based methods in \textit{preserving
coupling} by introducing the Flow Walking (FW) algorithm. On the Pythia-410M
model, LFT trained with flow matching compresses 6 of 24 layers and outperforms
directly skipping 2 layers (KL Divergence of LM logits at 0.407 vs. 0.529),
demonstrating the feasibility of this design. When trained with FW, LFT further
distills 12 layers into one while reducing the KL to 0.736 surpassing that from
skipping 3 layers (0.932), significantly narrowing the gap between
autoregressive and flow-based generation paradigms.


### Minimum-Excess-Work Guidance
**Authors**: Christopher Kolloff, Tobias Höppe, Emmanouil Angelis, Mathias Jacob Schreiner, Stefan Bauer, Andrea Dittadi, Simon Olsson

**Published Date**: 2025-05-19

**Updated Date**: 2025-05-20

**PDF Url**: [2505.13375v2](http://arxiv.org/pdf/2505.13375v2)

**Abstract**: We propose a regularization framework inspired by thermodynamic work for
guiding pre-trained probability flow generative models (e.g., continuous
normalizing flows or diffusion models) by minimizing excess work, a concept
rooted in statistical mechanics and with strong conceptual connections to
optimal transport. Our approach enables efficient guidance in sparse-data
regimes common to scientific applications, where only limited target samples or
partial density constraints are available. We introduce two strategies: Path
Guidance for sampling rare transition states by concentrating probability mass
on user-defined subsets, and Observable Guidance for aligning generated
distributions with experimental observables while preserving entropy. We
demonstrate the framework's versatility on a coarse-grained protein model,
guiding it to sample transition configurations between folded/unfolded states
and correct systematic biases using experimental data. The method bridges
thermodynamic principles with modern generative architectures, offering a
principled, efficient, and physics-inspired alternative to standard fine-tuning
in data-scarce domains. Empirical results highlight improved sample efficiency
and bias reduction, underscoring its applicability to molecular simulations and
beyond.


### Learning to Integrate Diffusion ODEs by Averaging the Derivatives
**Authors**: Wenze Liu, Xiangyu Yue

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.14502v1](http://arxiv.org/pdf/2505.14502v1)

**Abstract**: To accelerate diffusion model inference, numerical solvers perform poorly at
extremely small steps, while distillation techniques often introduce complexity
and instability. This work presents an intermediate strategy, balancing
performance and cost, by learning ODE integration using loss functions derived
from the derivative-integral relationship, inspired by Monte Carlo integration
and Picard iteration. From a geometric perspective, the losses operate by
gradually extending the tangent to the secant, thus are named as secant losses.
The secant losses can rapidly convert (via fine-tuning or distillation) a
pretrained diffusion model into its secant version. In our experiments, the
secant version of EDM achieves a $10$-step FID of $2.14$ on CIFAR-10, while the
secant version of SiT-XL/2 attains a $4$-step FID of $2.27$ and an $8$-step FID
of $1.96$ on ImageNet-$256\times256$. Code will be available.


## Quantitative Finance
### Quantum Reservoir Computing for Realized Volatility Forecasting
**Authors**: Qingyu Li, Chiranjib Mukhopadhyay, Abolfazl Bayat, Ali Habibnia

**Published Date**: 2025-05-20

**Updated Date**: 2025-05-20

**PDF Url**: [2505.13933v1](http://arxiv.org/pdf/2505.13933v1)

**Abstract**: Recent advances in quantum computing have demonstrated its potential to
significantly enhance the analysis and forecasting of complex classical data.
Among these, quantum reservoir computing has emerged as a particularly powerful
approach, combining quantum computation with machine learning for modeling
nonlinear temporal dependencies in high-dimensional time series. As with many
data-driven disciplines, quantitative finance and econometrics can hugely
benefit from emerging quantum technologies. In this work, we investigate the
application of quantum reservoir computing for realized volatility forecasting.
Our model employs a fully connected transverse-field Ising Hamiltonian as the
reservoir with distinct input and memory qubits to capture temporal
dependencies. The quantum reservoir computing approach is benchmarked against
several econometric models and standard machine learning algorithms. The models
are evaluated using multiple error metrics and the model confidence set
procedures. To enhance interpretability and mitigate current quantum hardware
limitations, we utilize wrapper-based forward selection for feature selection,
identifying optimal subsets, and quantifying feature importance via Shapley
values. Our results indicate that the proposed quantum reservoir approach
consistently outperforms benchmark models across various metrics, highlighting
its potential for financial forecasting despite existing quantum hardware
constraints. This work serves as a proof-of-concept for the applicability of
quantum computing in econometrics and financial analysis, paving the way for
further research into quantum-enhanced predictive modeling as quantum hardware
capabilities continue to advance.


