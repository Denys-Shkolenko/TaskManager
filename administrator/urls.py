from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('stats/', views.task_statistics, name='task_statistics'),
]
