from django.db import models

ESCOLHAS_UNIDADE = (
    ('UN', 'Unidade'),
    ('GR', 'Grama'),
    ('KG', 'Quilograma'),
    ('L', 'Litro'),
    ('ML', 'Mililitro'),
    ('PACOTE', 'Pacote'),
    ('MT', 'Metro'),
)


# Create your models here.
class Produto(models.Model):
    cod_produto = models.AutoField(primary_key=True)
    unidade = models.CharField(max_length=30, choices=ESCOLHAS_UNIDADE)
    descricao = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cod_produto} - {self.descricao}'