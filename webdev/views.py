from django.shortcuts import render


# Create your views here.


def hello(request):
    context = {}
    # context['url'] = request.get_host()+request.get_full_path()
    context['hello'] = 'Hello world!'
    return render(request, 'index.html', context)


def login(request):
    context = {}
    # context['url'] = request.get_host()+request.get_full_path()
    context['hello'] = 'Hello world!'
    return render(request, 'login.html', context)


