# MM_CFDRR-Net: Multi-Modal Residual Network for Efficient Reflection Removal Using Flash-Only Indices

This repository provides the official project page for the manuscript:
**"Multi-Modal Residual Network for Efficient Reflection Removal Using Flash-Only Indices"**
(submitted to *The Visual Computer*).

> **Release plan:**
> The experimental codebase and related data organization are still being curated and consolidated, and this repository will serve as the foundation for our subsequent research and continued development. At this stage, we provide documentation, environment setup guidance, evaluation utilities, and dataset access instructions. The complete code (including training and inference pipelines) will be uploaded in a future update once the release is finalized.

## Overview
MM_CFDRR-Net is a reflection removal framework that leverages **flash-only indices** as physically interpretable cues and uses a dual-map fusion design with attention and multi-scale residual modeling for robust reflection suppression under misalignment.

## Dataset
We use the public Flash-Only Reflection Removal (FOR) dataset from:
Lei, C., Chen, Q., "Robust Reflection Removal with Reflection-Free Flash-Only Cues", CVPR 2021.
DOI: https://doi.org/10.1109/CVPR46437.2021.01457

- Please follow the official FOR project page to download the dataset.
- See [data/README.md](data/README.md) for instructions and expected folder structure.

To setup a conda environment, test on demo data:
```
conda env create -f environment.yml
conda activate flashrr-rfc
bash download.sh
python test.py
```

## Setup

### Environment
This code is based on tensorflow. It has been tested on Ubuntu 18.04 LTS.

Anaconda is recommended: [Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-18-04)
| [Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04)

After installing Anaconda, you can setup the environment simply by

```
conda env create -f environment.yml
```

### Download checkpoint and VGG model

You can download the ckpt and VGG model by
```
bash download.sh
```

## Quick inference 
You can get the results for the demo data by:
```
python test.py
```

If you prepare your own dataset, note that each data sample must contains an ambient image and a flash-only iamge:
```
python test.py --testset /path/to/your/testset
```

## Training 
### Reproduce our results
First, download the dataset:
```
bash download_data.sh
```

Then, you can train a model by
```
python train.py
```
