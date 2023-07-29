from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):
    fields=('chat', 'text', 'created_at', 'author', 'receiver')
    list_display=('text', 'created_at', 'author', 'receiver')
    search_fields=('text',)


class ChatAdmin(admin.ModelAdmin):
    fields=('created_at',)
    list_display=('created_at',)
    search_fields=('created_at',)

# Register your models here.

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)