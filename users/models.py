from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FTP = models.IntegerField(default = 0)
    weight = models.FloatField(default = 0)
    
    @property
    def wkg(self):
        if self.weight > 0:
            wkg = round(self.FTP/self.weight, 2)
        else:
            wkg = ''
        return wkg

    def __str__(self):
        return f'{self.user.username} Profile'
