from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # la página principal de tu portfolio
]
