from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyUser

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'adress',
    )

admin.site.register(MyUser, UserAdmin)