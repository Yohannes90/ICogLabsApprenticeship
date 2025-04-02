from django.urls import path
from . import views


urlpatterns = [
    path('', views.predict_post_quality, name="predict_post_quality"),
]
