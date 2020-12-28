from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from .models import Race, RaceRegistration, Team, Season
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RaceForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

class RaceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Race
    template = 'race_form.html'
    form_class = RaceForm
    success_url = reverse_lazy('race-overview')

    def test_func(self):
        return self.request.user.is_staff


class RaceListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        season_nr = self.kwargs.get('season')
        races = Race.objects.filter(season = season_nr)
        print(season_nr)
        context = {
            races:'races',
            season_nr: "season_nr"
        }
        return render(request, 'racelistview.html', context=context)


@login_required
def raceview(request, pk):
    user_signed_up = RaceRegistration.objects.filter(participant=request.user, race_id=pk).exists()
    show_signup_button = not user_signed_up

    context = {
        'signups': RaceRegistration.objects.filter(race_id=pk),
        'show_signup_button': show_signup_button,
        'race_id': pk,
        'event': Race.objects.get(id=pk), 
        'event_date': Race.objects.get(id=pk).date, 
    }
    
    return render(request, 'race/race_detail.html', context=context)

