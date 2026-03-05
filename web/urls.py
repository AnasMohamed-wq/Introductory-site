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
    
]
