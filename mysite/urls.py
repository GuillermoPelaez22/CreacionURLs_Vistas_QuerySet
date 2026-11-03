from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tareas.urls')),
]

handler400 = 'tareas.views.mi_error_400'
handler403 = 'tareas.views.mi_error_403'
handler404 = 'tareas.views.mi_error_404'
handler500 = 'tareas.views.mi_error_500'