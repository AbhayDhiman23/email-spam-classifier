# backend/app/model.py

import joblib

# Load the trained pipeline (TF-IDF + LogisticRegression)
model = joblib.load('spam_classifier.pkl')

def predict_spam(message: str) -> str:
    """
    Predict whether the input message is spam or ham.

    Args:
        message (str): The email/message content.

    Returns:
        str: 'Spam' or 'Ham'
    """
    prediction = model.predict([message])[0]  # returns 0 or 1
    return 'Spam' if prediction == 1 else 'Ham'
