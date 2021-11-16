from django import http
from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

# Create your views here.
def yt_menu(request):
    return render(request, 'yt_menu.html')

def yt_download(request):
    var_url = request.GET['url']
    downloader = YouTube(var_url).streaming_data
    url = []
    for i in downloader["formats"][::-1]:
        url.append({i['qualityLabel']:i['url']})
    return render(request, 'yt_download.html', {'url' : url})
