import requests
import json
from datetime import datetime
from ..models import QualidadeAr, QualidadeArDetalhes
from asgiref.sync import sync_to_async


class Consulta:
    save_database: bool

    def __init__(self, save_database=False):
        self.save_database = save_database

    def principal(self):
        url = "https://arcgis.cetesb.sp.gov.br/server/rest/services/QUALAR/CETESB_QUALAR/MapServer/6/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:-5244191.63658331,%22ymin%22:-2739503.0937498696,%22xmax%22:-5165920.11961926,%22ymax%22:-2661231.5767858177,%22spatialReference%22:{%22wkid%22:102100}}&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100"
        response = requests.get(url)
        data = response.json()
        lista_qualidade_ar = []
        for feature in data['features']:
            nome = feature['attributes']['Nome']
            data_split = feature['attributes']['DATA'].split(':')
            data = data_split[0] + ':' + data_split[1]
            situacao_rede = feature['attributes']['Situacao_Rede']
            qualidade = feature['attributes']['Qualidade'] or 'Não coletado'
            tipo_rede = feature['attributes']['Tipo_Rede']
            endereco = feature['attributes']['Endereco']
            indice = feature['attributes']['Indice']
            poluente = feature['attributes']['POLUENTE']
            municipio = feature['attributes']['Municipio']

            qualidade_ar: QualidadeAr = QualidadeAr(nome=nome,
                                                    situacao_rede=situacao_rede,
                                                    tipo_rede=tipo_rede,
                                                    data=data,
                                                    qualidade=qualidade,
                                                    endereco=endereco,
                                                    indice=indice,
                                                    poluente=poluente,
                                                    municipio=municipio)
            if self.save_database:
                sync_to_async(qualidade_ar.save())

            lista_qualidade_ar.append(qualidade_ar)
        return lista_qualidade_ar

    def detalhes(self):
        url = "https://arcgis.cetesb.sp.gov.br/server/rest/services/QUALAR/CETESB_QUALAR/MapServer/0/query?f=json&where=1=1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*"
        # json_data = '{"M1": 2, "TM1": 1678550400000, "M2": 2, "TM2": 1678546800000, "M3": 2, "TM3": 1678543200000, "M4": 2, "TM4": 1678539600000, "M5": 2, "TM5": 1678536000000}'
        response = requests.get(url)
        features = json.loads(response.content)['features']

        lista_completa_detalhes = []
        for f in features:
            nome = f['attributes']['STATNM']
            del f['attributes']['ID']
            del f['attributes']['STATNM']
            detalhes = self._atribute_detalhes(f['attributes'], nome)
            lista_completa_detalhes.append(detalhes)
        return lista_completa_detalhes

    def _atribute_detalhes(self, data, nome):
        lista_detalhes = []
        keys = list(data.keys())
        count = 24 if len(keys) > 24 else len(keys)
        for i in range(count, 0, -2):
            valueIndice = data[keys[i]]
            valueData = datetime.fromtimestamp(data[keys[i + 1]] / 1000).strftime("%Y-%m-%d %Hh")
            qualiadade_ar_detalhes = QualidadeArDetalhes(indice=valueIndice, data=valueData, nome=nome)

            if self.save_database:
                sync_to_async(qualiadade_ar_detalhes.save())

            lista_detalhes.append(qualiadade_ar_detalhes)
        return lista_detalhes
