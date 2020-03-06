from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import *

# Create your views here.
def index(request):

    if request.method == 'POST': 
        form = imgForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/') 
    else: 
        form = imgForm() 
    context = {
        'nav': True,
        'form': form,
    }
    return render(request, 'post.html', context)