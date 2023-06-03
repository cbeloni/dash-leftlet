from django.shortcuts import render
from leaftlet.service.qualidade_ar import listar_todos, listar_detalhes
from leaftlet.service.indicadores import prepara_grafico
import json

def home(request):
    lista_qualidade_ar = listar_todos()
    with open('./static/js/grande-sp-pop.json', 'r') as f:
        grande_sp_indices = json.load(f)

    for feature in grande_sp_indices['features']:
        if feature['properties']['Indice'] is not None:
            matching_items = [item for item in lista_qualidade_ar if item.municipio.lower() == feature['properties']['Municipio'].lower() and item.indice is not None]
            feature['properties']['Indice'] = matching_items[0].indice if any(matching_items) else None

    contexto = {"grande_sp_indices": json.dumps(grande_sp_indices)}

    return render(request, 'home.html', contexto)

def dash(request):
    detalhes = listar_detalhes()
    todos = listar_todos()

    contexto = {"lista_qualidade_ar": todos,
                "detalhes": detalhes}

    return render(request, 'dash.html', contexto)

def indicadores(request):
    lista_datas, lista_series, lista_municipios = prepara_grafico()
    contexto = {"lista_datas": json.dumps(lista_datas),
                "lista_series": json.dumps(lista_series),
                "lista_municipios": json.dumps(lista_municipios)}
    return render(request, 'indicadores.html', contexto)

def tabelas(request):
    contexto = {}
    return render(request, 'tabelas.html', contexto)

if __name__ == '__main__':
    print('main')