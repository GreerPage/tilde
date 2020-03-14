from django.shortcuts import render
import json
from django.conf import settings
import os
import operator

# Create your views here.
def index(request):
    postnames= os.listdir('{}/images'.format(settings.MEDIA_ROOT))
    linknames = []
    for x in postnames:
        linknames.append(os.path.splitext(x)[0]) 
    with open(os.path.join(settings.MEDIA_ROOT, 'json/imageviews.json')) as file:
                data = json.load(file)
                highest = sorted(data, key=data.get, reverse=True)[:10]
                print(highest)
    highestfiles = []
    for x in highest:
        if x in linknames:
            i = linknames.index(x)
            highestfiles.append(postnames[i])
            
    print(highestfiles)
    context = {
        'nav': True,
        'images': zip(highestfiles, highest)
    }
    return render(request, 'home.html', context)