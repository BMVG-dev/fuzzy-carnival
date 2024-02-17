from django.shortcuts import render
from django.http import HttpResponse

from gopolls.models import Question


# Create your views here.
def home_page(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail_page(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results_page(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote_page(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
