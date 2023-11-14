from django.shortcuts import render
from django import http



def form_return_from_database(request):
    print(request.POST)
    return http.HttpResponse("")


