#from django.shortcuts import render #To delete
from .models import Proces
from .serializers import ProcesSerializer
from rest_framework import generics

# Create your views here.
class ProcesListCreate(generics.ListCreateAPIView):
    """
    docstring
    """
    queryset = Proces.objects.all()
    serializer_class = ProcesSerializer