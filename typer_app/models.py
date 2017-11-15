from django.db import models





# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    rank = models.CharField(max_length=500,blank=True)
    type = models.CharField(max_length=500,blank=True)

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        if not instance.is_superuser:
            instance.userprofile.save()