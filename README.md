# Gestión de Tareas - URLs, Vistas y QuerySets

## URL 1: Lista de proyectos
- **URL:** `/proyectos/`
- **Vista:** `lista_proyectos`
- **Requisitos que cumple:** ManyToOne (creador del proyecto y de las tareas), ManyToMany (etiquetas de las tareas), relación reversa (`tareas`), `select_related` y `prefetch_related`, sin parámetros.

## URL 2: Detalle de una tarea
- **URL:** `/tarea/<int:id_tarea>/`
- **Vista:** `dame_tarea`
- **Requisitos que cumple:** parámetro entero, `get()`, ManyToOne (proyecto y creador, con `select_related`), ManyToMany (etiquetas), relación reversa (`comentarios`), tabla intermedia (`Asignacion`, con `asignacion_set`) y `prefetch_related`.