from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Story:
  def __init__(self, plot, genre, theme):
    self.plot = plot
    self.genre = genre
    self.theme = theme

stories = [
  Story('People are lost but then they are like even more lost', 'Comedy', 'Psychological Horor'),
  Story('People are lost but then they like stay lost bc they suck at travel.', 'Comedy', 'Psychological Horor'),
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stories_index(request):
  return render(request, 'stories/index.html', { 'stories': stories })