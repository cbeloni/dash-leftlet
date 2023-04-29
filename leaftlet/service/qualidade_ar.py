import requests
from cachetools import cached, LRUCache, TTLCache

from leaftlet.integrations.cetesb import Consulta
from ..integrations import cetesb

_consulta: Consulta = cetesb.Consulta(save_database=False)

def listar_todos():
    return _get_cetesb()

def listar_detalhes():
    return _listar_detalhes()

@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def _get_cetesb():
    return _consulta.principal()

@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def _listar_detalhes():
    return _consulta.detalhes()

if __name__ == '__main__':
    detalhes = listar_todos()