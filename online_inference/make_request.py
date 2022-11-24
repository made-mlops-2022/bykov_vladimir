import requests
import pandas as pd
import numpy as np
import json

def make_request(path_to_data):
    data = pd.read_csv(path_to_data)
    data = data[['sex', 'cp', 'fbs', 'restecg', 'exang',
             'slope', 'ca', 'thal', 'age', 'trestbps', 'chol', 'thalach', 'oldpeak']]

    data["id"] = range(1, len(data) + 1)
    print(data.columns)
    response = None
    for row in data.to_dict(orient="records"):
        response = requests.get("http://0.0.0.0:8000/predict", json=row)
        print(response.json())


if __name__ == "__main__":
   make_request("./heart_cleveland_upload.csv")


