# alumni/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('alumni_form/', views.alumni_form, name='alumni_form'),
    path('custom_query/', views.custom_query, name='custom_query'),
]
