# Generated by Django 4.1.5 on 2023-01-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amostra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setor_local_avaliado', models.CharField(max_length=100)),
                ('hora_da_coleta', models.CharField(max_length=20)),
                ('data_da_coleta', models.CharField(max_length=20)),
                ('metodo_de_analise', models.CharField(max_length=100)),
                ('descricao_do_metodo', models.CharField(max_length=100)),
                ('entrada_no_laboratorio', models.CharField(max_length=20)),
                ('data_do_relatorio_de_ensaio', models.CharField(max_length=20)),
                ('unidade_de_medida', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=20)),
                ('conclusao', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=100)),
                ('irregularidades', models.CharField(max_length=100)),
            ],
        ),
    ]
