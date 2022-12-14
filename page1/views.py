from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth import *
from django.contrib.auth.models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
# Create your views here.

#class JobListView(ListView):
    #paginate_by = 2
    #model = Kar

def index(request):
    request.session.set_test_cookie()
    jobs = kar.objects.all()
    #pagination broke in reverting , fix it later
    paginator = Paginator(jobs , 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dic = {
    'jobs' : jobs , 
    'page_obj': page_obj,
    'requset': request,
    }

    #signup : 
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_rpt = request.POST.get('password_rpt')
        master = (request.POST.get('master') == 'on')
       # print(">>>master: " , master)
        if  User.objects.filter(username=username).count() > 0 or User.objects.filter(email=email).count() > 0 or password != password_rpt:
            print(">>signuperror") #handle it later
        else: 
           user = User.objects.create_user(email=email , username=username , password=password)
           if(master):
               NewEmp = karfarma()
               NewEmp.user = user
           else:
                NewEmp = karmand()
                NewEmp.user = user
            
           NewEmp.save()
           user.save()
           login(request ,user)
#          print("account with " , email , "CREATED!" , User.objects.filter(email=email).count())


    response = render(request, 'page1/index.html', context_dic)
    response.set_cookie('last' , page_number)
    return response


def AddJob(request):
    user = request.user
    if request.method == 'POST':
        form = karForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(">>>>>>>>>>>>formt not valid")
    else:
        form = karForm()
    context = {
        'user': user,
        'form': form,
    }
    return render(request , 'AddJob/AddJob.html' , context)
    #return redirect(reverse('page1:index'))

def LoginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request , user)
        #not valid username and pass should be handled
    else :
        print(">>>>account doesn't exist!" , User.objects.filter(email = email).count())
    return redirect(reverse('page1:index'))

def LogoutView(request):
    logout(request)
    return redirect(reverse('page1:index'))

@login_required
@cache_page(60 * 5)
def moreinf(request, num):
    context = RequestContext(request)
    if request.session.test_cookie_worked():
        print(">>>> TESTWORKED!!!!")
        request.session.delete_test_cookie()

    job = kar.objects.get(pk=num)
    bisahab = False
    if job.user == None : #kargozae case shoud be handled
        bisahab = True
        print(">>>>>" , request.user.karfarma)
    print(">>>>>> job user "  , job.user , bisahab)
    context = {
        'job':job,
        'request': request,
        'bisahab': bisahab,
    }
    response = render(request, 'explanations/details.html', context)
    return response

@login_required
def AssignTask(request, num):
    job = kar.objects.get(pk=num)
    job.user = request.user
    print(">>>>>" ,job.title , job.user)
    job.save()
    return redirect(reverse('page1:index'))
    
