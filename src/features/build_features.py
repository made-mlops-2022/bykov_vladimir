"""Scripts to turn raw data into features for modeling"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin


# import project modules
from src.enities.feature_params import FeatureParams


def transform_numerical_feature(numerical_data) -> pd.DataFrame:
    numerical_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(missing_values=np.nan, strategy="most_frequent")),
        ]
    )
    numerical_pipeline.fit(numerical_data)
    numerical_pipeline.transform(numerical_data)
    return numerical_data


def transform_categorical_feature(categorical_data) -> pd.DataFrame:
    categorical_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(missing_values=np.nan, strategy="most_frequent")),
            ("ohe", OneHotEncoder()),
        ]
    )
    categorical_pipeline.fit(categorical_data)
    categorical_pipeline.transform(categorical_data)
    return pd.DataFrame(categorical_data)


class Transformer(BaseEstimator, TransformerMixin):

    def __init__(self, feature_params: FeatureParams):
        self.numerical_features = list(feature_params.numerical_features)
        self.categorical_features = list(feature_params.categorical_features)
        self.data = None

    def fit(self, data: pd.DataFrame):
        self.data = data
        return self

    def transform(self) -> pd.DataFrame:
        self.data[self.numerical_features] = \
            transform_numerical_feature(self.data[self.numerical_features])
        self.data[self.categorical_features] = \
            transform_numerical_feature(self.data[self.categorical_features])
        return self.data


def extract_target(data: pd.DataFrame, features_params: FeatureParams) -> pd.DataFrame:
    """Extracts target, returns pd.Series of target feature"""
    target = data[features_params.target]
    return target
