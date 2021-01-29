from profile_view.views import add, details, home,list
from django.urls import path

urlpatterns = [
    path('details', details, name="profile_details"),
    path('home', home, name="profile_home"),
    path('add', add, name="profile_add"),
    path('list', list, name="profile_list"),
]
