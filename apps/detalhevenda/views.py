from django.shortcuts import redirect, render

from .forms import DetalheVendaForm
from .models import DetalheVenda


def detalhe_venda_lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = DetalheVenda.objects.filter(descricao_produto__icontains=search)
    else:
        data['db'] = DetalheVenda.objects.all()
    return render(request, 'detalhevenda/lista.html', data)


def detalhe_venda_form(request):
    data = {'form': DetalheVendaForm()}
    return render(request, 'detalhevenda/form.html', data)


def detalhe_venda_create(request):
    if request.method == 'POST':
        form = DetalheVendaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('detalhe_venda_form')


def detalhe_venda_edit(request, pk):
    data = {'db': DetalheVenda.objects.get(pk=pk)}
    data['form'] = DetalheVendaForm(instance=data['db'])
    return render(request, 'detalhevenda/form.html', data)


def detalhe_venda_update(request, pk):
    data = {'db': DetalheVenda.objects.get(pk=pk)}
    form = DetalheVendaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('detalhe_venda_form')


def detalhe_venda_delete(request, pk):
    db = DetalheVenda.objects.get(pk=pk)
    db.delete()
    return redirect('detalhe_venda_lista')