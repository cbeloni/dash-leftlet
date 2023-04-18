from django.shortcuts import render
from .qualidade_ar import listar_todos, listar_detalhes
import json

def home(request):
    lista_qualidade_ar = listar_todos()
    print(lista_qualidade_ar)
    with open('./static/js/grande-sp-pop.json', 'r') as f:
        grande_sp_indices = json.load(f)

    for feature in grande_sp_indices['features']:
        if feature['properties']['Indice'] is not None:
            matching_items = [item for item in lista_qualidade_ar if item.municipio.lower() == feature['properties']['Municipio'].lower() and item.indice is not None]
            feature['properties']['Indice'] = matching_items[0].indice if any(matching_items) else None

    contexto = {"grande_sp_indices": json.dumps(grande_sp_indices),
                "mapa_active": "active"}

    return render(request, 'home.html', contexto)

def dash(request):
    detalhes = listar_detalhes()
    todos = listar_todos()

    contexto = {"lista_qualidade_ar": todos,
                "detalhes": detalhes,
                "dash_active": "active"}

    return render(request, 'dash.html', contexto)

if __name__ == '__main__':
    print('main')