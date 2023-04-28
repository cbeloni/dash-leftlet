from django.db import models

class QualidadeAr(models.Model):
    class Meta:
        db_table = 'qualidade_ar'

    nome = models.CharField(max_length=255)
    situacao_rede = models.CharField(max_length=10)
    tipo_rede = models.CharField(max_length=5)
    data = models.CharField(max_length=255) #todo: converter para date
    qualidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, null=True)
    indice = models.IntegerField(default=0, null=True)
    poluente = models.CharField(max_length=10, null=True)
    municipio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(vars(self))

class QualidadeArDetalhes(models.Model):

    class Meta:
        db_table = 'qualidade_ar_detalhes'

    nome = models.CharField(max_length=100)
    indice = models.DecimalField(max_digits=5, decimal_places=2 , null=True)
    data = models.CharField(max_length=255) #todo: converter para date
    # date.today().strftime('%Y-%m-%d')

    def __str__(self):
        return str(vars(self))
