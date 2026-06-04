# 🛣️ CNN-based Spatio-Temporal Traffic Speed Prediction in Urban Road Networks (Seoul Case Study)

## 📄 Abstract

Accurate short-term traffic speed prediction is a fundamental problem in intelligent transportation systems, requiring effective modeling of complex spatio-temporal dependencies in urban road networks.  

In this study, we investigate Convolutional Neural Networks (CNNs) for traffic speed forecasting by reformulating traffic time series as 2D image-like representations. Building upon the framework introduced in *"Learning Traffic as Images: A Deep Convolutional Neural Network for Large-Scale Transportation Network Speed Prediction"*, we adapt and evaluate the model on Seoul’s urban road network using real-world traffic data.

We systematically evaluate multiple prediction horizons and historical input windows, and analyze the impact of network depth on predictive performance. Furthermore, we compare CNN-based architectures against a Multilayer Perceptron (MLP) baseline to assess the benefit of explicit spatial feature extraction.

---

## 🎯 Research Objectives

This project aims to:

- Reformulate spatio-temporal traffic data into structured 2D representations suitable for CNN-based learning  
- Capture spatial dependencies and temporal dynamics for short-term traffic speed prediction  
- Evaluate the effect of CNN architectural depth on forecasting performance  
- Compare deep convolutional models against a fully connected neural network (MLP) baseline  
- Analyze the trade-off between representation learning capacity and model simplicity in urban traffic forecasting  

---

## 🧪 Experimental Design

We follow and extend the experimental settings from the original paper, defining four prediction tasks:

- **Task 1:** Predict 10-minute traffic speed using the past 30 minutes  
- **Task 2:** Predict 10-minute traffic speed using the past 40 minutes  
- **Task 3:** Predict 20-minute traffic speed using the past 30 minutes  
- **Task 4:** Predict 20-minute traffic speed using the past 40 minutes  

These configurations allow systematic evaluation of temporal context length and prediction horizon.

---

## 📊 Dataset

- **Source:** Seoul Open Data Plaza (TOPIS traffic speed dataset)  
- **Period:** April 2018  
- **Spatial Scope:** Central and urban road network links in Seoul  
- **Task:** Link-level traffic speed forecasting  

---

## 🧠 Methodology

### Input Representation

Traffic time series are transformed into structured spatio-temporal matrices and reshaped into 2D image-like tensors, enabling convolutional feature extraction over both spatial and temporal dimensions.

### Models

- **Baseline:** Multilayer Perceptron (MLP) with fully connected layers  
- **Proposed Models:** 2D CNN architectures with varying depth (2–4 convolutional layers)

### Output

- Short-term traffic speed prediction for:
  - 10-minute horizon  
  - 20-minute horizon  

---

## ⚙️ Implementation Details

- **Framework:** PyTorch  
- **Language:** Python  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn  

### Hyperparameter Design

To improve generalization and optimization stability, the following hyperparameters were introduced and tuned:

- Hidden dimension (`hid_dim`)  
- L2 regularization  
- Dropout  
- Batch normalization (`use_bn`)  
- Learning rate (`lr`)  
- Learning rate scheduler  
- Early stopping  

**Design Rationale:**
- Regularization techniques reduce overfitting in sparse traffic observations  
- Learning rate scheduling improves convergence stability  
- Increased model capacity enables better spatio-temporal feature learning  

---

## 📐 Comparison with Original Work

| Aspect | Original Study | This Work |
|--------|----------------|-----------|
| Study Area | Beijing road network | Seoul urban road network |
| Baseline Models | OLS, RF, ANN, statistical ML models | MLP (fully connected neural network) |
| Input Design | Traffic-as-image representation | Same framework adapted to Seoul topology |
| Evaluation Metrics | MSE, MAE, scaled metrics | MSE, MAE (also reported in original scale) |
| Hyperparameter Scope | Limited tuning (mainly early stopping) | Extended systematic tuning (regularization, scheduler, architecture depth) |

---

## 📈 Key Contributions

- Adaptation of a CNN-based traffic forecasting framework to a new metropolitan-scale dataset (Seoul)  
- Systematic evaluation of CNN depth effects on predictive performance  
- Empirical comparison between representation learning (CNN) and fully connected baselines (MLP)  
- Extension of hyperparameter space for improved model robustness and generalization  

---

## 🧠 Summary

This project provides an empirical study on CNN-based spatio-temporal learning for urban traffic forecasting. The results highlight that performance is highly sensitive to architectural depth, temporal context length, and representation design, and demonstrate the trade-offs between deep convolutional architectures and simpler fully connected models in real-world traffic prediction tasks.
