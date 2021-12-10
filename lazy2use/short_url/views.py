from django import urls
from . import views
from django.conf.urls import url
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.urls import path
from .models import urldb as db
import string
import random
#import pymongo
# Create your views here.

def shorturl_main(request):
    db.objects.all()
    return render(request, 'shorturl_main.html')

def shorten_url(): #url genarator
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = db.objects.filter(surl=rand_letters).first()
        if not short_url:
            return rand_letters

def shorturl_process(request): #url_process
    if request.method == "POST":
        var_url = request.POST['nm_url']
        found_url = db.objects.filter(lurl=var_url).first() # databases lurl 
        if found_url:
            return redirect('displayshorturl', url=found_url.surl)
        else:
            short_url = shorten_url()
            new_url = db(lurl=var_url, surl=short_url)
            # fix insert mongodb https://www.youtube.com/watch?v=I17uA1sVQ2g
            db.save(new_url)
            return redirect('displayshorturl', url=short_url)
    else:
        return render(request, 'shorturl_main.html')
        #var_url = request.POST['nm_url']
        # var_url = request.POST(shorten_url)
        # print(var_url)
        # return HttpResponse(var_url)
        #return HttpResponse['nm_url']

def display_short_url(request, url):
    return render(request, 'short_rs.html', {'short_url_display':url})

def redirection(request, short_url):
    long_url = db.objects.filter(surl=short_url).first()
    if long_url:
        return redirect(long_url.lurl)
    else:
        return render(request, '404.html')