import pickle
import os
import pandas as pd
import click
import json
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score


@click.command("validate")
@click.option("--input-path", type=click.Path())
@click.option("--model-path", type=click.Path())
@click.option("--output-path", type=click.Path())
def validate(input_path: str, model_path: str, output_path: str):
    
    x_val = pd.read_csv(f"{input_path}/x_val.csv")
    y_val = pd.read_csv(f"{input_path}/y_val.csv")

    with open(f"{model_path}/rf_clf.pkl", "rb") as f:
        model = pickle.load(f)
    y_val = y_val["condition"]
    print(y_val)
    y_pred = model.predict(x_val)
    y_pred = y_pred[:,1]
    print(y_pred)
    
    metrics = {
        "f1": f1_score(y_val, y_pred),
        "precision": precision_score(y_val, y_pred),
        "recall": recall_score(y_val, y_pred),
        "accuracy": accuracy_score(y_val, y_pred)
    }

    os.makedirs(output_path, exist_ok=True)
    with open(f"{output_path}/metrics.json", "w") as f:
        json.dump(metrics, f)    


if __name__ == "__main__":
    validate()
