from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


app_name = 'page1'
urlpatterns = [
        path('' , views.index , name='index'),
        path('explanations/<int:num>' ,  views.moreinf , name='moreinf'),
        path('login' , views.LoginView , name='LoginView'),
        path('logout', views.LogoutView , name='LogoutView'),
        path('AddJob', views.AddJob , name='AddJob'),
        path('AssignTask/<int:num>', views.AssignTask , name='AssignTask')
        ]
