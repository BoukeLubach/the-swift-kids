from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from ftp.models import FTPtest
from results.models import RiderResult
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView, DetailView

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LogoutView):
    template_name = 'users/logout.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('password-change-done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


@login_required
def profile_by_id(request, pk):
    selected_profile = Profile.objects.get(id=pk)
    selected_user = selected_profile.user

    try:
        userFTPtests = FTPtest.objects.filter(user=selected_user).order_by('-date')
        current_user_metrics = userFTPtests.first()
        user_riderresult = RiderResult.objects.filter(rider=selected_user.id)
    except:
        userFTPtests = "No data available"
        user_riderresult = "No data available"


    context = {
        'profile': selected_profile,
        'userFTPtests': userFTPtests,
        'user_riderresult': user_riderresult,
    }

    print(current_user_metrics)
    return render(request, 'users/profile_from_id.html', context=context)




class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Profile
    fields = ['zwiftpower_link']
    def get_success_url(self, **kwargs):

        return reverse_lazy("profile-by-id", kwargs={'pk': self.request.user.id})


def register():

    return render(request, 'users/register.html', context = {})



class RiderListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        # order_by = request.GET.get('order_by', 'project_name')
        riders = Profile.objects.all()
        context = {'riders': riders}

        return render(request, 'rider_listview.html', context=context)
