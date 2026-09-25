from django.urls import path
from . import views

urlpatterns = [
    path('universities/', views.list_universities),
]