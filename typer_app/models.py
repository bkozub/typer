from django.db import models





# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse

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
    rank = models.IntegerField(max_length=500,blank=True,default=0)
    photo = models.ImageField(upload_to='uploads/profile/{}',blank=True)

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        if not instance.is_superuser:
            instance.userprofile.save()

class Competition_Location(models.Model):
    location = models.CharField(max_length=200, blank=False)
    nationality = models.CharField(max_length=200, blank=False,choices=NATIONALITY_CHOICES)
    photo = models.ImageField(upload_to='uploads/location/{}')

    def __str__(self):
        return '{}'.format(self.location)


class Competition(models.Model):
    COMP_STATUS_CHOICES = (
        ('Created','Created'),
        ('In_Progress','In_Progress'),
        ('Canceled','Canceled'),
        ('Ended','Ended'),
    )
    date = models.DateField(blank=False)
    location = models.OneToOneField(Competition_Location)
    status = models.CharField(max_length=15, choices=COMP_STATUS_CHOICES, default='Pl')

    def get_absolute_url(self):
        return reverse('competition-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.location,self.date)



class Ski_Jumper(models.Model):
    name = models.CharField(max_length=200, blank=False)
    surname = models.CharField(max_length=200, blank=False)
    nationality = models.CharField(max_length=3,blank=False,choices=NATIONALITY_CHOICES)
    photo = models.ImageField(upload_to='uploads/jumpers/{}', blank=True)
    def __str__(self):
        return '{} {}'.format(self.name,self.surname)



class Type(models.Model):

    user_id = models.ForeignKey(User)
    comp_id = models.ForeignKey(Competition)
    jumpers = models.ForeignKey(Ski_Jumper)
    place = models.IntegerField()


class Result(models.Model):
    PLACE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    competition_id = models.ForeignKey(Competition)
    jumper_id = models.ForeignKey(Ski_Jumper)
    place = models.CharField(max_length=100,blank=False, choices=PLACE_CHOICES)
    score = models.IntegerField(blank=False)

    def __str__(self):
        return '{},{},{}'.format(self.comp_id,self.jumper_id,self.place)






