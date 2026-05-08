---
id: paper_ddpm
title: "paper_ddpm"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:2006.11239
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "Denoising Diffusion Probabilistic Models - DDPMs for high-quality image synthesis using diffusion models."
conflicts: []
versions: []
claims: [{"id": "c2eafc907", "text": "We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:2006.11239"}]
---

# paper_ddpm

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 2006.11239 |
| Title | Denoising Diffusion Probabilistic Models |
| Authors | Jonathan Ho, Ajay Jain, Pieter Abbeel |
| Year | 2020 |
| Published | 2020-06-19 |
| Categories | cs.LG, stat.ML |

## Summary

We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion

## Details

Denoising Diffusion Probabilistic Models (DDPMs) introduced a new paradigm for generative modeling:

- **Diffusion Process**: Gradually adds noise to data (forward process) and learns to reverse this process (reverse process)
- **Thermodynamics Inspiration**: The forward process is inspired by nonequilibrium thermodynamics, diffusing data to noise
- **Variational Training**: Uses a weighted variational bound for training
- **Connection to Score Matching**: Links to denoising score matching with Langevin dynamics
- **Results**: Achieved Inception score of 9.46 and FID of 3.17 on CIFAR10, state-of-the-art at the time
- **Progressive Decoding**: Supports progressive lossy decompression, similar to autoregressive decoding

DDPMs became the foundation for modern diffusion models used in image generation (DALL-E 2, Stable Diffusion, Imagen) and have expanded to other domains including video generation and molecule design.

## Related

- Source: [[https://arxiv.org/abs/2006.11239]]
- PDF: [[https://arxiv.org/pdf/2006.11239]]

## Provenance

> [!source]| c2eafc907
> We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics.
