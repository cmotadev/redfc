from django.urls import path
from .feeds import MatchFeed

urlpatterns = [
    path('latest/feed.ics', MatchFeed()),
]
