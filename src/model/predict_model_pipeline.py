"""Scripts to predict"""

import logging
import sys
import hydra
from hydra.core.config_store import ConfigStore
import pandas as pd

# Import project modules
from src.enities.predict_params import PredictParams
from src.data.make_dataset import read_data
from src.features.build_features import Transformer
from src.model.predict_model import predict_model, load_model


# ConfigStore for caring parameters from configuration
# file in TrainingParams dataclass
cs = ConfigStore.instance()
cs.store(name="predict", node=PredictParams)


# setting logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False


def run_predict_pipeline(predict_params: PredictParams):
    # read data
    logger.info(f"Reading data from {predict_params.input_data_path}...")
    data = read_data(predict_params.input_data_path)

    # load model
    logger.info(f"Loading model from {predict_params.input_model_path}...")
    model = load_model(predict_params.input_model_path)

    # transform data
    logger.info(f"Transforming data...")
    transformer = Transformer(predict_params.feature_params)
    transformer.fit(data)
    data = transformer.transform()

    # predict
    logger.info(f"Getting predictions...")
    predictions = predict_model(model, data)

    # save prediction
    logger.info(f"Setting prediction to {predict_params.output_predictions_path}...")
    pd.DataFrame(predictions).to_csv(predict_params.output_predictions_path)

    return predictions


@hydra.main(version_base=None, config_path="../../configs/.", config_name="predict_config")
def predict_pipeline(config_params: PredictParams) -> None:
    """Function to read terminal arguments"""
    run_predict_pipeline(config_params)


if __name__ == "__main__":
    predict_pipeline()
