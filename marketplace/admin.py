from django.contrib import admin
from .models import DigitalArtwork, Category

admin.site.register(DigitalArtwork)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    search_fields = ['name']