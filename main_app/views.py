from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Story:
  def __init__(self, plot, genre, themes):
    self.plot = plot
    self.genre = genre
    self.themes = themes

stories = [
  Story('People are lost but then they are like even more lost', 'Comedy', 'Psychological Horor')
]



def home(request):
  return HttpResponse('<h1>Hello this is the first page, like a page named home or something</h1>')

def about(request):
  return render(request, 'about.html')

def stories_index(request):
  return render(request, 'stories/index.html', { 'stories': stories })