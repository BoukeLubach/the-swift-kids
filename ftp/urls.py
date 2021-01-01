from django.urls import path
from .views import FTPtestListView, ftptest_create, FTPtestDeleteView

urlpatterns = [
    path('', FTPtestListView.as_view(), name='FTP-test-overview'),
    path('add/', ftptest_create, name='FTP-test-add'),
    path('<int:pk>/delete/', FTPtestDeleteView.as_view(), name='FTP-test-delete')
]
