from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Story
# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def stories_index(request):
  stories = Story.objects.all()
  return render(request, 'stories/index.html', { 'stories': stories })

def stories_detail(request, story_id):
  story = Story.objects.get(id=story_id)
  return render(request, 'stories/detail.html', { 'story': story })

class StoryCreate(CreateView):
  model = Story
  fields = '__all__'
  successful_url = '/stories/'

class StoryUpdate(UpdateView):
  model = Story
  fields = '__all__'

class StoryDelete(DeleteView):
  model = Story
  success_url = '/stories/'
