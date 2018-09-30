from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from . import models as reroom_models


class CatalogItemImgAdminInline(admin.StackedInline):
    model = reroom_models.CatalogItemImg


class CatalogItemAdmin(admin.ModelAdmin):
    inlines = [CatalogItemImgAdminInline]


class HeadingAndTextInlineAdmin(GenericStackedInline):
    model = reroom_models.HeadingAndText
    extra = 1


class CatalogItemInline(admin.StackedInline):
    model = reroom_models.CatalogItem
    extra = 3


class ServicePageAdmin(admin.ModelAdmin):
    inlines = [HeadingAndTextInlineAdmin]


class ServiceAccordionItemAdmin(admin.ModelAdmin):
    inlines = [HeadingAndTextInlineAdmin]
    extra = 1


class ServiceItemAccordionInline(admin.StackedInline):
    model = reroom_models.ServiceItemAccordion
    extra = 0


admin.site.register(reroom_models.IndexPage)
admin.site.register(reroom_models.ContactInfo)
admin.site.register(reroom_models.ProjectsPage)
admin.site.register(reroom_models.CatalogItem, CatalogItemAdmin)
admin.site.register(reroom_models.ServicesPage, ServicePageAdmin)
admin.site.register(reroom_models.ServiceItemAccordion, ServiceAccordionItemAdmin)
admin.site.register(reroom_models.ServicesItem)
