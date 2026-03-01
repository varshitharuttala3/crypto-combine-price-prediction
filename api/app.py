from flask import Flask, request, render_template_string
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model safely
model_path = os.path.join(os.path.dirname(__file__), "..", "model.pkl")
model = pickle.load(open(model_path, "rb"))

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Crypto Price Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #141e30, #243b55);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            width: 350px;
            text-align: center;
        }

        h2 {
            margin-bottom: 20px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #243b55;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background-color: #141e30;
        }

        .result {
            margin-top: 15px;
            font-weight: bold;
            color: #243b55;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>Crypto Price Prediction</h2>
        <form action="/predict" method="post">
            <input type="text" name="feature1" placeholder="Feature 1" required>
            <input type="text" name="feature2" placeholder="Feature 2" required>
            <input type="text" name="feature3" placeholder="Feature 3" required>
            <input type="text" name="feature4" placeholder="Feature 4" required>
            <input type="text" name="feature5" placeholder="Feature 5" required>
            <button type="submit">Predict</button>
        </form>

        <div class="result">
            {{ prediction_text }}
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_form, prediction_text="")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        f1 = float(request.form["feature1"])
        f2 = float(request.form["feature2"])
        f3 = float(request.form["feature3"])
        f4 = float(request.form["feature4"])
        f5 = float(request.form["feature5"])

        features = np.array([[f1, f2, f3, f4, f5]])
        prediction = model.predict(features)

        result_text = f"Predicted Price: {prediction[0]:,.2f}"

        return render_template_string(html_form, prediction_text=result_text)

    except Exception as e:
        return render_template_string(html_form, prediction_text="Error in input values")
