from django import urls
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import urldb as db
import pymongo
# Create your views here.

def shorturl_main(request):
    db.objects.all()
    return render(request, 'shorturl_main.html')

def shorten_url():
    return "abc"

def shorturl_process(request):
    var_url = request.POST['nm_url']
    if var_url == request.POST['nm_url']:
        found_url = db.objects.filter(lurl=var_url).first() # store in databases lurl 
        if found_url:
            return f"{found_url.surl}"
        else:
            short_url = shorten_url()
            new_url = db(var_url, short_url)
            # fix insert mongodb https://www.youtube.com/watch?v=I17uA1sVQ2g
            db.insert_one(new_url)
            return shorten_url
    else:
        return render(request, 'shorturl_main.html')
    # var_url = request.POST['nm_url']
    # print(var_url)
    # return HttpResponse(var_url)