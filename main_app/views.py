from re import template
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Story
# Create your views here.


class Home(LoginView):
  template_name = 'home.html'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
@login_required
def stories_index(request):
  stories = Story.objects.all()
  return render(request, 'stories/index.html', { 'stories': stories })

@login_required
def stories_detail(request, story_id):
  story = Story.objects.get(id=story_id)
  return render(request, 'stories/detail.html', { 'story': story })

class StoryCreate(LoginRequiredMixin, CreateView):
  model = Story
  fields = '__all__'
  successful_url = '/stories/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class StoryUpdate(LoginRequiredMixin, UpdateView):
  model = Story
  fields = '__all__'

class StoryDelete(LoginRequiredMixin, DeleteView):
  model = Story
  success_url = '/stories/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('stories_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)