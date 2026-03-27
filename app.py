from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="Smart Agriculture API")

# Load model
model = joblib.load("model/crop_model.pkl")


# Home route
@app.get("/")
def home():
    return {"message": "API Working"}


# Prediction route
@app.post("/predict")
def predict(
    N: float,
    P: float,
    K: float,
    temperature: float,
    humidity: float,
    ph: float,
    rainfall: float
):
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(data)

    return {"recommended_crop": prediction[0]}