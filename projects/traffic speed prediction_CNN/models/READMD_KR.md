### 🧠 Models
- `model/cnn.py` : CNN 구조 정의 (`class CNN`)
- `model/mlp.py` : MLP 구조 정의 (`class MLP`)
- `train.py` : 모델 학습 스크립트
- `validate.py` : 모델 validate 스크립트
- `test.py` : 모델 test 스크립트
- `experiment.py` : 테스트 및 성능평가
- `preprocess.py` : 데이터 전처리
- `utils.py` : 시각화 함수

---
💡 본 프로젝트의 코드는 [Standalone-DeepLearning]의 강의 자료를 기반으로 변형 및 확장하여 작성되었습니다.

- 원본 강의 자료: [강의 GitHub 링크](https://github.com/heartcored98/Standalone-DeepLearning/tree/master])
- 변형 내용: 데이터 전처리 추가(scaling 추가, data split 변경, Spatio-temporal 2d image data로 변경), 모델 구조 수정(Fc layer 다독 모델, Depth 구조에 따른 CNN 모델 형성 등), Loss function 변경 및 추가, 데이터 시각화 코드 변경 및 추가, Early stopping 및 Schedular learning rate 추가 등
