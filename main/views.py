from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from .models import UserProfile

# Create your views here.


def home(request):
    return render(request,'home.html')




def profile(request):
    return render(request, 'profile/profile.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def new_session(request):
    if request.method =='POST':
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return JsonResponse