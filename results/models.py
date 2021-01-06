from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from race.models import Race, Team


class RaceResult(models.Model):
    team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True)
    place = models.IntegerField(blank=True, null=True)
    race = models.ForeignKey(Race, models.CASCADE)
    category = models.CharField(max_length=124, blank=True, null=True)
    division = models.CharField(max_length=124, blank=True, null=True)
    riders = models.IntegerField(blank=True, null=True)
    team_participating = models.IntegerField(blank=True, null=True)

    @property
    def league_points(self):
        finish_points_array = [20, 19, 18, 17, 16, 
                               15, 14, 13, 12, 11, 
                               10, 9,  8,  7,  6, 
                               5,  4,  3,  2,  1]

        return finish_points_array[self.place-1]

    def __str__(self):
        return (self.team.name + " " + self.race.course)
    

class RiderResult(models.Model):
    rider = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    race = models.ForeignKey(Race, models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, models.CASCADE, blank=True, null=True)
    KOM_points = models.IntegerField(default=0, blank=True, null=True)
    finish_place = models.IntegerField(blank=True, null=True)
    teamresult = models.ForeignKey(RaceResult, models.SET_NULL, blank=True, null=True)
    fit_file = models.FileField(upload_to='fit_files', blank=True, null=True)
    fit_file_name = models.CharField(max_length=124, blank=True, null=True)
    avg_power = models.IntegerField(blank=True, null=True)
    norm_power = models.IntegerField(blank=True, null=True)

    power_15s = models.DecimalField(max_digits = 6, decimal_places = 2, blank=True, null=True)
    power_1min = models.DecimalField(max_digits = 6, decimal_places = 2, blank=True, null=True)
    power_5min = models.DecimalField(max_digits = 6, decimal_places = 2, blank=True, null=True)
    power_20min = models.DecimalField(max_digits = 6, decimal_places = 2, blank=True, null=True)

    
    
    class Meta:
        unique_together = [['rider', 'race']]

    @property
    def finish_points(self):
        if self.finish_place != None:

            if self.finish_place>30:
                return 1
            else:
                finish_points_array = [40, 35, 30, 27, 26, 
                                    25, 24, 23, 22, 21, 
                                    20, 19, 18, 17, 16, 
                                    15, 14, 13, 12, 11, 
                                    10, 9,  8,  7,  6, 
                                    5,  4,  3,  2,  1]

                return finish_points_array[self.finish_place-1]
        else:
            return 1

    @property
    def total_points(self):
        return self.KOM_points + self.finish_points

    
    def __str__(self):
        return (str(self.rider) + " - " + self.race.course + " " + self.team.name)