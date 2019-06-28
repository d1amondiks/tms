# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render_to_response('test_app/index.html')

def base(request):
    return render_to_response('test_app/base.html')

def region(request, regions):
    if regions in ['Brest', 'homel_obl', 'hrodna_obl', 'Magileu_obl',
                   'Minsk', 'Minsk_obl', 'Vitebsk_obl']:
        return render_to_response("test_app/"+regions+".html")
    else: 
        return HttpResponse('<h1>Hello, region!</h1>')
