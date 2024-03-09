from typing import Any
from django import forms 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .import models
from .import constants

class JobForm(forms.ModelForm):
    class Meta:
        model= models.Job
        exclude= ["employer"]
        
        
class ApplyJobForm(forms.ModelForm):
    class Meta:
        model= models.ApplyJob
        fields=['experience', 'cv']
        labels = {
            'experience': 'Your Experience',
            'cv': 'Drop your CV',
        }
        
    