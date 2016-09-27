from django.shortcuts import render
from .models import News
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def news(request):
    all_news = News.objects.all()
    return render(request, "news.html", {'all_news': all_news})

def add_news(request):
    return render(request,'add_news.html')

def post(request):
    new_news = News()
    new_news.company = request.POST['company']
    new_news.subject = request.POST['subject']
    new_news.body = request.POST['body']
    new_news.save()
    return render(request , 'success.html')
