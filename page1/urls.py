from django.urls import path

from . import views
app_name = 'page1'
urlpatterns = [
        path('' , views.index , name='index'),
        path('explanations/<int:num>' , views.moreinf , name='moreinf'),
        path('login' , views.LoginView , name='LoginView'),
        path('logout', views.LogoutView , name='LogoutView'),
        ]
