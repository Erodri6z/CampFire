from django.shortcuts import render
from .models import Story
# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stories_index(request):
  stories = Story.objects.all()
  return render(request, 'stories/index.html', { 'stories': stories })