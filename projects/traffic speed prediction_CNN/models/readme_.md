### 🧠 Models
- `model/cnn.py` : Defines the CNN architectur (`class CNN`)
- `model/mlp.py` : Defines the MLP architecture (`class MLP`)
- `train.py` : Model training script
- `validate.py` : Model validation script
- `test.py` : Model testing script
- `experiment.py` : Experimentation and performance evaluation
- `preprocess.py` : Data preprocessing
- `utils.py` : Visualization utilities
---
💡 This project is developed based on and extends the lecture materials from the Standalone-DeepLearning course.

- Original lecture materials: https://github.com/heartcored98/Standalone-DeepLearning/tree/master
- Modifications and extensions:
  - Added data preprocessing steps (feature scaling, modified data splitting, conversion to spatio-temporal 2D image data)
  - Modified model architectures (enhanced fully connected layers, designed CNN structures with varying depth)
  - Updated and extended loss functions
  - Enhanced data visualization code
  - Implemented early stopping and learning rate scheduling
