from django.db import models
from django.contrib.auth.models import User

#class Question(models.Model):
   # question_text = models.CharField(max_length=200)
class karfarma(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
class karmand(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    token = models.CharField(max_length = 64 , default = "a")
class kar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ) 
    title = models.CharField(max_length = 100)
    value = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    owner = models.CharField(max_length = 100)
    explanations = models.CharField(max_length = 500)
    token = models.CharField(max_length = 64 , default = "a")
class newmodel(models.Model):
    name = models.CharField(max_length = 50)
