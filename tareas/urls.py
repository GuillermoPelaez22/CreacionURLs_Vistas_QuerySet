from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyecto/<int:id_proyecto>/tareas/', views.tareas_proyecto, name='tareas_proyecto'),
    path('tarea/<int:id_tarea>/usuarios/', views.usuarios_tarea, name='usuarios_tarea'),
    path('tareas/observaciones/<str:texto>/', views.tareas_observaciones, name='tareas_observaciones'),
    path('tareas/completadas/<int:anyo_inicio>/<int:anyo_fin>/', views.tareas_completadas, name='tareas_completadas'),
    path('proyecto/<int:id_proyecto>/ultimo-comentario/', views.ultimo_comentario, name='ultimo_comentario'),
    path('tarea/<int:id_tarea>/comentarios/<str:palabra>/<int:anyo>/', views.comentarios_tarea, name='comentarios_tarea'),
    path('proyecto/<int:id_proyecto>/etiquetas/', views.etiquetas_proyecto, name='etiquetas_proyecto'),
    re_path(r'^usuarios/sin-tarea/$', views.usuarios_sin_tarea, name='usuarios_sin_tarea'),
    path('tarea/<int:id_tarea>/', views.dame_tarea, name='dame_tarea'),
    path('tareas/buscar/<str:texto>/', views.buscar_tareas, name='buscar_tareas'),
    path('usuario/<int:id_usuario>/', views.ficha_usuario, name='ficha_usuario'),
]