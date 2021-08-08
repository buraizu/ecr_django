from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

def home(request):
    return render(request, 'ecr/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'ecr/signupuser.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
            except IntegrityError:
                return render(request, 'ecr/signupuser.html', {'form':UserCreationForm(), 'error':'That username is already taken.  Please make another selection.'})
        else:
            return render(request, 'ecr/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

