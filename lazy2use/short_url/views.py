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

def shorturl_main(request): #main
    db.objects.all()
    return render(request, 'shorturl_new.html')

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
        found_url = db.objects.filter(lurl=var_url).first()
        if found_url:
            return redirect('displayshorturl', url=found_url.surl)
        else:
            short_url = shorten_url()
            new_url = db(lurl=var_url, surl=short_url)
            db.save(new_url)
            return redirect('displayshorturl', url=short_url)
    else:
        return render(request, 'shorturl_new.html')

def display_short_url(request, url): #url result
    return render(request, 'shorturl_out.html', {'short_url_display':url})

def redirection(request, short_url): # redirect 
    long_url = db.objects.filter(surl=short_url).first()
    if long_url:
        return redirect(long_url.lurl)
    else:
        return render(request, '404.html')
