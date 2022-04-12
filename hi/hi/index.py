import json
from django.http import HttpResponse
from django.shortcuts import render

def web(request):
    print(request.POST)
    return render(request,"form.html") 