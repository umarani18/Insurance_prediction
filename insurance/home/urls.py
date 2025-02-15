from django.urls import path
from .views import home, about, predict_insurance

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('predict/', predict_insurance, name='predict_insurance'),
]
