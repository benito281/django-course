from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject
from django.views import View
from json import loads


def getAllProjects(request):
    try:
        projects = list(Projects.objects.values())
        return JsonResponse(projects, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=500)

class ProjectsViews(View):
    form_class = CreateNewProject
    template_name = 'projects/projects.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form': self.form_class()
        })

    def post(self, request, *args, **kwargs):
        try:
            data = loads(request.body)
            form = self.form_class(data)

            if form.is_valid():
                Projects.objects.create(name_project=data.get('name_project'), 
                                        description=data.get('description'))
                return JsonResponse({'icon': 'success',
                                'title': 'Correcto',
                                'text': 'Proyecto creado correctamente'}, 
                                safe=False, status=201)
            else:
                return JsonResponse({'icon': 'warining',
                                'title': 'Error',
                                'text': 'Error al rellenar los campos'}, 
                                safe=False, status=201)
        except Exception as e:
            print(e)
            return JsonResponse({'icon': 'error',
                                'title': 'Error',
                                'text': str(e)}, 
                                safe=False, status=500)


class Home(View):
    template_name = 'index.html'
    title = " Welcome to Django Course"
    def get(self, request):
        return render(request, self.template_name, {
            'title': self.title
        })

class About(View):
    template_name = 'about.html'

    def get(self, request):
        username = "Benito"
        return render(request, template_name=self.template_name, context={'username': username})



class Viewsproject():
    
    
    def projects(request):
        # project = list(Projects.objects.values()) #Muestra los valores de la tabla projects
        projects = Projects.objects.all()  # Muestra los valores de la tabla projects
        return render(request, "projects/projects.html", {
            'projects': projects
        })
        # return JsonResponse(project, safe=False)

    def create_project(request):
        if request.method == 'GET':
            return render(request, 'projects/create_project.html', {
                'form': CreateNewProject()
            })
        else:
            # print(request.POST['name_project'])
            nameProject = request.POST['name_project']
            Projects.objects.create(name_project=nameProject)
            return redirect("projects")

    def tasks(request):
        # tasks = list(Task.objects.values())
        tasks = Task.objects.all()
        return render(request, "tasks/tasks.html", {
            'tasks': tasks
        })
        # return JsonResponse(tasks, safe=False)

    def get_task(request, titleTask):
        # task = Task.objects.get(id=idTask)
        # task = get_object_or_404(Task, id=idTask) #Hace lo mismo que el anterior pero si hay un error muestra un 404 con el mensaje
        task = Task.objects.get(title=titleTask)
        return HttpResponse("<h1>Task: %s</h1>" % task.title)

    def create_task(request):
        if request.method == 'GET':
            form = CreateNewTask()
            projects = Projects.objects.all()
            return render(request, 'tasks/create_task.html', {
                'form': form,
                'projects': projects
            })
        else:
            title = request.POST['titleTask']
            description = request.POST['descriptionTask']
            project_id = request.POST['project_id']
            Task.objects.create(
                title=title, description=description, project_id=project_id)
            return redirect("tasks")
