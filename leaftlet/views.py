from django.shortcuts import render
from .qualidade_ar import listar_todos, listar_detalhes

def home(request):
    return render(request, 'home.html')

def dash(request):
    detalhes = listar_detalhes()
    # Page from the theme
    return render(request, 'dash.html',{ "lista_qualidade_ar": listar_todos(),
                                                 "detalhes": detalhes})