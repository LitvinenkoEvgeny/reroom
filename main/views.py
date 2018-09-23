from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    return render_to_response('main/index.html')


def about(request):
    return render_to_response('main/about.html')


def catalog(request):
    return render_to_response('main/catalog.html')
