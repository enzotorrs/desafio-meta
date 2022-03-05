from django.urls import path
from insights import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addcard', views.addcard, name='addcard'),
    path('adcionacardpostado', views.adciona_card_postado, name='adcionacardpostado')
]
