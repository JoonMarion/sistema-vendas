from django.contrib import admin
from django.urls import path, include

from apps.home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', home, name='home'),

    # CRUD PRODUTOS
    path('produtos/', include('apps.produtos.urls')),

    # CRUD CLIENTES
    path('clientes/', include('apps.clientes.urls')),

    # CRUD VENDAS
    path('vendas/', include('apps.vendas.urls')),

    # CRUD DETALHE VENDA
    path('detalhevenda/', include('apps.detalhevenda.urls')),
]
