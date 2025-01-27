from django.shortcuts import render
from .models import Score

def index(request):
    return render(request, 'game/index.html')

def save_score(request):
    # Logic to save score
    pass  # Placeholder statement to prevent indentation error