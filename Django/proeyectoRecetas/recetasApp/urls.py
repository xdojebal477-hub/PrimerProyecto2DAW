from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('incgredientes/', views.ingredientes_list, name='ingredientes_list'),]