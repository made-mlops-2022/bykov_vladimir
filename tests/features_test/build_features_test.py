import unittest

from src.features.build_features import Transformer
from src.data.make_dataset import read_data
from src.enities.feature_params import FeatureParams


class BuildFeaturesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.params = FeatureParams(
            categorical_features=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'],
            numerical_features=['age', 'trestbps', 'chol', 'thalach', 'oldpeak'],
            features_to_drop=[],
            target='condition'
            )

    def test_transformer(self):
        data = read_data("./tests/test_data/synthetic_data.csv")
        transformer = Transformer(self.params)
        transformer.fit(data)
        data = transformer.transform()
        self.assertEqual(data.shape, (50, 15))


if __name__ == '__main__':
    unittest.main()
