from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('catalog/<str:type>', views.CatalogView.as_view(), name='catalog'),
    path('catalog/item/<int:pk>', views.SingleItemView.as_view(), name='catalog-item'),
    path('services', views.ServicesListView.as_view(), name='services'),
    path('services/<str:type>', views.ServiceItemDetail.as_view(), name='services-item'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('mail', views.mail, name='mail'),
]
