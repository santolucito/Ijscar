---
layout: default
title: "Evaluating the Causal Faithfulness of SHAP as a Candidate Attribution Method for SAE Features"
description: "Samuel Xie, Noura Al-Moubayed — IJSCAR Vol. 3, Issue 4, 2026, pp. 94–106"
citation_authors:
  - "Xie, Samuel"
  - "Al-Moubayed, Noura"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 94
citation_lastpage: 106
---

# Evaluating the Causal Faithfulness of SHAP as a Candidate Attribution Method for SAE Features

Samuel Xie, Noura Al-Moubayed

**Affiliation:** Seven Lakes High School, Katy, TX, USA

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 94–106



---

## Abstract

Sparse autoencoders (SAEs) decompose language model activations into interpretable features, but interpreting those features remains largely correlational. Attribution methods could estimate which features matter, yet it is unclear whether such estimates track causal effects on the model. We test this in a probe-mediated pipeline on GPT-2 Small and SST-2: we train linear and MLP probes on a layer-7 SAE, attribute probe outputs to features with SHapley Additive exPlanations (SHAP), Integrated Gradients (IG), and Gradient×Input, and score each attribution against the effect of ablating or steering that feature on the language model's logit difference. Because this combines attribution error with any mismatch between what the probe encodes and what the model uses, our results characterize the full pipeline rather than attribution alone. The three methods nearly coincide (and are analytically identical for linear probes), but this agreement does not indicate causal validity. Importance faithfulness survives multiple-comparison correction but is modest and no better than a simple background-free baseline, while directional faithfulness is near zero and nonsignificant. In the linear arm, probe-side controls trace the directional failure to centering attributions on a background mean. Local per-example attribution outranks global averaging on importance only in the MLP arm and only when inactive features are included; among active features we find no advantage. In minimal pairs with known ground truth, attribution does not recover changed features beyond what feature activity alone provides. Importance and directional faithfulness are separable properties that require separate evaluation, and agreement among attribution methods should not substitute for causal validation. Code is available at <https://github.com/froge79/shap-sae>.

---

**Keywords:** Sparse autoencoders, Mechanistic interpretability, Feature attribution, Faithfulness evaluation, Causal interventions, Shapley values

---

[View Full Issue PDF](../vol3-issue4.pdf#page=94){: .button} &nbsp; [All Publications](../)
