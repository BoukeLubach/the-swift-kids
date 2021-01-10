from django.shortcuts import render, redirect, get_object_or_404
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

    def get_success_url(self):
        season = get_object_or_404(Season, id=self.kwargs.get('season'))
        return reverse_lazy('race-listview', kwargs={'season': season.id})

    def get_initial(self):
        season = get_object_or_404(Season, id=self.kwargs.get('season'))

        return {
            "season": season
        }

    def test_func(self):
        return self.request.user.is_staff



class RaceListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        season_nr = self.kwargs.get('season')
        races = Race.objects.filter(season = season_nr)

        for race in races:
            if RaceRegistration.objects.filter(race=race, participant=request.user).exists():
                race.user_is_registered = True
                race.user_signup_id = RaceRegistration.objects.get(race=race, participant=request.user).id
            else:
                race.user_is_registered = False


        context = {
            'races':races,
            "season_nr": season_nr
        }
        return render(request, 'race/racelistview.html', context=context)


@login_required
def race_detailview(request, pk):
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




class RaceRegistrationView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        race_id = self.kwargs.get('pk')
        RaceRegistration(race = Race.objects.get(id=race_id),  participant=request.user).save()

        return redirect(f'/race/{race_id}/')


class StaffRaceRegisterView(LoginRequiredMixin, CreateView):
    model = RaceRegistration
    template = 'raceregistration_form.html'
    fields = '__all__'
    success_url = '/race/{race_id}'

    def get_context_data(self, **kwargs):
        event_name = Race.objects.get(id=self.kwargs['pk'])
        context = super(StaffRaceRegisterView, self).get_context_data(**kwargs)
        context['event_name'] = event_name
        
        return context

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SignupDeleteView(LoginRequiredMixin, DeleteView):

    model = RaceRegistration
    success_url = '/race/{race_id}'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def signup_selection(request, pk):


    context = {
        'signups': RaceRegistration.objects.filter(race_id=pk),
    }
    

    return render(request, "race/signup_selection.html", context = context)
