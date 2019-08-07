from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_chart/', views.view_chart, name='view-chart'),
    path('add_user/', views.add_user, name='add-user'),
    path('view_connections/', views.view_connections, name='view-connections'),
    path('delete_view/', views.delete_user, name='delete-view'),
    path('connect_users/', views.connect_users, name='connect-users'),
    path('add_connection/', views.add_connection, name='add-connection'),
]
