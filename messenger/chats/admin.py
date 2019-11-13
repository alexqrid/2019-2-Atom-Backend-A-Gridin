from django.contrib import admin
from .models import Chat


class ChatsAdmin(admin.ModelAdmin):
    list_display = ('title','is_group')
    list_filter = ['is_group']


admin.site.register(Chat, ChatsAdmin)