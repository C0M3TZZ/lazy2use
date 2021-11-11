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