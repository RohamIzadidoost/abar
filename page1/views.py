from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.template import RequestContext
from django.shortcuts import redirect
# Create your views here.

class JobListView(ListView):
    paginate_by = 2
    model = Job

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
    jobs = Job.objects.all()
    paginator = Paginator(jobs , 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
    'jobs' : jobs , 
    'page_obj': page_obj 
    }
    return render(request , "page1/index.html" , context)

def moreinf(request, num):
    context = RequestContext(request)
    if request.session.test_cookie_worked():
        print (">>>> TESTWORKED!!!!" )
        request.session.delete_test_cookie()
    
    job = Job.objects.get(pk=num)
   # response = render_to_response('explanations/details.html' , {'job': job} , context)
    response =  render(request, 'explanations/details.html' , {'job': job})
    response.set_cookie('last' , num)
    return response
   




