import requests

dummy_data = {
    "features": [0] * 3000  # all zeros (safe test)
}

response = requests.post("http://127.0.0.1:8000/predict", json=dummy_data)
print(response.json())
