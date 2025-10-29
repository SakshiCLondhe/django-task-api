from django.urls import path
from .views import TaskListCreateView, TaskDetailView, get_random_user, show_task_chart

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('random-user/', get_random_user, name='random-user'),
    path('chart/', show_task_chart, name='task-chart'),
]
