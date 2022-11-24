import uvicorn
from fastapi import FastAPI
import os
import pickle
import logging
from typing import List, Union, Optional
from pydantic import BaseModel

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from enities import HeartDisease, HeartDiseaseResponse


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(message)s")
file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

app = FastAPI()

ClassifierModel = Union[RandomForestClassifier, GradientBoostingClassifier]
model: Optional[ClassifierModel] = None


@app.get("/")
def home() -> str:
    """Base"""
    logger.info("Home")
    return "Heart Disease detection"


@app.get("/health")
def health() -> bool:
    """Check model is ready to predict"""
    return model is not None


@app.get("/predict", response_model = List[HeartDiseaseResponse])
def predict(request: HeartDisease) -> List[HeartDiseaseResponse]:
    """Function to send predictions"""
    logger.info(f"Predict")
    dataset = pd.DataFrame([request.dict()])
    ids = dataset["id"]
    dataset = dataset.drop("id", axis=1)
    
    logs = dataset.to_dict(orient="records")
    logger.info(f"Data:\n{logs}")
    predicts = model.predict(dataset)
    
    return list(
        HeartDiseaseResponse(condition=result, id=id_) for result, id_ in zip(predicts, ids)
    )


@app.on_event("startup")
def load_model() -> None:
    """Function for loading model from PATH_TO_MODEL environment variable"""
    global model
    path_to_model = os.getenv("PATH_TO_MODEL")
    if path_to_model is None:
        error_message = f"Error while reading PATH_TO_MODEL"
        logger.info(error_message)
        raise RuntimeError(error_message)
    else:
        with open(path_to_model, "rb") as f:
            model = pickle.load(f)
        logger.info(f"Model is loaded")


def make_predict(model: ClassifierModel, data: HeartDisease) -> List[HeartDiseaseResponse]:

    logger.info(f"Making predict")

    dataset = pd.DataFrame([data.dict()])
    ids = dataset["id"]
    dataset = dataset.drop("id", axis=1)
    logger.info(f"{input_df.columns}")
    predicts = model.predict(dataset)

    return list(
        HeartDiseaseResponse(condition=result, id=id_) for result, id_ in zip(predicts, ids)
    )


if __name__ == "__main__":
    logger.info(f"Start app")
    uvicorn.run("server:app", host="0.0.0.0", port=os.getenv("PORT", 8000))

