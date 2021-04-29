from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_id = models.CharField(max_length=11, null=True)
    email_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if not created:
        Profile.objects.create(user=instance)
    instance.profile.save()