"""Testing predict module"""
import unittest
from fastapi.testclient import TestClient
from server import app, load_model

class TestApp(unittest.TestCase):
    def setUp(self):
        load_model()
        self.client = TestClient(app)

    def test_predict(self):

        # all is ok
        request = {'id': 1,
                   'age': 69.0, 
                   'sex': 1, 
                   'cp': 0, 
                   'trestbps': 160.0, 
                   'chol': 234.0, 
                   'fbs': 1, 
                   'restecg': 2, 
                   'thalach': 131.0, 
                   'exang': 0, 
                   'oldpeak': 0.1, 
                   'slope': 1, 
                   'ca': 1, 
                   'thal': 0}

        response = self.client.get("http://0.0.0.0:8000/predict", json=request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': 1, 'condition': 0}])


        # no "id" field
        request = {'age': 69.0, 
                   'sex': 1, 
                   'cp': 0, 
                   'trestbps': 160.0, 
                   'chol': 234.0, 
                   'fbs': 1, 
                   'restecg': 2, 
                   'thalach': 131.0, 
                   'exang': 0, 
                   'oldpeak': 0.1, 
                   'slope': 1, 
                   'ca': 1, 
                   'thal': 0}

        response = self.client.get("http://0.0.0.0:8000/predict", json=request)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'detail': [{'loc': ['body', 'id'],
                                                       'msg': 'field required', 
                                                       'type': 'value_error.missing'}]})
        
        # invalid sex value
        request = {'id': 10,
                   'age': 4.0, 
                   'sex': 4, 
                   'cp': 0, 
                   'trestbps': 160.0, 
                   'chol': 234.0, 
                   'fbs': 1, 
                   'restecg': 2, 
                   'thalach': 131.0, 
                   'exang': 0, 
                   'oldpeak': 0.1, 
                   'slope': 1, 
                   'ca': 1, 
                   'thal': 0}

        response = self.client.get("http://0.0.0.0:8000/predict", json=request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'detail': [{'msg': 'ValueError: invalid sex value'}]})



if __name__ == "__main__":
    unittest.main()
