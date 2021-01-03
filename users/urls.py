from django.urls import path

from .views import (
    RiderListView, 
    profile_by_id, 
    LoginView, 
    LogoutView, 
    MyPasswordChangeView, 
    MyPasswordResetDoneView,
    ProfileUpdateView,
    AccountUpdateView,
    profile_raceresults,
    profile_ftptests,
    account_view
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('riders/', RiderListView.as_view(), name='rider-listview'),

    path('profile/<int:pk>/', profile_by_id, name='profile-by-id'),
    path('profile/<int:pk>/edit-profile/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/account/', account_view, name='account-view'),

    path('profile/<int:pk>/update-account/', AccountUpdateView.as_view(), name='account-edit'),
    path('profile/<int:pk>/raceresults/', profile_raceresults, name='profile-raceresults'),
    path('profile/<int:pk>/ftptests/', profile_ftptests, name='profile-ftptests'),

    path('profile/change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('profile/change-password/done/', MyPasswordResetDoneView.as_view(), name='password-change-done'),
]
