import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestQualidadeAr:
    def test_qualidade_ar(self):
        qualidade_ar = mixer.blend("leaftlet.QualidadeAr")
        assert qualidade_ar.pk == 1, "Should create a QualidadeAr instance"
