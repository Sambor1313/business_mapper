from rest_framework import serializers
from .models import Proces


class ProcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proces
        fields = ('id', 'name', 'description')