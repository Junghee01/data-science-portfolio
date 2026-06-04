## 📁 Projects

### 1. 🛣️ Traffic Speed Prediction in Seoul Using CNNs

This project investigates short-term traffic speed forecasting by transforming spatio-temporal traffic data into 2D image representations and applying Convolutional Neural Networks (CNNs) to model network-wide future traffic conditions.

Dataset: Seoul TOPIS traffic data (April 2018)
Tech Stack: Python, PyTorch, Pandas, Seaborn
Methodology: Construction of spatio-temporal matrices to encode traffic dynamics as images; development and evaluation of CNN architectures with varying depths; performance comparison against a baseline MLP model
Key Experiments:
Analysis of CNN performance with respect to network depth
Benchmarking against Multilayer Perceptron (MLP) as a fully connected baseline
Results: The CNN with 2 convolutional layers achieved the lowest Mean Squared Error (MSE) among CNN variants. However, the MLP baseline demonstrated stronger overall predictive performance, indicating the importance of feature representation for this task.

→ [View Project Details](https://github.com/Junghee01/data-science-portfolio/tree/main/projects/traffic%20speed%20prediction_CNN)

