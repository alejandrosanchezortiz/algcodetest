from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_chart/', views.view_chart, name='view-chart'),
]
