🌱 Crop Recommendation API (Smart Agriculture)
📌 Project Overview

The Crop Recommendation API is a Machine Learning–based system that recommends the most suitable crop based on soil nutrients and environmental conditions.

This project is part of a Smart Agriculture System aimed at helping farmers make data-driven decisions to improve crop yield and resource utilization.
🎯 Objective

To predict the best crop using:

    Nitrogen (N)

    Phosphorus (P)

    Potassium (K)

    Temperature

    Humidity

    pH level

    Rainfall

🧠 Machine Learning Model

    Algorithm Used: Random Forest Classifier

    Dataset: Crop Recommendation Dataset

    Training Language: Python

    Framework: FastAPI

📂 Project Structure

crop-recommendation-api/
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── model/
│   └── crop_model.pkl
│
├── app.py                # FastAPI application
├── train_model.py        # Model training script
├── requirements.txt      # Dependencies
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/Crop_recommendation.git
cd Crop_recommendation

2️⃣ Create Virtual Environment

python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

🚀 Run the API

uvicorn app:app --reload

Server will start at:

http://127.0.0.1:8000

📖 API Documentation (Swagger UI)

Open in browser:

http://127.0.0.1:8000/docs

You can test API directly from this interface.
🔮 Prediction Endpoint
POST /predict
Request Body (JSON)

{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.8,
  "humidity": 82,
  "ph": 6.5,
  "rainfall": 202.9
}

Response

{
  "recommended_crop": "rice"
}

📊 Dataset Features
Feature	Description
N	Nitrogen content
P	Phosphorus content
K	Potassium content
temperature	Temperature (°C)
humidity	Relative humidity (%)
ph	Soil pH value
rainfall	Rainfall (mm)
🌍 Applications

    Smart Farming

    Precision Agriculture

    Farmer Decision Support Systems

    IoT Agriculture Integration (ESP32 Sensors)

🛠 Technologies Used

    Python

    FastAPI

    Scikit-learn

    Pandas

    NumPy

    Uvicorn
