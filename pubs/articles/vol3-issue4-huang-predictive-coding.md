---
layout: default
title: "Comparing the Sample and Computational Efficiency of Unit-Precision Predictive Coding and Backpropagation"
description: "Austin Huang — IJSCAR Vol. 3, Issue 4, 2026, pp. 4–15"
citation_authors:
  - "Huang, Austin"
citation_year: 2026
citation_volume: 3
citation_issue: 4
citation_firstpage: 4
citation_lastpage: 15
---

# Comparing the Sample and Computational Efficiency of Unit-Precision Predictive Coding and Backpropagation

Austin Huang

**Affiliation:** Eton College, Windsor, Berkshire, United Kingdom

**IJSCAR** Vol. 3, Issue 4 (2026) &nbsp;·&nbsp; pp. 4–15



---

## Abstract

Synchronous unit-precision predictive coding (PC) replaces back-propagation’s (BP’s) immediate backward pass with recurrent activity inference. We compared PC with objective- and optimizer-matched BP in tanh multilayer perceptrons on MNIST and Fashion-MNIST. In the depth-2 network trained on 100 labelled MNIST examples, each method’s learning rate was selected independently using validation data, and both searches met the prespecified bracketing rule. With 200 inference steps, PC came close to BP’s accuracy but remained lower. Across ten fresh paired seeds, the mean epoch-30 PC-minus-BP test-accuracy difference was −0.295 percentage points (95% paired-bootstrap interval [−0.376, −0.181]). PC nevertheless required substantially more computation. Diagnostic-free float32 training took 130.6 times as long as BP on a single CPU thread, while analytical counts gave approximately 113 times as many MACs, 112 times as many FLOPs, and 403 times as many tanh evaluations. The depth-2, 500-label Fashion-MNIST comparison remained unresolved because the BP learning-rate search did not show the required numerically valid decline at a higher rate; its result is therefore descriptive. These findings apply only to the tested synchronous unit-precision formulation, datasets, architecture, and digital CPU implementation, not to all predictive-coding variants or hardware.

---

**Keywords:** predictive coding, backpropagation, sample efficiency, computational efficiency, iterative inference, implementation validation

---

[View Full Issue PDF](../vol3-issue4.pdf#page=4){: .button} &nbsp; [All Publications](../)
