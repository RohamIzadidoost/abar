from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

#class Question(models.Model):
   # question_text = models.CharField(max_length=200)
class karfarma(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    master = models.IntegerField(default=1)
class karmand(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    master = models.IntegerField(default=0)
    token = models.CharField(max_length = 64 , default = "a")
class kar(models.Model):
    title = models.CharField(max_length = 100)
    value = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    owner = models.CharField(max_length = 100)
    explanations = models.CharField(max_length = 500)
    is_done=models.IntegerField(default=0)
    user = models.ForeignKey(User, default= None , null = True , on_delete=models.CASCADE) 
    #token = models.CharField(max_length = 64 , default = "a")
class newmodel(models.Model):
    name = models.CharField(max_length = 50)
class karForm(ModelForm):
	class Meta:
		model = kar
		fields = ['user' , 'title', 'value' , 'time' , 'owner' , 'explanations'] 
