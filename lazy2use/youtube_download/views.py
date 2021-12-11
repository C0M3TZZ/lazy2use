import urllib
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from django.http import FileResponse
import requests
import subprocess
import os
import pathlib

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
    high_dev = {}
    for i in stream_data.streaming_data['adaptiveFormats']:
        all_video_quarry[i['itag']] = i['url']
    for i in stream_data.streams.filter(only_audio=True):
        audio_url.append(
            {i.abr: urllib.parse.quote_plus(all_video_quarry[i.itag])})
    for i in stream_data.streaming_data["formats"][::-1]:
        video_url.append(
            {i['qualityLabel']: urllib.parse.quote_plus(i['url'])})
    for i in stream_data.streaming_data['adaptiveFormats']:
        high_dev[i['qualityLabel']] = '/beta/?url=' + urllib.parse.quote_plus(stream_data.watch_url) + '&qulity=' + i['qualityLabel'] + '&fps=' + str(i['fps'])
        if i['qualityLabel'] == "720p60":
            break
        elif i['qualityLabel'] == "720p":
            high_dev.pop('720p')
            break
    return render(request, 'yt_download.html', {'video': video_url, 'audio_track': audio_url, 'title_video': title_url, 'img_url': img_url,
                                                'yt_author': yt_tile, 'author_link': yt_a_url, 'video_url': stream_data.watch_url, "highdev": high_dev})


def yt_mp4(request):
    var_url = http.HttpResponse(request.GET.get('url')).content.decode()
    var_name = http.HttpResponse(request.GET.get('name')).content.decode()
    fr = FileResponse(requests.get(var_url, allow_redirects=True))
    fr['Content-Type'] = 'video/mp4'
    fr['Content-Disposition'] = 'attachment; filename=' + \
        var_name.split("?v=")[1] + ".mp4"
    return fr


def yt_mp3(request):
    var_url = http.HttpResponse(request.GET.get('url')).content.decode()
    var_name = http.HttpResponse(request.GET.get('name')).content.decode()
    print(var_name)
    fr = FileResponse(requests.get(var_url, allow_redirects=True))
    fr['Content-Type'] = 'audio/webm'
    fr['Content-Disposition'] = 'attachment; filename=' + \
        var_name.split("?v=")[1] + ".weba"
    return fr


def yt_highdefi(request):
    return HttpResponse(pathlib.Path().resolve())
    # var_url = http.HttpResponse(request.GET.get('url')).content.decode()
    # var_qulity = http.HttpResponse(request.GET.get('qulity')).content.decode()
    # var_fps = http.HttpResponse(request.GET.get('fps')).content.decode()
    # var_clip = YouTube(var_url)
    # var_video_path = "youtube_download/download/" + \
    #     var_clip.video_id + "/" + var_clip.video_id + ".webm"
    # var_audio_path = "youtube_download/download/" + \
    #     var_clip.video_id + "/" + var_clip.video_id + ".weba"
    # var_export = "youtube_download/download/" + var_clip.video_id + \
    #     "/" + var_clip.video_id+"_"+var_qulity+".mp4"
    # if os.path.exists(var_export) == False:
    #     var_clip.streams.filter(resolution=var_qulity.replace("p60", 'p')).first().download(
    #         'youtube_download/download/' + var_clip.video_id, var_clip.video_id + '.webm')
    #     var_clip.streams.get_audio_only().download('youtube_download/download/' +
    #                                                 var_clip.video_id, var_clip.video_id + '.weba')
    #     cmd = 'ffmpeg -y -i ' + var_video_path + ' -r ' + var_fps + ' -i ' + var_audio_path + \
    #         ' -strict -2 -filter:a aresample=async=1 -c:a flac -c:v copy ' + var_export
    #     subprocess.call(cmd, shell=False)
    # if os.path.exists(var_video_path):
    #     os.remove(var_video_path)
    # if os.path.exists(var_audio_path):
    #     os.remove(var_audio_path)
    # fr = FileResponse(open(var_export, 'rb'))
    # fr['Content-Type'] = 'video/mp4'
    # fr['Content-Disposition'] = 'attachment; filename=' + \
    #     var_clip.video_id+"_"+var_qulity+".mp4"
    # return fr

def get_path(request):
    return HttpResponse(pathlib.Path().resolve())
