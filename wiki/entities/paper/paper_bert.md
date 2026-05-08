---
id: paper_bert
title: "paper_bert"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:1810.04805
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding - Revolutionary pre-training approach for NLP."
conflicts: []
versions: []
claims: [{"id": "c3c0672b3", "text": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova Google AI Language {jacobdevlin,mingweichang,kentonl,kristout}@google.com Abstract We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:1810.04805"}]
---

# paper_bert

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 1810.04805 |
| Title | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding |
| Authors | Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova |
| Year | 2018 |
| Published | 2018-10-11 |
| Categories | cs.CL |

## Summary

We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

## Details

BERT (Bidirectional Encoder Representations from Transformers) introduced a revolutionary pre-training approach for NLP:

- **Bidirectional Pre-training**: Unlike previous language models that read text left-to-right or right-to-left, BERT conditions on both left and right context in all layers.
- **Masked Language Model (MLM)**: BERT randomly masks some tokens and predicts the masked words, enabling bidirectional conditioning.
- **Next Sentence Prediction (NSP)**: Pre-training includes predicting whether one sentence follows another, helping with tasks like natural language inference.
- **Fine-tuning**: Pre-trained BERT can be fine-tuned for specific tasks with minimal architecture changes, just by adding a task-specific output layer.

BERT achieved state-of-the-art results on 11 NLP tasks upon release and sparked the large language model revolution.

## Related

- Source: [[https://arxiv.org/abs/1810.04805]]
- PDF: [[https://arxiv.org/pdf/1810.04805]]

## Provenance

> [!source]| c3c0672b3
> BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova Google AI Language {jacobdevlin,mingweichang,kentonl,kristout}@google.com Abstract We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
