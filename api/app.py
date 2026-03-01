from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../model.pkl")

model = pickle.load(open(model_path, "rb"))

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Crypto Price Prediction</title>
</head>
<body>
    <h2>Crypto Price Prediction</h2>
    <form method="POST">
        <input type="number" step="any" name="feature1" placeholder="Enter Feature 1" required><br><br>
        <input type="number" step="any" name="feature2" placeholder="Enter Feature 2" required><br><br>
        <button type="submit">Predict</button>
    </form>
    <h3>{{ prediction_text }}</h3>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    if request.method == "POST":
        f1 = float(request.form["feature1"])
        f2 = float(request.form["feature2"])
        prediction = model.predict([[f1, f2]])
        prediction_text = f"Predicted Price: {prediction[0]}"
    return render_template_string(html, prediction_text=prediction_text)
