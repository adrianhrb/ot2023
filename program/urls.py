from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<tofind>/', views.search, name='search'),
]
