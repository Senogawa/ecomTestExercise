from django.shortcuts import render
from django import http
import json



def form_return_from_database(request):
    if request.method == "POST":
       return http.HttpResponse(json.dumps({"abobius":"belbi"}))

    else:
        return http.HttpResponse("<h1>Oops! This page made for POSTS requests!</h1>")


