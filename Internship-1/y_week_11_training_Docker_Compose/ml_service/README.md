# ML Service - Decision Tree Model

## Overview

This is a Flask-based API that serves predictions from a Decision Tree Classifier model, which is trained to classify data based on a set of features. The model is optimized using `GridSearchCV` and the best model is served via this API.

## Project Structure

- `app.py`: The main Flask application file that exposes the `/predict` API endpoint.
- `model/best_decision_tree_model.pkl`: The saved Decision Tree model file.
- `config.py`: Contains the path to the saved model.
- `Dockerfile`: Docker configuration for containerizing the application.
- `requirements.txt`: The list of required Python packages.

## Requirements

To run this project locally, you will need:

- Python 3.x
- The following Python libraries (listed in `requirements.txt`):
  - Flask
  - scikit-learn
  - joblib
  - numpy

You can install the dependencies using:

```bash
pip install -r requirements.txt
