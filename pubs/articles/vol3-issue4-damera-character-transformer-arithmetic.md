---
layout: default
title: "Interpreting Character-Level Transformers for Addition and Multiplication Through Integrated Gradients"
description: "Abhinav Damera — IJSCAR Vol. 3, Issue 4, 2026, pp. 107–116"
citation_authors:
  - "Damera, Abhinav"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 107
citation_lastpage: 116
citation_doi: "10.67149/yhjs2024.5/88bi6k5z"
citation_pdf: "/pubs/articles/vol3-issue4-damera-character-transformer-arithmetic.pdf"
---

# Interpreting Character-Level Transformers for Addition and Multiplication Through Integrated Gradients

Abhinav Damera

**Affiliation:** Northern Burlington County Regional High School, Columbus, NJ, USA

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 107–116

**DOI:** [10.67149/yhjs2024.5/88bi6k5z](vol3-issue4-damera-character-transformer-arithmetic.pdf)

---

## Abstract

Transformer models have demonstrated strong performance across a variety of reasoning tasks. However, understanding how these models perform arithmetic reasoning remains an open challenge. This study focuses on investigating the factors that influence arithmetic performance and the interpretability of character-level transformer models. These models were trained on increasingly complex tasks including one-digit arithmetic, two-digit arithmetic, and natural language prompts containing arithmetic expressions embedded within them. Model performance was evaluated by examining the effects of altering training iterations, dataset size, and model configurations. In order to account for training variability, representative two-digit configurations were trained using five independent random seeds and evaluated using a standardized prompt-level procedure. In order to perform the interpretability analysis, Integrated Gradients was utilized to calculate token-level attribution for each input token across zero-embedding and mean-embedding baselines. The results show that model performance generally improved as training iterations, dataset size, and model configurations increased. Additionally, expanding the character vocabulary allowed the model to process natural language prompts containing arithmetic expressions while generally assigning lower attribution scores to contextual letters and whitespace than for arithmetic tokens. The findings show that the character-level transformer models achieved high accuracy on arithmetic expressions embedded within natural language, while attribution scores were generally higher for arithmetic tokens than for contextual letters and whitespace. This study examines factors associated with the performance of character-level transformer models and provides interpretability evidence of the internal features that contribute to model predictions.

---

**Keywords:** Transformer Models, Arithmetic Reasoning, Integrated Gradients, Explainable Artificial Intelligence, Interpretability

---

[View Full Issue PDF](../vol3-issue4.pdf#page=107){: .button} &nbsp; [All Publications](../)
