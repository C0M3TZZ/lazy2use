from django.shortcuts import render
# Create your views here.
def hello(request):
    tags = ['นํ้าตาล','ฝน','ธรรมชาติ']
    ratings = 5
    return render(request,'index.html',
    {'name':'โปรเเกรมส่งจากname',
    'author':'คนเเต่ง',
    'tags':tags,
    'rating':ratings
    })

def page1(request):
    return render(request,'page1.html')

def createform(request):
    return render(request,'form.html')

def addblog(request):
    name=request.POST['name']
    description=request.POST['description']
    return render(request,'result.html',{'name':name,'description':description})