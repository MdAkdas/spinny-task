from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Box

class BoxAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at',)

admin.site.register(Box, BoxAdmin)