import os
from django.shortcuts import render
from .post_quality_predictor import PostQualityPredictor


def predict_post_quality(request):
    prediction = reputation = interaction = None
    if request.method == 'POST':
        try:
            reputation = int(request.POST.get('reputation'))
            interaction = float(request.POST.get('interaction'))

            predictor = PostQualityPredictor()
            file_path = os.path.join(os.path.dirname(__file__), './post_quality_model.joblib')
            predictor.load_model(file_path)
            prediction = predictor.predict(reputation, interaction)
        except(ValueError, TypeError):
            prediction = "Invalid Input"

    return render(request, 'predict.html', {'prediction': prediction, 'reputation': reputation, 'interaction': interaction})
