---
id: paper_resnet
title: "paper_resnet"
created: 2026-05-07
updated: 2026-05-07
type: entity-paper
source: arxiv:1512.03385
domain: ["ai"]
tags: ["paper", "ai"]
confidence: 0.95
summary: "Deep Residual Learning for Image Recognition - ResNet enables training of very deep neural networks through residual connections."
conflicts: []
versions: []
claims: [{"id": "cba85b68e", "text": "Deep Residual Learning for Image Recognition Kaiming He Xiangyu Zhang Shaoqing Ren Jian Sun Microsoft Research {kahe, v-xiangz, v-shren, jiansun}@microsoft.com Abstract Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers. The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.", "para_index": 0, "entities": [], "domains": ["ai"], "type": "fact", "source": "arxiv:1512.03385"}]
---

# paper_resnet

## Metadata

| Field | Value |
|-------|-------|
| arXiv ID | 1512.03385 |
| Title | Deep Residual Learning for Image Recognition |
| Authors | Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun |
| Year | 2015 |
| Published | 2015-12-10 |
| Categories | cs.CV |

## Summary

Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers—8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers. The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.

## Details

ResNet (Deep Residual Learning for Image Recognition) solved the degradation problem in deep neural networks:

- **Residual Connections**: Instead of learning the direct mapping H(x), learn the residual mapping F(x) = H(x) - x, which is easier to optimize
- **Shortcut Connections**: Identity mappings are added to the network to enable gradient flow through skip connections
- **Depth**: Enabled training of networks up to 152 layers (compared to typical 20-30 layer networks)
- **Performance**: Won ILSVRC 2015 with 3.57% error on ImageNet test set
- **Downstream Tasks**: Foundation for object detection and segmentation models, winning multiple categories in COCO challenges

ResNet's residual learning framework became a foundational architecture for computer vision and was later adapted for many other domains including NLP (with Transformers using similar concepts).

## Related

- Source: [[https://arxiv.org/abs/1512.03385]]
- PDF: [[https://arxiv.org/pdf/1512.03385]]

## Provenance

> [!source]| cba85b68e
> Deep Residual Learning for Image Recognition Kaiming He Xiangyu Zhang Shaoqing Ren Jian Sun Microsoft Research {kahe, v-xiangz, v-shren, jiansun}@microsoft.com Abstract Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.
