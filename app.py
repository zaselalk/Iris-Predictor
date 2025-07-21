import json
from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)

# load the trained model

model = load('model.joblib')

# Route to serve the web page
from flask import send_from_directory

# This route serves the index.html file when the root or /predict endpoint is accessed
@app.route('/')
@app.route('/predict')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Check if 'features' key exists in the input data
    if  'features' not in data:
        return jsonify({'error': 'No input data provided'}), 400

    # Convert the input features to a numpy array and reshape it for prediction
    arr = np.array(data["features"]).reshape(1,-1)

    # Make the prediction using the loaded model
    pred = model.predict(arr)[0]
   
    # Return the prediction as a JSON response
    return jsonify({"prediction": pred})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)