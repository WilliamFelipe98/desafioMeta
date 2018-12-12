from rest_framework import serializers
from . import models

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        
        fields = ('id', 'nome', 'canal', 'valor', 'created_at',)
        fields = '__all__'
        model = models.Contato