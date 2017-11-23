from django.db import models





# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

NATIONALITY_CHOICES = (
    ('AUT', 'Austria'),
    ('CZE','Czech'),
    ('EST', 'Estonia'),
    ('FIN','Finland'),
    ('FRN','France'),
    ('GER','Germany'),
    ('ITA','Italy'),
    ('JPN','Japan'),
    ('KAZ','Kazachstam'),
    ('NOR','Norway'),
    ('PL','Poland'),
    ('RUS','Russia'),
    ('SLO','Slovenia'),
    ('SUI','Switzerland'),
    ('SVK','Slovakia'),
    ('SWE','Sweden'),
    ('US','United States')
)


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

class Competition_Location(models.Model):
    location = models.CharField(max_length=200, blank=False)
    nationality = models.CharField(max_length=200, blank=False,choices=NATIONALITY_CHOICES)


class Competition(models.Model):
    COMP_STATUS_CHOICES = (
        ('Pl','Planned'),
        ('INP','In_Progress'),
        ('Cnd)','Canceled'),
        ('End','Ended'),
    )
    comp_date = models.DateField(blank=False)
    competition_location = models.OneToOneField(Competition_Location)
    comp_status = models.CharField(max_length=5, choices=COMP_STATUS_CHOICES, default='Pl')


class Ski_Jumpers(models.Model):
    name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200, blank=False)
    nationality = models.CharField(max_length=3,blank=False,choices=NATIONALITY_CHOICES)

class Type(models.Model):
    user_id = models.OneToOneField(User)
    comp_id = models.ForeignKey(Competition_Location)
    jumpers = models.ForeignKey(Ski_Jumpers)

class Results(models.Model):
    comp_id = models.ForeignKey(Competition)
    jumper_id = models.ForeignKey(Ski_Jumpers)
    place = models.IntegerField(blank=False)
    score = models.IntegerField(blank=False)





