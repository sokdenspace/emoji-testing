from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def efeed(response):
    return render(response, "eFeed/efeed.html", {})

def echat(response):
    return render(response, "eChat/echat.html", {})

def eread(response):
    return render(response, "eRead/eread.html", {})

def ewatch(response):
    return render(response, "eWatch/ewatch.html", {})

def emusic(request):
    return render(request, "eMusic/emusic.html", {})
