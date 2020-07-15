from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
    #request.session['lang'] = 'hi'
    context = {'latest_question_list': "latest_question_list"}
    return render(request, 'farmers/index.html', context)
