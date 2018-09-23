from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    return render_to_response('main/index.html')


def about(request):
    return render_to_response('main/about.html')


def catalog(request):
    return render_to_response('main/catalog.html')


def services(request):
    return render_to_response('main/services.html')


def contacts(request):
    return render_to_response('main/contacts.html')


def design(request):
    return render_to_response('main/design.html')


def home_repair(request):
    return render_to_response('main/home-repair.html')


def office_repair(request):
    return render_to_response('main/office-repair.html')
