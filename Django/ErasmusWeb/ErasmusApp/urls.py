from django.urls import path
from . import views
urlpatterns = [
    # '': Muestra todas las fichas ordenadas
    path('', views.ficha_lista, name='ficha_lista'),
    # 'ficha/crear': Crear (IMPORTANTE: Ponerla ANTES de la de detalle para que no confunda 'crear' con un ID)
    path('ficha/crear/', views.ficha_crear, name='ficha_crear'),
    # 'ficha/x': Detalle
    path('ficha/<int:pk>/', views.ficha_detalle, name='ficha_detalle'),
    # 'ficha/x/editar': Editar
    path('ficha/<int:pk>/editar/', views.ficha_editar, name='ficha_editar'),
    # 'ficha/x/eliminar': Eliminar
    path('ficha/<int:pk>/eliminar/', views.ficha_eliminar, name='ficha_eliminar'),
]