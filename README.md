# MM_CFDRR-Net: Multi-Modal Residual Network for Efficient Reflection Removal Using Flash-Only Indices

This repository provides the official project page for the manuscript:
**"Multi-Modal Residual Network for Efficient Reflection Removal Using Flash-Only Indices"**
(submitted to *The Visual Computer*).

> **Release plan (important):**
> To reduce potential risks before the manuscript is formally accepted, this repository is currently released as a **pre-acceptance skeleton**.
> We provide documentation, environment setup, evaluation tools, and dataset access instructions.
> The **full training/inference code and pretrained models** will be released **upon acceptance**.

## Overview
MM_CFDRR-Net is a reflection removal framework that leverages **flash-only indices** as physically interpretable cues and uses a dual-map fusion design with attention and multi-scale residual modeling for robust reflection suppression under misalignment.

## Dataset
We use the public Flash-Only Reflection Removal (FOR) dataset from:
Lei, C., Chen, Q., "Robust Reflection Removal with Reflection-Free Flash-Only Cues", CVPR 2021.
DOI: https://doi.org/10.1109/CVPR46437.2021.01457

- Please follow the official FOR project page to download the dataset.
- See [data/README.md](data/README.md) for instructions and expected folder structure.

## Environment
Tested with:
- Python >= 3.8
- PyTorch >= 2.0
- CUDA (optional, for training)

Install dependencies:
```bash
pip install -r requirements.txt
