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
|── illustrations                           # screenshots
|── models                                  # models in h5 format
    |── resnet50_01_0.597.h5
    |── resnet50_02_0.654.h5
    |── resnet50_06_0.684.h5
    |── resnet50_25_0.700.h5
|── notebooks
    |── notebook.ipynb                      # experiment different CNNs
|── .gitignore
└── README.md
```

## Dataset

This dataset used comes from Kaggle website. It is available here : [Cat Breeds Refined Dataset](https://www.kaggle.com/datasets/doctrinek/catbreedsrefined-7k).

## Methodology

--WIP--

## How to use the app?

--WIP--

## Technologies

- Python 3
- Tensorflow
- Keras


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
