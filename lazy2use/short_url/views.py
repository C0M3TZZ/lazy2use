from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def shorturl_main(request):
    return render(request, 'shorturl_main.html')

def shorturl_process(request):
    var_url = request.GET['nm_url']
    print(var_url)
    return HttpResponse(var_url)

# Create your views here.
