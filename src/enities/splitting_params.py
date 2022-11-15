from dataclasses import dataclass, field


@dataclass()
class SplittingParams:
    """Dataclass of splitting params from configuration file"""
    val_size: float = field(default=0.2)
    random_state: int = field(default=42)
