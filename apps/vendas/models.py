from django.db import models

from apps.clientes.models import Cliente


# Create your models here.
class Venda(models.Model):
    cod_venda = models.AutoField(primary_key=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField()

    def __str__(self):
        return f'{self.cod_venda}'