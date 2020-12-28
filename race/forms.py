from django import forms
from django.contrib.auth.models import User
from .models import Race
import datetime 

class RaceForm(forms.ModelForm):

    class Meta:
        model = Race
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
        }

