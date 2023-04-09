from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task','done']