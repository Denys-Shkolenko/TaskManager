from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('upcoming/', views.upcoming_tasks, name='upcoming_tasks'),
    path('overdue/', views.overdue_tasks, name='overdue_tasks'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/', views.detail_task, name='detail_task'),
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('<int:task_id>/assign/', views.assign_task, name='assign_task'),
]
