from django import forms 

class JobNameFilterForm(forms.Form):
    location = forms.CharField()