from django.urls import path, include
from rest_framework import routers
from . import views

app_name: str = 'api'

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register('', views.Records, basename='records')

urlpatterns = [
    path('', include(default_router.urls)),
    path('/', include(default_router.urls)),
]
