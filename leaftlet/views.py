from django.shortcuts import render
from .qualidade_ar import listar_todos, listar_detalhes
import json

def home(request):
    return render(request, 'home.html')

def dash(request):
    detalhes = listar_detalhes()
    # print(json.json_dump(listar_todos()))
    todos = listar_todos()
    # print(todos)
    # Page from the theme
    return render(request, 'dash.html',{ "lista_qualidade_ar": todos,
                                                 "detalhes": detalhes})

