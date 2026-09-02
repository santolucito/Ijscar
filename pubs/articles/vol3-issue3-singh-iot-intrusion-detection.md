---
layout: default
title: "A Five-Run Comparison of Lightweight Machine Learning Models for IoT Intrusion Detection"
description: "Pradyumn Singh, Russ Alizadeh — IJSCAR Vol. 3, Issue 3, 2026, pp. –"
---

# A Five-Run Comparison of Lightweight Machine Learning Models for IoT Intrusion Detection

Pradyumn Singh, Russ Alizadeh

**Affiliation:** John F. Kennedy High School

**IJSCAR** Vol. 3, Issue 3 (2026) &nbsp;·&nbsp; pp. –

**DOI:** [10.67149/yhjs2024.5/br0qqg04](https://doi.org/10.67149/yhjs2024.5/br0qqg04)

---

## Abstract

IoT intrusion-detection models are useful only if they detect attacks without becoming too costly to run. We compared Logistic Regression Decision Tree Random Forest and XGBoost on binary CICIoT2023 intrusion detection using a cleaned file with 21005260 rows and 37 numeric features. The main experiment used five attack-resampling balanced outer runs: each outer run reused all 1047367 benign records and sampled an equal number of attack records followed by five inner train-validation-test splits. XGBoost had the highest default-threshold F1-score in the main experiment (0.983109 ± 0.000205) followed by Decision Tree (0.982860 ± 0.000257) Random Forest (0.982237 ± 0.000371) and Logistic Regression (0.974215 ± 0.000272). Because the main outer runs share the benign records we interpret the paired tests as evidence from repeated attack resampling rather than as five fully independent datasets. To address this limitation we added a disjoint sensitivity analysis in which both benign and attack rows were resampled into non-overlapping 100000-per-class outer subsets. The same general pattern remained: XGBoost reached 0.982572 ± 0.000612 F1 while Logistic Regression reached 0.974407 ± 0.000920. A feature-ablation check dropping Number and HTTPS caused only small F1 decreases and did not change the main ordering. Per-record inference latency on the main balanced test split ranged from 0.615 μs for Logistic Regression to 1.124 μs for Random Forest with XGBoost at 0.647 μs. Overall the results support tree-based models for this controlled binary benchmark while also showing why latency footprint and dataset-specific shortcuts must be considered before making deployment claims.

---

**Keywords:** IoT security, cybersecurity, intrusion detection, machine learning, XGBoost

---

[View Full Issue PDF](../vol3-issue3.pdf#page=){: .button} &nbsp; [All Publications](../)
