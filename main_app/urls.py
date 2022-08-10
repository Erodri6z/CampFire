from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('stories/', views.stories_index, name='stories_index'),
  path('stories/<int:story_id>/', views.stories_detail, name='stories_detail')
]