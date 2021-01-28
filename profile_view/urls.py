from profile_view.views import details
from django.urls import path

urlpatterns = [
    path('details', details, name="profile_details"),
]
