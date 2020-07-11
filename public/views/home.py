from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'latest_question_list': "latest_question_list"}
    return render(request, 'home/index.html', context)
