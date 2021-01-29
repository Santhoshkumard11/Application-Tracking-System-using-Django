from profile_view.utils import get_profile_view_model
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def details(request):

    return JsonResponse({"result": "Hello World!!!"}, status=200)


def home(request):

    title = " Welcome to ATS!!!"

    return render(request, "profile_home.html", {"title": title})


def add(request):

    title = " Add Profile View"

    return render(request, "profile_add.html", {"title": title})


def list(request):

    # get the list of name from the db

    profile_view_model = get_profile_view_model()

    return render(request, "profile_list.html", {"profile_view_model": profile_view_model})

""" 
create
read
update
delete
CRUD
"""