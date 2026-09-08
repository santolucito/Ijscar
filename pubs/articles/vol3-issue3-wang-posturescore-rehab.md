---
layout: default
title: "PostureScore: An On-Device, Phase-Aware Scoring Pipeline for At-Home Rehabilitation"
description: "Ella Wang — IJSCAR Vol. 3, Issue 3, 2026, pp. 4–13"
---

# PostureScore: An On-Device, Phase-Aware Scoring Pipeline for At-Home Rehabilitation

Ella Wang

**Affiliation:** Emma Willard School

**IJSCAR** Vol. 3, Issue 3 (2026) &nbsp;·&nbsp; pp. 4–13

**DOI:** [10.67149/yhjs2024.5/17iljp8h](vol3-issue3-wang-posturescore-rehab.pdf)

---

## Abstract

After surgery many patients do their rehab exercises at home without knowing whether their form is correct. This project originated from the author’s own post-surgical rehabilitation (ACL reconstruction 2025; shoulder arthroscopy six months later) which surfaced three engineering gaps in existing tools. Smartphone pose models like MediaPipe Pose only output landmarks; the tools that wrap them typically use one fixed target angle regardless of rehabilitation week; and many upload video to a server which fellow patients met during rehabilitation were uncomfortable with. PostureScore is a prototype that addresses these three gaps in one mobile app. Its core is a scoring formula combining whether the patient holds the movement long enough and whether the movement is steady with targets that change by rehabilitation week (wider tolerance early narrower later). The privacy design sends no video at all; only session-summary numbers (total reps average score peak range of motion and similar) reach the backend. The pipeline was measured at 38.5 fps on iPhone 16 and 31.0 fps on iPhone 14 and deployed to seven post-surgical patients over an 8- to 12-week window. The system ran across all 664 sessions and produced consistent per-rep scores. The work is reported as an engineering feasibility check on the prototype. It does not provide evidence that PostureScore improves clinical outcomes.

---

**Keywords:** Human-centered computing, Ubiquitous and mobile computing, Applied computing, Consumer health, Computing methodologies (activity recognition and understanding)

---

[View Full Issue PDF](../vol3-issue3.pdf#page=4){: .button} &nbsp; [All Publications](../)
