from django.shortcuts import render
from django.http import HttpResponse

def my_home(request):
    return render(request, 'recipes/pages/home.html', context = { 'name': 'kevin'})

def my_sobre(request):
    return HttpResponse('SOBRE')

def my_contatos(request):
    return HttpResponse('CONTATOS')
