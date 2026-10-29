---
layout: default
title: "Iterative Development of an AI Prototype for Dental Caries Detection and Localization with Informal Clinical Feedback"
description: "Chinmay Karthik Amancha — IJSCAR Vol. 3, Issue 4, 2026, pp. 88–93"
citation_authors:
  - "Amancha, Chinmay Karthik"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 88
citation_lastpage: 93
---

# Iterative Development of an AI Prototype for Dental Caries Detection and Localization with Informal Clinical Feedback

Chinmay Karthik Amancha

**Affiliation:** Chelmsford High School, Chelmsford, MA, USA

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 88–93



---

## Abstract

This paper documents the iterative development of a student-built dental caries detection prototype and compares its final version, V4.1, with the preceding V4 system and a fresh factory-default YOLO11n baseline, testing sensitivity to validation selection and reader choice. The final phase used 100 public permanent-dentition bitewing radiographs with annotations from eight dentists and a fixed 60/20/20 image split. V4.1 selected a two-model fusion from 75 validation configurations and was evaluated exploratorily on a previously viewed 20-image holdout. Against reader E0 on this holdout, V4.1 achieved precision 0.415, recall 0.449, F1 0.431, AP50 0.491, and 1.55 false-positive boxes per image; V4 achieved 0.412, 0.286, 0.337, 0.271, and 1.00, and the factory-default baseline achieved 0.750, 0.306, 0.435, 0.458, and 0.25. Only three of the 75 validation configurations were within 0.05 F1 of the winner, and at threshold 0.16 V4.1 F1 ranged from 0.140 to 0.448 across the eight reader references. A precision-oriented threshold of 0.37 reduced V4.1 false positives to 0.50 per image with recall 0.367, and a conditional three-fold out-of-fold stress test produced F1 0.538 and AP50 0.510. V4.1 thus improved recall and AP50 over both comparators, but its F1 was essentially the same as the factory-default baseline and it produced more false-positive boxes. Performance depended strongly on reader choice and threshold, and the small reused holdout, concentrated validation winner, non-nested cross-validation, and absence of patient identifiers prevent clinical or causal claims.

---

**Keywords:** Artificial intelligence, dental caries, bitewing radiography, YOLO, object detection, multi-reader evaluation, precision-recall

---

[View Full Issue PDF](../vol3-issue4.pdf#page=88){: .button} &nbsp; [All Publications](../)
