from django.urls import path
from ropa.views import listar_pedidos, contacto, crear_pedido

urlpatterns = [
    path('listar_pedidos/', listar_pedidos, name = 'lista_pedidos'),
    path('contacto/', contacto, name = 'contacto'),
    path('crear_pedido/', crear_pedido, name = 'crear_pedido')
]