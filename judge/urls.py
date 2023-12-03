from django.urls import path

from . import views

app_name = 'jueces'

urlpatterns = [
    path('', views.index, name='index'),
    path('identificacion/', views.judge_identification, name='identification'),
    path('show/', views.judge_list, name='list'),
    path('show/<slug:judge_slug>/', views.judge_detail, name='detail'),
]
