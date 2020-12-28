from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import DeleteView  

from .forms import FTPtestForm
from users.models import Profile
from .models import FTPtest


class FTPtestListView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        FTPtests = FTPtest.objects.all()
        userFTPtests = FTPtest.objects.filter(user=request.user).order_by('-date')
        print(userFTPtests)
        context = {
            'FTPtests': FTPtests,
            'userFTPtests': userFTPtests
        }

        return render(request, 'ftptest_listview.html', context=context)

class FTPtestDeleteView(LoginRequiredMixin, DeleteView):
    model = FTPtest
    success_url = '/FTPtest/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

@login_required
def ftptest_create(request):
    if request.method == 'POST':
        form = FTPtestForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = form.cleaned_data['user']

            #check if FTP is more recent than previous test, if so, update FTP in profile
            try:
                latest_prev_test_date = FTPtest.objects.filter(user=instance.user).order_by('date').last().date
                form_FPT_test_date = form.cleaned_data['date']

                if latest_prev_test_date < form_FPT_test_date:
                    profile = instance.user.profile
                    profile.FTP = form.cleaned_data['FTP']
                    profile.weight = form.cleaned_data['weight']
                    profile.save()
            except:
                profile = instance.user.profile
                profile.FTP = form.cleaned_data['FTP']
                profile.weight = form.cleaned_data['weight']
                profile.save()
            instance.save()
            form.save()

            return redirect('/FTPtest/')
        else:
            redirect('/FTPtest/')
    else:
        form = FTPtestForm()
        return render(request, 'ftptest_form.html', {'form': form})

