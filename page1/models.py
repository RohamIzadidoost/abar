from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
class Job(models.Model):
    title = models.CharField(max_length = 100)
    value = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    owner = models.CharField(max_length = 100)
    explanations = models.CharField(max_length = 500)
