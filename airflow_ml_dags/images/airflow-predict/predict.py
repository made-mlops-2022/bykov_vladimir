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
def predict(input_path: str, model_path: str, output_path: str):
    
    data = pd.read_csv(f"{input_path}/train_data.csv")
    
    print(model_path)
    with open(f"{model_path}/rf_clf.pkl", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(data)
    predictions = pd.DataFrame(y_pred)

    os.makedirs(output_path, exist_ok=True) 
    predictions.to_csv(f"{output_path}/predictions.csv")


if __name__ == "__main__":
    predict()
