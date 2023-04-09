from django.db import models


class QualidadeAr(models.Model):
    class Meta:
        db_table = 'qualidade_ar'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title
