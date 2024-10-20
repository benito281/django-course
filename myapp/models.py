from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name_project = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default=timezone.now)

    def __str__(self):
        return self.name_project
    

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200) 
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 


    def __str__(self):
        return self.title + ' - ' + self.project.name_project