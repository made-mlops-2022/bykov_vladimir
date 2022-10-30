"""Scripts to train models"""

import logging
import sys
import hydra
from hydra.core.config_store import ConfigStore


# Import project modules
from src.enities.training_params import TrainingParams
from src.data.make_dataset import read_data, train_val_split
from src.features.build_features import Transformer, extract_target
from src.model.predict_model import evaluate, train_model, serialize_model, predict_model

# ConfigStore for caring parameters from configuration
# file in TrainingParams dataclass
cs = ConfigStore.instance()
cs.store(name="train", node=TrainingParams)

# setting logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False


def run_training_pipeline(training_params: TrainingParams) -> None:
    """Main training pipeline"""

    # read data
    logger.info(f"Reading dataset from {training_params.input_data_path}...")
    data = read_data(training_params.input_data_path)
    logger.info(f"  Dataset size: {data.shape[0]}\n"
                f"  Number of features: {data.shape[1]}")

    # transform data
    logger.info(f"Transforming data...")
    train_transformer = Transformer(training_params.feature_params)
    train_transformer.fit(data)
    transformed_data = train_transformer.transform()

    logger.info(f"Extracting target...")
    target = extract_target(transformed_data, training_params.feature_params)
    processed_data = transformed_data.drop(labels=training_params.feature_params.target, axis=1)

    # split data
    logger.info(f"Splitting data with parameters:\n"
                f"  validation size: {training_params.splitting_params.val_size}\n"
                f"  random state: {training_params.splitting_params.random_state}")
    train_data, val_data = train_val_split(processed_data, training_params.splitting_params)
    train_target, val_target = train_val_split(target, training_params.splitting_params)

    # train model
    logger.info(f"Training model with parameters:\n"
                f"  model: {training_params.model_params.model}\n"
                f"  random state: {training_params.model_params.random_state}")
    model = train_model(train_data, train_target, training_params)

    # validate model
    logger.info(f"Validating model...")
    predicted_target = predict_model(model, val_data)
    metrics = evaluate(predicted_target, val_target)

    logger.info(f"Metrics: {metrics}")

    # serialize model
    logger.info(f"Serializing model to {training_params.output_model_path} ...")
    serialize_model(model, training_params.output_model_path)


@hydra.main(version_base=None, config_path="../../configs/.", config_name="train_config")
def train_pipeline(config_params: TrainingParams) -> None:
    """Function to read terminal arguments"""
    run_training_pipeline(config_params)


if __name__ == "__main__":
    train_pipeline()
