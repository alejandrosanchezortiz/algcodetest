from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_chart/', views.view_chart, name='view-chart'),
    path('add_user/', views.add_user, name='add-user'),
    path('view_connections/', views.view_connections, name='view-connections'),
    path('delete_view/<int:user_id>', views.delete_user, name='delete_view'),
]
