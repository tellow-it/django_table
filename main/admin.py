from django.contrib import admin
from .models import Table


# Register your models here.

class TableAdmin(admin.ModelAdmin):
    Model = Table
    list_display = ['name', 'numbers', 'distance', 'data']


admin.site.register(Table, TableAdmin)
