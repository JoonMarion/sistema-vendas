from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cpf', 'email', 'renda', 'classe')