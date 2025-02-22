from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'
