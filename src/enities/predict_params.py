"""Main dataclass to read predict configuration file"""

from dataclasses import dataclass

# import project modules
from src.enities.feature_params import FeatureParams


@dataclass()
class PredictParams:
    """Dataclass to care config params"""
    input_data_path: str
    input_model_path: str
    output_predictions_path: str
    feature_params: FeatureParams
