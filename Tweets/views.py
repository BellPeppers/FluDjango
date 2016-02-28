from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext
from django.views.generic.list import ListView
from .models import Tweet
from .tweetHelper import analysis
import requests

class IndexView(ListView):
    template_name = 'Flu/index.html'

    def get_queryset(self):
        tweets = Tweet.objects.all()
        for tweet in tweets:
            tweet.score = analysis(tweet.content)
            tweet.save()
        return