from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ver_recetas/', views.ver_recetas, name='ver_recetas'),    
    path('receta/<int:pk>/descripcion/', views.receta_descripcion, name='receta_descripcion'),
    path('receta/crear/',views.crear_receta,name='crear_receta'),
    path('relaciones', views.relaciones, name='relaciones'),#vamosa ver las relaciones entre tablas many to many y foreign key
    



    # path('ingredientes/', views.ingredientes_list, name='ingredientes_list'),
    path('ingredientes/', views.IngredienteListView.as_view(), name='ingredientes_list'),

    # path('ingredientes/<int:pk>', views.ingrediente_detalle, name='ingrediente_detalle'),
    path('ingredientes/<int:pk>', views.IngredienteDetailView.as_view(), name='ingrediente_detalle'),

    # path('ingredientes/<int:pk>/editar',views.ingrediente_editar,name='ingrediente_editar'),
    path('ingredientes/<int:pk>/editar',views.IngredienteUpdateView.as_view(),name='ingrediente_editar'),
    path('ingredientes/<int:pk>/eliminar',views.ingrediente_eliminar,name='ingrediente_eliminar'),

    # path('ingredientes/crear/',views.crear_ingrediente,name='crear_ingrediente'),
    path('ingredientes/crear/',views.IngredienteCreateView.as_view(),name='crear_ingrediente'),

    path('ingredientes/creacion_masiva/',views.creacion_masiva_ingredientes,name='creacion_masiva_ingredientes'),
    ]