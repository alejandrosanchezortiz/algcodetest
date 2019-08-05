from django.contrib import admin

# Register your models here.

from .models import Users

class UsersAdmin(admin.ModelAdmin):
    fields = ['name','connects']
    list_display = ['user_id','name']
    ordering = ['user_id']

admin.site.register(Users,UsersAdmin)