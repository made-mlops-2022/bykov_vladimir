import unittest

from src.data.make_dataset import read_data, train_val_split
from src.enities.splitting_params import SplittingParams


class MakeDatasetTest(unittest.TestCase):
    def setUp(self) -> None:
        self.dataset_path = "./tests/test_data/synthetic_data.csv"
        self.target = "condition"

    def test_load_dataset(self):
        data = read_data(self.dataset_path)
        self.assertEqual(data.shape, (50, 15))
        assert self.target in data.keys()

    def test_split_dataset(self):
        val_size = 0.2
        splitting_params = SplittingParams(random_state=42, val_size=val_size)
        data = read_data(self.dataset_path)
        train, val = train_val_split(data, splitting_params)
        self.assertEqual(train.shape, (data.shape[0] * (1 - val_size), 15))
        self.assertEqual(val.shape, (data.shape[0] * val_size, 15))


if __name__ == '__main__':
    unittest.main()
