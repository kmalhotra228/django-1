from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from . import models
from django.contrib.auth import login ,logout ,authenticate

# Create your views here.
def home(request):
    return render(request,'authentications/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('authentications:signin'))
    else:
        form =  UserCreationForm()

    return render(request,'authentications/signup.html', context = {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if form.is_valid() and user.is_staff:
            login(request,user)
            return redirect(reverse('authentications:detail'))
        elif form.is_valid():
            login(request,user)
            try:
                obj = models.Personal_details.objects.get(username = username)
                firstname = obj.first_name
                lastname = obj.last_name
                email = obj.email
                phone_number = obj.phone_number
                dob = obj.date_of_birth
                gender = obj.gender
                context = {'username':username,
                            'firstname':firstname,
                            'lastname':lastname,
                            'email':email,
                            'phone_number':phone_number,
                            'dob':dob,
                            'gender':gender
                }

                return render(request,'authentications/single_detail.html',context)
            except:
                return redirect(reverse('authentications:sucess'))
    else:
        form = AuthenticationForm()
    return render(request,'authentications/signin.html',context = {'form': form})

def signout(request):
    logout(request)
    return redirect(reverse('authentications:home'))

def sucess(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your details have been saved!')
    else:
        form = ReviewForm()
    return render(request,'authentications/sucess.html',context = {'form':form})

def detail(request):
    all_detail = models.Personal_details.objects.all()
    context = {'all_detail': all_detail}
    return render(request,'authentications/details.html',context = context)

def single_detail(request):
    pass



