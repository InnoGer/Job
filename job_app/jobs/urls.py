from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # Mappe la racine de l'application "jobs" à la vue job_list
]