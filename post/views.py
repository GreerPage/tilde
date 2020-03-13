from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import *

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
            cropper(original_image, x, y, h, w)
            return redirect('/gallery') 
    else: 
        form = imgForm() 
    context = {
        'nav': True,
        'form': form,
    }
    return render(request, 'post.html', context)