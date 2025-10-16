from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "sender", "recipient", "created", "read")
    search_fields = ("subject", "body", "sender__username", "recipient__username")
