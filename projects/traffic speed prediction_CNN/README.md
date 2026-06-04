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

## 📐 Differences from the Original Study

This section summarizes the key methodological differences between the original paper and this project.

| Aspect | Original Study | This Project |
|--------|----------------|--------------|
| **Study Area** | Beijing road network | Seoul urban road network |
| **Baseline Models** | OLS, Random Forest, ANN, and 4 additional models | Multilayer Perceptron (MLP) as the primary fully connected baseline |
| **Loss Functions** | (original scale) MSE | MSE, MAE, and inverse-transformed (original-scale) MSE/MAE |

### Loss Function Rationale
Although MSE computed on normalized data can yield small numerical values, it is not always directly interpretable. Therefore, MAE is additionally considered, and both metrics are also transformed back to the original scale to ensure a more interpretable and consistent performance comparison.

### Hyperparameter Design

| Hyperparameter | Original Study | This Project | Purpose / Motivation |
|----------------|----------------|--------------|----------------------|
| `hid_dim` | Not explicitly explored | Included | To increase model capacity and improve predictive performance |
| `L2 regularization` | Not specified | Included | To reduce overfitting and improve generalization |
| `Batch Normalization (use_bn)` | Not specified | Included | To stabilize training and improve convergence |
| `Dropout` | Not specified | Included | To prevent overfitting in dense feature representations |
| `Learning rate (lr)` | Basic setting | Tuned | To improve optimization efficiency |
| `Learning rate scheduler` | Not used | Included | To dynamically adjust learning rate for better convergence |
| `Early stopping` | Used | Used | To prevent overfitting and reduce unnecessary training |

---

## 🧠 Summary

This study presents an empirical investigation of CNN-based spatio-temporal learning for urban traffic forecasting. The results indicate that model performance is highly sensitive to architectural depth, while temporal context length has a moderate but noticeable impact on performance. The results also demonstrate that convolutional architectures outperform simpler fully connected models in real-world traffic prediction tasks. Furthermore, for the Seoul urban core dataset, a shallower CNN architecture yields the best performance. This may be attributed to the low volatility and relatively simple spatio-temporal dynamics of the data, where spatial correlation is relatively weak or locally constrained. In such cases, deeper architectures may introduce unnecessary model complexity, leading to overfitting and reduced generalization performance.
