# Federated X-ray Classifier

## Highlights

- Privacy-preserving training using Federated Learning
- Classifies X-ray scans as Normal or Abnormal
- No need to share patient data across hospitals
- Built with EfficientNet-B0 using transfer learning
- Achieved 84.51% accuracy across 3 nodes

## Overview

This project simulates a real-world healthcare scenario where hospitals collaboratively train an X-ray classification model without ever sharing sensitive patient data.
We used Federated Learning to train a neural network across three virtual hospital nodes on the MURA dataset, with added encryption during weight sharing to enhance security.

### Authors

Saad Naseer Mahfood

Firas Obieda Ali Abu-Bader

Majid Mohamed Almheiri

Ali Hamzeh Johar

## Installation
```bash
git clone https://github.com/shimT20/federated-xray-classifier.git
cd federated-xray-classifier
```

```bash
pip install -r requirements.txt
```
Requires Python 3.7+ and compatible with Linux/Windows/Mac.
