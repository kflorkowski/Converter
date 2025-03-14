from django.urls import path
from . import views

urlpatterns = [
    path('', views.distance_conversion, name='distance_converter'),
    path('distance_converter', views.distance_conversion, name='distance_converter'),
    path('weight_converter', views.weight_conversion, name='weight_converter'),
    path('temperature_converter', views.temperature_conversion, name='temperature_converter'),
]