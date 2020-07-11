from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import datetime

def index(request):
    context = {'latest_question_list': "latest_question_list"}
    return render(request, 'home/index.html', context)
