import pandas as pd
import numpy as np


def generate_data(size: int, path_to_synthetic_data: str) -> pd.DataFrame:
    columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal',
               'age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'condition']

    synthetic_data = pd.DataFrame(columns=columns)

    synthetic_data['sex'] = np.random.randint(0, 2, size)
    synthetic_data['cp'] = np.random.randint(0, 5, size)
    synthetic_data['fbs'] = np.random.randint(0, 2, size)

    synthetic_data['restecg'] = np.random.randint(0, 3, size)
    synthetic_data['exang'] = np.random.randint(0, 2, size)
    synthetic_data['slope'] = np.random.randint(0, 3, size)

    synthetic_data['ca'] = np.random.randint(0, 4, size)
    synthetic_data['thal'] = np.random.randint(0, 3, size)
    synthetic_data['age'] = np.array(np.random.normal(54, 9, size), dtype="int")

    synthetic_data['trestbps'] = np.array(np.random.normal(132, 17, size), dtype="int")
    synthetic_data['chol'] = np.array(np.random.normal(247, 51, size), dtype="int")
    synthetic_data['thalach'] = np.array(np.random.normal(150, 20, size), dtype="int")

    synthetic_data['oldpeak'] = np.random.exponential(1, size)
    synthetic_data['condition'] = np.random.randint(0, 2, size)

    synthetic_data.to_csv(path_to_synthetic_data)
    return synthetic_data


def extract_target_for_test(path_to_synthetic_data: str, predict_data_path: str) -> None:
    synthetic_data = pd.read_csv(path_to_synthetic_data)
    synthetic_data = synthetic_data.drop('condition', axis=1)
    synthetic_data.to_csv(predict_data_path)


if __name__ == "__main__":
    generate_data(50, "tests/test_data/synthetic_data.csv")
    extract_target_for_test("tests/test_data/synthetic_data.csv", "tests/test_data/data_for_predict.csv")
