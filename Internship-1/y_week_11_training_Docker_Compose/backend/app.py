import requests
from flask import Flask, request, jsonify
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app, origins=["*"])

ML_SERVICE_URL = "http://ml_service:5000/predict"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        response = requests.post(ML_SERVICE_URL, json=data)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
