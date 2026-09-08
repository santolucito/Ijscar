---
layout: default
title: "A Reproducible Computational Pipeline for Modelling Sequential Decision Thresholds from Stopping-Rule Data"
description: "Alex Kolesnikov — IJSCAR Vol. 3, Issue 3, 2026, pp. 14–20"
---

# A Reproducible Computational Pipeline for Modelling Sequential Decision Thresholds from Stopping-Rule Data

Alex Kolesnikov

**Affiliation:** Eton College

**IJSCAR** Vol. 3, Issue 3 (2026) &nbsp;·&nbsp; pp. 14–20

**DOI:** [10.67149/yhjs2024.5/3s7gdh1q](https://doi.org/10.67149/yhjs2024.5/3s7gdh1q)

---

## Abstract

Stopping-rule experiments ask participants to move through ordered stages until they decide to act. These designs are useful for studying intervention thresholds but raw survey exports are usually stored in wide form while correct modelling requires scenario-level thresholds and stage-level at-risk rows. This paper presents a runnable R artifact for reconstructing and validating stopping-rule data. The artifact uses a JSON configuration layer modular R source files toy data a second structurally different toy configuration automated testthat tests adversarial validation checks reference outputs licensing and citation metadata. In a de-identified sequential risk-decision case study the same reconstruction logic maps 1108 potential scenario observations from 277 consenting participants flags 25 ambiguous response sequences retains 1083 clean scenario-level observations and generates 3047 stage-level at-risk rows. The evaluation documents local execution automated test coverage end-to-end preprocessing behaviour a second configuration demonstration adversarial failure behaviour and expected linear scaling for larger survey exports. The contribution is a reproducible data-engineering system that bridges raw stopping-rule survey exports and standard event-history or repeated-measures modelling tools while making exclusion decisions auditable rather than hidden in manual recoding.

---

**Keywords:** Stopping-Rule Data; Sequential Decision-Making; Computational Pipeline; R Software; Reproducibility; Data Validation; Data Engineering; Discrete-Time Hazard Models; Right-Censoring; Decision-Support Systems

---

[View Full Issue PDF](../vol3-issue3.pdf#page=14){: .button} &nbsp; [All Publications](../)
