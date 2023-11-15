from django.shortcuts import render
from django import http
import json
from ecom_forms.forms_functions.forms import ValidateForm



def form_return_from_database(request):
    if request.method == "POST":
        if not request.POST:
            return http.HttpResponse(json.dumps({"error": "request must have body"}))
        
        users_form = ValidateForm(request.POST.dict())
        result = users_form.find_suitable_form()

        if type(result) is str:
            return http.HttpResponse(json.dumps({"form_name": result}))
        
        return http.HttpResponse(json.dumps(result))

    

    else:
        return http.HttpResponse("<h1>Oops! This page made for POSTS requests!</h1>")


