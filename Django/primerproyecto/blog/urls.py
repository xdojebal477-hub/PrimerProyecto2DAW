from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('<int:pk>/', views.detalle_post, name='detalle_post'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autor/<int:autor_pk>',views.autor_post,name='autor_post'),
    path('autor/nuevo',views.autor_nuevo,name='autor_nuevo'),
    path('autor/editar/<int:autor_pk>',views.autor_editar,name='autor_nuevo'),
    path('autor/eliminar/<int:autor_pk>',views.autor_eliminar,name='autor_eliminar'),
]
