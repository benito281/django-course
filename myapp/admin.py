from django.contrib import admin
from .models import Projects, Task


# Register your models here.
# Se importa los modelos para poder utilizarlos en la panel de administración de Django
admin.site.register(Projects)
admin.site.register(Task)