from django.forms import ModelForm
from .models import Trip, Task
from django import forms

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['nazwa_imprezy', 'start_date', 'finish_date', 'uczestnicy', 'cena', 'instutucja', 'organizator',
                  'wyżywienie', 'przewoźnik', 'program', 'umowa', 'pliki']

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'