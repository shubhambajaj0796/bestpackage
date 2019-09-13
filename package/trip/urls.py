from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from. import views

urlpatterns = [
        url(r'pro', views.index, name='index'),
        url('about', views.about, name='about'),
        url('tour', views.our_tour, name='tour'),
        url('destination', views.destination, name='destination'),
        url('contact', views.contact, name='contact'),
        url('register', views.register, name='reg'),
        url('login', views.logedin, name='log'),
        url('home', views.home, name='home'),

]
