from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category


def index0(request):
    # html = "WELCOME" + '<p><a href="/rango/about">About</a></p>' + '<p><a href="/rango">Oh</a></p>'
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)


def index(request):
    context_dict = {'boldmessage': "Cookie, candy, pancake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
