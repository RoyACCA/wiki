---
id: 6f530351
title: "Unknown"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: raw/papers/ff5819e3_unknown.pdf
domain: ["general"]
tags: ["paper, general"]
confidence: 0.65
summary: "Generative Adversarial Nets。Ian J. Goodfellow, Jean Pouget-Abadie∗, Mehdi Mirza, Bing Xu, David Warde-Farley,。Sherjil Ozair†, Aaron Courville, Yoshua Bengio‡。"
conflicts: []
versions: []
claims: [{"id": "cdb5fc6c6", "text": "Generative Adversarial Nets\nIan J. Goodfellow, Jean Pouget-Abadie∗, Mehdi Mirza, Bing Xu, David Warde-Farley,\nSherjil Ozair†, Aaron Courville, Yoshua Bengio‡\nD´epartement d’informatique et de recherche op´erationnelle\nUniversit´e de Montr´eal\nMontr´eal, QC H3C 3J7\nAbstract\nWe propose a new framework for estimating generative models via an adversar-\nial process, in which we simultaneously train two models: a generative model G\nthat captures the data distribution, and a discriminative model D that", "para_index": 0, "entities": [], "domains": ["ai"], "type": "analysis", "source": "/home/agentuser/temp/papers/gan_generative_adversarial_nets.pdf"}]
---

# Unknown

## Summary
Generative Adversarial Nets。Ian J. Goodfellow, Jean Pouget-Abadie∗, Mehdi Mirza, Bing Xu, David Warde-Farley,。Sherjil Ozair†, Aaron Courville, Yoshua Bengio‡。

## Details
Generative Adversarial Nets
Ian J. Goodfellow, Jean Pouget-Abadie∗, Mehdi Mirza, Bing Xu, David Warde-Farley,
Sherjil Ozair†, Aaron Courville, Yoshua Bengio‡
D´epartement d’informatique et de recherche op´erationnelle
Universit´e de Montr´eal
Montr´eal, QC H3C 3J7
Abstract
We propose a new framework for estimating generative models via an adversar-
ial process, in which we simultaneously train two models: a generative model G
that captures the data distribution, and a discriminative model D that estimates
the probability that a sample came from the training data rather than G. The train-
ing procedure for G is to maximize the probability of D making a mistake. This
framework corresponds to a minimax two-player game. In the space of arbitrary
functions G and D, a unique solution exists, with G recovering the training data
distribution and D equal to 1
2 everywhere. In the case where G and D are deﬁned
by multilayer perceptrons, the entire system can be trained with backpropagation.
There is no need for any Markov chains or unrolled approximate inference net-
works during either training or generation of samples. Experiments demonstrate
the potential of the framework through qualitative and quantitative evaluation of
the generated samples.
1
Introduction
The promise of deep learning is to discover rich, hierarchical models [2] that represent probability
distributions over the kinds of data encountered in artiﬁcial intelligence applications, such as natural
images, audio waveforms containing speech, and symbols in natural language corpora. So far, the
most striking successes in deep learning have involved discriminative models, usually those that
map a high-dimensional, rich sensory input to a class label [14, 22]. These striking successes have
primarily been based on the backpropagation and dropout algorithms, using piecewise linear units
[19, 9, 10] which have a particularly well-behaved gradient . Deep generative models have had less
of an impact, due to the difﬁcul

[... truncated ...]

restricted Boltzmann machines using approximations to the likelihood
gradient. In W. W. Cohen, A. McCallum, and S. T. Roweis, editors, ICML 2008, pages 1064–1071. ACM.
[30] Vincent, P., Larochelle, H., Bengio, Y., and Manzagol, P.-A. (2008). Extracting and composing robust
features with denoising autoencoders. In ICML 2008.
[31] Younes, L. (1999).
On the convergence of Markovian stochastic algorithms with rapidly decreasing
ergodicity rates. Stochastics and Stochastic Reports, 65(3), 177–228.
9


## Related
- Sources: [[../raw/papers/ff5819e3_unknown.pdf]]



## Provenance
> [!source]| cdb5fc6c6
> Generative Adversarial Nets Ian J. Goodfellow, Jean Pouget-Abadie∗, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair†, Aaron Courville, Yoshua Bengio‡ D´epartement d’informatique et de recherch
