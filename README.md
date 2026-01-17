# Consensus Formation under Distorted Deliberation

## Overview

This project studies *consensus formation* in a system of interacting agents using an agent-based opinion dynamics model.  The focus is on how **different interaction distortions affect the emergence, speed, and stability of consensus**. It examines how opinions evolve through repeated local interactions under varying deliberative conditions.

---

## Research Objective

The main objective of this study is to analyze:

- How consensus emerges in a deliberative system
- How emotional disturbances and social conformity influence:
  - time to consensus
  - opinion fragmentation
  - stability of consensus after perturbation

Consensus is treated as a *system-level outcome*, not as a correct or optimal opinion.

---

## Model Scope

### Included
- Continuous opinion dynamics
- Bounded confidence interaction
- Emotional noise in opinion updates
- Social conformity (consensus pressure)
- Network-based agent interactions

### Excluded
- Demographic or identity-based attributes
- Electoral choice (voting) prediction 
- Political, candidates parties, or ideological classification
- Artificial intelligence or machine learning

---

## Agent Description

Each agent represents an anonymous individual participating in public discourse.

Agents have:
- a continuous opinion value
- internal parameters affecting how they update opinions
- no social, demographic, or political identity

All observed behaviors emerge from interaction rules and system parameters.

---

## Project Structure

```text
consensus-formation/
├── config/        # Parameter settings
├── src/           # Core model implementation
├── experiments/   # Experiment scripts
├── results/       # Simulation outputs and figures
├── analysis/      # Data analysis and plotting
└── paper/         # Draft sections of the paper
```

---

## Methodological Approach 
- Agent-based simulation
- Repeated local interactions on a network
- Parameterized opinion update rules
- Multiple simulation runs for robustness
- Evaluation using system-level metrics (variance, clusters, stability)

--- 

## Intended Use 
This repository is intended as:
- a research prototype
- a methodological reference for opinion dynamics
- a reproducible simulation framework for consensus studies

It is *not* intended for prediction or normative evaluation.

--- 

## Status

This project is under active development. Model design and scope are intentionally kept minimal to ensure clarity and reproducibility.

--- 

## License
This project is for academic and research purposes.
