from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ingredientes/', views.ingredientes_list, name='ingredientes_list'),
    path('ingredientes/crear/',views.crear_ingrediente,name='crear_ingrediente'),
    path('ingredientes/<int:pk>/', views.ingrediente_detalle, name='ingrediente_detalle'),
    path('ingredientes/<int:pk>/editar/',views.ingrediente_editar,name='ingrediente_editar'),
    path('ingredientes/<int:pk>/eliminar/',views.ingrediente_eliminar,name='ingrediente_eliminar'),
    ]