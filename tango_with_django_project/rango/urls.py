from django.conf.urls import url
from django import views
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]