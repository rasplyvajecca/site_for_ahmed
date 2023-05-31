from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create/', views.create, name="create"),
    path('feedback/', views.feedback, name="feedback"),
    path('about/', views.table, name="about"),
    path('contact/', views.contact, name="contact"),
    ]
