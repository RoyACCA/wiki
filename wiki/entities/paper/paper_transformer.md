---
id: paper_transformer
title: "paper_transformer"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:1706.03762
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "Attention Is All You Need - The Transformer architecture that revolutionized NLP by replacing recurrence with attention mechanisms."
conflicts: []
versions: []
claims: [{"id": "c77a27e84", "text": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:1706.03762"}]
---

# paper_transformer

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 1706.03762 |
| Title | Attention Is All You Need |
| Authors | Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin |
| Year | 2017 |
| Published | 2017-06-12 |
| Categories | cs.CL, cs.LG |

## Summary

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## Details

The Transformer architecture introduced by Vaswani et al. (2017) revolutionized natural language processing by replacing recurrent neural networks with self-attention mechanisms. Key innovations include:

- **Self-Attention**: The model computes attention between all positions in the sequence simultaneously, allowing for parallel processing and capturing long-range dependencies.
- **Multi-Head Attention**: Multiple attention heads allow the model to attend to different aspects of the input simultaneously.
- **Positional Encoding**: Since the architecture has no recurrence, positional information is injected using sinusoidal encodings.
- **Encoder-Decoder Structure**: The original Transformer uses an encoder to process the input sequence and a decoder to generate the output.

The paper demonstrated that the Transformer achieves state-of-the-art results on machine translation tasks while being more computationally efficient than previous models based on recurrent or convolutional networks.

## Related

- Source: [[https://arxiv.org/abs/1706.03762]]
- PDF: [[https://arxiv.org/pdf/1706.03762]]

## Provenance

> [!source]| c77a27e84
> The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
