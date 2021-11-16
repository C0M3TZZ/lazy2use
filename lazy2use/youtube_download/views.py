from django import http
from django.shortcuts import render
from django.http import HttpResponseRedirect
from pytube import YouTube

# Create your views here.

# Youtube Downloader

def yt_menu(request):
    return render(request, 'yt_menu.html')


def yt_download(request):
    var_url = request.GET['url']
    stream_data = YouTube(var_url)
    img_url = stream_data.thumbnail_url
    title_url = stream_data.title
    yt_tile = stream_data.author
    yt_a_url = stream_data.channel_url
    all_video_quarry = {}
    audio_url = []
    video_url = []
    for i in stream_data.streaming_data['adaptiveFormats']:
        all_video_quarry[i['itag']] = i['url']
    for i in stream_data.streams.filter(only_audio=True):
        audio_url.append({i.abr: all_video_quarry[i.itag]})
    for i in stream_data.streaming_data["formats"][::-1]:
        video_url.append({i['qualityLabel']: i['url']})
    return render(request, 'yt_download.html', {'video': video_url, 'audio_track': audio_url, 'title_video': title_url, 'img_url': img_url,
                                                'yt_author': yt_tile, 'author_link': yt_a_url, 'video_url': var_url})


# URL Shortener

def shorturl_main(request):
    if request.method == 'POST':
        url_rs = request.form["nm_url"]
        return url_rs
    else:
        return render(request, 'shorturl_main.html')

def home(request):
    return render(request, 'home.html')