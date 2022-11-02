import unittest
import os

from src.model.predict_model_pipeline import run_predict_pipeline
from src.enities.predict_params import PredictParams
from src.enities.feature_params import FeatureParams


class PredictModelPipeline(unittest.TestCase):

    def setUp(self) -> None:

        feature_params = FeatureParams(
            categorical_features=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'],
            numerical_features=['age', 'trestbps', 'chol', 'thalach', 'oldpeak'],
            features_to_drop=[],
            target='condition'
        )
        self.predict_params = PredictParams(
            input_data_path="tests/test_data/data_for_predict.csv",
            input_model_path="models/model_rf.pkl",
            output_predictions_path="tests/test_data/predictions.csv",
            feature_params=feature_params
        )

    def train_model_test(self):
        predictions = run_predict_pipeline(self.predict_params)
        self.assertEqual(predictions.shape, (50, 1))
        self.assertTrue(os.path.exists("tests/test_data/predictions.csv"))


if __name__ == '__main__':
    unittest.main()
