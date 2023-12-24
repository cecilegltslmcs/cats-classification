FROM tensorflow/serving:2.14.1@sha256:fdc296e313fa4454173c5728fceda38f5d18cdb44c71a9f279ce61bc5818335e

COPY ../cats-classifier /models/cats-classifier/1
ENV MODEL_NAME="cats-classifier"
