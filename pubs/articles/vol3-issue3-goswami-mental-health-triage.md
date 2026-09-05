---
layout: default
title: "Precision versus Efficiency: A Quantized DistilBERT Framework for Automated Mental Health Text Triage"
description: "Ayaan Goswami, Clayton Greenberg — IJSCAR Vol. 3, Issue 3, 2026, pp. 21–35"
---

# Precision versus Efficiency: A Quantized DistilBERT Framework for Automated Mental Health Text Triage

Ayaan Goswami, Clayton Greenberg

**Affiliation:** Carnegie Vanguard High School

**IJSCAR** Vol. 3, Issue 3 (2026) &nbsp;·&nbsp; pp. 21–35

**DOI:** [10.67149/yhjs2024.5/5wcbbc4m](https://doi.org/10.67149/yhjs2024.5/5wcbbc4m)

---

## Abstract

This study addresses the challenge of automatically triaging online mental health data by engineering a text-analysis system capable of accurately and efficiently categorizing human psychological distress in a lightweight web-deployable format. As more people turn to social media and other online platforms when experiencing psychological distress for both interaction with others and to seek support the volume of such disclosure increasingly outpaces the capacity of moderators and clinicians to review it forming a bottleneck to accurate and efficient triaging. To overcome the bottleneck this study proposes an automated classification system deployed as a web application where users submit text directly. Within this approach an optimization framework was utilized targeting the classification head encoder inference runtime and numeric precision of a bidirectional deep learning transformer (BERT). Because inference cost is dominated by the encoder rather than the classifier optimizing the classification head yielded no speedup so the encoder itself was replaced with a distilled model and quantized. The final framework was able to successfully categorize raw user text into seven different psychological states at an overall accuracy of about 82% on unseen test data. Additionally the distilled and quantized model measurably reduced response time lowering latency from 186.4 to 43.8 ms and model size from 438.7 to 68.3 MB with per-class performance reported for every configuration. The result quantifies what each optimization costs: the runtime change is numerically lossless but contributes under 10% of the speedup distillation and quantization supply the rest and quantization damages the smallest classes severely for one encoder while leaving the other’s per-class F1 intact. The deployed system is offered as a research prototype for prioritizing human review of written text not as a diagnostic or standalone screening tool.

---

**Keywords:** Natural Language Processing, Text Classification, Mental Health Triage, Machine Learning, BERT, Optimization, Sentiment Analysis

---

[View Full Issue PDF](../vol3-issue3.pdf#page=21){: .button} &nbsp; [All Publications](../)
