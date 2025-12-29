# Abstracts of Papers

## Physics
### Charge-Informed Quantum Error Correction
**Authors**: Vlad Temkin, Zack Weinstein, Ruihua Fan, Daniel Podolsky, Ehud Altman

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.22119v1](https://arxiv.org/pdf/2512.22119v1)

**Abstract**: We investigate the statistical physics of quantum error correction in ${\rm U}(1)$ symmetry-enriched topological quantum memories. Starting from a phenomenological error model of charge-conserving noise, we study the optimal decoder assuming the local charges of each anyon can be measured. The error threshold of the optimal decoder corresponds to a continuous phase transition in a disordered two-dimensional integer loop model on the Nishimori line. Using an effective replica field theory analysis and Monte Carlo numerics, we show that the optimal decoding transition exhibits Berezinskii-Kosterlitz-Thouless universality with a modified universal jump in winding number variance. We further generalize the model beyond the Nishimori line, which defines a large class of suboptimal decoders. At low nonzero temperatures and strong disorder, we find numerical evidence of a disorder-dominated loop-glass phase which corresponds to a "confidently incorrect" decoder. The zero-temperature limit defines the minimum-cost flow decoder, which serves as the ${\rm U}(1)$ analog of minimum-weight perfect matching in $\mathbb{Z}_2$ topological codes. Both the optimal and minimum-cost flow decoders are shown to dramatically outperform the charge-agnostic optimal decoder in symmetry-enriched topological codes.


### A simple realization of Weyl-Heisenberg covariant measurements
**Authors**: Sachin Gupta, Matthew B. Weiss

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.22111v1](https://arxiv.org/pdf/2512.22111v1)

**Abstract**: Informationally complete (IC) measurements are fundamental tools in quantum information processing, yet their physical implementation remains challenging. By the Naimark extension theorem, an IC measurement may be realized by a von Neumann measurement on an extended system after a suitable interaction. In this work, we elaborate on a simple algorithm for realizing Naimark extensions for rank-one Weyl-Heisenberg covariant informationally complete measurements in arbitrary finite dimensions. Exploiting Weyl-Heisenberg covariance, we show that the problem reduces to determining a $d \times d$ unitary from which the full $d^2 \times d^2$ unitary interaction can be constructed. The latter unitary enjoys a block-circulant structure which allows e.g., for an elegant optical implementation. We illustrate the procedure with explicit calculations for qubit, qutrit, and ququart SIC-POVMs. Finally, we show that from another point of view, this method amounts to preparing an ancilla system according to a so-called fiducial state, followed by a generalized Bell-basis measurement on the system and ancilla. These results provide a straightforward framework for implementing informationally complete measurements in the laboratory suitable for both qubit and qudit based systems.


### Rewards-based image analysis in microscopy
**Authors**: Kamyar Barakati, Yu Liu, Utkarsh Pratiush, Boris N. Slautin, Sergei V. Kalinin

**Published Date**: 2025-02-23

**Updated Date**: 2025-12-26

**PDF Url**: [2502.18522v2](https://arxiv.org/pdf/2502.18522v2)

**Abstract**: Imaging and hyperspectral data analysis is central to progress across biology, medicine, chemistry, and physics. The core challenge lies in converting high-resolution or high-dimensional datasets into interpretable representations that enable insight into the underlying physical or chemical properties of a system. Traditional analysis relies on expert-designed, multistep workflows, such as denoising, feature extraction, clustering, dimensionality reduction, and physics-based deconvolution, or on machine learning (ML) methods that accelerate individual steps. Both approaches, however, typically demand significant human intervention, including hyperparameter tuning and data labeling. Achieving the next level of autonomy in scientific imaging requires designing effective reward-based workflows that guide algorithms toward best data representation for human or automated decision-making. Here, we discuss recent advances in reward-based workflows for image analysis, which capture key elements of human reasoning and exhibit strong transferability across various tasks. We highlight how reward-driven approaches enable a shift from supervised black-box models toward explainable, unsupervised optimization on the examples of Scanning Probe and Electron Microscopies. Such reward-based frameworks are promising for a broad range of applications, including classification, regression, structure-property mapping, and general hyperspectral data processing.


### Lorentz Transformation in Quantum Mechanics
**Authors**: Marcello Baldo

**Published Date**: 2025-11-14

**Updated Date**: 2025-12-26

**PDF Url**: [2511.11342v3](https://arxiv.org/pdf/2511.11342v3)

**Abstract**: The compatibility of special relativity and Quantum Mechanics has been questioned by several authors. The origin of this tension can be traced back mainly to the introduction of the measurement processes and the corresponding wave function reduction, which play a crucial role in Quantum Mechanics. We approach this problem with the help of a recent proposal for a model of Quantum Mechanics, where the measurement is explicitly described as a specific stochastic process. This implements ordinary Quantum Mechanics, where measurement and reduction are treated as phenomenological events of unknown origin without any physical justification. To state clearly the question in general, we first discuss and establish the effect of a Lorentz transformation on a generic wave function in space-time. Alongside the analysis we formulate the relativistic version of the model. We then consider few thought experiments in order to analyze to what extent Quantum Mechanics follows relativistic invariance and find the specific critical points where non invariance possibly occurs. The analysis can shade light to the interpretation of the existing experimental observations.


### NetQMPI: An MPI-Inspired library for programming Distributed Quantum Applications over Quantum Networks using NetQASM SDK
**Authors**: F. Javier Cardama, Tomás F. Pena

**Published Date**: 2025-12-12

**Updated Date**: 2025-12-26

**PDF Url**: [2512.11483v2](https://arxiv.org/pdf/2512.11483v2)

**Abstract**: Distributed Quantum Computing (DQC) is essential for scaling quantum algorithms beyond the limitations of monolithic NISQ devices. However, the current software ecosystem forces developers to manually orchestrate low-level network resources, such as entanglement generation (EPR pairs) and classical synchronization, leading to verbose, error-prone, and non-scalable code. This paper introduces \textbf{NetQMPI}, a high-level Python framework that adapts the Message Passing Interface (MPI) standard to the quantum domain using the Single Program Multiple Data (SPMD) paradigm. Built as a middleware over the NetQASM SDK, NetQMPI abstracts the underlying physical topology, automating network initialization and resource management through a unified Communicator interface. We propose semantic point-to-point primitives and novel collective operations--such as expose and unexpose--that address the constraints of the No-Cloning Theorem by leveraging multipartite entanglement for data distribution. Our comparative analysis demonstrates that NetQMPI decouples algorithmic logic from network size, reducing the code complexity for generating an $N$-node GHZ state from $\mathcal{O}(N^2)$ to constant complexity $\mathcal{O}(1)$. Furthermore, the framework ensures backend agnosticism, enabling the seamless execution of high-level applications on rigorous physical simulators, such as NetSquid (via SquidASM), and future quantum hardware adhering to the NetQASM standard.


### Enhanced Distributed Variational Quantum Eigensolver for Large-Scale MaxCut Problem
**Authors**: Yuefeng Lin, Kun Wang, Qinyuan Zheng, Rui Zhang, Jing-Kai Fang, Tiejun Meng, Jingen Xiang, Cong Guo, Jun-Han Huang

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.22056v1](https://arxiv.org/pdf/2512.22056v1)

**Abstract**: MaxCut is a canonical NP-hard combinatorial optimization problem in graph theory with broad applications ranging from physics to bioinformatics. Although variational quantum algorithms offer promising new approaches that may eventually outperform classical schemes, they suffer from resource constraints and trainability issues such as barren plateaus, making large-scale instances intractable on noisy intermediate-scale quantum devices. In this paper, we propose an enhanced distributed variational quantum eigensolver for large-scale MaxCut problems, which extends our prior distributed variational quantum eigensolver framework by integrating a novel hybrid classical-quantum perturbation strategy, enhances optimization scalability and efficiency. Our algorithm solves weighted MaxCut instances with up to 1000 vertices using only 10 qubits, and numerical results indicate that it consistently outperforms the Goemans-Williamson algorithm. We further employ a warm-start initialization strategy, seeding the algorithm with high-quality solutions from the Goemans-Williamson algorithm, with results confirming that the optimal classical solution can be effectively further improved. The practical utility of the proposed algorithm is further validated through its application to haplotype phasing on genome sequencing data of the human ABCA1 gene, producing high-quality haplotypes that rival those obtained by the Goemans-Williamson algorithm with $10^6$ projections. These results establish the proposed algorithm as a scalable, NISQ-compatible framework for near-term quantum-enhanced large-scale combinatorial optimization.


### Real-time propagators resummed with nontrivial boundary wavefunctions in a constant electric field
**Authors**: Kenji Fukushima, Shuhei Minato

**Published Date**: 2025-12-22

**Updated Date**: 2025-12-26

**PDF Url**: [2512.19337v2](https://arxiv.org/pdf/2512.19337v2)

**Abstract**: We present the derivation of an alternative representation of the real-time in-in formalism under a spatially homogeneous and time independent electric field. Because the system exhibits instability associated with pair production of particles and antiparticles, the perturbation theory should be reorganized depending on the choice of the reference vacuum. We recast the boundary wavefunctions into the quadratic self-energy-like terms in the functional integration formalism. The resulting generating functional in the modified in-in formalism leads to the propagators that resum infinite diagrams necessary to capture the vacuum-instability effects. The proper-time representations of the propagators reproduce the known expressions from the canonical operator formalism, but our derivation based on the generating functional along the closed-time path clarifies the origin of the additional proper-time contour and provides a better physical understanding. Finally, as a concrete example of the application, we compute the in-in expectation value of the vector current in a constant electric field, and find that the simple one-loop calculation captures the pair production effect.


### Rethinking photonic nanojets: a new definition and design paradigm
**Authors**: Mirza Karamehmedović, Kristoffer Linder-Steinlein, Jesper Glückstad

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.22008v1](https://arxiv.org/pdf/2512.22008v1)

**Abstract**: We propose a rigorous, physically interpretable, and quantifiable definition of the photonic nanojet (PNJ). This framework resolves longstanding ambiguities in measuring PNJ dimensions and leverages an optimal mass transport-based metric to quantify PNJ quality. Building on this metric, we develop a PNJ steering methodology that requires no opto-mechanical intervention, relying solely on phase-only illumination modulation.


### Revealing the transient ionization dynamics and mode-coupling mechanisms of helicon discharge through a self-consistent multiphysics model
**Authors**: Jing-Jing Ma, Lei Chang, Ming-Yang Wu, Hua Zhou, Yi-Wei Zhang, Ilya Zadiriev, Elena Kralkina, Shogo Isayama, Shin-Jae You

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.21974v1](https://arxiv.org/pdf/2512.21974v1)

**Abstract**: Helicon plasma sources play a central role in applications ranging from material treatment to space propulsion and fusion, yet the physical processes governing their ignition, transient ionization, and mode evolution remain incompletely understood. Here we develop a self-consistent, fully coupled multiphysics framework that integrates Maxwell equations, electron energy transport, drift-diffusion kinetics, and heavy-species chemistry to capture the complete spatiotemporal evolution of helicon discharges. The model reproduces experimental measurements across pressure, magnetic field, and frequency ranges, and reveals a previously unresolved transient ionization stage characterized by a rapid density rise within ~10-4 s, accompanied by a two-peak electron temperature structure that governs the formation of the dense plasma core. By tracking the RF power flow and field topology, we characterize the transient redistribution of RF energy during ignition. A short-lived phase of localized energy deposition accompanies the onset of ionization, followed by an evolution toward helicon-like field characteristics together with rapid density growth and profile restructuring. Systematic parametric scans further reveal the sensitivity of this mode-coupling process to gas pressure, magnetic field strength, and driving frequency. These results provide a unified picture of the ignition and mode-transition physics in helicon plasmas and establish a predictive tool for the design and optimization of RF plasma sources across space propulsion, manufacturing, and fusion technologies.


### The Wiener Path Integral Interpretation of the 3:1 Combat Rule
**Authors**: Wei Liang, Ming Zhong

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.21957v1](https://arxiv.org/pdf/2512.21957v1)

**Abstract**: The Wiener path integral framework is proposed to model military combat dynamics by incorporating the neglected stochastic effects to the Lanchester's square law. This framework is applied to evaluate the empirical 3:1 combat rule, which posits that an attacker requires a threefold force superiority to achieve victory. Specifically, the attacker's winning probability is computed utilizing a semi-analytical Rayleigh-Ritz method. Numerical results demonstrate that the validity of the rule critically depends on specific parameter regimes, primarily contingent upon the relative combat effectiveness ratio between the opposing forces and the tolerance for attrition. This work establishes a physics-informed theoretical bridge between statistical mechanics and military operations research for analyzing uncertain combat systems.


## Diffusion
### Accelerating Diffusion Planners in Offline RL via Reward-Aware Consistency Trajectory Distillation
**Authors**: Xintong Duan, Yutong He, Fahim Tajwar, Ruslan Salakhutdinov, J. Zico Kolter, Jeff Schneider

**Published Date**: 2025-06-09

**Updated Date**: 2025-12-26

**PDF Url**: [2506.07822v2](https://arxiv.org/pdf/2506.07822v2)

**Abstract**: Although diffusion models have achieved strong results in decision-making tasks, their slow inference speed remains a key limitation. While consistency models offer a potential solution, existing applications to decision-making either struggle with suboptimal demonstrations under behavior cloning or rely on complex concurrent training of multiple networks under the actor-critic framework. In this work, we propose a novel approach to consistency distillation for offline reinforcement learning that directly incorporates reward optimization into the distillation process. Our method achieves single-step sampling while generating higher-reward action trajectories through decoupled training and noise-free reward signals. Empirical evaluations on the Gym MuJoCo, FrankaKitchen, and long horizon planning benchmarks demonstrate that our approach can achieve a 9.7% improvement over previous state-of-the-art while offering up to 142x speedup over diffusion counterparts in inference time.


### StreamAvatar: Streaming Diffusion Models for Real-Time Interactive Human Avatars
**Authors**: Zhiyao Sun, Ziqiao Peng, Yifeng Ma, Yi Chen, Zhengguang Zhou, Zixiang Zhou, Guozhen Zhang, Youliang Zhang, Yuan Zhou, Qinglin Lu, Yong-Jin Liu

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.22065v1](https://arxiv.org/pdf/2512.22065v1)

**Abstract**: Real-time, streaming interactive avatars represent a critical yet challenging goal in digital human research. Although diffusion-based human avatar generation methods achieve remarkable success, their non-causal architecture and high computational costs make them unsuitable for streaming. Moreover, existing interactive approaches are typically limited to head-and-shoulder region, limiting their ability to produce gestures and body motions. To address these challenges, we propose a two-stage autoregressive adaptation and acceleration framework that applies autoregressive distillation and adversarial refinement to adapt a high-fidelity human video diffusion model for real-time, interactive streaming. To ensure long-term stability and consistency, we introduce three key components: a Reference Sink, a Reference-Anchored Positional Re-encoding (RAPR) strategy, and a Consistency-Aware Discriminator. Building on this framework, we develop a one-shot, interactive, human avatar model capable of generating both natural talking and listening behaviors with coherent gestures. Extensive experiments demonstrate that our method achieves state-of-the-art performance, surpassing existing approaches in generation quality, real-time efficiency, and interaction naturalness. Project page: https://streamavatar.github.io .


### Real-Time Streamable Generative Speech Restoration with Flow Matching
**Authors**: Simon Welker, Bunlong Lay, Maris Hillemann, Tal Peer, Timo Gerkmann

**Published Date**: 2025-12-22

**Updated Date**: 2025-12-26

**PDF Url**: [2512.19442v2](https://arxiv.org/pdf/2512.19442v2)

**Abstract**: Diffusion-based generative models have greatly impacted the speech processing field in recent years, exhibiting high speech naturalness and spawning a new research direction. Their application in real-time communication is, however, still lagging behind due to their computation-heavy nature involving multiple calls of large DNNs.
  Here, we present Stream$.$FM, a frame-causal flow-based generative model with an algorithmic latency of 32 milliseconds (ms) and a total latency of 48 ms, paving the way for generative speech processing in real-time communication. We propose a buffered streaming inference scheme and an optimized DNN architecture, show how learned few-step numerical solvers can boost output quality at a fixed compute budget, explore model weight compression to find favorable points along a compute/quality tradeoff, and contribute a model variant with 24 ms total latency for the speech enhancement task.
  Our work looks beyond theoretical latencies, showing that high-quality streaming generative speech processing can be realized on consumer GPUs available today. Stream$.$FM can solve a variety of speech processing tasks in a streaming fashion: speech enhancement, dereverberation, codec post-filtering, bandwidth extension, STFT phase retrieval, and Mel vocoding. As we verify through comprehensive evaluations and a MUSHRA listening test, Stream$.$FM establishes a state-of-the-art for generative streaming speech restoration, exhibits only a reasonable reduction in quality compared to a non-streaming variant, and outperforms our recent work (Diffusion Buffer) on generative streaming speech enhancement while operating at a lower latency.


### From In Silico to In Vitro: Evaluating Molecule Generative Models for Hit Generation
**Authors**: Nagham Osman, Vittorio Lembo, Giovanni Bottegoni, Laura Toni

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.22031v1](https://arxiv.org/pdf/2512.22031v1)

**Abstract**: Hit identification is a critical yet resource-intensive step in the drug discovery pipeline, traditionally relying on high-throughput screening of large compound libraries. Despite advancements in virtual screening, these methods remain time-consuming and costly. Recent progress in deep learning has enabled the development of generative models capable of learning complex molecular representations and generating novel compounds de novo. However, using ML to replace the entire drug-discovery pipeline is highly challenging. In this work, we rather investigate whether generative models can replace one step of the pipeline: hit-like molecule generation. To the best of our knowledge, this is the first study to explicitly frame hit-like molecule generation as a standalone task and empirically test whether generative models can directly support this stage of the drug discovery pipeline. Specifically, we investigate if such models can be trained to generate hit-like molecules, enabling direct incorporation into, or even substitution of, traditional hit identification workflows. We propose an evaluation framework tailored to this task, integrating physicochemical, structural, and bioactivity-related criteria within a multi-stage filtering pipeline that defines the hit-like chemical space. Two autoregressive and one diffusion-based generative models were benchmarked across various datasets and training settings, with outputs assessed using standard metrics and target-specific docking scores. Our results show that these models can generate valid, diverse, and biologically relevant compounds across multiple targets, with a few selected GSK-3$β$ hits synthesized and confirmed active in vitro. We also identify key limitations in current evaluation metrics and available training data.


### Convolutional autoencoders for the reconstruction of three-dimensional interfacial multiphase flows
**Authors**: Murray Cutforth, Shahab Mirjalili

**Published Date**: 2025-08-06

**Updated Date**: 2025-12-26

**PDF Url**: [2508.04084v2](https://arxiv.org/pdf/2508.04084v2)

**Abstract**: We present a systematic investigation of convolutional autoencoders for the reduced-order representation of three-dimensional interfacial multiphase flows. Focusing on the reconstruction of phase indicators, we examine how the choice of interface representation, including sharp, diffuse, and level-set formulations, impacts reconstruction accuracy across a range of interface complexities. Training and validation are performed using both synthetic datasets with controlled geometric complexity and high-fidelity simulations of multiphase homogeneous isotropic turbulence. We show that the interface representation plays a critical role in autoencoder performance. Excessively sharp interfaces lead to the loss of small-scale features, while overly diffuse interfaces degrade overall accuracy. Across all datasets and metrics considered, a moderately diffuse interface provides the best balance between preserving fine-scale structures and achieving accurate reconstructions. These findings elucidate key limitations and best practices for dimensionality reduction of multiphase flows using autoencoders. By clarifying how interface representations interact with the inductive biases of convolutional neural networks, this work lays the foundation for decoupling the training of autoencoders for accurate state compression from the training of surrogate models for temporal forecasting or input-output prediction in latent space.


## Quantitative Finance
### MASFIN: A Multi-Agent System for Decomposed Financial Reasoning and Forecasting
**Authors**: Marc S. Montalvo, Hamed Yaghoobian

**Published Date**: 2025-12-26

**Updated Date**: 2025-12-26

**PDF Url**: [2512.21878v1](https://arxiv.org/pdf/2512.21878v1)

**Abstract**: Recent advances in large language models (LLMs) are transforming data-intensive domains, with finance representing a high-stakes environment where transparent and reproducible analysis of heterogeneous signals is essential. Traditional quantitative methods remain vulnerable to survivorship bias, while many AI-driven approaches struggle with signal integration, reproducibility, and computational efficiency. We introduce MASFIN, a modular multi-agent framework that integrates LLMs with structured financial metrics and unstructured news, while embedding explicit bias-mitigation protocols. The system leverages GPT-4.1-nano for reproducability and cost-efficient inference and generates weekly portfolios of 15-30 equities with allocation weights optimized for short-term performance. In an eight-week evaluation, MASFIN delivered a 7.33% cumulative return, outperforming the S&P 500, NASDAQ-100, and Dow Jones benchmarks in six of eight weeks, albeit with higher volatility. These findings demonstrate the promise of bias-aware, generative AI frameworks for financial forecasting and highlight opportunities for modular multi-agent design to advance practical, transparent, and reproducible approaches in quantitative finance.


### Applications of synthetic financial data in portfolio and risk modeling
**Authors**: Christophe D. Hounwanou, Yae Ulrich Gaba

**Published Date**: 2025-12-25

**Updated Date**: 2025-12-25

**PDF Url**: [2512.21798v1](https://arxiv.org/pdf/2512.21798v1)

**Abstract**: Synthetic financial data offers a practical way to address the privacy and accessibility challenges that limit research in quantitative finance. This paper examines the use of generative models, in particular TimeGAN and Variational Autoencoders (VAEs), for creating synthetic return series that support portfolio construction, trading analysis, and risk modeling. Using historical daily returns from the S and P 500 as a benchmark, we generate synthetic datasets under comparable market conditions and evaluate them using statistical similarity metrics, temporal structure tests, and downstream financial tasks. The study shows that TimeGAN produces synthetic data with distributional shapes, volatility patterns, and autocorrelation behaviour that are close to those observed in real returns. When applied to mean-variance portfolio optimization, the resulting synthetic datasets lead to portfolio weights, Sharpe ratios, and risk levels that remain close to those obtained from real data. The VAE provides more stable training but tends to smooth extreme market movements, which affects risk estimation. Finally, the analysis supports the use of synthetic datasets as substitutes for real financial data in portfolio analysis and risk simulation, particularly when models are able to capture temporal dynamics. Synthetic data therefore provides a privacy-preserving, cost-effective, and reproducible tool for financial experimentation and model development.


