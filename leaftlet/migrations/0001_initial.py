# Generated by Django 4.2 on 2023-04-23 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QualidadeAr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('situacao_rede', models.CharField(max_length=10)),
                ('tipo_rede', models.CharField(max_length=5)),
                ('data', models.CharField(max_length=255)),
                ('qualidade', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255, null=True)),
                ('indice', models.IntegerField(default=0)),
                ('poluente', models.CharField(max_length=10)),
                ('municipio', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'qualidade_ar',
            },
        ),
        migrations.CreateModel(
            name='QualidadeArDetalhes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('indice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'qualidade_ar_detalhes',
            },
        ),
    ]
