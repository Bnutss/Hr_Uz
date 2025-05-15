from django.urls import path
from .views import *

app_name = 'mobileapp'

urlpatterns = [
    path('api/job-applications/', JobApplicationListCreateAPIView.as_view(), name='jobapplication-list-create'),
    path('api/job-applications/<int:pk>/', JobApplicationRetrieveUpdateDestroyAPIView.as_view(),
         name='jobapplication-detail'),
]
