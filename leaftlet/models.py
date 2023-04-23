from django.db import models
from datetime import date


class QualidadeAr(models.Model):
    class Meta:
        db_table = 'qualidade_ar'

    nome = models.CharField(max_length=255)
    situacao_rede = models.CharField(max_length=10)
    tipo_rede = models.CharField(max_length=5)
    data = models.DateField(default=date.today)
    qualidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, null=True)
    indice = models.IntegerField(default=0)
    poluente = models.CharField(max_length=10)
    municipio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
