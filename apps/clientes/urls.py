from django.urls import path

from .views import cliente_lista, cliente_form, cliente_create, cliente_edit, cliente_update, cliente_delete

urlpatterns = [
    path('lista/', cliente_lista, name='cliente_lista'),
    path('form/', cliente_form, name='cliente_form'),
    path('create/', cliente_create, name='cliente_create'),
    path('edit/<int:pk>/', cliente_edit, name='cliente_edit'),
    path('update/<int:pk>/', cliente_update, name='cliente_update'),
    path('delete/<int:pk>/', cliente_delete, name='cliente_delete'),
]
