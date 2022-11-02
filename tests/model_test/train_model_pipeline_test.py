import unittest
import os

from src.model.train_model_pipeline import run_training_pipeline
from src.enities.training_params import TrainingParams
from src.enities.splitting_params import SplittingParams
from src.enities.model_params import ModelParams
from src.enities.feature_params import FeatureParams


class TrainModelPipelineTests(unittest.TestCase):

    def setUp(self) -> None:
        split_params = SplittingParams(
            val_size=0.2,
            random_state=42
        )
        model_params = ModelParams(
            model="RF",
            random_state=42,
            n_estimators=100
        )
        feature_params = FeatureParams(
            categorical_features=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'],
            numerical_features=['age', 'trestbps', 'chol', 'thalach', 'oldpeak'],
            features_to_drop=[],
            target='condition'
        )

        self.train_params = TrainingParams(
            input_data_path="tests/test_data/synthetic_data.csv",
            output_model_path="",
            splitting_params=split_params,
            model_params=model_params,
            feature_params=feature_params
        )

    def train_model_test(self):
        metrics = run_training_pipeline(self.train_params)

        self.assertTrue(metrics["accuracy"] > 0)
        self.assertTrue(metrics["recall"] > 0)
        self.assertTrue(metrics["f1"] > 0)
        self.assertTrue(metrics["precision"] > 0)

        self.assertTrue(os.path.exists("./models/model.pkl"))


if __name__ == '__main__':
    unittest.main()
