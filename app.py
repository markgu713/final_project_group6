import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request
from keras.models import load_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# load model
model = load_model('model/model.h5')
# summarize model.
model.summary()

# data = {'fixed acidity':  [5.8, 7.1],
#         'volatile acidity': [0.300, 0.26],
#         'citric acid': [0.33, 0.49],
#         'residual sugar': [3.5, 2.2],
#         'chlorides': [0.033, 0.032],
#         'free sulfur dioxide': [25.0, 31.0],
#         'total sulfur dioxide': [116.0, 113.0],
#         'density': [0.99057, 0.9903],
#         'pH': [3.2, 3.37],
#         'sulphates': [0.44, 0.42],
#         'alcohol': [11.7, 12.9]
#         }
# df = pd.DataFrame (data, columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'])

from sklearn.preprocessing import MinMaxScaler
# X_scaler = MinMaxScaler().fit(df)
# test_scaled = X_scaler.transform(df)
# encoded_predictions = model.predict_classes(test_scaled[:2])
# print(f"Predicted classes: {encoded_predictions}")

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    """Return the homepage."""
    if request.method == 'POST':
        alcohol = request.form['alcohol']
        data = {'fixed acidity':  [5.8, 7.1],
            'volatile acidity': [0.300, 0.26],
            'citric acid': [0.33, 0.49],
            'residual sugar': [3.5, 2.2],
            'chlorides': [0.033, 0.032],
            'free sulfur dioxide': [25.0, 31.0],
            'total sulfur dioxide': [116.0, 113.0],
            'density': [0.99057, 0.9903],
            'pH': [3.2, 3.37],
            'sulphates': [0.44, 0.42],
            'alcohol': [11.7, 12.9]
        }
        df = pd.DataFrame (data, columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)
        encoded_predictions = model.predict_classes(test_scaled[:2])

        return render_template('index.html', prediction = encoded_predictions)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.debug = True
    app.run()
