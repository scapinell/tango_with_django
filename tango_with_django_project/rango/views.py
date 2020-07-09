from django.http import HttpResponse
from django.shortcuts import render


def index0(request):
    html = "WELCOME" + '<p><a href="/rango/about">About</a></p>' + '<p><a href="/rango">Oh</a></p>'
    return HttpResponse(html)


def index(request):
    context_dict = {'boldmessage': "Cookie, candy, pancake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
