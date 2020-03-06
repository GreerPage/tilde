# forms.py 
from django import forms 
from .models import *
  
class imgForm(forms.ModelForm): 
  
    class Meta: 
        model = imgUpload 
        fields = ['img'] 