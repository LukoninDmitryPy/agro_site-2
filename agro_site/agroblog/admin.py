from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'author')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Post , PostAdmin)
# изменения
admin.site.register(Comment, CommentAdmin)