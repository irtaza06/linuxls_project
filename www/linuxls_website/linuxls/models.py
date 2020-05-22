from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    videoURL = models.URLField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Telling a django that if user is deleted than we want to delete their posts as well

    def __str__(self):
        return self.title
#we need to create get absolute URL mehod so django knows how to find the location to specific method
#we used reverse function (it simple return the full url as a string)
#while redirect redirects to sepcific route
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


