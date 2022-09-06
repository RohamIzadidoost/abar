from django import forms 
from .models import *
class SignupForm(forms.ModelForm):
	password_rpt = forms.CharField()
	master = forms.BooleanField()
	class Meta:
	        model = User
	        fields = ['email', 'username' , 'password']
   
    #email = forms.CharField()
    #username = forms.CharField()
    #password = forms.CharField()
    #password_rpt = forms.CharField()
    #master = forms.BooleanField()
    
