from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class FTPtest(models.Model):

    FTP_test_types = [
        ('Ramp', 'Ramp'),
        ('20 min test', '20 min test'),
        ('Raceresult', 'Raceresult')
    ]

    date = models.DateField(default=datetime.now)
    FTP = models.IntegerField()
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    weight = models.FloatField()
    testType = models.CharField(max_length = 15, choices = FTP_test_types)
    
    @property
    def wkg(self):
        if self.weight > 0:
            wkg = round(self.FTP/self.weight, 2)
        else:
            wkg = ''
        return wkg