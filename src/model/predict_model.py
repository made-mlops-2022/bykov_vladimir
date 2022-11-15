"""Scripts to use trained models to make predictions"""
import pickle

import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from typing import Dict, Union

# import project modules
from src.enities.training_params import TrainingParams

# define
SklearnClassifierModel = Union[RandomForestClassifier, GradientBoostingClassifier]


def train_model(data: pd.DataFrame, target: pd.DataFrame, train_params: TrainingParams) -> SklearnClassifierModel:
    if train_params.model_params.model == "RF":
        model = sklearn.ensemble.RandomForestClassifier(
            n_estimators=train_params.model_params.n_estimators,
            random_state=train_params.model_params.random_state
        )
    elif train_params.model_params.model == "GB":
        model = sklearn.ensemble.GradientBoostingClassifier(
            n_estimators=train_params.model_params.n_estimators,
            random_state=train_params.model_params.random_state
        )
    else:
        raise NotImplementedError()
    model.fit(data, target)
    return model


def predict_model(model: SklearnClassifierModel, data: pd.DataFrame) -> np.ndarray:
    predicted = model.predict(data)
    return predicted


def evaluate(target_predicted: np.ndarray, target: pd.DataFrame) -> Dict[str, float]:
    return {
        "f1": f1_score(target, target_predicted),
        "precision": precision_score(target, target_predicted),
        "recall": recall_score(target, target_predicted),
        "accuracy": accuracy_score(target, target_predicted)
    }


def serialize_model(model: SklearnClassifierModel, output_path: str) -> None:
    with open(output_path, "wb") as f:
        pickle.dump(model, f)


def load_model(model_path: str) -> SklearnClassifierModel:
    model = pickle.load(open(model_path, 'rb'))
    return model
