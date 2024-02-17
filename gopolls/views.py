from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return HttpResponse(" Hello, World...you're at the Home_page ")
