from django import urls
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import urldb as db
import string
import random
#import pymongo
# Create your views here.

def shorturl_main(request):
    db.objects.all()
    return render(request, 'shorturl_main.html')

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = db.objects.filter(surl=rand_letters).first()
        if not short_url:
            return rand_letters

def shorturl_process(request):
    if request.method == "POST":
        var_url = request.POST['nm_url']
        found_url = db.objects.filter(lurl=var_url).first() # store in databases lurl 
        if found_url:
            return f"{found_url.surl}"
        else:
            short_url = shorten_url()
            new_url = db(var_url, short_url)
            # fix insert mongodb https://www.youtube.com/watch?v=I17uA1sVQ2g
            db.save(new_url)
            return shorten_url
    else:
        return render(request, 'shorturl_main.html')
    # var_url = request.POST['nm_url']
    # print(var_url)
    # return HttpResponse(var_url)