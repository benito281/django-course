#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
#from django.shortcuts import get_object_or_404 #<-- Ayuda a mostrar un mensaje mas personalizado
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

#request : información que viene del cliente al momento de ejecutar las función helloWorld
class Viewsproject():
    def home(request): 
        title = " Welcome to Django Course"
        return render(request, "index.html", {
            'title' : title
        })

    def about(request):
        username = "Benito"
        return render(request,"about.html",{
            'username' : username
        })
    
    def hello(request, username):
        return HttpResponse("<h1>Hello %s</h1>" %username)
    
    def projects(request):
        #project = list(Projects.objects.values()) #Muestra los valores de la tabla projects
        projects = Projects.objects.all() #Muestra los valores de la tabla projects
        return render(request, "projects/projects.html", {
            'projects' : projects
        })
        #return JsonResponse(project, safe=False)
    def create_project(request):
        if request.method == 'GET':
            return render(request, 'projects/create_project.html', {
                'form' : CreateNewProject()
            })
        else:
            #print(request.POST['name_project'])
            nameProject = request.POST['name_project']
            Projects.objects.create(name_project=nameProject)
            return redirect("projects")


    def tasks(request):
        #tasks = list(Task.objects.values())
        tasks = Task.objects.all()
        return render(request, "tasks/tasks.html", {
            'tasks' : tasks
        })
        #return JsonResponse(tasks, safe=False)
    
    def get_task(request, titleTask):
        #task = Task.objects.get(id=idTask)
        #task = get_object_or_404(Task, id=idTask) #Hace lo mismo que el anterior pero si hay un error muestra un 404 con el mensaje
        task = Task.objects.get(title=titleTask)
        return HttpResponse("<h1>Task: %s</h1>" %task.title)

    def create_task(request):
        if request.method == 'GET':
            form = CreateNewTask()
            projects = Projects.objects.all()
            return render(request, 'tasks/create_task.html', {
                'form' : form,
                'projects' : projects
            })
        else:
            title = request.POST['titleTask']
            description = request.POST['descriptionTask']
            project_id = request.POST['project_id']
            Task.objects.create(title=title, description=description, project_id=project_id)
            return redirect("tasks")
    