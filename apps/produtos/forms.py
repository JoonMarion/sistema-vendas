from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['unidade', 'descricao', 'valor_unitario', 'estoque_minimo', 'quantidade_estoque', ]
        labels = {'unidade': 'Unidade', 'descricao': 'Descrição', 'valor_unitario': 'Valor Unitário',
                  'estoque_minimo': 'Estoque Mínimo', 'quantidade_estoque': 'Quantidade em Estoque', }
