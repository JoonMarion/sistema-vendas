from django.shortcuts import redirect, render

from .forms import VendaForm
from .models import Venda


def venda_lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Venda.objects.filter(cod_venda__icontains=search) | Venda.objects.filter(
            cod_cliente=search) | Venda.objects.filter(data_venda__icontains=search)
    else:
        data['db'] = Venda.objects.all()
    return render(request, 'vendas/lista.html', data)


def venda_form(request):
    data = {'form': VendaForm()}
    return render(request, 'vendas/form.html', data)


def venda_create(request):
    if request.method == 'POST':
        form = VendaForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('detalhe_venda_form')


def venda_edit(request, pk):
    data = {'db': Venda.objects.get(pk=pk)}
    data['form'] = VendaForm(instance=data['db'])
    return render(request, 'vendas/form.html', data)


def venda_update(request, pk):
    data = {'db': Venda.objects.get(pk=pk)}
    form = VendaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('venda_form')


def venda_delete(request, pk):
    db = Venda.objects.get(pk=pk)
    db.delete()
    return redirect('venda_lista')
