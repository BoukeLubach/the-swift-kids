from django.urls import path
from .views import raceview, RaceCreateView, RaceListView

urlpatterns = [
    path('season/<int:season>/create/', RaceCreateView.as_view(), name='race-create'),
    path('season/<int:season>/', RaceListView.as_view(), name='race-listview'),
    
]
