from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def error_404(request, exception):
    data = {
        'error': 'page not found',
        'errornum': '404',
        'linknum': '1',
        'nav': True,
    }
    return render(request,'error.html', data)

def error_500(request):
    data = {
        'error': 'internal server error',
        'errornum': '500',
        'linknum': '1',
        'nav': True,
    }
    return render(request,'error.html', data)
def error_400(request, exception):
    data = {
        'error': 'bad request',
        'errornum': '400',
        'linknum': '1',
        'nav': True,
    }
    return render(request,'error.html', data)
def error_403(request, exception):
    data = {
        'error': 'forbidden',
        'errornum': '403',
        'linknum': '1',
        'nav': True,
    }
    return render(request,'error.html', data)

def error(request, errornum, error):
    valid_error_nums = '500 404'.split()
    valid_errors = ['file name cannot contain spaces']
    if errornum not in valid_error_nums:
        raise Http404
    if error not in valid_errors:
        raise Http404
    context = {
        'error': error,
        'errornum': errornum,
        'nav': True
    }
    return render(request, 'error.html', context)
    