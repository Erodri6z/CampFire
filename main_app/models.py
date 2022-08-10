from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
  name = models.CharField(max_length=50)
  plot = models.CharField(max_length=300)
  genre = models.CharField(max_length=100)
  theme = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.plot

  def get_absolute_url(self):
      return reverse("stories_detail", kwargs={"story_id": self.id})
  
