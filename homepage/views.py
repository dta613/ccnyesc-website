# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')
