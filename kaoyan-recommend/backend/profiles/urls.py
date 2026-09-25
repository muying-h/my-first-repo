from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.create_profile),
]