## 📁 Projects

###  🛣️ Traffic Speed Prediction in Seoul Using CNNs

This project investigates short-term traffic speed forecasting by transforming spatio-temporal traffic data into 2D image representations and applying Convolutional Neural Networks (CNNs) to model network-wide future traffic conditions.

- **Dataset:** Seoul TOPIS traffic data (April 2018)
- **Tech Stack:** Python, PyTorch, Pandas, Seaborn
- **Methodology:** Construction of spatio-temporal matrices to encode traffic dynamics as images; development and evaluation of CNN architectures with varying depths; performance comparison against a baseline MLP model
- **Key Experiments:** Analysis of CNN performance with respect to network depth; Benchmarking against Multilayer Perceptron (MLP) as a fully connected baseline model.
- **Results:** Convolutional architectures outperform simpler fully connected baseline models in real-world traffic prediction tasks, achieving up to a 6.14% improvement and an average performance gain of 3.80% in MSE; specifically, the CNN with two convolutional layers achieves the lowest MSE among all tested depths.
- **Insights:** For the Seoul urban core dataset, shallower CNN architectures achieve the best performance. This may be attributed to the low volatility and relatively simple spatiotemporal structure of the data, where spatial dependencies are weak or locally constrained. Consequently, deeper architectures may introduce unnecessary model complexity, resulting in overfitting and degraded generalization performance.

→ [View Project Details](https://github.com/Junghee01/data-science-portfolio/tree/main/projects/traffic%20speed%20prediction_CNN)

