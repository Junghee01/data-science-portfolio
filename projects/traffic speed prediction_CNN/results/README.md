# Seoul Urban Core – Traffic Speed Prediction Results

## 📊 Task 1 Results

* Compared to a fully connected model (Depth 1), CNN-based models (Depth 2–Depth 4) achieve substantially lower Mean Squared Error (MSE).

* Among the CNN variants, the Depth 2 model yields the best performance, indicating that increasing model depth does not necessarily guarantee improved predictive accuracy.

* In contrast to the referenced study—where the best performance on Beijing traffic data was achieved with a Depth 4 model—our results suggest that performance differences may arise from dataset characteristics. Specifically, the Seoul urban core dataset appears to favor a shallower architecture.

  1. If the spatial structure of the Seoul traffic data deviates from a regular grid or exhibits weak correlations between adjacent roads, deeper architectures may overfit to noise, leading to degraded performance.
  2. If the dataset is relatively small or exhibits limited variability, a shallower model (e.g., Depth 2) may generalize more effectively.

* The lower MSE observed on the test set can be attributed to:

  1. The use of L2 regularization and dropout, which mitigate overfitting and enhance generalization.
  2. Early stopping based on validation performance, preventing over-training.

* The figure above presents a heatmap visualization comparing ground truth and predicted values using the best-performing CNN model (Depth 2).

---

## 📊 Task 2 Results

* Similar to Task 1, the Depth 2 CNN model achieves the lowest MSE.
* The range shown in the figure reflects variations across different hidden dimensions. Regardless of the hidden dimension, the Depth 2 model consistently demonstrates superior performance.
* A Multi-Layer Perceptron (MLP) model was also evaluated under identical experimental conditions, with results compared against CNN.
* The CNN model shows marginally better performance than the MLP model.
* The bottom figures illustrate heatmap visualizations of predictions from both the MLP and the best CNN model compared to ground truth.

---

## 📊 Task 3 Results

* The Depth 2 CNN model again achieves the lowest MSE.
* Comparative experiments using an MLP model indicate that CNN consistently outperforms MLP.
* The figures below present heatmap visualizations comparing predicted and actual values for both models.

---

## 📊 Task 4 Results

* In Task 4, both Depth 2 and Depth 4 models achieve strong performance; however, Depth 2 slightly outperforms Depth 4 in terms of MSE.
* As in previous tasks, experiments with an MLP model show that CNN provides superior performance.
* The figures below illustrate heatmap comparisons between predicted and actual values for both models.

---

## 📋 Overall Comparison (Task 1–Task 4)

* Across all tasks, CNN models consistently outperform MLP models, achieving up to 6.14% improvement and an average performance gain of 3.80%.
* From the comparison between Task 1 and Task 2, when predicting traffic speed 10 minutes ahead, using 30 minutes of historical data yields higher accuracy than using 40 minutes.
* From the comparison between Task 3 and Task 4, when predicting traffic speed 20 minutes ahead, using 40 minutes of historical data results in better predictive performance than using 30 minutes.
