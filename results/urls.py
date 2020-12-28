from django.urls import path
from results.views import Season1ResultsListView, season_listview, race_analytics

urlpatterns = [
    path('results/season/1/team/<int:team>/', Season1ResultsListView.as_view(), name='season-1-results'),
    path('season/', season_listview, name='season-listview'),
    path('race_analytics/', race_analytics, name='race-analytics'),
]
