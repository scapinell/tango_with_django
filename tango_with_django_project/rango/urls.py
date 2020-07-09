from django.conf.urls import url
from django import views
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]