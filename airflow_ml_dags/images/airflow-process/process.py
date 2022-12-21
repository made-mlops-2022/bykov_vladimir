import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import click
import os


@click.command("process")
@click.option("--input-path", type=click.Path())
@click.option("--output-path", type=click.Path())
def process(input_path: str, output_path: str):
    
    print(input_path)
    data = pd.read_csv(f"{input_path}/data.csv")
    target = pd.read_csv(f"{input_path}/target.csv")
    
    print(data)
    # process data
    imputer = SimpleImputer(strategy="most_frequent")
    processed = imputer.fit_transform(data)
    processed_data = pd.DataFrame(processed, columns=data.columns)
    
    os.makedirs(output_path, exist_ok=True)
    processed_data.to_csv(f"{output_path}/train_data.csv", index=False)

    # save target to new folder
    target.to_csv(f"{output_path}/train_target.csv", index=False)
    

if __name__ == "__main__":
    process()
