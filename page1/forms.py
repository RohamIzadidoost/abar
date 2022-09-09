from django import forms 
from .models import *

class karForm(forms.ModelForm):
    class Meta:
    	model=kar
    	fields = ['title' , 'value' , 'time' , 'owner' , 'explanations']
  
