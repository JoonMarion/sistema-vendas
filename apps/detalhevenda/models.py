from django.db import models

from apps.produtos.models import Produto
from apps.vendas.models import Venda


# Create your models here.
class DetalheVenda(models.Model):
    cod_venda = models.ForeignKey(Venda, on_delete=models.CASCADE, primary_key=True)
    cod_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, default=None)
    quantidade_produto = models.DecimalField(max_digits=20, decimal_places=2)
