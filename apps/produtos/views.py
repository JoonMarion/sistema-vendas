from django.shortcuts import redirect, render

from .forms import ProdutoForm
from .models import Produto


def produto_lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produto.objects.filter(descricao_produto__icontains=search) | Produto.objects.filter(cod_produto__icontains=search)
    else:
        data['db'] = Produto.objects.all()
    return render(request, 'produtos/lista.html', data)


def produto_form(request):
    data = {'form': ProdutoForm()}
    return render(request, 'produtos/form.html', data)


def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('produto_form')


def produto_edit(request, pk):
    data = {'db': Produto.objects.get(pk=pk)}
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'produtos/form.html', data)


def produto_update(request, pk):
    data = {'db': Produto.objects.get(pk=pk)}
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('produto_form')


def produto_delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('produto_lista')