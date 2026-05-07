---
id: 6e4e8f81
title: "Unknown"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: raw/papers/1e0651b6_unknown.pdf
domain: ["general"]
tags: ["paper, general"]
confidence: 0.65
summary: "Deep Residual Learning for Image Recognition。Xiangyu Zhang。Shaoqing Ren。"
conflicts: []
versions: []
claims: [{"id": "cba85b68e", "text": "Deep Residual Learning for Image Recognition\nKaiming He\nXiangyu Zhang\nShaoqing Ren\nJian Sun\nMicrosoft Research\n{kahe, v-xiangz, v-shren, jiansun}@microsoft.com\nAbstract\nDeeper neural networks are more difﬁcult to train. We\npresent a residual learning framework to ease the training\nof networks that are substantially deeper than those used\npreviously. We explicitly reformulate the layers as learn-\ning residual functions with reference to the layer inputs, in-\nstead of learning unreferenced functio", "para_index": 0, "entities": [], "domains": ["ai"], "type": "policy", "source": "/home/agentuser/temp/papers/resnet_deep_residual_learning.pdf"}]
---

# Unknown

## Summary
Deep Residual Learning for Image Recognition。Xiangyu Zhang。Shaoqing Ren。

## Details
Deep Residual Learning for Image Recognition
Kaiming He
Xiangyu Zhang
Shaoqing Ren
Jian Sun
Microsoft Research
{kahe, v-xiangz, v-shren, jiansun}@microsoft.com
Abstract
Deeper neural networks are more difﬁcult to train. We
present a residual learning framework to ease the training
of networks that are substantially deeper than those used
previously. We explicitly reformulate the layers as learn-
ing residual functions with reference to the layer inputs, in-
stead of learning unreferenced functions. We provide com-
prehensive empirical evidence showing that these residual
networks are easier to optimize, and can gain accuracy from
considerably increased depth. On the ImageNet dataset we
evaluate residual nets with a depth of up to 152 layers—8×
deeper than VGG nets [41] but still having lower complex-
ity. An ensemble of these residual nets achieves 3.57% error
on the ImageNet test set. This result won the 1st place on the
ILSVRC 2015 classiﬁcation task. We also present analysis
on CIFAR-10 with 100 and 1000 layers.
The depth of representations is of central importance
for many visual recognition tasks. Solely due to our ex-
tremely deep representations, we obtain a 28% relative im-
provement on the COCO object detection dataset. Deep
residual nets are foundations of our submissions to ILSVRC
& COCO 2015 competitions1, where we also won the 1st
places on the tasks of ImageNet detection, ImageNet local-
ization, COCO detection, and COCO segmentation.
1. Introduction
Deep convolutional neural networks [22, 21] have led
to a series of breakthroughs for image classiﬁcation [21,
50, 40]. Deep networks naturally integrate low/mid/high-
level features [50] and classiﬁers in an end-to-end multi-
layer fashion, and the “levels” of features can be enriched
by the number of stacked layers (depth). Recent evidence
[41, 44] reveals that network depth is of crucial importance,
and the leading results [41, 44, 13, 16] on the challenging
ImageNet dataset [36] all exploit “very deep”

[... truncated ...]

se proposals’ scores and box positions.
This method reduces the top-5 localization error to
10.6% (Table 13). This is our single-model result on the
validation set. Using an ensemble of networks for both clas-
siﬁcation and localization, we achieve a top-5 localization
error of 9.0% on the test set. This number signiﬁcantly out-
performs the ILSVRC 14 results (Table 14), showing a 64%
relative reduction of error. This result won the 1st place in
the ImageNet localization task in ILSVRC 2015.
12


## Related
- Sources: [[../raw/papers/1e0651b6_unknown.pdf]]



## Provenance
> [!source]| cba85b68e
> Deep Residual Learning for Image Recognition Kaiming He Xiangyu Zhang Shaoqing Ren Jian Sun Microsoft Research {kahe, v-xiangz, v-shren, jiansun}@microsoft.com Abstract Deeper neural networks are more
