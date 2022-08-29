from django.shortcuts import redirect, render

from .forms import ClienteForm
from .models import Cliente


def cliente_lista(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(nome_cliente__icontains=search) | Cliente.objects.filter(
            cod_cliente__icontains=search) | Cliente.objects.filter(cpf__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'clientes/lista.html', data)


def cliente_form(request):
    data = {'form': ClienteForm()}
    return render(request, 'clientes/form.html', data)


def cliente_create(request):
    if request.method == 'POST':
        post_data = request.POST
        post_data._mutable = True
        form = ClienteForm(request.POST or None)

        if float(request.POST.get('renda')) > 4591:
            post_data['classe'] = 'AB'
        elif float(request.POST.get('renda')) > 1064:
            post_data['classe'] = 'C'
        elif float(request.POST.get('renda')) > 768:
            post_data['classe'] = 'D'
        else:
            post_data['classe'] = 'E'

        if form.is_valid():
            form.save()
            return redirect('cliente_form')


def cliente_edit(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'clientes/form.html', data)


def cliente_update(request, pk):
    data = {'db': Cliente.objects.get(pk=pk)}
    post_data = request.POST
    post_data._mutable = True
    form = ClienteForm(request.POST or None, instance=data['db'])
    if float(request.POST.get('renda')) > 4591:
        post_data['classe'] = 'AB'
    elif float(request.POST.get('renda')) > 1064:
        post_data['classe'] = 'C'
    elif float(request.POST.get('renda')) > 768:
        post_data['classe'] = 'D'
    else:
        post_data['classe'] = 'E'

    if form.is_valid():
        form.save()
        return redirect('cliente_form')


def cliente_delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('cliente_lista')
