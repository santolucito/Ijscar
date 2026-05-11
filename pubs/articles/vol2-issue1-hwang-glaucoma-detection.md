---
layout: default
title: "Comparative Analysis of Vision Transformer and ResNet50 for Glaucoma Detection: Balancing Performance and Efficiency"
description: "Eric Hwang — IJSCAR Vol. 2, Issue 1, 2025, pp. 3–8"
---

# Comparative Analysis of Vision Transformer and ResNet50 for Glaucoma Detection: Balancing Performance and Efficiency

Eric Hwang

**Affiliation:** Dulwich College Seoul

**IJSCAR** Vol. 2, Issue 1 (2025) &nbsp;·&nbsp; pp. 3–8

**DOI:** [10.5281/zenodo.15149831](https://doi.org/10.5281/zenodo.15149831)

---

## Abstract

This study develops and evaluates the performance and computational efficiency of ResNet50 (CNN-based architecture) and Vision Transformer (Transformer-based architecture) for detecting glaucoma from fundus photographs. Glaucoma is one of the leading causes of irreversible blindness that affects millions of people around the world. Using deep learning methods both models are trained to learn indicators of glaucomatous fundus photographs such as thinning of the retinal nerve fiber layer (RNFL) and nasalization of blood vessels to classify healthy and glaucomatous eyes. Gradient-weighted Class Activation Mapping (Grad-CAM) was used to interpret the model predictions by visualizing the regions of fundus photographs that contributed most significantly to the classification. With a publicly available dataset we fine-tuned both models by leveraging transfer learning with a small learning rate (0.0001) on pre-trained layers. Both models were assessed with metrics such as accuracy F1 score inference time throughput and maximum GPU memory usage under controlled conditions. ResNet50 outperformed ViT achieving higher accuracy (90.72% vs 87.64%) and an F1 score (0.9104 vs 0.8614) while being significantly more computationally efficient with 68.48% faster inference and 50.52% lower GPU usage. These findings highlight the suitability of ResNet50 over ViT for use in resource-constrained medical settings to assist ophthalmologists diagnosing patients as it effectively balances performance and efficiency.

---

**Keywords:** Artificial Intelligence, Computer Vision, Deep Learning, Neural Networks, Transfer Learning, Medical Imaging, Glaucoma Detection

---

[View Full Issue PDF](../vol2-issue1.pdf#page=3){: .button} &nbsp; [All Publications](../)
