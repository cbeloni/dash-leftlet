from leaftlet.service.qualidade_ar import Consulta
from leaftlet.dto.indicadores import Serie
_consulta = Consulta(False)

def prepara_grafico():
    detalhes = _consulta.principal_repository()

    # detalhes_ordenado = sorted(detalhes, key=lambda x: x.data_atual])

    lista_datas = [detalhe.data for detalhe in detalhes]
    lista_datas = list(dict.fromkeys(lista_datas))
    lista_municipios = [i.municipio for i in detalhes]
    lista_municipios = list(dict.fromkeys(lista_municipios))

    lista_series = []

    for municipio in lista_municipios:
        lista_indices = [detalhe.indice for detalhe in detalhes if detalhe.municipio == municipio]
        serie = Serie(name=municipio, type='line', stack='Total', data=lista_indices)
        lista_series.append(serie.to_dict())

    return lista_datas, lista_series, lista_municipios
