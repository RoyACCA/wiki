---
id: paper_instructgpt
title: "paper_instructgpt"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:2203.02155
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "Training language models to follow instructions with human feedback - InstructGPT uses RLHF to align language models with user intent."
conflicts: []
versions: []
claims: [{"id": "c43ca0180", "text": "Training language models to follow instructions with human feedback Long Ouyang Jeff Wu Xu Jiang Diogo Almeida Carroll L. Wainwright Pamela Mishkin Chong Zhang Sandhini Agarwal Katarina Slama Alex Ray John Schulman Jacob Hilton Fraser Kelton Luke Miller Maddie Simens Amanda Askell Peter Welinder Paul Christiano Jan Leike Ryan Lowe OpenAI Abstract Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:2203.02155"}]
---

# paper_instructgpt

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 2203.02155 |
| Title | Training language models to follow instructions with human feedback |
| Authors | Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe |
| Year | 2022 |
| Published | 2022-03-04 |
| Categories | cs.CL, cs.AI, cs.LG |

## Summary

Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

## Details

InstructGPT introduced Reinforcement Learning from Human Feedback (RLHF) for aligning language models:

- **Problem**: Larger models don't automatically follow user intent; they can be unhelpful, untruthful, or harmful
- **Supervised Fine-tuning (SFT)**: Fine-tune GPT-3 on labeler demonstrations of desired behavior
- **Reward Model**: Train a reward model on human rankings of model outputs
- **Reinforcement Learning**: Use RL (PPO algorithm) to optimize against the reward model
- **Results**: 1.3B InstructGPT preferred over 175B GPT-3 by humans, despite 100x fewer parameters
- **Improvements**: Better truthfulness, less toxicity, minimal regression on other NLP tasks

InstructGPT's RLHF approach became the foundation for ChatGPT and subsequent对齐 research, making AI assistants more helpful and safe.

## Related

- Source: [[https://arxiv.org/abs/2203.02155]]
- PDF: [[https://arxiv.org/pdf/2203.02155]]

## Provenance

> [!source]| c43ca0180
> Training language models to follow instructions with human feedback Long Ouyang Jeff Wu Xu Jiang Diogo Almeida Carroll L. Wainwright Pamela Mishkin Chong Zhang Sandhini Agarwal Katarina Slama Alex Ray John Schulman Jacob Hilton Fraser Kelton Luke Miller Maddie Simens Amanda Askell Peter Welinder Paul Christiano Jan Leike Ryan Lowe OpenAI Abstract Making language models bigger does not inherently make them better at following a user's intent.
