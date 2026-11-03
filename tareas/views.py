from django.shortcuts import render, get_object_or_404
from .models import Proyecto, Tarea, Asignacion, Comentario, Etiqueta, Usuario


def index(request):
    return render(request, 'index.html')


# Ejercicio 1: lista de proyectos con sus datos
def lista_proyectos(request):
    proyectos = (Proyecto.objects
                 .select_related('creador')
                 .prefetch_related('tareas')
                 .all())
    return render(request, 'proyecto/lista.html', {'proyectos': proyectos})


# Ejercicio 2: tareas de un proyecto, de más nueva a más antigua
def tareas_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    tareas = (Tarea.objects
              .select_related('creador')
              .filter(proyecto=id_proyecto)
              .order_by('-fecha_creacion'))
    return render(request, 'tarea/lista.html',
                  {'proyecto': proyecto, 'tareas': tareas})


# Ejercicio 3: usuarios asignados a una tarea, por fecha de asignación ascendente
def usuarios_tarea(request, id_tarea):
    tarea = get_object_or_404(Tarea, id=id_tarea)
    asignaciones = (Asignacion.objects
                    .select_related('usuario')
                    .filter(tarea=id_tarea)
                    .order_by('fecha_asignacion'))
    return render(request, 'tarea/usuarios.html',
                  {'tarea': tarea, 'asignaciones': asignaciones})
    
# Ejercicio 4: tareas con un texto en las observaciones de su asignación
def tareas_observaciones(request, texto):
    tareas = (Tarea.objects
              .select_related('proyecto')
              .filter(asignacion__observaciones__contains=texto)
              .distinct())
    return render(request, 'tarea/observaciones.html',
                  {'tareas': tareas, 'texto': texto})


# Ejercicio 5: tareas completadas, creadas entre dos años
def tareas_completadas(request, anyo_inicio, anyo_fin):
    tareas = (Tarea.objects
              .select_related('proyecto')
              .filter(estado='CO',
                      fecha_creacion__year__gte=anyo_inicio,
                      fecha_creacion__year__lte=anyo_fin)
              .order_by('fecha_creacion'))
    return render(request, 'tarea/completadas.html',
                  {'tareas': tareas, 'anyo_inicio': anyo_inicio,
                   'anyo_fin': anyo_fin})


# Ejercicio 6: último usuario que ha comentado en una tarea de un proyecto
def ultimo_comentario(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    comentario = (Comentario.objects
                  .select_related('autor', 'tarea')
                  .filter(tarea__proyecto=id_proyecto)
                  .order_by('-fecha_comentario')
                  .first())
    return render(request, 'comentario/ultimo.html',
                  {'proyecto': proyecto, 'comentario': comentario})

# Ejercicio 7: comentarios de una tarea que empiezan por una palabra y son de un año
def comentarios_tarea(request, id_tarea, palabra, anyo):
    tarea = get_object_or_404(Tarea, id=id_tarea)
    comentarios = (Comentario.objects
                   .select_related('autor')
                   .filter(tarea=id_tarea,
                           texto__startswith=palabra,
                           fecha_comentario__year=anyo)
                   .order_by('fecha_comentario'))
    return render(request, 'comentario/lista.html',
                  {'tarea': tarea, 'comentarios': comentarios,
                   'palabra': palabra, 'anyo': anyo})


# Ejercicio 8: etiquetas usadas en las tareas de un proyecto
def etiquetas_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    etiquetas = (Etiqueta.objects
                 .filter(tareas__proyecto=id_proyecto)
                 .distinct())
    return render(request, 'etiqueta/lista.html',
                  {'proyecto': proyecto, 'etiquetas': etiquetas})


# Ejercicio 9: usuarios que no están asignados a ninguna tarea
def usuarios_sin_tarea(request):
    usuarios = Usuario.objects.filter(tareas_asignadas=None)
    return render(request, 'usuario/sin_tarea.html', {'usuarios': usuarios})

def mi_error_400(request, exception=None):
    return render(request, 'errores/400.html', status=400)

def mi_error_403(request, exception=None):
    return render(request, 'errores/403.html', status=403)

def mi_error_404(request, exception=None):
    return render(request, 'errores/404.html', status=404)

def mi_error_500(request):
    return render(request, 'errores/500.html', status=500)