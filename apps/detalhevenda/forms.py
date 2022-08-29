from django import forms

from apps.detalhevenda.models import DetalheVenda


class DetalheVendaForm(forms.ModelForm):
    class Meta:
        model = DetalheVenda
        fields = ('cod_venda', 'cod_produto', 'quantidade_produto')
        labels = {'cod_produto': 'Produto', 'quantidade_produto': 'Quantidade', }
