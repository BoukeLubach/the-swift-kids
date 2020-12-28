from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from .models import FTPtest
from datetime import date
from crispy_forms.helper import FormHelper

class FTPtestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FTPtestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    FTP_test_types = [
        ('Ramp', 'Ramp'),
        ('20 min test', '20 min test'),
        ('Raceresult', 'Raceresult')
    ]

    testType = forms.ChoiceField(initial="20 min test", choices = FTP_test_types)
    date = forms.DateField(
                initial=date.today, 
                widget=forms.DateInput(
                    attrs={'firstDay': 1, 
                    'pattern=': '\d{4}-\d{2}-\d{2}', 
                    'lang': 'pl', 
                    'format': 'yyyy-mm-dd', 
                    'type': 'date'}
                )
             )

    FTP = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'FTP'}))
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Weight'}))


    class Meta:
        model = FTPtest
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
        }
