# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django import template
from django.db import connection
from django.shortcuts import render
import json
import itertools
from .models import subscriber
from django.shortcuts import render_to_response
from app.models import subscriber
from django.core import serializers
resultdisplay = subscriber.objects.first()
context = {'subs': resultdisplay}
print(context)

def showapp(request):
    context = {}
    resultdisplay = list(subscriber.objects.filter(err = 50))
    context = {'subs': resultdisplay}
    return render(request,context)


def index(request):
    resultdisplay = subscriber.objects.all()
    context = {'subs': resultdisplay}
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        resultdisplay = subscriber.objects.first()
        context = {'subs': resultdisplay}

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
