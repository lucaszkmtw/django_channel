from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request,'home.html')




def profile(request):
    return render(request, 'profile/profile.html')

def nuevo_usaurio(request):
    if request.method == 'POST':
        pass
    return JsonResponse

