from django.shortcuts import render_to_response
from .models import IndexPage, ContactInfo, ServicesPage


# Create your views here.
def index(request):
    context = {
        'index_page': IndexPage.objects.first(),
        'contact': ContactInfo.objects.first(),
        'service_objects': ServicesPage.objects.first().get_random_catalog_items(3)
    }
    return render_to_response('main/index.html', context=context)


def about(request):
    return render_to_response('main/about.html')


def catalog(request):
    return render_to_response('main/catalog.html')


def services(request):
    return render_to_response('main/services.html')


def design(request):
    return render_to_response('main/design.html')


def home_repair(request):
    return render_to_response('main/home-repair.html')


def office_repair(request):
    return render_to_response('main/office-repair.html')


def construction(request):
    return render_to_response('main/construction.html')


def contacts(request):
    return render_to_response('main/contacts.html')
