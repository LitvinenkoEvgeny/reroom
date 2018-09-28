from django.contrib import admin
from . import models as reroom_models


class CatalogItemImgAdminInline(admin.StackedInline):
    model = reroom_models.CatalogItemImg


class CatalogItemAdmin(admin.ModelAdmin):
    inlines = [CatalogItemImgAdminInline]


admin.site.register(reroom_models.IndexPage)
admin.site.register(reroom_models.ContactInfo)
admin.site.register(reroom_models.ProjectsPage)
admin.site.register(reroom_models.CatalogItem, CatalogItemAdmin)
