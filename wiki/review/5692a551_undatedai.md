---
id: 0da7a5f9
title: "Undatedai"
created: 2026-05-07
updated: 2026-05-07
type: entity-event
source: raw/papers/5692a551_undatedai.pdf
domain: ["ai"]
tags: ["event, ai"]
confidence: 0.8
summary: "BERT: Pre-training of Deep Bidirectional Transformers for。Language Understanding。Jacob Devlin。"
conflicts: []
versions: []
claims: [{"id": "c3c0672b3", "text": "BERT: Pre-training of Deep Bidirectional Transformers for\nLanguage Understanding\nJacob Devlin\nMing-Wei Chang\nKenton Lee\nKristina Toutanova\nGoogle AI Language\n{jacobdevlin,mingweichang,kentonl,kristout}@google.com\nAbstract\nWe introduce a new language representa-\ntion model called BERT, which stands for\nBidirectional Encoder Representations from\nTransformers. Unlike recent language repre-\nsentation models (Peters et al., 2018a; Rad-\nford et al., 2018), BERT is designed to pre-\ntrain deep bidirecti", "para_index": 0, "entities": [], "domains": ["ai"], "type": "policy", "source": "/home/agentuser/temp/papers/bert_pre-training_deep_bidirectional.pdf"}]
---

# Undatedai

## Summary
BERT: Pre-training of Deep Bidirectional Transformers for。Language Understanding。Jacob Devlin。

## Details
BERT: Pre-training of Deep Bidirectional Transformers for
Language Understanding
Jacob Devlin
Ming-Wei Chang
Kenton Lee
Kristina Toutanova
Google AI Language
{jacobdevlin,mingweichang,kentonl,kristout}@google.com
Abstract
We introduce a new language representa-
tion model called BERT, which stands for
Bidirectional Encoder Representations from
Transformers. Unlike recent language repre-
sentation models (Peters et al., 2018a; Rad-
ford et al., 2018), BERT is designed to pre-
train deep bidirectional representations from
unlabeled text by jointly conditioning on both
left and right context in all layers. As a re-
sult, the pre-trained BERT model can be ﬁne-
tuned with just one additional output layer
to create state-of-the-art models for a wide
range of tasks, such as question answering and
language inference, without substantial task-
speciﬁc architecture modiﬁcations.
BERT is conceptually simple and empirically
powerful.
It obtains new state-of-the-art re-
sults on eleven natural language processing
tasks, including pushing the GLUE score to
80.5% (7.7% point absolute improvement),
MultiNLI accuracy to 86.7% (4.6% absolute
improvement), SQuAD v1.1 question answer-
ing Test F1 to 93.2 (1.5 point absolute im-
provement) and SQuAD v2.0 Test F1 to 83.1
(5.1 point absolute improvement).
1
Introduction
Language model pre-training has been shown to
be effective for improving many natural language
processing tasks (Dai and Le, 2015; Peters et al.,
2018a; Radford et al., 2018; Howard and Ruder,
2018). These include sentence-level tasks such as
natural language inference (Bowman et al., 2015;
Williams et al., 2018) and paraphrasing (Dolan
and Brockett, 2005), which aim to predict the re-
lationships between sentences by analyzing them
holistically, as well as token-level tasks such as
named entity recognition and question answering,
where models are required to produce ﬁne-grained
output at the token level (Tjong Kim Sang and
De Meulder, 2003; Rajpurkar et al., 2016).
There 

[... truncated ...]

 the paper represents the
Dev set results. For the feature-based approach,
we concatenate the last 4 layers of BERT as the
features, which was shown to be the best approach
in Section 5.3.
From the table it can be seen that ﬁne-tuning is
surprisingly robust to different masking strategies.
However, as expected, using only the MASK strat-
egy was problematic when applying the feature-
based approach to NER. Interestingly, using only
the RND strategy performs much worse than our
strategy as well.


## Related
- Sources: [[../raw/papers/5692a551_undatedai.pdf]]

- Concepts: [[concept_ai]]

## Provenance
> [!source]| c3c0672b3
> BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova Google AI Language {jacobdevlin,mingweichang,kentonl,kristout
