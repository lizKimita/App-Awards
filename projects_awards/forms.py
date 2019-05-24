from .models import Projects, Profile
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['profile','date', 'poster_id']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']