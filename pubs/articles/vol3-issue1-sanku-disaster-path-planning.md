---
layout: default
title: "A Vision-Based Approach to Safe Void Detection and Path Planning in Post-Disaster Rubble Using Segment Anything Models"
description: "Abhiram Sanku — IJSCAR Vol. 3, Issue 1, 2026, pp. 31–36"
---

# A Vision-Based Approach to Safe Void Detection and Path Planning in Post-Disaster Rubble Using Segment Anything Models

Abhiram Sanku

**Affiliation:** John Champe High School

**IJSCAR** Vol. 3, Issue 1 (2026) &nbsp;·&nbsp; pp. 31–36

**DOI:** [10.5281/zenodo.18404630](https://doi.org/10.5281/zenodo.18404630)

---

## Abstract

In disaster-stricken environments such as collapsed buildings landslides or earthquake zones human-led search and rescue efforts are often impeded by unstable structures and limited visibility. This paper presents an AI-enhanced robotic navigation framework designed to autonomously identify and traverse structurally safe spaces within rubble piles. Our system integrates Geo-SAM a state-of-the-art segmentation model built on the Segment Anything Model (SAM) to detect safe and unsafe regions from overhead or robot-mounted images. A hybrid path planning module then applies four distinct algorithms A* RRT* Greedy Best-First Search and Lawnmower coverage to evaluate navigation efficiency and spatial coverage through identified safe zones. The A* and RRT* algorithms are used to optimize path efficiency and obstacle avoidance while the Greedy Best-First Search algorithm provides a heuristic-driven computationally lightweight alternative. The Lawnmower algorithm enables complete area coverage analysis for mapping and validation purposes. Each algorithm's results are overlaid onto the segmented imagery for visual verification and the shortest valid path is converted into robot-executable movement commands. Evaluation across multiple runs of the LADI-v2 disaster imagery dataset demonstrates the framework's robustness and flexibility showing consistent identification of traversable paths while minimizing exposure to hazardous zones. The model achieves 93.4% pixel-wise segmentation accuracy 89.7% safe/unsafe classification accuracy and IoU scores of 0.78 (safe) and 0.81 (unsafe). This work contributes to advancing autonomous navigation in complex unstructured environments and establishes a modular multi-algorithm foundation for scalable urban search-and-rescue robotics applications.

---

**Keywords:** Geo-SAM, Safe Void Detection, Path Planning, Disaster Robotics, A*, RRT*, LADI-v2

---

[View Full Issue PDF](../vol3-issue1.pdf#page=31){: .button} &nbsp; [All Publications](../)
