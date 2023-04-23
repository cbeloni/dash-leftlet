import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestQualidadeAr:
    def teste_deve_criar_qualidade_ar(self):
        qualidade_ar = mixer.blend("leaftlet.QualidadeAr")
        assert qualidade_ar.pk == 1, "Should create a QualidadeAr instance"

    def teste_deve_criar_qualidade_ar_detalhes(self):
        detalhes = mixer.blend("leaftlet.QualidadeArDetalhes")
        assert detalhes.pk == 1, "Should create a QualidadeArDetalhes instance"