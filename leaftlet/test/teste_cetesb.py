import pytest
from mixer.backend.django import mixer
from django.test import TestCase, Client
from leaftlet.integrations.cetesb import Consulta
from datetime import datetime, timedelta

_consulta = Consulta(False)

@pytest.mark.django_db
class TestCetesb(TestCase):

    def teste_deve_obter_ultimos_dez_registros(self):
        for i in range(1, 20):
            qualidade_ar = mixer.blend("leaftlet.QualidadeAr", data_atual=datetime.now() - timedelta(days=i))
            qualidade_ar.save()
        detalhes = _consulta.principal_repository()
        print(detalhes)

        assert len(detalhes) == 9, "Deve recuperar os últimos 9 registros"