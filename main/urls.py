from django.urls import path
from .views import HomePage, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create-task/', TaskCreateView.as_view(), name='task_create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),

]