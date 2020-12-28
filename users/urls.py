from django.urls import path

from .views import RiderListView, profile_by_id, LoginView, LogoutView 

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('riders/', RiderListView.as_view(), name='rider-listview'),
    path('profile/<int:pk>', profile_by_id, name='profile-by-id'),

]
