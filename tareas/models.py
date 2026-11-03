from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE,
                                related_name='proyectos_creados')

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    ESTADOS = [
        ('PE', 'Pendiente'),
        ('PR', 'En progreso'),
        ('CO', 'Completada'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=2, choices=ESTADOS, default='PE')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,
                                 related_name='tareas')
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE,
                                related_name='tareas_creadas')
    usuarios = models.ManyToManyField(Usuario, through='Asignacion',
                                      related_name='tareas_asignadas')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas')

    def __str__(self):
        return self.titulo


class Asignacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True)
    fecha_asignacion = models.DateTimeField(default=timezone.now)


class Comentario(models.Model):
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE,
                              related_name='comentarios')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE,
                              related_name='comentarios')

    def __str__(self):
        return self.texto[:30]