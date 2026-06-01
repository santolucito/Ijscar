---
layout: default
title: "Entropy-Minimal Noise Schedules for Denoising Diffusion Probabilistic Models: A Non-Equilibrium Thermodynamics Approach"
description: "Tawhid Bin Omar — IJSCAR Vol. 3, Issue 2, 2026, pp. 10–15"
---

# Entropy-Minimal Noise Schedules for Denoising Diffusion Probabilistic Models: A Non-Equilibrium Thermodynamics Approach

Tawhid Bin Omar

**Affiliation:** St. Joseph Higher Secondary School

**IJSCAR** Vol. 3, Issue 2 (2026) &nbsp;·&nbsp; pp. 10–15

**DOI:** [10.67149/yhjs2024.5/k2v9p4cz](https://doi.org/10.67149/yhjs2024.5/k2v9p4cz)

---

## Abstract

Noise schedules in denoising diffusion probabilistic models (DDPMs) control how quickly information is destroyed during the forward Markov chain. Existing schedules -- linear cosine quadratic -- were designed by heuristic trial-and-error. We ask: what schedule is optimal for a fixed number of diffusion steps T? We answer this by framing the problem as minimizing the total discretization error of the forward process which is a sum of KL divergences between consecutive noise marginals. Using a Cauchy-Schwarz argument we prove that the unique minimizer is a geometric interpolation of the noise variance equivalently requiring log(1 - alpha_t) to be linear in t. We call this the Entropy-Minimal (EM) schedule as it is the discrete analog of the minimum entropy production principle from non-equilibrium thermodynamics. Experiments on a 2D Gaussian mixture show that the EM schedule achieves a coefficient of variation in per-step KL divergence of 0.03 more than 500x lower than any standard schedule and produces the best generative quality by both Maximum Mean Discrepancy (MMD = 0.0106) and Sliced Wasserstein Distance (SWD = 0.2118).

---

**Keywords:** diffusion models, noise schedule, entropy production, stochastic thermodynamics, generative models

---

[View Full Issue PDF](../vol3-issue2.pdf#page=10){: .button} &nbsp; [All Publications](../)
