---
id: a1ec90f9
title: "Undatedai"
created: 2026-05-07
updated: 2026-05-07
type: entity-event
source: raw/papers/2e663675_undatedai.pdf
domain: ["ai"]
tags: ["event, ai"]
confidence: 0.8
summary: "LLaMA: Open and Efﬁcient Foundation Language Models。Hugo Touvron∗, Thibaut Lavril∗, Gautier Izacard∗, Xavier Martinet。Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal。"
conflicts: []
versions: []
claims: [{"id": "c0dff5952", "text": "LLaMA: Open and Efﬁcient Foundation Language Models\nHugo Touvron∗, Thibaut Lavril∗, Gautier Izacard∗, Xavier Martinet\nMarie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal\nEric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin\nEdouard Grave∗, Guillaume Lample∗\nMeta AI\nAbstract\nWe introduce LLaMA, a collection of founda-\ntion language models ranging from 7B to 65B\nparameters. We train our models on trillions\nof tokens, and show that it is possible to train\nstate-of-the-art mod", "para_index": 0, "entities": [], "domains": ["ai"], "type": "policy", "source": "/home/agentuser/temp/papers/llama_open_efficient_foundation.pdf"}]
---

# Undatedai

## Summary
LLaMA: Open and Efﬁcient Foundation Language Models。Hugo Touvron∗, Thibaut Lavril∗, Gautier Izacard∗, Xavier Martinet。Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal。

## Details
LLaMA: Open and Efﬁcient Foundation Language Models
Hugo Touvron∗, Thibaut Lavril∗, Gautier Izacard∗, Xavier Martinet
Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal
Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin
Edouard Grave∗, Guillaume Lample∗
Meta AI
Abstract
We introduce LLaMA, a collection of founda-
tion language models ranging from 7B to 65B
parameters. We train our models on trillions
of tokens, and show that it is possible to train
state-of-the-art models using publicly avail-
able datasets exclusively, without resorting
to proprietary and inaccessible datasets.
In
particular, LLaMA-13B outperforms GPT-3
(175B) on most benchmarks, and LLaMA-
65B is competitive with the best models,
Chinchilla-70B and PaLM-540B. We release
all our models to the research community1.
1
Introduction
Large Languages Models (LLMs) trained on mas-
sive corpora of texts have shown their ability to per-
form new tasks from textual instructions or from a
few examples (Brown et al., 2020). These few-shot
properties ﬁrst appeared when scaling models to a
sufﬁcient size (Kaplan et al., 2020), resulting in a
line of work that focuses on further scaling these
models (Chowdhery et al., 2022; Rae et al., 2021).
These efforts are based on the assumption that
more parameters will lead to better performance.
However, recent work from Hoffmann et al. (2022)
shows that, for a given compute budget, the best
performances are not achieved by the largest mod-
els, but by smaller models trained on more data.
The objective of the scaling laws from Hoff-
mann et al. (2022) is to determine how to best
scale the dataset and model sizes for a particular
training compute budget. However, this objective
disregards the inference budget, which becomes
critical when serving a language model at scale.
In this context, given a target level of performance,
the preferred model is not the fastest to train but the
fastest at inference, and although it may be cheaper
to train a larg

[... truncated ...]

output:
/home/human
Is this helpful?
ls -l
Here’s the output:
-rw-r–r– 1 human human 8 Sep 10 10:56 ﬁle.txt
Is this helpful?
cp ﬁle.txt ﬁle2.txt && ls -l
Here’s the output:
-rw-r–r– 1 human human 8 Sep 10 10:56 ﬁle.txt
-rw-r–r– 1 human human 8 Sep 10 10:56 ﬁle2.txt
Is this helpful?
rm ﬁle.txt && ls -l
Here’s the output:
-rw-r–r– 1 human human 0 Sep 10 10:56 ﬁle2.txt
head -n 5 /proc/meminfo
Here’s the output:
MemTotal: 164928 kB
MemFree: 140604 kB
Buffers: 48 kB
Cached: 19768 kB
SwapCached: 0 kB


## Related
- Sources: [[../raw/papers/2e663675_undatedai.pdf]]

- Concepts: [[concept_ai]]

## Provenance
> [!source]| c0dff5952
> LLaMA: Open and Efﬁcient Foundation Language Models Hugo Touvron∗, Thibaut Lavril∗, Gautier Izacard∗, Xavier Martinet Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal Eric Hambro, F
