from django.db import models


# Create your models here.
class Cliente(models.Model):
    cod_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    classe = models.CharField(max_length=1)
