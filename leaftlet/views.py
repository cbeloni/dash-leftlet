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

    return render(request, 'home.html', { "grande_sp_indices": json.dumps(grande_sp_indices)})

def dash(request):
    detalhes = listar_detalhes()
    # print(json.json_dump(listar_todos()))
    todos = listar_todos()
    # print(todos)
    # Page from the theme
    return render(request, 'dash.html',{ "lista_qualidade_ar": todos,
                                                 "detalhes": detalhes})

if __name__ == '__main__':
    print('main')