from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from. import views

urlpatterns = [
        url('pro', views.index, name='index'),
        url(r'about', views.about, name='about'),
        url(r'tour', views.our_tour, name='tour'),
        url(r'destination', views.destination, name='destination'),
        url(r'contact', views.contact, name='contact'),
        url('register', views.register, name='reg'),
        url(r'login', views.logedin, name='log'),
        url(r'home', views.home, name='home'),

]
