from flask import Flask, request, jsonify
import os
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "Crypto Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    
    # Dummy prediction (replace later with real model)
    prediction = float(np.mean(features))
    
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)