from django.urls import path
from .views import ProjectsViews, Home, About, getAllProjects, Viewsproject

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('about/', About.as_view(), name="about"),
    path('projects/', ProjectsViews.as_view(), name="projects"),
    path('all_projects/', getAllProjects, name="all_projects"),
    path('tasks/', Viewsproject.tasks, name="tasks"),
    path('task/<str:titleTask>', Viewsproject.get_task, ),
    path('create_task/', Viewsproject.create_task, name="create_task"),
    path('create_project/', Viewsproject.create_project, name="create_project")
]
