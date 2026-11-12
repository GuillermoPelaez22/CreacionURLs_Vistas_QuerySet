from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('tarea/<int:id_tarea>/', views.dame_tarea, name='dame_tarea'),
    path('tareas/completadas/<int:anyo_inicio>/<int:anyo_fin>/', views.tareas_completadas, name='tareas_completadas'),
    path('tareas/buscar/<str:texto>/', views.buscar_tareas, name='buscar_tareas'),
    path('proyecto/<int:id_proyecto>/ultimo-comentario/', views.ultimo_comentario, name='ultimo_comentario'),
    re_path(r'^usuarios/sin-tarea/$', views.usuarios_sin_tarea, name='usuarios_sin_tarea'),
    path('usuario/<int:id_usuario>/', views.ficha_usuario, name='ficha_usuario'),
    path('proyecto/<int:id_proyecto>/estadisticas/', views.estadisticas_proyecto, name='estadisticas_proyecto'),
    path('asignaciones/observaciones/<str:texto>/', views.asignaciones_observaciones, name='asignaciones_observaciones'),
    path('usuario/<int:id_usuario>/comentarios/', views.ultimos_comentarios_usuario, name='ultimos_comentarios_usuario'),
    path('error/400/', views.mi_error_400, name='error_400'),
    path('error/403/', views.mi_error_403, name='error_403'),
    path('error/500/', views.mi_error_500, name='error_500'),
]