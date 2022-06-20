from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    dict = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    
    return HttpResponse(dict)
