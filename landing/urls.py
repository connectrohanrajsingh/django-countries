from .views import *
from django.urls import path

app_name = 'landing'

urlpatterns = [
    path('', LandingRequest.as_view(), name='landingRequest'),
    path('country-details/<str:country>',LandingRequest.as_view(), name='countryDetails'),
]
