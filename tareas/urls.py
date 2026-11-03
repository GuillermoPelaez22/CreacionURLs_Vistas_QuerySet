from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyecto/<int:id_proyecto>/tareas/', views.tareas_proyecto, name='tareas_proyecto'),
    path('tarea/<int:id_tarea>/usuarios/', views.usuarios_tarea, name='usuarios_tarea'),
]