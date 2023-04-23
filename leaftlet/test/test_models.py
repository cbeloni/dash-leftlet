import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestQualidadeAr:
    def test_qualidade_ar(self):
        my_model = mixer.blend("leaftlet.QualidadeAr")
        assert my_model.pk == 1, "Should create a MyModel instance"
