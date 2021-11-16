from django.shortcuts import render
# Create your views here.

def shorturl_main(request):
    return render(request, 'shorturl_main.html')