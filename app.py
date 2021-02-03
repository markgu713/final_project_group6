import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import joblib

# load model
deep_learning_model = load_model('model/deep_learning_model.h5')

logistic_regression_model = joblib.load('model/logistic_model.h5')

svm_model = joblib.load('model/SVM.h5')

#gradient_boosting_model = joblib.load('model/gradient_boosting_model.h5')

# summarize model.
# deep_learning_model.summary()

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
        residual_sugar = request.form['residual_sugar']
        chlorides = request.form['chlorides']
        free_sulfur_dioxide = request.form['free_sulfur_dioxide']
        total_sulfur_dioxide = request.form['total_sulfur_dioxide']
        density = request.form['density']
        pH = request.form['pH']
        sulphates = request.form['sulphates']
        alcohol = request.form['alcohol']
        winetype = request.form['winetype']

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
        #     'alcohol': [alcohol],
        #     'winetype': [winetype]
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
                'alcohol': [11.7, alcohol],
                'winetype': [0, winetype]
                }

        df = pd.DataFrame(data, columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                                         'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'winetype'])
        X_scaler = MinMaxScaler().fit(df)
        test_scaled = X_scaler.transform(df)

        deep_learning_encoded_predictions = deep_learning_model.predict_classes(test_scaled[:2])
        logistic_regression_encoded_predictions = logistic_regression_model.predict(test_scaled[:2])
        svm_encoded_predictions = svm_model.predict(test_scaled[:2])
        #gradient_boosting_encoded_predictions = gradient_boosting_model.predict(test_scaled[:2])



        if deep_learning_encoded_predictions[1] == 0:
            final_deep_learning_prediction = "Bad Quality!"
        else:
            final_deep_learning_prediction = "Good Quality!"

        if logistic_regression_encoded_predictions[1] == 0:
            final_logistic_regression_prediction = "Bad Quality!"
        else:
            final_logistic_regression_prediction = "Good Quality!"

        if svm_encoded_predictions[1] == 0:
            final_svm_prediction = "Bad Quality!"
        else:
            final_svm_prediction = "Good Quality!"

        # if gradient_boosting_encoded_predictions[1] < 7:
        #     final_gradient_boosting_prediction = "Bad Quality!"
        # else:
        #     final_gradient_boosting_prediction = "Good Quality!"

        return render_template('index.html', svm_prediction = final_svm_prediction, deep_learning_prediction=final_deep_learning_prediction, logistic_regression_prediction = final_logistic_regression_prediction, fixed_acidity=fixed_acidity, volatile_acidity=volatile_acidity, citric_acid=citric_acid, residual_sugar=residual_sugar, chlorides=chlorides, free_sulfur_dioxide=free_sulfur_dioxide, total_sulfur_dioxide=total_sulfur_dioxide, density=density, pH=pH, sulphates=sulphates, alcohol=alcohol, winetype=winetype)
    else:
        return render_template('index.html')

@app.route("/about")
@app.route("/about.html")
    def about():
        return render_template("about.html")

if __name__ == "__main__":
    # app.debug = True
    app.run()
