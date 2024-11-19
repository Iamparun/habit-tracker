from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['description', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter habit name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter habit description'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
