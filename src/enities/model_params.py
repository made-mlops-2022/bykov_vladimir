from dataclasses import dataclass, field


@dataclass()
class ModelParams:
    """Dataclass of model parameters from configuration file"""
    model: str
    random_state: int = field(default=42)
    n_estimators: int = field(default=100)
