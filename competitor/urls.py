from django.urls import path

from . import views

app_name = 'concursantes'

urlpatterns = [
    path('', views.competitors_list, name='competitors_list'),
]
