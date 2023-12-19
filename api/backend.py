from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to the cat classifier"


@app.post("/predict")
def predict():
    pass
