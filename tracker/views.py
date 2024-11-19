from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import HabitForm
from .models import Habit, HabitCompletion, HabitStreak


# Dashboard view
@login_required
def dashboard(request):
    habits = Habit.objects.filter(user=request.user)  # User-specific habits
    return render(request, 'tracker/dashboard.html', {'habits': habits})


# Add Habit view
@login_required
def add_habit(request):
    if request.method == "POST":
        description = request.POST.get('description')  # Get the description input
        Habit.objects.create(
            description=description,
            user=request.user,  # Associate habit with the logged-in user
        )
        return redirect('dashboard')  # Redirect to dashboard after saving
    return render(request, 'tracker/add_habit.html')


# Edit Habit view
@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'tracker/edit_habit.html', {'form': form})


# Delete Habit view
@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        return redirect('dashboard')
    return render(request, 'tracker/confirm_delete.html', {'habit': habit})


# Mark Habit as Complete view
@login_required
def mark_complete(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    completion, created = HabitCompletion.objects.get_or_create(
        habit=habit,
        date_completed=date.today()
    )
    streak, _ = HabitStreak.objects.get_or_create(habit=habit)
    streak.update_streak(completed_today=created)
    return redirect('dashboard')


# Update Status view
@login_required
def update_status(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if habit.status == 'Pending' and request.method == 'POST':
        habit.status = 'Completed'
        habit.save()
    return redirect('dashboard')


# User Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Custom Logout view
def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the appropriate login URL pattern
