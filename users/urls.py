from django.urls import path

from .views import (
    RiderListView, 
    profile_by_id, 
    LoginView, 
    LogoutView, 
    MyPasswordChangeView, 
    MyPasswordResetDoneView,
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('riders/', RiderListView.as_view(), name='rider-listview'),
    path('profile/<int:pk>', profile_by_id, name='profile-by-id'),
    path('change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name='password-change-done'),
]
