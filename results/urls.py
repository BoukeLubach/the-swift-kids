from django.urls import path
from results.views import (
    Season1ResultsListView, 
    season_listview, 
    race_analytics, 
    season1_raceresult_detail,
    upload_fit_file,
    fit_upload_failed_user_not_available,
    fit_upload_failed_filetype,
)

urlpatterns = [
    path('season/<int:season>/team/<int:team>/', Season1ResultsListView.as_view(), name='season-1-results'),
    path('season/<int:season>/team/<int:team>/race/<int:race>/', season1_raceresult_detail, name='season1-raceresults-detail'), 
    path('season/<int:season>/team/<int:team>/race/<int:race>/upload-fit-file', upload_fit_file, name='fitfile-upload'), 
    path('season/<int:season>/team/<int:team>/race/<int:race>/upload-failed/result-does-not-exist', fit_upload_failed_user_not_available, name='upload-failed-user-not-available'),     
    path('season/<int:season>/team/<int:team>/race/<int:race>/upload-failed/filetype-error', fit_upload_failed_filetype, name='upload-failed-filetype'),     
    path('season/', season_listview, name='season-listview'),
    path('race_analytics/', race_analytics, name='race-analytics'),
]
