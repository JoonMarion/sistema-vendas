from django import forms

from apps.vendas.models import Venda


class DateInput(forms.DateInput):
    input_type = 'date'


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('cod_venda', 'cod_cliente', 'data_venda')

        labels = {'cod_cliente': 'Cliente', 'data_venda': 'Data da Venda',}

        widgets = {
            'data_venda': DateInput(),
        }