---
id: fef797f0
title: "Undatedai"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: raw/papers/c1984bb5_undatedai.pdf
domain: ["ai"]
tags: ["paper, ai"]
confidence: 0.65
summary: "Training language models to follow instructions。with human feedback。Long Ouyang∗。"
conflicts: []
versions: []
claims: [{"id": "c43ca0180", "text": "Training language models to follow instructions\nwith human feedback\nLong Ouyang∗\nJeff Wu∗\nXu Jiang∗\nDiogo Almeida∗\nCarroll L. Wainwright∗\nPamela Mishkin∗\nChong Zhang\nSandhini Agarwal\nKatarina Slama\nAlex Ray\nJohn Schulman\nJacob Hilton\nFraser Kelton\nLuke Miller\nMaddie Simens\nAmanda Askell†\nPeter Welinder\nPaul Christiano∗†\nJan Leike∗\nRyan Lowe∗\nOpenAI\nAbstract\nMaking language models bigger does not inherently make them better at following\na user’s intent. For example, large language models can gene", "para_index": 0, "entities": [], "domains": ["ai"], "type": "policy", "source": "/home/agentuser/temp/papers/instructgpt_instructions_following.pdf"}]
---

# Undatedai

## Summary
Training language models to follow instructions。with human feedback。Long Ouyang∗。

## Details
Training language models to follow instructions
with human feedback
Long Ouyang∗
Jeff Wu∗
Xu Jiang∗
Diogo Almeida∗
Carroll L. Wainwright∗
Pamela Mishkin∗
Chong Zhang
Sandhini Agarwal
Katarina Slama
Alex Ray
John Schulman
Jacob Hilton
Fraser Kelton
Luke Miller
Maddie Simens
Amanda Askell†
Peter Welinder
Paul Christiano∗†
Jan Leike∗
Ryan Lowe∗
OpenAI
Abstract
Making language models bigger does not inherently make them better at following
a user’s intent. For example, large language models can generate outputs that
are untruthful, toxic, or simply not helpful to the user. In other words, these
models are not aligned with their users. In this paper, we show an avenue for
aligning language models with user intent on a wide range of tasks by ﬁne-tuning
with human feedback. Starting with a set of labeler-written prompts and prompts
submitted through the OpenAI API, we collect a dataset of labeler demonstrations
of the desired model behavior, which we use to ﬁne-tune GPT-3 using supervised
learning. We then collect a dataset of rankings of model outputs, which we use to
further ﬁne-tune this supervised model using reinforcement learning from human
feedback. We call the resulting models InstructGPT. In human evaluations on
our prompt distribution, outputs from the 1.3B parameter InstructGPT model are
preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters.
Moreover, InstructGPT models show improvements in truthfulness and reductions
in toxic output generation while having minimal performance regressions on public
NLP datasets. Even though InstructGPT still makes simple mistakes, our results
show that ﬁne-tuning with human feedback is a promising direction for aligning
language models with human intent.
1
Introduction
Large language models (LMs) can be “prompted” to perform a range of natural language process-
ing (NLP) tasks, given some examples of the task as input. However, these models often express
unintended behaviors such as making up facts, gene

[... truncated ...]

in the body (such as the ﬁght-or-ﬂight response), as well as any biological predispositions you may have.
Lastly, environmental stressors that can contribute to anxiety can also impact the experience of anxiety
lumps.
Figure 50: Labeler-written prompt from our dataset, along with the human-written demonstration,
and completions from GPT-3 175B and InstructGPT175B. Prompt is lightly cherry-picked (5 selected
from 15 to show a diverse range of tasks), and the completions are not cherry-picked.
68


## Related
- Sources: [[../raw/papers/c1984bb5_undatedai.pdf]]

- Concepts: [[concept_ai]]

## Provenance
> [!source]| c43ca0180
> Training language models to follow instructions with human feedback Long Ouyang∗ Jeff Wu∗ Xu Jiang∗ Diogo Almeida∗ Carroll L. Wainwright∗ Pamela Mishkin∗ Chong Zhang Sandhini Agarwal Katarina Slama Al
