import click
import pandas as pd
from sklearn.model_selection import train_test_split
import os


@click.command("split")
@click.option("--input-path", type=click.Path())
@click.option("--output-path", type=click.Path())
def split(input_path: str, output_path: str, test_size=0.2):

    data = pd.read_csv(f"{input_path}/train_data.csv")
    target = pd.read_csv(f"{input_path}/train_target.csv")

    x_train, x_val, y_train, y_val = train_test_split(data, target, test_size=test_size)


    os.makedirs(output_path, exist_ok=True)
    x_train.to_csv(f"{output_path}/x_train.csv", index=False)
    x_val.to_csv(f"{output_path}/x_val.csv", index=False)
    y_train.to_csv(f"{output_path}/y_train.csv", index=False)
    y_val.to_csv(f"{output_path}/y_val.csv", index=False)
    

if __name__ == "__main__":
    split()
