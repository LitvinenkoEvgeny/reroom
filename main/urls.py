from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<str:type>', views.CatalogView.as_view(), name='catalog'),
    path('catalog/item/<int:pk>', views.SingleItemView.as_view(), name='catalog-item'),
    path('services', views.services, name='services'),
    path('services/design', views.design, name='design'),
    path('services/home-repair', views.home_repair, name='home-repair'),
    path('services/office-repair', views.office_repair, name='office-repair'),
    path('services/construction', views.construction, name='construction'),
    path('contacts', views.contacts, name='contacts'),
]
