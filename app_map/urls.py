from django.urls import path
from . import views


urlpatterns = [
    path('api/proces/', views.ProcesListCreate.as_view()),
]
