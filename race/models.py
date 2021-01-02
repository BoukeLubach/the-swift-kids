from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)

class Race(models.Model):
    racetype_options = [
        ('Race', 'Race'),
        ('Team time trial', 'Team time trial'),
        
    ]

    number = models.IntegerField()
    course = models.CharField(max_length = 50)
    distance = models.FloatField()
    elevation = models.IntegerField(blank=True, null=True)
    racetype = models.CharField(max_length = 15, choices = racetype_options)
    date = models.DateField()
    elevation = models.IntegerField(blank=True, null=True)
    season = models.ForeignKey(Season, models.CASCADE, blank=True, null=True)
    zwiftinsider_route_link = models.URLField(max_length = 128, blank=True, null=True)

    # class Meta:
    #     unique_together = [['number', 'season']]
    

    @property
    def is_finished(self):
        if self.date < datetime.now:
            return True
        else:
            return False

    def __str__(self):
        return (self.course + " " + str(self.date))


class RaceRegistration(models.Model):
    race = models.ForeignKey(Race, models.SET_NULL, blank=True, null=True)
    participant = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = [['race', 'participant']]
    

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)
