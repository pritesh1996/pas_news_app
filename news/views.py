from django.shortcuts import render
from .models import News
from django.http import HttpResponse
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request,'home.html')

def news(request):
    all_news_full = News.objects.all().order_by('datetime')
    paginator = Paginator(all_news_full, 4)
    page = request.GET.get('page')
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        all_news = paginator.page(paginator.num_pages)
    return render(request, "news.html", {'all_news': all_news , 'range': paginator.page_range })

def add_news(request):
    return render(request,'add_news.html')

def post(request):
    new_news = News()
    new_news.company = request.POST['company']
    new_news.subject = request.POST['subject']
    new_news.body = request.POST['body']
    new_news.save()
    return render(request , 'success.html')
