from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.
def index(request):
    context = {
        'nav': True,
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'gallery.html', context)