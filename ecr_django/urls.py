"""ecr_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecr import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Runs
    path('runs/', views.allruns, name='allruns'),
    path('createrun/', views.createrun, name='createrun'),
    path('run/<int:run_pk>', views.viewrun, name='viewrun'),
    path('run/<int:run_pk>/delete', views.deleterun, name='deleterun'),

    # Events
    path('events/', views.allevents, name='allevents'),

    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
]
