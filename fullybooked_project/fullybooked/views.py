from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Testing index response")
    # changing what is returned later from HttpResponse to something else