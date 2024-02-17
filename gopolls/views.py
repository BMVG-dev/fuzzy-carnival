from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return HttpResponse(" Hello, World...you're at the Home_page ")


def detail_page(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results_page(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote_page(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
