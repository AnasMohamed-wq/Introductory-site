from django.urls import include , path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),

    
]
