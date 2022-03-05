from django.contrib import admin
from django.urls import path, include
from insights.views import CardViewSet, TagViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('card', CardViewSet, basename='Card')
router.register('tag', TagViewSet, basename='Tag')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
