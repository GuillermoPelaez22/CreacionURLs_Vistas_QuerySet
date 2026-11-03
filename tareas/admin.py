from django.contrib import admin
from .models import Usuario, Proyecto, Etiqueta, Tarea, Asignacion, Comentario

admin.site.register([Usuario, Proyecto, Etiqueta, Tarea, Asignacion, Comentario])