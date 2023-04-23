import requests
from cachetools import cached, LRUCache, TTLCache
import json
from datetime import datetime
from ..models import QualidadeAr

class QualidadeArDetalhes:
    def __init__(self, nome, indice, data):
        self.nome = nome
        self.indice = indice
        self.data = data

def listar_todos():
    lista_qualidade_ar2 = _get_cetesb()
    return lista_qualidade_ar2

def listar_detalhes():
    return _listar_detalhes()

@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def _get_cetesb():
    url = "https://arcgis.cetesb.sp.gov.br/server/rest/services/QUALAR/CETESB_QUALAR/MapServer/6/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:-5244191.63658331,%22ymin%22:-2739503.0937498696,%22xmax%22:-5165920.11961926,%22ymax%22:-2661231.5767858177,%22spatialReference%22:{%22wkid%22:102100}}&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100"
    response = requests.get(url)
    data = response.json()
    lista_qualidade_ar = []
    for feature in data['features']:
        nome = feature['attributes']['Nome']
        data = feature['attributes']['DATA'][:16]
        situacao_rede = feature['attributes']['Situacao_Rede']
        qualidade = feature['attributes']['Qualidade'] or 'Não coletado'
        tipo_rede = feature['attributes']['Tipo_Rede']
        endereco = feature['attributes']['Endereco']
        indice = feature['attributes']['Indice']
        poluente = feature['attributes']['POLUENTE']
        municipio = feature['attributes']['Municipio']

        lista_qualidade_ar.append(QualidadeAr(nome=nome,
                                              situacao_rede=situacao_rede,
                                              tipo_rede=tipo_rede,
                                              data=data,
                                              qualidade=qualidade,
                                              endereco=endereco,
                                              indice=indice,
                                              poluente=poluente,
                                              municipio=municipio))


    return lista_qualidade_ar

def _listar_detalhes():
    url = "https://arcgis.cetesb.sp.gov.br/server/rest/services/QUALAR/CETESB_QUALAR/MapServer/0/query?f=json&where=1=1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*"
    #json_data = '{"M1": 2, "TM1": 1678550400000, "M2": 2, "TM2": 1678546800000, "M3": 2, "TM3": 1678543200000, "M4": 2, "TM4": 1678539600000, "M5": 2, "TM5": 1678536000000}'
    response = requests.get(url)
    features = json.loads(response.content)['features']

    lista_completa_detalhes = []
    for f in features:
        print (f['attributes']['ID'])
        print(f['attributes']['STATNM'])
        nome = f['attributes']['STATNM']
        del f['attributes']['ID']
        del f['attributes']['STATNM']
        detalhes = _atribute_detalhes(f['attributes'], nome)
        lista_completa_detalhes.append(detalhes)
    return lista_completa_detalhes

def _atribute_detalhes(data, nome):
    lista_detalhes = []
    keys = list(data.keys())
    count = 24 if len(keys) > 24 else len(keys)
    for i in range(count, 0, -2):
        valueIndice = data[keys[i]]
        valueData = datetime.fromtimestamp(data[keys[i + 1]] / 1000).strftime("%Y-%m-%d %Hh")
        lista_detalhes.append(QualidadeArDetalhes(indice=valueIndice, data=valueData, nome=nome))
    return lista_detalhes

if __name__ == '__main__':
    detalhes = listar_detalhes()