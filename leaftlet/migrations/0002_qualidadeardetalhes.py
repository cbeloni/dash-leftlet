# Generated by Django 4.2 on 2023-04-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaftlet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualidadeArDetalhes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('indice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField()),
            ],
            options={
                'db_table': 'qualidade_ar_detalhes',
            },
        ),
    ]
