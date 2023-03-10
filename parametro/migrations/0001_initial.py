# Generated by Django 4.1.5 on 2023-01-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_parametro', models.CharField(help_text='nome do agente químico', max_length=100)),
                ('unidade_de_medida_do_parametro', models.CharField(help_text='unidade de medida do agente químico', max_length=10)),
                ('resultado', models.CharField(help_text='valor mensurado do agente químico na amostra', max_length=10)),
                ('lq', models.CharField(help_text='valor de referência', max_length=100)),
            ],
        ),
    ]
