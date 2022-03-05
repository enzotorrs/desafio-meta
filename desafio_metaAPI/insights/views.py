from rest_framework import viewsets
from django.shortcuts import render
from insights.serializer import CardSerializer, TagSerializer
from insights.models import Card, Tag


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
