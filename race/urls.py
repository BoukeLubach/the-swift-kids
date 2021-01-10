from django.urls import path

from .views import (
    race_detailview, 
    RaceCreateView, 
    RaceListView, 
    StaffRaceRegisterView, 
    SignupDeleteView, 
    RaceRegistrationView,
    signup_selection
) 

urlpatterns = [
    path('season/<int:season>/create/', RaceCreateView.as_view(), name='race-create'),
    path('season/<int:season>/', RaceListView.as_view(), name='race-listview'),
    path('<int:pk>/', race_detailview, name='race-detail'),
    path('signup/<int:pk>/', RaceRegistrationView.as_view(), name='race-signup'),
    path('signup/<int:pk>/staff_signup', StaffRaceRegisterView.as_view(), name='staff-race-signup'),
    path('signup/<int:pk>/delete', SignupDeleteView.as_view(), name='remove-signup'),
    path('signup/<int:pk>/select', signup_selection, name='signup-select'),

]
