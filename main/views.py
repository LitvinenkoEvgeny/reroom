from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from . import models
from django.views.generic import DetailView, ListView
from . import mixins


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


class CatalogView(mixins.ContactInfoMixin, ListView):
    model = models.CatalogItem
    template_name = 'main/catalog.html'
    context_object_name = 'catalog_items'

    def get_queryset(self):
        if 'type' in self.kwargs:
            return get_list_or_404(models.CatalogItem, type=self.kwargs['type'])
        return models.CatalogItem.objects.all()


class ServicesListView(mixins.ContactInfoMixin, ListView):
    model = models.ServicesItem
    template_name = 'main/services_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServicesListView, self).get_context_data(**kwargs)
        context['services_page'] = models.ServicesPage.objects.first()
        return context


class ServiceItemDetail(mixins.ContactInfoMixin, DetailView):
    model = models.ServicesItem
    template_name = 'main/service_item.html'

    def get_object(self, queryset=None):
        if 'type' in self.kwargs:
            return get_object_or_404(models.ServicesItem, type=self.kwargs['type'])


class ContactsView(mixins.ContactInfoMixin, DetailView):
    model = models.ContactsPage
    template_name = 'main/contacts.html'

    def get_object(self, queryset=None):
        return self.model.objects.first()


class SingleItemView(mixins.ContactInfoMixin, DetailView):
    model = models.CatalogItem
    context_object_name = 'catalog_item'
    template_name = 'main/catalog_item.html'

    def get_context_data(self, **kwargs):
        context = super(SingleItemView, self).get_context_data(**kwargs)
        return context
