#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from fastapi import FastAPI, Request, File, UploadFile
import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from keras_image_helper import create_preprocessor
from proto import np_to_protobuf
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


TF_SERVING_HOST = os.getenv("TF_SERVING_HOST", "localhost:8500")
HOST = "0.0.0.0"
PORT = 8000

channel = grpc.insecure_channel(TF_SERVING_HOST)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

preprocessor = create_preprocessor("resnet50", target_size=(224, 224))

CLASSES = [
    "Ragdoll",
    "Bombay",
    "American Curl",
    "Birman",
    "Egyptian Mau",
    "Bengal",
    "Siamese",
    "Maine Coon",
    "American Bobtail",
    "Turkish Angora",
    "Russian Blue",
    "British Shorthair",
    "Persian",
    "Abyssinian",
    "Norwegian Forest",
    "Manx",
    "Scottish Fold",
    "American Shorthair",
    "Exotic Shorthair",
    "Sphynx",
]

app = FastAPI()


def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = "cats-classifier"
    pb_request.model_spec.signature_name = "serving_default"

    pb_request.inputs["input_2"].CopyFrom(np_to_protobuf(X))

    return pb_request


def prepare_response(pb_response):
    preds = pb_response.outputs["dense_1"].float_val
    return dict(zip(CLASSES, preds))


def predict(path):
    try:
        X = preprocessor.from_path(path)
        pb_request = prepare_request(X)
        pb_response = stub.Predict(pb_request, timeout=20.0)
        response = prepare_response(pb_response)
        return response
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return {"error": "Prediction failed"}


@app.post("/predict")
async def predict_endpoint(request: Request, file: UploadFile = File(...)):
    result = predict(file.file)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
