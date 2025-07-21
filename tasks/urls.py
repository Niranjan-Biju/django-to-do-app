from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.taskList,name='tasks'),
    path('update/<int:pk>/', views.updateTask, name='update-task'),
    path('delete/<int:pk>/', views.deleteTask, name='delete-task'),
    path('edit/<int:pk>/', views.editTask, name='edit-task'),
    path('login/', auth_views.LoginView.as_view(template_name='registrations/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
