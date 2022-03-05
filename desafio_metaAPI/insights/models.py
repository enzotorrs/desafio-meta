from django.db import models


class Tag(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Card(models.Model):
    texto = models.CharField(max_length=255)
    data_criacao = models.DateField()
    data_modificacao = models.DateField()
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.texto
