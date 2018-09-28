from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from .models import IndexPage, ContactInfo, ProjectsPage, CatalogItem
from django.views.generic import DetailView, ListView


# Create your views here.
def index(request):
    context = {
        'index_page': IndexPage.objects.first(),
        'contact': ContactInfo.objects.first(),
        'service_objects': ProjectsPage.objects.first().get_random_catalog_items(3)
    }
    return render_to_response('main/index.html', context=context)


def about(request):
    return render_to_response('main/about.html')


class CatalogView(ListView):
    model = CatalogItem
    template_name = 'main/catalog.html'
    context_object_name = 'catalog_items'

    def get_queryset(self):
        if 'type' in self.kwargs:
            return get_list_or_404(CatalogItem, type=self.kwargs['type'])
        return CatalogItem.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['contact'] = ContactInfo.objects.first()
        return context


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


class SingleItemView(DetailView):
    model = CatalogItem
    context_object_name = 'catalog_item'
    template_name = 'main/catalog_item.html'

    def get_context_data(self, **kwargs):
        context = super(SingleItemView, self).get_context_data(**kwargs)
        context['contact'] = ContactInfo.objects.first()
        return context
