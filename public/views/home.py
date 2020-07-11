from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
    context = {'latest_question_list': "latest_question_list"}
    return render(request, 'home/index.html', context)


def apple_touch_icon_png(request):
    valid_image = os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))), "static/img/logo-180x180.png")
    with open(valid_image, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")


def favicon_png(request):
    valid_image = os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))), "static/img/logo-32x32.png")
    with open(valid_image, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")


def favicon_ico(request):
    valid_image = os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))), "static/img/favicon.ico")
    with open(valid_image, "rb") as f:
        return HttpResponse(f.read(), content_type="image/x-icon")
