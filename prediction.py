import matplotlib.pyplot as plt
import requests
import base64
import json
import numpy as np
import pandas as pd

#load MNIST dataset
test = pd.read_csv("sign_mnist_test/sign_mnist_test.csv")
x_test = test.drop('label',axis=1).values
y_test = test['label'].values
# reshape data to have a single channel
x_test = x_test.reshape((-1,28,28, 1))
# normalize pixel values
x_test = x_test.astype('float32') / 255.0

#server URL
url = 'http://localhost:8501/v1/models/sign_classifier:predict'

def make_prediction(instances):
   data = json.dumps({"signature_name": "serving_default", "instances": instances.tolist()})
   headers = {"content-type": "application/json"}
   json_response = requests.post(url, data=data, headers=headers)
   predictions = json.loads(json_response.text)['predictions']
   return predictions

predictions = make_prediction(x_test[0:4])

for i, pred in enumerate(predictions):
   print(f"True Value: {y_test[i]}, Predicted Value: {np.argmax(pred)}")