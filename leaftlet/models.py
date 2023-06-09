from django.db import models
from django.utils.timezone import now

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
    data_atual = models.DateTimeField(default=now, blank=True)

    def to_dict(self):
        return {
            "nome": self.nome,
            "situacao_rede": self.situacao_rede,
            "tipo_rede": self.tipo_rede,
            "data": self.data,
            "qualidade": self.qualidade,
            "endereco": self.endereco,
            "indice": self.indice,
            "poluente": self.poluente,
            "municipio": self.municipio,
            "data_atual": self.data_atual.isoformat() if self.data_atual else None
        }

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
