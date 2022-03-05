from django.contrib import admin
from .models import Card, Tag


class AdminCards(admin.ModelAdmin):
    list_display = ('id', 'texto', 'data_criacao', 'data_modificacao', 'tags')
    list_display_links = ('id', )
    search_fields = ('id', 'texto')
    list_filter = ('tags',)
    list_editable = ('texto', 'tags')

class AdminTags(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)
    list_editable = ('nome',)

admin.site.register(Card, AdminCards)
admin.site.register(Tag, AdminTags)

