from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import RunForm
from .models import Run

def home(request):
    return render(request, 'ecr/home.html')

# Auth
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'ecr/signupuser.html', {'form':UserCreationForm()})
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
    runs = Run.objects.filter(user=request.user)
    return render(request, 'ecr/allruns.html', {'runs':runs})

def createrun(request):
    if request.method == 'GET':
        return render(request, 'ecr/createrun.html', {'form':RunForm(), 'error':'Invalid data, please check your inputs and try again.'})
    else:
        form = CreateRunForm(request.POST)
        newrun = form.save(commit=False)
        newrun.user = request.user
        newrun.save()
        return redirect('allruns')

def viewrun(request, run_pk):
    run = get_object_or_404(Run, pk=run_pk)
    if request.method == 'GET':
        form = RunForm(instance=run)
        return render(request, 'ecr/viewrun.html', {'run':run, 'form':form})
    else:
        try:
            form = RunForm(request.POST, instance=run)
            form.save()
            return redirect('allruns')
        except ValueError:
            return render(request, 'ecr/viewrun.html', {'run':run, 'form':form, 'error':'Invalid data, please check your inputs and try again.'})
