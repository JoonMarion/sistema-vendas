from django.urls import path

from .views import produto_lista, produto_form, produto_create, produto_edit, produto_update, produto_delete

urlpatterns = [
    path('lista/', produto_lista, name='produto_lista'),
    path('form/', produto_form, name='produto_form'),
    path('create/', produto_create, name='produto_create'),
    path('edit/<int:pk>/', produto_edit, name='produto_edit'),
    path('update/<int:pk>/', produto_update, name='produto_update'),
    path('delete/<int:pk>/', produto_delete, name='produto_delete'),
]
