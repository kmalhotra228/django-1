from django.urls import path
from . import views

app_name = 'authentications'

urlpatterns = [
    path('home',views.home, name ='home'),
    path('signin', views.signin,name = 'signin'),
    path('signup', views.signup,name = 'signup'),
    path('signout', views.signout,name = 'signout'),
    path('sucess',views.sucess,name = 'sucess'),
    path('detail',views.detail, name = 'detail'),
    path('adminlogin',views.adminlogin,name = 'adminlogin')



]
