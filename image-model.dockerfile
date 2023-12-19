FROM tensorflow/serving:2.7.0

COPY ../cats-classifier /models/cats-classifier/1
ENV MODEL_NAME="cats-classifier"
