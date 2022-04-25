from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyUser


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'adress',
    )
    search_fields = ('username', 'first_name')
    list_filter = ('username', 'is_seller')

admin.site.register(MyUser, UserAdmin)