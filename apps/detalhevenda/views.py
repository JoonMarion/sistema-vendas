from django.shortcuts import redirect, render

from .forms import DetalheVendaForm
from .models import DetalheVenda
from ..produtos.models import Produto
from ..vendas.models import Venda


def detalhe_venda_lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = DetalheVenda.objects.filter(
            cod_venda=search) | DetalheVenda.objects.filter(
            cod_produto=search)
    else:
        data['db'] = DetalheVenda.objects.all()
    return render(request, 'detalhevenda/lista.html', data)


def detalhe_venda_form(request):
    data = {'form': DetalheVendaForm()}
    return render(request, 'detalhevenda/form.html', data)


def atualiza_estoque(quantidade, cod_produto):
    db = Produto.objects.get(pk=cod_produto)
    db.quantidade_estoque = float(db.quantidade_estoque) - quantidade
    db.save()
    return redirect('detalhe_venda_form')


def valor_total(request, quantidade, cod_produto):
    data = Produto.objects.get(pk=cod_produto)
    resultado = float(data.valor_unitario) * float(quantidade)
    print(resultado)
    return render(request, 'detalhevenda/form.html', {'resultado': resultado})


def detalhe_venda_create(request):
    if request.method == 'POST':
        form = DetalheVendaForm(request.POST or None)
        post_data = request.POST
        post_data._mutable = True
        post_data['cod_venda'] = Venda.objects.latest('cod_venda')
        post_data._mutable = False
        if form.is_valid():
            atualiza_estoque(float(request.POST.get('quantidade_produto')), request.POST.get('cod_produto'))
            valor_total(request, float(request.POST.get('quantidade_produto')), request.POST.get('cod_produto'))
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
