from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = ('id', 'curso', 'nome', 'email','comentario', 'avaliacao', 'criacao', 'ativo')

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliacao precisa ser um numero entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship
    #avaliacao = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliacao =serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail'
    )

    # # Primary Key Related field
    # avaliacao = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'atualizacao', 'ativo', 'avaliacao')


