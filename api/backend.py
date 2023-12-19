from fastapi import FastAPI, Request, File, UploadFile
import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from keras_image_helper import create_preprocessor
import os
from proto import np_to_protobuf

host = os.getenv("TF_SERVING_HOST", "localhost:8500")
channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
preprocessor = create_preprocessor("resnet50", target_size=(224, 224))

app = FastAPI()


def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = "cats-classifier"
    pb_request.model_spec.signature_name = "serving_default"

    pb_request.inputs["input_6"].CopyFrom(np_to_protobuf(X))

    return pb_request


classes = [
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


def prepare_response(pb_response):
    preds = pb_response.outputs["dense_5"].float_val
    return dict(zip(classes, preds))


def predict(path):
    X = preprocessor.from_path(path)
    pb_request = prepare_request(X)
    pb_response = stub.Predict(pb_request, timeout=20.0)
    response = prepare_response(pb_response)
    return response


@app.get("/")
def home():
    return "Welcome to the cat classifier"


@app.post("/predict")
async def predict_endpoint(request: Request, file: UploadFile = File(...)):
    result = predict(file.file)
    return result


if __name__ == "__main__":
    # url = 'https://image.petmd.com/files/styles/978x550/public/2023-07/scottish-fold.jpg?w=1080&q=75'
    # response = predict(url)
    # print(response)
    app.run(debug=True, host="0.0.0.0")
