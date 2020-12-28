from django.contrib import admin

# Register your models here.
from .models import Season, Race, RaceRegistration, Team


admin.site.register(Season)
admin.site.register(Race)
admin.site.register(RaceRegistration)
admin.site.register(Team)