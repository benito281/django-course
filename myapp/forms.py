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
        label="Nombre del proyecto",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introduzca el nombre del proyecto'
        })
    )
    description = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción del proyecto',
            'rows': 3
        })
    )