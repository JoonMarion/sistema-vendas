from django import forms

from apps.detalhevenda.models import DetalheVenda


class DetalheVendaForm(forms.ModelForm):
    class Meta:
        model = DetalheVenda
        fields = ('codigo_venda', 'cod_produto', 'quantidade_produto')