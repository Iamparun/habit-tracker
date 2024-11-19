from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:username>/', views.user_dashboard, name='user_dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_habit, name='add_habit'),
    path('complete/<int:habit_id>/', views.mark_complete, name='mark_complete'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),  # Using the built-in login view
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('logout/', views.custom_logout_view, name='logout'),
]
