from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyecto/<int:id_proyecto>/tareas/', views.tareas_proyecto, name='tareas_proyecto'),
    path('tarea/<int:id_tarea>/usuarios/', views.usuarios_tarea, name='usuarios_tarea'),
    path('tareas/observaciones/<str:texto>/', views.tareas_observaciones, name='tareas_observaciones'),
    path('tareas/completadas/<int:anyo_inicio>/<int:anyo_fin>/', views.tareas_completadas, name='tareas_completadas'),
    path('proyecto/<int:id_proyecto>/ultimo-comentario/', views.ultimo_comentario, name='ultimo_comentario'),
]