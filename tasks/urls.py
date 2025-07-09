from django.urls import path
from . import views

urlpatterns = [
    path('',views.taskList,name='tasks'),
    path('update/<int:pk>/', views.updateTask, name='update-task'),
    path('delete/<int:pk>/', views.deleteTask, name='delete-task'),
]
