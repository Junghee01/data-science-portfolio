### [Paper] https://doi.org/10.3390/s17040818
# Learning Traffic as Images: A Deep Convolutional Neural Network for Large-Scale Transportation Network Speed Prediction
 **Xiaolei Ma 1, Zhuang Dai 1, Zhengbing He 2, Jihui Ma 2,*, Yong Wang 3 and Yunpeng Wang 1**

 1 School of Transportation Science and Engineering, Beijing Key Laboratory for Cooperative Vehicle
 Infrastructure System and Safety Control, Beihang University, Beijing 100191, China;
 xiaolei@buaa.edu.cn (X.M.); zhuangdai@buaa.edu.cn (Z.D.); ypwang@buaa.edu.cn (Y.W.)
 
 2 School of Traffic and Transportation, Beijing Jiaotong University, Beijing 100044, China; he.zb@hotmail.com
 
 3  School of Economics and Management, Chongqing Jiaotong University, Chongqing 400074, China; yongwx6@gmail.com
  * Correspondence: jhma@bjtu.edu.cn; Tel.: +86-10-5168-8514
  Academic Editor: Simon X. Yang

 Received: 30 January 2017; Accepted: 7 April 2017; Published: 10 April 2017

### [Summary]
이 논문은 합성곱 신경망(CNN) 기반의 방법을 제안하며, 교통 상황을 이미지로 학습하고 대규모 교통망 전반의 속도를 높은 정확도로 예측합니다. 시공간적인 교통 흐름의 변화를 2차원 시공간 행렬로 변환하여 시간과 공간상의 관계를 이미지로 표현하고, 이 이미지에 CNN을 적용합니다. 제안된 방법의 효과는 중국 베이징의 실제 교통 네트워크인 2차 순환도로와 북동부 교통망을 사례로 평가되며, OLS, KNN, ANN, random forest, SAE, RNN, 그리고 LSTM 과 같은 기존 알고리즘들과 비교합니다. 그 결과, 제안된 CNN 기반 방법은 평균적으로 다른 알고리즘보다 42.91% 높은 정확도 향상을 보였으며, 실행 시간도 수용 가능한 수준으로 나타났습니다.
##### 1. 해당 논문의 실험 대상 지역 및 TASK 설명
![image](https://github.com/user-attachments/assets/ba4fd260-d210-446e-83f8-02f2992f8587)

위의 두 도로(a.베이징 2차 순환도로, b.베이징 북동부 교통망 도로) 에 대한 다음과 같은 4개의 Task 를 수행합니다.
- Task 1: 과거 30분 교통속도를 통해 미래 10 분 교통 속도 예측 
- Task 2: 과거 40분 교통속도를 통해 미래 10 분 교통 속도 예측
- Task 3: 과거 30분 교통속도를 통해 미래 20 분 교통 속도 예측 
- Task 4: 과거 40분 교통속도를 통해 미래 20 분 교통 속도 예측  

##### 2. 방법론 설명
![image](https://github.com/user-attachments/assets/73595d52-5f10-46f1-bdda-0d690d23f0fd)
![image](https://github.com/user-attachments/assets/dee1c858-de73-4c01-9e45-b45ed1ea556a)

- Figure 2 에서 처럼 Convolution Layer, Max Pooling Layer 를 반복하고, 마지막에 FC Layer 를 통과하는 CNN 모델을 생성합니다.
- Table 1 에서 처럼 CNN 모델을 총 4개의 모델(Depth1, Depth2, Depth3, Depth4)로 생성하여 각 모델의 성능을 비교합니다. **이 때, Depth1은 Convolution layer 와 Pooling Layer가 없는 FC layer 단독으로 구성된 모델을 나타냅니다.**
- 해당 논문은 37일 동안의 taxi data 활용하여 시간-공간 행렬을 이미지의 채널로 사용하며, input 값은 normalize 하여 모델 트레이닝이 어려워 지는 것을 방지합니다.
- 해당 연구의 파라미터 튜닝에 관하여는, LeNet과 AlexNet(이미지 classification competition 우승)을 참고하여 파라미터 세팅하였는데, 즉, filter size는 (3,3), max pooling size는 (2,2)로 세팅하였습니다.
- 해당 연구는 Early stopping criterion를 사용하여 모델의 오버피팅 문제가 발생하지 않도록 하였고, MSE를 예측값과 실제값의 거리측정을 위한 Loss 로 활용하였으며, activation function은 relu를 활용하였습니다. 

##### 3. 결과 설명
![image](https://github.com/user-attachments/assets/524f3f05-ceac-4d29-8a4f-d4015d1ce9c0)
- CNN 모델 중에서 Depth 1 이 가장 성능이 좋지 않으며, Depth 4에서 MSE 가 가장 낮은 값을 기록하여 좋은 성능을 보여줍니다.
![image](https://github.com/user-attachments/assets/8abaf546-1fac-499d-8cc4-d1658315b6eb)
- CNN 은 resonable 한 시간을 소요하며, 다른 7개의 기존 모델보다 가장 좋은 성능을 나타냅니다.
- CNN 은 다른 딥러닝 모델보다눈 소요시간은 오래 걸리나, 더 높은 정확도를 나타내는데, 이는 시공간적 특징 추출을 통해서 가능합니다.
- CNN 은 long term 예측 보다는 short term 예측에서 더 정확하게 예측합니다.


