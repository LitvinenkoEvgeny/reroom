from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from . import models
from django.views.generic import DetailView, ListView


# Create your views here.
def index(request):
    context = {
        'index_page': models.IndexPage.objects.first(),
        'contact': models.ContactInfo.objects.first(),
        'service_objects': models.ProjectsPage.objects.first().get_random_catalog_items(3)
    }
    return render_to_response('main/index.html', context=context)


def about(request):
    return render_to_response('main/about.html')


class CatalogView(ListView):
    model = models.CatalogItem
    template_name = 'main/catalog.html'
    context_object_name = 'catalog_items'

    def get_queryset(self):
        if 'type' in self.kwargs:
            return get_list_or_404(models.CatalogItem, type=self.kwargs['type'])
        return models.CatalogItem.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['contact'] = models.ContactInfo.objects.first()
        return context


def catalog(request):
    return render_to_response('main/catalog.html')


# def services(request):
#     return render_to_response('main/services_list.html')

class ServicesListView(ListView):
    model = models.ServicesItem
    template_name = 'main/services_list.html'

    def get_queryset(self):
        if 'type' in self.kwargs:
            return get_list_or_404(models.ServicesItem, type=self.kwargs['type'])
        return models.ServicesItem.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServicesListView, self).get_context_data(**kwargs)
        context['contact'] = models.ContactInfo.objects.first()
        context['services_page'] = models.ServicesPage.objects.first()
        return context


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


class SingleItemView(DetailView):
    model = models.CatalogItem
    context_object_name = 'catalog_item'
    template_name = 'main/catalog_item.html'

    def get_context_data(self, **kwargs):
        context = super(SingleItemView, self).get_context_data(**kwargs)
        context['contact'] = models.ContactInfo.objects.first()
        return context
