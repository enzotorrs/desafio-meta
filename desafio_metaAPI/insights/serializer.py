from rest_framework import serializers
from insights.models import Card, Tag


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'texto', 'data_criacao', 'data_modificacao', 'tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'nome']





