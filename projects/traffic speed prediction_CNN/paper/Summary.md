### [📄Paper] https://doi.org/10.3390/s17040818
##### Ma, X., Dai, Z., He, Z., Ma, J., Wang, Y., & Wang, Y. (2017). Learning traffic as images: A deep convolutional neural network for large-scale transportation network speed prediction. sensors, 17(4), 818.

### [📝Paper Summary]
This study proposes a convolutional neural network (CNN)-based approach that learns traffic conditions as images and predicts traffic speeds across large-scale transportation networks with high accuracy. Spatiotemporal variations in traffic flow are transformed into a two-dimensional spatiotemporal matrix, enabling the representation of temporal and spatial relationships in the form of images, to which a CNN model is applied.

The effectiveness of the proposed method is evaluated using real-world traffic networks in Beijing, China, specifically the Second Ring Road and the northeastern traffic network. The proposed approach is compared with conventional algorithms, including Ordinary Least Squares (OLS), K-Nearest Neighbors (KNN), Artificial Neural Networks (ANN), Random Forest (RF), Stacked Autoencoders (SAE), Recurrent Neural Networks (RNN), and Long Short-Term Memory (LSTM).

Experimental results demonstrate that the proposed CNN-based method achieves, on average, a 42.91% improvement in prediction accuracy compared to the other algorithms, while maintaining a computational time within an acceptable range.

## 1. Study Area and Task Description
![image](https://github.com/user-attachments/assets/ba4fd260-d210-446e-83f8-02f2992f8587)

This study considers two real-world traffic networks in Beijing, China: **(a)Beijing Second Ring Road**, **(b)Northeastern Beijing Traffic Network**
To evaluate the proposed model, four prediction tasks are defined under different input-output temporal settings:

* **Task 1**: Predict traffic speed for the next 10 minutes using the past 30 minutes of traffic data
* **Task 2**: Predict traffic speed for the next 10 minutes using the past 40 minutes of traffic data
* **Task 3**: Predict traffic speed for the next 20 minutes using the past 30 minutes of traffic data
* **Task 4**: Predict traffic speed for the next 20 minutes using the past 40 minutes of traffic data

## 2. Methodology
![image](https://github.com/user-attachments/assets/73595d52-5f10-46f1-bdda-0d690d23f0fd)
![image](https://github.com/user-attachments/assets/dee1c858-de73-4c01-9e45-b45ed1ea556a)
* As illustrated in Figure 2, a CNN model is constructed by repeatedly stacking convolutional layers and max-pooling layers, followed by a fully connected (FC) layer at the final stage.
* The formulation of the model can be expressed as follows:
#####  (Equation) ![image](https://github.com/user-attachments/assets/bce41be6-6fde-4afe-b6f6-626d43a3e1bc)
## 2. Model Configuration and Training Details

* As shown in Table 1, four CNN-based models (**Depth1**, **Depth2**, **Depth3**, and **Depth4**) are constructed to compare performance across different network depths.
  * **Depth1** represents a baseline model composed solely of a fully connected (FC) layer, without any convolutional or pooling layers.
* The study utilizes 37 days of taxi trajectory data. The spatiotemporal matrix is treated as multi-channel image input, and all input values are normalized to facilitate stable model training.
* For hyperparameter tuning, the model configuration is inspired by established architectures such as LeNet and AlexNet (winner of an image classification competition). Specifically:
  * The filter size is set to **(3, 3)**
  * The max-pooling size is set to **(2, 2)**
* To prevent overfitting, an early stopping criterion is applied during training. The model uses **Mean Squared Error (MSE)** as the loss function to measure the discrepancy between predicted and actual values, and the **ReLU** activation function is employed.

## 3. Results
![image](https://github.com/user-attachments/assets/524f3f05-ceac-4d29-8a4f-d4015d1ce9c0)
* Among the CNN models, Depth1 exhibits the poorest performance, whereas Depth4 achieves the lowest MSE value, demonstrating the best predictive performance.
![image](https://github.com/user-attachments/assets/8abaf546-1fac-499d-8cc4-d1658315b6eb)
* The CNN model requires a reasonable computational time while achieving the best performance compared to the seven conventional baseline models.
* Although CNN requires a longer training and inference time compared to some other deep learning models, it yields higher predictive accuracy, which can be attributed to its ability to effectively extract spatiotemporal features.
* The CNN model demonstrates higher prediction accuracy in short-term forecasting tasks compared to long-term forecasting scenarios.

