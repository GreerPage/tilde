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
            caption = form.cleaned_data['caption']
            original_image = form.cleaned_data['img']
            form.save() 
            newName = generateName(0, str(original_image))
            cropper(original_image, x, y, h, w, newName)
            try:
                with open(os.path.join(settings.BASE_DIR, 'json/imageviews.json')) as file:
                    data = json.load(file)
                    data[newName] = 0
                    with open(os.path.join(settings.BASE_DIR, 'json/imageviews.json'), 'w') as file1:
                        json.dump(data, file1)
            except FileNotFoundError:
                try:   
                    open(os.path.join(settings. BASE_DIR, 'json/postcaptions.json'), 'a').close()
                    with open(os.path.join(settings.BASE_DIR, 'json/postcaptions.json'), 'w') as file1:
                        data = {}
                        data[newName] = 0
                        json.dump(data, file1)
                except FileNotFoundError:
                    os.mkdir(os.path.join(settings. BASE_DIR, 'json/'))
                    open(os.path.join(settings. BASE_DIR, 'json/imageviews.json'), 'a').close()
                    with open(os.path.join(settings.BASE_DIR, 'json/imageviews.json'), 'w') as file1:
                        data = {}
                        data[newName] = 0
                        json.dump(data, file1)
            except:
                with open(os.path.join(settings.BASE_DIR, 'json/imageviews.json'), 'w') as file1:
                        data = {}
                        data[newName] = 0
                        json.dump(data, file1)
            try:
                with open(os.path.join(settings.BASE_DIR, 'json/postcaptions.json')) as file:
                    data = json.load(file)
                    data[newName] = caption
                    with open(os.path.join(settings.BASE_DIR, 'json/postcaptions.json'), 'w') as file1:
                        json.dump(data, file1)
            except FileNotFoundError:
                    open(os.path.join(settings. BASE_DIR, 'json/postcaptions.json'), 'a').close()
                    with open(os.path.join(settings.BASE_DIR, 'json/postcaptions.json'), 'w') as file1:
                        data = {}
                        data[newName] = caption
                        json.dump(data, file1)
            except:
                with open(os.path.join(settings.BASE_DIR, 'json/postcaptions.json'), 'w') as file1:
                        data = {}
                        data[newName] = caption
                        json.dump(data, file1)

            return redirect('/gallery') 
    else: 
        form = imgForm() 
    context = {
        'nav': True,
        'form': form,
    }
    return render(request, 'post.html', context)