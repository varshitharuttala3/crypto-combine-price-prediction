from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("crypto_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "Crypto Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)

    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)