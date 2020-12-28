from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
# @login_required
def home(request):
    return render(request, 'home.html')
