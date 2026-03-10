

from django.urls import include , path
from . import views



    



urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('courses/', views.courses, name='courses'),
    path('vision/', views.vision, name='vision'),
    path('machine/', views.machine, name='machine'),
    path('contact/', views.contact, name='contact'),
    path('send-inquiry/', views.send_inquiry, name='send_inquiry'),


    path('a/', views.a, name='a'),
    path('index/', views.index, name='index'),
    path('h/', views.h, name='h'),
    path('about2/', views.about2, name='about2'),
    path('j/', views.j, name='j'),
   


    
    
]
