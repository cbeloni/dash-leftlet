from django.db import models


class QualidadeAr(models.Model):
    class Meta:
        db_table = 'qualidade_ar'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    nome = models.CharField(max_length=255)
    situacao_rede = models.CharField(max_length=10)
    tipo_rede = models.CharField(max_length=5)
    data = models.DateField()
    qualidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    indice = models.IntegerField()
    poluente = models.CharField(max_length=10)
    municipio = models.CharField(max_length=255)

    def __str__(self):
        return self.title
