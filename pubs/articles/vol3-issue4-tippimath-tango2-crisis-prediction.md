---
layout: default
title: "Dynamic Mathematical PDE Modeling and Machine Learning for TANGO2 Identification and Crisis Prediction"
description: "Abhay Tippimath — IJSCAR Vol. 3, Issue 4, 2026, pp. 29–37"
citation_authors:
  - "Tippimath, Abhay"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 29
citation_lastpage: 37
citation_pdf: "/pubs/articles/vol3-issue4-tippimath-tango2-crisis-prediction.pdf"
---

# Dynamic Mathematical PDE Modeling and Machine Learning for TANGO2 Identification and Crisis Prediction

Abhay Tippimath

**Affiliation:** McNeil High School, Austin, TX, USA

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 29–37



---

## Abstract

TANGO2 (Transport And Golgi Organization 2) deficiency disorder (TDD) is a rare autosomal recessive condition marked by unpredictable, life-threatening metabolic crises, including rhabdomyolysis, cardiac arrhythmias, and metabolic encephalopathy. Supportive treatment, particularly B-complex vitamin supplementation and fasting avoidance, substantially reduces the frequency and severity of crises, so undiagnosed patients remain at the greatest risk. This work presents a two-stage framework that couples supervised machine learning classification with numerical simulation of a stochastic partial differential equation (PDE). The first stage identifies TDD patients from their stable baseline presentation, and the second models future crisis behavior as a threshold-crossing dynamical system. Using deidentified Human Phenotype Ontology (HPO) profiles from 90 molecularly confirmed TDD patients and 141 diagnosed Undiagnosed Diseases Network (UDN) controls, we exclude all 23 crisis-defining phenotypes and restrict the primary analysis to the 30 HPO terms recorded by both annotating teams, so that classification depends only on information available before a crisis. A Random Forest classifier, evaluated by repeated stratified tenfold cross-validation, attains an AUC of 0.993 (variance-corrected 95% interval 0.980 to 1.000), with 95.6% sensitivity and 100% specificity. The result withstands a label permutation test (p = 0.001), stricter feature sets, and ablation of the most important features, indicating a signal distributed across many correlated phenotypes. Two phenotypes, paroxysmal lethargy and compensatory head posture, were recorded only in TDD patients; because the control annotating team never used these terms, they are reported as hypotheses that cannot yet be separated from annotation style. Separately, a stochastic reaction-diffusion PDE with a patient-specific source term reproduces the episodic nature of metabolic crises and exhibits a critical source amplitude that partitions patients into stable and recurrent regimes. Scalar models without diffusion cannot reproduce this behavior without recalibration, and the patient-specific parameter is recoverable from a single simulated timeline (r = 0.992). Together, these results indicate that phenotypes present before any crisis can identify TDD before life-threatening events occur, while the PDE offers a testable hypothesis for how continuous metabolic risk produces discrete, episodic crises.

---

**Keywords:** TANGO2, rare disease, Random Forest, reaction diffusion equation, partial differential equations, Human Phenotype Ontology, crisis prediction, bioinformatics, machine learning

---

[View Full Issue PDF](../vol3-issue4.pdf#page=29){: .button} &nbsp; [All Publications](../)
