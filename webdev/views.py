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

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
from django.http import HttpResponse
import matplotlib.pyplot as plt
import datetime
import random
def refreshCode(request):
    fig = Figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(fig)
    return response
    # return render(request, 'login.html', {'captcha': plt.show()})
