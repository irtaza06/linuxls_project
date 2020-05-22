from django.db.models.signals import post_save
from django.contrib.auth.models import User #sender, which sends the signal
from django.dispatch import receiver # recevier, which receiver the signal
#we want to import profile from out models
from .models import Profile
#lets tie them together

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #Now we have create profile function whcih will run everytime when a user is created


#receiver is a decorator

#save profile function

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
#we have to now import our signals inside the ready function of user app in apps.py file in order to work


