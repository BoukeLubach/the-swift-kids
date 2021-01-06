from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from race.models import Race, RaceRegistration, Team, Season
from .models import RiderResult, RaceResult
from .forms import FitfileUploadForm
from .fit_processing import process_fit_file
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required



class Season1ResultsListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        selected_team = self.kwargs.get('team')
        selected_team = 1 if selected_team==None else selected_team
        raceresults = RaceResult.objects.filter(team=selected_team, race__season=self.kwargs.get('season'))

        context = {
            'team' : selected_team,
            'raceresults': raceresults,
        }

        return render(request, 'season1_results.html', context=context)



# class Season2ResultsListView(LoginRequiredMixin, ListView):

#     def get(self, request, *args, **kwargs):
#         selected_team = self.kwargs.get('team')
#         selected_team = 1 if selected_team==None else selected_team
#         raceresults = RaceResult.objects.filter(team=selected_team, race__season=2)

#         context = {
#             'team' : selected_team,
#             'raceresults': raceresults,
#         }

#         return render(request, 'season2_results.html', context=context)

def season_listview(request):

    return render(request, 'results_homeview.html', context = {})

def race_analytics(request):

    return render(request, 'race_analytics.html', context={})


@login_required
def season1_raceresult_detail(request, season, team, race):

    team = Team.objects.get(id=team)
    race = Race.objects.get(id=race, season=1)

    riderResult = RiderResult.objects.filter(race=race, team=team)
    
    context = {
        "race": race,
        "team": team,
        "riderResults": riderResult,
    }
    return render(request, 'season1_results_detail.html', context=context)






@login_required
def upload_fit_file(request, season, team, race):

    result_model_ids = {"season": season, "team": team, "race": race}
    try:
        riderresult_object = RiderResult.objects.get(rider=request.user, team=team, race=race)
    except:
        print("no results model exists for rider, team, user combination")
        return HttpResponseRedirect(reverse('upload-failed-user-not-available', kwargs=result_model_ids))

    if request.method == 'POST':
        form = FitfileUploadForm(request.POST, request.FILES)

        if form.is_valid():

            if request.FILES['file'].name.lower().endswith(('.fit')):
                riderresult_object.fit_file = request.FILES['file']
                riderresult_object.fit_file_name = request.FILES['file'].name
                riderresult_object.save()
                process_fit_file(request.FILES['file'].name, riderresult_object)
                
            else:
                print("file uploaded not a .fit file")
                return HttpResponseRedirect(reverse('upload-failed-filetype', kwargs=result_model_ids))

            return HttpResponseRedirect(reverse('season1-raceresults-detail', kwargs=result_model_ids))
    else:

        form = FitfileUploadForm()
    return render(request, 'fitfile_uploadform.html', {'form': form})


@login_required
def fit_upload_failed_user_not_available(request, season, team, race):
   
    context = {
        "season": season, 
        "team": team, 
        "race": race, 
        "message_title": "Upload failed",
        "message": "Are you sure you participated in this race?",
    }

    return render(request, 'fitfile_upload_failed.html', context=context)


@login_required
def fit_upload_failed_filetype(request, season, team, race):
    context = {
        "season": season, 
        "team": team, 
        "race": race, 
        "message_title": "Upload failed",
        "message": "Uploaded file is not a .fit file",
    }
    return render(request, 'fitfile_upload_failed.html', context=context)