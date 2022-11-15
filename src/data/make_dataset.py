"""Scripts to download or generate data"""

import pandas as pd
from sklearn.model_selection import train_test_split
from src.enities.splitting_params import SplittingParams


def read_data(data_path: str) -> pd.DataFrame:
    """Reads data from data_path and return pd.DataFrame"""
    data = pd.read_csv(data_path)
    return data


def train_val_split(
        data: pd.DataFrame, split_params: SplittingParams
) -> [pd.DataFrame, pd.DataFrame]:
    """Function to split data according to splitting parameters"""
    train, val = train_test_split(data, test_size=split_params.val_size,
                                  random_state=split_params.random_state)

    return train, val
