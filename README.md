# Gestión de Tareas - URLs, Vistas y QuerySets

## URL 1: Lista de proyectos
- **URL:** `/proyectos/`
- **Vista:** `lista_proyectos`
- **Requisitos que cumple:** ManyToOne (creador del proyecto y de las tareas), ManyToMany (etiquetas de las tareas), relación reversa (`tareas`), `select_related` y `prefetch_related`, sin parámetros.