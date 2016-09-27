from django.conf.urls import url
from . import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.home , name = 'home'),
    url(r'^news/$' , views.news , name = 'news'),
    url(r'^add_news/$' , views.add_news , name = 'add_news'),
    url(r'^post/$' , views.post , name = 'post'),
]
