# Cats Classifier

![image](illustrations/cat_banner_readme.avif)

## Table of contents

- [Summary](#summary)
- [Repo Structure](#repo-structure)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [How to use the app ?](#how-to-use-the-app)
- [Technologies](#technologies)
- [Bibliography](#bibliography)

## Summary

Deep learning algorithms are widely used in various fields, such as computer vision. Computer vision allows the computer to "see" and do things like identify specific objects in an image, or classify images according to their content.
This project is about image classification. More specifically, the aim is to identify the breed of a cat in an image. To achieve this classifier, Transfer learning will be performed. Among all existing models, three will be explored: Xception, ResNet50 and EfficientNetB7.

## Repo Structure

```bash
.
|── api
    |── backend.py
    |── frontend.py
    |── proto.py
|── illustrations                           # screenshots
|── models                                  # models in h5 format
    |── resnet50_28_0.692.h5
|── notebooks                               # notebook with model training
    |── notebook.ipynb
    |── tf-serving.ipynb
|── scripts                                 # script to train the model
    |── train_model.py
|── .gitattributes
|── .gitignore
|── README.md
└── requirements.txt
```

## Dataset

This dataset used comes from Kaggle website. It is available here : [Cat Breeds Refined Dataset](https://www.kaggle.com/datasets/doctrinek/catbreedsrefined-7k).

## Methodology



*Summary of the different training and tuning*
|Model | Accuracy | Loss | Time for tuning |
|------|----------|------|------|
|Xception | 65.93% | 1.16| 52 min |
|ResNet50 | 69.97% | 0.974 | 59 min |
| EfficientNetB7 | 66.18% | 1.738 | 2h25 |


*Transform h5 to files for tensorflow-serving-api*
```
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("models/resnet50_28_0.692.h5")
tf.saved_model.save(model, 'cat-classifier')

```

## How to use the app?

### Launch locally

- Launch container with Tensorflow serving
```
docker run -it --rm \
  -p 8500:8500 \
  -v $(pwd)/cats-classifier:/models/cats-classifier/1 \
  -e MODEL_NAME="cats-classifier" \
  tensorflow/serving:2.7.0
```
- Launch with backend only

After launching docker, you can launch the backend alone: `uvicorn backend:app` and go this address `localhost:8000/docs`. You may see this window :
![Alt text](/illustrations/fastapi-1.png)
Click on the arrow in the green area. You might see this :
![Alt text](/illustrations/fastapi-2.png)
Click on the "Try it out" button and you can submit your pictures.
![Alt text](/illustrations/fastapi-3.png)
After submitting your pictures, your predictions appears below.
![Alt text](/illustrations/fastapi-3.png)

- Launch with backend and frontend

After launching Docker and backend, you can open an other terminal and type : `streamlit run frontend.py`. You may see this window :
![Alt text](/illustrations/front_streamlit.png)
Click on the 'Browse files' and you will obtain your predictions.

## Technologies

- Python 3
- Tensorflow
- Keras
- Streamlit
- FastAPI


## Bibliography

**General**:
- [Introduction to Dropout for Regularization](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/)
- [How Do Convolutional Layers Work?](https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/)

**Optimizer and Loss Functions for multiclasses classification:**

- [Adam Optimizer for multiclasses classification](https://towardsdatascience.com/multiclass-classification-neural-network-using-adam-optimizer-fb9a4d2f73f4)
- [Understanding Loss functions for classification](https://medium.com/mlearning-ai/understanding-loss-functions-for-classification-81c19ee72c2a)

**Transfer Learning**:
- [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357)
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946)

**Keras Tuner:**
- [Introduction to Keras Tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner?hl=en)
