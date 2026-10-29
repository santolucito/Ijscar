---
layout: default
title: "A Jet-Multiplicity Confound in Reconstruction-Based Anomaly Detection: Evidence from a Higgs-to-Tau-Pair Proxy Signal"
description: "Abhijay Arun — IJSCAR Vol. 3, Issue 4, 2026, pp. 72–87"
citation_authors:
  - "Arun, Abhijay"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 72
citation_lastpage: 87
citation_doi: "10.67149/yhjs2024.5/6uf9c50f"
citation_pdf: "/pubs/articles/vol3-issue4-arun-collider-anomaly-detection.pdf"
---

# A Jet-Multiplicity Confound in Reconstruction-Based Anomaly Detection: Evidence from a Higgs-to-Tau-Pair Proxy Signal

Abhijay Arun

**Affiliation:** GEMS Modern Academy, Nad Al Sheba, Dubai, United Arab Emirates

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 72–87

**DOI:** [10.67149/yhjs2024.5/6uf9c50f](vol3-issue4-arun-collider-anomaly-detection.pdf)

---

## Abstract

Unsupervised anomaly detectors trained on background events alone have been proposed for model-independent searches at the Large Hadron Collider. This study tests, for one proxy signal, whether a model that reconstructs the background better also detects an unseen signal better. Principal component analysis (PCA), an autoencoder (AE) and a variational autoencoder (VAE) with latent sizes from 2 to 16 are trained on simulated background events from the ATLAS Higgs Boson Machine Learning Challenge 2014 dataset, and their reconstruction error ranks Higgs boson decays to tau pairs, which are never used in training or tuning. Raw scores reach an area under the receiver operating characteristic curve (AUC) of 0.55 to 0.61, but the jet count alone, used as a score, reaches 0.59: signal events have more jets, and reconstruction error rises with jet count. Ranked only against background events with the same jet count, the AE and VAE fall to or below chance (mean AUC 0.47 to 0.50). Only PCA reconstruction with two or four components stays above chance, and its larger edge (1.61% of signal at a 1% false-positive rate, against 1% for chance) is reproduced on a held-out half of the signal. Below-chance scores trace back to signal taus and leptons being more central in pseudorapidity. Simple baselines, scores on the latent codes, a masked score and retraining without jet inputs leave the picture unchanged, and the detectors that catch independent feature shifts miss correlated energy-scale shifts. Better reconstruction never brought detection clearly above chance.

---

**Keywords:** Computer Science and Software Engineering, Machine Learning, Anomaly Detection, Autoencoders, Particle Physics

---

[View Full Issue PDF](../vol3-issue4.pdf#page=72){: .button} &nbsp; [All Publications](../)
