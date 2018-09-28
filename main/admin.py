from django.contrib import admin
from .models import IndexPage, ContactInfo, CatalogItem, ProjectsPage, CatalogItemImg


class CatalogItemImgAdminInline(admin.StackedInline):
    model = CatalogItemImg


class CatalogItemAdmin(admin.ModelAdmin):
    inlines = [CatalogItemImgAdminInline]


admin.site.register(IndexPage)
admin.site.register(ContactInfo)
admin.site.register(ProjectsPage)
admin.site.register(CatalogItem, CatalogItemAdmin)
