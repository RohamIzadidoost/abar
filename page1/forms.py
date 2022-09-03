from django import forms 

class SignupForm(forms.Form):
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    password_rpt = forms.CharField()
    master = forms.BooleanField()
    