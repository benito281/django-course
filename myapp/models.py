from django.db import models

# Create your models here.
class Projects(models.Model):
    name_project = models.CharField(max_length=150)

    def __str__(self):
        return self.name_project
    

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200) 
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name_project