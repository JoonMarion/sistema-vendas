from django.urls import path

from .views import detalhe_venda_lista, detalhe_venda_edit, detalhe_venda_update, detalhe_venda_delete, \
    detalhe_venda_create, detalhe_venda_form

urlpatterns = [
    path('lista/', detalhe_venda_lista, name='detalhe_venda_lista'),
    path('form/', detalhe_venda_form, name='detalhe_venda_form'),
    path('create/', detalhe_venda_create, name='detalhe_venda_create'),
    path('edit/<int:pk>/', detalhe_venda_edit, name='detalhe_venda_edit'),
    path('update/<int:pk>/', detalhe_venda_update, name='detalhe_venda_update'),
    path('delete/<int:pk>/', detalhe_venda_delete, name='detalhe_venda_delete'),
]
