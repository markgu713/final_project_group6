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
        fixed_acidity = request.form['fixed_acidity']
        volatile_acidity = request.form['volatile_acidity']
        citric_acid = request.form['citric_acid']
        residual_sugar =request.form['residual_sugar']
        chlorides = request.form['chlorides']
        free_sulfur_dioxide = request.form['free_sulfur_dioxide']
        total_sulfur_dioxide = request.form['total_sulfur_dioxide']
        density = request.form['density']
        pH = request.form['pH']
        sulphates = request.form['sulphates']
        alcohol = request.form['alcohol']
        
        # data = {'fixed acidity':  [fixed_acidity],
        #     'volatile acidity': [volatile_acidity],
        #     'citric acid': [citric_acid],
        #     'residual sugar': [residual_sugar],
        #     'chlorides': [chlorides],
        #     'free sulfur dioxide': [free_sulfur_dioxide],
        #     'total sulfur dioxide': [total_sulfur_dioxide],
        #     'density': [density],
        #     'pH': [pH],
        #     'sulphates': [sulphates],
        #     'alcohol': [alcohol]
        # }

        data = {'fixed acidity':  [5.8, fixed_acidity],
            'volatile acidity': [0.300, volatile_acidity],
            'citric acid': [0.33, citric_acid],
            'residual sugar': [3.5, residual_sugar],
            'chlorides': [0.033, chlorides],
            'free sulfur dioxide': [25.0, free_sulfur_dioxide],
            'total sulfur dioxide': [116.0, total_sulfur_dioxide],
            'density': [0.99057, density],
            'pH': [3.2, pH],
            'sulphates': [0.44, sulphates],
            'alcohol': [11.7, alcohol]
        }

        df = pd.DataFrame (data, columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)
        encoded_predictions = model.predict_classes(test_scaled[:2])
        if encoded_predictions[1] == 0:
            final_prediction = "Bad Quality!"
        else: 
            final_prediction = "Good Quality!"
        return render_template('index.html', prediction = final_prediction, fixed_acidity = fixed_acidity)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    # app.debug = True
    app.run()
