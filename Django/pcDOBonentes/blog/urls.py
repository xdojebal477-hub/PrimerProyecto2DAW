from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('cliente/<int:cliente_pk>/', views.ver_pcs_cliente, name='ver_pcs_cliente'),
    path('pc/<int:pc_pk>/', views.especificaciones_pc, name='especificaciones_pc'),
]
