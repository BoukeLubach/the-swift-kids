from django import forms

class FitfileUploadForm(forms.Form):
    file = forms.FileField()