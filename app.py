import json
from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)

# load the trained model

model = load('model.joblib')

# Route to serve the web page
from flask import send_from_directory

@app.route('/')
@app.route('/predict')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if  'features' not in data:
        return jsonify({'error': 'No input data provided'}), 400

    arr = np.array(data["features"]).reshape(1,-1)
    pred = model.predict(arr)[0]
    print(pred)
    return jsonify({"prediction": pred})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)