# 🛣️ CNN-based Traffic Speed Prediction in Seoul

This project implements and evaluates a Convolutional Neural Network (CNN) for short-term traffic speed prediction in Seoul.

Inspired by *"Learning Traffic as Images: A Deep Convolutional Neural Network for Large-Scale Transportation Network Speed Prediction"*, this work adapts the original framework to Seoul’s urban road network, focusing on both central and downtown regions.

The study reproduces and evaluates the four experimental settings proposed in the paper:

- **Task 1:** 10-minute prediction using past 30-minute traffic speeds  
- **Task 2:** 10-minute prediction using past 40-minute traffic speeds  
- **Task 3:** 20-minute prediction using past 30-minute traffic speeds  
- **Task 4:** 20-minute prediction using past 40-minute traffic speeds  

---

## 🎯 Objectives

- Transform spatio-temporal traffic data into 2D image-like representations for CNN input  
- Learn spatial and temporal dependencies for traffic speed prediction  
- Analyze the effect of CNN depth on performance (4 model variants)  
- Compare CNN models against a Multilayer Perceptron (MLP) baseline  

---

## 🧪 Project Overview

- **Data Source:** Seoul Open Data Plaza (TOPIS traffic speed data, April 2018)  
- **Prediction Target:** Link-level traffic speeds for 10- and 20-minute horizons in urban road networks  
- **Tech Stack:** Python, PyTorch, NumPy, Pandas, Matplotlib, Seaborn  

### Model Architectures

- **MLP (Fully Connected Network):** baseline model  
- **2D CNN Models:** 2–4 convolutional layers (Depth 2 to Depth 4)  
- **Input:** Spatio-temporal traffic matrices converted into 2D image-like tensors using past 30- and 40-minute windows  
- **Output:** Future traffic speed prediction (10-minute and 20-minute horizons)  

---

## 📐 Differences from the Original Paper

### Study Domain
- Original: Beijing road network  
- This study: Seoul urban road network  

### Baseline Models
- Original: OLS, Random Forest, ANN, and other ML/statistical models  
- This study: Multilayer Perceptron (MLP) as the primary baseline  

### Evaluation Metrics
- Original: MSE, MAE, scaled MSE, scaled MAE  
- This study: MSE and MAE, additionally reported in original scale for interpretability  

**Rationale:**  
Although MSE on normalized data is useful for optimization, MAE and inverse-scaled metrics provide more interpretable performance comparisons.

### Hyperparameters
- Original: limited hyperparameter tuning (mainly early stopping)  
- This study: extended configuration including:
  - hidden dimension (`hid_dim`)  
  - L2 regularization  
  - batch normalization (`use_bn`)  
  - dropout  
  - learning rate (`lr`)  
  - learning rate scheduler  
  - early stopping  

**Rationale:**
- `hid_dim`: improves model capacity  
- Regularization methods (L2, dropout, batch norm): reduce overfitting and improve generalization  
- Learning rate scheduler: stabilizes optimization and improves convergence when combined with early stopping  

---

## 🧠 Summary

This project provides an empirical study on CNN-based spatio-temporal learning for urban traffic forecasting. The results highlight that performance is highly sensitive to architectural depth, temporal context length, and representation design, and demonstrate the trade-offs between deep convolutional architectures and simpler fully connected models in real-world traffic prediction tasks.
