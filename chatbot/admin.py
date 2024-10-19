from django.contrib import admin
from .models import Chat

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'timestamp')  # Adjust fields as necessary
    search_fields = ('user__username', 'role', 'content')  # Allows searching by user, role, or content
