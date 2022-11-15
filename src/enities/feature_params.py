from dataclasses import dataclass
from typing import List


@dataclass()
class FeatureParams:
    """Dataclass to care feature parameters from configuration file"""
    categorical_features: List[str]
    features_to_drop: List[str]
    numerical_features: List[str]
    target: str
