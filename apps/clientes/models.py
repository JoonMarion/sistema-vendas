from django.db import models


# Create your models here.
class Cliente(models.Model):
    cod_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    renda = models.DecimalField(max_digits=20, decimal_places=2)
    classe = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.cod_cliente} - {self.nome_cliente}'