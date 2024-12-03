from django.contrib import admin
from django.urls import include, path
from tracker import views  # Make sure this import is correct
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes default auth URLs like login, logout, etc.
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_habit, name='add_habit'),
    path('complete/<int:habit_id>/', views.mark_complete, name='mark_complete'),
    path('edit_habit/<int:habit_id>/', views.edit_habit, name='edit_habit'),    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('update_status/<int:habit_id>/', views.update_status, name='update_status'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Add a path for the root URL (home page)
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),]


