---
layout: default
title: "Investigating the Efficacy of the Gemini 2.5 Pro Model in the Estimation of Macronutrient Content"
description: "Sonali Guttikonda, Junyao Chen, He Tu, Zhengyuan Zhou — IJSCAR Vol. 3, Issue 4, 2026, pp. 38–43"
citation_authors:
  - "Guttikonda, Sonali"
  - "Chen, Junyao"
  - "Tu, He"
  - "Zhou, Zhengyuan"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 38
citation_lastpage: 43
---

# Investigating the Efficacy of the Gemini 2.5 Pro Model in the Estimation of Macronutrient Content

Sonali Guttikonda, Junyao Chen, He Tu, Zhengyuan Zhou

**Affiliation:** University High School, Carmel, IN, USA

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 38–43



---

## Abstract

Health guidance is a topic that has been gaining increasing traction in the past few years. Specifically, apps utilizing AI to provide health guidance and allow users to track macronutrient content have been gaining prevalence in recent research. However, current apps require users to manually input all information into the app. Therefore, this work seeks to evaluate the effectiveness of the Gemini 2.5 Pro model, a multimodal large language model (LLM), in analyzing the macronutrient content (i.e., proteins, fats, and carbohydrates) in food images. We tested 100 dishes randomly sampled from the Nutrition5k dataset. Each image was queried three times with three different prompt phrasings and the estimated values were compared with the ground truth values in the dataset. For the baseline prompt, the mean absolute error (MAE) was 4.1 g for protein, 3.6 g for fat, and 6.1 g for carbohydrates, and the median absolute percentage errors were 29.9%, 29.2%, and 32.1% respectively. The mean absolute percentage error (MAPE) was 38.5% for protein but 211.2% for fats and 442.7% for carbohydrates, which were inflated due to a small number of dishes containing less than 0.5 g of fat or carbohydrate, where errors of a few grams produced errors in the thousands. Without dishes with less than 2 g of the nutrient, the MAPE was 38.5%, 33.6%, and 33.5%. On metrics not sensitive to near-zero values, error was of similar size across the three macronutrients, and protein was underestimated on average, with the largest errors concentrated in a subset of dishes. MAE differed by at most 0.6 g across prompt wordings, although fat MdAPE was higher under both alternative prompts. Because no confidence intervals or significance tests were computed, these are observations from a single 100-dish sample rather than established differences. Additionally, the 100 dishes selected for the study came from a 400-dish subset whose selection cannot be reproduced.

---

**Keywords:** Multimodal Large Language Models, Gemini 2.5 Pro, Macronutrient Estimation, Food Image Analysis, Nutrition5k, Prompt Engineering

---

[View Full Issue PDF](../vol3-issue4.pdf#page=38){: .button} &nbsp; [All Publications](../)
