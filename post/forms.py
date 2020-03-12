# forms.py 
from django import forms 
from .models import *

  
class imgForm(forms.ModelForm): 
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    
    class Meta: 
        model = imgUpload 
        fields = ('img', 'y', 'width', 'x', 'height',)