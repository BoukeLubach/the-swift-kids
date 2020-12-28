from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from ftp.models import FTPtest
from results.models import RiderResult
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView, DetailView

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'



@login_required
def profile_by_id(request, pk):
    selected_profile = Profile.objects.get(id=pk)
    selected_user = selected_profile.user

    try:
        userFTPtests = FTPtest.objects.filter(user=selected_user).order_by('-date')
        user_riderresult = RiderResult.objects.filter(rider=selected_user.id)
    except:
        userFTPtests = "No data available"
        user_riderresult = "No data available"

    context = {
        'profile': profile,
        'userFTPtests': userFTPtests,
        'user_riderresult': user_riderresult,
    }
    
    return render(request, 'profile_from_id.html', context=context)



@login_required
def profile(request):

    try:
        userFTPtests = FTPtest.objects.filter(user=request.user).order_by('-date')
        user_riderresult = RiderResult.objects.filter(rider=request.user.id)
    except:
        userFTPtests = "No data available"
        user_riderresult = "No data available"

    context = {
        'profile': profile,
        'userFTPtests': userFTPtests,
        'user_riderresult': user_riderresult,
    }
    
    return render(request, 'profile_from_id.html', context=context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['FTP', 'weight']
    success_url = reverse_lazy('profile')



def register():

    return render(request, 'users/register.html', context = {})



class RiderListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        # order_by = request.GET.get('order_by', 'project_name')
        riders = Profile.objects.all()
        context = {'riders': riders}

        return render(request, 'rider_listview.html', context=context)
