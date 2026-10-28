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
---

# Dynamic Mathematical PDE Modeling and Machine Learning for TANGO2 Identification and Crisis Prediction

Abhay Tippimath

**Affiliation:** McNeil High School, Austin, TX, USA

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 29–37



---

## Abstract

TANGO2 deficiency disorder (TDD) is a rare autosomal recessive condition marked by unpredictable, life threatening metabolic crises, including rhabdomyolysis, cardiac arrhythmias, and meta- bolic encephalopathy. Clinical outcomes depend heavily on early diagnosis, because patients receiving supportive treatment, particularly B complex vitamin supplementation together with fasting avoidance, experience substantially fewer and less severe crises than untreated individuals; undiagnosed patients therefore remain at the greatest risk, often suffering preventable and sometimes fatal crises before treatment begins. The computational contribution of this work is a two stage framework that couples supervised machine learning classification with numerical simulation of a stochastic partial differential equation: the first stage identifies TDD patients from their stable baseline presentation, and the second models future crisis behavior as a threshold crossing dynamical system. Using deidentified Human Phenotype Ontology (HPO) profiles from 90 molecularly confirmed TDD patients and 141 diagnosed control participants from the Undiagnosed Diseases Network (UDN), we exclude all 23 crisis defining phenotypes and restrict the primary analysis to the 30 HPO terms recorded by both annotating teams, so that classification depends only on information available before a crisis. A Random Forest classifier, evaluated by repeated stratified tenfold cross validation and compared against logistic regression and a support vector machine, attains an AUC of 0.993 ±0.002 (variance corrected 95% interval 0.980 to 1.000), 98.3% accuracy, 95.6% sensitivity, 100% specificity, and a Brier score of 0.017. A label permutation test (1,000 shuffles, 𝑝= 0.001) and stricter feature sets support this result, and performance declines only gradually under ablation (AUC 0.993 after removing the six most important features and 0.980 after removing eight), indicating a signal distributed across many correlated phenotypes rather than one driven by a few terms. Two phenotypes, paroxysmal lethargy and compensatory head posture, were recorded only in TDD patients; because the control annotating team never used these terms, they are re- ported as hypotheses that cannot yet be separated from annotation style. Separately, a stochastic reaction diffusion partial differential equation (PDE) with a patient specific source term, solved by an implicit explicit finite difference scheme, reproduces the episodic nature of metabolic crises and exhibits a critical source amplitude 𝛽∗= 0.01273 that partitions patients into stable and recurrent regimes. Simulations show that scalar models without diffusion cannot reproduce this behavior without recalibration, and that the patient specific parameter is recoverable from a single simulated timeline (𝑟 = 0.992). Together these results indicate that phenotypes present before any crisis carry sufficient information to identify TDD before life threatening events occur, while the PDE provides a mathematically grounded, testable hypothesis for how continuous metabolic risk produces discrete, episodic crises.

---

**Keywords:** TANGO2, rare disease, Random Forest, reaction diffusion equation, partial differential equations, Human Phenotype Ontology, crisis prediction, bioinformatics, machine learning

---

[View Full Issue PDF](../vol3-issue4.pdf#page=29){: .button} &nbsp; [All Publications](../)
