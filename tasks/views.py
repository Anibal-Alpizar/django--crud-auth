from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET': 
        # enviar formulario
        return render(request, 'signup.html',{
        "form" : UserCreationForm
    })
    else:
        # enviar datos
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # cookies
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html',{
                    "form" : UserCreationForm,
                    "error" : "User already exists"
                })
        return render(request, 'signup.html',{
            "form" : UserCreationForm,
            "error" : "Password do not match"
        })

def tasks(request):
    return render(request, 'tasks.html')





    
