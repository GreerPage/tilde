from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import glob
from pathlib import Path

# Create your views here.
def index(request):
    postnamessorted = os.listdir('{}/images'.format(settings.MEDIA_ROOT))
    postnamessortedpath = []
    for file in postnamessorted:
        postnamessortedpath.append(os.path.join(settings.MEDIA_ROOT, 'images/{}'.format(file)))
    sorted1 = sorted(postnamessortedpath,key=os.path.getctime, reverse=True)
    postnamesext = []
    for x in sorted1:
        postnamesext.append(os.path.basename(x))
    postnames = []
    for x in postnamesext:
        postnames.append(os.path.splitext(x)[0])
    context = {
        'nav': True,
        'images': zip(postnamesext, postnames),
    }
    return render(request, 'gallery.html', context)

def postPage(request, postname):
    postnames = []
    for x in os.listdir('{}/images'.format(settings.MEDIA_ROOT)):
        postnames.append(os.path.splitext(x)[0])
    if postname not in postnames:
        raise Http404()
    for x in os.listdir('{}/images'.format(settings.MEDIA_ROOT)):
        if os.path.splitext(x)[0]==postname:
            postext = x
    context = {
        'postname': postname,
        'postnameext': postext,
    }
    return render(request, 'postpage.html', context)
def p(index):
    return redirect('/gallery')