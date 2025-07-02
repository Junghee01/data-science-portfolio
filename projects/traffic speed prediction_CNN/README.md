# 🛣️ CNN-based Traffic Speed Prediction in Seoul

본 프로젝트는 CNN(Convolutional Neural Network)을 활용하여 서울시 주요 도로의 교통 속도를 예측하는 모델을 구현하고, 성능을 평가한 실험입니다.
CNN Paper(Learning Traffic as Images: A Deep Convolutional Neural Network for Large-Scale Transportation Network Speed Prediction) 를 참고하여 서울의 중심도로와 도심도로에 적용한 프로젝트로, 해당 논문에서 설계한 TASK 4개에 대해 실험한 프로젝트입니다.
- Task 1: 10-min traffic prediction using last 30-min traffic speeds;  
- Task 2: 10-min traffic prediction using last 40-min traffic speeds;  
- Task 3: 20-min traffic prediction using last 30-min traffic speeds; and 
- Task 4: 20-min traffic prediction using last 40-min traffic speeds.  


**목표**  
- 시계열 교통 데이터를 이미지 형태로 변환하여 CNN에 입력  
- 시·공간적 패턴을 학습해 미래 속도 예측 정확도 향상
- Convolution layer의 깊이에 따른 4가지 모델의 성능 비교
- MLP 모델과의 예측 성능 비교

## 🧪 프로젝트 개요
- **데이터 출처**: [서울 열린데이터광장](https://data.seoul.go.kr) / TOPIS 2018년 4월 교통 속도 데이터  
- **예측 대상**: 도시중심부도로와 도심도로의 도로 링크 별 향후 10분 및 20분 동안의 속도 예측
- **기술 스택**: Python, PyTorch, NumPy, Matplotlib, Seaborn, Pandas  
- **모델 구조**:
  - FC : Fully Connected layer 단독 구성(Depth1)
  - 2D CNN: 2~4개 Conv layer 구성(Depth2 ~ Depth4)
  - 입력: 시계열+공간을 2D 이미지로 매핑한 matrix로, 과거 30분 및 40분의 이미지를 input으로 활용  
  - 출력: 향후 10분 과 20분 속도 예측
  
## 📐기존논문 설계와의 차이(프로젝트/ 해당논문)
- 분석 대상지 : 서울의 2개 도로 네트워크의 교통속도 예측 / 베이징 2개 도로 네트워크의 교통속도 예측
- 비교 모델 : MLP / OLS, RF, ANN 외 4개 모델
- Loss : MSE, MAE, original scaled MSE, original scaled MAE / original scaled MSE
  - 다양한 Loss 활용 이유 : 정규화 데이터에서의 MSE 가 작은 단위로 나와 MAE를 추가적으로 확인하였으며, 두 Loss 값을 원자료 스케일로 환산하여 성능 비교를 명확히 하기 위함
- 파라미터 : hid_dim, l2, use_bn, dropout, lr, early_stopping, scheduler_learning_rate / early_stopping 만 명시됨
  - hid_dim 추가이유 : 좋은 예측 성능을 만드는 모델로 튜닝하기 위함
  - l2, use_bn, dropout 추가 이유 : Over-fitting 을 방지함으로써, 일반화된 모델을 만들어 val data와 test data에서 예측 성능 향상을 위함
  - scheduler_learning_rate 추가 이유 : early_stopping 과 함께 learning rate를 적용하면 Loss에 따라 적절하게 lr이 줄어들면서 효율적인 모델 트레이닝이 가능하기 때문

---
💡 본 프로젝트의 코드는 [Standalone-DeepLearning]의 강의 자료를 기반으로 변형 및 확장하여 작성되었습니다.

- 원본 강의 자료: [[강의 GitHub 링크]([https://github.com/heartcored98/Standalone-DeepLearning/blob/master/Lec5/Lab7_CIFAR-10_with_CNN.ipynb](https://github.com/heartcored98/Standalone-DeepLearning/tree/master])
- 변형 내용: 데이터 전처리 추가(scaling 추가, data split 변경, Spatio-temporal 2d image data로 변경), 모델 구조 수정(Fc layer 다독 모델, Depth 구조에 따른 CNN 모델 형성 등), Loss function 변경 및 추가, 데이터 시각화 코드 변경 및 추가, Early stopping 및 Schedular learning rate 추가 등
