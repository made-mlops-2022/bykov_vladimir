from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import pandas as pd
import click

@click.command("train")
@click.option("--input-path", type=click.Path())
@click.option("--output-path", type=click.Path())
def train(input_path: str, output_path: str):
    
    x_train = pd.read_csv(f"{input_path}/x_train.csv")
    y_train = pd.read_csv(f"{input_path}/y_train.csv")

    model = RandomForestClassifier(
            n_estimators=20,
            random_state=89
    )
    model.fit(x_train, y_train)
    
    os.makedirs(output_path, exist_ok=True)
    with open(f"{output_path}/rf_clf.pkl", "wb") as f:
        pickle.dump(model, f)    


if __name__ == "__main__":
    train()
