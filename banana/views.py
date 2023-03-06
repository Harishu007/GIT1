from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sweet(request):
    return HttpResponse('<marquee><h1>banana is very sweet</h1></marquee>')
