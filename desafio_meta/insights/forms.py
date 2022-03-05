from django import forms
import requests
import json


request_para_api = requests.get('http://desafio:8080/tag/')
print(request_para_api)
request_parseado = json.loads(request_para_api.content)
tags = []

for tag in request_parseado:
    tags.append((tag['nome'], tag['nome']))
    


class AdicionarCard(forms.Form):
    insight = forms.CharField(
                            label='Insight',
                            max_length=255,
                            widget=forms.TextInput(attrs={'placeholder':'Escreva aqui seu insight',
                                                           'class':'formulario-input card-texto'}))
    categoria = forms.ChoiceField(
                                label='Categoria',
                                choices=tags,
                                widget=forms.Select(attrs={'class':'formulario-input card-tag'}))
