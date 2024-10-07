from django import forms

class CreateNewTask(forms.Form):
    titleTask = forms.CharField(
        label="Task Title", 
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task title'
        })
    )
    descriptionTask = forms.CharField(
        label="Task Description",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task description',
            'rows': 3
        })
    )
    

class CreateNewProject(forms.Form):
    name_project = forms.CharField(
        label="Project Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter project name'
        })
    )
    description = forms.CharField(
        label="Project Description",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter project description',
            'rows': 3
        }),
        required=False
    )