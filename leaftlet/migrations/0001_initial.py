# Generated by Django 4.2 on 2023-04-09 14:51

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
                ('title', models.CharField(max_length=200)),
                ('seconds', models.IntegerField()),
            ],
            options={
                'db_table': 'qualidade_ar',
            },
        ),
    ]
