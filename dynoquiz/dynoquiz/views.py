from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("List all quizes here")

def detail(request, quiz_id):
    return HttpResponse("Quiz number %s." % quiz_id)
