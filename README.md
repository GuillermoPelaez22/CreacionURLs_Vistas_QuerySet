# Gestión de Tareas - URLs, Vistas y QuerySets

## URL 1: Lista de proyectos
- **URL:** `/proyectos/`
- **Vista:** `lista_proyectos`
- **Requisitos que cumple:** ManyToOne (creador del proyecto y de las tareas), ManyToMany (etiquetas de las tareas), relación reversa (`tareas`), `select_related` y `prefetch_related`, sin parámetros.

## URL 2: Detalle de una tarea
- **URL:** `/tarea/<int:id_tarea>/`
- **Vista:** `dame_tarea`
- **Requisitos que cumple:** parámetro entero, `get()`, ManyToOne (proyecto y creador, con `select_related`), ManyToMany (etiquetas), relación reversa (`comentarios`), tabla intermedia (`Asignacion`, con `asignacion_set`) y `prefetch_related`.

## URL 3: Tareas completadas entre dos años
- **URL:** `/tareas/completadas/<int:anyo_inicio>/<int:anyo_fin>/`
- **Vista:** `tareas_completadas`
- **Requisitos que cumple:** dos parámetros, filtro con AND (estado y año de inicio y fin), `order_by`, ManyToOne (proyecto y creador, con `select_related`), ManyToMany (etiquetas), tabla intermedia (`Asignacion`) y `prefetch_related`.
- **Explicación de código no visto en clase:** `fecha_creacion__year__gte` y `fecha_creacion__year__lte`. Se usa `__year` (visto en clase) para obtener el año del campo de fecha, y se le añade `__gte` ("greater than or equal", mayor o igual) o `__lte` ("less than or equal", menor o igual) para comparar. Equivale en SQL a `YEAR(fecha_creacion) >= anyo_inicio AND YEAR(fecha_creacion) <= anyo_fin`.