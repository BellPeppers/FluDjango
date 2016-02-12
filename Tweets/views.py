from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext
from django.views.generic.list import ListView
from .models import Tweet
import requests

class IndexView(ListView):
    template_name = 'Flu/index.html'
    def get_queryset(self):
        return