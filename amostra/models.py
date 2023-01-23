from django.db import models
class Amostra(models.Model):
    setor_local_avaliado=models.CharField(max_length=100, help_text='')
    hora_da_coleta=models.CharField(max_length=20, help_text='')
    data_da_coleta=models.CharField(max_length=20, help_text='')
    metodo_de_analise=models.CharField(max_length=100, help_text='')
    descricao_do_metodo=models.CharField(max_length=100, help_text='')
    entrada_no_laboratorio=models.CharField(max_length=20, help_text='')
    data_do_relatorio_de_ensaio=models.CharField(max_length=20, help_text='')
    unidade_de_medida=models.CharField(max_length=20, help_text='')
    volume=models.CharField(max_length=20, help_text='')
    conclusao=models.CharField(max_length=100, help_text='')
    observacao=models.CharField(max_length=100, help_text='')
    irregularidades=models.CharField(max_length=100, help_text='')
