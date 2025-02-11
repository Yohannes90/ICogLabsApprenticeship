import pandas as pd # type: ignore
from flask import Flask, request, jsonify
import joblib  # type: ignore
from flask_cors import CORS # type: ignore


app = Flask(__name__)
CORS(app, origins=["http://backend:8000"])


# Load the trained model
model = joblib.load('./model/best_decision_tree_model.pkl')

# Define correct feature names
FEATURE_NAMES = ['buying_price', 'maintenance_cost', 'no_of_doors', 'no_of_persons', 'lug_boot', 'safety']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'features' not in data:
            return jsonify({'error': 'Missing "features" key in request body'}), 400

        # Convert input to DataFrame (ensuring feature names are preserved)
        features_df = pd.DataFrame([data['features']], columns=FEATURE_NAMES)
        # Make a prediction
        prediction = model.predict(features_df)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

