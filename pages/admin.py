from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created")
    search_fields = ("title", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
