from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from race.models import Race, RaceRegistration, Team, Season
from .models import RiderResult, RaceResult
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

class Season1ResultsListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        selected_team = self.kwargs.get('team')
        selected_team = 1 if selected_team==None else selected_team
        raceresults = RaceResult.objects.filter(team=selected_team, race__season=1)

        context = {
            'team' : selected_team,
            'raceresults': raceresults,
        }

        return render(request, 'season1_results.html', context=context)



class Season2ResultsListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        selected_team = self.kwargs.get('team')
        selected_team = 1 if selected_team==None else selected_team
        raceresults = RaceResult.objects.filter(team=selected_team, race__season=2)

        context = {
            'team' : selected_team,
            'raceresults': raceresults,
        }

        return render(request, 'season2_results.html', context=context)



def season_listview(request):

    return render(request, 'results_homeview.html', context = {})



def race_analytics(request):

    return render(request, 'race_analytics.html', context={})