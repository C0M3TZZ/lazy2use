"""lazy2use URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from youtube_download import views as yt
from short_url import views as su

urlpatterns = [
    #youtube
    path('admin/', admin.site.urls),
    path('youtube/', yt.yt_menu),
    path('youtube/download/', yt.yt_download),
    path('', yt.home),
    #shorturl
    path('url/', su.shorturl_main),
    path('url/short_url', su.shorturl_process),
    path('url/display/<url>', su.display_short_url)
]
