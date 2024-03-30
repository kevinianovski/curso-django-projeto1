from django.urls import path
from recipes.views import my_home, my_contatos, my_sobre

urlpatterns = [
    path('', my_home),
    path('sobre/', my_sobre),
    path('contatos/', my_contatos),
]