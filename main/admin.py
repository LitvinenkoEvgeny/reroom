from django.contrib import admin
from .models import IndexPage, ContactInfo, CatalogItem, ServicesPage, CatalogItemImg


class CatalogItemImgAdminInline(admin.StackedInline):
    model = CatalogItemImg


class CatalogItemAdmin(admin.ModelAdmin):
    inlines = [CatalogItemImgAdminInline]


admin.site.register(IndexPage)
admin.site.register(ContactInfo)
admin.site.register(ServicesPage)
admin.site.register(CatalogItem, CatalogItemAdmin)
