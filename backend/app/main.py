from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


# Load trained model
model = joblib.load("spam_classifier.pkl")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Input schema: 3000 features from vectorized email
class EmailVector(BaseModel):
    features: list[float]  # list of 3000 float values

@app.get("/")
def home():
    return {"message": "✅ Spam classifier API is running!"}

@app.post("/predict")
def predict(input_data: EmailVector):
    # Convert input list to NumPy array and reshape
    vector = np.array(input_data.features).reshape(1, -1)

    # Predict using the loaded model
    prediction = model.predict(vector)[0]

    # Map prediction to label
    label = "Spam" if prediction == 1 else "Ham"
    return {"prediction": label}
