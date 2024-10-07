from django.urls import path
from .views import Viewsproject 


#TODO: 02:49:00 Video

urlpatterns = [
    path('', Viewsproject.home, name="index"),
    path('about/', Viewsproject.about, name="about"),
    #path('hello/<str:username>', Viewsproject.hello), <-- Params
    path('projects/', Viewsproject.projects, name="projects"),
    path('tasks/', Viewsproject.tasks, name="tasks"),
    path('task/<str:titleTask>', Viewsproject.get_task, ),
    path('create_task/', Viewsproject.create_task, name="create_task"),
    path('create_project/', Viewsproject.create_project, name="create_project")
]
