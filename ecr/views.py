from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'ecr/home.html')

# Auth
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'ecr/signupuser.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('allruns')
            except IntegrityError:
                return render(request, 'ecr/signupuser.html', {'form':UserCreationForm(), 'error':'That username is already taken.  Please make another selection.'})
        else:
            return render(request, 'ecr/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'ecr/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ecr/loginuser.html', {'form':AuthenticationForm(), 'error':'Unable to authenticate with this data, please check and try again.'})
        else:
            login(request, user)
            return redirect('allruns')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


# Runs

def allruns(request):
    return render(request, 'ecr/allruns.html')