from django.urls import path

from . import views

app_name = 'profesores'

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('<slug:teacher_slug>', views.teacher_detail, name='teacher_detail'),
]
