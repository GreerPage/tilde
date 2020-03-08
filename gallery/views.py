from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    postnames = []
    for x in os.listdir('{}/images'.format(settings.MEDIA_ROOT)):
        postnames.append(os.path.splitext(x)[0])
    context = {
        'nav': True,
        'images': zip(os.listdir('{}/images'.format(settings.MEDIA_ROOT)), postnames),
    }
    return render(request, 'gallery.html', context)

def postPage(request, postname):
    postnames = []
    for x in os.listdir('{}/images'.format(settings.MEDIA_ROOT)):
        postnames.append(os.path.splitext(x)[0])
    if postname not in postnames:
        return Http404()
    for x in os.listdir('{}/images'.format(settings.MEDIA_ROOT)):
        if os.path.splitext(x)[0]==postname:
            postext = x
    context = {
        'postname': postname,
        'postnameext': postext,
    }
    return render(request, 'postpage.html', context)
