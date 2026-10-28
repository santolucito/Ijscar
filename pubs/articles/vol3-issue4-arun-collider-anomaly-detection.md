---
layout: default
title: "Evaluating Representation Learning for Model-Independent Anomaly Detection in High-Energy Particle Collisions"
description: "Abhijay Arun — IJSCAR Vol. 3, Issue 4, 2026, pp. 72–87"
citation_authors:
  - "Arun, Abhijay"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 72
citation_lastpage: 87
---

# Evaluating Representation Learning for Model-Independent Anomaly Detection in High-Energy Particle Collisions

Abhijay Arun

**Affiliation:** GEMS Modern Academy, Nad Al Sheba, Dubai, United Arab Emirates

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 72–87



---

## Abstract

Unsupervised anomaly detectors, trained on background events alone, have been proposed for model-independent collider searches. This study tests whether a model that represents the background better also detects an unseen signal better. Principal component analysis (PCA), an autoencoder (AE) and a variational autoencoder (VAE) with latent sizes from 2 to 16 are trained on simulated background events from the ATLAS Higgs Boson Machine Learning Challenge 2014 dataset. Their reconstruction error then ranks Higgs boson decays to tau pairs, a proxy signal never used in training or tuning. Raw scores appear to detect the signal, with an area under the receiver operating characteristic curve (AUC) of 0.55 to 0.61, but this comes mostly from jet multiplicity: signal events have more jets, and scores rise with jet count. When each score is ranked only against background events with the same jet count, the AE and VAE fall to or below chance (mean AUC 0.47 to 0.50), and only PCA with four components keeps a small edge (1.61% signal efficiency at a 1% false-positive rate, against 1% for chance). The same models detect synthetic feature shifts well, and linear probes find signal information in their latent codes that reconstruction error ignores.

---

**Keywords:** Computer Science and Software Engineering, Machine Learning, Anomaly Detection, Autoencoders, Particle Physics

---

[View Full Issue PDF](../vol3-issue4.pdf#page=72){: .button} &nbsp; [All Publications](../)
