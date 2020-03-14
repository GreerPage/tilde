from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import *
from django.conf import settings
import json

# Create your views here.
def index(request):

    if request.method == 'POST': 
        form = imgForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            w = form.cleaned_data['width']
            h = form.cleaned_data['height']
            original_image = form.cleaned_data['img']
            form.save() 
            newName = generateName(0, str(original_image))
            cropper(original_image, x, y, h, w, newName)
            with open(os.path.join(settings.MEDIA_ROOT, 'json/imageviews.json')) as file:
                data = json.load(file)
                data[newName] = 0
                with open(os.path.join(settings.MEDIA_ROOT, 'json/imageviews.json'), 'w') as file1:
                    json.dump(data, file1)
            return redirect('/gallery') 
    else: 
        form = imgForm() 
    context = {
        'nav': True,
        'form': form,
    }
    return render(request, 'post.html', context)