from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.views.generic import ListView
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs , 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    'jobs' : jobs , 
    'page_obj': page_obj 
    }
    return render(request , "page1/index.html" , context)
