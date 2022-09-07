from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import *
# Create your views here.

#class JobListView(ListView):
    #paginate_by = 2
    #model = Kar

def index(request):
    request.session.set_test_cookie()
    if 'last' in request.COOKIES:
        num  = request.COOKIES['last']
        print(">>>>>>>" , num)
        ans = "explanations/" 
        ans = ans + str(num) 
        return redirect(ans)
    else :
        print(" NOOO FUCKING COOKIE WTF")
    jobs = kar.objects.all()
    paginator = Paginator(jobs , 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    'jobs' : jobs , 
    'page_obj': page_obj 
    }

    #signup : 
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_rpt = request.POST.get('password_rpt')
        master = (request.POST.get('master') == 'on')
       # print(">>>master: " , master)
        if 2 < 0 : 
            print(">>user exists") #handle it later
        else: 
           user = User.objects.create_user(email=email , username=username , password=password)
           if(master):
               NewEmp = karfarma()
               NewEmp.User = user
           else:
                NewEmp = karmand()
                NewEmp.User = user
            
           NewEmp.save()
 


    response = render(request, 'page1/index.html', context_dic)
    response.set_cookie('last' , page_number)
    return response


def moreinf(request, num):
    context = RequestContext(request)
    if request.session.test_cookie_worked():
        print (">>>> TESTWORKED!!!!" )
        request.session.delete_test_cookie()
    
    job = kar.objects.get(pk=num)
   # response = render_to_response('explanations/details.html' , {'job': job} , context)
    response =  render(request, 'explanations/details.html' , {'job': job})
    response.set_cookie('last' , num)
    return response
   




