from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    all_sensitive_news = SensitiveNews.objects.all()
    all_recent_news = RecentNews.objects.order_by('-post_date')

    context = {
        'all_sensitive_news': all_sensitive_news,
        'all_recent_news': all_recent_news,
    }

    # return HttpResponse("You are in home page.")
    return render(request, 'home/home.html', context)

