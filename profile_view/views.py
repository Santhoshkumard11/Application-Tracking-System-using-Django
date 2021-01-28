from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def details(request):
    
    return JsonResponse({"result": "Hello World!!!"}, status= 200)