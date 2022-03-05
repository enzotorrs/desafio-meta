from insights import forms
from django.shortcuts import render, redirect
import datetime
from insights.forms import AdicionarCard
from requests import get, post
import json


def index(request):
    resposta_api = get('http://localhost:8080/card/')
    dados = {
        'insights': json.loads(resposta_api.content)
    }
    return render(request, 'index.html', context=dados)


def addcard(request):
    form = AdicionarCard()
    contexto = {
        'form':form
    }
    return render(request, 'adicionar-card.html', contexto)

def adciona_card_postado(request):
    if request.method == 'POST':
        form = forms.AdicionarCard(request.POST)
        insight = {'texto': form['insight'].value(),
                   'tags':form['categoria'].value(),
                   'data_criacao': datetime.date.today(),
                   'data_modificacao': datetime.date.today()}
        post('http://localhost:8080/card/', data=insight)

        return redirect('index')


