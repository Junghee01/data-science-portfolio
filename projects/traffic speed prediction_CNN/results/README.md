# [Seoul Urban Core – Traffic Speed Prediction Results]
  ## 📊Task 1 Result 
  ![image](https://github.com/user-attachments/assets/d0dbe46b-6fd3-4cc9-9e24-a40f18efa0a3)
- FC layer로만 구성된 모델(Depth1) 보다 CNN 모델(Depth2~Depth4)에서 MSE 가 월등히 작은 것을 확인하였습니다.
- CNN 모델 중 Depth2에서 가장 좋은 MSE 가 나타나며, 이는 모델의 깊이가 깊다고 좋은 성능을 나타내는 것은 아님을 보여줍니다.
- 참고한 논문과의 차이점은, 북경 내 도로 데이터에서의 결과는 Depth4 에서 성능이 가장 높게 나타났다는 것입니다. 이부분은 데이터의 차이에서 나타나는 결과 일 수 있으며, 즉, Urban core 데이터 특성에 최적화된 모델은 더 shallow 한 구조 임을 확인할 수 있습니다. 
  1) 만약 서울 교통 데이터의 spatial 구조가 정형적인 grid가 아니거나, 인접도로 간 상관관계가 약한 경우라면, 깊게 쌓을수록 오히려 noise만 학습하게 되어 성능 저하 가능.
  2) 서울 데이터가 상대적으로 크지 않거나 변동성이 적다면, shallow한 모델(Depth 2)이 더 잘 일반화할 수 있음.
- Test data 에서 MSE가 더 낮은 이유를 추론하면,
  1) L2, dropout regularization 활용하여 train data에 덜 과적합 되고 일반화 성능이 높아지게 되기 때문이며,
  2) Early stopping 을 사용하여 val data 기준으로 모델학습을 멈추기 때문입니다.



![image](https://github.com/user-attachments/assets/6a1077f2-e701-4fcb-9099-a6716b60a1d0)
- 위 Figure는 Best CNN model(Depth 2)로 실제 값과 예측값의 차이를 heatmap으로 시각한 결과입니다.

---

  ## 📊Task 2 Result
  ![image](https://github.com/user-attachments/assets/672762be-6e76-4667-a003-6c161492e9a7)
- Task 2 에서도 Task 1과 유사한 양상을 보이며, Depth 2 CNN 모델의 MSE 가 가장 작은 것을 확인할 수 있습니다.
- 위의 Figure가 범위로 나타나는 이유는, hidden dimension 에 따라 어떻게 달라지는 지를 함께 나타낸 것입니다. hidden_dim 이 달라지더라도 Depth 2에서 가장 좋은 성능을 보입니다.

- Multi Layer Perceptron(MLP) 모델을 활용하여 동일한 실험을 진행하였으며, CNN과의 성능비교 결과는 아래와 같습니다.
- CNN 모델이 MLP 모델보다 근소하게 좋은 성능을 보여줍니다.
- 가장 아래 두 그림은 MLP와 Best CNN model로 예측한 값과 실제값을 heatmap으로 시각화 한 것입니다.
  
![image](https://github.com/user-attachments/assets/2833c73b-0bd3-40ed-a1cb-85b862612047)
![image](https://github.com/user-attachments/assets/3624d1d5-d41c-48bb-878d-1a2d2417c653)
![image](https://github.com/user-attachments/assets/c9b38019-07bd-4d0d-93c4-8182bb9a28cc)


---

  ## 📊Task 3 Result
![image](https://github.com/user-attachments/assets/f9f70817-4103-46f2-8512-be1a7577378b)
- Task 3 에서도 Depth 2 CNN 모델의 MSE 가 가장 작은 것을 확인할 수 있습니다.
- MLP 모델을 활용하여 동일한 실험을 진행하였으며, CNN 과의 성능비교 결과는 아래와 같으며, CNN 모델에서 더 좋은 성능을 나타냄을 보여줍니다.
![image](https://github.com/user-attachments/assets/a516f471-ef06-4464-b2cd-d381e0c3657b)
- 아래 그림은 MLP와 CNN 모델로 예측한 값과 실제값을 heatmap으로 시각화 한 것입니다.
![image](https://github.com/user-attachments/assets/d055a3d6-5cb9-46c6-b020-038c45680e30)
![image](https://github.com/user-attachments/assets/7d8f85d2-8523-46a2-8d5a-914902a08a83)


 ---

  ## 📊Task 4 Result
![image](https://github.com/user-attachments/assets/c186d492-e6bf-4710-81e0-d3f658ffdaf7)
- Task 4에서는 Depth 2와 Depth4에서 가장 좋은 MSE를 보여주나, Depth 2에서 미세하게 더 좋은 성능을 나타냈습니다.
- MLP 모델을 활용하여 동일한 실험을 진행하였으며, CNN 과의 성능비교 결과는 아래와 같으며, CNN 모델에서 더 좋은 성능을 나타냄을 보여줍니다.
![image](https://github.com/user-attachments/assets/12eef6d8-14fa-4dec-9b9a-b210afa6a9a8)
- 아래 그림은 MLP와 CNN 모델로 예측한 값과 실제값을 heatmap으로 시각화 한 것입니다.
![image](https://github.com/user-attachments/assets/f2902b40-aae4-4a6e-b5c7-e52b35d54035)
![image](https://github.com/user-attachments/assets/addf893b-f28d-4b76-a8df-ef43a5e6aeab)
  
--- 

## 📋전체 결과 비교(Task1~Task4)
![image](https://github.com/user-attachments/assets/fba9e4c9-1947-47c1-8b54-3fc739384052)
- 모든 Task 에서 MLP 모델보다 CNN 모델에서 좋은 성능을 보여줍니다.(최대 6.14%, 평균 3.80% 성능향상)
- Task1 과 Task2 의 비교를 통해, 향후 10 분 속도를 예측할 경우 과거 30분 데이터를 활용하는 것이 과거 40분 데이터를 활용 할 때 보다 예측 정확도가 높음을 보여줍니다.
- Task3 과 Task4 의 비교를 통해, 향후 20 분 속도를 예측할 경우 과거 40분 데이터를 활용하는 것이 과거 30분 데이터를 활용 할 때 보다 예측 정확도가 높음을 보여줍니다.
