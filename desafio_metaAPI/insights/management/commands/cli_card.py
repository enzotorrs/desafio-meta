from django.core.management.base import BaseCommand
from insights import models

class Command(BaseCommand):
    help = "escrebe no terminal em formato CSV os cards"

    def handle(self, *args, **kwargs):
        cards = models.Card.objects.all()
        for card in cards:
            print(f'{card.texto}, {card.tags}')
