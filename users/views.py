from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

    link_classes = {
        'profile': '',
        'account': '',
        'results': '',
        'ftp' : '',
        'password' : 'active',
    }

    extra_context = {
        'link_class': link_classes,
    }

    def get_context_data(self, **kwargs):
        context = super(MyPasswordChangeView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

    link_classes = {
        'profile': '',
        'account': '',
        'results': '',
        'ftp' : '',
        'password' : 'active',
    }

    extra_context = {
        'link_class': link_classes,
    }

    def get_context_data(self, **kwargs):
        context = super(MyPasswordResetDoneView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context



@login_required
def profile_by_id(request, pk):
    selected_profile = Profile.objects.get(id=pk)
    selected_user = selected_profile.user

    try:
        current_user_metrics = FTPtest.objects.filter(user=selected_user).order_by('-date').first()
    except:
        current_user_metrics = "No data available"

    link_classes = {
        'profile': 'active',
        'account': '',
        'results': '',
        'ftp' : '',
        'password' : '',
    }

    context = {
        'profile': selected_profile,
        'link_class': link_classes,
    }

    return render(request, 'users/profile_from_id.html', context=context)




class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Profile
    fields = ['zwiftpower_link']

    link_classes = {
        'profile': 'active',
        'account': '',
        'results': '',
        'ftp' : '',
        'password' : '',
    }

    extra_context = {
        'link_class': link_classes,
    }

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("profile-by-id", kwargs={'pk': self.request.user.id})



class RiderListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        # order_by = request.GET.get('order_by', 'project_name')
        riders = Profile.objects.all()
        context = {'riders': riders}

        return render(request, 'rider_listview.html', context=context)


@login_required
def account_view(request,pk):
    link_classes = {
        'profile': '',
        'account': 'active',
        'results': '',
        'ftp' : '',
        'password' : '',
    }

    context = {

        'link_class': link_classes,
    }

    return render(request, 'users/profile_account_view.html', context=context)

class AccountUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ['email']

    link_classes = {
        'profile': '',
        'account': 'active',
        'results': '',
        'ftp' : '',
        'password' : '',
    }

    extra_context = {
        'link_class': link_classes,
    }

    def get_context_data(self, **kwargs):
        context = super(AccountUpdateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy("profile-by-id", kwargs={'pk': self.request.user.id})


@login_required
def profile_raceresults(request,pk):
    selected_user = Profile.objects.get(id=pk).user
    
    try:
        user_riderresult = RiderResult.objects.filter(rider=selected_user.id)
    except:
        user_riderresult = "No data available"

    link_classes = {
        'profile': '',
        'account': '',
        'results': 'active',
        'ftp' : '',
        'password' : '',
    }

    context = {
        'user_riderresult': user_riderresult,
        'link_class': link_classes,
    }

    return render(request, 'users/profile_raceresults.html', context = context)



@login_required
def profile_ftptests(request, pk):
    selected_user = Profile.objects.get(id=pk).user
    
    try:
        userFTPtests = FTPtest.objects.filter(user=selected_user).order_by('-date')
    except:
        userFTPtests = "No data available"

    link_classes = {
        'profile': '',
        'account': '',
        'results': '',
        'ftp' : 'active',
        'password' : '',
    }

    context = {
        'userFTPtests': userFTPtests,
        'link_class': link_classes,
    }

    return render(request, 'users/profile_ftptests.html', context = context)