# 1. Urban Core Dataset
  ## Task 1 Result 
  ![image](https://github.com/user-attachments/assets/ea82719a-2b31-4b1a-a89b-2a1008058229)
- FC layer로만 구성된 모델(Depth1) 보다 CNN 모델(Depth2~Depth4)에서 MSE 가 월등히 작은 것을 확인하였습니다.
- CNN 모델 중 Depth2에서 가장 좋은 MSE 가 나타나며, 이는 모델의 깊이가 깊다고 좋은 성능을 나타내는 것은 아님을 보여줍니다.
- 참고한 논문과의 차이점은, 북경 내 도로 데이터에서의 결과는 Depth4 에서 성능이 가장 높게 나타났다는 것입니다. 이부분은 데이터의 차이에서 나타나는 결과 일 수 있으며, 즉, Urban core 데이터 특성에 최적화된 모델은 더 shallow 한 구조 임을 확인할 수 있습니다. 
  1) 만약 서울 교통 데이터의 spatial 구조가 정형적인 grid가 아니거나, 인접도로 간 상관관계가 약한 경우라면, 깊게 쌓을수록 오히려 noise만 학습하게 되어 성능 저하 가능.
  2) 서울 데이터가 상대적으로 크지 않거나 변동성이 적다면, shallow한 모델(Depth 2)이 더 잘 일반화할 수 있음.
- Test data 에서 MSE가 더 낮은 이유를 추론하면,
  1) L2, dropout regularization 활용하여 train data에 덜 과적합 되고 일반화 성능이 높아지게 되기 때문이며,
  2) Early stopping 을 사용하여 val data 기준으로 모델학습을 멈추기 때문입니다.



![image](https://github.com/user-attachments/assets/5e72274b-4dd5-4d49-b7b1-b5a513ed6db8)
- 위의 Figure는 Best CNN model(Depth 2)로 실제 값과 예측값의 차이를 heatmap으로 시각한 결과입니다.


  ## Task 2 Result
  ![image](https://github.com/user-attachments/assets/672762be-6e76-4667-a003-6c161492e9a7)
- Task 2 에서도 Task 1과 유사한 양상을 보이며, Depth 2 CNN 모델의 MSE 가 가장 작은 것을 확인할 수 있습니다.
- 위의 Figure가 범위로 나타나는 이유는, hidden dimension 에 따라 어떻게 달라지는 지를 함께 나타낸 것입니다. hidden_dim 이 달라지더라도 Depth 2에서 가장 좋은 성능을 보입니다.
  ![image](https://github.com/user-attachments/assets/1e4b53fa-c791-45a9-9faf-a8912895bcc1)
- 위 그림은 MLP 과 Best CNN 모델을 비교한 것으로, 서울 Urban Core Dataset에서 MLP 모델이 조금 더 좋은 성능을 보여줍니다.
