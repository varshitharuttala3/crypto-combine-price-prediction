from flask import Flask, request, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Crypto Price Prediction</title>
</head>
<body>
    <h2>Crypto Price Prediction</h2>
    <form action="/predict" method="post">
        <input type="text" name="feature1" placeholder="Enter Feature 1"><br><br>
        <input type="text" name="feature2" placeholder="Enter Feature 2"><br><br>
        <button type="submit">Predict</button>
    </form>
    <h3>{{ prediction_text }}</h3>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_form)

@app.route("/predict", methods=["POST"])
def predict():
    f1 = float(request.form["feature1"])
    f2 = float(request.form["feature2"])

    prediction = model.predict([[f1, f2]])

    return render_template_string(html_form, prediction_text=f"Prediction: {prediction[0]}")

if __name__ == "__main__":
    app.run()
