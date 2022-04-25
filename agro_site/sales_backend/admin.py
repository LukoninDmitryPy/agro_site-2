from django.contrib import admin

from .models import Product, ProductGroup, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'product_group',
        'price',
        'description',
        'count'
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug'
    )
    empty_value_display = '-пусто-'

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug'
    )
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Comment)
