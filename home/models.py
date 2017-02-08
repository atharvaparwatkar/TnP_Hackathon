from django.db import models
from django.utils import timezone


class SensitiveNews(models.Model):
    news = models.CharField(max_length=250)
    link = models.CharField(max_length=250, default="#")

    def __str__(self):
        return self.news


class RecentNews(models.Model):
    news = models.CharField(max_length=250)
    link = models.CharField(max_length=250, default="#")
    post_date = models.DateTimeField('date posted', auto_now_add=True)

    def __str__(self):
        return self.news
