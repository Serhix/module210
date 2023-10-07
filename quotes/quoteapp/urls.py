from django.urls import path
from . import views
from .apps import QuoteappConfig

app_name = QuoteappConfig.name

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
]
