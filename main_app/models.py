from django.db import models
from django.urls import reverse

# Create your models here.

class Story(models.Model):
  plot = models.CharField(max_length=300)
  genre = models.CharField(max_length=100)
  theme = models.CharField(max_length=100)

  def __str__(self):
    return self.plot

  def get_absolute_url(self):
      return reverse("stories_detail", kwargs={"story_id": self.id})
  
