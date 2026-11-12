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

## URL 4: Buscar tareas por texto
- **URL:** `/tareas/buscar/<str:texto>/`
- **Vista:** `buscar_tareas`
- **Requisitos que cumple:** parámetro `str`, filtro con OR (`Q` con `|`) sobre título y descripción, `__contains` (LIKE), `order_by` descendente, ManyToOne (proyecto y creador, con `select_related`), ManyToMany (etiquetas), tabla intermedia (`Asignacion`) y `prefetch_related`.

## URL 5: Último comentario de un proyecto
- **URL:** `/proyecto/<int:id_proyecto>/ultimo-comentario/`
- **Vista:** `ultimo_comentario`
- **Requisitos que cumple:** parámetro entero, límite `[:1]`, `order_by` descendente, OneToOne (perfil del usuario, con `select_related`), ManyToOne (autor, tarea y proyecto, con `select_related`).

## URL 6: Usuarios sin tarea asignada
- **URL:** `/usuarios/sin-tarea/` (definida con `re_path`)
- **Vista:** `usuarios_sin_tarea`
- **Requisitos que cumple:** `re_path`, filtro con `None` en una tabla intermedia (`asignacion=None`), OneToOne (perfil, con `select_related`), relaciones reversas (`proyectos_creados`, `tareas_creadas`, `comentarios`, con `prefetch_related`).

## URL 7: Ficha de un usuario
- **URL:** `/usuario/<int:id_usuario>/`
- **Vista:** `ficha_usuario`
- **Requisitos que cumple:** parámetro entero, `get()`, OneToOne (perfil, con `select_related`), relaciones reversas (`proyectos_creados`, `tareas_creadas`, `comentarios`), tabla intermedia (`asignacion_set`), `prefetch_related` y `Prefetch` con `order_by`.
- **Explicación:** `Prefetch` permite personalizar la consulta que lanza `prefetch_related`. Aquí se usa para traer las asignaciones y los comentarios del usuario ya ordenados por fecha descendente y con su tarea y proyecto cargados (`select_related`), evitando consultas adicionales.

## URL 8: Estadísticas de un proyecto
- **URL:** `/proyecto/<int:id_proyecto>/estadisticas/`
- **Vista:** `estadisticas_proyecto`
- **Requisitos que cumple:** parámetro entero, `get()`, `aggregate`, ManyToOne (creador, con `select_related`), relación reversa (`tareas`), ManyToMany (etiquetas) y `prefetch_related`.
- **Explicación de código no visto en clase (`aggregate`, `Count`, `Min`, `Max`):** `aggregate()` calcula un valor sobre todas las filas de un QuerySet y devuelve un diccionario, no un QuerySet. Las funciones que se le pasan se importan de `django.db.models`: `Count` cuenta filas (`COUNT` en SQL), `Min` obtiene el valor más pequeño (`MIN`) y `Max` el más grande (`MAX`). Cada argumento con nombre es una clave del diccionario resultante, por ejemplo `aggregate(total=Count('id'))` devuelve `{'total': 4}`. Se usa para calcular el número de tareas, comentarios y asignaciones del proyecto y las fechas de la primera y la última tarea y asignación.

## URL 9: Asignaciones con un texto en las observaciones
- **URL:** `/asignaciones/observaciones/<str:texto>/`
- **Vista:** `asignaciones_observaciones`
- **Requisitos que cumple:** parámetro `str`, tabla intermedia (`Asignacion`), `__contains` (LIKE), `order_by` descendente, OneToOne (perfil del usuario, con `select_related`), ManyToOne (usuario, tarea, proyecto y creador, con `select_related`), ManyToMany (etiquetas de la tarea, con `prefetch_related`).

## URL 10: Últimos 5 comentarios de un usuario
- **URL:** `/usuario/<int:id_usuario>/comentarios/`
- **Vista:** `ultimos_comentarios_usuario`
- **Requisitos que cumple:** parámetro entero, `get()`, `order_by` descendente, límite `[:5]`, OneToOne (perfil del usuario, con `select_related`), ManyToOne (tarea, proyecto y creador, con `select_related`), ManyToMany (etiquetas de la tarea, con `prefetch_related`).