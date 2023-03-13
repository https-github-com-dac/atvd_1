from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=250)
    data_de_lancamento = models.DateField()


class Editora(models.Model):
    codigo = models.BigAutoField(primary_key=True)  # default especificado em apps.py
    local_de_origem = models.CharField(max_length=250)
    nome_fantasia = models.CharField(max_length=250)
