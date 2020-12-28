from django.urls import path
from .views import raceview, RaceCreateView, RaceListView

urlpatterns = [
    path('create/', RaceCreateView.as_view(), name='race-create'),
    path('season/<int:season>/', RaceListView.as_view(), name='race-listview'),
    
]
