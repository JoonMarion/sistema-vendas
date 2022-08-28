from django.urls import path

from .views import venda_lista, venda_create, venda_edit, venda_update, venda_delete, venda_form

urlpatterns = [
    path('lista/', venda_lista, name='venda_lista'),
    path('form/', venda_form, name='venda_form'),
    path('create/', venda_create, name='venda_create'),
    path('edit/<int:pk>/', venda_edit, name='venda_edit'),
    path('update/<int:pk>/', venda_update, name='venda_update'),
    path('delete/<int:pk>/', venda_delete, name='venda_delete'),
]