# Seoul Urban Core – Traffic Speed Prediction Results


## 📊 Task 1 Results
 ![image](https://github.com/user-attachments/assets/d0dbe46b-6fd3-4cc9-9e24-a40f18efa0a3)

* Compared to a fully connected model (Depth 1), CNN-based models (Depth 2–Depth 4) achieve substantially lower Mean Squared Error (MSE).

* Among the CNN variants, the Depth 2 model yields the best performance, indicating that increasing model depth does not necessarily guarantee improved predictive accuracy.

* In contrast to the referenced study—where the best performance on Beijing traffic data was achieved with a Depth 4 model—our results suggest that performance differences may arise from dataset characteristics. Specifically, the Seoul urban core dataset appears to favor a shallower architecture.

  1. If the spatial structure of the Seoul traffic data does not fully conform to a regular grid and exhibits weak correlations between adjacent roads or is locally constrained, deeper architectures may overfit to noise, leading to degraded performance.
  2. If the dataset exhibits limited variability, a shallower model (e.g., Depth 2) may generalize more effectively.

* The lower MSE observed on the test set can be attributed to:

  1. The use of L2 regularization and dropout, which mitigate overfitting and enhance generalization.
  2. Early stopping based on validation performance, preventing over-training.

![image](https://github.com/user-attachments/assets/6a1077f2-e701-4fcb-9099-a6716b60a1d0)
* The figure above presents a heatmap visualization comparing ground truth and predicted values using the best-performing CNN model (Depth 2).

---

## 📊 Task 2 Results
![imgage](https://github.com/user-attachments/assets/672762be-6e76-4667-a003-6c161492e9a7)
* Similar to Task 1, the Depth 2 CNN model achieves the lowest MSE.
* The range shown in the figure reflects variations across different hidden dimensions. Regardless of the hidden dimension, the Depth 2 model consistently demonstrates superior performance.
* A Multi-Layer Perceptron (MLP) model was also evaluated under identical experimental conditions, with results compared against CNN.
* The CNN model shows marginally better performance than the MLP model.
![image](https://github.com/user-attachments/assets/2833c73b-0bd3-40ed-a1cb-85b862612047)
* The bottom figures illustrate heatmap visualizations of predictions from both the MLP and the best CNN model compared to ground truth.
![image](https://github.com/user-attachments/assets/3624d1d5-d41c-48bb-878d-1a2d2417c653)
![image](https://github.com/user-attachments/assets/c9b38019-07bd-4d0d-93c4-8182bb9a28cc)
---

## 📊 Task 3 Results
![image](https://github.com/user-attachments/assets/f9f70817-4103-46f2-8512-be1a7577378b)
* The Depth 2 CNN model again achieves the lowest MSE.
* Comparative experiments using an MLP model indicate that CNN consistently outperforms MLP.
![image](https://github.com/user-attachments/assets/a516f471-ef06-4464-b2cd-d381e0c3657b) 
* The figures below present heatmap visualizations comparing predicted and actual values for both models.
![image](https://github.com/user-attachments/assets/d055a3d6-5cb9-46c6-b020-038c45680e30)
![image](https://github.com/user-attachments/assets/7d8f85d2-8523-46a2-8d5a-914902a08a83)
---

## 📊 Task 4 Results
![image](https://github.com/user-attachments/assets/c186d492-e6bf-4710-81e0-d3f658ffdaf7)
* In Task 4, both Depth 2 and Depth 4 models achieve strong performance; however, Depth 2 slightly outperforms Depth 4 in terms of MSE.
* As in previous tasks, experiments with an MLP model show that CNN provides superior performance.
![image](https://github.com/user-attachments/assets/12eef6d8-14fa-4dec-9b9a-b210afa6a9a8)
* The figures below illustrate heatmap comparisons between predicted and actual values for both models.
![image](https://github.com/user-attachments/assets/f2902b40-aae4-4a6e-b5c7-e52b35d54035)
![image](https://github.com/user-attachments/assets/addf893b-f28d-4b76-a8df-ef43a5e6aeab)
---

## 📋 Overall Comparison (Task 1–Task 4)
![image](https://github.com/user-attachments/assets/fba9e4c9-1947-47c1-8b54-3fc739384052)
* Across all tasks, CNN models consistently outperform MLP models, achieving up to 6.14% improvement and an average performance gain of 3.80%.
* From the comparison between Task 1 and Task 2, when predicting traffic speed 10 minutes ahead, using 30 minutes of historical data yields higher accuracy than using 40 minutes.
* From the comparison between Task 3 and Task 4, when predicting traffic speed 20 minutes ahead, using 40 minutes of historical data results in better predictive performance than using 30 minutes.

