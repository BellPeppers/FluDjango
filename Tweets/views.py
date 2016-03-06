from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext
from django.core import serializers
from django.views.generic.list import ListView
from .models import Tweet, Region
from .tweetHelper import analysis
import requests

class IndexView(ListView):
    template_name = 'Flu/index.html'
    context_object_name = 'regionList'

    def get_queryset(self):
        return Region.objects.all()