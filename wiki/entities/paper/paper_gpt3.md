---
id: paper_gpt3
title: "paper_gpt3"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:2005.14165
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "Language Models are Few-Shot Learners - GPT-3 with 175 billion parameters demonstrates few-shot learning capabilities."
conflicts: []
versions: []
claims: [{"id": "cf69a88f3", "text": "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:2005.14165"}]
---

# paper_gpt3

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 2005.14165 |
| Title | Language Models are Few-Shot Learners |
| Authors | Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei |
| Year | 2020 |
| Published | 2020-05-28 |
| Categories | cs.CL |

## Summary

Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic.

## Details

GPT-3 (Generative Pre-trained Transformer 3) was a landmark paper in AI that demonstrated:

- **Scale**: 175 billion parameters, 10x larger than any previous non-sparse language model
- **Few-shot Learning**: Instead of fine-tuning, GPT-3 uses few-shot learning where tasks are specified via text prompts with a few examples
- **Broad Capabilities**: Achieved strong performance across diverse NLP tasks including translation, QA, and cloze tasks
- **Emergent Abilities**: Showed surprising capabilities like performing 3-digit arithmetic and learning from novel word definitions
- **Concerns**: Generated news articles indistinguishable from human-written ones, raising societal impact concerns

The paper showed that scaling language models dramatically improves few-shot performance, setting the stage for future large language models.

## Related

- Source: [[https://arxiv.org/abs/2005.14165]]
- PDF: [[https://arxiv.org/pdf/2005.14165]]

## Provenance

> [!source]| cf69a88f3
> Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do.
