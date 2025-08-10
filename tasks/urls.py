from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',auth_views.LoginView.as_view(),name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('home/',views.taskList,name='tasks' ),
    path('update/<int:pk>/', views.updateTask, name='update-task'),
    path('delete/<int:pk>/', views.deleteTask, name='delete-task'),
    path('edit/<int:pk>/', views.editTask, name='edit-task'),
]
