from .models import *

from django.contrib import admin

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Brand, BrandAdmin)


class ParentAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Parent, ParentAdmin)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Collection, CollectionAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Color, ColorAdmin)


class ConsistAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Consist, ConsistAdmin)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Content, ContentAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Country, CountryAdmin)


class OptionAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Option, OptionAdmin)


class KindAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Kind, KindAdmin)


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Season, SeasonAdmin)


class SiAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Si, SiAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(Warehouse, WarehouseAdmin)


class WBSizeAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name', )

admin.site.register(WBSize, WBSizeAdmin)


class ItemOfWBSizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'wbsize', 'size_min', 'size_max',  ]
    list_filter = ('wbsize', )

    search_fields = ('name', )

admin.site.register(ItemOfWBSize, ItemOfWBSizeAdmin)


class ObjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', ]
    list_filter = ('parent', )

    search_fields = ('name', )
    
admin.site.register(Object, ObjectAdmin)