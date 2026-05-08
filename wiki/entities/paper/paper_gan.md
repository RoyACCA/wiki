---
id: paper_gan
title: "paper_gan"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:1406.2661
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "Generative Adversarial Networks - The GAN framework for training generative models via adversarial process."
conflicts: []
versions: []
claims: [{"id": "cdb5fc6c6", "text": "Generative Adversarial Nets Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio Departement d'informatique et de recherche operationnelle Universite de Montreal Montreal, QC H3C 3J7 Abstract We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1/2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:1406.2661"}]
---

# paper_gan

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 1406.2661 |
| Title | Generative Adversarial Networks |
| Authors | Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio |
| Year | 2014 |
| Published | 2014-06-10 |
| Categories | stat.ML, cs.LG |

## Summary

We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1/2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

## Details

Generative Adversarial Networks (GANs) introduced a revolutionary framework for training generative models:

- **Adversarial Training**: Two neural networks (generator G and discriminator D) are trained simultaneously in a game-theoretic setting
- **Generator**: Learns to create fake samples that look like real data
- **Discriminator**: Learns to distinguish between real and fake samples
- **Minimax Game**: The training is formulated as a minimax optimization problem where G tries to minimize D's ability to detect fakes, while D tries to maximize its accuracy
- **No Sampling Chains**: Unlike Boltzmann machines, GANs don't require Markov chains for sampling

The GAN framework has spawned numerous variants and applications including image generation, style transfer, data augmentation, and more.

## Related

- Source: [[https://arxiv.org/abs/1406.2661]]
- PDF: [[https://arxiv.org/pdf/1406.2661]]

## Provenance

> [!source]| cdb5fc6c6
> Generative Adversarial Nets Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio Departement d'informatique et de recherche operationnelle Universite de Montreal Montreal, QC H3C 3J7 Abstract We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G.
