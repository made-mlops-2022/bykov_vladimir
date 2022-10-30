"""Main dataclass to read train configuration file"""

from dataclasses import dataclass

# import project modules
from src.enities.splitting_params import SplittingParams
from src.enities.model_params import ModelParams
from src.enities.feature_params import FeatureParams


@dataclass()
class TrainingParams:
    """Dataclass to care config params"""
    input_data_path: str
    output_model_path: str
    splitting_params: SplittingParams
    model_params: ModelParams
    feature_params: FeatureParams
