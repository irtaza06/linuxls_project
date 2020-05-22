from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Now it is possible to add as many fields as we want for the user variable
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #dunder method to disply discriptive profile
    def __str__(self):
        return f'{self.user.username} Profile'
#This save method will run after our model is saved, it already exit in parent class but we are adding our own to add some functaionality
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


