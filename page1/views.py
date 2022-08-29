from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context = {'jobs' : jobs}
    return render(request , "page1/index.html" , context)
